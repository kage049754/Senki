#!/usr/bin/env python3
"""Produce a conservative source-level character package inventory.

This is an audit aid, not a completeness or gameplay verifier. Presence of files
never proves they are referenced, compatible, licensed, or functional.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

GAME = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path("character-package-audit.md")
BASIC = GAME / "lua/class/basic.lua"
if not BASIC.is_file():
    raise SystemExit(f"Missing expected roster source: {BASIC}")

source = BASIC.read_text(encoding="utf-8", errors="replace")
SKILL_LAYER = GAME / "lua/ui/SkillLayer.lua"
skill_source = SKILL_LAYER.read_text(encoding="utf-8", errors="replace") if SKILL_LAYER.is_file() else ""
alias_match = re.search(r"local skillUiAlias\s*=\s*\{([\s\S]*?)\n\}", skill_source)
skill_ui_aliases = dict(
    re.findall(r"([A-Za-z0-9_]+)\s*=\s*'([^']+)'", alias_match.group(1))
) if alias_match else {}
match = re.search(r"ns\.CharactersLayout\s*=\s*\{([\s\S]*?)\n\}", source)
if not match:
    raise SystemExit("Could not locate ns.CharactersLayout in basic.lua")
body = re.sub(r"--\[\[[\s\S]*?\]\]", "", match.group(1))
body = re.sub(r"--[^\n]*", "", body)
names = []
for item in re.finditer(r"'([^']*)'|\"([^\"]*)\"|(?<![\w])_None(?![\w])", body):
    name = item.group(1) or item.group(2) or ""
    if name and name.lower() != "none" and name not in names:
        names.append(name)

# Enum entries outside the visible selection list may be forms, clones, summons,
# or implementation-only entities. Report them for manual classification; never
# count them as playable merely because an enum exists.
HERO_ENUM = GAME / "Classes/Enums/HeroEnum.h"
enum_source = HERO_ENUM.read_text(encoding="utf-8", errors="replace") if HERO_ENUM.is_file() else ""
enum_names = list(dict.fromkeys(re.findall(r"mk_const\(([^)]+)\)", enum_source)))
unlisted_enum_names = [name for name in enum_names if name not in names]

all_files = [p for p in GAME.rglob("*") if p.is_file()]
relative = [(p, p.relative_to(GAME).as_posix()) for p in all_files]
text_files = []
for path, rel in relative:
    if path.suffix.lower() in {".lua", ".cpp", ".h", ".hpp", ".xml", ".plist", ".json", ".ini"}:
        try:
            text_files.append((rel, path.read_text(encoding="utf-8", errors="replace")))
        except OSError:
            pass

def under_dir(rel: str, parent: str, name: str) -> bool:
    parts = rel.lower().split("/")
    try:
        idx = parts.index(parent.lower())
    except ValueError:
        return False
    return idx + 1 < len(parts) and parts[idx + 1] == name.lower()

def fmt(value):
    return str(value).replace("|", "\\|").replace("\n", " ")

rows = []
detail_rows = []
for name in names:
    low = name.lower()
    header = any(rel.lower() == f"classes/core/shinobi/{low}.hpp" for _, rel in relative)
    # This candidate stores fighter sprites/config under Resources/Unit/<name>/.
    unit = []
    for _, rel in relative:
        parts = rel.lower().split("/")
        if "unit" in parts and low in parts[parts.index("unit") + 1:]:
            unit.append(rel)
    audio = [rel for _, rel in relative if under_dir(rel, "Audio", name)]
    named_selection = [rel for _, rel in relative if Path(rel).name.lower() in {
        f"{low}_select.png", f"{low}_half.png", f"{low}_font.png"
    }]
    enum_refs = [rel for rel, content in text_files if re.search(rf"HeroEnum::{re.escape(name)}\b", content, re.IGNORECASE)]
    ai_refs = [rel for rel, content in text_files if "setAIHandler" in content and re.search(rf"HeroEnum::{re.escape(name)}\b", content, re.IGNORECASE)]
    # SkillLayer.lua may alias a form to its base character for skill icons/labels.
    # Count the exact art name that the runtime lookup actually uses.
    skill_name = skill_ui_aliases.get(name, name)
    skill_low = skill_name.lower()
    resource_names = {Path(rel).name.lower() for _, rel in relative}
    plist_text = "\\n".join(content.lower() for rel, content in text_files if rel.lower().endswith(".plist"))
    # Battle HUD kill/death reports load portraits from the Report atlas as <Name>_rp.png.
    # Track both attacker and victim portrait frames independently from selection art.
    report_plist = GAME / "Resources/Report.plist"
    report_text = report_plist.read_text(encoding="utf-8", errors="replace").lower() if report_plist.is_file() else ""
    report_frames_found = sum(1 for suffix in ("_rp.png", "_rpf.png") if f"{low}{suffix}" in report_text)
    skill_icons_found = sum(1 for i in range(1, 6) if f"{skill_low}_skill{i}.png" in resource_names or f"{skill_low}_skill{i}.png" in plist_text)
    skill_labels_found = sum(1 for i in range(1, 6) if f"{skill_low}_label{i}.png" in resource_names or f"{skill_low}_label{i}.png" in plist_text)
    # Atlas-packed selection art may not exist as standalone PNG files.
    atlas = GAME / "Resources/Select.plist"
    atlas_text = atlas.read_text(encoding="utf-8", errors="replace") if atlas.is_file() else ""
    required_frames = [f"{name}_select.png", f"{name}_half.png", f"{name}_font.png"]
    frames_found = [frame for frame in required_frames if frame.lower() in atlas_text.lower()]
    if len(frames_found) == len(required_frames) or len(named_selection) == 3:
        selection = "ALL_3_FRAMES_FOUND"
    elif frames_found or named_selection:
        selection = "PARTIAL_FRAMES_FOUND"
    else:
        selection = "NOT_FOUND_MANUAL_CHECK"
    rows.append((name, "YES" if header else "NO/MONOLITHIC", "ENUM_REFERENCE_FOUND" if enum_refs else "NO_ENUM_REFERENCE_FOUND", f"{skill_icons_found}/5", f"{skill_labels_found}/5", len(unit), len(audio), selection, f"{report_frames_found}/2", "AI_REGISTRATION_REFERENCE_FOUND" if ai_refs else "MANUAL_AI_AUDIT_REQUIRED"))
    # Exact per-character package checks: animation/config XML, sprite atlas,
    # referenced texture, and audio events declared by the XML.
    unit_dir = GAME / "Resources/Unit/Ninja" / name
    unit_xml = unit_dir / f"{name}.xml"
    unit_plist = unit_dir / f"{name}.plist"
    xml_text = unit_xml.read_text(encoding="utf-8", errors="replace") if unit_xml.is_file() else ""
    plist_exact = unit_plist.is_file()
    texture_name = None
    if plist_exact:
        plist_exact_text = unit_plist.read_text(encoding="utf-8", errors="replace")
        texture_match = re.search(r"<key>textureFileName</key>\s*<string>([^<]+)</string>", plist_exact_text)
        if texture_match:
            texture_name = texture_match.group(1)
    texture_ok = bool(texture_name and (unit_dir / texture_name).is_file())
    animation_status = "XML_FOUND" if unit_xml.is_file() else "XML_MISSING"
    atlas_status = "PLIST+TEXTURE_FOUND" if plist_exact and texture_ok else ("PLIST_FOUND_TEXTURE_MISSING" if plist_exact else "PLIST_MISSING")
    audio_events = len(re.findall(r"""<e\s+type=['"]setSound['"]>\s*Audio/[^<]+""", xml_text, re.IGNORECASE))
    detail_rows.append((name, animation_status, atlas_status, f"{audio_events} audio event refs", f"{len(audio)} exact-name audio files", "YES" if enum_refs else "NO", "YES" if ai_refs else "MANUAL"))

portrait_complete = sum(1 for row in rows if row[8] == "2/2")
missing_portrait_names = [row[0] for row in rows if row[8] != "2/2"]
label_complete = sum(1 for row in rows if row[4] == "5/5")
missing_label_names = [(row[0], row[4]) for row in rows if row[4] != "5/5"]

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as f:
    f.write("# Automated Character Package Inventory\n\n")
    f.write(f"- Candidate root: `{GAME}`\n")
    f.write(f"- Roster source: `lua/class/basic.lua`\n")
    target_gap = max(0, 70 - len(names))
    f.write(f"- Unique selectable names found: **{len(names)}**\n")
    f.write(f"- Distinct selectable-entry target: **{len(names)}/70 declared ({target_gap} more entries to reach 70; gameplay completeness is not implied).**\n")
    f.write("- Gameplay-verified playable count: **not measured by this static audit.**\n")
    f.write(f"- HeroEnum entries absent from the visible selection list: **{len(unlisted_enum_names)} requiring manual classification** (not counted as playable).\n")
    if unlisted_enum_names:
        f.write("- Non-roster enum leads: " + ", ".join(chr(96) + name + chr(96) for name in unlisted_enum_names) + ".\n")
    else:
        f.write("- Non-roster enum leads: none found.\n")
    f.write(f"- Kill-feed portrait atlas coverage: **{portrait_complete}/{len(rows)} roster entries have both frames.**\n")
    f.write(f"- Skill-description label frame coverage: **{label_complete}/{len(rows)} roster entries have all five expected frames after applying SkillLayer UI aliases.**\n")
    if skill_ui_aliases:
        f.write("- Skill UI art aliases used by the audit: " + ", ".join(f"`{name}` → `{base}`" for name, base in sorted(skill_ui_aliases.items())) + ".\n")
    if missing_label_names:
        f.write("- Skill-description label exceptions requiring manual review: " + ", ".join(f"`{name}` ({count})" for name, count in missing_label_names) + ".\n")
    else:
        f.write("- Skill-description label exceptions requiring manual review: none detected by filename/frame-name audit.\n")
    f.write("- Generated by `scripts/audit_character_packages.py`.\n")
    f.write("- **Warning:** this is a filename/source-reference inventory only. It does not prove a character is complete, licensed, selectable at runtime, or playable by AI. Manual skill-view, animation, audio-trigger, combat, and device tests remain mandatory.\n\n")
    f.write("| Character | Separate C++ header | Native enum reference | Skill icon frames | Skill description frames | Unit/resource file matches | Exact-name audio files | Selection art check | Kill-feed portrait frames | AI registration clue |\n")
    f.write("|---|---|---|---|---|---:|---:|---|---|---|\n")
    for row in rows:
        f.write("| " + " | ".join(fmt(x) for x in row) + " |\n")
    f.write("\n## Detailed animation, atlas, audio, and AI checks\n\n")
    f.write("| Character | Animation/config XML | Sprite atlas + texture | Audio event references in XML | Exact-name audio files | Enum reference | AI registration clue |\n")
    f.write("|---|---|---|---:|---:|---|---|\n")
    for row in detail_rows:
        f.write("| " + " | ".join(fmt(x) for x in row) + " |\n")
    f.write("\n## Interpretation rules\n\n")
    f.write("- A `NO/MONOLITHIC` header result means the code may be in a shared C++ file; it is not proof the character is absent. Unit/resource counts are broad filename matches and do not prove the correct frames load.\n")
    f.write("- Missing skill icon or description-label frame names require manual investigation. A missing label can make the skill-view UI request a nonexistent frame; this audit does not test runtime handling or invent replacement descriptions. Some forms may share assets/classes and some skill UI may be assembled indirectly.\n")
    f.write("- Audio counts are path matches only and do not distinguish voice from effects or prove event triggers.\n")
    f.write("- A selection art result is based on finding expected frame names in `Select.plist` or standalone files; runtime selection still needs testing.\n- Kill-feed portrait count checks `<Name>_rp.png` and `<Name>_rpf.png` in `Resources/Report.plist`; it does not prove killer/victim attribution or on-screen rendering works at runtime.\n")
    f.write("- Do not promote any entry to implemented or verified based on this report alone. Record voice lines, SFX triggers, skills, resource paths, AI behavior, provenance, and rights separately.\n")
print(f"Wrote {OUT}; audited {len(names)} unique selectable names; kill-feed portrait atlas coverage {portrait_complete}/{len(rows)}.")
if missing_portrait_names:
    raise SystemExit("Missing kill-feed portrait frames for: " + ", ".join(missing_portrait_names))
