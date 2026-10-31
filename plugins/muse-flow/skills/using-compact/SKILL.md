---
name: using-compact
description: Router for the compact framework. Load at session start, map intent to one phase skill, enforce hard gates.
---

# Using Compact

Load this file at session start and after compaction.

## Intent map

- Vague request or new idea -> `clarify`.
- Approved scope, no task list -> `plan-small`.
- Approved plan, build asked -> `build-verify`.
- Bug, test failure, unexpected behavior -> `debug-focus`.
- Claim of done, branch ready -> `review-release`.
- Material trade-off or open choice -> `record-decide`.

## Hard gates

- Build requires an approved plan.
- Merge requires review evidence.
- Done requires verification output.

If the required artifact is missing, route back to the skill that produces it. Do not skip forward.
