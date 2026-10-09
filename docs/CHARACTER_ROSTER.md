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
