#!/usr/bin/env python3
"""Add the source-visible Saso/Sasori fighter as an additive playable slot.

Uses the mod repository's tracked Saso sprite atlas and the V2 Kankuro animation/
combat template as a compatibility baseline. Missing frame names are mapped to
real atlas frames; the base Kankuro entry is never replaced.
"""
from pathlib import Path
import plistlib, re, shutil, sys, xml.etree.ElementTree as ET

if len(sys.argv) != 3:
    raise SystemExit("usage: apply_sasori.py PATH_TO_GAME PATH_TO_NarutoSenki1.17Mod")
game, mod = map(Path, sys.argv[1:])
assets = mod / "assets"
source = assets / "Element/Saso"
required = [source / "Saso.png", source / "Saso.plist", source / "Saso.xml"]
for p in required:
    if not p.is_file() or p.stat().st_size == 0:
        raise SystemExit(f"Required tracked Saso source asset missing: {p}")

resources = game / "Resources"
unit = resources / "Unit/Ninja/Sasori"
unit.mkdir(parents=True, exist_ok=True)
shutil.copy2(source / "Saso.png", unit / "Sasori.png")
data = plistlib.loads((source / "Saso.plist").read_bytes())
frames = {}
for name, meta in data.get("frames", {}).items():
    clean = name[:-4] if name.endswith(".png") else name
    frames[re.sub(r"^Saso(?=[_./-]|$)", "Sasori", clean)] = meta
if not frames:
    raise SystemExit("Saso atlas has no frames")
data["frames"] = frames
data["metadata"] = data.get("metadata", {})
data["metadata"]["textureFileName"] = "Sasori.png"
data["metadata"]["realTextureFileName"] = "Sasori.png"
(unit / "Sasori.plist").write_bytes(plistlib.dumps(data, fmt=plistlib.FMT_XML, sort_keys=False))

# Keep the V2 animation schema and retarget it to the Sasori atlas.
base = resources / "Unit/Ninja/Kankuro"
source_xml = source / "Saso.xml"
base_skill_plist = base / "Kankuro_Skill.plist"
base_skill_png = next((base / n for n in ("Kankuro_Skill.png", "Kankuro_Skill.pvr.ccz", "Kankuro_Skill.ccz") if (base / n).is_file()), None)
if not source_xml.is_file() or not base_skill_plist.is_file() or base_skill_png is None:
    raise SystemExit("Sasori source animations or V2-compatible skill UI template are incomplete")
# Prefer Sasori's own action/frame data rather than reusing Kankuro's moves.
(unit / "Sasori.xml").write_text(source_xml.read_text(encoding="utf-8").replace("Saso", "Sasori"), encoding="utf-8")
shutil.copy2(base_skill_plist, unit / "Sasori_Skill.plist")
skill_data = plistlib.loads((unit / "Sasori_Skill.plist").read_bytes())
skill_data["frames"] = {
    re.sub(r"^Kankuro(?=[_./-]|$)", "Sasori", (k[:-4] if k.endswith(".png") else k)): v
    for k, v in skill_data.get("frames", {}).items()
}
skill_data["metadata"] = skill_data.get("metadata", {})
skill_texture_ext = ".pvr.ccz" if base_skill_png.name.lower().endswith(".pvr.ccz") else base_skill_png.suffix
skill_texture_name = "Sasori_Skill" + skill_texture_ext
skill_data["metadata"]["textureFileName"] = skill_texture_name
skill_data["metadata"]["realTextureFileName"] = skill_texture_name
(unit / "Sasori_Skill.plist").write_bytes(plistlib.dumps(skill_data, fmt=plistlib.FMT_XML, sort_keys=False))
shutil.copy2(base_skill_png, unit / skill_texture_name)

# Fill frame-name gaps only with actual rectangles present in the imported atlas.
root = ET.parse(unit / "Sasori.xml").getroot()
refs = {n.text.strip() for n in root.iter("f") if n.text and n.text.strip()}
main = plistlib.loads((unit / "Sasori.plist").read_bytes())
known = set(main.get("frames", {})) | set(skill_data.get("frames", {}))
main_frames = main["frames"]
def frame_number(name):
    m = re.search(r"_(\d+)$", name)
    return int(m.group(1)) if m else -1
for missing in sorted(refs - known):
    prefix = missing.rsplit("_", 1)[0] + "_"
    candidates = [n for n in main_frames if n.startswith(prefix)]
    if not candidates:
        candidates = [n for n in main_frames if "_NAttack_" in n]
    if not candidates:
        candidates = list(main_frames)
    if not candidates:
        raise SystemExit(f"No atlas frame can satisfy animation reference {missing}")
    target = max(candidates, key=lambda n: (frame_number(n) <= frame_number(missing), frame_number(n), n))
    main_frames[missing] = main_frames[target]
main["frames"] = main_frames
(unit / "Sasori.plist").write_bytes(plistlib.dumps(main, fmt=plistlib.FMT_XML, sort_keys=False))

# Copy the compatible native audio paths so every referenced clip resolves.
audio = resources / "Audio/Sasori"
audio.mkdir(parents=True, exist_ok=True)
base_audio = resources / "Audio/Kankuro"
if not base_audio.is_dir():
    raise SystemExit("V2 Kankuro audio fallback is missing")
for p in base_audio.iterdir():
    if p.is_file():
        shutil.copy2(p, audio / re.sub("Kankuro", "Sasori", p.name, flags=re.I))
xml_text = (unit / "Sasori.xml").read_text(encoding="utf-8")
xml_text = re.sub(r"Audio/Kankuro/", "Audio/Sasori/", xml_text, flags=re.I)
xml_text = re.sub(r"Kankuro", "Sasori", xml_text, flags=re.I)
(unit / "Sasori.xml").write_text(xml_text, encoding="utf-8")

# Clone the native controller and register a new identity without replacing Kankuro.
header_src = game / "Classes/Core/Shinobi/Kankuro.hpp"
header_dst = game / "Classes/Core/Shinobi/Sasori.hpp"
header = header_src.read_text(encoding="utf-8")
header = re.sub(r"\bKankuro\b", "Sasori", header)
if "class Sasori" not in header:
    raise SystemExit("Could not derive Sasori native controller from Kankuro")
header = "// Compatibility baseline: Kankuro controller; Sasori-specific tuning remains a follow-up.\n// HeroEnum::Sasori\n" + header
header_dst.write_text(header, encoding="utf-8")
enum_path = game / "Classes/Enums/HeroEnum.h"
enum = enum_path.read_text(encoding="utf-8")
if "mk_const(Sasori);" not in enum:
    anchor = "mk_const(Kankuro);"
    if enum.count(anchor) != 1: raise SystemExit("Could not find Kankuro enum anchor")
    enum_path.write_text(enum.replace(anchor, anchor + "\n\tmk_const(Sasori);", 1), encoding="utf-8")
provider_path = game / "Classes/Core/Provider.hpp"
provider = provider_path.read_text(encoding="utf-8")
if '#include "Shinobi/Sasori.hpp"' not in provider:
    anchor = '#include "Shinobi/Kankuro.hpp"'
    if provider.count(anchor) != 1: raise SystemExit("Could not find Kankuro Provider include")
    provider = provider.replace(anchor, anchor + '\n#include "Shinobi/Sasori.hpp"', 1)
if 'is("Sasori")' not in provider:
    m = re.search(r'is\("Kankuro"\)\s*ptr\s*=\s*new Kankuro\(\);', provider)
    if not m: raise SystemExit("Could not find Kankuro Provider dispatch")
    provider = provider[:m.end()] + '\n\t\tis("Sasori")\t\tptr = new Sasori();' + provider[m.end():]
provider_path.write_text(provider, encoding="utf-8")

basic_path = game / "lua/class/basic.lua"
basic = basic_path.read_text(encoding="utf-8")
if "'Sasori'" not in basic:
    pos = basic.find("ns.CharactersLayout = {")
    if pos < 0: raise SystemExit("Could not locate character roster")
    prefix, roster = basic[:pos], basic[pos:]
    roster, count = re.subn(r"(?<![\w])_None(?![\w])", "'Sasori'", roster, count=1)
    if count != 1: raise SystemExit("No empty roster slot for Sasori")
    basic_path.write_text(prefix + roster, encoding="utf-8")

select_path = game / "lua/ui/SelectLayer.lua"
select = select_path.read_text(encoding="utf-8")
def add_table_entry(source, table_name, entry, identity):
    if identity in source:
        return source
    start = source.find(table_name)
    if start < 0: raise SystemExit(f"Missing UI table: {table_name}")
    end = source.find("\n}", start)
    if end < 0: raise SystemExit(f"Could not locate end of {table_name}")
    body = source[start:end].rstrip()
    if body.endswith(","): pass
    else: body += ","
    return source[:start] + body + "\n    " + entry + source[end:]
select = add_table_entry(select, "local selectionAssetAlias = {", "Sasori = 'Kankuro'", "Sasori = 'Kankuro'")
select = add_table_entry(select, "local selectionDisplayName = {", "Sasori = 'Sasori'", "Sasori = 'Sasori'")
old = "        local select_btn = SelectButton:create(charName .. '_select.png')"
new = "        local selectAssetName = selectionAssetAlias[charName] or charName\n        local select_btn = SelectButton:create(selectAssetName .. '_select.png')"
if old in select: select = select.replace(old, new, 1)
elif new not in select: raise SystemExit("Could not route Sasori selection button to Kankuro base art")
old = "        self._heroHalfImage = display.newSprite(charName .. '_half.png', 10, 10)"
new = "        local selectAssetName = selectionAssetAlias[btn._charName] or btn._charName\n        self._heroHalfImage = display.newSprite('#' .. selectAssetName .. '_half.png', 10, 10)"
if old in select: select = select.replace(old, new, 1)
elif new not in select: raise SystemExit("Could not route Sasori portrait to compatible UI art")
old = "        self._heroName = display.newSprite(charName .. '_font.png', 100, 20)\n        self._heroName:setAnchorPoint(CCPoint(0.5, 0))\n        self:addChild(self._heroName, 5)"
new = """        local displayName = selectionDisplayName[btn._charName]
        if displayName then
            self._heroName = ui.newTTFLabel({text = displayName, font = ui.DEFAULT_TTF_FONT, size = 16, color = ccc3(255, 255, 255)})
            self._heroName:setPosition(100, 20)
        else
            self._heroName = display.newSprite(charName .. '_font.png', 100, 20)
        end
        self._heroName:setAnchorPoint(CCPoint(0.5, 0))
        self:addChild(self._heroName, 5)"""
if old in select: select = select.replace(old, new, 1)
elif "selectionDisplayName[btn._charName]" not in select: raise SystemExit("Could not add display name support")
select_path.write_text(select, encoding="utf-8")

skill_path = game / "lua/ui/SkillLayer.lua"
skill = skill_path.read_text(encoding="utf-8")
if "Sasori = 'Kankuro'" not in skill:
    marker = "local skillUiAlias = {"
    pos = skill.find(marker)
    if pos < 0: raise SystemExit("Missing skillUiAlias")
    end = skill.find("\n}", pos)
    if end < 0: raise SystemExit("Missing end of skillUiAlias")
    prefix = skill[:end].rstrip()
    if not prefix.endswith(","): prefix += ","
    skill = prefix + "\n    Sasori = 'Kankuro'," + skill[end:]
skill_path.write_text(skill, encoding="utf-8")

# Selection/kill-feed atlas aliases use existing UI atlas rectangles, never replace originals.
for plist_path in resources.glob("*.plist"):
    try: ui_data = plistlib.loads(plist_path.read_bytes())
    except Exception: continue
    ui_frames = ui_data.get("frames")
    if not isinstance(ui_frames, dict): continue
    aliases = {}
    for frame, meta in list(ui_frames.items()):
        if frame.startswith("Kankuro_"):
            aliases.setdefault("Sasori_" + frame[len("Kankuro_"):], meta)
    if aliases:
        ui_frames.update({k:v for k,v in aliases.items() if k not in ui_frames})
        plist_path.write_bytes(plistlib.dumps(ui_data, fmt=plistlib.FMT_XML, sort_keys=False))

# Verify every animation frame and referenced sound exists.
main = plistlib.loads((unit / "Sasori.plist").read_bytes())
skills = plistlib.loads((unit / "Sasori_Skill.plist").read_bytes())
missing = refs - set(main.get("frames", {})) - set(skills.get("frames", {}))
if missing: raise SystemExit("Unresolved Sasori animation frames: " + ", ".join(sorted(missing)[:10]))
for clip in re.findall(r"Audio/Sasori/([^<\" ]+?\.ogg)", xml_text):
    if not (audio / clip).is_file(): raise SystemExit(f"Missing Sasori audio: {clip}")
for p in [header_dst, unit / "Sasori.xml", unit / "Sasori.plist", unit / "Sasori.png", unit / "Sasori_Skill.plist", unit / skill_texture_name]:
    if not p.is_file() or p.stat().st_size == 0: raise SystemExit(f"Missing/empty Sasori package file: {p}")
ET.parse(unit / "Sasori.xml")
print("Added Sasori as a new selectable fighter using tracked Saso atlas, native dispatch, selection/profile aliases, and compatible Kankuro baseline behavior.")
