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


## V2-derived fork with real CI — 2026-10-10
- [x] Found and inspected `Wilykun/NarutoSenki-V2`, a V2-derived fork of `hitlabmodv2/NarutoSenki-V2`.
- [x] Compared its history to its parent: 15 commits ahead, including changes to game-mode logic/UI, Spectate mode, resources, and Android build workflow.
- [x] Verified the fork's own Actions run `37911640387` completed successfully; JDK/SDK/NDK setup, `assembleDebug`, and artifact upload all passed.
- [x] Verified fork artifact `NarutoSenki-debug-apk` exists (86,137,495 bytes; SHA-256 `9400c4d1db9b3f09630824a27656160e737876e3383ad234340a87082c3585e6`; expires 2027-01-07).
- [x] Recorded the technical candidate in `docs/MOD_RESEARCH.md` (commit `f8c637f50fc95cd19e1131e41dc31a740d075599`).
- [ ] Verify the fork's exact relationship to the selected v2.1.6-fix release and inspect full build documentation.
- [ ] Resolve source and asset permissions before adopting/copying the fork into the central repo.
- [ ] Once permitted, build the chosen V2 base inside `kage049754/Senki`; do not count another repository's successful artifact as this repo's build.


## Android-only V2 clean-base candidate — 2026-10-10
- [x] Inspected `muhammadadilsyaputra08-alt/NarutoSenki-Custom` README and root tree; it describes an Android-only V2-derived Cocos2d-x 2.2.6/C++/Lua base.
- [x] Verified its latest inspected Actions run `34331260360` succeeded through SDK/NDK setup, `assembleDebug`, APK discovery, and artifact upload.
- [x] Verified artifact `narutosenki-debug-apk` exists (83,468,934 bytes; SHA-256 `5704b77cdd63369b83e74febc03d640628220e4512d43f12832063522ce72271`; expires 2026-12-08).
- [x] Added the candidate and CI evidence to `docs/MOD_RESEARCH.md`.
- [ ] Compare this Android-only source snapshot with `Wilykun/NarutoSenki-V2` and the selected v2.1.6-fix release.
- [ ] Resolve code/asset rights and provenance before import.
- [ ] Once approved, select one base, port it into `kage049754/Senki`, and make the central repo's own V2 build succeed before adding more mods.


## Additional local PvP/co-op candidate — 2026-10-10
- [x] Inspected `likill/NarutoSenki-master` README, metadata, root tree, recent commits, and release metadata.
- Finding: legacy Cocos2d-x 2.2.2 / Visual Studio 2010 source with Windows-oriented release; recent work documents local PvP/co-op, UI sizing, and control remapping.
- Classification: reference-only for feature research; not a verified Android/V2 source base and no declared license.
- [x] Added a comparative candidate matrix to `docs/MOD_RESEARCH.md`.
- [ ] Continue with permission/provenance review and a single-base decision; no full-repository merges or asset extraction.


## Latest documentation pass — 2026-10-10
- [x] Updated `README.md` with the current V2 source-candidate findings and clear separation between external candidate artifacts and this repo's prototype artifact. README commit: `7da15f308ab4a3bf0486f062b9242e76d0c0b5a7`.
- [x] Updated the roadmap, base notes, mod inventory, and permission register with the candidate comparison.
- [x] Rechecked the central repository's Actions list after the documentation updates. No newer central V2 build exists; the latest central workflow remains run `37963412816`, which builds only the prototype scaffold. Documentation-only commits did not trigger the prototype workflow's path filters.
- [ ] The project is not at the final game stage: source/asset permission and provenance are still blocking actual base import, central V2 build, mod merges, and device verification.


## Actual V2 source build attempt added — 2026-10-10
- [x] Added `.github/workflows/v2-source-smoke.yml` in commit `6a39f56bae357e8720a506c22fbb7b8fceeddc5a`.
- The workflow checks out a **pinned** revision of `muhammadadilsyaputra08-alt/NarutoSenki-Custom` into a temporary CI workspace, verifies the Android project structure, provisions the documented legacy SDK/NDK/JDK versions, and attempts `assembleDebug`.
- It deliberately does **not** upload or release the candidate APK. It is a build-feasibility diagnostic, not the integrated central game build and not device testing.
- Run `37965089554` failed before compilation because setup-android tried to install the obsolete `tools` SDK package; that provisioning error was fixed in `b6b9f83913f14445df1e5fbf558e42a5cf03a0a3`.
- [x] Run `37965165366` completed **successfully** on 2026-10-09. The pinned candidate's Android project built with `assembleDebug`, and the workflow verified that an APK existed in the temporary runner workspace.
- This confirms build feasibility for the candidate revision only. The APK was **not uploaded**, the candidate source was **not merged** into `kage049754/Senki`, and no physical-device test was performed.
- Rights/provenance remains a distribution consideration; it is not being used as a reason to stop researching or running private build diagnostics.


## First V2 smoke-test failure and fix — 2026-10-10
- Run `37965089554` failed **before compilation**, during `android-actions/setup-android@v3`. Actual logs show it attempted to install the obsolete SDK package `tools` and reported `Warning: Failed to find package 'tools'`, then `sdkmanager ... failed with exit code 1`.
- This was a workflow provisioning error, not a C++/Lua source compilation error.
- [x] Fixed `.github/workflows/v2-source-smoke.yml` in commit `b6b9f83913f14445df1e5fbf558e42a5cf03a0a3` by configuring setup-android to install only `platform-tools`; the workflow explicitly installs the required SDK platform/build-tools/NDK afterward.
- [x] New run `37965165366` triggered for the fix.
- Last poll: run is still **in progress** while setting up Java 17; no second-run build result confirmed yet.
- [ ] Continue polling; if provisioning succeeds, inspect the actual Gradle build result. If it fails, read the next failure log and repair the actual cause before rerunning.


## User direction — continue broader Senki source search — 2026-10-10
- [x] User clarified they want us to continue looking for other Naruto Senki sources/mods, including repositories outside GitHub, rather than repeatedly stopping at the permission caveat.
- [ ] Compare additional candidates by Android buildability, game version, mod features, source completeness, and documented permissions. Keep candidates separate until a practical base is chosen; do not claim public visibility alone grants redistribution rights.


## Continued work — additional V2 candidates and artifact pipeline (2026-10-10)

- [x] Updated the central candidate-build workflow in commit `fe22f50b802b798802a06c383b8e91e726dd2e09` to upload the compiled V2-derived debug APK as a 14-day Actions artifact after a successful build.
- [x] Expanded source discovery and found the additional `sansaks-jpg/NarutoSenki-V2` candidate. Its public history shows an Android-capable Cocos2d-x V2 source tree, 59 recorded Actions runs, a latest visible successful run on 2026-09-15, and newer LAN multiplayer fixes worth diffing. Its license remains undeclared.
- [x] Classified `SILXNTRAY` and `hitlabmodv2` as likely mirror/fork lineage pending diff, and identified older Zx-Akito-derived forks as lower-priority comparison candidates.
- [ ] Verify a new central Actions run for commit `fe22f50b802b798802a06c383b8e91e726dd2e09` and confirm the uploaded artifact is actually present. The existing successful run `37965165366` predates this workflow change and had no artifact upload.
- [ ] Compare `sansaks-jpg`'s changes against the pinned build-tested source and decide which Android base is strongest.
- [ ] No source has yet been imported into the central repo; no unified modded APK or phone gameplay has been verified.


### Candidate build loop result — 2026-10-10
- Run `37966549532` was superseded/cancelled after its Gradle build began printing repeated legacy SDK repository XML parse errors (including invalid `api-level` values such as `34x` and unsupported `base-extension` / `extension-level` elements). No artifact was produced by that attempt.
- Fixed the runner setup in commit `fcccc784c39f0f33c041c4d00bb39b3408ccaef9`: install the required legacy Android SDK/NDK packages into an isolated SDK root, then point `ANDROID_HOME` and `ANDROID_SDK_ROOT` at that root so preinstalled/newer platform metadata does not break the old Gradle plugin.
- Run `37966861114`: **SUCCESS** on commit `fcccc784c39f0f33c041c4d00bb39b3408ccaef9`. All steps passed: pinned source checkout, isolated SDK provisioning, Gradle build, APK existence check, and artifact upload.
- Verified artifact: `naruto-senki-v2-candidate-debug-apk`, artifact ID `11634177274`, ZIP size 83,435,979 bytes, expires 2026-10-23. Open the [successful Actions run](https://github.com/kage049754/Senki/actions/runs/37966861114) and download the artifact card.
- Scope: this is a successfully compiled debug APK of the pinned external V2-derived candidate in CI. It is not yet source-integrated into this repo and has not been physically installed or gameplay-tested on the user's phone.


## Second V2 candidate build — 2026-10-10
- [x] Added `.github/workflows/v2-lan-candidate.yml` in commit `6cc298c6791a42f00aa4a3ec968705255f95a4a7` to build the feature-rich `sansaks-jpg/NarutoSenki-V2` branch at pinned commit `1751b7fb8f05a96ff6e85bc8a6c8e3fdcca3f74a`.
- [x] GitHub Actions run `37967514487`: **SUCCESS**. Source checkout, Java 8 + NDK r17c setup, release APK build, APK existence check, and artifact upload all passed.
- [x] Verified artifact `naruto-senki-v2-lan-candidate-apk`, artifact ID `11633633661`, ZIP size 80,405,874 bytes, expires 2026-10-23. Download from the [successful LAN candidate Actions run](https://github.com/kage049754/Senki/actions/runs/37967514487).
- [x] Source diff review confirmed this branch adds LAN hotspot multiplayer and hardening, including reliable state/order handling, app-background forfeits, crash-safe pause/gear/game-over cleanup, and runtime UI localization. It retains the original Cocos2d-x C++/Lua game foundation.
- [ ] Compare its gameplay/resource baseline with the Android-clean candidate before deciding which source tree becomes the central base.
- [ ] APK install and actual gameplay on the user's phone are still unverified. Both verified CI artifacts are candidate builds, not the unified final mod.



## Direct source-tree comparison — 2026-10-10
- Compared recursive Git trees for Android-clean commit `279e85e73040558c84988a0eea310b6286eb77f0` and LAN-enhanced commit `1751b7fb8f05a96ff6e85bc8a6c8e3fdcca3f74a`.
- Tree sizes: Android-clean 1,903 tracked files; LAN-enhanced 2,618. Of 1,886 common paths, 1,828 have identical blob hashes and 58 differ. The LAN tree has 732 paths not present in the Android-clean tree, largely desktop/platform content plus LAN networking. Android-clean has 17 unique paths.
- Important roster finding: Android-clean uniquely contains `Classes/Core/Shinobi/Kabuto.hpp`, `Bunshin/KabutoClone.hpp`, Kabuto sprite/plist/XML assets, Kabuto audio, and projectile data. The inspected LAN-enhanced branch does not contain `Kabuto.hpp`. The Android-clean README calls it a clean base, but it contains this substantive custom Kabuto redesign and is not simply an untouched vanilla snapshot.
- Practical direction: **use the successfully built Android-clean source as the current lead candidate** for an Android/offline-first mod base because it is smaller and preserves the unique Kabuto content. Treat LAN-enhanced V2 as a source for selective crash fixes and optional networking research, not a wholesale replacement. Do not copy all 58 changed files at once; review and port individual fixes with tests.
- This is a provisional engineering recommendation based on tree/build evidence, not yet the final source import. Both candidates have successful central CI artifacts; neither has been tested on the user's phone.



## First central source patch successfully built — 2026-10-10
- [x] Added `patches/android-clean/0001-custom-app-identity.patch` (commit `e7afac52b3f1ee838e96a3705d8891b7e63b4e42`). It changes the Android application ID to `com.senki.naruto.mod`, version to `2.1.0-mod` / code 3, and launcher label to `Naruto Senki Mod`.
- [x] Updated `.github/workflows/v2-source-smoke.yml` to require and apply the ordered central patch series before building, then inspect the actual APK with `aapt dump badging` and assert the custom package/version/label.
- [x] Run `37968632537`: **SUCCESS** on commit `c07abc442d8b2e5ceab542fe999c67fecb09dddd`. The patch-application step passed, Gradle reported `BUILD SUCCESSFUL`, APK existence passed, and package identity assertions passed.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, artifact ID `11634478692`, ZIP size 83,447,929 bytes, expires 2026-10-23. Download from the [successful patched candidate run](https://github.com/kage049754/Senki/actions/runs/37968632537).
- This is the first central patch applied to the pinned existing V2-derived source and verified in the resulting APK. The upstream source is still fetched into a temporary CI workspace rather than fully vendored into this repo; the game has not yet been installed or tested on the user's phone.


## Custom launcher, loading screen, and character-selection pass — 2026-10-10
- [x] Added editable vector art in `artwork/senki-launcher.svg`, `artwork/senki-launcher-foreground.svg`, `artwork/senki-loading.svg`, and `artwork/senki-select.svg`.
- [x] Added `patches/android-clean/0002-custom-loading-screen.patch`: the existing Cocos2d-x loading layer now uses the custom 16:9 loading artwork while retaining the original character tips and loading animation.
- [x] Added `patches/android-clean/0004-custom-character-select-background.patch`: the character-pick screen now uses a custom dark HUD layout, but preserves the existing character grid, hero preview/name, paging, selection rules, skill/ranking buttons, and start-game action.
- [x] The workflow renders SVG sources into game PNG assets and Android launcher densities; it also uses a dark navy adaptive-icon background.
- [x] Strengthened CI to verify the actual APK archive contains both `assets/senki_loading.png` and `assets/senki_select.png`, and checks the package ID/version/app label.
- [x] Latest run `37971031426`: **SUCCESS**. All patches applied, art rendered, Gradle build passed, both custom backgrounds were found inside the APK, package identity checks passed, and the artifact uploaded.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11636815575`, ZIP size 83,466,499 bytes, expires 2026-10-23. Download from the [successful custom-UI build](https://github.com/kage049754/Senki/actions/runs/37971031426).
- [ ] Still required: install on the phone and inspect the loading screen, character-selection layout, touch targets, portrait/landscape behavior, and actual battle flow. CI proves packaging and asset presence, not visual/runtime correctness.


## Main menu redesign build — 2026-10-10
- [x] Added editable main menu artwork `artwork/senki-menu.svg` and `patches/android-clean/0005-custom-main-menu-background.patch`.
- [x] The existing main menu now uses the custom Senki background while retaining the original game-mode carousel, button actions, credits/training/exit callbacks, and menu flow.
- [x] The workflow renders and verifies `senki_menu.png` alongside the loading and selection backgrounds.
- [x] Latest run `37971712613`: **SUCCESS**. Patch application, SVG rendering, Gradle build, package identity verification, and APK archive checks all passed.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, artifact ID `11637705354`, ZIP size 83,718,905 bytes, expires 2026-10-23. Download from the [successful main-menu build](https://github.com/kage049754/Senki/actions/runs/37971712613).
- [ ] Physical phone validation remains outstanding. The CI archive now contains all three custom screens, but visual placement, button overlap, and touch behavior still need a real device check.


## Latest verification — selection instructions and complete custom UI asset set (2026-10-10)
- [x] Updated the selection background's instruction text to make the existing interaction explicit: tap once to preview, tap again to confirm.
- [x] Latest run `37972501198`: **SUCCESS** on commit `ca54dc7f7b199ce85d3c5dceffe81493cc09a3f0`.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11637936223`, ZIP size 83,729,869 bytes, expires 2026-10-23.
- [x] Confirmed the APK archive contains all three custom screen backgrounds and that package identity checks pass.
- [ ] On-device install, visual layout, actual touch behavior, and battle regression tests remain unverified.


## Landscape stability hardening — 2026-10-10

- [x] Reviewed the pinned Android manifest: the game already starts in `sensorLandscape`, matching the requested landscape gameplay.
- [x] Added `patches/android-clean/0007-landscape-config-stability.patch` to handle both `orientation` and `screenSize` configuration changes, reducing the risk of Android recreating the game activity during display-size/orientation configuration updates.
- [x] Updated the central candidate build workflow to assert the manifest retains `sensorLandscape` and `orientation|screenSize`, then inspect the compiled APK manifest for the sensor-landscape value.
- [ ] Current verification run `38015169691` is in progress on commit `8d31f68ae4912078266a207ade5bbe05cfc4b8b8`. The previous run for the manifest patch alone was cancelled by the newer workflow commit before completing; wait for the latest run and inspect any failure logs before counting this change as built.
- [ ] Device rotation/touch/gameplay still requires phone testing. CI checks the compiled manifest, not real hardware behavior.


## Blank-screen fallback hardening — 2026-10-10

- [x] Reviewed custom loading, menu, and character-selection background patches after the earlier blank-after-intro report.
- [x] Updated the loading and main-menu C++ patches to fall back to the original `red_bg.png` if the custom PNG cannot be loaded, rather than returning `false` and aborting scene initialization.
- [x] Updated the Lua character-selection patch to fall back to `blue_bg.png` and guard the background sprite before applying layout calls.
- [x] Corrected unified-diff hunk counts after editing the patch files; the latest workflow's “Apply central Senki patches” step passed, confirming the patch series applies cleanly to the pinned source.
- [ ] Latest run `38015483353` is still in progress. Wait for the final APK build, landscape manifest verification, and artifact upload before marking this fallback hardening as fully build-verified.
- [ ] This improves failure tolerance but does not prove the user's earlier blank-screen issue is fixed on-device; real launch and menu navigation still need phone testing.


## Latest central build verified — 2026-10-10

- [x] Run `38015483353` completed **SUCCESS** on commit `5a0b8b2950eb3ab4a09e8744fd9d01f508983873`: [open run](https://github.com/kage049754/Senki/actions/runs/38015483353).
- [x] The ordered central patch series applied successfully, including the new fallback backgrounds and landscape stability patch.
- [x] Gradle reported `BUILD SUCCESSFUL in 2m 26s`.
- [x] The compiled APK manifest verified `android:screenOrientation=0x6` (sensor landscape), and the source manifest check verified `orientation|screenSize` handling.
- [x] APK checks passed for package `com.senki.naruto.mod`, version `2.1.0-mod` / code 3, app label `Naruto Senki Mod`, and all three packaged backgrounds: `assets/senki_loading.png`, `assets/senki_select.png`, `assets/senki_menu.png`.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11655846337`, ZIP size 83,726,412 bytes, SHA-256 `38e9900dae77eccee4120c61d03a1c87416b866837d70f72a83fa5057b2ef495`, expires 2026-10-24. Download from the [successful build's artifact card](https://github.com/kage049754/Senki/actions/runs/38015483353).
- [ ] This remains a CI-built APK assembled from the pinned external V2-derived source plus central patches in a temporary workspace; the full game source has not been vendored into the central repository.
- [ ] No physical phone install/gameplay result has been reported yet. Blank-screen fallback changes are compile/package verified, but actual launch behavior still needs device testing.


## APK installability checks — 2026-10-10

- [x] Added a CI step to verify the final debug APK signature with Android `apksigner` and require native libraries for supported ABIs.
- [x] One attempted workflow edit produced invalid YAML before GitHub created a job (run `38015821546`, named after the workflow file and with no job records). Rebuilt the workflow tail cleanly in commit `d3dbf83f6bc1ada8eb9b43504b540876402f4768`.
- [x] Run `38015857617`: **SUCCESS** on commit `d3dbf83f6bc1ada8eb9b43504b540876402f4768`. All patches applied; Gradle build passed; package, custom assets, sensor-landscape manifest, APK signature, and native ABI checks passed.
- [x] Signature check: APK Signature Scheme v1 and v2 verified. Native libraries verified for both `arm64-v8a` and `armeabi-v7a` (`libcocos2dcpp.so`, `libc++_shared.so`).
- [x] Verified latest artifact `naruto-senki-v2-candidate-debug-apk`, ID `11656381799`, ZIP size 83,732,890 bytes, SHA-256 `c9114464e52be0cefe7ad2c4a273e6f40441649a32d4a19a8e3137733fc3f9ff`, expires 2026-10-24. See [run and artifact card](https://github.com/kage049754/Senki/actions/runs/38015857617).
- [ ] Signature/native checks reduce packaging uncertainty, but they do not prove installation on the user's specific Android device. Phone install and gameplay still need to be checked.


## Lua syntax and installability checks verified — 2026-10-10

- [x] Added a Lua 5.1 syntax pass across every game script after the patch series is applied.
- [x] Run `38016218553`: **SUCCESS** on commit `a250c15d592bc06dad97e4d629c612c71b7808b4`; all source patches applied, all Lua scripts passed `luac5.1 -p`, Gradle build passed, and APK identity/landscape/signature/native-ABI checks passed.
- [x] Gradle reported `BUILD SUCCESSFUL in 3m 11s`.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11655967631`, ZIP size 83,749,269 bytes, SHA-256 `3fe28a0f6f3282c2674e3ea8ecc9ca5bcaae6b440bd15aa708ac0f7a25cd06c6`, expires 2026-10-24. [Open the run and artifact card](https://github.com/kage049754/Senki/actions/runs/38016218553).
- [x] Added an exact source-level roster inventory: 37 unique selectable names in the pinned Android-clean candidate. This is not a count of device-verified playable characters.
- [ ] Next: continue mod-source discovery and compare per-character class/config/resource sets for unique additions; then integrate one compatible character at a time and build.
- [ ] Physical install, launch after engine intro, selection, and battle remain unverified on the user's phone. Syntax/build/signature checks cannot replace runtime testing.


## Dynamic roster pagination patch built successfully — 2026-10-10

- [x] Found and removed the fixed three-page limit in the existing Senki character-selection Lua layer.
- [x] Added `patches/android-clean/0008-dynamic-roster-pagination.patch`: page count is now calculated from `#ns.CharactersLayout / 21`, and numbered page controls use text labels rather than only the three hardcoded `page1/page2/page3` sprite frames.
- [x] CI asserts the fixed `self.pageNum = 3` line is gone and the dynamic count/text-label implementation is present.
- [x] Lua 5.1 syntax validation passed after applying the patch.
- [x] Run `38016671857`: **SUCCESS** on commit `c2820ec8449d3dedfb62c437ee647b82b20969e2`; Gradle reported `BUILD SUCCESSFUL in 2m 25s`; landscape, app identity, screen assets, APK signature, and native ABI checks passed.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11655938596`, ZIP size 83,752,290 bytes, SHA-256 `7072d0a89ad6d41afe25e62ef12004cdd919cafffaf85d3ee5915a8a91603c1c`, expires 2026-10-24. [Open successful run and artifact](https://github.com/kage049754/Senki/actions/runs/38016671857).
- [ ] Runtime pagination still needs phone testing with more than three pages of actual character entries. The change removes the fixed cap in source; it does not yet add search/filtering or prove 70+ characters are fully implemented.


## Additional mod-source discovery — 2026-10-10

- [x] Audited more V2 forks and found most older forks share the same 41-header baseline; none of the inspected older V2 forks exposed a new complete selectable roster beyond the Android-clean candidate's unique Kabuto.
- [x] Inspected the public release host for Naruto Senki v1.26 beta 1/2. Release notes identify additional character leads: Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Might Guy, Yamato, Sasori, Zetsu, Iruka, Jirobo, Tayuya, Anko, and others.
- [x] Classified the v1.26 release as APK-only and server-side-processing-dependent; it is not a direct offline V2 source base. The release notes are discovery evidence only, not implementation evidence.
- [x] Added these names to `docs/CHARACTER_ROSTER.md` as DISCOVERED leads, separate from the 37-name source inventory and from verified playable characters.
- [ ] Continue looking for editable C++/Lua/resource sets for these characters; prioritize an additive port that does not replace existing roster slots.


## Dynamic roster pagination build verified — 2026-10-10

- [x] Fixed the source UI's hard-coded three-page roster limit in `patches/android-clean/0008-dynamic-roster-pagination.patch`.
- [x] Character page count now derives from the actual `ns.CharactersLayout` list at 21 slots/page; numbered page controls replace reliance on the original page-specific sprite pairs.
- [x] Added CI assertions proving the dynamic expression is present and the old `self.pageNum = 3` cap is absent.
- [x] Run `38016671857`: **SUCCESS**, commit `c2820ec8449d3dedfb62c437ee647b82b20969e2`. Lua 5.1 syntax checks, dynamic pagination assertion, landscape manifest, Gradle build, package identity, signature, and both native ABIs passed.
- [x] Latest artifact: `naruto-senki-v2-candidate-debug-apk`, ID `11655938596`, ZIP size 83,752,290 bytes, SHA-256 `7072d0a89ad6d41afe25e62ef12004cdd919cafffaf85d3ee5915a8a91603c1c`, expires 2026-10-24. [Run 38016671857](https://github.com/kage049754/Senki/actions/runs/38016671857).
- [ ] Dynamic pagination is source/build verified, but actual page navigation and selecting characters still need phone runtime testing.


## Search/filter selection UI built and packaged — 2026-10-10

- [x] Added `scripts/apply_character_search.py` so the search enhancement is applied with exact, checked source replacements instead of a brittle large unified-diff hunk.
- [x] Added a search field to the existing character-selection screen, case-insensitive name filtering, automatic navigation to the first page with a match, hiding empty pages during a search, and a “No characters found” message.
- [x] Kept the selection cursor hidden when its character is filtered out and restored it when a visible character is selected. Moved the search field left so it does not overlap the ranking button.
- [x] Added a final APK check that extracts the packaged `SelectLayer.lua` and asserts the filter method, no-results text, and corrected search-field position are really inside the APK.
- [x] Run `38018448399`: **SUCCESS** on commit `f1d5efe0841d55c4c3e5f91edf4f5c5f403ca1b2`; Lua syntax, dynamic pagination, landscape, package identity, APK signature, native ABI, and packaged search code checks all passed.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11657656484`, ZIP size 83,699,768 bytes, SHA-256 `51faf000d5ff9ef9027f351db0915f5aed58590ccd57f698392a8e1b2b9a3305`, expires 2026-10-24. [Open run and artifact card](https://github.com/kage049754/Senki/actions/runs/38018448399).
- [ ] Search/filter behavior and 4+ pages still need real-device testing. CI proves the code is packaged and parses; it cannot prove Android keyboard events or Cocos2d touch behavior.

## Complete playable-character requirements recorded — 2026-10-10

- [x] Added the per-character completeness standard to README and AI agent instructions: selection portrait/name, preview and actual skill information where supported, model/sprites, animations, movement, attacks, skills, effects/sounds, player controls, AI, resource references, and roster registration.
- [x] Added the requested kill/death feedback requirement: show the real killer and victim with their portraits/names when supported by the existing battle-event system, while preserving score/game-over behavior and correctly attributing AI/ally kills.
- [x] Added a roadmap checklist for character implementation, runtime tests, kill/death UI, and pagination visual/touch consistency.
- [x] Clarified that discovered, ported, build-verified, and gameplay-verified are different states. A portrait or roster name alone is not a complete playable character.
- [x] Documented the UI expectation that pages 1–3 retain their original image-based controls and pages 4+ receive matching image-based normal/selected buttons rather than text-only clickable replacements.
- [ ] These are now explicit implementation requirements; this documentation update does not claim that new characters or kill/death overlays have already been implemented or phone-tested.



## User-requested original background rollback and character profile requirements — 2026-10-10

**Requested background behavior:** restore the original background/decorative interface for the main menu containing Training / Network / Exit, and restore the original character-selection background. The loading background is separate and is not included in this rollback.

- [x] Updated the central build workflow to exclude the retired custom main-menu and character-selection background patches.
- [x] Removed generation and APK assertions for senki_menu.png and senki_select.png; custom loading artwork remains separate.
- [x] Confirm the retired `0004-custom-character-select-background.patch` and `0005-custom-main-menu-background.patch` files are absent from the current tree; the workflow excludes them and the generated `senki_menu.png` / `senki_select.png` assets.
- [x] Fresh Actions run `38019992304` completed successfully and uploaded the candidate APK artifact (artifact ID `11657109973`).
- [ ] Inspect the APK's packaged assets explicitly to confirm the custom menu/selection replacement PNGs are absent.
- [ ] Install on the phone and visually confirm both original backgrounds and their decorative layers are restored.

**Character completion contract:** every new character must have the right portrait/name and selection preview; actual skill details where supported; sprites/model, animations, movement, basic attacks, hit detection, skills/cooldowns, effects/audio, player controls, AI, and correct IDs/resource paths. For kills/deaths, inspect existing engine hooks and show the actual killer/victim portrait and name when feasible. These are planned acceptance criteria, not a claim that the feature is already implemented. A character counts as playable only after gameplay tests, and CI success alone does not prove the visual rollback or gameplay.


## Latest verified CI run — original background rollback build (2026-10-10)

- Run: [38019992304](https://github.com/kage049754/Senki/actions/runs/38019992304), workflow run #64.
- Commit: `e874e45d90f7e83082ff55b304bdb6f49f82fe65` — `Remove retired custom menu and selection artwork`.
- Result: **SUCCESS**; all 23 substantive build/verification steps passed, including all Lua syntax, search/filter behavior, dynamic pagination, landscape settings, Gradle build, APK identity, signature, ABI packaging, and artifact upload.
- Artifact: `naruto-senki-v2-candidate-debug-apk`, ID `11657109973`, 83,344,194-byte ZIP, SHA-256 `07c153b870d5a56f704dec61907278689cbd8325140b8a533fba9059b4eb9618`, expires 2026-10-24.
- The workflow no longer applies the custom main-menu and character-selection background patches. The patch files are absent from the current tree; custom loading artwork remains separate.
- Not yet verified: explicit inspection of the APK ZIP contents for absence of `senki_menu.png`/`senki_select.png`, phone visual confirmation, physical installation, and gameplay.
- Known UI gap: pages 4+ still use text-only page controls. The user requirement is matching image-based normal/selected controls for all pages while preserving original image-based pages 1–3. Dynamic page count is not the same as finishing the page-button design.

## Persistent rule: full character package and AI support

Every character addition must be tracked as a whole integration: selection name/ID/portrait/avatar/button art and preview; matching skill-view names/icons/descriptions; in-game sprite/model, atlas/plist and animation states; basic attacks, skills/cooldowns, hitboxes/damage, effects/projectiles/summons; voice clips where available and action-specific SFX with event triggers; player controls; existing game AI roster/selection/spawn and combat behavior; and all resource/config references. Where supported, verify actual killer/victim name and portrait in kill/death feedback.

AI means the game's computer-controlled fighter behavior here: it must be able to select/spawn the character in relevant modes and use its supported moves/skills. Player selection alone does not satisfy AI support. For each character, list source assets and paths, source URL/commit, reuse/permission status, tests, and every missing or unsupported item. Never claim an absent voice pack, skill icon, animation or effect was included. Use the states DISCOVERED → SOURCE-INSPECTED → PORTED → BUILD-VERIFIED → PLAYABLE-VERIFIED; only the last state means gameplay verification passed. CI success is not a substitute for in-game/device testing.


## Latest CI verification — run #82 (2026-10-10)
- [x] Run [38020781870](https://github.com/kage049754/Senki/actions/runs/38020781870) completed with **SUCCESS** on commit `3cc5d3bd807ae6c7814dcce1d61710c05552b7b9`.
- [x] Patch application, Lua syntax checks, search/filter regression checks, dynamic image-based pagination checks, landscape checks, and artwork rendering all passed.
- [x] Android debug build completed; candidate APK existence, package identity, packaged search code, signature, and native ABI checks all passed.
- [x] Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11657917474`, size 83,355,267 bytes; SHA-256 `303f9dfbabd11fec739b91dcdda4f818421618c242dda4182794d9497aa6c147`; expires 2026-10-24.
- [x] Workflow asserts the APK includes generated page 4 and 5 normal/selected image assets and does not include the retired custom main-menu/character-selection background replacements.
- [ ] Visually inspect page controls and original backgrounds on a physical Android device; CI packaging checks cannot confirm their appearance or touch behavior on device.
- [ ] The artifact is still a technical build of an external V2-derived source candidate with central patches, not a permission-cleared final release or a verified multi-mod character merge.
- [ ] Source and third-party art/audio/voice permissions remain unresolved; no newly integrated character is counted as fully playable or AI-verified.


## Character-package audit automation — latest build run #86 (2026-10-10)

- [x] Added `scripts/audit_character_packages.py` to scan the pinned source roster and produce a per-character source inventory for C++ headers, character-named Lua files, unit/resource files, audio folders, packed selection frames, and detectable native AI registration references.
- [x] Added the audit to the CI workflow and uploads the report as artifact `senki-character-package-audit`.
- [x] Run [38021855646](https://github.com/kage049754/Senki/actions/runs/38021855646), run #86, commit `fd874238aa9aabf115bffa8712d58b63e46fadf5`, completed **SUCCESS**. The source audit, Lua/search/pagination checks, Android build, APK package identity, signature/native ABI checks, and both artifact uploads passed.
- [x] Audit artifact ID `11657868789`, 1,333 bytes, expires 2026-10-24.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11658183639`, 83,324,238 bytes, expires 2026-10-24.
- [x] Improved the audit to check the candidate's actual `Resources/Unit/` layout and the three expected packed selection frames in `Resources/Select.plist`, and to look for the current C++ `HeroEnum::Name` + `setAIHandler` registration pattern.
- [ ] The audit is a source-level heuristic only. "Manual AI audit required" means the pattern wasn't found in the scanned files; it does not prove AI support is missing. No character is marked newly added or playable-verified by this report.
- [ ] Next implementation gate: find a character source with clear code/art/audio permission, map its complete assets and AI behavior to the current modular architecture, then integrate one character and add tests before counting it.


## Continued work — run #89 and skill UI audit improvement (2026-10-10)

- [x] Latest source commit `e1008de1046d449ab641f1eac9208132cfc12d9d` adds exact-name checks for the five skill icon and five skill-description frames requested by `SkillLayer.lua`, in addition to selection art, enum, Unit-resource, audio-path and AI-registration clues.
- [x] Run [#89](https://github.com/kage049754/Senki/actions/runs/38022671278) completed **SUCCESS** against that commit. Android build and both artifact uploads passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11658199787`, 83,357,018 bytes, expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11657914883`, 1,425 bytes, expires 2026-10-24.
- [x] Audit output now distinguishes skill icon frame count and skill description frame count. These are source filename/plist-name checks, not visual/functional proof.
- [ ] Source research has not yet identified a character package whose code, selection art, skills, animations, voice/SFX and other assets are all permission-cleared and compatible. No new character has been integrated.
- [ ] Next phases remain: resolve authorized character source/assets; port a complete character and AI behavior; add automated per-character checks; inspect the UI and test actual gameplay on device; repeat fixes/builds until final verification.


## Latest central V2-candidate CI verification — 2026-10-10

- [x] Commit `4d3bea9232aa4c65ea4e4432d814fcf837b0d046` completed GitHub Actions run **#98** successfully: https://github.com/kage049754/Senki/actions/runs/38024493952
- [x] Verified the exact run SHA matches the latest source commit.
- [x] Lua syntax and source smoke checks passed; the character audit report structure/coverage test passed.
- [x] Android diagnostic candidate build passed; APK existence, package identity, packaged character-search code, signature/native ABI checks, and artifact upload all passed.
- [x] Verified APK artifact `naruto-senki-v2-candidate-debug-apk`, artifact ID `11659787739`, size 83,342,550 bytes; SHA-256 `210a7b2d26374658db6a3097cd0821609b7db7b7fd47e4303b9397626ba21fa6`; expires 2026-10-24.
- [x] Verified audit artifact `senki-character-package-audit`, artifact ID `11659742756`; expires 2026-10-24.
- [x] Improved the automated inventory to report skill-description label coverage and list exceptions requiring manual review. The candidate's Kabuto skill-label frames remain absent by exact-name audit; no replacement labels were invented and no new character was integrated.
- [ ] Install and launch this exact artifact on the user's physical Android device; inspect original backgrounds, page 4+ navigation, character preview/selection, skill viewer, and battle behavior.
- [ ] Establish source/asset permissions or another permission-cleared source base before treating this candidate as an importable/releasable unified game.
- [ ] Current verified playable character count remains **unmeasured**; new characters integrated by this pass: **0**.

This is a successful **diagnostic candidate build**, not a final unified release or proof of physical-device gameplay. The external source is still cloned into the CI runner rather than vendored into this repository, and rights review remains open.


## Missing skill-description fallback — run #101 (2026-10-10)

- [x] Added `scripts/apply_skill_label_fallback.py` to patch the pinned candidate's `lua/ui/SkillLayer.lua` safely during CI.
- [x] The skill-details screen now checks whether the requested label frame exists before constructing its sprite. If a frame is missing, it shows a visible `Skill description unavailable` text label rather than attempting to construct a missing sprite.
- [x] Added `scripts/test_skill_label_fallback.py` and wired both application and regression test into `.github/workflows/v2-source-smoke.yml`.
- [x] Run [#101](https://github.com/kage049754/Senki/actions/runs/38024966443), commit `2ca3914ae8e10300c3e3070b376c8cf241a26ddb`, completed **SUCCESS**. The fallback step, Lua parse checks, character audit, search/pagination checks, Android build, APK identity/search/signature/ABI checks, and both artifact uploads passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11659082992`, 83,302,507 bytes; SHA-256 `2c71b02890ee86d87e7882d5365299cde4dc7ff2524cc89f88edb54be218870b`; expires 2026-10-24.
- [x] Audit artifact `senki-character-package-audit`, ID `11659103029`; SHA-256 `fa7d7ae391c5f82fc4196797e8b33be6750459c32c7ba8b7d40496fb31664d40`; expires 2026-10-24.
- [ ] Confirm the fallback visually in the actual skill-view screen on an Android device. CI validates the Lua patch and packages it but cannot establish how the Cocos2d-x UI looks at runtime.
- [ ] This does not add or complete a character; Kabuto's original description content remains missing and the UI reports that honestly.


## Skill-description fallback checkpoint — 2026-10-10

- [x] Commit `2ca3914ae8e10300c3e3070b376c8cf241a26ddb` completed GitHub Actions run **#101** successfully: https://github.com/kage049754/Senki/actions/runs/38024966443
- [x] The pinned V2 candidate received a guarded skill-description frame lookup: when an expected label sprite frame is absent, the skill-details view displays the visible fallback text `Skill description unavailable` instead of blindly constructing the missing sprite.
- [x] Static fallback regression test passed; source Lua validation and character-audit report structure test passed.
- [x] Dynamic pagination, landscape/rotation-stability checks, startup-failure diagnostics, APK package identity, packaged character-search, APK signature/native ABI checks, and artifact uploads passed in the same run.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11659082992`, size 83,302,507 bytes, SHA-256 `2c71b02890ee86d87e7882d5365299cde4dc7ff2524cc89f88edb54be218870b`, expires 2026-10-24.
- [x] Audit artifact `senki-character-package-audit`, ID `11659103029`, SHA-256 `fa7d7ae391c5f82fc4196797e8b33be6750459c32c7ba8b7d40496fb31664d40`, expires 2026-10-24.
- [ ] Confirm the fallback and skill-view behavior on a real Android device; static tests cannot prove Cocos2d-x runtime compatibility or visual correctness.
- [ ] Install/launch and play-test the candidate APK on the user's device; CI does not replace device verification.
- [ ] Continue source-base comparison/provenance and code/asset permissions; no additional character was integrated by this change.


## Packaged skill fallback verification — run #104 (2026-10-10)

- [x] Fixed the CI workflow after the first attempt to add an APK-content check introduced malformed duplicate YAML. Runs #102 and #103 failed before starting a job; the workflow was corrected and the full build rerun.
- [x] Run [#104](https://github.com/kage049754/Senki/actions/runs/38025372460), commit `277fd96969ac471136c0ecbc0b73a2b42e38cb49`, completed **SUCCESS**.
- [x] Added a post-build check that extracts `SkillLayer.lua` from the built APK and verifies both the missing-label fallback text and protected sprite-frame lookup are actually packaged.
- [x] Confirmed the new APK-content verification step passed, alongside all previous source checks, Android build, APK identity, signature/native ABI checks, and uploads.
- [x] Latest APK artifact: `naruto-senki-v2-candidate-debug-apk`, ID `11659729329`, 83,306,812 bytes; SHA-256 `97e37a19c006b4c3af9a0fe301013b0f1cb94c2a20d99c02eefb5eb6e24b7d2e`; expires 2026-10-24.
- [x] Latest character audit artifact: `senki-character-package-audit`, ID `11660148824`; SHA-256 `fe4b7314d5cce2e6e0ec77dc67f3bd0112416f65bd6c82a73c08efea5900a527`; expires 2026-10-24.
- [ ] Still needs physical-device visual/gameplay verification. The successful CI checks confirm packaging, not runtime behavior.


## Packaged skill-description fallback verification — 2026-10-10

- [x] Follow-up run **#104** completed successfully: https://github.com/kage049754/Senki/actions/runs/38025372460
- [x] The fallback patch passed source tests and Lua validation.
- [x] The APK build completed and the workflow extracted the packaged `SkillLayer.lua` from the APK and verified both the fallback message and protected frame lookup are actually present in the packaged file.
- [x] APK signature and native ABI checks passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11659729329`, size 83,306,812 bytes, SHA-256 `97e37a19c006b4c3af9a0fe301013b0f1cb94c2a20d99c02eefb5eb6e24b7d2e`, expires 2026-10-24.
- [x] Audit artifact `senki-character-package-audit`, ID `11660148824`, SHA-256 `fe4b7314d5cce2e6e0ec77dc67f3bd0112416f65bd6c82a73c08efea5900a527`, expires 2026-10-24.
- [ ] Runtime UI and device behavior remain unverified. A packaged-string check proves the fallback is in the APK, not that it renders correctly on all runtime states.


## Additional mod research — Fukasaku/Shima lead (2026-10-10)

- [x] Inspected `LeaderOnePro/NarutoSenki1.17Mod`: a packaged Android mod based on Senki 1.17 that replaces Choji with the two Great Sage Toads, Fukasaku/Shima.
- [x] Confirmed the APK tree includes dedicated Fukasaku audio and element/resource folders, but not an editable source project in the inspected tree.
- [x] Compared `wsnbbnbb/NarutoSenki1.17Mod`; it is a fork of the same repository with matching reported size/layout, not a separate source implementation.
- [x] Recorded the lead as reference-only in `docs/MOD_RESEARCH.md`; no packaged APK assets were copied into Senki.
- [ ] Find an editable, compatible Fukasaku/Shima implementation or a permission-cleared source; do not count it as integrated or playable in the V2 candidate.


## Legacy source character research — Han and Roshi (2026-10-10)

- [x] Inspected the legacy source at commit d847b113dfce486822768ef5a1c1c874b50fa3cd.
- [x] Confirmed Han and Roshi each have animation XML/plist resources, audio, report portrait frames, and cut-in art; the XML includes attack/skill sequences and event metadata.
- [x] Confirmed legacy Classes/Element.cpp contains special-case behavior for Han/Roshi; porting requires more than copying animation metadata.
- [x] Confirmed the pinned V2 candidate has no Han/Roshi class/resource folders and neither character is in its selectable roster.
- [x] Documented the source paths and compatibility gaps in docs/MOD_RESEARCH.md; no source/assets copied.
- [ ] Map the legacy Han/Roshi behavior to the current V2 character interfaces before selecting one for a complete implementation.


## Pagination artwork regression test — run #109

- [x] Run **#109** passed: https://github.com/kage049754/Senki/actions/runs/38025803886
- [x] Added an image regression test for generated page 4 and 5 controls. It extracts the original page button frames from `Select.png` + `Select.plist`, verifies 40x40 visible normal/selected controls, and checks that the outer button artwork remains pixel-identical outside the center numeral region.
- [x] The first test attempt failed because the test looked for atlas frames as standalone PNG files; the actual assets are packed in the Select atlas. After reading the real atlas frames, a second attempt exposed an overly strict center-region comparison. The test was corrected to validate the untouched outer rim; the corrected check passed.
- [x] Dynamic pagination, source Lua validation, skill-label fallback tests, Android candidate build, packaged fallback check, APK signature/native ABI checks, and artifact upload all passed on run #109.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11660410133`, size 83,334,545 bytes, SHA-256 `a48e46cf0467d0bab35717534aad02ecd8d6bfcaf0d6dd935fb6719c41264635`, expires 2026-10-24.
- [x] Audit artifact `senki-character-package-audit`, ID `11659909978`, SHA-256 `a1f6650cb079a6bb5a8b46bc94a232b35e06f2f7dca79db0036d95cf0334b4bc`, expires 2026-10-24.
- [ ] Physical-device UI/gameplay remains unverified. The current source inventory has 63 layout slots (3 pages at 21 slots/page), so pages 4 and 5 are generated and validated as future-ready controls but are not currently reached by this candidate's present roster count.


## Artifact access warning — public repository — 2026-10-10

GitHub API confirms `kage049754/Senki` is currently **public**. Therefore, the short-lived Actions APK artifacts are not private to the user; people with public repository read access may be able to download them during the retention window. The workflow's “private testing” wording describes intended use, not access control. The APK contains the third-party V2-derived game's resources and is not permission-cleared for redistribution. Do not describe this artifact as a private release. Repository visibility has not been changed; that would require the user's explicit decision.


## Latest skill-view resilience patch — 2026-10-10

- [x] Added `scripts/apply_skill_label_fallback.py` to the pinned-candidate workflow. The patch checks whether the expected skill-description frame exists before constructing the sprite.
- [x] If the frame is missing, the skill-details view now displays a visible “Skill description unavailable” text fallback instead of unconditionally constructing a sprite from a missing frame.
- [x] Added `scripts/test_skill_label_fallback.py`; the latest CI run validates the patched Lua source and completed the Android candidate build successfully.
- [x] Latest run #101: https://github.com/kage049754/Senki/actions/runs/38024966443; commit `2ca3914ae8e10300c3e3070b376c8cf241a26ddb`.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, artifact ID `11659082992`, size 83,302,507 bytes, digest `sha256:2c71b02890ee86d87e7882d5365299cde4dc7ff2524cc89f88edb54be218870b`, expires 2026-10-24.
- [ ] Runtime test the missing-label case on device/emulator and confirm the fallback renders and scrolls correctly. Static checks and packaging do not prove runtime UI behavior.
- [ ] This patch does not supply missing character descriptions or integrate any new character. Newly integrated characters this pass: **0**.
- [ ] The candidate source is still cloned into the workflow's temporary runner workspace. The central repo contains the patches and build workflow, not a vendored editable copy of the complete upstream game.


## Expanded roster candidate — six existing native forms exposed on page four

- [x] Compared the current V2 candidate's `HeroEnum`, native character classes, and resource packages; found six already-implemented forms absent from `ns.CharactersLayout`: `SageJiraiya`, `ImmortalSasuke`, `SageNaruto`, `RikudoNaruto`, `RockLee`, and `Nagato`.
- [x] Added source-controlled `scripts/apply_selectable_forms.py` to expose these six existing native forms in page four. The patch reuses their existing dedicated half-portrait frames, uses base-character small selection/skill icons where form-specific UI art is missing, shows readable form names, and uses the existing missing-description fallback.
- [x] Added `scripts/test_selectable_forms.py` to check the 84-slot/four-page roster, native enum and class registrations, form XML/plist resources, half portraits, and UI aliases.
- [x] Added a post-build APK inspection step that extracts the packaged `basic.lua`, `SelectLayer.lua`, and `SkillLayer.lua` and verifies the six form names and UI aliases are actually present in the APK.
- [x] GitHub Actions run #117 succeeded on exact source SHA `da6bc5e446e32f7480a21c2826798398130f186c`: https://github.com/kage049754/Senki/actions/runs/38027092821
- [x] Verified APK artifact `naruto-senki-v2-candidate-debug-apk`, artifact ID `11661160453`, size 83,341,459 bytes, digest `sha256:62c07ff29f8c1f7ba0bddc49abd79861ed2ff00534051424a0ea47eb3cf5379e`, expires 2026-10-24.
- [ ] Physically install and test all six form selections, preview portraits, skill screen, character spawn, AI, movement, attacks, transformations, and death/respawn. CI verifies source packaging only, not in-game behavior.
- [ ] Page four now has six extra form entries. Page-five normal/selected button assets are generated and packaged, but page five is not displayed yet because the current roster has 84 slots (four pages). More verified character implementations are needed before page five should be enabled.
- [ ] Newly exposed forms are **not yet counted as verified playable characters**. This is roster/UI exposure of existing native implementations, not a port of new external assets or code.


## Latest roster/resource validation build — 2026-10-10

- [x] Strengthened the form regression test to parse each form's atlas plist metadata and verify the referenced texture file actually exists. This handles the candidate's mixed texture naming/extensions (for example, some form atlases reference `.pvr.ccz`, while Nagato references `.png`).
- [x] Latest GitHub Actions run #121 completed successfully on `7a1aa062dc306a9c0180a551b91753ef55604416`: https://github.com/kage049754/Senki/actions/runs/38027680983
- [x] The run passed the selectable-form source checks, full Lua syntax validation, character package audit, Android build, APK roster-packaging checks, signature/ABI checks, and artifact upload.
- [x] Latest APK artifact: `naruto-senki-v2-candidate-debug-apk`, ID `11660673063`, size 83,313,937 bytes, digest `sha256:cfeca041cc20e0c6a423f492fcab286b38bc802ee8cd4de82c1b528c388341c1`; expires 2026-10-24.
- [ ] Install and test the exact artifact on an Android device/emulator. No physical-device results are available in this session.


## Latest packaged tooltip-cleanup verification — run #122 (2026-10-10)

- [x] Run **#122** succeeded on exact workflow commit `6f636b5cf429231e760546b2ce17afbd5c6f7ff9`: https://github.com/kage049754/Senki/actions/runs/38027909214
- [x] Added post-build checks proving the APK-packaged `SkillLayer.lua` contains both the missing-label fallback and whole-tooltip-container cleanup (`self._skillExplainClipper:removeFromParent()` and `self._skillExplainClipper = clipper`).
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11661206511`, size 83,310,581 bytes; SHA-256 `ea413331b1a90c61fedcd44f8ba65b19a31f8559c94edf7e7554e5d323d69b12`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11661201551`; expires 2026-10-24.
- [ ] The next milestone remains runtime validation on an Android device/emulator, then additional character integrations sourced from compatible editable implementations. Current 43 selectable entries/forms are not equivalent to 43 gameplay-verified characters.


## Latest native-form transformation regression — run #123 (2026-10-10)

- [x] Run **#123** succeeded on exact source SHA `7bb1f98598cbb06d5587fb623b8fdb33c35d6b4d`: https://github.com/kage049754/Senki/actions/runs/38028261338
- [x] Strengthened the form roster regression test to verify the six entries correspond to actual native transformation paths in `CharacterBase.cpp` (Naruto → Sage Naruto → Six Paths Naruto, Jiraiya → Sage Jiraiya, Sasuke → Immortal Sasuke, Lee → Rock Lee, Pain → Nagato).
- [x] Lua validation, expanded form/resource/texture checks, APK build, packaged form checks, and artifact upload passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11660823928`, size 83,302,910 bytes; SHA-256 `885fbdb5b403d5f14c9bc05274887efa317751c54aa7a8995adcec5fe47078c2`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11660579136`; expires 2026-10-24.
- [ ] These checks still do not prove the forms launch or behave correctly in gameplay; physical-device/emulator verification is outstanding.


## Roster-target accounting — run #126 (2026-10-10)

- [x] Run **#126** succeeded on exact source SHA `9aa276227fa118e89246eef561aa318209d3c60a`: https://github.com/kage049754/Senki/actions/runs/38028647795
- [x] Character audit now explicitly reports the gap to 70 declared entries and states that gameplay-verified count is not measured by static inventory.
- [x] Audit table structure/row-count/target-gap checks passed; Android diagnostic candidate build, package/signature/ABI checks, and artifact upload passed.
- [x] Audit artifact `senki-character-package-audit`, ID `11661505149`, SHA-256 `50d7cc2e83c2c99a8c093f758ef65b127cd1f2c0b2e562491aa10252b68b3465`; expires 2026-10-24.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11660439960`, size 83,357,309 bytes; SHA-256 `865afbe5def724a1f0c0da37ad9aec845d12ccac4ed56a14411c156e6ce3b76c`; expires 2026-10-24.
- [ ] Current declared selectable roster is **43 distinct names/forms** against the 70-entry target, leaving **27 additional distinct entries** before gameplay verification. The six added entries are existing native transformation forms, not newly ported external characters.
- [ ] Continue investigating permission-cleared, editable source for new characters; source-level inventory is not a substitute for combat, AI, animation, and device tests.


## Latest CI checkpoint — expanded native-form roster — 2026-10-10

- [x] GitHub Actions run **#126** succeeded on exact source SHA `9aa276227fa118e89246eef561aa318209d3c60a`: https://github.com/kage049754/Senki/actions/runs/38028647795
- [x] The six existing native forms remain registered in the four-page roster, with UI aliases, native class/enum/resource checks, and transformation-path checks.
- [x] Candidate Android build, packaged-form inspection, APK signature/native ABI checks, and artifact upload all passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11660439960`, size 83,357,309 bytes, SHA-256 `865afbe5def724a1f0c0da37ad9aec845d12ccac4ed56a14411c156e6ce3b76c`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11661505149`, SHA-256 `50d7cc2e83c2c99a8c093f758ef65b127cd1f2c0b2e562491aa10252b68b3465`.
- [x] Latest static roster inventory finds 37 original unique names plus six existing forms (43 distinct selectable names). This is **not** a count of gameplay-verified playable characters; 27 additional distinct roster entries would be needed to reach the declared 70-entry target, and each still requires functional tests.
- [ ] Device/emulator test remains outstanding: selection, preview art, skill UI, spawn, AI, movement, attacks, transformations, death/respawn, and original menu backgrounds.
- [ ] Source/asset permission and source-vendoring gates remain open. No new external character has been integrated in this pass.


## Latest background-preservation regression and APK — run #128 (2026-10-10)

- [x] Added `scripts/test_original_backgrounds.py` to prevent accidental replacement of the original character-selection background logic and original GameModeLayer red background/menu bars/title.
- [x] GitHub Actions run **#128** succeeded on exact workflow SHA `b41d47fb8fa0d9feda4ef3b3c9a4055c87e620f7`: https://github.com/kage049754/Senki/actions/runs/38029026945
- [x] Background source-preservation regression, Lua syntax checks, Android candidate build, APK existence, signature/native ABI checks, and artifact upload passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11662000429`, size 83,353,676 bytes, SHA-256 `ff1fc6f15d0dfe3f40f570851b68208e29385477c4fce2d2cc873995dcf4754a`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11661615867`.
- [ ] The regression verifies source fragments only. It does **not** replace installing the APK and visually checking the character-selection and training/network/exit screens on Android.
- [ ] Current selectable roster remains 43 distinct names including six existing forms; gameplay-verified count remains unmeasured. No new external character was integrated in this pass.


## Latest original-background asset packaging verification — run #136 (2026-10-10)

- [x] Added a CI check that the built APK includes the original background textures `red_bg.png`, `blue_bg.png`, `menu_bar2.png`, and `menu_bar3.png`, in addition to the source-level check of the original selection/mode-menu background setup.
- [x] GitHub Actions run **#136** succeeded on exact workflow SHA `9c4aa3dbd82c91cef8fb90297030b809ae0cdd42`: https://github.com/kage049754/Senki/actions/runs/38029520544
- [x] Original-background source regression, Lua syntax checks, Android build, APK existence, package identity, character-search/skill fallback/form packaging, signature/native ABI checks, and artifact upload passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11661441846`, size 83,348,767 bytes, SHA-256 `65a9116d9652b65a21eaf9f765ff709b3475aad45da3c2922522ad0253464a8f`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11661511654`.
- [ ] Source and packaged asset checks do not prove visual appearance at runtime. The character-selection and training/network/exit backgrounds still need to be inspected on an actual Android device/emulator.


## Latest skill-description fallback and alias-aware audit — run #141 (2026-10-10)

- [x] GitHub Actions run **#141** succeeded on exact source SHA `c02bfb51c34b9bc6ae1c4285eacd48e3cfec4f09`: https://github.com/kage049754/Senki/actions/runs/38030022200
- [x] The candidate applies a guarded skill-description frame lookup and shows a visible “Skill description unavailable” fallback if an expected label frame is absent.
- [x] The skill tooltip's clipper container is tracked and removed when switching skills, preventing stale tooltip containers from accumulating.
- [x] Lua syntax checks, character audit report structure, APK build, package identity, packaged character-search code, signature/native ABI checks, and artifact upload passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11661692440`, size 83,322,088 bytes, SHA-256 `3342575c632dee2a795af2207d510a97c3f70f6952eb68a536d31f6fa070bb13`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11662017164`; expires 2026-10-24.
- [x] Corrected the audit to honor the six `SkillLayer` art aliases: **42/43** entries now have all five expected skill-description labels; only `Kabuto` remains a real missing-label exception (0/5), with the safe generic fallback packaged in the APK.
- [ ] Physical-device verification of the missing-label fallback, tooltip switching, page 4/5 controls, and original backgrounds remains open.
- [ ] No new external character was integrated. The audit remains a static resource/source inventory, not a gameplay completeness test.
- [ ] Source vendoring and code/asset permission review remain open; this successful candidate build does not remove those blockers.


## Latest alias-aware character audit and packaged background verification — run #141 (2026-10-10)

- [x] Character package audit now reads the `SkillLayer.lua` UI alias map so forms that reuse a base character's skill art are not incorrectly flagged as missing all five skill icons/labels.
- [x] Regression checks require the known `RockLee → Lee` skill-art alias to be recognized while keeping Kabuto's missing label frames flagged for manual review.
- [x] Added `scripts/test_packaged_background_assets.py` to compare SHA-256 hashes of the APK's original red/blue backgrounds and menu bars against the pinned source files byte-for-byte.
- [x] GitHub Actions run **#141** succeeded on exact workflow SHA `c02bfb51c34b9bc6ae1c4285eacd48e3cfec4f09`: https://github.com/kage049754/Senki/actions/runs/38030022200
- [x] Character-audit structure, original-background checks, Android candidate build, APK verification, and artifact uploads all passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11661692440`, size 83,322,088 bytes, SHA-256 `3342575c632dee2a795af2207d510a97c3f70f6952eb68a536d31f6fa070bb13`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11662017164`, SHA-256 `c859375f2ec3f74ba1b7ba34a630687c178808ec670574c58b903273b56bc512`.
- [ ] Runtime visual/gameplay testing is still outstanding; source and APK byte checks do not replace an Android install and play test.


## Latest form skill-label alias verification — run #143 (2026-10-10)

- [x] Updated the actual candidate patch so existing forms use their base character's skill-description label frames, not only their base skill icons/full-screen art. This resolves the false missing-label issue for `RockLee` and other aliased forms.
- [x] GitHub Actions run **#143** succeeded on exact workflow SHA `40aea9917261a9355c76d1f6b4b5496c036593be`: https://github.com/kage049754/Senki/actions/runs/38030471776
- [x] Lua syntax, character package audit, alias-aware audit regression, Android diagnostic build, packaged skill fallback, APK signature/native ABI checks, and artifact upload passed.
- [x] Audit result remains **42/43** entries with all five expected skill-description frames after aliases. Only `Kabuto` lacks all five label frames (0/5); the generic visible fallback is included. This is a resource audit, not proof of runtime skill-view behavior.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11661893046`, size 83,325,632 bytes, SHA-256 `b7c57d7b60880c85109ae3dd0bf79fc78daa6a367589aa9a74954bbbf5a22145`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11661603360`, SHA-256 `3397364510d2db1177a5ae6bc7f442fa329b10afd632a989c83e188f18799943`; expires 2026-10-24.
- [ ] Physical-device verification of skill-label rendering, tooltip switching, page 4/5 controls, and original backgrounds remains open.
- [ ] The roster remains 43 distinct selection names. No new character was added by this fix; gameplay-verified playable count is still unmeasured.


## Latest informative skill-description fallback — run #152 (2026-10-10)

- [x] Corrected the form-label patch so existing forms use their base character's description labels, and Kabuto receives five readable skill descriptions when the source lacks its expected label frames.
- [x] Descriptions are based on the pinned candidate's Kabuto class/XML comments and actions: Chakra Scalpel Activation; Nerve Strike Dash; Dead Soul Vault; Dead Soul Jutsu (Possession); Nehan Shojo: Final Slash.
- [x] GitHub Actions run **#152** succeeded on exact workflow SHA `680ae6429e52e142ba10707ebd71d783525fc261`: https://github.com/kage049754/Senki/actions/runs/38031233006
- [x] Lua syntax, form-resource regression, character audit, APK build, packaged skill-description checks, expanded roster packaging, signature/native ABI checks, and artifact upload passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11661624590`, size 83,299,837 bytes, SHA-256 `a14c09e7c0d646504ee9b775a23e415cd25c28cc9476bac754dc9ac934f05193`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11662099251`, SHA-256 `fbd2915a317262947ba38b27dfe2f58db12efebbc827e85c656b6f8ceb52dead`; expires 2026-10-24.
- [ ] Runtime rendering and tooltip scrolling still require Android device/emulator testing.
- [ ] The roster remains 43 declared selection names; no new character was integrated. Gameplay-verified count remains unmeasured.


## Latest roster-source research checkpoint — 2026-10-10

- [x] Compared additional repositories, including `Fansirsqi/NarutoSenki`, `likill/NarutoSenki-master`, `RieyuXhen/NarutoSenki`, `Zx-Akito/NarutoSenki`, `hendprw/NarutoSenki`, and the paired 1.17 mod repositories.
- [x] Confirmed `wsnbbnbb/NarutoSenki1.17Mod` and `LeaderOnePro/NarutoSenki1.17Mod` share the same recursive tree SHA; they are not independent sources.
- [x] Confirmed `hendprw/NarutoSenki` and `Zx-Akito/NarutoSenki` share the same recursive tree SHA. Legacy Cocos2d-x 2.2.2 source files expose 58 distinct AI method names, but those are not 58 verified player characters.
- [x] Compared the V2-family original selection layouts: inspected forks expose 36 original selection names, while the pinned Android-only candidate exposes 37 because it includes Kabuto. The V2 family does not supply the 27 additional complete playable packages needed to reach 70.
- [ ] Continue looking for independent, editable, compatible character implementations. Do not count APK-only resources, duplicate mirrors, enum-only support classes, summons, or AI method names as new playable characters.


### Failure → fix → successful rerun notes for skill-description work

- Run #150 failed because a regression expected the old generic “Skill description unavailable” text after the fallback became character-specific. The failure was inspected in the actual job logs.
- Run #151 then exposed the same stale expectation in the selectable-form regression. That assertion was updated to check the new fallback table and real Kabuto skill descriptions.
- The packaged-APK workflow check was also updated to assert the new dynamic fallback expression and actual Kabuto description strings instead of the retired generic text.
- Run #152 then passed the updated source checks, Android build, packaged skill-description checks, form roster packaging, signature/ABI validation, and artifact upload. The earlier failed runs remain failed in GitHub history; run #152 is the verified successful rerun.


## Latest roster gap and non-roster enum audit — run #159 (2026-10-10)

- [x] Added an automated inventory of `HeroEnum.h` names that are not in `ns.CharactersLayout`. The report explicitly marks these as manual-review leads, not playable characters.
- [x] CI classified 9 non-roster enum leads: `AnimalPath`, `AsuraPath`, `HumanPath`, `PertaPath`, `NarakaPath`, `NarutoClone`, `SageNarutoClone`, `RikudoNarutoClone`, and `Guardian`. The five Pain-path entries appear to be internal/summoned entities; the three NarutoClone entries are clones, and Guardian is support content. They are not automatically counted as selectable characters.
- [x] Audit report confirms **43 distinct declared selectable names**, leaving **27 more distinct entries** to reach 70 declared names. This is not a gameplay-verified count.
- [x] GitHub Actions run **#159** succeeded on exact workflow SHA `3f6ac555fa5b9fb5a9f64c195679e0abe50da2aa`: https://github.com/kage049754/Senki/actions/runs/38031862251
- [x] Lua/source checks, character audit structure, Android candidate build, packaged Kabuto skill-description fallback, APK verification, and artifact uploads passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11662291624`, size 83,328,393 bytes, SHA-256 `f5529a7558f1e60fe8176c78f13a92364d866ce4e9e81a21092910118a3bef70`; expires 2026-10-24.
- [x] Character audit artifact `senki-character-package-audit`, ID `11662461471`, SHA-256 `34caeb205755ca9d78516b1cdc0ed9991efe467ff414a4f8175e08a729bdcb52`.
- [ ] Determine whether any of the five Pain paths can legitimately become player-selectable without breaking Pain's summon kit; do not promote them based on enum/resource presence alone.
- [ ] Continue finding at least 27 additional complete character packages from compatible source trees and document source/asset rights before merging.
- [ ] Physical-device verification and source/asset permission review remain open.


## Latest non-roster enum audit and build verification — run #159 (2026-10-10)

- [x] Extended the static character audit to list `HeroEnum` identifiers not present in the visible selection list; these are explicitly marked for manual classification and are not counted as playable characters.
- [x] Added regression assertions for the 70-entry declared-roster gap, the enum-only lead inventory, and known summon/support identifiers such as `AnimalPath` and `Guardian`.
- [x] Inspected the actual failure/fix chain: runs #155–#158 were superseded/cancelled while the audit output escaping and test regex were corrected. The latest exact-source run #159 completed successfully.
- [x] GitHub Actions run **#159** succeeded on exact SHA `3f6ac555fa5b9fb5a9f64c195679e0abe50da2aa`: https://github.com/kage049754/Senki/actions/runs/38031862251
- [x] Android diagnostic APK built; candidate APK presence and signature/native ABI packaging checks passed.
- [x] APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11662291624`, size 83,328,393 bytes; SHA-256 `f5529a7558f1e60fe8176c78f13a92364d866ce4e9e81a21092910118a3bef70`; expires 2026-10-24.
- [x] Audit artifact `senki-character-package-audit`, ID `11662461471`; SHA-256 `34caeb205755ca9d78516b1cdc0ed9991efe467ff414a4f8175e08a729bdcb52`; expires 2026-10-24.
- [ ] Review each non-roster enum identifier against native class, provider dispatch, XML/plist/texture, AI, and transformation logic before considering it a selectable character.
- [ ] The declared roster is still 43 names; verified playable count is not measured. This audit adds discovery leads, not new playable characters.
- [ ] Continue physical-device testing, source-vendoring/provenance work, and integration of complete compatible characters.


## New character-resource discovery: Hokage Minato (reference-only)

- [x] Found a concrete older-mod package containing Hokage Minato's sprite atlas/texture, animation XML, audio clips, selection half portrait, and kill-feed portraits: `LeaderOnePro/NarutoSenki1.17Mod`.
- [x] Confirmed its XML uses the older 1.x `<animation>/<date>/<frameName>` schema, not V2's `<unit>/<data>/<f>` schema; it includes multiple skill actions and references buffs, summons, bullets, commands, and effects.
- [x] Confirmed the V2 candidate has the half-portrait/audio references but lacks the actual unit package and native enum/class. This explains why the existing selection art alone was not enough.
- [ ] Locate or implement a compatible native V2 class/AI and safely adapt the XML only after the provenance/permission decision; test all resource references and combat behavior.
- [ ] This is a research lead, not an integrated character. The declared roster remains 43 and the target gap remains 27; no playable count is inferred.


## Latest verification pass — 2026-10-10 (run #161)

- [x] Rechecked GitHub Actions run **#161**: https://github.com/kage049754/Senki/actions/runs/38032354146
- [x] Run conclusion: **SUCCESS** on commit `af4a96195948011e9852cfadfe1cc4a902a81fe4` (workflow `V2 Source Candidate Build (Private Testing Artifact)`).
- [x] All 34 substantive job steps completed successfully, including applying the central patches, Lua syntax validation, original-background checks, generated image-based page 4/5 buttons, character-package audit, pagination/search tests, Android SDK/NDK setup, APK build, package identity, packaged-code, signature, and native ABI checks.
- [x] GitHub Actions artifact `naruto-senki-v2-candidate-debug-apk`, ID `11662811306`, is present, not expired, and is 83,375,086 bytes as a ZIP artifact; SHA-256 of the artifact ZIP: `d559a415cb1bcbb7ae3dc85b7f9f6ac8262d8c9634d4089f44d93e017ad7f73a`. It expires 2026-10-24.
- [x] Character-package audit artifact `senki-character-package-audit`, ID `11662666611`, is present, not expired, and expires 2026-10-24.
- [ ] This is still a **diagnostic build of the pinned external V2-derived candidate in a temporary CI workspace**. It is not proof that the full source has been imported into this central repository, and it is not a release-ready unified mod.
- [ ] No newly added character is counted as playable from this build. Current roster notes still distinguish 43 declared selectable names from the unmeasured verified-playable count.
- [ ] Next work: review audit findings, identify a character whose complete assets and reuse permissions are actually established, then integrate/test one full character package into the selected native base. Continue documenting unresolved code/artwork/audio rights rather than silently copying reference-only assets.
- [ ] Physical-device installation and gameplay remain unverified; CI success confirms only the checks performed by this workflow.


## Character asset audit regex fix and regression verification — 2026-10-10

- [x] Fixed two escaped-whitespace regexes in `scripts/audit_character_packages.py` that had incorrectly reported zero XML audio-event references and unresolved sprite textures.
- [x] Verified the corrected patterns against the pinned V2 Minato XML/plist: the plist resolves `Minato.pvr.ccz` and the XML has 26 matching sound-event references in that sample.
- [x] Added regression gates in `scripts/test_character_package_audit.py`: every current roster entry must resolve a sprite plist + texture, and the audit must recognize audio-event references.
- [x] GitHub Actions run **#162** succeeded: https://github.com/kage049754/Senki/actions/runs/38032617069
- [x] GitHub Actions run **#164** succeeded on exact commit `2fd6ba8de4ae7334e0451c397ab8b5342840e4bd`: https://github.com/kage049754/Senki/actions/runs/38032945561. All 37 successful steps completed; no failed steps.
- [x] Run #164 diagnostic APK artifact `naruto-senki-v2-candidate-debug-apk`, ID `11663366691`, ZIP size 83,323,243 bytes, SHA-256 `8eac9d1221393eb9fb1cd916d4b3cc3945afa3c40b0da592f01f43d55997f104`; expires 2026-10-24.
- [x] Run #164 audit artifact `senki-character-package-audit`, ID `11663032190`; expires 2026-10-24.
- [x] Corrected report confirms all **43/43** declared entries have a detected unit XML, sprite plist + texture, and both kill-feed portrait frames; the static audit recognizes non-zero audio-event references.
- [ ] **42/43** entries have all five expected skill-description label frames; Kabuto remains flagged for manual skill-view/art review.
- [ ] The audit finds 9 enum-only leads (including summon/support/clone identifiers) that still need manual classification. They are not counted as playable characters.
- [ ] Declared roster remains **43**, with **27 more declared entries** to reach 70. The gameplay-verified playable count is still unmeasured; no character was added or promoted to VERIFIED by this audit.
- [ ] The APK remains a diagnostic build of the pinned external V2-derived candidate in a temporary CI workspace. It is not yet the final unified mod or a physical-device-tested release.
- [ ] Next: resolve code/art/audio permission status; manually inspect Kabuto's skill labels and the AI registration gaps; only then select a permission-cleared character package for a controlled native integration and gameplay verification.


## Animation XML-to-atlas cross-check — 2026-10-10

- [x] Added an audit that compares every distinct `<f>` animation-frame name in each character XML against frame keys in that character's sprite plist.
- [x] Run #168 passed all 37 workflow steps and produced the diagnostic APK plus the expanded audit: https://github.com/kage049754/Senki/actions/runs/38033542630
- [x] Run #168 static audit result: **39/43** declared entries have no XML-to-atlas frame-name mismatches.
- [!] Four entries need review: **Asuma (12 missing frame names), Kimimaro (5), SageJiraiya (6), RockLee (55)**. These are name-level mismatches; some may be intentional shared/base-form references, so they are not automatically declared runtime defects.
- [!] The Kimimaro XML references `Jugo_Skill05_14` through `Jugo_Skill05_18`; this looks like a cross-character frame-name mismatch and should be checked against the correct atlas/source before editing.
- [x] Extended the report to include the first 12 missing frame names per affected character and added a regression assertion so the known Kimimaro-to-Jugo mismatch cannot silently disappear from the audit.
- [ ] Awaiting final CI run for the expanded exception details and regression assertion. No source/assets have been imported from the external reference; permission status remains unresolved.
- [ ] Next: inspect whether the four mismatch groups are intentional shared atlas dependencies or real references to absent frames. Only apply an authorized, evidence-based fix; then rerun the audit/build.

## User priority: add distinct mod characters to pages 1–3 first (2026-10-10)

- User instruction: fill available/explicitly approved character slots on pages 1, 2, and 3 with distinct characters from other Naruto Senki mods before progressing to pages 4 or 5.
- Preserve the original image-based page 1–3 buttons and their touch behavior, and preserve the original character-select and mode-menu backgrounds.
- Do not treat transformations/forms of Naruto, Pain, Sasuke, Rock Lee, or Jiraiya as satisfying the distinct-character milestone.
- Updated README.md, AGENTS.md, ROADMAP.md, and docs/CHARACTER_ROSTER.md to make this order mandatory for future work.
- Candidate leads (not integrated): Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Yamato, Zetsu, Iruka, Jirobo, Tayuya, Anko, Han, and Immortal Sasuke. Verify exact source, unique contribution vs fork, schema compatibility, and reuse permission before import.
- Current blocker: external code/assets permissions for the V2 candidate and several leads are unresolved. Do not copy those assets until authorized or a source with clear compatible reuse terms is found.
- Latest inspected run #170: **SUCCESS** — https://github.com/kage049754/Senki/actions/runs/38033790172. It produced diagnostic candidate APK artifact naruto-senki-v2-candidate-debug-apk (artifact ID 11663288408; ZIP digest SHA-256 1fcd463e448a031c60ff749cc19c4e4ca9c1d24452cea4a30347d68ac04285ec; expires 2026-10-24) and audit artifact senki-character-package-audit (ID 11662689122). This is a pinned V2-derived diagnostic candidate, not proof of new external characters, a final unified release, or physical-device testing. The run explicitly added existing native forms to page four, which does not meet the new page 1–3 distinct-character priority.
- Verified newly integrated distinct external characters: **0**. Do not inflate this count based on candidate leads, existing forms, static audits, or page navigation.


## Character portrait requirement (2026-10-10)
User requires every new character to have its own correct avatar/portrait in the exact character-select slot, not merely a name or placeholder. The requirement is now documented in README.md, AGENTS.md, ROADMAP.md, and docs/CHARACTER_ROSTER.md. Each roster record must track the page/slot, stable ID, portrait resource/frame, source/license, and validation; supported profile/skill and kill/death displays must use the matching identity. This documentation update does not import new character assets or claim any new character is playable. Distinct external character integrations remain unverified until their resources, permissions, compatibility, and in-game behavior are checked.


## Latest continued-work update — 2026-10-10

- [x] Run #178 completed successfully on source commit `03b1247d01f9d6b981207b3e86914cea661992d3`: https://github.com/kage049754/Senki/actions/runs/38034685428
- [x] All 37 reported workflow steps completed without a failed step.
- [x] Verified current-run artifact `naruto-senki-v2-candidate-debug-apk` (83,337,410 bytes; SHA-256 `d8736bafad17d8257ca86ef910fbb6ec9aa8bb3f521ff04c0c50b048ad3fad87`) and `senki-character-package-audit` (3,670 bytes; SHA-256 `6770be74a205d7ade9c94f1a1fe6e414251892ef836433d22288663b772abe3f`). Both were unexpired when checked.
- [x] Expanded the character research tracker with the Han/Roshi guardian-resource discovery and its technical caveat: the pinned source routes both names to the generic Guardian class, and the resource packages alone do not establish full playable/selection integration.
- [x] Kept the roster counts honest: 37 source-visible selectable names, 43 after the six existing native forms exposed by the diagnostic patch; Han/Roshi are not counted as integrated characters. Gameplay-verified playable count is still not measured.
- [ ] Do not mark this as a finished game or final release. This workflow builds a diagnostic candidate from a pinned external source in a temporary CI workspace. Device installation, actual selection/battle/skill tests, full source import, and the 70-verified-character goal remain outstanding.
- [ ] Next technical step for Han/Roshi: complete the selection portrait/name art and skill UI dependency audit, trace how Guardian units behave when selected as a player, then implement a complete character batch only after those checks pass.

## Latest continued-work update — run #185 (2026-10-10)

- [x] Run #185 completed successfully on commit `cfdb9a7151d9c2bfbc5957c6d3a7f3cbe0db8dd1`: https://github.com/kage049754/Senki/actions/runs/38035532569
- [x] All 38 workflow steps completed successfully; no failed steps were reported.
- [x] Verified the current-run diagnostic APK artifact: `naruto-senki-v2-candidate-debug-apk`, ZIP size 83,343,195 bytes, GitHub artifact digest `sha256:adcc6cf6cbc232b3b453c71d53565a798d2fc711809a4cda66d8da550e45d055`, artifact ID 11664276520, expires 2026-10-24.
- [x] Downloaded and inspected the run #185 character audit. The static source inventory remains 43 declared selectable entries (including six existing native forms), with 27 more declared entries needed to reach 70. Gameplay-verified playable count remains unmeasured.
- [x] The XML-comment parsing fix improved the XML-to-atlas report: **40/43** entries now have no missing frame-name references. Remaining name-level exceptions: Asuma (12), SageJiraiya (6), and RockLee (55). Investigate actual atlas dependencies before editing.
- [x] Character selection art: **37/43** entries have all three expected selection frames/files; SageJiraiya, ImmortalSasuke, SageNaruto, RikudoNaruto, RockLee, and Nagato remain partial. The forms share base-art aliases, so this is not evidence of unique portrait compliance.
- [x] Skill-description label frames: **42/43** entries pass; Kabuto still requires manual review. Kill/death report portrait frames are present for all 43 declared entries.
- [!] Off-roster Han and Roshi each have Guardian XML/plist/texture, report portraits and exact-name audio files, but neither has a HeroEnum entry, selection frames, nor skill-icon frames. The shared Guardian AI behavior and resources alone do not prove they work as player-controlled characters; do not count them as playable yet.
- [ ] Next: inspect the remaining XML/atlas exceptions and selection-art generation path; continue searching for distinct Senki characters with complete resource packages, prioritizing filling pages 1–3. A new character only counts after unique selection portrait/name, skill UI, class/provider/enum wiring, animations/effects/audio references, AI/player behavior, and in-game verification are covered.
- [ ] This successful artifact is still a diagnostic build assembled from a pinned external source in a temporary CI workspace, not the final unified mod APK and not a physical-device-tested release.

## Latest continued-work update — run #186 (2026-10-10)

- [x] Continued polling run #186 until GitHub reported a terminal result; it completed **SUCCESS** with all 37 workflow steps successful and no failed steps: https://github.com/kage049754/Senki/actions/runs/38036488927
- [x] Verified the current-run APK artifact `naruto-senki-v2-candidate-debug-apk` (83,320,922 bytes; SHA-256 `a92b3189c9ffbab39c43a50d921c9e4bb7de8a396c1f518f7c53351fa5b313da`, artifact ID 11664052182, expires 2026-10-24) and downloaded it for artifact inspection.
- [x] Downloaded and inspected the audit artifact (3,615 bytes; SHA-256 `ea85affb98d03244af748b2790e88a3ccc0ada134bd4280326f389a1543da1a8`, artifact ID 11663777243).
- [x] The shared-atlas audit improvement resolved all name-level XML-to-atlas warnings: **43/43** declared entries now have no missing XML frame names when the audit includes the character's separate skill atlases and explicit base-character aliases.
- [!] Selection art is still only **37/43** complete by the static frame/file check. The six flagged entries are SageJiraiya, ImmortalSasuke, SageNaruto, RikudoNaruto, RockLee, and Nagato; some are form/base aliases, but this does not meet the unique-portrait requirement for distinct additions.
- [!] Kabuto still has **0/5** expected skill-description label frames and requires a runtime/UI dependency fix or explicit fallback, not merely an audit suppression.
- [ ] Roster remains **43/70 declared entries**; no new distinct external character has been integrated or gameplay-verified. Han/Roshi remain off-roster Guardian-resource leads until unique selection art, skill UI, player-control behavior, and permission status are resolved.
- [ ] Next implementation focus: repair Kabuto's skill-description label presentation and improve the source audit to verify the actual runtime lookup/fallback behavior. Then resume distinct-character integration research, keeping the page 1–3 priority and original background/page-button behavior.
- [ ] Build artifact verification is separate from installation or gameplay testing on a physical Android device.

## Latest continued-work update — run #188 (2026-10-10)

- [x] Continued polling run #188 through terminal **SUCCESS**: all 37 workflow steps passed, no failed steps: https://github.com/kage049754/Senki/actions/runs/38036909331
- [x] Verified current-run APK artifact `naruto-senki-v2-candidate-debug-apk` (83,312,356 bytes; SHA-256 `b592502ed3064a03bf2ccad1a106d4f33b449435099859a9feb99c0fde2e33aa`, artifact ID 11664048922; expires 2026-10-24).
- [x] Downloaded and inspected current-run audit artifact (3,663 bytes; SHA-256 `a32ccdc72c35f67499d05e54766fcbdbba2c01290c72074fc267648ea3cd25df`, artifact ID 11664058878).
- [x] The audit explicitly detects **5/5 Kabuto text fallback descriptions** in patched `SkillLayer.lua`, while still honestly reporting 0/5 Kabuto image-label frames. This separates runtime fallback coverage from sprite-frame coverage rather than hiding the missing art.
- [x] XML-to-atlas name coverage remains **43/43** after shared/skill atlas resolution; roster remains 43 declared entries, 27 below the 70-entry target.
- [ ] Next: audit the actual skill-label fallback behavior and source art needs, then continue the priority of integrating distinct characters into open slots on pages 1–3. Public repository presence alone is not a license grant; no new external character is counted until its source/reuse permission and runtime integration are validated.
- [ ] This is still a diagnostic build from a pinned external source in a temporary CI workspace, not the final unified game release and not a substitute for physical-device gameplay testing.

## Continued-work update — run #192 (2026-10-10)

- [x] Rechecked run #192 through terminal **SUCCESS** after fixing the regex failure from run #191: https://github.com/kage049754/Senki/actions/runs/38037457581
- [x] Verified the run produced the diagnostic APK artifact `naruto-senki-v2-candidate-debug-apk` (83,345,639 bytes; artifact ID `11663773527`; GitHub artifact digest `sha256:8b1d535723ae346b1ed3bcb6a67735499fcef21d2c761ce74dc9ba91ed245e08`; expires 2026-10-24).
- [x] Downloaded and inspected audit artifact `senki-character-package-audit` (artifact ID `11664488112`; digest `sha256:b27e6daa23bf705c2c16edddebf9c91a2c194834db29f02aad4d1577edd4c71b`). Audit reports 43 selectable UI entries but only **37 entries after excluding six known alternate forms**; **33 additional distinct characters** are needed to reach the 70-distinct-character target.
- [x] The audit still finds selection-art gaps for six current entries, 42/43 skill-description label frames (Kabuto uses a 5/5 text fallback), and 43/43 XML-to-atlas name coverage. These are static checks, not runtime playability proof.
- [ ] Next: investigate character-selection slot wiring and the Guardian/Han/Roshi lifecycle further, while keeping unlicensed external assets out of the build. Find a complete distinct-character source with explicit reuse terms or prepare a permission-safe implementation plan before roster integration.
- [ ] No new distinct character has been integrated or gameplay-verified. Device testing remains separate from CI build/artifact verification.

## Continued-work update — run #195 (2026-10-10)

- [x] Run #195 reached terminal **SUCCESS** after inspecting and fixing run #194's Python syntax error: https://github.com/kage049754/Senki/actions/runs/38038427248
- [x] Verified diagnostic APK artifact `naruto-senki-v2-candidate-debug-apk` (83,323,437 bytes; artifact ID `11665320110`; digest `sha256:04a1b487e0f779233a348f12311e85a649f92f67013fdc8b0031be4b4829d931`). This remains a diagnostic candidate, not device-tested gameplay.
- [x] Downloaded and inspected audit artifact `senki-character-package-audit` (artifact ID `11665246523`; digest `sha256:1c8951908bb3ae559375b944201b659d0355399e1cd0a3695ba1eb802362435c`). The report now explicitly flags Guardian's source-level AI combat override while warning this is not proof of player control for Han/Roshi.
- [x] Static inventory remains **43 selectable UI entries / 37 after excluding six known alternate forms**, 33 distinct characters short of 70; gameplay-verified count remains unmeasured.
- [ ] Next: continue investigating distinct-character candidates with explicit reuse permission and compatible complete resources. Do not add Han/Roshi as selectable characters until a player-controlled Hero lifecycle and all selection, skill, portrait, effects/audio, AI, death/respawn, and gameplay checks are completed.

## Continued source research — 2026-10-10

- [x] Rechecked additional public source repositories for licensing metadata. `Fansirsqi/NarutoSenki` has Mulan PSL v2 repository metadata, but the inspected tree is an APK-style extracted asset package rather than editable character source; the license does not independently establish rights to third-party Naruto art/audio. It is not used as an asset source.
- [x] Compared `kuiyr0810/NarutoSenki-V2`; its visible roster layout is the same 43-entry pattern and no new distinct selectable character was found in the inspected layout. No license file or GitHub license metadata was present in the checked branch.
- [x] Also checked `likill/NarutoSenki-master`, `LeaderOnePro/NarutoSenki1.17Mod`, and `Zx-Akito/NarutoSenki-Release`; no clear reuse license was found in the inspected default branches, and the release-only repository lacks a source tree.
- [x] Corrected README wording to distinguish 43 UI entries from 37 distinct base characters. No new character was added or counted.
- [ ] Continue searching for explicit permission/licensing and complete distinct character packages. Current public mod sources remain research leads, not automatically reusable content.
