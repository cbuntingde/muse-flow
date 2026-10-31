# muse-flow

Small work guide that moves a request through clear steps with checks before release. It can be added to Muse and Claude Code. Current set is 0.1.0.

Some checks run on their own today. Signed release steps and full record-keeping are planned next. The policy pages below state what is live and what is planned.

## What you need before you start

- The Muse program on your computer (`muse --help` shows it is ready), and/or
  the Claude Code program (`claude --help` shows it is ready).
- Web access to `github.com` for installs from the web.

## Add it

### Option A — from the web (suggested)

Add this project to your shared list once, then add the work guide:

```sh
muse plugins marketplace add muse-flow https://github.com/cbuntingde/muse-flow.git
muse plugins install muse-flow@muse-flow
```

### Option B — from a saved copy

```sh
git clone https://github.com/cbuntingde/muse-flow.git
cd muse-flow
muse plugins validate plugins/muse-flow
muse plugins install plugins/muse-flow
```

## Confirm it works

Run these to confirm the guide is listed, added, and turned on:

```sh
muse plugins list --available   # muse-flow should be listed
muse plugins list               # muse-flow should be installed and enabled
muse plugins inspect muse-flow  # version, capabilities, active state
muse skills list --source plugin
```

The check step must show `"valid": true` before you install. If the shared list
stops showing the guide after an update, refresh it with:

```sh
muse plugins marketplace update muse-flow
muse plugins update muse-flow
```

To take it off:

```sh
muse plugins remove muse-flow
```

## Add it to Claude Code

Inside a Claude Code chat (2.1.275 or later), one step:

```text
/plugin install muse-flow --marketplace cbuntingde/muse-flow
```

Or from the command line, from a saved copy or from the web:

```sh
git clone https://github.com/cbuntingde/muse-flow.git
cd muse-flow
claude plugin validate plugins/muse-flow   # must report success
claude plugin validate .                    # marketplace manifest check
claude plugin marketplace add .
claude plugin install muse-flow@muse-flow-catalog
```

Confirm with `claude plugin list` and
`claude plugin details muse-flow` (shows all 7 guides).
Take it off with `claude plugin uninstall muse-flow@muse-flow-catalog`.

## What you get

| Guide | When to use it | What you get |
|---|---|---|
| `using-compact` | Each time you start | Points you to the right step |
| `clarify` | Request is unclear | Short written scope you sign |
| `plan-small` | Scope is signed, no task list yet | Numbered tasks with checks |
| `build-verify` | Task list is signed | Small tested change |
| `debug-focus` | Something fails or acts wrong | Cause before fixes |
| `review-release` | You say it is done | Release check with proof |
| `record-decide` | A real choice is open | Dated written choice |

Firm rules: no work without a signed scope and task list, no sharing without check proof, no done without test proof.

## What is in this project

- `plugins/muse-flow/` — the set you add
  (setup details for Muse and Claude Code, plus `skills/` and `references/`,
  which hold the rule pages so people who add it get the rules too).
- `.claude-plugin/marketplace.json` — the shared list entry that shows the guide
  when this project is added as a shared list. Read by both Muse and Claude Code.
- `LICENSE` — MIT.
