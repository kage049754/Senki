# SENKI — Naruto Senki V2 Mod Integration Workspace

> **MAIN MISSION:** Find genuinely new playable characters implemented by other Naruto Senki mods and integrate them into this existing Naruto Senki V2 game. Do not build a separate game. Do not count existing V2 forms, summons, clones, or support units as new characters.

## Read these first

Every AI/developer session must read README.md, AGENTS.md, ROADMAP.md, PROGRESS.md, docs/MOD_RESEARCH.md, docs/ASSET_LICENSES.md, and docs/CHARACTER_ROSTER.md before changing code, assets, or roster records. If documents conflict, follow AGENTS.md and correct the conflicting documents.

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

## External character research policy

Search broadly across public Senki mod source repositories, forks, release notes, and creator-provided resource/source packages. Verify actual implementation and distinguish selectable fighters from summons, guardians, clones, NPCs, alternate forms, and image-only/release-note leads.

Record exact source revision, provenance, code license, asset/voice permission, dependencies, and compatibility. Public visibility is not automatic permission to redistribute source or assets. Do not extract assets/code from APKs or copy unclear-rights content into a distributable build. Continue research and compatibility analysis while seeking a viable authorized source; never fabricate progress.

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

- Last verified central Actions run: [#206 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38043294444), commit [3c3f7f2](https://github.com/kage049754/Senki/commit/3c3f7f25818dce5c9b966e53a755fd50d74ca04c).
- The run checks page-button atlas parsing, dynamic pagination, Lua/source assertions, Android candidate build/package checks, and artifact upload.
- External-mod characters integrated: **0**. External-mod characters verified playable: **0**.
- Page 4/5 image-style pagination is groundwork, not roster progress.
- Physical-phone install, startup, and gameplay have **not** been verified.
- Source and third-party asset permissions remain unresolved for inspected candidates. The full V2 source tree is not yet vendored here.

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
