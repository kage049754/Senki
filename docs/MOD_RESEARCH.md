# Naruto Senki / Mod Research Inventory

> **Project rule: this is research for modding and merging the user's selected Naruto Senki: V2 game, not creating a new game.** The release reference is https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix. The goal is to obtain and verify its editable source base, then integrate compatible mod content into kage049754/Senki. See docs/BASE_GAME.md.

**Last reviewed:** 2026-10-10  
**Status:** Candidate inventory; no base is selected until the repository contents, buildability, and reuse terms have been verified.

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
- Prior notes indicate a Cocos2d-x/C++ project with Lua/UI scripts, resources, character directories, bullets, summons, towers, and Android project files. Re-open and verify those paths against the current repository before relying on the notes.
- **Status:** strongest initial candidate to audit, not yet approved as the base. Verify current tree, branch, buildability, fork differences, code license, and separate asset permissions.

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
Select **one existing, editable Naruto Senki project** as the foundation after a comparative audit. Preserve its engine and original gameplay wherever practical. Keep `kage049754/Senki` as the central integration workspace. Do not extend the Kotlin/Canvas prototype into a new game while the base is unresolved. After selection, document why the base won, what will be migrated, and how attribution/permissions are handled.

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
