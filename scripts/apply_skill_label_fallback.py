#!/usr/bin/env python3
"""Protect missing skill-description frames and clean up their tooltip container."""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: apply_skill_label_fallback.py PATH_TO_SkillLayer.lua")

target = Path(sys.argv[1])
source = target.read_text(encoding="utf-8")

old_cleanup = "    if self._skillExplain then self._skillExplain:removeFromParent() end"
new_cleanup = """    if self._skillExplainClipper then
        self._skillExplainClipper:removeFromParent()
        self._skillExplainClipper = nil
        self._skillExplain = nil
    elseif self._skillExplain then
        self._skillExplain:removeFromParent()
        self._skillExplain = nil
    end"""
if old_cleanup in source:
    source = source.replace(old_cleanup, new_cleanup, 1)
elif "if self._skillExplainClipper then" not in source:
    raise SystemExit("Cannot find skill-description cleanup block.")

old_sprite = """    self._skillExplain = display.newSprite('#' .. imgPath)
    self._skillExplain:setAnchorPoint(0, 0)
    self._skillExplain:setPositionX(10)
"""
new_sprite = """    -- A missing description frame must not break the skill-details view.
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
if old_sprite in source:
    source = source.replace(old_sprite, new_sprite, 1)
elif "local skillFrameOk, skillFrame = pcall(display.newSpriteFrame, imgPath)" not in source:
    raise SystemExit("Cannot find skill-description sprite construction block.")

old_add = "    self:addChild(clipper, 600)"
if "self._skillExplainClipper = clipper" not in source:
    if source.count(old_add) != 1:
        raise SystemExit("Cannot attach tooltip container tracking: expected one clipper addChild call.")
    source = source.replace(old_add, "    self._skillExplainClipper = clipper\n" + old_add, 1)

target.write_text(source, encoding="utf-8")
print(f"Applied safe missing-label fallback and tooltip cleanup to {target}")
