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
