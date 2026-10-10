# Mandatory Instructions for AI Agents — READ FIRST

## Absolute project rule

**THIS PROJECT IS FOR MODDING AND MERGING EXISTING NARUTO SENKI PROJECTS. DO NOT CREATE A NEW GAME.**

The central repository is `kage049754/Senki`. The user selected Naruto Senki: V2 as the target game. Use https://github.com/Naruto-Senki/files/releases and the v2.1.6-fix reference at https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix; see docs/BASE_GAME.md. This repository is the integration workspace, not a mandate to invent a new engine. Release assets are packaged binaries, not editable source; verify and import actual source before source-level modding. The intended result is one unified modded version of an existing Naruto Senki game.

If older instructions, roadmap entries, issues, or code encourage building a game from scratch, these rules override them. Pause new-game development. Inspect the existing Kotlin/Canvas prototype scaffold, but do not extend it as the final engine. First identify and verify the most suitable existing Senki source/base. Only decide what to retain, replace, or remove after the source audit.

## Mandatory reading at the start of every task

1. Read `README.md`.
2. Read this file completely.
3. Read `ROADMAP.md` and `PROGRESS.md`.
4. Read `docs/MOD_RESEARCH.md` before investigating/importing external mods.
5. Read `docs/ASSET_LICENSES.md` before any reuse.
6. Read roster/scalability docs before roster changes.
7. Inspect current tree, latest commits, candidate upstreams/forks, and latest Actions run before assuming anything.

## Correct workflow: research → choose base → merge

1. Search for existing Naruto Senki source repositories and mod projects.
2. Inspect repository tree, source files, engine/version, build scripts, dependencies, history, upstream/fork relation, and licenses.
3. Compare candidates and document evidence. Do not assume any previously mentioned candidate is compatible or permitted.
4. Select one existing, buildable Senki project as the base and record the decision in the research docs before large implementation changes.
5. Preserve that game's engine and core mechanics wherever possible.
6. Integrate compatible modded characters, skills, animations, effects, maps, UI, and other content into the chosen base. Resolve naming/ID/resource conflicts and engine-version differences.
7. Keep one central integration workspace and one final APK. Do not produce a family of disconnected game implementations.
8. Verify each merge by building and testing it. A code copy or successful build alone does not prove a character is playable.
9. Keep source attribution, license, and asset provenance records accurate.

## Prohibited behavior

- Do not design or implement a replacement game engine as the main deliverable.
- Do not continue expanding the standalone Kotlin/Canvas prototype into a new game while base selection is unresolved.
- Do not invent new gameplay systems as a substitute for finding/merging existing Senki systems.
- Do not claim that a repository, mod, character, animation, or asset was inspected/merged unless evidence exists.
- Do not blindly merge complete repositories or APKs.
- Do not extract and redistribute APK assets or copyrighted content without permission.
- Do not assume a public GitHub repository means its code/assets are free to reuse.
- Do not call forks independent projects without comparing changes.
- Do not report queued/running/failed CI as success or claim physical-device tests without actually performing them.

## Merge engineering rules

- Prefer adapting content to the selected base's native architecture rather than replacing the architecture.
- Maintain a source inventory: canonical URL, upstream/fork relationship, inspected paths, engine, buildability, license/asset terms, useful content, and integration status.
- Preserve existing gameplay behavior unless the requested mod integration requires a documented change.
- Standardize identifiers/resources only as needed for compatibility; preserve meaningful variants with distinct gameplay.
- Make changes in reviewable batches, with a build/test after each batch.
- If source or asset permission is unclear, mark it reference-only or excluded until clarified.
- Roster scalability (including 70+ if practical) is a content goal, never a reason to start a new game engine.

## Build and failure loop

For every integration milestone:
1. Inspect the latest workflow run.
2. Wait/poll if queued or running, when tools allow.
3. On failure, inspect the actual failed job/step logs.
4. Fix the identified cause directly in the repository.
5. Commit and rerun.
6. Repeat until a completed successful run is verified or a real blocker is documented.
7. Verify the APK artifact and record its exact name and run link.
8. Separate CI/package verification from real Android installation/gameplay testing.

If the current tool session cannot keep polling in the background, report the exact last verified state; never pretend work continued.

## License and fan-project rule

The user may choose to describe this as a fan-made/non-commercial project, but that does not waive external source licenses or third-party asset rights. The repository root LICENSE covers only original contributions made for this repository; it must not be presented as a license for external Naruto Senki source/assets. Keep unlicensed source/assets as reference-only until terms or permission are established. Read NOTICE.md and docs/V2_BUILD_AUDIT.md.

The current Android workflow is explicitly a legacy prototype scaffold build, not a Naruto Senki V2 build. Never report its success as completion of the target game.

## Documentation duties

Update `ROADMAP.md` and `PROGRESS.md` after meaningful work. Update `docs/MOD_RESEARCH.md` for source inspections/base decisions; update `docs/ASSET_LICENSES.md` for provenance and permission decisions. Keep planned, copied, integrated, built, and device-tested content as separate states.

**Remember every session: we are modding/merging an existing Naruto Senki game. We are not creating a new game.**

## User's personal-use modding priority (2026-10-10)
The user explicitly prioritizes building a personal Naruto Senki mod and wants research to continue even when a candidate has no explicit reuse license or permission statement. Do not stop source discovery, compatibility analysis, or private build experiments solely because a public repository lacks a license. Continue examining publicly accessible Senki forks, mods, releases, source snapshots, and game resources; compare and test promising candidates; record provenance and technical findings; and prioritize getting a complete Android build running for the user's personal testing.

Do not repeatedly interrupt progress with generic permission warnings. Keep legal/licensing discussion brief and only raise it when it materially affects a concrete step. Do not misrepresent a license, bypass access controls, break into private systems, or claim the user has redistribution rights. Never treat public visibility as proof of a license. The immediate engineering goal is private mod development/testing, not publishing a redistributed package. Keep candidate imports traceable so the user can choose how to handle a future public release.


## Central patch and artwork workflow
- Keep the pinned Android-clean V2-derived source as the current lead base. Do not replace it with a new engine or the separate LAN branch wholesale.
- Implement modifications as ordered unified patches under `patches/android-clean/NNNN-*.patch`. Keep original editable vector art under `artwork/`; generate PNG assets in the build workflow rather than committing generated binary outputs.
- The candidate workflow must apply every patch in sorted order, render required artwork, build the real V2 source, inspect the APK package metadata, verify required assets are inside the APK, and upload a short-lived Actions artifact.
- After any failure, inspect actual logs, correct the cause, rerun, and verify the final run/artifact. Do not call a build successful while queued/running/failed/cancelled.
- CI success is not proof of a correct visual layout, touch behavior, installation, or gameplay. Track phone testing separately and do not claim it happened unless confirmed.
- For the next screen work, preserve the existing hero roster, character selection mechanics, battle scene, skills/HP/level, minions, and towers. UI changes must not replace the underlying Naruto Senki V2 gameplay with a new prototype.


## Current UI work status
- Source-controlled editable artwork now covers launcher icon, main menu, loading screen, and character selection.
- Build workflow renders the SVG artwork, applies patches in filename order, builds the pinned V2-derived source, and verifies the generated background assets inside the APK.
- Preserve the original mode carousel, hero roster/grid/paging, selection behavior, and battle mechanics. Make coordinate/touch changes only after observing the actual device layout; don't assume CI proves visuals are correct.

## Complete character integration contract

When asked to add a character, do not stop after adding a name, portrait, or selection-grid slot. Inspect the target character's actual source implementation and assets, then integrate and verify every applicable layer:

- **Selection identity:** character ID, display name, portrait/avatar, selection entry, correct touch/selection behavior, and a preview if supported.
- **Skill display:** the character's actual skill names, icons, and descriptions in the skill view when the base supports it. Skill information must correspond to the real combat implementation; do not invent working skills from icons alone.
- **Assets/animation:** sprites or model, sprite sheets/plists, animation definitions, idle/move/run, basic attack, skill/cast, hit/damage, knockback, death, and other states required by the engine.
- **Combat logic:** movement, attack timing, hitboxes, damage, cooldowns, projectiles/summons, special skills, visual effects, sound effects, and resource/config references.
- **Player and AI:** player controls invoke the correct attacks/skills; AI-controlled copies can move, choose attacks/skills, and respond to combat without crashes.
- **Registration/integrity:** selection roster, character IDs/classes, C++/Lua/XML/plist/config references, resource paths, and effect/sound links must all point to the intended character. Avoid ID collisions and accidental replacement of an existing fighter.
- **Kill/death feedback:** investigate the base game's battle-event and UI systems. Where feasible, show the actual killer and defeated character with both portrait/avatar and name on kill/death events, plus a clear message such as "Naruto defeated Sasuke." Update existing counters/score/game-over logic consistently. Do not falsely attribute a kill to the selected character when a different AI/ally made it.
- **Tests:** build and inspect the packaged APK; test character selection and preview, skill panel, movement, basic attacks, each skill, hit detection/damage, animation/effects/sounds, AI, death/respawn, and kill/death attribution. CI success alone is not gameplay verification.

Track each fighter with explicit states: **discovered → source inspected → ported → build-verified → gameplay-verified**. A portrait, name, or skill icon alone is not a playable character. If an implementation or asset is missing, document the gap and complete it rather than marking the fighter done.

For roster pagination, preserve the original image-based page buttons 1–3 and their touch behavior. Pages 4+ must use matching image-based normal/selected button visuals and functional hit targets, not a different-looking text-only clickable control. Pagination only exposes roster entries; it does not make those entries playable.



## Original background rollback requirement (user-requested, 2026-10-10)

Preserve the original Naruto Senki main-menu/mode-carousel background and the original character-selection background. The main menu here is the interface with Training, Network, and Exit. Do not apply 0004-custom-character-select-background.patch or 0005-custom-main-menu-background.patch; do not generate or package senki_select.png or senki_menu.png as replacements. Preserve original decorative layers and selection/menu callbacks. The loading screen is a separate asset and may remain customized. After changing the build recipe, verify a fresh APK build and clearly separate CI evidence from visual confirmation on the phone.

## Full character integration contract

For each requested new character, connect and validate all of the following where the V2 engine/source supports it: selection portrait/avatar and display name; selection preview; skill names/icons/descriptions; character sprites/model and animation states; movement and basic attacks; hit detection/damage; character-specific skills, cooldowns, projectiles/summons and effects; sound; player controls; computer AI; stable IDs and resource/config references. A portrait or skill icon alone is not a playable character. Test that the selected entry maps to the correct combat implementation and does not overwrite another roster entry.

For kill/death identity UI, inspect existing combat, damage, death, scoring, and game-over hooks first. Where supported, show the actual killer and victim portraits/names and optional supported counters; verify that the correct killer/victim are identified for player, ally, and AI kills. Do not mark this complete without runtime testing.


## Required complete-character package — applies to every added fighter/form

Do not implement a character as just a roster entry, portrait, sprite, or skill icon. Before porting it, search the complete source tree and record a per-character manifest with exact file paths, source revision, provenance/permission, and one of these states for every category: FOUND, ADAPTED, CREATED, NOT APPLICABLE (with reason), MISSING, or BLOCKED.

1. **Selection and identity:** display name, stable ID/form ID, portrait/avatar, button/thumbnail normal and selected states, preview art/model/sprite, and working select/confirm flow.
2. **Skill display:** actual skill names, icons, descriptions, slot/order, and supported cooldown/cost information. These must correspond to the actual combat functions, not placeholder UI.
3. **Character art/animation:** sprite/model, atlas/texture/plist, idle, movement/run, facing, basic attacks, casts/skills, hit/damage, knockback, death, transformation/ultimate, and any other states used by the code.
4. **Audio:** search for and inventory voice clips/voice lines when the source includes them or the design requires them, plus attacks, skills, hit, summon, transformation, and other character-specific sound effects. Never silently claim voice assets exist. If a category has no source asset, document whether it is genuinely not applicable or is a missing completion requirement; do not substitute unrelated sounds without documenting the adaptation.
5. **Skills and effects:** every skill's logic, animation, projectile/summon, particles/effects, hitbox, damage, cooldown, costs, and all referenced resources/config values.
6. **AI integration:** explicitly register the character in existing computer-controlled character selection/spawn pools and AI dispatch logic where the mode supports it. Verify AI can select/spawn the character, navigate/move, use basic attacks and every supported skill under valid range/state/cooldown conditions, and handle transformations/summons without crashing. Include team/random selection paths when present. Player selection alone is not proof of AI support.
7. **Resource/ID integrity:** all C++/Lua/XML/plist/config, character class, animation, UI, effect, and audio references resolve to the correct fighter; IDs are unique; existing characters are not accidentally overwritten.

Use only assets whose reuse is permitted under the repository's provenance/permission rules. Record all missing categories and their impact. A character is not fully complete if required icons, selection art, animation states, voice/audio, skill behavior, or AI support is missing; it may only be reported as partial/incomplete with an explicit gap list. Mark a character playable-verified only after testing selection, preview, skill display, player combat, audio/effects, AI selection and combat, death/respawn, and resource stability. Keep build verification separate from runtime/device verification.
