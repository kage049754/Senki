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
- [ ] Establish permission/license terms for the game code and especially Naruto artwork, sprites, audio, animations, and other bundled assets.
- [ ] Verify the exact source revision's relationship to the selected v2.1.6-fix release.
- [ ] Import/adapt source into this central repo after rights and import strategy are resolved.
- [ ] Build the imported base before mod integration.
- [ ] Integrate requested mods/characters in verified batches.
- [ ] Verify a unified modded APK artifact and device behavior separately.

**Decision:** the V2 source candidate is technically credible and has the expected Android project, but it is not yet safe to copy wholesale into this repo because the repository has no declared license and asset permissions are not established. Keep it as a source/reference candidate until terms are clarified; do not infer permission from public visibility.

## Current project contents and cautions
The repo previously received a native Kotlin/Canvas prototype scaffold. It is not the intended final foundation. The latest observed Actions run 37961789724 completed successfully on commit 90f01e26e2ffb3cc9e618b065fa1c1899c699e1e, and it produced an artifact named senki-debug-apk (823,056 bytes). This is the scaffold's debug APK, not a verified Naruto Senki V2 build or unified modded APK. It must not be represented as the requested final game.

## Next actions
1. Resolve code and asset permission terms for the V2 source candidate or locate a source distribution with clear reuse terms.
2. Compare its source revision with the selected release where possible.
3. Import/adapt the existing V2 source into kage049754/Senki only when the source and permission decision is documented.
4. Build/verify the original base, then start merging mods.
5. Keep CI reporting explicit about whether a run builds the prototype scaffold or the real V2 source.

## CI and APK status
- Latest observed Actions run: https://github.com/kage049754/Senki/actions/runs/37961789724
- Status: completed, conclusion success (prototype scaffold only).
- Artifact: senki-debug-apk, 823,056 bytes; not the selected V2 release and not a modded V2 build.
- Unified mod APK artifact: not verified.
- Physical-device installation/gameplay: not verified.

## Session log
- Updated project documentation to make Naruto Senki V2 the explicit target.
- Audited Zx-Akito/NarutoSenki-V2: verified C++/Lua/Cocos2d-x layout and Android Gradle project; confirmed no declared repository license.
- Identified that copying source/assets into this central repo requires resolving permissions first.
- Rechecked latest known workflow run and artifact; success is only for the existing prototype scaffold.

## Reminder
**Every session: work toward Naruto Senki V2 in kage049754/Senki. If adding a character/mod, integrate it into the existing V2 game here. No separate new game. Never call a prototype build the final Senki build.**
