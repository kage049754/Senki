# Repository-wide Copilot instructions

Before making any change in this repository:
1. Read README.md.
2. Read AGENTS.md.
3. Read ROADMAP.md.
4. Read PROGRESS.md and continue from the exact verified state and next action.
5. Read docs/MOD_RESEARCH.md before using any outside Naruto Senki code, mod, character, or asset.
6. Read docs/CHARACTER_ROSTER.md and docs/ROSTER_SCALABILITY.md before changing the roster or character systems.
7. Read docs/ASSET_LICENSES.md before importing any external code or asset.
8. Inspect the current project tree, recent commits, and latest GitHub Actions run. Do not assume any code or build status.
9. Follow the mandatory build/failure/fix/rebuild/artifact-verification loop in AGENTS.md.
10. Update progress, roadmap, roster, and research documentation when relevant.

Project direction: landscape-first Android 2D lane-battle game; core offline gameplay; selectable fighters and distinct skills; HP, levels, minions, towers, victory/defeat, and reliable menu-to-battle flow. Never leave the game blank after startup.

## Large roster requirement
The character catalog must support 70+ playable characters and be expandable beyond 70. Do not hardcode a maximum of 29, 30, 50, 70, or any other fixed number. Use stable character IDs, a data-driven registry, scrolling/pagination, search/filtering, and lazy asset loading. Adding a standard character should not require rewriting the battle engine or adding a hardcoded UI slot. Test scalability with at least 75 synthetic entries, but never count synthetic entries as real playable characters. Only report the 70+ goal as complete after at least 70 distinct real characters pass the verification criteria in docs/CHARACTER_ROSTER.md.

Do not blindly merge APKs or repositories. Verify source provenance and reuse rights. Public availability is not permission to redistribute copyrighted assets or code. If rights are unclear, build an original implementation instead.

Never claim tests, successful builds, APK artifacts, or physical-device tests without evidence. If a tool cannot continue polling, state the last verified result honestly.
