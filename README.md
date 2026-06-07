# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-herdr?label=last%20updated)

> A curated index of the **[Herdr](https://github.com/ogulcancelik/herdr)** ecosystem — the tools people build on top of the terminal-native agent multiplexer.

[Herdr](https://herdr.dev/) is tmux for AI agents. It gives agents and humans persistent workspaces, tabs, and panes; tracks what every agent is doing; survives detach/reattach and remote attach; and exposes a local Unix socket so anything can drive it.

```sh
curl -fsSL https://herdr.dev/install.sh | sh
herdr
```

Everything below builds on those primitives — running fleets of agents side by side, wiring editors and MCP clients into panes, persisting sessions, and shaping the terminal around them.

---

## Contents

- [At a glance](#at-a-glance)
- [Core & forks](#core--forks)
- [Run & orchestrate agents](#run--orchestrate-agents)
- [Connect over socket & MCP](#connect-over-socket--mcp)
- [Persist & restore sessions](#persist--restore-sessions)
- [Worktrees & terminal UX](#worktrees--terminal-ux)
- [Work in progress](#work-in-progress)
- [Resources](#resources)
- [Reference](#reference)
- [Contributing](#contributing)
- [Related](#related)

---

## At a glance

| Project | What it gives you |
|---|---|
| [herdr](https://github.com/ogulcancelik/herdr) ![Rust](https://img.shields.io/badge/-Rust-DEA584?logo=rust&logoColor=black&style=flat-square) | The multiplexer itself |
| [hako](https://github.com/masakirocorp/hako) ![Rust](https://img.shields.io/badge/-Rust-DEA584?logo=rust&logoColor=black&style=flat-square) | A standalone fork with its own namespace |
| [claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | Claude Code driving Codex in another pane |
| [herdr-peer-agents-skill](https://github.com/msadig/herdr-peer-agents-skill) ![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnubash&logoColor=white&style=flat-square) | Agents that spawn and talk to peers |
| [skills](https://github.com/hcaiano/skills) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | Pairing Claude and Codex as peers |
| [pi-overseer](https://github.com/SecretAardvark/pi-overseer) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square) | Role-based Pi agent fleets |
| [herdr-python-client](https://github.com/54rt1n/herdr-python-client) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | A Python client for the socket API |
| [herdr-cursor](https://github.com/rbb/herdr-cursor) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square) | Cursor agent state shown in Herdr |
| [herdr-mcp](https://github.com/eugeneb50/herdr-mcp) ![Rust](https://img.shields.io/badge/-Rust-DEA584?logo=rust&logoColor=black&style=flat-square) | Drive Herdr from any MCP client |
| [herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) | Layout + Claude sessions across reboots |
| [git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr) ![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnubash&logoColor=white&style=flat-square) | Git worktrees mapped to tabs |
| [pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square) | Pi session names on your tabs |
| [native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd) ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square) | macOS-native keys in Ghostty + Herdr |

---

## Core & forks

**[ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)** ![Rust](https://img.shields.io/badge/-Rust-DEA584?logo=rust&logoColor=black&style=flat-square)

The multiplexer everything here builds on. It keeps your agents in persistent, mouse-native workspaces with tabs and panes, shows you at a glance which ones are working, idle, or blocked, and lets you walk away and reattach — locally or over SSH. The Unix socket API is what makes the rest of this list possible.

**[masakirocorp/hako](https://github.com/masakirocorp/hako)** ![Rust](https://img.shields.io/badge/-Rust-DEA584?logo=rust&logoColor=black&style=flat-square)

A standalone fork of Herdr by Masakiro Corp, shipping as its own `hako` binary with a separate config and `HAKO_ENV` namespace so it can run alongside upstream. Useful if you want a product-branded build or to track a different release line.

---

## Run & orchestrate agents

The headline use: more than one agent working at once, in panes you can watch.

**[yigitkonur/claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin)** ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)

Lets a Claude Code session hand a job to a Codex agent in an adjacent pane and get back a clean done / question / blocked answer each turn — no screen-scraping, no status polling. It can spawn the helper in a pane, a tab, a fresh workspace, or an isolated worktree, which makes it the easy way to get two agents collaborating in one place.

**[msadig/herdr-peer-agents-skill](https://github.com/msadig/herdr-peer-agents-skill)** ![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnubash&logoColor=white&style=flat-square)

A skill that teaches Claude, Pi, or Codex to spawn a peer agent, prompt it, and read its output — so an agent can delegate the way you would. Includes a manual-split fallback for when agent detection races, so the workflow doesn't stall.

**[hcaiano/skills](https://github.com/hcaiano/skills)** ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)

A personal collection of agent skills, including `herdr-pair` for running Claude and Codex as collaborating peers inside Herdr. A good starting point if you want to see how a real pairing workflow is wired up before writing your own.

**[SecretAardvark/pi-overseer](https://github.com/SecretAardvark/pi-overseer)** ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square)

Turns a workspace into a small team: an overseer hands work to implementer, tester, reviewer, and researcher agents, each in its own pane and Jujutsu worktree. Per-role command allowlists keep workers in their lane, and task state is persisted so a run survives a restart. For anyone who wants structured, multi-agent execution rather than one chat at a time.

---

## Connect over socket & MCP

Wiring outside tools — Python code, editors, MCP clients — into Herdr.

**[54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client)** ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)

A lightweight Python client for Herdr's Unix socket, so you can script the multiplexer instead of pressing keys. It handles the tedious parts — socket discovery, request envelopes, typed errors, subscriptions, pane reads and waits — and still gives you raw `request()` access when you need it. The fastest way to build your own automation.

**[rbb/herdr-cursor](https://github.com/rbb/herdr-cursor)** ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square)

A small shim around the Cursor SDK runtime that reports a Cursor agent's idle / working / blocked state back to Herdr, so a Cursor session shows up in your status sidebar like any native agent. Design-stage as of 2026-05.

**[eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp)** ![Rust](https://img.shields.io/badge/-Rust-DEA584?logo=rust&logoColor=black&style=flat-square)

An MCP server that exposes Herdr to any MCP-speaking client — Claude Desktop, Cursor, and friends — as a set of tools for discovering, launching, reading, and writing panes. A recipe engine chains those calls into reusable flows, with an optional HTTP bridge and a browser playground for trying them out.

---

## Persist & restore sessions

**[nickmaglowsch/herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore)** ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)

Snapshots your whole layout — workspaces, tabs, panes — along with each pane's Claude Code session ID on clean shutdown, then replays it on next launch so your conversations resume exactly where they were. The answer to losing your agent setup to a reboot.

---

## Worktrees & terminal UX

Bridging external tools to Herdr's layout, and making the terminal itself feel right.

**[noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr)** ![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnubash&logoColor=white&style=flat-square)

Maps your git worktree lifecycle onto Herdr — creating a worktree spins up a matching workspace and tab, removing it tears them down, and focus follows you. Pure Bash with `yq`, no Node or Python, so it drops cleanly into an existing `git-wt` setup.

**[justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync)** ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square)

Keeps your Herdr tab labels in sync with Pi session names, so you can tell what each tab is doing at a glance instead of decoding generic titles. Only activates inside Herdr-managed panes.

**[yigitkonur/native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd)** ![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square)

A safe config patcher that makes Ghostty + Herdr respond to macOS-native shortcuts — `cmd+t`, `cmd+n`, `cmd+w`, `cmd+1..9`, and tab cycling — so the multiplexer feels like a native tabbed app instead of a prefix-key TUI.

---

## Work in progress

Announced or scaffolded, but not yet usable — listed so submitters know they exist, without endorsing them as ready.

**[shippy/raycast-herdr](https://github.com/shippy/raycast-herdr)** ![YAML](https://img.shields.io/badge/-YAML-CB171E?logo=yaml&logoColor=white&style=flat-square)

A Raycast extension meant to add Herdr control commands to Raycast. As of 2026-05 only the build-and-publish workflow is wired up; the `extensions/` directory is still empty.

---

## Resources

Official Herdr docs:

| Resource | Covers |
|---|---|
| [herdr.dev](https://herdr.dev/) | Install, overview, comparison vs tmux/GUI managers, remote attach, supported agents, socket examples |
| [CONFIGURATION.md](https://github.com/ogulcancelik/herdr/blob/master/CONFIGURATION.md) | Config file, live reload, keybindings, indexed shortcuts, commands, themes, UI, notifications, scrollback |
| [SOCKET_API.md](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md) | The newline-delimited JSON protocol — envelopes, events, workspace/tab/pane/agent methods, reads, waits, input |
| [INTEGRATIONS.md](https://github.com/ogulcancelik/herdr/blob/master/INTEGRATIONS.md) | Built-in integrations for Pi, Claude Code, Codex, and OpenCode |
| [SKILL.md](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) | Skill instructions for agents already running inside Herdr |
| [Releases](https://github.com/ogulcancelik/herdr/releases) | Current release stream and compatibility changes |

Local guides in this repo:

| Guide | Covers |
|---|---|
| [Configuration](./docs/configuration.md) | Config location, reload model, keybindings, themes, UI, notifications, logs |
| [Socket API](./docs/socket-api.md) | Protocol shape, method families, reads, waits, events, client-library checklist |
| [Integrations](./docs/integrations.md) | Built-in integrations, hook paths, env vars, custom integration checklist |
| [Agent Workflows](./docs/agent-workflows.md) | Worker panes, pair programming, watcher panes, waits, safety notes |

---

## Reference

**Primitives.** Nearly every project here builds on the same handful of ideas — `workspace.*`, `tab.*`, and `pane.*` for layout; `agent.*` for terminal-backed agents; and `events.subscribe` for watching status, output, and layout changes. Config lives in `~/.config/herdr/config.toml` (keys, indexed shortcuts, custom commands, UI, toasts, sounds), and integrations install with `herdr integration install <pi|claude|codex|opencode>`. The full surface — config areas, the raw socket methods, and the agent-workflow command families — is in [docs/](./docs) and the upstream [SOCKET_API.md](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md).

**Releases.** Herdr moves fast. The ecosystem-relevant recent additions are indexed keybind families (`[keys.indexed]`), terminal-backed agent socket methods, direct terminal attach, manual pane labels (`pane.rename`), and remote attach (`herdr --remote`). Always check the upstream [releases](https://github.com/ogulcancelik/herdr/releases) for the version your project depends on. *Last reviewed: 2026-05-25.*

**Building your own.** Most projects start from one primitive: a shortcut/config pack from `[keys]`, a socket client from `SOCKET_API.md`, an editor bridge via `pane.report_agent`, an MCP server over the CLI, a skill via `SKILL.md`, a hook integration via `INTEGRATIONS.md`, or an orchestrator over `pane run` + `wait agent-status` + `events.subscribe`. Pick the closest example above and read its source.

---

## Contributing

Pull requests welcome. Read [AGENTS.md](./AGENTS.md) for the entry format and rules, and [CONTRIBUTING.md](./CONTRIBUTING.md) for the PR checklist.

Entry format:

```md
- [owner/repo](https://github.com/owner/repo) - Specific description of the Herdr integration surface and who should use it.
```

The bar: a public repo with a working README, that uses or configures Herdr directly, explains its setup, and states which Herdr version or feature it relies on. Keep it factual — no hype words, affiliate links, generated filler, or unmaintained private repos. Don't claim official status unless it lives in `ogulcancelik/herdr`. Scaffold-only repos go in [Work in progress](#work-in-progress).

## Related

- [awesome-cmux](https://github.com/yigitkonur/awesome-cmux) - Similar ecosystem index for cmux.
- [awesome](https://github.com/sindresorhus/awesome) - The canonical awesome-list convention.
