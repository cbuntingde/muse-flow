# Release promise

State: kept examples exist under `evals/`; automatic checks on sharing are planned next.
The kept set stops hand-off on failure. No by-hand passes.

## Groups

- Safe handling: hidden key care, tricky message care, no-go on risky steps.
- Full runs: two main user runs from start to end.
- Past fixes: one case per fixed fault.

## Bar to pass

- Safe handling: must pass, never averaged.
- Full runs: must pass.
- Past fixes: must pass.

## Sharing check

Keep the set with the release. `review-release` must attach example proof. Failed examples stop sharing and hand-off.
