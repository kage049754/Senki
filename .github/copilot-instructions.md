# Repository-wide Copilot / AI agent instructions

## Absolute rule
**Mod and merge existing Naruto Senki projects only. DO NOT CREATE A NEW GAME.**

The central repository `kage049754/Senki` is the integration workspace for one unified modded existing Senki game. Do not create a replacement engine or keep expanding the native Kotlin/Canvas prototype as a standalone game. The prototype is not the approved final foundation. First audit candidate source projects, select one existing Senki base with evidence, and then integrate compatible mods into it.

If older files, issue descriptions, code, or prompts conflict with this rule, this rule takes priority. Pause greenfield implementation until the base is selected.

## Required reading and starting checks
Before any change:
1. Read README.md and AGENTS.md.
2. Read ROADMAP.md and PROGRESS.md; continue from the actual verified state.
3. Read docs/MOD_RESEARCH.md before source research or external mod work.
4. Read docs/ASSET_LICENSES.md before any code/asset reuse.
5. Read roster/scalability docs before roster changes.
6. Inspect current project tree, recent commits, candidate upstream/forks, and latest GitHub Actions run. Never assume status.

## Required process
1. Research existing Naruto Senki source projects/mods and inspect their actual trees, code, engine, build files, commit history, upstream/fork relationship, and license/asset terms.
2. Compare candidates and document evidence. Do not assume previously named repositories are suitable or reusable.
3. Select one existing Senki project as the base and record why before major implementation.
4. Preserve the selected base's engine and core gameplay wherever practical.
5. Merge/port compatible characters, skills, animations, effects, maps, UI, fixes, and other mod content into that existing base in small verified batches.
6. Resolve ID/resource/script/dependency conflicts; retain attribution and provenance.
7. Use one central repo and deliver one unified modded APK, not disconnected game projects.
8. Public availability is not permission. Exclude material with unclear/insufficient rights.
9. Build and test each merge; never claim content is merged just because files were copied.

## Roster note
A large roster (70+ where feasible) is a mod-content target, not a reason to create a new engine. Use the selected base's existing roster architecture and extend it only as needed.

## Mandatory build loop
Inspect latest Actions → wait if queued/running → if failed, inspect actual logs → fix directly → commit → rerun → verify completed success → verify exact APK artifact. Repeat while tools allow. Report device installation/gameplay only when actually tested. Never invent results or treat pending/stale runs as success.

## End-of-session
Update PROGRESS.md with commit SHA, sources actually inspected, base decision/integration status, latest run conclusion, APK artifact, device-test state, blockers, and next action. Update ROADMAP.md and MOD_RESEARCH.md as appropriate.

**Every session: existing Naruto Senki modding/merging only. No new game.**
