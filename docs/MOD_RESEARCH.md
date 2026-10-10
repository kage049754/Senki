# Naruto Senki / Mod Research Inventory

> **Project rule: this is research for modding and merging the user's selected Naruto Senki: V2 game, not creating a new game.** The release reference is https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix. The goal is to obtain and verify its editable source base, then integrate compatible mod content into kage049754/Senki. See docs/BASE_GAME.md.

**Last reviewed:** 2026-10-10  
**Status:** User-selected target is Naruto Senki V2. The strongest source candidate has been structurally verified, but code/asset reuse permission remains unresolved; no source has been imported.

## Candidate classification
- **Source candidate:** likely contains editable source; inspect the complete tree, build scripts, license, and assets.
- **Release/changelog reference:** helps research characters/features but is not necessarily editable source.
- **Fork:** compare with upstream; do not count as independent without meaningful changes.
- **Support repository:** files, translations, docs, or website; not necessarily a playable implementation.
- **Unverified:** name/search result alone is not enough to confirm its identity or contents.
- **Unrelated game/mod:** not a drop-in Senki implementation.

## User-selected release reference (not editable source)

- Release listing: https://github.com/Naruto-Senki/files/releases
- Selected reference: https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix
- The GitHub release API lists NSV2_2.1.6-fix_Android.apk (about 159 MB), plus iOS and Linux packaged assets.
- Repository metadata describes Naruto-Senki/files as a V2 File Host and reports no repository license. The release page is the selected game/reference, but its APK is a binary and cannot serve as the editable source tree. Do not assume the absence of a license grants redistribution/modification rights.
- Status: user-selected target; source import and rights review pending. Keep this release link in the main README and docs/BASE_GAME.md.

## Candidate repositories

### Naruto Senki V2 source family
- Candidate: https://github.com/Zx-Akito/NarutoSenki-V2
- Candidate fork: https://github.com/kuiyr0810/NarutoSenki-V2
- Documentation: https://github.com/Zx-Akito/NarutoSenki-V2/blob/master/Doc/README_ZH.md
- Verified on 2026-10-10: public Cocos2d-x/C++ project with Lua scripts, resources, engine/dependency directories, build scripts, and `projects/NarutoSenki/proj.android-studio` containing Gradle files and wrapper.
- Default branch: `master`. The repository metadata reports it is a fork of `real-re/NarutoSenki-V2-old` (parent marked private); latest visible commits inspected were dated 2026-05-09.
- No root `LICENSE` was found and GitHub metadata reports no declared license. Bundled game assets' separate rights are not established.
- **Status:** technically credible source candidate, but `PERMISSION_REQUIRED`; do not copy wholesale into the central repo until code and asset permissions are resolved. Exact correspondence with release `v2.1.6-fix` is also unverified.
- Additional mirrors/forks checked: `kuiyr0810/NarutoSenki-V2`, `SILXNTRAY/NarutoSenki-V2`, `sansaks-jpg/NarutoSenki-V2`, `hitlabmodv2/NarutoSenki-V2`, `BF667/NarutoSenki-V2`, `rikudousennin22/NarutoSenki-V2`, and `dont-cry-522/NarutoSenki-V2`. Their repository metadata also reports no declared license, so they do not resolve the permission blocker. Several are mirrors/forks rather than independent sources.

### Naruto Senki release history
- https://github.com/Zx-Akito/NarutoSenki-Release
- Prior notes identify release/changelog history around v1.24–v1.26 beta and various characters/modes/bug fixes.
- Use as a feature/roster reference unless editable source and reuse rights are verified. Release notes are not permission to copy assets.

### Older Naruto Senki source candidate
- https://github.com/LeaderOnePro/NarutoSenki
- Prior notes indicate `Classes`, `Resources`, `proj.win32`, Cocos2d-x 2.2.2 / Visual Studio 2010.
- Audit current contents, Android build support, history, license, and asset terms before deciding whether it is a viable base or source of specific compatible fixes.

### Supporting repositories
- V2 file host: https://github.com/Naruto-Senki/files
- Localization: https://github.com/Naruto-Senki/localization
- Website/docs: https://github.com/real-re/nsv2-website
- Treat these as supporting references unless actual editable game source is verified.

### Unverified search lead
- https://github.com/search?q=NarutoSenki1.17Mod&type=repositories
- Prior search did not reliably identify the owner/full repository or enough source-tree details. Find the exact repository, inspect it, compare its fork parent/history, and check terms before treating it as a candidate.

## Search starting points
- https://github.com/topics/naruto-senki
- https://github.com/topics/naruto-game
- https://github.com/search?q=NarutoSenki&type=repositories
- https://github.com/search?q=Naruto+Senki+mod&type=repositories
- https://github.com/search?q=%E7%81%AB%E5%BD%B1%E6%88%98%E记&type=repositories

Search results are not proof that all mods have been found. Some are private, deleted, renamed, APK-only, mirrors, or unrelated Naruto games. Do not claim completeness.

## Required source audit for every candidate
Record:
1. Canonical repository URL, owner, default branch, latest relevant commit.
2. Original/fork/mirror status, upstream, and meaningful changes compared with upstream.
3. Actual engine/language, build system, dependencies, and Android build feasibility.
4. Exact source paths inspected; whether editable character, skill, animation, effects, minion/tower, UI, and map implementations exist.
5. Useful mod differences and known conflicts with the chosen base.
6. License file, third-party notices, asset-specific terms, and permission decision.
7. Classification: candidate base, compatible source for selected content, reference-only, or excluded.
8. Exact components actually integrated and their build/gameplay test evidence.

## Base selection rule
The user has selected Naruto Senki V2 as the intended foundation. Continue validating the existing V2 source and permission status before importing it. Preserve its engine and original gameplay wherever practical. Keep `kage049754/Senki` as the central integration workspace. Do not extend the Kotlin/Canvas prototype into a new game while the base is unresolved. After selection, document why the base won, what will be migrated, and how attribution/permissions are handled.

## Merge rules
- Merge compatible source changes/content in controlled batches; do not blindly combine whole repositories or APKs.
- Keep one unified game and one final APK.
- Adapt characters, skills, animations, effects, maps, and UI to the selected base's existing systems rather than inventing a replacement engine.
- Compare forks before using their changes; avoid duplicate content.
- Do not extract and redistribute APK contents without permission.
- Public visibility does not mean public domain.
- If terms are unclear, do not import/redistribute the content; mark it reference-only/excluded until resolved.
- Never label a component “merged” until the unified project builds and the relevant in-game behavior is tested.

## Roster growth
Expand the selected game's existing roster with compatible and permitted content. A target of 70+ characters is desirable if the base/content support it, but this target must never justify starting a new engine. Track discovered, planned, integrated, build-verified, and device-tested counts separately. Alternate forms should be distinct entries only when appropriate and meaningfully different.


## Second-pass fork/license metadata check (2026-10-10)
A fresh metadata check of the following additional or previously identified V2 forks found no declared GitHub license in each repository's metadata:
- `SILXNTRAY/NarutoSenki-V2` (fork lineage not shown by metadata response).
- `sansaks-jpg/NarutoSenki-V2` (fork lineage not shown by metadata response).
- `hitlabmodv2/NarutoSenki-V2` (fork of `SILXNTRAY/NarutoSenki-V2`).
- `ZhReimu/NarutoSenki-V2` (fork of `Fansirsqi/NarutoSenki-V2`).
- `roktra4/NarutoSenki-V2` (fork of `Zx-Akito/NarutoSenki-V2`).
- `dont-cry-522/NarutoSenki-V2` (fork of `Zx-Akito/NarutoSenki-V2`).

This metadata check does not prove that no separate permission statement exists elsewhere, but none of these mirrors resolves the licensing issue by itself. Do not infer a license from fork activity, recent updates, or public accessibility.


## Older Cocos2d-x source-family metadata check (2026-10-10)
A metadata pass on the older `NarutoSenki-cocos2dx` source family found no declared GitHub license for:
- `LeaderOnePro/NarutoSenki-cocos2dx` (candidate upstream).
- `dadafei8/NarutoSenki-cocos2dx` (fork of the candidate upstream).
- `Heachy/NarutoSenki-cocos2dx` (fork of the candidate upstream).
- `wuhewanxiang/NarutoSenki-cocos2dx` (fork of the candidate upstream).

These may be useful for technical comparison only; this metadata result does not establish code or asset reuse rights. They do not currently provide a permission-cleared replacement for the selected V2 source.


## Third-pass repository search — 2026-10-10

### `LeaderOnePro/NarutoSenki1.17Mod` — APK/decompiled package, not a source base
- Repository: https://github.com/LeaderOnePro/NarutoSenki1.17Mod
- Description identifies it as a custom mod based on Naruto Senki 1.17.
- GitHub metadata: public, non-fork repository; default branch `main`; repository size reported as 37,613 KB; no declared license.
- Root tree inspection found Android package/decompiled distribution artifacts such as `AndroidManifest.xml`, `classes.dex`, `resources.arsc`, `META-INF/`, `lib/`, `res/`, and `assets/`; this is not an editable Cocos2d-x game source tree.
- A similarly named `wsnbbnbb/NarutoSenki1.17Mod` appears in search results with the same reported repository size; treat it as a likely mirror/duplicate until commit/tree comparison proves otherwise.
- Classification: **APK/package reference only; not a compatible source base at present.**
- Reuse status: **PERMISSION_REQUIRED**; no license declared, and included Naruto/game assets are not cleared. Do not extract, copy, or redistribute its assets/binaries into the V2 project.
- Use: metadata and public documentation may inform the inventory; do not count this as a source-level mod integrated into V2.

### Search outcome and next audit targets
- The search surfaced an explicit 1.17 mod repository, but its package-oriented tree does not solve the editable-source or permission blocker.
- Continue auditing the older editable-source family `LeaderOnePro/NarutoSenki` and compare it with the existing V2 candidate by actual source structure, Android build support, provenance, and rights. Do not switch away from the user's selected V2 target merely because another repository is easier to find.
- Search is ongoing and not exhaustive. Repository names/search snippets are leads, not evidence of unique content or permission.


### Detailed audit: `LeaderOnePro/NarutoSenki` — older editable source, not the selected V2 base
- Canonical repository: https://github.com/LeaderOnePro/NarutoSenki
- Description: “火影战记源代码” (Naruto Senki source code); default branch `master`; repository metadata reports no declared license.
- README identifies Cocos2d-x 2.2.2 and Visual Studio 2010 as the framework/build environment and points to a Windows-era setup. It does not document a maintained Android Studio/Gradle project.
- Tree inspection verified editable C++ files under `Classes/`, including `Characters.cpp`, `ActionManager.cpp`, `GameLayer.cpp`, `HudLayer.cpp`, `JoyStick.cpp`, `LoadLayer.cpp`, and other game systems. `Resources/` includes game resource bundles such as audio, effects, element data, maps, menu assets, and other packaged game content.
- Technical value: useful as a reference for legacy character/action/skill architecture and comparison of the original 1.x-style Cocos2d-x implementation.
- Limitations: Windows/VS2010-oriented setup; no verified Android build path from the inspected root; its architecture/version is not shown to be compatible with V2's Cocos2d-x/C++/Lua Android project.
- Rights: no declared repository license; source and Naruto/game assets have not been cleared for reuse.
- Classification: **reference-only; not selected as the V2 foundation and not approved for source/assets import.**
- Decision: do not switch the user-selected V2 target to this older project simply because it exposes C++ files. Reconsider only if the user explicitly changes the target and code/asset permissions are established.

### Duplicate check: `wsnbbnbb/NarutoSenki1.17Mod`
- GitHub metadata marks it as a fork of `LeaderOnePro/NarutoSenki1.17Mod`; both report the same repository size and the same two commits (initial commit and README update) in the inspected history.
- Classification: **duplicate fork/mirror, not an independent mod**. Do not count it as a separate content source or merge candidate.


### Newly identified stronger technical candidate: `Wilykun/NarutoSenki-V2`
- Canonical repository: https://github.com/Wilykun/NarutoSenki-V2
- GitHub metadata identifies it as a fork of `hitlabmodv2/NarutoSenki-V2`; that parent is itself in the Naruto Senki V2 source family. It is therefore a V2-derived project, not a separate replacement game.
- The fork is 15 commits ahead of its parent at the comparison inspected on 2026-10-10. The diff includes an Android APK build workflow, changelog/readme updates, C++ game-loop/mode changes, a new AI-vs-AI Spectate mode, mode UI changes, and a few Lua/UI/resource changes.
- Its changelog describes Spectate as AI-vs-AI matches from 1v1 through 5v5, camera tracking, live team/fighter statistics, and visual/menu changes. This is a fork author's own changelog, not independent gameplay verification by this project.
- The GitHub Actions run `37911640387` completed **successfully** on commit `527e7766a26484cfc3cbe6748cf41fb469720e41`; the build, APK existence/upload steps passed. Artifact `NarutoSenki-debug-apk` is present (86,137,495 bytes; SHA-256 `9400c4d1db9b3f09630824a27656160e737876e3383ad234340a87082c3585e6`; expires 2027-01-07). This is the fork's own artifact, not an artifact built in `kage049754/Senki` and not a device test performed here.
- Its workflow uses JDK 17 and installs Android platform 34, build-tools 34.0.0, and NDK 21.4.7075529, then runs `./gradlew assembleDebug` in `projects/NarutoSenki/proj.android-studio`. This is a stronger observed CI signal than the previously inspected unbuilt V2 candidate.
- Repository metadata reports **no declared license**. Naruto character artwork, sprites, audio, animation, and inherited code/dependencies are not cleared by the successful build. The README credits the parent project, but attribution alone is not a license.
- Classification: **top technical candidate for a V2-derived base pending code/asset permission review and exact comparison with the user's v2.1.6-fix reference**. Do not import/redistribute its source/assets or publish its APK through this project until permission is established.
- Next technical checks: inspect its full build docs and source provenance; compare its changes against the selected release and other forks; document permission evidence; then, once approved, adopt one base and bring up CI in the central repository before merging additional mods.


### Android-only V2 clean base candidate: `muhammadadilsyaputra08-alt/NarutoSenki-Custom`
- Repository: https://github.com/muhammadadilsyaputra08-alt/NarutoSenki-Custom
- README describes an Android-only working base extracted from Naruto Senki V2, with Cocos2d-x 2.2.6, C++ gameplay, Lua/LuaJIT, Android Studio/Gradle/NDK, and `projects/NarutoSenki/proj.android-studio`.
- The root contains engine/source/resource directories (`cocos2dx/`, `CocosDenshion/`, `extensions/`, `external/`, `scripting/`, and `projects/`) and an Android-focused workflow.
- Latest inspected commit: `279e85e73040558c84988a0eea310b6286eb77f0` (“fix bug & nerf”, 2026-09-09).
- Its Actions run `34331260360` completed **successfully**; SDK/NDK provisioning, `assembleDebug`, APK discovery, and artifact upload passed. Artifact `narutosenki-debug-apk` exists (83,468,934 bytes; SHA-256 `5704b77cdd63369b83e74febc03d640628220e4512d43f12832063522ce72271`; expires 2026-12-08). This is the candidate's artifact, not a build from the central Senki repo and not physical-device verification.
- The workflow intentionally uses JDK 17 for SDK provisioning then JDK 8 for legacy AGP 3.3.3, and pins NDK r21e; this is useful evidence for recreating a compatible build environment.
- GitHub metadata reports no declared license. The README says the source was extracted from original V2, but that statement alone does not establish permission for code or bundled Naruto assets.
- Classification: **strong Android build candidate for technical comparison, pending permission/provenance review and exact comparison to the user's v2.1.6-fix reference**. Do not import or redistribute until rights are established.
- Decision: retain the selected target (existing Naruto Senki V2); evaluate this clean Android snapshot against the Wilykun fork before choosing one technical base. Do not merge two full source trees.


### Additional candidate: `likill/NarutoSenki-master` — legacy local PvP/co-op work
- Repository: https://github.com/likill/NarutoSenki-master
- Description says the project focuses on local PvP/co-op. README and tree identify Cocos2d-x 2.2.2, Visual Studio 2010, `Classes/`, `Resources/`, and Windows project files; no Android Studio project was found in the root listing.
- Recent commits include a local dual-player PvP plan, configurable UI sizing, and control-remapping work. The repository has a `V2` release containing a Windows `NarutoSenki.rar` package, not an Android APK.
- GitHub metadata reports no declared license. Source and bundled game assets are not cleared.
- Classification: **feature reference only for local PvP/co-op/control ideas; not a drop-in Android/V2 source base**. Do not merge its legacy implementation into V2 without a compatibility analysis and explicit rights.

### Candidate comparison snapshot (2026-10-10)
| Candidate | Source/build evidence | Potential value | Current blocker |
| --- | --- | --- | --- |
| `Wilykun/NarutoSenki-V2` | V2-derived; 15 commits ahead of parent; its Android Actions build and artifact verified | Spectate mode, mode UI, cross-platform build fixes | No declared license; inherited code/assets not cleared; exact release match unverified |
| `muhammadadilsyaputra08-alt/NarutoSenki-Custom` | Android-only V2-derived source snapshot; its Android Actions build and artifact verified | Cleaner Android-only tree; documented JDK 8/NDK r21e setup | No declared license; extraction provenance/asset rights not cleared |
| `Zx-Akito/NarutoSenki-V2` | Editable C++/Lua/Cocos2d-x Android project inspected; no build run in central repo | Broad V2 source tree/reference | No declared license; legacy toolchain; exact release match unverified |
| `LeaderOnePro/NarutoSenki` | Editable legacy C++/resources; Cocos2d-x 2.2.2 / VS2010 | Older character/action implementation reference | No declared license; no verified Android build path |
| `likill/NarutoSenki-master` | Legacy Cocos2d-x 2.2.2/VS2010; Windows package release | Local PvP/co-op and control/UI reference | No declared license; not a verified Android base |
| `LeaderOnePro/NarutoSenki1.17Mod` | APK/package-oriented root tree | Historical 1.17 mod reference | No declared license; not editable game source |
 
**Selection remains conditional:** prefer one V2-derived Android source tree after permission/provenance review. Do not combine entire forks; compare diffs and cherry-pick only compatible, permitted changes into the single selected base.

## Search directive: personal-use mod development (2026-10-10)
Continue candidate discovery and technical evaluation even where a source repository does not include an explicit license. Search public forks, mod variants, archived releases, mirrors, and other accessible source/download pages. Look for complete Android V2 builds and useful character/skill/animation/effect/stage/UI additions. A missing license is not a reason to stop private build-feasibility testing.

For every promising candidate, record the source URL, revision/release, engine, Android build path, included game components, unique mod features, and whether we actually built it. Test it in an isolated workspace before merging into kage049754/Senki. Keep attribution/provenance factual; do not invent permissions or license terms. The current priority is the user's personal working APK and device testing, not publishing or redistributing the candidate.


## Fifth-pass V2 fork and build-artifact audit — 2026-10-10

### Additional candidates found
- `sansaks-jpg/NarutoSenki-V2` — public repository described by its owner as a personal-development mirror. It has the expected full Cocos2d-x/C++/Lua V2 tree and a GitHub Actions workflow with 59 recorded runs; its latest visible run (2026-09-15, run 35014823951) completed successfully. Recent history includes LAN multiplayer fixes, so this is a meaningful additional candidate to diff against the simpler V2-derived bases rather than assuming it is just a byte-for-byte mirror. No declared GitHub license was found. Inspect its changed files, Android output and feature stability before choosing it.
- `SILXNTRAY/NarutoSenki-V2` — public full-tree upload, but only two recent “Add files via upload” commits were visible; no Actions runs were found. Treat as a possible source mirror, not an independently verified mod.
- `hitlabmodv2/NarutoSenki-V2` — fork of SILXNTRAY's repository; no Actions runs found. Do not count as an independent mod without a meaningful diff.
- `kuiyr0810/NarutoSenki-V2` — fork of `Zx-Akito/NarutoSenki-V2`, labelled as an early open-source version; source size is smaller and its history diverges. Keep as a compatibility/history candidate.
- `BF667/NarutoSenki-V2` — fork of the early-version mirror, last source push in 2021; lower priority.
- `ZhReimu/NarutoSenki-V2` — older fork with last source push in 2021; lower priority.
- `rikudousennin22/NarutoSenki-V2` — fork of the already inspected Zx-Akito source; no independent feature claim established yet.

### Build workflow improvement
- Updated `.github/workflows/v2-source-smoke.yml` in commit `fe22f50b802b798802a06c383b8e91e726dd2e09` so a successful candidate build uploads `naruto-senki-v2-candidate-debug-apk` as a 14-day Actions artifact for private testing. This changes artifact retention only; it does not import the candidate source into the central repository or claim a final unified build.
- The prior candidate compile succeeded in run `37965165366`, but that run predates the artifact-upload change and did not publish an APK. The new workflow revision has not yet been observed in a new Actions run; do not claim the new artifact exists until a new run succeeds and its artifact list is checked.

### Next audit
1. Diff the active `sansaks-jpg` source branch against the pinned, already build-tested Android candidate; identify its exact Android source commit and any LAN-specific modifications.
2. Check its latest successful build artifact metadata and Android workflow configuration.
3. Trigger/re-run the central candidate workflow when repository Actions permissions allow, then verify run conclusion and artifact metadata.
4. Choose the source with the best reproducible Android build and feature baseline, then plan controlled integration into this central repository. Keep CI success and physical phone testing as separate gates.


## Candidate APK artifact verification — 2026-10-10
- The first artifact-enabled run (`37966549532`) started but Gradle hit legacy Android SDK repository metadata parsing errors; a follow-up workflow revision isolated the SDK root.
- Successful run: `kage049754/Senki` Actions run `37966861114`, commit `fcccc784c39f0f33c041c4d00bb39b3408ccaef9`.
- Verified artifact `naruto-senki-v2-candidate-debug-apk` (ID `11634177274`, 83,435,979-byte ZIP, expiry 2026-10-23). This is a CI-produced debug APK of the pinned `muhammadadilsyaputra08-alt/NarutoSenki-Custom` source, built in a temporary runner workspace. It is not yet the integrated modded game.
- The isolation fix is in `.github/workflows/v2-source-smoke.yml`: install only required legacy packages under a clean `$RUNNER_TEMP/android-sdk` and set SDK environment variables for subsequent Gradle steps.
- Next: compare the more feature-rich `sansaks-jpg/NarutoSenki-V2` source against the current pinned candidate; do not treat its expired prior artifact as downloadable. Keep the central candidate artifact build as a known-good build-environment baseline.


## Sixth-pass source feature comparison and build — 2026-10-10
### Feature-rich LAN-enhanced V2 candidate
- Inspected `sansaks-jpg/NarutoSenki-V2` branches and commit diffs. Branch `fix/lan-multiplayer-audit-hardening` is pinned at `1751b7fb8f05a96ff6e85bc8a6c8e3fdcca3f74a`; its history includes LAN hotspot multiplayer, reliable battle/session ordering, rejoin fixes, app-background forfeit behavior, crash-safe overlay cleanup, and runtime UI localization. These are meaningful source changes, not just a renamed copy.
- Added central diagnostic build workflow `.github/workflows/v2-lan-candidate.yml` (commit `6cc298c6791a42f00aa4a3ec968705255f95a4a7`) using the candidate's legacy NDK r17c / Java 8 build requirements.
- Run `37967514487`: **SUCCESS**. Verified artifact `naruto-senki-v2-lan-candidate-apk`, ID `11633633661`, ZIP size 80,405,874 bytes, expiry 2026-10-23.
- This candidate now has a verified central-CI APK artifact alongside the Android-clean candidate. The LAN-enabled branch is not yet selected as the central source base; compare source/resource deltas and keep optional LAN functionality isolated if offline-only gameplay is the target.



## Direct source-tree comparison — 2026-10-10
- Compared recursive Git trees for Android-clean commit `279e85e73040558c84988a0eea310b6286eb77f0` and LAN-enhanced commit `1751b7fb8f05a96ff6e85bc8a6c8e3fdcca3f74a`.
- Tree sizes: Android-clean 1,903 tracked files; LAN-enhanced 2,618. Of 1,886 common paths, 1,828 have identical blob hashes and 58 differ. The LAN tree has 732 paths not present in the Android-clean tree, largely desktop/platform content plus LAN networking. Android-clean has 17 unique paths.
- Important roster finding: Android-clean uniquely contains `Classes/Core/Shinobi/Kabuto.hpp`, `Bunshin/KabutoClone.hpp`, Kabuto sprite/plist/XML assets, Kabuto audio, and projectile data. The inspected LAN-enhanced branch does not contain `Kabuto.hpp`. The Android-clean README calls it a clean base, but it contains this substantive custom Kabuto redesign and is not simply an untouched vanilla snapshot.
- Practical direction: **use the successfully built Android-clean source as the current lead candidate** for an Android/offline-first mod base because it is smaller and preserves the unique Kabuto content. Treat LAN-enhanced V2 as a source for selective crash fixes and optional networking research, not a wholesale replacement. Do not copy all 58 changed files at once; review and port individual fixes with tests.
- This is a provisional engineering recommendation based on tree/build evidence, not yet the final source import. Both candidates have successful central CI artifacts; neither has been tested on the user's phone.



## First central patch verified inside the APK — 2026-10-10
- Added `patches/android-clean/0001-custom-app-identity.patch` to give the candidate a distinct install identity and version/label: `com.senki.naruto.mod`, `2.1.0-mod`, code 3, `Naruto Senki Mod`.
- Updated the central Android-clean candidate workflow to apply all ordered `patches/android-clean/*.patch` files to the pinned source and refuse to build if the patch series is empty.
- Added a post-build `aapt dump badging` check for package ID, version, and app label.
- Run `37968632537`: **SUCCESS**; patch application, Gradle build, APK existence, package identity checks, and artifact upload all passed.
- Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11634478692`, 83,447,929-byte ZIP, expiry 2026-10-23. This confirms a centrally maintained patch can alter the real V2-derived APK while retaining the existing game engine; it is not yet a gameplay/UI redesign or phone-tested release.


## Custom UI artwork and package verification — 2026-10-10
- Added source-controlled vector artwork: `artwork/senki-launcher.svg`, `artwork/senki-launcher-foreground.svg`, `artwork/senki-loading.svg`, and `artwork/senki-select.svg`.
- The workflow renders the launcher icon to all Android density folders, renders the loading and selection backgrounds to 1280×720 PNGs, applies the background-color update, and then builds the APK.
- `0002-custom-loading-screen.patch` replaces the old loading bars/title/clouds with the custom background while keeping the existing tips and animated loading indicator.
- `0004-custom-character-select-background.patch` replaces old decorative background/chrome only. It leaves character buttons, grid/paging, hero portrait/name, selection logic, and start-game behavior intact.
- The first color patch attempt failed because its unified-diff hunk was malformed. That failure was inspected, the bad patch file was removed, and the color is now set explicitly in the artwork-render step; subsequent build succeeded.
- Run `37971031426`: **SUCCESS**. Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11636815575`, 83,466,499-byte ZIP, expires 2026-10-23. The job's archive inspection found both custom backgrounds inside the APK; `aapt` verified `com.senki.naruto.mod`, version `2.1.0-mod`, code 3, and label `Naruto Senki Mod`.
- The APK is still a CI candidate. No phone installation or visual/gameplay test has been recorded.


## Main menu redesign — 2026-10-10
- Added `artwork/senki-menu.svg` and `patches/android-clean/0005-custom-main-menu-background.patch`.
- Replaced the old main-menu bars/clouds/title decoration in `StartMenu.cpp` with the custom Senki background; existing game-mode carousel and menu callbacks are untouched.
- Updated CI to render and verify `assets/senki_menu.png` inside the APK.
- Run `37971712613`: **SUCCESS**. Verified artifact `naruto-senki-v2-candidate-debug-apk`, ID `11637705354`, 83,718,905-byte ZIP, expiry 2026-10-23. The APK archive contains `assets/senki_loading.png`, `assets/senki_select.png`, and `assets/senki_menu.png`; app identity assertions also pass.
- Current custom UI coverage: launcher icon, main menu background, loading background, and character-selection background. Gameplay code and character selection mechanics remain from the V2-derived base.


## Latest verified candidate — 2026-10-10
- Updated character-selection guidance to state the existing tap-once preview / tap-again confirm interaction.
- Run `37972501198`: **SUCCESS**, artifact `naruto-senki-v2-candidate-debug-apk` (ID `11637936223`, 83,729,869-byte ZIP, expires 2026-10-23).
- The archive contains `assets/senki_loading.png`, `assets/senki_select.png`, and `assets/senki_menu.png`; package ID/version/label checks passed.
- No phone runtime test is claimed.


## Selectable roster inventory for Android-clean candidate — 2026-10-10

Pinned source `muhammadadilsyaputra08-alt/NarutoSenki-Custom@279e85e73040558c84988a0eea310b6286eb77f0` was inspected directly:
- `lua/class/basic.lua` defines `ns.CharactersLayout` with **37 unique selectable character names**: Naruto, Sakura, Sai, Kakashi, Shikamaru, Ino, Choji, Asuma, Kiba, Hinata, Shino, Neji, Tenten, Lee, Tobirama, Hiruzen, Minato, Jiraiya, Tsunade, Orochimaru, Gaara, Kankuro, Chiyo, Sasuke, Karin, Suigetsu, Jugo, Kabuto, Tobi, Konan, Pain, Deidara, Kakuzu, Hidan, Kimimaro, Itachi, Kisame.
- The C++ `Classes/Core/Shinobi/` folder contains 42 headers, including five Pain-path implementation classes in addition to the selectable character classes. Header count is not a playable-roster count.
- Direct comparison against `sansaks-jpg/NarutoSenki-V2@1751b7fb8f05a96ff6e85bc8a6c8e3fdcca3f74a` confirms Android-clean uniquely includes `Kabuto.hpp`; the LAN candidate has no `Kabuto.hpp`.
- Kabuto is a substantive custom kit implementation with skills, effects, audio/resource definitions, and behavior changes, not just a portrait. It remains source-inspected only; the current CI build has not verified the character in live battle.
- The selectable layout has 37 unique entries, but the number of fully functional and device-tested characters is **not yet measured**. Do not label all 37 as verified playable until runtime checks pass.
- Next roster phase: inventory per-character C++ class, XML/config, sprite/plist, effects, audio, skill IDs and selection assets; then identify mod sources that add unique compatible characters without replacing the V2 engine.


## Seventh-pass legacy source and mod inventory — 2026-10-10

### `LeaderOnePro/NarutoSenki-cocos2dx`
- Repository description identifies it as a Cocos2d-x 2.2.6 modernization of the original Naruto Senki source, with Windows/Android/macOS project folders.
- Root contains `projects/NarutoSenki/proj.android/`, Gradle wrapper/build files, Android manifest, and C++/resource directories. The README documents Android packaging with an old NDK toolchain; GitHub Actions has successful historical runs (latest inspected: `27602136103`, June 16, 2026).
- This is a useful legacy-source/build reference, but it is not confirmed as the selected V2 base. Treat it as a possible source for investigating older character logic and resource formats, not as a replacement for the Android-clean V2 candidate.
- No declared GitHub license was found. The project includes an explicit `licenses/` directory and `AUTHORS`; inspect individual dependency notices before using anything. Bundled Naruto/game content remains a separate issue.

### `Zx-Akito/NarutoSenki`
- Legacy source tree has `Classes/`, `Resources/`, and `proj.win32/`; README states Cocos2d-x 2.2.2 / Visual Studio 2010.
- `Classes/Characters.cpp` contains the older monolithic character/AI implementation. It references additional support entities (for example Pain paths and summons) but is not a modern per-character V2 module layout.
- No declared GitHub license was found. Classification: reference-only for tracing older mechanics/resources; Android build path not established.

### `RieyuXhen/NarutoSenki`
- Public source tree has `Classes/` and `Resources/` only; latest inspected commit adds resources (2025-08-01). No Android project or declared license was found in the root.
- Its `Characters.cpp` resembles the older monolithic source lineage, so do not count it as an independent new mod without a meaningful file/resource diff.

### `syahron951/NarutoSenki`
- This repository is a GameMaker project (`.yyp`, `sprites/`, `objects/`, `rooms/`, `scripts/`), not a Cocos2d-x Senki source tree. It may be an unrelated remake/prototype and is excluded from the V2 source-base shortlist.

### Roster evidence
- Pinned Android-clean V2-derived source has 37 unique selectable names in `lua/class/basic.lua`; 42 C++ Shinobi headers include five Pain-path classes. See `docs/CHARACTER_ROSTER.md`.
- No new character from these legacy references has been ported or counted as playable. Any candidate contribution must be mapped to the V2 resource formats, IDs, scripts, and animations before a controlled port.


## Eighth-pass modded-release character leads — 2026-10-10

### `Zx-Akito/NarutoSenki-Release` (legacy v1.x release line)
- Official public release listing: https://github.com/Zx-Akito/NarutoSenki-Release/releases
- Latest inspected release: `v1.26-beta-2`, APK asset `NarutoSenki-v1.26-beta-2.apk` (78,074,332 bytes; release metadata SHA-256 `8ac4869dfcfc5aed043a124d26298b47b91d6598a5dddfcdc56880ce031cdaef`; published 2026-09-12).
- Previous inspected `v1.26-beta-1` changelog names new characters: **Shizune, Hashirama, Rin, Sakon & Ukon, and Juzo**; it also brings back Jonin Minato and revises Zetsu, Awakened Sasori, Iruka, and Third Kazekage AI.
- Earlier v1.24/v1.25 release notes also name **Jirobo, Tayuya, Anko, Kurenai, Might Guy, Yamato, Sasori, Zetsu, Iruka**, and other changes.
- Important compatibility finding: v1.26-beta-1's notes explicitly say the game switched to **server-side processing** and added Global Chat. It is an APK-only release host, not an editable V2 source tree, and is not a direct offline-first base. Keep it as a lead for roster/skill research, not a source-integrated mod.
- No declared repository license was found; release notes alone do not expose the editable C++/Lua/resource files for the new characters. Do not count any of these as implemented or playable in this project.

### `FDPL Naruto Senki The Last Fixed V1.22` (third-party mod release lead)
- A public mod listing reports four character replacements/additions: **Might Guy (replaces Tenten), Hashirama (replaces Karin), White Mask Tobi (revamped, replaces Tobi), and Pain (replaces Kankuro)**, plus nine character revamps and a new map.
- This is a third-party APK/mod listing rather than a verified editable source repository. Treat the names and feature list as unverified leads until an original release/source and file inventory are inspected.
- Do not merge or count it as a new V2 roster addition yet; its slot-replacement approach also conflicts with the goal of expanding the existing roster without losing current entries.

### Next extraction/port research
- Prioritize finding editable character source/assets for the above leads and compare their implementation requirements with V2's C++ classes, XML/config files, sprite/plist sheets, effects, audio, and selection resources.
- Any import should be a small, auditable character batch with unique IDs and an APK build. APK-only release metadata is discovery evidence, not proof that the character can be ported or that its assets are already available.


## Ninth-pass V2 fork deduplication — 2026-10-10

A repository search for `NarutoSenki V2` returned several additional public mirrors/forks. Their metadata and branch-head commit SHAs were compared before treating them as new mod sources:

### `kuiyr0810/NarutoSenki-V2`
- GitHub metadata identifies it as a fork of `Zx-Akito/NarutoSenki-V2`, with the same source lineage through `real-re/NarutoSenki-V2-old`.
- The inspected `master` head SHA is exactly `ed4009cf443b82899bb0af0e20e3df97d16995d8`, identical to the inspected `Zx-Akito/NarutoSenki-V2` head.
- GitHub compare API result: `identical`, 0 commits ahead/behind, 0 differing files at those heads.
- No declared license found in repository metadata. **Classification: duplicate mirror, not an independent mod; no new content to port.**

### `BF667/NarutoSenki-V2`
- GitHub metadata identifies it as a fork of `kuiyr0810/NarutoSenki-V2`.
- The inspected `master` head `d1a01eb4a6c007a0aea429e8883a079e06ab7387` is 8 commits behind the current `kuiyr0810`/Zx-Akito head; it is a stale ancestor, not a newer independent mod.
- Recent visible commits in this older branch include parser/cache and map changes from 2021; no new roster contribution was verified by this metadata/history comparison.
- No declared license found. **Classification: stale duplicate/ancestor, reference-only; no merge recommended.**

### `Fansirsqi/NarutoSenki-V2` and `ZhReimu/NarutoSenki-V2`
- The inspected `master` heads both resolve to `093caa9be474f500b95a13d1cfdf9030cd7bed81`.
- GitHub compare API result: `identical`, 0 commits ahead/behind, 0 differing files at those heads.
- No declared license found. **Classification: duplicate fork pair, not two independent mod projects.**

### Research conclusion
These additional search hits are useful for tracing lineage but do not add verified unique characters or skills to the integration queue. Continue prioritizing source candidates with demonstrable unique changes (for example, the Android-clean candidate's Kabuto implementation) and compare exact commits/paths before planning any port. Current CI build evidence remains tied to the pinned candidate `muhammadadilsyaputra08-alt/NarutoSenki-Custom@279e85e73040558c84988a0eea310b6286eb77f0`; the duplicate forks above were not used to build the current artifact. All candidates remain unlicensed/unapproved for public redistribution unless separate permission evidence is found.

## Character-source research acceptance checklist

When researching a mod or candidate character, inspect the whole source package instead of counting only roster labels. For each candidate, look for selection portrait/avatar and button states; display name/ID and preview; skill-view data/icons/descriptions; character class and combat implementation; sprite sheets/atlases/plists and animation definitions; attack/skill/ultimate logic, projectiles/summons and effects; voice lines and action-specific sound effects; and the game AI roster/selection/spawn/decision logic. Record exact source paths, branch/commit/version, dependencies, engine compatibility, and source/asset permission status.

Classify every category as PRESENT-AND-INSPECTED, MISSING, INCOMPATIBLE, NOT-APPLICABLE-WITH-REASON, or NOT-YET-INSPECTED. A release-note name or APK portrait is only a lead, not evidence that editable assets or AI support exist. Confirm whether a character is genuinely selectable and playable in the source, whether the AI can select/spawn it, and whether each skill shown in the UI maps to working code. Preserve provenance for voice, music, SFX, artwork, sprites, animation and effects separately. Do not mark a candidate as a complete character source until its applicable resources and implementation have been inspected.


## Tenth-pass legacy-source inspection — 2026-10-10

### Candidate: `LeaderOnePro/NarutoSenki-cocos2dx`

- Repository: https://github.com/LeaderOnePro/NarutoSenki-cocos2dx
- Inspected branch/head: `main` at `187fca6efd1ba6b89a91659fa7c591dde3995280` (recursive source tree inspected).
- This is an older Cocos2d-x 2.2.6 C++ implementation with a monolithic `Classes/Characters.cpp`, not the same modular C++/Lua structure as the pinned Android-clean candidate.
- **Useful source leads found:** the source contains an `AI_ImmortalSasuke()` implementation and a Han AI dispatch branch in `Classes/Characters.cpp`; resources include `Resources/Element/Han/Han.{xml,plist,pvr.ccz}`, `Resources/Element/ImmortalSasuke/ImmortalSasuke.{xml,plist,pvr.ccz}`, plus character-named audio folders. This is stronger evidence than a release-note name alone that some character logic/resources exist in an editable source tree.
- **Critical gap:** the inspected `SelectLayer.cpp` hardcodes a selection list that does not include Han or ImmortalSasuke, and the tree search did not find their expected `*_select.png`, `*_half.png`, or `*_font.png` selection assets. The presence of AI dispatch, resource atlases and audio does **not** prove a complete selectable character package.
- **Compatibility gap:** this fork's legacy C++ architecture and resource/config conventions differ from the current modular V2 candidate. Porting the old `Characters.cpp` blocks directly would be unsafe; each character would need behavior, skill, resource and AI mapping into the current native systems.
- **Rights gate:** no root `LICENSE`/copying/notice file was found in the inspected repository tree. Its code and game artwork/audio are **not approved for redistribution** on the basis of public visibility alone. Keep the source reference-only until permission/license status is resolved.
- **Classification:** `RESOURCE_REVIEW / BLOCKED`; no character from this source has been copied into the project or counted as added.
- **Next action:** locate a permission-cleared source for the same character(s), or obtain explicit permission; then build a per-character manifest and port one complete character at a time. Do not start with the old monolithic AI branch as if it were a drop-in module.

This inspection identifies a new *source lead*, not a new in-game character. Current roster counts remain unchanged.


## Follow-up research: complete-package audit and permission gate — 2026-10-10

- The current pinned candidate's `SkillLayer.lua` requests skill icon frames named `<Character>_skill1.png` through `_skill5.png` and skill-description frames `<Character>_label1.png` through `_label5.png`. This provides a more actionable inventory than merely checking for a file called `<Character>_skill.plist`.
- The CI audit script was expanded to check those exact expected frame names in loose resources and plist frame declarations, alongside native enum references, selection frames, Unit paths, audio path matches, and detectable AI registration patterns.
- The latest audit found the expected 5/5 skill icon and 5/5 label frames for Naruto, Sakura, Sai, Kakashi, Shikamaru, Ino, Choji, Asuma, Hinata and others in the candidate tree. These are **name-presence checks only**; they do not prove the images are correct, text is readable, skill names match behavior, or audio triggers at the right events.
- Candidate audit also flags exceptions (for example Kiba has only 3/5 name-matched Unit/resource paths), which are investigation targets, not proof of a broken character.
- Research source: [LeaderOnePro/NarutoSenki](https://github.com/LeaderOnePro/NarutoSenki) is an older Cocos2d-x 2.2.2 source project; it is not a drop-in extension for this project's modular V2 candidate. Public access and a source tree are not a redistribution license.
- No additional character has passed the permission + compatibility + complete-assets gate. New characters added remains **0**; don't label an audit-only finding as an integration.


## Eleventh-pass legacy mod source comparison — 2026-10-10

### Candidate: `Zx-Akito/NarutoSenki`

- Repository: https://github.com/Zx-Akito/NarutoSenki
- Inspected branch: `master` at commit `d847b113dfce486822768ef5a1c1c874b50fa3cd`; recursive tree contains 1,199 entries. The inspected source includes a monolithic `Classes/Characters.cpp` / `Classes/Characters.h` AI and character implementation, and resource paths under `Resources/Element/` rather than the current V2 candidate's `Resources/Unit/Ninja/` layout.
- Confirmed source/resource leads include alternate forms and characters such as `SageJiraiya`, `ImmortalSasuke`, `RikudoNaruto`, and `MaskRaidon`. Examples inspected: `Resources/Element/SageJiraiya/SageJiraiya.{xml,plist,pvr.ccz}`, `Resources/Element/ImmortalSasuke/ImmortalSasuke.{xml,plist,pvr.ccz}`, `Resources/Element/RikudoNaruto/RikudoNaruto.{xml,plist,pvr.ccz}`, plus character-specific audio folders and skill clips. `Characters.cpp` has explicit AI dispatch branches for several of these names.
- These are editable implementation/resource leads, stronger than release notes alone, but the source uses the older monolithic architecture and its resource/animation naming conventions differ from the pinned V2 candidate. Its files cannot be copied straight into V2 and expected to work. Each candidate needs a behavior/animation/skill/AI mapping and a full resource manifest before porting.
- No declared repository license was present in the GitHub repository metadata. For the user's private experimentation, continue technical analysis rather than stopping research; keep this source marked as a legacy porting reference and do not imply public redistribution rights.
- **Classification: SOURCE-INSPECTED / LEGACY-PORT CANDIDATE.** No character from this source has been integrated or counted as playable in the current build.

### Cross-check: current V2 forks

The inspected `Fansirsqi/NarutoSenki-V2`, `ZhReimu/NarutoSenki-V2`, `sansaks-jpg/NarutoSenki-V2`, and `Wilykun/NarutoSenki-V2` trees each expose the same 41 separate `Classes/Core/Shinobi/*.hpp` header count at their current default branches; the sample class-name tails are identical. They remain lineage/reference leads, not evidence of a new complete character package beyond the pinned candidate. Do not count duplicate forks as extra characters.

### Follow-up: kill-feed portrait audit

- The current battle HUD's `HudLayer::createReport()` requests `<Name>_rp.png` and `<Name>_rpf.png` frames, while the frames live in `Resources/Report.plist`. The audit script now checks both expected portrait frames per roster name and CI asserts that Kabuto and Kiba have both frames declared.
- This is an atlas-name integrity check only. It does not prove the correct killer/victim names are passed, portraits are rendered in the right order, or the notification works during battle; those still need runtime tests.


### NarutoSenki 1.17 mod — Fukasaku replacement (inspected 2026-10-10)

- Repository: https://github.com/LeaderOnePro/NarutoSenki1.17Mod
- Default branch: `main`; repository metadata showed last update 2026-07-27, size 37,613 KB, no declared license.
- README description (Chinese): a custom mod based on Naruto Senki 1.17; it replaces Akimichi Choji with the two Great Sage Toads (Fukasaku/Shima).
- Tree inspection found 1,043 paths, including packaged Android APK contents (`classes.dex`, `resources.arsc`, `lib/`, and `assets/`) rather than an editable C++/Lua source project. Assets include `assets/Audio/Fukasaku/`, `assets/Element/Fukasaku/`, and related character/effect atlases.
- Fork comparison: `wsnbbnbb/NarutoSenki1.17Mod` reports this repository as its parent and has the same reported size/tree layout; it is a fork/mirror, not an independent implementation.
- **Classification: REFERENCE_ONLY / APK-PACKAGED MOD.** It is useful evidence that a Fukasaku/Shima character replacement exists in a 1.17 mod and helps identify the resource families needed for a complete character package. It is not a drop-in V2 source port: no editable character source was found in the tree inspection, the base version differs, and code/assets have no declared reuse terms.
- **Integration status: not imported.** No APK extraction, binary patching, or asset copying was done. Next step is to find a source-editable version of this character or implement it from a permission-cleared source; then map selection art, skill icons/descriptions, sprites/animations, audio, effects, skill logic, and AI to the chosen V2 architecture and test it.


### Legacy source roster leads — Han and Roshi (inspected 2026-10-10)

- Repository: https://github.com/Zx-Akito/NarutoSenki
- Inspected revision: d847b113dfce486822768ef5a1c1c874b50fa3cd (legacy Cocos2d-x 2.2.2-era source; see the existing base audit).
- Confirmed editable character animation/config resources: Resources/Element/Han/Han.xml, Resources/Element/Han/Han.plist, Resources/Element/Roshi/Roshi.xml, and Resources/Element/Roshi/Roshi.plist, plus corresponding audio folders, report portraits, and cut-in frames.
- The XMLs include named states (idle, walk, hurt, float, dead, normal attack, and skills), frame sequences, attack values/ranges, and events for sound, attack boxes, invincibility, buffs, and other commands. Legacy Classes/Element.cpp contains explicit Han/Roshi behavior branches, so the resource XML alone is not a complete portable character implementation.
- The currently pinned V2 candidate does not include Classes/Core/Shinobi/Han.hpp, Roshi.hpp, Resources/Unit/Ninja/Han/, or Roshi/; neither name appears in its selectable roster. These are potential roster-expansion targets, not already implemented characters.
- Classification: LEGACY SOURCE REFERENCE. Useful for mapping desired behavior and identifying all resource categories; not a drop-in port because the engine/character architecture differs from the pinned V2 candidate. No files/assets were copied.
- Next port gate: inspect the corresponding legacy character branches and current V2 Shinobi interfaces; build a complete mapping for selection assets, five skills, XML/animation frames, effects, audio triggers, combat values, and AI before implementing either character. Keep provenance/permission status attached to each component.
