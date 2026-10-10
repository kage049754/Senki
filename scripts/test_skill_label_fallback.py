#!/usr/bin/env python3
"""Static regression checks for missing skill-description frame handling."""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_skill_label_fallback.py PATH_TO_SkillLayer.lua")

source = Path(sys.argv[1]).read_text(encoding="utf-8")
required = [
    "local skillUiAlias = {",
    "local skillLabelHero = skillUiAlias[self.selectHero] or self.selectHero",
    "imgPath = skillLabelHero .. '_label' .. (buttonType - 2) .. '.png'",
    "local skillFrameOk, skillFrame = pcall(display.newSpriteFrame, imgPath)",
    "if skillFrameOk and skillFrame then",
    "self._skillExplain = display.newSprite('#' .. imgPath)",
    'text = "Skill description unavailable"',
    "self._skillExplain:setAnchorPoint(0, 0)",
    "self._skillExplain:setPositionX(10)",
    "self._skillExplainClipper = clipper",
    "if self._skillExplainClipper then",
    "self._skillExplainClipper:removeFromParent()",
    "self._skillExplainClipper = nil",
]
missing = [fragment for fragment in required if fragment not in source]
if missing:
    raise SystemExit("Missing skill-description fallback behavior: " + ", ".join(missing))
assert source.index("local skillUiAlias = {") < source.index("function SkillLayer:setSkillExplain")
assert source.index("local skillLabelHero = skillUiAlias[self.selectHero] or self.selectHero") < source.index("local skillFrameOk, skillFrame")
assert source.index("local skillFrameOk, skillFrame") < source.index("self._skillExplain = display.newSprite('#' .. imgPath)")
assert source.index('text = "Skill description unavailable"') < source.index("self._skillExplain:setAnchorPoint(0, 0)")
assert source.index("self._skillExplainClipper:removeFromParent()") < source.index("self._skillExplainClipper = clipper")
print("Missing skill labels have a visible fallback; switching skills removes the old tooltip container.")
