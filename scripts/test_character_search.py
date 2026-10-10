#!/usr/bin/env python3
"""Static regression checks for the character page controls and switch handler."""

from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_character_search.py PATH_TO_SelectLayer.lua")

source = Path(sys.argv[1]).read_text(encoding="utf-8")

required = [
    "function SelectLayer:onPageButtonClick(index)",
    "pageBtn:selected()",
    "pageBtn:unselected()",
    "pageLayer:show()",
    "pageLayer:hide()",
    "pageLayer:setPositionY(0)",
    "pageLayer:setPositionY(10000)",
    "local pageListener = function()",
    "return self:onPageButtonClick(index)",
    "if i <= 3 then",
    "ui.newImageMenuItem",
    "senki_page\' .. tostring(i) .. \'_off.png",
    "senki_page\' .. tostring(i) .. \'_on.png",
    "self.pageNum = math.max(1, math.ceil(#charactersList / 21))",
]
missing = [fragment for fragment in required if fragment not in source]
if missing:
    raise SystemExit("Missing character pagination behavior: " + ", ".join(missing))

if "ui.newTTFLabelMenuItem" in source:
    raise SystemExit("Text-only page controls are still present.")

if "self.pageNum = 3" in source:
    raise SystemExit("The fixed three-page limit is still present.")

print("Character page controls retain image-based normal/selected states, dynamic page count, and the original page visibility/selection handler.")
