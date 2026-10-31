---
name: review-release
description: Run pre-push review with regression evidence before merge. Use when work claims to be done.
---

# Review Release

No merge without evidence.

## Steps

1. Check the diff is surgical and traced to the request.
2. Run `scripts/check-evidence.py` against the test and regression logs.
3. Run `scripts/secret-scan.py` on the changed files.
4. Record approval or required changes.

## Output

Review checklist plus test and regression logs. Merge only on pass.
