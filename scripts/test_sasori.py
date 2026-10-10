#!/usr/bin/env python3
"""Static/resource regression checks for the additive Sasori character integration."""
from pathlib import Path
import plistlib, re, sys, xml.etree.ElementTree as ET
if len(sys.argv) != 2:
    raise SystemExit("usage: test_sasori.py PATH_TO_GAME")
game = Path(sys.argv[1])
basic = (game / "lua/class/basic.lua").read_text(encoding="utf-8")
provider = (game / "Classes/Core/Provider.hpp").read_text(encoding="utf-8")
enum = (game / "Classes/Enums/HeroEnum.h").read_text(encoding="utf-8")
select = (game / "lua/ui/SelectLayer.lua").read_text(encoding="utf-8")
skill = (game / "lua/ui/SkillLayer.lua").read_text(encoding="utf-8")
header = (game / "Classes/Core/Shinobi/Sasori.hpp").read_text(encoding="utf-8")
assert "'Sasori'" in basic, "Sasori is not in the selectable roster"
roster = basic.split("ns.CharactersLayout = {", 1)[1].split("\n}", 1)[0]
roster = re.sub(r"--\[\[[\s\S]*?\]\]", "", roster)
roster = re.sub(r"--[^\n]*", "", roster)
tokens = re.findall(r"'[^']*'|\"[^\"]*\"|(?<![\w])_None(?![\w])", roster)
assert len(tokens) == 84, f"Unexpected roster size: {len(tokens)}"
assert tokens.count("'Sasori'") == 1, "Sasori must occupy one slot only"
assert "mk_const(Sasori);" in enum
assert '#include "Shinobi/Sasori.hpp"' in provider
assert re.search(r'is\("Sasori"\)\s*ptr\s*=\s*new Sasori\(\);', provider)
assert "class Sasori" in header and "HeroEnum::Sasori" in header
assert "Sasori = 'Kankuro'" in select and "Sasori = 'Sasori'" in select
assert "Sasori = 'Kankuro'" in skill
unit = game / "Resources/Unit/Ninja/Sasori"
for p in [unit/"Sasori.png", unit/"Sasori.plist", unit/"Sasori.xml", unit/"Sasori_Skill.plist"]:
    assert p.is_file() and p.stat().st_size > 0, f"Missing package file: {p}"
main = plistlib.loads((unit/"Sasori.plist").read_bytes())
skills = plistlib.loads((unit/"Sasori_Skill.plist").read_bytes())
assert main.get("frames") and skills.get("frames")
main_texture = main.get("metadata", {}).get("textureFileName")
skill_texture = skills.get("metadata", {}).get("textureFileName")
assert main_texture and (unit/main_texture).is_file(), f"Missing main atlas texture {main_texture}"
assert skill_texture and (unit/skill_texture).is_file(), f"Missing skill atlas texture {skill_texture}"
root = ET.parse(unit/"Sasori.xml").getroot()
refs = {n.text.strip() for n in root.iter("f") if n.text and n.text.strip()}
assert not (refs - set(main["frames"]) - set(skills["frames"])), "Unresolved animation frame references remain"
xml = (unit/"Sasori.xml").read_text(encoding="utf-8")
for clip in re.findall(r'Audio/Sasori/([^<\" ]+?\.ogg)', xml):
    assert (game/"Resources/Audio/Sasori"/clip).is_file(), f"Missing audio clip: {clip}"
assert "Audio/Kankuro/" not in xml
print("Sasori checks passed: roster, enum/provider dispatch, atlases, animation frames, audio references, and selection/skill UI aliases.")
