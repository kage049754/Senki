# Senki Persistent Progress Tracker

Last verified checkpoint: **2026-10-10**  
Repository: https://github.com/kage049754/Senki  
Mission: merge real external Naruto Senki mod characters into the existing V2 game. Do not create a new game.

## Current status

| Area | Verified state |
|---|---|
| V2-derived central CI candidate | Builds in GitHub Actions |
| Latest verified run | [#206 — SUCCESS](https://github.com/kage049754/Senki/actions/runs/38043294444) |
| Tested commit | [3c3f7f25818dce5c9b966e53a755fd50d74ca04c](https://github.com/kage049754/Senki/commit/3c3f7f25818dce5c9b966e53a755fd50d74ca04c) |
| Pagination / page-button checks | Passed in that CI run |
| External-mod characters integrated | **0** |
| External-mod characters verified playable | **0** |
| Goal of 70+ distinct playable characters | Not achieved |
| Physical-phone install/start/gameplay | **Not verified** |
| Full source vendored into this repo | Not complete; workflow uses a pinned external source checkout in temporary CI |
| Third-party source/asset permissions | Unresolved for inspected candidates |

## Latest successful build — Run #206

- Workflow: V2 Source Candidate Build (Private Testing Artifact).
- Run: https://github.com/kage049754/Senki/actions/runs/38043294444
- Commit: 3c3f7f25818dce5c9b966e53a755fd50d74ca04c
- Conclusion: **completed / success**.
- Fix: corrected an over-escaped numeric regular expression in the atlas parser used by the original page-button asset regression check, after run #205 failed.
- Verified scope: source assertions, Lua validation, character-package audit, Android candidate APK build, packaging/signature/native-library checks, and artifact upload.
- Candidate APK archive: naruto-senki-v2-candidate-debug-apk, artifact ID 11666950333, 83,338,578 bytes.
- Audit archive: senki-character-package-audit, artifact ID 11666955285, 4,336 bytes.
- Download artifacts from the [Actions run page](https://github.com/kage049754/Senki/actions/runs/38043294444). APK archive API URL: https://api.github.com/repos/kage049754/Senki/actions/artifacts/11666950333/zip
- This is a diagnostic/private-testing candidate, not a final release. The build does not contain a new external character and does not prove phone installation/gameplay.

## Latest failure and fix

- Failed run #205: https://github.com/kage049754/Senki/actions/runs/38043254054
- Cause: a newly added page-button atlas test parsed rectangle numbers incorrectly because of an over-escaped regular expression.
- Fix commit: 3c3f7f25818dce5c9b966e53a755fd50d74ca04c.
- Re-run #206 completed successfully. This demonstrates the required inspect → fix → rerun loop.

## External character status

No external character has been integrated. Release-note leads in [Zx-Akito/NarutoSenki-Release](https://github.com/Zx-Akito/NarutoSenki-Release/releases) include Shizune, Hashirama, Rin, Sakon & Ukon, Juzo, Kurenai, Might Guy, Yamato, Sasori, Zetsu, Iruka, Jirobo, Tayuya, and Anko. These are discovery leads, not source-level ports.

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
