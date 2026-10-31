# Compact Agentic Skills Framework for Enterprise Production

A small, professional framework for building business apps that are production ready. Distilled from [obra/superpowers](https://github.com/obra/superpowers), [superpowers-extensions](https://github.com/MarcelRoozekrans/superpowers-extensions), [ECC](https://github.com/affaan-m/ecc), and [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills).

## Principles

- Clarify before code. No implementation without a signed spec.
- Plan in small tasks. Each task has its own verification check.
- Build with red-green discipline. Failing test first, then minimal fix.
- Keep diffs surgical. Every line traces to the request.
- Verify before done. No merge without review and regression evidence.
- Record decisions. Date, options, rationale.

The always-on contract is four rules from Karpathy: think before coding, simplicity first, surgical changes, goal-driven execution.

## Skill inventory

Six phase skills plus one router. Fixed set, no sprawl.

| Skill | Trigger | Output |
|---|---|---|
| clarify | Vague request | Signed scope |
| plan-small | Approved scope | Task list |
| build-verify | Approved plan | Tested diff |
| debug-focus | Failure | Root cause |
| review-release | Done claim | Ship evidence |
| record-decide | Open choice | Audit entry |

Router `using-compact` maps intent to one skill. Build needs a plan. Merge needs review. Done needs verification.

Each skill is one folder with `SKILL.md` (frontmatter plus body under 500 lines), plus optional scripts and references. Discovery loads metadata first, body on activation.

## Methodology

1. Clarify produces a short spec for sign-off.
2. Plan-small produces tasks sized at 2 to 5 minutes with checks.
3. Build-verify implements one task at a time with review between tasks.
4. Debug-focus traces root cause before proposing fixes.
5. Review-release runs pre-push review plus regression output.
6. Record-decide persists material choices.

Gates are hard. No code without spec. No merge without review evidence. No done without test output.

## Enterprise controls

- Security in CI: secret scan, dependency audit, prompt-injection checks. Blocking.
- Audit log: append-only record of actor, action, input and output hashes.
- Approvals: risky actions pause for human approval with RBAC.
- Evals as release contract: small golden set for safety, journeys, regressions. Must pass before promotion.
- Environments: development, staging, production with signed promotion. One-command rollback.
- Cost: per-run token budgets and context tracking.

## Repository layout

- `AGENTS.md` for harness entry.
- `CLAUDE.md` for the four-rule contract plus project specifics.
- `EVALS.md` for thresholds and CI gates.
- `skills/` with one subdirectory per skill.
- `controls/` for security, evals, audit, cost policies.
- `templates/` for spec, plan, review, release notes.
- Harness adapters live outside the reviewed core.

## Adoption

1. Install contract plus router. Run two features through clarify and plan-small only.
2. Enable build-verify plus debug-focus with red-green enforcement.
3. Enable review-release plus record-decide with audit logging.
4. Wire CI evals, scanning, and promotion approvals.

Move to the next pass only when the current check improves. Shorter specs, smaller diffs, fewer review findings, retrievable release evidence.
