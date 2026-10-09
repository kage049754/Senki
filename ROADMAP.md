# Senki Mod-Merging Roadmap

**Project rule: mod and merge existing Naruto Senki projects only. Do not create a new game.** This roadmap supersedes older plans that treated this repository as a greenfield game-development project.

## Phase 0 — Audit and freeze conflicting work
**Status: In progress**

- [x] Clarify in README that Senki is a mod-merging workspace.
- [x] Make no-new-game rule explicit in AI instructions.
- [ ] Inspect current Kotlin/Canvas prototype and classify it as temporary tooling/prototype, not the target foundation.
- [ ] Audit candidate Senki source repositories and identify real editable source, engine/version, buildability, forks, and rights.
- [ ] Record the evidence and unknowns for each candidate in `docs/MOD_RESEARCH.md`.

**Exit checks:** current repo state and all candidates are honestly documented; no further new-game systems are added while base selection is unresolved.

## Phase 1 — Select one existing Senki base
**Status: Not started**

- [ ] Compare the strongest existing source candidates against Android buildability, engine compatibility, code/resource completeness, mod support, and maintenance.
- [ ] Check code licenses and separate asset/content permissions.
- [ ] Select one existing game as the foundation; document why it was selected and what cannot be reused.
- [ ] Decide what to do with the current prototype scaffold only after the base decision; do not mistake it for the final game.

**Exit checks:** one existing Senki source base is selected with evidence, build instructions, known blockers, and documented permission status.

## Phase 2 — Establish the chosen base in the central repository
**Status: Not started**

- [ ] Bring or adapt the chosen base into `kage049754/Senki` using a documented, provenance-preserving method.
- [ ] Preserve original engine/game loop and existing behavior wherever practical.
- [ ] Resolve dependencies and Android build issues without replacing the engine with a new implementation.
- [ ] Establish CI for the chosen base and verify its actual APK artifact.
- [ ] Confirm install/launch separately on a device when possible.

**Exit checks:** the selected existing Senki game builds and launches from the central repo before major mod merges begin.

## Phase 3 — Inventory and prepare mod content
**Status: Not started**

- [ ] Continue researching existing Senki mods, source forks, release histories, and compatible resources.
- [ ] Compare forks to upstream and identify meaningful changes.
- [ ] Inventory characters/forms, skills, animation states, effects, summons, maps, UI changes, balance edits, and bug fixes.
- [ ] Record exact paths, source links, license/permission, compatibility, and whether content is source-editable or APK-only.
- [ ] Deduplicate content and resolve conflicting IDs/names.
- [ ] Exclude content whose reuse rights are absent or unclear.

**Exit checks:** each planned merge has source evidence, a compatibility plan, and a permission/provenance decision.

## Phase 4 — Merge in verified batches
**Status: Not started**

- [ ] Port compatible changes into the chosen game's existing architecture.
- [ ] Integrate content in small batches with clear commit messages and attribution.
- [ ] Preserve existing engine, input, combat, minions, towers, menus, and save/config behavior unless a specific merge requires changes.
- [ ] Resolve collisions in IDs, resources, scripts, animations, dependencies, and balance.
- [ ] Build and test each batch; verify affected characters and skills in actual gameplay.
- [ ] Track imported, adapted, built, and device-tested content separately.

**Exit checks:** each integrated batch builds, launches, and passes the relevant gameplay checks; no unverified merge is labelled complete.

## Phase 5 — Unified roster and polish
**Status: Not started**

- [ ] Expand the chosen base's roster using compatible and permitted mod content.
- [ ] Keep the roster expandable beyond 70 where feasible, without replacing the existing game engine just to meet a number.
- [ ] Test character selection, skills, animations, hitboxes, effects, AI, death/respawn, and balance.
- [ ] Fix merge-related crashes, missing resources, blank screens, and UI conflicts.
- [ ] Retain the selected base's core gameplay identity.

**Exit checks:** the merged roster and content work together in one game; only individually tested characters are counted as playable.

## Phase 6 — Final build and verification
**Status: Not started**

- [ ] Inspect latest Actions run and fix real failures through the log-driven loop in AGENTS.md.
- [ ] Confirm final workflow completed successfully.
- [ ] Verify the exact APK artifact and record the run/artifact link.
- [ ] Install and test the unified APK on a physical Android device when possible.
- [ ] Document remaining compatibility issues and release notes.

**Exit checks:** one verified unified mod APK; CI and physical-device results are reported separately.

## Rules that override older plans

- Do not create a new game or replacement engine.
- Do not add new-game features to the Kotlin/Canvas prototype while the existing base is unresolved.
- Do not assume a candidate source or its assets are reusable without evidence.
- Do not merge whole APKs/repositories blindly.
- Do not call a source “merged” until the unified build and relevant gameplay have been tested.
- Do not claim success without a completed CI result and confirmed artifact.
