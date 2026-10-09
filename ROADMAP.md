# Senki Development Roadmap

This roadmap is a living plan. The checked status must reflect repository evidence, not intention. Update it whenever a milestone is completed or the plan changes.

## Phase 0 — Repository foundation and audit
**Status: In progress**

- [x] Create README entrypoint and mandatory AI instructions.
- [x] Establish source-research and rights/provenance rules.
- [ ] Inspect all files and determine whether any game implementation exists.
- [ ] Choose/confirm the Android engine and build toolchain based on the actual repository state.
- [ ] Add a reproducible GitHub Actions Android build.
- [ ] Make CI upload the APK as an artifact.
- [ ] Record baseline build result and known issues.

**Exit checks:** project structure is documented; build can be reproduced; latest CI run is green; APK artifact is confirmed.

## Phase 1 — Startup and landscape shell
**Status: Not started**

- [ ] Android app installs with a valid package/application ID.
- [ ] Configure landscape orientation and handle common phone aspect ratios/safe areas.
- [ ] Show a loading state and then a visible main menu after startup.
- [ ] Add menu navigation: Play, Mode, Characters, Settings, Exit/back behavior.
- [ ] Add touch target sizing and basic sound/music toggles.
- [ ] Add crash logging and a graceful error screen instead of a blank screen.

**Exit checks:** cold launch, back navigation, menu taps, and orientation behavior are verified; no blank screen after splash.

## Phase 2 — Playable battle vertical slice
**Status: Not started**

- [ ] One arena/map with ground/lane and both bases.
- [ ] Player character movement and facing.
- [ ] Basic attack with hit detection, animation timing, damage, and hit reaction.
- [ ] HP/death/respawn.
- [ ] At least two skills with cooldowns and visible feedback.
- [ ] Simple enemy AI.
- [ ] Pause/restart/quit battle flow.

**Exit checks:** player can enter a match, move, attack, use skills, take damage, die/respawn, pause, and return to the menu without crashing.

## Phase 3 — Lane combat systems
**Status: Not started**

- [ ] Allied and enemy minion wave spawning.
- [ ] Minion pathing, targeting, attacks, HP, and death.
- [ ] Towers/base objectives with target range and damage.
- [ ] Experience/level progression and agreed stat/skill upgrades.
- [ ] Victory/defeat conditions and result screen.
- [ ] Match reset restores all state without stale units or timers.

**Exit checks:** a complete match has a clear winner, can be restarted repeatedly, and has no stuck waves or immortal objectives.

## Phase 4 — Scalable character framework and starter roster
**Status: Not started**

- [ ] Define data-driven character stats and skill metadata.
- [ ] Define a dynamic character registry/catalog with stable string IDs; no fixed roster capacity.
- [ ] Define animation/state contracts: idle, move, attack, cast, hit, death, respawn.
- [ ] Standardize skill interface: input, cooldown, targeting, hitbox/projectile, effects, damage, duration.
- [ ] Build responsive roster selection with portrait/name/stats and locked/unlocked states if needed.
- [ ] Support scrolling/pagination, search, and useful filters/categories.
- [ ] Add a small balanced starter roster with genuinely distinct move sets.
- [ ] Ensure bots use the same battle/skill rules as players where appropriate.
- [ ] Add validation for missing IDs, resources, animations, and skill references.
- [ ] Add a test fixture with at least 75 synthetic/test entries to prove the catalog/UI is not capped at 29 or 70; these test entries must not be presented as real playable characters.

**Exit checks:** adding a character does not require rewriting the core battle engine; roster selection reliably spawns the selected fighter; the catalog handles at least 75 test entries without a fixed-capacity limit.

## Phase 5 — Research-driven roster expansion (target: 70+ playable characters, expandable beyond)
**Status: Not started**

- [ ] Continue searching GitHub for Naruto Senki source repositories, forks, mod repositories, release changelogs, and compatible character implementations.
- [ ] Inspect each candidate's code/resources and record exact findings in docs/MOD_RESEARCH.md.
- [ ] Separate actual game source from APK-only distributions, file hosts, documentation sites, translations, and unrelated Naruto mods.
- [ ] Map characters, alternate forms, skills, summons, animations, effects, and balance ideas.
- [ ] Review license/terms and provenance before reuse.
- [ ] Port only compatible, permitted implementations; otherwise implement original equivalents from high-level gameplay observations.
- [ ] Consolidate duplicate characters; keep forms only when gameplay is meaningfully different.
- [ ] Add characters in manageable batches and test each batch for crashes, animation errors, and balance.
- [ ] Track discovered, planned, implemented, tested, and verified counts separately.
- [ ] Keep roster size data-driven; do not add a hardcoded upper bound.
- [ ] Lazy-load resources and test memory use as the roster grows.
- [ ] Ensure selection, AI, save/unlock data, and battle spawning work with the full catalog.

**Exit checks:** at least 70 distinct playable characters are implemented and individually verified before claiming the 70+ target is met; no artificial code-level roster ceiling; every imported code/asset has recorded provenance and permission basis; each character passes selection, battle, skills, death, respawn, and applicable AI checks. Continue to allow expansion beyond 70.

## Phase 6 — Modes, polish, and performance
**Status: Not started**

- [ ] Add more maps and modes only after the core battle is stable.
- [ ] Add effects, sounds, hit flashes, camera feedback, and readable skill telegraphs.
- [ ] Add pause/settings and control customization if justified.
- [ ] Optimize memory, texture sizes, loading time, and frame pacing for mid-range Android phones.
- [ ] Test different screen sizes and Android versions.
- [ ] Add automated tests for game-state transitions and core combat calculations where possible.
- [ ] Test a large roster without loading every character's heavy assets into memory simultaneously.

**Exit checks:** stable repeated matches, no major UI clipping, no obvious memory leaks, and acceptable performance on target devices.

## Phase 7 — Release candidate
**Status: Not started**

- [ ] Run clean release build and inspect logs.
- [ ] Confirm application ID, version, signing setup, orientation, permissions, and package integrity.
- [ ] Confirm final GitHub Actions run is completed and successful.
- [ ] Verify the exact APK artifact and provide the artifact/run link.
- [ ] Install and launch on a physical Android phone.
- [ ] Test first launch, character select, battle, skills, minions, towers, result, and restart on device.
- [ ] Document known issues and release notes.

**Exit checks:** CI success and APK artifact are verified; device installation and launch are separately verified; no unresolved blocker prevents the planned release.

## Working rules

- Do not jump to a huge roster before one complete battle works, but design the roster architecture for 70+ from the beginning.
- Do not jump to a huge roster before one complete battle works.
- Do not merge entire projects blindly. Port systems into a single consistent architecture.
- Do not assume a source repository grants permission to redistribute its code or assets.
- Keep the game landscape-first and core gameplay offline.
- After each code milestone, follow the full failure-inspection/fix/rebuild/verify loop in AGENTS.md.
- Mark a task complete only after its stated exit checks have evidence.
