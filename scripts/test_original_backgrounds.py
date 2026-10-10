#!/usr/bin/env python3
"""Regression guard: preserve the candidate's original selection and mode-menu backgrounds."""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_original_backgrounds.py PATH_TO_projects/NarutoSenki")

game = Path(sys.argv[1])
select = (game / "lua/ui/SelectLayer.lua").read_text(encoding="utf-8")
mode = (game / "Classes/UI/GameModeLayer.cpp").read_text(encoding="utf-8")

required_select = [
    "local bg_src = self.enableCustomSelect and 'red_bg.png' or 'blue_bg.png'",
    "local bgSprite = display.newSprite(bg_src, 0, 0)",
]
required_mode = [
    'auto bgSprite = Sprite::create("red_bg.png");',
    'auto menu_bar_b = Sprite::create("menu_bar2.png");',
    'auto menu_bar_t = Sprite::create("menu_bar3.png");',
    'Sprite::createWithSpriteFrameName("startmenu_title.png")',
]
missing = [f"SelectLayer.lua: {item}" for item in required_select if item not in select]
missing += [f"GameModeLayer.cpp: {item}" for item in required_mode if item not in mode]
if missing:
    raise SystemExit("Original selection/mode-menu background regression: " + "; ".join(missing))

print("Original character-selection red/blue background logic and original mode-menu background/menu-bar/title sources are preserved.")
