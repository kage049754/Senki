#!/usr/bin/env python3
"""Apply the source-controlled character-search enhancement to the pinned V2 source."""

from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: apply_character_search.py PATH_TO_SelectLayer.lua")

target = Path(sys.argv[1])
source = target.read_text(encoding="utf-8")

if "function SelectLayer:filterCharacters(query)" in source:
    print("Character search/filter already present; leaving file unchanged.")
    raise SystemExit(0)


def replace_once(old: str, new: str, label: str) -> None:
    global source
    count = source.count(old)
    if count != 1:
        raise SystemExit(f"Cannot apply character-search change '{label}': expected 1 match, found {count}.")
    source = source.replace(old, new, 1)


replace_once(
    "    local charactersList = ns.CharactersLayout or {}\\n"
    "    -- Keep page 5 reachable for the planned 70+ distinct-character roster.\\n"
    "    -- It may be empty until a verified character batch is added there.\\n"
    "    self.pageNum = math.max(5, math.ceil(#charactersList / 21))\\n",
    "    local charactersList = ns.CharactersLayout or {}\\n"
    "    -- Keep page 5 reachable for the planned 70+ distinct-character roster.\\n"
    "    -- It may be empty until a verified character batch is added there.\\n"
    "    self.pageNum = math.max(5, math.ceil(#charactersList / 21))\\n"
    "    self.currentPage = 1\\n",
    "initialize current page",
)

replace_once(
    "        select_btn._charName = charName\n",
    "        select_btn._charName = charName\n"
    "        select_btn._pageIndex = Page + 1\n",
    "remember each character's page",
)

replace_once(
    "    self.selectButtons = selectButtons\n"
    "    self.selectNameList = selectNameList\n"
    "    self:setSelectList(table.toCCArray(selectNameList))\n",
    "    self.selectButtons = selectButtons\n"
    "    self.selectNameList = selectNameList\n"
    "    self:setSelectList(table.toCCArray(selectNameList))\n"
    "\n"
    "    local function onCharacterSearch(event, editbox)\n"
    "        if event == \"changed\" or event == \"return\" then\n"
    "            self:filterCharacters(editbox:getText())\n"
    "        end\n"
    "    end\n"
    "    local searchOk, searchBox = pcall(function()\n"
    "        local box = ui.newEditBox({\n"
    "            image = '#status_bar_bg.png',\n"
    "            imagePressed = '#status_bar_bg.png',\n"
    "            imageDisabled = '#status_bar_bg.png',\n"
    "            size = CCSizeMake(156, 30),\n"
    "            x = width - 145,\n"
    "            y = height - 26,\n"
    "            listener = onCharacterSearch\n"
    "        })\n"
    "        if box then\n"
    "            box:setPlaceHolder(\"Search character\")\n"
    "            box:setFontSize(12)\n"
    "            box:setFontColor(ccc3(255, 255, 255))\n"
    "        end\n"
    "        return box\n"
    "    end)\n"
    "    if searchOk and searchBox then\n"
    "        self.searchBox = searchBox\n"
    "        self:addChild(searchBox, 20)\n"
    "    end\n"
    "\n"
    "    self.searchEmptyLabel = ui.newTTFLabel({\n"
    "        text = \"No characters found\",\n"
    "        font = ui.DEFAULT_TTF_FONT,\n"
    "        size = 20,\n"
    "        color = ccc3(255, 255, 255)\n"
    "    })\n"
    "    self.searchEmptyLabel:setPosition(width / 2, height / 2)\n"
    "    self.searchEmptyLabel:setVisible(false)\n"
    "    self:addChild(self.searchEmptyLabel, 100)\n",
    "add search box and no-results label",
)

replace_once(
    "function SelectLayer:onPageButtonClick(index)\n"
    "    audio.playSound(ns.menu.SELECT_SOUND)\n",
    "function SelectLayer:onPageButtonClick(index)\n"
    "    self.currentPage = index\n"
    "    audio.playSound(ns.menu.SELECT_SOUND)\n",
    "track manually selected page",
)

replace_once(
    "function SelectLayer:setSelected(btn)\n",
    "function SelectLayer:filterCharacters(query)\n"
    "    query = string.lower(tostring(query or \"\"))\n"
    "    query = string.gsub(query, \"^%s*(.-)%s*$\", \"%1\")\n"
    "\n"
    "    local pageHasMatches = {}\n"
    "    local firstPage = nil\n"
    "    local selectedVisible = false\n"
    "    local matchCount = 0\n"
    "\n"
    "    for _, btn in ipairs(self.selectButtons or {}) do\n"
    "        local name = string.lower(tostring(btn._charName or \"\"))\n"
    "        local isPlaceholder = name == \"none\" or name == \"_none\"\n"
    "        local matches = not isPlaceholder and\n"
    "                        (query == \"\" or string.find(name, query, 1, true) ~= nil)\n"
    "        btn:setVisible(matches)\n"
    "        if matches then\n"
    "            if btn._charName == self.selectHero then selectedVisible = true end\n"
    "            local page = btn._pageIndex or 1\n"
    "            pageHasMatches[page] = true\n"
    "            firstPage = firstPage or page\n"
    "            matchCount = matchCount + 1\n"
    "        end\n"
    "    end\n"
    "\n"
    "    if self._selectImg then\n"
    "        self._selectImg:setVisible(selectedVisible)\n"
    "    end\n"
    "\n"
    "    for i, pageBtn in ipairs(self.pageButtons or {}) do\n"
    "        pageBtn:setVisible(query == \"\" or pageHasMatches[i] == true)\n"
    "    end\n"
    "\n"
    "    if self.searchEmptyLabel then\n"
    "        self.searchEmptyLabel:setVisible(matchCount == 0)\n"
    "    end\n"
    "\n"
    "    if firstPage and firstPage ~= self.currentPage then\n"
    "        self.currentPage = firstPage\n"
    "        self:onPageButtonClick(firstPage)\n"
    "    end\n"
    "end\n"
    "\n"
    "function SelectLayer:setSelected(btn)\n",
    "add cross-page character filtering",
)

replace_once(
    "    if self._selectImg then\n        self._selectImg:setPosition(",
    "    if self._selectImg then\n        self._selectImg:setVisible(true)\n        self._selectImg:setPosition(",
    "restore selection cursor after filtering",
)

target.write_text(source, encoding="utf-8")
print(f"Applied character search/filter to {target}")
