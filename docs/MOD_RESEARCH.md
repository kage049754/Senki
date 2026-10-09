# Naruto Senki / Mod Research Inventory

**Last reviewed:** 2026-10-10  
**Purpose:** identify source projects and mod ideas worth evaluating for Senki. This is an evolving public-GitHub research list, not a claim that every mod has been found or that all listed content is reusable.

## How candidates are classified

- **Source candidate:** code and resources appear to be present; inspect the full tree, build files, license, and content before use.
- **Release/changelog reference:** useful for roster and mechanic research, but not necessarily a source-code repository.
- **Fork:** must compare against upstream; do not count it as an independent mod unless it has meaningful original changes.
- **Support repository:** translations, files, docs, or website; not a separate playable game implementation.
- **Unverified:** name/search result suggests a mod, but owner, source contents, license, or compatibility still need confirmation.
- **Unrelated engine/game mod:** Naruto content exists, but it is not Naruto Senki and should not be treated as drop-in code.

## Candidate repositories

### 1. Naruto Senki V2 source family
- **Upstream source candidate:** https://github.com/Zx-Akito/NarutoSenki-V2
- **Known fork:** https://github.com/kuiyr0810/NarutoSenki-V2
- **Documentation:** https://github.com/Zx-Akito/NarutoSenki-V2/blob/master/Doc/README_ZH.md
- **What is known:** the V2 project documentation describes a Cocos2d-x codebase with C++ gameplay systems, Lua/UI scripts, resources, character directories, bullets, summons, towers, and Android project files. The documented tree includes `Classes/Core/Shinobi`, `Warrior`, `Bullet`, `Guardian`, `Kuchiyose`, `Tower`, `lua`, `Resources`, and `proj.android-studio`.
- **Research value:** high. This is the strongest candidate to study for the lane-battle architecture, character/skill systems, minions/towers, and Android build setup.
- **Caution:** the kuiyr0810 repository identifies itself as a fork of Zx-Akito's repository. Count it as a fork, not an independent mod, until a diff shows meaningful original work. V2 code/asset terms still need explicit review before reuse.

### 2. Naruto Senki release and changelog history
- **Release repository:** https://github.com/Zx-Akito/NarutoSenki-Release
- **What is known:** public release notes include v1.24, v1.25, and v1.26 beta series. Notes mention characters such as Jirobo, Tayuya, Anko, Kurenai, Guy, Yamato, Sasori, Zetsu, Iruka, Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, and Jonin Minato; they also mention training modes, a Mugen mode, aiming/dragging skill direction, AI improvements, and bug fixes.
- **Research value:** high for feature/roster history, alternate forms, and testing edge cases.
- **Caution:** release notes are not the same as source code or reuse permission. Inspect individual release assets only as references unless rights allow otherwise.

### 3. Original/older Cocos2d-x source candidate
- **Repository:** https://github.com/LeaderOnePro/NarutoSenki
- **What is known:** repository lists `Classes`, `Resources`, and `proj.win32`, and its README says Cocos2d-x 2.2.2 / Visual Studio 2010. It describes the content as Naruto Senki source code.
- **Research value:** medium-high for older architecture and historical implementations.
- **Caution:** old engine/toolchain and project structure may not directly build in a modern Android pipeline. Verify license and actual files before reuse.

### 4. Naruto Senki V2 file host
- **Repository:** https://github.com/Naruto-Senki/files
- **What is known:** the Naruto-Senki GitHub organization describes it as a V2 file host.
- **Research value:** supporting reference for release files and related project resources.
- **Caution:** a file host is not automatically a source-code implementation. Review each file and its terms; do not treat binaries as editable source.

### 5. Naruto Senki localization
- **Repository:** https://github.com/Naruto-Senki/localization
- **What is known:** repository description says it contains translations for Naruto Senki V2.
- **Research value:** language strings and UI terminology reference.
- **Caution:** not a character/engine mod; translation licensing does not grant rights to the game or its assets.

### 6. Naruto Senki V2 website/documentation
- **Repository:** https://github.com/real-re/nsv2-website
- **What is known:** public repository described as the Naruto Senki V2 website/docs.
- **Research value:** documentation and feature history only.
- **Caution:** not the battle engine or a standalone mod.

### 7. NarutoSenki1.17Mod search result — unverified
- **Search reference:** https://github.com/search?q=NarutoSenki1.17Mod&type=repositories
- **What is known:** GitHub repository search returned a repository name `NarutoSenki1.17Mod` on branch `main`, but the available search result did not reliably provide the owner/full repository name or enough source-tree details.
- **Next step:** identify the exact owner/repository, inspect the tree, establish whether it contains source or only binaries, compare its history/fork parent, and inspect license/terms.
- **Status:** do not use or claim it as an independent source until verified.

## Additional searches / discovery pages

These are search starting points, not proof that every result is a compatible Senki mod:

- https://github.com/topics/naruto-senki
- https://github.com/topics/naruto-game
- https://github.com/search?q=NarutoSenki&type=repositories
- https://github.com/search?q=Naruto+Senki+mod&type=repositories
- https://github.com/search?q=%E7%81%AB%E5%BD%B1%E6%88%98%E8%AE%B0&type=repositories

Searches so far have also returned general Naruto game/mod projects for other engines (for example Minecraft or RimWorld). These may provide high-level ideas but are **not** drop-in Naruto Senki character implementations.

## Research findings and limits

- Public GitHub searches found only a small number of clearly identifiable Senki code/source families; several search results are forks, release mirrors, documentation, or support repositories.
- Many community mods appear to be shared through APKs or file-hosting pages rather than source repositories. APK-only projects cannot be merged as source code, and their extracted assets should not be redistributed without permission.
- Search results can omit owners or fail to reveal whether a repository is original. Every candidate needs direct inspection.
- Do not say “all mods have been found.” Public search cannot guarantee completeness; private, deleted, renamed, or APK-only mods may not be indexed.
- No repository listed here is approved for copying merely because it is public.

## Per-repository review checklist

For each new candidate, record:
1. Canonical repository URL and owner.
2. Original repository vs fork/mirror; upstream and meaningful changes.
3. Main branch, latest commit date, engine/language, build system.
4. Actual source directories and whether character/skill implementation is present.
5. Roster/forms and distinct skills documented in source or changelog.
6. License file and any separate asset/third-party terms.
7. Android build feasibility and dependency age.
8. Whether content is approved for reuse, reference-only, or excluded.
9. Exact files inspected and a short evidence note.
10. Whether any port has been integrated and tested in Senki.

## Integration policy

Do not combine entire repositories or APKs into one package. Use a single Senki architecture and port compatible mechanics/characters one at a time. Every imported component must pass provenance/permission review, fit the common character and skill interfaces, and pass selection/combat/death/respawn/AI tests. If reuse permission is absent or unclear, create an original implementation and original assets instead.
