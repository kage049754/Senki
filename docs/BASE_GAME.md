# Selected Senki Base — Naruto Senki V2

## User-confirmed direction

The user's chosen game target is **Naruto Senki: V2**, using the public release listing below as the reference/baseline release.

- **Release listing:** https://github.com/Naruto-Senki/files/releases
- **Selected reference:** v2.1.6-fix, published 2024-01-22.
- **Android release asset:** NSV2_2.1.6-fix_Android.apk (binary release asset, about 159 MB).
- **Specific release page:** https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix
- **Direct Android APK:** https://github.com/Naruto-Senki/files/releases/download/v2.1.6-fix/NSV2_2.1.6-fix_Android.apk
- **Editable source candidate:** https://github.com/Zx-Akito/NarutoSenki-V2
- **Source documentation:** https://github.com/Zx-Akito/NarutoSenki-V2/blob/master/Doc/README_ZH.md

The release host is described as a V2 file host and the release assets are packaged binaries. The APK is a download/reference point, not an editable source tree.

## Source audit result (2026-10-10)

The public Zx-Akito/NarutoSenki-V2 repository is a real source candidate, not merely an APK:
- Its root includes Cocos2d-x engine folders and C++/Lua game source structure.
- It contains projects/NarutoSenki/proj.android-studio, including Gradle build files and a Gradle wrapper.
- Its documentation describes the Android build flow and source/resource layout.
- Its repository metadata identifies it as a fork of real-re/NarutoSenki-V2-old; the parent was reported private.
- The repository has no root LICENSE, and GitHub metadata reports no declared license. Asset-specific permissions are also not documented in the files checked.

**Current decision:** technically promising, but **not approved for wholesale copying/import** until code and bundled asset permissions are clarified. Do not assume a public repository grants permission to redistribute Naruto characters, sprites, animations, sound, or music. See docs/ASSET_LICENSES.md.

The current source revision has not been proven to correspond exactly to the v2.1.6-fix APK. That comparison remains open.

## Central workspace

kage049754/Senki remains the single central integration workspace for all authorized source changes and mod integrations. When an approved mod character, skill, animation, fix, or other component is integrated, its source changes and provenance record belong here—not in a separate disconnected project.

## Required next steps

1. Resolve permission/license terms for V2 code and each asset set, or locate a source distribution with clear reuse terms.
2. Compare the source revision with v2.1.6-fix where possible.
3. Once the permission decision is documented, bring/adapt the existing V2 source into this repository while preserving provenance.
4. Build the original base before merging mods.
5. Do not continue developing the separate Kotlin/Canvas prototype as a new game. Decide whether to remove or retain its files only after the source import path is verified.
6. Do not commit the 159 MB APK or extracted APK contents into this repository as a substitute for editable source.

## Status

- User-selected target: **Naruto Senki V2**.
- Release reference identified: **v2.1.6-fix**.
- Editable source candidate located and structure inspected: **yes**.
- Source imported into kage049754/Senki: **no**.
- Code/asset reuse permission: **unresolved; permission required**.
- Exact source-to-release match: **not verified**.
- Unified modded build: **not built or verified**.

Do not describe the base as imported, built, or modded until those steps have actually happened.


## Additional V2-derived technical candidate (audited 2026-10-10)
`Wilykun/NarutoSenki-V2` is a candidate fork of `hitlabmodv2/NarutoSenki-V2`, with 15 commits ahead of that parent at the inspected comparison. It includes a successful Android CI workflow and a Spectate mode. Its own Actions run `37911640387` produced `NarutoSenki-debug-apk`; this artifact is evidence of the fork's build only, not of a build in the central repository or physical-device testing.

This may be a stronger technical base candidate than the previously inspected unbuilt V2 source fork, but the exact match to the selected `v2.1.6-fix` release is unverified and its repository has no declared license. Do not import or redistribute its code/assets until rights are clarified. The target remains the existing Naruto Senki V2 game.
