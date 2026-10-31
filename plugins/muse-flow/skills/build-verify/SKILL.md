---
name: build-verify
description: Implement one approved task with red-green verification. Use when a plan-small task is approved for build.
---

# Build Verify

Implement one task at a time. No adjacent cleanup.

## Steps

1. Write a failing check that defines the task.
2. Show the failing output.
3. Write minimum code to pass.
4. Show the passing output.
5. Keep the diff surgical.

## Output

Tested diff with failing then passing evidence. One task per cycle.
