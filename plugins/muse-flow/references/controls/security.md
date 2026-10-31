# Safe handling

State: in part live. The hidden key check runs on its own on each shared change
(through the `review-release` helper). Checks of outside parts and tricky message
handling are planned: this project has no outside parts and no message test bench yet.

Checks that must pass on each change.

- Hidden key check (live on its own).
- Outside parts check (planned).
- Tricky message check (planned).

Failed checks stop sharing. The helper never signs off its own risky step.
