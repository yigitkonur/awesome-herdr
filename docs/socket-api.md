# Herdr TUI Socket API

A field guide for people building scripts, clients, and agent tools on the Herdr TUI socket API.

Canonical sources: [Socket API](https://herdr.dev/tui/docs/socket-api/), [CLI reference](https://herdr.dev/tui/docs/cli-reference/), [Agent automation](https://herdr.dev/tui/docs/agent-automation/), [API schema](https://github.com/herdrdev/herdr/blob/v0.9.5/docs/next/api/herdr-api.schema.json). Last reviewed: 2026-11-10.

Covers Herdr TUI v0.9.5 (stable, released 2026-10-14; socket protocol 22). It does not cover the Herdr app, herdr-core (`hc`), or the mobile apps; for those see the guides listed at the end.

## Pick a layer

| Layer | Use it for |
|---|---|
| Agent skill | Teaching a coding agent how to use Herdr from inside a pane. |
| CLI wrappers | Shell scripts, simple orchestration, and human debugging. |
| Raw socket API | Custom tools, protocol clients, and event subscribers. |

The layers share the same control surface. Start with the CLI wrappers, which print JSON for most commands, and drop to the raw socket only for direct request/response control or long-lived event subscriptions.

## Protocol shape

Herdr uses newline-delimited JSON over a local socket: a Unix domain socket on Unix, a named pipe on Windows. Send one request per line. The response carries the same `id`.

Request:

```json
{"id":"req_1","method":"ping","params":{}}
```

Success (captured from a v0.9.5 server):

```json
{"id":"req_1","result":{"type":"pong","version":"0.9.5","protocol":22,"capabilities":{"live_handoff":true,"detached_server_daemon":false,"endpoint_protocol_generation":1,"surface_interest":true,"health_check":true,"ssh_agent_registration":true}}}
```

Error (captured from a v0.9.5 server):

```json
{"id":"req_2","error":{"code":"pane_not_found","message":"pane w999:p9 not found"}}
```

Rules worth knowing:

- Error responses echo the request `id` when the line reached JSON decoding, including for invalid methods or parameters. Invalid JSON, or a missing top-level string `id`, gives an empty `id`.
- Transport errors, such as invalid UTF-8, can close the connection without a response.
- An unknown method returns `invalid_request`.
- JSON clients should ignore unknown fields and treat unsupported methods as normal errors.
- `events.subscribe` keeps the connection open after its first response. Closing the connection ends the subscription.
- The old `pane.graphics.*` socket methods are removed. There is no replacement socket image API; emit the Kitty graphics protocol from the pane instead.

## Socket path and named sessions

| Session | Socket |
|---|---|
| default | `~/.config/herdr/herdr.sock` |
| named | `~/.config/herdr/sessions/<name>/herdr.sock` |

On Linux and macOS the config directory is `$XDG_CONFIG_HOME/herdr` when `XDG_CONFIG_HOME` is set, otherwise `$HOME/.config/herdr`. Windows uses a named pipe instead of a socket file, so do not build the path by hand there.

Resolution order for the CLI:

1. Explicit `herdr --session <name>`.
2. `HERDR_SOCKET_PATH`.
3. `HERDR_SESSION=<name>`.
4. The default session socket.

Use `HERDR_SOCKET_PATH` only for low-level overrides. Inside a Herdr pane it already points at the running server.

Session facts:

- A named session has its own panes, tabs, workspaces, sockets, and runtime state. It shares the global config file.
- Names use ASCII letters, numbers, `.`, `_`, and `-`, up to 64 bytes; `.` and `..` are rejected. The name `default` selects the default session.
- `herdr session list --json` prints each session's `name`, `default`, `running`, `socket_path`, and `session_dir`.
- On Windows, raw clients must use the platform-native local socket form. Plugins that need portable Windows behaviour should call `HERDR_BIN_PATH` and the CLI wrappers.

## IDs

Public ids are opaque, stable handles. The docs show these shapes:

| Object | Example |
|---|---|
| Workspace | `w1` |
| Tab | `w1:t1` |
| Pane | `w1:p1` |

- Parse ids from JSON responses. Do not derive them from sidebar order or examples. A live v0.9.5 server returned ids such as `wTX:p2F`.
- Closed tab and pane ids are not reused.
- Moving a pane to another workspace gives it a new workspace-qualified id. Use `.result.move_result.pane.pane_id` afterwards; the old value is at `.result.move_result.previous_pane_id`.
- Ids and agent names belong to one server. Two saved SSH machines can both have `w1:p1`.
- Agent methods take a `target`: a unique live agent name or the pane id hosting the agent. Terminal ids and bare agent-kind labels are not targets.
- Agent names match `[a-z][a-z0-9_-]{0,31}` and are unique among live agents.
- Creation responses hand you the next ids: `workspace create` returns `.result.workspace`, `.result.tab`, and `.result.root_pane`; `tab create` returns `.result.tab` and `.result.root_pane`; `pane split` returns `.result.pane`.

## Method families

Method names use dot notation. This is the table from the v0.9.5 docs.

| Area | Methods |
|---|---|
| Server | `ping`, `server.stop`, `server.reload_config`, `server.agent_manifests`, `server.reload_agent_manifests` |
| Notification | `notification.show` |
| Client | `client.window_title.set`, `client.window_title.clear` |
| Session | `session.snapshot` |
| Workspace | `workspace.create`, `workspace.list`, `workspace.get`, `workspace.focus`, `workspace.rename`, `workspace.move`, `workspace.move_block`, `workspace.report_metadata`, `workspace.close` |
| Worktree | `worktree.list`, `worktree.create`, `worktree.open`, `worktree.remove` |
| Tab | `tab.create`, `tab.list`, `tab.get`, `tab.focus`, `tab.rename`, `tab.move`, `tab.close` |
| Pane | `pane.split`, `pane.swap`, `pane.move`, `pane.zoom`, `pane.layout`, `pane.process_info`, `pane.neighbor`, `pane.edges`, `pane.focus_direction`, `pane.resize`, `pane.list`, `pane.current`, `pane.get`, `pane.rename`, `pane.send_text`, `pane.send_keys`, `pane.send_input`, `pane.read`, `pane.report_agent`, `pane.report_agent_session`, `pane.report_metadata`, `pane.clear_agent_authority`, `pane.release_agent`, `pane.close`, `pane.wait_for_output` |
| Popup | `popup.close` |
| Layout | `layout.export`, `layout.apply`, `layout.set_split_ratio` |
| Agent | `agent.list`, `agent.get`, `agent.read`, `agent.explain`, `agent.send_keys`, `agent.prompt`, `agent.wait`, `agent.rename`, `agent.focus`, `agent.start`, `agent.view.set`, `agent.view.clear` |
| Events | `events.subscribe`, `events.wait` |
| Integrations | `integration.install`, `integration.uninstall` |
| Plugins | `plugin.link`, `plugin.list`, `plugin.unlink`, `plugin.enable`, `plugin.disable`, `plugin.action.list`, `plugin.action.invoke`, `plugin.log.list`, `plugin.pane.open`, `plugin.pane.focus`, `plugin.pane.close` |

The schema is the authority. It also defines methods this table omits, for example `pane.focus`, `pane.input.set`, and `integration.list`.

Behaviour that trips up clients:

- Pane methods whose schema makes `pane_id` optional use the server's active focused pane when it is omitted. `pane.move` always needs the source `pane_id`.
- `pane.send_text` sends literal text. `pane.send_keys` and `pane.send_input.keys` take Herdr key-combo strings such as `enter`, `esc`, `ctrl+h`, `shift+tab`, `f1`, `minus`, and `plus`. They do not accept `prefix+` binding strings.
- Methods that launch processes accept an `env` object that applies to the new process only. Herdr-managed variables win when they conflict.
- `workspace.close` refuses to close a primary workspace while linked-worktree workspaces are open unless params include `"close_group": true`. Without it you get `workspace_group_close_required`.
- `session.snapshot` is a one-time bootstrap read, not a subscription.
- `pane.report_agent` reports semantic agent state (`state` affects waits, notifications, and rollups). `pane.report_metadata` is display-only.
- On macOS, `pane.send_input` and `agent.start` reject an oversized line in full. Wait for the shell prompt and retry. A successful response acknowledges queue admission, not command execution.

## Reads and waits

`pane.read` is the core feedback primitive. `source` is required.

```json
{"id":"r1","method":"pane.read","params":{"pane_id":"w1:p1","source":"recent","lines":80,"format":"text","strip_ansi":true}}
```

`pane_id` and `source` are required. The response is `type: "pane_read"` with the text at `.result.read.text`; `.result.read` also has `revision` and `truncated`.

| Raw `source` | CLI `--source` | Meaning |
|---|---|---|
| `visible` | `visible` | Current rendered screen. |
| `recent` | `recent` | Recent scrollback with terminal wrapping. |
| `recent_unwrapped` | `recent-unwrapped` | Recent scrollback without soft wrapping. Best for logs. |
| `detection` | `detection` | Bottom-buffer snapshot used by agent screen detection. |

- `format` is `text` (default) or `ansi`. `strip_ansi` defaults to `true`. On the CLI, `pane read` takes `--format ansi` or `--ansi`.
- For the recent sources, omitting `lines` reads the last 80 rendered rows. For `visible` and `detection`, omitting it returns the full snapshot.
- `lines` is capped at 1000.
- `detection` is always plain text.

`pane.wait_for_output` takes a `match` of type `substring` or `regex`:

```json
{"id":"w1","method":"pane.wait_for_output","params":{"pane_id":"w1:p1","source":"recent","lines":200,"match":{"type":"substring","value":"ready"},"timeout_ms":30000,"strip_ansi":true}}
```

- It checks the snapshot immediately, so output already on screen can match, then polls.
- For waits, `recent` is searched as unwrapped recent output (latest 80 rows unless `lines` is set).
- Substring and regex (Rust syntax) both match one line at a time.
- The CLI result has `.result.pane_id`, `.result.matched_line`, and `.result.read`.

Agent waits observe lifecycle state, not command completion.

- `agent.wait` is server-owned and event-driven. It pins the resolved pane occupant, so a replacement agent cannot satisfy the wait.
- `agent.prompt` accepts an optional `wait` object with `until` and `timeout_ms`, which submits the prompt and starts the wait in one request. If the agent is already `blocked`, it returns `agent_blocked` without sending input.
- Agent states: `idle`, `working`, `blocked`, `done`, `unknown`. `done` means idle and not yet seen. `idle` and `done` both mean ready for input.
- Waits default to `idle`, `done`, or `blocked`; ask for `unknown` explicitly.
- A timeout or `agent_prompt_stalled` does not prove the prompt was never delivered. Read the agent before retrying.
- `events.wait` currently supports pane agent status matches only, for example:

```json
{"id":"wait_1","method":"events.wait","params":{"match_event":{"event":"pane_agent_status_changed","pane_id":"w1:p1","agent_status":"blocked"},"timeout_ms":1000}}
```

## Events and subscriptions

```json
{"id":"sub_1","method":"events.subscribe","params":{"subscriptions":[{"type":"pane.agent_status_changed","pane_id":"w1:p1","agent_status":"blocked"}]}}
```

The first response is `{"id":"sub_1","result":{"type":"subscription_started"}}`. Later lines are pushed events.

Subscription types in v0.9.5:

| Kind | Types |
|---|---|
| Workspace | `workspace.created`, `workspace.updated`, `workspace.metadata_updated`, `workspace.renamed`, `workspace.moved`, `workspace.reordered`, `workspace.closed`, `workspace.focused` |
| Worktree | `worktree.created`, `worktree.opened`, `worktree.removed` |
| Tab | `tab.created`, `tab.closed`, `tab.focused`, `tab.renamed`, `tab.moved` |
| Pane | `pane.created`, `pane.updated`, `pane.closed`, `pane.focused`, `pane.moved`, `pane.exited`, `pane.agent_detected` |
| Layout | `layout.updated` |
| Needs params | `pane.output_matched`, `pane.agent_status_changed`, `pane.scroll_changed` |

- `pane.output_matched` takes `pane_id`, `source`, `match`, and optional `lines` and `strip_ansi`.
- `pane.agent_status_changed` takes `pane_id` and an optional `agent_status` filter.
- `pane.scroll_changed` takes `pane_id`.
- Pushed lifecycle events are `{"event": ..., "data": ...}` envelopes with snake_case names such as `workspace_created`. The three parameterized types keep their dotted names, such as `pane.output_matched`.
- All subscription entries must be valid. If a referenced pane does not exist, Herdr rejects the whole request with an error and closes the connection.
- Subscriptions start when the request is accepted and do not replay earlier events. History is not durable.
- If a subscriber falls behind, the server sends an error with the original request `id` and `error.code: "events_lost"`, then closes that connection.
- Recovery: open a new subscription, wait for `subscription_started`, and call `session.snapshot` on another connection. Replace your cache with the snapshot and treat events as signals to re-read. Do not replay buffered event payloads onto the snapshot.
- Plugin event hooks receive a narrower set of events than API subscribers. `workspace.metadata_updated`, `pane.updated`, and `layout.updated` do not invoke hooks.

## CLI wrappers

```sh
herdr status
herdr workspace create --cwd ~/project --label api --no-focus
herdr tab create --label logs
herdr pane split w1:p1 --direction right
herdr pane run w1:p2 "npm test"
herdr pane read w1:p2 --source recent --lines 50
herdr pane wait-output w1:p2 --regex "passed|failed" --timeout 120000
herdr agent wait w1:p1 --until done
herdr agent prompt reviewer "Review the current diff" --wait --timeout 120000
herdr terminal attach <terminal_id> --takeover
herdr api snapshot
```

- `pane run` submits text plus Enter as one operation. Prefer it over `send-text` plus `send-keys enter`.
- There is no top-level `herdr wait` command. Use `herdr pane wait-output` for output and `herdr agent wait` for agent state.
- `pane wait-output` and `agent wait` wait indefinitely when `--timeout` is omitted. With `agent prompt --wait`, a prompt sent from a non-working state returns `agent_prompt_stalled` after five seconds without observed activity.
- A timeout or server error prints JSON on stderr and exits 1. CLI usage errors exit 2.
- `herdr --machine <label-or-id> ...` routes API commands to a saved SSH machine. It cannot be combined with `--session` or `--remote`.
- `herdr api snapshot` prints the live `session.snapshot` response as JSON.

## Environment variables

| Where | Variables |
|---|---|
| Managed pane processes | `HERDR_SOCKET_PATH`, `HERDR_BIN_PATH`, `HERDR_ENV=1`, `HERDR_WORKSPACE_ID`, `HERDR_TAB_ID`, `HERDR_PANE_ID` |
| Plugin commands | `HERDR_SOCKET_PATH`, `HERDR_BIN_PATH`, `HERDR_ENV=1`, `HERDR_PLUGIN_ID`, `HERDR_PLUGIN_ROOT`, `HERDR_PLUGIN_CONFIG_DIR`, `HERDR_PLUGIN_STATE_DIR`, `HERDR_PLUGIN_CONTEXT_JSON`, plus `HERDR_WORKSPACE_ID`, `HERDR_TAB_ID`, `HERDR_PANE_ID` when available |
| Plugin actions, events, panes | Actions add `HERDR_PLUGIN_ACTION_ID`. Startup and event hooks add `HERDR_PLUGIN_EVENT`; event hooks also get `HERDR_PLUGIN_EVENT_JSON`. Pane commands add `HERDR_PLUGIN_ENTRYPOINT_ID`. |
| Custom keybind commands | `HERDR_SOCKET_PATH`, `HERDR_BIN_PATH`, `HERDR_ACTIVE_WORKSPACE_ID`, `HERDR_ACTIVE_TAB_ID`, `HERDR_ACTIVE_PANE_ID`, `HERDR_ACTIVE_PANE_CWD` when available |
| Your shell or service | `HERDR_SESSION` selects a named session. `HERDR_SOCKET_PATH` overrides the socket path. |

- `--current` on pane commands uses the calling pane's `HERDR_PANE_ID`, and errors when it is unset.
- The agent skill's guardrail: if `HERDR_ENV=1` is not set, stop; you are not in a Herdr-managed pane.
- A plugin popup has no pane id and does not get `HERDR_PANE_ID`.
- `HERDR_PLUGIN_CONFIG_DIR` and `HERDR_PLUGIN_STATE_DIR` are path discovery only; Herdr has no plugin storage API in v1.
- New panes identify as `TERM_PROGRAM=herdr`.

## API schema

```sh
herdr api schema
herdr api schema --json
herdr api schema --output herdr-api.schema.json
```

Plain `herdr api schema` prints a short summary. `--json` prints the full JSON Schema, and `--output PATH` writes it to a file. The schema covers requests, success responses, error responses, emitted events, and subscription events. A v0.9.5 binary reports `protocol: 22`, `schema_version: 1`, and the schemas `error_response`, `event`, `request`, `subscription_event`, and `success_response`.

The binary embeds the schema file, so `herdr api schema` always matches the version you run. The canonical link above points at the copy tagged `v0.9.5`.

## Client libraries

Community clients from the [awesome-herdr README](../README.md), taken from its "Socket API and herdr-core clients and SDKs" section.

| Project | Language and scope (summarized from the README) |
|---|---|
| [54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client) | Typed Python bindings and socket utilities. |
| [QuiquiMatCom2004/herdr-py](https://github.com/QuiquiMatCom2004/herdr-py) | Python programs control workspaces, panes, agents, and other resources through the socket API. |
| [dmmulroy/herdr-ts-sdk](https://github.com/dmmulroy/herdr-ts-sdk) | Effect-native TypeScript SDK. The README names protocol 21; v0.9.5 reports protocol 22, so check compatibility first. |
| [egriff38/effect-herdr](https://github.com/egriff38/effect-herdr) | Typed Effect-TS SDK. |
| [brooswit-factory/jsHerdrSDK](https://github.com/brooswit-factory/jsHerdrSDK) | Typed TypeScript client generated from the published JSON Schema. |
| [lib-x/herdr-sock-go](https://github.com/lib-x/herdr-sock-go) | Go client with typed and raw methods. |
| [cyperx84/herdr-api](https://github.com/cyperx84/herdr-api) | Go client with typed agent models and event subscriptions. |
| [vika2603/herdr-client](https://github.com/vika2603/herdr-client) | Typed Go client and plugin toolkit generated from the schema the binary prints, covering protocol 22. |
| [maxandersen/jherdr](https://github.com/maxandersen/jherdr) | Java client with a scripting facade, generated typed methods, or raw calls. |
| [rudironsoni/HerdrKit](https://github.com/rudironsoni/HerdrKit) | Swift 6 client kit for protocols 17 through 22. |
| [vinceferro/herdr-tg crates/herdr-client](https://github.com/vinceferro/herdr-tg/tree/HEAD/crates/herdr-client) | Typed Rust client for the socket protocol. |
| [kevinWangSheng/herdr-kit](https://github.com/kevinWangSheng/herdr-kit) | Saves and restores declarative pane layouts, watches events, and calls socket methods. |

If you write your own client:

1. Keep a raw `request(method, params)` escape hatch, because methods outside the docs table exist.
2. Surface transport errors and API error codes separately.
3. Support long-lived `events.subscribe`, including `events_lost` recovery with `session.snapshot`.
4. Ignore unknown response fields and handle unsupported methods as normal errors.
5. Expose ids exactly as returned.
6. Read `version` and `protocol` from `ping`; it also advertises server capabilities.

## Related guides

[Configuration](./configuration.md), [Integrations](./integrations.md), [Agent workflows](./agent-workflows.md), [Herdr app](./herdr-app.md), [herdr-core](./herdr-core.md).
