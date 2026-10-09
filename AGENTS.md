# Mandatory Instructions for AI Coding Agents

These rules apply to every task in this repository. Read README.md, ROADMAP.md, and docs/MOD_RESEARCH.md before coding.

## 1. First actions
- Inspect the current branch, file tree, Android/build setup, and recent commit history.
- Inspect the latest GitHub Actions run and its APK artifacts before assuming build status.
- Establish what is actually implemented. Do not infer functionality from the roadmap.
- Keep the user informed with concrete verified progress, not unsupported claims.
- Read docs/CHARACTER_ROSTER.md before changing roster architecture or adding characters.
- Read docs/ROSTER_SCALABILITY.md before making any roster-size, selection-screen, or character-loading decisions.

## 2. Development approach
- Build a landscape-first Android game with a stable launch sequence: engine/application initialization → loading → main menu. Never leave a blank screen after splash.
- Keep gameplay systems modular: character definitions, skill definitions, combat, minions, towers, leveling, UI, input, match state, and audio should have clear responsibilities.
- Preserve the core game loop: HP, skills, cooldowns, minions, towers/objectives, progression, and win/loss conditions.
- Prefer a small playable vertical slice before adding a huge roster.
- Keep the core offline battle playable without login/network access.
- Do not replace working systems without inspecting them and explaining why a replacement is needed.
- Avoid large opaque changes. Commit coherent milestones and document important architecture choices.

## 3. Large roster requirement — IMPORTANT
The roster must be designed to support **70+ playable characters and remain expandable beyond that**. Seventy is a planning target, not a hard maximum or a promise that 70 characters already exist.

- Never hardcode a maximum roster size such as 29, 30, 50, or 70.
- Never tie character capacity to a fixed number of UI buttons, array slots, enum values, or switch-case branches.
- Character selection must be generated from a data-driven registry/catalog, not manually fixed slots.
- Character IDs must be stable and unique. Do not use list position as a character's identity.
- Adding a character should normally mean adding a validated character definition and permitted resources/behavior modules, then registering/discovering it automatically—not rewriting the core battle engine.
- Use pagination, scrolling, search, filters, categories, and/or virtualized/lazy-loaded UI so the roster remains usable on phone screens.
- Load heavyweight sprites, animations, and audio on demand; unload or release resources when safe.
- Avoid loading every character's full assets into memory at startup.
- Validate definitions at build time or startup and report missing IDs, portraits, animations, skills, and resource paths clearly.
- Support alternate forms as either distinct playable entries or selectable variants according to whether their movesets/gameplay differ. Avoid accidental duplicates.
- Keep selection, battle spawning, save/unlock data, AI, and tests compatible with an expanding catalog.
- Prefer shared reusable skill implementations and data-driven parameters, while allowing custom behavior for genuinely unique mechanics.
- Define no artificial roster ceiling. Practical limits should come from measured device performance, asset size, and tested UX—not an arbitrary source-code constant.
- Keep a verified count of implemented and tested playable characters in docs/CHARACTER_ROSTER.md. Never count planned, discovered, or untested entries as verified playable characters.

## 4. Mod/source research and asset provenance
- Read docs/MOD_RESEARCH.md before importing external content.
- For every external repository, record its canonical URL, fork/upstream relationship, engine, what was actually inspected, license/terms, and what may be reusable.
- A public repository, APK, sprite sheet, or mod description is not automatically permission to reuse or redistribute its contents.
- Do not copy extracted APK assets, ripped sprites, audio, proprietary code, or other copyrighted content unless rights/permission clearly allow the planned use.
- When rights are unclear, use the source as research only and create original compatible implementations/assets instead.
- Do not claim to have combined a mod unless its implementation has actually been ported, built, and tested.
- Deduplicate characters/forms while preserving meaningful variants with genuinely different movesets.

## 5. Build and failure loop — mandatory
For each implementation milestone:
1. Inspect the latest workflow run.
2. If queued or running, poll/check until an actual terminal result if tools allow.
3. If failed, open the actual failed job/step logs and identify the root cause.
4. Make a targeted fix in the repository.
5. Commit the fix and rerun the workflow.
6. Repeat until a completed successful run is observed or a real blocker prevents further action.
7. Verify the APK artifact exists, record its exact name and run, and verify package/build metadata when possible.
8. Distinguish CI build success from physical-device installation and gameplay testing.

Never say a build succeeded because it was merely started, is still running, or because an older run succeeded. Never fabricate logs, test results, APK artifacts, or device testing. If continuing background work/polling is not possible in the current tool session, state the exact last verified status rather than pretending to keep working.

## 6. Acceptance criteria
- App opens reliably and proceeds to visible UI after the engine splash.
- Main menu, mode selection, and character selection buttons work.
- Game runs in landscape with responsive touch controls and no clipped essential UI.
- A match can start, run, end, and restart.
- Player and enemies have visible HP; attacks and skills apply expected damage and cooldowns.
- Minions move/attack and towers/base objectives can be destroyed or otherwise resolve a win/loss.
- Level/experience mechanics work if included in the current milestone.
- No fatal startup exception, blank scene, or invalid APK packaging.
- Automated tests/build pass and the generated APK artifact is verified.
- Real-device behavior is only marked verified after an actual install/launch test.
- The roster UI and registry have no fixed 29-character ceiling; tests can register more than 70 entries without code changes to a fixed-capacity UI.

## 7. Documentation
- Update ROADMAP.md when a milestone changes status.
- Update docs/MOD_RESEARCH.md when sources, mods, licenses, forks, or character ideas are verified.
- Update docs/CHARACTER_ROSTER.md whenever roster entries or their verification statuses change.
- Update docs/ROSTER_SCALABILITY.md when architecture or load/performance decisions change.
- Record build run links, artifact names, known failures, and exact validation status.
- Do not mark unchecked items complete without evidence.
