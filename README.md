# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-herdr?label=last%20updated)

> A curated index of the **[Herdr](https://github.com/ogulcancelik/herdr)** ecosystem — the tools people build on top of the terminal-native agent multiplexer.

[Herdr](https://herdr.dev/) is tmux for AI agents. It gives agents and humans persistent workspaces, tabs, and panes; tracks what every agent is doing; survives detach/reattach and remote attach; and exposes a local Unix socket so anything can drive it.

```sh
curl -fsSL https://herdr.dev/install.sh | sh
herdr
```

Everything below builds on those primitives — running fleets of agents side by side, wiring editors and MCP clients into panes, switching and restoring sessions, and shaping the terminal around them.

---

## At a glance

| Group | Project | What it gives you |
|---|---|---|
| Orchestrate | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [herdr/SKILL.md](#run--orchestrate-agents) | Official skill for agents inside Herdr |
| Orchestrate | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [herdr-pm](#run--orchestrate-agents) | A technical PM/CTO for every agent tab |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-peer-agents-skill](#run--orchestrate-agents) | Agents that spawn and talk to peers |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [hcaiano/skills](#run--orchestrate-agents) | Pairing Claude and Codex as peers |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [pi-overseer](#run--orchestrate-agents) | Role-based Pi agent fleets |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [pi-herdr-workflow-kit](#run--orchestrate-agents) | Gated planner → coder → reviewer pipeline |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [mcdonc-pi-herdr](#run--orchestrate-agents) | Background Pi tasks into panes & tabs |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [herdr-python-client](#connect-over-socket--mcp) | A Python client for the socket API |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-mcp](#connect-over-socket--mcp) | Drive Herdr from any MCP client |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-mesh](#connect-over-socket--mcp) | MCP tools for agent-to-agent orchestration |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [herdr.nvim](#editor-integrations) | Neovim ↔ Herdr pane navigation |
| Editor | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-cursor](#editor-integrations) | Cursor agent state shown in Herdr |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [switchr](#sessions-switch--restore) | TUI session picker with pane tree |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [herdrctx](#sessions-switch--restore) | TUI to attach, stop, manage sessions |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [herdr-session-restore](#sessions-switch--restore) | Layout + Claude sessions across reboots |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [git-wt-herdr](#worktrees-config--terminal-ux) | Git worktrees mapped to tabs |
| Worktrees | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [superherd](#worktrees-config--terminal-ux) | Bridge Superset workspaces into Herdr |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [pi-herdr-tab-sync](#worktrees-config--terminal-ux) | Pi session names on your tabs |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [native-shortcuts-herd](#worktrees-config--terminal-ux) | macOS-native keys in Ghostty + Herdr |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-dotfiles](#worktrees-config--terminal-ux) | Drop-in config: prefix-free navigation |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [herdr-menu-bar](#desktop-apps--packaging) | macOS menu-bar agent-status widget |
| Desktop | ![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square) [deepin-herdr](#desktop-apps--packaging) | Native Deepin Linux window for Herdr |
| Packaging | ![Nix](https://img.shields.io/badge/-555555?logo=nixos&logoColor=white&style=flat-square) [herdr-nix](#desktop-apps--packaging) | Nix flake, auto-updated, with binary cache |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [ogulcancelik/pi-extensions](#run--orchestrate-agents) | Pi extensions suite with Herdr pane orchestration |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [aldrickdev/herdr_subagents](#run--orchestrate-agents) | Pi subagents in a shared visible Herdr pane |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-codex-usage-kit](#connect-over-socket--mcp) | Codex quota live in your Herdr sidebar |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [ogulcancelik/herdr-plugin-examples](#connect-over-socket--mcp) | Official plugin examples from Herdr's creator |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [gaijinjoe/herdres](#connect-over-socket--mcp) | Herdr pane output piped to Telegram |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [LittleDrinks/herdr-orchestrator-skill](#run--orchestrate-agents) | Coordinator-only orchestration skill for multi-agent Herdr |
| Orchestrate | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [luweiCN/herdr-ops](#run--orchestrate-agents) | Natural language workspace and worktree ops |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [sarmientoF/herdr-pr-loop](#run--orchestrate-agents) | Multi-agent PR loop with durable state |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [david-lutz/herdr-claude-teams](#run--orchestrate-agents) | Claude agent-teams as native Herdr panes |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [mattarau/wt-herdr](#worktrees-config--terminal-ux) | Worktrunk worktrees synced to Herdr workspaces |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [liu-qingyuan/herdr-tmux-local-config](#worktrees-config--terminal-ux) | Herdr + Codex + Oh My Tmux config |
| Desktop | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [re2zero/zenix](#desktop-apps--packaging) | GPUI desktop app with system metrics sidebar |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [kcosr/herdr-web](#desktop-apps--packaging) | Browser-based Herdr viewer for any device |
| Packaging | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [lachieh/vfox-herdr](#desktop-apps--packaging) | mise/vfox plugin with SHA256 verification |

---

## Run & orchestrate agents

The headline use: more than one agent working at once, in panes you can watch.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[ogulcancelik/herdr · SKILL.md](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md)**

The official, upstream skill file: drop-in instructions that teach an agent already running inside a Herdr pane to use the multiplexer — list workspaces, tabs, and panes, spawn helpers, send input, and wait on output and agent status. The canonical starting point before reaching for any of the third-party skills below.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[yigitkonur/herdr-pm](https://github.com/yigitkonur/herdr-pm)**

Walks your live agent tabs and drops a conductor on each — a per-tab technical-PM that reads the session, cross-checks git, surfaces scored impact×effort decisions, then drives the agent already sitting there to carry them out. It conducts rather than codes: one manager per tab (or split beside the agent), each in isolated context, so you stay on the decisions instead of babysitting ten parallel projects. Backend-agnostic across Claude, Codex, Pi, and Hermes, with an optional persistent `.herdr-pm/` notebook for the repos you want a standing PM on.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[msadig/herdr-peer-agents-skill](https://github.com/msadig/herdr-peer-agents-skill)**

A skill that teaches Claude, Pi, or Codex to spawn a named peer agent, prompt it, and read its output when it goes idle — so an agent can delegate the way you would. A shell wrapper smooths the rough edges, sending Codex's composer a second Enter and falling back to a manual pane split when `herdr agent start` loses the process before detection.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[hcaiano/skills](https://github.com/hcaiano/skills)**

A personal skill collection whose `herdr-pair` skill runs Claude and Codex as co-equal peers in one Herdr tab: either can initiate, the other auto-joins, and they exchange structured task / review / question / accepted messages until both sign off. A solid reference for how a real peer-agent protocol — spawn checks, send verification, per-tab session isolation — is wired against the Herdr CLI.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[SecretAardvark/pi-overseer](https://github.com/SecretAardvark/pi-overseer)**

Turns a workspace into a small team: an overseer hands work to implementer, tester, reviewer, and researcher agents, each in its own Herdr workspace and Jujutsu worktree. Every command a worker runs is checked against its role's allowlist — testers can run tests but not write files, pushes need a one-time human-approved token — and all task state persists under `.pi/overseer/` so a run survives a restart. For anyone who wants structured, guard-railed multi-agent execution rather than one chat at a time.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Jackliu-miaozi/pi-herdr-workflow-kit](https://github.com/Jackliu-miaozi/pi-herdr-workflow-kit)**

Turns Pi-in-Herdr into a gated pipeline: an orchestrator spawns planner, coder, and reviewer agents in their own panes, requires the plan to be approved before any code is written, and runs a review on each phase before it lands as its own commit. Handoffs pass through files under `.pi-herdr/` instead of terminal pastes, keeping long plans and diffs out of the input stream. For Pi users who want enforced plan-then-review structure over free-form agent runs.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[mcdonc/mcdonc-pi-herdr](https://github.com/mcdonc/mcdonc-pi-herdr)**

A Pi extension that gives Pi's background-task and conversation-fork features a home in Herdr: `/bg` offloads the running task into a visible pane, and `/tab` forks the conversation into a new tab, both over the socket API. Long builds and parallel workstreams become first-class panes and tabs you can watch, instead of invisible background processes. For Pi users running inside Herdr who want their side-work surfaced, not hidden.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ogulcancelik/pi-extensions](https://github.com/ogulcancelik/pi-extensions)**

A maintained suite of Pi coding-agent extensions from Herdr's creator, spanning ephemeral overlays, parallel-agent spawning, session recall, and — through the `pi-herdr` package — direct orchestration of Herdr panes, tabs, and workspaces from a Pi session. Install any package individually with `pi install npm:@ogulcancelik/<name>`. The reference collection for Pi users who want first-party Herdr integration alongside a rich set of productivity extensions.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[aldrickdev/herdr_subagents](https://github.com/aldrickdev/herdr_subagents)**

A Pi extension that delegates work to visible subagents in a shared Herdr tab named `subagents`, so you can watch each delegated task directly instead of waiting for a result. Parent Pi sessions get tools to spawn named child agents, steer them mid-run, and read their output when they go idle. Requires `herdr integration install pi` and Pi running inside a Herdr-managed pane.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[LittleDrinks/herdr-orchestrator-skill](https://github.com/LittleDrinks/herdr-orchestrator-skill)**

Turns the main Claude Code session into a coordinator that plans, dispatches workers to Herdr panes, and monitors their output — without writing code itself. Includes Python monitoring helpers, a YAML state-machine template, and prompt files for implementation, verification, and review roles. For teams who want enforced plan-then-execute discipline in Herdr without building their own multi-agent harness.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[luweiCN/herdr-ops](https://github.com/luweiCN/herdr-ops)**

Adds natural-language workspace control on top of Herdr's official skill: say "open a worktree for feat-login off main" and the agent translates it into the right herdr CLI commands, including worktree operations the upstream skill omits. Uses progressive disclosure — a lean primary document plus referenced detail files — to stay light on context. For developers who find the raw Herdr CLI syntax tedious to compose in conversation.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[sarmientoF/herdr-pr-loop](https://github.com/sarmientoF/herdr-pr-loop)**

Spawns tester, coder, and reviewer agents in dedicated Herdr tabs and orchestrates them through local task cycles and GitHub PR reviews, storing all state in files rather than session context so runs survive restarts. A human-approval gate and run log keep the loop auditable; a budget cap and pause file let you stop it mid-cycle. For developers who want automated PR review cycles that stay observable and interruptible.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[david-lutz/herdr-claude-teams](https://github.com/david-lutz/herdr-claude-teams)**

Shims Claude Code's experimental agent-teams feature onto Herdr so teammates spawn as native Herdr panes rather than tmux panes, using a translation layer between tmux commands and the Herdr socket API. Requires Herdr 0.6.10 and integrates with the sidebar, metadata, and notification surfaces natively. For Claude Code users who want visible team-mode panes without tmux inside a Herdr workspace.

---

## Connect over socket & MCP

Wiring outside tools — Python code, MCP clients — into Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client)**

A zero-dependency Python client for Herdr's Unix socket, so you can script the multiplexer instead of pressing keys. It handles the tedious parts — socket discovery, request envelopes, typed errors, event subscriptions, pane reads and waits — with ten convenience helpers and a raw `request()` escape hatch validated against the full method surface. The fastest way to build your own automation.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp)**

An MCP server that exposes Herdr to any MCP-speaking client — Claude Desktop, Cursor, Claude Code — as 21 tools for discovering, launching, reading, and writing panes. A recipe engine chains those calls into reusable flows with `{{ step.result.path }}` variable passing, reachable over both MCP and an HTTP bridge, with a bundled React playground for trying them out by hand.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[runchr-works/herdr-mesh](https://github.com/runchr-works/herdr-mesh)**

Another MCP server, this one tuned for agents coordinating agents: it hands any MCP-capable client tools to read another agent's pane, relay a message, hand off a task, spawn an agent, and wait on a result. It turns manual copy-paste between panes into one-sentence orchestration, and `herdr-mesh install` auto-registers itself with whichever agents (Claude Code, Codex, opencode) you have installed.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[jerryfane/herdr-codex-usage-kit](https://github.com/jerryfane/herdr-codex-usage-kit)**

Publishes Codex subscription quota — remaining 5-hour and weekly usage — into the Herdr agents sidebar as compact labels refreshed every 30 seconds, and opens a live usage dashboard in any shell pane. It reads Codex's own JSONL session logs without calling an API or consuming tokens, and installs as a systemd service plus two terminal commands. For Codex users running on Linux who want quota awareness without leaving the Herdr workspace.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ogulcancelik/herdr-plugin-examples](https://github.com/ogulcancelik/herdr-plugin-examples)**

Official reference plugins from Herdr's creator demonstrating four patterns: Telegram notification, development layout, GitHub link preview, and Rust release tracking — each a standalone `herdr-plugin.toml` package. They are provided as-is for adaptation rather than direct dependency. The canonical starting point for developers building their own Herdr plugins before reaching for the full API docs.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[gaijinjoe/herdres](https://github.com/gaijinjoe/herdres)**

Maps each live Herdr pane to a Telegram forum topic so your AI agent activity streams into a chat thread readable on any device. Accepts bot commands to relay input back into panes and consumes structured turn data from Herdr when available. For developers who want ambient monitoring of their Herdr sessions through Telegram without keeping a terminal window visible.

---

## Editor integrations

Bringing Herdr into the editor you already live in.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[devxplay/herdr.nvim](https://github.com/devxplay/herdr.nvim)**

Unifies pane navigation between Neovim and Herdr: the same `Ctrl+h/j/k/l` that moves between Vim splits flows straight into the adjacent Herdr pane when you hit an edge, and back again. A small Rust helper talks to the socket for focus, splits, and layout, and it coexists with vim-tmux-navigator — Neovim detects whether it's inside Herdr or tmux and routes accordingly. For Neovim users who want one set of muscle memory across editor and multiplexer.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[rbb/herdr-cursor](https://github.com/rbb/herdr-cursor)**

A planned shim around the Cursor SDK runtime that would report a Cursor agent's idle / working / blocked state back to Herdr, so a Cursor session shows up in your status sidebar like any native agent. Design-stage as of 2026-05 — the repo is a detailed spec with no code written yet, but the integration it sketches is a clean one to watch.

---

## Sessions: switch & restore

Finding the session you want, attaching to it, and getting it all back after a reboot.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[ridho9/switchr](https://github.com/ridho9/switchr)**

A full-screen session picker for Herdr: it lists every session next to its workspace / tab / pane tree, and you attach to the one you want with a keypress. Wire it up as your terminal's startup command and it greets you on each new window; it also spots an incompatible daemon and offers an in-place restart. For anyone juggling several named sessions who wants a fast visual switchboard.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[j0urneyk/herdrctx](https://github.com/j0urneyk/herdrctx)**

A keyboard-driven TUI for the housekeeping side of sessions — attach, stop, delete, create, and search, without copying names out of `herdr session list`. It ships through a Homebrew tap with prebuilt macOS and Linux binaries and refuses to launch nested when you're already inside a Herdr pane. For developers managing sessions across many projects who want a faster daily driver than the raw CLI.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[nickmaglowsch/herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore)**

Tags every Claude Code pane with a session ID, then snapshots your workspace / tab / cwd layout on a clean `herdr server stop` and replays it on the next cold boot — `claude --resume` and all — so your conversations come back where you left them. Claude-only and clean-shutdown-only by design, it's the answer to losing your agent setup to a reboot.

---

## Worktrees, config & terminal UX

Bridging external tools to Herdr's layout, and shaping the terminal itself.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr)**

Maps your git worktree lifecycle onto Herdr — creating a worktree opens a focused tab at that directory, removing it closes the tab, and switching focus brings the right one forward. It's the reference implementation of the `git-wt.plugin.v0` contract, pure Bash with `yq` and no Node or Python, so it drops cleanly into an existing `git-wt` setup.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[SirTenzin/superherd](https://github.com/SirTenzin/superherd)**

A CLI that bridges the Superset workspace manager into Herdr: from a Superset-imported repo, one command creates the worktree, opens it as a Herdr workspace, and mirrors Superset's setup terminals as live tabs. It drives the Herdr CLI for workspace and tab creation, forwards Ctrl-C into the Superset PTYs, and ejects the launching pane when it's done. For teams who run Superset (the agent-tooling one, not Apache Superset) alongside Herdr and want worktree setup automated end to end.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync)**

Renames the active Herdr tab to match your Pi session name on resume or agent start, so you can tell what each tab is doing at a glance instead of decoding generic titles. It talks to the socket directly and only activates inside Herdr-managed panes, so it's safe to install globally and forget.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[yigitkonur/native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd)**

Patches Ghostty and Herdr together so `cmd+t`, `cmd+n`, `cmd+w`, `cmd+1..9`, and tab cycling behave the way they do in Chrome or Safari — no manual escape-sequence wiring. It routes the keys through a Ghostty sidecar file (never touching your main config), maps them to the matching Herdr actions, and keeps timestamped backups plus a clean uninstall path. macOS only.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Taeyoung96/herdr-dotfiles](https://github.com/Taeyoung96/herdr-dotfiles)**

A drop-in Herdr `config.toml` built around prefix-free navigation: pane movement is mapped to bare `Shift+Alt+arrow` chords, the tmux-style prefix moves to `ctrl+space`, and it ships with the Catppuccin theme and a global agent panel. A one-command `install.sh` symlinks it in and backs up whatever was there — a clean, documented starting point for anyone who finds the default prefix-heavy bindings slow.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[mattarau/wt-herdr](https://github.com/mattarau/wt-herdr)**

Keeps Worktrunk-managed git worktrees and Herdr workspaces in sync: a workspace opens when a worktree is created, closes when it is removed, and focus follows when you switch. Ships health checks, dry-run mode, and toast notifications for lifecycle events. For teams running Worktrunk and Herdr side-by-side who want their workspace layout to mirror their worktree state without manual management.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[liu-qingyuan/herdr-tmux-local-config](https://github.com/liu-qingyuan/herdr-tmux-local-config)**

A workstation dotfile stack that integrates Herdr, Codex hook scripts, and Oh My Tmux into a single shell setup — Codex hook scripts report agent state to Herdr's sidebar, and Oh My Tmux adds theming alongside. Ships installation scripts and documented merge steps for each component. For Codex users who want a pre-integrated Herdr config without assembling the pieces themselves.

---

## Desktop apps & packaging

Running and installing Herdr outside the bare terminal.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[hmu332233/herdr-menu-bar](https://github.com/hmu332233/herdr-menu-bar)**

A macOS menu-bar app that keeps your agents' states — working, idle, blocked, done — in the system status bar, so you don't have to keep the TUI on screen to know when one needs you. Agents are grouped by workspace in the dropdown, and clicking one can jump you straight to its pane. For Mac users running several agents who want ambient awareness without a foreground terminal.

![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square) **[re2zero/deepin-herdr](https://github.com/re2zero/deepin-herdr)**

A native Deepin Linux / UOS app (Qt + the DTK toolkit) that launches Herdr inside an embedded terminal window — on first run it fetches the binary, starts the server if needed, and drops you into the client with theme-matched colors. It ships as a proper `.deb` maintained by a UnionTech developer, the straightforward way onto Herdr for Deepin desktops. (No README yet; the Debian packaging is the documentation.)

![Nix](https://img.shields.io/badge/-555555?logo=nixos&logoColor=white&style=flat-square) **[AodhanHayter/herdr-nix](https://github.com/AodhanHayter/herdr-nix)**

A Nix flake that packages the Herdr CLI for macOS and Linux (Intel and ARM), so you can `nix run` it or wire it into a NixOS overlay or Home Manager config instead of reaching for Homebrew. An hourly GitHub Action watches upstream releases and bumps the version, hashes, and a public Cachix binary cache automatically — so the flake tracks Herdr with no manual upkeep. The canonical path for anyone on a declarative Nix setup.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[re2zero/zenix](https://github.com/re2zero/zenix)**

A GPUI-native desktop app that wraps Herdr workspace, tab, and pane management with a live system-metrics sidebar (CPU, memory, network, disk), four built-in themes (Gruvbox, Solarized, Tokyo Night, Matrix), and CJK input support. Bundles the Herdr binary with PATH isolation to prevent version conflicts inside spawned sessions. For developers who want a richer desktop UI around Herdr than the bare terminal client, built on the same GPUI framework as Zed.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kcosr/herdr-web](https://github.com/kcosr/herdr-web)**

A React + Vite web UI for monitoring and controlling Herdr agents from any browser — desktop or mobile — over Herdr's socket API. Streams live pane state with terminal attachment, event subscriptions, and cross-client synchronization; a work-in-progress prototype with functional terminal attachment. For developers who want browser-based Herdr access without a native terminal, or a starting point for building their own remote client.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[lachieh/vfox-herdr](https://github.com/lachieh/vfox-herdr)**

A mise/vfox plugin for installing Herdr that verifies every download against GitHub's published SHA256 digest, supports preview builds via `herdr@preview`, and generates shell completions for bash, zsh, and fish that include live session data. Solves two gaps in Herdr's own self-updater: preview-channel access and completion scripts with dynamic data. For developers on declarative package setups who want versioned, verified Herdr installs outside Homebrew.

---

## Work in progress

Announced or scaffolded, but not yet usable — listed so submitters know they exist, without endorsing them as ready.

![YAML](https://img.shields.io/badge/-555555?logo=yaml&logoColor=white&style=flat-square) **[shippy/raycast-herdr](https://github.com/shippy/raycast-herdr)**

A Raycast extension meant to add Herdr control commands to Raycast. As of mid-2026 only the build-and-publish workflow is wired up; the `extensions/` directory is still an empty scaffold.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[SuperInstance/herdr-cocapn](https://github.com/SuperInstance/herdr-cocapn)**

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
