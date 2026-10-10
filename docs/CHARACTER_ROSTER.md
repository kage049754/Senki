# Senki Modded Roster and Verification Tracker
> **PRIMARY PRIORITY — EXTERNAL SENKI MOD CHARACTERS:** This tracker must focus on characters implemented by other Naruto Senki mods and their port/integration status. Do not spend roster-expansion work auditing or recounting current V2 characters, forms, summons, or enum-only entities. Use the current V2 roster only as a duplicate/compatibility check. Prioritize new external characters for available slots on pages 1–3, preserving original image-based page controls. Record exact source, implementation files, provenance/permissions, missing components, integration state, and test evidence. A name, asset-only lead, or release-note mention is not an integrated/playable character.

> **This tracker is for content merged into one selected existing Naruto Senki base. Do not create a new game or replacement roster engine. First select the base, then record compatible mod content ported into its native systems.**

## Purpose
Track character discovery, implementation, rights review, and gameplay verification separately. The chosen game's existing roster may be expanded toward 70+ verified playable characters where feasible. Extend its native systems only as needed; roster size is not a reason to build a new engine.

## Status definitions
- DISCOVERED — a name or implementation lead has been found.
- RIGHTS_REVIEW — code/asset permission needs review.
- RESOURCE_REVIEW — source files and resource formats are being inspected.
- PLANNED — intended for the game, not implemented.
- IN_PROGRESS — implementation is underway.
- IMPLEMENTED — code/resources exist, but full testing is incomplete.
- TESTING — required tests are in progress.
- VERIFIED — required tests pass and provenance/permissions are recorded.
- BLOCKED — permission, resource, or technical blocker.
- EXCLUDED — not included in this project.

## Count rules
Always report separate counts for discovered leads, planned characters, implemented characters, characters in testing, verified playable characters, and blocked/excluded entries.

Do not count planned characters, portraits, untested entries, synthetic test entries, or duplicate variants as verified playable characters.

Target: at least 70 verified playable characters. The registry itself must not have a hardcoded upper limit.

## Character entry template
- Unique character ID:
- Display name:
- Form/variant:
- Source repository or original design:
- Source commit/version:
- Source category: original / licensed / permission-approved / reference-only
- Code license status:
- Asset permission status:
- Portrait:
- Animation set:
- Basic attack:
- Skills:
- Ultimate/transformation:
- Stats and balance:
- AI profile:
- Selection test:
- Battle spawn test:
- Skill tests:
- Death/respawn test:
- Performance/resource test:
- Status:
- Evidence/notes:
- Next action:

## Current verified roster
**Verified playable character count: NOT YET MEASURED.**

**Source inventory (not runtime-verified):** the pinned Android-clean candidate's original roster defines 37 unique selectable names. The current CI patch exposes six additional existing native forms on page four and adds the Two Sage Toads mod variant, for **44 selectable entries but only 37 distinct base characters** across 84 slots/four pages. The target gap remains **33 additional distinct characters** to reach 70; alternate forms and replacement-based mod variants do not count as new base characters. The five Pain-path C++ headers are implementation classes, not separate selectable roster entries. Gameplay-verified count remains unmeasured. See `PROGRESS.md` for the latest build and artifact.

No individual character is marked VERIFIED by this tracker. Populate entries only after inspecting the actual project and testing the character.

## Current external mod integration — Two Sage Toads

- **Status:** IMPLEMENTED in the CI candidate; **not gameplay-verified**.
- **External source:** [LeaderOnePro/NarutoSenki1.17Mod](https://github.com/LeaderOnePro/NarutoSenki1.17Mod), pinned by CI to commit `8c800efe09f8e5489f37ee3314596b329f533225`.
- **New roster ID/display name:** `TwoSageToads` / Two Sage Toads. Added as a separate selectable entry; existing Choji remains available.
- **Integrated package:** modded character atlas and skill atlas; V2-compatible animation XML; audio package with fallbacks; native enum/Provider dispatch; selection portrait/name handling; UI atlas aliases; resolved XML-to-atlas frame references.
- **Important limitation:** this is a Choji-replacement mod adapted as a separate variant. It reuses Choji's native combat/AI and skill behavior as a compatibility baseline; it does **not** yet have a unique Two Sage Toads moveset.
- **CI evidence:** [run #225 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38050182005), commit `de44153c133a56482be4b8ff07f3e0368607cdf1`. APK artifact ID `11669112048`; audit artifact ID `11669441632`.
- **Remaining verification:** install the APK on a phone, confirm selection art/preview, start a battle, test movement/attacks/skills/AI/death/respawn, and inspect for missing sprites/audio/crashes. Do not count this variant toward the 70 distinct-base-character goal.

## Batch verification checklist
- [ ] IDs are unique and stable.
- [ ] Required assets and permission records exist.
- [ ] Character appears in the dynamic catalog.
- [ ] Search/filter/scrolling can find it.
- [ ] Selection spawns the intended character.
- [ ] Movement and facing work.
- [ ] Basic attack works.
- [ ] Every declared skill works.
- [ ] Cooldowns and damage are correct.
- [ ] Animation transitions work.
- [ ] Death and respawn work.
- [ ] AI behavior works when applicable.
- [ ] Resources load and release safely.
- [ ] No blocking crash remains.
- [ ] Status and evidence are recorded.

## Historical/possible character leads
Names mentioned in source release notes or mod descriptions belong in research records first. They must not be treated as implemented until individually ported and verified. Refer to docs/MOD_RESEARCH.md for sources and evidence.


## Source baseline inventory — 2026-10-10

- [x] Inspected `lua/class/basic.lua` in Android-clean candidate commit `279e85e73040558c84988a0eea310b6286eb77f0`.
- [x] Counted 37 unique selectable character names in `ns.CharactersLayout`.
- [x] Inspected the C++ `Classes/Core/Shinobi/` folder: 42 headers total, five of which are Pain-path implementation classes rather than standalone selectable characters.
- [x] Identified Kabuto as a custom redesigned character unique to the Android-clean candidate compared with the LAN-enhanced candidate.
- [ ] Test each selectable character in battle before counting it as verified playable.
- [ ] Audit every character's class, XML/config, sprite/plist, animation/effects/audio, skill IDs, and selection portrait/button assets.


## Selection scalability patch status — 2026-10-10

- [x] Central patch `patches/android-clean/0008-dynamic-roster-pagination.patch` removes the fixed three-page cap and derives pages from the actual layout list.
- [x] CI build `38016671857` passed Lua syntax checks and produced artifact `11655938596`.
- [ ] No new character has been added by this patch. Current source-level selectable count remains 37; verified playable count remains unmeasured.
- [ ] After device validation, begin adding compatible characters in small batches with all portrait/button/XML/sprite/plist/audio/skill references audited.


## Additional discovered mod character leads — 2026-10-10

These are **DISCOVERED / RESOURCE_REVIEW leads only** from release notes, not integrated characters. The release source and exact asset files are not yet mapped to V2.

| Character or form | Discovery source | Current status | Next action |
|---|---|---|---|
| Shizune | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources; check offline compatibility |
| Hashirama | NarutoSenki v1.26 beta 1 and FDPL v1.22 notes | DISCOVERED / APK-only lead | Find source/asset lineage; compare skill kit |
| Rin | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Sakon & Ukon | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Determine whether implemented as one selectable slot or linked forms |
| Juzo | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Kurenai | NarutoSenki v1.25 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Might Guy | NarutoSenki v1.25 beta 1 and FDPL v1.22 notes | DISCOVERED / APK-only lead | Find source/resources; do not overwrite Tenten in the unified roster |
| Yamato | NarutoSenki v1.25 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Sasori (awakened form) | NarutoSenki v1.26 beta 1/2 release notes | DISCOVERED / form/skill lead | Identify separate form vs shared character implementation |
| Zetsu | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Iruka | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Third Kazekage | NarutoSenki v1.26 beta 1 release notes | DISCOVERED / AI lead | Determine whether selectable and find implementation |
| Jirobo | NarutoSenki v1.24 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Tayuya | NarutoSenki v1.24 beta 1 release notes | DISCOVERED / APK-only lead | Find editable class/resources |
| Anko (including revised skin) | NarutoSenki v1.24 beta 1 and v1.24 beta 2 release notes | DISCOVERED / form/skill lead | Find editable class/resources |
| White Mask Tobi | FDPL v1.22 third-party mod listing | DISCOVERED / replacement-based lead | Seek additive implementation so existing Tobi is preserved |
| Pain (alternate implementation) | FDPL v1.22 third-party mod listing | DISCOVERED / replacement-based lead | Compare against existing Pain; avoid losing base character |

Source inventory links and compatibility notes are recorded in docs/MOD_RESEARCH.md. Do not count these as planned/implemented/verified until the exact source files, resources, and integration tests are available.


## Latest pagination acceptance status — 2026-10-10

- [x] Dynamic page count and image-based pagination patch passed central CI build [run 38020781870](https://github.com/kage049754/Senki/actions/runs/38020781870).
- [x] Pages 1–3 retain their original image controls; pages 4+ use generated normal/selected image states styled from the original page-button art. CI confirms page 4/5 image assets are packaged and the retired custom menu/selection backgrounds are absent.
- [ ] Device-test the visual match, page navigation, original page 1–3 controls, preview/tap-again confirmation, and character spawn behavior.
- The original source baseline was 37 selectable names. The current patched candidate declares 43 names after six existing native forms were exposed. Verified playable count remains unmeasured; pagination itself does not add characters.


## Required per-character asset and AI manifest

Add this manifest to every planned or integrated character entry. Fill in exact paths/references; do not use a generic “assets complete” statement.

- Selection display name and stable character/form ID:
- Selection portrait/avatar path:
- Selection button/thumbnail normal + selected assets:
- Selection preview art/model/sprite path and preview test:
- Skill viewer: skill names / icons / descriptions / order / cooldown-cost fields:
- Main sprite/model and atlas/texture/plist paths:
- Animation states: idle / move / attack / cast-skill / hit / knockback / death / transform / other:
- Voice clips/voice lines (paths, triggers, or documented not-applicable reason):
- Attack/skill/hit/summon/transformation sound effects (paths and event references):
- Per-skill logic, projectile/summon, effects, hitbox, damage, cooldown, costs:
- Character class/script/XML/config and all referenced resource paths:
- Player selection/control tests:
- AI roster/selection/spawn registration path:
- AI behavior tests (move, basic attack, each skill, range/state/cooldown, summon/transform):
- Resource manifest state per category: FOUND / ADAPTED / CREATED / NOT APPLICABLE / MISSING / BLOCKED:
- Source commit/version and provenance/permission record:
- Missing items and completion impact:
- Test evidence and status:

### Full-completion checklist (all applicable items required)
- [ ] Correct display name, unique ID, selection avatar/portrait, button states, and preview.
- [ ] Skill viewer correctly shows every actual skill's name, icon, and description.
- [ ] All required sprite/model, atlas/plist, and animation states are present and load.
- [ ] Voice clips/voice lines are inventoried; supplied/required clips play at the correct events, or absence is explicitly documented and classified.
- [ ] Skill, attack, hit, summon, transformation audio and visual effects map to the intended actions.
- [ ] Player selection, movement, basic attack, every skill, hit detection/damage, cooldowns, and death/respawn work.
- [ ] Existing game AI can select/spawn this character in supported modes and use its valid attacks/skills without resource errors.
- [ ] All resource/config references resolve and IDs do not collide with existing fighters.
- [ ] Manifest, provenance, missing assets, and runtime evidence are recorded.

A character with missing required assets or unverified AI remains partial/incomplete/blocked. Do not count it as VERIFIED based on its name, portrait, a successful build, or player-only selection. The current 37 roster names are only source-level selectable entries; the number with complete asset packages and verified AI is not yet measured.

## Full character package: required per-entry audit

For each discovered or integrated character, complete these fields in the roster entry or its linked manifest:

- Stable character/form ID and exact source URL, branch/commit/version.
- Display name; selection portrait/avatar; normal/selected selection button art; preview resource and preview test.
- Skill-view entries: skill names, icons, descriptions, IDs and link to the actual implementation.
- In-game sprite/model; texture/atlas/plist; animation states and frame references.
- Basic attacks, hitboxes/range/timing, damage, cooldowns, passive/active/ultimate abilities supported by the source, projectiles/summons/status effects/VFX.
- Voice lines/clips, file paths, and the events that trigger them.
- Attack/skill/ultimate/hit/death/summon/transformation SFX, file paths and event triggers.
- Player input/selection test and the character actually spawned in battle.
- Game AI registration/selection/spawn path; AI tests for movement, basic attacks, range/state/cooldowns and each supported skill/summon/transform.
- Resource/config integrity, duplicate-ID check, APK packaging check, in-game test results and explicit missing/not-applicable reasons.
- Source/license/permission status for code, art, animation, voice, SFX and effects.

A field may be marked missing/not-applicable only with a brief reason. Do not treat a missing voice pack or unavailable skill as complete. A fighter is not PLAYABLE-VERIFIED until the intended character spawns correctly, the skill UI maps to working skills, applicable assets/audio resolve, and supported AI behavior passes. Build checks and source-level roster names are separate from gameplay verification.


## Findings from latest automated source inventory (2026-10-10)

- **Kabuto — manual skill-view audit required:** expected `Kabuto_label1.png` through `Kabuto_label5.png` were not found by the current loose-file/plist-name heuristic (0/5 matches). The same report found 5/5 expected skill-icon frame names, selection frame names, a native enum reference, a C++ header, Unit resource paths, and Kabuto-named audio paths. This discrepancy may mean the labels use a different naming/atlas convention; it is **not** proof the skill descriptions are absent. Inspect `SkillLayer.lua`, the actual atlas frame keys, and the in-game skill viewer before deciding.
- **Kiba — manual resource audit required:** only three path matches were counted by the broad Unit-resource heuristic. This count does not prove missing assets; inspect exact sprite/projectile/config references.
- The audit's AI column is only a recognizable registration-pattern clue. `MANUAL_AI_AUDIT_REQUIRED` is not a verdict that AI is broken.
- These are audit exceptions, not new characters. New characters added: **0**. Full playable/AI-verified roster count remains unmeasured.


## Legacy V1.17/V2-adjacent source leads — not integrated

Source inspected: [Zx-Akito/NarutoSenki](https://github.com/Zx-Akito/NarutoSenki), branch `master` at commit `d847b113dfce486822768ef5a1c1c874b50fa3cd`. This is a legacy monolithic Cocos2d-x project, not the current modular V2 candidate. These entries are **DISCOVERED / SOURCE-INSPECTED** only; none is added to the central game's roster by this research.

| Candidate form/character | Evidence found in legacy source | Selection package check | Current status / missing work |
|---|---|---|---|
| Sage Jiraiya | `Classes/Characters.cpp` has an `AI_SageJiraiya()` dispatch branch; `Resources/Element/SageJiraiya/SageJiraiya.{xml,plist,pvr.ccz}`; character audio folder and skill clips; Ougi audio | `SageJiraiya_half.png` found in legacy `Resources/Select.plist`; expected `_select.png` and `_font.png` not found | **SOURCE-INSPECTED / PARTIAL**. No complete selection identity and no V2 class/resource/AI port. |
| Immortal Sasuke | AI dispatch branch; `Resources/Element/ImmortalSasuke/ImmortalSasuke.{xml,plist,pvr.ccz}`; character audio and Ougi clip | `ImmortalSasuke_half.png` found; expected `_select.png` and `_font.png` not found | **SOURCE-INSPECTED / PARTIAL**. V2 already has Sasuke but this variant needs a collision-free form ID, actual skill/animation mapping and full selection package. |
| Rikudo Naruto | AI dispatch branch; `Resources/Element/RikudoNaruto/RikudoNaruto.{xml,plist,pvr.ccz}`; character skill audio and Ougi clip | `RikudoNaruto_half.png` found; expected `_select.png` and `_font.png` not found | **SOURCE-INSPECTED / PARTIAL**. V2 has Naruto-related forms; do not assume this is a drop-in alternate form. |
| MaskRaidon | AI dispatch branch in legacy `Classes/Characters.cpp`; `Resources/Element/MaskRaidon/MaskRaidon.{xml,plist,pvr.ccz}` | No `_select.png`, `_half.png`, or `_font.png` frame found in the inspected legacy Select atlas | **SOURCE-INSPECTED / PARTIAL**. Needs complete selection UI, skill/audio inventory, and V2 port analysis. |

**Shared gaps for all four:** old Cocos2d-x class/AI architecture and `Resources/Element` conventions do not match the current V2 candidate's `Classes/Core/Shinobi`, AI registration, and `Resources/Unit/Ninja` layout. No asset was copied. Each port still needs a category-by-category manifest covering identity, skill icons/descriptions, model/animations, skills/cooldowns/hitboxes, voice/SFX triggers, effects/projectiles/summons, player controls, AI behavior, unique IDs, and runtime evidence. CI must verify source changes; actual battle/device tests are required before PLAYABLE-VERIFIED.


## Automated package audit — run #109 — 2026-10-10

The generated report for pinned candidate `279e85e73040558c84988a0eea310b6286eb77f0` found:

- **37** unique selectable names in source (not equivalent to 37 verified playable characters).
- **37/37** names have both expected kill-feed portrait frames declared in the audited atlas.
- **36/37** names have all five expected skill-description label frames under the current naming rule.
- **Kabuto** is the sole exact-name exception: **0/5** expected `Kabuto_labelN.png` frames were detected.
- A guarded skill-view fallback is now applied in CI: if the requested description frame is missing, the viewer uses a visible generic `Skill description unavailable` label rather than blindly creating a sprite from a nonexistent frame. The fallback's source test and presence inside the packaged APK passed run #109.
- **No character was added by this UI/audit work.** No character has been promoted to VERIFIED; the playable count is still unmeasured.

Evidence: [run #109](https://github.com/kage049754/Senki/actions/runs/38025803886). Audit report artifact: `senki-character-package-audit` (artifact ID `11659909978`, expires 2026-10-24).

The filename/frame audit is a heuristic, not a runtime completeness proof. It does not establish that the five label frames are the only possible description mechanism, nor does it verify skill logic, animation, AI, audio, or device gameplay.


## Legacy mod leads found by source comparison — 2026-10-10

These are research leads from the older Cocos2d-x 2.2.2 source at `Zx-Akito/NarutoSenki`, not integrated V2 characters. Its fork `hendprw/NarutoSenki` has the same inspected tree SHA, so it is not a second independent source.

| Lead | Evidence found | Status | Porting issue |
|---|---|---|---|
| Sage Jiraiya | AI dispatch branch plus Element atlas/XML and dedicated audio folder | DISCOVERED / RESOURCE_REVIEW | Legacy C++ combat logic and PVR atlas format need adaptation |
| Immortal Sasuke | AI dispatch branch plus Element atlas/XML and multiple skill audio files | DISCOVERED / RESOURCE_REVIEW | Need map skills, transformations, and V2 state/resource IDs |
| Sage Naruto | AI dispatch branch plus Element atlas/XML and skill audio | DISCOVERED / RESOURCE_REVIEW | Clone/AI behavior must be separated from selectable character behavior |
| Rikudo Naruto | AI dispatch branch plus Element atlas/XML and skill audio | DISCOVERED / RESOURCE_REVIEW | Clone, Kurama and summon relationships need mapping |
| Roshi | AI dispatch branch plus Element atlas/XML and audio | DISCOVERED / RESOURCE_REVIEW | Confirm it is a complete selectable hero, not only an AI dispatch entry |
| Han | AI dispatch branch plus Element atlas/XML and audio | DISCOVERED / RESOURCE_REVIEW | Confirm selection and full battle initialization path |
| MaskRaidon / MaskFudon / MaskKadon | AI dispatch branches and Element atlas/XML packages | DISCOVERED / ENTITY_REVIEW | Current evidence may indicate related summon/entity units, not standalone heroes |
| Akamaru / Karasu / Saso / Parents / Sanshouuo / Slug / Centipede | AI dispatch and/or Element resource packages | DISCOVERED / ENTITY_REVIEW | Treat as summon/entity dependencies until hero-selection evidence exists |

**Counts:** these are 6 high-priority character/form leads and 9 additional entity leads (some categories may overlap); **0** have been ported or gameplay-verified. See `docs/MOD_RESEARCH.md` for the source and compatibility details. Do not increase the verified roster count from this list.


## Candidate roster expansion built in CI — 2026-10-10

The current CI patch exposes these six native forms in page four. Their native enum/class and XML/plist resources existed in the pinned candidate before the selection-list change. Run #121 also verifies each form atlas points to an existing texture file and that all six roster/UI aliases are packaged in the APK.

| Form | Existing native implementation | Selection UI adaptation | CI result | Device gameplay |
|---|---|---|---|---|
| Sage Jiraiya | Jiraiya class dispatch + form resources | Reuses Jiraiya small selection/skill icons; dedicated half portrait; readable text name | BUILD-VERIFIED in runs #117 and #121 | NOT TESTED |
| Immortal Sasuke | Sasuke class dispatch + form resources | Reuses Sasuke small selection/skill icons; dedicated half portrait; readable text name | BUILD-VERIFIED in runs #117 and #121 | NOT TESTED |
| Sage Naruto | Naruto class dispatch + form resources | Reuses Naruto small selection/skill icons; dedicated half portrait; readable text name | BUILD-VERIFIED in runs #117 and #121 | NOT TESTED |
| Six Paths Naruto (Rikudo Naruto) | Naruto class dispatch + form resources | Reuses Naruto small selection/skill icons; dedicated half portrait; readable text name | BUILD-VERIFIED in runs #117 and #121 | NOT TESTED |
| Rock Lee | Lee class dispatch + form resources | Reuses Lee small selection/skill icons; dedicated half portrait; readable text name | BUILD-VERIFIED in runs #117 and #121 | NOT TESTED |
| Nagato | Pain class dispatch + form resources | Reuses Pain small selection/skill icons; dedicated half portrait; readable text name | BUILD-VERIFIED in runs #117 and #121 | NOT TESTED |

**Important:** BUILD-VERIFIED means the roster/UI changes are present in the successfully built APK and the package checks pass. It does not prove each form can be selected, spawned, controlled, or used by AI at runtime. The verified playable character count remains **NOT YET MEASURED** until physical-device or suitable emulator gameplay checks pass.


## Latest roster regression and target-gap checks — 2026-10-10

- [x] Central CI run #126 passed the report target-gap validation and Android diagnostic build: https://github.com/kage049754/Senki/actions/runs/38028647795
- [x] Automated report states 43/70 declared names (27 more entries needed) and explicitly does not measure gameplay-verified playable count.
- [ ] None of the 43 declared entries should be called VERIFIED until selection, battle spawn, movement, attacks, skills, AI, death/respawn, and device/runtime checks are completed.
- [ ] Continue sourcing compatible, editable character implementations; asset-only or APK-only leads remain research references.


## Native enum-only entity audit — 2026-10-10

The pinned V2-derived candidate has 52 enum names but only 37 original selectable names before the six central form entries. The six existing forms are now exposed, for 43 declared selection names. The other enum-only entries include Pain paths, Naruto clones, and a shared Guardian implementation. These are not counted as playable characters because their complete standalone selection assets, player skill/control kits, and gameplay behavior have not been verified. See `docs/MOD_RESEARCH.md` for exact names and paths.


## Internal Pain-path character candidates — inspected 2026-10-10

The pinned source contains native classes and unit XML/atlas/texture resources for `AnimalPath`, `AsuraPath`, `NarakaPath`, `HumanPath`, and `PertaPath`. The code indicates that `NarakaPath` spawns several of the other paths as summons; these are not automatically equivalent to five fully playable roster entries.

- Selection atlas check: no `*_select.png`, `*_half.png`, or `*_font.png` frames were found for these five names in the inspected `Resources/Select.plist`.
- Several paths have specialized summon/AI behavior; simply adding their names to `ns.CharactersLayout` would not provide correct selection art, skill icons/descriptions, player-control UX, or proof of independent AI behavior.
- Status: **DISCOVERED / RESOURCE_REVIEW — do not count toward the 70-character target.**
- Next action: determine which paths are intended as summon-only, inventory their actual actions/sounds/AI, and only consider a selectable conversion if the full skill UI and player-control behavior can be implemented and tested without breaking Pain's existing summon logic.


## Automated enum-vs-roster check — run #159 (2026-10-10)

- Visible selection list: **43 distinct names** (the six existing native forms are included).
- Target shortfall: **27 additional distinct declared entries** to reach 70; actual verified playable count is still unmeasured.
- Nine enum names are absent from the visible selection list: `AnimalPath`, `AsuraPath`, `HumanPath`, `PertaPath`, `NarakaPath`, `NarutoClone`, `SageNarutoClone`, `RikudoNarutoClone`, and `Guardian`.
- These are manual-review leads, not extra playable entries: the clone classes and Guardian are support content, while the Pain paths appear to be specialized units used by NarakaPath/Pain. The selection atlas lacks their own selection button/portrait/name frames.
- CI run [#159](https://github.com/kage049754/Senki/actions/runs/38031862251) passed the updated report test and produced a verified diagnostic APK artifact. This still does not prove runtime playability or device installation.


## Hokage Minato resource lead — inspected 2026-10-10

The pinned V2 candidate has a `HokageMinato_half.png` selection frame and named audio references, but lacks the V2 unit XML/atlas/texture and native class/enum. A separate 1.17 APK/decompiled package, `LeaderOnePro/NarutoSenki1.17Mod`, contains `HokageMinato.xml`, `.plist`, `.png`, multiple skill/Ougi audio clips, a half portrait, and kill-feed portrait frames. Its XML uses the older 1.x schema and references multiple events/projectiles, so it is a resource lead—not a directly importable V2 character.

- Status: **DISCOVERED / RESOURCE_REVIEW; not integrated**.
- Next action: resolve provenance/permission, convert the XML to V2's unit schema, determine the native class/AI/control behavior, and test every skill, effect, sound, selection state, and death/respawn before counting it.
- The source package lacks dedicated `HokageMinato_select.png` and `HokageMinato_font.png` frames; selection button art and display-name handling need an explicit plan.
- The `NarutoRikudo` and `SasukeImmortal` strings found in selection artwork are naming variants of existing `RikudoNaruto` and `ImmortalSasuke`, not extra characters. `Black`, `Blink`, `None`, `None2`, `loading`, and `unknow` are not character entries based on this filename audit.


## Latest detailed package audit — 2026-10-10

- [x] Corrected texture-file and animation sound-event parsing in the audit script; run #164 passed the new regression gates.
- [x] Current declared roster: **43 distinct entries**; remaining gap to 70 declared entries: **27**.
- [x] Static resource audit: **43/43** have unit XML plus sprite plist/texture and both kill-feed portrait frames.
- [x] The audit now recognizes audio-event references in animation XML rather than incorrectly reporting zero.
- [ ] Skill-description art: **42/43** have all five expected label frames. Kabuto is the one flagged exception; fallback text exists, but the in-game skill view still needs manual verification.
- [ ] AI registration: the audit only identifies clues, not proof of complete AI behavior. Manually review entries marked MANUAL.
- [ ] Nine enum-only names remain manual-classification leads; do not count summons/support/clones as playable characters without proving they are independent selectable fighters.
- [ ] None of these static results promotes a character to VERIFIED. Test selection, spawn, movement, attacks, each skill, audio, AI, death/respawn, and resource stability in the actual game.
- [ ] The source and bundled asset permission review remains unresolved; no new external character package should be copied or redistributed until its permission status is approved.
- Evidence: [run #164 and diagnostic artifact](https://github.com/kage049754/Senki/actions/runs/38032945561).


## Animation XML-to-atlas frame-name audit — 2026-10-10

The audit now compares frame names referenced by each unit XML with frame keys in the corresponding unit plist. Latest verified result from run #168: **39/43** declared roster entries had no name mismatches.

Four packages require manual triage:

- **Asuma — 12 missing names:** all are `Asuma_Skill05_002` through `Asuma_Skill05_013`.
- **Kimimaro — 5 missing names:** the XML references `Jugo_Skill05_14` through `Jugo_Skill05_18`, which appears to be a likely copy/paste or wrong-atlas reference.
- **SageJiraiya — 6 missing names:** the XML references base `Jiraiya_AirHurt` / `Jiraiya_KnockDown` frames. Confirm whether the base atlas is loaded at runtime.
- **RockLee — 55 missing names:** many references use the base `Lee_` prefix while the form's XML also uses `RockLee_`; confirm whether the unit loader registers the base atlas or whether frame names are wrong.

These are static name mismatches, not yet confirmed runtime failures. The next audit output lists up to 12 missing frame names per affected entry. The known Kimimaro/Jugo mismatch is now guarded by a regression test. No character is promoted to VERIFIED by this static check; inspect runtime atlas loading and verify permissions before any source/assets are integrated.

Evidence: [run #168](https://github.com/kage049754/Senki/actions/runs/38033542630).


## User-priority slot plan — pages 1–3 first (2026-10-10)

The user's explicit order is to add **distinct characters sourced from other Naruto Senki mods into slots on pages 1, 2, and 3 before proceeding to pages 4 or 5**.

- Keep original page 1–3 image-based page buttons and their touch behavior. Keep the original character-selection and mode-menu backgrounds.
- First map the current slot-to-character order and identify open/replaceable slots. Do not silently replace an original character; note the exact slot and reason for any change.
- Prioritize distinct characters, not merely alternate transformations of Naruto, Pain, Sasuke, Rock Lee, or Jiraiya.
- Research leads such as Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Yamato, Zetsu, Iruka, Jirobo, Tayuya, Anko, Han, and Immortal Sasuke remain unverified leads unless the tracker has evidence for their exact source, permission, compatibility, and tests.
- Do not import external code/assets without permission. The current V2 source candidate has unresolved reuse rights; public visibility or a private fan build does not itself grant permission.
- A character is not “added” because its name appears in the layout or an audit finds files. Require complete assets and gameplay integration, then selection/spawn/skills/AI/death-respawn/resource tests.
- Keep page 4/5 expansion blocked behind the first verified page 1–3 batch. Do not pad page 4 with existing forms as if they were new mod characters.


## Required portrait mapping for every roster addition
Each new entry must have its own matching portrait/avatar rendered in its assigned character-selection slot. Track at minimum: page number, slot index, stable character ID, displayed name, portrait image file and atlas/frame key, source URL/repository, license or explicit permission evidence, and selection-screen test result. Also record supported skill/profile and kill/death portrait references. A missing, broken, unrelated, or placeholder portrait means the character is incomplete and cannot be counted as playable. Reference images used in discussion are not proof that assets have been imported. Existing entries must not be displaced without explicit approval; work on pages 1–3 first.


## Additional leads found — 2026-10-10

### Han and Roshi (guardian-package research only)

- **Names:** Han; Roshi
- **Source candidate:** `muhammadadilsyaputra08-alt/NarutoSenki-Custom`, pinned commit `279e85e73040558c84988a0eea310b6286eb77f0`
- **Available lead:** each has a unit XML, sprite atlas plist, and texture under `Resources/Unit/Guardian/`; Han also has named audio events.
- **Current status:** RESOURCE_REVIEW — **not playable / not integrated**. The source uses a shared `HeroEnum::Guardian` class and has no dedicated Han/Roshi selectable hero class. Their visible roster does not include them. These must not be counted as new playable characters.
- **Next action:** trace how Guardian instances are spawned and named; determine whether their animation/actions can be adapted to the existing player-controlled Hero lifecycle; inspect required skill/effect/report/selection art; then implement and verify selection, controls, AI, skills, death/respawn, and resource cleanup before changing status.
- **Rights:** source repository and asset terms are not declared in the inspected metadata. Keep this as a research lead; do not vendor or redistribute its binary/art files until provenance and applicable permissions are resolved.

The source inventory remains **37 visible selectable names / 43 after six existing native forms are exposed by the CI patch**. Han and Roshi do not increase either count. Gameplay-verified playable count remains unmeasured.

### Additional source/license triage — 2026-10-10

- **Repository inspected:** `Fansirsqi/NarutoSenki` (default branch `main`). GitHub reports repository-level license metadata as **Mulan PSL v2** and the repository contains a `LICENSE` file.
- **Important scope limit:** the inspected tree is an APK-style extracted package (root includes `AndroidManifest.xml`, `META-INF/`, and bundled `assets/` audio), not an editable game source tree with character class implementations and integration tests. A repository license can cover contributors' software contributions; it does not by itself establish permission to reuse third-party Naruto character art, voices, music, or other franchise assets bundled in the package.
- **Decision:** research-only; do not copy its bundled media into Senki or count any character as integrated based on this repository. It is not currently a suitable source for a complete, auditable playable-character port.
- Other checked source repositories `LeaderOnePro/NarutoSenki`, `LeaderOnePro/NarutoSenki-cocos2dx`, `Zx-Akito/NarutoSenki-V2`, and `muhammadadilsyaputra08-alt/NarutoSenki-Custom` did not expose a repository license file or GitHub license metadata in the inspected default branches. Keep their source/assets blocked from import pending explicit permission or clearer licensing.
- Next research target remains a complete source implementation whose own license and asset provenance are explicit, or direct permission from the relevant rights holders/contributors. Do not treat public GitHub visibility as permission.

### Additional source comparison — 2026-10-10

- **`kuiyr0810/NarutoSenki-V2`** has a full source tree and the same 43-entry visible roster pattern in `projects/NarutoSenki/lua/class/basic.lua`; the inspected visible layout did not reveal a new distinct playable character beyond the current candidate. No repository license file or GitHub license metadata was found, so no code/assets were imported.
- **`likill/NarutoSenki-master`** and **`LeaderOnePro/NarutoSenki1.17Mod`** are additional public mod repositories; the inspected default branches expose no repository license metadata or top-level license file. Their presence is a research lead, not reuse permission.
- **`Zx-Akito/NarutoSenki-Release`** is a release-only repository with no source tree in the inspected default branch; it cannot serve as an auditable character-code integration source by itself.
- This comparison did not identify a new distinct character with both a complete compatible source package and clear reuse authorization. Roster count remains unchanged; do not fabricate progress by adding names without assets and working gameplay.

### Guardian lead cross-check — `likill/NarutoSenki-master` (2026-10-10)

- The inspected fork includes Han/Roshi unit animation XML, sprite atlases/textures, audio paths, and kill/death portrait frames. Its `GameLayer::initGard()` creates a generic `Hero`, assigns either `Roshi` or `Han` with role `Com`, sets the guardian spawn point, and calls `doAI()`; `Characters.cpp` routes both names to `AI_Guardian()`.
- Han/Roshi were not found in the fork's visible character-select layout or select-layer code search. This supports the current classification as **AI-spawned guardian units, not selectable player characters** in that source. It does not mean they could never be adapted; it means a player-controlled selection/lifecycle path would need to be implemented and tested.
- This repository has no license metadata/license file in the inspected default branch. Its Han/Roshi files are useful architectural research only; no code or assets were copied into Senki.


## Next integration batch decision — 2026-10-10

### Candidate screen
The v1.26 Beta 1 changelog publicly names Shizune, Hashirama, Rin, Sakon & Ukon, and Juzo as added characters; the later Beta 2 release is primarily a fix release. See https://github.com/Zx-Akito/NarutoSenki-Release/releases.

- Classification: DISCOVERED / REFERENCE_ONLY until editable source, exact per-character files, provenance, and reuse permission are verified.
- None of these five is counted as integrated, implemented, or playable in the selected V2 candidate based on release notes alone.
- The release host currently supplies packaged APK assets, not a source patch that can be applied to the selected V2 Lua/C++ project. Do not extract or transplant the APK to fabricate a character integration.
- Next eligible batch: inspect a source repository or obtain creator permission and a source/resource package for one character. Map its selection portrait/button, XML/atlas/texture, animation/effects/audio, native class/AI/skill definitions, and selection/skill/death UI references against the pinned V2 candidate before editing.
- Until that source/rights gate is cleared, keep the roster count at 43 declared selectable entries / 37 distinct base names in the current audited candidate, with runtime-verified playable count still unmeasured.


## External-mod candidates — do not count as integrated

- **Release-note leads:** Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Might Guy, Yamato, Zetsu, Iruka, Jirobo, Tayuya, and Anko are listed in [Zx-Akito/NarutoSenki-Release](https://github.com/Zx-Akito/NarutoSenki-Release/releases) changelogs. These are distinct external-mod candidates, but release notes alone do not supply editable implementation files.
- **Legacy resource lead:** [Fansirsqi/NarutoSenki](https://github.com/Fansirsqi/NarutoSenki) contains a Nagato animation XML/atlas and other unit resources, but its tree is package-style rather than a V2 source implementation. Nagato is a candidate for further compatibility analysis only; the inspected XML has a suspicious attackValue=6000000 field and must not be ported blindly.
- **Not a new addition:** Karin already exists in the pinned V2 roster. Do not count Karin from another resource pack as a new character.
- **Not playable characters by default:** Han/Roshi Guardian resources, Pain-path implementation classes, clones, and other summons do not satisfy the user's external playable-character priority unless a mod source explicitly implements them as independently selectable fighters.

Current external-mod additions integrated: **0**. Current external-mod additions verified playable: **0**. The next batch must target available slots on pages 1–3 before any page 4/5 expansion.


## External source comparison checkpoint — 2026-10-10

The latest external-source comparison found **no eligible new playable character package to port yet**:
- The v1.24–v1.26 release host provides changelog evidence for mod characters but its repository tree contains only a README, not editable character source.
- The inspected legacy Cocos2d-x source has a selectable roster matching the core cast and no independent selectable implementation for the external release-note candidates.
- The Wilykun V2 fork has no distinct selectable roster additions versus the pinned candidate.

Do not count these as integrations. Keep the target gap at 33 distinct base characters based on the current source-level roster inventory; verified-playable count remains unmeasured. The next milestone must identify an editable external character package and resolve code/art/audio permissions before porting it into pages 1–3.


## Active work checkpoint — external mod source comparison (2026-10-10)

**User priority reaffirmed:** do not spend character-expansion effort on V2-internal forms, summons, enum names, or roster recounting. Find independently implemented characters in other Naruto Senki mods and port them into the selected V2 build. Pages 1–3 remain the first target, with original image-button navigation preserved.

### Newly inspected external source lead: `Zx-Akito/NarutoSenki`
- Repository: https://github.com/Zx-Akito/NarutoSenki
- The README identifies it as a modified Naruto game and states that it is based on Cocos2d-x 2.2.2 / Visual Studio 2010. It exposes editable C++ files such as `Classes/Characters.cpp` and `Classes/SelectLayer.cpp`, unlike the release-only host.
- Its character AI routing includes character-specific implementations for entries such as `Asuma`, `Sai`, `Tenten`, `Suigetsu`, `Konan`, `Nagato`, and others. This is an actual source-code lead, but the old Cocos2d-x code and resource format are not yet confirmed compatible with the selected V2 Lua/C++ project.
- The initial comparison is a **candidate for deeper per-character diffing**, not proof that any of these names are new relative to V2, complete in all required UI/resource paths, or already integrated.
- No code or assets have been copied. Before a port, compare its actual selection roster, unit/skill/resource files, animation and audio references against the pinned V2 candidate; record each source revision and resolve reuse permission/provenance. If a distinct complete character is confirmed, adapt one character as a small isolated port to a page 1–3 slot and run the Android build/test loop.

### Current honest status
- External source lead with editable C++ character logic: **found**.
- New distinct character fully diffed and selected for port: **not yet confirmed**.
- External character integrated into central V2 candidate: **0**.
- External character verified playable: **0**.
- Do not describe this source lead as a completed character addition.


### Follow-up roster diff — external V2 fork check (2026-10-10)

- Compared the visible `projects/NarutoSenki/lua/class/basic.lua` roster across `Zx-Akito/NarutoSenki-V2`, `kuiyr0810/NarutoSenki-V2`, `SILXNTRAY/NarutoSenki-V2`, `hitlabmodv2/NarutoSenki-V2`, `BF667/NarutoSenki-V2`, `4399erbai/NarutoSenki-V2`, and the pinned `muhammadadilsyaputra08-alt/NarutoSenki-Custom` candidate.
- The inspected forks share the same core V2 visible roster pattern; none of those roster files surfaced the external release-note leads Shizune, Hashirama, Rin, Juzo, Jirobo, Tayuya, Anko, Yamato, Sasori, Zetsu, Iruka, or Kurenai. Do not treat another fork of the same roster as a source of new characters.
- `Zx-Akito/NarutoSenki` (older Cocos2d-x 2.2.2 source) has editable C++ character AI and a small selectable roster, but the inspected selectable names (Naruto, Sakura, Sai, Itachi, Konan, Deidara, Sasuke, Karin, Jugo) are already represented in the V2 roster. It is not yet a source for a distinct new selectable character.
- `LeaderOnePro/NarutoSenki1.17Mod` was confirmed by its root tree to be an APK/package extraction (`AndroidManifest.xml`, `classes.dex`, `assets/`, `res/`), not an editable source project; it cannot supply a source-level character port without relying on packaged binary extraction.
- Decision: no new character port is justified by these comparisons. Continue searching for an external Senki mod with an independently selectable character implementation and complete source/resource package. Current integrated external characters remain **0**; do not count internal V2 forms or support entities.


## New external-source audit checkpoint — 2026-10-10

Checked additional C++/V2 repositories and compared their actual selection code. `LeaderOnePro/NarutoSenki` and `LeaderOnePro/NarutoSenki-cocos2dx` have editable C++ but their inspected selectable lists contain only characters already in the V2 base. Their AI routing for support entities/forms is not counted as a new selectable fighter. `sansaks-jpg/NarutoSenki-V2` is a stock-roster fork. `likill/NarutoSenki-master` lacks the expected V2 Lua roster path. No new, permission-cleared, complete external character package was identified.

**Count remains unchanged:** external characters integrated **0**; external characters verified playable **0**. Release-note names remain candidates only until editable source/resources and reuse rights are confirmed. Do not fill character slots with placeholders and call them finished.

## Candidate rejection — likill legacy source — 2026-10-10

- Source: https://github.com/likill/NarutoSenki-master
- Inspected Network/Hardcore selection list: 35 non-empty names; all overlap the pinned V2 candidate's selectable roster. Training selection remains the original nine-name list.
- AI/resource-loader references include forms, support entities, and related assets; these are not counted as additional standalone characters.
- Rights: no declared source license or root LICENSE found in the checked tree; bundled art/audio permissions are unknown.
- Decision: **REFERENCE_ONLY / PERMISSION_REQUIRED**. No source/assets copied; no character added. This is a duplicate-roster lead, not an eligible port.

## User-requested priority candidates — 2026-10-10

These six are explicitly prioritized by the user for external-mod discovery and integration. Their inclusion here records the request, **not** a claim that they are implemented or playable. For each, inspect editable source and resource files; verify compatibility with the pinned V2-derived candidate; record code license separately from art/audio/voice rights; and only then start a complete native port. Prefer available page 1–3 slots without replacing existing characters.

### Kurenai Yūhi
- Unique character ID: `kurenai_yuhi`
- Display name: Kurenai
- Source repository/version: not yet qualified; search Senki mod source and release-history leads
- Source category: reference-only until editable source and provenance are verified
- Code license status: unresolved
- Asset/audio permission status: unresolved
- Required port scope: portrait/selection entry, sprites and animation, genjutsu-themed basic attack/skills/effects, available audio, AI/player controls, skill/profile display, kill/death UI
- Status: DISCOVERED / RIGHTS_REVIEW
- Next action: find a distinct, inspectable implementation and map all dependencies

### Might Guy
- Unique character ID: `might_guy`
- Display name: Might Guy
- Source repository/version: not yet qualified; search Senki mod source and release-history leads
- Source category: reference-only until editable source and provenance are verified
- Code license status: unresolved
- Asset/audio permission status: unresolved
- Required port scope: portrait/selection entry, sprites and animation, taijutsu combos and skill effects, Eight Gates/ultimate if present in the source, available audio, AI/player controls, skill/profile display, kill/death UI
- Status: DISCOVERED / RIGHTS_REVIEW
- Next action: find a distinct, inspectable implementation and map all dependencies

### Yamato
- Unique character ID: `yamato`
- Display name: Yamato
- Source repository/version: not yet qualified; search Senki mod source and release-history leads
- Source category: reference-only until editable source and provenance are verified
- Code license status: unresolved
- Asset/audio permission status: unresolved
- Required port scope: portrait/selection entry, sprites and animation, Wood Release attacks and effects, available audio, AI/player controls, skill/profile display, kill/death UI
- Status: DISCOVERED / RIGHTS_REVIEW
- Next action: find a distinct, inspectable implementation and map all dependencies

### Shizune
- Unique character ID: `shizune`
- Display name: Shizune
- Source repository/version: not yet qualified; search Senki mod source and release-history leads
- Source category: reference-only until editable source and provenance are verified
- Code license status: unresolved
- Asset/audio permission status: unresolved
- Required port scope: portrait/selection entry, sprites and animation, attacks/medical/poison techniques and effects, available audio, AI/player controls, skill/profile display, kill/death UI
- Status: DISCOVERED / RIGHTS_REVIEW
- Next action: find a distinct, inspectable implementation and map all dependencies

### Hashirama Senju
- Unique character ID: `hashirama_senju`
- Display name: Hashirama Senju
- Source repository/version: not yet qualified; search Senki mod source and release-history leads
- Source category: reference-only until editable source and provenance are verified
- Code license status: unresolved
- Asset/audio permission status: unresolved
- Required port scope: portrait/selection entry, sprites and animation, Wood Release techniques, large-scale effects/summons if present in the source, available audio, AI/player controls, skill/profile display, kill/death UI
- Status: DISCOVERED / RIGHTS_REVIEW
- Next action: find a distinct, inspectable implementation and map all dependencies

### Rin Nohara
- Unique character ID: `rin_nohara`
- Display name: Rin
- Source repository/version: not yet qualified; search Senki mod source and release-history leads
- Source category: reference-only until editable source and provenance are verified
- Code license status: unresolved
- Asset/audio permission status: unresolved
- Required port scope: portrait/selection entry, sprites and animation, attacks/skills/effects present in the source, available audio, AI/player controls, skill/profile display, kill/death UI
- Status: DISCOVERED / RIGHTS_REVIEW
- Next action: find a distinct, inspectable implementation and map all dependencies

**Completion rule:** do not change any of these statuses to IMPLEMENTED or VERIFIED based on a release-note mention, a name/portrait, an APK-only lead, or a passing build. Record exact files and test evidence after a real native integration.


## Sasori — initial CI integration candidate (2026-10-10)

- Unique character ID: `Sasori`
- Display name: Sasori
- Source repository/version: `LeaderOnePro/NarutoSenki1.17Mod`, commit `8c800efe09f8e5489f37ee3314596b329f533225`
- Tracked visual source files: `assets/Element/Saso/Saso.png`, `assets/Element/Saso/Saso.plist`, `assets/Element/Saso/Saso.xml`
- Integration: separate roster ID, HeroEnum entry, native Provider dispatch, converted V2-native action XML, Sasori atlas/frame mapping, audio paths, selection display-name alias, and skill UI alias.
- Source XML supplies unique idle/walk/hurt/death/basic-attack and skill01 animation data. skill02–skill05 have empty frame lists; native controller and skill-icon atlas remain Kankuro-compatible. This is not yet Sasori's complete unique move set.
- Build evidence: [Run #316 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38064802954); legacy-to-V2 XML conversion, frame/audio references, character audit, Lua checks, APK signature, and ABI packaging passed.
- Asset/code permissions: unresolved. The source tree is an APK/resource distribution and no asset-specific reuse grant was confirmed. Candidate APK is a private testing artifact only; do not publish or redistribute the copied Saso artwork/audio without permission.
- Runtime status: not tested in an actual match; phone installation not tested.
- Status: **IN_PROGRESS / CI_CHECKED / GAMEPLAY_UNVERIFIED / RIGHTS_REVIEW**
- Next: implement character-specific puppetry attacks, skill effects/cooldowns, and appropriate AI/player-control behavior; verify selection portrait, profile/skill view, kill/death identity, death/respawn, and repeated matches. Only then consider VERIFIED.
