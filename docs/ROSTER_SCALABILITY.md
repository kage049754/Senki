# Roster Expansion Within the Existing Senki Base

> **Do not create a new game or replacement engine.** These notes apply only after an existing Naruto Senki base is selected. Preserve its roster/character architecture and adapt it for compatible mod content where practical.

## Goal
Expand the selected existing Senki game's roster toward **70+ playable characters**, with room for future expansion if the base supports it. Do not replace the game engine just to reach a number. Preserve the chosen base's native architecture and change it only as required for compatible content.

This is an architecture requirement, not a claim that the roster system is already implemented or that 70 characters already exist.

## Mandatory design rules
1. **No hardcoded roster cap.** Do not use constants, fixed arrays, enum ranges, or fixed UI slots to limit the catalog to 29, 30, 50, 70, or another arbitrary count.
2. **Data-driven registration.** Character definitions must be discoverable through a registry/catalog. Every character needs a stable unique ID independent of list position.
3. **Content-first addition.** Adding a standard character should normally involve adding a validated definition and permitted resources/behavior, not rewriting the selection screen or battle engine.
4. **Reusable mechanics.** Prefer shared skill/action implementations with data-driven values. Add custom code for mechanics that genuinely need it.
5. **Scalable selection UI.** Use scrolling or pagination and support search, filters, and categories. Never create a separate hardcoded button for every character.
6. **Lazy resource loading.** Load portraits and heavyweight animation/effect/audio resources as needed. Release resources safely when no longer needed.
7. **Stable references.** Save data, unlock states, AI choices, and battle spawning must use stable character IDs, never list indices.
8. **Validation.** Detect duplicate IDs, missing portraits/animations, invalid skill references, missing resources, and unsupported schema versions. Report actionable diagnostics.
9. **Variants and deduplication.** Represent distinct forms separately when appropriate. Avoid duplicate entries that differ only in spelling; preserve variants with meaningful gameplay differences.
10. **Measured limits only.** Runtime limits may restrict simultaneously loaded resources or fighters for performance, but must not impose an arbitrary maximum on the total roster catalog.
11. **Offline catalog.** Core roster browsing and battles must not depend on a server or account.
12. **Verified counts.** Count only characters that are implemented and have passed the defined tests as verified playable characters.

## Suggested character data
Use the format appropriate to the chosen engine. A character definition should include stable ID, display name, schema version, stats, skill IDs/parameters, animation-state mappings, resource identifiers, collision settings, AI profile, optional form relationship, and provenance/license references.

Do not implement a new engine, roster framework, or data format before the existing base has been selected and its actual architecture inspected. Prefer its native systems.

## Character selection UX
- Search by display name or ID.
- Filter by category, role, or form when metadata supports it.
- Scroll or paginate through the catalog.
- Show selected character details and clear selection state.
- Avoid loading every full animation atlas at once.
- Handle missing/locked content safely rather than crashing.
- Keep controls usable on phone-sized landscape screens.

## Performance plan
- Separate lightweight catalog metadata from heavy resources.
- Load detailed resources when a character is selected or spawned.
- Cache only a bounded number of recently used resource bundles where useful.
- Release textures/audio/animations using the engine's correct lifecycle.
- Test memory, frame time, and load time with large catalogs and active battles.
- Keep total roster size independent from the number of fighters simultaneously instantiated in a battle.

## Required scalability tests
Before claiming the architecture supports a large roster:
- [ ] Register at least 75 synthetic/test definitions.
- [ ] Confirm all 75 appear through scrolling/search/filtering without fixed-capacity UI changes.
- [ ] Confirm duplicate IDs are detected.
- [ ] Confirm missing/invalid resource references produce useful errors.
- [ ] Confirm selection resolves by stable ID, not index.
- [ ] Confirm valid test entries can spawn using test resources/behavior.
- [ ] Confirm browsing does not load every heavy character resource.
- [ ] Confirm repeated selection/switching remains stable.
- [ ] Record actual CI and device/emulator results.

Synthetic entries test architecture only and must not be counted as real playable characters.

## Definition of 70+ playable characters
The milestone is met only when at least 70 distinct entries are in the in-game catalog and can be selected and spawned into battle, have functional movement/basic attacks and declared skills, pass animation/death/respawn/applicable AI checks, load resources safely, and have provenance/permissions recorded.

Portrait-only placeholders, planned entries, synthetic tests, unreviewed assets, and characters with broken skills do not count.

## Current status
- Architecture requirement documented.
- Actual registry/UI implementation: NOT VERIFIED.
- 75-entry scalability test: NOT RUN.
- Verified playable roster count: NOT YET MEASURED.

Update only after inspecting and testing the actual code.
