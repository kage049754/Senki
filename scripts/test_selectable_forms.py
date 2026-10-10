#!/usr/bin/env python3
"""Check roster exposure for existing native transformation forms."""
from pathlib import Path
import re
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_selectable_forms.py PATH_TO_projects/NarutoSenki")
game = Path(sys.argv[1])
basic = (game / "lua/class/basic.lua").read_text(encoding="utf-8")
select = (game / "lua/ui/SelectLayer.lua").read_text(encoding="utf-8")
skill = (game / "lua/ui/SkillLayer.lua").read_text(encoding="utf-8")
enum = (game / "Classes/Enums/HeroEnum.h").read_text(encoding="utf-8")
forms = {
    "SageJiraiya": ("Jiraiya", "Sage Jiraiya", "Jiraiya"),
    "ImmortalSasuke": ("Sasuke", "Immortal Sasuke", "Sasuke"),
    "SageNaruto": ("Naruto", "Sage Naruto", "Naruto"),
    "RikudoNaruto": ("Naruto", "Six Paths Naruto", "Naruto"),
    "RockLee": ("Lee", "Rock Lee", "Lee"),
    "Nagato": ("Pain", "Nagato", "Pain"),
}
body_match = re.search(r"ns\.CharactersLayout\s*=\s*\{([\s\S]*?)\n\}", basic)
if not body_match:
    raise SystemExit("Could not locate roster table after adding forms")
body = re.sub(r"--\[\[[\s\S]*?\]\]", "", body_match.group(1))
body = re.sub(r"--[^\n]*", "", body)
tokens = re.findall(r"'[^']*'|\"[^\"]*\"|(?<![\w])_None(?![\w])", body)
if len(tokens) != 84:
    raise SystemExit(f"Expected exactly 84 slots (4 pages), found {len(tokens)}")
class_headers = {
    "SageJiraiya": "Jiraiya.hpp",
    "ImmortalSasuke": "Sasuke.hpp",
    "SageNaruto": "Naruto.hpp",
    "RikudoNaruto": "Naruto.hpp",
    "RockLee": "Lee.hpp",
    "Nagato": "Pain.hpp",
}
for name, (alias, display, skill_alias) in forms.items():
    if f"'{name}'" not in body:
        raise SystemExit(f"Form is missing from roster: {name}")
    if not re.search(rf"mk_const\({re.escape(name)}\)", enum):
        raise SystemExit(f"Native enum missing for {name}")
    resource = game / "Resources/Unit/Ninja" / name / f"{name}.xml"
    atlas = game / "Resources/Unit/Ninja" / name / f"{name}.plist"
    header = game / "Classes/Core/Shinobi" / class_headers[name]
    if not resource.is_file() or not atlas.is_file() or not header.is_file():
        raise SystemExit(f"Missing character XML/plist/class header for {name}")
    if f"HeroEnum::{name}" not in header.read_text(encoding="utf-8"):
        raise SystemExit(f"Native character class does not register {name}: {header}")
    if f"{name} = '{alias}'" not in select or f"{name} = '{display}'" not in select:
        raise SystemExit(f"Missing selection art/display-name aliases for {name}")
    if f"{name} = '{skill_alias}'" not in skill:
        raise SystemExit(f"Missing skill UI alias for {name}")
for fragment in ["skillUiAlias[self.selectHero] or self.selectHero", "local skillFrameOk, skillFrame = pcall(display.newSpriteFrame, imgPath)", 'text = "Skill description unavailable"']:
    if fragment not in skill:
        raise SystemExit(f"Missing safe skill-view handling: {fragment}")
select_plist = (game / "Resources/Select.plist").read_text(encoding="utf-8", errors="replace")
for name in forms:
    if f"<key>{name}_half.png</key>" not in select_plist:
        raise SystemExit(f"Missing dedicated form portrait frame: {name}_half.png")
print("Six existing native forms are in the 84-slot roster, have enum/XML/atlas support, and have safe selection/skill UI aliases.")
