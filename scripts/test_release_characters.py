#!/usr/bin/env python3
"""Regression checks for the v1.25/v1.26 release character import batch."""
from pathlib import Path
import json
import plistlib
import re
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    raise SystemExit("usage: test_release_characters.py PATH_TO_projects/NarutoSenki")
game = Path(sys.argv[1])
resources = game / "Resources"
manifest_path = resources / "Unit/Ninja/release_character_import_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
expected = {
    "Kurenai": ("Hinata", "Kurenai", True),
    "MightGuy": ("Lee", "Might Guy", True),
    "Yamato": ("Kakashi", "Yamato", True),
    "Sasori": ("Kankuro", "Sasori", True),
    "Zetsu": ("Sai", "Zetsu", True),
    "Iruka": ("Asuma", "Iruka", True),
    "Shizune": ("Sakura", "Shizune", True),
    "Hashirama": ("Tobirama", "Hashirama", True),
    "Rin": ("Sakura", "Rin", True),
    "SakonUkon": ("Jugo", "Sakon & Ukon", True),
    "Juzo": ("Kisame", "Juzo", True),
    "JoninMinato": ("Minato", "Jonin Minato", False),
}
characters = {entry["id"]: entry for entry in manifest.get("characters", [])}
assert set(characters) == set(expected), f"Imported character IDs differ: missing={sorted(set(expected)-set(characters))}, extra={sorted(set(characters)-set(expected))}"
assert sum(1 for entry in characters.values() if entry.get("distinct")) == 11
assert sum(1 for entry in characters.values() if not entry.get("distinct")) == 1

enum_text = (game / "Classes/Enums/HeroEnum.h").read_text(encoding="utf-8")
provider_text = (game / "Classes/Core/Provider.hpp").read_text(encoding="utf-8")
basic = (game / "lua/class/basic.lua").read_text(encoding="utf-8")
select = (game / "lua/ui/SelectLayer.lua").read_text(encoding="utf-8")
skill = (game / "lua/ui/SkillLayer.lua").read_text(encoding="utf-8")
roster = basic.split("ns.CharactersLayout = {", 1)[1].split("\n}", 1)[0]
roster = re.sub(r"--\[\[[\s\S]*?\]\]", "", roster)
roster = re.sub(r"--[^\n]*", "", roster)
tokens = re.findall(r"'[^']*'|\"[^\"]*\"|(?<![\w])_None(?![\w])", roster)
assert len(tokens) == 84, f"Expected 84 roster slots, got {len(tokens)}"

for char_id, (base, display, distinct) in expected.items():
    entry = characters[char_id]
    assert entry["base_ai"] == base, f"{char_id} is mapped to the wrong compatibility AI"
    assert entry["display"] == display
    assert bool(entry["distinct"]) == distinct
    assert tokens.count(f"'{char_id}'") == 1, f"{char_id} must occupy exactly one selectable slot"
    assert f"mk_const({char_id});" in enum_text, f"Missing HeroEnum entry for {char_id}"
    assert f'#include "Shinobi/{char_id}.hpp"' in provider_text, f"Missing Provider include for {char_id}"
    assert re.search(r'is\("' + re.escape(char_id) + r'"\)\s*ptr = new ' + re.escape(char_id) + r'\(\);', provider_text), f"Missing Provider dispatch for {char_id}"
    header = game / "Classes/Core/Shinobi" / (char_id + ".hpp")
    assert header.is_file() and f"HeroEnum::{char_id}" in header.read_text(encoding="utf-8")
    assert f"{char_id} = '{base}'" in select
    assert f"{char_id} = '{display}'" in select
    assert f"{char_id} = '{base}'" in skill

    unit = resources / "Unit/Ninja" / char_id
    xml_path = unit / (char_id + ".xml")
    main_plist = unit / (char_id + ".plist")
    main_data = plistlib.loads(main_plist.read_bytes())
    skill_plist = unit / (char_id + "_Skill.plist")
    skill_data = plistlib.loads(skill_plist.read_bytes())
    xml_root = ET.parse(xml_path).getroot()
    main_texture = main_data.get("metadata", {}).get("textureFileName")
    skill_texture = skill_data.get("metadata", {}).get("textureFileName")
    assert main_texture and (unit / main_texture).is_file(), f"{char_id} main atlas texture missing"
    assert skill_texture and (unit / skill_texture).is_file(), f"{char_id} skill atlas texture missing"
    refs = {node.text.strip() for node in xml_root.iter("f") if node.text and node.text.strip()}
    missing = sorted(refs - set(main_data.get("frames", {})) - set(skill_data.get("frames", {})))
    assert not missing, f"{char_id} has unresolved animation frames: {missing[:12]}"
    xml_text = xml_path.read_text(encoding="utf-8")
    audio_refs = re.findall(r"Audio/([^<\" ]+?\.ogg)", xml_text)
    for audio_ref in audio_refs:
        assert (resources / "Audio" / audio_ref).is_file(), f"{char_id} references missing audio: {audio_ref}"

print("Release character import checks passed: 12 selectable IDs, 10 distinct base fighters, 1 alternate Minato form, native dispatch, atlases, animation frame coverage, audio references, and UI aliases.")
