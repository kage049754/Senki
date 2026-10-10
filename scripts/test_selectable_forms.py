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
character_base = (game / "Classes/CharacterBase.cpp").read_text(encoding="utf-8")
provider = (game / "Classes/Core/Provider.hpp").read_text(encoding="utf-8")
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
    resource_dir = game / "Resources/Unit/Ninja" / name
    resource = resource_dir / f"{name}.xml"
    atlas = resource_dir / f"{name}.plist"
    header = game / "Classes/Core/Shinobi" / class_headers[name]
    if not resource.is_file() or not atlas.is_file() or not header.is_file():
        raise SystemExit(f"Missing character XML/plist/class header for {name}")
    atlas_text = atlas.read_text(encoding="utf-8", errors="replace")
    texture_match = re.search(r"<key>textureFileName</key>\s*<string>([^<]+)</string>", atlas_text)
    if not texture_match:
        raise SystemExit(f"Cannot determine atlas texture filename from {atlas}")
    texture = resource_dir / texture_match.group(1)
    if not texture.is_file():
        raise SystemExit(f"Missing texture referenced by {atlas}: {texture.name}")
    if f"HeroEnum::{name}" not in header.read_text(encoding="utf-8"):
        raise SystemExit(f"Native character class does not register {name}: {header}")
    if f"{name} = '{alias}'" not in select or f"{name} = '{display}'" not in select:
        raise SystemExit(f"Missing selection art/display-name aliases for {name}")
    if f"{name} = '{skill_alias}'" not in skill:
        raise SystemExit(f"Missing skill UI alias for {name}")
for fragment in ["skillUiAlias[self.selectHero] or self.selectHero", "local skillFrameOk, skillFrame = pcall(display.newSpriteFrame, imgPath)", 'text = "Skill description unavailable"']:
    if fragment not in skill:
        raise SystemExit(f"Missing safe skill-view handling: {fragment}")

# These are the existing native form-transition paths, not just names in a UI list.
transformations = [
    ("HeroEnum::Naruto", "HeroEnum::SageNaruto"),
    ("HeroEnum::SageNaruto", "HeroEnum::RikudoNaruto"),
    ("HeroEnum::Jiraiya", "HeroEnum::SageJiraiya"),
    ("HeroEnum::Sasuke", "HeroEnum::ImmortalSasuke"),
    ("HeroEnum::Lee", "HeroEnum::RockLee"),
    ("HeroEnum::Pain", "HeroEnum::Nagato"),
]
for base_name, form_name in transformations:
    if base_name not in character_base or form_name not in character_base:
        raise SystemExit(f"Native transformation path is missing: {base_name} -> {form_name}")

# Ensure each selectable form is dispatched to its existing native class.
provider_patterns = [
    r'is_or\("Jiraiya",\s*"SageJiraiya"\)\s*ptr\s*=\s*new Jiraiya\(\);',
    r'is_or\("Sasuke",\s*"ImmortalSasuke"\)\s*ptr\s*=\s*new Sasuke\(\);',
    r'is\("SageNaruto"\)\s*is_role\(Role::Clone\).*?else ptr = new Naruto\(\);',
    r'is\("RikudoNaruto"\)\s*is_role\(Role::Clone\).*?else ptr = new Naruto\(\);',
    r'is_or\("Lee",\s*"RockLee"\)\s*ptr\s*=\s*new Lee\(\);',
    r'is_or\("Pain",\s*"Nagato"\)\s*ptr\s*=\s*new Pain\(\);',
]
for pattern in provider_patterns:
    if not re.search(pattern, provider, re.DOTALL):
        raise SystemExit(f"Native Provider dispatch is missing or changed: {pattern}")
select_plist = (game / "Resources/Select.plist").read_text(encoding="utf-8", errors="replace")
for name in forms:
    if f"<key>{name}_half.png</key>" not in select_plist:
        raise SystemExit(f"Missing dedicated form portrait frame: {name}_half.png")
print("Six existing native forms are in the 84-slot roster, have enum/XML/atlas support, and have safe selection/skill UI aliases.")
