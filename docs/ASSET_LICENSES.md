# Code, Asset, and Permission Register

## Rule
A public repository or downloadable APK is not automatically permission to reuse or redistribute its contents. Evaluate source-code licensing and artwork/audio/animation licensing separately.

## Status definitions
- UNREVIEWED
- REVIEWED
- APPROVED
- PERMISSION_REQUIRED
- REFERENCE_ONLY
- EXCLUDED

## Naruto Senki V2 source candidate — Zx-Akito/NarutoSenki-V2
- Canonical URL: https://github.com/Zx-Akito/NarutoSenki-V2
- Material: C++/Lua game source, Cocos2d-x engine/dependencies, Android project, game resources and bundled assets
- Verified source structure: includes projects/NarutoSenki/proj.android-studio and source/resource directories described in the repository documentation.
- Repository metadata: public fork; parent listed as real-re/NarutoSenki-V2-old, which is private in the returned metadata.
- Code license: no root LICENSE found; GitHub metadata reports no declared license.
- Asset-specific license: not verified.
- Attribution requirements: unknown for game code/assets; third-party engine components may have separate notices.
- Modification/redistribution permission: not established.
- Permission evidence: none identified during the 2026-10-10 audit.
- Approved scope: reference/audit only; do not copy source/assets into this central repo or package them in a build until permission is established.
- Status: **PERMISSION_REQUIRED**
- Review date: 2026-10-10
- Notes: the source appears technically suitable for deeper build investigation, but public availability is not a license. The selected v2.1.6-fix APK is a separate binary release reference and is not source.

## Source review template
- Source/repository or creator:
- Canonical URL:
- Material type: source code / sprites / animation / sound / music / fonts / documentation / other
- Exact files or commit:
- Code license:
- Asset-specific license:
- Attribution required:
- Modification permitted:
- Redistribution permitted:
- Commercial use permitted:
- Permission evidence:
- Approved scope:
- Status:
- Reviewer/date:
- Notes:

## Rules
- Never strip copyright or attribution notices.
- Do not redistribute extracted APK contents without authorization.
- Do not assume an open-source code license covers art, music, or other third-party assets.
- If permission is unclear, mark the source REFERENCE_ONLY or PERMISSION_REQUIRED and do not package it in the APK.
- Use original or appropriately licensed replacements where necessary.
- Keep provenance linked to every imported character, skill, animation, portrait, and sound.
- Recheck licenses of forks and bundled third-party dependencies.
- A character must not be marked VERIFIED for release if required asset permissions remain unresolved.

## Initial status
No external source is approved for copying solely by virtue of appearing in the research inventory. Review each candidate and each asset set before integration.
