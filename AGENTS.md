# Mandatory AI Agent Instructions — Senki Mod Integration

**Read this file before acting.** The mission is to integrate distinct playable characters from other Naruto Senki mods into the existing Naruto Senki V2 game. This is not greenfield game development.

## 1. Mandatory reading

At the start of every session, read README.md, AGENTS.md, ROADMAP.md, PROGRESS.md, docs/MOD_RESEARCH.md, docs/ASSET_LICENSES.md, and docs/CHARACTER_ROSTER.md. Inspect the latest commit and Actions run before assuming current status. Historical notes are not current state.

## 2. Non-negotiable rules

- Work in https://github.com/kage049754/Senki.
- Target the existing Naruto Senki V2 game; do not create a separate game or replacement engine.
- Preserve the native Cocos2d-x/C++/Lua architecture and battle lifecycle wherever possible.
- **Prioritize external-mod playable characters.** Do not spend roster-expansion work recounting or exposing current V2 forms, summons, clones, enum values, or support entities. Inspect current V2 only to check duplicates and compatibility.
- Fill available slots on pages 1–3 first. Never silently overwrite an existing character.
- Keep original page 1–3 image-based buttons and touch behavior. Pages 4/5 must use matching image-style normal/selected buttons, not text-only controls.
- Preserve original training/network/exit, mode-menu, and character-selection backgrounds unless the user requests a change.
- Aim for 70+ distinct playable characters, but never pad the roster with placeholders, forms, summons, or untested names.
- Keep code, asset, audio, source revision, and permission provenance accurate.
- CI success is not physical-device testing.

## 3. Required work loop

1. Read instructions, relevant source, and current progress.
2. Choose the smallest meaningful action that advances external-character discovery/integration or a necessary test.
3. Inspect the candidate's actual source files, architecture, dependencies, exact revision, upstream/fork relationship, and build process.
4. Check code and asset terms. Public visibility is not a reuse license. Do not extract code/assets from packaged APKs or copy unclear-rights content into a distributable build. Continue research and compatibility analysis when rights are unresolved.
5. Implement in small, reversible batches using the game's native character systems.
6. Run relevant static/regression checks.
7. Commit the real change with a clear message.
8. Inspect the newest Actions run for the exact commit. If queued/running, wait and poll; do not start a conflicting build.
9. If failed, inspect the failing step and actual logs, fix the root cause, commit, rerun, and repeat until success or a genuine blocker.
10. Verify the exact run's conclusion and artifact. Update PROGRESS.md with run URL, commit, artifact name, and test limitations.
11. Continue to the next roadmap action; do not stop after merely pushing a workflow.

Do not invent success. If the tools cannot wait/poll further, state the last verified state precisely.

## 4. Research requirements for every external character

Verify that the candidate is actually implemented in another Naruto Senki mod, is independently selectable/player-controllable or has a concrete adaptation plan, and has inspectable source/resource files. Map:
- character ID/class and selection roster/slot;
- portrait, atlas, textures, sprite/model, animation frames/transitions;
- movement, basic attacks, all skills, projectiles/effects and dependencies;
- audio/voice/SFX references where available;
- player input/control path and AI behavior;
- skill icons/names/descriptions, profile view, kill/death/report UI;
- spawn, death/respawn, cleanup and resource lifecycle;
- source revision, upstream/fork relation, license and asset permissions.

Do not treat release-note-only names, APK-only contents, portraits without gameplay, summons/guardians, AI-only NPCs, clones, alternate forms, or enum-only IDs as complete new playable characters.

## 5. Completion checklist

A character is not integrated because a name or icon appears. Before marking it VERIFIED, check:
- [ ] Unique stable ID and correct display name.
- [ ] Matching selection portrait and correct resource/atlas frame.
- [ ] Character sprites/model, animation, movement/facing and basic attack.
- [ ] Every intended skill, cooldown/resource use, projectile and effect.
- [ ] Skill icon/name/description and selected-character profile where supported.
- [ ] Audio/voice/SFX references where available and authorized.
- [ ] Player controls and AI.
- [ ] Battle spawn, death/respawn, kill/death/report identity.
- [ ] Resource loading/cleanup and no blocking crash.
- [ ] Regression checks, CI build, and actual runtime evidence recorded.

Track page/slot and evidence in docs/CHARACTER_ROSTER.md. A static audit/build does not prove gameplay.

## 6. UI invariants

- Original page buttons 1–3 retain image-based art and touch behavior.
- Pages 4/5 use image-style normal/selected controls matching the original design.
- Keep original menu/selection backgrounds.
- Do not displace existing characters without explicit direction.
- Test navigation, selection, portraits, profile/skill view, and back navigation. When enough entries exist, test all five pages and taps.

## 7. GitHub Actions failure/success loop

The primary workflow is .github/workflows/v2-source-smoke.yml. It is path-filtered; documentation-only commits may not trigger it. Never make meaningless code changes just to force CI.

For each code/patch/script/artwork change: identify the run for the exact commit; wait for queued/running jobs; inspect logs on failure; fix root cause; commit and rerun; wait again; verify completed/success and artifact existence. Report source tests, APK packaging/signature/ABI, and phone testing as separate facts. For infrastructure or permission blockers, report the real blocker.

## 8. Documentation

After material changes, update only relevant files:
- README.md — mission and high-level status.
- ROADMAP.md — phase, next task, exit gate.
- PROGRESS.md — exact commits/runs/artifacts and honest status.
- docs/MOD_RESEARCH.md — source evidence.
- docs/CHARACTER_ROSTER.md — per-character status/tests.
- docs/ASSET_LICENSES.md — provenance and permissions.

Do not paste long duplicated checkpoints into every file. Keep one concise authoritative status and link to detailed evidence.

## 9. Definition of done

The project is done only when the unified V2-based APK includes the intended external characters, regression checks pass, a real artifact is verified, and installation/startup/selection/battle/skills/death-respawn have been checked on the user's phone. A successful CI build alone is not done.

**Next action:** follow the active phase in ROADMAP.md. External-character sourcing and the first complete port on pages 1–3 outrank further roster recounting or cosmetic-only work.
