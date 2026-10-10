# External Naruto Senki Mod Audit 3 — 2026-10-11

## New candidate: Fansirsqi/NarutoSenki

Repository: https://github.com/Fansirsqi/NarutoSenki  
Inspected revision: `636315c1cd9e5859d3efbe97bd42bf519fd4a9d8`  
Classification: **asset-rich legacy package / reference-only pending provenance and compatibility review**.

This repository is more promising than the previous two leads because the indexed tree contains per-character animation XML, sprite atlas metadata, selection art, skill icons, skill-view labels, and audio manifests—not just a name or an audio file.

### Candidate 1 — Kimimaro

Evidence:
- Animation/attack configuration: [assets/Element/Kimimaro/Kimimaro.xml](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/Element/Kimimaro/Kimimaro.xml). It declares the Kimimaro identity, base attack stats/range/cooldown, idle/walk/hurt and other animation actions, frame names, hitbox events, and sound events.
- Character sprite atlas metadata: [assets/Element/Kimimaro/Kimimaro.plist](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/Element/Kimimaro/Kimimaro.plist).
- Selection portrait/thumbnail frame: [assets/Select.plist](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/Select.plist) includes `Kimimaro_half.png`.
- Skill icon/avatar frames: [assets/UI.plist](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/UI.plist) includes `Kimimaro_avator.png` and `Kimimaro_skill1.png`.
- Skill-view label frames: [assets/Record2.plist](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/Record2.plist) includes `Kimimaro_label1.png` and `Kimimaro_label2.png`.
- Ultimate/cut-in and result/profile frame names also exist in `Ougis2.plist`, `Record.plist`, `Report.plist`, and `Result.plist`; audio files are listed under `assets/Audio/Kimimaro/`.

Assessment: **strong source-level character package lead**, but not yet proven as a distinct selectable character in a running build from this repository. No character class/roster dispatch or runtime test was established in this pass. The central target's indexed source search did not find a Kimimaro entry; still verify against the exact pinned source tree before declaring it new.

### Candidate 2 — Jugo

Evidence:
- Animation/attack configuration: [assets/Element/Jugo/Jugo.xml](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/Element/Jugo/Jugo.xml) declares Jugo-specific attack values, range/cooldown, movement frames, and animation event commands.
- Sprite atlas metadata: [assets/Element/Jugo/Jugo.plist](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/Element/Jugo/Jugo.plist).
- Skill atlas metadata: [assets/Element/Skills/Jugo_Skill.plist](https://github.com/Fansirsqi/NarutoSenki/blob/636315c1cd9e5859d3efbe97bd42bf519fd4a9d8/assets/Element/Skills/Jugo_Skill.plist).
- Selection portrait/label/avatar/skill-icon frame names appear in `Select.plist`, `Record2.plist`, and `UI.plist`; related audio paths also appear in the package manifest.

Assessment: **strong source-level character package lead**, but selectable roster registration, exact skill logic and runtime playability remain unverified. It may be a character or alternate/overwritten implementation in this package; inspect its select roster and source lineage before treating it as new.

### Compatibility and permission gate

- The package uses the legacy Cocos2d-style `assets/Element/<Character>/<Character>.xml` and `.plist` layout. The current central V2 candidate uses a different resource/class organization. XML events, atlas frame references, audio paths, effect/projectile dependencies, skill dispatch and AI registration must be mapped into the V2 native systems rather than copied blindly.
- The repository does not currently provide verified permission for redistribution of character sprites, voices, effects, or other game assets. **Do not copy or redistribute these assets until rights/permission is resolved.**
- Asset names are evidence of a substantial package, not proof that every referenced binary file is present or that the fighter is selectable/playable.
- Target repo search did not return Kimimaro or Jugo matches, but this is not a substitute for a full pinned-tree scan.

## Result and next action

- New promising character leads: **2** — Kimimaro and Jugo.
- New characters integrated into the central game in this audit: **0**.
- Playable/selectable characters verified from this source in a running game: **0**.
- Next: inspect the repository's roster/select registration and commit lineage; enumerate all per-character packages; compare each candidate against the exact central source revision; resolve code and asset permission; then port one genuinely new character through the target's native selection, skill UI, animation, audio, AI and battle systems. Do not relabel an existing fighter or count an asset-only package as playable.

