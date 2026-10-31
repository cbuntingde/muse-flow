# Release

Status: target state. No environments, promotion signing, RBAC, or rollback
automation exist yet.

Explicit environments with signed promotion.

- Development, staging with production-like data controls, production.
- Promotion requires passing evals plus `review-release` evidence.
- Risky actions need human approval with RBAC.
- One-command rollback with one owner.
- Per-run token budgets and context tracking.
