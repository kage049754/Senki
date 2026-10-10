# Senki Modded Roster and Verification Tracker

> **This tracker is for content merged into one selected existing Naruto Senki base. Do not create a new game or replacement roster engine. First select the base, then record compatible mod content ported into its native systems.**

## Purpose
Track character discovery, implementation, rights review, and gameplay verification separately. The chosen game's existing roster may be expanded toward 70+ verified playable characters where feasible. Extend its native systems only as needed; roster size is not a reason to build a new engine.

## Status definitions
- DISCOVERED — a name or implementation lead has been found.
- RIGHTS_REVIEW — code/asset permission needs review.
- RESOURCE_REVIEW — source files and resource formats are being inspected.
- PLANNED — intended for the game, not implemented.
- IN_PROGRESS — implementation is underway.
- IMPLEMENTED — code/resources exist, but full testing is incomplete.
- TESTING — required tests are in progress.
- VERIFIED — required tests pass and provenance/permissions are recorded.
- BLOCKED — permission, resource, or technical blocker.
- EXCLUDED — not included in this project.

## Count rules
Always report separate counts for discovered leads, planned characters, implemented characters, characters in testing, verified playable characters, and blocked/excluded entries.

Do not count planned characters, portraits, untested entries, synthetic test entries, or duplicate variants as verified playable characters.

Target: at least 70 verified playable characters. The registry itself must not have a hardcoded upper limit.

## Character entry template
- Unique character ID:
- Display name:
- Form/variant:
- Source repository or original design:
- Source commit/version:
- Source category: original / licensed / permission-approved / reference-only
- Code license status:
- Asset permission status:
- Portrait:
- Animation set:
- Basic attack:
- Skills:
- Ultimate/transformation:
- Stats and balance:
- AI profile:
- Selection test:
- Battle spawn test:
- Skill tests:
- Death/respawn test:
- Performance/resource test:
- Status:
- Evidence/notes:
- Next action:

## Current verified roster
**Verified playable character count: NOT YET MEASURED.**

**Source inventory (not runtime-verified):** the pinned Android-clean candidate defines 37 unique selectable names in `lua/class/basic.lua`. The five Pain-path C++ headers are implementation classes, not separate selectable roster entries. See `docs/MOD_RESEARCH.md` for the exact 37-name list and source comparison.

No individual character is marked VERIFIED by this initial tracker. Populate entries only after inspecting the actual project and testing the character.

## Batch verification checklist
- [ ] IDs are unique and stable.
- [ ] Required assets and permission records exist.
- [ ] Character appears in the dynamic catalog.
- [ ] Search/filter/scrolling can find it.
- [ ] Selection spawns the intended character.
- [ ] Movement and facing work.
- [ ] Basic attack works.
- [ ] Every declared skill works.
- [ ] Cooldowns and damage are correct.
- [ ] Animation transitions work.
- [ ] Death and respawn work.
- [ ] AI behavior works when applicable.
- [ ] Resources load and release safely.
- [ ] No blocking crash remains.
- [ ] Status and evidence are recorded.

## Historical/possible character leads
Names mentioned in source release notes or mod descriptions belong in research records first. They must not be treated as implemented until individually ported and verified. Refer to docs/MOD_RESEARCH.md for sources and evidence.


## Source baseline inventory — 2026-10-10

- [x] Inspected `lua/class/basic.lua` in Android-clean candidate commit `279e85e73040558c84988a0eea310b6286eb77f0`.
- [x] Counted 37 unique selectable character names in `ns.CharactersLayout`.
- [x] Inspected the C++ `Classes/Core/Shinobi/` folder: 42 headers total, five of which are Pain-path implementation classes rather than standalone selectable characters.
- [x] Identified Kabuto as a custom redesigned character unique to the Android-clean candidate compared with the LAN-enhanced candidate.
- [ ] Test each selectable character in battle before counting it as verified playable.
- [ ] Audit every character's class, XML/config, sprite/plist, animation/effects/audio, skill IDs, and selection portrait/button assets.


## Selection scalability patch status — 2026-10-10

- [x] Central patch `patches/android-clean/0008-dynamic-roster-pagination.patch` removes the fixed three-page cap and derives pages from the actual layout list.
- [x] CI build `38016671857` passed Lua syntax checks and produced artifact `11655938596`.
- [ ] No new character has been added by this patch. Current source-level selectable count remains 37; verified playable count remains unmeasured.
- [ ] After device validation, begin adding compatible characters in small batches with all portrait/button/XML/sprite/plist/audio/skill references audited.


## Additional discovered mod character leads — 2026-10-10

These are **DISCOVERED / RESOURCE_REVIEW leads only** from release notes, not integrated characters. The release source and exact asset files are not yet mapped to V2.

| Character or form | Discovery source | Current status | Next action |
|---|---|---|---|
| Shizune | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources; check offline compatibility |
| Hashirama | NarutoSenki v1.26 beta 1 and FDPL v1.22 notes | DISCOVERED / APK-only lead | Find source/asset lineage; compare skill kit |
| Rin | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Sakon & Ukon | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Determine whether implemented as one selectable slot or linked forms |
| Juzo | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Kurenai | NarutoSenki v1.25 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Might Guy | NarutoSenki v1.25 beta 1 and FDPL v1.22 notes | DISCOVERED / APK-only lead | Find source/resources; do not overwrite Tenten in the unified roster |
| Yamato | NarutoSenki v1.25 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Sasori (awakened form) | NarutoSenki v1.26 beta 1/2 release notes | DISCOVERED / form/skill lead | Identify separate form vs shared character implementation |
| Zetsu | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Iruka | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Third Kazekage | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / AI lead | Determine whether selectable and find implementation |
| Jirobo | NarutoSenki v1.24 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Tayuya | NarutoSenki v1.24 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Anko (including revised skin) | NarutoSenki v1.24 beta 1 and v1.24 beta 2 release notes | DISCOVERED / form/skill lead | Find editable class/resources |
| White Mask Tobi | FDPL v1.22 third-party mod listing | DISCOVERED / replacement-based lead | Seek additive implementation so existing Tobi is preserved |
| Pain (alternate implementation) | FDPL v1.22 third-party mod listing | DISCOVERED / replacement-based lead | Compare against existing Pain; avoid losing base character |

Source inventory links and compatibility notes are recorded in docs/MOD_RESEARCH.md. Do not count these as planned/implemented/verified until the exact source files, resources, and integration tests are available.


## Latest pagination acceptance status — 2026-10-10

- [x] Dynamic page count and image-based pagination patch passed central CI build [run 38020781870](https://github.com/kage049754/Senki/actions/runs/38020781870).
- [x] Pages 1–3 retain their original image controls; pages 4+ use generated normal/selected image states styled from the original page-button art. CI confirms page 4/5 image assets are packaged and the retired custom menu/selection backgrounds are absent.
- [ ] Device-test the visual match, page navigation, original page 1–3 controls, preview/tap-again confirmation, and character spawn behavior.
- The source-level roster remains 37 selectable names. Verified playable count remains unmeasured; pagination does not add characters.


## Required per-character asset and AI manifest

Add this manifest to every planned or integrated character entry. Fill in exact paths/references; do not use a generic “assets complete” statement.

- Selection display name and stable character/form ID:
- Selection portrait/avatar path:
- Selection button/thumbnail normal + selected assets:
- Selection preview art/model/sprite path and preview test:
- Skill viewer: skill names / icons / descriptions / order / cooldown-cost fields:
- Main sprite/model and atlas/texture/plist paths:
- Animation states: idle / move / attack / cast-skill / hit / knockback / death / transform / other:
- Voice clips/voice lines (paths, triggers, or documented not-applicable reason):
- Attack/skill/hit/summon/transformation sound effects (paths and event references):
- Per-skill logic, projectile/summon, effects, hitbox, damage, cooldown, costs:
- Character class/script/XML/config and all referenced resource paths:
- Player selection/control tests:
- AI roster/selection/spawn registration path:
- AI behavior tests (move, basic attack, each skill, range/state/cooldown, summon/transform):
- Resource manifest state per category: FOUND / ADAPTED / CREATED / NOT APPLICABLE / MISSING / BLOCKED:
- Source commit/version and provenance/permission record:
- Missing items and completion impact:
- Test evidence and status:

### Full-completion checklist (all applicable items required)
- [ ] Correct display name, unique ID, selection avatar/portrait, button states, and preview.
- [ ] Skill viewer correctly shows every actual skill's name, icon, and description.
- [ ] All required sprite/model, atlas/plist, and animation states are present and load.
- [ ] Voice clips/voice lines are inventoried; supplied/required clips play at the correct events, or absence is explicitly documented and classified.
- [ ] Skill, attack, hit, summon, transformation audio and visual effects map to the intended actions.
- [ ] Player selection, movement, basic attack, every skill, hit detection/damage, cooldowns, and death/respawn work.
- [ ] Existing game AI can select/spawn this character in supported modes and use its valid attacks/skills without resource errors.
- [ ] All resource/config references resolve and IDs do not collide with existing fighters.
- [ ] Manifest, provenance, missing assets, and runtime evidence are recorded.

A character with missing required assets or unverified AI remains partial/incomplete/blocked. Do not count it as VERIFIED based on its name, portrait, a successful build, or player-only selection. The current 37 roster names are only source-level selectable entries; the number with complete asset packages and verified AI is not yet measured.

## Full character package: required per-entry audit

For each discovered or integrated character, complete these fields in the roster entry or its linked manifest:

- Stable character/form ID and exact source URL, branch/commit/version.
- Display name; selection portrait/avatar; normal/selected selection button art; preview resource and preview test.
- Skill-view entries: skill names, icons, descriptions, IDs and link to the actual implementation.
- In-game sprite/model; texture/atlas/plist; animation states and frame references.
- Basic attacks, hitboxes/range/timing, damage, cooldowns, passive/active/ultimate abilities supported by the source, projectiles/summons/status effects/VFX.
- Voice lines/clips, file paths, and the events that trigger them.
- Attack/skill/ultimate/hit/death/summon/transformation SFX, file paths and event triggers.
- Player input/selection test and the character actually spawned in battle.
- Game AI registration/selection/spawn path; AI tests for movement, basic attacks, range/state/cooldowns and each supported skill/summon/transform.
- Resource/config integrity, duplicate-ID check, APK packaging check, in-game test results and explicit missing/not-applicable reasons.
- Source/license/permission status for code, art, animation, voice, SFX and effects.

A field may be marked missing/not-applicable only with a brief reason. Do not treat a missing voice pack or unavailable skill as complete. A fighter is not PLAYABLE-VERIFIED until the intended character spawns correctly, the skill UI maps to working skills, applicable assets/audio resolve, and supported AI behavior passes. Build checks and source-level roster names are separate from gameplay verification.
