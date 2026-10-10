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
**Status: In progress — central CI run #152 succeeded, including base-form skill-label reuse, informative Kabuto skill descriptions, page-button/background checks, and APK packaging verification; source vendoring, rights review, and phone validation remain open.**

- [ ] Bring or adapt the chosen base into `kage049754/Senki` using a documented, provenance-preserving method.
- [ ] Preserve original engine/game loop and existing behavior wherever practical.
- [ ] Resolve dependencies and Android build issues without replacing the engine with a new implementation.
- [x] Establish central CI for the pinned Android-clean V2-derived candidate and verify its actual patched APK artifact (latest run #152: https://github.com/kage049754/Senki/actions/runs/38031233006; artifact ID 11661624590; SHA-256 `a14c09e7c0d646504ee9b775a23e415cd25c28cc9476bac754dc9ac934f05193`).
- [ ] Vendor or otherwise preserve a reproducible, editable copy of the chosen source tree inside this repository; the current workflow still clones it into a temporary runner workspace.
- [ ] Confirm install/launch separately on a device when possible.

**Exit checks:** the selected existing Senki game builds and launches from the central repo before major mod merges begin.

## Phase 3 — Inventory and prepare mod content
**Status: In progress — external-mod character sourcing is the priority. Do not spend roster-expansion time classifying V2's own internal entities as additions.**

- [x] Continue researching existing Senki mods, source forks, release histories, and compatible resources; record the V2 custom-registry fork and mirror SHA comparisons in `docs/MOD_RESEARCH.md`.
- [x] Re-read the explicit user priority: external Senki-mod characters must be added to pages 1–3 before further page 4/5 work. Internal V2 enum/class audits are not character additions.
- [x] Verify that the inspected `SILXNTRAY/NarutoSenki-V2` custom registry is an architecture reference, not 70 ready-made characters: its custom character table is empty/commented examples and the inspected tree has no dedicated registry unit-test suite.
- [x] Confirm that the inspected `ZhReimu/NarutoSenki-V2` `basic.lua` change does not add a new selectable roster beyond the stock list.
- [ ] Identify and port distinct playable characters from OTHER Naruto Senki mods into available page 1–3 slots first. Do not count characters already in the selected V2 roster, internal AI/Guardian classes, summons, or alternate forms as new additions.
- [ ] Audit each external character package's selection portrait, sprite/atlas, animation schema, skills/effects, audio, player implementation, and AI implementation before selecting it for porting.
- [ ] Identify at least 27 additional distinct character/form source packages beyond the current 43 declared names, and verify their XML/atlas/texture/audio/skill/AI files individually.
- [x] Locate a complete older-schema Hokage Minato sprite/XML/audio package in `LeaderOnePro/NarutoSenki1.17Mod`; classify it as a resource lead only because it lacks V2-native class integration and reuse permission remains unresolved.
- [ ] Evaluate whether the old Hokage Minato animation XML can be safely converted to V2's unit schema, and identify the required class/AI/selection UI changes without importing uncleared assets.
- [x] Compare key files and tree paths across several V2 forks; record which forks are mirrors and which contain distinct architecture/UI changes.
- [ ] Compare remaining meaningful fork diffs against the pinned Android-only candidate and determine whether any new character implementations are genuinely unique.
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
**Status: In progress — six existing native forms are exposed on page four in CI; physical-device gameplay verification is pending.**

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



## Phase 5B — Restore original menu and character-selection backgrounds
**Status: Build-verified in central CI; phone visual confirmation and explicit APK asset-absence check remain open**

- [x] Stop applying the custom character-selection background patch.
- [x] Stop applying the custom main-menu background patch for the Training / Network / Exit mode interface.
- [x] Stop generating custom senki_select.png and senki_menu.png in the build workflow; keep the custom loading artwork separate.
- [x] Fresh V2-derived candidate APK build completed successfully in run `38019992304` on commit `e874e45d90f7e83082ff55b304bdb6f49f82fe65`; workflow no longer applies the retired menu/selection background patches.
- [ ] Inspect the APK's packaged assets explicitly to confirm no custom `senki_menu.png` or `senki_select.png` replacement is present.
- [ ] Check the main-menu and character-selection screens on the phone and confirm the original background/decorative layers are visible.

## Character profile and combat-event acceptance criteria

Every added character must be treated as a full playable integration, not a roster label. Acceptance requires: correct portrait/avatar and display name; correct selection preview; accurate skill names/icons/descriptions where supported; connected sprite/model and animation states; working movement, basic attacks, hitboxes, skills/cooldowns, effects and sounds where available; correct player controls and AI; valid IDs/config/resource references; and tests for selection, combat, damage, death/respawn, and relevant modes.

When supported by existing battle hooks, implement kill/death identity notifications showing the actual killer and victim portraits and names. Confirm events identify the real participants, including when an ally or AI character makes the kill. Add kill counts/streaks only where the existing mode supports them. A character is playable-verified only after runtime gameplay checks, not merely after a successful build or visible portrait.


## Current authoritative CI checkpoint — 2026-10-10

The latest verified build is [run 38020781870](https://github.com/kage049754/Senki/actions/runs/38020781870), run #82, commit `3cc5d3bd807ae6c7814dcce1d61710c05552b7b9`. It completed **SUCCESS** and uploaded `naruto-senki-v2-candidate-debug-apk` (artifact ID `11657917474`, 83,355,267 bytes, SHA-256 `303f9dfbabd11fec739b91dcdda4f818421618c242dda4182794d9497aa6c147`, expires 2026-10-24). The workflow confirms image-based page 4/5 normal/selected controls are packaged and retired custom menu/selection background replacements are absent. This is still a V2-derived diagnostic candidate, not a finished merged roster or phone-tested game. Physical-device appearance and touch behavior remain unverified.


## Mandatory per-character asset manifest and AI acceptance gate

This gate applies to every new character or meaningful form across Phases 3–5. A name/portrait appearing in the roster is not character integration. For each candidate, inventory exact source paths and provenance for:

- selection display name, portrait/avatar, button states, preview art/model/sprite, and select/confirm behavior;
- skill-view data: real skill names, icons, descriptions, slot/order, and supported cooldown/cost fields;
- sprite/model, atlas/texture/plist, idle, movement, attacks, cast/skill, hit/damage, knockback, death, transformation/ultimate and other used animation states;
- voice clips/voice lines where supplied or required, and attack/skill/hit/summon/transformation sound effects;
- skill implementations, projectiles/summons, effects, hitboxes, damage, cooldowns, costs and their resource/config references;
- character class/script/config, stable unique IDs, resource paths and form/variant registration;
- computer AI roster/selection/spawn registration, decision logic, movement, valid attacks/skills, range/state/cooldown handling, and supported random/team selection paths.

For every category, record exact paths and mark FOUND, ADAPTED, CREATED, NOT APPLICABLE (explain why), MISSING, or BLOCKED. Search source and resource bundles; do not infer that an asset exists from a reference in code. Do not claim a character has voice assets if no clips were found. Do not use unrelated sounds or placeholder icons without recording the adaptation. Apply source/asset permission and provenance rules to every imported item.

### Phase 3 exit-gate addition — asset/source completeness
- [ ] Create a per-character manifest before porting any candidate.
- [ ] Map selection portrait/avatar, name, preview, all skill UI fields, sprites/animations, audio/voice, skill/effect assets, configuration and AI-selection hooks.
- [ ] Record all missing or not-applicable categories and the reason; resolve required gaps or keep the character explicitly partial/blocked.

### Phase 4 implementation and test addition
- [ ] Integrate the character into both player selection and existing computer AI selection/spawn paths supported by the game.
- [ ] Confirm the AI can move and execute the character's valid basic attacks and every supported skill; test cooldown, range, state, transformation/summon, and resource edge cases.
- [ ] Confirm skill-view names/icons/descriptions match the real combat implementation and every audio/resource reference resolves.
- [ ] Test player and AI in battle, including preview, skills, sounds, hit detection/damage, death/respawn, and resource loading/release.
- [ ] Record asset manifest and test evidence before marking a character VERIFIED.

**Completion rule:** a character is fully complete only when all applicable categories are accounted for and the player and AI tests pass. If voice/audio or any other required category is unavailable, state the exact gap instead of reporting full completion. The current 37 source-level roster names are not evidence that 37 characters have complete assets or working AI.

## Mandatory character-completion gate (applies to Phases 3–6)

Every character port in Phase 4/5 must pass this gate before being called complete. The task is to reuse and connect the full character implementation from a compatible existing source wherever available—not to add a name/portrait-only placeholder.

- [ ] **Identity/selection:** stable ID, display name, correct portrait/avatar, normal + selected roster button artwork, preview, selection/start callback.
- [ ] **Skill information:** correct skill names, icons and descriptions in the existing skill-view UI; listed abilities must match the implemented skills.
- [ ] **Sprite/model/animation:** main sprite/model, atlas/texture/plist/config, idle, move/run, basic attack, skill/cast, hit/knockback, death and applicable ultimate/summon/transformation states.
- [ ] **Combat:** movement, attack logic/range/timing, hitboxes, damage, cooldowns, passive/active/ultimate skills supported by the source, projectiles/summons, status effects, VFX and resource references.
- [ ] **Voice and audio:** character voice lines/clips where available; attack, skill/ultimate, hit, death, summon and transformation SFX with correct triggers. Inventory files and trigger mappings. Missing or unsupported audio must be explicitly documented; never report it as included.
- [ ] **Game AI:** register the fighter in the existing game's AI roster/selection/spawn logic where supported. Test AI movement, attack decisions, range/state/cooldown behavior and all supported skills/summons/transforms. Player-selectable is not equivalent to AI-selectable.
- [ ] **Data integrity:** all IDs, roster/classes, C++/Lua/XML/plist/config references, skill definitions, animation frames, portraits, audio, effects and file paths resolve with no collisions.
- [ ] **Match feedback:** where supported, correctly identify the actual killer and victim by name and portrait/avatar while retaining existing kill counts and game-over behavior.
- [ ] **Verification:** build and inspect APK resources, then test character selection, preview, skill view, each attack/skill, animation/effect/audio triggers, AI roster selection/spawn, damage, death/respawn and supported modes. Record CI and physical-device tests separately.

Maintain a per-character manifest in `docs/CHARACTER_ROSTER.md`. Mark unavailable assets as missing/blocked/not-applicable with evidence and source reason. Do not invent missing assets and claim they are original. Track states separately: DISCOVERED → SOURCE-INSPECTED → PORTED → BUILD-VERIFIED → PLAYABLE-VERIFIED. A portrait, icon, class file, or successful APK build alone never qualifies a character as complete.


## Character package audit automation — 2026-10-10

- [x] Added source-level inventory script `scripts/audit_character_packages.py`.
- [x] CI now generates and uploads `senki-character-package-audit` alongside the candidate APK. Latest verified run: [#86](https://github.com/kage049754/Senki/actions/runs/38021855646), SUCCESS.
- [x] The audit checks the current roster source, per-character C++ header, Unit resource paths, audio folder paths, packed selection art frame names, and detectable AI registration.
- [ ] This audit is not gameplay verification; it cannot confirm skill viewer contents, exact voice/SFX triggers, animation correctness, resource runtime stability, or AI combat quality.
- [ ] No new character is added by this tooling. The first character port remains gated on finding a compatible, permission-cleared complete package or documented approval for the code and each relevant asset category.


### Latest verification note — 2026-10-10

Central CI run #98 passed source checks, character-audit report validation, Android diagnostic build, APK identity/search/signature/ABI checks, and artifact upload. This verifies the pinned patched candidate can be packaged by CI. It does **not** establish that the APK installs or plays correctly on the user's phone, that every character is complete, or that external source/assets are cleared for redistribution. Kabuto's expected skill-description labels remain a manual UI issue; no character was added in this pass.


### Skill-description missing-frame guard — 2026-10-10

A safe UI fallback was added in central CI for characters whose expected `<Character>_labelN.png` frame is absent. The patch checks the sprite-frame cache and shows `Skill description unavailable` when missing. Run #101 passed, including the Android candidate build and artifact verification: https://github.com/kage049754/Senki/actions/runs/38024966443 (APK artifact ID 11659082992). This is a guard against a missing-frame UI failure, not a replacement for the missing skill-description art/content and not proof of runtime appearance. Physical-device testing remains open.


### Skill-description fallback verification — 2026-10-10

Run #101 passed the new static fallback regression test and the Android candidate build. The patched skill view now guards the expected description frame and uses a visible generic fallback if the frame is absent. Runtime rendering and actual device behavior remain unverified; this does not add a character or fabricate skill descriptions.


### Packaged skill fallback verification — 2026-10-10

Run #104 passed after fixing a malformed intermediate workflow edit. CI now extracts `SkillLayer.lua` from the actual APK and checks that the missing-label fallback text and guarded frame lookup are present in the packaged asset. Verified artifact: https://github.com/kage049754/Senki/actions/runs/38025372460 (APK artifact ID 11659729329, SHA-256 `97e37a19c006b4c3af9a0fe301013b0f1cb94c2a20d99c02eefb5eb6e24b7d2e`). This remains a diagnostic candidate; physical device and gameplay tests are outstanding.


### Packaged skill-description fallback — run #104

The workflow now extracts `SkillLayer.lua` from the built APK and checks for both the guarded frame lookup and the visible fallback string. Run #104 passed this packaged-source check, APK build, signature/native ABI checks, and artifact upload. This is stronger than a source-only test but still does not replace physical-device visual/gameplay testing.


### Pagination artwork regression — run #109

Run #109 passed a regression check that reads the original page-button frames from the actual Select atlas and verifies generated page 4/5 normal/selected states preserve the original outer artwork. The test initially failed due to assumptions about standalone frame files and an overly strict center-region boundary; those test defects were corrected based on the actual CI logs. The same run also passed the Android build, packaged skill-fallback check, signature/native ABI validation, and artifact upload.

The current source still has 63 roster layout slots (three pages at 21 slots per page). The generated page 4/5 button artwork is ready and validated, but those pages will not appear until the roster actually grows beyond three pages.


### Artifact-access gate — repository is public (2026-10-10)

The GitHub API confirms `kage049754/Senki` is public. Workflow artifacts therefore must not be described as private: users with public repository access may download the APK during its retention period. The APK contains third-party game resources whose reuse/redistribution rights are unresolved. No repository visibility change has been made. Before any broader distribution, either obtain the needed permissions or explicitly decide on repository/artifact access controls; a successful diagnostic build is not a release approval.


### Latest candidate patch — 2026-10-10

Run #101 passed after adding a safe missing-skill-description frame fallback to the pinned Android candidate. See [run #101](https://github.com/kage049754/Senki/actions/runs/38024966443) and the exact artifact details in `PROGRESS.md`.

This improves failure handling when a skill label frame is absent; it does not restore missing character-specific descriptions, prove runtime rendering, or count as a character integration. Device/emulator validation is still pending. The candidate is still cloned into CI temporarily rather than vendored into this repository.


### Roster expansion milestone — 2026-10-10

The pinned candidate now exposes six existing native forms on a fourth character-selection page: Sage Jiraiya, Immortal Sasuke, Sage Naruto, Six Paths Naruto, Rock Lee, and Nagato. The patch reuses existing native enum/class/resource implementations and adds safe UI aliases where dedicated selection or skill-guide frames are missing.

- Latest build: [Actions run #117 — success](https://github.com/kage049754/Senki/actions/runs/38027092821).
- The workflow now inspects the APK itself to verify the six roster names and their UI aliases are packaged.
- The roster contains 84 slots and currently computes four pages. Page 4 is populated by six forms; page 5 button art is prepared and packaged but is not displayed until the roster exceeds 84 slots.
- Physical-device selection, battle, AI, skill, and transformation tests remain pending. Do not count these entries as verified playable until those checks pass.


Latest verification refresh: run #121 succeeded after adding atlas-texture existence checks to the six-form roster regression test. See `PROGRESS.md` for artifact ID `11660673063` and its SHA-256 digest. Device gameplay verification remains pending.


### Latest checkpoint — 2026-10-10 (run #126)

The latest candidate APK built and passed static form-registration, resource/texture, transformation-path, packaged roster, signature, and native ABI checks. The central repository now exposes six existing native transformation forms alongside the 37 original selectable names, for 43 distinct selectable names in the candidate. The declared 70-entry goal is a roster target, not a claim of 70 working characters; the static audit explicitly leaves gameplay-verified count unmeasured.

- Successful run: https://github.com/kage049754/Senki/actions/runs/38028647795
- Exact SHA: `9aa276227fa118e89246eef561aa318209d3c60a`
- APK artifact ID: `11660439960`; SHA-256: `865afbe5def724a1f0c0da37ad9aec845d12ccac4ed56a14411c156e6ce3b76c`
- Outstanding: actual device/emulator gameplay tests, source-vendoring, and code/asset rights review. No external character port is counted as complete.


### Original background preservation — CI run #136 (2026-10-10)

Run #136 passed both source-level checks and packaged-APK checks for the original character-selection and mode-menu background resources. The workflow confirms that the retired custom menu/selection replacement assets are absent and the original red/blue backgrounds and menu bars are present in the APK. This is not a visual runtime test; device/emulator verification remains open.

- Run: https://github.com/kage049754/Senki/actions/runs/38029520544
- SHA: `9c4aa3dbd82c91cef8fb90297030b809ae0cdd42`
- APK artifact ID: `11661441846`, SHA-256: `65a9116d9652b65a21eaf9f765ff709b3475aad45da3c2922522ad0253464a8f`


### Latest skill-view resilience verification — run #141 (2026-10-10)

The candidate now guards missing skill-description frame lookups and renders a visible fallback instead of blindly constructing a sprite from a missing frame. The tooltip clipper is tracked and cleaned up on skill switches. CI passed the source-level regression, Lua syntax validation, APK build, packaging checks, and artifact upload. Runtime visual behavior remains unverified on a device. No new characters were added by this change.


### Latest candidate verification — run #141 (2026-10-10)

Run #141 passed the alias-aware character audit, source-level background preservation check, byte-for-byte APK texture comparison, Android diagnostic build, APK packaging checks, and artifact upload. Skill-art inventory now accounts for the existing UI alias map; Kabuto's missing skill-description frames remain flagged instead of being hidden by the new aliases.

- Run: https://github.com/kage049754/Senki/actions/runs/38030022200
- Exact SHA: `c02bfb51c34b9bc6ae1c4285eacd48e3cfec4f09`
- APK artifact ID: `11661692440`, SHA-256: `3342575c632dee2a795af2207d510a97c3f70f6952eb68a536d31f6fa070bb13`
- Remaining: physical-device runtime validation, source-vendoring and rights review, and integration/testing of additional characters.

### Latest form skill-label alias verification — run #143 (2026-10-10)

The candidate now maps existing native forms to their base character's skill-description label frames as well as skill icons and large portraits. This avoids showing the generic missing-label fallback for forms that can reuse existing labels. Kabuto remains the only audited entry missing all five expected labels, and receives the visible fallback. Run #143 passed Lua syntax, character audit, Android candidate build, APK package/ABI/signature checks, and artifact upload.

- Run: https://github.com/kage049754/Senki/actions/runs/38030471776
- Exact source SHA: `40aea9917261a9355c76d1f6b4b5496c036593be`
- APK artifact ID: `11661893046`, size 83,325,632 bytes, SHA-256: `b7c57d7b60880c85109ae3dd0bf79fc78daa6a367589aa9a74954bbbf5a22145`
- Audit artifact ID: `11661603360`, SHA-256: `3397364510d2db1177a5ae6bc7f442fa329b10afd632a989c83e188f18799943`
- Still open: physical-device UI/gameplay verification, source vendoring, permission review, and integration of additional characters.

### Latest informative skill-description fallback — run #152 (2026-10-10)

Existing native forms now use their base character's skill-description label frames. Kabuto's five expected label frames are absent in the pinned candidate, so the fallback now provides descriptions for Chakra Scalpel Activation, Nerve Strike Dash, Dead Soul Vault, Dead Soul Jutsu (Possession), and Nehan Shojo: Final Slash. CI passed source tests, Lua parsing, Android build, packaged-description/form-roster checks, APK signature/ABI checks, and artifact upload. This is not device-level visual/gameplay verification.

- Run: https://github.com/kage049754/Senki/actions/runs/38031233006
- Exact source SHA: `680ae6429e52e142ba10707ebd71d783525fc261`
- APK artifact ID: `11661624590`, SHA-256: `a14c09e7c0d646504ee9b775a23e415cd25c28cc9476bac754dc9ac934f05193`
- Audit artifact ID: `11662099251`, SHA-256: `fbd2915a317262947ba38b27dfe2f58db12efebbc827e85c656b6f8ceb52dead`
- Remaining: physical-device testing, source vendoring, permissions/provenance, and actual additional character integrations.


### Latest non-roster enum inventory — run #159 (2026-10-10)

The character package audit now reports `HeroEnum` entries that are not present in the visible selection list, with an explicit warning that enum identifiers may represent forms, clones, summons, or internal implementation types and must not be counted as playable. Regression checks for the inventory and known support identifiers passed. Run #159 successfully built and packaged the patched diagnostic candidate.

- Run: https://github.com/kage049754/Senki/actions/runs/38031862251
- Exact SHA: `3f6ac555fa5b9fb5a9f64c195679e0abe50da2aa`
- APK artifact ID: `11662291624`; SHA-256: `f5529a7558f1e60fe8176c78f13a92364d866ce4e9e81a21092910118a3bef70`
- Audit artifact ID: `11662461471`; SHA-256: `34caeb205755ca9d78516b1cdc0ed9991efe467ff414a4f8175e08a729bdcb52`
- This is not roster expansion: the candidate still declares 43 distinct selection names, and gameplay-verified count remains unmeasured. The next task is classifying enum-only leads and locating complete compatible character packages.


## User-priority subphase — populate pages 1–3 before pages 4–5
**Status: Required next roster milestone; no new external character is currently verified as integrated.**

- [ ] Inspect the actual current character order and all selectable slots on pages 1–3; record which slots are available and which original characters must remain untouched.
- [ ] Research distinct characters implemented in other Naruto Senki mods; compare source history/forks and record exact source revisions and asset/code permission.
- [ ] Choose the first compatible, permission-cleared batch of distinct characters and place them in available/approved slots on pages 1–3 before expanding later pages.
- [ ] For every character, integrate complete resources and gameplay: selection name/portrait, sprite/model, animation frames, movement/attacks/skills, skill icons/names/descriptions, effects, available sound/voice, AI/player behavior, and battle/death/kill profile references.
- [ ] Run resource/ID/frame audits and test character selection, battle spawn, basic attacks, every skill, AI behavior, death/respawn, and performance.
- [ ] Update the verified roster counts only after the full test set passes; keep discovery/planned/blocked counts separate.
- [ ] Once the first distinct-character batch is verified on pages 1–3, proceed to page 4, then page 5. Do not use existing forms as filler to claim this milestone complete.

**Important current limitation:** external source and asset reuse permission remains unresolved for the current V2 candidate and research leads. Research and slot planning can proceed, but external assets must not be copied into the build until reuse is authorized or a clearly licensed source is found.


### Mandatory acceptance check: character portraits
For every new character on pages 1–3, confirm a real matching portrait/avatar appears in the exact assigned selection slot with the correct display name and valid atlas/frame reference. Record page + slot + stable ID + portrait resource + provenance/license + test result in docs/CHARACTER_ROSTER.md. Check supported skill/profile and kill/death portrait displays too. Blank, unrelated, placeholder, or broken images fail acceptance; the character remains incomplete and is not counted playable. Do not move priority to pages 4–5 until the initial distinct-character batch and its portraits are validated.


### Latest verified CI checkpoint — run #203 (2026-10-10)

- Run [#203](https://github.com/kage049754/Senki/actions/runs/38039686618) completed **SUCCESS** on commit `f70e617977f175b74ae417a04283c4abbb36554f`.
- APK artifact: `naruto-senki-v2-candidate-debug-apk`, artifact ID `11665148893`, ZIP size 83,320,489 bytes, digest `sha256:837a3bc327ec046cc4b41fb6a45843740ec4c411fffe1d75ed74d939989e025e`, expires 2026-10-24. Audit artifact: `senki-character-package-audit`, ID `11665043752`.
- The audit still reports **43 selectable entries / 37 distinct base characters** (six known alternate forms excluded), 84 slots across four pages, and nine enum-only leads needing manual classification. Selection-art check: 37/43 complete; kill-feed portrait frame pairs: 43/43; XML-to-atlas frame names: 43/43; skill-description label frames: 42/43, with Kabuto's five text fallbacks detected.
- Pagination and reserved page-empty-state checks pass, but page 5 remains empty. The roster target and actual playable-verified count are not met/measured. No physical-device installation or gameplay verification is claimed.
- **Next priority:** pages 1–3 first. Continue searching and inspecting complete, compatible distinct Senki characters; map available slots and asset needs; do not import external code/assets without resolved permission. Do not promote Han/Roshi guardian packages or enum-only entries into the playable count without full Hero lifecycle integration and testing.


### Follow-up after run #204 — enum audit and source discovery

- [x] Add a source-based classification table for the nine enum-only IDs so clone/support implementations are not mistaken for selectable characters.
- [x] Validate the classification table with the character-audit regression test and complete the Android diagnostic build; [run #204 passed](https://github.com/kage049754/Senki/actions/runs/38041108524).
- [x] Record the new `LeaderOnePro/NarutoSenki-cocos2dx` source lead. It contains C++/Cocos2d-x 2.2.6 source and an Android project, but is a legacy architecture and lacks a root license declaration.
- [ ] Compare this legacy candidate's character implementations with the pinned V2-derived candidate and identify a distinct, complete package that can be adapted without blindly copying its old XML/resource schema.
- [ ] Continue to prioritize a real new playable character on pages 1–3. Require selection portrait/name, V2-compatible resources, player controls, skills/effects/audio references, AI, kill/death display, and lifecycle tests before counting it.


### Legacy-source roster findings

- [x] Count the explicit legacy selection list: 35 distinct names; empty `None` slots excluded.
- [x] Confirm that resource folders include summons/support entities and cannot be treated as playable characters.
- [ ] Continue the search for distinct, complete character packages; do not treat this legacy three-page roster as the 70+ solution.
