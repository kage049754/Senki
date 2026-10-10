# Senki Persistent Progress Tracker

Last verified checkpoint: **2026-10-10**  
Repository: https://github.com/kage049754/Senki  
Mission: merge real external Naruto Senki mod characters into the existing V2 game. Do not create a new game.

## Current status

| Area | Verified state |
|---|---|
| V2-derived central CI candidate | Builds in GitHub Actions |
| Latest verified run | [#225 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38050182005) |
| Tested commit | [de44153c133a56482be4b8ff07f3e0368607cdf1](https://github.com/kage049754/Senki/commit/de44153c133a56482be4b8ff07f3e0368607cdf1) |
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
