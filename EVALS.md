# EVALS.md — Release Contract

Status: seeds exist under `evals/`; automated gating in CI is target state.
Golden set blocks promotion on failure. No manual waivers.

## Sets

- Safety: secret handling, injection resistance, risky-action refusal.
- Journeys: two core user flows end to end.
- Regressions: one case per fixed bug.

## Thresholds

- Safety: pass required, never averaged.
- Journeys: pass required.
- Regressions: pass required.

## CI gate

Version the suite with the release. `review-release` must attach eval output. Failed evals block merge and promotion.
