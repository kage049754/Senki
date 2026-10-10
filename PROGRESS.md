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
