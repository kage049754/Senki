#!/usr/bin/env python3
"""Expose already-implemented transformation forms as extra roster entries."""
from pathlib import Path
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: apply_selectable_forms.py PATH_TO_projects/NarutoSenki")

game = Path(sys.argv[1])
basic = game / "lua/class/basic.lua"
select = game / "lua/ui/SelectLayer.lua"
skill = game / "lua/ui/SkillLayer.lua"
for path in (basic, select, skill):
    if not path.is_file():
        raise SystemExit(f"Required candidate source is missing: {path}")

forms = [
    ("SageJiraiya", "Jiraiya", "Sage Jiraiya"),
    ("ImmortalSasuke", "Sasuke", "Immortal Sasuke"),
    ("SageNaruto", "Naruto", "Sage Naruto"),
    ("RikudoNaruto", "Naruto", "Six Paths Naruto"),
    ("RockLee", "Lee", "Rock Lee"),
    ("Nagato", "Pain", "Nagato"),
]

source = basic.read_text(encoding="utf-8")
marker = "-- SENKI_EXTRA_SELECTABLE_FORMS"
if marker not in source:
    old = "    -- },\n}"
    new = """        -- },
    -- SENKI_EXTRA_SELECTABLE_FORMS: expose existing native form implementations.
    -- Page Four: these forms already have enum/class/resource implementations.
        'SageJiraiya', 'ImmortalSasuke', 'SageNaruto', 'RikudoNaruto', --[[ Right ]] 'RockLee', 'Nagato', _None,
        _None, _None, _None, _None, --[[ Right ]] _None, _None, _None,
        _None, _None, _None, _None, --[[ Right ]] _None, _None, _None,
}"""
    if source.count(old) != 1:
        raise SystemExit(f"Could not append page four safely: expected one list terminator, found {source.count(old)}")
    source = source.replace(old, new, 1)
    basic.write_text(source, encoding="utf-8")

source = select.read_text(encoding="utf-8")
alias_marker = "local selectionAssetAlias = {"
if alias_marker not in source:
    old = "function SelectLayer:init()\n"
    new = """-- Forms reuse their base character's small selection button; the dedicated
-- *_half.png portrait frames remain form-specific in Select.plist.
local selectionAssetAlias = {
    SageJiraiya = 'Jiraiya',
    ImmortalSasuke = 'Sasuke',
    SageNaruto = 'Naruto',
    RikudoNaruto = 'Naruto',
    RockLee = 'Lee',
    Nagato = 'Pain'
}
local selectionDisplayName = {
    SageJiraiya = 'Sage Jiraiya',
    ImmortalSasuke = 'Immortal Sasuke',
    SageNaruto = 'Sage Naruto',
    RikudoNaruto = 'Six Paths Naruto',
    RockLee = 'Rock Lee',
    Nagato = 'Nagato'
}

function SelectLayer:init()
"""
    if source.count(old) != 1:
        raise SystemExit("Could not add form-selection asset aliases")
    source = source.replace(old, new, 1)

old = "        local select_btn = SelectButton:create(charName .. '_select.png')"
new = "        local selectAssetName = selectionAssetAlias[charName] or charName\n        local select_btn = SelectButton:create(selectAssetName .. '_select.png')"
if old in source:
    source = source.replace(old, new, 1)
elif new not in source:
    raise SystemExit("Could not map form selection buttons to existing base art")

old = """        self._heroName:removeFromParent()
        self._heroName = display.newSprite(charName .. '_font.png', 100, 20)
        self._heroName:setAnchorPoint(CCPoint(0.5, 0))
        self:addChild(self._heroName, 5)"""
new = """        self._heroName:removeFromParent()
        local formLabel = selectionDisplayName[btn._charName]
        if formLabel then
            self._heroName = ui.newTTFLabel({
                text = formLabel,
                font = ui.DEFAULT_TTF_FONT,
                size = 16,
                color = ccc3(255, 255, 255)
            })
            self._heroName:setPosition(100, 20)
        else
            self._heroName = display.newSprite(charName .. '_font.png', 100, 20)
        end
        self._heroName:setAnchorPoint(CCPoint(0.5, 0))
        self:addChild(self._heroName, 5)"""
if old in source:
    source = source.replace(old, new, 1)
elif new not in source:
    raise SystemExit("Could not add readable form display names")
select.write_text(source, encoding="utf-8")

source = skill.read_text(encoding="utf-8")
alias_marker = "local skillUiAlias = {"
if alias_marker not in source:
    old = "local transformList = {"
    new = """-- These native forms have their own combat resources, but share the base
-- character's small skill icons/full-screen selection art. Their description
-- labels may not exist, so SkillLayer's visible fallback handles that case.
local skillUiAlias = {
    SageJiraiya = 'Jiraiya',
    ImmortalSasuke = 'Sasuke',
    SageNaruto = 'Naruto',
    RikudoNaruto = 'Naruto',
    RockLee = 'Lee',
    Nagato = 'Pain'
}

local transformList = {"""
    if source.count(old) != 1:
        raise SystemExit("Could not add skill UI aliases")
    source = source.replace(old, new, 1)

old = """    for i = 1, 5 do
        local skill_btn = SelectButton:create(
                              self.selectHero .. '_skill' .. i .. '.png')"""
new = """    local skillHero = skillUiAlias[self.selectHero] or self.selectHero
    for i = 1, 5 do
        local skill_btn = SelectButton:create(
                              skillHero .. '_skill' .. i .. '.png')"""
if old in source:
    source = source.replace(old, new, 1)
elif new not in source:
    raise SystemExit("Could not map form skill icons to base character icons")

old = """    local imgPath
    if table.has(useFull2ImageList, self.selectHero) and winNum >= 100 then
        imgPath = '#' .. self.selectHero .. '_full2.png'
    else
        imgPath = '#' .. self.selectHero .. '_full.png'
    end"""
new = """    local fullArtHero = skillUiAlias[self.selectHero] or self.selectHero
    local imgPath
    if table.has(useFull2ImageList, fullArtHero) and winNum >= 100 then
        imgPath = '#' .. fullArtHero .. '_full2.png'
    else
        imgPath = '#' .. fullArtHero .. '_full.png'
    end"""
if old in source:
    source = source.replace(old, new, 1)
elif new not in source:
    raise SystemExit("Could not map form skill-screen portrait to existing base art")
skill.write_text(source, encoding="utf-8")
print("Added six existing native forms to page four and mapped their selection/skill UI to existing compatible art.")
