# Herdr Socket API Ecosystem Guide

This guide is for people building clients, scripts, agent tools, and workflow orchestrators on top of Herdr.

Canonical source: [SOCKET_API.md](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md). Last reviewed: 2026-05-17.

## Protocol Shape

Herdr exposes a local Unix socket API for scripts, tools, and coding agents.

| Field | Value |
|---|---|
| Transport | Unix domain socket |
| Encoding | Newline-delimited JSON |
| Request model | Send one JSON request per line |
| Response model | Read one JSON response per line |
| Subscriptions | Send `events.subscribe`, receive ack, keep the same connection open |

Request:

```json
{"id":"req_1","method":"ping","params":{}}
```

Success:

```json
{"id":"req_1","result":{"type":"pong","version":"0.1.2","protocol":2}}
```

Error:

```json
{"id":"req_1","error":{"code":"pane_not_found","message":"pane 1-99 not found"}}
```

## Socket Path Resolution

Named sessions are runtime/socket namespaces. Config remains global.

Resolution order from the official socket docs:

1. Explicit `herdr --session <name>`.
2. `HERDR_SOCKET_PATH`.
3. `HERDR_SESSION=<name>`.
4. Default session path under `$XDG_CONFIG_HOME/herdr/herdr.sock` or `$HOME/.config/herdr/herdr.sock`.

Session names may contain ASCII letters, numbers, `.`, `_`, and `-`. `default` is reserved.

## IDs

Responses use stable id forms:

| Object | Shape |
|---|---|
| Workspace | `w64e95948145ed1` |
| Pane | `w64e95948145ed1-1` |
| Tab | `w64e95948145ed1:1` |

Requests also accept older positional forms such as `1`, `1:2`, and `1-2` as shorthand for current session order. If you are building long-running tools, prefer re-reading current ids rather than assuming a positional id still points to the same object after panes/tabs/workspaces close.

## Method Families

The socket API includes these public method families:

| Family | Methods |
|---|---|
| Server | `ping`, `server.stop` |
| Workspaces | `workspace.list`, `workspace.get`, `workspace.create`, `workspace.focus`, `workspace.rename`, `workspace.close` |
| Tabs | `tab.list`, `tab.get`, `tab.create`, `tab.focus`, `tab.rename`, `tab.close` |
| Agents | `agent.list`, `agent.get`, `agent.read`, `agent.send`, `agent.rename`, `agent.focus`, `agent.start` |
| Panes | `pane.list`, `pane.get`, `pane.rename`, `pane.read`, `pane.split`, `pane.send_text`, `pane.send_keys`, `pane.send_input`, `pane.report_agent`, `pane.clear_agent_authority`, `pane.release_agent`, `pane.close`, `pane.wait_for_output` |
| Events | `events.subscribe` |

Recent releases expanded terminal-backed agent control. The raw method table above covers the documented socket methods; direct attachment is exposed through CLI wrappers such as `herdr agent attach <target>` and `herdr terminal attach <terminal_id>`.

## Reads and Waits

`pane.read` is the core feedback primitive.

```json
{
  "pane_id": "1-1",
  "source": "recent",
  "lines": 80,
  "format": "text",
  "strip_ansi": true
}
```

Read sources:

| Source | Meaning |
|---|---|
| `visible` | Current viewport |
| `recent` | Recent scrollback as rendered in the pane |
| `recent_unwrapped` | Recent terminal text with soft wraps joined |

Implementation notes:

- `strip_ansi` defaults to `true`.
- Reads default to 80 lines when `lines` is omitted.
- Reads are capped at 1000 lines.
- ANSI reads are available through CLI/socket support such as `herdr pane read --format ansi` / `--ansi`.

`pane.wait_for_output` accepts substring or regex matchers:

```json
{
  "pane_id": "1-1",
  "source": "recent",
  "lines": 200,
  "match": {"type": "substring", "value": "ready"},
  "timeout_ms": 30000,
  "strip_ansi": true
}
```

## Events

`events.subscribe` is the long-lived pubsub entrypoint.

Base lifecycle subscriptions include:

- `workspace.created`
- `workspace.closed`
- `workspace.focused`
- `tab.created`
- `tab.closed`
- `tab.focused`
- `tab.renamed`
- `pane.created`
- `pane.closed`
- `pane.focused`
- `pane.exited`
- `pane.agent_detected`

Parameterized subscriptions include:

- `pane.output_matched`
- `pane.agent_status_changed`

Base lifecycle pushed event names use snake case, such as `workspace_created`. Parameterized subscription event names keep dotted names, such as `pane.output_matched`.

## CLI Wrappers

Prefer CLI wrappers when you are writing shell scripts or agent skills. Use the raw socket when you need language-native clients, streaming subscriptions, or custom transport handling.

Common wrappers:

```sh
herdr status
herdr workspace list
herdr workspace create --cwd ~/project --label api
herdr tab create --label logs
herdr pane split 1-1 --direction right
herdr pane run 1-2 "npm test"
herdr pane read 1-2 --source recent --lines 50
herdr wait output 1-2 --match ready --timeout 30000
herdr wait agent-status 1-1 --status done
herdr terminal attach <terminal_id> --takeover
```

Notes:

- `herdr -V` and `herdr --version` print the local executable version without contacting the server.
- `pane run` is a convenience wrapper around `pane.send_input` with command text plus Enter.
- `wait agent-status` is built on event subscriptions.
- `pane.send_text` sends literal text only.
- Closing the socket connection ends an event subscription.

## Client Libraries

- [54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client) - Python client with socket discovery, request envelopes, typed errors, helper methods, and `events.subscribe` streaming.

Library checklist:

1. Implement socket discovery compatible with Herdr.
2. Preserve raw `request(method, params)` access.
3. Expose typed transport and API errors.
4. Support long-lived `events.subscribe`.
5. Do not hide stable ids from callers.
6. Keep CLI wrapper behavior documented when it differs from raw socket behavior.
