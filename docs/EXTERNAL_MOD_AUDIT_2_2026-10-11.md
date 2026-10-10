# External Mod Audit 2 — 2026-10-11

## Mod inspected: Wilykun/NarutoSenki-V2

Repository: https://github.com/Wilykun/NarutoSenki-V2  
README: https://github.com/Wilykun/NarutoSenki-V2/blob/master/README.md  
Changelog: https://github.com/Wilykun/NarutoSenki-V2/blob/master/CHANGELOG.md  
Latest release linked by its README: v1.2.0; changelog also documents v1.2.1.

### What this mod actually changes

The README explicitly describes it as a fork of `hitlabmodv2/NarutoSenki-V2`. Its listed additions are:
- AI-vs-AI spectate mode with 1v1 through 5v5 configurations;
- new menu/selection backgrounds;
- Indonesian-language UI;
- developer/contact button and build fixes.

The inspected changelog does **not** list a new character or a new playable character moveset. Its stated focus is modes, backgrounds, language, and build reliability.

### Character audit result

- Distinct new character leads from this mod: **0 identified**.
- New independently selectable/playable characters verified: **0**.
- Transfer candidates: **none from the inspected README/changelog evidence**.
- Decision: **DO NOT port as a character source**. It may be useful later as a reference for spectate mode, UI, or build fixes, but those are outside the current external-character priority.

This is a negative result, not proof that no unmentioned changes exist in its full source tree. The fork relationship and changelog provide no evidence of a distinct character implementation, so it must not be counted as a character mod.

## Next source inspected: LeaderOnePro/NarutoSenki (legacy Cocos2d-x 2.2.2)

Repository: https://github.com/LeaderOnePro/NarutoSenki  
Source listing: https://github.com/LeaderOnePro/NarutoSenki

The repository README identifies this as an older Cocos2d-x 2.2.2 project associated with “超战记 (original Naruto Senki EX)” and a Visual Studio 2010 setup. It is not the same proven Android-clean V2 base.

A code search found a `Kimimaro_ougis.mp3` audio reference in `Resources/Audio/list.xml`, but this is **audio-only evidence**. No matching independently selectable character class, roster entry, sprite/animation set, skills, or AI/control implementation was confirmed by this search. Therefore:

- Kimimaro: **LEAD ONLY — not verified playable/selectable in this source**.
- Transfer eligibility: **not qualified** until a full character implementation is located.
- Other distinct external characters: **none qualified by this pass**.

Do not add Kimimaro using only the audio reference or a renamed existing fighter. Next research should inspect the legacy repository's character classes and resource tree using exact paths, then compare its architecture/character IDs against the target before selecting a port candidate.

## Current project decision

Neither source in this audit produced a verified new character ready to transfer. The correct next step is continued source discovery—not a placeholder integration. The target remains https://github.com/kage049754/Senki, and no new playable character is claimed as added by this audit.
