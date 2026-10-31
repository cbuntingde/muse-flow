# muse-flow

Compact agentic skills framework for enterprise production: a router plus six phase skills with review gates and decision records. Installable as a Muse plugin.

## Requirements

- Muse Code CLI by Meta on your `PATH` (`muse --help` works).
- For GitHub installs: network access to `github.com`.

## Install

### Option A — from GitHub (recommended)

Register the repo as a marketplace once, then install the plugin:

```sh
muse plugins marketplace add muse-flow https://github.com/cbuntingde/muse-flow.git
muse plugins install muse-flow@muse-flow
```

### Option B — from a cloned checkout

```sh
git clone https://github.com/cbuntingde/muse-flow.git
cd muse-flow
muse plugins validate plugins/muse-flow
muse plugins install plugins/muse-flow
```

## Verify

```sh
muse plugins list --available   # muse-flow should be listed
muse plugins list               # muse-flow should be installed and enabled
muse skills list --source plugin
```

`validate` must report `"valid": true` before installing. If the marketplace
stops seeing the plugin after an update, refresh it with:

```sh
muse plugins marketplace update muse-flow
muse plugins update muse-flow
```

To remove:

```sh
muse plugins remove muse-flow
```

## What you get

| Skill | Trigger | Output |
|---|---|---|
| `using-compact` | Every session (router) | Maps intent to one phase skill |
| `clarify` | Vague request | Short signed spec |
| `plan-small` | Approved scope, no task list | Numbered tasks with checks |
| `build-verify` | Approved plan | Tested diff |
| `debug-focus` | Bug or test failure | Root cause before fixes |
| `review-release` | Claim of done | Pre-push review evidence |
| `record-decide` | Open trade-off | Dated decision entry |

Hard gates: no build without an approved plan, no merge without review
evidence, no done without verification output.

## Layout

- `plugins/muse-flow/` — the installable plugin bundle
  (`.muse-plugin/plugin.json` + `skills/`).
- `.claude-plugin/marketplace.json` — marketplace catalog that exposes the
  plugin when this repo is registered as a marketplace.
- `.agents/skills/` — working copy of the same skills for this checkout.
- `AGENTS.md` — harness entry point and always-on contract.
- `controls/` — security, release, and audit policies.
- `EVALS.md` — release contract: safety, journey, and regression thresholds.
- `compact-agentic-skills-framework-plan.md` — framework design notes.
