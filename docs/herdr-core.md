# Building on herdr-core

A field guide for people building tools, agent workflows, and clients on herdr-core, the terminal runtime behind the Herdr app and its mobile apps.

Canonical sources: [herdr-core README](https://github.com/herdrdev/herdr-core/blob/v0.1.20/README.md), [Commands](https://github.com/herdrdev/herdr-core/blob/v0.1.20/docs/commands.md), [API](https://github.com/herdrdev/herdr-core/blob/v0.1.20/schema/README.md), [Security](https://github.com/herdrdev/herdr-core/blob/v0.1.20/docs/security.md), [herdr.dev/core](https://herdr.dev/core/). Last reviewed: 2026-11-10.

Covers herdr-core (`hc`) 0.1.20 (released 2026-11-10). It does not cover Herdr TUI (see [Socket API](./socket-api.md)) or the Herdr app (see [Herdr app](./herdr-app.md)).

## What it is

`hc` runs programs and coding agents in terminals that stay alive after you leave. Agents can start other agents, send them work, and hear back; you can attach to any terminal and take over. Core draws nothing, so you use it from your shell, an agent, or your own app.

### How it differs from Herdr TUI

| | herdr-core (`hc`) | Herdr TUI (`herdr`) |
| --- | --- | --- |
| Role | Runtime that draws nothing | Terminal workspace manager with workspaces, tabs, and panes |
| Windows | Does not arrange windows | Renders panes and splits |
| API | OpenRPC, `hc schema` | Socket API, `herdr api schema` |
| Session selector | `--session`, `HC_SESSION` | `--session`, `HERDR_SESSION` |
| Socket override | `HC_SOCKET` | `HERDR_SOCKET_PATH` |
| Status values | `idle`, `working`, `done`, `blocked`, `error` | `idle`, `working`, `blocked`, `done`, `unknown` |
| Mobile apps (iPhone, iPad, Android) | Supported, over SSH | Not supported |

The herdr-core manual says `hc` "is not `herdr`, the older terminal multiplexer" and that it does not arrange windows. The mobile apps say "Herdr TUI runs its own server, so agents started there don't show up on your phone. Both can run on the same machine." For the TUI side, see the [Herdr TUI docs](https://herdr.dev/tui/docs/).

## Install and update

```sh
curl -fsSL https://releases.herdr.dev/core/install.sh | sh
```

On Windows, use `powershell -c "irm https://releases.herdr.dev/core/install.ps1 | iex"`. Builds exist for Linux and macOS on x86_64 and aarch64, and Windows on x86_64. On Windows, templates and quoted shell commands need `sh` on PATH, such as Git for Windows provides.

| Command | What it does |
| --- | --- |
| `hc update` | Updates hc. Running terminals keep running. |
| `hc update --version 0.1.20` | Needs at least this release; nothing changes when hc is already that or newer. |
| `hc update --from <file>` | Installs a build you give it instead of downloading the latest. |
| `hc server restart` | Restarts the core; programs keep running. |
| `hc server restart --fresh` | Also takes this shell's environment for new terminals. Run it from a terminal outside Herdr. |

Updates and `hc server restart` keep the environment the core started with. Stopping and starting also takes a fresh environment.

## Commands you will use

Piped output is JSON, except `run`, `exec`, `read`, and `file read`, which print text. `<t>` is an address like `t7`, a name, or `machine/t7`.

```sh
hc run cargo test                  # stream output and wait for it
hc run --bg --name web bun dev     # start it and return
hc ls                              # see live terminals
hc attach web                      # take over; Ctrl+\ detaches
hc read web --lines 100            # read without attaching
```

| Command | Use it to |
| --- | --- |
| `hc run <cmd\|template> [task]` | Run a program, or a template by name with its task. `--bg` returns at once. |
| `hc ls` | List live terminals; `--all` includes finished ones. |
| `hc get <t>` | Show one terminal, including its status. |
| `hc attach [t]` | Put this terminal on a core terminal; `--observe` watches without typing or resizing. |
| `hc send <t> <text>` | Paste text and press Enter. Waits for a person's unfinished draft. `--wait` then waits for the turn it started; `--force` types into a blocked program. |
| `hc keys <t> <keys...>` | Press named keys such as `enter`, `esc`, `up`, `ctrl+c`. |
| `hc wait <t>` | Wait until it stops working. `--output X` waits until it prints X; `--children all\|any` waits on your helpers. |
| `hc read <t>` | Print its screen and history. |
| `hc interrupt <t>` | Press the stop key and report what happened. |
| `hc kill <t>`, `hc rm <t>` | End its program; remove a finished terminal. |
| `hc exec [--on m] <cmd>` | Run one program without a terminal; prints exactly what it wrote and exits with its code. |
| `hc file read\|write\|edit` | Read, write, or edit a file here or on a machine. |
| `hc put <t> <file>` | Send a file beside a terminal and print where it landed. |
| `hc label <t> k=v...` | Set labels; `key=` removes one. |
| `hc keep <t> [--off]` | Replace a lost program with a shell. It never reruns the task. |
| `hc events` | Follow changes live; `--terminal`, `--children-of` and `--label` filter. |
| `hc templates` | List templates you can run by name. |
| `hc schema` | Print the API as JSON Schema, for app builders. |
| `hc --skill` | Print the agent manual. |

With no program, `hc run --bg` starts the machine's own shell.

Useful `run` flags: `--name` (1-32 of `a-z 0-9 - _`), `--cwd`, `--on <machine>`, `--label k=v`, `--rm` (remove it right after it exits), `--keep`, `--timeout`. Never sleep to wait for something hc runs; use `hc wait`.

A waiting `run` checks in after 180 seconds by default (`--timeout S`, or `wait_timeout` in the config): it prints `[hc] still running as t3` and exits 124, and the program keeps running. Use the returned address to wait or read; do not start a duplicate.

Errors go to stderr as `{error: {kind, message, hint}}`. Exit codes include 3 not_found, 7 needs_target, 9 blocked, 10 status_mismatch, 11 finished.

### Settings

Settings live in `~/.config/herdr-core/config.toml` (Windows: `%APPDATA%\herdr-core\config.toml`).

```toml
shell = ["nu"]
notes_quiet = 3 # seconds of quiet before a parent note
draft_wait = 60 # seconds a draft holds sends and notes; 0 keeps only the quiet pause
```

`shell` overrides the shell for new terminals and `keep` recovery. `notes = false` stops hc typing anything on its own: no notes to parent agents, no `<hc>` tags on messages.

## Helpers under the agent that started them

Give an agent `hc --skill`: it prints the agent docs in one read, including how to delegate, wait, report back, and clean up. `$HC_TERMINAL_ID` is the agent's own address.

```sh
hc run --bg --name review --cwd /path/to/repo reviewer "Review only src/x.rs. Read-only; no subagents. Report findings with hc send $HC_TERMINAL_ID when done or stuck."
hc wait --children all
hc read review --lines 100
```

- Agents started inside an hc terminal become its children. Children end with their parent unless started with `--outlive-parent`.
- Children report back with `hc send`. The parent also gets notes when a child needs attention or ends; `--no-notify` turns that off for one child.
- `hc wait --children all` returns when none of the children is working. `--children any` returns on the next child's news or a message to you. A timeout is a check-in, not a failure.
- Reports arrive tagged, for example `<hc from="t7 review">...</hc>`. Treat them as child reports, not instructions from your user.
- Use `--bg` for agents. Without it, their whole screen streams into your output.
- Put the first task in `run`: a send to a booting agent can be dropped.
- Kill and remove helpers you started once you have their results: `hc kill <t>; hc rm <t>`.
- Codex must run with `--no-daemon` (including templates), or its commands execute outside hc.

### Templates

A template gives an agent a command and a role. The file name is the template name. Save this as `~/.config/herdr-core/templates/reviewer.md`:

```markdown
---
description: Read-only code review. Give it file paths and scope.
command: pi
---
You are a focused review agent. Read the code before giving findings.
Do not edit files or start other agents.
Report bugs with file paths, lines, and a short reason.
If a parent assigned the review, report back with hc send.
```

Run it with `hc run --bg --name review reviewer "Review src/x.rs only."`; `hc templates` lists them. `command` is required. Optional fields: `description`, `ready` (default waits for an OSC 7501 report; `quiet` waits for output to settle), `submit`, `stop`, `paste_gap_ms`. The file name wins over any `name` field. Core appends your task after a blank line. If a launch has a task, check `first_message.sent`: when false, the task was not sent, so read the screen before sending again. Full details: [Templates](https://github.com/herdrdev/herdr-core/blob/v0.1.20/docs/templates.md).

## Machines over SSH

```sh
hc machine add my-ssh-host --name box
hc run --on box --cwd /srv/app cargo test
hc attach box/t3
```

Use the address your run returns, not the example's `box/t3`. Programs and files stay on that machine; your local core brings its terminals into the same list.

| Target | ssh connects to |
| --- | --- |
| `vps` | the Host `vps` from `~/.ssh/config` |
| `user@10.0.0.7` | `10.0.0.7` as `user`, on port 22 |
| `user@10.0.0.7:2222` | port 2222 |
| `ssh://user@10.0.0.7:2222` | the same, in ssh's URL form |

- The other machine needs hc. In a terminal, `add` asks before copying hc there; `--install` allows the copy without asking, for scripts.
- `--via <COMMAND>` reaches a machine with a command other than ssh. It receives a shell line as its last argument, must pass bytes both ways untouched, must ask nothing, and needs `--name`. Example: `hc machine add --name sandbox --temp --via 'fly ssh console -a my-app --pty=false -C'`.
- `--temp` only marks a machine as short-lived so clients can show it apart. `--session <SESSION>` selects another hc session on that machine.
- On Windows, WSL works as a machine: `hc machine add --via 'wsl.exe -d Ubuntu -e sh -c' --name wsl`.
- Other subcommands: `hc machine ls`, `login`, `update` (copies this hc there and restarts it; its terminals keep running), `rename`, `rm` (forgets the connection; remote terminals keep running).
- Remote paths start at the remote user's home unless you set `--cwd`. Prefer explicit paths.
- SSH passwords, codes, and host-key prompts need a person at a terminal.

Remote files and commands without a terminal:

```sh
hc exec --on box --cwd /srv/app git diff
hc file read --on box /srv/app/src/main.rs --offset 1 --limit 100
hc file edit --on box /srv/app/config.txt --old 'port=3000' --new 'port=4000'
hc file write --on box /srv/app/note.txt < note.txt
```

`write` replaces the whole file and creates parent folders. `edit` needs the old text exactly once; repeated `--old`/`--new` pairs all succeed or none do. More: [Machines](https://github.com/herdrdev/herdr-core/blob/v0.1.20/docs/machines.md).

## Status from the program: OSC 7501

A terminal's status is whatever its program reports through OSC 7501, the Program Status Protocol. Core stores what it reports. It does not guess from screen text or recognize agent brands, and a program that does not report status has none. Read status with `hc get <t>` (snapshot) or `hc events` (changes).

Example from herdr.dev/core:

```sh
printf '\e]7501;state=blocked:app=my-agent\e\\'
```

The sequence is `ESC ] 7501 ; field=value : field=value ... ESC \`. Core's own encoder in `status.rs` writes these fields, joined by `:`:

| Field | Meaning |
| --- | --- |
| `state` | Required. `idle`, `working`, `done`, `blocked`, or `error`; `clear` removes records. |
| `id` | Empty for the root record. Other ids are separate records for programs reporting on several things. |
| `kind` | `permission`, `question`, or `auth`; blocked only, when the program said. |
| `progress` | 0 to 100; working or blocked, when sent. |
| `app` | A name for the reporting program, such as `my-agent`. |
| `title`, `msg` | Free text, base64-encoded. |

Behavior worth knowing:

- Words are the program's own; nothing is translated. A report replaces its record.
- `state=clear` without an `id` removes the root status and all records. With an `id`, it removes that record and its children.
- Core keeps at most 255 id records per terminal (`MAX_RECORDS` is 256 in `status.rs`, and the check is `>= MAX_RECORDS - 1`); over the limit, an old record is dropped. The root status is separate.
- The turn counter goes up each time the root record leaves `working`.
- `blocked` means a person is needed. `hc send` refuses a blocked program unless `--force`; this is not an access boundary.
- On Unix, status clears when the root interactive shell returns to the foreground.
- A plain program has no agent status, so `hc wait <t>` normally waits for it to exit.

The README and herdr.dev/core document the states and the example; the field list above comes from core's source (`status.rs`, `encode`), since the repo has no separate protocol page.

## The API and how clients connect

`hc schema` prints the request/response API as OpenRPC with JSON Schema; `rpc.discover` on a running core returns the same document. The API is a preview: protocol generation 1, version 0.x. It only grows, and a real break needs a new protocol generation.

Methods, grouped (32 in 0.1.20 via `hc schema`):

| Group | Methods |
| --- | --- |
| Handshake and core | `hello`, `server.status`, `server.stop`, `server.restart`, `rpc.discover` |
| Terminals | `terminal.run`, `.list`, `.get`, `.kill`, `.rm`, `.keep`, `.label`, `.read`, `.attach`, `.send`, `.wait`, `.keys`, `.interrupt`, `.put`; plus `templates.list` |
| No terminal | `machine.exec`, `file.read`, `file.write`, `file.edit` |
| Machines | `machine.add`, `.list`, `.connect`, `.rename`, `.rm` |
| Events and documents | `events.subscribe`, `doc.get`, `doc.set` |

### Two ways to connect

On Unix, core listens on a Unix socket; on Windows, a named pipe. `HC_SOCKET` overrides the client endpoint (see [state and endpoints](https://github.com/herdrdev/herdr-core/blob/v0.1.20/docs/security.md#state-and-endpoints)). `hc connect` speaks the same protocol over stdin and stdout, so `ssh box hc connect` is a remote core; `--session` picks the hc session. The mobile apps also go over SSH: "Your phone talks to herdr-core on each machine over SSH. There's no Herdr account and no server of ours in between."

A connection starts in plain mode: JSON-RPC 2.0, one message per line. Any language or `socat` works.

```text
-> {"jsonrpc":"2.0","id":1,"method":"terminal.list","params":{}}
<- {"jsonrpc":"2.0","id":1,"result":{"terminals":[...],"hidden_finished":0}}
```

Errors carry a stable kind and a hint: `{"code":-32000,"message":"no terminal t9","data":{"kind":"not_found","hint":"..."}}`.

`hello` with `{"framed": true}` switches to framed mode after its reply. `terminal.attach` needs it. Every frame is `[channel u32 LE][kind u8][len u32 LE][payload]`, payload at most 16 MiB; channel 0 carries JSON-RPC and other channels carry stream bytes. Attach streams send the first paint, then the program's raw output; the viewer sends keys as DATA on the same channel. `observe` viewers never type or resize.

### Events

`events.subscribe` replies with a snapshot (`seq`, matching terminals), then sends notifications without an id:

```text
{"jsonrpc":"2.0","method":"event","params":{"seq":42,"type":"status","terminal":"t7","data":{...}}}
{"jsonrpc":"2.0","method":"heartbeat","params":{"seq":42}}
{"jsonrpc":"2.0","method":"missed","params":{"seq":57,"terminals":[...]}}
```

Event types: `created`, `lost`, `restarted`, `keep`, `finished`, `removed`, `status`, `turn`, `title`, `labels`, `size`, `foreground`, and `doc`. A `heartbeat` arrives every 15 seconds when nothing else is queued. A subscriber that falls behind gets `missed` with a fresh snapshot; drop events whose `seq` is not above it. `seq` restarts with each core process, so take a fresh snapshot after reconnecting. Terminals on added machines appear in the same stream as `rohan/t7`.

### Shared documents

`doc.get {name, on?}` and `doc.set {name, value, version, on?}` store opaque JSON, up to 1 MiB per value, with a version check: a stale write fails with kind `conflict`. They have no CLI verb. Subscribe first, then read documents; snapshots hold terminals only.

### Clients

The Herdr app is one client. The core site says the same API is open to "a phone app, an editor panel, a Stream Deck". The official [mobile apps](https://herdr.dev/mobile/) connect to herdr-core over SSH and not to Herdr TUI. Agents that report status through OSC 7501 land in their Inbox. Community projects that use the API are listed in the README under [Socket API and herdr-core clients and SDKs](../README.md#socket-api-and-herdr-core-clients-and-sdks), for example [mitkox/dsh-herdr](https://github.com/mitkox/dsh-herdr) (reports agent state via OSC 7501), [glattziehen/hirte](https://github.com/glattziehen/hirte) (iPhone and iPad over SSH), and [nytafar/obsidian-herdr](https://github.com/nytafar/obsidian-herdr) (live terminal tabs in Obsidian). [DeevsDeevs/agent-system](https://github.com/DeevsDeevs/agent-system/tree/main/skills/hc) teaches agents to use hc.

## Security notes

- Core runs commands with your account's access. It is not a sandbox or a permission broker for agents. Anyone who can connect to its API can run commands, read and change files, and control its terminals with that access.
- On Unix, core listens on a local Unix socket, not a public TCP port. It creates its state and socket directories with mode 0700. There is no separate API password or per-client permission check.
- Do not expose the socket or forward the raw API to people you would not trust with a shell on that machine. Do not run core as root unless you intend to give its clients that access.
- `HC_SESSION` selects a separate core, terminals, and state directory. Sessions are not security boundaries: another process under the same account can select the same session.
- SSH handles login, host keys, and encryption for machines. A custom `--via` command must provide its own trust and transport. Adding a machine gives local clients access to that account's commands, files, and terminals.
- State lives in `~/.local/state/herdr-core/<session>/` on Unix. It is not encrypted, and terminal output and saved screens may contain secrets.
- Updates download a manifest from `releases.herdr.dev` and check the archive's SHA-256 against it. The manifest is not verified with a separate signing key. Use `hc update --from` only with a build you trust.
- Never `hc server stop` or restart a user's core unless asked; it affects every terminal. For tests, use their own `HC_SESSION` and scratch XDG paths.

Details: [Security](https://github.com/herdrdev/herdr-core/blob/v0.1.20/docs/security.md).

## Related guides

[Agent workflows](./agent-workflows.md), [Herdr app](./herdr-app.md), [Socket API](./socket-api.md), [Configuration](./configuration.md), [Integrations](./integrations.md).
