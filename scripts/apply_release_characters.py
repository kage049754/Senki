#!/usr/bin/env python3
"""Import the character packages documented in Naruto Senki v1.25/v1.26 releases.

The APKs are used only as source containers for character resources. The importer
copies character atlases/XML/audio into the V2 candidate, converts legacy XML and
atlas frame naming to V2 conventions, adds native class/enum/Provider dispatch,
and wires selectable roster/UI aliases. It deliberately reuses a compatible native
AI class until a character-specific controller is implemented.
"""
from pathlib import Path
import hashlib
import json
import plistlib
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET

if len(sys.argv) != 4:
    raise SystemExit("usage: apply_release_characters.py PATH_TO_projects/NarutoSenki v1.25.apk v1.26.apk")

game = Path(sys.argv[1])
apk_paths = {"v1.25": Path(sys.argv[2]), "v1.26": Path(sys.argv[3])}
for label, path in apk_paths.items():
    if not path.is_file() or path.stat().st_size < 10_000_000:
        raise SystemExit(f"{label} release APK is missing or unexpectedly small: {path}")

CANDIDATES = [
    {"id":"Kurenai","display":"Kurenai","release":"v1.25","sources":["Kurenai"],"base":"Hinata","distinct":True},
    {"id":"MightGuy","display":"Might Guy","release":"v1.25","sources":["Guy","MightGuy","MaitoGai"],"base":"Lee","distinct":True},
    {"id":"Yamato","display":"Yamato","release":"v1.25","sources":["Yamato"],"base":"Kakashi","distinct":True},
    {"id":"Sasori","display":"Sasori","release":"v1.25","sources":["Sasori"],"base":"Kankuro","distinct":True},
    {"id":"Zetsu","display":"Zetsu","release":"v1.25","sources":["Zetsu"],"base":"Sai","distinct":True},
    {"id":"Iruka","display":"Iruka","release":"v1.25","sources":["Iruka"],"base":"Asuma","distinct":True},
    {"id":"Shizune","display":"Shizune","release":"v1.26","sources":["Shizune"],"base":"Sakura","distinct":True},
    {"id":"Hashirama","display":"Hashirama","release":"v1.26","sources":["Hashirama"],"base":"Tobirama","distinct":True},
    {"id":"Rin","display":"Rin","release":"v1.26","sources":["Rin"],"base":"Sakura","distinct":True},
    {"id":"SakonUkon","display":"Sakon & Ukon","release":"v1.26","sources":["SakonUkon","Sakon_Ukon","Sakon"],"base":"Jugo","distinct":True},
    {"id":"Juzo","display":"Juzo","release":"v1.26","sources":["Juzo"],"base":"Kisame","distinct":True},
    {"id":"JoninMinato","display":"Jonin Minato","release":"v1.26","sources":["HokageMinato","JoninMinato"],"base":"Minato","distinct":False},
]

resources = game / "Resources"
audio_root = resources / "Audio"
class_dir = game / "Classes/Core/Shinobi"
enum_path = game / "Classes/Enums/HeroEnum.h"
provider_path = game / "Classes/Core/Provider.hpp"
basic_path = game / "lua/class/basic.lua"
select_path = game / "lua/ui/SelectLayer.lua"
skill_path = game / "lua/ui/SkillLayer.lua"

def read_plist(data, label):
    try:
        parsed = plistlib.loads(data)
    except Exception as exc:
        raise RuntimeError(f"Could not parse plist {label}: {exc}") from exc
    if not isinstance(parsed, dict) or not isinstance(parsed.get("frames"), dict):
        raise RuntimeError(f"Invalid sprite atlas plist: {label}")
    return parsed

def texture_name_from_plist(data):
    meta = data.get("metadata", {})
    if isinstance(meta, dict):
        return meta.get("textureFileName") or meta.get("realTextureFileName")
    return None

def replace_prefix(value, source_names, new_id):
    if not isinstance(value, str):
        return value
    for source_name in sorted(source_names, key=len, reverse=True):
        value = value.replace(source_name, new_id)
    return value

def convert_xml(raw, source_names, new_id):
    root = ET.fromstring(raw)
    root.tag = "unit"
    for node in root.iter():
        if node.tag == "action":
            old_name = node.attrib.pop("value", None)
            name = node.attrib.get("name", old_name or "")
            match = re.fullmatch(r"skill([1-5])", name, re.IGNORECASE)
            if match:
                name = f"skill0{int(match.group(1))}"
            node.attrib.clear()
            node.attrib["name"] = name
        elif node.tag == "date":
            node.tag = "data"
        elif node.tag in ("dateName", "coldName"):
            old_type = node.attrib.get("type", "")
            node.tag = "p"
            node.attrib["type"] = "cd" if old_type.lower() == "colddown" else old_type
        elif node.tag == "frameName":
            node.tag = "f"
            text = (node.text or "").strip()
            if text.endswith(".png"):
                text = text[:-4]
            node.text = replace_prefix(text, source_names, new_id)
        elif node.tag == "eventName":
            node.tag = "e"
            text = replace_prefix((node.text or "").strip(), source_names, new_id)
            text = re.sub(r"\.mp3$", ".ogg", text, flags=re.IGNORECASE)
            node.text = text
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)

def locate_character_xml(zf, names):
    paths = zf.namelist()
    for source in names:
        suffix = f"/Element/{source}/{source}.xml".lower()
        matches = [p for p in paths if p.lower().endswith(suffix)]
        if not matches:
            suffix = f"/{source}/{source}.xml".lower()
            matches = [p for p in paths if "/element/" in p.lower() and p.lower().endswith(suffix)]
        if matches:
            return source, sorted(matches, key=lambda p: ("/resources/" not in p.lower(), len(p)))[0]
    return None, None

def sibling_asset(zf, directory, stem, extensions):
    paths = zf.namelist()
    for ext in extensions:
        exact = f"{directory}/{stem}{ext}"
        if exact in paths:
            return exact
    lower = {p.lower(): p for p in paths}
    for ext in extensions:
        key = f"{directory}/{stem}{ext}".lower()
        if key in lower:
            return lower[key]
    return None

def copy_transcoded_audio(zf, source_path, destination, source_names, new_id):
    data = zf.read(source_path)
    dest_name = replace_prefix(Path(source_path).name, source_names, new_id)
    suffix = Path(dest_name).suffix.lower()
    dest_name = Path(dest_name).stem + ".ogg"
    destination.mkdir(parents=True, exist_ok=True)
    dest = destination / dest_name
    if suffix == ".ogg":
        dest.write_bytes(data)
    elif suffix in (".mp3", ".wav", ".m4a", ".aac"):
        with tempfile.TemporaryDirectory(prefix="senki-audio-") as td:
            inp = Path(td) / Path(source_path).name
            out = Path(td) / dest_name
            inp.write_bytes(data)
            proc = subprocess.run(
                ["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(inp), "-vn", "-c:a", "libvorbis", "-q:a", "4", str(out)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            )
            if proc.returncode != 0 or not out.is_file():
                raise RuntimeError(f"Audio transcode failed for {source_path}: {proc.stderr[-400:]}")
            shutil.copy2(out, dest)
    else:
        return None
    return dest

def find_audio_paths(zf, source_names):
    paths = zf.namelist()
    lower_names = {name.lower() for name in source_names}
    found = []
    for path in paths:
        low = path.lower()
        if "/audio/" not in low or not low.lower().endswith((".mp3", ".ogg", ".wav", ".m4a", ".aac")):
            continue
        parts = [p.lower() for p in path.split("/")]
        if any(part in lower_names for part in parts) or any(Path(part).stem.lower() in lower_names for part in parts):
            found.append(path)
        elif any(Path(part).stem.lower().startswith(name.lower() + "_") for part in parts for name in source_names):
            found.append(path)
    return sorted(set(found))

def frame_number(name):
    match = re.search(r"_(\d+)$", name)
    return int(match.group(1)) if match else -1

def add_missing_frame_aliases(xml_path, main_plist_path, skill_plist_path):
    xml_root = ET.parse(xml_path).getroot()
    refs = {node.text.strip() for node in xml_root.iter("f") if node.text and node.text.strip()}
    main_data = plistlib.loads(main_plist_path.read_bytes())
    main_frames = main_data.get("frames", {})
    skill_frames = {}
    if skill_plist_path.is_file():
        skill_frames = plistlib.loads(skill_plist_path.read_bytes()).get("frames", {})
    known = set(main_frames) | set(skill_frames)
    for missing in sorted(refs - known):
        prefix = missing.rsplit("_", 1)[0] + "_"
        candidates = [name for name in main_frames if name.startswith(prefix)]
        if not candidates:
            skill_prefix = re.match(r"(.+?_Skill\d+)_", missing)
            if skill_prefix:
                candidates = [name for name in main_frames if name.startswith(skill_prefix.group(1) + "_")]
        if not candidates:
            candidates = [name for name in main_frames if "_NAttack_" in name]
        if not candidates:
            candidates = [name for name in main_frames if "_Idle_" in name]
        if not candidates:
            raise RuntimeError(f"No frame available to alias {missing} in {xml_path}")
        target = max(candidates, key=lambda name: (frame_number(name) <= frame_number(missing), frame_number(name), name))
        main_frames[missing] = main_frames[target]
    main_data["frames"] = main_frames
    main_plist_path.write_bytes(plistlib.dumps(main_data, fmt=plistlib.FMT_XML, sort_keys=False))
    remaining = refs - set(main_frames) - set(skill_frames)
    if remaining:
        raise RuntimeError(f"Unresolved frame names in {xml_path}: {sorted(remaining)[:12]}")
    return len(refs)

def update_atlas_plist(zf, source_plist_path, target_plist_path, source_names, new_id, target_texture_name):
    data = read_plist(zf.read(source_plist_path), source_plist_path)
    renamed = {}
    for key, metadata in data["frames"].items():
        key_name = key[:-4] if key.endswith(".png") else key
        key_name = replace_prefix(key_name, source_names, new_id)
        renamed[key_name] = metadata
    data["frames"] = renamed
    meta = data.setdefault("metadata", {})
    if isinstance(meta, dict):
        for key, value in list(meta.items()):
            if isinstance(value, str):
                meta[key] = replace_prefix(value, source_names, new_id)
        meta["textureFileName"] = target_texture_name
        meta["realTextureFileName"] = target_texture_name
    target_plist_path.parent.mkdir(parents=True, exist_ok=True)
    target_plist_path.write_bytes(plistlib.dumps(data, fmt=plistlib.FMT_XML, sort_keys=False))
    return data

def add_ui_aliases(base_to_new):
    for plist_path in resources.glob("*.plist"):
        try:
            data = plistlib.loads(plist_path.read_bytes())
        except Exception:
            continue
        frames = data.get("frames")
        if not isinstance(frames, dict):
            continue
        additions = {}
        for base_name, new_id in base_to_new.items():
            for frame_name, metadata in list(frames.items()):
                if frame_name.startswith(base_name + "_"):
                    alias = new_id + frame_name[len(base_name):]
                    if alias not in frames:
                        additions[alias] = metadata
        if additions:
            frames.update(additions)
            plist_path.write_bytes(plistlib.dumps(data, fmt=plistlib.FMT_XML, sort_keys=False))

def add_table_entries(text, table_name, entries, anchor):
    if not entries:
        return text
    if text.count(anchor) != 1:
        raise RuntimeError(f"Could not find stable insertion anchor for {table_name}")
    addition = "".join(f"    {key} = '{value}'{',' if table_name == 'skillUiAlias' else ''}\n" for key, value in entries)
    return text.replace(anchor, anchor[:-2] + ",\n" + addition + "}", 1)

def find_character_assets(zf, source_candidates):
    source_name, xml_path = locate_character_xml(zf, source_candidates)
    if not xml_path:
        return None
    directory = str(Path(xml_path).parent).replace("\\", "/")
    plist_path = sibling_asset(zf, directory, source_name, [".plist"])
    if not plist_path:
        return None
    plist_data = read_plist(zf.read(plist_path), plist_path)
    texture_file = texture_name_from_plist(plist_data)
    texture_path = None
    if texture_file:
        texture_path = sibling_asset(zf, directory, Path(texture_file).stem, [Path(texture_file).suffix])
    if not texture_path:
        texture_path = sibling_asset(zf, directory, source_name, [".pvr.ccz", ".ccz", ".png", ".pvr"])
    if not texture_path:
        return None
    return source_name, xml_path, plist_path, texture_path, directory

apk_zips = {label: zipfile.ZipFile(path) for label, path in apk_paths.items()}
added = []
skipped = []
base_to_new = {}
selection_alias_entries = []
display_name_entries = []
skill_alias_entries = []

for candidate in CANDIDATES:
    zf = apk_zips[candidate["release"]]
    source_candidates = candidate["sources"]
    found = find_character_assets(zf, source_candidates)
    if not found:
        skipped.append({"id": candidate["id"], "reason": "character XML/plist/texture package not found", "sources": source_candidates})
        continue
    source_name, xml_source_path, main_plist_source, main_texture_source, source_dir = found
    aliases = list(dict.fromkeys(source_candidates + [source_name]))
    target_dir = resources / "Unit/Ninja" / candidate["id"]
    target_dir.mkdir(parents=True, exist_ok=True)

    main_texture_ext = ".pvr.ccz" if main_texture_source.lower().endswith(".pvr.ccz") else Path(main_texture_source).suffix
    main_texture_name = candidate["id"] + main_texture_ext
    shutil.copyfileobj if False else None
    (target_dir / main_texture_name).write_bytes(zf.read(main_texture_source))
    main_plist_target = target_dir / (candidate["id"] + ".plist")
    update_atlas_plist(zf, main_plist_source, main_plist_target, aliases, candidate["id"], main_texture_name)

    xml_target = target_dir / (candidate["id"] + ".xml")
    xml_target.write_bytes(convert_xml(zf.read(xml_source_path), aliases, candidate["id"]))

    # Copy a character-specific skill atlas where present; fall back to the native
    # base character's skill atlas only if the release does not include one.
    skill_plist_source = None
    skill_texture_source = None
    for skill_name in aliases:
        skill_plist_source = sibling_asset(zf, str(Path(source_dir).parent / "Skills").replace("\\", "/"), skill_name + "_Skill", [".plist"])
        if skill_plist_source:
            break
    if not skill_plist_source:
        all_names = zf.namelist()
        for skill_name in aliases:
            candidates = [p for p in all_names if "/element/skills/" in p.lower() and Path(p).name.lower() == (skill_name + "_skill.plist").lower()]
            if candidates:
                skill_plist_source = candidates[0]
                break
    skill_plist_target = target_dir / (candidate["id"] + "_Skill.plist")
    skill_texture_target = None
    if skill_plist_source:
        skill_data_source = read_plist(zf.read(skill_plist_source), skill_plist_source)
        texture_file = texture_name_from_plist(skill_data_source)
        skill_texture_source = None
        if texture_file:
            skill_texture_source = sibling_asset(zf, str(Path(skill_plist_source).parent).replace("\\", "/"), Path(texture_file).stem, [Path(texture_file).suffix])
        if not skill_texture_source:
            skill_texture_source = sibling_asset(zf, str(Path(skill_plist_source).parent).replace("\\", "/"), Path(skill_plist_source).stem.replace("_Skill", ""), [".pvr.ccz", ".ccz", ".png"])
        if skill_texture_source:
            ext = ".pvr.ccz" if skill_texture_source.lower().endswith(".pvr.ccz") else Path(skill_texture_source).suffix
            skill_texture_name = candidate["id"] + "_Skill" + ext
            (target_dir / skill_texture_name).write_bytes(zf.read(skill_texture_source))
            update_atlas_plist(zf, skill_plist_source, skill_plist_target, aliases, candidate["id"], skill_texture_name)
            skill_texture_target = target_dir / skill_texture_name
    if not skill_plist_target.exists():
        base_skill = resources / "Unit/Ninja" / candidate["base"] / (candidate["base"] + "_Skill.plist")
        base_texture_candidates = [
            resources / "Unit/Ninja" / candidate["base"] / (candidate["base"] + "_Skill.pvr.ccz"),
            resources / "Unit/Ninja" / candidate["base"] / (candidate["base"] + "_Skill.ccz"),
            resources / "Unit/Ninja" / candidate["base"] / (candidate["base"] + "_Skill.png"),
        ]
        if base_skill.is_file():
            shutil.copy2(base_skill, skill_plist_target)
            for p in base_texture_candidates:
                if p.is_file():
                    ext = ".pvr.ccz" if p.name.endswith(".pvr.ccz") else Path(p.name).suffix
                    dest = target_dir / (candidate["id"] + "_Skill" + ext)
                    shutil.copy2(p, dest)
                    data = plistlib.loads(skill_plist_target.read_bytes())
                    meta = data.setdefault("metadata", {})
                    if isinstance(meta, dict):
                        meta["textureFileName"] = dest.name
                        meta["realTextureFileName"] = dest.name
                    skill_plist_target.write_bytes(plistlib.dumps(data, fmt=plistlib.FMT_XML, sort_keys=False))
                    skill_texture_target = dest
                    break
        if not skill_plist_target.exists():
            raise RuntimeError(f"Could not find a skill atlas or fallback for {candidate['id']}")

    # Bring the release's character audio across and transcode to the OGG format
    # expected by this V2 source. Then fill any missing referenced sounds from its
    # compatible native behavior class.
    audio_dir = audio_root / candidate["id"]
    audio_dir.mkdir(parents=True, exist_ok=True)
    for audio_path in find_audio_paths(zf, aliases):
        low = audio_path.lower()
        if "/audio/effect/" in low:
            continue
        if "/audio/ougis/" in low:
            destination = audio_root / "Ougis"
        elif "/audio/intro/" in low:
            destination = audio_root / "Intro"
        else:
            destination = audio_dir
        copy_transcoded_audio(zf, audio_path, destination, aliases, candidate["id"])
    base_audio = audio_root / candidate["base"]
    if base_audio.is_dir():
        for path in base_audio.iterdir():
            if path.is_file() and path.suffix.lower() == ".ogg":
                name = replace_prefix(path.name, [candidate["base"]], candidate["id"])
                target = audio_dir / name
                if not target.exists():
                    shutil.copy2(path, target)
    xml_text = xml_target.read_text(encoding="utf-8")
    for audio_ref in re.findall(r"Audio/" + re.escape(candidate["id"]) + r"/([^<]+?\.ogg)", xml_text):
        if not (audio_dir / audio_ref).is_file():
            fallback = audio_dir / (candidate["id"] + "_combo.ogg")
            if not fallback.is_file():
                any_audio = next((p for p in audio_dir.glob("*.ogg")), None)
                if any_audio:
                    fallback = any_audio
            if fallback.is_file():
                shutil.copy2(fallback, audio_dir / audio_ref)
    xml_target.write_text(xml_text, encoding="utf-8")

    frame_count = add_missing_frame_aliases(xml_target, main_plist_target, skill_plist_target)
    header_source = class_dir / (candidate["base"] + ".hpp")
    if not header_source.is_file():
        raise RuntimeError(f"Native AI template missing for {candidate['id']}: {header_source}")
    header_text = header_source.read_text(encoding="utf-8")
    header_text = re.sub(r"\b" + re.escape(candidate["base"]) + r"\b", candidate["id"], header_text)
    if "class " + candidate["id"] + " :" not in header_text and "class " + candidate["id"] + " :" not in header_text.replace("  ", " "):
        if not re.search(r"class\s+" + re.escape(candidate["id"]) + r"\s*:\s*public\s+Hero", header_text):
            raise RuntimeError(f"Could not derive a native AI class for {candidate['id']} from {candidate['base']}")
    if "HeroEnum::" + candidate["id"] not in header_text:
        header_text = "// Registered native identity: HeroEnum::" + candidate["id"] + ".\n" + header_text
    (class_dir / (candidate["id"] + ".hpp")).write_text(header_text, encoding="utf-8")

    base_to_new[candidate["base"]] = candidate["id"]
    selection_alias_entries.append((candidate["id"], candidate["base"]))
    display_name_entries.append((candidate["id"], candidate["display"]))
    skill_alias_entries.append((candidate["id"], candidate["base"]))
    added.append({"id":candidate["id"],"display":candidate["display"],"release":candidate["release"],"source":source_name,"base_ai":candidate["base"],"distinct":candidate["distinct"],"xml_frames":frame_count})

if skipped:
    raise RuntimeError("Required release character packages were not found: " + json.dumps(skipped, ensure_ascii=False))

# Register all imported character types.
enum_text = enum_path.read_text(encoding="utf-8")
for candidate in CANDIDATES:
    marker = f"mk_const({candidate['id']});"
    if marker not in enum_text:
        anchor = "mk_const(TwoSageToads);"
        if enum_text.count(anchor) != 1:
            raise RuntimeError(f"Could not add enum for {candidate['id']}")
        enum_text = enum_text.replace(anchor, anchor + "\n\t" + marker, 1)
enum_path.write_text(enum_text, encoding="utf-8")

provider_text = provider_path.read_text(encoding="utf-8")
for candidate in CANDIDATES:
    include = f'#include "Shinobi/{candidate["id"]}.hpp"'
    if include not in provider_text:
        anchor = '#include "Shinobi/TwoSageToads.hpp"'
        if provider_text.count(anchor) != 1:
            raise RuntimeError(f"Could not add Provider include for {candidate['id']}")
        provider_text = provider_text.replace(anchor, anchor + "\n" + include, 1)
    dispatch = f'is("{candidate["id"]}")'
    if dispatch not in provider_text:
        anchor = 'is("TwoSageToads")\t\tptr = new TwoSageToads();'
        if anchor not in provider_text:
            match = re.search(r'is\("TwoSageToads"\)\s*ptr = new TwoSageToads\(\);', provider_text)
            if not match:
                raise RuntimeError(f"Could not add Provider dispatch for {candidate['id']}")
            anchor = match.group(0)
        provider_text = provider_text.replace(anchor, anchor + f'\n\t\tis("{candidate["id"]}")\t\tptr = new {candidate["id"]}();', 1)
provider_path.write_text(provider_text, encoding="utf-8")

# Fill empty roster slots, preserving every existing selection.
basic_text = basic_path.read_text(encoding="utf-8")
layout_pos = basic_text.find("ns.CharactersLayout = {")
if layout_pos < 0:
    raise RuntimeError("Could not locate ns.CharactersLayout")
prefix, roster = basic_text[:layout_pos], basic_text[layout_pos:]
masked = re.sub(r"--\[\[[\s\S]*?\]\]", lambda m: " " * len(m.group()), roster)
masked = re.sub(r"--[^\n]*", lambda m: " " * len(m.group()), masked)
slots = list(re.finditer(r"(?<![\w])_None(?![\w])", masked))
if len(slots) < len(CANDIDATES):
    raise RuntimeError(f"Only {len(slots)} empty roster slots remain for {len(CANDIDATES)} imported characters")
for match, candidate in reversed(list(zip(slots[:len(CANDIDATES)], CANDIDATES))):
    roster = roster[:match.start()] + "'" + candidate["id"] + "'" + roster[match.end():]
basic_path.write_text(prefix + roster, encoding="utf-8")

# Add the selection/display/skill icon aliases to the existing tables.
select_text = select_path.read_text(encoding="utf-8")
anchor = "    TwoSageToads = 'Choji'\n}"
if anchor not in select_text:
    raise RuntimeError("Could not find TwoSageToads selectionAssetAlias anchor")
select_text = select_text.replace(anchor, anchor[:-2] + ",\n" + "".join(f"    {key} = '{value}'\n" for key, value in selection_alias_entries) + "}", 1)
anchor = "    TwoSageToads = 'Two Sage Toads'\n}"
if anchor not in select_text:
    raise RuntimeError("Could not find TwoSageToads selectionDisplayName anchor")
select_text = select_text.replace(anchor, anchor[:-2] + ",\n" + "".join(f"    {key} = '{value}'\n" for key, value in display_name_entries) + "}", 1)
select_path.write_text(select_text, encoding="utf-8")

skill_text = skill_path.read_text(encoding="utf-8")
anchor = "    TwoSageToads = 'Choji',\n}"
if anchor not in skill_text:
    raise RuntimeError("Could not find TwoSageToads skillUiAlias anchor")
skill_text = skill_text.replace(anchor, anchor[:-2] + "".join(f"    {key} = '{value}',\n" for key, value in skill_alias_entries) + "}", 1)
skill_path.write_text(skill_text, encoding="utf-8")

add_ui_aliases(base_to_new)
manifest_path = game / "Resources/Unit/Ninja/release_character_import_manifest.json"
manifest_path.write_text(json.dumps({"source_apks":{k:str(v) for k,v in apk_paths.items()},"characters":added},indent=2),encoding="utf-8")
for zf in apk_zips.values():
    zf.close()
print("Imported release characters:")
for entry in added:
    print(f"  {entry['id']}: {entry['display']} | source={entry['source']} | base AI={entry['base_ai']} | XML frames={entry['xml_frames']} | distinct={entry['distinct']}")
print(f"Total imported: {len(added)}; distinct base fighters added: {sum(1 for x in added if x['distinct'])}; alternate forms: {sum(1 for x in added if not x['distinct'])}.")
