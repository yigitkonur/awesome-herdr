# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-herdr?label=last%20updated)

> A curated index of the **[Herdr](https://github.com/ogulcancelik/herdr)** ecosystem — the tools people build on top of the terminal-native agent multiplexer.

[Herdr](https://herdr.dev/) is tmux for AI agents. It gives agents and humans persistent workspaces, tabs, and panes; tracks what every agent is doing; survives detach/reattach and remote attach; and exposes a local Unix socket so anything can drive it.

```sh
curl -fsSL https://herdr.dev/install.sh | sh
herdr
```

Everything below builds on those primitives — running fleets of agents side by side, wiring editors and MCP clients into panes, switching and restoring sessions, and shaping the terminal around them.

---

## Contents

- [At a glance](#at-a-glance)
- [Run & orchestrate agents](#run--orchestrate-agents)
- [Connect over socket & MCP](#connect-over-socket--mcp)
- [Editor integrations](#editor-integrations)
- [Sessions: switch & restore](#sessions-switch--restore)
- [Worktrees, config & terminal UX](#worktrees-config--terminal-ux)
- [Desktop apps & packaging](#desktop-apps--packaging)
- [Work in progress](#work-in-progress)
- [Resources](#resources)
- [Reference](#reference)
- [Contributing](#contributing)
- [Related](#related)

---

## At a glance

| Project | What it gives you |
|---|---|
| [claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin) ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square) | Claude Code driving Codex in another pane |
| [herdr-peer-agents-skill](https://github.com/msadig/herdr-peer-agents-skill) ![Shell](https://img.shields.io/badge/-4EAA25?logo=gnubash&logoColor=white&style=flat-square) | Agents that spawn and talk to peers |
| [skills](https://github.com/hcaiano/skills) ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square) | Pairing Claude and Codex as peers |
| [pi-overseer](https://github.com/SecretAardvark/pi-overseer) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | Role-based Pi agent fleets |
| [pi-herdr-workflow-kit](https://github.com/Jackliu-miaozi/pi-herdr-workflow-kit) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | Gated planner → coder → reviewer pipeline |
| [mcdonc-pi-herdr](https://github.com/mcdonc/mcdonc-pi-herdr) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | Background Pi tasks into panes & tabs |
| [herdr-python-client](https://github.com/54rt1n/herdr-python-client) ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square) | A Python client for the socket API |
| [herdr-mcp](https://github.com/eugeneb50/herdr-mcp) ![Rust](https://img.shields.io/badge/-DEA584?logo=rust&logoColor=black&style=flat-square) | Drive Herdr from any MCP client |
| [herdr-mesh](https://github.com/runchr-works/herdr-mesh) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | MCP tools for agent-to-agent orchestration |
| [herdr.nvim](https://github.com/devxplay/herdr.nvim) ![Lua](https://img.shields.io/badge/-2C2D72?logo=lua&logoColor=white&style=flat-square) | Neovim ↔ Herdr pane navigation |
| [herdr-cursor](https://github.com/rbb/herdr-cursor) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | Cursor agent state shown in Herdr |
| [switchr](https://github.com/ridho9/switchr) ![Go](https://img.shields.io/badge/-00ADD8?logo=go&logoColor=white&style=flat-square) | TUI session picker with pane tree |
| [herdrctx](https://github.com/j0urneyk/herdrctx) ![Go](https://img.shields.io/badge/-00ADD8?logo=go&logoColor=white&style=flat-square) | TUI to attach, stop, manage sessions |
| [herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore) ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square) | Layout + Claude sessions across reboots |
| [git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr) ![Shell](https://img.shields.io/badge/-4EAA25?logo=gnubash&logoColor=white&style=flat-square) | Git worktrees mapped to tabs |
| [superherd](https://github.com/SirTenzin/superherd) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | Bridge Superset workspaces into Herdr |
| [pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | Pi session names on your tabs |
| [native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd) ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square) | macOS-native keys in Ghostty + Herdr |
| [herdr-dotfiles](https://github.com/Taeyoung96/herdr-dotfiles) ![Shell](https://img.shields.io/badge/-4EAA25?logo=gnubash&logoColor=white&style=flat-square) | Drop-in config: prefix-free navigation |
| [herdr-menu-bar](https://github.com/hmu332233/herdr-menu-bar) ![Swift](https://img.shields.io/badge/-FA7343?logo=swift&logoColor=white&style=flat-square) | macOS menu-bar agent-status widget |
| [deepin-herdr](https://github.com/re2zero/deepin-herdr) ![C++](https://img.shields.io/badge/-00599C?logo=cplusplus&logoColor=white&style=flat-square) | Native Deepin Linux window for Herdr |
| [herdr-nix](https://github.com/AodhanHayter/herdr-nix) ![Nix](https://img.shields.io/badge/-5277C3?logo=nixos&logoColor=white&style=flat-square) | Nix flake, auto-updated, with binary cache |

---

## Run & orchestrate agents

The headline use: more than one agent working at once, in panes you can watch.

**[yigitkonur/claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin)** ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square)

Lets a Claude Code session hand a job to a Codex agent in an adjacent pane and get back a clean done / question / blocked verdict each turn — no screen-scraping, no status polling. It streams one verdict per state change, can spawn the helper in a pane, tab, fresh workspace, or isolated git worktree, and keys the session to a stable handle so it survives pane reshuffling. The easy way to get one agent driving another in the same workspace.

**[msadig/herdr-peer-agents-skill](https://github.com/msadig/herdr-peer-agents-skill)** ![Shell](https://img.shields.io/badge/-4EAA25?logo=gnubash&logoColor=white&style=flat-square)

A skill that teaches Claude, Pi, or Codex to spawn a named peer agent, prompt it, and read its output when it goes idle — so an agent can delegate the way you would. A shell wrapper smooths the rough edges, sending Codex's composer a second Enter and falling back to a manual pane split when `herdr agent start` loses the process before detection.

**[hcaiano/skills](https://github.com/hcaiano/skills)** ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square)

A personal skill collection whose `herdr-pair` skill runs Claude and Codex as co-equal peers in one Herdr tab: either can initiate, the other auto-joins, and they exchange structured task / review / question / accepted messages until both sign off. A solid reference for how a real peer-agent protocol — spawn checks, send verification, per-tab session isolation — is wired against the Herdr CLI.

**[SecretAardvark/pi-overseer](https://github.com/SecretAardvark/pi-overseer)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

Turns a workspace into a small team: an overseer hands work to implementer, tester, reviewer, and researcher agents, each in its own Herdr workspace and Jujutsu worktree. Every command a worker runs is checked against its role's allowlist — testers can run tests but not write files, pushes need a one-time human-approved token — and all task state persists under `.pi/overseer/` so a run survives a restart. For anyone who wants structured, guard-railed multi-agent execution rather than one chat at a time.

**[Jackliu-miaozi/pi-herdr-workflow-kit](https://github.com/Jackliu-miaozi/pi-herdr-workflow-kit)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

Turns Pi-in-Herdr into a gated pipeline: an orchestrator spawns planner, coder, and reviewer agents in their own panes, requires the plan to be approved before any code is written, and runs a review on each phase before it lands as its own commit. Handoffs pass through files under `.pi-herdr/` instead of terminal pastes, keeping long plans and diffs out of the input stream. For Pi users who want enforced plan-then-review structure over free-form agent runs.

**[mcdonc/mcdonc-pi-herdr](https://github.com/mcdonc/mcdonc-pi-herdr)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

A Pi extension that gives Pi's background-task and conversation-fork features a home in Herdr: `/bg` offloads the running task into a visible pane, and `/tab` forks the conversation into a new tab, both over the socket API. Long builds and parallel workstreams become first-class panes and tabs you can watch, instead of invisible background processes. For Pi users running inside Herdr who want their side-work surfaced, not hidden.

---

## Connect over socket & MCP

Wiring outside tools — Python code, MCP clients — into Herdr.

**[54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client)** ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square)

A zero-dependency Python client for Herdr's Unix socket, so you can script the multiplexer instead of pressing keys. It handles the tedious parts — socket discovery, request envelopes, typed errors, event subscriptions, pane reads and waits — with ten convenience helpers and a raw `request()` escape hatch validated against the full method surface. The fastest way to build your own automation.

**[eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp)** ![Rust](https://img.shields.io/badge/-DEA584?logo=rust&logoColor=black&style=flat-square)

An MCP server that exposes Herdr to any MCP-speaking client — Claude Desktop, Cursor, Claude Code — as 21 tools for discovering, launching, reading, and writing panes. A recipe engine chains those calls into reusable flows with `{{ step.result.path }}` variable passing, reachable over both MCP and an HTTP bridge, with a bundled React playground for trying them out by hand.

**[runchr-works/herdr-mesh](https://github.com/runchr-works/herdr-mesh)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

Another MCP server, this one tuned for agents coordinating agents: it hands any MCP-capable client tools to read another agent's pane, relay a message, hand off a task, spawn an agent, and wait on a result. It turns manual copy-paste between panes into one-sentence orchestration, and `herdr-mesh install` auto-registers itself with whichever agents (Claude Code, Codex, opencode) you have installed.

---

## Editor integrations

Bringing Herdr into the editor you already live in.

**[devxplay/herdr.nvim](https://github.com/devxplay/herdr.nvim)** ![Lua](https://img.shields.io/badge/-2C2D72?logo=lua&logoColor=white&style=flat-square) ![Rust](https://img.shields.io/badge/-DEA584?logo=rust&logoColor=black&style=flat-square)

Unifies pane navigation between Neovim and Herdr: the same `Ctrl+h/j/k/l` that moves between Vim splits flows straight into the adjacent Herdr pane when you hit an edge, and back again. A small Rust helper talks to the socket for focus, splits, and layout, and it coexists with vim-tmux-navigator — Neovim detects whether it's inside Herdr or tmux and routes accordingly. For Neovim users who want one set of muscle memory across editor and multiplexer.

**[rbb/herdr-cursor](https://github.com/rbb/herdr-cursor)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

A planned shim around the Cursor SDK runtime that would report a Cursor agent's idle / working / blocked state back to Herdr, so a Cursor session shows up in your status sidebar like any native agent. Design-stage as of 2026-05 — the repo is a detailed spec with no code written yet, but the integration it sketches is a clean one to watch.

---

## Sessions: switch & restore

Finding the session you want, attaching to it, and getting it all back after a reboot.

**[ridho9/switchr](https://github.com/ridho9/switchr)** ![Go](https://img.shields.io/badge/-00ADD8?logo=go&logoColor=white&style=flat-square)

A full-screen session picker for Herdr: it lists every session next to its workspace / tab / pane tree, and you attach to the one you want with a keypress. Wire it up as your terminal's startup command and it greets you on each new window; it also spots an incompatible daemon and offers an in-place restart. For anyone juggling several named sessions who wants a fast visual switchboard.

**[j0urneyk/herdrctx](https://github.com/j0urneyk/herdrctx)** ![Go](https://img.shields.io/badge/-00ADD8?logo=go&logoColor=white&style=flat-square)

A keyboard-driven TUI for the housekeeping side of sessions — attach, stop, delete, create, and search, without copying names out of `herdr session list`. It ships through a Homebrew tap with prebuilt macOS and Linux binaries and refuses to launch nested when you're already inside a Herdr pane. For developers managing sessions across many projects who want a faster daily driver than the raw CLI.

**[nickmaglowsch/herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore)** ![Python](https://img.shields.io/badge/-3776AB?logo=python&logoColor=white&style=flat-square)

Tags every Claude Code pane with a session ID, then snapshots your workspace / tab / cwd layout on a clean `herdr server stop` and replays it on the next cold boot — `claude --resume` and all — so your conversations come back where you left them. Claude-only and clean-shutdown-only by design, it's the answer to losing your agent setup to a reboot.

---

## Worktrees, config & terminal UX

Bridging external tools to Herdr's layout, and shaping the terminal itself.

**[noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr)** ![Shell](https://img.shields.io/badge/-4EAA25?logo=gnubash&logoColor=white&style=flat-square)

Maps your git worktree lifecycle onto Herdr — creating a worktree opens a focused tab at that directory, removing it closes the tab, and switching focus brings the right one forward. It's the reference implementation of the `git-wt.plugin.v0` contract, pure Bash with `yq` and no Node or Python, so it drops cleanly into an existing `git-wt` setup.

**[SirTenzin/superherd](https://github.com/SirTenzin/superherd)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

A CLI that bridges the Superset workspace manager into Herdr: from a Superset-imported repo, one command creates the worktree, opens it as a Herdr workspace, and mirrors Superset's setup terminals as live tabs. It drives the Herdr CLI for workspace and tab creation, forwards Ctrl-C into the Superset PTYs, and ejects the launching pane when it's done. For teams who run Superset (the agent-tooling one, not Apache Superset) alongside Herdr and want worktree setup automated end to end.

**[justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

Renames the active Herdr tab to match your Pi session name on resume or agent start, so you can tell what each tab is doing at a glance instead of decoding generic titles. It talks to the socket directly and only activates inside Herdr-managed panes, so it's safe to install globally and forget.

**[yigitkonur/native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd)** ![TypeScript](https://img.shields.io/badge/-3178C6?logo=typescript&logoColor=white&style=flat-square)

Patches Ghostty and Herdr together so `cmd+t`, `cmd+n`, `cmd+w`, `cmd+1..9`, and tab cycling behave the way they do in Chrome or Safari — no manual escape-sequence wiring. It routes the keys through a Ghostty sidecar file (never touching your main config), maps them to the matching Herdr actions, and keeps timestamped backups plus a clean uninstall path. macOS only.

**[Taeyoung96/herdr-dotfiles](https://github.com/Taeyoung96/herdr-dotfiles)** ![Shell](https://img.shields.io/badge/-4EAA25?logo=gnubash&logoColor=white&style=flat-square)

A drop-in Herdr `config.toml` built around prefix-free navigation: pane movement is mapped to bare `Shift+Alt+arrow` chords, the tmux-style prefix moves to `ctrl+space`, and it ships with the Catppuccin theme and a global agent panel. A one-command `install.sh` symlinks it in and backs up whatever was there — a clean, documented starting point for anyone who finds the default prefix-heavy bindings slow.

---

## Desktop apps & packaging

Running and installing Herdr outside the bare terminal.

**[hmu332233/herdr-menu-bar](https://github.com/hmu332233/herdr-menu-bar)** ![Swift](https://img.shields.io/badge/-FA7343?logo=swift&logoColor=white&style=flat-square)

A macOS menu-bar app that keeps your agents' states — working, idle, blocked, done — in the system status bar, so you don't have to keep the TUI on screen to know when one needs you. Agents are grouped by workspace in the dropdown, and clicking one can jump you straight to its pane. For Mac users running several agents who want ambient awareness without a foreground terminal.

**[re2zero/deepin-herdr](https://github.com/re2zero/deepin-herdr)** ![C++](https://img.shields.io/badge/-00599C?logo=cplusplus&logoColor=white&style=flat-square)

A native Deepin Linux / UOS app (Qt + the DTK toolkit) that launches Herdr inside an embedded terminal window — on first run it fetches the binary, starts the server if needed, and drops you into the client with theme-matched colors. It ships as a proper `.deb` maintained by a UnionTech developer, the straightforward way onto Herdr for Deepin desktops. (No README yet; the Debian packaging is the documentation.)

**[AodhanHayter/herdr-nix](https://github.com/AodhanHayter/herdr-nix)** ![Nix](https://img.shields.io/badge/-5277C3?logo=nixos&logoColor=white&style=flat-square)

A Nix flake that packages the Herdr CLI for macOS and Linux (Intel and ARM), so you can `nix run` it or wire it into a NixOS overlay or Home Manager config instead of reaching for Homebrew. An hourly GitHub Action watches upstream releases and bumps the version, hashes, and a public Cachix binary cache automatically — so the flake tracks Herdr with no manual upkeep. The canonical path for anyone on a declarative Nix setup.

---

## Work in progress

Announced or scaffolded, but not yet usable — listed so submitters know they exist, without endorsing them as ready.

**[shippy/raycast-herdr](https://github.com/shippy/raycast-herdr)** ![YAML](https://img.shields.io/badge/-CB171E?logo=yaml&logoColor=white&style=flat-square)

A Raycast extension meant to add Herdr control commands to Raycast. As of mid-2026 only the build-and-publish workflow is wired up; the `extensions/` directory is still an empty scaffold.

**[SuperInstance/herdr-cocapn](https://github.com/SuperInstance/herdr-cocapn)** ![Rust](https://img.shields.io/badge/-DEA584?logo=rust&logoColor=black&style=flat-square)

A Herdr fork that adds a fleet-management layer on top of CoCapn: each agent pane becomes a tiered "device," and deadband monitors auto-escalate work to a cloud agent under load, then de-escalate to save cost when it goes idle, with a crossfade handoff so nothing drops mid-transition. A genuinely novel idea — but not buildable as shipped, since its `cocapn-core` dependency is referenced by a hardcoded local path rather than bundled.

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

**Releases.** Herdr moves fast — it's in the `v0.6.x` line as of mid-2026. The capabilities most projects here lean on are indexed keybind families (`[keys.indexed]`), terminal-backed agent socket methods, direct terminal attach, manual pane labels (`pane.rename`), and remote attach (`herdr --remote`). Always check the upstream [releases](https://github.com/ogulcancelik/herdr/releases) for the version your project depends on.

**Building your own.** Most projects start from one primitive: a config/keymap pack from `[keys]`, a socket client from `SOCKET_API.md`, an editor bridge via `pane.report_agent`, an MCP server over the CLI, a skill via `SKILL.md`, a hook integration via `INTEGRATIONS.md`, or an orchestrator over `pane run` + `wait agent-status` + `events.subscribe`. Pick the closest example above and read its source.

---

## Contributing

Pull requests welcome. See [AGENTS.md](./AGENTS.md) for the entry format, sections, language badges, and the inclusion bar, and [CONTRIBUTING.md](./CONTRIBUTING.md) for the PR checklist. Scaffold-only or not-yet-usable repos go in [Work in progress](#work-in-progress).

## Related

- [awesome-cmux](https://github.com/yigitkonur/awesome-cmux) - Similar ecosystem index for cmux.
- [awesome](https://github.com/sindresorhus/awesome) - The canonical awesome-list convention.
