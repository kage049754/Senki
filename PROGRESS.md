# Senki Persistent Progress Tracker

Last updated: 2026-10-10

## Absolute project direction
**Modding and merging existing Naruto Senki projects only. Do not create a new game.**

- Central integration repository: https://github.com/kage049754/Senki
- Goal: choose one existing Senki game as the base, then merge compatible modded content into that game.
- Final deliverable: one unified modded game and one verified APK.
- Preserve the selected base's engine/core gameplay wherever practical.
- Do not continue building the standalone Kotlin/Canvas prototype as a new game while base selection is unresolved.

## Current verified repository state
- The repository contains planning/research docs, an Android build workflow, and a native Kotlin/Canvas prototype scaffold from earlier work.
- The prototype scaffold is **not confirmed as the correct foundation** and is not the intended final game.
- Existing Senki source candidates have been listed in `docs/MOD_RESEARCH.md`, but the best base has not yet been selected through a complete comparative audit.
- CI status and APK artifact: MUST be checked from the latest Actions run before any claim. Historical/pending status must not be reused as current verification.
- Physical-device install/gameplay: NOT VERIFIED unless a new documented device test proves it.

## Documentation changes
- [x] README explicitly states this is a mod-merging workspace, not a new-game project.
- [x] AGENTS.md makes “do not create a new game” the overriding instruction.
- [x] ROADMAP.md replaced greenfield development phases with source audit, base selection, integration, and merged-build verification.
- [ ] Update Copilot instructions to repeat the same rule.
- [ ] Continue the actual source candidate audit and record evidence in docs/MOD_RESEARCH.md.

## Candidate/base decision
- Selected existing base: **NOT SELECTED YET**.
- Strong candidate to inspect first: `Zx-Akito/NarutoSenki-V2` (candidate only; not approved until source, buildability, upstream relationship, and rights are verified).
- Other candidates and their known limits are documented in `docs/MOD_RESEARCH.md`.
- Do not begin major content merges until one base is selected.

## Next actions — in order
1. Finish updating repository-wide Copilot instructions with the non-negotiable no-new-game rule.
2. Inspect the latest GitHub Actions run and artifact state, but do not confuse prototype build success with the final goal.
3. Audit candidate source repositories and compare actual code/build files, history/forks, engine, and license/asset terms.
4. Select one existing Senki base and document the evidence.
5. Decide whether/how to migrate or replace the prototype scaffold only after base selection.
6. Build the selected base in this central repository, then merge compatible mods in tested batches.

## Build / QA record
- Latest run: verify live Actions state before reporting.
- Last verified workflow conclusion: NOT RECORDED HERE; re-check actual run.
- APK artifact: NOT VERIFIED HERE; re-check the actual artifact list.
- Physical-device installation: NOT VERIFIED HERE.

## Required session log
For every session, record changed files, commit SHA, repositories actually inspected, integration status, latest workflow run/conclusion, artifact name/link, device-test status, blockers, and exact next step. Never copy stale or pending status as verified fact.

## Reminder for every future AI session
**Do not build a new Naruto-inspired game. Mod and merge an existing Naruto Senki project. The base has to be selected from real source repositories first.**
