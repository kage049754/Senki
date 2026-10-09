# Senki Persistent Progress Tracker

Last updated: 2026-10-10

## Repository
- GitHub repository: https://github.com/kage049754/Senki
- Default branch: main
- Current engine/build state: Native Android Canvas/Kotlin prototype scaffold committed; build validation pending
- Latest CI result: Runs #1–#9 triggered while scaffolding; earlier runs failed/cancelled because the Android project was incomplete. Run #9 (current workflow with provisioned Gradle) is queued at last check.
- APK artifact: NOT CHECKED IN THIS SESSION
- Physical-device installation/gameplay: NOT VERIFIED IN THIS SESSION

## Current goal
Build one cohesive landscape-first Android 2D lane-battle game with a data-driven roster that supports 70+ playable characters and can expand beyond 70 without a hardcoded roster limit.

## Documentation status
- [x] README updated with AI instructions, progress tracker link, and scalable 70+ roster target.
- [x] AGENTS.md and .github/copilot-instructions.md updated with no-hardcoded-cap rules and mandatory tracker reads.
- [x] ROADMAP.md updated with dynamic registry and 75-entry scalability test.
- [x] Verified docs/MOD_RESEARCH.md contains the roster-scaling requirement.
- [x] Created and verified docs/CHARACTER_ROSTER.md.
- [x] Created and verified docs/ROSTER_SCALABILITY.md.
- [x] Created and verified docs/ASSET_LICENSES.md.
- [x] Inspected the complete repository tree: it contains documentation only; no Android app source, Gradle project, or game engine files exist yet.
- [x] Added .github/workflows/android.yml to build with provisioned Gradle and upload an APK. Build success/APK still not verified.

## Roster metrics
- Discovered leads: NOT YET COUNTED
- Planned characters: NOT YET COUNTED
- Implemented characters: NOT YET COUNTED
- Testing: NOT YET COUNTED
- Verified playable characters: NOT YET MEASURED
- Required target: 70+ verified playable characters
- Artificial roster cap: PROHIBITED
- 75-entry synthetic architecture test: REQUIRED, NOT YET RUN

- [x] Created GitHub Issue #1 for the first playable Android battle prototype: https://github.com/kage049754/Senki/issues/1

## Session log

### 2026-10-10 — Start implementation and establish CI
Verified repository audit:
- The full main-branch tree contains documentation only: README, AGENTS, ROADMAP, PROGRESS, and docs; no Gradle project, Android source, assets, or engine implementation exists yet.
- Added an Android APK GitHub Actions workflow; it will fail clearly until the project scaffold exists. Workflow trigger and result are not yet verified.
- Created Issue #1 defining the first implementation milestone.

Initial Kotlin/Android prototype scaffold committed: landscape-only launch, drawn menu, dynamic starter selection cards, and an early battle loop with movement, attack, skill cooldown, HP, simple rival AI, minions, pause, XP/levels, result/rematch. This is prototype code and has not yet passed a build or gameplay test.
Build/gameplay tests: pending CI.

## Next actions
1. Verify run #9 outcome; inspect logs and fix actual Gradle/Kotlin errors, rerunning after each fix.
2. Confirm an APK artifact is uploaded.
3. Improve and test prototype battle loop (including towers/objective damage and match completion).
4. Add the 75-entry registry/UI scalability test and validation.
5. Replace prototype shapes with properly licensed/original assets and expand systems in tested milestones.
6. Expand real characters in batches after rights/provenance review.

## Required end-of-session record
Record actual files changed, commit IDs, test results, workflow/run IDs, APK artifact state, device-test state, blockers, and the exact next task. Never copy example or pending statuses as if they were verified results.
