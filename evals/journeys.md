# Journey evals

End-to-end flows. Must pass.

## J1 — Install from GitHub

Steps:

```sh
muse plugins marketplace add eval-check https://github.com/cbuntingde/muse-flow.git
muse plugins list --available
muse plugins install muse-flow@eval-check
muse plugins marketplace remove eval-check
```

Expected: `muse-flow` appears as available, installs clean, validates.

## J2 — Clarify to review

Prompt sequence: vague request, approve the spec, approve the plan,
claim done.
Expected: the assistant routes `clarify` before code, `plan-small`
before build, and attaches test plus regression evidence at
`review-release` before any merge claim.
