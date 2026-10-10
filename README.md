# SENKI — Existing Naruto Senki Mod-Merging Workspace

> **Non-negotiable project direction: MODDING AND MERGING ONLY. DO NOT CREATE A NEW GAME.**

## What this repository is for

`kage049754/Senki` is the **central workspace for researching, adapting, and combining compatible parts of existing Naruto Senki game/mod projects into one unified modded Senki build**. It is not a request to invent a new game, replace the original engine with a home-made engine, or build a Naruto-inspired clone.

**Preserve an existing Senki game as the foundation.** First inspect candidate source repositories and select the most suitable existing, buildable foundation. Then merge or port compatible mod content into that foundation, resolving conflicts carefully. The final objective is one unified modded game/APK—not multiple unrelated APKs.

## Mandatory instructions for every AI agent

Before acting, read this file, [AGENTS.md](AGENTS.md), [ROADMAP.md](ROADMAP.md), [PROGRESS.md](PROGRESS.md), and [docs/MOD_RESEARCH.md](docs/MOD_RESEARCH.md). Read [docs/ASSET_LICENSES.md](docs/ASSET_LICENSES.md) before reuse, and the roster documents before roster work.

If an instruction, task, or earlier commit conflicts with the rule **“mod and merge an existing Naruto Senki project; do not create a new game,” STOP the conflicting work and follow this rule**. Do not treat an existing prototype scaffold in this repository as permission to continue building a separate game. Audit it and decide whether it is useful tooling or should be removed/replaced after identifying the real Senki base.

These repository instructions guide repository-aware agents; they cannot technically force every external AI to obey. Keep them in the obvious entry-point files and re-read them each session.

## Required workflow

1. Inspect this repository and its latest commit/build status.
2. Research existing Naruto Senki source projects and mods; verify their real contents, upstream/fork relationships, engine, buildability, and licenses/permissions.
3. Select and document **one existing Senki game as the base** before major implementation. Do not assume a candidate is suitable until inspected.
4. Keep `kage049754/Senki` as the central integration workspace. Preserve the selected base's engine and core gameplay wherever practical.
5. Merge compatible source changes/content in controlled batches. Resolve duplicate IDs, incompatible formats, engine/version conflicts, dependencies, UI collisions, and gameplay balance.
6. Track every source and asset's provenance and reuse permission. Public availability is not permission to redistribute.
7. Build the unified mod and verify the actual APK artifact. If CI fails, inspect logs, fix, commit, rerun, and verify again.
8. Report exact verified status. CI success is not the same as physical-device testing.

## What “unified” means

- One existing Senki game foundation and engine.
- One integrated character roster, including compatible mod characters and meaningful alternate forms.
- Compatible skills, animations, effects, UI, maps, and other content integrated into the same game.
- One consistent set of IDs, resources, configuration, dependencies, and gameplay rules.
- One final Android package after successful build and testing.

The roster can be expanded beyond 70 entries if the chosen base and resources support it, but **do not build a new engine just to meet a roster target**. Prefer adapting the existing game's native systems.

## Source research and merging rules

- Treat candidate repositories as unverified until their trees and source files have been inspected.
- Compare forks against upstream; do not count a fork as a distinct mod without meaningful changes.
- Distinguish editable source projects from APK-only releases, file hosts, translations, websites, and unrelated Naruto games.
- Do not blindly merge entire repositories or APKs.
- Do not copy or redistribute code/assets unless their license or explicit permission allows the intended use.
- If a mod is incompatible or lacks reuse permission, document it as reference-only/excluded; do not pretend it was merged.
- Never claim a character or mod is integrated until it builds and has been tested in the unified game.

## Build and verification

Follow the full failure-inspection/fix/rebuild loop in [AGENTS.md](AGENTS.md). Record the latest run, commit, actual result, artifact name/link, and device-test status in [PROGRESS.md](PROGRESS.md). Never call a queued, running, stale, or failed run a success.

## Current status

The repository previously received a native Kotlin/Canvas prototype scaffold. **That scaffold is not the agreed final game foundation.** The V2 source candidate and Android build configuration have now been inspected; see [docs/V2_BUILD_AUDIT.md](docs/V2_BUILD_AUDIT.md). The candidate uses legacy Android tooling, and code/asset reuse permissions remain unresolved. Do not continue adding original game-engine/gameplay systems to the prototype as a substitute for the existing game.

## Research documents

- [AI agent rules](AGENTS.md)
- [Roadmap](ROADMAP.md)
- [Persistent progress](PROGRESS.md)
- [Mod/source research inventory](docs/MOD_RESEARCH.md)
- [Character roster tracker](docs/CHARACTER_ROSTER.md)
- [Roster scalability notes](docs/ROSTER_SCALABILITY.md)
- [Asset/license tracking](docs/ASSET_LICENSES.md)

## Rights and disclaimer

This is an independent fan-made, non-commercial modding/research workspace. Fan-made/non-commercial status does not automatically grant rights to third-party code or assets. The root LICENSE covers only original contributions authored for this repository by contributors who can license them; it does not override external source terms or rights held by Naruto/Naruto Senki owners. See NOTICE.md, docs/ASSET_LICENSES.md, and docs/V2_BUILD_AUDIT.md. Do not redistribute material without permission.


## Selected base game: Naruto Senki V2

The user has selected **Naruto Senki: V2** as the game to mod. The original release listing is the reference point: [Naruto-Senki/files releases](https://github.com/Naruto-Senki/files/releases), with the [v2.1.6-fix release page](https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix) currently identified. The direct [Android APK release asset](https://github.com/Naruto-Senki/files/releases/download/v2.1.6-fix/NSV2_2.1.6-fix_Android.apk) is linked for reference/download from the original host.

**All future authorized modding work is centralized in this repository, `kage049754/Senki`.** Changes to characters, skills, animations, fixes, and other content must be integrated into the selected existing Senki V2 base here, not built as a separate new game.

Important: the linked release page is a file host with packaged release assets, including an APK; it is not itself editable source code. The V2 source project and its license/asset terms still need to be verified and imported before actual source-level modding can be completed. See [docs/BASE_GAME.md](docs/BASE_GAME.md). The APK is linked as a reference and is not claimed to be copied into this repository.


## Latest source research status (2026-10-10)

Two V2-derived Android source candidates have now been found with their **own** successful GitHub Actions APK builds:
- [Wilykun/NarutoSenki-V2](https://github.com/Wilykun/NarutoSenki-V2) — includes a documented AI-vs-AI Spectate mode and build fixes.
- [muhammadadilsyaputra08-alt/NarutoSenki-Custom](https://github.com/muhammadadilsyaputra08-alt/NarutoSenki-Custom) — documents an Android-only V2-derived C++/Lua source tree and a reproducible legacy Android build setup.

These are technical candidates, **not imported into this repository**. Both currently report no declared GitHub license, and the permissions for inherited source and Naruto/game assets remain unresolved. Their CI artifacts are not builds from `kage049754/Senki`. See [the source comparison inventory](docs/MOD_RESEARCH.md), [the permission register](docs/ASSET_LICENSES.md), and [the base-game notes](docs/BASE_GAME.md).

The next milestone is to establish source provenance and obtain appropriate code/asset permissions, then choose exactly one V2 base and build it in this central repository. The current prototype-only CI success does not satisfy that milestone. No unified mod APK or device-tested game has been completed yet.

## Personal-use development direction (updated 2026-10-10)
The user wants active research and private testing to continue even if a public Senki source/mod does not state an explicit reuse license. Missing license metadata must not be treated as a blocker to finding candidates, comparing features, or checking whether source builds. Search more GitHub forks, mod releases, archives, mirrors, and other publicly accessible sources for character models, sprites, animations, effects, skills, stages, UI, and complete Android game projects.

The immediate goal is a working personal Android test build based on the existing Naruto Senki/V2 game—not a replacement prototype and not a public redistribution release. Test candidates in isolation, document their origin/version, choose a strong base, integrate incrementally, and verify actual build results. A successful CI build still does not prove installation or gameplay on a physical phone. Keep rights/provenance notes accurate, but do not let repetitive generic permission warnings derail technical progress.


## Additional verified V2 candidate builds (2026-10-10)

A second, feature-rich V2-derived source candidate has now built successfully in this repository's CI: [`sansaks-jpg/NarutoSenki-V2` LAN candidate run](https://github.com/kage049754/Senki/actions/runs/37967514487). Its artifact is `naruto-senki-v2-lan-candidate-apk` (80,405,874-byte ZIP; expires 2026-10-23). It retains the existing Cocos2d-x/C++/Lua game and adds LAN multiplayer hardening and crash fixes. The first candidate also has a successful artifact-enabled build: [Android-clean V2 candidate run](https://github.com/kage049754/Senki/actions/runs/37966861114), artifact `naruto-senki-v2-candidate-debug-apk` (83,435,979-byte ZIP; expires 2026-10-23).

Both are **candidate APKs built in CI**, not yet integrated into one central source tree and not physically tested on the user's phone. The next engineering gate is a source/resource comparison to select the best V2 base, then controlled integration and device testing. See [PROGRESS.md](PROGRESS.md) and [docs/MOD_RESEARCH.md](docs/MOD_RESEARCH.md) for exact commits and build evidence.


### Source comparison result
A direct recursive-tree comparison found 1,828 identical files across the two successful candidates. The Android-clean candidate uniquely includes a redesigned Kabuto character, clone logic, sprite/audio assets and projectile data; the LAN-enhanced branch does not contain that character. For the offline-first mod, Android-clean is therefore the provisional lead base, while LAN-enhanced changes will be reviewed as selective bug-fix patches rather than merged wholesale. This is a provisional engineering choice pending source integration and phone testing.


## Latest verified custom UI candidate (2026-10-10)

The latest successful build includes a new original Senki launcher icon, loading-screen background, and character-selection HUD background, while preserving the existing Cocos2d-x game and its selection logic. CI verifies both custom backgrounds are inside the APK and checks the package identity. [Open the successful build and download the artifact](https://github.com/kage049754/Senki/actions/runs/37971031426) — artifact `naruto-senki-v2-candidate-debug-apk`, 83,466,499-byte ZIP, expires 2026-10-23.

This is still a CI-built candidate, not phone-verified. See `PROGRESS.md` and `ROADMAP.md` for the exact status and remaining checks.


### Latest main-menu build
The main menu background has now been redesigned too. The existing game-mode carousel and menu callbacks are preserved. [Download the newest candidate artifact from successful Actions run 37971712613](https://github.com/kage049754/Senki/actions/runs/37971712613) — artifact `naruto-senki-v2-candidate-debug-apk`, 83,718,905-byte ZIP, expires 2026-10-23. CI confirms that the APK contains all three custom backgrounds and has the expected `Naruto Senki Mod` package identity. Device/gameplay testing is not yet confirmed.


### Newest verified artifact (2026-10-10)
The latest successful run is [37972501198](https://github.com/kage049754/Senki/actions/runs/37972501198), artifact `naruto-senki-v2-candidate-debug-apk` (ID `11637936223`, 83,729,869-byte ZIP, expires 2026-10-23). It includes the custom launcher icon and three custom screen backgrounds; CI verifies those assets and the app identity. The on-device visual/gameplay test is still pending.


## Latest verified central APK build (2026-10-10)

The latest central candidate build is [Actions run 38015483353](https://github.com/kage049754/Senki/actions/runs/38015483353), which completed **SUCCESS** on commit `5a0b8b2950eb3ab4a09e8744fd9d01f508983873`.

- Artifact: `naruto-senki-v2-candidate-debug-apk` (83,726,412-byte ZIP; SHA-256 `38e9900dae77eccee4120c61d03a1c87416b866837d70f72a83fa5057b2ef495`; expires 2026-10-24).
- Verified app identity: `com.senki.naruto.mod`, version `2.1.0-mod`, label `Naruto Senki Mod`.
- Verified the compiled Android manifest uses sensor-landscape orientation; the patch also handles `orientation|screenSize` configuration changes.
- Verified the APK contains the custom loading, character-selection, and main-menu background assets.
- Hardened the custom loading/menu/selection backgrounds with original-background fallbacks to reduce the risk of a blank screen if a custom image fails to load.

**Important scope:** the workflow clones the pinned Android-clean V2-derived source into a temporary CI workspace, applies this repository's ordered patches, builds the APK, and uploads it. The full external game source is not yet vendored into the central repo, and no physical-phone installation/gameplay has been verified. This is a real V2-derived candidate APK build, not the old Kotlin/Canvas prototype artifact and not a completed unified mod roster.


### Latest packaging verification — 2026-10-10

A further check was added specifically because an earlier APK was reported as invalid during installation. [Run 38015857617](https://github.com/kage049754/Senki/actions/runs/38015857617) completed **SUCCESS** after building the patched V2-derived APK and verifying its signature plus native Android libraries.

- Artifact: `naruto-senki-v2-candidate-debug-apk`, ID `11656381799`, ZIP size 83,732,890 bytes, SHA-256 `c9114464e52be0cefe7ad2c4a273e6f40441649a32d4a19a8e3137733fc3f9ff`, expires 2026-10-24.
- Android APK Signature Scheme v1 and v2: verified.
- Native libraries: `arm64-v8a` and `armeabi-v7a` both present.
- Sensor-landscape orientation, custom screen assets, and package identity checks: passed.

This removes some packaging-related uncertainty, but the APK still must be installed and tested on the actual phone before we can say the earlier install or blank-screen issue is fixed.


### Latest verified build with Lua validation — 2026-10-10

[Run 38016218553](https://github.com/kage049754/Senki/actions/runs/38016218553) completed **SUCCESS** on commit `a250c15d592bc06dad97e4d629c612c71b7808b4`.

- All game Lua scripts passed Lua 5.1 syntax validation.
- C++/Android Gradle build passed.
- Compiled manifest, custom UI asset packaging, package identity, APK signature, and `arm64-v8a` / `armeabi-v7a` native library checks passed.
- Artifact: `naruto-senki-v2-candidate-debug-apk`, ID `11655967631`, 83,749,269-byte ZIP, SHA-256 `3fe28a0f6f3282c2674e3ea8ecc9ca5bcaae6b440bd15aa708ac0f7a25cd06c6`, expires 2026-10-24.

The source roster inventory contains 37 unique selectable names; that is a source-level count, not a verified-playable count. Physical-device install, startup, character selection, and battle checks remain outstanding.


### Roster scalability groundwork — 2026-10-10

The existing character-selection screen no longer hardcodes exactly three pages. Patch `0008-dynamic-roster-pagination.patch` calculates the page count from the current character layout and uses numbered text page controls instead of requiring only three page-image assets. Lua syntax checks and the Android build passed in [run 38016671857](https://github.com/kage049754/Senki/actions/runs/38016671857); artifact ID `11655938596`.

This is groundwork for the user's 70+ roster goal, **not** a claim that 70 characters are already present. The inspected base currently lists 37 unique selectable names. The new pagination still needs phone testing with 4+ pages, and characters must be added and verified individually.


### Dynamic character pagination and expanded source research — 2026-10-10

The latest successful build is [run 38016671857](https://github.com/kage049754/Senki/actions/runs/38016671857), artifact `naruto-senki-v2-candidate-debug-apk` (ID `11655938596`, 83,752,290-byte ZIP). It includes the dynamic selection-pagination patch, passes Lua 5.1 syntax checks, and verifies the landscape manifest, APK signature, and both native ABIs.

Additional release-note research found potential character leads in [Zx-Akito's Naruto Senki release line](https://github.com/Zx-Akito/NarutoSenki-Release/releases): Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Might Guy, Yamato, Sasori, Zetsu, Iruka, Jirobo, Tayuya, Anko, and others. These are discovery leads only; the latest v1.26 release is APK-only and reports server-side processing, so it is not a direct offline V2 source base. The lead list is tracked in `docs/CHARACTER_ROSTER.md` and the compatibility notes in `docs/MOD_RESEARCH.md`.

The selected V2-derived base still has 37 unique selectable names. Pagination groundwork is built, but no additional character from those release leads has been ported or verified. The next goal is to locate editable source/resource sets and add compatible characters incrementally without replacing existing roster entries.
