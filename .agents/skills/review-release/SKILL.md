---
name: review-release
description: Run pre-push review with regression evidence before merge. Use when work claims to be done.
---

# Review Release

No merge without evidence.

## Steps

1. Check the diff is surgical and traced to the request.
2. Run the relevant tests and attach output.
3. Run regression checks for touched areas.
4. Record approval or required changes.

## Output

Review checklist plus test and regression logs. Merge only on pass.
