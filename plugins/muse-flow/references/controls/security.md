# Security

Status: partially enforced. Secret scanning runs in CI on every push
(`review-release` script). Dependency audit and prompt-injection hierarchy
checks are target state: this repo has no dependencies and no injection
harness yet.

Blocking checks on every change.

- Secret scanning (enforced in CI).
- Dependency audit (target).
- Prompt-injection hierarchy checks (target).

Failures block merge. The coding agent never self-approves a risky action.
