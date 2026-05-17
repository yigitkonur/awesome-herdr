# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-herdr?label=last%20updated)

> A curated starting point for the **[Herdr](https://github.com/ogulcancelik/herdr)** ecosystem: tools, workflows, configs, clients, skills, and integrations for terminal-native agent multiplexing.

[Herdr](https://herdr.dev/) is an agent multiplexer that lives in your terminal. It gives agents and humans persistent workspaces, tabs, panes, status awareness, detach/reattach, remote attach, and a local Unix socket API for automation.

```sh
curl -fsSL https://herdr.dev/install.sh | sh
herdr
```

This list tracks Herdr itself and projects that build on Herdr's core primitives: workspaces, tabs, panes, persistent sessions, agent state, CLI wrappers, and the local socket API.

---

## Contents

- [Start Here](#start-here)
- [Featured Project](#featured-project)
- [Official Herdr](#official-herdr)
- [Configuration](#configuration)
- [Socket API & Clients](#socket-api--clients)
- [Agent Skills & Workflows](#agent-skills--workflows)
- [Agent Integrations](#agent-integrations)
- [Terminal UX & Keymaps](#terminal-ux--keymaps)
- [Pi Ecosystem](#pi-ecosystem)
- [Reference Docs](#reference-docs)
- [Release Notes](#release-notes)
- [Build Your Own](#build-your-own)
- [Contributing](#contributing)
- [Related](#related)

---

## Start Here

| Goal | Go to |
|---|---|
| Make Ghostty + Herdr feel native on macOS | Featured Project |
| Learn Herdr's core model | Official Herdr |
| Configure keybindings, themes, notifications, and sessions | Configuration |
| Build socket-driven tools and agents | Socket API & Clients |
| Teach agents to use Herdr directly | Agent Skills & Workflows |
| Wire Claude, Codex, Pi, or OpenCode into Herdr | Agent Integrations |
| Track recent compatibility changes | Release Notes |
| Add a project to this list | Contributing |

---

## Featured Project

The first featured project is intentionally the one that turns Herdr into a macOS-native feeling daily driver.

- [yigitkonur/native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd) - Make Ghostty + Herdr navigation feel native to macOS and Chrome-style tab workflows. Patches Ghostty safely, configures Herdr keybindings, supports install/uninstall flags, includes a purple glass preset, and targets Herdr `0.5.10+` indexed keybinds. `TypeScript`.

---

## Official Herdr

- [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr) - Agent multiplexer that lives in your terminal. Provides persistent sessions, workspaces, tabs, panes, mouse-native TUI behavior, local or remote attach, direct terminal attach, agent status detection, integrations, and a Unix socket API. `Rust`.
- [herdr.dev](https://herdr.dev/) - Official landing page with install command, comparison against tmux/gui managers, remote/thin-client overview, supported agents, and socket API examples.
- [Herdr Releases](https://github.com/ogulcancelik/herdr/releases) - Current release stream. `v0.5.10` added indexed keybind families, hook-owned custom status labels, terminal-backed agent commands/socket methods, direct terminal attach, `ui.prompt_new_tab_name = false`, and `keys.edit_scrollback`.

---

## Configuration

- [CONFIGURATION.md](https://github.com/ogulcancelik/herdr/blob/master/CONFIGURATION.md) - Official reference for `~/.config/herdr/config.toml`, live reload, keybindings, indexed shortcuts, command keybindings, themes, UI options, notifications, sounds, experimental flags, advanced scrollback, logs, and environment variables.

This repo also includes a compact [configuration field guide](./docs/configuration.md) organized around what plugin authors and power users usually need first.

Key configuration areas:

| Area | Why it matters |
|---|---|
| `[keys]` | Prefix mode, direct terminal-mode jumps, pane focus, tab/workspace navigation, resize, zoom, and custom command entrypoints |
| `[keys.indexed]` | Number-key families for direct workspace, tab, or visible-agent jumps |
| `[[keys.command]]` | Prefix-mode commands that launch detached shell helpers or temporary panes |
| `[ui]` | Sidebar width, mouse capture, close confirmation, promptless tab names, agent labels, and panel scope |
| `[ui.toast]` / `[ui.sound]` | Background notifications and per-agent sound policy |
| `[experimental]` | Nested Herdr launches and local Kitty graphics rendering |
| `[advanced]` | Per-pane retained scrollback size |

---

## Socket API & Clients

- [SOCKET_API.md](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md) - Official local Unix socket protocol. Uses newline-delimited JSON, request/response envelopes, long-lived `events.subscribe`, and methods for workspaces, tabs, panes, agents, terminals, waits, reads, and input.
- [54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client) - Lightweight Python client for Herdr's Unix socket API. Handles socket discovery, request envelopes, response parsing, typed errors, subscriptions, pane reads, waits, input, and raw `request()` access. `Python`.

For builder notes, see this repo's [socket API ecosystem guide](./docs/socket-api.md).

Socket ecosystem primitives:

| Primitive | Use it for |
|---|---|
| `workspace.*` | Create, list, focus, rename, and close project contexts |
| `tab.*` | Create, focus, rename, and close subcontexts inside a workspace |
| `pane.*` | Split panes, read output, send input, report agent state, wait for output, and close panes |
| `agent.*` | List, read, send to, rename, focus, and start terminal-backed agents |
| `events.subscribe` | Build watchers for workspace, tab, pane, output, and agent-status changes |

Direct terminal attachment is exposed through CLI commands such as `herdr agent attach <target>` and `herdr terminal attach <terminal_id>`. Check the upstream socket reference for the exact raw method surface before implementing a client.

---

## Agent Skills & Workflows

- [ogulcancelik/herdr/SKILL.md](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) - Official reusable skill for agents already running inside Herdr. Teaches agents to create workspaces/tabs, split panes, run commands, read output, wait for text, wait for agent status, and spawn helper agents.
- [hcaiano/skills](https://github.com/hcaiano/skills) - Personal agent skills for Claude, Codex, and other runtimes. Includes `herdr-pair`, a collaboration skill for pairing Claude and Codex as peer agents inside Herdr. `Python`.

For recipes, see this repo's [agent workflow guide](./docs/agent-workflows.md).

Useful Herdr skill capabilities:

| Capability | Herdr command family |
|---|---|
| See what other panes and agents are doing | `workspace list`, `tab list`, `pane list`, `agent list` |
| Start helper panes | `pane split`, `pane run`, `pane send-input` |
| Watch logs or test output | `pane read`, `wait output` |
| Wait for another agent | `wait agent-status --status done` |
| Keep context separated | `workspace create`, `tab create` |

---

## Agent Integrations

- [INTEGRATIONS.md](https://github.com/ogulcancelik/herdr/blob/master/INTEGRATIONS.md) - Official integration guide for Pi, Claude Code, Codex, and OpenCode. Built-in installers forward semantic state such as `working`, `blocked`, and `idle` over the local socket API when the agent exposes useful hooks.

For implementation notes, see this repo's [integration guide](./docs/integrations.md).

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

---

## Terminal UX & Keymaps

This category is for terminal-side polish: Ghostty routes, native-feeling tab behavior, glass themes, reliable modifier handling, and Herdr profiles that do not require every user to hand-edit `config.toml`.

Start with the featured project above for the current Ghostty + Herdr shortcut pack.

---

## Pi Ecosystem

- [justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync) - Pi extension that syncs the Pi session name to the active Herdr tab label on resume or agent start. Only activates inside Herdr-managed panes via `HERDR_ENV=1`. `TypeScript`.

---

## Reference Docs

This repo includes local guides for:

| Guide | Covers |
|---|---|
| [Configuration](./docs/configuration.md) | Config file location, reload model, keybindings, themes, UI, notifications, logs |
| [Socket API](./docs/socket-api.md) | Protocol shape, method families, reads, waits, events, client-library checklist |
| [Integrations](./docs/integrations.md) | Built-in integrations, hook paths, env vars, custom integration checklist |
| [Agent Workflows](./docs/agent-workflows.md) | Worker panes, pair programming, watcher panes, waits, safety notes |
| [Curation](./docs/curation.md) | Inclusion rules, entry format, category policy |

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

Source: [Herdr releases](https://github.com/ogulcancelik/herdr/releases). Last reviewed: 2026-05-17.

---

## Build Your Own

Good Herdr ecosystem projects usually do one of these:

| Project type | Start with |
|---|---|
| Shortcut/config pack | `CONFIGURATION.md`, `[keys]`, `[keys.indexed]`, Ghostty key routing |
| Agent skill | `SKILL.md`, `HERDR_ENV=1`, CLI wrappers, `pane read`, `wait output` |
| Client library | `SOCKET_API.md`, socket discovery, request envelopes, subscriptions |
| Hook integration | `INTEGRATIONS.md`, `pane.report_agent`, semantic status labels |
| Workflow orchestrator | Workspaces/tabs/panes, `pane run`, `wait agent-status`, `events.subscribe` |

Submission quality bar:

1. Public repository with a README.
2. Uses Herdr directly or teaches/configures Herdr behavior.
3. Explains install/setup clearly.
4. States which Herdr version or feature family it relies on.
5. Avoids claiming official status unless it is in `ogulcancelik/herdr`.

---

## Contributing

Pull requests are welcome. Read [CONTRIBUTING.md](./CONTRIBUTING.md) and [docs/curation.md](./docs/curation.md) before adding a project.

Entry format:

```md
- [owner/repo](https://github.com/owner/repo) - Neutral, specific description that explains the Herdr integration surface and who should use it. `Language`
```

Keep entries factual. Avoid hype words, affiliate links, generated filler, and unmaintained private repos.

## Related

- [awesome-cmux](https://github.com/yigitkonur/awesome-cmux) - Similar ecosystem index for cmux.
- [awesome](https://github.com/sindresorhus/awesome) - The canonical awesome-list convention.
