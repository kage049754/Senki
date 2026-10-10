#!/usr/bin/env python3
"""Static regression checks for missing skill-description frame handling."""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_skill_label_fallback.py PATH_TO_SkillLayer.lua")

source = Path(sys.argv[1]).read_text(encoding="utf-8")
required = [
    "local skillFrameOk, skillFrame = pcall(display.newSpriteFrame, imgPath)",
    "if skillFrameOk and skillFrame then",
    "self._skillExplain = display.newSprite('#' .. imgPath)",
    'text = "Skill description unavailable"',
    "self._skillExplain:setAnchorPoint(0, 0)",
    "self._skillExplain:setPositionX(10)",
]
missing = [fragment for fragment in required if fragment not in source]
if missing:
    raise SystemExit("Missing skill-description fallback behavior: " + ", ".join(missing))
assert source.index("local skillFrameOk, skillFrame") < source.index("self._skillExplain = display.newSprite('#' .. imgPath)")
assert source.index('text = "Skill description unavailable"') < source.index("self._skillExplain:setAnchorPoint(0, 0)")
print("Skill-description frame lookup is protected; missing frames show a visible fallback label.")
