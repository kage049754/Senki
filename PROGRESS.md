# Senki Persistent Progress Tracker

Last updated: 2026-10-10

## Absolute project direction
**Mod and merge the existing Naruto Senki: V2 game only. Do not create a new game.**

- Central integration repository: https://github.com/kage049754/Senki
- User-selected game target: Naruto Senki: V2.
- Release listing: https://github.com/Naruto-Senki/files/releases
- Selected reference release: https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix
- Release APK asset: NSV2_2.1.6-fix_Android.apk (about 159 MB), hosted by the original release repository.
- All future mod changes that are approved and actually integrated must be committed into this central repo.
- The release APK is a packaged binary, not editable source. Source license and asset reuse terms still need resolution.
- Do not continue building the standalone Kotlin/Canvas prototype as a separate game.

## Source audit findings (2026-10-10)
- [x] Located a public, editable V2 source candidate: https://github.com/Zx-Akito/NarutoSenki-V2
- [x] Verified its root includes Cocos2d-x engine directories, C++/Lua project structure, build scripts, and projects/NarutoSenki/proj.android-studio with Gradle wrapper/build files.
- [x] Verified the V2 documentation describes Android Studio build steps and the C++/Lua/resource structure.
- [x] Verified the source repo is a fork whose parent is real-re/NarutoSenki-V2-old (private in repository metadata); latest visible source commits inspected are from 2026-05-09.
- [x] Checked for a root LICENSE; none was found, and GitHub repository metadata reports no license.
- [x] Inspected Android build configuration: Android Gradle Plugin 3.3.3, Gradle 5.6.4, compile SDK 31, min SDK 21, and legacy NDK toolchain 4.9 request.
- [ ] Establish permission/license terms for the game code and especially Naruto artwork, sprites, audio, animations, and other bundled assets.
- [ ] Verify the exact source revision's relationship to the selected v2.1.6-fix release.
- [ ] Import/adapt source into this central repo after rights and import strategy are resolved.
- [ ] Build the imported base before mod integration.
- [ ] Integrate requested mods/characters in verified batches.
- [ ] Verify a unified modded APK artifact and device behavior separately.

**Decision:** the V2 source candidate is technically credible and has the expected Android project, but it is not yet safe to copy wholesale into this repo because the repository has no declared license and asset permissions are not established. Keep it as a source/reference candidate until terms are clarified; do not infer permission from public visibility.

## Fan-project license and build labeling
- [x] Added root LICENSE scoped only to original contributions made for this repository.
- [x] Added NOTICE.md explaining fan-made/non-commercial intent without claiming third-party rights.
- [x] Added docs/V2_BUILD_AUDIT.md with source structure and Android toolchain risks.
- [x] Renamed the existing Actions workflow/artifact so prototype success cannot be mistaken for a V2 build.

## Current project contents and cautions
The repo previously received a native Kotlin/Canvas prototype scaffold. It is not the intended final foundation. The successful Actions run 37963412816 completed on commit 3b10909d5cc66b6348f2f3308ccf42e5f238bc96 and uploaded `senki-prototype-scaffold-debug-apk` (823,054 bytes; SHA-256 reported by GitHub for the ZIP: bc67abc87ae1bf7889f7b2c4aca4385b3cb6c40e529dbb7e4fb8ff7f496d9af5). This is a prototype scaffold debug APK, not a verified Naruto Senki V2 build or unified modded APK. It must not be represented as the requested final game.

## Next actions
1. Resolve code and asset permission terms for the V2 source candidate or locate a source distribution with clear reuse terms. Fan-made/non-commercial status does not itself remove this requirement.
2. Verify source compatibility with the selected release where possible.
3. After permission is resolved, import/adapt the existing V2 source into kage049754/Senki with provenance preserved.
4. Establish a compatible legacy Android/NDK build environment, build/verify the original base, then merge mods.
5. Keep CI reporting explicit about whether a run builds the prototype scaffold or the real V2 source.

## CI and APK status
- Run 37963412816: **SUCCESS** — https://github.com/kage049754/Senki/actions/runs/37963412816
- Job `inspect-and-build`: completed successfully. The configuration validation, debug APK build, APK existence check, and artifact upload all succeeded.
- Artifact `senki-prototype-scaffold-debug-apk`: verified present, 823,054 bytes, artifact ID 11631953325, expires 2026-10-23.
- This successful run builds only the existing prototype scaffold. It is **not** Naruto Senki V2, not a merged mod, and not a device-tested final game.
- Run 37963389348 was cancelled by the newer run because workflow concurrency cancels an older run on the same branch. It did not produce an artifact.
- Unified mod APK artifact: not built or verified.
- Physical-device installation/gameplay: not verified.

## Session log
- Updated project documentation to make Naruto Senki V2 the explicit target.
- Audited Zx-Akito/NarutoSenki-V2: verified C++/Lua/Cocos2d-x layout and Android Gradle project; confirmed no declared repository license.
- Identified that copying source/assets into this central repo requires resolving permissions first.
- Rechecked the latest workflow and verified its result/artifact; success applies only to the prototype scaffold, not the V2 target.
- Rechecked the latest source build files: the old Gradle/AGP and NDK settings require a compatible legacy build environment once a permitted source copy is available.

## Reminder
**Every session: work toward Naruto Senki V2 in kage049754/Senki. If adding a character/mod, integrate it into the existing V2 game here. No separate new game. Never call a prototype build the final Senki build.**


## Additional mod repository audit — 2026-10-10
- [x] Re-ran GitHub repository search for Naruto Senki mod/source projects.
- [x] Inspected metadata and the root tree of `LeaderOnePro/NarutoSenki1.17Mod`.
- Finding: the repository is a package/decompiled distribution with `AndroidManifest.xml`, `classes.dex`, `resources.arsc`, `META-INF/`, `lib/`, `res/`, and `assets/`, rather than an editable Cocos2d-x/C++ source project.
- Finding: no declared GitHub license was reported; bundled game assets remain uncleared.
- [x] Added the candidate classification, permission status, and next audit targets to `docs/MOD_RESEARCH.md` in commit `bc6f22531fa0c709043c462a5384518eacec3ecb`.
- [ ] Compare the similar `wsnbbnbb/NarutoSenki1.17Mod` repository with this candidate to establish whether it is a duplicate/mirror.
- [ ] Inspect `LeaderOnePro/NarutoSenki` editable source candidate in detail, including its source tree, Android build support, and license/asset notices.
- [ ] Resolve V2 source and asset permission before import; then establish a real V2 build and begin controlled, verified merges.

**Important:** this search pass did not produce a permission-cleared source base or a new APK. The latest successful CI still builds only the prototype scaffold, not Naruto Senki V2. No modded character has been counted as integrated or verified.


## Fourth-pass source comparison — 2026-10-10
- [x] Inspected `LeaderOnePro/NarutoSenki` metadata, README, source tree, and resource directories.
- [x] Confirmed it contains editable legacy C++ game systems under `Classes/` and game resources under `Resources/`.
- [x] Confirmed its README documents Cocos2d-x 2.2.2 and Visual Studio 2010, not a verified modern Android build path.
- [x] Compared `wsnbbnbb/NarutoSenki1.17Mod` metadata/history against `LeaderOnePro/NarutoSenki1.17Mod`; GitHub marks it as a fork and inspected history shows the same two commits, so it is not counted as an independent mod.
- [x] Recorded both findings in `docs/MOD_RESEARCH.md` (latest research commit `c86df00189fba1903c9e4552554dd566c2962ac0`).
- [ ] Continue searching for additional editable, permission-cleared V2-compatible source/mods.
- [ ] Resolve code and asset rights for the selected V2 source before import; build the real V2 base and then start verified merges.

**Decision unchanged:** `LeaderOnePro/NarutoSenki` is reference-only due its older Windows-focused build path and unresolved rights. The selected target remains Naruto Senki V2. No external code/assets were imported, no character was merged, and no final V2 APK was produced in this pass.
