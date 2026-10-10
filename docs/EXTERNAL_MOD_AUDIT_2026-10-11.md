# External Naruto Senki Mod Audit — 2026-10-11

## Selected lead for character discovery

**Selected repository:** [Zx-Akito/NarutoSenki-Release](https://github.com/Zx-Akito/NarutoSenki-Release)

**Why this one:** its versioned release notes identify concrete character additions and gameplay changes, making it the best roster-discovery index among the inspected repositories. It is **not** the editable source tree for a port: the repository is a release/changelog reference, and the published APK assets are packaged binaries. Do not claim a character has been ported from this repository.

**Primary source evidence:** [release history](https://github.com/Zx-Akito/NarutoSenki-Release/releases). The release notes describe the following additions:
- v1.26 Beta 1: Shizune, Hashirama, Rin, Sakon & Ukon, and Juzo.
- v1.25 Beta 3: Kurenai, Might Guy, Yamato, Sasori, Zetsu, and Iruka.
- v1.24 Beta 1: Jirobo, Tayuya, and Anko.
- v1.25 Beta 3 also mentions an Anko skin with unique gameplay; that is a form/skin candidate, not automatically a distinct base character.

## Character transfer eligibility

**Complete external characters verified ready to transfer from this repository: 0.** The release notes are evidence that these characters were announced in a released game version, but do not expose their character classes/scripts, animation atlases, full skill dependencies, player-control/AI paths, portraits/profile UI wiring, or source revision for a compatible editable implementation.

| Character lead | Evidence in release notes | Transfer status | Required next proof |
|---|---|---|---|
| Shizune | v1.26 Beta 1 addition | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Hashirama Senju | v1.26 Beta 1 addition | DISCOVERED — not source-verified | Same; verify independent selection and complete skills |
| Rin Nohara | v1.26 Beta 1 addition | DISCOVERED — not source-verified | Same; verify independent selection and complete skills |
| Sakon & Ukon | v1.26 Beta 1 addition | DISCOVERED — not source-verified | Determine whether one selectable fighter or two; inspect controller/resources |
| Juzo | v1.26 Beta 1 addition | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Kurenai | v1.25 Beta 3 addition | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Might Guy | v1.25 Beta 3 addition | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Yamato | v1.25 Beta 3 addition; aimed/dragged Skill 2 noted | DISCOVERED — not source-verified | Find editable implementation; map aimed-skill input and effects |
| Sasori | v1.25 Beta 3 addition and later skill fix | DUPLICATE/COMPATIBILITY CHECK REQUIRED | Compare with target roster and verify that no existing character is renamed/reused |
| Zetsu | v1.25 Beta 3 addition and skill revamp | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Iruka | v1.25 Beta 3 addition and skill revamp | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Jirobo | v1.24 Beta 1 addition; Skill 2 later adjusted | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Tayuya | v1.24 Beta 1 addition; later adjustments | DISCOVERED — not source-verified | Find editable implementation and all resource dependencies |
| Anko | v1.24 Beta 1 addition; separate unique-gameplay skin mentioned in v1.25 Beta 3 | DISCOVERED — not source-verified | Find editable implementation; separate base character from skin/variant |

## Source comparison and decision

- [Zx-Akito/NarutoSenki-V2](https://github.com/Zx-Akito/NarutoSenki-V2) has inspectable C++/Lua/Cocos2d-x source, but it is the V2 base/fork family, not proof of these release-only characters' editable implementations.
- [LeaderOnePro/NarutoSenki-cocos2dx](https://github.com/LeaderOnePro/NarutoSenki-cocos2dx) is an editable Cocos2d-x source candidate with Android build instructions, but the inspected README does not establish that it contains any of the distinct release-note characters above. Do not assume it does without checking its actual selection and character implementation files.
- [LeaderOnePro/NarutoSenki1.17Mod](https://github.com/LeaderOnePro/NarutoSenki1.17Mod) is package/decompiled-distribution oriented rather than a clean editable source project; it is not accepted as a complete character source merely because assets or package files are present.
- V2 forks/mirrors are not independent character sources unless a meaningful character implementation difference is identified.

## First-port gate

Do not start another character by renaming an existing fighter or mapping a new display name to unrelated behavior. Before code integration, identify an editable character implementation and map:
1. stable character ID and selection entry;
2. sprite/model, atlas frames, animation and transitions;
3. movement, basic attack, each skill, effects/projectiles and resource/cooldown behavior;
4. portrait, skill icons/descriptions and selected-character profile;
5. player controls, AI, spawn/death/respawn, kill/death identity;
6. available audio/voice/SFX and exact resource paths;
7. source repository/revision and asset provenance.

The first transfer should use an unused page 1–3 slot, preserve all existing entries, and only be marked playable after runtime checks. CI success alone is not gameplay proof.

## Next action

Continue source-level research specifically for an editable implementation of one of the 13 release-note leads. Prioritize candidates whose complete class/script, animation/resource set, and selection path can all be inspected. If no compatible implementation is found, report that fact and implement an original compatible character only when it can be clearly distinguished from the existing roster—never fake a port.
