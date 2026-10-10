#!/usr/bin/env python3
"""Exercise the actual SelectLayer filter function with lightweight Lua stubs."""

from pathlib import Path
import subprocess
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_character_search.py PATH_TO_SelectLayer.lua")

source = Path(sys.argv[1]).read_text(encoding="utf-8")
start_marker = "function SelectLayer:filterCharacters(query)"
end_marker = "\nfunction SelectLayer:setSelected(btn)"
start = source.find(start_marker)
end = source.find(end_marker, start + len(start_marker))
if start < 0 or end < 0:
    raise SystemExit("Cannot find the exact filter function boundaries in SelectLayer.lua.")

filter_function = source[start:end]
harness = r'''
SelectLayer = {}

function SelectLayer:onPageButtonClick(index)
    self.currentPage = index
    self.pageSwitches = (self.pageSwitches or 0) + 1
end

local function node(fields)
    local result = fields or {}
    function result:setVisible(value)
        self.visible = value
    end
    result.visible = true
    return result
end

''' + filter_function + r'''

local naruto = node({_charName = "Naruto", _pageIndex = 1})
local kabuto = node({_charName = "Kabuto", _pageIndex = 2})
local sakura = node({_charName = "Sakura", _pageIndex = 1})
local emptySlot = node({_charName = "None", _pageIndex = 3})
local page1 = node({})
local page2 = node({})
local page3 = node({})
local cursor = node({})
local emptyLabel = node({})

local layer = {
    selectButtons = {naruto, kabuto, sakura, emptySlot},
    pageButtons = {page1, page2, page3},
    currentPage = 1,
    selectHero = "Naruto",
    _selectImg = cursor,
    searchEmptyLabel = emptyLabel
}

layer:filterCharacters("KABU")
assert(kabuto.visible == true, "case-insensitive match should keep Kabuto visible")
assert(naruto.visible == false and sakura.visible == false, "non-matches should be hidden")
assert(emptySlot.visible == false, "placeholder slots should never appear in search results")
assert(page1.visible == false and page2.visible == true and page3.visible == false,
       "only pages with matches should be visible during a search")
assert(layer.currentPage == 2, "search should navigate to the first matching page")
assert(cursor.visible == false, "cursor should hide when its selected character is filtered out")
assert(emptyLabel.visible == false, "matching query should hide the no-results label")

layer:filterCharacters("nar")
assert(naruto.visible == true and kabuto.visible == false, "second query should update filtering")
assert(layer.currentPage == 1, "search should navigate back to the first matching page")
assert(cursor.visible == true, "cursor should return when the selected character matches again")

layer:filterCharacters("not-a-character")
assert(emptyLabel.visible == true, "empty result should show no-results feedback")
assert(page1.visible == false and page2.visible == false and page3.visible == false,
       "empty result should hide all page buttons")

layer:filterCharacters("")
assert(naruto.visible == true and kabuto.visible == true and sakura.visible == true,
       "clearing query should restore all real characters")
assert(emptySlot.visible == false, "clearing query must not reveal placeholder slots")
assert(page1.visible == true and page2.visible == true and page3.visible == true,
       "clearing query should restore all page buttons")
assert(emptyLabel.visible == false and cursor.visible == true,
       "clearing query should clear empty state and restore selected cursor")

print("Character search/filter behavior tests passed.")
'''
subprocess.run(["lua5.1", "-"], input=harness, text=True, check=True)
