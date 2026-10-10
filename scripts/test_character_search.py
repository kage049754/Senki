#!/usr/bin/env python3
"""Exercise the real character-page switching method with lightweight Lua stubs."""

from pathlib import Path
import subprocess
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_character_search.py PATH_TO_SelectLayer.lua")

source = Path(sys.argv[1]).read_text(encoding="utf-8")
start_marker = "function SelectLayer:onPageButtonClick(index)"
end_marker = "\nfunction SelectLayer:setSelected(btn)"
start = source.find(start_marker)
end = source.find(end_marker, start + len(start_marker))
if start < 0 or end < 0:
    raise SystemExit("Cannot find the exact page-switch function boundaries in SelectLayer.lua.")

page_function = source[start:end]
if "function SelectLayer:filterCharacters(query)" not in page_function:
    raise SystemExit("Expected patched character filter method alongside page-switch handler.")
if "if i <= 3 then" not in source or "ui.newImageMenuItem" not in source:
    raise SystemExit("Original image-based touch menu items for the first three pages are missing.")
if "self.pageNum = 3" in source:
    raise SystemExit("The fixed three-page limit is still present.")

harness = r'''
SelectLayer = {}
audio = { playSound = function(_) end }
ns = { menu = { SELECT_SOUND = "select" } }

local function node()
    local result = {visible = true, y = 0, selectedState = false}
    function result:selected() self.selectedState = true end
    function result:unselected() self.selectedState = false end
    function result:show() self.visible = true end
    function result:hide() self.visible = false end
    function result:setPositionY(value) self.y = value end
    return result
end

''' + page_function + r'''

local page1, page2, page3 = node(), node(), node()
local btn1, btn2, btn3 = node(), node(), node()
local layer = {
    pageLayers = {page1, page2, page3},
    pageButtons = {btn1, btn2, btn3}
}

layer:onPageButtonClick(2)
assert(page1.visible == false and page1.y == 10000, "page 1 should hide")
assert(page2.visible == true and page2.y == 0, "page 2 should become visible")
assert(page3.visible == false and page3.y == 10000, "page 3 should hide")
assert(btn1.selectedState == false and btn2.selectedState == true and btn3.selectedState == false,
       "page 2 should be the selected button")

layer:onPageButtonClick(1)
assert(page1.visible == true and page1.y == 0, "page 1 should become visible again")
assert(page2.visible == false and page2.y == 10000, "page 2 should hide again")
assert(btn1.selectedState == true and btn2.selectedState == false,
       "page 1 should become the selected button")

print("Character page switching tests passed.")
'''
subprocess.run(["lua5.1", "-"], input=harness, text=True, check=True)
