#!/usr/bin/env python3
"""Static/resource regression checks for Han's additive playable integration."""
from pathlib import Path
import plistlib, re, sys, xml.etree.ElementTree as ET
if len(sys.argv) != 2:
    raise SystemExit("usage: test_han.py PATH_TO_GAME")
game = Path(sys.argv[1])
basic = (game / "lua/class/basic.lua").read_text(encoding="utf-8")
provider = (game / "Classes/Core/Provider.hpp").read_text(encoding="utf-8")
enum = (game / "Classes/Enums/HeroEnum.h").read_text(encoding="utf-8")
select = (game / "lua/ui/SelectLayer.lua").read_text(encoding="utf-8")
skill = (game / "lua/ui/SkillLayer.lua").read_text(encoding="utf-8")
header = (game / "Classes/Core/Shinobi/Han.hpp").read_text(encoding="utf-8")
assert "'Han'" in basic, "Han missing from selectable roster"
roster = basic.split("ns.CharactersLayout = {", 1)[1].split("\n}", 1)[0]
roster = re.sub(r"--\[\[[\s\S]*?\]\]", "", roster)
roster = re.sub(r"--[^\n]*", "", roster)
tokens = re.findall(r"'[^']*'|\"[^\"]*\"|(?<![\w])_None(?![\w])", roster)
assert len(tokens) == 84, f"Unexpected roster size: {len(tokens)}"
assert tokens.count("'Han'") == 1, "Han must occupy one slot only"
assert "mk_const(Han);" in enum
assert '#include "Shinobi/Han.hpp"' in provider
assert re.search(r'is\("Han"\)\s*ptr\s*=\s*new Han\(\);', provider)
assert "class Han" in header and "HeroEnum::Han" in header
assert "Han = 'Kankuro'" in select and "Han = 'Han'" in select
assert "Han = 'Kankuro'" in skill
unit = game / "Resources/Unit/Ninja/Han"
for p in (unit/"Han.pvr.ccz", unit/"Han.plist", unit/"Han.xml", unit/"Han_Compat.plist"):
    assert p.is_file() and p.stat().st_size > 0, f"Missing Han package file: {p}"
main = plistlib.loads((unit/"Han.plist").read_bytes())
compat = plistlib.loads((unit/"Han_Compat.plist").read_bytes())
assert main.get("frames") and compat.get("frames")
assert main.get("metadata", {}).get("textureFileName") == "Han.pvr.ccz"
compat_texture = compat.get("metadata", {}).get("textureFileName")
assert compat_texture and (unit/compat_texture).is_file(), f"Missing Han compatibility texture: {compat_texture}"
root = ET.parse(unit/"Han.xml").getroot()
assert root.tag == "unit"
actions = {node.get("name"): node for node in root.findall("action")}
for name in ("Idle", "Walk", "Dead", "nAttack", "skill01", "skill02", "skill03", "skill04", "skill05"):
    assert name in actions, f"Missing Han action {name}"
for name in ("skill01", "skill02", "skill03", "skill04", "skill05"):
    assert list(actions[name].iter("f")), f"Han {name} has no animation frames"
hp = actions["Idle"].find("./data/p[@type='attackValue']")
assert hp is not None and hp.text == "5500", "Han must use playable-scale HP, not Guardian boss HP"
refs = {n.text.strip() for n in root.iter("f") if n.text and n.text.strip()}
assert not (refs - set(main["frames"]) - set(compat["frames"])), "Unresolved Han animation frames remain"
for clip in re.findall(r'Audio/Han/([^<"]+?\.ogg)', (unit/"Han.xml").read_text(encoding="utf-8")):
    assert (game/"Resources/Audio/Han"/clip).is_file(), f"Missing Han audio: {clip}"
assert "Audio/Kankuro/" not in (unit/"Han.xml").read_text(encoding="utf-8")
print("Han checks passed: roster, native dispatch, transformation actions, animation frames, fallback skills, audio, and UI aliases.")
