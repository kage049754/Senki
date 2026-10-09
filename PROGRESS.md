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
- Important: the release host contains packaged release assets and is not, by itself, editable source. Source import and license/asset terms remain unverified.
- Do not continue building the standalone Kotlin/Canvas prototype as a separate game while the selected base is being verified.

## Current verified status
- [x] README identifies Naruto Senki V2 as the chosen target and links to the release.
- [x] Created docs/BASE_GAME.md documenting the target, source requirements, and status.
- [x] Updated AGENTS.md and ROADMAP.md to record the chosen target.
- [ ] Verify the editable V2 source project and exact revision corresponding to/compatible with v2.1.6-fix.
- [ ] Verify code license and asset-specific reuse permissions.
- [ ] Import/adapt the existing V2 source into this repo with provenance preserved.
- [ ] Build the imported base before integrating mods.
- [ ] Integrate requested mods/characters in verified batches.
- [ ] Verify a unified modded APK artifact and device behavior separately.

## Current project contents and cautions
The repo previously received a native Kotlin/Canvas prototype scaffold. That scaffold is not the intended final foundation. No claim is made that the V2 source has been imported or that the release APK has been copied into this repository. Keep the original release page linked as a reference; do not commit large packaged binaries as a substitute for editable source.

## Next actions
1. Inspect the source repository linked by the V2 documentation and verify actual source/build files.
2. Check the source's current license and any separate asset terms.
3. Determine whether the source revision can be built in the current Android toolchain and how it relates to the v2.1.6-fix release.
4. Import the existing game source into this central repo only after the source and permission decision is documented.
5. Build/verify the base, then start merging mods.

## CI and APK status
- Latest workflow: must be checked live before reporting.
- Latest workflow conclusion: not verified in this documentation update.
- Unified mod APK artifact: not verified.
- Physical-device installation/gameplay: not verified.

## Session log
- Updated README, AGENTS.md, ROADMAP.md, and this tracker to make the user's selected Naruto Senki V2 target explicit.
- Added docs/BASE_GAME.md with release reference and a clear distinction between packaged APK and editable source.
- The public release API identifies v2.1.6-fix as a release with an Android APK asset. The APK itself was not copied into this repository, and no mod integration has been claimed.

## Reminder
**Every session: work on Naruto Senki V2 in kage049754/Senki. If adding a character/mod, integrate it into the existing V2 game here. No separate new game.**
