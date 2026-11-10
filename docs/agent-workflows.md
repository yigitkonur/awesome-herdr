# Agent Workflows on Herdr

Herdr is useful to humans, but its socket API and CLI wrappers also make it useful to agents that need to inspect, create, and coordinate terminal work.

Canonical sources: [Herdr TUI README](https://github.com/herdrdev/herdr), [SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md), and [Socket API](https://herdr.dev/tui/docs/socket-api/). Last reviewed: 2026-05-17. This guide covers Herdr TUI, not the Herdr app or herdr-core.

## Core Mental Model

| Concept | Workflow meaning |
|---|---|
| Workspace | Project or top-level context |
| Tab | Subcontext inside a workspace |
| Pane | Terminal surface where a shell, tool, or agent runs |
| Agent status | `idle`, `working`, `blocked`, `done`, or `unknown` |
| Named session | Runtime/socket namespace with its own state and shared global config |

## Recommended Agent Loop

1. Check whether you are inside Herdr with `HERDR_ENV=1`.
2. Read current topology with `workspace list`, `tab list`, and `pane list`.
3. Create a tab or split pane for the side task.
4. Run the command or helper agent.
5. Read recent or visible output.
6. Wait for output or agent completion.
7. Summarize and close or keep the pane depending on whether it is still useful.

## Worker Pane Recipe

```sh
herdr tab create --label tests --focus
herdr pane split 1-1 --direction right
herdr pane run 1-2 "npm test"
herdr wait output 1-2 --match "Tests" --timeout 60000
herdr pane read 1-2 --source recent --lines 80
```

## Agent Pairing Recipe

Use a dedicated tab per peer:

```sh
herdr tab create --label claude --focus
herdr pane run 1-1 "claude"
herdr tab create --label codex --focus
herdr pane run 1-1 "codex"
```

Then use `wait agent-status` and `pane read` to coordinate handoffs.

Related project:

- [hcaiano/skills](https://github.com/hcaiano/skills) - `herdr-pair` teaches Claude and Codex to collaborate inside Herdr.

## Watcher Pane Recipe

Good watcher panes are explicit and disposable:

```sh
herdr tab create --label logs
herdr pane run 1-1 "tail -f ./log/dev.log"
herdr pane read 1-1 --source visible --ansi
```

Use ANSI reads when the visual shape of a TUI matters. Use stripped text reads when you want parsing.

## Waiting

Use output waits when a pane is a plain command:

```sh
herdr wait output 1-1 --match "ready" --timeout 30000
```

Use status waits when the pane is an agent:

```sh
herdr wait agent-status 1-1 --status done --timeout 600000
```

## Safety Notes

- Re-read ids after closing workspaces, tabs, or panes.
- Avoid guessing positional ids in long-running scripts.
- Prefer `--json` where commands support it.
- Treat `pane.send_text` as literal text, not as keypress input.
- Use `pane.send_input` or `pane run` when you need Enter.
