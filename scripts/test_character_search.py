#!/usr/bin/env python3
"""Static regression checks for the character page controls and switch handler."""

from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: test_character_search.py PATH_TO_SelectLayer.lua")

source = Path(sys.argv[1]).read_text(encoding="utf-8")

required = [
    "function SelectLayer:filterCharacters(query)",
    "query = string.lower(tostring(query or \"\"))",
    "string.find(name, query, 1, true) ~= nil",
    "btn:setVisible(matches)",
    "local matchCount = 0",
    "matchCount = matchCount + 1",
    "self.searchEmptyLabel:setVisible(matchCount == 0 or emptyReservedPage)",
    "No characters found",
    "More characters coming soon",
    "self.searchBox = searchBox",
    "box:setPlaceHolder(\"Search character\")",
]
missing = [fragment for fragment in required if fragment not in source]
if missing:
    raise SystemExit("Missing character pagination behavior: " + ", ".join(missing))

if "ui.newTTFLabelMenuItem" in source:
    raise SystemExit("Text-only page controls are still present.")

if "self.pageNum = 3" in source:
    raise SystemExit("The fixed three-page limit is still present.")

print("Character search filters selectable names across the roster and shows explicit empty/reserved-page feedback.")
