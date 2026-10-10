#!/usr/bin/env python3
"""Port the Two Sage Toads Choji-replacement mod as an additive playable slot.

The external mod replaces Choji's artwork/resources. This integration preserves
Choji and adds a separate TwoSageToads roster identity using the native Choji
combat/AI implementation as the compatibility baseline.
"""
from pathlib import Path
import plistlib
import re
import shutil
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 3:
    raise SystemExit("usage: apply_two_sage_toads.py PATH_TO_GAME PATH_TO_NarutoSenki1.17Mod")

game, mod = map(Path, sys.argv[1:])
resources = game / "Resources"
source_assets = mod / "assets"
required = [
    source_assets / "Element/Choji/Choji.png",
    source_assets / "Element/Choji/Choji.plist",
    source_assets / "Element/Skills/Choji_Skill.png",
    source_assets / "Element/Skills/Choji_Skill.plist",
]
for path in required:
    if not path.is_file():
        raise SystemExit(f"External Two Sage Toads mod asset missing: {path}")

# Copy the modded character/skill atlases into a new resource package.
unit_dir = resources / "Unit/Ninja/TwoSageToads"
unit_dir.mkdir(parents=True, exist_ok=True)
shutil.copy2(source_assets / "Element/Choji/Choji.png", unit_dir / "TwoSageToads.png")
shutil.copy2(source_assets / "Element/Choji/Choji.plist", unit_dir / "TwoSageToads.plist")
shutil.copy2(source_assets / "Element/Skills/Choji_Skill.png", unit_dir / "TwoSageToads_Skill.png")
shutil.copy2(source_assets / "Element/Skills/Choji_Skill.plist", unit_dir / "TwoSageToads_Skill.plist")

for plist_path in (unit_dir / "TwoSageToads.plist", unit_dir / "TwoSageToads_Skill.plist"):
    data = plistlib.loads(plist_path.read_bytes())
    if "frames" not in data:
        raise SystemExit(f"Atlas has no frames dictionary: {plist_path}")
    renamed = {}
    for frame_name, metadata in data["frames"].items():
        # Legacy atlas keys include .png; V2 animation XML uses extensionless keys.
        name = frame_name[:-4] if frame_name.endswith(".png") else frame_name
        name = name.replace("Choji", "TwoSageToads")
        renamed[name] = metadata
    data["frames"] = renamed
    if "metadata" in data and isinstance(data["metadata"], dict):
        for key, value in list(data["metadata"].items()):
            if isinstance(value, str):
                data["metadata"][key] = value.replace("Choji.png", "TwoSageToads.png").replace("Choji_Skill.png", "TwoSageToads_Skill.png")
    data["metadata"] = data.get("metadata", {})
    data["metadata"]["textureFileName"] = (
        "TwoSageToads_Skill.png" if "Skill" in plist_path.name else "TwoSageToads.png"
    )
    plist_path.write_bytes(plistlib.dumps(data, fmt=plistlib.FMT_XML, sort_keys=False))

# Use the current V2-compatible animation definition, retargeted to the modded atlas.
base_unit = resources / "Unit/Ninja/Choji"
for suffix in (".xml",):
    original = base_unit / ("Choji" + suffix)
    if not original.is_file():
        raise SystemExit(f"V2 animation template missing: {original}")
    text = original.read_text(encoding="utf-8").replace("Choji", "TwoSageToads")
    (unit_dir / ("TwoSageToads" + suffix)).write_text(text, encoding="utf-8")

# Copy existing compatible voice/SFX and overlay any clips supplied by the mod.
audio_dir = resources / "Audio/TwoSageToads"
audio_dir.mkdir(parents=True, exist_ok=True)
base_audio = resources / "Audio/Choji"
if base_audio.is_dir():
    for path in base_audio.iterdir():
        if path.is_file():
            shutil.copy2(path, audio_dir / path.name.replace("Choji", "TwoSageToads").replace("choji", "TwoSageToads"))
external_audio = source_assets / "Audio/Choji"
if external_audio.is_dir():
    for path in external_audio.iterdir():
        if path.is_file():
            shutil.copy2(path, audio_dir / path.name.replace("Choji", "TwoSageToads").replace("choji", "TwoSageToads"))
xml_path = unit_dir / "TwoSageToads.xml"
xml_text = xml_path.read_text(encoding="utf-8")
# If the legacy mod doesn't provide a particular voice clip, use the compatible
# Choji fallback already copied into this package rather than leaving a dead path.
for stem in re.findall(r"Audio/TwoSageToads/([^<]+?\.ogg)", xml_text):
    if not (audio_dir / stem).is_file():
        fallback = stem.replace("TwoSageToads", "Choji")
        if (base_audio / fallback).is_file():
            shutil.copy2(base_audio / fallback, audio_dir / stem)
        else:
            # Keep all audio paths resolvable; use the available combo clip as a last resort.
            fallback_path = audio_dir / "TwoSageToads_combo.ogg"
            if fallback_path.is_file():
                shutil.copy2(fallback_path, audio_dir / stem)

# Add UI-atlas aliases for selection, small portraits, and kill/death feeds. The
# aliases point at existing atlas rectangles; no unrelated fighter artwork is replaced.
for plist_path in resources.glob("*.plist"):
    try:
        data = plistlib.loads(plist_path.read_bytes())
    except Exception:
        continue
    frames = data.get("frames")
    if not isinstance(frames, dict):
        continue
    additions = {}
    for frame_name, metadata in list(frames.items()):
        if frame_name.startswith("Choji_"):
            alias = frame_name.replace("Choji_", "TwoSageToads_", 1)
            additions.setdefault(alias, metadata)
    if additions:
        frames.update({name: meta for name, meta in additions.items() if name not in frames})
        plist_path.write_bytes(plistlib.dumps(data, fmt=plistlib.FMT_XML, sort_keys=False))

# Duplicate the native AI/combat class so the roster ID is not silently rewritten to Choji.
choji_header = game / "Classes/Core/Shinobi/Choji.hpp"
new_header = game / "Classes/Core/Shinobi/TwoSageToads.hpp"
header_text = choji_header.read_text(encoding="utf-8")
header_text = header_text.replace("class Choji :", "class TwoSageToads :")
header_text = header_text.replace("Choji::resumeAction", "TwoSageToads::resumeAction")
if "class TwoSageToads : public Hero" not in header_text:
    raise SystemExit("Could not safely derive TwoSageToads native AI from the Choji class")
new_header.write_text(header_text, encoding="utf-8")

enum_path = game / "Classes/Enums/HeroEnum.h"
enum_text = enum_path.read_text(encoding="utf-8")
if "mk_const(TwoSageToads);" not in enum_text:
    marker = "\tmk_const(Choji);"
    if enum_text.count(marker) != 1:
        raise SystemExit("Could not add TwoSageToads enum next to Choji")
    enum_text = enum_text.replace(marker, marker + "\n\tmk_const(TwoSageToads);", 1)
    enum_path.write_text(enum_text, encoding="utf-8")

provider_path = game / "Classes/Core/Provider.hpp"
provider_text = provider_path.read_text(encoding="utf-8")
if '#include "Shinobi/TwoSageToads.hpp"' not in provider_text:
    marker = '#include "Shinobi/Choji.hpp"'
    if provider_text.count(marker) != 1:
        raise SystemExit("Could not include TwoSageToads class in Provider.hpp")
    provider_text = provider_text.replace(marker, marker + '\n#include "Shinobi/TwoSageToads.hpp"', 1)
if 'is("TwoSageToads")' not in provider_text:
    pattern = r'(\t*is\("Choji"\)\s*ptr = new Choji\(\);)'
    provider_text, count = re.subn(
        pattern,
        lambda match: match.group(1) + '\n\t\tis("TwoSageToads")\t\tptr = new TwoSageToads();',
        provider_text,
        count=1,
    )
    if count != 1:
        raise SystemExit("Could not add TwoSageToads to native Provider dispatch")
provider_path.write_text(provider_text, encoding="utf-8")

# Add to the first genuinely empty roster slot; do not replace an existing fighter.
basic_path = game / "lua/class/basic.lua"
basic_text = basic_path.read_text(encoding="utf-8")
if "'TwoSageToads'" not in basic_text:
    start = basic_text.find("ns.CharactersLayout = {")
    if start < 0:
        raise SystemExit("Could not locate ns.CharactersLayout")
    prefix, roster = basic_text[:start], basic_text[start:]
    roster, count = re.subn(r"(?<![\w])_None(?![\w])", "'TwoSageToads'", roster, count=1)
    if count != 1:
        raise SystemExit("No empty roster slot available for TwoSageToads")
    basic_path.write_text(prefix + roster, encoding="utf-8")

# Use existing selection UI frame art for the button/preview while showing the true name.
select_path = game / "lua/ui/SelectLayer.lua"
select_text = select_path.read_text(encoding="utf-8")
alias_anchor = "    Nagato = 'Pain'\n}"
if "TwoSageToads = 'Choji'" not in select_text:
    if select_text.count(alias_anchor) != 1:
        raise SystemExit("Could not add TwoSageToads to selectionAssetAlias")
    select_text = select_text.replace(alias_anchor, "    Nagato = 'Pain',\n    TwoSageToads = 'Choji'\n}", 1)
display_anchor = "    Nagato = 'Nagato'\n}"
if "TwoSageToads = 'Two Sage Toads'" not in select_text:
    if select_text.count(display_anchor) != 1:
        raise SystemExit("Could not add TwoSageToads to selectionDisplayName")
    select_text = select_text.replace(display_anchor, "    Nagato = 'Nagato',\n    TwoSageToads = 'Two Sage Toads'\n}", 1)
select_path.write_text(select_text, encoding="utf-8")

# Route the selected portrait to the aliased frame and render a true display name.
old_half = "        self._heroHalfImage = display.newSprite(charName .. '_half.png', 10, 10)"
new_half = "        local selectAssetName = selectionAssetAlias[btn._charName] or btn._charName\n        self._heroHalfImage = display.newSprite('#' .. selectAssetName .. '_half.png', 10, 10)"
if old_half in select_text:
    select_text = select_text.replace(old_half, new_half, 1)
elif new_half not in select_text:
    raise SystemExit("Could not route selected character portrait to aliased selection art")
old_name = """        self._heroName = display.newSprite(charName .. '_font.png', 100, 20)
        self._heroName:setAnchorPoint(CCPoint(0.5, 0))
        self:addChild(self._heroName, 5)"""
new_name = """        local displayName = selectionDisplayName[btn._charName]
        if displayName then
            self._heroName = ui.newTTFLabel({
                text = displayName,
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
if old_name in select_text:
    select_text = select_text.replace(old_name, new_name, 1)
elif "local formLabel = selectionDisplayName[btn._charName]" not in select_text:
    raise SystemExit("Could not render external character display name")
select_path.write_text(select_text, encoding="utf-8")

skill_path = game / "lua/ui/SkillLayer.lua"
skill_text = skill_path.read_text(encoding="utf-8")
if "TwoSageToads = 'Choji'" not in skill_text:
    marker = "local skillUiAlias = {"
    pos = skill_text.find(marker)
    if pos < 0:
        raise SystemExit("Missing skillUiAlias; skill UI patch order is incorrect")
    end = skill_text.find("\n}", pos)
    if end < 0:
        raise SystemExit("Could not find end of skillUiAlias")
    prefix = skill_text[:end].rstrip()
    if not prefix.endswith(","):
        prefix += ","
    skill_text = prefix + "\n    TwoSageToads = 'Choji'," + skill_text[end:]
skill_path.write_text(skill_text, encoding="utf-8")

# Basic integrity checks before the Android build.
for path in (
    new_header, unit_dir / "TwoSageToads.xml", unit_dir / "TwoSageToads.plist",
    unit_dir / "TwoSageToads.png", unit_dir / "TwoSageToads_Skill.plist",
    unit_dir / "TwoSageToads_Skill.png",
):
    if not path.is_file() or path.stat().st_size == 0:
        raise SystemExit(f"TwoSageToads package output missing/empty: {path}")
ET.parse(unit_dir / "TwoSageToads.xml")
print("Added Two Sage Toads as a separate roster identity with a native AI class, V2 animation XML, modded atlases, audio fallbacks, selection UI alias, and skill UI alias.")
