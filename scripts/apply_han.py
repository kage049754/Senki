#!/usr/bin/env python3
"""Add Han as a separate playable character using the candidate's tracked Guardian assets."""
from pathlib import Path
import plistlib, re, shutil, sys, xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    raise SystemExit("usage: apply_han.py PATH_TO_GAME")
game = Path(sys.argv[1])
resources = game / "Resources"
source = resources / "Unit/Guardian/Han"
unit = resources / "Unit/Ninja/Han"
for name in ("Han.xml", "Han.plist", "Han.pvr.ccz"):
    p = source / name
    if not p.is_file() or not p.stat().st_size:
        raise SystemExit(f"Required existing Han Guardian asset missing: {p}")
unit.mkdir(parents=True, exist_ok=True)
for name in ("Han.xml", "Han.plist", "Han.pvr.ccz"):
    shutil.copy2(source / name, unit / name)

# Guardian assets have boss-scale HP; make Han a normal selectable fighter.
root = ET.parse(unit / "Han.xml").getroot()
actions = {node.get("name"): node for node in root.findall("action")}
idle = actions.get("Idle")
if idle is None:
    raise SystemExit("Han source package has no Idle action")
hp = idle.find("./data/p[@type='attackValue']")
if hp is None:
    raise SystemExit("Han Idle action has no attackValue stat")
hp.text = "5500"

# Skills 03-05 are empty in the Guardian XML. Keep Han's own skills 01/02 and
# provide working compatibility actions 03-05 from the native Kankuro template.
base = resources / "Unit/Ninja/Kankuro"
base_xml = ET.parse(base / "Kankuro.xml").getroot()
base_actions = {node.get("name"): node for node in base_xml.findall("action")}
base_plist = plistlib.loads((base / "Kankuro.plist").read_bytes())
texture_name = base_plist.get("metadata", {}).get("textureFileName", "Kankuro.pvr.ccz")
texture = base / texture_name
if not texture.is_file():
    texture = next((base / n for n in ("Kankuro.pvr.ccz", "Kankuro.png") if (base / n).is_file()), None)
if texture is None:
    raise SystemExit("Kankuro compatibility atlas texture is missing")
compat_frames = {}
for frame, meta in base_plist.get("frames", {}).items():
    clean = frame[:-4] if frame.endswith(".png") else frame
    if clean.startswith("Kankuro_"):
        compat_frames[re.sub(r"^Kankuro_", "HanCompat_", clean)] = meta
compat_ext = ".pvr.ccz" if texture.name.lower().endswith(".pvr.ccz") else texture.suffix
compat_texture = "Han_Compat" + compat_ext
compat_data = {"frames": compat_frames, "metadata": dict(base_plist.get("metadata", {}))}
compat_data["metadata"]["textureFileName"] = compat_texture
compat_data["metadata"]["realTextureFileName"] = compat_texture
(unit / "Han_Compat.plist").write_bytes(plistlib.dumps(compat_data, fmt=plistlib.FMT_XML, sort_keys=False))
shutil.copy2(texture, unit / compat_texture)

han_actions = {node.get("name"): node for node in root.findall("action")}
for skill_name in ("skill03", "skill04", "skill05"):
    target, template = han_actions.get(skill_name), base_actions.get(skill_name)
    if target is None or template is None:
        raise SystemExit(f"Missing Han/template action {skill_name}")
    target_frame, template_frame = target.find("frame"), template.find("frame")
    if target_frame is None or template_frame is None:
        raise SystemExit(f"Missing frame container for {skill_name}")
    if target_frame.findall("f"):
        continue
    for child in list(template_frame):
        copied = ET.fromstring(ET.tostring(child, encoding="unicode"))
        if copied.tag == "f" and copied.text:
            copied.text = re.sub(r"^Kankuro_", "HanCompat_", copied.text.strip())
        elif copied.tag == "e" and copied.get("type") == "setSound" and copied.text:
            copied.text = re.sub(r"Audio/Kankuro/", "Audio/Han/", copied.text, flags=re.I)
            copied.text = re.sub(r"Kankuro", "Han", copied.text, flags=re.I)
        target_frame.append(copied)
ET.indent(root, space="\t")
(unit / "Han.xml").write_text(ET.tostring(root, encoding="unicode", xml_declaration=True), encoding="utf-8")

# Only copy the fallback clips actually referenced by Han's compatibility skills.
audio = resources / "Audio/Han"
audio.mkdir(parents=True, exist_ok=True)
for clip in ("kankuro_skill3.ogg", "kankuro_skill4.ogg"):
    src = resources / "Audio/Kankuro" / clip
    if not src.is_file():
        raise SystemExit(f"Missing fallback audio for Han: {src}")
    shutil.copy2(src, audio / re.sub(r"^kankuro_", "Han_", clip, flags=re.I))

# Add the separate native class/dispatch; keep the original Guardian implementation.
header = r'''#pragma once
#include "Hero.hpp"

class Han : public Hero
{
    bool transformed = false;

    void perform() override
    {
        _mainTarget = nullptr;
        findHeroHalf();
        if (!_mainTarget)
            findTowerHalf();

        if (_mainTarget)
        {
            Vec2 sp = getDistanceToTarget();
            if (abs(sp.x) > 96 || abs(sp.y) > 24)
            {
                walk(sp.getNormalized());
                return;
            }
            if (isFreeState())
            {
                changeSide(sp);
                if (_isCanSkill1 && !transformed)
                    attack(SKILL1);
                else if (_isCanSkill2)
                    attack(SKILL2);
                else if (_isCanSkill3)
                    attack(SKILL3);
                else if (_isCanSkill4)
                    attack(SKILL4);
                else if (_isCanSkill5)
                    attack(SKILL5);
                else
                    attack(NAttack);
            }
            return;
        }
        checkHealingState();
    }

    void changeAction() override
    {
        if (_skillChangeBuffValue == 17)
        {
            setNAttackValue(getNAttackValue() + 700);
            _originNAttackType = _nAttackType;
            _nAttackType = _spcAttackType2;
            _isArmored = true;
            hasArmorBroken = true;
            setWalkAction(createAnimation(skillSPC1Array, 10, true, false));
            setNAttackAction(createAnimation(skillSPC2Array, 10, false, true));
            setIdleAction(createAnimation(skillSPC3Array, 5, true, false));
            _skillChangeBuffValue = 0;
            transformed = true;
        }
    }

private:
    string _originNAttackType;
};
'''
(game / "Classes/Core/Shinobi/Han.hpp").write_text(header, encoding="utf-8")
enum_path = game / "Classes/Enums/HeroEnum.h"
enum = enum_path.read_text(encoding="utf-8")
if "mk_const(Han);" not in enum:
    anchor = "mk_const(Kankuro);"
    if enum.count(anchor) != 1:
        raise SystemExit("Could not find Kankuro enum anchor for Han")
    enum_path.write_text(enum.replace(anchor, anchor + "\n\tmk_const(Han);", 1), encoding="utf-8")
provider_path = game / "Classes/Core/Provider.hpp"
provider = provider_path.read_text(encoding="utf-8")
if '#include "Shinobi/Han.hpp"' not in provider:
    anchor = '#include "Shinobi/Kankuro.hpp"'
    if provider.count(anchor) != 1:
        raise SystemExit("Could not find Kankuro Provider include for Han")
    provider = provider.replace(anchor, anchor + '\n#include "Shinobi/Han.hpp"', 1)
if 'is("Han")' not in provider:
    match = re.search(r'is\("Kankuro"\)\s*ptr\s*=\s*new Kankuro\(\);', provider)
    if not match:
        raise SystemExit("Could not find Kankuro Provider dispatch for Han")
    provider = provider[:match.end()] + '\n\t\tis("Han")\t\tptr = new Han();' + provider[match.end():]
provider_path.write_text(provider, encoding="utf-8")

basic_path = game / "lua/class/basic.lua"
basic = basic_path.read_text(encoding="utf-8")
if "'Han'" not in basic:
    pos = basic.find("ns.CharactersLayout = {")
    if pos < 0:
        raise SystemExit("Could not locate character roster")
    prefix, roster = basic[:pos], basic[pos:]
    roster, count = re.subn(r"(?<![\w])_None(?![\w])", "'Han'", roster, count=1)
    if count != 1:
        raise SystemExit("No empty roster slot for Han")
    basic_path.write_text(prefix + roster, encoding="utf-8")

def add_table_entry(source, table_name, entry, identity):
    if identity in source:
        return source
    start = source.find(table_name)
    if start < 0:
        raise SystemExit(f"Missing UI table: {table_name}")
    end = source.find("\n}", start)
    if end < 0:
        raise SystemExit(f"Could not locate end of {table_name}")
    body = source[start:end].rstrip()
    if not body.endswith(","):
        body += ","
    return source[:start] + body + "\n    " + entry + source[end:]

select_path = game / "lua/ui/SelectLayer.lua"
select = select_path.read_text(encoding="utf-8")
select = add_table_entry(select, "local selectionAssetAlias = {", "Han = 'Kankuro'", "Han = 'Kankuro'")
select = add_table_entry(select, "local selectionDisplayName = {", "Han = 'Han'", "Han = 'Han'")
select_path.write_text(select, encoding="utf-8")
skill_path = game / "lua/ui/SkillLayer.lua"
skill = skill_path.read_text(encoding="utf-8")
skill = add_table_entry(skill, "local skillUiAlias = {", "Han = 'Kankuro'", "Han = 'Kankuro'")
skill_path.write_text(skill, encoding="utf-8")

# Reuse existing Kankuro UI atlas rectangles for selection and kill/death labels.
for plist_path in resources.glob("*.plist"):
    try:
        ui_data = plistlib.loads(plist_path.read_bytes())
    except Exception:
        continue
    ui_frames = ui_data.get("frames")
    if not isinstance(ui_frames, dict):
        continue
    aliases = {}
    for frame, meta in list(ui_frames.items()):
        if frame.startswith("Kankuro_"):
            aliases.setdefault("Han_" + frame[len("Kankuro_"):], meta)
    if aliases:
        ui_frames.update({k: v for k, v in aliases.items() if k not in ui_frames})
        plist_path.write_bytes(plistlib.dumps(ui_data, fmt=plistlib.FMT_XML, sort_keys=False))

# Verify all animation references and fallback resources before returning.
main = plistlib.loads((unit / "Han.plist").read_bytes())
compat = plistlib.loads((unit / "Han_Compat.plist").read_bytes())
known = set(main.get("frames", {})) | set(compat.get("frames", {}))
missing = {n.text.strip() for n in root.iter("f") if n.text and n.text.strip()} - known
if missing:
    raise SystemExit("Unresolved Han animation frames: " + ", ".join(sorted(missing)[:10]))
for skill_name in ("skill01", "skill02", "skill03", "skill04", "skill05"):
    if not list(han_actions[skill_name].iter("f")):
        raise SystemExit(f"Han has no animation frames for {skill_name}")
print("Added Han with unique Guardian sprite/action data, native class dispatch, transformation handling, and compatible fallback actions for skills 03-05.")
