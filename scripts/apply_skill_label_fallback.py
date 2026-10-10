#!/usr/bin/env python3
"""Add a safe, visible fallback when a skill-description sprite frame is absent."""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: apply_skill_label_fallback.py PATH_TO_SkillLayer.lua")

target = Path(sys.argv[1])
source = target.read_text(encoding="utf-8")
marker = "local skillFrameOk, skillFrame = pcall(display.newSpriteFrame, imgPath)"
if marker in source:
    print("Skill-description fallback already present; leaving file unchanged.")
    raise SystemExit(0)

old = """    self._skillExplain = display.newSprite('#' .. imgPath)
    self._skillExplain:setAnchorPoint(0, 0)
    self._skillExplain:setPositionX(10)
"""
new = """    -- Some characters in this source snapshot do not ship every expected
    -- *_labelN.png frame. Check the frame cache before constructing a sprite:
    -- a missing frame should never blank/crash the skill-details view.
    local skillFrameOk, skillFrame = pcall(display.newSpriteFrame, imgPath)
    if skillFrameOk and skillFrame then
        self._skillExplain = display.newSprite('#' .. imgPath)
    else
        self._skillExplain = ui.newTTFLabel({
            text = "Skill description unavailable",
            font = ui.DEFAULT_TTF_FONT,
            size = 16,
            color = ccc3(255, 255, 255)
        })
    end
    self._skillExplain:setAnchorPoint(0, 0)
    self._skillExplain:setPositionX(10)
"""
count = source.count(old)
if count != 1:
    raise SystemExit(f"Cannot apply skill-description fallback: expected 1 target block, found {count}.")
source = source.replace(old, new, 1)
target.write_text(source, encoding="utf-8")
print(f"Applied safe missing-skill-label fallback to {target}")
