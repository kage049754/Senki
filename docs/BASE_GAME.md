# Selected Senki Base — Naruto Senki V2

## User-confirmed direction

The user's chosen game target is **Naruto Senki: V2**, using the official public release listing below as the reference/baseline release.

- **Release listing:** https://github.com/Naruto-Senki/files/releases
- **Current release found during audit:** `v2.1.6-fix`, published 2024-01-22.
- **Android release asset:** `NSV2_2.1.6-fix_Android.apk` (binary release asset, about 159 MB).
- **Specific release page:** https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix
- **Direct Android APK:** https://github.com/Naruto-Senki/files/releases/download/v2.1.6-fix/NSV2_2.1.6-fix_Android.apk
- **V2 source documentation candidate:** https://github.com/Zx-Akito/NarutoSenki-V2/blob/master/Doc/README_ZH.md

The releases repository is described as a **file host** and the inspected release assets are packaged binaries (Android APK, iOS IPA, Linux archive). This release page is therefore a download/reference point, not by itself an editable Android source project. Do not treat the APK as source code.

## What is the central workspace?

`kage049754/Senki` remains the single central workspace where all authorized source changes and mod integrations should be maintained. When an approved mod character, skill, animation, fix, or other component is integrated, its source changes and provenance record belong here—not in a separate disconnected project.

## Required next steps before calling the game integrated

1. Inspect the linked V2 source candidate and any canonical/upstream repository links from its documentation.
2. Verify the repository is accessible, contains the actual C++/Lua/Cocos2d-x game source and Android project, and determine its current commit/branch.
3. Compare its code/content to the `v2.1.6-fix` release where possible; do not assume the source tree exactly matches the binary release.
4. Inspect code license and asset-specific permissions. The file-host release has no license field in its repository metadata; do not assume that means redistribution/modification rights are granted.
5. Once source and permissions are understood, bring/adapt the chosen existing V2 source into this repository with provenance preserved, then build the original base before merging mods.
6. Do not continue developing the separate Kotlin/Canvas prototype as a new game. Decide whether to remove or retain its files only after the source-base import plan is verified.
7. Keep the release APK linked as the reference download. Do not commit the 159 MB APK/other packaged binaries into the source repository as a substitute for editable source. Only mirror binaries if the rights, repository policy, and distribution plan explicitly permit it.

## Status

- User-selected game target: **Naruto Senki V2**.
- Release reference identified: **v2.1.6-fix**.
- Release APK linked: yes, via the original release page.
- Editable source imported into `kage049754/Senki`: **not yet verified**.
- License/asset reuse permission: **not yet verified**.
- Unified modded build: **not yet built or verified**.

Do not describe the base as fully installed/imported or modded until those steps have actually happened.
