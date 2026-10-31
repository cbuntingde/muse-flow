# Decisions

## 2026-10-30 — plugins/muse-flow/skills is the source of truth
- Options: plugin wins vs .agents wins vs manual sync
- Rationale: Plugin copies were newer in all 3 drifted files and included scripts missing from .agents; sync script mirrors plugin to .agents plus controls and EVALS into bundle references
- Owner: cbuntingde

## 2026-10-30 — MIT license, copyright cbuntingde
- Options: MIT vs Apache-2.0 vs none
- Rationale: Public repo with install instructions needs a license for adoption; MIT is the permissive default, holder is the repo owner
- Owner: cbuntingde
