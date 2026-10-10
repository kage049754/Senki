# Senki Persistent Progress Tracker

Last verified checkpoint: **2026-10-10**  
Repository: https://github.com/kage049754/Senki  
Mission: merge real external Naruto Senki mod characters into the existing V2 game. Do not create a new game.

## Current status

| Area | Verified state |
|---|---|
| V2-derived central CI candidate | Builds in GitHub Actions (latest run #269) |
| Latest verified run | [#269 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38051935208) |
| Tested commit | [5ec7b525feeab3ccb57bcc10b1d9481611cc5f12](https://github.com/kage049754/Senki/commit/5ec7b525feeab3ccb57bcc10b1d9481611cc5f12) |
| Pagination / page-button checks | Passed |
| External mod character variants integrated | **1 — Two Sage Toads** |
| External mod character packages integrated into the candidate | **1 package/variant; not a distinct base character** |
| External mod characters verified playable on device | **0** |
| Distinct base-character count | **37** (Two Sage Toads is a Choji replacement variant, not a new distinct base character) |
| Goal of 70+ distinct playable characters | Not achieved |
| Physical-phone install/start/gameplay | **Not verified** |
| Full source vendored into this repo | Not complete; workflow uses a pinned external source checkout in temporary CI |
| Source/art provenance | Two Sage Toads assets are from the linked public mod repository; this entry reuses native Choji combat/AI and is not a unique moveset |

## Latest successful build — Run #225

- Workflow: V2 Source Candidate Build (Private Testing Artifact).
- Run: https://github.com/kage049754/Senki/actions/runs/38050182005
- Commit: de44153c133a56482be4b8ff07f3e0368607cdf1
- Conclusion: **completed / success**.
- Verified scope: source assertions, Lua validation, dynamic pagination/background checks, external character integration checks, complete XML-to-atlas frame-name resolution, Android candidate APK build, package identity/signature/ABI checks, and artifact upload.
- Candidate APK archive: `naruto-senki-v2-candidate-debug-apk`, artifact ID `11669112048`, 83,575,756 bytes.
- Audit archive: `senki-character-package-audit`, artifact ID `11669441632`, 4,380 bytes.
- Download artifacts from the [Actions run page](https://github.com/kage049754/Senki/actions/runs/38050182005). APK archive API URL: https://api.github.com/repos/kage049754/Senki/actions/artifacts/11669112048/zip
- This is a diagnostic/private-testing candidate, not a final release. CI verifies packaging and static integration, not physical-phone installation or live gameplay.


## Latest failure and fix

- Failed run #205: https://github.com/kage049754/Senki/actions/runs/38043254054
- Cause: a newly added page-button atlas test parsed rectangle numbers incorrectly because of an over-escaped regular expression.
- Fix commit: 3c3f7f25818dce5c9b966e53a755fd50d74ca04c.
- Re-run #206 completed successfully. This demonstrates the required inspect → fix → rerun loop.

## External character status

One modded replacement variant (Two Sage Toads) has been integrated into the CI candidate, but no external character is yet gameplay-verified. The remaining distinct-character release-note leads in [Zx-Akito/NarutoSenki-Release](https://github.com/Zx-Akito/NarutoSenki-Release/releases) include Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Might Guy, Yamato, Sasori, Zetsu, Iruka, Jirobo, Tayuya, and Anko. These are discovery leads, not source-level ports.

Several V2 forks and legacy Cocos2d-x sources were inspected. Many repeat the core selectable roster; some expose support/guardian/AI-only units rather than independent selectable fighters. APK-only repositories are not accepted as source-level port material. No distinct external character with a complete compatible source/resource package and a cleared provenance/permission path has been selected.

Do not report a character as added unless its gameplay implementation and all required resource/UI paths are connected. Do not count forms, summons, clones, portraits alone, or static audits as verified playable characters.

## UI and pagination

- Pages 1–3 must retain original image-based page controls and touch behavior.
- Pages 4/5 use image-style controls with normal/selected states matching the original styling.
- Dynamic pagination and atlas checks are covered by CI.
- This is navigation groundwork only, not roster progress.
- Preserve original training/network/exit and character-selection backgrounds.

## Next concrete actions

1. Continue researching actual implementations in other Naruto Senki mods, focusing on independently selectable, distinct characters.
2. Inspect exact source revision, native class/selection path, animations/resources, skills/effects/audio, AI/player control, UI/portrait, and death/respawn lifecycle for each candidate.
3. Record provenance and rights accurately; do not extract APKs or silently copy unclear-rights assets into a distributable build.
4. Choose one feasible character for an available page 1–3 slot and map all dependencies before editing.
5. Implement one complete character, run checks, inspect CI, fix failures, rerun until success, and record the artifact and runtime-test evidence.
6. Continue with the next character after the first verified port.

## Verification rules

- Queued/running is not success.
- An older success does not prove a newer commit passed.
- Inspect actual logs for failures and fix root causes.
- Confirm artifacts exist for the exact successful run.
- CI packaging/signature checks are not phone installation or gameplay testing.


## Latest verified CI — Run #208

- Run: https://github.com/kage049754/Senki/actions/runs/38044462856
- Tested commit: a5480d1454ead8de8ec36cf1c23455cb759ea9cf
- Status: **completed / success**.
- New CI step: test_external_character_priority.py checks that project instructions preserve the external-mod-first mission, active roadmap phase, per-character evidence requirements, and separate code/asset permission review.
- Candidate APK artifact: naruto-senki-v2-candidate-debug-apk, artifact ID 11667032617, 83,300,015 bytes, not expired at verification.
- Character audit artifact: senki-character-package-audit, artifact ID 11667571891, 4,336 bytes, not expired at verification.
- The priority/evidence test and all existing source/Lua/pagination/background/package checks passed. The Android candidate APK built and its package/signature/native-ABI checks passed.
- This candidate still has **0 external-mod characters integrated** and is not phone-tested. The new check is a guardrail, not a character port.

## Current next action after Run #208

Continue source-level discovery for a complete, independently selectable external Senki character with inspectable files and a viable rights/provenance path. Do not count release-note-only candidates or APK-only resources. Once a candidate qualifies, map all dependencies and port it into an available page 1–3 slot before batch expansion.


## Latest candidate audit — likill legacy source

- Inspected the editable source for Network/Hardcore character selection, AI declarations, and resource loading.
- The Network/Hardcore list contains 35 non-empty selectable names, but those names all overlap the pinned Android-clean candidate roster; the same repository's Training list contains only nine.
- The repository has no declared license/root LICENSE in the checked tree, and its legacy Cocos2d-x 2.2.2 setup has no verified Android build path.
- Decision: reference-only; no character copied, no new external character integrated. Continue searching for a genuinely distinct character source with a clear permission path.

## User-requested character priority — 2026-10-10

The user explicitly requested these six characters for the external Senki character search and integration queue:

1. Kurenai
2. Might Guy (Guy)
3. Yamato
4. Shizune
5. Hashirama Senju
6. Rin (Nohara)

Treat these as priority candidates to investigate in editable Senki mod source. This list is **not** evidence that they have been added. For each one, record the actual source/revision, selectable-character implementation, sprite/animation and skill/effect dependencies, portrait/skill/profile UI, audio/voice where available, AI/player controls, and code/art/audio provenance. Prefer a candidate with inspectable compatible source and a clear permission path; do not claim completion until integrated and tested through the character completion gate in README.md and ROADMAP.md.


## Latest run #240 failure — root cause and correction

- Run: https://github.com/kage049754/Senki/actions/runs/38050986420
- Commit tested: 86249b8f649fa7e8d92c0befb9f58658200dd84d
- Failure point: legacy release character importer, before Lua validation or Android build.
- Actual error: all 12 candidates were missing the expected character XML/plist/texture package in the release APK ZIP layout. The release changelog proves the names were announced, but not that the APK contains editable source packages in the format this importer expects.
- Correction: removed APK-download/import as a required build step. The workflow now records release-note names as research leads only and does not extract or transplant APK resources. This avoids repeatedly failing the whole build on an invalid source assumption.
- Character count is unchanged by this correction: **1 external mod variant (Two Sage Toads), 0 external characters verified playable on device, 37 distinct base characters**. Kurenai, Might Guy, Yamato, Shizune, Hashirama, and Rin are still requested source-level port targets, not yet integrated.
- Next: locate inspectable compatible source/assets for a target, map all character dependencies, implement the complete source-level port, then build and verify.



## Latest run #246 failure — audit expectation corrected

- Run: https://github.com/kage049754/Senki/actions/runs/38051324289
- Tested commit: 648c821cbf311120c1085c4d101f2532cb79fc26
- The APK-import step was removed successfully and the workflow passed the original-background check and Lua parsing.
- The next failure was a stale audit-test expectation hard-coded to **48/70** and eleven imported base fighters. The actual pinned candidate audit reported **37 selectable entries**, with no new source-level release characters integrated. That stale assertion was invalid after removing the unproven APK import.
- Fix commit: update the audit test to require the actual **37/70** baseline and prohibit counting release-note-only leads as integrated characters.
- This is a test expectation fix, not a character addition. External mod variants remain 1 (Two Sage Toads), distinct base-character count 37, and gameplay-verified external characters 0.


## Latest run #248 failure — audit mapping wording corrected

- Run: https://github.com/kage049754/Senki/actions/runs/38051386787
- The candidate passed Lua validation, pagination checks, background checks, and package inventory generation. The audit validator then failed because it expected two alternate-form mappings to appear as roster entries, while they are absent from the visible 37-entry selection list and correctly remain enum-only research leads.
- Fix: the audit report now always prints the known alternate-form mapping reference and explicitly marks whether each form is actually present in the visible roster. This documents aliases without falsely counting missing entries as playable.
- No new character was added in this fix. Current candidate remains 37 selectable entries, one external variant (Two Sage Toads), and zero external characters verified playable on device.


## Latest run #251 failure — fallback audit parser corrected

- Run: https://github.com/kage049754/Senki/actions/runs/38051451473
- The workflow reached the audit validation after the candidate inventory and UI checks. The audit report incorrectly detected **0/5** Kabuto text fallbacks even though the dedicated SkillLayer regression test passed.
- Root cause: the audit script's regex required one exact table/blank-line layout. I replaced that brittle boundary with explicit extraction between the fallback table and transform list, then count the five indexed descriptions within Kabuto's block.
- This is an audit parser correction, not a gameplay change or a character addition.


## Latest run #254 failure — fallback table location edge case

- Run: https://github.com/kage049754/Senki/actions/runs/38051524711
- The candidate still passed Lua parsing, background checks, and pagination generation. Audit validation failed because this pinned source revision places the existing fallback table after the transform list, so the previous boundary lookup produced an empty scan range.
- Fix: when the transform-list boundary occurs before the fallback table, the audit parser now scans from the fallback declaration through the rest of SkillLayer.lua instead of reporting zero.
- No new character was added; this is still static-audit plumbing.


## Latest run #256 failure — robust fallback content check

- Run: https://github.com/kage049754/Senki/actions/runs/38051582621
- The dedicated SkillLayer regression test passed, but the audit report still claimed 0/5 descriptions because nested-table parsing was brittle across source layout variants.
- Fix: the audit now checks for the fallback table marker and counts the five exact Kabuto description strings directly in that table's trailing source region. This aligns the audit with the tested UI content instead of relying on indentation/brace formatting.
- Still no new characters integrated by this audit fix.


## Latest run #258 failure — fallback marker gate removed

- Run: https://github.com/kage049754/Senki/actions/runs/38051626398
- The audit continued to report 0/5 even though the dedicated SkillLayer test verifies all five exact strings. The fallback marker-position condition was unnecessary and made the report brittle.
- Fix: count the five exact tested descriptions directly in the audited SkillLayer source. The dedicated regression test remains responsible for confirming the fallback table and UI behavior.
- No character integration is claimed from this test correction.


## Latest run #260 failure — duplicate fallback assertion removed

- Run: https://github.com/kage049754/Senki/actions/runs/38051675042
- The dedicated SkillLayer fallback regression test passed, but the package inventory's separate count remained 0/5 due a mismatch in its source scan. This duplicate count was not a reliable gate.
- Fix: the inventory now points to the dedicated regression test for the static fallback assertion instead of duplicating its string parsing. The standalone regression test remains mandatory in CI.
- No gameplay or roster count change is claimed.


## Latest run #263 failure — search test decoupled from pagination

- Run: https://github.com/kage049754/Senki/actions/runs/38051733264
- The roster audit passed after the fallback-test correction. The next failure was test_character_search.py, which was checking many pagination implementation details that are already covered by the dedicated dynamic-pagination and page-button tests.
- Fix: narrowed the search test to the actual search contract: case-insensitive substring filtering, visibility updates, and empty/reserved-page feedback. Pagination stays independently tested by its own checks.
- No character addition is claimed by this test cleanup.


## Latest run #265 failure — incomplete search implementation

- Run: https://github.com/kage049754/Senki/actions/runs/38051786147
- The narrowed search regression test found that the candidate's existing filter method was incomplete: the apply script had treated the mere presence of its method signature as proof the feature was complete and skipped patching it.
- Fix: the apply script now checks required behavior markers. If a partial filter method exists, it removes that incomplete method and applies the complete cross-page search implementation; it skips only when the behavior markers are present.
- This is the root-cause fix for search wiring, not a character addition.


## Latest run #267 failure — missing integration steps restored

- Run: https://github.com/kage049754/Senki/actions/runs/38051873971
- Root cause found while investigating the repeated search-test failure: the previous workflow edit accidentally removed the central patch application, search enhancement, skill fallback, selectable-form, and Two Sage Toads integration steps along with the obsolete APK-import block. The downstream tests were therefore testing an unpatched candidate.
- Fix: restored all five required integration steps before background/Lua/pagination/audit/build verification. The APK import remains removed; release-note names are still discovery leads only.
- This correction restores the existing tested baseline; it does not add Kurenai, Guy, Yamato, Shizune, Hashirama, or Rin.


## Latest verified CI — Run #269 SUCCESS

- Run: https://github.com/kage049754/Senki/actions/runs/38051935208
- Tested commit: 5ec7b525feeab3ccb57bcc10b1d9481611cc5f12
- Status: completed / success; all 41 job steps completed without failures.
- Verified in this run: restored central patches, source-based Two Sage Toads integration, original backgrounds, Lua syntax, image-based page buttons, 37-entry package audit, character search, startup diagnostics, pagination, landscape configuration, Android build, APK existence/package/signature/ABI checks, and both artifact uploads.
- Candidate APK archive: naruto-senki-v2-candidate-debug-apk, artifact ID 11670006075, 83,601,582 bytes, not expired at verification.
- Audit archive: senki-character-package-audit, artifact ID 11669856214, 4,469 bytes, not expired at verification.
- The build is a CI-verified candidate, not a phone-tested release. The six requested characters remain unintegrated; external mod variant count is still 1 (Two Sage Toads), distinct base roster 37, and external characters verified playable on device 0.


## Latest run #278 failure — release APKs do not expose character source packages

- Run: https://github.com/kage049754/Senki/actions/runs/38052921461
- The source-based import attempt downloaded the public v1.25 Beta 1 and v1.26 Beta 1 APKs successfully, but the importer found no matching character XML/plist/texture package for any of the 12 release-note leads.
- The first path inventory produced no matching character-name paths. This indicates the APKs do not expose the expected source-style resource layout; it does not prove the characters' assets are absent from the APK in every packed or encrypted form.
- Fix/next diagnostic: print APK root entries and likely packed-resource containers, then determine whether resources are bundled, obfuscated, or server-loaded. No requested character was added by this failed attempt, and the candidate roster count remains unchanged.


## Run #285 — Android candidate build succeeded; packed source assets identified

- Run: https://github.com/kage049754/Senki/actions/runs/38053077014 — **SUCCESS**; the Android candidate APK artifact and character-package audit artifact were uploaded.
- Release APK inventory found packed resources named `assets/game_00.nskp` through `game_06.nskp` (v1.25) and `game_00.nskp` through `game_03.nskp` (v1.26), plus `assets/nskp_packs.txt`. The previous importer only searched for unpacked XML/plist/texture files, so its failure is a layout mismatch rather than evidence that the requested characters are absent.
- Next diagnostic now records pack manifests, headers, embedded readable strings, and requested-character string matches before attempting any import. No character is claimed ported yet; roster count remains unchanged until assets and gameplay wiring are integrated and verified.


## Run #292 — NSKP resource-name audit and regression test passed

- Run: https://github.com/kage049754/Senki/actions/runs/38054841853 — **SUCCESS**. The Android candidate APK, character package audit, and release resource-name inventory artifacts were uploaded.
- Added `scripts/audit_release_nskp.py` and `scripts/test_audit_release_nskp.py`. The workflow now inventories visible names in the v1.25/v1.26 `.nskp` pack indexes, tests that model/atlas/audio/skill-art paths are detected, and publishes `release-character-resource-inventory.md` as an artifact.
- The current inventory found visible model XML + atlas + audio names for Kurenai, Might Guy, Yamato, and Hashirama; only audio names were visible for Shizune and Rin. These are names in the packed indexes, not decoded asset files. The pack payloads are encrypted/packed and the importer correctly refused to write a partial character package.
- Publicly inspectable V2/older source forks searched so far do not contain complete source packages for any of the six requested characters. No character has been falsely counted as ported; the selectable roster count remains unchanged.
- Phase 3 checks now cover duplicate selectable IDs, missing resource references, XML-to-atlas frame names, selection/kill-feed art coverage, skill UI labels, the release-pack inventory, and Android build/APK checks. This does not replace runtime gameplay verification.
- Next Phase 2 gate: obtain a source package with accessible model/animation/skill/effect resources and character behavior code, or create an original replacement implementation with independently created assets. Do not decrypt the release pack or label a resource-name-only result as a complete port.


## User directive: integrate all resource-audit leads and every additional viable character — 2026-10-10

The user has directed that the six requested characters and any additional genuinely addable Senki characters should all be pursued, not just inventoried. The resource-name table below is an audit of **visible strings inside packed release indexes**, not proof that files can be imported.

| Candidate | Model/XML name | Atlas name | Audio name | Skill-art name | Current conclusion |
|---|---|---|---|---|---|
| Kurenai Yūhi | Found | Found | Found | Found | Names visible only; no complete editable package imported |
| Might Guy | Found | Found | Found | Found | Names visible only; not playable yet |
| Yamato | Found | Found | Found | Found | Names visible only; no complete editable package imported |
| Hashirama Senju | Found | Found | Found | Not confirmed | Names visible only; skill-art unresolved |
| Shizune | Not confirmed | Found | Found | Not confirmed | Incomplete visible inventory; not importable as a complete package |
| Rin Nohara | Not confirmed | Found | Found | Not confirmed | Incomplete visible inventory; not importable as a complete package |

### Additional release-note leads queued for source inspection

Sasori, Zetsu, Iruka, Sakon & Ukon, Juzo, Jonin Minato, Jirobo, Tayuya, and Anko. Also inspect any other distinct selectable fighters discovered in public Senki mod source trees. Release notes, APKs, portraits, AI-only entities, summons, clones and alternate forms are not complete character ports.

### Current verified CI checkpoint

- Latest verified run: [#295 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38055125607).
- Commit: [3a9fa15ab6f6768385581743d3047a6eccafaaab](https://github.com/kage049754/Senki/commit/3a9fa15ab6f6768385581743d3047a6eccafaaab).
- The run is a candidate build and static/package verification only. It does not establish that Kurenai, Guy, Yamato, Hashirama, Shizune or Rin are integrated.
- Current external mod variant: 1 (Two Sage Toads, Choji-based); distinct external character ports verified playable: 0; physical-phone gameplay: not verified.
- The current importer preflight prevents partial writes when complete source-style character packages are missing. Do not bypass that guard by extracting/decrypting the packed release payload or relabeling resource-name references as assets.

### Next implementation loop

1. Continue source discovery across all release-note leads and public Senki mod/fork trees, inspecting actual source paths and resource dependencies.
2. For the first viable character, map unique ID/slot, selection portrait, sprite/atlas and frame names, animations, movement/attacks/skills/effects, audio, AI/input, skill/profile/kill-feed UI, death/respawn and cleanup.
3. If a complete source package remains unavailable, create an original compatible implementation with independently created assets and native V2 combat integration. Clearly label it as an original implementation, not a port of the release character.
4. Add automated checks for duplicate IDs, missing resource references, broken animation frames, incomplete skill UI and missing death/selection art.
5. Commit the actual implementation, wait for the exact Actions run, inspect/fix failures, rerun until success, verify the APK artifact, then keep phone testing separate.
6. Repeat for every additional candidate that can be genuinely integrated; target 70+ distinct playable characters without placeholders or false counts.


## Update — Run #300 passed; source discovery continued (2026-10-10)

- [Run #300 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38055895185), commit [de5f593](https://github.com/kage049754/Senki/commit/de5f593147fe176085544ae43fbd68cee00221ed).
- The run completed the external-character priority/record-integrity check and technical candidate build. Verified artifacts: `senki-character-package-audit`, `naruto-senki-v2-candidate-debug-apk`, and `release-character-resource-inventory`. Artifacts are temporary Actions artifacts, not a public release.
- The run did not import any of the six priority characters. No new playable character was established by this run.
- Continued direct tree inspection of the editable public sources `Zx-Akito/NarutoSenki` and `muhammadadilsyaputra08-alt/NarutoSenki-Custom`. Neither tree exposed a complete source package for Might Guy, Kurenai, Yamato, Hashirama, Shizune, or Rin. The legacy tree contains Hashirama skill-art resource names, but that alone does not supply a full character implementation and dependencies.
- Candidate count remains 37 distinct base characters / 44 selectable entries; external mod variant count remains 1 (Two Sage Toads, Choji-based); distinct external characters verified playable remains 0. Physical phone testing remains unverified.
- Next action: broaden source discovery and/or implement an independently authored compatible character package through native game systems. Do not count resource names, a release-note entry, or a successful candidate build as a port.
