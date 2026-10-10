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
**Status: In progress — the patched V2-derived source builds in central CI from a pinned temporary clone; full source vendoring and phone validation remain open.**

- [ ] Bring or adapt the chosen base into `kage049754/Senki` using a documented, provenance-preserving method.
- [ ] Preserve original engine/game loop and existing behavior wherever practical.
- [ ] Resolve dependencies and Android build issues without replacing the engine with a new implementation.
- [x] Establish central CI for the pinned Android-clean V2-derived candidate and verify its actual patched APK artifact (run 38015483353).
- [ ] Vendor or otherwise preserve a reproducible, editable copy of the chosen source tree inside this repository; the current workflow still clones it into a temporary runner workspace.
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


## Current base-selection evidence (2026-10-10)
Two source candidates now have successful central CI APK artifacts. The lead candidate for the requested offline-first Android mod is the Android-clean V2-derived source at `muhammadadilsyaputra08-alt/NarutoSenki-Custom@279e85e73040558c84988a0eea310b6286eb77f0`. A recursive tree comparison found it uniquely contains a redesigned Kabuto character, clone logic, sprites, audio, and projectile data that are absent from the LAN-enhanced branch. It also avoids hundreds of desktop-only paths. The LAN-enhanced candidate at `sansaks-jpg/NarutoSenki-V2@1751b7fb8f05a96ff6e85bc8a6c8e3fdcca3f74a` is valuable for selective crash fixes and optional networking, but should not replace the lead base wholesale.

Next implementation sequence:
1. Keep the Android-clean candidate as the provisional lead; preserve its unique Kabuto source and assets.
2. Review the 58 differing shared paths file-by-file and cherry-pick only clearly beneficial crash/stability fixes from the LAN-enhanced branch.
3. Create a reproducible central integration mechanism that applies tracked local patches to the pinned source, then builds the combined result.
4. Add character/mod changes in small batches, checking roster identifiers, asset paths, skill/animation data, and Android build after each batch.
5. Download the verified candidate APK to the user's phone and record install, launch, character selection, battle, skills, HP/level, minions, towers, and post-match results separately from CI success.


## First verified local patch milestone (2026-10-10)
The Android-clean source is now built through a central patch pipeline. The first patch changes only the install identity/version/label; CI confirms the patch applied and checks the built APK metadata with `aapt`. Run `37968632537` succeeded and uploaded artifact `naruto-senki-v2-candidate-debug-apk` (ID `11634478692`, expires 2026-10-23).

Next mod pass: inspect and redesign the existing V2 loading/menu/character-selection UI while preserving the Cocos2d-x battle, level/HP/skills, minions, and towers. Keep changes as small ordered patches against the pinned source, and require build + metadata/resource checks before treating a patch as done. Then test install and actual gameplay on the phone.


## UI pass 1 complete in CI (2026-10-10)
The custom launcher icon, loading background, and character-selection background are now part of the central patch pipeline. Existing character grid/selection logic and battle mechanics are preserved. Run `37971031426` succeeded; its artifact contains both custom UI background assets and passes package identity checks.

### Next UI/gameplay work
1. Install the current artifact on the target phone and check the actual rendered loading and selection screens before making assumptions about scaling.
2. Adjust selection-screen grid spacing, preview placement, and touch targets only from observed behavior; preserve double-tap/confirm and mode-specific team selection.
3. Redesign the main menu and skill/hero info presentation, then improve launcher splash transition without disturbing the battle scene.
4. Run the APK build and archive checks after each patch; phone install/launch/battle checks remain a separate gate.


## UI pass 2 complete in CI (2026-10-10)
The main menu now uses the new Senki artwork while preserving the original mode carousel and callbacks. The latest successful APK archive contains the custom launcher icon plus loading, main-menu, and character-selection backgrounds. See run `37971712613`.

Next work should focus on the visible controls and interaction layer: confirm menu button placement, improve selected-mode feedback, refine character portrait/selection highlights and team-pick status, and retain all existing selection rules. Device visual checks are still required before making coordinate changes.


The newest artifact and CI evidence are tracked in `PROGRESS.md`; on-device visual and gameplay checks remain the next validation gate.


## Latest engineering update — 2026-10-10

- [x] The pinned Android-clean V2-derived source now builds in central CI with the ordered custom identity/loading/selection/menu patches.
- [x] Added landscape stability handling and CI assertions for the compiled manifest's sensor-landscape orientation.
- [x] Added fallback backgrounds to loading, menu, and selection so a missing custom PNG does not immediately abort scene setup.
- [x] Latest verified run: `38015483353` **SUCCESS**; artifact `naruto-senki-v2-candidate-debug-apk`, ID `11655846337`, 83,726,412-byte ZIP. See [run and artifact card](https://github.com/kage049754/Senki/actions/runs/38015483353).
- [ ] Install and launch on the user's phone; test post-engine-intro startup, main menu, character selection, battle start, touch controls, and orientation behavior.
- [ ] Keep expanding the character/mod research inventory and choose individual compatible changes to port after runtime baseline validation.
- [ ] Full V2 source tree is not yet vendored into this repository; current CI clones the pinned source and applies central patches temporarily.


## Roster expansion status — 2026-10-10

- [x] Source inventory measured: 37 unique selectable names in the current Android-clean base; do not confuse this with verified playable count.
- [x] Removed the fixed three-page selection cap in patch `0008-dynamic-roster-pagination.patch`; central CI run `38016671857` passed and uploaded artifact ID `11655938596`.
- [x] Added a separate discovered-leads registry for characters mentioned in the Naruto Senki v1.24–v1.26 release notes.
- [ ] Locate editable source/resource implementations for the discovered character leads; the current release-host APK is server-side-dependent and not a direct offline source base.
- [ ] Port one character at a time: class/behavior, XML/config, sprite/plist, animation/effects, audio, portrait/button, roster entry, and build/runtime tests.
- [ ] Device-test four or more selection pages and verify that the new text page buttons preserve existing tap-once preview / tap-again confirm behavior.

## Phase 5A — Character completeness, selection details, and combat event UI
**Status: Planned requirements; individual new characters and kill/death UI are not yet verified as implemented**

### Per-character integration checklist
- [ ] Record source repository/revision and inspect the character's real code and asset set.
- [ ] Add the correct selection portrait/avatar, display name, stable character ID, and roster entry.
- [ ] Connect selection to the correct character implementation and preview; verify taps do not select a different entry.
- [ ] Show the character's actual skill names/icons/descriptions in the skill-information view where supported.
- [ ] Integrate sprite/model assets, sprite sheets/plists, animation definitions, and required idle/movement/attack/skill/hit/death states.
- [ ] Connect basic attacks, movement, hitboxes, damage, cooldowns, character-specific skills, projectiles/summons, effects, and sounds where available.
- [ ] Connect player controls and computer AI to the correct actions and ability logic.
- [ ] Resolve all character IDs, resource paths, config, Lua/C++/XML/plist references, and dependencies; ensure no existing character is accidentally overwritten.
- [ ] Build the unified APK and verify the expected assets and code are packaged.
- [ ] Test selection, preview, skill information, movement, attacks, every skill, hit detection, damage, effects, AI, death/respawn, and relevant match modes.
- [ ] Mark a character **playable-verified** only after gameplay checks; do not count a portrait-only or roster-only entry as complete.

### Kill/death identity UI
- [ ] Inspect existing battle events, damage/death callbacks, score counters, and game-over UI before designing a new overlay.
- [ ] Where supported by the existing engine, show the actual killer's portrait/name and victim's portrait/name on a kill event (for example, "Naruto defeated Sasuke").
- [ ] Show corresponding victim/killer identity on death feedback, and update existing kill/death counters consistently where the mode supports them.
- [ ] Correctly attribute events to the real killer, including AI/ally interactions; don't infer the killer from the character selected at match start.
- [ ] Preserve existing match flow and avoid duplicate overlays, stale portraits, or changes to damage/game-over behavior.
- [ ] Verify the event UI in an actual match. CI can check compilation and packaged resources, but cannot by itself prove correct runtime attribution.

### Selection pagination consistency
- [ ] Preserve the original image-based page buttons 1, 2, and 3 and their original touch behavior.
- [ ] Create matching image-based normal/selected states for pages 4, 5, and future pages; all must remain reliably tappable and visually consistent with the original interface.
- [ ] Ensure each page displays the intended registered characters without changing their IDs or replacing existing fighters.
- [ ] Test page navigation and character selection on an Android device. Dynamic page count alone does not add or complete characters.

