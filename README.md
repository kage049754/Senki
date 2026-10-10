# SENKI — Naruto Senki V2 Mod Integration Workspace

> **MAIN MISSION:** Find genuinely new playable characters implemented by other Naruto Senki mods and integrate them into this existing Naruto Senki V2 game. Do not build a separate game. Do not count existing V2 forms, summons, clones, or support units as new characters.

## Read these first

Every AI/developer session must read README.md, AGENTS.md, ROADMAP.md, PROGRESS.md, docs/MOD_RESEARCH.md, docs/ASSET_LICENSES.md, and docs/CHARACTER_ROSTER.md before changing code, assets, or roster records. If documents conflict, follow AGENTS.md and correct the conflicting documents.

## Immediate priority: port an external character

**Do not spend the next character-expansion task on more pagination, roster recounting, internal forms, summons, or documentation-only changes.** The next substantive milestone is to identify and qualify one distinct playable character from another Naruto Senki mod, map its actual implementation/resources and permission status, and complete the first port into an available slot on pages 1–3.

1. Inspect the actual source files for an external character—not just a release note, screenshot, or APK.
2. Compare its character ID/name, class or script, animation/atlas, skills/effects, audio/voice, AI/player controls, selection portrait, skill/profile view, and kill/death UI against the pinned V2 candidate.
3. Check the code license and the separate rights/provenance for game art, voices, and audio. If rights are unclear, seek an authorized source/package or creator permission; do not extract or redistribute APK contents.
4. Pick one distinct candidate only after the source, resource dependencies, compatibility, and permission path are documented. Then implement it in the native game systems and record exact changed files.
5. Run CI, inspect actual logs if it fails, fix and rerun until success, and verify the APK artifact. Report phone installation/gameplay separately.
6. Continue to the next character after the first port. Never count a character based on a name, portrait, static audit, or build success alone.

Known release-note leads include Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Might Guy, Yamato, Zetsu, Iruka, Jirobo, Tayuya, and Anko. These remain leads, not integrated characters, until editable source/resources and permissions are verified. The legacy `Zx-Akito/NarutoSenki` source has editable C++ but its inspected selectable roster overlaps the existing V2 roster; `likill/NarutoSenki-master` likewise did not qualify a new character. Continue the search rather than claiming these as ports.

## The actual goal

- Keep one existing Naruto Senki game and its native Cocos2d-x/C++/Lua systems as the foundation.
- Bring compatible, distinct playable characters from other Senki mods into that game.
- Target **70+ distinct playable characters** if compatible source and resources can support it.
- Work on available slots on character-select pages **1, 2, and 3 first**. Never silently replace an existing character.
- Preserve the original character-selection, training/network/exit, and mode-menu backgrounds unless the user explicitly requests a change.
- Preserve original image-based page buttons 1–3 and their touch behavior. Pages 4 and 5 must use matching image-style normal/selected buttons, not text-only controls.
- Integrate each character completely: selection identity, sprite/model and animation data, movement, attacks, skills/effects, available audio/voice, player controls, AI, skill/profile display, and kill/death UI.
- Produce one unified Android APK. Report CI and physical-phone testing separately.

## No-new-game rule

The central repository is [kage049754/Senki](https://github.com/kage049754/Senki). The selected game reference is [Naruto Senki V2 v2.1.6-fix](https://github.com/Naruto-Senki/files/releases/tag/v2.1.6-fix). A release APK is a packaged binary, not editable source. The source tree used by CI is currently fetched from a pinned external V2-derived repository into a temporary workspace; it is not fully vendored here.

Do not expand the old Kotlin/Canvas prototype as the final game. Keep the existing game engine and battle loop; adapt existing mod content to its native systems.

## Character completion gate

A character counts as integrated only after its code/resources are connected to the game's actual selection and battle lifecycle. It counts as verified playable only after selection, spawn, movement, basic attack, each skill, effects/audio, AI, death/respawn, profile/skill view, kill/death display, and resource stability have been checked. A passing static audit or Android build is not gameplay proof.

Track each candidate's source, revision, permission status, ID, page/slot, portrait/atlas frame, animation, skills/effects/audio, AI/control path, missing dependencies, test evidence, and status in docs/CHARACTER_ROSTER.md.

## Phases

1. **Phase 0 — Instructions and truthful baseline:** align docs and inspect latest CI.
2. **Phase 1 — V2 base:** maintain one existing V2-derived base and document source/provenance.
3. **Phase 2 — External character discovery:** find distinct playable implementations from other Senki mods.
4. **Phase 3 — First complete port:** adapt one character to an available page 1–3 slot and test it end-to-end.
5. **Phase 4 — Batch integration:** add more verified characters toward 70+.
6. **Phase 5 — Final regression and release:** verify build/artifact, then separately install and test on the phone.

See [ROADMAP.md](ROADMAP.md) for task lists and exit gates.

## Current honest status (2026-10-10)

- Latest verified central Actions run: [#295 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38055125607), commit [3a9fa15](https://github.com/kage049754/Senki/commit/3a9fa15ab6f6768385581743d3047a6eccafaaab).
- Run #295 is a successful technical candidate build; it does **not** mean the six requested characters were ported.
- External mod character packages integrated into the candidate: **1 variant — Two Sage Toads** (Choji-based; not a distinct base character). External mod variant integrated into the candidate: **1 — Two Sage Toads** (uses native Choji combat/AI; not a distinct base character). Distinct external characters gameplay-verified: **0**.
- Source-level roster baseline: **37 distinct base characters / 44 selectable entries**. Goal: 70+ distinct playable characters.
- Release APK resource-name audit found visible model/XML, atlas and audio *names* for Kurenai, Might Guy and Yamato; Hashirama had model/XML, atlas and audio names but skill-art was not confirmed. Shizune and Rin had atlas/audio names; model/XML and skill-art were not confirmed. These are packed NSKP index references, **not importable assets or proof of playable implementation**.
- The six priority characters remain **not integrated**: Kurenai, Might Guy, Yamato, Hashirama Senju, Shizune, and Rin Nohara. Other release-note leads to investigate include Sasori, Zetsu, Iruka, Sakon & Ukon, Juzo, Jonin Minato, Jirobo, Tayuya, and Anko.
- The source-package importer correctly refuses partial writes when complete editable packages are unavailable. The public v1.25/v1.26 release APKs use packed NSKP resources; do not claim a port based on path names alone.
- Next: search for inspectable editable character source packages across additional Senki mods and forks; for every viable character, integrate the complete behavior and all available dependencies, then run CI and verify artifacts. If source is unavailable, implement a genuinely original compatible character with independently created assets rather than pretending the packed release assets were imported.
- Physical-phone install/startup/gameplay remain **unverified**. CI success is not device testing.

## Reference docs

- [AI agent rules](AGENTS.md)
- [Roadmap and phases](ROADMAP.md)
- [Persistent progress and CI evidence](PROGRESS.md)
- [Mod/source research inventory](docs/MOD_RESEARCH.md)
- [Character tracker](docs/CHARACTER_ROSTER.md)
- [Asset/license register](docs/ASSET_LICENSES.md)
- [Base-game/source audit](docs/BASE_GAME.md) and [V2 build audit](docs/V2_BUILD_AUDIT.md)

## Rights and disclaimer

This is an independent fan-made research/modding workspace. Non-commercial intent does not itself grant rights to third-party code, art, audio, or franchise assets. The root LICENSE applies only to eligible original contributions and does not override external licenses or rights held by Naruto/Naruto Senki owners.
