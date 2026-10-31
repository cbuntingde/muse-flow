# Audit

Append-only log for side-effecting tool calls.

Record actor, action, input hash, and output hash per call. `record-decide` owns decision entries. `review-release` owns review evidence. Logs are retrievable without asking the agent.
