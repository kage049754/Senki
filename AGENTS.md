# Mandatory Instructions for AI Agents — READ FIRST

## Absolute project rule

**THIS PROJECT IS FOR MODDING AND MERGING EXISTING NARUTO SENKI PROJECTS. DO NOT CREATE A NEW GAME.**

The central repository is `kage049754/Senki`. It is the integration workspace, not a mandate to invent a new engine or build a separate Naruto-inspired clone. The intended result is one unified modded version of an existing Naruto Senki game.

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

## Documentation duties

Update `ROADMAP.md` and `PROGRESS.md` after meaningful work. Update `docs/MOD_RESEARCH.md` for source inspections/base decisions; update `docs/ASSET_LICENSES.md` for provenance and permission decisions. Keep planned, copied, integrated, built, and device-tested content as separate states.

**Remember every session: we are modding/merging an existing Naruto Senki game. We are not creating a new game.**
