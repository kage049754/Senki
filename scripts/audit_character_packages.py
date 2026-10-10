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

# These entries are existing forms or modded variants of base characters, not
# additional distinct characters toward the 70+ distinct-character goal.
KNOWN_FORM_BASES = {
    "SageJiraiya": "Jiraiya",
    "ImmortalSasuke": "Sasuke",
    "SageNaruto": "Naruto",
    "RikudoNaruto": "Naruto",
    "RockLee": "Lee",
    "Nagato": "Pain",
    # This is an external modded replacement/variant of Choji, not a distinct
    # base character toward the 70+ distinct-character target.
    "TwoSageToads": "Choji",
    "JoninMinato": "Minato",
}
distinct_base_names = [name for name in names if name not in KNOWN_FORM_BASES]

# Preserve empty slots so every portrait can be checked against its exact page/slot.
slot_tokens = []
for item in re.finditer(r"'([^']*)'|\"([^\"]*)\"|(?P<none>(?<![\w])_None(?![\w]))", body):
    slot_name = item.group(1) or item.group(2) or None
    slot_tokens.append(slot_name)

# Enum entries outside the visible selection list may be forms, clones, summons,
# or implementation-only entities. Report them for manual classification; never
# count them as playable merely because an enum exists.
HERO_ENUM = GAME / "Classes/Enums/HeroEnum.h"
enum_source = HERO_ENUM.read_text(encoding="utf-8", errors="replace") if HERO_ENUM.is_file() else ""
enum_names = list(dict.fromkeys(re.findall(r"mk_const\(([^)]+)\)", enum_source)))
unlisted_enum_names = [name for name in enum_names if name not in names]

# Manual source-level classifications for enum-only identifiers. These are
# research classifications, not a claim that any ID is impossible to control;
# each is excluded from the playable count until it has a roster entry and tests.
ENUM_LEAD_CLASSIFICATIONS = {
    "AnimalPath": ("Pain path / AI-controlled support entity", "Classes/Core/Shinobi/AnimalPath.hpp"),
    "AsuraPath": ("Pain path / AI-controlled support entity", "Classes/Core/Shinobi/AsuraPath.hpp"),
    "HumanPath": ("Pain path / implementation entity; control path needs runtime review", "Classes/Core/Shinobi/HumanPath.hpp"),
    "PertaPath": ("Pain path / implementation entity; spelling follows source ID", "Classes/Core/Shinobi/PertaPath.hpp"),
    "NarakaPath": ("Pain path / implementation entity; control path needs runtime review", "Classes/Core/Shinobi/NarakaPath.hpp"),
    "NarutoClone": ("Summoned clone AI unit", "Classes/Core/Shinobi/Bunshin/NarutoClone.hpp"),
    "SageNarutoClone": ("Summoned clone AI unit", "Classes/Core/Shinobi/Bunshin/SageNarutoClone.hpp"),
    "RikudoNarutoClone": ("Summoned clone AI unit", "Classes/Core/Shinobi/Bunshin/RikudoNarutoClone.hpp"),
    "Guardian": ("Guardian AI class; Han/Roshi resources are off-roster leads", "Classes/Core/Guardian/Guardian.hpp"),
}

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
missing_frame_ref_details: dict[str, list[str]] = {}
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
    # XML comments sometimes retain abandoned animations that reference frames
    # from another character's atlas. Ignore those examples: they are not runtime
    # actions and must not be reported as broken frame references.
    active_xml_text = re.sub(r"<!--.*?-->", "", xml_text, flags=re.DOTALL)
    audio_events = len(re.findall(r"""<e\s+type=['"]setSound['"]>\s*Audio/[^<]+""", active_xml_text, re.IGNORECASE))
    xml_frames = set(re.findall(r"<f>\s*([^<]+?)\s*</f>", active_xml_text, re.IGNORECASE))
    # A few native forms share animation frames with their base character, and
    # skill frames may live in a separate *_Skill.plist beside the main atlas.
    # Compare against all atlases packaged for the character plus its explicit
    # SkillLayer UI/base-character alias; checking only Name.plist creates false
    # missing-frame alarms for valid shared frames.
    frame_atlas_paths = list(unit_dir.glob("*.plist"))
    frame_alias = skill_ui_aliases.get(name)
    if frame_alias and frame_alias != name:
        alias_dir = GAME / "Resources/Unit/Ninja" / frame_alias
        if alias_dir.is_dir():
            frame_atlas_paths.extend(alias_dir.glob("*.plist"))
    plist_frames = set()
    for frame_atlas_path in dict.fromkeys(frame_atlas_paths):
        try:
            frame_atlas_text = frame_atlas_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        plist_frames.update(re.findall(r"<key>([^<]+)</key>\s*<dict>", frame_atlas_text, re.IGNORECASE))
    missing_frame_refs = sorted(xml_frames - plist_frames)
    frame_coverage = f"{len(xml_frames - set(missing_frame_refs))}/{len(xml_frames)}" if xml_frames else "NO_XML_FRAMES"
    if missing_frame_refs:
        # Keep the full names in the report so likely copy/paste and alias issues can be triaged.
        missing_frame_ref_details[name] = missing_frame_refs
    detail_rows.append((name, animation_status, atlas_status, frame_coverage, f"{len(missing_frame_refs)} missing frame refs", f"{audio_events} audio event refs", f"{len(audio)} exact-name audio files", "YES" if enum_refs else "NO", "YES" if ai_refs else "MANUAL"))

portrait_complete = sum(1 for row in rows if row[8] == "2/2")
missing_portrait_names = [row[0] for row in rows if row[8] != "2/2"]
label_complete = sum(1 for row in rows if row[4] == "5/5")
missing_label_names = [(row[0], row[4]) for row in rows if row[4] != "5/5"]
selection_complete = sum(1 for row in rows if row[7] == "ALL_3_FRAMES_FOUND")
missing_selection_names = [row[0] for row in rows if row[7] != "ALL_3_FRAMES_FOUND"]

# Surface off-roster resource packages so future additions are researched instead
# of being silently ignored or counted as playable from file presence alone.
provider_path = GAME / "Classes/Core/Provider.hpp"
provider_source = provider_path.read_text(encoding="utf-8", errors="replace") if provider_path.is_file() else ""
select_atlas_path = GAME / "Resources/Select.plist"
select_atlas_source = select_atlas_path.read_text(encoding="utf-8", errors="replace") if select_atlas_path.is_file() else ""
report_atlas_path = GAME / "Resources/Report.plist"
report_atlas_source = report_atlas_path.read_text(encoding="utf-8", errors="replace") if report_atlas_path.is_file() else ""
guardian_class_path = GAME / "Classes/Core/Guardian/Guardian.hpp"
guardian_class_source = guardian_class_path.read_text(encoding="utf-8", errors="replace") if guardian_class_path.is_file() else ""
guardian_ai_override_detected = "void perform() override" in guardian_class_source and "attack(" in guardian_class_source and "walk(" in guardian_class_source

off_roster_candidates = []
for kind in ("Ninja", "Guardian"):
    root = GAME / "Resources/Unit" / kind
    if not root.is_dir():
        continue
    for unit_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        candidate = unit_dir.name
        if candidate in names:
            continue
        candidate_xml = unit_dir / f"{candidate}.xml"
        candidate_plist = unit_dir / f"{candidate}.plist"
        if not candidate_xml.is_file() and not candidate_plist.is_file():
            continue
        candidate_plist_text = candidate_plist.read_text(encoding="utf-8", errors="replace") if candidate_plist.is_file() else ""
        candidate_texture_match = re.search(r"<key>textureFileName</key>\s*<string>([^<]+)</string>", candidate_plist_text)
        candidate_texture_ok = bool(candidate_texture_match and (unit_dir / candidate_texture_match.group(1)).is_file())
        candidate_select_frames = sum(
            1 for suffix in ("_select.png", "_half.png", "_font.png")
            if f"{candidate}{suffix}".lower() in select_atlas_source.lower()
        )
        candidate_report_frames = sum(
            1 for suffix in ("_rp.png", "_rpf.png")
            if f"{candidate}{suffix}".lower() in report_atlas_source.lower()
        )
        candidate_skill_icons = sum(
            1 for i in range(1, 6)
            if f"{candidate}_skill{i}.png".lower() in resource_names
            or f"{candidate}_skill{i}.png".lower() in candidate_plist_text.lower()
        )
        candidate_audio = [rel for _, rel in relative if under_dir(rel, "Audio", candidate)]
        off_roster_candidates.append((
            candidate, kind,
            "XML+PLIST+TEXTURE" if candidate_xml.is_file() and candidate_plist.is_file() and candidate_texture_ok
            else ("XML+PLIST" if candidate_xml.is_file() and candidate_plist.is_file() else "INCOMPLETE"),
            "YES" if candidate in provider_source else "NO",
            "YES" if candidate in enum_names else "NO",
            f"{candidate_select_frames}/3",
            f"{candidate_report_frames}/2",
            f"{candidate_skill_icons}/5",
            len(candidate_audio),
        ))

OUT.parent.mkdir(parents=True, exist_ok=True)
with OUT.open("w", encoding="utf-8") as f:
    f.write("# Automated Character Package Inventory\n\n")
    f.write(f"- Candidate root: `{GAME}`\n")
    f.write(f"- Roster source: `lua/class/basic.lua`\n")
    target_gap = max(0, 70 - len(names))
    distinct_gap = max(0, 70 - len(distinct_base_names))
    f.write(f"- Unique selectable names found: **{len(names)}**\n")
    f.write(f"- Explicit selection slots mapped: **{len(slot_tokens)}** across **{(len(slot_tokens) + 20) // 21} pages** (21 slots per page).\n")
    f.write(f"- Selectable-entry target: **{len(names)}/70 declared ({target_gap} more entries to reach 70; alternate forms are included in this UI-entry count).**\n")
    f.write(f"- Distinct base-character count (excluding {len(KNOWN_FORM_BASES)} known alternate forms): **{len(distinct_base_names)}/70 ({distinct_gap} additional distinct characters needed; gameplay completeness is not implied).**\n")
    f.write("- Known alternate forms excluded from the distinct-character count: " + ", ".join(f"`{name}` → `{base}`" for name, base in KNOWN_FORM_BASES.items() if name in names) + ".\n")
    f.write("- Gameplay-verified playable count: **not measured by this static audit.**\n")
    f.write(f"- HeroEnum entries absent from the visible selection list: **{len(unlisted_enum_names)} requiring manual classification** (not counted as playable).\n")
    if unlisted_enum_names:
        f.write("- Non-roster enum leads: " + ", ".join(chr(96) + name + chr(96) for name in unlisted_enum_names) + ".\n")
    else:
        f.write("- Non-roster enum leads: none found.\n")
    f.write("\n## Enum-only ID classification (research aid)\n\n")
    f.write("These source-level labels help distinguish summon/support implementations from missing roster entries. They are not runtime-control proof; keep every ID out of the playable count until selection, player control, and battle lifecycle are tested.\n\n")
    f.write("| Enum ID | Preliminary classification | Inspected source path |\n")
    f.write("|---|---|---|\n")
    for enum_name in unlisted_enum_names:
        classification = ENUM_LEAD_CLASSIFICATIONS.get(enum_name, ("UNCLASSIFIED — inspect before roster planning", "not mapped"))
        f.write("| " + " | ".join(fmt(value) for value in (enum_name, *classification)) + " |\n")
    f.write(f"- Kill-feed portrait atlas coverage: **{portrait_complete}/{len(rows)} roster entries have both frames.**\n")
    f.write(f"- Character-selection image coverage: **{selection_complete}/{len(rows)} roster entries have all three expected selection frames/files.**\n")
    if missing_selection_names:
        f.write("- Selection image exceptions requiring manual review: " + ", ".join(f"`{name}`" for name in missing_selection_names) + ".\n")
    else:
        f.write("- Selection image exceptions requiring manual review: none detected by filename/frame-name audit.\n")
    f.write(f"- Skill-description label frame coverage: **{label_complete}/{len(rows)} roster entries have all five expected frames after applying SkillLayer UI aliases.**\n")
    # Image-label frame coverage and runtime text fallback coverage are separate:
    # Kabuto intentionally has no label sprites, but patched SkillLayer supplies
    # five descriptions so the UI can still explain its skills.
    fallback_block = re.search(r"local skillDescriptionFallbacks\s*=\s*\{([\s\S]*?)\n\}\n\nlocal transformList", skill_source)
    kabuto_fallback_count = 0
    if fallback_block:
        kabuto_block = re.search(r"Kabuto\s*=\s*\{([\s\S]*?)\n\s{4}\}", fallback_block.group(1))
        if kabuto_block:
            kabuto_fallback_count = len(re.findall(r"\[\d+\]\s*=\s*\"", kabuto_block.group(1)))
    f.write(f"- Kabuto runtime skill-description text fallbacks: **{kabuto_fallback_count}/5 detected in patched SkillLayer.lua** (separate from image-label frame coverage).\n")
    frame_complete = sum(1 for row in detail_rows if row[4].startswith("0 "))
    missing_frame_ref_rows = [(row[0], row[4]) for row in detail_rows if not row[4].startswith("0 ")]
    f.write(f"- Animation XML frame-reference coverage: **{frame_complete}/{len(detail_rows)} roster entries have no missing XML-to-atlas frame names.**\n")
    if missing_frame_ref_rows:
        f.write("- XML-to-atlas frame-reference exceptions: " + ", ".join(f"`{name}` ({count})" for name, count in missing_frame_ref_rows) + ".\n")
        f.write("\n### Missing XML frame names (first 12 per entry)\n\n")
        for name, missing_names in missing_frame_ref_details.items():
            shown = missing_names[:12]
            suffix = f"; plus {len(missing_names) - len(shown)} more" if len(missing_names) > len(shown) else ""
            f.write(f"- `{name}`: " + ", ".join(f"`{frame}`" for frame in shown) + suffix + ".\n")
    else:
        f.write("- XML-to-atlas frame-reference exceptions: none detected by name comparison.\n")
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
    f.write("\n## Exact character-selection slot map\n\n")
    f.write("| Page | Slot | Character ID/name | Selection art check |\n")
    f.write("|---:|---:|---|---|\n")
    for index, slot_name in enumerate(slot_tokens):
        if not slot_name:
            continue
        row = next((entry for entry in rows if entry[0] == slot_name), None)
        selection_status = row[7] if row else "NOT_IN_AUDIT"
        f.write(f"| {(index // 21) + 1} | {(index % 21) + 1} | {fmt(slot_name)} | {selection_status} |\n")
    f.write("\n## Detailed animation, atlas, audio, and AI checks\n\n")
    f.write("| Character | Animation/config XML | Sprite atlas + texture | XML frame refs resolved in atlas | Missing XML frame refs | Audio event references in XML | Exact-name audio files | Enum reference | AI registration clue |\n")
    f.write("|---|---|---|---:|---:|---:|---:|---|---|\n")
    for row in detail_rows:
        f.write("| " + " | ".join(fmt(x) for x in row) + " |\n")
    f.write("\n## Off-roster character package leads (not counted as playable)\n\n")
    f.write("These entries have resource folders but are not in the visible character roster. File presence alone does not establish a selectable/playable character.\n\n")
    f.write("| Candidate | Resource folder | Package completeness | Provider route | HeroEnum entry | Selection frames | Kill-feed frames | Skill icon frames | Exact-name audio files |\n")
    f.write("|---|---|---|---|---|---:|---:|---:|---:|\n")
    for row in off_roster_candidates:
        f.write("| " + " | ".join(fmt(x) for x in row) + " |\n")
    if not off_roster_candidates:
        f.write("| None found | — | — | — | — | — | — | — | — |\n")
    f.write("\n")
    f.write("\n### Guardian control-path note\n\n")
    if guardian_ai_override_detected:
        f.write("- Source-level Guardian assessment: **AI combat behavior override detected** (`perform()` includes target-seeking, `walk()`, and `attack()` calls). This is evidence of an AI behavior path, not evidence of direct player-control support for Han or Roshi.\n")
    else:
        f.write("- Source-level Guardian assessment: **not established by this static check**; manually inspect the class and its control path before classifying Han/Roshi.\n")
    f.write("- Han/Roshi remain resource leads only until a player-controlled Hero lifecycle, unique selection art, skill UI, effects/audio, AI behavior, and full gameplay tests are implemented and verified.\n")
    f.write("\n## Interpretation rules\n\n")
    f.write("- A `NO/MONOLITHIC` header result means the code may be in a shared C++ file; it is not proof the character is absent. Unit/resource counts are broad filename matches and do not prove the correct frames load.\n")
    f.write("- Missing skill icon or description-label frame names require manual investigation. A missing label can make the skill-view UI request a nonexistent frame; this audit does not test runtime handling or invent replacement descriptions. Some forms may share assets/classes and some skill UI may be assembled indirectly.\n")
    f.write("- XML frame-reference coverage compares every <f> frame name in the character XML against keys in that character's plist. Missing names are reported for manual investigation; this does not verify animation timing, atlas loading, or visual correctness.\n")
    f.write("- Audio counts are path matches only and do not distinguish voice from effects or prove event triggers.\n")
    f.write("- A selection art result is based on finding expected frame names in `Select.plist` or standalone files; runtime selection still needs testing.\n- Kill-feed portrait count checks `<Name>_rp.png` and `<Name>_rpf.png` in `Resources/Report.plist`; it does not prove killer/victim attribution or on-screen rendering works at runtime.\n")
    f.write("- Do not promote any entry to implemented or verified based on this report alone. Record voice lines, SFX triggers, skills, resource paths, AI behavior, provenance, and rights separately.\n")
print(f"Wrote {OUT}; audited {len(names)} unique selectable names; kill-feed portrait atlas coverage {portrait_complete}/{len(rows)}.")
if missing_portrait_names:
    raise SystemExit("Missing kill-feed portrait frames for: " + ", ".join(missing_portrait_names))
