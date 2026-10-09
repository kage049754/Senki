# SENKI — Naruto Senki-Inspired Android Battle Game

> **Project status:** Planning and repository bootstrap. This repository was empty when this roadmap was added; no playable build or APK is claimed yet.

Senki is a landscape-first Android 2D lane-battle game project inspired by the feel of Naruto Senki: selectable fighters, basic attacks, skills, HP, leveling, minions, towers, and fast matches. The long-term goal is one cohesive game with a broad roster and polished launch flow—not a pile of unrelated APKs or incompatible mods.

## AI / Contributor: read these rules first

**Before editing this repository, every AI coding agent or contributor must:**
1. Read this README from top to bottom.
2. Read [AGENTS.md](AGENTS.md) for mandatory workflow and coding rules.
3. Read [ROADMAP.md](ROADMAP.md) for current priorities and acceptance criteria.
4. Read [docs/MOD_RESEARCH.md](docs/MOD_RESEARCH.md) before adding outside Naruto Senki code, assets, character concepts, or dependencies.
5. Read [docs/CHARACTER_ROSTER.md](docs/CHARACTER_ROSTER.md) and [docs/ROSTER_SCALABILITY.md](docs/ROSTER_SCALABILITY.md) before roster/character work.
6. Inspect the current files and latest GitHub Actions run before making changes. Never assume the project structure, build status, or stage.
7. Update the roadmap/research/progress records when work changes the plan or a source is verified.

These instructions are repository guidance, not a technical mechanism that can force every AI to obey. They are placed in prominent, conventional files so repository-aware agents can discover them. An agent that ignores repository instructions cannot be guaranteed to read them automatically.

## Core gameplay target

- **Orientation:** landscape, responsive to Android phone aspect ratios and safe areas.
- **Battle camera:** 2D side-view lane battlefield.
- **Player loop:** main menu → mode select → character select → battle → result/retry.
- **Combat:** movement, basic attack, skill buttons, cooldowns, HP, damage, hit reactions, death/respawn.
- **Progression:** experience/leveling and skill unlock or upgrade rules where appropriate.
- **Lane combat:** allied/enemy minions, towers/base objectives, waves, and match win/loss conditions.
- **Roster:** data-driven catalog designed for **70+ playable characters with no artificial hardcoded maximum**. Each entry may have distinct stats, attack timing, skill kits, effects, portraits, and animation states. This is a design target; it is not a claim that 70 characters are already implemented.
- **Scalable selection:** search/filter/category and scrolling or pagination; do not create one fixed button per character.
- **Performance:** lazy-load character resources and release them safely so the whole roster does not need to remain in memory at once.
- **Offline-first:** the core single-player battle must not require an account or internet connection.
- **Quality:** no blank screen after engine splash, no invisible menu, no dead buttons, no crash on launch, and no invalid APK package.

## Combining characters and mod ideas

We will research public GitHub repositories, forks, source projects, changelogs, and mod descriptions. We will maintain a source-by-source inventory rather than claiming every mod has been found. Many Naruto Senki mods are distributed only as APKs, are private, or do not publish source code.

**Do not blindly merge whole APKs or copy every mod's assets.** Different projects can use different engines, code structures, animation formats, physics, naming, and balancing. Instead:
1. Identify each candidate's actual source, engine, roster, and license/terms.
2. Record characters, forms, skills, animations, effects, and useful mechanics with source links.
3. Prefer compatible source code and documented, reusable mechanics.
4. Port each approved character into Senki's own character-data and skill interfaces.
5. Rebuild/retarget animations and effects as needed; standardize input, cooldowns, hitboxes, damage, and AI.
6. Track provenance for every external asset/code contribution.
7. Exclude assets or code whose license/permission does not allow the intended use. Publicly viewable does not mean public domain or freely redistributable.
8. If permissions are unclear, implement an original equivalent or leave the material out. Do not redistribute extracted APK contents or copyrighted assets without authorization.

The current research list is a starting point, not a claim that these projects are all compatible or that they provide permission to reuse their content. See [docs/MOD_RESEARCH.md](docs/MOD_RESEARCH.md).

## Development roadmap

The ordered phases and their acceptance checks are in [ROADMAP.md](ROADMAP.md). Work proceeds in small, verifiable milestones:
1. Repository audit and Android build foundation.
2. Reliable landscape launch, menu, mode select, and character select.
3. One complete playable battle loop.
4. Minions, towers, leveling, win/loss, and restart.
5. Data-driven character framework and a starter roster.
6. Roster expansion to 70+ playable entries, with no fixed cap, after the battle architecture is stable.
7. Additional modes, UI/audio/performance polish, and device testing.
8. Release build, APK artifact verification, and documented known issues.

A phase is not complete because code was written. It is complete only after its acceptance checks pass.

## Required build / QA loop

For every code milestone:
1. Inspect current source and build configuration.
2. Run or inspect the latest GitHub Actions workflow.
3. If queued/running, wait for the actual result before declaring status.
4. If failed, read the real failing step/log, fix the cause, commit, and rerun.
5. Confirm the final run is **completed and successful**.
6. Confirm the APK artifact exists and can be downloaded; record the artifact name and run link.
7. Test installation and launch on a real Android device when possible. CI success alone does not prove the game launches correctly on a phone.
8. If a fix fails, repeat the failure-inspection loop. Never report a pending, stale, or failed run as success.

If a tool/session cannot continue polling after a response, state that limitation honestly and provide the exact last verified state; do not pretend work continued in the background.

## Current status

- [x] Confirmed repository exists and is public.
- [x] Added initial roadmap and AI/contributor instructions.
- [ ] Inspect and establish actual Android project structure.
- [ ] Establish reproducible CI build and APK artifact.
- [ ] Fix launch-to-menu flow and landscape behavior.
- [ ] Implement the first complete battle loop.
- [ ] Implement a data-driven roster registry with no fixed character cap.
- [ ] Expand roster in verified batches toward 70+ playable entries.

## Useful project documents

- [Mandatory AI/contributor rules](AGENTS.md)
- [Milestone roadmap and acceptance criteria](ROADMAP.md)
- [Naruto Senki/mod source research inventory](docs/MOD_RESEARCH.md)
- [Character implementation tracker](docs/CHARACTER_ROSTER.md)
- [Large-roster architecture rules](docs/ROSTER_SCALABILITY.md)

## Disclaimer

This is an independent fan-inspired project. Naruto, its characters, names, logos, music, and related assets belong to their respective rights holders. This repository does not claim ownership or official affiliation. Do not add or redistribute third-party copyrighted material without the necessary rights. If the project is later intended for public/commercial release, plan an original-character/content conversion before release.
