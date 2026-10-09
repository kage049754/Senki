# Senki Mod-Merging Roadmap

**Project rule: mod and merge existing Naruto Senki projects only. Do not create a new game.** The user-selected target is Naruto Senki: V2, with the v2.1.6-fix release as reference. See docs/BASE_GAME.md. This roadmap supersedes older greenfield plans.

## Phase 0 — Audit and freeze conflicting work
**Status: In progress**

- [x] Clarify in README that Senki is a mod-merging workspace.
- [x] Make no-new-game rule explicit in AI instructions.
- [ ] Inspect current Kotlin/Canvas prototype and classify it as temporary tooling/prototype, not the target foundation.
- [x] Audit the V2 source candidate's real editable source structure, engine/version, Android Gradle configuration, and fork history.
- [x] Record build compatibility risks and unresolved code/asset permission status.
- [ ] Record the evidence and unknowns for each candidate in `docs/MOD_RESEARCH.md`.

**Exit checks:** current repo state and all candidates are honestly documented; no further new-game systems are added while base selection is unresolved.

## Phase 1 — Verify and import the selected Naruto Senki V2 base
**Status: In progress — target selected, source import not verified**

- [x] Record the user's selected game target: Naruto Senki: V2, release reference v2.1.6-fix.
- [x] Inspect an editable V2 source candidate and verify its C++/Lua/Cocos2d-x structure and Android Gradle project.
- [x] Inspect legacy Android Gradle/SDK/NDK configuration; see docs/V2_BUILD_AUDIT.md.
- [ ] Verify it matches/is compatible with the selected release. The release host contains packaged binaries, not editable source.
- [ ] Resolve code and separate asset permissions, or obtain a source distribution with clear reuse terms.
- [ ] Test actual source buildability in a suitable environment after permission is resolved.
- [ ] Compare source candidates against engine compatibility, code/resource completeness, mod support, and maintenance.
- [ ] Check code licenses and separate asset/content permissions.
- [x] Record the user-selected existing game as the intended foundation.
- [ ] Verify source repository, exact revision, and rights before importing it.
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


### Updated base-research decision (2026-10-10)
The selected game remains Naruto Senki V2. New audits found two V2-derived Android source candidates with their own successful CI artifacts: `Wilykun/NarutoSenki-V2` (Spectate mode/build fixes) and `muhammadadilsyaputra08-alt/NarutoSenki-Custom` (Android-only source snapshot). Both currently lack a declared license and cleared asset permissions, so neither has been imported. Older Cocos2d-x 2.2.2 repositories were classified as reference-only rather than interchangeable bases.

**Current gate:** finish source/provenance comparison and obtain appropriate permission for code and bundled assets. Then choose exactly one base, bring up its build in this central repo, verify the APK, and only then start merging additional mods. The existing prototype CI remains unrelated to the target game.

## User-prioritized personal modding workflow — added 2026-10-10
The user has explicitly directed us to keep searching for Senki characters, skills, animations, effects, stages, UI, and other useful components even when source repositories do not expressly grant reuse permission, because the current goal is personal-use development/testing. Missing license metadata is not a reason to stop research or private build-feasibility tests.

1. Search GitHub forks, mod repositories, release archives, mirrors, and other publicly accessible sources for complete Senki/V2 builds and individual mod features.
2. Record each candidate's URL, revision/version, Android project structure, engine/toolchain, features, and actual build evidence.
3. Prefer complete, buildable Android V2-derived sources; compare them before selecting a base.
4. Test candidates in isolated workspaces first; do not let an unverified mod break the central project.
5. Integrate the selected game and compatible components incrementally; build and inspect logs after each change.
6. Continue the fail → inspect actual logs → fix → commit → rerun → verify loop until CI build succeeds, then separately verify installation and gameplay on the user's phone.
7. Keep provenance notes so source and assets can be traced. Do not make unsupported claims about licenses or redistribution rights. Public release is not the current milestone; a working personal test build is.

Current evidence: central diagnostic run 37965165366 succeeded in compiling the pinned muhammadadilsyaputra08-alt/NarutoSenki-Custom candidate in a temporary runner workspace. Its APK was not uploaded and the source is not yet integrated into the central repository. This is build-feasibility evidence, not a device test.
