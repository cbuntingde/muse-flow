# Example session

A short transcript showing the router and gates in action. Skill bodies live
under `plugins/muse-flow/skills/`; `using-compact` routes, the others do one
job each.

## 1. Vague request routes to clarify

> user: speed up the test run
>
> assistant (skill: clarify): What is slow about it — full-suite wall time,
> one file, or flaky reruns? I will spec the winner before touching code.

No code is written in this phase.

## 2. Approved scope becomes tasks

> user: full-suite wall time. Spec approved.
>
> assistant (skill: plan-small):
> 1. Time the suite per file and post the table. Check: slowest file named.
> 2. Split the slowest file. Check: suite passes, total time down.
> 3. ...implementation starts only after you approve this list.

## 3. Build with verification

> user: approved.
>
> assistant (skill: build-verify): Failing check first, minimum diff second,
> passing output attached. One task per cycle, no adjacent cleanup.

## 4. Done claims need evidence

> user: done, ready to merge.
>
> assistant (skill: review-release):
> - Diff traces to the request.
> - `python plugins/muse-flow/skills/review-release/scripts/check-evidence.py --test-log ... --regression-log ...` passes.
> - `python plugins/muse-flow/skills/review-release/scripts/secret-scan.py` over changed files passes.
> - Approval or required changes recorded.

Merge only on pass.
