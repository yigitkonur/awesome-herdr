# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-herdr?label=last%20updated)

> A curated index of the **[Herdr](https://github.com/ogulcancelik/herdr)** ecosystem: forks, clients, MCP servers, skills, hooks, and workflow tools built around the terminal-native agent multiplexer.

[Herdr](https://herdr.dev/) lives in your terminal and gives agents and humans persistent workspaces, tabs, panes, status awareness, detach/reattach, remote attach, and a local Unix socket API for automation.

```sh
curl -fsSL https://herdr.dev/install.sh | sh
herdr
```

This list tracks Herdr itself plus projects that build on its primitives: workspaces, tabs, panes, persistent sessions, agent state, CLI wrappers, hooks, and the local socket API.

---

## Contents

- [Project Index](#project-index)
- [Find by Goal](#find-by-goal)
- [Categories](#categories)
  - [Core](#core)
  - [Socket Clients & Libraries](#socket-clients--libraries)
  - [MCP Servers](#mcp-servers)
  - [Agent Skills & Plugins](#agent-skills--plugins)
  - [Worktree & Workflow Orchestration](#worktree--workflow-orchestration)
  - [Session Persistence](#session-persistence)
  - [Pi Integrations](#pi-integrations)
  - [Terminal UX & Keymaps](#terminal-ux--keymaps)
  - [Work in Progress](#work-in-progress)
- [Resources](#resources)
- [Herdr Primitives](#herdr-primitives)
- [Release Notes](#release-notes)
- [Build Your Own](#build-your-own)
- [Contributing](#contributing)
- [Related](#related)

---

## Project Index

Every actively maintained project in one scannable table. Categories below give the longer descriptions.

| Project | Category | Use it for | Lang |
|---|---|---|---|
| [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) | Core | Run the terminal-native agent multiplexer | `Rust` |
| [masakirocorp/hako](https://github.com/masakirocorp/hako) | Core fork | Herdr fork with separate binary, config, and `HAKO_ENV` namespace | `Rust` |
| [54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client) | Socket client | Build Python tools against the Unix socket API | `Python` |
| [rbb/herdr-cursor](https://github.com/rbb/herdr-cursor) | Socket bridge | Report Cursor SDK agent state to Herdr | `TypeScript` |
| [eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp) | MCP server | Drive Herdr from any MCP-compatible AI client | `Rust` |
| [hcaiano/skills](https://github.com/hcaiano/skills) | Agent skills | Personal skills for Claude, Codex, and peers in Herdr | `Python` |
| [msadig/herdr-peer-agents-skill](https://github.com/msadig/herdr-peer-agents-skill) | Agent skill | Spawn and orchestrate peer agents in adjacent panes | `Shell` |
| [yigitkonur/claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin) | Claude Code plugin | Drive a Codex sub-agent from Claude Code through a Herdr pane with a JSON verdict | `Python` |
| [noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr) | Worktree hook | Map git worktree lifecycle to Herdr tabs and workspaces | `Shell` |
| [SecretAardvark/pi-overseer](https://github.com/SecretAardvark/pi-overseer) | Pi orchestrator | Run role-based Pi agents across Herdr workspaces and `jj` worktrees | `TypeScript` |
| [nickmaglowsch/herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore) | Session manager | Snapshot and restore layout + Claude Code session IDs | `Python` |
| [justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync) | Pi extension | Sync Pi session names into Herdr tab labels | `TypeScript` |
| [yigitkonur/native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd) | Keymaps | Native macOS shortcuts in Ghostty + Herdr | `TypeScript` |

Work-in-progress entries below the bar are listed in [Work in Progress](#work-in-progress).

---

## Find by Goal

| If you want to... | Go to |
|---|---|
| Install the multiplexer | [Core](#core) |
| Try the Masakiro Corp product fork | [Core](#core) |
| Build socket-driven tools in Python | [Socket Clients & Libraries](#socket-clients--libraries) |
| Surface a Cursor agent's state in Herdr | [Socket Clients & Libraries](#socket-clients--libraries) |
| Control Herdr from Claude Desktop / Cursor via MCP | [MCP Servers](#mcp-servers) |
| Teach an agent to use Herdr | [Agent Skills & Plugins](#agent-skills--plugins) |
| Delegate work between peer agents in panes | [Agent Skills & Plugins](#agent-skills--plugins) |
| Drive a Codex sub-agent from Claude Code via Herdr | [Agent Skills & Plugins](#agent-skills--plugins) |
| Pair git worktrees with Herdr tabs | [Worktree & Workflow Orchestration](#worktree--workflow-orchestration) |
| Orchestrate role-based Pi workers | [Worktree & Workflow Orchestration](#worktree--workflow-orchestration) |
| Restore Claude conversations across reboots | [Session Persistence](#session-persistence) |
| Sync Pi session names to tab labels | [Pi Integrations](#pi-integrations) |
| Make Ghostty + Herdr feel macOS-native | [Terminal UX & Keymaps](#terminal-ux--keymaps) |
| Read the upstream protocol docs | [Resources](#resources) |
| Understand configuration and socket concepts | [Herdr Primitives](#herdr-primitives) |
| Add a project | [Contributing](#contributing) |

---

## Categories

### Core

The multiplexer and downstream forks.

- [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) - Agent multiplexer that lives in your terminal. Provides persistent sessions, workspaces, tabs, panes, mouse-native TUI behavior, local or remote attach, direct terminal attach, agent status detection, integrations, and a Unix socket API. `Rust`.
- [masakirocorp/hako](https://github.com/masakirocorp/hako) - Product fork of Herdr by Masakiro Corp. Same primitives (workspaces, tabs, panes, sockets, named sessions, agent state sidebar) under the `hako` binary, `~/.config/hako/config.toml`, and `HAKO_ENV=1`. Supports Claude Code, Codex, Pi, Droid, Amp, OpenCode, Grok CLI, and Hermes. `Rust`.

### Socket Clients & Libraries

Direct consumers of Herdr's local Unix socket and CLI surface.

- [54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client) - Lightweight Python client for Herdr's Unix socket API. Handles socket discovery, request envelopes, response parsing, typed errors, subscriptions, pane reads, waits, input, and raw `request()` access. `Python`.
- [rbb/herdr-cursor](https://github.com/rbb/herdr-cursor) - CLI shim that wraps the `@cursor/sdk` local runtime and reports Cursor agent lifecycle (`idle`/`working`/`blocked`) to Herdr via `pane.report_agent` and `pane.release_agent` socket calls. Reads `HERDR_ENV`, `HERDR_SOCKET_PATH`, and `HERDR_PANE_ID`; design-stage as of 2026-05. `TypeScript`.

### MCP Servers

Expose Herdr to AI clients that speak the Model Context Protocol.

- [eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp) - MCP server that wraps the `herdr` CLI and exposes 21 tools across discovery, lifecycle, read, write, and synchronize. Adds a recipe engine with `{{ stepId.result.path }}` interpolation, an optional HTTP bridge, and a React-based browser playground. `Rust`.

### Agent Skills & Plugins

Skill files, Claude Code plugins, and helpers that teach agents how to use Herdr from inside a pane.

- [hcaiano/skills](https://github.com/hcaiano/skills) - Personal agent skills for Claude, Codex, and other runtimes. Includes `herdr-pair`, a collaboration skill for pairing Claude and Codex as peer agents inside Herdr. `Python`.
- [msadig/herdr-peer-agents-skill](https://github.com/msadig/herdr-peer-agents-skill) - `SKILL.md` plus a shell wrapper that teaches Claude, Pi, and Codex how to spawn, prompt, and read peer agents via `herdr agent start/send/wait/read` and `herdr pane split/run/send-keys`. Includes a manual-split fallback when agent detection races. `Shell`.
- [yigitkonur/claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin) - Claude Code plugin (installed as `herdr-claude-plugin`) that drives a Codex sub-agent end-to-end through a Herdr pane, tab, or fresh workspace and returns one JSON verdict per turn — no screen-scraping, no status polling. Handles completion vs. question disambiguation, long-plan capture, spawn-mode selection, and optional `--worktree` isolation; vendors `herdr-python-client` and keys sessions by stable `terminal_id`. `Python`.

### Worktree & Workflow Orchestration

Bridges between external workflow tools (`git-wt`, `jj`, Pi roles) and Herdr's workspace/tab/pane layout.

- [noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr) - `git-wt.plugin.v0` adapter that maps worktree lifecycle events (`worktree-created`, `worktree-removed`, `focus`, `list`) to `herdr workspace create`, `herdr tab create/close/focus`, and pane lookup by `cwd`. Pure Bash with `yq`; no Node, Python, or compiled deps. `Shell`.
- [SecretAardvark/pi-overseer](https://github.com/SecretAardvark/pi-overseer) - Pi extension that orchestrates role-differentiated worker agents (overseer, implementer, tester, reviewer, researcher) across Herdr workspaces and Jujutsu worktrees. Spawns workers with `herdr agent start --workspace ... --split right`, enforces per-role command allowlists, and persists task/agent state under `.pi/overseer/`. `TypeScript`.

### Session Persistence

Tools that survive Herdr restarts and reboots.

- [nickmaglowsch/herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore) - Zsh wrapper plus Python script pair that snapshots workspace, tab, and pane layout (along with per-pane Claude Code `--session-id` values) on clean shutdown, then replays them via `claude --resume <session-id>` on next launch. Stores state under `~/.config/herdr/restore/`. `Python`.

### Pi Integrations

Pi-specific extensions and adapters.

- [justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync) - Pi extension that syncs the Pi session name to the active Herdr tab label on resume or agent start. Only activates inside Herdr-managed panes via `HERDR_ENV=1`. `TypeScript`.
- See also: [SecretAardvark/pi-overseer](#worktree--workflow-orchestration) for multi-role Pi orchestration.

### Terminal UX & Keymaps

Terminal-side polish: Ghostty routing, native-feeling tab behavior, themes, modifier handling, and config patchers.

- [yigitkonur/native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd) - Safe Ghostty + Herdr config patcher for macOS-native shortcut behavior, including `cmd+t`, `cmd+n`, `cmd+w`, `cmd+1..9`, `ctrl+tab`, and `ctrl+option+tab`. `TypeScript`.

### Work in Progress

Repositories that have been announced or scaffolded but not yet usable. Listed here so submitters know they exist, without endorsing them as ready.

- [shippy/raycast-herdr](https://github.com/shippy/raycast-herdr) - Raycast private-store scaffold intended to add Herdr control commands to Raycast. As of 2026-05 the `extensions/` directory is empty; only the build-and-publish workflow is wired up. `YAML`.

---

## Resources

Official Herdr resources:

| Resource | Covers |
|---|---|
| [herdr.dev](https://herdr.dev/) | Install command, overview, comparison against tmux/gui managers, remote attach, supported agents, and socket examples |
| [CONFIGURATION.md](https://github.com/ogulcancelik/herdr/blob/master/CONFIGURATION.md) | `~/.config/herdr/config.toml`, live reload, keybindings, indexed shortcuts, commands, themes, UI, notifications, sounds, scrollback, logs |
| [SOCKET_API.md](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md) | Newline-delimited JSON socket protocol, request envelopes, events, workspace/tab/pane/agent methods, reads, waits, and input |
| [INTEGRATIONS.md](https://github.com/ogulcancelik/herdr/blob/master/INTEGRATIONS.md) | Built-in integrations for Pi, Claude Code, Codex, and OpenCode |
| [SKILL.md](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) | Reusable skill instructions for agents already running inside Herdr |
| [Herdr Releases](https://github.com/ogulcancelik/herdr/releases) | Current release stream and compatibility changes |

Local guides in this repo:

| Guide | Covers |
|---|---|
| [Configuration](./docs/configuration.md) | Config file location, reload model, keybindings, themes, UI, notifications, logs |
| [Socket API](./docs/socket-api.md) | Protocol shape, method families, reads, waits, events, client-library checklist |
| [Integrations](./docs/integrations.md) | Built-in integrations, hook paths, env vars, custom integration checklist |
| [Agent Workflows](./docs/agent-workflows.md) | Worker panes, pair programming, watcher panes, waits, safety notes |
| [Curation](./docs/curation.md) | Inclusion rules, entry format, category policy |

---

## Herdr Primitives

These are the Herdr concepts most ecosystem projects build on.

### Configuration

| Area | Why it matters |
|---|---|
| `[keys]` | Prefix mode, direct terminal-mode jumps, pane focus, tab/workspace navigation, resize, zoom, and custom command entrypoints |
| `[keys.indexed]` | Number-key families for direct workspace, tab, or visible-agent jumps |
| `[[keys.command]]` | Prefix-mode commands that launch detached shell helpers or temporary panes |
| `[ui]` | Sidebar width, mouse capture, close confirmation, promptless tab names, agent labels, and panel scope |
| `[ui.toast]` / `[ui.sound]` | Background notifications and per-agent sound policy |
| `[experimental]` | Nested Herdr launches and local Kitty graphics rendering |
| `[advanced]` | Per-pane retained scrollback size |

### Socket API

| Primitive | Use it for |
|---|---|
| `workspace.*` | Create, list, focus, rename, and close project contexts |
| `tab.*` | Create, focus, rename, and close subcontexts inside a workspace |
| `pane.*` | Split panes, read output, send input, report agent state, wait for output, and close panes |
| `agent.*` | List, read, send to, rename, focus, and start terminal-backed agents |
| `events.subscribe` | Build watchers for workspace, tab, pane, output, and agent-status changes |

Direct terminal attachment is exposed through CLI commands such as `herdr agent attach <target>` and `herdr terminal attach <terminal_id>`. Check the upstream socket reference for the exact raw method surface before implementing a client.

### Integrations

Built-in install commands:

```sh
herdr integration install pi
herdr integration install claude
herdr integration install codex
herdr integration install opencode
```

Important integration paths and variables:

| Runtime | Herdr integration surface |
|---|---|
| Pi | `~/.pi/agent/extensions/herdr-agent-state.ts`, `$PI_CODING_AGENT_DIR` |
| Claude Code | `~/.claude/hooks/herdr-agent-state.sh`, `$CLAUDE_CONFIG_DIR` |
| Codex | `~/.codex/herdr-agent-state.sh`, `$CODEX_HOME` |
| OpenCode | `~/.config/opencode/plugins/herdr-agent-state.js` |

### Agent Workflows

| Capability | Herdr command family |
|---|---|
| See what other panes and agents are doing | `workspace list`, `tab list`, `pane list`, `agent list` |
| Start helper panes | `pane split`, `pane run`, `pane send-input` |
| Watch logs or test output | `pane read`, `wait output` |
| Wait for another agent | `wait agent-status --status done` |
| Keep context separated | `workspace create`, `tab create` |

---

## Release Notes

Herdr is moving quickly. For ecosystem authors, the most important recent changes are:

| Release | Ecosystem impact |
|---|---|
| `v0.5.10` | Indexed keybind families under `[keys.indexed]`, hook-owned custom status labels, terminal-backed agent socket methods, direct terminal attach, promptless tab creation, `keys.edit_scrollback`, and `keys.zoom` rename |
| `v0.5.9` | Experimental Kitty graphics, system toast delivery, light theme variants, and `[experimental]` config migration |
| `v0.5.8` | Manual pane labels, `pane.rename`, pane-border agent labels, and integration status checks |
| `v0.5.7` | ANSI-formatted pane reads for CLI/socket feedback loops |
| `v0.5.6` | `herdr --remote <ssh-target>` and no-focus defaults for created workspace/tab/pane wrappers |
| `v0.5.3` | Named persistent sessions with separate sockets/runtime state and shared global config |

Source: [Herdr releases](https://github.com/ogulcancelik/herdr/releases). Last reviewed: 2026-05-25.

---

## Build Your Own

Good Herdr ecosystem projects usually do one of these:

| Project type | Start with | Example in this list |
|---|---|---|
| Shortcut/config pack | `CONFIGURATION.md`, `[keys]`, `[keys.indexed]`, Ghostty key routing | [native-shortcuts-herd](#terminal-ux--keymaps) |
| Socket client library | `SOCKET_API.md`, socket discovery, request envelopes, subscriptions | [herdr-python-client](#socket-clients--libraries) |
| Socket bridge for an editor/agent SDK | `pane.report_agent`, `pane.release_agent`, `HERDR_ENV` / `HERDR_PANE_ID` | [herdr-cursor](#socket-clients--libraries) |
| MCP server | `herdr` CLI subcommands, MCP stdio + HTTP transports | [herdr-mcp](#mcp-servers) |
| Agent skill | `SKILL.md`, `HERDR_ENV=1`, CLI wrappers, `pane read`, `wait output` | [herdr-peer-agents-skill](#agent-skills--plugins) |
| Hook integration | `INTEGRATIONS.md`, `pane.report_agent`, semantic status labels | [git-wt-herdr](#worktree--workflow-orchestration) |
| Workflow orchestrator | Workspaces/tabs/panes, `pane run`, `wait agent-status`, `events.subscribe` | [pi-overseer](#worktree--workflow-orchestration) |
| Session manager | CLI snapshot of `workspace list` / `tab list` / `agent list`, per-agent resume IDs | [herdr-session-restore](#session-persistence) |

Submission quality bar:

1. Public repository with a working README.
2. Uses Herdr directly or teaches/configures Herdr behavior.
3. Explains install/setup clearly.
4. States which Herdr version or feature family it relies on.
5. Avoids claiming official status unless it lives in `ogulcancelik/herdr`.

---

## Contributing

Pull requests are welcome. Read [CONTRIBUTING.md](./CONTRIBUTING.md) and [docs/curation.md](./docs/curation.md) before adding a project.

Entry format:

```md
- [owner/repo](https://github.com/owner/repo) - Neutral, specific description that explains the Herdr integration surface and who should use it. `Language`
```

Keep entries factual. Avoid hype words, affiliate links, generated filler, and unmaintained private repos. Scaffold-only repos belong in [Work in Progress](#work-in-progress), not the main index.

## Related

- [awesome-cmux](https://github.com/yigitkonur/awesome-cmux) - Similar ecosystem index for cmux.
- [awesome](https://github.com/sindresorhus/awesome) - The canonical awesome-list convention.
