# Code, Asset, and Permission Register

## Rule
A public repository or downloadable APK is not automatically permission to reuse or redistribute its contents. Evaluate source-code licensing and artwork/audio/animation licensing separately.

## Status definitions
- UNREVIEWED
- REVIEWED
- APPROVED
- PERMISSION_REQUIRED
- REFERENCE_ONLY
- EXCLUDED

## Naruto Senki V2 source candidate — Zx-Akito/NarutoSenki-V2
- Canonical URL: https://github.com/Zx-Akito/NarutoSenki-V2
- Material: C++/Lua game source, Cocos2d-x engine/dependencies, Android project, game resources and bundled assets
- Verified source structure: includes projects/NarutoSenki/proj.android-studio and source/resource directories described in the repository documentation.
- Repository metadata: public fork; parent listed as real-re/NarutoSenki-V2-old, which is private in the returned metadata.
- Code license: no root LICENSE found; GitHub metadata reports no declared license.
- Asset-specific license: not verified.
- Attribution requirements: unknown for game code/assets; third-party engine components may have separate notices.
- Modification/redistribution permission: not established.
- Permission evidence: none identified during the 2026-10-10 audit.
- Approved scope: reference/audit only; do not copy source/assets into this central repo or package them in a build until permission is established.
- Status: **PERMISSION_REQUIRED**
- Review date: 2026-10-10
- Notes: the source appears technically suitable for deeper build investigation, but public availability is not a license. The selected v2.1.6-fix APK is a separate binary release reference and is not source.

## Source review template
- Source/repository or creator:
- Canonical URL:
- Material type: source code / sprites / animation / sound / music / fonts / documentation / other
- Exact files or commit:
- Code license:
- Asset-specific license:
- Attribution required:
- Modification permitted:
- Redistribution permitted:
- Commercial use permitted:
- Permission evidence:
- Approved scope:
- Status:
- Reviewer/date:
- Notes:

## Rules
- Never strip copyright or attribution notices.
- Do not redistribute extracted APK contents without authorization.
- Do not assume an open-source code license covers art, music, or other third-party assets.
- If permission is unclear, mark the source REFERENCE_ONLY or PERMISSION_REQUIRED and do not package it in the APK.
- Use original or appropriately licensed replacements where necessary.
- Keep provenance linked to every imported character, skill, animation, portrait, and sound.
- Recheck licenses of forks and bundled third-party dependencies.
- A character must not be marked VERIFIED for release if required asset permissions remain unresolved.

## Initial status
No external source is approved for copying solely by virtue of appearing in the research inventory. Review each candidate and each asset set before integration.


## Additional audited repositories — 2026-10-10

### `LeaderOnePro/NarutoSenki` (older editable source)
- Code: public repository, no declared GitHub license found in metadata.
- Assets: `Resources/` contains Naruto/game resource bundles; individual rights and dependency notices are not established.
- Technical classification: reference-only; Cocos2d-x 2.2.2 / Visual Studio 2010 setup, with no verified Android build path from the inspected root.
- Permission status: **PERMISSION_REQUIRED** for source and bundled assets. Do not import/package.

### `LeaderOnePro/NarutoSenki1.17Mod` and fork `wsnbbnbb/NarutoSenki1.17Mod`
- Both repositories report no declared license.
- The root tree of the original is package/decompiled-distribution oriented (`classes.dex`, `AndroidManifest.xml`, `assets/`, `lib/`, `res/`) rather than an editable source project.
- The second repository is a fork with matching inspected commit history; it is not an independent mod.
- Permission status: **PERMISSION_REQUIRED**; APK/package contents are not approved for extraction, redistribution, or reuse.


### `Wilykun/NarutoSenki-V2` — V2-derived fork with working CI
- Source lineage: fork of `hitlabmodv2/NarutoSenki-V2`; 15 commits ahead at the inspected comparison.
- Code and inherited assets: no declared GitHub license; separate permissions not established.
- Observed fork CI success and artifact do not grant permission to copy, redistribute, or repackage its code/assets.
- Status: **PERMISSION_REQUIRED**. Technical review may continue; import/release remains blocked pending terms.


### `muhammadadilsyaputra08-alt/NarutoSenki-Custom` — Android-only V2-derived source
- Material: Android engine/source/resource snapshot, C++/Lua gameplay and Android Gradle project.
- Technical evidence: its own GitHub Actions run `34331260360` built and uploaded `narutosenki-debug-apk`.
- Rights/provenance: no declared GitHub license; README says extracted from original V2, but inherited code and Naruto assets are not thereby cleared.
- Status: **PERMISSION_REQUIRED**. Do not import or redistribute until source and asset permissions are established.


### `likill/NarutoSenki-master` — local PvP/co-op reference
- Source: legacy Cocos2d-x 2.2.2 / Visual Studio 2010, Windows-oriented package; no declared GitHub license.
- Potential content: local PvP/co-op plan and UI/control customization changes.
- Status: **PERMISSION_REQUIRED / REFERENCE_ONLY**; no code/assets approved for reuse and no Android build path verified.

## Per-character asset-rights review — voices and full character packages

For each character/form, record provenance and permission status separately for: selection portraits/avatars/button art; skill icons and UI artwork; sprites/models and animation sheets; skill/effect/projectile/summon assets; voice clips/voice lines; attack/skill/hit/death/transform/summon sound effects; music; and code/configuration. A permission status for source code must not be assumed to cover third-party character art, voices, sound effects, or music.

The character manifest in `docs/CHARACTER_ROSTER.md` must link each asset category to its exact source path and source revision where known. Mark absent categories as missing/not-applicable with evidence, and mark unknown rights as `PERMISSION_REQUIRED` or `UNREVIEWED`; do not silently treat public visibility, an APK extraction, or attribution as redistribution permission. Technical private testing and source discovery may continue while permission is being investigated, but public release claims must not overstate the rights status.



### `LeaderOnePro/NarutoSenki-cocos2dx` — modernized legacy C++ source reference
- Canonical URL: https://github.com/LeaderOnePro/NarutoSenki-cocos2dx
- Material: Cocos2d-x 2.2.6 framework, older Naruto Senki C++ game code, Android/Windows/macOS projects, bundled game assets.
- Repository metadata: no declared game-source license found in the inspected metadata. The `licenses/` directory contains dependency/framework license texts; these are not evidence of permission for the Naruto Senki game code or Naruto franchise assets.
- Asset-specific terms: not established.
- Approved scope: technical research and compatibility inspection only; no game code/assets copied to the central repository.
- Status: **REFERENCE_ONLY / PERMISSION_REQUIRED**
- Review date: 2026-10-10
- Notes: the Android project documents an armeabi-v7a-only legacy build path. It is a reference source, not a directly compatible V2 character package.


### `dogoo110/Naruto-godot` — Godot conversion reference
- Canonical URL: https://github.com/dogoo110/Naruto-godot
- Repository metadata declares MIT for the repository code. The repository also contains Naruto/Naruto Senki sprites, character portraits, audio, and other franchise materials.
- Code license: MIT metadata reported.
- Asset-specific license: not established; do not assume the code license clears franchise art/audio.
- Approved scope: inspect source structure and identify compatibility leads only; no files copied or packaged from this repository.
- Status: **REFERENCE_ONLY / ASSET_PERMISSION_REQUIRED**
- Review date: 2026-10-10
- Notes: the `HokageMinato` files found are a partial visual/audio lead, not proof of a complete playable character.


## Additional candidate asset-provenance findings — 2026-10-10

- `Fansirsqi/NarutoSenki` includes a root Mulan PSL v2 license, but its inspected tree is an Android package/resource distribution rather than an editable V2 source tree. Its README identifies some content as extracted package assets and references original asset creators. Do not assume the repository license clears bundled Naruto Senki sprites, animation frames, audio, or other third-party content; provenance must be checked asset by asset.
- `likill/NarutoSenki-master`, `RieyuXhen/NarutoSenki`, and `Zx-Akito/NarutoSenki` are legacy Cocos2d-x 2.2.2 source references with no root license found in the inspected trees. Their character/AI code and resource files are not approved for copying into the V2 candidate. Treat as reference-only until both code rights and asset rights are documented.
- No new third-party character assets were copied into this repository by this research pass.


## Legacy source candidate — LeaderOnePro/NarutoSenki-cocos2dx
- Canonical URL: https://github.com/LeaderOnePro/NarutoSenki-cocos2dx
- Material: legacy C++ Naruto Senki game source, Cocos2d-x 2.2.6 framework, Android/Windows/macOS project files, and game resources.
- Observed repository state: root `licenses/` directory exists for framework/dependency notices, but no root `LICENSE` file or repository-level license declaration was found in the inspected root.
- Game-code license: not established.
- Naruto character art, sprite, animation, audio, and other game-asset permissions: not established by framework license files.
- Compatibility: not a drop-in for the selected V2 Lua roster/Android Studio source; use for read-only technical comparison unless a reviewed integration path is approved.
- Approved scope: source structure, history, and compatibility research only; no code/assets copied into this central repo.
- Status: **PERMISSION_REQUIRED / REFERENCE_ONLY**
- Review date: 2026-10-10


### `likill/NarutoSenki-master` — legacy Cocos2d-x reference audit
- Canonical URL: https://github.com/likill/NarutoSenki-master
- Inspected files: `Classes/NetworkLayer.cpp`, `Classes/SelectLayer.cpp`, `Classes/Characters.h`, and `Classes/LoadLayer.cpp`.
- Source metadata: no declared repository license and no root LICENSE file found in the checked tree.
- Technical observation: Network/Hardcore mode lists 35 non-empty selectable names, while Training mode still lists nine. The inspected 35 names overlap the pinned V2 base roster; this is not a new-character package for the current project.
- Assets/audio/animations: bundled in the source tree, but separate asset rights are not established.
- Status: **REFERENCE_ONLY / PERMISSION_REQUIRED**. Do not copy or package code or assets without explicit permission.
