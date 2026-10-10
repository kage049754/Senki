#!/usr/bin/env python3
"""Regression checks for the additive Two Sage Toads character port."""
from pathlib import Path
import plistlib
import re
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    raise SystemExit("usage: test_two_sage_toads.py PATH_TO_projects/NarutoSenki")
game = Path(sys.argv[1])
basic = (game / "lua/class/basic.lua").read_text(encoding="utf-8")
provider = (game / "Classes/Core/Provider.hpp").read_text(encoding="utf-8")
enum = (game / "Classes/Enums/HeroEnum.h").read_text(encoding="utf-8")
select = (game / "lua/ui/SelectLayer.lua").read_text(encoding="utf-8")
skill = (game / "lua/ui/SkillLayer.lua").read_text(encoding="utf-8")
header = (game / "Classes/Core/Shinobi/TwoSageToads.hpp").read_text(encoding="utf-8")
unit = game / "Resources/Unit/Ninja/TwoSageToads"
xml_path = unit / "TwoSageToads.xml"
main_plist = unit / "TwoSageToads.plist"
skill_plist = unit / "TwoSageToads_Skill.plist"
main_png = unit / "TwoSageToads.png"
skill_png = unit / "TwoSageToads_Skill.png"

assert "'TwoSageToads'" in basic, "Two Sage Toads is not selectable in the roster"
roster = basic.split("ns.CharactersLayout = {", 1)[1].split("\n}", 1)[0]
roster = re.sub(r"--\[\[[\s\S]*?\]\]", "", roster)
roster = re.sub(r"--[^\n]*", "", roster)
tokens = re.findall(r"'[^']*'|\"[^\"]*\"|(?<![\w])_None(?![\w])", roster)
assert len(tokens) == 84, f"Roster slot count changed unexpectedly: {len(tokens)}"
assert tokens.count("'TwoSageToads'") == 1, "Two Sage Toads must occupy exactly one slot"
assert "mk_const(TwoSageToads);" in enum
assert '#include "Shinobi/TwoSageToads.hpp"' in provider
assert re.search(r'is\("TwoSageToads"\)\s+ptr\s*=\s*new TwoSageToads\(\);', provider)
assert "class TwoSageToads : public Hero" in header
assert "TwoSageToads = 'Choji'" in select
assert "TwoSageToads = 'Two Sage Toads'" in select
assert "TwoSageToads = 'Choji'" in skill
for path in (xml_path, main_plist, skill_plist, main_png, skill_png):
    assert path.is_file() and path.stat().st_size > 0, f"Missing/empty character asset: {path}"
ET.parse(xml_path)
main = plistlib.loads(main_plist.read_bytes())
skills = plistlib.loads(skill_plist.read_bytes())
assert main.get("frames"), "Main character atlas has no frame entries"
assert skills.get("frames"), "Skill atlas has no frame entries"
assert main.get("metadata", {}).get("textureFileName") == "TwoSageToads.png"
assert skills.get("metadata", {}).get("textureFileName") == "TwoSageToads_Skill.png"
xml_text = xml_path.read_text(encoding="utf-8")
assert "Audio/TwoSageToads/" in xml_text, "Animation XML does not point at the new audio package"
assert "Audio/Choji/" not in xml_text, "Animation XML still points at Choji audio"
assert "Choji_" not in xml_text, "Animation XML still contains old character frame IDs"
print("Two Sage Toads integration checks passed: unique selectable slot, native enum/AI dispatch, V2 animation XML, modded atlases, audio package, and selection/skill UI aliases.")
