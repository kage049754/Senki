# Naruto Senki V2 Mod-Merging Roadmap

**Mission:** integrate distinct playable characters from other Naruto Senki mods into the existing V2 game. Do not create a separate game. Long-term target: 70+ distinct playable characters, counted only after complete integration and testing.

## Priority order

1. Find actual external Senki mod character implementations.
2. Compare them with the V2-derived base and map all source/resource dependencies.
3. Port one distinct character completely into an available page 1–3 slot.
4. Build and test that character.
5. Repeat in small batches toward 70+.
6. Expand pages 4/5 as needed without breaking original page controls.

Do not spend roster-expansion effort recounting V2 forms, summons, clones, or support units. Do not silently replace existing characters. Preserve original backgrounds and navigation behavior.

## Phase 0 — Instructions and truthful baseline
**Status: DOCUMENTATION REFRESHED; maintenance continues**

- [x] Make the no-new-game rule explicit.
- [x] Make external-mod playable characters the first roster priority.
- [x] Define complete character integration and verification.
- [x] Define the CI wait → inspect logs → fix → rerun → verify artifact loop.
- [x] Separate CI from physical-phone testing.
- [ ] Keep docs aligned after real changes.

**Exit gate:** a new session can identify the mission, latest build, honest character count, and next task without relying on stale checkpoints.

## Phase 1 — Maintain a buildable existing V2 base
**Status: CI candidate builds; full source vendoring and phone validation incomplete**

- [x] Keep the V2-derived Cocos2d-x/C++/Lua architecture in the central candidate workflow.
- [x] Maintain central patch/build/package checks in .github/workflows/v2-source-smoke.yml.
- [x] Build and test dynamic pagination and image-style page 4/5 controls in CI.
- [ ] Document the exact chosen source revision and provenance decision.
- [ ] Establish a reproducible editable source tree or stable integration method in this repository.
- [ ] Resolve relevant source and asset permissions before importing/redistributing external content.
- [ ] Install the candidate APK on the user's phone and record startup/menu results.

**Exit gate:** reproducible V2-based build and source provenance are documented; install/startup are separately tested on the phone.

## Phase 2 — Discover external playable characters (ACTIVE)
**Status: ACTIVE — one Sasori's source action XML is converted to V2 and passes CI integration checks; unique controller/skill completion and source discovery continue**

- [x] Review public Senki mod repositories and release histories.
- [x] Record leads including Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Might Guy, Yamato, Sasori, Zetsu, Iruka, Jirobo, Tayuya, and Anko.
- [x] Inspect several V2 forks and legacy Cocos2d-x sources; many repeat the base roster or expose support/NPC implementations only.
- [x] Inventory visible release-pack resource names for the six priority characters (names only; payloads are packed and not importable by the current importer).
- [ ] Continue searching for complete, inspectable source/resource implementations from other Senki mods and forks.
- [ ] If no editable package is found, build an original compatible implementation with independently created assets; never call a name-only audit a port.
- [ ] Verify that each candidate is independently selectable or map a concrete adaptation path.
- [ ] Compare exact dependencies with the pinned V2 candidate and identify duplicates.
- [ ] Track source revision, code license, asset/audio provenance, and permission evidence.
- [ ] Select the first technically feasible external character and document its port plan.

**Exit gate:** at least one distinct external character has a complete inspectable implementation, a clear provenance/permission decision, and a documented port plan. Release-note names and APK-only leads do not pass.

## Phase 3 — Port the first complete character
**Status: IN PROGRESS — Sasori candidate integrated with Kankuro-compatible baseline; unique combat and runtime validation remain incomplete**

- [ ] Reserve an available page 1–3 slot without displacing an existing character.
- [ ] Add stable ID, display name, selection portrait, and atlas/resource mapping.
- [ ] Adapt sprites/model, animation data, movement, basic attack, all skills, projectiles/effects, and dependencies.
- [ ] Connect skill icons/names/descriptions, selected-character profile, and kill/death/report UI.
- [ ] Connect player controls and AI using native game systems.
- [ ] Wire available audio/voice/SFX where permitted.
- [ ] Test spawn, movement/facing, basic attack, every skill, cooldown/resource use, AI, death/respawn, and cleanup.
- [ ] Run static/resource checks and Android build; inspect failures and rerun until success.
- [ ] Mark VERIFIED only with runtime evidence.

**Exit gate:** one genuinely selectable/playable external character is integrated, CI passes, and runtime/device-test status is documented.

## Phase 4 — Repeat and grow toward 70+
**Status: WAITING FOR FIRST VERIFIED PORT**

- [ ] Reuse the proven integration pattern in small batches.
- [ ] Keep pages 1–3 the first target; add pages 4/5 as capacity requires.
- [ ] Preserve each character's portrait, animations, skills/effects/audio, AI/control path, and kill/death/profile identity.
- [ ] Run duplicate-ID, missing-resource, atlas-frame, Lua syntax, pagination, and APK regression checks.
- [ ] Update per-character evidence and the remaining gap after each batch.
- [ ] Do not count forms or variants as distinct characters unless independently playable and explicitly classified.

**Exit gate:** 70+ distinct playable characters are individually verified, or the precise source/technical limit is evidenced and the remaining gap is reported honestly.

## Phase 5 — Final regression, APK, and phone validation
**Status: NOT STARTED**

- [ ] Run full regression/build workflow on the final commit.
- [ ] Confirm the exact run is completed/success, not queued/running/stale.
- [ ] Verify the exact artifact, package identity, signature, native ABI libraries, and required assets.
- [ ] Install on the user's Android phone.
- [ ] Check startup, main menu, character select, page buttons 1–5, portraits, original backgrounds, battle launch, movement, skills, audio, death/respawn, and repeated matches.
- [ ] Fix installation/blank-screen/crash issues using actual device or log evidence.
- [ ] Publish only when build and device-test status are recorded.

**Exit gate:** final artifact and actual device results are documented, with remaining issues clearly listed.

## Mandatory CI loop

For every code-affecting change: inspect latest run for exact commit → wait while queued/running → inspect failure logs → fix root cause → commit/rerun → wait → verify success and artifacts. Repeat after each failure. Docs-only commits may not trigger the path-filtered workflow; do not create fake code changes to force CI.

## Current blocker and next task

External character variants integrated: **1 — Two Sage Toads** (Choji-based variant, not a distinct base character). Initial Sasori candidate: **1** roster identity/atlas integrated and CI-checked, using Sasori-specific converted action XML with a Kankuro-compatible controller/skill UI. Distinct external characters verified playable in runtime: **0**. Page 4/5 image-style pagination is engineering groundwork only.

**Next:** finish Sasori's character-specific combat and runtime checks, while continuing source-level discovery across the remaining priority targets. The Sasori uses a tracked Saso atlas and converted character-specific animation XML, but the controller/skill UI remains Kankuro-compatible and source asset permissions are unresolved; keep candidate artifacts private. Do not mark Sasori VERIFIED until unique skills, selection/profile/kill-feed identity, AI/player controls, and match lifecycle are checked. Then continue with Kurenai, Might Guy, Yamato, Hashirama, Shizune, Rin, and other leads in small batches.

## Related records

- Source inventory: docs/MOD_RESEARCH.md
- Character implementation/testing: docs/CHARACTER_ROSTER.md
- Code/asset provenance: docs/ASSET_LICENSES.md
- Base/source audit: docs/BASE_GAME.md and docs/V2_BUILD_AUDIT.md
- Latest build evidence: PROGRESS.md
