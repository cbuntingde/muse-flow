# Regression evals

One case per fixed bug. Must pass.

## R1 — Skill-tree drift

Bug: `.agents/skills` copies fell behind `plugins/muse-flow/skills`
(3 of 7 files differed, 3 gate scripts missing from the working copy).
Fix: `plugins/muse-flow/skills` is the source of truth;
`python scripts/sync-skills.py` mirrors it.
Regression check: `python scripts/sync-skills.py --check` in CI.
