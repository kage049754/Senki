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
