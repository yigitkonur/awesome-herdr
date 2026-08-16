# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Last updated](https://img.shields.io/github/last-commit/yigitkonur/awesome-herdr?label=last%20updated)

> A curated index of the **[Herdr](https://github.com/ogulcancelik/herdr)** ecosystem — the tools people build on top of the terminal-native agent multiplexer.

[Herdr](https://herdr.dev/) is tmux for AI agents. It gives agents and humans persistent workspaces, tabs, and panes; tracks what every agent is doing; survives detach/reattach and remote attach; and exposes a local Unix socket so anything can drive it.

```sh
curl -fsSL https://herdr.dev/install.sh | sh
herdr
```

**Official Links:** [Website](https://herdr.dev/) · [GitHub](https://github.com/ogulcancelik/herdr) · [Documentation](https://herdr.dev/docs/) · [Plugin Marketplace](https://herdr.dev/plugins/) · [Official Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) · [Socket API](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md)

---

## Contents

- [Strong starting points](#strong-starting-points)
- [Practical starter stacks](#practical-starter-stacks)
- [Choose by architecture](#choose-by-architecture)
- [At a glance](#at-a-glance)
- [Run & orchestrate agents (157)](#run--orchestrate-agents)
  - [Orchestration › Official Skills & Foundation (1)](#orchestration--official-skills--foundation)
  - [Orchestration › Multi-Agent Fleets & Supervisors (51)](#orchestration--multi-agent-fleets--supervisors)
  - [Orchestration › Subagent Spawners & Delegation (40)](#orchestration--subagent-spawners--delegation)
  - [Orchestration › Autonomous PR & Coding Loops (10)](#orchestration--autonomous-pr--coding-loops)
  - [Orchestration › Task Queues, Backlogs & Event Triggers (6)](#orchestration--task-queues-backlogs--event-triggers)
  - [Orchestration › General Workflows & Skill Packs (49)](#orchestration--general-workflows--skill-packs)
- [Connect over socket & MCP (105)](#connect-over-socket--mcp)
  - [Connect › Model Context Protocol (MCP) Servers (6)](#connect--model-context-protocol-mcp-servers)
  - [Connect › Socket API Clients & SDKs (54)](#connect--socket-api-clients--sdks)
  - [Connect › Push Notifications & Webhook Alerts (26)](#connect--push-notifications--webhook-alerts)
  - [Connect › Telemetry, Events & Quota Streaming (7)](#connect--telemetry-events--quota-streaming)
  - [Connect › Voice, Hardware & Remote Bridges (1)](#connect--voice-hardware--remote-bridges)
  - [Connect › Protocol & Third-Party Bridges (11)](#connect--protocol--third-party-bridges)
- [Editor integrations (60)](#editor-integrations)
  - [Editor › Neovim Navigation & Splits (32)](#editor--neovim-navigation--splits)
  - [Editor › Full Neovim-Hosted Workspaces (1)](#editor--full-neovim-hosted-workspaces)
  - [Editor › VS Code, Cursor & Devcontainers (9)](#editor--vs-code-cursor--devcontainers)
  - [Editor › Vim, Kakoune & Other Editors (13)](#editor--vim-kakoune--other-editors)
  - [Editor › REPL & Code Dispatchers (2)](#editor--repl--code-dispatchers)
  - [Editor › Editor Plugins & Bridges (3)](#editor--editor-plugins--bridges)
- [Sessions: switch & restore (64)](#sessions-switch--restore)
  - [Sessions › Fuzzy Session Switchers & TUI Pickers (46)](#sessions--fuzzy-session-switchers--tui-pickers)
  - [Sessions › Persistence, Snapshot & State Restore (11)](#sessions--persistence-snapshot--state-restore)
  - [Sessions › Workspace & Multi-Session Management (7)](#sessions--workspace--multi-session-management)
- [Worktrees, config & terminal UX (363)](#worktrees-config--terminal-ux)
  - [Worktrees › Git Worktree Automation (99)](#worktrees--git-worktree-automation)
  - [Worktrees › Workspace Lifecycle & Multi-Repo (4)](#worktrees--workspace-lifecycle--multi-repo)
  - [Terminal UX › Diff Review & File Viewers (40)](#terminal-ux--diff-review--file-viewers)
  - [Terminal UX › Pane Navigation, Keymaps & Hints (92)](#terminal-ux--pane-navigation-keymaps--hints)
  - [Terminal UX › Command Palettes & Workspace Switchers (13)](#terminal-ux--command-palettes--workspace-switchers)
  - [Terminal UX › Statuslines, Sidebars & Tab Sync (70)](#terminal-ux--statuslines-sidebars--tab-sync)
  - [Terminal UX › Status Overlays, HUDs & Agent Gauges (22)](#terminal-ux--status-overlays-huds--agent-gauges)
  - [Terminal UX › Output Inspection, Logs & Transcripts (9)](#terminal-ux--output-inspection-logs--transcripts)
  - [Terminal UX › Dotfiles & Drop-in Config Packs (12)](#terminal-ux--dotfiles--drop-in-config-packs)
  - [Terminal UX › Plugin Collections & Developer Frameworks (2)](#terminal-ux--plugin-collections--developer-frameworks)
- [Desktop apps & packaging (77)](#desktop-apps--packaging)
  - [Desktop › Native GUI & Menu Bar Apps (47)](#desktop--native-gui--menu-bar-apps)
  - [Desktop › Web Dashboards & Remote Viewers (4)](#desktop--web-dashboards--remote-viewers)
  - [Packaging › Package Managers & Flakes (21)](#packaging--package-managers--flakes)
  - [Packaging › Version Managers (mise, vfox) (5)](#packaging--version-managers-mise-vfox)
- [Work in progress (16)](#work-in-progress)
  - [WIP › Experiments, Concepts & Scaffolds (16)](#wip--experiments-concepts--scaffolds)
- [Resources](#resources)
- [Reference](#reference)

---

## Strong starting points

> [!TIP]
> **Getting started?** Start with the [Official Agent Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) and [herdr-navigator](https://github.com/thanhdat77/herdr-navigator) before adding multi-agent orchestrators or external bridges.

If you are new to the ecosystem, start with these focused, high-leverage tools:

| Goal | Recommended projects | Why start here |
|---|---|---|
| **Learn & automate Herdr** | [Official Agent Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md)<br>[54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client)<br>[54rt1n/herdr-simple-mcp](https://github.com/54rt1n/herdr-simple-mcp) | Teach an agent running in Herdr to use the CLI/socket, or drive Herdr from Python scripts and MCP clients. |
| **Run multi-agent fleets** | [edxeth/pi-subagents](https://github.com/edxeth/pi-subagents)<br>[transparent-pegasus/herdrpowers](https://github.com/transparent-pegasus/herdrpowers)<br>[yigitkonur/herdr-pm](https://github.com/yigitkonur/herdr-pm)<br>[jillesme/pi-herdr-squad](https://github.com/jillesme/pi-herdr-squad) | Delegate work to visible subagent panes, conduct parallel tasks, or run autonomous review loops. |
| **Editor integration** | [MomePP/herd.nvim](https://github.com/MomePP/herd.nvim)<br>[lmilojevicc/herdr-splits.nvim](https://github.com/lmilojevicc/herdr-splits.nvim)<br>[devxplay/herdr.nvim](https://github.com/devxplay/herdr.nvim) | Seamlessly navigate between Neovim splits and Herdr panes with unified keybindings. |
| **Session navigation & restore** | [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator)<br>[j0urneyk/herdrctx](https://github.com/j0urneyk/herdrctx)<br>[ridho9/switchr](https://github.com/ridho9/switchr) | Fuzzy search, switch, attach, and restore complex session layouts across restarts. |
| **Worktrees & diff review** | [noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr)<br>[razajamil/herdr-plugin-workspace-manager](https://github.com/razajamil/herdr-plugin-workspace-manager)<br>[persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr)<br>[jhochenbaum/herdr-hunk-diff](https://github.com/jhochenbaum/herdr-hunk-diff) | Isolate agent tasks in separate git worktrees, inspect diffs cleanly, and hand off comments to agents. |
| **Remote & mobile access** | [y011d4/herdr-plugin-agentweb](https://github.com/y011d4/herdr-plugin-agentweb)<br>[dcolinmorgan/herdr-remote](https://github.com/dcolinmorgan/herdr-remote)<br>[AltanS/collie](https://github.com/AltanS/collie) | Monitor and control your agent sessions securely from a web browser or phone. |

### Practical starter stacks

- **Lean local setup:** [Official Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) + [thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator) + [jhochenbaum/herdr-hunk-diff](https://github.com/jhochenbaum/herdr-hunk-diff). Gives agents basic awareness, adds fuzzy session switching, and lets you review diffs in an adjacent pane.
- **Neovim flow:** Keep Neovim as your editor with [MomePP/herd.nvim](https://github.com/MomePP/herd.nvim) or [lmilojevicc/herdr-splits.nvim](https://github.com/lmilojevicc/herdr-splits.nvim), while Herdr manages the terminal agents and background watchers.
- **Parallel multi-agent team:** [noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr) for branch isolation + [yigitkonur/herdr-pm](https://github.com/yigitkonur/herdr-pm) or [edxeth/pi-subagents](https://github.com/edxeth/pi-subagents) + [persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr) for structured review gates.
- **Remote / mobile setup:** [dcolinmorgan/herdr-remote](https://github.com/dcolinmorgan/herdr-remote) or [AltanS/collie](https://github.com/AltanS/collie) over Tailscale / SSH for secure on-the-go agent monitoring.

### Choose by architecture

| Need | Preferred approach | Why |
|---|---|---|
| Teach one agent Herdr commands | Official Agent Skill (`SKILL.md`) | Zero dependencies, instant setup, operates within the agent's natural context. |
| Script custom workflows | Typed Socket Client (`herdr-python-client`, `herdr-sock-go`) | Clean structured JSON protocol instead of brittle terminal screen-scraping. |
| Connect external AI tools | Focused MCP Server (`herdr-mcp`, `herdr-simple-mcp`) | Standard tool interfaces without adding overlapping control layers. |
| Parallel development | Git worktrees per tab/workspace | Prevents merge collisions and file write contention between concurrent agents. |
| Monitor long-running runs | Read-only TUI / web viewer / push notifier | Keeps tabs on progress without risking accidental inputs or unintended state mutations. |

[↑ Back to contents](#contents)

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
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [firegnu/herdr-loop-lab](#run--orchestrate-agents) | Verification-driven inner/fleet/epic agent loops |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [joelhooks/pi-bellwether](#run--orchestrate-agents) | Manage Herdr agents from a Pi session |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [madarco/agentbox-herdr-plugin](#run--orchestrate-agents) | AgentBox sandboxed-VM agents inside Herdr |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [Tudor0404/dual-author](#run--orchestrate-agents) | Issue → implement → dual-review → auto-merge |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-factory-loop-skill](#run--orchestrate-agents) | Spec-driven fleet factory loop skill |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [pi-herdr-subagents](#run--orchestrate-agents) | TUI dashboard for async Pi subagents |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [ask-fable-skill](#run--orchestrate-agents) | Delegate heavy tasks to a Fable worker |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [opencode-herdr](#run--orchestrate-agents) | Auto-split panes for OpenCode subagents |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [kirel/herdr-subagents](#run--orchestrate-agents) | Pi subagents in panes with callbacks |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [yangyang0507/herdr-skill](#run--orchestrate-agents) | Skill with structured non-blocking messaging |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [claude-orchestration](#run--orchestrate-agents) | Five Claude orchestration skills with hooks |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [cloudmanic/herdr-plus](#run--orchestrate-agents) | Project templates and quick-action launcher |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-plugin-github-start](#run--orchestrate-agents) | Start an agent from a GitHub issue |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [action-button-agent](#run--orchestrate-agents) | iPhone Action Button dispatches agent tasks |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-insight](#run--orchestrate-agents) | Live agent-state timeline across workspaces |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [herdr-todo](#run--orchestrate-agents) | Prompt backlog you drop into sessions |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-symphony](#run--orchestrate-agents) | GitHub Projects board → agents in panes |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [razajamil/herdr-factory](#run--orchestrate-agents) | Jira/markdown → PR autonomous factory |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-telemetry-bridge](#connect-over-socket--mcp) | Stream workspace and agent telemetry out |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [herdr-sock-go](#connect-over-socket--mcp) | Typed Go client for the socket API |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-simple-mcp](#connect-over-socket--mcp) | Stateless MCP server, 75 tools, role profiles |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [mimo-code-herdr-plugin](#connect-over-socket--mcp) | MiMo Code agent state in the sidebar |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-ntfy-notify](#connect-over-socket--mcp) | ntfy push alerts with pane location |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [tinysend-herdr](#connect-over-socket--mcp) | Email alerts you reply to unblock |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [dcolinmorgan/herdr-push](#connect-over-socket--mcp) | Zero-dep event push to herdr-remote |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-focus-notify](#connect-over-socket--mcp) | Clickable macOS toast jumps to pane |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-terminal-notifier](#connect-over-socket--mcp) | Branded macOS notifications, click-to-jump |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-hex-browser-voice-command](#connect-over-socket--mcp) | Voice transcripts routed to the right pane |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [MomePP/herd.nvim](#editor-integrations) | Neovim as host for Herdr agents |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [vim-herdr-navigation](#editor-integrations) | vim-tmux-navigator ported to Herdr |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [herdr-splits.nvim](#editor-integrations) | Smart split navigation and resizing |
| Editor | ![Vim Script](https://img.shields.io/badge/-555555?logo=vim&logoColor=white&style=flat-square) [herdr.vim](#editor-integrations) | Send lines and spawn REPLs in panes |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [sidekick_herdr](#editor-integrations) | Herdr backend for sidekick.nvim |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-sessionizer](#sessions-switch--restore) | Fuzzy-open projects into TOML layouts |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-picker-plus](#sessions-switch--restore) | One overlay for workspaces, SSH, agents |
| Sessions | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [alon-z/herdr-command-palette](#sessions-switch--restore) | Lightweight workspace/directory switcher |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-last-workspace](#sessions-switch--restore) | Toggle to the previous workspace |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-worktree-lifecycle](#worktrees-config--terminal-ux) | Repo-owned setup/teardown on worktree events |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-setup-bootstrap](#worktrees-config--terminal-ux) | TOML setup + gitignored file copy |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-fresh-worktree](#worktrees-config--terminal-ux) | Reset new worktrees to origin default |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-plugin-workspace-manager](#worktrees-config--terminal-ux) | Declarative YAML layouts per worktree |
| Worktrees | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-devup](#worktrees-config--terminal-ux) | Per-project dev stack, tunnel-URL sync |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-conductor-worktree](#worktrees-config--terminal-ux) | Sync Conductor workspaces into Herdr |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-plugin-jj-workspace](#worktrees-config--terminal-ux) | Jujutsu workspaces as Herdr workspaces |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-worktrunk](#worktrees-config--terminal-ux) | Interactive fzf picker for Worktrunk |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-plugin-gh-workflow](#worktrees-config--terminal-ux) | Issue → branch → worktree → workspace |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-reviewr](#worktrees-config--terminal-ux) | Code-review sidebar; comments to agent |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-launcher](#worktrees-config--terminal-ux) | Multi-field forms that run a command |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [JanTvrdik/herdr-command-palette](#worktrees-config--terminal-ux) | fzf palette over all plugin actions |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-file-viewer](#worktrees-config--terminal-ux) | Git-aware file viewer with diffs |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [herdr-flist](#worktrees-config--terminal-ux) | Directory sidebar that follows focus |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [herdr-fzf-url](#worktrees-config--terminal-ux) | Scan panes for URLs, pick with fzf |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-pluck](#worktrees-config--terminal-ux) | Keyboard-hint copy for any pane token |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-lazygit-overlay](#worktrees-config--terminal-ux) | lazygit as a focus-restoring overlay |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [herdr-plugin-hunk](#worktrees-config--terminal-ux) | Open Hunk diffs in splits or tabs |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [herdr-plugin-tiles](#worktrees-config--terminal-ux) | Six split-ratio layout presets |
| Terminal UX | ![Zig](https://img.shields.io/badge/-555555?logo=zig&logoColor=white&style=flat-square) [herdr_sync](#worktrees-config--terminal-ux) | Broadcast a command to every pane |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [cc-controller](#worktrees-config--terminal-ux) | Drive Herdr from a game controller |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-window-title-sync](#worktrees-config--terminal-ux) | Sync terminal title to workspace/agent |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [herdr-git-status](#worktrees-config--terminal-ux) | CI status dots for GitLab and GitHub |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-helpr](#worktrees-config--terminal-ux) | Workspace naming and pane cleanup |
| Terminal UX | ![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) [llmtrim-herdr](#worktrees-config--terminal-ux) | Per-pane token-savings badge |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [herdr-token-dashboard](#worktrees-config--terminal-ux) | Live multi-agent cost dashboard |
| Desktop | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [herdr-webui](#desktop-apps--packaging) | Standalone browser UI with terminal attach |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [herdr-remote](#desktop-apps--packaging) | Approve agents from phone, watch, Telegram |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [herdr-ios](#desktop-apps--packaging) | Native iOS client over SSH |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [herdr-controller](#desktop-apps--packaging) | Web dashboard and 3D agent office |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [stream-deck-herdr-plugin](#desktop-apps--packaging) | Stream Deck keys mirror agent status |
| Desktop | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [herdr-ulanzi-deck](#desktop-apps--packaging) | Ulanzi keypad shows live agents |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [agent-view](#desktop-apps--packaging) | Pixel-art office where agents live |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [erwins-enkel/shepherd](#run--orchestrate-agents) | Web/phone mission control for agent fleets |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [carze/herdr-smolmachine](#run--orchestrate-agents) | Run each agent pane in a microVM |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [sean1588/herdr-orchestrator](#run--orchestrate-agents) | YAML state-graph from issue to PR |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [saiashirwad/homestead](#run--orchestrate-agents) | Per-worktree ports, env, and agents |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [noor-latif/herd](#run--orchestrate-agents) | Bootstrap an N-agent grid per project |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [klittle32/letta-herdr-mod](#connect-over-socket--mcp) | Letta Code agent state in sidebar |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Phoobobo/herdr-traex-integration](#connect-over-socket--mcp) | TraeX agent state via lifecycle hooks |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [vaclavik-xyz/herdwatch](#connect-over-socket--mcp) | Hold pane working until CI finishes |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [carsonjones/herdr-agent-dashboard](#connect-over-socket--mcp) | Live TUI dashboard of running agents |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [alexei-led/ccgram](#connect-over-socket--mcp) | Control agents from Telegram topics |
| Editor | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [Daniel-Steinberger/obsidian-herdr](#editor-integrations) | Drive agents from an Obsidian checklist |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [maayanyosef/herdr-aws-ssm](#sessions-switch--restore) | Pick an EC2 box, attach over SSM |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [wyattjoh/herdr-plugin-renamer](#worktrees-config--terminal-ux) | Auto-name tabs and branches from prompts |
| Worktrees | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [ynny-github/herdr-event-hook](#worktrees-config--terminal-ux) | Run docker compose on worktree lifecycle |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [mkdir700/herdr-config](#worktrees-config--terminal-ux) | LazyVim-style config with local plugins |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [alexjsp/herdr-scrollback-capture](#worktrees-config--terminal-ux) | Save pane scrollback as HTML or text |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [akhillb/herdr-attention](#worktrees-config--terminal-ux) | Next-meeting countdown pane via gcalcli |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ppggff/herdr-plugin](#worktrees-config--terminal-ux) | Keep macOS input source per pane |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [astkaasa/herdr-tokscale-dashboard](#worktrees-config--terminal-ux) | Tokscale cost dashboard as a pane |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [aiki-sh/aiki-integration-herdr](#worktrees-config--terminal-ux) | Live aiki epic list in a pane |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [AltanS/collie](#desktop-apps--packaging) | Reply to agents from your phone |
| Desktop | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [0cv/herdr-mobile-relay](#desktop-apps--packaging) | Mobile PWA to approve and monitor agents remotely |
| Worktrees | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [3mmdrew/herdr-layout](#worktrees-config--terminal-ux) | Minimal Lua workspace layout definition for Herdr |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [4Born/herdr-pane-id-labeler](#worktrees-config--terminal-ux) | Sync pane labels with public pane IDs |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [a-curious-coder/herdr-iris](#worktrees-config--terminal-ux) | Agent-scoped fuzzy cheatsheet for skills and rules |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [a-curious-coder/herdr-plugin-manager](#worktrees-config--terminal-ux) | Popup TUI to manage and discover plugins |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [a2u/herdr-jira](#run--orchestrate-agents) | Jira TUI with one-key agent delegation |
| Orchestrate | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [aashishd/herdr-agent-messenger](#run--orchestrate-agents) | One-shot text messaging protocol between agent panes |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [abtris/herdr-plugin-jira-pr](#connect-over-socket--mcp) | Link branch PRs to Jira issues |
| Editor | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [aclima01/herdr-edit-windows](#editor-integrations) | Minimal pane text editor for Windows |
| Terminal UX | ![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) [aclima01/herdr-powershell-title-sync](#worktrees-config--terminal-ux) | Sync Windows terminal titles to active sessions |
| Terminal UX | ![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) [aclima01/herdr-todos-windows](#worktrees-config--terminal-ux) | Live task list panel for agent plans |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [adamwangxx/herdr-codex-resume](#sessions-switch--restore) | Codex resume picker in split panes |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [aemrebarut/herdr-dagr](#run--orchestrate-agents) | Live agent swarm DAG in split pane |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [aimdevlee/herdr-nvim-nav](#editor-integrations) | Seamless Neovim and Herdr pane navigation |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [AkashJana18/herdr-scratch](#worktrees-config--terminal-ux) | Persistent named scratchpads and floating utility panes |
| Desktop | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [alasano/house-of-herdr](#desktop-apps--packaging) | Work Louder Codex Micro hardware agent controller |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [alejodelosrios/herdr-claude-usage](#connect-over-socket--mcp) | Claude quota live in Herdr sidebar |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [aleslanger/herdr-strays](#worktrees-config--terminal-ux) | TUI to review stray worktrees and diffs |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [alexarthurs/herdr-sidebar](#worktrees-config--terminal-ux) | VS Code-style file explorer and Git sidebar pane |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [aliou/herdr-cast](#worktrees-config--terminal-ux) | macOS alerts, fuzzy navigation, and zoxide workspaces |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [allmight-ai/herdr-pet](#desktop-apps--packaging) | Retro virtual pet mirroring agent activity states |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [alvinunreal/oh-my-opencode-slim](#run--orchestrate-agents) | Multi-agent OpenCode delegation across Herdr panes |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [amurru/herdr-whistle](#connect-over-socket--mcp) | Remote agent management plugin over socket |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [aneym/herdr-voice](#connect-over-socket--mcp) | Voice-controlled Herdr workspace and agent management |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [Angel-O/herdr-agent-resume](#sessions-switch--restore) | Insert or copy agent resume commands |
| Orchestrate | ![YAML](https://img.shields.io/badge/-555555?logo=yaml&logoColor=white&style=flat-square) [aorumbayev/herdr-workflows](#run--orchestrate-agents) | Declarative YAML workflows for repetitive Herdr tasks |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [ArteenHD/herdr-cache-timer](#worktrees-config--terminal-ux) | Live prompt cache expiration timer in sidebar |
| Worktrees | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [AsgardMuninn/herdr-plugin-orbstack](#worktrees-config--terminal-ux) | Open OrbStack Linux machines as workspaces |
| Worktrees | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [asumaran/gotopr](#worktrees-config--terminal-ux) | Jump to open PRs across worktrees |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [asumaran/herdr-goto](#sessions-switch--restore) | Tree-style switcher across repos and worktrees |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [AVGVSTVS96/herdr-drovr](#sessions-switch--restore) | Move tabs across workspaces via fzf |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [azizuysal/herdr-workbench](#worktrees-config--terminal-ux) | Full IDE sidebar with search and diffs |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [baotran01/herdr-agent-diff](#worktrees-config--terminal-ux) | Inspect agent filesystem and git diff changes |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [bayoudhi/herdr-prayer-times](#worktrees-config--terminal-ux) | Prayer countdown in sidebar with timetable popup |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [bengemine/herdr-hibernate](#sessions-switch--restore) | Hibernate idle agent panes to free RAM |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [benkraus/herdr-plugin-codex-subs](#connect-over-socket--mcp) | Codex subscription quota and credit dashboard |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [beyondlex/herdr-recent-navigator](#sessions-switch--restore) | Fuzzy MRU popup for workspaces and agents |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [bfreed/herdr-corral](#worktrees-config--terminal-ux) | Workmux alternative for worktree and environment lifecycle |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [blockshiftnetwork/herdr-telegram-attention](#connect-over-socket--mcp) | Instant Telegram alerts for agent events |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [blurname/herdr-git-tab-name](#worktrees-config--terminal-ux) | Rename tabs to focused pane Git branch |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [bojackduy/nvim-herdr-navigation](#editor-integrations) | Seamless Neovim split ↔ Herdr navigation |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [bon5co/bermuda](#run--orchestrate-agents) | Schedule and run jobs as interactive agents |
| Desktop | ![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square) [bowlofsoup/herdr-stoplight](#desktop-apps--packaging) | Physical Arduino traffic light status monitor |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [bredebjorhovd/herdr-board](#run--orchestrate-agents) | Kanban board driving autonomous agents in panes |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [brianh20/herdr-stagr](#worktrees-config--terminal-ux) | Source control sidebar with side-by-side diffs |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [Brutheron/Renderd](#worktrees-config--terminal-ux) | Live Markdown reader for completed responses |
| Desktop | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [bsorescu/herdr-mobile](#desktop-apps--packaging) | Mobile-optimized TUI for agents over SSH |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [btorresgil/herdr-hermes-session-title](#worktrees-config--terminal-ux) | Hermes Agent session titles in sidebar |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [caioniehues/herdmates](#run--orchestrate-agents) | Native Claude Code agent teams and mission control |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [candypoets/buzzr](#connect-over-socket--mcp) | Mirror Herdr agents to Buzz channels |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [carellano/herdr-dev-servers](#worktrees-config--terminal-ux) | Discover and manage dev servers in panes |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [cdc-lst/herdr-wait](#worktrees-config--terminal-ux) | Process-tree-aware wait tags for idle panes |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [cdowell09/herdr-pr-board](#worktrees-config--terminal-ux) | Cross-repository GitHub PR dashboard in a tab |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [cdpath/herdr-warp](#connect-over-socket--mcp) | Drive Warp Agent CLI within Herdr panes |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [chantlong/herdr-habitat](#worktrees-config--terminal-ux) | Living terminal habitat nurtured by agents |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [chmarax/herdr-nvim](#editor-integrations) | Native Rust and Lua Neovim integration |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [chouxcreams/herdr-dashboard](#worktrees-config--terminal-ux) | PR, CI, and review status per pane |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [cinco/herdr-grep-nvim](#editor-integrations) | Live grep into split Neovim buffers |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [clawsouls/clawsouls-herdr-plugin](#run--orchestrate-agents) | ClawSouls AI agent personas for Herdr |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [cokekitten/herdr-telegram-bridge](#connect-over-socket--mcp) | Telegram alerts with direct reply unblocking |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [cpcloud/herdr-agentsview](#worktrees-config--terminal-ux) | Compressed AgentsView activity in one terminal |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [crexi/herdr-worktree-copy](#worktrees-config--terminal-ux) | Copy and symlink files into worktrees |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Crokily/herdr-lazygit](#worktrees-config--terminal-ux) | Sidebar lazygit with AI commit messages |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [cyperx84/herdr-loop](#run--orchestrate-agents) | Event-driven multi-model loop and graph orchestration |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [cyperx84/herdr-notes](#worktrees-config--terminal-ux) | Per-workspace markdown scratch notes in Go |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [damianpoole/herdr-opencode-sessions](#sessions-switch--restore) | Fuzzy-search and preview OpenCode sessions |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [danbuhler/herdr-pane-topic-sync](#worktrees-config--terminal-ux) | Auto-sync pane and tab titles to agent topics |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [danilolucasmd/herdr-clone-layout](#worktrees-config--terminal-ux) | Clone active workspace layout to new worktrees |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [dantehemerson/herdr-last-tab](#sessions-switch--restore) | One-key toggle to previously focused tab |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [darjss/herdr-orchestrate](#run--orchestrate-agents) | Pi-native orchestration board with model routing |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [davidolrik/herdr-titles](#worktrees-config--terminal-ux) | Dynamic tab and window titles from templates |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [ddfonseca/herdr-paste-image](#worktrees-config--terminal-ux) | Paste clipboard images as pane file paths |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [den-tanui/herdr-zoxide](#sessions-switch--restore) | Spawn workspaces from zoxide frecent paths |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [dev-shimada/herdr-auto-tab-name](#worktrees-config--terminal-ux) | Auto-rename tabs to current working directory |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [devoc09/herdr-equalize-vsplit](#worktrees-config--terminal-ux) | Split right and equalize pane columns |
| Packaging | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [dio16/herdr-auto-update](#desktop-apps--packaging) | Auto-update installed Herdr plugins on startup |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [DIodide/herdr-telemetry](#connect-over-socket--mcp) | Self-hosted agent telemetry stream in Go |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [disintegrator/trunkr](#worktrees-config--terminal-ux) | Integrate Worktrunk worktrees with Herdr workspaces |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [dleen/herdr-agents](#sessions-switch--restore) | Worst-first fzf agent picker with previews |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [dmangla3/herdr-fork-from-message](#sessions-switch--restore) | Fork agent sessions from previous message checkpoints |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [dnf0/herdr-llm-summary-header](#worktrees-config--terminal-ux) | Auto-write LLM task summaries to pane titles |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [DnzzL/herdr-automations](#run--orchestrate-agents) | Scheduled cron trigger engine for agent worktrees |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [douglascorrea/herdr-agent-inbox](#sessions-switch--restore) | Shared agent inbox with triage and rollups |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [dwarvesf/herdr-quicklook](#worktrees-config--terminal-ux) | Clipboard path preview in overlay popup |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [dzwduan/herdr-convo-index](#worktrees-config--terminal-ux) | Turn index popup for Claude Code panes |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [eabadim/herdr-context-namer](#worktrees-config--terminal-ux) | Auto-name tabs from OpenCode pane context |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [edmundmiller/herdr-plugin-dotfiles-github-link-preview](#worktrees-config--terminal-ux) | Preview GitHub issues and PRs in side-panes |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [edouard-andrei/herdr-layout-tools](#worktrees-config--terminal-ux) | In-place pane reshaping and layout equalization |
| Work in progress | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [eliasstravik/herdr-call](#work-in-progress) | Voice control interface for Herdr panes |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Elio2000/herdr-peer-review](#run--orchestrate-agents) | Dual-agent diff review and revision loop |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [elKei24/herdr-title-sync](#worktrees-config--terminal-ux) | Mirror agent terminal titles to tabs |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay](#worktrees-config--terminal-ux) | Per-workspace CPU and RAM usage overlay |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [EzraCerpac/jj-waltz](#worktrees-config--terminal-ux) | Jujutsu workspace switcher for Herdr |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Feasy01/herdr-allow](#worktrees-config--terminal-ux) | Copy gitignored allowlisted files into new worktrees |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [flupke/herdr-progressive-reviewer](#worktrees-config--terminal-ux) | Turn-based diff reviewer for agent turns |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [freethinkel/herdr-plugin-git-worktree-hooks](#worktrees-config--terminal-ux) | Worktree lifecycle hooks via global YAML config |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [funsaized/herdr-mise](#desktop-apps--packaging) | Pixel-art kitchen visualizer for agent steps |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [furuhashin/herdr-synchronize-panes](#worktrees-config--terminal-ux) | Broadcast commands to all tab panes |
| Desktop | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [gabrielbarretoo/herdr-medieval](#desktop-apps--packaging) | 3D medieval camp visualizer for agents |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [gambtho/herdr-devcontainer](#worktrees-config--terminal-ux) | Launch shells and agents inside Dev Containers |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [GavinTomlins/herdr-oh-my-agent](#run--orchestrate-agents) | Mirror subagent delegations into dedicated panes |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [gejiliang/herdr-openclaw](#connect-over-socket--mcp) | First-class OpenClaw agent monitoring in sidebar |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [getpipher/herdr-sysmon](#worktrees-config--terminal-ux) | System metrics in the Herdr sidebar |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [go-min/herdr-fwd](#connect-over-socket--mcp) | Auto loopback port forwarding for remote sessions |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [go-min/herdr-pane-name](#worktrees-config--terminal-ux) | Dynamic automatic pane renaming based on activity |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [GranamyrBR/herdr-english-coach](#worktrees-config--terminal-ux) | Color-coded English corrections in a side pane |
| Desktop | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [gw31415/herdr-amphetamine-macos](#desktop-apps--packaging) | Keep macOS awake while agents are working |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Hanyang-Li/herdr-espresso](#worktrees-config--terminal-ux) | Keep Mac awake while agents run |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [haphamdev/herdr-simple-switcher](#sessions-switch--restore) | Fuzzy-switch workspaces, tabs, and AI agents |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [happyeric77/agent-keep-awake](#worktrees-config--terminal-ux) | Prevent macOS sleep during active agent runs |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [happyeric77/agent-webhook-notify](#connect-over-socket--mcp) | Webhook notifications for blocked and done agents |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [hasuwini77/herdr-follow-cwd](#worktrees-config--terminal-ux) | Sync workspace labels to active pane directories |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [HexSleeves/herdr-warp](#worktrees-config--terminal-ux) | Open Herdr workspaces in native Warp panes |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [HikaruEgashira/say-hook](#connect-over-socket--mcp) | ElevenLabs TTS voice alerts for finished agents |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [hmu332233/herdr-f1](#desktop-apps--packaging) | F1 race dashboard for agent monitoring |
| Work in progress | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [hmu332233/herdr-plugins-labs](#work-in-progress) | Incubator lab for experimental Herdr plugins |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [hmu332233/herdr-symlink-worktree](#worktrees-config--terminal-ux) | Symlinks shared local files into new worktrees |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [horn553/herdr-ntfy](#connect-over-socket--mcp) | Zero-dep ntfy alerts on agent completion |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [hotchpotch/herdr-tiny-fingers](#worktrees-config--terminal-ux) | Keyboard copy hints for visible pane text |
| Terminal UX | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [htlin222/herdr-gamepad](#worktrees-config--terminal-ux) | Drive Herdr navigation using game controllers |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [iamhouser/herdr-claude-usage-multi](#connect-over-socket--mcp) | Multi-account Claude usage gauges in sidebar |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [iikjl/herdr-spotify](#worktrees-config--terminal-ux) | Spotify now-playing overlay with album art |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [ImArtisann/herdr-workspace-launcher](#sessions-switch--restore) | Fast directory picker for focused workspaces |
| Editor | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [ImArtisann/zed-herdr](#editor-integrations) | Sync active Herdr workspaces into Zed |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [iskwyuki/herdr-control-panel](#sessions-switch--restore) | Unified fzf control panel for workspaces and actions |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [ismaelosuna7824/herdr-recent-workspaces](#sessions-switch--restore) | Fuzzy-open and refocus recent workspace folders |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [iuhoay/herdr-break-pane](#worktrees-config--terminal-ux) | Move focused pane into a new tab |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [iurysza/herdr-tab-smart-rename](#worktrees-config--terminal-ux) | Context-aware auto-renamer for workspaces and tabs |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [iurysza/termscope](#worktrees-config--terminal-ux) | Open visible terminal paths in split panes |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [iviaxpow3r/herdr-session-parker](#sessions-switch--restore) | Stash and resume pane/tab agent sessions |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [JacquesvanWyk/herdr-hunk](#worktrees-config--terminal-ux) | Interactive fzf Hunk picker and autodiff |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [JacquesvanWyk/herdr-lazygit](#worktrees-config--terminal-ux) | Smart toggle lazygit in splits/tabs |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [jagzmz/herdr-annotations](#worktrees-config--terminal-ux) | Popup annotations and collections on terminal text |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [jagzmz/herdr-s3-clipboard](#worktrees-config--terminal-ux) | Upload clipboard images to S3 URLs |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [jatingargiitk/herdr-memory](#connect-over-socket--mcp) | Persistent workspace memory from agent sessions |
| Connect | ![C#](https://img.shields.io/badge/-555555?logo=csharp&logoColor=white&style=flat-square) [Javamomma/herdr-scribe](#connect-over-socket--mcp) | RAM-only live meeting transcripts in panes |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [jeffarese/herdr-bar](#sessions-switch--restore) | Cmd+K fuzzy jump across sessions |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [jeffarese/herdr-newtab-plus](#worktrees-config--terminal-ux) | Folder picker and agent launcher for tabs |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [jeffory/herdr-walkietalkie](#run--orchestrate-agents) | Token-efficient agent delegation across tabs and worktrees |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [jeromychu23/herdr-popupx](#worktrees-config--terminal-ux) | Persistent native floating scratch popups |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [JLighter/herdr-spawn](#run--orchestrate-agents) | Spawn agents with dedicated git worktrees |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [jlimas/herdr-worktree-seed](#worktrees-config--terminal-ux) | Copy-on-write node_modules and dotfiles for worktrees |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [joelhooks/herdr-pings](#run--orchestrate-agents) | Turn wake events and agent notifications |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [jorge-huxley/herdr-git-graph](#worktrees-config--terminal-ux) | Read-only git graph TUI with diffs |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [joshka0/herdr-watcher](#run--orchestrate-agents) | Durable agent continuations and detached callbacks |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [joshuadavidthomas/hrd](#sessions-switch--restore) | Terminal picker for local and sandboxed sessions |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [jsmenzies/mergr](#worktrees-config--terminal-ux) | GitHub PR status badges in sidebar rows |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [jugyo/herdr-nav-history](#worktrees-config--terminal-ux) | Browser-style back/forward focus navigation |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [JYasha11/herdr-in-your-face](#connect-over-socket--mcp) | Escalating ASCII alerts when agents get blocked |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [kakigakki/herdr-auto-namer](#worktrees-config--terminal-ux) | Auto-names agents and workspaces from Claude titles |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [kay-ws/herdr-island](#run--orchestrate-agents) | Filter Agents panel to agents needing input |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [kazimshah39/herdr-suffix-agent-filter](#worktrees-config--terminal-ux) | Filter Agents sidebar by workspace name suffix |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [kbrdn1/herdr-plugin-gwm](#worktrees-config--terminal-ux) | Drive gwm git worktrees from Herdr |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [keinstn/drover-notify](#connect-over-socket--mcp) | Push alerts to Drover when agents block |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [kenchan/herdr-ghq-open-agent](#sessions-switch--restore) | Fzf ghq repo picker launching Claude |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [kevinWangSheng/herdr-kit](#connect-over-socket--mcp) | Declarative layouts, event watcher, socket client |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [khatriafaz/herdr-plugin-auto-rename](#worktrees-config--terminal-ux) | Auto-rename workspaces and branches from agent prompts |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [kiitosu/herdr-jira-board](#run--orchestrate-agents) | Jira Kanban board with Claude launcher |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [KonstantinKai/herdr-harpoon](#worktrees-config--terminal-ux) | Harpoon-style marked pane navigation by index |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [kosuketut/herdr-remotedownloder](#connect-over-socket--mcp) | Download remote pane files to local Mac |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [kukv/herdr-plugin-github-dash](#connect-over-socket--mcp) | Browse and manage GitHub PRs and issues |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [langtind/gren-herdr](#worktrees-config--terminal-ux) | Manage git worktrees with gren in Herdr |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [LeonardoTrapani/herdr-js-worktree-bootstrap](#worktrees-config--terminal-ux) | Auto-bootstrap JS/TS worktrees with lockfiles |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [linuxing3/herdr-nnn](#worktrees-config--terminal-ux) | Launch nnn file manager in panes |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [lmilojevicc/seshagy](#sessions-switch--restore) | Agent-aware session manager for tmux and Herdr |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [lucasleon2107/herdr-tab-title-sync](#worktrees-config--terminal-ux) | Sync tab titles with agent conversation topics |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [mackt/herdr-window-title](#worktrees-config--terminal-ux) | Template-driven outer terminal title sync |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [maedana/herdr-agents-preview](#worktrees-config--terminal-ux) | Multi-agent terminal preview with focused main view |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [maedana/herdr-hint](#worktrees-config--terminal-ux) | Vimium-style jump labels for tabs and panes |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [makyinmars/herdr-context.nvim](#editor-integrations) | Stage Neovim code context into agent prompts |
| Work in progress | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [makyinmars/muster](#work-in-progress) | Swift menu bar widget for agent status |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [malone-c/herdr-agent-smart-rename](#worktrees-config--terminal-ux) | Smart agent pane renaming from activity |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [malone-c/herdr-keybind-search](#worktrees-config--terminal-ux) | Fuzzy-search and trigger active keybindings |
| Work in progress | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [malone-c/herdr-pane-balancer](#work-in-progress) | Auto-equalizes Herdr pane geometry across tabs |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [marcjfj-vmlyr/quickTUI](#run--orchestrate-agents) | Snap-together TUI primitives skill for coding agents |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [marcoskichel/herdr-muster](#sessions-switch--restore) | Fuzzy workspace picker with agent states |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [mariotmc/herdr-source-control](#worktrees-config--terminal-ux) | Terminal-native source control tab and status tracker |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [marius-se/herdr-brainrot](#worktrees-config--terminal-ux) | Play DOOM in a pane while agents work |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [markhuot/herdr-equalize-splits](#worktrees-config--terminal-ux) | Equalizes all split panes in active tab |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [maro114510/herdr-toggle-popup](#worktrees-config--terminal-ux) | Overlay popup shell on a single keybinding |
| Desktop | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [matheus3301/herdr-phone](#desktop-apps--packaging) | Mobile remote console via Cloudflare Tunnel |
| Work in progress | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [matovidlo/herdr-pr-tracker](#work-in-progress) | PR status tracker for agent branches |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [mattyan1053/herdr-compose](#worktrees-config--terminal-ux) | Docker Compose sidebar status and popup controls |
| Work in progress | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [meerzulee/herdr-float](#work-in-progress) | Zellij-style floating pane toggled with Alt+F |
| Desktop | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [mejiasd3v/herdr-farm](#desktop-apps--packaging) | 3D farm visualizing agents as livestock |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [mgh3326/scopefuel](#worktrees-config--terminal-ux) | Scope-aware headroom gauge for agent rate limits |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [mikedclarke/herdr-shepherd](#run--orchestrate-agents) | Scheduled agent sessions launched in visible workspaces |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [mikedclarke/herdr-workspaces](#sessions-switch--restore) | Fuzzy-pick registered directories into named workspaces |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [mo-arvan/herdr-claude-auto-retry](#sessions-switch--restore) | Auto-resume Claude Code on rate limits |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [moneycaringcoder/herdr-tether](#sessions-switch--restore) | Keep terminal tasks running after closing Herdr |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [mr04vv/herdr-pane-navigator](#sessions-switch--restore) | Status-sorted fuzzy tree navigator with previews |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [mroth/herdr-jj-status](#worktrees-config--terminal-ux) | Jujutsu bookmark status in workspace sidebar |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [napalmpapalam/herdr-quotr](#worktrees-config--terminal-ux) | Popup to quote agent output into prompts |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [narumiruna/herdr-plugins](#worktrees-config--terminal-ux) | Read-only GitHub PR and review popup |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [natori-hrj/herdr-hail](#connect-over-socket--mcp) | Bidirectional Slack and Discord bridge for agents |
| Packaging | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [natori-hrj/herdr-lazy](#desktop-apps--packaging) | Declarative plugin manager with TUI pane |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [natori-hrj/herdr-standup](#run--orchestrate-agents) | Summarize commits and work across agent repos |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [natori-hrj/herdr-triage](#run--orchestrate-agents) | Prioritize agents needing attention by blocked duration |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [ndom91/herdr-ai-tab-name](#worktrees-config--terminal-ux) | Auto-rename Herdr tabs using local LLMs |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [neilwashere/herdr-unrecoverable](#run--orchestrate-agents) | Watchdog recovering Pi agents from terminal errors |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [nelsonPires5/herdr-board](#run--orchestrate-agents) | Kanban board dispatching prompt cards to agents |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [neon-solutions/neon-herdr](#connect-over-socket--mcp) | Neon Postgres management inside Herdr panes |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [nicosuave/memex](#sessions-switch--restore) | Search agent transcripts and resume sessions into tabs |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [nikok6/herdr-mirror](#sessions-switch--restore) | Mirror remote Herdr sessions into your local sidebar |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [nimrc/herdr-git-pull](#worktrees-config--terminal-ux) | One-key git pull in an overlay pane |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [noviadi/herdr-layout](#sessions-switch--restore) | Save and replay pane layouts across sessions |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [ntindle/herdr-resurrect](#sessions-switch--restore) | Snapshot and restore sessions after reboots |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Numbered-com/herdr-ports](#worktrees-config--terminal-ux) | Active TCP listener badge for workspace sidebars |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [nwarwick/herdr-caffeinate](#worktrees-config--terminal-ux) | Keep macOS awake while agents are working |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [nytafar/herdr-cache-ttl](#worktrees-config--terminal-ux) | Live prompt-cache TTL countdown per pane |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [ogulcancelik/herdr-browser](#worktrees-config--terminal-ux) | Live interactive Chromium view inside Herdr panes |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [OliverGilan/herdr-jj](#worktrees-config--terminal-ux) | Jujutsu workspace support and sidebar status |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [Only-Moon/herdr-nerd-font-tab-name-windows](#worktrees-config--terminal-ux) | Nerd Font icons for Herdr tabs cross-platform |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [openclaw/crabbox](#connect-over-socket--mcp) | Warm isolated sandboxes and run tests from Herdr |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [opsydyn/herdr-questmancer](#worktrees-config--terminal-ux) | 16-bit RPG guild interface for agent fleets |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [osamahbeig/herdr-grove](#sessions-switch--restore) | Clickable project tree overlay to jump |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [osamahbeig/herdr-pane-mover](#worktrees-config--terminal-ux) | Clickable overlay to move and swap panes |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [osolmaz/ghzinga](#worktrees-config--terminal-ux) | View clicked GitHub PRs in side panes |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [osolmaz/herdr-branch-cleanup](#worktrees-config--terminal-ux) | Auto-checkout default branch on merged PRs |
| Desktop | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [osuki-dev/muqun-gateway](#desktop-apps--packaging) | Direct peer-to-peer mobile bridge for agent control |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [oullin/herdr-plugins](#worktrees-config--terminal-ux) | Curated suite of independent focused Herdr plugins |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [pedroloch/herdr-undo-close](#sessions-switch--restore) | Browser-style Cmd+Shift+T undo tab or pane close |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [phine-apps/mux-prompter](#worktrees-config--terminal-ux) | Fuzzy-pick and inject context prompts into panes |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [Phoobobo/herdr-agent-config-manager](#connect-over-socket--mcp) | Bulk-manage skills, MCPs, and agent hooks |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [Phoobobo/herdr-workboard](#worktrees-config--terminal-ux) | Kanban workboard TUI mapped to workspaces |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [Pimpmuckl/herdr-streamdeck](#desktop-apps--packaging) | Stream Deck+ physical dials and agent triage |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [pjs-0457/herdr-yazi-explorer](#worktrees-config--terminal-ux) | Context-aware Yazi file explorer in splits |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [plannotator/herdr-plannotator](#worktrees-config--terminal-ux) | Open Plannotator reviews in browser panes |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [playsthisgame/herdr-api-client](#worktrees-config--terminal-ux) | TUI HTTP client in splits or tabs |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [poweroutlet2/herdr-confirm-close-pane](#worktrees-config--terminal-ux) | Confirmation prompt before closing a pane |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [qq88976321/herdr-copy-search](#worktrees-config--terminal-ux) | Regex scrollback search and token copy |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [qu8n/herdr-automatic-rename](#worktrees-config--terminal-ux) | tmux-style tab renaming and 1-9 jump keys |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [quan-meng/herdr-slurm](#run--orchestrate-agents) | Slurm job workspaces with monitored agent tabs |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [quantk/herdr-review](#worktrees-config--terminal-ux) | Review agent changes and draft feedback back |
| Desktop | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ragamo/herdr-flock](#desktop-apps--packaging) | Pixel-art farm visualizing live AI coding agents |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [ram4-dev/herdr-automations](#run--orchestrate-agents) | Declarative cron and event automations for agents |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [ram4-dev/herdr-notify-center](#connect-over-socket--mcp) | Persistent popup inbox for agent notifications |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ramarivera/herdr-pretty-which](#worktrees-config--terminal-ux) | Which-key style keybinding overlay for Herdr |
| Work in progress | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [rbb/herdr-cursor](#work-in-progress) | Cursor SDK state reporter shim |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [Resetnak/herdr-logbook](#worktrees-config--terminal-ux) | Offline Markdown working memory and logbook |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [retroaalto/herdr-smartnav](#worktrees-config--terminal-ux) | Direction-aware pane navigation across splits |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [revanp/herdr-discord-presence](#connect-over-socket--mcp) | Discord Rich Presence for live agent sessions |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [robert-flo/herdr-terminal-file-manager](#worktrees-config--terminal-ux) | Launch elio file manager in active panes |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [rohankewal/herdr-nerd-font-tab-name](#worktrees-config--terminal-ux) | Nerd Font icons for Herdr tabs |
| Worktrees | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ropali/herdr-compose](#worktrees-config--terminal-ux) | Declarative YAML workspace and tab layout manager |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [rotemb-wond/herdr-copy-hints](#worktrees-config--terminal-ux) | Keyboard copy hints for terminal screen tokens |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [Royal-lobster/herdr-spinup](#worktrees-config--terminal-ux) | New-tab interactive tool start menu in Herdr |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [rvalledorjr/herdr-fresh](#worktrees-config--terminal-ux) | Embed Fresh terminal IDE in panes |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [ryanlewis/herdr-tab-renamer](#worktrees-config--terminal-ux) | Auto-rename tabs from agent titles and directories |
| Connect | ![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) [saeedrahimi/herdr-notify-wsl](#connect-over-socket--mcp) | Windows 11 toast alerts from WSL agents |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [sanirudh17/herdr-agent-handoff](#run--orchestrate-agents) | Handoff agent sessions across different CLIs |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Sawakee/herdr-imebox](#worktrees-config--terminal-ux) | IME popup text box for CJK input |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [scott-the-programmer/vscode-devcontainers-herdr](#connect-over-socket--mcp) | Relay Herdr socket into VS Code devcontainers |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [scott306lr/herdr-plugin-hunk-autodiff](#worktrees-config--terminal-ux) | Auto-opens hunk diffs when agents finish changes |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [scoussens-nthplusio/herdr-worktree-include](#worktrees-config--terminal-ux) | Copy untracked files via .worktreeinclude |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [sebcbi1/herdr-edge-nav](#editor-integrations) | Seamless edge navigation across panes and Neovim |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [second-state/vibetty](#connect-over-socket--mcp) | Live agent terminal streaming over MQTT |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [sergeybataev/herdr-codex-session-title](#worktrees-config--terminal-ux) | Sync Codex chat titles to agent names |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [serhii-chernenko/herdr-worktreeinclude](#worktrees-config--terminal-ux) | Respect .worktreeinclude when creating new worktrees |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [sfroment/herdr-git-detail](#worktrees-config--terminal-ux) | Detailed git status in sidebar token |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [sh1ma/herdr-auto-title](#worktrees-config--terminal-ux) | Auto-title tabs from Claude and Codex chats |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [shadowfax92/herdr-comments](#editor-integrations) | Annotate Herdr pane output in Neovim |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [shadowfax92/herdr-ferry](#sessions-switch--restore) | Move live panes and tabs across workspaces |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [shadowfax92/herdr-scratch](#worktrees-config--terminal-ux) | Persistent per-pane scratchpad popup using tmux |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [shadowfax92/herdr-talon](#worktrees-config--terminal-ux) | Spatial keyboard hints for Talon voice control |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [ShankyJS/herdr-space-scoped-agents](#worktrees-config--terminal-ux) | Scope agent panel to active space |
| Work in progress | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [shippy/raycast-herdr](#work-in-progress) | Raycast extension for Herdr commands |
| Work in progress | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [shoaibkhanz/herdr-nav-plus](#work-in-progress) | Pane-to-workspace directional navigation with wrapping |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [silverwolfdoc/herdr-usage-bar](#worktrees-config--terminal-ux) | Compact bottom bar for agent usage limits |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [speardragon/herdr-agents-history](#connect-over-socket--mcp) | Live TUI streaming agent tool calls |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [speardragon/herdr-ask-inbox](#worktrees-config--terminal-ux) | Centralized popup inbox for blocked agent questions |
| Packaging | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [speardragon/herdr-plugin-manager](#desktop-apps--packaging) | Popup TUI to manage Herdr plugins |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [speardragon/herdr-yazi](#worktrees-config--terminal-ux) | Open Yazi file manager in panes |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [steig/worktender](#run--orchestrate-agents) | Bridge GitHub issues to worktree agent sessions |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [StructuPath/herdr-browser](#run--orchestrate-agents) | Interactive Chromium browser pane for agents |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [StructuPath/herdr-conductor](#run--orchestrate-agents) | Attended producer and gate agent orchestration |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [StructuPath/herdr-guard](#worktrees-config--terminal-ux) | Audit and block dangerous agent shell commands |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [StructuPath/herdr-swarm](#run--orchestrate-agents) | Fan out parallel agents into isolated worktrees |
| Desktop | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [suisya-systems/herdr-agent-office](#desktop-apps--packaging) | Pixel-art terminal office showing agent statuses |
| Work in progress | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [superinstance/herdr-cocapn](#work-in-progress) | CoCapn fleet layer for Herdr |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [szrenwei/herdr-agent-metrics](#worktrees-config--terminal-ux) | Lightweight context and session metrics for agents |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [szrenwei/herdr-space-tab-metadata](#worktrees-config--terminal-ux) | Active tab indicator in Herdr workspace sidebar |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [tajdien/herdr-confirm-close](#worktrees-config--terminal-ux) | Confirmation prompt before closing panes and tabs |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [takemo101/wave-tui](#worktrees-config--terminal-ux) | Terminal radio with orbiting agent planet visualization |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [talent-factory/herdr-linear](#run--orchestrate-agents) | Linear issue panel to dispatch agent tasks |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [tanshio/herdr-worktreeinclude](#worktrees-config--terminal-ux) | Populates new worktrees from .worktreeinclude patterns |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [taxueseek/session-digger](#sessions-switch--restore) | Cross-environment session mining and search |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [tdi/herdr-worktree-from-linear](#worktrees-config--terminal-ux) | Linear issue picker into Git worktrees |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [tdi/herdr-worktree-from-pr](#worktrees-config--terminal-ux) | Open GitHub PRs in isolated worktrees |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [tdi/herdr-worktree-setup](#worktrees-config--terminal-ux) | Automated environment setup for new git worktrees |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [thanhdat77/herdr-navigator](#sessions-switch--restore) | Fuzzy jump to workspaces, agents, remotes, and actions |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [TheMetalStorm/herdr-commandcode-plugin](#connect-over-socket--mcp) | Command Code integration with lifecycle state reporting |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [TheMetalStorm/herdr-freebuff-plugin](#connect-over-socket--mcp) | Freebuff agent lifecycle and state bridge |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [TheThoughtagen/attic](#sessions-switch--restore) | Auto-archive and close idle coding agent sessions |
| Desktop | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [third774/herdr-sidepulse](#desktop-apps--packaging) | Ambient SidePulse hardware LED agent status |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [thomasschafer/herdr-kiosk](#worktrees-config--terminal-ux) | Fuzzy-search Git checkouts into worktree workspaces |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [tigorlazuardi/herdr-web-tui](#desktop-apps--packaging) | Browser and PWA frontend for Herdr |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [timofey-TK/herdr-open-in-editor](#editor-integrations) | Open focused Herdr workspaces in VS Code or |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [tjg184/herdr-worktree](#worktrees-config--terminal-ux) | Worktree management with Worktrunk and native git |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [tmn73/herdr-claude-tab-title](#worktrees-config--terminal-ux) | Sync Claude Code session titles to tabs |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [to4iki/herdr-unread-jump](#sessions-switch--restore) | Jump to next blocked or completed pane |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [tomasvarga/herdr-e2b](#sessions-switch--restore) | Mirror worktrees to E2B cloud sandboxes |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [tomasvarga/herdr-pickr](#worktrees-config--terminal-ux) | Ctrl-click PR review router with AI |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [tomasvarga/herdr-sniffr](#run--orchestrate-agents) | Agentic pre-review PR sniffer for tuicr |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Tomatio13/herdr-google-gmail](#worktrees-config--terminal-ux) | TUI Gmail browser panel powered by gogcli |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [toyamarinyon/herdr-thread-to-tab](#worktrees-config--terminal-ux) | Sync tab labels with agent thread titles |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Tyru5/herdr-floax](#worktrees-config--terminal-ux) | Floating scratchpad popup shell per workspace |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ugurtarlig/herdr-agent-recency](#sessions-switch--restore) | Pick agents sorted by recent activity |
| Work in progress | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ugurtarlig/herdr-pane-picker](#work-in-progress) | Quick character-hint pane selector overlay |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [Unayung/herdr-watch](#desktop-apps--packaging) | Monitor Herdr agent states on Apple Watch |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [usrivastava92/herdr-wakeup](#connect-over-socket--mcp) | Prevents OS sleep while agents work |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [uuie/reasonix-herdr](#connect-over-socket--mcp) | Live Reasonix lifecycle reporting and workspace control |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [vekexasia/pi-extensible-workflows](#run--orchestrate-agents) | Deterministic multi-agent workflow orchestration for Pi |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [vercel-labs/herdr-vercel-sandbox-plugin](#run--orchestrate-agents) | Isolated Vercel Sandboxes for Herdr agents |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [vonzelle-vzt/herdr-extensions](#editor-integrations) | Multi-panel LSP editor and tool suite |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [voodootikigod/adlc-herdr](#run--orchestrate-agents) | ADLC lifecycle gates and fleet status tracking |
| Desktop | ![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square) [walcew/herdr-assist](#desktop-apps--packaging) | Physical ESP32 desk panel with agent alerts |
| Terminal UX | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [WerrySs/herdr-cmux-cwd-sync](#worktrees-config--terminal-ux) | Sync cmux file explorer to focused pane |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [wilbeibi/herdr-catchup](#run--orchestrate-agents) | Cross-agent session summary, fork, and handoff |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [willfish/herdr-balance-panes](#worktrees-config--terminal-ux) | Evenly balance pane sizes in current tab |
| Editor | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [willfish/herdr-navigator](#editor-integrations) | Vim-aware split navigation on Herdr side |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [winoooops/herdr-agent-title-sync](#worktrees-config--terminal-ux) | Auto-sync pane titles with coding agents |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [wjarka/herdr-ghostty-tab-title](#worktrees-config--terminal-ux) | Color-coded agent status counts in Ghostty tabs |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [wraithyy/herdr-hintr](#worktrees-config--terminal-ux) | Which-key popup cheatsheet for Herdr keybindings |
| Work in progress | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [wraithyy/herdr-openr](#work-in-progress) | Fuzzy-open files and URLs from agent transcripts |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [wraithyy/herdr-waypoint](#sessions-switch--restore) | Bookmark and fuzzy-pick folders into workspaces |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [wyattjoh/herdr-plugin-gh-pr](#worktrees-config--terminal-ux) | GitHub PR status in the sidebar |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ycros/herdr-compass](#worktrees-config--terminal-ux) | Unified directional navigation across panes and workspaces |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [yigitkg/herdr-open-local-paths](#worktrees-config--terminal-ux) | Open or reveal paths in pane output |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [yoshiori/herdr-configurable-picker](#sessions-switch--restore) | Configurable tree-format goto picker for Herdr |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [yuk1ty/herdr-spreader](#worktrees-config--terminal-ux) | Declarative YAML layouts for workspaces, tabs, and panes |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [yuucu/herdr-hunk](#worktrees-config--terminal-ux) | Toggle Hunk diff reviews with fzf |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [yuuta1219/claude-usage](#connect-over-socket--mcp) | Claude Code usage pinned to sidebar bottom |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [yuuta1219/herdr-gekiatsu-plugin](#worktrees-config--terminal-ux) | Pachislot-themed Claude Code usage counter plugin |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [yxhta/herdr-agents-picker](#sessions-switch--restore) | Fuzzy agent-pane picker with live preview |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [zerodice0/herdr-plugin-worktree-bootstrap](#worktrees-config--terminal-ux) | Copy ignored files into new worktrees |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [zetlen/herdr-hud](#worktrees-config--terminal-ux) | Keybound popup HUD for session facts |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [zhenyufu/herdr-cadence](#run--orchestrate-agents) | Lead-and-worker agent fleet orchestrator in worktrees |

| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [cobanov/herdr-ntfysh](https://github.com/cobanov/herdr-ntfysh) | push ntfy notifications when an agent finishes |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [edxeth/pi-subagents](https://github.com/edxeth/pi-subagents) | Pi multi-agent framework for power users |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [jhochenbaum/herdr-hunk-diff](https://github.com/jhochenbaum/herdr-hunk-diff) | Review agent-authored changes in hunk from herdr |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [pbean/bmad-loop-adapter-herdr](https://github.com/pbean/bmad-loop-adapter-herdr) | herdr terminal-multiplexer backend for bmad-loop |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [vinicius91carvalho/harness-engineering](https://github.com/vinicius91carvalho/harness-engineering) | Harness Engineering for Claude Code, Codex, Opencode, Pi |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [jillesme/pi-herdr-squad](https://github.com/jillesme/pi-herdr-squad) | Visible, strictly read-only Herdr investigation squads for Pi |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [hungv47/herdr-agent-orchestration](https://github.com/hungv47/herdr-agent-orchestration) | A Herdr-first captain/worker workflow for Hermes, Codex, Grok, |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [transparent-pegasus/herdrpowers](https://github.com/transparent-pegasus/herdrpowers) | bringing agentic superpowers to the pane-driven |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [pdjsh/herdr-plugins](https://github.com/pdjsh/herdr-plugins) | Rust plugins for herdr |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [jbaham2/herdr-plugin](https://github.com/jbaham2/herdr-plugin) | Claude Code expert plugin for herdr, the agent-aware |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [loopkeep/herdr-plugin-loopreview](https://github.com/loopkeep/herdr-plugin-loopreview) | for loopreview |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [noctaIO/herdr-plugin-aos](https://github.com/noctaIO/herdr-plugin-aos) | Spawn Agentic OS-enabled Claude Code agents |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [y011d4/herdr-plugin-agentweb](https://github.com/y011d4/herdr-plugin-agentweb) | herdr-plugin-agentweb [English](./README.md) | 日本語 [herdr]( で動いているすべてのコーディングエージェントを、スマホから モニタリング・操作するための herdr |
| Orchestrate | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [lalanikarim/herdr-skills](https://github.com/lalanikarim/herdr-skills) | Pi agent skills for herdr terminal workspace management |
| Orchestrate | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [zoridos/herdr-skill](https://github.com/zoridos/herdr-skill) | Herdr agent skill — control panes, spawn agents, |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [marv1nnnnn/pi-yahe](https://github.com/marv1nnnnn/pi-yahe) | Yet Another Herdr Extension |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [TheShellLand/herdr-agent](https://github.com/TheShellLand/herdr-agent) | Herdr tool for agent |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [hewenyu/herdr-agent](https://github.com/hewenyu/herdr-agent) | 专门用于管理herdr 的agent，方便手机上沟通开发 |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [MinhDuyDEV/pi-subagents](https://github.com/MinhDuyDEV/pi-subagents) | Delegation runtime for Pi |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [giuseppecrj/pi-herdr-agents](https://github.com/giuseppecrj/pi-herdr-agents) | Pi Herdr Agents ![Pi Herdr Agents |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [calebcauthon/herdr-agent-copy-paste-fork](https://github.com/calebcauthon/herdr-agent-copy-paste-fork) | fork by simply copying and pasting, or hotkey |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [leonho/herdr-agent-inbox](https://github.com/leonho/herdr-agent-inbox) | popup triage list of all agents with their |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [thkt/herdr-agentchat](https://github.com/thkt/herdr-agentchat) | leader/coder two-agent conversation with send-and-wake (Claude Code x |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [huynguyen03dev/herdr-agent](https://github.com/huynguyen03dev/herdr-agent) | Agent-agnostic role profiles for running an AI technical |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [muslihudindev/herdr-agent-orchestrator](https://github.com/muslihudindev/herdr-agent-orchestrator) | HerdR Pi Orchestration Local-first, provider-agnostic multi-agent software engineering |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [MartinBspheroid/herdr-agent-dash](https://github.com/MartinBspheroid/herdr-agent-dash) | Herdr Agent Board Herdr Agent Board is |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [zerodice0/herdr-agent-labels](https://github.com/zerodice0/herdr-agent-labels) | Assign readable color-animal names to unnamed Herdr agents |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [okonomi/herdr-agent-queue](https://github.com/okonomi/herdr-agent-queue) | herdr-agent-queue herdr のエージェントのうち手が止まっているものへ、キー 1 つで待たせている順に巡回 フォーカスするプラグイン。対象は「入力待ち (blocked)」だけではない。応答が完了して 次の指示を待っているもの |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [w-gitops/herdr-agent-factory](https://github.com/w-gitops/herdr-agent-factory) | Herdr-native, harness-agnostic multi-agent team launcher and control plane |
| Orchestrate | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [eliebak/herdr-agent-island](https://github.com/eliebak/herdr-agent-island) | slop repo from claude that works for me, |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [aerain/herdr-agent-orchestration](https://github.com/aerain/herdr-agent-orchestration) | Herdr pane-based multi-agent orchestration skill for OMP, Claude |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [cowcow02/herdr-agent-orchestrator](https://github.com/cowcow02/herdr-agent-orchestrator) | Herdr Agent Orchestrator Event-driven orchestration for one existing |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [mikeyobrien/herdr-agent-profiles](https://github.com/mikeyobrien/herdr-agent-profiles) | Data-driven CLI harness and model profiles for Herdr |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [shubham399/herdr-agents-auto-compact](https://github.com/shubham399/herdr-agents-auto-compact) | herdr-agents-auto-compact Herdr plugin that auto-compacts AI agent sessions |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [hisetu/herdr-agent-skill](https://github.com/hisetu/herdr-agent-skill) | herdr p align="center" img src="assets/logo.png" alt="herdr" width="100" / |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [lifez/herdr-agent-dashboard](https://github.com/lifez/herdr-agent-dashboard) | Agent Dashboard A read-only local dashboard for unmodified |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ahnsv/maeh](https://github.com/ahnsv/maeh) | Rust CLI for hmph/herdr agent orchestration |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [eyalev/herdr-web](https://github.com/eyalev/herdr-web) | Mobile-first web UI for the herdr agent multiplexer |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [minhtran3124/Brichan](https://github.com/minhtran3124/Brichan) | epository-native AI Chief of Staff for Codex |
| Orchestrate | ![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) [Xz-FreeMan/herdr-hint](https://github.com/Xz-FreeMan/herdr-hint) | Herdr Agent 会话提示工具 |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [dkarter/foreman](https://github.com/dkarter/foreman) | 👷‍♂️🐑 Live Herdr agent monitoring dashboard hardware |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [BlazzzPlay/herdr-office](https://github.com/BlazzzPlay/herdr-office) | Read-only pixel-art office for visualizing Herdr agents |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop) | Automated cross-review between agents in a herdr workspace |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [jwkicklighter/herdr-prompt-library](https://github.com/jwkicklighter/herdr-prompt-library) | for browsing, managing, and inserting reusable local |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [masakirocorp/oh-my-herdr](https://github.com/masakirocorp/oh-my-herdr) | Oh My Herdr — terminal workspace manager |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [lucasdeprit/Puppy](https://github.com/lucasdeprit/Puppy) | Multi-Agent system with herdr terminal & claude code |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [egriff38/effect-herdr](https://github.com/egriff38/effect-herdr) | Typed Effect-TS SDK for the herdr terminal-native agent |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Sebastiangmz/herdr-plus](https://github.com/Sebastiangmz/herdr-plus) | Agent skill |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [chetanunadkat-lang/herdr-fleet](https://github.com/chetanunadkat-lang/herdr-fleet) | Run a fleet of Claude/Codex coding agents |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [misty-step/kelpie](https://github.com/misty-step/kelpie) | Phone-first console for triaging a fleet of omp |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [yigitkonur/claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin) | Claude Code skill |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [Drozerah/herdr-voice](https://github.com/Drozerah/herdr-voice) | Real-time Text-to-Speech (TTS) voice synthesis plugin |
| Orchestrate | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [inbeomheo/herdr-orchestra](https://github.com/inbeomheo/herdr-orchestra) | Multi-agent orchestration skill for herdr — Claude Code |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [goatbjh/pi-herdr-claude-subagents](https://github.com/goatbjh/pi-herdr-claude-subagents) | Direct Herdr-backed Claude oracle, reviewer, and planner execution |
| Orchestrate | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [wenxichang/herdr-pal](https://github.com/wenxichang/herdr-pal) | control AI-agent in IM via herdr |
| Orchestrate | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [motionharvest/herdr](https://github.com/motionharvest/herdr) | agent multiplexer that lives in your terminal |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [RenKoya1/herdr-approve-all](https://github.com/RenKoya1/herdr-approve-all) | approve every blocked agent at once (one keystroke, |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [nhclink16/herdr-announcer](https://github.com/nhclink16/herdr-announcer) | speaks a one-sentence LLM summary when an agent |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [hoon-ch/herdr-gjc-plugin](https://github.com/hoon-ch/herdr-gjc-plugin) | GJC (Gajae Code) plugin that reports agent lifecycle |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [narumiruna/herdr-web](https://github.com/narumiruna/herdr-web) | A terminal-first browser workbench for the herdr agent |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [persinac/agents-nexus](https://github.com/persinac/agents-nexus) | Batteries-included toolkit for running fleets of AI coding |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [EDMND-SRC/herdr-subagents](https://github.com/EDMND-SRC/herdr-subagents) | OpenCode plugin that launches subagents in named herdr |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [conpiracy/ep-starter](https://github.com/conpiracy/ep-starter) | Starter factory for Pi inside Herdr — agent |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [eciuca/herdr-drover](https://github.com/eciuca/herdr-drover) | Herdr tool for drover |
| Orchestrate | ![AutoHotkey](https://img.shields.io/badge/-555555?logo=autohotkey&logoColor=white&style=flat-square) [wtcrowe4/DialDeck](https://github.com/wtcrowe4/DialDeck) | Surface Dial control surface for agent workflows — |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [IgorWarzocha/herdr-annotations](https://github.com/IgorWarzocha/herdr-annotations) | Collect annotations on terminal selections and stage them |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [huntergdavis/dunkingsheep](https://github.com/huntergdavis/dunkingsheep) | Keep herdr agents engaged |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [EricBois/herdr-nudge](https://github.com/EricBois/herdr-nudge) | Arm a continue-nudge on a herdr agent — |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [BrianM0330/pi-herdr-snooze](https://github.com/BrianM0330/pi-herdr-snooze) | Toggle a forced Herdr agent lifecycle state (snooze) |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [kyokosawada/viu](https://github.com/kyokosawada/viu) | Mobile client for a herdr agent fleet - |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [shimo4228/herdr-toolkit](https://github.com/shimo4228/herdr-toolkit) | Claude Code plugin |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [terafin/herdr-restart-always](https://github.com/terafin/herdr-restart-always) | Supervise herdr agent panes and always restart whatever |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [hewel/herdr-harness-coordinator](https://github.com/hewel/herdr-harness-coordinator) | for coordinating autonomous coding-agent harnesses |
| Orchestrate | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [ryanlewis/herdr-workspace-renamer](https://github.com/ryanlewis/herdr-workspace-renamer) | syncs agent session names onto workspace labels |
| Orchestrate | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [andpeicunha/herdr-output-comment-composer](https://github.com/andpeicunha/herdr-output-comment-composer) | annotate AI agent output inline with comments |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [yanekyuk/pi-herdr-orchestrator](https://github.com/yanekyuk/pi-herdr-orchestrator) | Project-agnostic Herdr orchestration for Pi |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Idan-Levin/herdr-implement-review](https://github.com/Idan-Levin/herdr-implement-review) | Herdr workflow for Codex implementation, security scanning, |
| Orchestrate | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [mithyer/ry-skill](https://github.com/mithyer/ry-skill) | Custom Pi skills for fast Herdr workflows |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [regenrek/codex-orchestration-herdr](https://github.com/regenrek/codex-orchestration-herdr) | Reusable Codex Sol/Luna Herdr orchestration skill with deterministic |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [di-rs/.dotfiles](https://github.com/di-rs/.dotfiles) | Personal dotfiles |
| Orchestrate | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [sh1ny/herdr-switchyard](https://github.com/sh1ny/herdr-switchyard) | Human-gated Hermes + Herdr orchestration for isolated OMP |
| Connect | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [schacon/micro-manager](https://github.com/schacon/micro-manager) | Mac bridge between the Creator Micro 2 |
| Connect | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [DanielOu1208/agentslate](https://github.com/DanielOu1208/agentslate) | iPhone remote keypad for supervising Herdr coding agents |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [luminexord/herdres](https://github.com/luminexord/herdres) | Telegram interface for monitoring and messaging Herdr coding |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [Tomyail/herdr-connect](https://github.com/Tomyail/herdr-connect) | Open-source LAN companion app for discovering and connecting |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [vantt/herdr-go](https://github.com/vantt/herdr-go) | Web-first remote gateway + supervisor for herdr — |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [benkraus/herdr-plugin-mobile-relay](https://github.com/benkraus/herdr-plugin-mobile-relay) | Herdr tool for mobile relay |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [islam3zzat/herdr-mcp](https://github.com/islam3zzat/herdr-mcp) | herdr-mcp MCP server that lets AI assistants orchestrate |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [bonsai/herdr-mcp](https://github.com/bonsai/herdr-mcp) | herdr-mcp Herdr tab control from opencode via MCP |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [nyanyaon/github-issue-herdr-plugin](https://github.com/nyanyaon/github-issue-herdr-plugin) | Claude Code plugin for herding GitHub issues |
| Connect | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [cryks/shepherd](https://github.com/cryks/shepherd) | herdr agents on local and remote hosts, monitored |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [LoneExile/merino](https://github.com/LoneExile/merino) | Merino 🐑 — remote tunnel dashboard for Herdr |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [akhileshrangani4/herdr-bridge](https://github.com/akhileshrangani4/herdr-bridge) | HTTP bridge + Charming control panel for herdr |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [maedana/herdr-agents-bridge](https://github.com/maedana/herdr-agents-bridge) | Mobile bridge for Herdr agents (web server + |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [winoooops/herdr-agent-watcher](https://github.com/winoooops/herdr-agent-watcher) | Coding-agent observability for Herdr |
| Connect | ![Java](https://img.shields.io/badge/-555555?logo=openjdk&logoColor=white&style=flat-square) [maxandersen/jherdr](https://github.com/maxandersen/jherdr) | Java client for the herdr socket API |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [juninaba/herdr-slack-notify](https://github.com/juninaba/herdr-slack-notify) | Send Slack notifications when Herdr agents finish |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [cyperx84/herdr-api](https://github.com/cyperx84/herdr-api) | Go client for the herdr socket API — |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [dcieslak19973/herdr-slackr](https://github.com/dcieslak19973/herdr-slackr) | Real-time Slack feed pane for herdr — Socket |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [thanh-dong/herdr-rich-preview](https://github.com/thanh-dong/herdr-rich-preview) | Browser-based rich preview (markdown, mermaid, D2, HTML, SVG) |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [flaricy/herdr-bridge](https://github.com/flaricy/herdr-bridge) | dsh-herdr-bridge Report [DeepSeek Harness]( agent activity |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [PlaneshiftDev/microd](https://github.com/PlaneshiftDev/microd) | Companion daemon for the Codex Micro macropad |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [atnine-ai/herdr-bridge](https://github.com/atnine-ai/herdr-bridge) | herdr-bridge Bridge [herdr]( panes to chat services |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [aiken884/herdr-bridge](https://github.com/aiken884/herdr-bridge) | Coordinate multiple AI coding agents from a single |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [damozhang/dsh-herdr-bridge](https://github.com/damozhang/dsh-herdr-bridge) | herdr-bridge A dsh plugin that bridges a [DeepSeek |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [sina85/herdr-mobile](https://github.com/sina85/herdr-mobile) | Password-protected, mobile-first Next.js control panel for a local |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [pepperhorn/herdr-remote](https://github.com/pepperhorn/herdr-remote) | Small remote dashboard for a running Herdr server |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [deanbaker/herdr-remote](https://github.com/deanbaker/herdr-remote) | herdr-remote A web/mobile client for [Herdr]( — |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [hisetu/pi-herdr-remote](https://github.com/hisetu/pi-herdr-remote) | pi-herdr-remote Pi-native tools for controlling Herdr servers |
| Connect | ![Kotlin](https://img.shields.io/badge/-555555?logo=kotlin&logoColor=white&style=flat-square) [bradydibble/herdi](https://github.com/bradydibble/herdi) | Herdi — private herdr remote client + relay |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [kkunkunya/herdr-remote-phone](https://github.com/kkunkunya/herdr-remote-phone) | Mobile-first fork of herdr-remote |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [alex-devdone/herdr-remote-agent-watch](https://github.com/alex-devdone/herdr-remote-agent-watch) | show a claude running behind ssh/tmux as |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Mic92/herdr-eternal](https://github.com/Mic92/herdr-eternal) | Roaming-friendly transport for herdr --remote |
| Connect | ![HTML](https://img.shields.io/badge/-555555?logo=html5&logoColor=white&style=flat-square) [georgolden/herdr-remote-setup](https://github.com/georgolden/herdr-remote-setup) | This is my setup for herdr + remote |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [mvallebr/herdr-telegram-plugin](https://github.com/mvallebr/herdr-telegram-plugin) | Telegram bot companion for herdr — remote control |
| Connect | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [backpine/remote-agent-workspace](https://github.com/backpine/remote-agent-workspace) | Blueprint for an always-on remote agent workspace |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [0xGosu/herdr-auto-pilot](https://github.com/0xGosu/herdr-auto-pilot) | that will automatically prompt the running AI Coding |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [ryonakae/shepherd](https://github.com/ryonakae/shepherd) | Worker observability daemon and runtime bridges for Herdr-managed |
| Connect | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [AgentWorkforce/herdr-relay-bridge](https://github.com/AgentWorkforce/herdr-relay-bridge) | Herdr agents as a fleet able to work |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [pinksaucepasta/paperboat-helper](https://github.com/pinksaucepasta/paperboat-helper) | Remote runtime for Paperboat environments |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [shaunbntan-create/vgpt-app](https://github.com/shaunbntan-create/vgpt-app) | A phone web UI for your Herdr agent |
| Connect | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [sbulav/herdr-relay](https://github.com/sbulav/herdr-relay) | Monitor and approve herdr agents from your phone, |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [shaunbntan-create/vgpt](https://github.com/shaunbntan-create/vgpt) | A phone web UI for your Herdr agent |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [rkbkosp/agent-beacon](https://github.com/rkbkosp/agent-beacon) | A local ESP32-S3 desktop status beacon for Codex |
| Connect | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [crabfishxy/awaytome](https://github.com/crabfishxy/awaytome) | "Away to me" — monitor and drive your |
| Connect | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [LuYanFCP/herdr-wechat-plugin](https://github.com/LuYanFCP/herdr-wechat-plugin) | for wechat remote control |
| Connect | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [trillium/herdr-tailscale](https://github.com/trillium/herdr-tailscale) | auto-attach trusted Tailscale peers as remote tabs |
| Editor | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [T0mSIlver/localvoxtral](https://github.com/T0mSIlver/localvoxtral) | Talk to your coding agents by voice |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [nettlesh/dotfiles](https://github.com/nettlesh/dotfiles) | Alacritty + Fish + Herdr + Neovim |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [uncaughterrs/dotfile](https://github.com/uncaughterrs/dotfile) | Config file for ghostty , neovim , herdr |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [luisgui1757/dotfiles](https://github.com/luisgui1757/dotfiles) | Cross-platform Rose Pine terminal/editor setup for Apple Silicon |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [ctbaum/herdr-agents.nvim](https://github.com/ctbaum/herdr-agents.nvim) | Neovim bridge for running editor-integrated coding agents |
| Editor | ![Emacs Lisp](https://img.shields.io/badge/-555555?logo=gnuemacs&logoColor=white&style=flat-square) [ionrock/ghostherd](https://github.com/ionrock/ghostherd) | Manage herdr agent terminals from Emacs via ghostel |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [RooseveltAdvisors/vim-herdr-navigation](https://github.com/RooseveltAdvisors/vim-herdr-navigation) | Seamless Ctrl/Alt hjkl navigation across herdr panes |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [willfish/herdr-navigator.nvim](https://github.com/willfish/herdr-navigator.nvim) | Seamless navigation between Neovim windows and Herdr panes |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [joo-was-already-taken/herdr-navigator.nvim](https://github.com/joo-was-already-taken/herdr-navigator.nvim) | Navigate between Neovim splits and Herdr panes |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [kaar/nvim-herdr-navigator](https://github.com/kaar/nvim-herdr-navigator) | Seamless navigation between Neovim splits and herdr panes |
| Editor | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Aerosnail/nvim-herdr-navigator](https://github.com/Aerosnail/nvim-herdr-navigator) | Custom plugin pair to navigate seamlessly between nvim |
| Editor | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [AVGVSTVS96/vim-herdr-navigator](https://github.com/AVGVSTVS96/vim-herdr-navigator) | Seamless navigation between herdr panes and vim/nvim splits |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [inferst/herdr-review.nvim](https://github.com/inferst/herdr-review.nvim) | Code review UI for Neovim with Git |
| Editor | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview) | Git status/diff panel for herdr - review changes, |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [utahta/herdr-prompt.nvim](https://github.com/utahta/herdr-prompt.nvim) | Ask a herdr agent about the code |
| Editor | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [AbhijithAnirudhan2907/herdr-sidebar](https://github.com/AbhijithAnirudhan2907/herdr-sidebar) | herdr-sidebar fork with an in-pane editor (edit/save, live |
| Editor | ![Emacs Lisp](https://img.shields.io/badge/-555555?logo=gnuemacs&logoColor=white&style=flat-square) [eddof13/herdr.el](https://github.com/eddof13/herdr.el) | Control the herdr terminal workspace manager from Emacs, |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [ocyedwin/editor](https://github.com/ocyedwin/editor) | Portable Ghostty, Herdr, Vim, Neovim, and VSCodeVim workflow |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [acmmarques/dotfiles](https://github.com/acmmarques/dotfiles) | ghostty • zsh • herdr • nvim • |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [TianZuo555/herdr.nvim](https://github.com/TianZuo555/herdr.nvim) | Send Neovim references to coding agents |
| Editor | ![GLSL](https://img.shields.io/badge/-555555?logo=opengl&logoColor=white&style=flat-square) [Jalmar01/my-dots](https://github.com/Jalmar01/my-dots) | Personal Nix home-manager flake |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [rahadur/herdr.nvim](https://github.com/rahadur/herdr.nvim) | herdr.nvim — Ink & Paper colorschemes ported |
| Editor | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [endoumame/herdr-vscode](https://github.com/endoumame/herdr-vscode) | herdr Review for VS Code Review code where |
| Editor | ![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) [SamuelCastrillon/tzemed](https://github.com/SamuelCastrillon/tzemed) | Tzemed — Windows native dev stack distro |
| Editor | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [andorexu/hermes-agent-skills-pack](https://github.com/andorexu/hermes-agent-skills-pack) | 28 production-grade Hermes Agent skills — decision frameworks, |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [alex-devdone/herdr-cursor-open](https://github.com/alex-devdone/herdr-cursor-open) | Open the focused herdr pane in Cursor |
| Editor | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [lurepos/herdr-vscode-tasks](https://github.com/lurepos/herdr-vscode-tasks) | useful herdr picker when dealing with .vscode folder |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [kbroomstd/herdr.nvim](https://github.com/kbroomstd/herdr.nvim) | Nvim bindings for herdr the agent multiplexer that |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [magimetal/matrix-themes](https://github.com/magimetal/matrix-themes) | Matrix-inspired themes for various software |
| Editor | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [gogamid/pi-herdr-cursor-focus](https://github.com/gogamid/pi-herdr-cursor-focus) | pi-herdr-cursor-focus A [Pi]( extension that hides the editor |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [beraterkanelcelik/agent-army](https://github.com/beraterkanelcelik/agent-army) | A three-tier agent hierarchy for running parallel AI |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [GMakeziG/ninjatronics-ai](https://github.com/GMakeziG/ninjatronics-ai) | AI operating system for orchestrating specialized engineering agents |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [AVGVSTVS96/starter-dotfiles](https://github.com/AVGVSTVS96/starter-dotfiles) | Minimal agent-first, auto-managed macOS dotfiles for React/TS dev |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [sjdonado/dotfiles](https://github.com/sjdonado/dotfiles) | Herdr tool for dotfiles |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [nwiizo/signalbox.nvim](https://github.com/nwiizo/signalbox.nvim) | Attention-first Neovim control surface for persistent Herdr coding |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Schaitanya535/herdr-config](https://github.com/Schaitanya535/herdr-config) | My herdr (agent multiplexer) config — keybindings, theme, |
| Editor | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [lhr0909/herdr-bel](https://github.com/lhr0909/herdr-bel) | Forward Herdr agent notifications to Zed Terminal Threads |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [s-0-a-r/copse](https://github.com/s-0-a-r/copse) | CLI-native ADE (Agent Development Environment) — Herdr + |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [jakkzz/herdr-setup](https://github.com/jakkzz/herdr-setup) | Reproducible Herdr + Neovim setup — pinned plugins, |
| Editor | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [vanducng/dotfiles](https://github.com/vanducng/dotfiles) | AI-native macOS dev environment |
| Editor | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [mirkobozzetto/dotfiles](https://github.com/mirkobozzetto/dotfiles) | macOS terminal setup |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [code-yeongyu/web-terminal](https://github.com/code-yeongyu/web-terminal) | Mobile-first self-hosted web terminal powered by Ghostty WASM |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Joxtacy/herdr-plugin-vault](https://github.com/Joxtacy/herdr-plugin-vault) | Browse past Claude Code sessions in a herdr |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [htlin222/herdr-agent-self-reload-skill](https://github.com/htlin222/herdr-agent-self-reload-skill) | Self-reload skill for herdr AI agent sessions — |
| Sessions | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [vsem-azamat/herdr-telegram](https://github.com/vsem-azamat/herdr-telegram) | Telegram forum topics bound to stable Herdr agent |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [BradleyLWood/herdr-sessions](https://github.com/BradleyLWood/herdr-sessions) | Herdr tool for sessions |
| Sessions | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [fjordlars/herdr-session-manager](https://github.com/fjordlars/herdr-session-manager) | Herdr Session Manager Small terminal UI for managing |
| Sessions | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer) | tmux-sessionizer for herdr |
| Sessions | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [Duzc01/herdr-session-finder](https://github.com/Duzc01/herdr-session-finder) | Fuzzy-search Claude Code sessions across every project |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [iiii1224/herdr-statusline](https://github.com/iiii1224/herdr-statusline) | Customizable status line for herdr sessions |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [pawaca/even-better](https://github.com/pawaca/even-better) | Mirror your live herdr terminal agent sessions (Claude |
| Sessions | ![HTML](https://img.shields.io/badge/-555555?logo=html5&logoColor=white&style=flat-square) [JeremiahChurch/herd-remote](https://github.com/JeremiahChurch/herd-remote) | Phone-friendly web control surface for herdr terminal/agent sessions |
| Sessions | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [nickboy/herddeck](https://github.com/nickboy/herddeck) | Stream Deck control surface for herdr agent sessions |
| Sessions | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [KUKARAF/collie_voice_commands](https://github.com/KUKARAF/collie_voice_commands) | Rust/Tauri Android app |
| Sessions | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [lsisoft/herdr-telegram-slack-bridge](https://github.com/lsisoft/herdr-telegram-slack-bridge) | Bidirectional Telegram and Slack bot bridge for Herdr |
| Worktrees | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [kenn-io/ghosthub](https://github.com/kenn-io/ghosthub) | A multiplexer-native power terminal for your local |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [spirin22/herdr-plugins](https://github.com/spirin22/herdr-plugins) | Herdr tool for plugins |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [mkdir700/herdr-plugin-worktree](https://github.com/mkdir700/herdr-plugin-worktree) | start a git worktree from a GitHub issue |
| Worktrees | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks) | run custom setup/teardown commands when a git worktree |
| Worktrees | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [dkarter/hwt](https://github.com/dkarter/hwt) | 🌳 Frictionless Herdr Worktree Orchestration |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [kennethkoontz/herdr-worktree-sync](https://github.com/kennethkoontz/herdr-worktree-sync) | herdr-worktree-sync A [Herdr]( plugin that copies gitignored files |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [arjenblokzijl/herdr-worktree-autosetup](https://github.com/arjenblokzijl/herdr-worktree-autosetup) | auto-run a setup command (e.g |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude) | copy .worktreeinclude-selected gitignored files into new worktrees |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [riclib/herdr-worktree-layout](https://github.com/riclib/herdr-worktree-layout) | auto-build a file-viewer + two-shells layout in git |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude) | that populates every new git worktree |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [botonddombi/boti-toolkit](https://github.com/botonddombi/boti-toolkit) | Personal dev environment toolkit |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab) | create a git worktree + workspace |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [dabeeeenster/herdr-worktree-local-files](https://github.com/dabeeeenster/herdr-worktree-local-files) | link gitignored local config files into new git |
| Worktrees | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [jal-co/pi-herdr-worktree](https://github.com/jal-co/pi-herdr-worktree) | Pi extension |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [toyamarinyon/herdr-worktree-setup](https://github.com/toyamarinyon/herdr-worktree-setup) | Run a repo-committed setup script in every new |
| Worktrees | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [AndreGeng/herdr-worktree-dispatcher](https://github.com/AndreGeng/herdr-worktree-dispatcher) | Herdr Worktree Dispatcher Standalone Herdr plugin that dispatches |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [wthorp/squeeze-chute](https://github.com/wthorp/squeeze-chute) | Coordinate GitHub issues through isolated Herdr worktree teams |
| Worktrees | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [mopeneko/herdr-worktree-hook-plugin](https://github.com/mopeneko/herdr-worktree-hook-plugin) | herdr-worktree-hook-plugin A [herdr]( plugin that runs user-defined shell |
| Worktrees | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [ralphcrisostomo/herdr-goal-skill](https://github.com/ralphcrisostomo/herdr-goal-skill) | Claude Code skill |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [mholtzscher/herdr-worktree-picker](https://github.com/mholtzscher/herdr-worktree-picker) | Create Herdr worktrees from local or remote branches |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [arjenblokzijl/herdr-worktree-provisioner](https://github.com/arjenblokzijl/herdr-worktree-provisioner) | Runs per-repo setup in a new worktree's own |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [hung-eggie-do-covergo/delegate-orchestrator](https://github.com/hung-eggie-do-covergo/delegate-orchestrator) | Fan out one isolated Claude Code sub-agent per |
| Worktrees | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [m1sk9/herdr-worktree-hooks-plugin](https://github.com/m1sk9/herdr-worktree-hooks-plugin) | A plugin that adds customizable hooks to Herdr's |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [QuentinTorg/stagehand](https://github.com/QuentinTorg/stagehand) | Human-guided orchestration for coding agents, coordinating Herdr worktrees, |
| Worktrees | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [eoinest/convo-history](https://github.com/eoinest/convo-history) | Voice scratchpad for coding agents |
| Worktrees | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [firew0rks/herdr-ci-tokens](https://github.com/firew0rks/herdr-ci-tokens) | Show PR, CI and review status for every |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [ditwrd/herdr-remote-worktrunk](https://github.com/ditwrd/herdr-remote-worktrunk) | Herdr remote worktrunk workspace |
| Worktrees | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [ribbons-digital/pi-herd](https://github.com/ribbons-digital/pi-herd) | Visible Pi session orchestration with Herdr panes |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [simoncrypta/agentic-dev-setup](https://github.com/simoncrypta/agentic-dev-setup) | Shareable Herdr + worktrunk dev layout for agentic |
| Worktrees | ![Ruby](https://img.shields.io/badge/-555555?logo=ruby&logoColor=white&style=flat-square) [sample-usr/herdr-devenv-worktree](https://github.com/sample-usr/herdr-devenv-worktree) | for working with devenv inside worktrees |
| Worktrees | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [danieljvdm/herdr-worktrunk](https://github.com/danieljvdm/herdr-worktrunk) | to integrate worktrunk for git worktree management |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [oscabriel/pi-herdr-btw](https://github.com/oscabriel/pi-herdr-btw) | pi install npm:pi-herdr-btw |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [benkraus/herdr-mobile](https://github.com/benkraus/herdr-mobile) | Herdr Mobile Herdr Mobile is a native iOS |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [bcihanc/herdr-claude-session-title](https://github.com/bcihanc/herdr-claude-session-title) | mirrors the Claude Code session title (/rename |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh) | Sesh-style workspace picker TUI for Herdr |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ramarivera/herdr-palette](https://github.com/ramarivera/herdr-palette) | A Rust/Ratatui fuzzy command palette for Herdr workspaces |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [senna-lang/herdr-agent-usage](https://github.com/senna-lang/herdr-agent-usage) | Context meters and provider rate limits for agents |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title) | Automatic tmux-like tab titles for Herdr |
| Terminal UX | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [multiplex-term/Multiplex](https://github.com/multiplex-term/Multiplex) | An SSH / tmux / herdr terminal |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [wenhanweime/herdr-plugin-renamer](https://github.com/wenhanweime/herdr-plugin-renamer) | LLM-powered session naming for herdr |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [MIDO-ruby7/herdr-plugins-directory](https://github.com/MIDO-ruby7/herdr-plugins-directory) | A link collection for finding herdr plugins |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Newt6611/herdr-plugin-rust](https://github.com/Newt6611/herdr-plugin-rust) | A Rust application framework for building Herdr plugins |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [lachieh/herdr-plugin-cmux](https://github.com/lachieh/herdr-plugin-cmux) | herdr-plugin-cmux Mirror every [herdr]( agent into the [cmux]( |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [Volpestyle/herdr-plugin-mermaid-preview](https://github.com/Volpestyle/herdr-plugin-mermaid-preview) | Live Mermaid previews for Claude Code and Codex |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [rcosteira79/herdr-plugins](https://github.com/rcosteira79/herdr-plugins) | Two independent herdr plugins |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [petitviolet/herdr-plugins](https://github.com/petitviolet/herdr-plugins) | Herdr tool for plugins |
| Terminal UX | ![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) [tomaszhanc/herdr-plugins](https://github.com/tomaszhanc/herdr-plugins) | herdr-plugins My monorepo of [herdr]( plugins |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [oyuk/herdr_plugin](https://github.com/oyuk/herdr_plugin) | herdrplugin [herdr]( のプラグイン jump-to-agent。エージェント一覧から特定ステータスのエージェントを探して、その端末にフォーカスをジャンプする。 ## Actions | Action |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [alastairsounds/herdr-plugins](https://github.com/alastairsounds/herdr-plugins) | s for herdr |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [tyler-jewell/herdr-plugins](https://github.com/tyler-jewell/herdr-plugins) | Pure-Rust Herdr plugins monorepo (stdlib-first) |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [GroepOnline/herdr-plugins](https://github.com/GroepOnline/herdr-plugins) | Mirrored from OnlineChefGroep/herdr-plugins (migrate fase5) |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [SeanRoberts/herdr-plugins](https://github.com/SeanRoberts/herdr-plugins) | s for herdr |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [lliwi/herdr-plugins](https://github.com/lliwi/herdr-plugins) | My personal herdr plugins |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [CyPack/herdr-plugins](https://github.com/CyPack/herdr-plugins) | File-manager plugins for the CyPack herdr fork |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [shelken/herdr-plugins](https://github.com/shelken/herdr-plugins) | s monorepo (auto-pi |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [paulrobello/par-herdr-plugins](https://github.com/paulrobello/par-herdr-plugins) | Custom Herdr plugins (monorepo) |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [aiki-sh/aiki-plugin-herdr](https://github.com/aiki-sh/aiki-plugin-herdr) | for Aiki |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [boooowy/herdr_plugins](https://github.com/boooowy/herdr_plugins) | Herdr tool for herdrplugins |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [BlockedPath/herdr-plugin](https://github.com/BlockedPath/herdr-plugin) | Herdr tool for plugin |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [tomotochi/herdr-plugin-picker](https://github.com/tomotochi/herdr-plugin-picker) | A Herdr file picker plugin that inserts selections |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [RestartDK/scatterer](https://github.com/RestartDK/scatterer) | Personal herdr plugin config |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [michiomochi/herdr-plugin-sidenote](https://github.com/michiomochi/herdr-plugin-sidenote) | herdr-plugin-sidenote herdr の母艦 space の右 pane に常駐する TUI |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [amine2233/herdr-plugin-kanban](https://github.com/amine2233/herdr-plugin-kanban) | to use kanban |
| Terminal UX | ![Zig](https://img.shields.io/badge/-555555?logo=zig&logoColor=white&style=flat-square) [dannycroft/hunk-herdr-plugin](https://github.com/dannycroft/hunk-herdr-plugin) | Hunk Diff Herdr plugin for opening Hunk diffs |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [daltonkyemiller/herdr-plugin-switchboard](https://github.com/daltonkyemiller/herdr-plugin-switchboard) | Switchboard for Herdr A focused Herdr plugin |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [BryanHeBY/anolisa-herdr-plugin](https://github.com/BryanHeBY/anolisa-herdr-plugin) | anolisa-herdr-plugin — ANOLISA × herdr 集成 把 [ANOLISA]( |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [m4salah/herdr-plugin-last](https://github.com/m4salah/herdr-plugin-last) | tmux-style last-tab and last-workspace navigation for Herdr |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [crierr/herdr-tmux-layout](https://github.com/crierr/herdr-tmux-layout) | tmux-style preset layouts for live Herdr panes |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [cokekitten/pi-recap](https://github.com/cokekitten/pi-recap) | Recent activity recap extension for Pi with optional |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [maedana/herdr-agents-status](https://github.com/maedana/herdr-agents-status) | Always-on-top agent status overlay |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Yemeni/herdr-agent-timer](https://github.com/Yemeni/herdr-agent-timer) | that alternates each agent's status label with its |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Tyru5/herdr-agent-state](https://github.com/Tyru5/herdr-agent-state) | Realtime agent status pane for herdr |
| Terminal UX | ![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) [aclima01/herdr-notify-windows](https://github.com/aclima01/herdr-notify-windows) | Windows 11 toast notifications for herdr agents (turn |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [bleedingfight/herdr-agent-manager](https://github.com/bleedingfight/herdr-agent-manager) | Herdr tool for agent manager |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [VinhLe1410/herdr-agent-priority](https://github.com/VinhLe1410/herdr-agent-priority) | for configurable agent status priority |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [AnnanKhan/herdr-agent-launcher](https://github.com/AnnanKhan/herdr-agent-launcher) | Clickable agent button pane for Herdr |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ningxiaoxiao/herdr-agent-picker](https://github.com/ningxiaoxiao/herdr-agent-picker) | Pick an AI agent and a working directory |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [mi2428/herdr-agent-layout](https://github.com/mi2428/herdr-agent-layout) | herdr-agent-layout herdr-agent-layout keeps a supervising pane at |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [spro/herdr-agent-launcher](https://github.com/spro/herdr-agent-launcher) | Open a new named tab running a specific |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [scaryrawr/herdr-agent-title](https://github.com/scaryrawr/herdr-agent-title) | herdr agents in the window title |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [Vistyy/pi-herdr-agents](https://github.com/Vistyy/pi-herdr-agents) | Run owned Pi agents in Herdr tabs |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [tomys22/herdr-agent-usage-plugin](https://github.com/tomys22/herdr-agent-usage-plugin) | AI Usage Plugin for Herdr Display Claude, Codex, |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [yansfil/herdr-agent-context-labels](https://github.com/yansfil/herdr-agent-context-labels) | Compact task summaries and runtime status for Herdr |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [the-inconvenience-store/herdr-agent-session-title](https://github.com/the-inconvenience-store/herdr-agent-session-title) | mirrors the Claude Code or Codex session title |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [advaitbd/herdr-notify](https://github.com/advaitbd/herdr-notify) | Herdr agent-status notifications via signed Hermes webhooks |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [adnichols/herdr-kitty-status](https://github.com/adnichols/herdr-kitty-status) | Live Herdr agent status counts in Kitty tabs |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [carlotran4/waybar-herdr](https://github.com/carlotran4/waybar-herdr) | Event-driven Herdr agent status module for Waybar |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [calebcauthon/herdr-theos-settler](https://github.com/calebcauthon/herdr-theos-settler) | Settle Herdr agent tabs and workspaces below active |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [cevr/herdr-hunk](https://github.com/cevr/herdr-hunk) | Send Hunk review notes to the correct Herdr |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [spr-networks/spr-herdr](https://github.com/spr-networks/spr-herdr) | Herdr TUI in an SPR-managed KVM microVM |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [tipok/herdr-layouts](https://github.com/tipok/herdr-layouts) | herdr-layouts A [herdr]( plugin that creates workspaces |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [caoer/ccc-herdr-layout](https://github.com/caoer/ccc-herdr-layout) | Visual layout picker plugin for herdr — one |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [timaliev/herdr-layout](https://github.com/timaliev/herdr-layout) | Declarative herdr session layouts — YAML-defined workspaces, tabs, |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [amiramay/herdr-layout-cycle](https://github.com/amiramay/herdr-layout-cycle) | cycle through preset pane layouts, tmux prefix+space style |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [shadowfax92/herdr-layouts](https://github.com/shadowfax92/herdr-layouts) | Tmux-style narrow pane splits and focused-pane equalization |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [phenome/herdr-layout](https://github.com/phenome/herdr-layout) | Herdr Layout Small Herdr plugin for three saved |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [jmarcelomb/herdr-nav](https://github.com/jmarcelomb/herdr-nav) | Pane, tab and workspace navigation plugin for herdr |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [iQua/herdr-flakes](https://github.com/iQua/herdr-flakes) | Flakes plugin for Herdr — mirror and steer |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [fredrikkvalvik/herdr-scratch](https://github.com/fredrikkvalvik/herdr-scratch) | A throwaway shell floating over your herdr session |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [corrius/herdr-numbered-navigation](https://github.com/corrius/herdr-numbered-navigation) | Herdr tool for numbered navigation |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [devenjarvis/herdr-review](https://github.com/devenjarvis/herdr-review) | herdr-planeditor A [herdr]( plugin that brings an interactive |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [pi-dal/herdr-preview](https://github.com/pi-dal/herdr-preview) | A diff-first Herdr review pane with safe Files-only |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [speardragon/herdr-status-platform](https://github.com/speardragon/herdr-status-platform) | Herdr tool for status platform |
| Terminal UX | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [jrswab/herdr-status](https://github.com/jrswab/herdr-status) | Ambient machine status pane for Herdr on Linux |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [markbrutx/pif-herdr-reporter](https://github.com/markbrutx/pif-herdr-reporter) | Herdr status reporter extension for the pif coding |
| Terminal UX | ![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) [bkroeze/omherdr](https://github.com/bkroeze/omherdr) | An Omarchy/Wayland Quickshell Herdr status launcher |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [alex-devdone/raycast-herdr-status-bar](https://github.com/alex-devdone/raycast-herdr-status-bar) | Agent Status Bar Raycast menu-bar extension showing live |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [yuhgo/herdr-tab-marker](https://github.com/yuhgo/herdr-tab-marker) | Claude Code / Codex のタブに、作業内容から生成したタイトルとリポジトリごとの絵文字を自動で付ける herdr hook |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [jeph/herdr-pane-balancer](https://github.com/jeph/herdr-pane-balancer) | Automatically balance, equalize, and tile Herdr terminal panes |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [masatokawano/to-herdr](https://github.com/masatokawano/to-herdr) | zellij → herdr terminal setup migration (config + |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [Tetat-Chulchue/meadow](https://github.com/Tetat-Chulchue/meadow) | Mouse-driven file explorer pane for the herdr terminal |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [jfdg01/herdr-claude-setup](https://github.com/jfdg01/herdr-claude-setup) | My herdr terminal + Claude Code workflow (caveman/ponytail, |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [jlangston/herdr-clipboard](https://github.com/jlangston/herdr-clipboard) | Clipboard history for the herdr terminal multiplexer — |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [RooseveltAdvisors/herdr-leap](https://github.com/RooseveltAdvisors/herdr-leap) | EasyMotion/leap-style character jump + select-to-copy for the Herdr |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [supex0fan/herdr-claude-swap](https://github.com/supex0fan/herdr-claude-swap) | Resume herdr's Claude Code panes under the claude-swap |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [kikyous/herdr-claude-usage](https://github.com/kikyous/herdr-claude-usage) | Claude Usage — Herdr plugin Once herdr starts, |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [lucasleon2107/herdr-claude-launcher](https://github.com/lucasleon2107/herdr-claude-launcher) | open a new tab with Claude Code already |
| Terminal UX | ![Astro](https://img.shields.io/badge/-555555?logo=astro&logoColor=white&style=flat-square) [alanpcurrie/herdr-claude](https://github.com/alanpcurrie/herdr-claude) | herdr claude demo output |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [quinnjr/herdr-claude-profile](https://github.com/quinnjr/herdr-claude-profile) | switch and manage claude-profile profiles from an overlay |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [allexborysov/herdr-claude-auto-title](https://github.com/allexborysov/herdr-claude-auto-title) | herdr-claude-auto-title Auto-generated session titles for [Herdr]( panes running |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [tigorlazuardi/herdr-claude-retry](https://github.com/tigorlazuardi/herdr-claude-retry) | herdr-claude-retry Watches Claude CLI panes running inside [herdr]( |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [floco/herdr-claude-resume](https://github.com/floco/herdr-claude-resume) | that detects Claude Code's 5-hour rate limit |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ram4-dev/herdr-codex-usage](https://github.com/ram4-dev/herdr-codex-usage) | for installed-agent detection and usage quota visibility |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ViSHNUPrABU/herdr-codex](https://github.com/ViSHNUPrABU/herdr-codex) | claude-code-herdr-plugin unofficial · v1.3.0 · mit · |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [bestony/herdr-codex-capacity-retry](https://github.com/bestony/herdr-codex-capacity-retry) | Make Codex in Herdr auto continue |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [jievince/herdr-codex-app](https://github.com/jievince/herdr-codex-app) | Turn Herdr into a terminal-first Codex app |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [kogakure/dotfiles](https://github.com/kogakure/dotfiles) | Herdr tool for dotfiles |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [alexarthurs/herdr-notes](https://github.com/alexarthurs/herdr-notes) | Persistent markdown notes pane for herdr - one |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [hrdle/hrdle](https://github.com/hrdle/hrdle) | hrder web frontend tools |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [phillipleblanc/ad](https://github.com/phillipleblanc/ad) | Agent dispatch CLI for messaging between local herdr |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [Howryann/herdr-monitor](https://github.com/Howryann/herdr-monitor) | Read-only HTTP monitor for herdr agent status, |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [TheMetalStorm/herdr-cline-plugin](https://github.com/TheMetalStorm/herdr-cline-plugin) | that makes a plain Cline CLI launched |
| Terminal UX | ![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) [stappmus/Udder](https://github.com/stappmus/Udder) | See your Herdr agents in the Omarchy bar, |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [mrcndz/herdr-routines](https://github.com/mrcndz/herdr-routines) | that runs scheduled routines |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [gadgj/agent-state-changed-bell](https://github.com/gadgj/agent-state-changed-bell) | agent state changed bell |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [milkyskies/herdr-attention](https://github.com/milkyskies/herdr-attention) | one keypress jumps focus to the next agent |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [MartinKei/herdr-tab-notes](https://github.com/MartinKei/herdr-tab-notes) | Simple herdr plugin for taking notes |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [arvindparmar-me/herdr-markdown-viewer](https://github.com/arvindparmar-me/herdr-markdown-viewer) | drag-select a markdown path and press prefix+m |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [edmundmiller/herdr-plugin-dotfiles-dev-layout](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout) | for opening my dotfiles dev workspace layout |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [zerkc/herdr-notify-firebase](https://github.com/zerkc/herdr-notify-firebase) | FCM push on agent status changes |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [varelaseb/tabherd](https://github.com/varelaseb/tabherd) | agent pinning, color-coded session tabs, and collapsible workspace |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [johnlindquist/herdr-pane-update-timestamps](https://github.com/johnlindquist/herdr-pane-update-timestamps) | for timestamped, scrollable pane output observations |
| Terminal UX | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [donghaolicd/herdr-teams-notify](https://github.com/donghaolicd/herdr-teams-notify) | for bounded Microsoft Teams agent lifecycle notifications |
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [QuantumDancer/herdr-last-tab](https://github.com/QuantumDancer/herdr-last-tab) | to switch to the last focussed tab |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [capt-marbles/herdr-jcode-integration](https://github.com/capt-marbles/herdr-jcode-integration) | for Jcode lifecycle state and session reporting |
| Terminal UX | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [nmogil/agent-skill-patterns](https://github.com/nmogil/agent-skill-patterns) | Portable Agent Skills patterns for Claude Code, Hermes, |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [datalover37/dotfiles](https://github.com/datalover37/dotfiles) | the configuration of dotfiles ghostty, zsh, herdr, opencode |
| Terminal UX | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [The-Dave-Stack/herdr-keymap](https://github.com/The-Dave-Stack/herdr-keymap) | shows every keybinding in an overlay palette |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Angel-O/dotfiles](https://github.com/Angel-O/dotfiles) | Modular chezmoi setup for Ghostty, Herdr, OpenCode, Starship, |
| Terminal UX | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [DMelisena/shipmates](https://github.com/DMelisena/shipmates) | Hermes plugin for out of the box kun |
| Desktop | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [joeseesun/herdr-guide](https://github.com/joeseesun/herdr-guide) | Herdr 软件全面调研、使用价值分析与上手教程 | An independent practical guide |
| Desktop | ![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) [cxnmai/dms-herdr-plugin](https://github.com/cxnmai/dms-herdr-plugin) | DankMaterialShell widget for monitoring and controlling Herdr agents |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [sunnoy/livis](https://github.com/sunnoy/livis) | 在手机上盯着自己主机上跑的编码 agent —— 自托管的 Android 终端客户端，SSH/Mosh + herdr/tmux，agent |
| Desktop | ![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) [spencerbull/xeneon-edge-agents](https://github.com/spencerbull/xeneon-edge-agents) | A fail-closed Omarchy and Herdr agent command center |
| Desktop | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [A1exthegreat/herdr-agent-notify](https://github.com/A1exthegreat/herdr-agent-notify) | desktop notifications when agents finish working, need confirmation, |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [TianZuo555/pi-herdr-agents](https://github.com/TianZuo555/pi-herdr-agents) | Pi extension for role-guided peer coding agents |
| Desktop | ![Java](https://img.shields.io/badge/-555555?logo=openjdk&logoColor=white&style=flat-square) [mohamed-essam/herdr-mobile](https://github.com/mohamed-essam/herdr-mobile) | Monitor and unblock your herdr agents |
| Desktop | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Tatendaz/herdr-launcher](https://github.com/Tatendaz/herdr-launcher) | Unofficial macOS Dock launcher for the herdr TUI |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [hbacheller-tribe/herdrStatusWidget](https://github.com/hbacheller-tribe/herdrStatusWidget) | A widget for Herdr that shows which tabs |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [leset0ng/pi-todo-herdr](https://github.com/leset0ng/pi-todo-herdr) | Hierarchical task tools for Pi with a live |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [cedrus-8864/herdr-prompt-reply](https://github.com/cedrus-8864/herdr-prompt-reply) | Answer herdr agent permission prompts straight |
| Desktop | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [richardadonnell/herdr-claude-manager](https://github.com/richardadonnell/herdr-claude-manager) | Tile a Herdr workspace with N Claude Code |
| Desktop | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [undivisible/herdr-gui](https://github.com/undivisible/herdr-gui) | a gui surface for herdr + more |
| Desktop | ![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) [yigitkonur/herdr-wezterm-setup](https://github.com/yigitkonur/herdr-wezterm-setup) | My macOS terminal setup |
| Desktop | ![HTML](https://img.shields.io/badge/-555555?logo=html5&logoColor=white&style=flat-square) [DavidTWhitlatch/dotfiles-template](https://github.com/DavidTWhitlatch/dotfiles-template) | Shareable macOS dotfiles |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [skeletor-js/bessie](https://github.com/skeletor-js/bessie) | Native macOS client for Herdr |
| Desktop | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [KaminariOS/whip](https://github.com/KaminariOS/whip) | Keep whipping AI agents at home painlessly while |
| Desktop | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [miiraheart/herdr-beads](https://github.com/miiraheart/herdr-beads) | A beads (bd) task board for herdr |
| Desktop | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [zerodice0/herdr-booking-task-plugin](https://github.com/zerodice0/herdr-booking-task-plugin) | Schedule Herdr agent prompts and local CLI commands |
| Desktop | ![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) [calorie/herdr-auto-focus](https://github.com/calorie/herdr-auto-focus) | Focus Herdr agents that need attention after macOS |
| Desktop | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [quinnjr/herdr-notifications](https://github.com/quinnjr/herdr-notifications) | Native OS desktop notifications for herdr agent status |
| Desktop | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [AlexBSoD/qubeherd](https://github.com/AlexBSoD/qubeherd) | Push herdr agent state, host clock and keyboard |
| Desktop | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [neefrehman/herdr-caffeinate](https://github.com/neefrehman/herdr-caffeinate) | Keeps macOS awake (even with the lid closed) |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [8-BitRhyon/bantay-tui](https://github.com/8-BitRhyon/bantay-tui) | Native macOS notch HUD for herdr agent status |
| Desktop | ![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) [omerturhan/herdr-touchbar](https://github.com/omerturhan/herdr-touchbar) | Shows working and blocked herdr agents |
| Desktop | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [afogel/shepherdr](https://github.com/afogel/shepherdr) | Shepherd delegated coding agents into visible, auditable herdr |
| Packaging | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [Yassimba/loom](https://github.com/Yassimba/loom) | Curated agent skills, Pi packages, and Herdr plugins |
| Packaging | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [ezcorp-org/herdr-git-status](https://github.com/ezcorp-org/herdr-git-status) | per-space git working-tree status (staged/modified/untracked/conflicts) in the sidebar, |
| Packaging | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [miya10kei/herdr-plugin-sidebar](https://github.com/miya10kei/herdr-plugin-sidebar) | herdr-plugin-sidebar Googleカレンダーの予定とGitHub Actionsの実行状況を、サイドバー風のsplitペインに表示する [herdr]( プラグイン。 📅 2026-01-15 |
| Packaging | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [khatriafaz/herdr-plugin-agent-repo](https://github.com/khatriafaz/herdr-plugin-agent-repo) | that shows agent, repository, and branch names |
| Packaging | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [levi-qiao/herdr-agent-quota](https://github.com/levi-qiao/herdr-agent-quota) | Never hit a quota limit mid-task |
| Packaging | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [maxto/dotfiles](https://github.com/maxto/dotfiles) | Personal WSL2 (Windows 11) human-AI terminal dev environment |
| Packaging | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [ondratuma/herdr-status-plugin](https://github.com/ondratuma/herdr-status-plugin) | Per-pane activity status for herdr agent panes — |
| Packaging | ![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) [cedrus-8864/herdr-sidebar-numbers](https://github.com/cedrus-8864/herdr-sidebar-numbers) | show workspace and agent position numbers |
| Packaging | ![Dart](https://img.shields.io/badge/-555555?logo=dart&logoColor=white&style=flat-square) [ablause/herdr-flutter](https://github.com/ablause/herdr-flutter) | A herdr sidebar to watch, hot reload |
| Packaging | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost) | Show estimated Codex session cost in the Herdr |
| Packaging | ![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) [aorumbayev/herdr-ctx](https://github.com/aorumbayev/herdr-ctx) | Claude context-window indicator for herdr sidebar panes |
| Packaging | ![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) [samuelbaldwin05/herdr-burn](https://github.com/samuelbaldwin05/herdr-burn) | Live Claude Code cost/quota per pane |
| Packaging | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [tyler-jewell/herdr-bootstrap](https://github.com/tyler-jewell/herdr-bootstrap) | Idempotent machine bootstrap for Herdr + Node/ Grok |
| Packaging | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [chrisjohnson/asdf-herdr](https://github.com/chrisjohnson/asdf-herdr) | for the asdf version manager |
| Packaging | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [mougua/herdr-reasonix](https://github.com/mougua/herdr-reasonix) | for detecting and displaying Reasonix agents |
| Work in progress | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [GoCodeAlone/mission-control-provider-herdr](https://github.com/GoCodeAlone/mission-control-provider-herdr) | External Herdr session runtime provider for Mission Control |
| Work in progress | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [robinbraemer/herdr-axi](https://github.com/robinbraemer/herdr-axi) | Agent-ergonomic CLI for Herdr terminal workspace operations |
| Work in progress | ![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) [yoshimi-I/gengar.nvim](https://github.com/yoshimi-I/gengar.nvim) | Editor-first Neovim environment built for herdr — agents |

---

[↑ Back to contents](#contents)

---

## Run & orchestrate agents

The headline use: more than one agent working at once, in panes you can watch.

### Orchestration › Official Skills & Foundation

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[ogulcancelik/herdr · SKILL.md](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md)**

The official, upstream skill file: drop-in instructions that teach an agent already running inside a Herdr pane to use the multiplexer — list workspaces, tabs, and panes, spawn helpers, send input, and wait on output and agent status. The canonical starting point before reaching for any of the third-party skills below.

[↑ Back to contents](#contents)

### Orchestration › Multi-Agent Fleets & Supervisors

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

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ogulcancelik/pi-extensions](https://github.com/ogulcancelik/pi-extensions)**

A maintained suite of Pi coding-agent extensions from Herdr's creator, spanning ephemeral overlays, parallel-agent spawning, session recall, and — through the `pi-herdr` package — direct orchestration of Herdr panes, tabs, and workspaces from a Pi session. Install any package individually with `pi install npm:@ogulcancelik/<name>`. The reference collection for Pi users who want first-party Herdr integration alongside a rich set of productivity extensions.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[LittleDrinks/herdr-orchestrator-skill](https://github.com/LittleDrinks/herdr-orchestrator-skill)**

Turns the main Claude Code session into a coordinator that plans, dispatches workers to Herdr panes, and monitors their output — without writing code itself. Includes Python monitoring helpers, a YAML state-machine template, and prompt files for implementation, verification, and review roles. For teams who want enforced plan-then-execute discipline in Herdr without building their own multi-agent harness.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[david-lutz/herdr-claude-teams](https://github.com/david-lutz/herdr-claude-teams)**

Shims Claude Code's experimental agent-teams feature onto Herdr so teammates spawn as native Herdr panes rather than tmux panes, using a translation layer between tmux commands and the Herdr socket API. Requires Herdr 0.6.10 and integrates with the sidebar, metadata, and notification surfaces natively. For Claude Code users who want visible team-mode panes without tmux inside a Herdr workspace.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[tomoasleep/herdr-symphony](https://github.com/tomoasleep/herdr-symphony)**

A headless orchestrator (docs in Japanese) that polls a GitHub Projects board for candidate issues, creates worktrees with `gwq`, and runs an `opencode` agent per issue in a Herdr pane, using `herdr agent wait` to detect completion. Agent state and logs live entirely in Herdr workspaces rather than a separate dashboard. For teams who want a background issue-to-PR pipeline driven from a project board.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[joelhooks/pi-bellwether](https://github.com/joelhooks/pi-bellwether)**

A Pi package that exposes Herdr's agent, pane, and session control surface as Pi slash commands and LLM tools — start, send, read, focus, and stop agents without leaving a Pi conversation. It's deliberately generic runtime plumbing that product-specific loop extensions can build on rather than reimplement. For Pi users who want to drive Herdr orchestration from inside Pi.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[NickPittas/pi-herdr-subagents](https://github.com/NickPittas/pi-herdr-subagents)**

A Pi extension that hooks Pi's async subagent event bus, tracking each run's id, task, status, and session file, and exposes a TUI dashboard where you can browse live subagents, open their session in a new tab, focus an existing pane, or spawn one directly into a pane. Unlike the shared-pane model of `aldrickdev/herdr_subagents`, it watches without changing how subagents run. For Pi users with many concurrent subagents who want one navigable view of the whole fleet.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kirel/herdr-subagents](https://github.com/kirel/herdr-subagents)**

A Pi extension that spawns each subagent into its own Herdr pane or tab, manages the session files, and notifies the parent session on completion so the orchestrator picks up results without polling. Child panes stay open after reporting back, leaving room for follow-up work, and each subagent can run on a different model. A dedicated-pane alternative to the shared-pane `aldrickdev/herdr_subagents`.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[bakescakes/claude-orchestration](https://github.com/bakescakes/claude-orchestration)**

A Claude Code plugin bundling five orchestration skills — a full-lifecycle "boss-mode" conductor, a one-shot Herdr fan-out, the Herdr CLI reference, an end-of-session durability auditor, and a docs scaffolder — alongside hooks that guard worktree hygiene, route prompt events, and report session state. Boss-mode owns a backlog of parallel initiatives end-to-end: spawn, build, QA gate, merge, deploy, verify-live, teardown. For Claude Code users who want a pre-wired multi-skill setup rather than assembling the pieces.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[erwins-enkel/shepherd](https://github.com/erwins-enkel/shepherd)**

Self-hosted mission control for interactive coding agents: spawn, watch, and steer many real Claude Code or Codex sessions in parallel from a browser or phone, each running in its own git-worktree pane that Herdr multiplexes. Plan-review, PR-critic, and merge-train gates layer engineering discipline on top of the parallelism. For teams running several agents at once who want a supervised fleet rather than a wall of terminals.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[aashishd/herdr-agent-messenger](https://github.com/aashishd/herdr-agent-messenger)**

A lightweight messaging specification and wire contract that enables live AI agents in separate Herdr panes to exchange targeted, self-contained single-line messages. Agents address peers via memorable two-word call-signs and wait on idle status to coordinate tasks without sharing full session contexts. For developers orchestrating multi-agent workflows who want decoupled inter-agent communication.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[aemrebarut/herdr-dagr](https://github.com/aemrebarut/herdr-dagr)**

Renders a live Directed Acyclic Graph (DAG) of an agent swarm directly inside a Herdr split pane, displaying tasks, retry attempts, review gates, and evidence tiers. Draws progress history similar to `git log --graph` based on a structured `run.json` contract updated by your orchestrator. For teams running multi-stage agent workflows who want transparent, real-time pipeline visualization without external web UIs.

![YAML](https://img.shields.io/badge/-555555?logo=yaml&logoColor=white&style=flat-square) **[aorumbayev/herdr-workflows](https://github.com/aorumbayev/herdr-workflows)**

Automates repetitive development routines and agent setup steps through declarative YAML workflow manifests. Each workflow executes ordered sequences of commands and agent interactions directly inside Herdr workspaces. For engineers looking to standardize recurring multi-step terminal tasks into repeatable scripts.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[bredebjorhovd/herdr-board](https://github.com/bredebjorhovd/herdr-board)**

A kanban-style automation engine that feeds GitHub issues into autonomous agents running across dedicated Herdr panes. Each card tracks agent progress, prompts, and run history, routing completed work straight into PR review cycles. Built for teams seeking an organized, card-based pipeline for autonomous agent fleets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[caioniehues/herdmates](https://github.com/caioniehues/herdmates)**

Brings Claude Code multi-agent teams into Herdr using a native teammux translation layer, dedicated focus panes, and a mission control overview board. Teammate agents coordinate in isolated panes while reporting status and task progress back to the orchestrator. For developers running collaborative Claude Code agent teams who want full terminal-native visibility.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[clawsouls/clawsouls-herdr-plugin](https://github.com/clawsouls/clawsouls-herdr-plugin)**

Connects ClawSouls persona definitions into Herdr workspaces to inject specialized behavioral specifications into running agent sessions. It configures persona environments and behavioral constraints across Claude Code and other supported agents in multiplexed panes. For teams standardizing agent roles and persona specifications across multi-agent workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Elio2000/herdr-peer-review](https://github.com/Elio2000/herdr-peer-review)**

Spawns a secondary coding agent in a dedicated split pane to perform automated peer reviews on active workspace diffs. It drives an autonomous review-revise-decide loop with read-only safeguards and includes a Claude Code skill for orchestration. For engineers who want continuous automated sanity checks on agent-authored changes before committing.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[jeffory/herdr-walkietalkie](https://github.com/jeffory/herdr-walkietalkie)**

Enables token-efficient delegation between agents by letting an orchestrator spawn Claude, OpenCode, or Antigravity worker sessions into dedicated Herdr tabs and worktrees. Uses file-based handoffs and structured completion signals to avoid bloated context windows. For developers building hierarchical multi-agent teams inside Herdr.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[joelhooks/herdr-pings](https://github.com/joelhooks/herdr-pings)**

Delivers turn-level wake notifications and crash detection for AI agents running inside Herdr panes, pairing a Pi extension with a companion wait CLI. Assigns playful Discworld callsigns to worker agents so you can distinguish concurrent fleet tasks at a glance. For developers orchestrating Pi agent swarms who need immediate alerts on turn completion or unexpected failure.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[joshka0/herdr-watcher](https://github.com/joshka0/herdr-watcher)**

Enables durable execution continuations and detached worker callbacks for agents running inside Herdr. It tracks asynchronous background tasks across disconnects and triggers agent resumes via the Herdr socket API when long-running jobs finish. For orchestrator authors building resilient multi-step workflows that must survive session interruptions.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kay-ws/herdr-island](https://github.com/kay-ws/herdr-island)**

Pinpoints Herdr agents that are blocked or waiting for user feedback and displays the exact reason for the stoppage. Filters the Agents sidebar panel down to only the agents that require immediate human action. Built for engineers supervising large concurrent agent swarms who want zero-distraction attention routing.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kiitosu/herdr-jira-board](https://github.com/kiitosu/herdr-jira-board)**

A terminal Kanban board for Jira running inside a Herdr pane with one-key Claude Code session launching. Lets you transition Jira ticket states directly from the TUI and displays live agent status badges on active ticket cards. For teams tracking sprint work in Jira who want hands-on agent orchestration from their backlog.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[natori-hrj/herdr-standup](https://github.com/natori-hrj/herdr-standup)**

Aggregates recent Git commits and uncommitted diffs across all active agent workspaces into a unified standup summary pane. It queries each workspace's local repository state to report what each agent completed and what remains in progress. For developers orchestrating multi-agent projects who need an at-a-glance digest of fleet activity without checking each repository manually.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[natori-hrj/herdr-triage](https://github.com/natori-hrj/herdr-triage)**

Ranks active Herdr agents by attention priority, surfacing blocked and stalled agents at the top of your list based on idle and wait duration. Helps you quickly spot which worker needs input or unblocking without scanning every workspace. For developers supervising large agent fleets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[neilwashere/herdr-unrecoverable](https://github.com/neilwashere/herdr-unrecoverable)**

A watchdog plugin that monitors Pi coding-agent sessions in Herdr panes and recovers them when stalled by terminal provider errors. It verifies failures against session transcripts, displays an in-interface countdown, and automatically submits continue commands up to three times. For developers running unattended Pi agent fleets who want automatic error recovery without manual restarts.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[steig/worktender](https://github.com/steig/worktender)**

Connects GitHub issues directly to isolated coding agent sessions running in dedicated git worktrees inside Herdr. It handles branch creation, worktree setup, agent invocation, and lifecycle teardown through a single command. For teams who want a streamlined issue-to-implementation workflow with isolated workspaces per ticket.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[StructuPath/herdr-browser](https://github.com/StructuPath/herdr-browser)**

Streams a live, interactive Chromium browser directly inside a Herdr pane with support for clicks, scrolling, and error logging. It allows human operators to take over agent-driven Playwright sessions on the fly while persisting per-session browser profiles. For teams building web-testing and autonomous browser agents that need live visual inspection.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[StructuPath/herdr-conductor](https://github.com/StructuPath/herdr-conductor)**

Coordinates task-bound producer and review gate roles across visible agent panes using strict task and report contracts, git compare-and-swap integration, and a passive board pane. For teams looking for operator-attended, deterministic multi-agent delivery workflows. ---

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[StructuPath/herdr-swarm](https://github.com/StructuPath/herdr-swarm)**

Runs multiple coding agents in parallel by provisioning dedicated git worktrees and branches for each agent pane. Provides real-time visibility into parallel modifications and lets you review and harvest the best implementation before merging. For teams executing concurrent, speculative agent workflows.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[voodootikigod/adlc-herdr](https://github.com/voodootikigod/adlc-herdr)**

Integrates the Agentic Development Lifecycle (ADLC) framework into Herdr, displaying per-pane gate phases, ticket states, and backlog boards right beside running agents. It provides actions to unblock gated milestones and track multi-agent fleet execution in real time. For teams running structured, gate-enforced agent workflows who need visual lifecycle telemetry.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[wilbeibi/herdr-catchup](https://github.com/wilbeibi/herdr-catchup)**

Enables cross-agent session handoffs directly from active Herdr panes across Claude Code, Codex, Cursor, Cline, and OpenCode. It captures and summarizes context from a live pane so you can fork tasks or transition work to another agent without losing state. For developers who alternate between different AI coding tools during a single development workflow.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[zhenyufu/herdr-cadence](https://github.com/zhenyufu/herdr-cadence)**

Coordinates a Lead agent that triages tasks and dispatches specialized worker agents into isolated Herdr tabs and git worktrees. Ensures clean git baselines before agent creation and injects focused task context into worker panes without context bloat. For developers who want structured, role-based delegation across agent fleets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[edxeth/pi-subagents](https://github.com/edxeth/pi-subagents)**

Pi multi-agent framework for power users: background/foreground agents, sync/async coordination, fresh/forked context, child-to-parent messaging, orchestrator mode, supports tmux | cmux | ZelliJ | WezTerm | Herdr. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[vinicius91carvalho/harness-engineering](https://github.com/vinicius91carvalho/harness-engineering)**

Harness Engineering for Claude Code, Codex, Opencode, Pi and integration with Herdr. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[jillesme/pi-herdr-squad](https://github.com/jillesme/pi-herdr-squad)**

Visible, strictly read-only Herdr investigation squads for Pi. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[muslihudindev/herdr-agent-orchestrator](https://github.com/muslihudindev/herdr-agent-orchestrator)**

Local-first, provider-agnostic multi-agent software engineering orchestration for the real Pi Coding Agent TUI running inside HerdR. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[cowcow02/herdr-agent-orchestrator](https://github.com/cowcow02/herdr-agent-orchestrator)**

Event-driven orchestration for one existing controller agent. Herdr observes. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[mikeyobrien/herdr-agent-profiles](https://github.com/mikeyobrien/herdr-agent-profiles)**

Data-driven CLI harness and model profiles for Herdr. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[chetanunadkat-lang/herdr-fleet](https://github.com/chetanunadkat-lang/herdr-fleet)**

Run a fleet of Claude/Codex coding agents in herdr terminal panes — orchestrator skills, hm CLI, agent defs, and installer for Claude Code. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[misty-step/kelpie](https://github.com/misty-step/kelpie)**

Phone-first console for triaging a fleet of omp coding agents in herdr terminal workspaces. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[inbeomheo/herdr-orchestra](https://github.com/inbeomheo/herdr-orchestra)**

Multi-agent orchestration skill for herdr — Claude Code as conductor driving codex/grok/gemini/claude workers in herdr panes. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[persinac/agents-nexus](https://github.com/persinac/agents-nexus)**

Batteries-included toolkit for running fleets of AI coding agents on the herdr multiplexer — substrate, plugins, memory/observability, conductor missions, opt-in installer. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[eciuca/herdr-drover](https://github.com/eciuca/herdr-drover)**

Drover: Herdr agent orchestrator for Claude Code, Codex, Kira CLI, and tmux-style workflows. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kyokosawada/viu](https://github.com/kyokosawada/viu)**

Mobile client for a herdr agent fleet - see your agents, answer them by voice or keyboard, from your phone. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[terafin/herdr-restart-always](https://github.com/terafin/herdr-restart-always)**

Supervise herdr agent panes and always restart whatever the pane is running (claude, hermes, codex, pi, opencode, ...) whenever the agent dies. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[hewel/herdr-harness-coordinator](https://github.com/hewel/herdr-harness-coordinator)**

Herdr plugin for coordinating autonomous coding-agent harnesses. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[yanekyuk/pi-herdr-orchestrator](https://github.com/yanekyuk/pi-herdr-orchestrator)**

Project-agnostic Herdr orchestration for Pi. Coordinates multiple agent loops across isolated panes and tracks active task status.

[↑ Back to contents](#contents)

### Orchestration › Subagent Spawners & Delegation

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[mcdonc/mcdonc-pi-herdr](https://github.com/mcdonc/mcdonc-pi-herdr)**

A Pi extension that gives Pi's background-task and conversation-fork features a home in Herdr: `/bg` offloads the running task into a visible pane, and `/tab` forks the conversation into a new tab, both over the socket API. Long builds and parallel workstreams become first-class panes and tabs you can watch, instead of invisible background processes. For Pi users running inside Herdr who want their side-work surfaced, not hidden.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[aldrickdev/herdr_subagents](https://github.com/aldrickdev/herdr_subagents)**

A Pi extension that delegates work to visible subagents in a shared Herdr tab named `subagents`, so you can watch each delegated task directly instead of waiting for a result. Parent Pi sessions get tools to spawn named child agents, steer them mid-run, and read their output when they go idle. Requires `herdr integration install pi` and Pi running inside a Herdr-managed pane.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ogulcancelik/herdr-plugin-github-start](https://github.com/ogulcancelik/herdr-plugin-github-start)**

An official plugin from Herdr's creator that turns a GitHub issue, PR, or discussion into a ready-to-work agent tab — it creates the tab, starts Codex or Claude, renames the session, and sends a structured prompt describing the linked item, all from one bound keypress. It accepts short references like `#614` or `issue 614` as well as full URLs. For developers who kick off agent sessions straight from a GitHub ticket without assembling the context by hand.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[gustavocaiano/opencode-herdr](https://github.com/gustavocaiano/opencode-herdr)**

An OpenCode plugin that watches for subagent session creation and automatically splits a new Herdr pane running `opencode attach` for each one, tiling them in a row-based grid to keep the layout readable. Panes can close automatically on idle, deletion, or error. For OpenCode users who want live visibility into every active subagent without splitting panes by hand.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[machine-machine/ask-fable-skill](https://github.com/machine-machine/ask-fable-skill)**

A Hermes and Claude Code skill that spawns an interactive Claude Code (Fable 5) worker inside Herdr, hands it the prompt through a file, and reads the complete answer back — sidestepping TUI scraping and output truncation. The worker's session UUID is surfaced so a follow-up can resume the same conversation. For users whose primary agent is a lighter tier who want to route deep-reasoning tasks to a more capable model without switching sessions.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[rohanthewiz/herdr-todo](https://github.com/rohanthewiz/herdr-todo)**

A Bubble Tea TUI for prompts you want to run later: jot multi-line entries with optional titles, fuzzy-filter them, then press Enter to paste one into a running Claude Code pane or spin up a fresh `claude` tab in the current workspace. Per-repo backlogs live under `<repo>/.herdr-todo/` so they travel with the project, alongside a global backlog visible everywhere. For engineers who accumulate follow-up prompts mid-session and want to queue them without interrupting the agent.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[freewillythe4th/action-button-agent](https://github.com/freewillythe4th/action-button-agent)**

A bridge that turns an iPhone Action Button into a remote for your own Herdr agents: a bundled iOS Shortcut with Whisper dictation sends a voice-transcribed task over Tailscale through a personal Telegram bot to a Claude Agent SDK operator, which starts or targets the right Herdr lane and replies in Telegram. A self-bootstrapping skill handles the one-time setup. For developers who want to assign work to their Herdr-backed agents from anywhere without opening a laptop.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[noor-latif/herd](https://github.com/noor-latif/herd)**

Two companion scripts that spin up a project-scoped Herdr workspace with an N-agent grid (default 2×2, one Pi agent per pane) keyed to the current directory, and relaunch any dead agents when you return. For anyone who wants a repeatable one-command "start a grid of agents for this repo" setup.

---

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[a2u/herdr-jira](https://github.com/a2u/herdr-jira)**

A Jira TUI plugin built with Ratatui that lets you browse, filter, and transition Jira issues directly inside Herdr. It features one-key task delegation that spins up a new pane or workspace and primes a coding agent with the ticket specifications. For developers managing backlog execution who want to dispatch Jira tickets to terminal agents seamlessly.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim)**

An OpenCode multi-agent suite that delegates tasks to specialized subagents across dedicated Herdr panes. It orchestrates roles like fixers, librarians, and explorers while serializing pane creation and managing split layouts. For OpenCode users running multi-agent workflows inside Herdr.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[cyperx84/herdr-loop](https://github.com/cyperx84/herdr-loop)**

Orchestrates multi-agent execution graphs across Claude Code, Codex, OpenCode, and Pi in dedicated Herdr panes until task convergence. Listens to socket events and pane output to route intermediate results between planner, coder, and reviewer agents across iterative cycles. For developers who want automated, multi-model verification loops running inside Herdr.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[darjss/herdr-orchestrate](https://github.com/darjss/herdr-orchestrate)**

Provides Pi-native orchestration across visible Herdr worker sessions with a live run board, persistent state tracking, and isolated Git worktrees. It implements explicit model routing and thinking-level profiles to separate fast evidence-scouting tasks from higher-tier analysis and review. For Pi users coordinating multi-agent workflows with structured oversight and safety gates.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[GavinTomlins/herdr-oh-my-agent](https://github.com/GavinTomlins/herdr-oh-my-agent)**

Mirrors oh-my-openagent subagent delegations into dedicated Herdr panes or tabs in real time as tasks are dispatched. It captures live agent states, preserves complete scrollback transcripts to disk for post-run inspection, and supports side-by-side splits or tabbed layouts without interfering with agent execution. For OpenCode users who want full terminal visibility into nested subagent delegations.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[JLighter/herdr-spawn](https://github.com/JLighter/herdr-spawn)**

Spawns coding agents into isolated Herdr panes, automatically provisioning a dedicated Git worktree for each agent. Exposes commands to prompt workers, inspect active jobs, and harvest completed task outputs. For orchestrating parallel agent runs without branch collision or workspace clutter.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[vekexasia/pi-extensible-workflows](https://github.com/vekexasia/pi-extensible-workflows)**

A deterministic workflow engine for Pi that orchestrates multi-agent pipelines with on-disk persistence and git worktree isolation. It scripts parallel agent tasks and automatically opens each worker in a dedicated Herdr pane. For Pi users who want structured, checkpointed agent workflows instead of unconstrained fan-out.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[vercel-labs/herdr-vercel-sandbox-plugin](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin)**

Runs terminal coding agents like Claude Code, Codex, and OpenCode inside isolated Vercel Sandbox microVMs while presenting each session as a live Herdr pane. It features upload manifest preview, automatic secret exclusion, and exports agent modifications back to your local worktree as Git patches. For developers who want to execute untrusted or autonomous agent runs safely in ephemeral cloud sandboxes.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[hungv47/herdr-agent-orchestration](https://github.com/hungv47/herdr-agent-orchestration)**

A Herdr-first captain/worker workflow for Hermes, Codex, Grok, OpenCode, Cline, Buzz, and other coding agents. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[jbaham2/herdr-plugin](https://github.com/jbaham2/herdr-plugin)**

Claude Code expert plugin for herdr, the agent-aware terminal multiplexer — multi-agent orchestration, layouts, agent monitoring, workspace/session management, and configuration. AGPL-3.0-or-later. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[noctaIO/herdr-plugin-aos](https://github.com/noctaIO/herdr-plugin-aos)**

Spawn Agentic OS-enabled Claude Code agents in a herdr pane from any workspace. Non-invasive herdr plugin. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[lalanikarim/herdr-skills](https://github.com/lalanikarim/herdr-skills)**

Pi agent skills for herdr terminal workspace management. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[marv1nnnnn/pi-yahe](https://github.com/marv1nnnnn/pi-yahe)**

Yet Another Herdr Extension: one composable herdr tool for Pi — visible, task-driven multi-agent work with automatic async result steering. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[MinhDuyDEV/pi-subagents](https://github.com/MinhDuyDEV/pi-subagents)**

Delegation runtime for Pi: robust task/subagent tool (foreground/background, HerdR/tmux/SDK) + orchestration (claims/leases, context packs, evidence-only review, doctor, telemetry) + pane-creation retry. Runtime-only (no agent profiles). Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[giuseppecrj/pi-herdr-agents](https://github.com/giuseppecrj/pi-herdr-agents)**

Asynchronous subagents and approved review workflows for [Pi]( running exclusively in [Herdr](. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[thkt/herdr-agentchat](https://github.com/thkt/herdr-agentchat)**

herdr plugin: leader/coder two-agent conversation with send-and-wake (Claude Code x Codex). Coordinates multiple agent loops across isolated panes and tracks active task status.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[eliebak/herdr-agent-island](https://github.com/eliebak/herdr-agent-island)**

slop repo from claude that works for me, sharing it here in case it's useful for your agent as well. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[aerain/herdr-agent-orchestration](https://github.com/aerain/herdr-agent-orchestration)**

Herdr pane-based multi-agent orchestration skill for OMP, Claude Code, and other coding agents. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[shubham399/herdr-agents-auto-compact](https://github.com/shubham399/herdr-agents-auto-compact)**

Herdr plugin that auto-compacts AI agent sessions (Claude Code, opencode) so long-running sessions never blow their context window. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[minhtran3124/Brichan](https://github.com/minhtran3124/Brichan)**

epository-native AI Chief of Staff for Codex: bounded project work, Herdr agent orchestration, verified outputs, and durable project memory. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[lucasdeprit/Puppy](https://github.com/lucasdeprit/Puppy)**

Multi-Agent system with herdr terminal & claude code. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Sebastiangmz/herdr-plus](https://github.com/Sebastiangmz/herdr-plus)**

Agent skill: teach AI coding agents to operate the Herdr terminal runtime and orchestrate sub-agents in Herdr spaces. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[yigitkonur/claude-code-herdr-plugin](https://github.com/yigitkonur/claude-code-herdr-plugin)**

Claude Code skill: drive a Codex sub-agent end-to-end through one tool over the herdr terminal multiplexer. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[goatbjh/pi-herdr-claude-subagents](https://github.com/goatbjh/pi-herdr-claude-subagents)**

Direct Herdr-backed Claude oracle, reviewer, and planner execution for Pi. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[EDMND-SRC/herdr-subagents](https://github.com/EDMND-SRC/herdr-subagents)**

OpenCode plugin that launches subagents in named herdr multiplexor panes with auto-intercept, delegation tools, and dynamic grid layout. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[BrianM0330/pi-herdr-snooze](https://github.com/BrianM0330/pi-herdr-snooze)**

Toggle a forced Herdr agent lifecycle state (snooze) via /snooze and a keybind — agent-agnostic pi lifecycle helper. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[shimo4228/herdr-toolkit](https://github.com/shimo4228/herdr-toolkit)**

Claude Code plugin: run Claude Code on top of the Herdr agent multiplexer — cross-vendor task delegation with fabrication-resistant acceptance, and phone-driven detached session spawning. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Idan-Levin/herdr-implement-review](https://github.com/Idan-Levin/herdr-implement-review)**

Herdr workflow for Codex implementation, security scanning, and mother-agent review. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[mithyer/ry-skill](https://github.com/mithyer/ry-skill)**

Custom Pi skills for fast Herdr workflows. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[regenrek/codex-orchestration-herdr](https://github.com/regenrek/codex-orchestration-herdr)**

Reusable Codex Sol/Luna Herdr orchestration skill with deterministic worker pane reuse. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[di-rs/.dotfiles](https://github.com/di-rs/.dotfiles)**

Personal dotfiles: helix, ghostty, zsh/zim, herdr, pi, Claude Code, agent-skills (GNU Stow). Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[sh1ny/herdr-switchyard](https://github.com/sh1ny/herdr-switchyard)**

Human-gated Hermes + Herdr orchestration for isolated OMP coding workers, with Beads as the task ledger. Coordinates multiple agent loops across isolated panes and tracks active task status.

[↑ Back to contents](#contents)

### Orchestration › Autonomous PR & Coding Loops

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[sarmientoF/herdr-pr-loop](https://github.com/sarmientoF/herdr-pr-loop)**

Spawns tester, coder, and reviewer agents in dedicated Herdr tabs and orchestrates them through local task cycles and GitHub PR reviews, storing all state in files rather than session context so runs survive restarts. A human-approval gate and run log keep the loop auditable; a budget cap and pause file let you stop it mid-cycle. For developers who want automated PR review cycles that stay observable and interruptible.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[firegnu/herdr-loop-lab](https://github.com/firegnu/herdr-loop-lab)**

A loop-engineering toolkit that layers three kinds of bounded agent iteration on Herdr: an inner loop that converges a single task through a mechanical gate and an adversarial cross-model judge, a fleet layer that runs batches of tasks in parallel worktrees, and an epic layer that decomposes a large goal and integrates the results into a branch. All state lives on disk so an interrupted run resumes cleanly. For developers who want auditable, convergence-checked agent loops rather than open-ended runs that stall silently.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[Tudor0404/dual-author](https://github.com/Tudor0404/dual-author)**

A Claude Code skill that processes GitHub issues end-to-end inside Herdr: each issue gets its own worktree, a Claude worker implements and pushes a draft PR, then paired Codex and Claude reviewers in split panes run fix-and-review rounds until the diff is clean and auto-merge is armed. A dashboard pane tracks per-issue stage and elapsed time across everything running in parallel. For teams who want a hands-off issue-to-merge pipeline that stays observable in the terminal.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[razajamil/herdr-factory](https://github.com/razajamil/herdr-factory)**

An autonomous coding factory that claims items from Jira or local markdown task files, spins up a Herdr worktree per item, and runs Claude Code through an ordered pipeline of steps (fix → review → PR, or a custom belt), riding each PR through CI and review to merge under a global concurrency cap. Belts are YAML-configured with their source, steps, match predicates, and priority. For teams who want a walk-away pipeline built on Herdr's workspace and worktree primitives.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[machine-machine/herdr-factory-loop-skill](https://github.com/machine-machine/herdr-factory-loop-skill)**

An installable skill that teaches Claude Code or Hermes to orchestrate a fleet of coding agents through Herdr — discovery, spawn, dispatch, fan-out/converge, approval unblocking, and spec-driven loops where `tasks.md` markers map directly to parallel workers. An onboarding TUI sets up the whole factory in one pass across Claude, Hermes, or Cursor. Broader than a coordinator-only skill: it adds steered and meta-orchestration tiers and integrates spec-kit.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[sean1588/herdr-orchestrator](https://github.com/sean1588/herdr-orchestrator)**

A Go control-plane daemon that drives the issue-to-PR loop from a declarative YAML state-graph, using Herdr as the execution backend — it spawns an implementer agent in a worktree, then a reviewer, then polls GitHub's merge gate before squash-merging (dry-run by default). Workflow configs are JSON-Schema-validated and checked with a `validate` subcommand. For teams who want a deterministic, auditable pipeline around agent-driven PRs.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[talent-factory/herdr-linear](https://github.com/talent-factory/herdr-linear)**

Integrates Linear project management directly into Herdr as an interactive issue browser panel. Select any issue and press Enter to spawn a dedicated agent pane pre-configured with the ticket context to start implementation immediately. For developers managing backlog tasks who want to trigger parallel agent runs without switching to a web browser.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[tomasvarga/herdr-sniffr](https://github.com/tomasvarga/herdr-sniffr)**

Dispatches an AI agent in a Herdr pane to run initial quality and bug scans on pull requests, depositing draft comments directly into tuicr. It operates agnostically across Claude, Codex, Cursor, and Grok backends without locking you into a single provider. For code reviewers who want automated preliminary PR analysis before conducting manual reviews.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[w-gitops/herdr-agent-factory](https://github.com/w-gitops/herdr-agent-factory)**

Herdr-native, harness-agnostic multi-agent team launcher and control plane. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[conpiracy/ep-starter](https://github.com/conpiracy/ep-starter)**

Starter factory for Pi inside Herdr — agent multiplexer + minimal extensible coding harness. Coordinates multiple agent loops across isolated panes and tracks active task status.

[↑ Back to contents](#contents)

### Orchestration › Task Queues, Backlogs & Event Triggers

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[0x5c0f/herdr-insight](https://github.com/0x5c0f/herdr-insight)**

A live timeline panel — dockable at the bottom or right — that aggregates agent task events across every Herdr workspace, showing working and blocked states, session IDs, and a deduplicated 7-day history, with individually togglable columns. It follows agents across workspace switches without a manual refresh. For anyone running several agents at once who wants a single panel to see which are active, blocked, or idle.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[carze/herdr-smolmachine](https://github.com/carze/herdr-smolmachine)**

Launches a coding agent fully sandboxed in a libkrun/KVM microVM straight from a Herdr pane, while Herdr keeps its usual multiplexing and detach/reattach UX around the isolated process. A baked agent image and a shell dispatch pipeline handle the VM lifecycle. For Linux users who want hardware-level isolation per agent without giving up Herdr's pane control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[saiashirwad/homestead](https://github.com/saiashirwad/homestead)**

Provisions an isolated worktree per branch or GitHub issue — its own ports, `.env`, and setup — and boots a coding agent into a Herdr pane for each, then tracks status, lands finished branches, and tears them down. It shells out to the Herdr CLI and only runs inside an active Herdr session. For developers running several agents or issues in parallel who are tired of services fighting over port 3000.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[DnzzL/herdr-automations](https://github.com/DnzzL/herdr-automations)**

Schedules recurring prompts and cron jobs that automatically spawn coding agents in fresh Herdr git worktrees for unattended execution. It acts as an automation trigger layer featuring per-task MCP configs, run collision guards, persistent execution histories, and a live monitoring board. For developers who want background agent maintenance, automated refactors, and scheduled tests running overnight.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[nelsonPires5/herdr-board](https://github.com/nelsonPires5/herdr-board)**

A Kanban board plugin with a responsive TUI and background daemon that turns cards into executable prompts dispatched to AI agents in visible Herdr panes. Moving cards across columns triggers agent creation, execution in dedicated tabs, and review gates across multiple workspaces. For developers managing a backlog of agent tasks directly inside their terminal.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ram4-dev/herdr-automations](https://github.com/ram4-dev/herdr-automations)**

Runs scheduled and event-driven agent tasks in Herdr using declarative cron schedules, interval timers, and lifecycle triggers. Features built-in overlap guards to prevent conflicting runs, provisions fresh git worktrees automatically, and logs full execution history. For developers who want reliable unattended agent jobs and background maintenance running inside Herdr.

[↑ Back to contents](#contents)

### Orchestration › General Workflows & Skill Packs

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[luweiCN/herdr-ops](https://github.com/luweiCN/herdr-ops)**

Adds natural-language workspace control on top of Herdr's official skill: say "open a worktree for feat-login off main" and the agent translates it into the right herdr CLI commands, including worktree operations the upstream skill omits. Uses progressive disclosure — a lean primary document plus referenced detail files — to stay light on context. For developers who find the raw Herdr CLI syntax tedious to compose in conversation.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[cloudmanic/herdr-plus](https://github.com/cloudmanic/herdr-plus)**

A first-class Herdr plugin built around two accelerators: Projects, declarative TOML templates that spin up an entire workspace — every tab, pane, and startup command — from a fuzzy picker in one keypress; and Quick Actions, a fuzzy launcher for one-off scripts in the current directory. It installs with or without a local Go toolchain and ships prebuilt binaries. For power users who want one-keypress environment setup across many repositories and a fast palette for recurring tasks.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[madarco/agentbox-herdr-plugin](https://github.com/madarco/agentbox-herdr-plugin)**

Brings the AgentBox sandbox into a Herdr session: a live overlay on `prefix+a`, a one-key shortcut to start a sandboxed VM in the current project, and an `agentbox://` Ctrl-click link handler. The plugin installs from the Herdr marketplace and wires its keybindings through a generated shim so the manifest stays static. For Herdr users who run agents in AgentBox sandboxes and want to reach them without leaving the terminal.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[yangyang0507/herdr-skill](https://github.com/yangyang0507/herdr-skill)**

A refinement of the default Herdr coordination patterns that swaps vague `wait agent-status done` polling for output-marker waits and structured messages carrying sender pane, reply-to metadata, and task kind — so a receiver can answer directly without the sender blocking. Ships a dependency-free `herdr-msg` Bash helper and a CLI reference behind progressive disclosure. For multi-agent workflows where blocking waits create needless stalls between sibling agents.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[bon5co/bermuda](https://github.com/bon5co/bermuda)**

Schedules work and executes each job as an interactive Herdr agent within a dedicated split pane. Coordinates multi-step flows, shared append-only thread logs, and exclusive resource claims that persist across ephemeral sessions. For developers orchestrating structured, observable agent tasks.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[marcjfj-vmlyr/quickTUI](https://github.com/marcjfj-vmlyr/quickTUI)**

Provides OpenTUI-based building blocks and a `/quicktui` agent skill for constructing interactive terminal interfaces inside Herdr. It enables AI coding agents to assemble dashboards, status monitors, and form prompts directly in terminal panes. For developers who want their agents to output interactive TUIs rather than raw text streams.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mikedclarke/herdr-shepherd](https://github.com/mikedclarke/herdr-shepherd)**

Schedules cron routines, heartbeats, and recurring automation scripts directly into visible Herdr workspaces. Keeps background agent maintenance visible and inspectable without manual spawning. Built for developers running autonomous periodic tasks across multi-workspace setups.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[quan-meng/herdr-slurm](https://github.com/quan-meng/herdr-slurm)**

Bridges Slurm HPC job allocations into Herdr by spinning up dedicated workspaces and monitored agent tabs for running compute tasks. It tracks Slurm queue status and surfaces agent progress directly in your terminal without manual polling. For research and ML engineers orchestrating batch-heavy agent workloads across clusters.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[sanirudh17/herdr-agent-handoff](https://github.com/sanirudh17/herdr-agent-handoff)**

Transfers an active coding agent conversation into a fresh session with a different installed agent CLI. It injects the unabridged transcript and execution history directly into the new agent's prompt so you avoid writing manual summaries or re-explaining requirements. For developers switching between specialized models mid-task.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[cobanov/herdr-ntfysh](https://github.com/cobanov/herdr-ntfysh)**

herdr plugin: push ntfy notifications when an agent finishes or needs your input. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[jhochenbaum/herdr-hunk-diff](https://github.com/jhochenbaum/herdr-hunk-diff)**

Review agent-authored changes in hunk from herdr and send inline comments back to the responsible agent. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[pbean/bmad-loop-adapter-herdr](https://github.com/pbean/bmad-loop-adapter-herdr)**

herdr terminal-multiplexer backend for bmad-loop. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[transparent-pegasus/herdrpowers](https://github.com/transparent-pegasus/herdrpowers)**

bringing agentic superpowers to the pane-driven. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[pdjsh/herdr-plugins](https://github.com/pdjsh/herdr-plugins)**

Rust plugins for herdr: a radial agent map and keyboard workspace reordering. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[loopkeep/herdr-plugin-loopreview](https://github.com/loopkeep/herdr-plugin-loopreview)**

Herdr plugin for loopreview. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[y011d4/herdr-plugin-agentweb](https://github.com/y011d4/herdr-plugin-agentweb)**

モニタリング・操作するための herdr プラグインです。小さなローカルブリッジサーバー. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[zoridos/herdr-skill](https://github.com/zoridos/herdr-skill)**

Herdr agent skill — control panes, spawn agents, and coordinate multi-agent workflows from inside a Herdr session. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[TheShellLand/herdr-agent](https://github.com/TheShellLand/herdr-agent)**

. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[hewenyu/herdr-agent](https://github.com/hewenyu/herdr-agent)**

专门用于管理herdr 的agent，方便手机上沟通开发. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[calebcauthon/herdr-agent-copy-paste-fork](https://github.com/calebcauthon/herdr-agent-copy-paste-fork)**

fork by simply copying and pasting, or hotkey the fork into a new pane. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[leonho/herdr-agent-inbox](https://github.com/leonho/herdr-agent-inbox)**

herdr plugin: popup triage list of all agents with their latest recap; Enter jumps to the agent's pane. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[huynguyen03dev/herdr-agent](https://github.com/huynguyen03dev/herdr-agent)**

Agent-agnostic role profiles for running an AI technical department on the Herdr protocol. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[MartinBspheroid/herdr-agent-dash](https://github.com/MartinBspheroid/herdr-agent-dash)**

Herdr Agent Board is a local, keyboard-first Herdr plugin for scanning active coding agents, their semantic state, effective working directory, Git context, and source-labelled activity. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[zerodice0/herdr-agent-labels](https://github.com/zerodice0/herdr-agent-labels)**

Assign readable color-animal names to unnamed Herdr agents. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[okonomi/herdr-agent-queue](https://github.com/okonomi/herdr-agent-queue)**

herdr のエージェントのうち手が止まっているものへ、キー 1 つで待たせている順に巡回. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[hisetu/herdr-agent-skill](https://github.com/hisetu/herdr-agent-skill)**

Provides integration and dedicated functionality for herdr agent skill in Herdr sessions. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[lifez/herdr-agent-dashboard](https://github.com/lifez/herdr-agent-dashboard)**

A read-only local dashboard for unmodified `herdr agent` processes. It runs on the Mac and serves a touch-friendly page that can be opened from a Boox on the same LAN. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ahnsv/maeh](https://github.com/ahnsv/maeh)**

Rust CLI for hmph/herdr agent orchestration. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[eyalev/herdr-web](https://github.com/eyalev/herdr-web)**

Mobile-first web UI for the herdr agent multiplexer — drive your coding agents from a phone. Coordinates multiple agent loops across isolated panes and tracks active task status.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[Xz-FreeMan/herdr-hint](https://github.com/Xz-FreeMan/herdr-hint)**

herdr-hint` 是一个给 Herdr 增加 Agent 会话提示的小工具。. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[dkarter/foreman](https://github.com/dkarter/foreman)**

👷‍♂️🐑 Live Herdr agent monitoring dashboard hardware. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[BlazzzPlay/herdr-office](https://github.com/BlazzzPlay/herdr-office)**

Read-only pixel-art office for visualizing Herdr agents. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[mikhail-angelov/herdr-review-loop](https://github.com/mikhail-angelov/herdr-review-loop)**

Automated cross-review between agents in a herdr workspace — one writes, the other reviews, repeat. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[jwkicklighter/herdr-prompt-library](https://github.com/jwkicklighter/herdr-prompt-library)**

A Herdr plugin for browsing, managing, and inserting reusable local or global Markdown prompts into the focused pane. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[masakirocorp/oh-my-herdr](https://github.com/masakirocorp/oh-my-herdr)**

Oh My Herdr — terminal workspace manager for AI coding agents. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[egriff38/effect-herdr](https://github.com/egriff38/effect-herdr)**

Typed Effect-TS SDK for the herdr terminal-native agent multiplexer. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[Drozerah/herdr-voice](https://github.com/Drozerah/herdr-voice)**

Real-time Text-to-Speech (TTS) voice synthesis plugin for the Herdr Terminal Multiplexer. Intelligent audio stream management for AI coding agents in multi-agent workspaces. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[wenxichang/herdr-pal](https://github.com/wenxichang/herdr-pal)**

control AI-agent in IM via herdr. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[motionharvest/herdr](https://github.com/motionharvest/herdr)**

agent multiplexer that lives in your terminal. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[RenKoya1/herdr-approve-all](https://github.com/RenKoya1/herdr-approve-all)**

herdr plugin: approve every blocked agent at once (one keystroke, all pending permission prompts). Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[nhclink16/herdr-announcer](https://github.com/nhclink16/herdr-announcer)**

Herdr plugin: speaks a one-sentence LLM summary when an agent finishes or needs input — local TTS, ElevenLabs, or any custom command. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[hoon-ch/herdr-gjc-plugin](https://github.com/hoon-ch/herdr-gjc-plugin)**

GJC (Gajae Code) plugin that reports agent lifecycle (idle/working/blocked, launch/exit) to the herdr multiplexer. Coordinates multiple agent loops across isolated panes and tracks active task status.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[narumiruna/herdr-web](https://github.com/narumiruna/herdr-web)**

A terminal-first browser workbench for the herdr agent runtime. Coordinates multiple agent loops across isolated panes and tracks active task status.

![AutoHotkey](https://img.shields.io/badge/-555555?logo=autohotkey&logoColor=white&style=flat-square) **[wtcrowe4/DialDeck](https://github.com/wtcrowe4/DialDeck)**

Surface Dial control surface for agent workflows — keyless AutoHotkey v2 engine driving herdr agent orchestration + dev/modeling macros. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[IgorWarzocha/herdr-annotations](https://github.com/IgorWarzocha/herdr-annotations)**

Collect annotations on terminal selections and stage them into Herdr agents. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[huntergdavis/dunkingsheep](https://github.com/huntergdavis/dunkingsheep)**

Keep herdr agents engaged: auto-send text to herdr panes on an interval (a herdr-native Dunking Bird). Coordinates multiple agent loops across isolated panes and tracks active task status.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[EricBois/herdr-nudge](https://github.com/EricBois/herdr-nudge)**

Arm a continue-nudge on a herdr agent — fire at a set time, or when it goes idle/blocked. Coordinates multiple agent loops across isolated panes and tracks active task status.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ryanlewis/herdr-workspace-renamer](https://github.com/ryanlewis/herdr-workspace-renamer)**

herdr plugin: syncs agent session names onto workspace labels. Coordinates multiple agent loops across isolated panes and tracks active task status.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[andpeicunha/herdr-output-comment-composer](https://github.com/andpeicunha/herdr-output-comment-composer)**

Herdr plugin: annotate AI agent output inline with comments. Coordinates multiple agent loops across isolated panes and tracks active task status.

[↑ Back to contents](#contents)

---

## Connect over socket & MCP

Driving Herdr from the outside: Unix socket clients, MCP servers, and push alerts.

### Connect › Model Context Protocol (MCP) Servers

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[eugeneb50/herdr-mcp](https://github.com/eugeneb50/herdr-mcp)**

An MCP server that exposes Herdr to any MCP-speaking client — Claude Desktop, Cursor, Claude Code — as 21 tools for discovering, launching, reading, and writing panes. A recipe engine chains those calls into reusable flows with `{{ step.result.path }}` variable passing, reachable over both MCP and an HTTP bridge, with a bundled React playground for trying them out by hand.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[runchr-works/herdr-mesh](https://github.com/runchr-works/herdr-mesh)**

Another MCP server, this one tuned for agents coordinating agents: it hands any MCP-capable client tools to read another agent's pane, relay a message, hand off a task, spawn an agent, and wait on a result. It turns manual copy-paste between panes into one-sentence orchestration, and `herdr-mesh install` auto-registers itself with whichever agents (Claude Code, Codex, opencode) you have installed.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[54rt1n/herdr-simple-mcp](https://github.com/54rt1n/herdr-simple-mcp)**

A single-binary MCP server that exposes Herdr's socket API as MCP tools with no state of its own — each call opens a fresh socket, sends one request, and returns. It covers 75 methods across workspace, tab, pane, agent, layout, and plugin surfaces, with named profiles (`coordinator`, `client`, `observer`) to scope the tool set per agent role and `HERDR_MCP_DENY` globs for finer removal; an unknown profile falls back to read-only. A leaner, role-aware alternative to the recipe-engine `herdr-mcp` for wiring agents straight to Herdr.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Phoobobo/herdr-agent-config-manager](https://github.com/Phoobobo/herdr-agent-config-manager)**

A hybrid CLI and Herdr plugin that scans, audits, and bulk-manages agent skills, MCP servers, plugins, and lifecycle hooks across all workspaces. Prevents configuration drift by standardizing agent capabilities and dependencies from a central manifest. For developers running varied agent fleets who want consistent tooling and hooks without manual per-workspace setup.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[islam3zzat/herdr-mcp](https://github.com/islam3zzat/herdr-mcp)**

MCP server that lets AI assistants orchestrate coding agents running in. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[bonsai/herdr-mcp](https://github.com/bonsai/herdr-mcp)**

Herdr tab control from opencode via MCP. Also a Herdr plugin. Exposes a communication bridge and socket transport for remote inspection and control.

[↑ Back to contents](#contents)

### Connect › Socket API Clients & SDKs

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client)**

A zero-dependency Python client for Herdr's Unix socket, so you can script the multiplexer instead of pressing keys. It handles the tedious parts — socket discovery, request envelopes, typed errors, event subscriptions, pane reads and waits — with ten convenience helpers and a raw `request()` escape hatch validated against the full method surface. The fastest way to build your own automation.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[jerryfane/herdr-codex-usage-kit](https://github.com/jerryfane/herdr-codex-usage-kit)**

Publishes Codex subscription quota — remaining 5-hour and weekly usage — into the Herdr agents sidebar as compact labels refreshed every 30 seconds, and opens a live usage dashboard in any shell pane. It reads Codex's own JSONL session logs without calling an API or consuming tokens, and installs as a systemd service plus two terminal commands. For Codex users running on Linux who want quota awareness without leaving the Herdr workspace.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[lib-x/herdr-sock-go](https://github.com/lib-x/herdr-sock-go)**

A Go module that speaks Herdr's newline-delimited JSON socket protocol directly, generated against the 0.7.0 surface, with typed helpers for common calls (current pane, pane read, agent-status subscribe) and a `Call`/`CallRaw` escape hatch for the rest. Socket resolution follows the standard env-var and default-path chain. The Go counterpart to the existing Python socket client, for developers writing plugins, CLIs, or automation in Go.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[CodyBontecou/herdr-telemetry-bridge](https://github.com/CodyBontecou/herdr-telemetry-bridge)**

A plugin that listens to Herdr lifecycle events and emits an NDJSON stream of pane focus intervals, detected agent and model metadata, and local session-trace summaries to a file, an HTTP webhook, or any command's stdin. Raw transcript text is redacted by default, with opt-in controls for trusted local sinks. For developers building menu-bar apps, time-trackers, or dashboards who want structured Herdr activity without writing their own socket client.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[klittle32/letta-herdr-mod](https://github.com/klittle32/letta-herdr-mod)**

A Letta Code modification that reports accurate idle / working / blocked state to Herdr's socket when the agent runs inside a Herdr pane, so a Letta session shows up in the status sidebar like any native agent. For Letta Code users who want the same pane-status visibility Herdr already gives other agent CLIs.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Phoobobo/herdr-traex-integration](https://github.com/Phoobobo/herdr-traex-integration)**

Wires TraeX's lifecycle hooks to Herdr's `pane.report_agent` / `pane.release_agent` socket calls, so a TraeX pane shows correct idle / working / blocked status in the sidebar even though Herdr ships no built-in detector for it. For anyone running the TraeX CLI agent inside Herdr panes.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[aneym/herdr-voice](https://github.com/aneym/herdr-voice)**

Controls Herdr workspaces, pane splitting, and coding agent dispatch through spoken voice commands using OpenAI's Realtime API. A floating HUD displays live audio transcription and command confirmation before routing instructions to target panes. For developers who want hands-free terminal and agent navigation while multitasking.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[benkraus/herdr-plugin-codex-subs](https://github.com/benkraus/herdr-plugin-codex-subs)**

A Bubble Tea popup dashboard that reads host-local CLIProxyAPI OAuth credentials to display live Codex subscription quotas, reset windows, and credit inventories. For developers managing multiple Codex accounts across active agent sessions. ---

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[cdpath/herdr-warp](https://github.com/cdpath/herdr-warp)**

Integrates the Warp Agent CLI with Herdr, letting you drive interactive Warp agents directly inside Herdr panes. It provides actions to send prompts, wait on output, and approve or deny actions, scraping terminal output to report accurate idle, working, and blocked states to the sidebar. For developers using Warp's agent CLI who want to orchestrate it alongside other Herdr workspaces.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[gejiliang/herdr-openclaw](https://github.com/gejiliang/herdr-openclaw)**

Brings OpenClaw TUI sessions into Herdr as first-class agents with live status, model metadata, and token tracking in the sidebar. Uses a background watcher that parses OpenClaw status lines and reports semantic agent states over the socket API via pane.report_agent. For developers running OpenClaw agents inside Herdr workspaces.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kevinWangSheng/herdr-kit](https://github.com/kevinWangSheng/herdr-kit)**

A developer toolkit offering declarative layout definitions, an event watcher daemon, plugin utilities, and a typed socket client for Herdr. It unlocks low-level socket API capabilities and streaming event subscriptions that the standard CLI does not expose. For tool builders and plugin authors crafting custom automations on top of Herdr.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[scott-the-programmer/vscode-devcontainers-herdr](https://github.com/scott-the-programmer/vscode-devcontainers-herdr)**

Relays Herdr's Unix domain socket into VS Code development containers over a loopback TCP bridge. Enables AI agents running inside isolated devcontainers to report status and be orchestrated by the host Herdr instance. - **Code Evidence & Technical Analysis:** Rust plugin (`Cargo.toml`, `herdr-plugin.toml`) implementing host-side daemon and container CLI wrapper (`@devcontainers/cli`) that proxies Herdr's socket over loopback TCP so containerized agents are visible in Herdr panes.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[speardragon/herdr-agents-history](https://github.com/speardragon/herdr-agents-history)**

A keyboard-driven terminal dashboard that streams live tool calls and command outputs from all active Claude Code and Codex agents running in Herdr. It connects directly to Herdr's socket event stream to aggregate real-time agent activities into a single scrollable feed with search and filtering. For developers managing fleets of parallel agents who need centralized visibility into what each agent is executing.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[TheMetalStorm/herdr-freebuff-plugin](https://github.com/TheMetalStorm/herdr-freebuff-plugin)**

A Herdr plugin that integrates Freebuff coding agents as first-class citizens in the multiplexer. It scrapes PTY output and polls local agent session files to report live idle, working, and blocked states to Herdr via socket status APIs. For developers running Freebuff agents who want live lifecycle visibility in their sidebar.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[usrivastava92/herdr-wakeup](https://github.com/usrivastava92/herdr-wakeup)**

A Herdr background plugin that prevents macOS or Linux from going to sleep while managed agents are running tasks. It listens to agent status events over the Herdr Unix socket, activating OS-level sleep inhibitors during active runs and releasing them as soon as all agents become idle. For developers who run long-running agent batch jobs on laptops without having to disable system power saving manually.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[uuie/reasonix-herdr](https://github.com/uuie/reasonix-herdr)**

Connects Reasonix agent lifecycles directly to Herdr to report active, blocked, and idle states in real time. Gives users native workspace and pane control to supervise Reasonix coding workflows side by side with other agents. - **Code Evidence & Technical Analysis:** Implements a Python integration with `herdr-plugin.toml` manifest connecting to Herdr's Unix domain socket API and lifecycle events to synchronize Reasonix agent statuses (`pane.report_agent`) and manage agent workspaces.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[yuuta1219/claude-usage](https://github.com/yuuta1219/claude-usage)**

Tracks Claude Code token consumption and pins session and weekly utilization percentages to the bottom of the Herdr sidebar. It reads local session telemetry without extra API calls, keeping quota awareness visible across all active panes. For Claude Code users who want to monitor their plan limits without leaving the multiplexer.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[schacon/micro-manager](https://github.com/schacon/micro-manager)**

Mac bridge between the Creator Micro 2 and Herdr. Exposes a communication bridge and socket transport for remote inspection and control.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[DanielOu1208/agentslate](https://github.com/DanielOu1208/agentslate)**

iPhone remote keypad for supervising Herdr coding agents over Tailscale. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Tomyail/herdr-connect](https://github.com/Tomyail/herdr-connect)**

Open-source LAN companion app for discovering and connecting to Herdr installations. Exposes a communication bridge and socket transport for remote inspection and control.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[vantt/herdr-go](https://github.com/vantt/herdr-go)**

Web-first remote gateway + supervisor for herdr — control AI coding agents from your phone. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[benkraus/herdr-plugin-mobile-relay](https://github.com/benkraus/herdr-plugin-mobile-relay)**

Provides integration and dedicated functionality for herdr plugin mobile relay in Herdr sessions. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[nyanyaon/github-issue-herdr-plugin](https://github.com/nyanyaon/github-issue-herdr-plugin)**

Claude Code plugin for herding GitHub issues. Exposes a communication bridge and socket transport for remote inspection and control.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[cryks/shepherd](https://github.com/cryks/shepherd)**

herdr agents on local and remote hosts, monitored from your macOS menu bar. Exposes a communication bridge and socket transport for remote inspection and control.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[LoneExile/merino](https://github.com/LoneExile/merino)**

Merino 🐑 — remote tunnel dashboard for Herdr agents. Exposes a communication bridge and socket transport for remote inspection and control.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[akhileshrangani4/herdr-bridge](https://github.com/akhileshrangani4/herdr-bridge)**

HTTP bridge + Charming control panel for herdr agents. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[maedana/herdr-agents-bridge](https://github.com/maedana/herdr-agents-bridge)**

Mobile bridge for Herdr agents (web server + QR code). Exposes a communication bridge and socket transport for remote inspection and control.

![Java](https://img.shields.io/badge/-555555?logo=openjdk&logoColor=white&style=flat-square) **[maxandersen/jherdr](https://github.com/maxandersen/jherdr)**

Java client for the herdr socket API. Exposes a communication bridge and socket transport for remote inspection and control.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[cyperx84/herdr-api](https://github.com/cyperx84/herdr-api)**

Go client for the herdr socket API — transport, event stream, and typed agent model for protocol 19. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[thanh-dong/herdr-rich-preview](https://github.com/thanh-dong/herdr-rich-preview)**

Browser-based rich preview (markdown, mermaid, D2, HTML, SVG) of the files an AI agent touched in your herdr session — SSH/--remote friendly. Exposes a communication bridge and socket transport for remote inspection and control.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[flaricy/herdr-bridge](https://github.com/flaricy/herdr-bridge)**

Report [DeepSeek Harness]( agent activity to the [herdr]( pane hosting the dsh process. herdr's status bar then shows the pane as an agent with live `working` / `blocked` / `idle` states. No herdr changes required. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[PlaneshiftDev/microd](https://github.com/PlaneshiftDev/microd)**

Companion daemon for the Codex Micro macropad: pad events, gestures, and RGB control over a Unix socket (+ herdr bridge). Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[atnine-ai/herdr-bridge](https://github.com/atnine-ai/herdr-bridge)**

Bridge [herdr]( panes to chat services. Exposes a communication bridge and socket transport for remote inspection and control.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[aiken884/herdr-bridge](https://github.com/aiken884/herdr-bridge)**

Coordinate multiple AI coding agents from a single command tower — dispatch, track, and verify with one sentence. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[damozhang/dsh-herdr-bridge](https://github.com/damozhang/dsh-herdr-bridge)**

A dsh plugin that bridges a [DeepSeek Harness]( web session to [Herdr]( letting the dsh agent discover, start, prompt, and observe other agents (pi, claude, codex, ...) running under Herdr — all from inside the dsh web UI. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[sina85/herdr-mobile](https://github.com/sina85/herdr-mobile)**

Password-protected, mobile-first Next.js control panel for a local Herdr terminal session, exposed via Cloudflare Tunnel + Access. Exposes a communication bridge and socket transport for remote inspection and control.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[pepperhorn/herdr-remote](https://github.com/pepperhorn/herdr-remote)**

Small remote dashboard for a running Herdr server. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[deanbaker/herdr-remote](https://github.com/deanbaker/herdr-remote)**

A **web/mobile client for [Herdr]( — the terminal workspace manager for AI coding agents. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[hisetu/pi-herdr-remote](https://github.com/hisetu/pi-herdr-remote)**

Pi-native tools for controlling Herdr servers on allowlisted SSH hosts. Exposes a communication bridge and socket transport for remote inspection and control.

![Kotlin](https://img.shields.io/badge/-555555?logo=kotlin&logoColor=white&style=flat-square) **[bradydibble/herdi](https://github.com/bradydibble/herdi)**

Herdi — private herdr remote client + relay (migrated off public fork). Exposes a communication bridge and socket transport for remote inspection and control.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[kkunkunya/herdr-remote-phone](https://github.com/kkunkunya/herdr-remote-phone)**

Mobile-first fork of herdr-remote: multi-Mac profiles, conversation UI, model/command pickers for phone. Exposes a communication bridge and socket transport for remote inspection and control.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[alex-devdone/herdr-remote-agent-watch](https://github.com/alex-devdone/herdr-remote-agent-watch)**

herdr plugin: show a claude running behind ssh/tmux as a live agent in the sidebar, plus resilient sshl/herdrl wrappers. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Mic92/herdr-eternal](https://github.com/Mic92/herdr-eternal)**

Roaming-friendly transport for herdr --remote: QUIC with WebSocket fallback, byte-exact resume, OIDC auth. Exposes a communication bridge and socket transport for remote inspection and control.

![HTML](https://img.shields.io/badge/-555555?logo=html5&logoColor=white&style=flat-square) **[georgolden/herdr-remote-setup](https://github.com/georgolden/herdr-remote-setup)**

This is my setup for herdr + remote phone access for multi project AI development insipred by Kun Chen. Exposes a communication bridge and socket transport for remote inspection and control.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[backpine/remote-agent-workspace](https://github.com/backpine/remote-agent-workspace)**

Blueprint for an always-on remote agent workspace: code on your Mac, run the work on an always-on Linux box (Herdr + Syncthing + Cloudflare Tunnel + Caddy). Exposes a communication bridge and socket transport for remote inspection and control.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[0xGosu/herdr-auto-pilot](https://github.com/0xGosu/herdr-auto-pilot)**

A Herdr plugin that will automatically prompt the running AI Coding CLI on-behalf of you via Herdr API. The plugin has training mode which learn from your actions and also has guards to prevent dangerous/malicious actions to be performed. Once it has been trained with enough interaction you can let it run on Full-Self Prompting mode (FSP). Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ryonakae/shepherd](https://github.com/ryonakae/shepherd)**

Worker observability daemon and runtime bridges for Herdr-managed coding agents. Exposes a communication bridge and socket transport for remote inspection and control.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[AgentWorkforce/herdr-relay-bridge](https://github.com/AgentWorkforce/herdr-relay-bridge)**

Herdr agents as a fleet able to work as a team. Exposes a communication bridge and socket transport for remote inspection and control.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[pinksaucepasta/paperboat-helper](https://github.com/pinksaucepasta/paperboat-helper)**

Remote runtime for Paperboat environments: PTYs, Herdr agents, previews, images, activity, and config sync. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[shaunbntan-create/vgpt-app](https://github.com/shaunbntan-create/vgpt-app)**

A phone web UI for your Herdr agent herd, served over Tailscale. Fork of AltanS/collie. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[shaunbntan-create/vgpt](https://github.com/shaunbntan-create/vgpt)**

A phone web UI for your Herdr agent herd, served over Tailscale. Fork of AltanS/collie. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[crabfishxy/awaytome](https://github.com/crabfishxy/awaytome)**

"Away to me" — monitor and drive your herdr agents from your phone. PWA + tailnet bridge with full-fidelity terminal mirroring. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[LuYanFCP/herdr-wechat-plugin](https://github.com/LuYanFCP/herdr-wechat-plugin)**

A Herdr plugin for wechat remote control. Exposes a communication bridge and socket transport for remote inspection and control.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[trillium/herdr-tailscale](https://github.com/trillium/herdr-tailscale)**

Herdr plugin: auto-attach trusted Tailscale peers as remote tabs. Exposes a communication bridge and socket transport for remote inspection and control.

[↑ Back to contents](#contents)

### Connect › Push Notifications & Webhook Alerts

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ogulcancelik/herdr-plugin-examples](https://github.com/ogulcancelik/herdr-plugin-examples)**

Official reference plugins from Herdr's creator demonstrating four patterns: Telegram notification, development layout, GitHub link preview, and Rust release tracking — each a standalone `herdr-plugin.toml` package. They are provided as-is for adaptation rather than direct dependency. The canonical starting point for developers building their own Herdr plugins before reaching for the full API docs.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[gaijinjoe/herdres](https://github.com/gaijinjoe/herdres)**

Maps each live Herdr pane to a Telegram forum topic so your AI agent activity streams into a chat thread readable on any device. Accepts bot commands to relay input back into panes and consumes structured turn data from Herdr when available. For developers who want ambient monitoring of their Herdr sessions through Telegram without keeping a terminal window visible.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[zom-2018/herdr-ntfy-notify](https://github.com/zom-2018/herdr-ntfy-notify)**

A plugin that pushes a structured notification to any ntfy topic when an agent blocks or finishes, so alerts reach your phone, tablet, or desktop regardless of which machine is running the agents. Each message carries the workspace, tab, and pane ID so you know exactly where to return, and a local ntfy server is auto-detected for near-instant delivery before falling back over the network. For developers who want cross-device agent alerts through the open ntfy ecosystem.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[tiny-send/tinysend-herdr](https://github.com/tiny-send/tinysend-herdr)**

A plugin that emails you a one-line summary when an agent blocks, finishes, or fails — and lets you reply to that email to drive the agent forward, turning your phone's mail app into a remote control for sessions running over SSH. A reply-watcher polls the tinysend mailbox and feeds your answer into the right pane to resume the blocked agent. For developers who manage agents remotely and want a low-friction approval loop from any device with email.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[yankewei/herdr-focus-notify](https://github.com/yankewei/herdr-focus-notify)**

A plugin that fires a clickable macOS notification when an agent goes blocked or done — but only when you're away from that pane, so you're never alerted about a pane you're already watching. Clicking the toast brings the terminal forward and focuses the exact pane that needs you, via the `alerter` utility. For macOS users who leave agents running unattended and want to be pulled back to precisely the right pane.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[dot/herdr-terminal-notifier](https://github.com/dot/herdr-terminal-notifier)**

A plugin that ships its own branded `HerdrNotify.app` so agent alerts carry the Herdr logo in macOS Notification Center — not a generic terminal icon — with templated messages and a click action that jumps to the blocked or finished pane. The bundled app re-registers with Launch Services on a six-hour TTL, recovering the icon automatically after reboots or OS updates without a cron job. For macOS users who want polished, on-brand desktop notifications from their agent fleet.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[dcolinmorgan/herdr-push](https://github.com/dcolinmorgan/herdr-push)**

A zero-dependency plugin — only curl and system Python or jq — that forwards agent status events to the herdr-remote relay whenever an agent blocks or changes state, enabling mobile monitoring and one-tap approval from the herdr-remote app, menu bar, or Telegram bot. Configuration is a single `HERDR_RELAY` variable, and a built-in test action verifies the pipeline without waiting for a real event. The Herdr-side companion to herdr-remote (listed below).

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[alexei-led/ccgram](https://github.com/alexei-led/ccgram)**

A Telegram bridge that maps each forum topic to one terminal window running an agent — Claude Code, Codex, Gemini, Pi, or a shell — and relays keystrokes and output over the multiplexer, with Herdr as a first-class backend alongside tmux. For developers who want to walk away mid-session and keep monitoring or replying to their Herdr agent panes from a phone.

---

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[blockshiftnetwork/herdr-telegram-attention](https://github.com/blockshiftnetwork/herdr-telegram-attention)**

Subscribes to Herdr agent lifecycle events and sends instant Telegram notifications when an agent gets blocked, finishes a run, or requires approval. Supports quick replies to unblock panes from your phone. For mobile and remote monitoring.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[cokekitten/herdr-telegram-bridge](https://github.com/cokekitten/herdr-telegram-bridge)**

Pushes instant Telegram notifications whenever a Herdr agent finishes or becomes blocked waiting for input. You can reply directly in Telegram with instructions or files to unblock the agent and send input back into its pane without configuring servers or port tunnels. For developers who step away from the keyboard and want to steer running agents from their phone.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[happyeric77/agent-webhook-notify](https://github.com/happyeric77/agent-webhook-notify)**

Listens to Herdr socket events and posts structured HTTP webhooks whenever an agent becomes blocked or finishes a task. Payloads include workspace identity, pane location, agent model, and recent terminal scrollback to provide instant context in Slack, Discord, or mobile push alerts. For developers who need remote notifications when their agent fleet requires intervention.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[HikaruEgashira/say-hook](https://github.com/HikaruEgashira/say-hook)**

Speaks one-line task summaries aloud via ElevenLabs TTS or macOS system speech whenever an agent pane transitions to done or blocked. Its bundled Herdr plugin hooks pane state changes to deliver audio notifications without requiring visual focus on the terminal. For developers multitasking across workspaces who want spoken status updates from background agents.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[horn553/herdr-ntfy](https://github.com/horn553/herdr-ntfy)**

A lightweight shell plugin that dispatches push notifications via ntfy whenever an agent transitions to done or blocked states. It requires only standard shell utilities and curl, reading configuration from a local environment file. For developers who want push alerts on agent progress without installing heavy runtime dependencies.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[keinstn/drover-notify](https://github.com/keinstn/drover-notify)**

Subscribes to Herdr agent status events and delivers a push alert to the Drover iOS app whenever an agent enters a blocked state. The plugin runs on native Node.js with zero npm dependencies and saves encrypted pairing credentials locally. For developers who step away from their desk and want mobile notification when an agent requires human intervention.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[natori-hrj/herdr-hail](https://github.com/natori-hrj/herdr-hail)**

Connects Herdr to Slack and Discord with a two-way webhook bridge that alerts you when an agent becomes blocked. Allows you to reply or tap action buttons directly from your chat app to unblock the agent without setting up tunnels. For developers managing long-running agent runs while away from their desks.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ram4-dev/herdr-notify-center](https://github.com/ram4-dev/herdr-notify-center)**

Captures and persists agent notifications across all workspaces into a durable popup inbox accessible from any Herdr pane. Developers can browse unread alerts, jump directly to the relevant pane, and clear resolved notifications without losing historical context across session restarts. For users running multi-agent workflows who need a centralized notifications tray.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[revanp/herdr-discord-presence](https://github.com/revanp/herdr-discord-presence)**

Broadcasts your active Herdr project, current agent name, and active agent count to Discord Rich Presence via a local RPC daemon. It hooks into the Herdr server lifecycle to poll state silently without requiring bots, API tokens, or external servers. For developers who want to show their live agent workflows in their Discord profile.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[saeedrahimi/herdr-notify-wsl](https://github.com/saeedrahimi/herdr-notify-wsl)**

Bridges Herdr agent lifecycle events from a WSL environment into native Windows 11 toast notifications, alerting you when a background agent finishes or requires approval. It adapts the Windows notification pipeline to invoke PowerShell across the WSL boundary without requiring native Windows daemon setup. For Windows developers running Herdr inside WSL who want desktop notifications without leaving the host OS workflow.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[TheMetalStorm/herdr-commandcode-plugin](https://github.com/TheMetalStorm/herdr-commandcode-plugin)**

Integrates Command Code into Herdr as a first-class agent runtime with automatic process detection and sidebar status reporting. It reports idle, working, and blocked states to the Herdr socket, supports session resumption after server restarts, and pushes toast alerts when the agent needs input. For Command Code users who want their agent sessions fully observable in the Herdr interface.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[luminexord/herdres](https://github.com/luminexord/herdres)**

Telegram interface for monitoring and messaging Herdr coding agents, powered by Tendwire. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[winoooops/herdr-agent-watcher](https://github.com/winoooops/herdr-agent-watcher)**

Coding-agent observability for Herdr: live sidebar cards, lifecycle notifications, and a zero-config Claude Code metrics bridge. Exposes a communication bridge and socket transport for remote inspection and control.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[juninaba/herdr-slack-notify](https://github.com/juninaba/herdr-slack-notify)**

Send Slack notifications when Herdr agents finish or get blocked. Exposes a communication bridge and socket transport for remote inspection and control.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[dcieslak19973/herdr-slackr](https://github.com/dcieslak19973/herdr-slackr)**

Real-time Slack feed pane for herdr — Socket Mode with polling fallback. Exposes a communication bridge and socket transport for remote inspection and control.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[mvallebr/herdr-telegram-plugin](https://github.com/mvallebr/herdr-telegram-plugin)**

Telegram bot companion for herdr — remote control any agent via Telegram forum topics, zero LLM in the path. Exposes a communication bridge and socket transport for remote inspection and control.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[sbulav/herdr-relay](https://github.com/sbulav/herdr-relay)**

Monitor and approve herdr agents from your phone, menu bar, or Telegram — no SSH required. Exposes a communication bridge and socket transport for remote inspection and control.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[rkbkosp/agent-beacon](https://github.com/rkbkosp/agent-beacon)**

A local ESP32-S3 desktop status beacon for Codex quotas, Herdr agents, QWeather forecasts, and full-screen alerts, powered by a macOS bridge. Exposes a communication bridge and socket transport for remote inspection and control.

[↑ Back to contents](#contents)

### Connect › Telemetry, Events & Quota Streaming

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[alejodelosrios/herdr-claude-usage](https://github.com/alejodelosrios/herdr-claude-usage)**

Displays real-time Claude plan quota usage — both session and weekly percentage — directly in the Herdr sidebar across all active workspaces. It reads authentication and status telemetry natively from Claude Code to mirror `/status` metrics without requiring extra browser logins or rate-limit estimations. For developers running multiple concurrent Claude Code sessions who need ambient quota tracking.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[amurru/herdr-whistle](https://github.com/amurru/herdr-whistle)**

A Go-powered Herdr plugin that enables remote control and status monitoring of agents running across remote daemon instances. It streams lifecycle updates and dispatches agent commands without requiring direct terminal session takeover. For developers managing headless or multi-machine Herdr agent deployments from a single workstation.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[DIodide/herdr-telemetry](https://github.com/DIodide/herdr-telemetry)**

A lightweight Go plugin that streams Herdr workspace and agent lifecycle telemetry to any user-controlled endpoint. Built with privacy-first defaults, it strips tokens, redacts sensitive prompts, and runs as a single zero-dependency binary. For platform teams and developers who need custom observability for terminal agent fleets without third-party services.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[iamhouser/herdr-claude-usage-multi](https://github.com/iamhouser/herdr-claude-usage-multi)**

Embeds Claude Code session and weekly rate-limit gauges directly into Herdr sidebar workspace rows, complete with color thresholds and unblock countdowns. It detects multi-account configurations by matching pane directories to their respective profile folders with zero token overhead. For developers juggling multiple Claude plans across parallel workspaces.

![C#](https://img.shields.io/badge/-555555?logo=csharp&logoColor=white&style=flat-square) **[Javamomma/herdr-scribe](https://github.com/Javamomma/herdr-scribe)**

Streams live microphone audio into ephemeral in-memory transcripts and analysis panes inside Herdr without persisting raw audio recordings. When a session ends, it automatically generates structured meeting minutes, policy gates, and draft task tickets for agent review. For developers and teams who want live meeting context turned into actionable agent tasks in real time.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[kosuketut/herdr-remotedownloder](https://github.com/kosuketut/herdr-remotedownloder)**

Transfers files generated or edited inside a remote Herdr pane directly back to your local macOS machine. Integrates as a plugin action that detects file paths in the active pane and triggers a download stream over the connection. For developers running agents on remote servers who frequently pull build artifacts, logs, or generated code locally.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[second-state/vibetty](https://github.com/second-state/vibetty)**

Streams live terminal screens from Herdr agent panes over MQTT to smart devices and wearable hardware like VibeKeys and VibeWatch with bidirectional keystroke relay. It includes an embedded MQTT broker and hooks directly into the Herdr command palette and status bar. For developers who want to monitor and interact with coding agents from dedicated external hardware.

[↑ Back to contents](#contents)

### Connect › Voice, Hardware & Remote Bridges

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[razajamil/herdr-hex-browser-voice-command](https://github.com/razajamil/herdr-hex-browser-voice-command)**

A Chrome extension plus local daemon that watches which browser URL was focused while you spoke to the Hex voice transcriber, then routes the resulting transcript to the matching Herdr workspace and pane — no manual focus switch. Routing rules map URL patterns to workspace/tab/pane triples and are configured in the extension popup. For developers who dictate to several Claude Code panes and want each spoken instruction to land in the right agent automatically.

[↑ Back to contents](#contents)

### Connect › Protocol & Third-Party Bridges

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[junliu-mde/mimo-code-herdr-plugin](https://github.com/junliu-mde/mimo-code-herdr-plugin)**

A user-level MiMo Code plugin that reports idle / working / blocked / done state to Herdr's sidebar via `pane.report_agent`, using an aggregate state machine across all MiMo subagent sessions to avoid flicker during multi-session runs. A detached watchdog releases the pane label on any exit — including `kill -9` and hard crashes — and a subprocess guard suppresses the plugin when MiMo runs as a tool call inside another pane. For MiMo Code users who want their agent's status visible in Herdr without waiting for native support.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[vaclavik-xyz/herdwatch](https://github.com/vaclavik-xyz/herdwatch)**

Keeps a Herdr pane flagged as working — with a ⏳ label — while background CI, review, or manual-marker work is still pending after the agent itself has gone idle, so a finished-looking pane isn't mistaken for done. Runs standalone or as a background service. For anyone whose agent wraps up a turn before the checks it triggered actually complete.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[carsonjones/herdr-agent-dashboard](https://github.com/carsonjones/herdr-agent-dashboard)**

A diff-rendered terminal dashboard (Bun + React/opentui) that lists every running Herdr agent with live status, reachable as a keybound plugin action or run standalone. For anyone managing many concurrent agent panes who wants one glanceable table instead of tabbing through workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[abtris/herdr-plugin-jira-pr](https://github.com/abtris/herdr-plugin-jira-pr)**

Cross-checks the current branch's GitHub pull request against linked Jira tickets, displaying issue status and warning if ticket keys are missing or mismatched. It surfaces Jira context directly within Herdr without opening a browser or leaving the terminal. For developers and teams using Jira who need ticket hygiene enforced across agent-generated branches and PRs.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[candypoets/buzzr](https://github.com/candypoets/buzzr)**

Mirrors live Herdr workspaces and agent panes into Buzz channels using Nostr identities and mention routing. Publishes agent availability declarations and routes channel mentions back into the right terminal pane without exposing your private key. For distributed teams collaborating with autonomous agents over decentralized chat.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[go-min/herdr-fwd](https://github.com/go-min/herdr-fwd)**

Automatically sets up loopback port forwarding between remote Herdr sessions and your local machine. Keeps port bindings synced so services and preview servers started by remote agents are immediately reachable locally without manual SSH tunneling. For developers using Herdr over remote SSH who want automatic port access.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[jatingargiitk/herdr-memory](https://github.com/jatingargiitk/herdr-memory)**

Builds a persistent memory graph across your Herdr coding sessions by observing agent actions, successes, and past decisions. It feeds accumulated project context back into future agent prompts so subsequent runs avoid repeating mistakes. Ideal for developers and teams running multi-agent workflows across complex codebases.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[JYasha11/herdr-in-your-face](https://github.com/JYasha11/herdr-in-your-face)**

Subscribes to Herdr agent status events and pops up an escalating ASCII art face whenever an agent enters a blocked state waiting for user input. Increases visual urgency the longer an approval is ignored to keep background agent workflows moving. For developers running unattended agent sessions who want unmissable in-terminal unblocking reminders.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[kukv/herdr-plugin-github-dash](https://github.com/kukv/herdr-plugin-github-dash)**

A Herdr plugin that brings GitHub pull request and issue management directly into your terminal workspace. Allows developers to review, track, and assign GitHub issues to agent tabs without leaving the multiplexer. For engineers integrating GitHub task backlogs with Herdr workflows.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[neon-solutions/neon-herdr](https://github.com/neon-solutions/neon-herdr)**

An official plugin that embeds an interactive Neon serverless Postgres dashboard into a Herdr pane. It allows developers to branch databases per agent worktree, toggle compute states, and inject connection strings without leaving the terminal. For developers building database-backed applications with parallel coding agents in Herdr.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[openclaw/crabbox](https://github.com/openclaw/crabbox)**

Brings Crabbox sandbox provisioning and remote test execution directly into Herdr sessions. A dedicated plugin exposes actions to prewarm ephemeral environments, sync diffs, and inspect active leases from a pane overlay. For developers who want isolated build and test verification without leaving their workspace.

[↑ Back to contents](#contents)

---

## Editor integrations

Navigating between your editor and Herdr panes without leaving the keyboard.

### Editor › Neovim Navigation & Splits

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[devxplay/herdr.nvim](https://github.com/devxplay/herdr.nvim)**

Unifies pane navigation between Neovim and Herdr: the same `Ctrl+h/j/k/l` that moves between Vim splits flows straight into the adjacent Herdr pane when you hit an edge, and back again. A small Rust helper talks to the socket for focus, splits, and layout, and it coexists with vim-tmux-navigator — Neovim detects whether it's inside Herdr or tmux and routes accordingly. For Neovim users who want one set of muscle memory across editor and multiplexer.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[paulbkim-dev/vim-herdr-navigation](https://github.com/paulbkim-dev/vim-herdr-navigation)**

A port of vim-tmux-navigator to Herdr: `Ctrl+h/j/k/l` flows between Vim/Neovim splits and adjacent Herdr panes, crossing the boundary at an edge in either direction. It runs as a real Herdr plugin action, checking the pane's foreground process via `herdr pane process-info` to decide whether to forward the key or move pane focus. For developers with vim-tmux-navigator muscle memory who want it working identically in Herdr.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[lmilojevicc/herdr-splits.nvim](https://github.com/lmilojevicc/herdr-splits.nvim)**

A port of smart-splits.nvim to Herdr that adds resizing to the navigation story: the same `Alt+h/j/k/l` that resizes Neovim splits delegates to Herdr when a window fills the terminal edge, and movement likewise crosses the boundary. Ships configurable at-edge behaviors (wrap, stop, split, custom callback), count-prefix support, and auto-unzoom on navigate. For Neovim users who want both navigation and resize parity between editor and multiplexer.

![Vim Script](https://img.shields.io/badge/-555555?logo=vim&logoColor=white&style=flat-square) **[luiarthur/herdr.vim](https://github.com/luiarthur/herdr.vim)**

A Vim and Neovim plugin that spawns a language-appropriate REPL in a Herdr pane and sends the current line, the whole file, or a visual selection to it with one key. Supports Vim 7.4 through 9 and Neovim 0.5+, with remappable defaults. For data scientists and scripters who want a send-to-REPL workflow inside Herdr without leaving the editor.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[UN-9BOT/sidekick_herdr](https://github.com/UN-9BOT/sidekick_herdr)**

Adds Herdr as a first-class session backend to sidekick.nvim, the Neovim plugin for AI CLI tools that already supports tmux and zellij — drop it in alongside sidekick.nvim and set `herdr` as the session provider, no fork or upstream patch required. For sidekick.nvim users who run Herdr as their multiplexer and want the same agent-launcher UX they'd get with tmux.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[aimdevlee/herdr-nvim-nav](https://github.com/aimdevlee/herdr-nvim-nav)**

Enables seamless Ctrl+h/j/k/l navigation across Neovim splits and Herdr panes using socket state tracking. Lets you cross editor and multiplexer boundaries with unified keybindings. For vim and Neovim users who live in split layouts.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[bojackduy/nvim-herdr-navigation](https://github.com/bojackduy/nvim-herdr-navigation)**

A Neovim plugin that brings vim-tmux-navigator style directional navigation to Herdr. It maps Ctrl+h/j/k/l to move seamlessly between internal Neovim splits and outer Herdr agent panes without changing keybinds at the editor boundary. For Neovim users who want friction-free movement between code editing and agent terminal panes.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[chmarax/herdr-nvim](https://github.com/chmarax/herdr-nvim)**

Bridges Neovim directly into Herdr workspaces with a native Rust core and Lua configuration. Lets you inspect panes, spawn agent sessions, and send selections directly to active panes. For Neovim users who want deep multiplexer integration.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[cinco/herdr-grep-nvim](https://github.com/cinco/herdr-grep-nvim)**

Combines `ripgrep` and `fzf` into a live-grep workflow that opens matching search locations directly in a Neovim split pane adjacent to your running agent. It lets you jump straight into code locations surfaced by searches or agent discussions without leaving the multiplexer context. For developers who want instant editor jumps alongside active agent panes.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[makyinmars/herdr-context.nvim](https://github.com/makyinmars/herdr-context.nvim)**

A Neovim plugin with a two-pane composer that formats buffer selections, cursor positions, and file context into structured Markdown payloads for active Herdr agents. It stages the gathered context into an agent's prompt without auto-submitting, allowing you to review or refine instructions beforehand. For Neovim users who want precise, structured code handoffs into Herdr agent sessions.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[sebcbi1/herdr-edge-nav](https://github.com/sebcbi1/herdr-edge-nav)**

Enables seamless directional navigation and resizing across Neovim splits, Herdr panes, tabs, and workspaces using unified keybindings. Automatically detects when cursor movement reaches an editor or pane boundary and forwards focus to the adjacent surface without mode switching. For developers who want frictionless navigation between their Neovim editor and Herdr agent splits.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[shadowfax92/herdr-comments](https://github.com/shadowfax92/herdr-comments)**

Brings annotated code review for Herdr terminal output into Neovim. Lets you capture output from active agent panes, attach line-level comments and review notes, and organize feedback directly within editor buffers. For Neovim users who want a structured review flow for agent sessions without switching windows.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[willfish/herdr-navigator](https://github.com/willfish/herdr-navigator)**

Provides the Herdr-side plugin actions for seamless navigation between Vim or Neovim splits and outer Herdr panes. Checks active pane processes to either forward directional keys to the inner editor or shift focus across Herdr splits. For Vim and Neovim users who want unified keyboard movement without jarring multiplexer boundaries.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[nettlesh/dotfiles](https://github.com/nettlesh/dotfiles)**

Alacritty + Fish + Herdr + Neovim. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[uncaughterrs/dotfile](https://github.com/uncaughterrs/dotfile)**

Config file for ghostty , neovim , herdr , tmux etc. developer tools. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[luisgui1757/dotfiles](https://github.com/luisgui1757/dotfiles)**

Cross-platform Rose Pine terminal/editor setup for Apple Silicon macOS, Linux, WSL2, and Windows: Neovim, Herdr, tmux/psmux, Starship, Ghostty, WezTerm, Windows Terminal, AeroSpace, zsh/PowerShell, lazygit, and CLI tooling. Nix on POSIX; chezmoi configs everywhere. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[ctbaum/herdr-agents.nvim](https://github.com/ctbaum/herdr-agents.nvim)**

Neovim bridge for running editor-integrated coding agents in Herdr panes. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[RooseveltAdvisors/vim-herdr-navigation](https://github.com/RooseveltAdvisors/vim-herdr-navigation)**

Seamless Ctrl/Alt hjkl navigation across herdr panes and Vim/Neovim splits (fork of paulbkim-dev/vim-herdr-navigation). Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[willfish/herdr-navigator.nvim](https://github.com/willfish/herdr-navigator.nvim)**

Seamless navigation between Neovim windows and Herdr panes. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[joo-was-already-taken/herdr-navigator.nvim](https://github.com/joo-was-already-taken/herdr-navigator.nvim)**

Navigate between Neovim splits and Herdr panes. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[kaar/nvim-herdr-navigator](https://github.com/kaar/nvim-herdr-navigator)**

Seamless navigation between Neovim splits and herdr panes: one set of `ctrl+h/j/k/l` chords moves through vim and herdr panes. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[inferst/herdr-review.nvim](https://github.com/inferst/herdr-review.nvim)**

Code review UI for Neovim with Git and herdr integration. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[utahta/herdr-prompt.nvim](https://github.com/utahta/herdr-prompt.nvim)**

Ask a herdr agent about the code in front of you, from Neovim. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[ocyedwin/editor](https://github.com/ocyedwin/editor)**

Portable Ghostty, Herdr, Vim, Neovim, and VSCodeVim workflow. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[TianZuo555/herdr.nvim](https://github.com/TianZuo555/herdr.nvim)**

Send Neovim references to coding agents in the same Herdr tab. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[rahadur/herdr.nvim](https://github.com/rahadur/herdr.nvim)**

herdr.nvim — Ink & Paper colorschemes ported from herdr.dev. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[kbroomstd/herdr.nvim](https://github.com/kbroomstd/herdr.nvim)**

Nvim bindings for herdr the agent multiplexer that lives in your terminal. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[nwiizo/signalbox.nvim](https://github.com/nwiizo/signalbox.nvim)**

Attention-first Neovim control surface for persistent Herdr coding agents. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[s-0-a-r/copse](https://github.com/s-0-a-r/copse)**

CLI-native ADE (Agent Development Environment) — Herdr + Neovim + parallel agent fan-out. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[jakkzz/herdr-setup](https://github.com/jakkzz/herdr-setup)**

Reproducible Herdr + Neovim setup — pinned plugins, cross-platform installer (macOS/Linux/WSL). Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[vanducng/dotfiles](https://github.com/vanducng/dotfiles)**

AI-native macOS dev environment: Herdr, Neovim, Yabai, and AI tools. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[mirkobozzetto/dotfiles](https://github.com/mirkobozzetto/dotfiles)**

macOS terminal setup: Ghostty over tmux or herdr, Neovim, and agent redirection that brings you to whichever coding agent needs you. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

[↑ Back to contents](#contents)

### Editor › Full Neovim-Hosted Workspaces

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[MomePP/herd.nvim](https://github.com/MomePP/herd.nvim)**

Makes Neovim the top-level UI for Herdr coding agents: spawn an agent into a fullscreen floating terminal, toggle it with one key, and push the current visual selection straight to the active agent without submitting. Herdr stays the backend process owner, so its status hooks and grouped dashboard keep working. For Neovim-first developers who want editor-native agent UX without giving up Herdr's orchestration layer.

[↑ Back to contents](#contents)

### Editor › VS Code, Cursor & Devcontainers

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[timofey-TK/herdr-open-in-editor](https://github.com/timofey-TK/herdr-open-in-editor)**

Binds a single shortcut to open the active local or remote Herdr workspace directory directly in VS Code or Zed. It automatically handles SSH remote workspace URIs so opening remote agent worktrees in your local GUI editor requires no manual connection setup. For developers who want to jump from a terminal agent session into their primary graphical editor instantly.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[T0mSIlver/localvoxtral](https://github.com/T0mSIlver/localvoxtral)**

Talk to your coding agents by voice. Realtime, fully local macOS dictation that streams words as you speak and grounds LLM polishing in the exact Claude Code session under your cursor — Ghostty, iTerm2, Terminal.app, even a herdr pane. 100% on-device on Apple Silicon. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[endoumame/herdr-vscode](https://github.com/endoumame/herdr-vscode)**

Review code where you read it. Write inline comments in VS Code — on pull. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[andorexu/hermes-agent-skills-pack](https://github.com/andorexu/hermes-agent-skills-pack)**

28 production-grade Hermes Agent skills — decision frameworks, thinking methodologies, engineering tools, and OCR/Web pipelines. Multi-platform (Hermes/Claude Code/Herdr/Cursor). Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[alex-devdone/herdr-cursor-open](https://github.com/alex-devdone/herdr-cursor-open)**

Open the focused herdr pane in Cursor or VS Code — including panes attached to a remote herdr, over Remote-SSH. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[lurepos/herdr-vscode-tasks](https://github.com/lurepos/herdr-vscode-tasks)**

useful herdr picker when dealing with .vscode folder at projects. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[magimetal/matrix-themes](https://github.com/magimetal/matrix-themes)**

Matrix-inspired themes for various software; pi-coding-agent, ghostty, herdr, vscode, zed. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[gogamid/pi-herdr-cursor-focus](https://github.com/gogamid/pi-herdr-cursor-focus)**

A [Pi]( extension that hides the editor cursor in unfocused [herdr]( panes. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[beraterkanelcelik/agent-army](https://github.com/beraterkanelcelik/agent-army)**

A three-tier agent hierarchy for running parallel AI coding missions under one human operator — Claude Code + Herdr + cursor-agent, files as the command bus. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

[↑ Back to contents](#contents)

### Editor › Vim, Kakoune & Other Editors

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ImArtisann/zed-herdr](https://github.com/ImArtisann/zed-herdr)**

Subscribes to Herdr workspace lifecycle events over the Unix socket to automatically sync active workspaces with your Zed editor sessions. It maintains real-time project state with resilient reconnection handling and snapshot sync. For Zed users running agent workloads across multiple Herdr workspaces.

![Emacs Lisp](https://img.shields.io/badge/-555555?logo=gnuemacs&logoColor=white&style=flat-square) **[ionrock/ghostherd](https://github.com/ionrock/ghostherd)**

Manage herdr agent terminals from Emacs via ghostel. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Aerosnail/nvim-herdr-navigator](https://github.com/Aerosnail/nvim-herdr-navigator)**

Custom plugin pair to navigate seamlessly between nvim splits and herdr panes. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[AVGVSTVS96/vim-herdr-navigator](https://github.com/AVGVSTVS96/vim-herdr-navigator)**

Seamless navigation between herdr panes and vim/nvim splits. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ChmaraX/herdr-gitview](https://github.com/ChmaraX/herdr-gitview)**

Git status/diff panel for herdr - review changes, edit in nvim, stage/commit/discard, all from the terminal. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Emacs Lisp](https://img.shields.io/badge/-555555?logo=gnuemacs&logoColor=white&style=flat-square) **[eddof13/herdr.el](https://github.com/eddof13/herdr.el)**

Control the herdr terminal workspace manager from Emacs, with herdr's terminals hosted inside Emacs via ghostel. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[acmmarques/dotfiles](https://github.com/acmmarques/dotfiles)**

ghostty • zsh • herdr • nvim • karabiner • git. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![GLSL](https://img.shields.io/badge/-555555?logo=opengl&logoColor=white&style=flat-square) **[Jalmar01/my-dots](https://github.com/Jalmar01/my-dots)**

Personal Nix home-manager flake: fish, ghostty, zellij, herdr, nvim, wezterm. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[SamuelCastrillon/tzemed](https://github.com/SamuelCastrillon/tzemed)**

Tzemed — Windows native dev stack distro. Herdr + Nvim + Peri + Gentle-ai SDD. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[GMakeziG/ninjatronics-ai](https://github.com/GMakeziG/ninjatronics-ai)**

AI operating system for orchestrating specialized engineering agents using Hermes, Herdr, Claude Code, and Codex. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[AVGVSTVS96/starter-dotfiles](https://github.com/AVGVSTVS96/starter-dotfiles)**

Minimal agent-first, auto-managed macOS dotfiles for React/TS dev. Ghostty, Herdr, Claude Code, Codex, LazyVim, Vite+, and Nub; plus minimal shell config and dev tools. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Schaitanya535/herdr-config](https://github.com/Schaitanya535/herdr-config)**

My herdr (agent multiplexer) config — keybindings, theme, scrollback→nvim helper. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[lhr0909/herdr-bel](https://github.com/lhr0909/herdr-bel)**

Forward Herdr agent notifications to Zed Terminal Threads as BEL. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

[↑ Back to contents](#contents)

### Editor › REPL & Code Dispatchers

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[AbhijithAnirudhan2907/herdr-sidebar](https://github.com/AbhijithAnirudhan2907/herdr-sidebar)**

herdr-sidebar fork with an in-pane editor (edit/save, live syntax highlight, undo/redo, find/replace). Fork of alexarthurs/herdr-sidebar (MIT). Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[sjdonado/dotfiles](https://github.com/sjdonado/dotfiles)**

macos/linux: terminal, editors, shell, AI harness. Integrates Herdr workspace navigation and agent dispatch directly with editor buffers.

[↑ Back to contents](#contents)

### Editor › Editor Plugins & Bridges

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Daniel-Steinberger/obsidian-herdr](https://github.com/Daniel-Steinberger/obsidian-herdr)**

An Obsidian desktop plugin that sends the next unchecked to-do from a markdown checklist to an agent running in the matching Herdr workspace and ticks the box when the agent finishes; a continuous mode works through a whole list unattended. For people who plan work in Obsidian notes and want Herdr to execute it directly.

---

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[aclima01/herdr-edit-windows](https://github.com/aclima01/herdr-edit-windows)**

A minimal text editor that opens inside a Herdr split pane on Windows, providing a directory tree, syntax highlighting, and an inline uncommitted diff tab. It lets you inspect, tweak, and git-stage files without switching out of the multiplexer. For Windows users who want a lightweight scratchpad editor directly beside active agents.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[vonzelle-vzt/herdr-extensions](https://github.com/vonzelle-vzt/herdr-extensions)**

Turns Herdr into a modular terminal IDE by layering a 12-panel workspace complete with LSP diagnostics, autocomplete, source control, testing, and agent diff reviewing. It installs with a single idempotent command to provide full IDE editing features directly within multiplexer panes. For developers seeking an all-in-one terminal coding environment alongside autonomous agents.

[↑ Back to contents](#contents)

---

## Sessions: switch & restore

Managing the lifecycle of persistent agent sessions — switching, picking, restoring.

### Sessions › Fuzzy Session Switchers & TUI Pickers

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[ridho9/switchr](https://github.com/ridho9/switchr)**

A full-screen session picker for Herdr: it lists every session next to its workspace / tab / pane tree, and you attach to the one you want with a keypress. Wire it up as your terminal's startup command and it greets you on each new window; it also spots an incompatible daemon and offers an in-place restart. For anyone juggling several named sessions who wants a fast visual switchboard.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[j0urneyk/herdrctx](https://github.com/j0urneyk/herdrctx)**

A keyboard-driven TUI for the housekeeping side of sessions — attach, stop, delete, create, and search, without copying names out of `herdr session list`. It ships through a Homebrew tap with prebuilt macOS and Linux binaries and refuses to launch nested when you're already inside a Herdr pane. For developers managing sessions across many projects who want a faster daily driver than the raw CLI.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[thanhdat77/herdr-picker-plus](https://github.com/thanhdat77/herdr-picker-plus)**

A single ratatui overlay — no fzf dependency — that surfaces open workspaces, Herdr Plus project templates, filesystem roots, zoxide frecency, SSH hosts, agent panes, and configured plugin integrations in one place. Selecting an SSH host creates or re-focuses a `server: NAME` workspace and runs the connection in its tab; selecting a directory checks for an existing workspace at that path before making a new one. For power users who want one keystroke to reach anything in their Herdr session.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer)**

A tmux-sessionizer-style workflow for Herdr: `fzf` over your project roots to open a workspace, or over your git worktrees to reopen one, with a TOML config defining the tabs, pane splits, and per-pane startup commands that appear. Ships a README-preview panel, per-repo layout overrides, and a `bat`-powered file preview. For developers who want one keypress to land in a fully arranged workspace rather than building it each time.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[alon-z/herdr-command-palette](https://github.com/alon-z/herdr-command-palette)**

A minimal palette — no Rust build step — that merges open workspaces, configured project roots, and optionally zoxide frecency into one fuzzy list; selecting a directory focuses an existing workspace for that path or creates one. Deliberately lighter than herdr-picker-plus: no SSH, no agent panes, no plugin contract, just workspace and directory navigation. For users who want a small standalone switcher without the full picker surface.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[maayanyosef/herdr-aws-ssm](https://github.com/maayanyosef/herdr-aws-ssm)**

Fuzzy-pick a running EC2 instance across your AWS profiles and drop into a full `herdr --remote` session tunneled over AWS SSM, using ephemeral EC2 Instance Connect keys and auto-detected SSH users — no bastion, public IP, or long-lived keys. For teams who want Herdr's remote thin-client session on private-subnet EC2 boxes.

---

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[adamwangxx/herdr-codex-resume](https://github.com/adamwangxx/herdr-codex-resume)**

Opens the native Codex resume picker in a new Herdr split pane with live workspace context. Lets you browse and resume previous Codex sessions without losing your active terminal view. For developers running multi-session Codex workflows in Herdr.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[asumaran/herdr-goto](https://github.com/asumaran/herdr-goto)**

A Bubble Tea popup switcher that organizes Herdr workspaces into a two-level repository and worktree hierarchy with fuzzy filtering. Panes can be expanded on demand with a toggle, and prebuilt binaries are fetched automatically on install. For users navigating large fleets of worktree-based agent workspaces.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[AVGVSTVS96/herdr-drovr](https://github.com/AVGVSTVS96/herdr-drovr)**

An interactive utility that uses `fzf` to move tabs and panes between different Herdr workspaces on the fly. It talks to the Herdr socket API to query open workspaces and reparent active tabs without terminating running agent processes. For developers managing dense multi-workspace layouts who need rapid cross-workspace organization.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[beyondlex/herdr-recent-navigator](https://github.com/beyondlex/herdr-recent-navigator)**

A Rust-powered popup switcher that tracks recently focused workspaces, tabs, panes, and AI agents across Herdr sessions. It maintains a live MRU index via socket event subscriptions and supports instant keyboard navigation and fuzzy search. For power users switching rapidly between multiple active agent panes and workspaces.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[damianpoole/herdr-opencode-sessions](https://github.com/damianpoole/herdr-opencode-sessions)**

A Herdr plugin for fuzzy-searching previous OpenCode sessions across projects, titles, dates, and transcript contents. Includes interactive conversation previews and one-key shortcuts to resume or fork a session in a new pane. For OpenCode users managing extensive conversation histories across multiple workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[dleen/herdr-agents](https://github.com/dleen/herdr-agents)**

An fzf-driven agent picker that aggregates every active agent pane and sorts them worst-first so blocked agents get immediate triage. Shows real-time session previews and lets you jump to any pane or launch new agents with a single keypress. For developers running parallel agent fleets who need fast attention queue management.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[haphamdev/herdr-simple-switcher](https://github.com/haphamdev/herdr-simple-switcher)**

Provides a lightweight, keyboard-driven fuzzy picker over your active Herdr workspaces, tabs, and running AI agents via fzf. Selecting an entry immediately focuses the matching workspace, tab, or agent pane without complex key combos. For users managing multi-agent sessions who want an instant switchboard without a heavy compiled TUI.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[ImArtisann/herdr-workspace-launcher](https://github.com/ImArtisann/herdr-workspace-launcher)**

A macOS-optimized Herdr plugin that provides a searchable, keyboard-driven directory picker for instant workspace creation. It scans designated project directories and uses Herdr CLI commands to spawn and focus dedicated workspaces in one keystroke. For developers on macOS who juggle multiple repositories and want zero-friction workspace switching.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[iskwyuki/herdr-control-panel](https://github.com/iskwyuki/herdr-control-panel)**

A lightweight popup control panel that lets you switch workspaces from history, open paths, or trigger custom actions via `fzf`. It requires no build step and integrates directly into Herdr keybindings for rapid workspace management. For developers who want single-keystroke access to all session and workspace operations.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[ismaelosuna7824/herdr-recent-workspaces](https://github.com/ismaelosuna7824/herdr-recent-workspaces)**

Maintains a searchable history of previously opened workspace directories to quickly refocus active workspaces or restore older sessions. It also includes filesystem navigation to browse and initialize new workspaces directly from the picker. For Herdr users frequently jumping between multiple project directories throughout the day.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[jeffarese/herdr-bar](https://github.com/jeffarese/herdr-bar)**

Provides a quick-switch command palette to fuzzy-find and jump to any Herdr tab, agent, repository, or branch. Built with zero external dependencies using only the Python standard library. For developers managing extensive multi-agent workspaces who need fast keyboard navigation.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[joshuadavidthomas/hrd](https://github.com/joshuadavidthomas/hrd)**

A Bubble Tea terminal interface that aggregates local and remote Herdr sessions alongside isolated sandboxes into a single picker. It lets you discover, inspect, and attach to agent sessions distributed across development environments. For developers running multiple sandboxed Herdr instances across machines or containers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[kenchan/herdr-ghq-open-agent](https://github.com/kenchan/herdr-ghq-open-agent)**

Interactive ghq repository picker powered by fzf that opens projects directly into Herdr workspaces or tabs. Automatically launches Claude Code in the selected directory upon initialization. For developers managing multiple repositories with ghq who want a fast one-key path to start agent coding sessions.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[lmilojevicc/seshagy](https://github.com/lmilojevicc/seshagy)**

A Bubble Tea session picker that discovers local repositories and manages both tmux and Herdr workspaces. It monitors running AI agent states across sessions so you can inspect active work before attaching. Ideal for developers navigating multiple parallel agent workflows across tmux and Herdr.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[marcoskichel/herdr-muster](https://github.com/marcoskichel/herdr-muster)**

Provides a fast fuzzy picker that displays active Herdr workspaces annotated with real-time agent execution states like working or blocked. Lets you jump straight to the workspace needing operator attention without checking tabs individually. For developers running parallel agent workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mikedclarke/herdr-workspaces](https://github.com/mikedclarke/herdr-workspaces)**

Registers your frequent project directories and exposes a fuzzy picker to jump into them as named Herdr workspaces. If a workspace is already running for the selected path, it switches focus rather than duplicating it. For developers who manage multiple active codebases and want fast keyboard navigation between workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mr04vv/herdr-pane-navigator](https://github.com/mr04vv/herdr-pane-navigator)**

A fuzzy tree navigator that lets you jump across workspaces, tabs, and panes based on active agent tasks. It sorts panes by urgency—putting blocked and completed agents at the top—and includes a live preview modal with working directory, agent status, and recent scrollback. For developers managing multiple concurrent workspaces who need fast situational awareness.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[nicosuave/memex](https://github.com/nicosuave/memex)**

Indexes and searches historical conversation transcripts across Claude Code, Codex, Pi, OpenCode, and Cursor using hybrid search. A native Herdr plugin embeds a session desk TUI into a pane so you can find past interactions and resume them in fresh tabs. For developers managing long-running agent histories across multiple tools.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[pedroloch/herdr-undo-close](https://github.com/pedroloch/herdr-undo-close)**

Restores accidentally closed tabs and panes with their exact split hierarchy, working directories, labels, and launched agents via a shortcut or an interactive history picker. For anyone who needs a safety net against accidental pane closures in Herdr. ---

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[shadowfax92/herdr-ferry](https://github.com/shadowfax92/herdr-ferry)**

A native Rust popup plugin that moves live running panes and entire tabs between Herdr workspaces without restarting processes. Operates with zero runtime dependencies like fzf or Node.js, binding directly to prefix shortcuts. Built for developers reorganizing sprawling multi-agent sessions across long-running projects.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[thanhdat77/herdr-navigator](https://github.com/thanhdat77/herdr-navigator)**

A unified fuzzy navigator overlay for quick switching between Herdr workspaces, running agents, remote hosts, and plugin actions. It consolidates session picking and action launching into a single keyboard-driven palette. For power users navigating complex, multi-workspace Herdr setups.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[TheThoughtagen/attic](https://github.com/TheThoughtagen/attic)**

Monitors idle AI coding agent sessions, snapshots their state to disk, and gracefully closes them to reclaim terminal resources while keeping them restorable on demand. It provides a Textual TUI dashboard and a Herdr plugin to pin, snooze, and review archived workspaces without leaving the multiplexer. For developers managing high-volume agent workflows who want automated session cleanup without losing work.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ugurtarlig/herdr-agent-recency](https://github.com/ugurtarlig/herdr-agent-recency)**

Provides a theme-aware fuzzy picker that ranks active agents and workspaces by the recency of their real Claude and Codex turns rather than static creation time. It surfaces whichever agent finished work or stalled most recently to the top of the selector. For developers managing high-concurrency agent swarms who need to quickly re-engage with the most recently active sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[wraithyy/herdr-waypoint](https://github.com/wraithyy/herdr-waypoint)**

Lets you bookmark favorite project directories as named waypoints and fuzzy-select them through fzf to open fresh Herdr workspaces. Saved paths persist in a lightweight text file for fast recall without repetitive directory navigation. For developers juggling diverse project folders across different paths on disk.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[yoshiori/herdr-configurable-picker](https://github.com/yoshiori/herdr-configurable-picker)**

A tree-based goto picker for Herdr with fully remappable keybindings, designed to replace hardcoded navigation keys that conflict with Japanese IMEs. Allows complete customization of navigation chords — such as `Ctrl+n` and `Ctrl+p` — across workspaces, tabs, and panes. For international and IME-reliant developers who need friction-free keyboard navigation.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[yxhta/herdr-agents-picker](https://github.com/yxhta/herdr-agents-picker)**

A modal fuzzy search popup built with Ratatui that previews active agent panes in real time and focuses the selected session on Enter. For developers navigating large numbers of parallel agent panes across workspaces. ---

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[code-yeongyu/web-terminal](https://github.com/code-yeongyu/web-terminal)**

Mobile-first self-hosted web terminal powered by Ghostty WASM — disconnect-surviving sessions, file explorer, herdr integration. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Joxtacy/herdr-plugin-vault](https://github.com/Joxtacy/herdr-plugin-vault)**

Browse past Claude Code sessions in a herdr popup and resume the one you pick in a new tab. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[htlin222/herdr-agent-self-reload-skill](https://github.com/htlin222/herdr-agent-self-reload-skill)**

Self-reload skill for herdr AI agent sessions — re-prompt the current pane after a delay. Install: add htlin222/herdr-agent-self-reload-skill. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[vsem-azamat/herdr-telegram](https://github.com/vsem-azamat/herdr-telegram)**

Telegram forum topics bound to stable Herdr agent sessions. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[BradleyLWood/herdr-sessions](https://github.com/BradleyLWood/herdr-sessions)**

Provides integration and dedicated functionality for herdr sessions in Herdr sessions. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[fjordlars/herdr-session-manager](https://github.com/fjordlars/herdr-session-manager)**

Small terminal UI for managing named [Herdr]( sessions. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[salkhalil/herdr-sessionizer](https://github.com/salkhalil/herdr-sessionizer)**

tmux-sessionizer for herdr: fzf over open workspaces and zoxide directories, create-or-focus with template tabs. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[Duzc01/herdr-session-finder](https://github.com/Duzc01/herdr-session-finder)**

Fuzzy-search Claude Code sessions across every project; resume the one you pick. A herdr plugin. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[iiii1224/herdr-statusline](https://github.com/iiii1224/herdr-statusline)**

Customizable status line for herdr sessions. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[pawaca/even-better](https://github.com/pawaca/even-better)**

Mirror your live herdr terminal agent sessions (Claude Code / Codex) to Even Realities G2 glasses — even-terminal protocol compatible. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![HTML](https://img.shields.io/badge/-555555?logo=html5&logoColor=white&style=flat-square) **[JeremiahChurch/herd-remote](https://github.com/JeremiahChurch/herd-remote)**

Phone-friendly web control surface for herdr terminal/agent sessions - spawn, monitor, and drive Claude/Codex sessions from your phone. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[nickboy/herddeck](https://github.com/nickboy/herddeck)**

Stream Deck control surface for herdr agent sessions (local + remote). Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[KUKARAF/collie_voice_commands](https://github.com/KUKARAF/collie_voice_commands)**

Rust/Tauri Android app: voice-driven commands to Collie/Herdr agent sessions with OpenRouter TTS summaries. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[lsisoft/herdr-telegram-slack-bridge](https://github.com/lsisoft/herdr-telegram-slack-bridge)**

Bidirectional Telegram and Slack bot bridge for Herdr agent sessions, routing blocked-agent alerts and chat replies back to Herdr or tmux panes. Enables rapid switching, fuzzy-finding, and lifecycle restoration across active sessions.

[↑ Back to contents](#contents)

### Sessions › Persistence, Snapshot & State Restore

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[nickmaglowsch/herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore)**

Tags every Claude Code pane with a session ID, then snapshots your workspace / tab / cwd layout on a clean `herdr server stop` and replays it on the next cold boot — `claude --resume` and all — so your conversations come back where you left them. Claude-only and clean-shutdown-only by design, it's the answer to losing your agent setup to a reboot.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Angel-O/herdr-agent-resume](https://github.com/Angel-O/herdr-agent-resume)**

A Herdr plugin that generates and pastes or copies the exact resume commands for interrupted AI agent sessions. Lets you quickly bring back Claude Code, Codex, or custom agent contexts inside any pane. For developers who frequently detach, switch, or restart agent sessions.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[bengemine/herdr-hibernate](https://github.com/bengemine/herdr-hibernate)**

Suspends idle coding agent panes (Claude Code, Codex, Grok) to free system memory while preserving pane state and working directory context. Allows instant resumption of hibernated sessions with a single Enter keypress. For developers running large fleets of concurrent agents who want to reduce background memory consumption without terminating processes.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[dmangla3/herdr-fork-from-message](https://github.com/dmangla3/herdr-fork-from-message)**

Forks Claude Code or Codex agent sessions from any earlier message checkpoint directly into a new Herdr workspace, tab, or pane. It parses agent conversation histories so you can explore alternative implementation branches without losing your original session state. Built for developers who want git-like branching for AI agent conversations.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[iviaxpow3r/herdr-session-parker](https://github.com/iviaxpow3r/herdr-session-parker)**

Stashes active panes and tabs into parked sessions and restores them later with their agent state intact. Lets you clear out working space during context switches without terminating running agents or losing prompt progress. For developers managing multiple active agent tasks across long-running sessions.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[mo-arvan/herdr-claude-auto-retry](https://github.com/mo-arvan/herdr-claude-auto-retry)**

Automatically detects when Claude Code panes stall on Anthropic rate limits or server errors and triggers a safe resume sequence without tmux or wrappers. It hooks Herdr agent status events and ensures only idle or blocked agent panes are prompted while actively working panes remain untouched. For developers running long Claude Code sessions who want unattended retry resilience.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[moneycaringcoder/herdr-tether](https://github.com/moneycaringcoder/herdr-tether)**

Detaches long-running terminal tasks into background daemons so processes persist even when the main Herdr window is closed. It allows local and remote terminal workloads to stay active independently of the multiplexer interface. Built for developers running persistent builds or remote tasks that must outlive UI sessions.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[nikok6/herdr-mirror](https://github.com/nikok6/herdr-mirror)**

Mirrors remote Herdr workspaces and agent states into your local sidebar over SSH or Docker. Remote sessions appear alongside local workspaces so you can inspect terminal streams, monitor agent status, and send inputs without switching windows. For developers orchestrating agent fleets across multiple remote servers.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[noviadi/herdr-layout](https://github.com/noviadi/herdr-layout)**

Saves and restores workspace pane layouts in Herdr, functioning like tmux-resurrect for agent workflows. It serializes active pane splits and arrangements so complex multi-agent workspace geometries can be replayed on demand. For developers who work with fixed split layouts and want instant layout restoration across sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[ntindle/herdr-resurrect](https://github.com/ntindle/herdr-resurrect)**

Captures complete Herdr environment snapshots—including workspaces, tabs, panes, directories, and running agent processes—for quick restoration after crashes or restarts. It operates like tmux-resurrect to make agent session state durable across power cycles. For developers running long-lived multi-agent workloads that need restart resilience.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[tomasvarga/herdr-e2b](https://github.com/tomasvarga/herdr-e2b)**

A Herdr plugin that mirrors any active git worktree into an ephemeral E2B cloud sandbox on demand. It uploads a snapshot containing uncommitted changes without requiring git push or remote branch setup, launching a remote agent session inside the isolated cloud environment. For developers who want to offload risky or resource-intensive agent execution to secure cloud microVMs.

[↑ Back to contents](#contents)

### Sessions › Workspace & Multi-Session Management

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[third774/herdr-last-workspace](https://github.com/third774/herdr-last-workspace)**

Stores the last two focused workspace IDs (not positional numbers, so it survives reordering) and binds one key to toggle focus between the current and previous workspace; if the previous one was closed, it exits cleanly with no error toast. For keyboard-heavy users who bounce between two workspaces and want a single `prefix+Tab` to do it.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[dantehemerson/herdr-last-tab](https://github.com/dantehemerson/herdr-last-tab)**

A lightweight navigation plugin that tracks tab focus history and lets you toggle back to your previously active tab with a single keystroke. It brings fast back-and-forth switching to complex multi-tab Herdr workflows. For developers juggling active coding tabs and reference panes who want instant toggle navigation.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[den-tanui/herdr-zoxide](https://github.com/den-tanui/herdr-zoxide)**

Connects zoxide's frecent directory database to Herdr's workspace, tab, and pane creation commands. It lets you jump straight into recent project paths without typing long directory strings. For developers who rely on zoxide for fast shell navigation and want the same speed when opening workspaces.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[douglascorrea/herdr-agent-inbox](https://github.com/douglascorrea/herdr-agent-inbox)**

A central inbox and session tracker for AI coding agents running inside Herdr. It aggregates running times, workspace-level statistics, session titles, and unread statuses to make parallel agent triage manageable. For engineers coordinating multiple agent sessions across workspaces who need an organized review queue.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[osamahbeig/herdr-grove](https://github.com/osamahbeig/herdr-grove)**

Renders a grouped directory and project tree in an interactive popup overlay inside Herdr. Lets you jump straight into any workspace or project folder with a single click or keypress. For developers juggling multiple repositories across deep folder structures.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[taxueseek/session-digger](https://github.com/taxueseek/session-digger)**

Indexes conversation histories from Claude Code, Codex, and other agents into an SQLite FTS5 database searchable directly within Herdr. It tracks token usage and cache performance while generating local HTML review reports without external dependencies. For developers auditing and retrieving knowledge across diverse agent sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[to4iki/herdr-unread-jump](https://github.com/to4iki/herdr-unread-jump)**

Binds a quick navigation action to jump immediately to the next Herdr pane that requires human attention. It prioritizes blocked agents waiting on user confirmation before cycling through completed tasks. Ideal for operators running large agent fleets who need to unblock agents without searching through tabs.

[↑ Back to contents](#contents)

---

## Worktrees, config & terminal UX

Shaping Herdr around your terminal — keymaps, worktrees, statuslines, diff review, and themes.

### Worktrees › Git Worktree Automation

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[noamsiegel/git-wt-herdr](https://github.com/noamsiegel/git-wt-herdr)**

Maps your git worktree lifecycle onto Herdr — creating a worktree opens a focused tab at that directory, removing it closes the tab, and switching focus brings the right one forward. It's the reference implementation of the `git-wt.plugin.v0` contract, pure Bash with `yq` and no Node or Python, so it drops cleanly into an existing `git-wt` setup.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[SirTenzin/superherd](https://github.com/SirTenzin/superherd)**

A CLI that bridges the Superset workspace manager into Herdr: from a Superset-imported repo, one command creates the worktree, opens it as a Herdr workspace, and mirrors Superset's setup terminals as live tabs. It drives the Herdr CLI for workspace and tab creation, forwards Ctrl-C into the Superset PTYs, and ejects the launching pane when it's done. For teams who run Superset (the agent-tooling one, not Apache Superset) alongside Herdr and want worktree setup automated end to end.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[mattarau/wt-herdr](https://github.com/mattarau/wt-herdr)**

Keeps Worktrunk-managed git worktrees and Herdr workspaces in sync: a workspace opens when a worktree is created, closes when it is removed, and focus follows when you switch. Ships health checks, dry-run mode, and toast notifications for lifecycle events. For teams running Worktrunk and Herdr side-by-side who want their workspace layout to mirror their worktree state without manual management.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[qdentity/herdr-worktree-lifecycle](https://github.com/qdentity/herdr-worktree-lifecycle)**

Dispatches `worktree.created`, `worktree.opened`, and `worktree.removed` to executable wrappers the repo ships itself (`scripts/worktree-setup` and `scripts/worktree-teardown`), serializing concurrent events per worktree path and notifying on completion. Unlike plugins that run a fixed command or read a TOML, the provisioning logic lives inside the repo being developed — the plugin is just the wiring. For teams who want reproducible per-repo setup checked into source control alongside the code it prepares.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[shizlie/herdr-setup-bootstrap](https://github.com/shizlie/herdr-setup-bootstrap)**

Reads `worktree_init.toml` from the main repo root and, for each new worktree, runs the configured command and copies the listed glob patterns (`.env*`, `.wrangler`, `public/`, …) from the primary checkout into the new one, preserving each file's repo-relative path. It hooks both the CLI and UI creation paths and writes an idempotency marker so a checkout is bootstrapped only once. For monorepos where gitignored locals need to travel to every worktree, not be re-created from scratch.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[persiyanov/herdr-fresh-worktree](https://github.com/persiyanov/herdr-fresh-worktree)**

On `worktree.created` it fetches `origin HEAD` and hard-resets the new worktree's branch to it — but only when the branch has no upstream, no same-named remote branch, a clean tree, and no commits that live nowhere else, so it freshens a genuinely new branch without ever moving real work. A `node --test` suite exercises every guard and idempotency path against throwaway repos. For developers who keep getting worktrees based on a stale local main and want each new branch to start from the real upstream tip.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[razajamil/herdr-plugin-workspace-manager](https://github.com/razajamil/herdr-plugin-workspace-manager)**

Define tabs, pane splits, and per-pane startup commands once in YAML, point a repo at a layout, and every new worktree — created from the CLI or the TUI — opens straight into it. Supports a one-off blocking setup command (e.g. `npm install`) before the layout spawns, and ships a `remove-gone` command that prunes worktrees whose upstream branch was deleted after a merge. For developers who rebuild the same working view by hand every time they start a feature branch.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[peterferguson/herdr-conductor-worktree](https://github.com/peterferguson/herdr-conductor-worktree)**

Creates Herdr worktrees under Conductor's expected `~/conductor/workspaces/<repo>/<workspace>` layout, registers them in Conductor's database, and ships a sync pane that reconciles which Conductor workspaces should open in Herdr and which archived ones should close — with a multi-select list and color-coded action previews. For developers running the Conductor workspace manager alongside Herdr who want the two tools to share state.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[NathanFlurry/herdr-plugin-jj-workspace](https://github.com/NathanFlurry/herdr-plugin-jj-workspace)**

Wraps `jj workspace add` and `jj workspace remove` behind two keybindings — one to create a named Jujutsu workspace as a fresh Herdr workspace, one to open it in a new tab — replacing the manual new-tab → add → cd sequence. For Jujutsu users who want worktree-like isolated contexts in Herdr without switching to git.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[devashish2203/herdr-worktrunk](https://github.com/devashish2203/herdr-worktrunk)**

Adds an `fzf` picker inside Herdr to switch to an existing Worktrunk-managed worktree or type a new branch name to create one, with Worktrunk's own hooks (install deps, copy `.env`, run templates) executing in the pane you land in; a separate remove action gates on unmerged or dirty branches first. Where `mattarau/wt-herdr` reactively mirrors Worktrunk state, this drives Worktrunk interactively from inside Herdr. For Worktrunk users who prefer a keyboard picker over automatic syncing.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[kkckkc/herdr-plugin-gh-workflow](https://github.com/kkckkc/herdr-plugin-gh-workflow)**

Takes a GitHub issue ID, creates a branch via `gh issue develop`, adds a worktree on it, and builds a new Herdr workspace with tabs pre-configured from a `herdr-workspace.yaml` in the repo root — collapsing the whole issue-to-environment flow into one action. Distinct from `herdr-plugin-github-start`, which launches agents from existing context; this builds the dev environment from scratch. For developers who start each issue in a dedicated worktree with a per-project layout.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[persiyanov/herdr-reviewr](https://github.com/persiyanov/herdr-reviewr)**

Opens a persistent split beside your agent showing an uncommitted, branch, or last-turn diff; you leave line-range comments as inline cards and drop every one into the agent's input buffer in a single keystroke. Eighteen palettes (Catppuccin, Dracula, Nord, Gruvbox, Tokyo Night, …), a `gh`-backed PR tab, and a full worktree browser ship alongside the review flow. For developers who review their agent's changes without ever leaving the terminal.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[smarzban/herdr-file-viewer](https://github.com/smarzban/herdr-file-viewer)**

A read-only TUI that lives in a Herdr split: the left pane is a git-status directory tree (M/A/D/? markers, changed-files filter, merge-base or HEAD baseline) and the right pane renders diffs, Markdown, or syntax-highlighted code chosen automatically by file state. In-pane fuzzy search, per-file search, a worktree switcher, and zoom ship out of the box, delegating to `delta`/`bat`/`glow` when present and degrading gracefully when not. For developers who want to review an agent's working tree without switching context.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[beomjungil/herdr-lazygit-overlay](https://github.com/beomjungil/herdr-lazygit-overlay)**

A two-file plugin: a manifest that declares a lazygit pane with `overlay` placement, and a launcher that forwards the focused pane's cwd via `--cwd` before opening it. Herdr's overlay mode zooms lazygit over the active pane and restores focus and zoom state on exit. For users who want one binding to inspect git state without rearranging their layout.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[edmundmiller/herdr-plugin-hunk](https://github.com/edmundmiller/herdr-plugin-hunk)**

Six actions — worktree, staged, and branch diffs, each in a split pane or a new tab — that launch the Hunk diff viewer scoped to the active workspace, with `HUNK_THEME` passing a named theme so it stays visually consistent with your Herdr theme. For teams already running Hunk who want diff panes without leaving their session.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer)**

Automatically renames a numbered Herdr tab — and, when it's an auto-generated linked worktree, the git branch and workspace too — to a short slug derived from the agent's first prompt, computed on-device via Apple FoundationModels or Codex. For anyone running many numbered tabs who wants them to self-label instead of staying "1", "2", "3".

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[ynny-github/herdr-event-hook](https://github.com/ynny-github/herdr-event-hook)**

A Herdr plugin that reads a committed `.herdr-event-hook.toml` and runs commands — e.g. `docker compose up -d` and `down` — on the `worktree.created` and `worktree.removed` events, so a new worktree's service stack starts automatically and tears down when the worktree is removed. For developers whose per-worktree dev environment needs a database or other background service.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mkdir700/herdr-config](https://github.com/mkdir700/herdr-config)**

A portable Herdr config pack: a `config.toml` with worktree settings and a full LazyVim-aligned keybinding remap, bundled with four small local plugins (diff review, copy-workspace-path, a lazygit tab, and a PR-status dot). For Vim users who want their Herdr bindings and layout to feel like their editor.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[aleslanger/herdr-strays](https://github.com/aleslanger/herdr-strays)**

A terminal dashboard that tracks and cleans up stray git worktrees created during multi-agent sessions. It lists active project trees, streams file diffs in real time, and lets you dispatch follow-up prompts directly to Claude Code panes in Herdr. Designed for developers managing parallel agent branches who need fast diff inspection and worktree hygiene.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[alexarthurs/herdr-sidebar](https://github.com/alexarthurs/herdr-sidebar)**

Combines a file tree explorer and Git source control into a single persistent Herdr sidebar pane. It features syntax-highlighted previews, visual diffs, GitLens-style change details, and AI commit message generation. For developers who want IDE-style file and version control navigation inside their terminal multiplexer.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[asumaran/gotopr](https://github.com/asumaran/gotopr)**

Scans local git repositories and worktrees to find open GitHub pull requests and switches Herdr focus directly to the matching workspace. It pairs with the Herdr CLI to streamline navigating between active review branches without searching through tabs manually. For developers juggling multiple simultaneous PR branches and worktrees across repositories.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[azizuysal/herdr-workbench](https://github.com/azizuysal/herdr-workbench)**

An IDE-style workbench sidebar plugin that brings collapsible file trees, live text search, git status grouping, and syntax-highlighted previews into a dedicated Herdr pane. It supports editor handoffs and quick-look views so you can inspect project structure without leaving your terminal workspace. For developers who want VS Code-like project browsing inside Herdr.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[baotran01/herdr-agent-diff](https://github.com/baotran01/herdr-agent-diff)**

Provides an in-pane diff viewer that lets you review unstaged git changes and filesystem modifications made by autonomous agents before approving them. It hooks into Herdr's pane management to present clean, navigable patch summaries side-by-side with agent output. For developers who want fast visual verification of agent edits without leaving their multiplexer workflow.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[bfreed/herdr-corral](https://github.com/bfreed/herdr-corral)**

A workmux replacement tailored for Herdr that automates Git worktree creation alongside per-branch environment files, dependencies, and dedicated tabs for agents, shells, and dev servers. It provisions isolated environments across Herdr workspaces and provides safe, merge-aware cleanup when tasks finish. For teams working across multiple feature worktrees who want full workspace scaffolding in one command.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[blurname/herdr-git-tab-name](https://github.com/blurname/herdr-git-tab-name)**

Automatically updates Herdr tab labels to match the active Git branch of the currently focused pane. Keeps multi-branch workspaces organized at a glance without manual tab renaming. - **Code Evidence & Technical Analysis:** Defines `herdr-plugin.toml` with lifecycle hooks listening to `pane.focused` and `tab.focused`, resolving the current Git branch and invoking Herdr socket `tab.rename` method.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[brianh20/herdr-stagr](https://github.com/brianh20/herdr-stagr)**

Adds a source control sidebar to Herdr for staging, unstaging, and discarding git changes with side-by-side diff views. Lets developers quickly review and manage agent modifications without switching context or opening external Git TUIs. Built for developers running parallel agents that touch multiple files across worktrees.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[cdowell09/herdr-pr-board](https://github.com/cdowell09/herdr-pr-board)**

Aggregates open GitHub pull requests across multiple repositories into a unified, configurable dashboard inside a Herdr tab. Tracks CI status, review states, and branch details alongside your active agent workspaces. For engineering leads and solo developers managing simultaneous PRs spawned by agent fleets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[chouxcreams/herdr-dashboard](https://github.com/chouxcreams/herdr-dashboard)**

A Ratatui terminal dashboard that aggregates GitHub pull requests across workspaces and panes, displaying live PR state, CI check results, and reviewer approvals. A background daemon caches state for instant modal popups, with keyboard navigation to jump straight to a pane or open the PR. For multi-agent setups where each pane manages its own branch and PR.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[crexi/herdr-worktree-copy](https://github.com/crexi/herdr-worktree-copy)**

Listens to Herdr worktree creation events and reads a .worktree-copy manifest to automatically copy environment files or symlink shared directories from the main worktree. For developers using worktrees who need automated local configuration setup. ---

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Crokily/herdr-lazygit](https://github.com/Crokily/herdr-lazygit)**

Runs lazygit inside a dedicated Herdr sidebar pane with one-key shortcuts to open, expand, and stage changes. Built-in AI assistance generates commit messages based on pending diffs directly from the pane. For developers who want interactive Git workflows and automated commit authoring in Herdr.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[cyperx84/herdr-notes](https://github.com/cyperx84/herdr-notes)**

Maintains dedicated Markdown scratchpads keyed to each Herdr workspace ID so planning notes and prompt drafts stay scoped to their project context. Opens scratch files in an instant side split without polluting your git working tree. For developers managing multiple concurrent workspaces who need persistent per-project notes.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[danilolucasmd/herdr-clone-layout](https://github.com/danilolucasmd/herdr-clone-layout)**

Clones your active workspace layout directly into every newly created Herdr worktree without requiring manual configuration files or static templates. It uses your currently arranged splits and tabs as a dynamic blueprint for fresh worktree environments. For developers who want consistent multi-pane setups across branches without writing declarative layout files.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[disintegrator/trunkr](https://github.com/disintegrator/trunkr)**

Connects Worktrunk worktree management directly into Herdr, synchronizing worktree lifecycles with persistent workspace sessions. Ideal for developers who use Worktrunk to switch branches and isolate multi-agent development environments. - **Code Evidence & Technical Analysis:** Rust-implemented plugin with `herdr-plugin.toml` bridging Worktrunk worktree operations to Herdr workspace creation/teardown socket endpoints.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[dwarvesf/herdr-quicklook](https://github.com/dwarvesf/herdr-quicklook)**

Pops open an instant preview overlay of any file path copied to your clipboard, with a single keypress to escalate into a full terminal file viewer. Saves the friction of manually typing out paths or splitting panes just to inspect an agent-generated artifact. For developers frequently reviewing files mentioned in agent outputs or git diffs.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[EzraCerpac/jj-waltz](https://github.com/EzraCerpac/jj-waltz)**

An interactive Jujutsu (`jj`) workspace switcher inspired by Worktrunk, designed to manage and switch between VCS workspaces inside Herdr. Automatically synchronizes Jujutsu workspace directories with Herdr tabs and workspaces so you can navigate version-controlled task branches without context loss. For Jujutsu users managing parallel agent checkouts alongside Herdr.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Feasy01/herdr-allow](https://github.com/Feasy01/herdr-allow)**

Uses a .herdr-allow file to copy uncommitted secrets, environment variables, and local configurations into freshly spawned worktrees. Ensures new agent workspaces are pre-configured and immediately ready for development. - **Code Evidence & Technical Analysis:** Contains `herdr-plugin.toml` manifest hooked into `workspace.created` events, reading `.herdr-allow` allowlists and replicating matched gitignored files from the root repository into new worktree directories.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[freethinkel/herdr-plugin-git-worktree-hooks](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks)**

Executes custom shell commands automatically upon Git worktree creation and removal, configured through a single global YAML file outside individual repositories. It passes project paths, main repo roots, and event metadata into shell hooks with durable execution tracking. For developers who want standardized bootstrap and teardown workflows across all their worktrees.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[hmu332233/herdr-symlink-worktree](https://github.com/hmu332233/herdr-symlink-worktree)**

Automatically symlinks gitignored files like .env and build caches from your main checkout into newly created Git worktrees. It listens for Herdr worktree creation events and links paths declared in your repo's .herdr-worktree-links file without overwriting existing files. For developers working with multi-agent worktree workflows who want shared local environment files instantly accessible in every branch.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[hotchpotch/herdr-tiny-fingers](https://github.com/hotchpotch/herdr-tiny-fingers)**

Brings tmux-fingers style keyboard hints to Herdr for rapid on-screen text copying. It scans the visible pane output for URLs, Git commit hashes, and file paths, generating short character tags you can type to copy tokens instantly. For terminal power users who want mouse-free token extraction from agent outputs.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[JacquesvanWyk/herdr-hunk](https://github.com/JacquesvanWyk/herdr-hunk)**

Combines an interactive fzf picker for Hunk git diffs with an autodiff hook that automatically opens changes in a split pane when an agent finishes. It inspects repository state to reuse existing diff viewers and ignore clean workspaces. For developers using Hunk who want immediate visual review of agent modifications without manual command execution.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[JacquesvanWyk/herdr-lazygit](https://github.com/JacquesvanWyk/herdr-lazygit)**

Opens `lazygit` in a Herdr split pane or dedicated tab with smart state toggling that dynamically opens, focuses, or closes the Git interface depending on your current focus. It preserves pane orientation and cwd so you can stage, commit, and inspect diffs beside your active agent without manual pane teardown. For developers who want frictionless Git operations inside their terminal workspace layout.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[jlimas/herdr-worktree-seed](https://github.com/jlimas/herdr-worktree-seed)**

Bootstraps new Git worktrees instantly with copy-on-write node_modules and pre-configured local dotfiles. It hooks Herdr worktree creation events to link heavy dependencies without duplicate disk usage and seeds project-specific configurations automatically. For TypeScript and Node.js developers spinning up ephemeral agent worktrees who want zero-wait package initialization.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[jorge-huxley/herdr-git-graph](https://github.com/jorge-huxley/herdr-git-graph)**

A read-only TUI plugin that renders your repository commit graph with colored ASCII branch lanes directly inside a Herdr pane. It features branch filtering, fast commit search, and on-demand diff viewing for inspected revisions. For developers tracking complex branch topologies across multiple active agent workspaces.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[jsmenzies/mergr](https://github.com/jsmenzies/mergr)**

Surfaces live GitHub pull request statuses and review indicators directly inside Herdr's workspace sidebar rows. It periodically queries PR metadata for each space's branch and displays compact status tags alongside workspace names without cluttering terminal output. For engineers running multi-branch agent workflows who want quick PR visibility across all active workspaces.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[kazimshah39/herdr-suffix-agent-filter](https://github.com/kazimshah39/herdr-suffix-agent-filter)**

Filters the Herdr Agents sidebar to display only agents running in workspaces that share a matching name suffix. It cleans up crowded agent lists in multi-repository and branched fleet setups by scoping the sidebar view to relevant environments. For developers running parallel agent swarms across similarly named project spaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[kbrdn1/herdr-plugin-gwm](https://github.com/kbrdn1/herdr-plugin-gwm)**

Integrates the gwm CLI into Herdr popup menus to create, switch, clean, and batch-exec across git worktrees, adopting them seamlessly as Herdr workspaces. By keeping gwm as the single source of truth, workspace lifecycles mirror worktree state without divergence. For developers managing multi-branch worktrees via gwm.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[khatriafaz/herdr-plugin-auto-rename](https://github.com/khatriafaz/herdr-plugin-auto-rename)**

Listens to the initial prompt submitted to an agent session and automatically renames the active Herdr workspace and Git branch accordingly. Keeps multi-agent session trees descriptive and aligned with ongoing tasks without manual intervention. - **Code Evidence & Technical Analysis:** `herdr-plugin.toml` manifest with JavaScript runtime hooking session prompt events, summarizing initial prompt intent, and calling `workspace.rename` and `git branch -m` via Herdr socket methods.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[langtind/gren-herdr](https://github.com/langtind/gren-herdr)**

Bridges the `gren` worktree manager into Herdr to create, switch, and remove git worktrees mapped to tabs. It triggers gren post-creation setup hooks automatically when provisioning new branch workspaces. For developers using gren who want isolated agent worktrees managed seamlessly from Herdr.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[LeonardoTrapani/herdr-js-worktree-bootstrap](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap)**

Automatically initializes fresh JavaScript and TypeScript worktrees by detecting project lockfiles and safely restoring untracked environment configs. It ensures newly spawned agent worktrees have installed dependencies and necessary runtime environment files before commands run. For JS and TS developers running agent fleets in isolated worktree workspaces.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[mariotmc/herdr-source-control](https://github.com/mariotmc/herdr-source-control)**

Embeds a lightweight source control pane inside Herdr that tracks modified files, current branch, and upstream synchronization state. It combines automatic background polling with focus-triggered refreshes to keep repository status up to date. For developers who want dedicated git status visibility alongside their agent sessions without switching windows.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mattyan1053/herdr-compose](https://github.com/mattyan1053/herdr-compose)**

Displays per-workspace Docker Compose container health in the Herdr sidebar, paired with quick toggle shortcuts and an interactive service-inspection popup. It cleans up compose stacks automatically when worktree checkouts are removed to prevent port collisions. For engineers running multi-container backend stacks across parallel worktrees.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mroth/herdr-jj-status](https://github.com/mroth/herdr-jj-status)**

Displays Jujutsu (jj) bookmarks, working copy status, and change IDs directly inside the Herdr workspace sidebar. It updates dynamically as agents commit changes or switch branches in their respective Jujutsu workspaces. Built for developers using Jujutsu alongside Herdr who want immediate VCS context without running status commands manually.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[nimrc/herdr-git-pull](https://github.com/nimrc/herdr-git-pull)**

Runs `git pull` for the active workspace in a non-intrusive overlay pane with a single keybinding. It automatically resolves the repository root across subdirectories and linked worktrees, falling back to an interactive shell if merge conflicts arise. For developers who want fast repository syncing without interrupting their primary terminal pane.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[osolmaz/herdr-branch-cleanup](https://github.com/osolmaz/herdr-branch-cleanup)**

Monitors git branches across Herdr panes and automatically checks out the default branch when a feature branch is merged or deleted on GitHub. Built-in guards verify that the working tree is clean and no agent is actively typing before switching branches. For developers running multi-branch agent workflows who want to keep idle panes tidy without manual git maintenance.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[qq88976321/herdr-copy-search](https://github.com/qq88976321/herdr-copy-search)**

Brings tmux-copycat pattern matching and extrakto token extraction to Herdr pane scrollback buffers. It lets you run incremental regex searches across terminal history and copy URLs, git SHAs, or file paths straight to the system clipboard via OSC 52. For keyboard-centric developers who want rapid text capture without reaching for the mouse.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[rotemb-wond/herdr-copy-hints](https://github.com/rotemb-wond/herdr-copy-hints)**

Overlays quick keyboard hint labels on visible terminal tokens like file paths, Git commit hashes, and URLs directly inside your Herdr pane. Typing the matching letter combination copies the target text straight to the system clipboard without touching the mouse. For keyboard-centric developers who frequently grab identifiers and paths from agent terminal scrollback.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[scott306lr/herdr-plugin-hunk-autodiff](https://github.com/scott306lr/herdr-plugin-hunk-autodiff)**

Automatically splits a companion pane running the hunk interactive diff viewer whenever an agent completes its turn with uncommitted changes. Keeps focus on the agent pane while giving you instant visual verification of what files were modified. For developers reviewing multi-turn agent edits without manual git diff invocations.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[scoussens-nthplusio/herdr-worktree-include](https://github.com/scoussens-nthplusio/herdr-worktree-include)**

Automatically copies ignored and untracked configuration files into newly spawned Herdr worktrees based on repository `.worktreeinclude` rules. It uses the same matching specification as Claude Code to ensure environment variables and local configurations carry over seamlessly. For developers relying on local environment files across parallel worktree sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[serhii-chernenko/herdr-worktreeinclude](https://github.com/serhii-chernenko/herdr-worktreeinclude)**

Enables custom target paths for new Git worktrees in Herdr while respecting `.worktreeinclude` configuration files. It automatically copies specified untracked environment and configuration files into newly initialized worktree workspaces, matching Claude CLI behavior. Built for teams with local configuration dependencies who need new agent workspaces fully initialized on creation.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[sfroment/herdr-git-detail](https://github.com/sfroment/herdr-git-detail)**

Exposes rich Git status metrics—including modified, staged, and untracked counts, ahead/behind commits, and stashes—as a `$git_detail` custom sidebar token. It updates automatically when pane focus changes, keeping repository health visible without running git status manually. For developers who want deep version control context alongside agent status in the sidebar.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[tanshio/herdr-worktreeinclude](https://github.com/tanshio/herdr-worktreeinclude)**

Listens to Herdr worktree creation events and automatically copies gitignored files like local envs and configs into new worktree directories using a standard .worktreeinclude pattern. Follows the Claude Code convention so agent workspaces are immediately ready to run without manual setup. For developers spinning up parallel worktree agents who need seamless local environment parity.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[tdi/herdr-worktree-from-linear](https://github.com/tdi/herdr-worktree-from-linear)**

Fuzzy-picks active Linear issues and spins up matching Git worktrees and Herdr workspaces in one step. It switches to existing branches seamlessly and can split a companion pane displaying full issue descriptions and assignees. For teams managing their development tasks in Linear who want instant workspace isolation.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[tdi/herdr-worktree-from-pr](https://github.com/tdi/herdr-worktree-from-pr)**

Automates the creation of isolated Git worktrees from GitHub pull requests and opens them directly as new Herdr workspaces. It handles branch checkout and multiplexer workspace initialization in one automated step. For developers and code reviewers who frequently inspect GitHub PRs in dedicated environments.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[tdi/herdr-worktree-setup](https://github.com/tdi/herdr-worktree-setup)**

Automates repository setup whenever Herdr creates a new Git worktree, copying `.env` files from the main branch and running commands like `mise trust` and `direnv allow`. It ensures fresh agent worktrees have installed dependencies and authorized tooling immediately upon creation. For teams using parallel worktrees who want zero-manual-step workspace bootstrapping.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[thomasschafer/herdr-kiosk](https://github.com/thomasschafer/herdr-kiosk)**

A fuzzy-finding launcher that searches local Git repositories and branch checkouts to open them directly as Herdr workspaces or worktrees. It supports customizable directory scan depths, keybinding overlays, and startup pane recipes configured via TOML. For developers who switch frequently between multiple repositories and branch worktrees.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[tjg184/herdr-worktree](https://github.com/tjg184/herdr-worktree)**

Integrates Worktrunk lifecycle hooks and native Git worktree operations directly into Herdr workspaces and tabs. It automates environment preparation such as dependency installation and environment variable propagation whenever a new worktree pane is created. For developers running parallel agent workspaces who need consistent worktree setup across projects.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[wyattjoh/herdr-plugin-gh-pr](https://github.com/wyattjoh/herdr-plugin-gh-pr)**

Surfaces the GitHub PR number and CI check status for the active agent pane's branch directly in the Herdr sidebar. Rate-limited background updates prevent API throttling while keybindings offer instant manual refresh and PR opening. For developers tracking branch and review status across parallel agent panes.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[zerodice0/herdr-plugin-worktree-bootstrap](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap)**

Hooks into Herdr Git worktree creation to copy gitignored local configs, environment files, and credentials into the new workspace. Automatically triggers required build or setup commands so new agent panes are immediately functional. For developers running multi-worktree fleets who need painless environment replication.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[kenn-io/ghosthub](https://github.com/kenn-io/ghosthub)**

A multiplexer-native power terminal for your local and remote sessions. Supports tmux, Herdr, and Zellij, with built-in git worktree management. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[spirin22/herdr-plugins](https://github.com/spirin22/herdr-plugins)**

herdr plugins: seed git worktrees with gitignored files and per-repo setup steps. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[mkdir700/herdr-plugin-worktree](https://github.com/mkdir700/herdr-plugin-worktree)**

herdr plugin: start a git worktree from a GitHub issue (new branch, claude-named), a PR, or a raw branch name — auto-detected. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[timofey-TK/herdr-worktree-hooks](https://github.com/timofey-TK/herdr-worktree-hooks)**

herdr plugin: run custom setup/teardown commands when a git worktree is created, opened, or removed. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[dkarter/hwt](https://github.com/dkarter/hwt)**

🌳 Frictionless Herdr Worktree Orchestration. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[kennethkoontz/herdr-worktree-sync](https://github.com/kennethkoontz/herdr-worktree-sync)**

A [Herdr]( plugin that copies gitignored files into freshly created worktrees, honors the repo's `.worktreeinclude` file, and allows and reloads direnv at the new worktree root. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[arjenblokzijl/herdr-worktree-autosetup](https://github.com/arjenblokzijl/herdr-worktree-autosetup)**

Herdr plugin: auto-run a setup command (e.g. p setup) in a new git worktree on worktree.created. Visible pane by default. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[eightHundreds/herdr-worktreeinclude](https://github.com/eightHundreds/herdr-worktreeinclude)**

Herdr plugin: copy .worktreeinclude-selected gitignored files into new worktrees. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[riclib/herdr-worktree-layout](https://github.com/riclib/herdr-worktree-layout)**

A herdr plugin: auto-build a file-viewer + two-shells layout in git worktrees (exact 60/40, 75/25 splits). Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[untalfranfernandez/herdr-worktreeinclude](https://github.com/untalfranfernandez/herdr-worktreeinclude)**

Herdr plugin that populates every new git worktree with the gitignored local files it needs — .env, settings.local.json, fixtures. Declare them once in a .worktreeinclude file using gitignore syntax and every worktree Herdr creates gets them automatically. Implements Claude Code’s .worktreeinclude contract. Works with any git repo. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[botonddombi/boti-toolkit](https://github.com/botonddombi/boti-toolkit)**

Personal dev environment toolkit: herdr worktree helpers, machine setup playbook, Claude Code setup agent. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[snics/herdr-worktree-from-gitlab](https://github.com/snics/herdr-worktree-from-gitlab)**

herdr plugin: create a git worktree + workspace from a GitLab issue (via glab). Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[dabeeeenster/herdr-worktree-local-files](https://github.com/dabeeeenster/herdr-worktree-local-files)**

herdr plugin: link gitignored local config files into new git worktrees. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[jal-co/pi-herdr-worktree](https://github.com/jal-co/pi-herdr-worktree)**

Pi extension: git worktrees via Herdr's native worktree API, with project-level post-create/pre-remove hooks. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[toyamarinyon/herdr-worktree-setup](https://github.com/toyamarinyon/herdr-worktree-setup)**

Run a repo-committed setup script in every new Herdr worktree. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[AndreGeng/herdr-worktree-dispatcher](https://github.com/AndreGeng/herdr-worktree-dispatcher)**

Standalone Herdr plugin that dispatches coding tasks into temporary git worktrees and starts an agent in the new checkout. The public entrypoint remains `scripts/dispatch.sh`; the implementation is TypeScript compiled to `dist/cli.js` for. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[wthorp/squeeze-chute](https://github.com/wthorp/squeeze-chute)**

Coordinate GitHub issues through isolated Herdr worktree teams. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[mopeneko/herdr-worktree-hook-plugin](https://github.com/mopeneko/herdr-worktree-hook-plugin)**

A [herdr]( plugin that runs user-defined shell commands right after a new worktree is created — the equivalent of a `postCreate` hook. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[ralphcrisostomo/herdr-goal-skill](https://github.com/ralphcrisostomo/herdr-goal-skill)**

Claude Code skill: orchestrate a goal across parallel lead agents in Herdr (worktrees, model tiering, self-updating). Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[mholtzscher/herdr-worktree-picker](https://github.com/mholtzscher/herdr-worktree-picker)**

Create Herdr worktrees from local or remote branches. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[arjenblokzijl/herdr-worktree-provisioner](https://github.com/arjenblokzijl/herdr-worktree-provisioner)**

Runs per-repo setup in a new worktree's own visible pane — composable and guard-free. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[hung-eggie-do-covergo/delegate-orchestrator](https://github.com/hung-eggie-do-covergo/delegate-orchestrator)**

Fan out one isolated Claude Code sub-agent per repo via herdr worktrees — multi-repo orchestration with worktree reuse and session resume. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[m1sk9/herdr-worktree-hooks-plugin](https://github.com/m1sk9/herdr-worktree-hooks-plugin)**

A plugin that adds customizable hooks to Herdr's Worktree. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[QuentinTorg/stagehand](https://github.com/QuentinTorg/stagehand)**

Human-guided orchestration for coding agents, coordinating Herdr worktrees, author-reviewer loops, Hunk feedback, and GitHub pull-request handoffs. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[eoinest/convo-history](https://github.com/eoinest/convo-history)**

Voice scratchpad for coding agents: a sliding window of speech becomes a Codex prompt in a fresh Herdr worktree, via hotkey or wake word. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[firew0rks/herdr-ci-tokens](https://github.com/firew0rks/herdr-ci-tokens)**

Show PR, CI and review status for every worktree in your herdr sidebar. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[ditwrd/herdr-remote-worktrunk](https://github.com/ditwrd/herdr-remote-worktrunk)**

Herdr remote worktrunk workspace. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ribbons-digital/pi-herd](https://github.com/ribbons-digital/pi-herd)**

Visible Pi session orchestration with Herdr panes and git worktrees. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[simoncrypta/agentic-dev-setup](https://github.com/simoncrypta/agentic-dev-setup)**

Shareable Herdr + worktrunk dev layout for agentic coding workflows. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Ruby](https://img.shields.io/badge/-555555?logo=ruby&logoColor=white&style=flat-square) **[sample-usr/herdr-devenv-worktree](https://github.com/sample-usr/herdr-devenv-worktree)**

A herdr plugin for working with devenv inside worktrees. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[danieljvdm/herdr-worktrunk](https://github.com/danieljvdm/herdr-worktrunk)**

Herdr Plugin to integrate worktrunk for git worktree management. Automates git worktree creation, workspace isolation, and repo-specific setup routines.

[↑ Back to contents](#contents)

### Worktrees › Workspace Lifecycle & Multi-Repo

![Markdown](https://img.shields.io/badge/-555555?logo=markdown&logoColor=white&style=flat-square) **[tomaszhanc/herdr-plugins](https://github.com/tomaszhanc/herdr-plugins)**

My monorepo of [herdr]( plugins. Each plugin lives in its own folder with a `herdr-plugin.toml` manifest and an executable. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[tyler-jewell/herdr-plugins](https://github.com/tyler-jewell/herdr-plugins)**

Pure-Rust Herdr plugins monorepo (stdlib-first). Install with: herdr plugin install tyler-jewell/herdr-plugins/. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[shelken/herdr-plugins](https://github.com/shelken/herdr-plugins)**

Herdr plugins monorepo (auto-pi: open pi by area + session picker). Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[paulrobello/par-herdr-plugins](https://github.com/paulrobello/par-herdr-plugins)**

Custom Herdr plugins (monorepo). Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Diff Review & File Viewers

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[alon-z/herdr-devup](https://github.com/alon-z/herdr-devup)**

Drop a `.herdr/dev.toml` into a project and three actions handle the dev stack: `up` opens the declared tabs and panes running each service, `sync` re-pulls the ngrok tunnel URL and rewrites every env file that bakes it in, and `down` closes exactly the tabs `up` created. The sync step is the differentiator — tunnel URLs rotate, and hand-updating four `.env` files before restarting is the usual time-sink. For full-stack developers who run a tunnel alongside local services and want the URL propagated automatically.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[devskale/herdr-flist](https://github.com/devskale/herdr-flist)**

Splits a narrow sidebar to the right of the focused pane and keeps it in sync with that pane's working directory as you `cd` — including inside SSH sessions, where the remote cwd is parsed from the shell prompt because Herdr doesn't propagate OSC 7 over SSH. Entries are dirs-first with git-status tags and polled on a configurable interval. A lighter glance than the full content-rendering herdr-file-viewer, for users who just want to see where they are.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[krystof018/herdr-git-status](https://github.com/krystof018/herdr-git-status)**

Surfaces CI/CD status inside Herdr two ways: a background poller prefixes each space's sidebar label with a colored dot and open MR/PR number, and an on-demand pane shows the latest run, recent failures, and clickable OSC 8 links — auto-detecting GitLab vs GitHub from each repo's `origin`. Review-state glyphs flag approved, changes-requested, and conflict states in the label itself. For developers who want fleet-wide CI awareness without leaving Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin)**

Remembers which macOS input source (e.g. English vs. Pinyin) was active in each Herdr pane and restores it automatically when focus returns, via a bundled Swift helper or the `macism` backend. For anyone who switches languages or input methods across different agent panes and is tired of fixing it by hand.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[carellano/herdr-dev-servers](https://github.com/carellano/herdr-dev-servers)**

Inspects active Herdr panes to detect running local development servers and monitor their bound ports and process states. It allows developers to review, focus, and safely shut down orphaned server instances without navigating through individual tabs manually. For engineers running multiple service backends across parallel agent workspaces.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[cpcloud/herdr-agentsview](https://github.com/cpcloud/herdr-agentsview)**

Renders a terminal dashboard inside a Herdr pane to aggregate and monitor active AgentsView sessions across projects, models, and agents. It provides real-time activity timelines and metrics without requiring an external web browser. For developers running multiple agent sessions who want an immediate, dense overview of agent workloads directly in their multiplexer.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[dzwduan/herdr-convo-index](https://github.com/dzwduan/herdr-convo-index)**

Builds an interactive turn index for Claude Code sessions running in Herdr panes so you can quickly review long conversation histories. It presents past user prompts and agent responses in a navigable popup overlay without scrolling through terminal buffers. Essential for developers managing lengthy agent reasoning loops who need to pinpoint specific past turns.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[edmundmiller/herdr-plugin-dotfiles-github-link-preview](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview)**

Detects GitHub issue and pull request URLs in active Herdr panes and renders a preview in an adjacent split pane using the GitHub CLI. Allows developers and agents to inspect issue details and discussion threads without leaving the terminal. - **Code Evidence & Technical Analysis:** Requires Herdr 0.7.0+, Python 3, and `gh` CLI.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[flupke/herdr-progressive-reviewer](https://github.com/flupke/herdr-progressive-reviewer)**

A turn-based diff reviewer inspired by Tidewave that steps through code changes generated across agent execution cycles. It presents incremental, turn-by-turn diffs in a Herdr pane so you can verify each editing step before approving follow-up agent runs. For engineers who want granular verification over rapid multi-turn edits.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[iurysza/termscope](https://github.com/iurysza/termscope)**

Scans your terminal screen for visible file paths and web links, letting you fuzzy-select and open them in a dedicated split pane. It keeps your primary shell or agent pane intact while inspecting referenced files. For developers navigating compiler outputs, logs, or agent diffs without manual copying.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[jagzmz/herdr-annotations](https://github.com/jagzmz/herdr-annotations)**

Allows users to select terminal text in Herdr and attach fast, local-first annotations organized into reusable collections. It enables reviewing AI agent plans directly from the terminal and composing line-specific comments into a single feedback prompt. For developers collaborating with coding agents who need structured inline notes without leaving the multiplexer.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[lucasleon2107/herdr-tab-title-sync](https://github.com/lucasleon2107/herdr-tab-title-sync)**

Automatically updates Herdr tab labels based on active conversation titles and prompt summaries extracted from agent sessions. It uses the socket API to rename tabs dynamically as agents progress through different tasks. For users running multiple agent tabs who want clear, self-updating tab descriptions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[maedana/herdr-agents-preview](https://github.com/maedana/herdr-agents-preview)**

A multi-agent preview dashboard that tiles all active agent panes while allocating the majority of terminal width to the focused agent. It gives you peripheral awareness of background workers without losing focus on your primary task. Designed for developers managing parallel agent fleets who want instant visual status.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[narumiruna/herdr-plugins](https://github.com/narumiruna/herdr-plugins)**

Provides a suite of standalone, high-performance Rust plugins designed for Herdr terminal workflows, including a popup GitHub pull request viewer. Each plugin is independently installable and plugs directly into Herdr's native plugin architecture with zero runtime dependencies. Great for developers looking for fast, compiled utilities to extend their Herdr environment.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[opsydyn/herdr-questmancer](https://github.com/opsydyn/herdr-questmancer)**

Transforms live Herdr coding agent sessions into a 16-bit fantasy adventurers' guild overlay. Active agents delve into dungeons, blocked agents request counsel at the guild hall, and completed runs return with loot corresponding to actual operational state. For developers who want a gamified, visual overview of their parallel agent fleet.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[osolmaz/ghzinga](https://github.com/osolmaz/ghzinga)**

A focused TUI that displays a single GitHub issue or pull request alongside your code. A dedicated Herdr plugin intercepts clicked GitHub links in terminal panes and opens them in an interactive side split with review and comment actions. For developers who want fast ticket context without switching to a web browser.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Phoobobo/herdr-workboard](https://github.com/Phoobobo/herdr-workboard)**

A Kanban-style TUI dashboard that structures Herdr workspaces into boards, task statuses into tabs, and active agent sessions into panes. Provides a top-level visual overview of ongoing development tasks and lets you navigate directly between cards and their underlying terminal panes. For developers running multiple concurrent agent tasks who want structured agile board tracking.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[plannotator/herdr-plannotator](https://github.com/plannotator/herdr-plannotator)**

Embeds Plannotator visual plan reviews directly inside a dedicated Herdr browser pane. It allows developers and agents to annotate, critique, and approve implementation plans without switching windows. For teams using Plannotator who want inline plan reviews alongside active coding sessions.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[quantk/herdr-review](https://github.com/quantk/herdr-review)**

Opens an interactive diff of the agent's working tree in a split or tab pane, lets you attach line-level comments, and drafts the notes directly into the source agent's prompt without submitting. It runs natively in Bun/Node without external diff tools. For developers who want fast human-in-the-loop review cycles beside running agents.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ramarivera/herdr-pretty-which](https://github.com/ramarivera/herdr-pretty-which)**

A Rust and Ratatui keybinding overlay that parses your active Herdr configuration alongside defaults to display a searchable which-key popup. Supports tree and list views, search filtering, and contrast-adaptive themes to help you discover and learn complex key chords. For Herdr power users who want an instant cheat sheet for custom bindings and plugin actions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[robert-flo/herdr-terminal-file-manager](https://github.com/robert-flo/herdr-terminal-file-manager)**

A lightweight wrapper that detects the active Herdr pane's working directory and launches the elio terminal file manager natively. Brings fast file previews, inline image rendering, and batch operations directly into agent workspace panes. - **Code Evidence & Technical Analysis:** Contains `herdr-plugin.toml` manifest and shell wrapper invoking `elio` inside active Herdr pane sessions, reading current working directory via Herdr CLI commands and presenting an interactive file manager pane.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[Royal-lobster/herdr-spinup](https://github.com/Royal-lobster/herdr-spinup)**

Displays a customizable launcher screen in every newly created Herdr tab, populated from a JSON configuration file. Selecting a tool launches it directly in the pane and integrates smoothly with Herdr's agent detection. For developers who frequently switch between different tools and agent runtimes across new tabs.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[rvalledorjr/herdr-fresh](https://github.com/rvalledorjr/herdr-fresh)**

A Herdr plugin that embeds the Fresh terminal IDE into a side pane for instant file viewing and editing. It automatically tracks the active workspace root so you can browse, inspect, and tweak source files without leaving your multiplexer layout. For developers who want a lightweight, full-featured terminal editor sidecar next to their agent sessions.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ryanlewis/herdr-tab-renamer](https://github.com/ryanlewis/herdr-tab-renamer)**

Monitors active Herdr panes and dynamically updates tab labels to reflect live agent session titles or current working directories. It eliminates generic tab numbering so you can immediately see what task is running in each tab. Ideal for power users juggling dozens of concurrent agent sessions across different repositories.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[sh1ma/herdr-auto-title](https://github.com/sh1ma/herdr-auto-title)**

Automatically renames Herdr tabs by extracting topics and intent from ongoing Claude Code and Codex conversations. It runs in the background to keep multiplexer tabs organized without manual renaming. For developers managing multiple concurrent AI coding sessions across different tabs.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ShankyJS/herdr-space-scoped-agents](https://github.com/ShankyJS/herdr-space-scoped-agents)**

Filters the Herdr agent sidebar so it only displays agents assigned to the currently focused workspace instead of the entire global fleet. It eliminates sidebar noise when switching between disparate projects and multi-agent workspaces. For developers running heavy multi-agent fleets across several workspaces who want workspace-isolated status views.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[speardragon/herdr-ask-inbox](https://github.com/speardragon/herdr-ask-inbox)**

Aggregates blocked Claude `AskUserQuestion` prompts from across all Herdr workspaces into a single unified popup inbox. You can review pending questions and reply on the spot without manually switching between workspaces or risking sending input to the wrong pane. Designed for developers managing parallel agent fleets who want a frictionless triage workflow for blocked agents.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[takemo101/wave-tui](https://github.com/takemo101/wave-tui)**

A terminal internet radio player with an Agent Planets view that visualizes running Herdr agents as planets orbiting around an audio visualizer. It connects to the Herdr socket when HERDR_ENV is active, offering an ambient stage to monitor fleet activity and jump between panes without interrupting background playback. For developers who want low-distraction background music and a creative live visual overview of active agents.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[tomasvarga/herdr-pickr](https://github.com/tomasvarga/herdr-pickr)**

Intercepts Ctrl-clicked GitHub PR and GitLab MR links to route diffs into tools like tuicr, hunk, or a browser. It supports an optional AI first-pass review to highlight notable changes before manual inspection. For developers reviewing pull requests created by coding agents without switching contexts.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Tomatio13/herdr-google-gmail](https://github.com/Tomatio13/herdr-google-gmail)**

Embeds a terminal Gmail browser directly into a dedicated Herdr split pane, combining `gogcli` and `fzf` for keyboard-driven inbox navigation. It converts HTML emails into formatted text and displays previews alongside your active agent workflows. For terminal-focused developers who want to triage incoming notifications and emails without context-switching away from Herdr.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[yuucu/herdr-hunk](https://github.com/yuucu/herdr-hunk)**

A lightweight Herdr plugin that brings interactive diff reviews into agent workspaces using fzf and the Hunk CLI. It lets you browse modified files and open side-by-side diff panes or tabs, optionally triggering automatically whenever an agent completes a run with uncommitted changes. For developers who want fast, keyboard-driven code review directly inside their Herdr sessions.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[Volpestyle/herdr-plugin-mermaid-preview](https://github.com/Volpestyle/herdr-plugin-mermaid-preview)**

Live Mermaid previews for Claude Code and Codex output in Herdr. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[CyPack/herdr-plugins](https://github.com/CyPack/herdr-plugins)**

File-manager plugins for the CyPack herdr fork: open spreadsheets, pictures, PDFs and text from the preview panel. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Zig](https://img.shields.io/badge/-555555?logo=zig&logoColor=white&style=flat-square) **[dannycroft/hunk-herdr-plugin](https://github.com/dannycroft/hunk-herdr-plugin)**

Herdr plugin for opening Hunk diffs in a split pane or tab. Written in Zig. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[cevr/herdr-hunk](https://github.com/cevr/herdr-hunk)**

Send Hunk review notes to the correct Herdr agent pane. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[caoer/ccc-herdr-layout](https://github.com/caoer/ccc-herdr-layout)**

Visual layout picker plugin for herdr — one key, live preview. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[devenjarvis/herdr-review](https://github.com/devenjarvis/herdr-review)**

A [herdr]( plugin that brings an **interactive plan-review** step. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[pi-dal/herdr-preview](https://github.com/pi-dal/herdr-preview)**

A diff-first Herdr review pane with safe Files-only browsing, comments, and image previews. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[alexarthurs/herdr-notes](https://github.com/alexarthurs/herdr-notes)**

Persistent markdown notes pane for herdr - one note per workspace, rendered preview + edit mode, autosaves and survives restarts. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[arvindparmar-me/herdr-markdown-viewer](https://github.com/arvindparmar-me/herdr-markdown-viewer)**

Herdr plugin: drag-select a markdown path and press prefix+m to preview it in a right-split pane. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Pane Navigation, Keymaps & Hints

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[yigitkonur/native-shortcuts-herd](https://github.com/yigitkonur/native-shortcuts-herd)**

Patches Ghostty and Herdr together so `cmd+t`, `cmd+n`, `cmd+w`, `cmd+1..9`, and tab cycling behave the way they do in Chrome or Safari — no manual escape-sequence wiring. It routes the keys through a Ghostty sidecar file (never touching your main config), maps them to the matching Herdr actions, and keeps timestamped backups plus a clean uninstall path. macOS only.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Taeyoung96/herdr-dotfiles](https://github.com/Taeyoung96/herdr-dotfiles)**

A drop-in Herdr `config.toml` built around prefix-free navigation: pane movement is mapped to bare `Shift+Alt+arrow` chords, the tmux-style prefix moves to `ctrl+space`, and it ships with the Catppuccin theme and a global agent panel. A one-command `install.sh` symlinks it in and backs up whatever was there — a clean, documented starting point for anyone who finds the default prefix-heavy bindings slow.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[JanTvrdik/herdr-command-palette](https://github.com/JanTvrdik/herdr-command-palette)**

Opens an `fzf` overlay listing every action exposed by every installed plugin, so you can fuzzy-search and invoke any of them without memorizing keybindings. It routes around the no-TTY constraint of plugin actions by spawning an overlay pane that carries the originating workspace's cwd, then tears down cleanly after selection. For users with many plugins who want a single `prefix+p` to reach any action.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[rmarganti/herdr-pluck](https://github.com/rmarganti/herdr-pluck)**

Mirrors tmux-fingers in Herdr: the bound key overlays one- and two-letter hints on every copyable token in the focused pane — URLs, paths, commit SHAs, UUIDs, IPs, Kubernetes refs, hex literals — and typing a hint copies that token to the clipboard, no mouse. A complement to herdr-fzf-url's URL-only scope. For anyone who copies long identifiers out of terminal output dozens of times a day.

![Zig](https://img.shields.io/badge/-555555?logo=zig&logoColor=white&style=flat-square) **[kamaaina/herdr_sync](https://github.com/kamaaina/herdr_sync)**

Type a command in your pane, then trigger the plugin action instead of Enter and herdr_sync sends the text to every other pane in the current tab at once — the synchronize-panes idea, rebuilt for Herdr in Zig. For users who need to run the same command across several concurrent agent or shell panes without copy-pasting across splits.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[twadams21/cc-controller](https://github.com/twadams21/cc-controller)**

Maps game-controller inputs (Switch Pro, Xbox, DualSense, or any SDL pad) to Herdr socket commands — switching workspaces, tabs, and panes, scrolling, and triggering voice mode without touching the keyboard. Works locally or with the controller on one machine and Herdr on another over SSH, dispatching every action through the socket so no OS-level input injection is needed. For developers who want hands-free navigation from a couch, a standing desk, or a headless remote box.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[Davidcreador/herdr-token-dashboard](https://github.com/Davidcreador/herdr-token-dashboard)**

A Bubble Tea dashboard that reads Pi session JSONL and the OpenCode server API to track live token spend, session cost, model, message count, and per-tool breakdowns across all active panes, refreshing every few seconds; when an agent goes done it fires a native Herdr toast with the cost and token summary. It falls back to disk-stored message files for completed OpenCode sessions. For Pi or OpenCode users who want spend visibility and finish alerts without leaving the workspace.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[astkaasa/herdr-tokscale-dashboard](https://github.com/astkaasa/herdr-tokscale-dashboard)**

Wires the Tokscale token/cost dashboard into Herdr as a split pane and a JSON-emitting quick action, without bundling or reimplementing Tokscale itself. For developers who already track spend with Tokscale and want it one keypress away.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[3mmdrew/herdr-layout](https://github.com/3mmdrew/herdr-layout)**

Defines declarative Herdr workspace layouts directly in pure Lua without external daemons or YAML boilerplate. It creates and splits panes with initial commands upon loading the configuration file. For developers who prefer lightweight, scriptable workspace definitions configured in Lua.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[a-curious-coder/herdr-plugin-manager](https://github.com/a-curious-coder/herdr-plugin-manager)**

A popup fzf-based TUI for discovering, installing, updating, and toggling Herdr plugins from within a running session. It connects to the public plugin registry topic on GitHub and ensures orphaned background daemons are terminated when a plugin is disabled. For Herdr users who want an interactive in-terminal interface for plugin discovery and lifecycle management.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[aclima01/herdr-todos-windows](https://github.com/aclima01/herdr-todos-windows)**

Renders a real-time task list panel on Windows that mirrors agent `TaskCreate` and `TaskUpdate` lifecycle events as they occur. It gives you a clear visual breakdown of each agent's planned execution stages and ongoing step status in a dedicated pane. For Windows developers who want live visibility into autonomous agent planning and progress.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[aliou/herdr-cast](https://github.com/aliou/herdr-cast)**

Bundles native macOS notifications for agent lifecycle events, fast fuzzy workspace jumping, zoxide-integrated workspace creation, and layout helpers into a single Herdr plugin. Streamlines the daily terminal loop between project navigation and agent monitoring. For macOS developers who want an all-in-one productivity enhancement pack for Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[AsgardMuninn/herdr-plugin-orbstack](https://github.com/AsgardMuninn/herdr-plugin-orbstack)**

Integrates OrbStack Linux virtual machines into Herdr by automatically provisioning and managing them as dedicated workspaces. It attaches directly through native shell execution with automated SSH fallback and keeps workspace states synchronized. For macOS developers who run isolated Linux container environments alongside their Herdr agent workflows.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[chantlong/herdr-habitat](https://github.com/chantlong/herdr-habitat)**

A living terminal habitat that runs in a Herdr pane and grows virtual plants and wildlife as your agents work and burn tokens. It turns background agent execution into a peaceful, evolving ecosystem while discouraging hyperactive "agentmaxxing." For developers who want ambient visual feedback and aesthetic warmth in their agent multiplexer. ---

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[devoc09/herdr-equalize-vsplit](https://github.com/devoc09/herdr-equalize-vsplit)**

A layout automation plugin for Herdr that splits the active pane vertically and instantly rebalances all column widths evenly. It calculates pane distribution via Herdr socket layout methods to avoid disproportionately squished panes when launching new agent splits. For developers who frequently split panes and want clean, balanced tiling with a single keystroke.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[gambtho/herdr-devcontainer](https://github.com/gambtho/herdr-devcontainer)**

Launches interactive shells and AI coding agents inside a repository's Dev Container via the official Dev Containers CLI. It bridges containerized development environments into native Herdr workspaces and panes without manual Docker or devcontainer CLI plumbing. For teams using Dev Containers who want container-isolated agent environments directly in Herdr.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[go-min/herdr-pane-name](https://github.com/go-min/herdr-pane-name)**

A Rust-based plugin that dynamically inspects active processes and agents to rename Herdr panes automatically. It replaces generic numerical pane identifiers with meaningful labels derived from currently executing commands or detected agent state. For operators managing busy workspaces with multiple simultaneous agents.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[hasuwini77/herdr-follow-cwd](https://github.com/hasuwini77/herdr-follow-cwd)**

Dynamically updates Herdr workspace labels to match the directory of the currently active pane. It features configurable path ceilings via its plugin configuration so top-level project boundaries are respected during deep subdirectory navigation. For developers managing multiple projects who want workspace names to reflect current working directories automatically.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[HexSleeves/herdr-warp](https://github.com/HexSleeves/herdr-warp)**

Bridges Herdr workspaces directly into native Warp terminal tabs and splits on macOS. It triggers Warp's native window controls to open and organize terminal panes aligned with your Herdr agent workspace structure. Perfect for Warp users who want native terminal features while driving background Herdr agent sessions.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[htlin222/herdr-gamepad](https://github.com/htlin222/herdr-gamepad)**

Maps gamepad and controller inputs to Herdr actions so you can navigate workspaces, inspect agent panes, and trigger splits from the couch. It uses macOS's GameController framework with customizable button bindings for Xbox, PlayStation, and 8BitDo controllers. For developers who want hands-free or lean-back monitoring of long-running agent tasks.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[jagzmz/herdr-s3-clipboard](https://github.com/jagzmz/herdr-s3-clipboard)**

A Herdr plugin that uploads clipboard screenshots directly to S3-compatible storage and pastes the resulting public or presigned URLs into the active pane. It eliminates manual image hosting when sharing UI mocks or error screenshots with multimodal coding agents. For developers prompting vision-capable agents with visual context inside Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[jeffarese/herdr-newtab-plus](https://github.com/jeffarese/herdr-newtab-plus)**

Replaces the standard new-tab shortcut with an interactive popup that autocompletes directories, surfaces frecent project folders, and prompts for an initial agent to launch. It automatically switches to existing workspaces when a target directory is already open. For developers frequently spinning up agent tabs across multiple projects.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[jugyo/herdr-nav-history](https://github.com/jugyo/herdr-nav-history)**

Adds browser-like back and forward focus navigation across your Herdr panes, tabs, and workspaces. It listens to focus transition events over the socket API to maintain a navigable history stack on dedicated keybindings. For developers navigating complex multi-workspace layouts who need to jump back to previously active contexts.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[KonstantinKai/herdr-harpoon](https://github.com/KonstantinKai/herdr-harpoon)**

A lightweight Harpoon port for Herdr that lets you bookmark frequently used panes and jump between them using numeric shortcuts. It requires no compilation or external runtime, managing marks through zero-dependency shell scripts and the Herdr CLI. For developers juggling multiple agent and editor panes who want fast, muscle-memory navigation across active splits.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[linuxing3/herdr-nnn](https://github.com/linuxing3/herdr-nnn)**

Integrates the nnn terminal file manager directly into Herdr splits and tabs. Uses a directory resolver script to automatically open nnn in the current focused pane's working directory. For developers who want fast keyboard-driven file navigation alongside running agents without leaving Herdr.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[maedana/herdr-hint](https://github.com/maedana/herdr-hint)**

Brings Vimium-style keyboard navigation to Herdr by overlaying single-letter hint tags across all active tabs and agent panes. Pressing the hint key instantly jumps focus to the target pane without cycling through split layouts. Built for keyboard-centric developers navigating dense multi-pane agent workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[malone-c/herdr-keybind-search](https://github.com/malone-c/herdr-keybind-search)**

An fzf-based overlay that parses your Herdr configuration to let you fuzzy-search and execute bound actions on demand. It eliminates the need to memorize complex key chords across heavily customized multi-agent setups. For Herdr users with extensive custom keymaps who want instant shortcut discoverability.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[marius-se/herdr-brainrot](https://github.com/marius-se/herdr-brainrot)**

Launches distraction apps and terminal games like DOOM in a dedicated Herdr pane while background coding agents run in neighboring splits. It supports pluggable terminal applications configured through its plugin manifest so you can pass time without switching away from your active workspace. For developers who want lightweight entertainment embedded alongside long-running agent tasks.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[markhuot/herdr-equalize-splits](https://github.com/markhuot/herdr-equalize-splits)**

Provides a quick keybinding (Ctrl+b =) to balance and equalize all split pane dimensions in the current Herdr tab row-by-row or column-by-column. Restores a clean, uniform layout after resizing or spawning multiple agent panes. For keyboard-driven Herdr users managing multi-pane agent workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[oullin/herdr-plugins](https://github.com/oullin/herdr-plugins)**

A collection of modular, independently installable plugins designed around standard Herdr plugin conventions and manifests. It provides focused utilities that enhance workspace navigation, agent awareness, and terminal workflows without bundle bloat. For power users looking for composable, single-purpose extensions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[qu8n/herdr-automatic-rename](https://github.com/qu8n/herdr-automatic-rename)**

Brings tmux-style automatic tab renaming to Herdr by dynamically updating tab labels with the active foreground process and icon. It also numbers workspaces, tabs, and agents with 1–9 prefixes for fast muscle-memory switching. For developers who want zero-friction visual orientation across many open panes.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[retroaalto/herdr-smartnav](https://github.com/retroaalto/herdr-smartnav)**

Adds geometric, direction-aware navigation across Herdr panes so you can move up, down, left, and right across complex grid layouts naturally. It calculates spatial pane boundaries rather than relying on linear cycle ordering, mimicking seamless window navigation. For power users managing dense multi-pane agent layouts who want intuitive directional navigation.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Sawakee/herdr-imebox](https://github.com/Sawakee/herdr-imebox)**

Opens an IME-friendly popup text box to input Japanese and CJK characters directly into Herdr agent panes without terminal encoding glitches. It intercepts multi-byte composition buffers and transmits finalized strings through the socket API. For multilingual developers interacting with AI coding agents in non-Latin scripts.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[shadowfax92/herdr-talon](https://github.com/shadowfax92/herdr-talon)**

Overlays spatial keyboard hints onto visible Herdr terminal targets so they can be triggered hands-free through the Talon voice-control system. It reads visible pane layouts and maps jump targets to spoken Talon phonetic labels. For developers using voice navigation who want quick, hands-free jumping between Herdr panes.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[speardragon/herdr-yazi](https://github.com/speardragon/herdr-yazi)**

Launches the Yazi terminal file manager inside a Herdr pane or tab focused on the current working directory. It reuses existing Yazi configurations and keeps the pane alive across file browsing sessions. For terminal power users who want rapid visual directory navigation beside their agents.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[StructuPath/herdr-guard](https://github.com/StructuPath/herdr-guard)**

Enforces cross-agent command safety policies across all active Herdr panes by auditing shell executions in real time. It intercepts destructive actions like force pushes, arbitrary base64 evaluation, and recursive deletions before they execute. Ideal for developers supervising autonomous coding agent fleets who need guardrails against destructive commands.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[tajdien/herdr-confirm-close](https://github.com/tajdien/herdr-confirm-close)**

Adds an interactive confirmation prompt before closing panes or tabs inside Herdr. It prevents accidental closures of long-running agent tasks by requiring explicit confirmation when triggering close keybindings. For developers running persistent or unattended agent runs who want safety guards against accidental keystrokes.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[WerrySs/herdr-cmux-cwd-sync](https://github.com/WerrySs/herdr-cmux-cwd-sync)**

A lightweight bridge that synchronizes the cmux terminal file explorer with the current working directory of whichever Herdr pane is actively focused. It observes pane focus transitions over Herdr's socket without modifying running shell sessions. For macOS developers running Herdr inside cmux who want their graphical file tree to follow their terminal navigation.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[wraithyy/herdr-hintr](https://github.com/wraithyy/herdr-hintr)**

A which-key style popup cheat sheet plugin that displays available Herdr keybindings and executes selected actions on keypress. Currently in active development and early prototyping. - **Rationale**: Valid Herdr-specific keybinding cheatsheet concept, properly categorized under Work in Progress per AGENTS.md guidelines.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ycros/herdr-compass](https://github.com/ycros/herdr-compass)**

A Python plugin that brings unified directional navigation across Herdr panes, tabs, and workspaces using consistent directional bindings. When navigation reaches the boundary of the current pane layout, it automatically wraps or steps to the adjacent tab or workspace. For keyboard-centric developers who want seamless spatial movement throughout their Herdr environment.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[yigitkg/herdr-open-local-paths](https://github.com/yigitkg/herdr-open-local-paths)**

Scans recent terminal output in the active pane to detect mentioned file and folder paths, opening them with default OS handlers or revealing them in file managers. If multiple paths are present, it presents a prioritized picker sorting files before folders. For developers working on Linux, Windows, or WSL who want quick navigation to agent-generated artifacts without manual path copying.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[yuk1ty/herdr-spreader](https://github.com/yuk1ty/herdr-spreader)**

Spins up entire Herdr workspace layouts—including tabs, splits, working directories, and startup commands—from a single YAML definition. It includes synchronization rules like waiting for output patterns before starting dependent panes. For developers migrating from tmuxinator or managing complex multi-service layouts.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[yuuta1219/herdr-gekiatsu-plugin](https://github.com/yuuta1219/herdr-gekiatsu-plugin)**

Gamifies Claude Code token consumption with a pachislot-style counter in the Herdr interface featuring jackpot animations and daily resets. It tracks token throughput across active agent panes and surfaces cost pacing in an entertaining visual format. For developers who want a playful way to monitor Claude Code usage during long coding sessions.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[oscabriel/pi-herdr-btw](https://github.com/oscabriel/pi-herdr-btw)**

pi install npm:pi-herdr-btw. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[benkraus/herdr-mobile](https://github.com/benkraus/herdr-mobile)**

Herdr Mobile is a native iOS and Android control surface for durable Herdr sessions. It connects to. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[petitviolet/herdr-plugins](https://github.com/petitviolet/herdr-plugins)**

Provides integration and dedicated functionality for herdr plugins in Herdr sessions. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[oyuk/herdr_plugin](https://github.com/oyuk/herdr_plugin)**

| Action | 説明 |. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[alastairsounds/herdr-plugins](https://github.com/alastairsounds/herdr-plugins)**

Plugins for [Herdr](. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[GroepOnline/herdr-plugins](https://github.com/GroepOnline/herdr-plugins)**

Mirrored from OnlineChefGroep/herdr-plugins (migrate fase5). Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[SeanRoberts/herdr-plugins](https://github.com/SeanRoberts/herdr-plugins)**

Plugins for herdr. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[lliwi/herdr-plugins](https://github.com/lliwi/herdr-plugins)**

My personal herdr plugins. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[aiki-sh/aiki-plugin-herdr](https://github.com/aiki-sh/aiki-plugin-herdr)**

Herdr plugin for Aiki. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[boooowy/herdr_plugins](https://github.com/boooowy/herdr_plugins)**

Provides integration and dedicated functionality for herdr_plugins in Herdr sessions. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[BlockedPath/herdr-plugin](https://github.com/BlockedPath/herdr-plugin)**

Provides integration and dedicated functionality for herdr plugin in Herdr sessions. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[michiomochi/herdr-plugin-sidenote](https://github.com/michiomochi/herdr-plugin-sidenote)**

herdr の母艦 space の右 pane に常駐する TUI プラグイン。各 space（workspace）の. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[amine2233/herdr-plugin-kanban](https://github.com/amine2233/herdr-plugin-kanban)**

Herdr plugin to use kanban. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[BryanHeBY/anolisa-herdr-plugin](https://github.com/BryanHeBY/anolisa-herdr-plugin)**

把 [ANOLISA]( 全家桶接入 herdr 终端工作区. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[m4salah/herdr-plugin-last](https://github.com/m4salah/herdr-plugin-last)**

tmux-style last-tab and last-workspace navigation for Herdr. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Tyru5/herdr-agent-state](https://github.com/Tyru5/herdr-agent-state)**

Realtime agent status pane for herdr; what each agent in the workspace is working on (in a more human-readable format). Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[aclima01/herdr-notify-windows](https://github.com/aclima01/herdr-notify-windows)**

Windows 11 toast notifications for herdr agents (turn finished / needs input). Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[mi2428/herdr-agent-layout](https://github.com/mi2428/herdr-agent-layout)**

herdr-agent-layout` keeps a supervising pane at a readable minimum width and arranges worker panes around it. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[yansfil/herdr-agent-context-labels](https://github.com/yansfil/herdr-agent-context-labels)**

Compact task summaries and runtime status for Herdr coding-agent panes. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[advaitbd/herdr-notify](https://github.com/advaitbd/herdr-notify)**

Herdr agent-status notifications via signed Hermes webhooks. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[spr-networks/spr-herdr](https://github.com/spr-networks/spr-herdr)**

Herdr TUI in an SPR-managed KVM microVM. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[amiramay/herdr-layout-cycle](https://github.com/amiramay/herdr-layout-cycle)**

herdr plugin: cycle through preset pane layouts, tmux prefix+space style. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[shadowfax92/herdr-layouts](https://github.com/shadowfax92/herdr-layouts)**

Tmux-style narrow pane splits and focused-pane equalization for Herdr. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[jmarcelomb/herdr-nav](https://github.com/jmarcelomb/herdr-nav)**

Pane, tab and workspace navigation plugin for herdr. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[iQua/herdr-flakes](https://github.com/iQua/herdr-flakes)**

Flakes plugin for Herdr — mirror and steer your Flakes runs in your local Herdr session. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[corrius/herdr-numbered-navigation](https://github.com/corrius/herdr-numbered-navigation)**

Deprecated: numbered navigation now lives in herdr-session-organizer v0.3.0+. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[jrswab/herdr-status](https://github.com/jrswab/herdr-status)**

Ambient machine status pane for Herdr on Linux. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[markbrutx/pif-herdr-reporter](https://github.com/markbrutx/pif-herdr-reporter)**

Herdr status reporter extension for the pif coding agent. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[jeph/herdr-pane-balancer](https://github.com/jeph/herdr-pane-balancer)**

Automatically balance, equalize, and tile Herdr terminal panes on create, close, and exit. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[Tetat-Chulchue/meadow](https://github.com/Tetat-Chulchue/meadow)**

Mouse-driven file explorer pane for the herdr terminal multiplexer. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[jlangston/herdr-clipboard](https://github.com/jlangston/herdr-clipboard)**

Clipboard history for the herdr terminal multiplexer — tmux prefix+= with images. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[RooseveltAdvisors/herdr-leap](https://github.com/RooseveltAdvisors/herdr-leap)**

EasyMotion/leap-style character jump + select-to-copy for the Herdr terminal multiplexer. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[supex0fan/herdr-claude-swap](https://github.com/supex0fan/herdr-claude-swap)**

Resume herdr's Claude Code panes under the claude-swap account that owns the session. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[kikyous/herdr-claude-usage](https://github.com/kikyous/herdr-claude-usage)**

Once herdr starts, the usage panel takes over a pane in the target workspace — click into that. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[tigorlazuardi/herdr-claude-retry](https://github.com/tigorlazuardi/herdr-claude-retry)**

Watches Claude CLI panes running inside [herdr]( When a pane hits Anthropic's. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[floco/herdr-claude-resume](https://github.com/floco/herdr-claude-resume)**

A herdr plugin that detects Claude Code's 5-hour rate limit and auto-resumes the session when it resets. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ViSHNUPrABU/herdr-codex](https://github.com/ViSHNUPrABU/herdr-codex)**

> unofficial · v1.3.0 · mit · not affiliated with herdr or anthropic. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[bestony/herdr-codex-capacity-retry](https://github.com/bestony/herdr-codex-capacity-retry)**

Make Codex in Herdr auto continue. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[jievince/herdr-codex-app](https://github.com/jievince/herdr-codex-app)**

Turn Herdr into a terminal-first Codex app: sync projects, resume chats. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[hrdle/hrdle](https://github.com/hrdle/hrdle)**

hrder web frontend tools. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[Howryann/herdr-monitor](https://github.com/Howryann/herdr-monitor)**

Read-only HTTP monitor for herdr agent status, with zero runtime dependencies. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) **[stappmus/Udder](https://github.com/stappmus/Udder)**

See your Herdr agents in the Omarchy bar, get notified when one finishes, and jump straight back to it. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[gadgj/agent-state-changed-bell](https://github.com/gadgj/agent-state-changed-bell)**

herdr plugin - agent state changed bell. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[milkyskies/herdr-attention](https://github.com/milkyskies/herdr-attention)**

A herdr plugin: one keypress jumps focus to the next agent that needs attention (blocked, then done). Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[zerkc/herdr-notify-firebase](https://github.com/zerkc/herdr-notify-firebase)**

Herdr plugin: FCM push on agent status changes. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[donghaolicd/herdr-teams-notify](https://github.com/donghaolicd/herdr-teams-notify)**

Herdr plugin for bounded Microsoft Teams agent lifecycle notifications. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[capt-marbles/herdr-jcode-integration](https://github.com/capt-marbles/herdr-jcode-integration)**

Herdr plugin for Jcode lifecycle state and session reporting. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[The-Dave-Stack/herdr-keymap](https://github.com/The-Dave-Stack/herdr-keymap)**

A herdr plugin: shows every keybinding in an overlay palette and runs the ones with a CLI equivalent. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[DMelisena/shipmates](https://github.com/DMelisena/shipmates)**

Hermes plugin for out of the box kun chen herdr opencode firstmate experience. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Command Palettes & Workspace Switchers

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[arjenblokzijl/herdr-launcher](https://github.com/arjenblokzijl/herdr-launcher)**

Defines named workflows as `.mjs` files, each declaring an arbitrary set of input fields and a `run()` function — filling the gap that single-input Quick Actions leaves open. The same workflows are reachable from a Herdr picker overlay or a plain `herdr-launcher run <name>` CLI call, so they fit interactive and scripted use alike. For teams who want config-as-code workflow menus without a dedicated dashboard.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mackt/herdr-window-title](https://github.com/mackt/herdr-window-title)**

Pushes dynamic, template-formatted session and agent states to the outer terminal window title. Mirrors tmux set-titles behavior to surface whether background agents are working, blocked, or done directly in your window manager or session picker. For developers juggling multiple Herdr windows who need clear external status indicators.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[phine-apps/mux-prompter](https://github.com/phine-apps/mux-prompter)**

An interactive prompt picker that scans local prompt collections and uses `fzf` to inject context-aware templates into the active Herdr pane. It eliminates repetitive manual prompt typing across parallel agent workflows without leaving the terminal. For developers who maintain reusable prompt libraries for coding agents.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[fullerzz/herdr-plugin-sesh](https://github.com/fullerzz/herdr-plugin-sesh)**

Sesh-style workspace picker TUI for Herdr. Integrates with zoxide to create workspaces from commonly used directories. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ramarivera/herdr-palette](https://github.com/ramarivera/herdr-palette)**

A Rust/Ratatui fuzzy command palette for Herdr workspaces. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[tomotochi/herdr-plugin-picker](https://github.com/tomotochi/herdr-plugin-picker)**

A Herdr file picker plugin that inserts selections from terminal browsers and search tools into the invoking pane. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[daltonkyemiller/herdr-plugin-switchboard](https://github.com/daltonkyemiller/herdr-plugin-switchboard)**

A focused Herdr plugin for one workflow. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[AnnanKhan/herdr-agent-launcher](https://github.com/AnnanKhan/herdr-agent-launcher)**

Clickable agent button pane for Herdr: left-click opens your configured agent, right-click drops down the rest. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ningxiaoxiao/herdr-agent-picker](https://github.com/ningxiaoxiao/herdr-agent-picker)**

Pick an AI agent and a working directory before herdr creates a new tab, split, or workspace. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[spro/herdr-agent-launcher](https://github.com/spro/herdr-agent-launcher)**

Open a new named tab running a specific Claude model. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) **[bkroeze/omherdr](https://github.com/bkroeze/omherdr)**

An Omarchy/Wayland Quickshell Herdr status launcher. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[lucasleon2107/herdr-claude-launcher](https://github.com/lucasleon2107/herdr-claude-launcher)**

herdr plugin: open a new tab with Claude Code already running. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[quinnjr/herdr-claude-profile](https://github.com/quinnjr/herdr-claude-profile)**

herdr plugin: switch and manage claude-profile profiles from an overlay palette. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Statuslines, Sidebars & Tab Sync

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync)**

Renames the active Herdr tab to match your Pi session name on resume or agent start, so you can tell what each tab is doing at a glance instead of decoding generic titles. It talks to the socket directly and only activates inside Herdr-managed panes, so it's safe to install globally and forget.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[liu-qingyuan/herdr-tmux-local-config](https://github.com/liu-qingyuan/herdr-tmux-local-config)**

A workstation dotfile stack that integrates Herdr, Codex hook scripts, and Oh My Tmux into a single shell setup — Codex hook scripts report agent state to Herdr's sidebar, and Oh My Tmux adds theming alongside. Ships installation scripts and documented merge steps for each component. For Codex users who want a pre-integrated Herdr config without assembling the pieces themselves.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[carsonjones/herdr-plugin-tiles](https://github.com/carsonjones/herdr-plugin-tiles)**

Adds six named split actions — 60/40 and 40/60 horizontals, 20/80 and 80/20 verticals, and 50/50 resets per axis — that override Herdr's default even split, with `shift` flipping which side is large and `alt` resetting to even. For users who routinely stage a sidebar or narrow reference pane and want consistent ratios without the mouse.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[rjyo/herdr-window-title-sync](https://github.com/rjyo/herdr-window-title-sync)**

A plugin that writes the focused workspace, tab, and agent name to the outer terminal window or tab title, pulling from pane metadata, agent status, or the most recent user prompt in local Codex/Claude Code session files as a fallback. Especially handy in terminals like Moshi that show session titles for quick reconnect. For Herdr users juggling many sessions who want at-a-glance context in their terminal chrome.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[fkiene/llmtrim-herdr](https://github.com/fkiene/llmtrim-herdr)**

Wires the llmtrim token-compression proxy into every Herdr pane on `workspace.created`, then pushes a compact savings badge into each pane's sidebar segment and exposes llmtrim's live TUI dashboard as a split. It reads llmtrim's own session data without extra API calls, and a routing check warns once if the proxy environment wasn't inherited. For users already running llmtrim who want token savings surfaced inside Herdr.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[alexjsp/herdr-scrollback-capture](https://github.com/alexjsp/herdr-scrollback-capture)**

Captures the focused pane's scrollback via `herdr pane read` and writes it to disk as a self-contained colored HTML file or plain text, with output directory, filename, and theme configurable. For anyone who wants to save an agent session transcript to share or archive.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[akhillb/herdr-attention](https://github.com/akhillb/herdr-attention)**

Docks a pane that counts down to your next calendar meeting and highlights when it's ten minutes away, pulling data through gcalcli and coloring itself to match your Herdr theme. For developers who want meeting awareness without leaving the terminal session.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[aiki-sh/aiki-integration-herdr](https://github.com/aiki-sh/aiki-integration-herdr)**

Opens a live-refreshing sidebar pane listing your in-flight aiki epics inside Herdr, and its install step bootstraps the companion aiki session-identity hook. For teams already using the aiki task tracker who want epic status visible alongside their agent panes.

---

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[4Born/herdr-pane-id-labeler](https://github.com/4Born/herdr-pane-id-labeler)**

Continuously synchronizes pane title labels with their canonical public pane identifiers like `w1:p2`. It listens to Herdr workspace and pane lifecycle events, automatically updating labels as panes are opened, split, or closed. Ideal for developers and orchestrator scripts that rely on predictable visual identifiers matching socket API addresses.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[aclima01/herdr-powershell-title-sync](https://github.com/aclima01/herdr-powershell-title-sync)**

Brings dynamic terminal title synchronization to Windows PowerShell hosts by updating the outer window title to match the focused Herdr workspace and agent state. It ports the behavior of Unix title synchronizers using native PowerShell console escape sequences and Herdr event listeners. For Windows developers managing multiple terminal windows who need immediate visual context in their taskbar and window tabs.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[bayoudhi/herdr-prayer-times](https://github.com/bayoudhi/herdr-prayer-times)**

Displays upcoming Islamic prayer times and a live countdown directly in the Herdr sidebar, complete with a keybound timetable popup and optional desktop alerts. It queries the Al Adhan API and caches prayer schedules locally to ensure reliable offline operation. For Muslim developers who want at-a-glance prayer schedules integrated into their terminal workspace.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[btorresgil/herdr-hermes-session-title](https://github.com/btorresgil/herdr-hermes-session-title)**

Reads Hermes Agent's local SQLite state to publish descriptive conversation titles into Herdr's agent sidebar. For users running Hermes Agent who want human-readable session names instead of generic identifiers. ---

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[cdc-lst/herdr-wait](https://github.com/cdc-lst/herdr-wait)**

Inspects the process tree of idle or blocked agent panes to automatically tag them with what they are waiting on, such as background builds or external CLI prompts. Overrides generic idle status with actionable labels like `waiting: build-api` or `waiting: codex` directly in the sidebar. For developers managing multiple parallel tasks who need immediate visibility into why a pane is paused.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[danbuhler/herdr-pane-topic-sync](https://github.com/danbuhler/herdr-pane-topic-sync)**

Automatically renames Herdr panes and tabs based on the active topic and terminal title emitted by agents like Claude Code or Codex. Tracks rename state locally to prevent update feedback loops and gracefully backs off when you manually rename a pane. Ideal for developers navigating dozens of numbered panes across complex tasks.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[davidolrik/herdr-titles](https://github.com/davidolrik/herdr-titles)**

Dynamically renames Herdr tabs and terminal windows using active foreground processes, live agent session titles, and workspace status counts rendered through HCL templates. Pairs with bash, zsh, and fish shell hooks while automatically preserving manually renamed tabs. For developers running multi-agent fleets who want expressive, glanceable window and tab titles.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[dev-shimada/herdr-auto-tab-name](https://github.com/dev-shimada/herdr-auto-tab-name)**

Automatically updates Herdr tab labels to match the active pane's current working directory as you navigate workspaces. It listens to Herdr lifecycle and focus events to refresh names dynamically, while preserving any tabs you have manually renamed. For developers running multi-project sessions who want self-labeling tabs without manual renaming.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[dnf0/herdr-llm-summary-header](https://github.com/dnf0/herdr-llm-summary-header)**

Listens for agent completion events and generates a concise one-line LLM summary of the executed work. Automatically writes the summary into the pane header so you can scan completed jobs across tabs without reading scrollback. For developers running parallel agent fleets who want instant visibility into finished tasks.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[eabadim/herdr-context-namer](https://github.com/eabadim/herdr-context-namer)**

Inspects active OpenCode session context inside Herdr panes and automatically renames tabs and workspaces to reflect current tasks. It queries the local agent context over the socket API to eliminate generic pane labels without manual renaming. For OpenCode users running multi-agent workspaces who want clear, self-updating tab titles.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[edouard-andrei/herdr-layout-tools](https://github.com/edouard-andrei/herdr-layout-tools)**

A layout management plugin that reshapes running panes into main-left or grid presets and equalizes split dimensions on the fly. It preserves existing pane IDs, tab IDs, and active processes during every layout reorganization so long-running agent tasks are never interrupted. For users who want flexible window tiling without killing or restarting sessions.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[elKei24/herdr-title-sync](https://github.com/elKei24/herdr-title-sync)**

Runs a lightweight daemon that reads dynamic OSC terminal titles emitted by coding agents like Claude Code and mirrors them to Herdr tab labels. It periodically reconciles tab and agent lists over the Herdr socket while maintaining single-instance safety via pidfile locking. For developers managing many parallel agent tabs who want immediate visual context without manual renaming.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[furuhashin/herdr-synchronize-panes](https://github.com/furuhashin/herdr-synchronize-panes)**

Broadcasts a single command to every pane across the current tab at once, mirroring tmux's synchronize-panes workflow. It provides a lightweight shell-driven plugin alternative for simultaneous multi-pane terminal control. For developers managing multiple shell sessions or agent panes that require synchronized commands.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[getpipher/herdr-sysmon](https://github.com/getpipher/herdr-sysmon)**

Ports classic tmux statusbar monitors into Herdr workspace tokens to display live CPU, memory, battery, network, and disk metrics directly in the sidebar. It updates efficiently on customizable intervals with macOS-optimized hardware probes. For developers running resource-intensive local models and compilation loops who want continuous visibility into host performance.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[iuhoay/herdr-break-pane](https://github.com/iuhoay/herdr-break-pane)**

Brings tmux-style pane breaking to Herdr by detaching the active pane into a fresh tab while preserving its running process and unzooming multi-pane tabs cleanly. Single-pane tabs are left untouched to prevent unnecessary tab churn. For users who want to promote an ad-hoc split into its own full tab.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[iurysza/herdr-tab-smart-rename](https://github.com/iurysza/herdr-tab-smart-rename)**

Uses lightweight LLM providers to inspect pane activity and automatically assign meaningful labels to your Herdr workspaces and tabs. It replaces generic tab numbers and directories with concise summaries of active tasks. For developers juggling many simultaneous projects and agent tabs in Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[kakigakki/herdr-auto-namer](https://github.com/kakigakki/herdr-auto-namer)**

Brings ChatGPT-style automatic naming to Herdr tabs and workspaces by assigning Claude Code session titles to agents and current directory names to workspaces. Keeps multi-agent terminal sessions clearly labeled without manual renaming commands. For developers running parallel Claude sessions across multiple projects who want clean workspace titles.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[malone-c/herdr-agent-smart-rename](https://github.com/malone-c/herdr-agent-smart-rename)**

Automatically renames Herdr panes and tabs based on the active task or prompt the agent is currently executing. Analyzes live terminal activity to replace generic session names with concise, descriptive summaries. For power users running multiple concurrent agent sessions who want effortless workspace clarity.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ndom91/herdr-ai-tab-name](https://github.com/ndom91/herdr-ai-tab-name)**

Uses a local LLM via Ollama to generate concise, descriptive names for Herdr tabs based on recent pane activity. Updates tab titles automatically as tasks change so you can navigate workspaces without deciphering generic numbered labels. For developers running multiple concurrent agent tasks who prefer self-hosted models for terminal metadata.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Numbered-com/herdr-ports](https://github.com/Numbered-com/herdr-ports)**

Monitors local network sockets and injects a dynamic `$ports` badge into the sidebar for any Herdr workspace running active TCP listeners. It inspects child processes and open listening ports so you can instantly verify which development servers or background services are live. For developers running web servers or API agents across multiple workspaces who want immediate port visibility.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[nytafar/herdr-cache-ttl](https://github.com/nytafar/herdr-cache-ttl)**

Displays a live countdown of prompt-cache TTL per agent pane with color-coded sidebar badges and threshold alerts. Includes a cache-sort action that reorders the agent panel by cache urgency to help prioritize warm sessions before expiry. For developers running multiple prompt-cached agent sessions who want to maximize token reuse.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[OliverGilan/herdr-jj](https://github.com/OliverGilan/herdr-jj)**

Adds Jujutsu version control integration to Herdr workspaces, fetching remotes and creating JJ workspaces directly from trunk revisions. It automates bookmark creation, surfaces live JJ change and status metadata in the Herdr sidebar, and triggers post-creation setup hooks. For developers using Jujutsu who want seamless VCS workspace switching and tracking inside Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[Only-Moon/herdr-nerd-font-tab-name-windows](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows)**

Adds contextual Nerd Font icons to Herdr tabs based on the active folder, project type, or running tool across Windows, macOS, and Linux. It automatically refreshes tab titles as you navigate directories, making dense multi-agent workspaces easy to distinguish at a glance. Tailored for developers working on Windows or across multiple operating systems.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[pjs-0457/herdr-yazi-explorer](https://github.com/pjs-0457/herdr-yazi-explorer)**

Spawns the Yazi terminal file manager inside a dedicated Herdr tab or split labeled with a folder icon, anchored to the active workspace directory. Automatically relaunches on exit so file browsing remains instantly accessible alongside running agents without manual restarts. For Herdr users who want fast, keyboard-driven file exploration inside their workspaces.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[playsthisgame/herdr-api-client](https://github.com/playsthisgame/herdr-api-client)**

Opens the ichigo TUI REST client in a dedicated split pane or tab, scoped to the current project's request collections. For developers testing API endpoints alongside running agent sessions. ---

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[Resetnak/herdr-logbook](https://github.com/Resetnak/herdr-logbook)**

An offline, Markdown-first TUI notebook and working-memory companion built with Bubble Tea for Herdr workspaces. It tracks active `now.md` task files, logs decisions without cloud or database dependencies, and generates activity heatmaps and standup summaries. For developers who need lightweight, structured note-taking and task memory tied to their Herdr sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[rohankewal/herdr-nerd-font-tab-name](https://github.com/rohankewal/herdr-nerd-font-tab-name)**

Ports tmux-nerd-font-window-name to Herdr to dynamically prepend Nerd Font icons to tab names based on running programs and directory context. Tab titles update automatically as panes switch between editors, shells, and agent processes. For users who want scannable, visual tab bars in complex multi-workspace sessions.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ropali/herdr-compose](https://github.com/ropali/herdr-compose)**

A standalone CLI and layout manager that defines Herdr workspaces, tabs, split directions, and startup commands in declarative YAML files. It supports active layout switching, starter templates, and visual hierarchy inspection from the terminal. For developers who want repeatable, version-controlled workspace configurations.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[sergeybataev/herdr-codex-session-title](https://github.com/sergeybataev/herdr-codex-session-title)**

Watches Codex session logs and dynamically updates Herdr agent labels to match the active conversation topic. It replaces generic numerical identifiers with descriptive task titles as the agent works. For developers running multiple Codex panes who want at-a-glance task context in the sidebar.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[szrenwei/herdr-space-tab-metadata](https://github.com/szrenwei/herdr-space-tab-metadata)**

Enriches the Herdr sidebar by displaying active tab labels and status indicators for each workspace at a glance. It listens to workspace and tab lifecycle events to maintain synchronized metadata without manual refreshing. For developers juggling multiple concurrent workspaces who need clear visibility into what each space is running.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[tmn73/herdr-claude-tab-title](https://github.com/tmn73/herdr-claude-tab-title)**

Hooks into Claude Code session events to automatically update Herdr tab titles with active task descriptions. Keeps multi-agent workspaces organized by replacing generic tab numbers with descriptive session summaries without manual intervention. For developers running multiple Claude Code sessions in parallel across separate tabs.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[toyamarinyon/herdr-thread-to-tab](https://github.com/toyamarinyon/herdr-thread-to-tab)**

Automatically renames single-pane Herdr tab labels to match the active thread titles generated by Claude Code or Codex. It reads session updates in the background and calls Herdr's tab rename socket API so you can identify tasks across dozens of tabs at a glance. For users running many parallel agent sessions who want meaningful tab titles without manually naming them.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[willfish/herdr-balance-panes](https://github.com/willfish/herdr-balance-panes)**

Restores equal dimensions to all panes in the active Herdr tab with a single keybinding, bringing tmux's `select-layout -E` behavior to Herdr. It calculates available terminal geometry and redistributes split ratios across active panes after repeated splitting. For users who frequently split panes and need a fast way to clean up cluttered layouts.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[winoooops/herdr-agent-title-sync](https://github.com/winoooops/herdr-agent-title-sync)**

Automatically synchronizes Herdr pane titles with active coding agents including Claude Code, Codex, Kimi Code, and OpenCode. Keeps pane headers updated as agents change tasks or switch roles across tabs. For users managing multi-agent grids who need clear visual orientation.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[wjarka/herdr-ghostty-tab-title](https://github.com/wjarka/herdr-ghostty-tab-title)**

Updates Ghostty terminal tab titles with color-coded counts of active, blocked, done, and idle agents across your workspaces. It watches Herdr agent state changes and writes escape sequences directly into the tab bar so you can check agent health at a glance without switching windows. For Ghostty users running background fleets who want passive visual status indicators.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[bcihanc/herdr-claude-session-title](https://github.com/bcihanc/herdr-claude-session-title)**

Herdr plugin: mirrors the Claude Code session title (/rename or auto summary) into the herdr pane metadata title. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[aarsh21/herdr-tab-title](https://github.com/aarsh21/herdr-tab-title)**

Automatic tmux-like tab titles for Herdr. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[wenhanweime/herdr-plugin-renamer](https://github.com/wenhanweime/herdr-plugin-renamer)**

LLM-powered session naming for herdr: Claude Code / Codex / Grok / Pi / opencode, Chinese or English tab labels, free opencode zen engine by default. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[lachieh/herdr-plugin-cmux](https://github.com/lachieh/herdr-plugin-cmux)**

Mirror every [herdr]( agent into the [cmux]( sidebar. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[rcosteira79/herdr-plugins](https://github.com/rcosteira79/herdr-plugins)**

Two independent herdr plugins: idle-shell-badge and readpending. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[cokekitten/pi-recap](https://github.com/cokekitten/pi-recap)**

Recent activity recap extension for Pi with optional session title and Herdr/tmux name sync. Standalone fork of @zhcsyncer/pi-recap with compact UI. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[bleedingfight/herdr-agent-manager](https://github.com/bleedingfight/herdr-agent-manager)**

一个基于fzf的模糊搜索workspace、tab、pane、agent工具. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[scaryrawr/herdr-agent-title](https://github.com/scaryrawr/herdr-agent-title)**

herdr agents in the window title. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Vistyy/pi-herdr-agents](https://github.com/Vistyy/pi-herdr-agents)**

Run owned Pi agents in Herdr tabs. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[the-inconvenience-store/herdr-agent-session-title](https://github.com/the-inconvenience-store/herdr-agent-session-title)**

Herdr plugin: mirrors the Claude Code or Codex session title (/rename or auto summary) into the herdr pane metadata title. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[adnichols/herdr-kitty-status](https://github.com/adnichols/herdr-kitty-status)**

Live Herdr agent status counts in Kitty tabs. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[carlotran4/waybar-herdr](https://github.com/carlotran4/waybar-herdr)**

Event-driven Herdr agent status module for Waybar. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[calebcauthon/herdr-theos-settler](https://github.com/calebcauthon/herdr-theos-settler)**

Settle Herdr agent tabs and workspaces below active work to get finished work out of the way. Theo's idea. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[tipok/herdr-layouts](https://github.com/tipok/herdr-layouts)**

A [herdr]( plugin that creates workspaces from declarative layout configuration files. Define your tabs, panes, split directions, and startup commands in TOML — the plugin builds the entire workspace in one shot. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[timaliev/herdr-layout](https://github.com/timaliev/herdr-layout)**

Declarative herdr session layouts — YAML-defined workspaces, tabs, panes. Session-aware, idempotent, startup auto-apply. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[phenome/herdr-layout](https://github.com/phenome/herdr-layout)**

Small Herdr plugin for three saved tab layouts. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[alex-devdone/raycast-herdr-status-bar](https://github.com/alex-devdone/raycast-herdr-status-bar)**

Raycast menu-bar extension showing **live AI coding agents** on this machine — how many, what type (claude/codex), their state (working / idle / blocked / done), plus per-agent token use and session runtime. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[yuhgo/herdr-tab-marker](https://github.com/yuhgo/herdr-tab-marker)**

Claude Code / Codex のタブに、作業内容から生成したタイトルとリポジトリごとの絵文字を自動で付ける herdr hook. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[jfdg01/herdr-claude-setup](https://github.com/jfdg01/herdr-claude-setup)**

My herdr terminal + Claude Code workflow (caveman/ponytail, statusline, autocompact, night-light), reproducible via setup.sh. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[allexborysov/herdr-claude-auto-title](https://github.com/allexborysov/herdr-claude-auto-title)**

Auto-generated session titles for [Herdr]( panes running Claude Code. Your first message in a session is summarized into a short kebab-case slug and shown in Herdr's agents sidebar. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[phillipleblanc/ad](https://github.com/phillipleblanc/ad)**

Agent dispatch CLI for messaging between local herdr agent tabs. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[TheMetalStorm/herdr-cline-plugin](https://github.com/TheMetalStorm/herdr-cline-plugin)**

Herdr plugin that makes a plain Cline CLI launched from any pane look like a native Herdr agent. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[mrcndz/herdr-routines](https://github.com/mrcndz/herdr-routines)**

Herdr plugin that runs scheduled routines: cron or interval schedules that open a tab in a workspace and run a command or launch an agent. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[MartinKei/herdr-tab-notes](https://github.com/MartinKei/herdr-tab-notes)**

Simple herdr plugin for taking notes. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[varelaseb/tabherd](https://github.com/varelaseb/tabherd)**

herdr plugin: agent pinning, color-coded session tabs, and collapsible workspace folders. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[QuantumDancer/herdr-last-tab](https://github.com/QuantumDancer/herdr-last-tab)**

Herdr plugin to switch to the last focussed tab. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[nmogil/agent-skill-patterns](https://github.com/nmogil/agent-skill-patterns)**

Portable Agent Skills patterns for Claude Code, Hermes, and Herdr workflows. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Status Overlays, HUDs & Agent Gauges

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[sohanemon/herdr-helpr](https://github.com/sohanemon/herdr-helpr)**

Adds keyboard-driven overlays for tasks Herdr doesn't expose by default: name a new workspace before it opens, rename the current one in place, and close every tab or pane except the focused one. Bindable as plugin actions in `config.toml` and installable from the marketplace. For Herdr users who manage many workspaces and want naming and cleanup without the mouse or a long command.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ArteenHD/herdr-cache-timer](https://github.com/ArteenHD/herdr-cache-timer)**

Tracks prompt cache windows for active LLM agents and displays real-time countdown timers directly in the Herdr sidebar. It alerts you before prompt caches expire so you can send follow-up requests within the active cache window to minimize latency and token costs. Essential for developers optimizing LLM spend across multiple agent panes.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay)**

A Linux-focused Rust plugin that monitors per-workspace CPU and memory consumption relative to total machine capacity. It updates live metrics in the background so you can identify resource-heavy agent panes before they throttle your system. For developers running concurrent multi-agent fleets on local hardware.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[happyeric77/agent-keep-awake](https://github.com/happyeric77/agent-keep-awake)**

Subscribes to Herdr socket events and invokes macOS caffeinate to keep your machine awake whenever any agent is actively working. Automatically releases sleep assertions as soon as all agents transition to idle, blocked, or done states. For macOS users running long unattended agent workflows who want to prevent interrupted jobs without disabling power management.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[iikjl/herdr-spotify](https://github.com/iikjl/herdr-spotify)**

Brings a Spotify now-playing overlay to Herdr on macOS, rendering album artwork via the Kitty graphics protocol alongside progress indicators and playback controls. It uses local AppleScript for zero-config playback and supports an optional Web API connection for search, queueing, and track-change toast notifications. For macOS developers who want integrated media controls without leaving their agent workspace.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[jeromychu23/herdr-popupx](https://github.com/jeromychu23/herdr-popupx)**

A Rust-based plugin that adds persistent native floating scratch popups to Herdr. It lets you toggle a floating terminal overlay on any keybind without disrupting your active tiled layout, keeping scratchpad context intact across workspace switches. For developers who want quick-access scratchpads alongside long-running agent panes.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[maro114510/herdr-toggle-popup](https://github.com/maro114510/herdr-toggle-popup)**

Toggles an overlay popup shell over your active Herdr session with a single keypress. Lets you run quick terminal tasks, check notes, or inspect plan files without reorganizing your agent panes or losing focus. For developers who want dedicated scratch space while monitoring running agents.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[mgh3326/scopefuel](https://github.com/mgh3326/scopefuel)**

A granular quota and headroom gauge that breaks down AI agent rate limits by account, model, and group. It clarifies exactly what is blocked and when quotas reset across 5-hour and weekly windows. Built for developers managing multi-model agent fleets across tight provider quotas.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[napalmpapalam/herdr-quotr](https://github.com/napalmpapalam/herdr-quotr)**

A popup overlay that captures recent agent responses from any pane, letting you select and quote specific snippets directly back to the agent. It eliminates tedious manual copy-pasting when refining instructions or challenging agent reasoning. Perfect for developers conducting iterative conversational tuning with Herdr agents.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[nwarwick/herdr-caffeinate](https://github.com/nwarwick/herdr-caffeinate)**

Maintains a macOS caffeinate assertion while any agent in Herdr is actively working, and automatically releases it after an idle grace period. For developers running long agent builds on Mac laptops without system sleep interruptions. ---

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[osamahbeig/herdr-pane-mover](https://github.com/osamahbeig/herdr-pane-mover)**

A clickable overlay menu for Herdr that lets you move, re-split, and swap panes across tabs and workspaces. Bridges the gap between keyboard-driven layout commands and visual layout management without requiring complex CLI invocations. For users who want fast, visual pane rearranging across complex workspace layouts.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[shadowfax92/herdr-scratch](https://github.com/shadowfax92/herdr-scratch)**

Provides a persistent, toggleable scratchpad overlay for individual Herdr panes backed by private background tmux sessions. It keeps temporary notes, REPL sessions, and side-commands tied to specific agent panes without cluttering the main workspace layout. For developers who need quick, context-isolated scratch areas while monitoring running agents.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[silverwolfdoc/herdr-usage-bar](https://github.com/silverwolfdoc/herdr-usage-bar)**

A compact bottom-docked usage bar that surfaces live token consumption, rate limit ceilings, and context-window meters for AI agents in Herdr. It keeps quota awareness always visible without consuming valuable pane real estate. Ideal for developers wanting unobtrusive tracking of model usage and costs during long agent runs.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[szrenwei/herdr-agent-metrics](https://github.com/szrenwei/herdr-agent-metrics)**

Tracks real-time context window usage and session token metrics across Claude Code, Codex, and TraeX instances running in Herdr panes. It reads agent status events and summarizes consumption statistics in a compact status overlay. For engineers managing token budgets across fleets of concurrent coding agents.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Tyru5/herdr-floax](https://github.com/Tyru5/herdr-floax)**

Adds a tmux-floax-style floating scratchpad popup shell that toggles over your current Herdr layout. Each workspace maintains its own persistent scratch session so quick commands and REPLs stay available without cluttering your pane layout. For developers who need disposable, toggleable terminal overlays without altering split geometry.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[zetlen/herdr-hud](https://github.com/zetlen/herdr-hud)**

Renders a floating HUD popup displaying live host, network, session, and agent metrics with a single keybinding. Allows customizing the layout dimensions and extending displayed telemetry through custom shell scripts. For developers managing remote or multi-agent sessions who need instant system context at a glance.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[senna-lang/herdr-agent-usage](https://github.com/senna-lang/herdr-agent-usage)**

Context meters and provider rate limits for agents running in Herdr. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[maedana/herdr-agents-status](https://github.com/maedana/herdr-agents-status)**

Always-on-top agent status overlay. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Yemeni/herdr-agent-timer](https://github.com/Yemeni/herdr-agent-timer)**

A Herdr plugin that alternates each agent's status label with its elapsed time. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[tomys22/herdr-agent-usage-plugin](https://github.com/tomys22/herdr-agent-usage-plugin)**

Display Claude, Codex, and Gemini API usage directly in Herdr. Keep track of session and weekly usage percentages and reset times at a glance in a split pane. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[speardragon/herdr-status-platform](https://github.com/speardragon/herdr-status-platform)**

Provides integration and dedicated functionality for herdr status platform in Herdr sessions. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ram4-dev/herdr-codex-usage](https://github.com/ram4-dev/herdr-codex-usage)**

Herdr plugin for installed-agent detection and usage quota visibility. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Output Inspection, Logs & Transcripts

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[x0d7x/herdr-fzf-url](https://github.com/x0d7x/herdr-fzf-url)**

Iterates every Herdr pane, captures visible content, extracts URLs by regex, deduplicates them, and pipes the list to `fzf` — Enter opens in a browser, `y` copies to the clipboard. A native-Herdr rewrite of tmux-fzf-url. For users whose agent or build panes emit URLs they'd rather not hunt for in scrollback.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[a-curious-coder/herdr-iris](https://github.com/a-curious-coder/herdr-iris)**

A context-aware cheatsheet plugin that inspects the active pane to detect the running agent and fuzzy-filters matching skills and rules from Claude `SKILL.md` and Cursor configurations. Selecting an entry automatically inserts the formatted invocation into the active pane for user confirmation. For developers working across multiple agent harnesses who want instant access to agent-specific skills.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[AkashJana18/herdr-scratch](https://github.com/AkashJana18/herdr-scratch)**

Persistent scratchpad panes you can toggle, focus, and hide without losing shells, notes, or REPL state across workspaces. It keeps dedicated utility panes scoped globally, per workspace, or per directory, persisting pane references in a versioned state registry. For developers who need temporary workspaces that stay alive in the background while switching tasks.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[Brutheron/Renderd](https://github.com/Brutheron/Renderd)**

Opens completed Claude Code and Codex responses in a scrollable side panel that updates live as the agent writes. It reads structured session files instead of terminal text to strip thinking blocks and format pure Markdown. For developers who want clean, readable agent output side-by-side with active sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[GranamyrBR/herdr-english-coach](https://github.com/GranamyrBR/herdr-english-coach)**

A Herdr plugin that turns a side pane into a live English and dev-jargon coaching board. As coding agents work, it logs grammar improvements and technical phrasing suggestions in real time. Ideal for non-native developers wanting continuous language polish alongside agent runs.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Hanyang-Li/herdr-espresso](https://github.com/Hanyang-Li/herdr-espresso)**

Subscribes to Herdr agent state transitions to keep your Mac awake whenever an agent in a monitored pane is actively working or blocked. It drives the macOS espresso power utility with near-zero idle CPU and automatically releases sleep assertions when tasks finish. For MacBook users running long coding jobs who want work to continue uninterrupted even with the lid closed.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[fredrikkvalvik/herdr-scratch](https://github.com/fredrikkvalvik/herdr-scratch)**

A throwaway shell floating over your herdr session. One key, a couple of commands, ctrl+d. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Astro](https://img.shields.io/badge/-555555?logo=astro&logoColor=white&style=flat-square) **[alanpcurrie/herdr-claude](https://github.com/alanpcurrie/herdr-claude)**

herdr claude demo output. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[johnlindquist/herdr-pane-update-timestamps](https://github.com/johnlindquist/herdr-pane-update-timestamps)**

Herdr plugin for timestamped, scrollable pane output observations. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Dotfiles & Drop-in Config Packs

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[ddfonseca/herdr-paste-image](https://github.com/ddfonseca/herdr-paste-image)**

Ports tmux-paste-image to Herdr, saving the clipboard's image to disk and pasting its file path directly into the active pane. It integrates with native OS clipboard utilities across macOS and Linux so multimodal agents can immediately reference screenshots and mockups without manual file saving. For developers providing visual context or bug screenshots to AI coding agents in the terminal.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[ogulcancelik/herdr-browser](https://github.com/ogulcancelik/herdr-browser)**

Renders a live, interactive Chromium browser session directly inside a Herdr pane using Kitty graphics protocol integration. Connects to agents via the Chrome DevTools Protocol so automated browser flows can be observed and steered with native keyboard and mouse input. For developers and AI agents requiring in-terminal web interaction and live visual automation feedback.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[poweroutlet2/herdr-confirm-close-pane](https://github.com/poweroutlet2/herdr-confirm-close-pane)**

Intercepts pane termination commands in Herdr to require confirmation before destroying a pane, mimicking tmux's confirm-before behavior. Prevents accidental closure of active agent runs and terminal tasks. - **Code Evidence & Technical Analysis:** Provides `herdr-plugin.toml` manifest defining `confirm-close-pane.confirm-close-pane` action bound to key combinations (e.g.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[multiplex-term/Multiplex](https://github.com/multiplex-term/Multiplex)**

An SSH / tmux / herdr terminal for Vision Pro and iPad. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[RestartDK/scatterer](https://github.com/RestartDK/scatterer)**

Personal herdr plugin config. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[crierr/herdr-tmux-layout](https://github.com/crierr/herdr-tmux-layout)**

tmux-style preset layouts for live Herdr panes: cycle, even-horizontal, even-vertical, main-horizontal, main-vertical, tiled, and balance. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[VinhLe1410/herdr-agent-priority](https://github.com/VinhLe1410/herdr-agent-priority)**

Herdr plugin for configurable agent status priority. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[masatokawano/to-herdr](https://github.com/masatokawano/to-herdr)**

zellij → herdr terminal setup migration (config + notes). Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[kogakure/dotfiles](https://github.com/kogakure/dotfiles)**

First, install the Xcode command-line tools. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[edmundmiller/herdr-plugin-dotfiles-dev-layout](https://github.com/edmundmiller/herdr-plugin-dotfiles-dev-layout)**

Herdr plugin for opening my dotfiles dev workspace layout. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[datalover37/dotfiles](https://github.com/datalover37/dotfiles)**

the configuration of dotfiles ghostty, zsh, herdr, opencode. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Angel-O/dotfiles](https://github.com/Angel-O/dotfiles)**

Modular chezmoi setup for Ghostty, Herdr, OpenCode, Starship, Zsh, and Git. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

### Terminal UX › Plugin Collections & Developer Frameworks

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[MIDO-ruby7/herdr-plugins-directory](https://github.com/MIDO-ruby7/herdr-plugins-directory)**

A link collection for finding herdr plugins by what you want to get done. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Newt6611/herdr-plugin-rust](https://github.com/Newt6611/herdr-plugin-rust)**

A Rust application framework for building Herdr plugins. Enhances terminal ergonomics with status monitors, keybindings, and custom layout presets.

[↑ Back to contents](#contents)

---

## Desktop apps & packaging

Native wrappers, status widgets, and install packages for Herdr.

### Desktop › Native GUI & Menu Bar Apps

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[hmu332233/herdr-menu-bar](https://github.com/hmu332233/herdr-menu-bar)**

A macOS menu-bar app that keeps your agents' states — working, idle, blocked, done — in the system status bar, so you don't have to keep the TUI on screen to know when one needs you. Agents are grouped by workspace in the dropdown, and clicking one can jump you straight to its pane. For Mac users running several agents who want ambient awareness without a foreground terminal.

![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square) **[re2zero/deepin-herdr](https://github.com/re2zero/deepin-herdr)**

A native Deepin Linux / UOS app (Qt + the DTK toolkit) that launches Herdr inside an embedded terminal window — on first run it fetches the binary, starts the server if needed, and drops you into the client with theme-matched colors. It ships as a proper `.deb` maintained by a UnionTech developer, the straightforward way onto Herdr for Deepin desktops. (No README yet; the Debian packaging is the documentation.)

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[re2zero/zenix](https://github.com/re2zero/zenix)**

A GPUI-native desktop app that wraps Herdr workspace, tab, and pane management with a live system-metrics sidebar (CPU, memory, network, disk), four built-in themes (Gruvbox, Solarized, Tokyo Night, Matrix), and CJK input support. Bundles the Herdr binary with PATH isolation to prevent version conflicts inside spawned sessions. For developers who want a richer desktop UI around Herdr than the bare terminal client, built on the same GPUI framework as Zed.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kcosr/herdr-web](https://github.com/kcosr/herdr-web)**

A React + Vite web UI for monitoring and controlling Herdr agents from any browser — desktop or mobile — over Herdr's socket API. Streams live pane state with terminal attachment, event subscriptions, and cross-client synchronization; a work-in-progress prototype with functional terminal attachment. For developers who want browser-based Herdr access without a native terminal, or a starting point for building their own remote client.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[alecuba16/herdr-webui](https://github.com/alecuba16/herdr-webui)**

A standalone browser UI that connects to a running Herdr backend over its JSON API and terminal-attach sockets, exposing workspace and worktree navigation, agent status, and live terminal interaction from any browser. Ships with macOS and Linux service helpers (install/start/stop/restart) for persistent background use. For developers who want a browser window into their Herdr session alongside the native terminal.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[dcolinmorgan/herdr-remote](https://github.com/dcolinmorgan/herdr-remote)**

A remote monitoring suite — a mobile-friendly web app (installable as a PWA, with Apple Watch notifications), a macOS menu-bar app, and a Telegram bot — that lets you watch live agent status and approve a blocked agent from your phone with one tap, routed through a zero-config Cloudflare tunnel so no SSH to the agent machine is required. The mobile UI shows a per-agent terminal view and yes/no/trust buttons, and auto-detects agent type for matching icons. Pairs with the herdr-push plugin that feeds it events. For developers who want to approve agents from a phone or watch.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[zackbart/herdr-ios](https://github.com/zackbart/herdr-ios)**

A native SwiftUI iOS app (TestFlight beta) that connects directly to a remote Herdr instance over SSH — speaking Herdr's JSON-RPC over an SSH exec channel — so live event subscriptions work from your phone with no relay or server-side component beyond SSH access. Covers workspaces, ANSI-stripped live scrollback, and a text input bar with quick-key extras; host keys are remembered on first connect. For iOS users who want a native phone client to browse workspaces and drive agents over an existing SSH connection.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[jgwesterlund/agent-view](https://github.com/jgwesterlund/agent-view)**

A cyberpunk pixel-art macOS app (built on Electrobun) where each running agent is a character in a neon shared office — working agents type at a holo-desk, blocked ones raise a hand, idle ones drift to the couch, and a cat named Daemon walks over to a blocked agent's desk if you ignore it. Double-clicking a character focuses its pane; the window is a frameless always-on-top widget. For Herdr users who want ambient agent awareness as a living scene rather than a status list.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[0cv/herdr-mobile-relay](https://github.com/0cv/herdr-mobile-relay)**

A mobile web app and relay service that lets you monitor Herdr agents and approve blocked actions from Android or iOS. It supports QR-code pairing, Cloudflare tunnels, push alerts, and multi-machine aggregation in a single dashboard. For developers who need to keep long-running agent workflows moving while away from their desks.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[alasano/house-of-herdr](https://github.com/alasano/house-of-herdr)**

Bridges Herdr agent telemetry to the Work Louder Codex Micro keypad, driving physical status LEDs, dials, and shortcut keys directly from active pane events. Gives tactile control over agent approvals and provides instant at-a-glance hardware status without checking terminal windows. For developers with dedicated macro hardware who want physical controls for agent fleets.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[bsorescu/herdr-mobile](https://github.com/bsorescu/herdr-mobile)**

A smartphone-tailored terminal UI that connects to your Herdr instance over SSH to inspect and steer AI coding agents from a mobile terminal. It formats agent status cards for narrow screens, filters scrollback, and exposes quick-action approval buttons without requiring a full desktop multiplexer view. For developers who want to unblock or monitor agents on the go without wrestling a full-width TUI.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[gabrielbarretoo/herdr-medieval](https://github.com/gabrielbarretoo/herdr-medieval)**

Renders your Herdr workspaces and panes as a 3D medieval continent using Three.js, mapping workspaces to encampments and panes to adventurers whose animations reflect agent status. Panes train, rest at campfires, or stand guard in towers depending on whether agents are working, idle, or blocked. For developers who want a playful, zero-dependency visual overview of their running agent fleet.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[matheus3301/herdr-phone](https://github.com/matheus3301/herdr-phone)**

A mobile remote console for Herdr that pairs a Go relay and embedded PWA with Cloudflare Tunnel and Access for secure smartphone control. Streams real-time agent status, lets you inspect active pane scrollback, and unblocks pending prompts from any mobile browser. For developers on the move who want remote supervision without exposing SSH ports or opening firewalls.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[osuki-dev/muqun-gateway](https://github.com/osuki-dev/muqun-gateway)**

A local-first, zero-cloud gateway daemon that connects Herdr sessions directly to the Muqun mobile companion app over encrypted peer-to-peer channels. Lets you inspect agent outputs, approve blocked turns, and issue prompts from your phone without third-party servers or accounts. For developers who want private, remote mobile oversight of their local agent terminal.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Pimpmuckl/herdr-streamdeck](https://github.com/Pimpmuckl/herdr-streamdeck)**

Brings tactile triage and fleet control to the Elgato Stream Deck+, mapping LCD keys, touch strips, and rotary dials to live Herdr agent states. You can pin attention-demanding threads, jump directly to active panes with a single tap, and monitor status colors at a glance. For developers with a Stream Deck+ who want hardware-level oversight of parallel agent runs.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[tigorlazuardi/herdr-web-tui](https://github.com/tigorlazuardi/herdr-web-tui)**

A lightweight browser and progressive web app frontend for daemon-mode Herdr instances. It brings terminal viewing, pane navigation, and plugin launching into any mobile or desktop web browser. For developers who want to check and drive their agent sessions from tablets, phones, or remote machines.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[Unayung/herdr-watch](https://github.com/Unayung/herdr-watch)**

A native Apple Watch companion app that displays real-time agent activity and status alerts directly on your wrist. It connects to Herdr to notify you when coding agents finish tasks or get blocked waiting for input. For developers who step away from their desk while long-running agent workflows execute.

![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square) **[walcew/herdr-assist](https://github.com/walcew/herdr-assist)**

A physical desk companion device powered by an ESP32-S3 and LVGL that displays Herdr session statuses on a color screen. It chimes an audible bell whenever an agent blocks on a user decision or approval request, preventing workflows from stalling unnoticed. For developers running long agent jobs who want hardware ambient feedback while away from their screen.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[joeseesun/herdr-guide](https://github.com/joeseesun/herdr-guide)**

Herdr 软件全面调研、使用价值分析与上手教程 | An independent practical guide to Herdr. Brings real-time agent status indicators and interactive controls to the desktop environment.

![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) **[cxnmai/dms-herdr-plugin](https://github.com/cxnmai/dms-herdr-plugin)**

DankMaterialShell widget for monitoring and controlling Herdr agents. Brings real-time agent status indicators and interactive controls to the desktop environment.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[sunnoy/livis](https://github.com/sunnoy/livis)**

在手机上盯着自己主机上跑的编码 agent —— 自托管的 Android 终端客户端，SSH/Mosh + herdr/tmux，agent 审批直推手机. Brings real-time agent status indicators and interactive controls to the desktop environment.

![QML](https://img.shields.io/badge/-555555?logo=qt&logoColor=white&style=flat-square) **[spencerbull/xeneon-edge-agents](https://github.com/spencerbull/xeneon-edge-agents)**

A fail-closed Omarchy and Herdr agent command center for the Corsair XENEON EDGE. Brings real-time agent status indicators and interactive controls to the desktop environment.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[A1exthegreat/herdr-agent-notify](https://github.com/A1exthegreat/herdr-agent-notify)**

Herdr plugin: desktop notifications when agents finish working, need confirmation, or go idle. Brings real-time agent status indicators and interactive controls to the desktop environment.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[TianZuo555/pi-herdr-agents](https://github.com/TianZuo555/pi-herdr-agents)**

Pi extension for role-guided peer coding agents in Herdr panes. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Java](https://img.shields.io/badge/-555555?logo=openjdk&logoColor=white&style=flat-square) **[mohamed-essam/herdr-mobile](https://github.com/mohamed-essam/herdr-mobile)**

Monitor and unblock your herdr agents from an Android phone — Go companion daemon + Kotlin/Compose app. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Tatendaz/herdr-launcher](https://github.com/Tatendaz/herdr-launcher)**

Unofficial macOS Dock launcher for the herdr TUI: click the ram, get herdr in your terminal. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[hbacheller-tribe/herdrStatusWidget](https://github.com/hbacheller-tribe/herdrStatusWidget)**

A widget for Herdr that shows which tabs need approvals. Brings real-time agent status indicators and interactive controls to the desktop environment.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[leset0ng/pi-todo-herdr](https://github.com/leset0ng/pi-todo-herdr)**

Hierarchical task tools for Pi with a live widget and Herdr sidebar integration. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[cedrus-8864/herdr-prompt-reply](https://github.com/cedrus-8864/herdr-prompt-reply)**

Answer herdr agent permission prompts straight from a macOS notification — real answer buttons, single Swift binary, nothing waiting in the background. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[richardadonnell/herdr-claude-manager](https://github.com/richardadonnell/herdr-claude-manager)**

Tile a Herdr workspace with N Claude Code panes, then list, resume, or kill it from one menu. PowerShell on Windows, bash on macOS and Linux. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[undivisible/herdr-gui](https://github.com/undivisible/herdr-gui)**

a gui surface for herdr + more. built with crepuscular gpui. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[yigitkonur/herdr-wezterm-setup](https://github.com/yigitkonur/herdr-wezterm-setup)**

My macOS terminal setup: herdr multiplexer + WezTerm as keyboard router. Brings real-time agent status indicators and interactive controls to the desktop environment.

![HTML](https://img.shields.io/badge/-555555?logo=html5&logoColor=white&style=flat-square) **[DavidTWhitlatch/dotfiles-template](https://github.com/DavidTWhitlatch/dotfiles-template)**

Shareable macOS dotfiles: zsh + oh-my-zsh, oh-my-posh prompt, herdr multiplexer, git template hooks. Based on thoughtbot/dotfiles. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[skeletor-js/bessie](https://github.com/skeletor-js/bessie)**

Native macOS client for Herdr. Brings real-time agent status indicators and interactive controls to the desktop environment.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[KaminariOS/whip](https://github.com/KaminariOS/whip)**

Keep whipping AI agents at home painlessly while you are traveling the world. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[miiraheart/herdr-beads](https://github.com/miiraheart/herdr-beads)**

A beads (bd) task board for herdr: List, Table, Kanban over your bd issues, docked as a sidebar or floating. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[zerodice0/herdr-booking-task-plugin](https://github.com/zerodice0/herdr-booking-task-plugin)**

Schedule Herdr agent prompts and local CLI commands on macOS and Linux. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[calorie/herdr-auto-focus](https://github.com/calorie/herdr-auto-focus)**

Focus Herdr agents that need attention after macOS input becomes idle. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[quinnjr/herdr-notifications](https://github.com/quinnjr/herdr-notifications)**

Native OS desktop notifications for herdr agent status changes (Linux, macOS, Windows, BSD). Brings real-time agent status indicators and interactive controls to the desktop environment.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[AlexBSoD/qubeherd](https://github.com/AlexBSoD/qubeherd)**

Push herdr agent state, host clock and keyboard layout to an Ergohaven Qube dongle screen. Brings real-time agent status indicators and interactive controls to the desktop environment.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[neefrehman/herdr-caffeinate](https://github.com/neefrehman/herdr-caffeinate)**

Keeps macOS awake (even with the lid closed) while any herdr agent pane is working. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[8-BitRhyon/bantay-tui](https://github.com/8-BitRhyon/bantay-tui)**

Native macOS notch HUD for herdr agent status — approvals, live usage/cost, a NotchDrop-style shelf, Barrie-style tasks with Apple Reminders sync, and a real-time control plane. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[omerturhan/herdr-touchbar](https://github.com/omerturhan/herdr-touchbar)**

Shows working and blocked herdr agents on the MacBook Touch Bar; tap one to jump straight to its tab. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[afogel/shepherdr](https://github.com/afogel/shepherdr)**

Shepherd delegated coding agents into visible, auditable herdr panes you can watch, resume, and take over — a herdr plugin. Brings real-time agent status indicators and interactive controls to the desktop environment.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[maxto/dotfiles](https://github.com/maxto/dotfiles)**

Personal WSL2 (Windows 11) human-AI terminal dev environment: herdr + broot + micro + shell, with a symlink installer and a herdr layout preset. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Dart](https://img.shields.io/badge/-555555?logo=dart&logoColor=white&style=flat-square) **[ablause/herdr-flutter](https://github.com/ablause/herdr-flutter)**

A herdr sidebar to watch, hot reload and inspect a running Flutter app beside the coding agent. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[aorumbayev/herdr-ctx](https://github.com/aorumbayev/herdr-ctx)**

Claude context-window indicator for herdr sidebar panes. Provides streamlined installation recipes and automated environment provisioning for Herdr.

[↑ Back to contents](#contents)

### Desktop › Web Dashboards & Remote Viewers

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[aviz85/herdr-controller](https://github.com/aviz85/herdr-controller)**

A Next.js dashboard in front of a running Herdr instance — live agent grid over SSE, terminal mirror, message box, and agent spawn — plus a first-person 3D office mode where each agent is a character at a desk with working/idle/blocked/done animations and a speech bubble of its last message (shoot a character three times to close its pane). The server talks to Herdr only through the CLI, so it runs on the same machine with no extra backend. For developers who want a visual web dashboard to supervise their fleet.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[AltanS/collie](https://github.com/AltanS/collie)**

A Herdr plugin plus Bun/TypeScript bridge that serves a PWA over your Tailscale network, so you can check which agent needs you and reply from your phone's own keyboard instead of SSHing in and wrestling a TUI. It mirrors each pane in color and adds a slash-command palette and a special-keys pad. Built for a single operator on one tailnet — served privately, never the public internet.

---

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[hmu332233/herdr-f1](https://github.com/hmu332233/herdr-f1)**

Visualizes your fleet of active Herdr agents as cars on an F1 racing circuit, updating positions and pit-stop statuses based on real-time agent activity. Offers a playful yet immediately readable web dashboard to track which agents are running, blocked, or finished. For developers who want an engaging visual overview of agent progress across their workspaces.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[mejiasd3v/herdr-farm](https://github.com/mejiasd3v/herdr-farm)**

Renders your Herdr workspaces and running agents as interactive livestock in a 3D Three.js farm world. Live agent states like idle, working, and blocked map directly to animal animations in the browser. Designed for developers who want a playful, gamified visual overview of their multi-agent workflows.

[↑ Back to contents](#contents)

### Packaging › Package Managers & Flakes

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[timvdhoorn/stream-deck-herdr-plugin](https://github.com/timvdhoorn/stream-deck-herdr-plugin)**

An Elgato Stream Deck plugin that assigns one physical key per agent, encoding status as color and glyph (orange working, red blocked, green done, grey idle) so you read your fleet at a glance. Pressing a key runs `herdr agent focus` and raises the terminal; a morphing pager key cycles through agents that need attention. Tested on the 6-key Mini. For Stream Deck users who want hardware-backed ambient awareness and one-press pane focus.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[zhongpei/herdr-ulanzi-deck](https://github.com/zhongpei/herdr-ulanzi-deck)**

Pushes live agent status to the LCD keys of a Ulanzi D200X macro keypad, with brand-color-coded per-agent displays, priority sorting (blocked first), and support for multiple Herdr instances on different machines over SSH. A three-process design separates state polling from display rendering so the keypad only redraws on actual state changes. For developers with a Ulanzi D200X who want a physical status panel for a multi-machine fleet.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[allmight-ai/herdr-pet](https://github.com/allmight-ai/herdr-pet)**

A retro 1-bit virtual pet companion that connects to Herdr's socket API and animates based on your coding agents' real-time states and tasks. Generates a persistent, deterministic pet species and personality seeded from your GitHub ID. For developers who want a playful, ambient visual monitor for their background AI agents.

![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square) **[bowlofsoup/herdr-stoplight](https://github.com/bowlofsoup/herdr-stoplight)**

Controls a physical Arduino traffic light module in real time based on the execution status of Herdr agents. Illuminates green when working, red when blocked or errored, and yellow when idle. For developers who want a tangible hardware status indicator on their desk.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[dio16/herdr-auto-update](https://github.com/dio16/herdr-auto-update)**

A startup plugin that checks all installed Herdr plugins against their upstream repositories and automatically reinstalls any with new commits. It ensures your plugin environment stays up to date without manual git pulls. For power users running multi-plugin setups who want hands-off updates.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[gw31415/herdr-amphetamine-macos](https://github.com/gw31415/herdr-amphetamine-macos)**

Monitors Herdr agent status events and keeps extending active Amphetamine sessions on macOS whenever coding agents are busy. Prevents the system from sleeping during long-running agent tasks without requiring manual session management. - **Code Evidence & Technical Analysis:** Implements a Python daemon and `herdr-plugin.toml` subscribing to Herdr `pane.agent_status_changed` / `events.subscribe` events, bridging active agent state to macOS Amphetamine keep-awake triggers.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ragamo/herdr-flock](https://github.com/ragamo/herdr-flock)**

Transforms your active Herdr agents into pixel-art sheep grazing on a procedural top-down farm, reflecting live agent states through sheep animations. When an agent session completes, its sheep moves to a persistent graveyard log, complete with clickable inspect tooltips and weather effects. For developers who want a playful, gamified overview of their running agent fleet.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[speardragon/herdr-plugin-manager](https://github.com/speardragon/herdr-plugin-manager)**

A lightweight popup interface to browse, install, update, and toggle Herdr plugins without leaving your active pane. It wraps the native plugin CLI with a zero-dependency menu bound to a single keypress like prefix+p. For users who frequently test and manage community plugins directly within the terminal.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[suisya-systems/herdr-agent-office](https://github.com/suisya-systems/herdr-agent-office)**

Renders active agent panes as characters at desks in a terminal pixel-art office, animating them based on native status events like working, idle, or blocked. Stuck agents raise speech-bubble alerts with escalating timers, and pressing Enter jumps focus directly to their pane. For developers running multi-agent fleets who want visual status tracking without leaving the terminal.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[third774/herdr-sidepulse](https://github.com/third774/herdr-sidepulse)**

Drives SidePulse Pro and SidePulse Dot USB hardware devices to display ambient LED status for all active Herdr agents. It aggregates agent states across workspaces to show high-priority patterns like amber heartbeats for blocked agents needing input and cyan pulses for active work. For developers who want peripheral, desk-level awareness of their agent fleet without checking a screen.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[Yassimba/loom](https://github.com/Yassimba/loom)**

Curated agent skills, Pi packages, and Herdr plugins with one setup CLI. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ezcorp-org/herdr-git-status](https://github.com/ezcorp-org/herdr-git-status)**

herdr plugin: per-space git working-tree status (staged/modified/untracked/conflicts) in the sidebar, next to the branch. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[miya10kei/herdr-plugin-sidebar](https://github.com/miya10kei/herdr-plugin-sidebar)**

Googleカレンダーの予定とGitHub Actionsの実行状況を、サイドバー風のsplitペインに表示する [herdr]( プラグイン。. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[khatriafaz/herdr-plugin-agent-repo](https://github.com/khatriafaz/herdr-plugin-agent-repo)**

Herdr plugin that shows agent, repository, and branch names in agent pane headers and the sidebar. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[levi-qiao/herdr-agent-quota](https://github.com/levi-qiao/herdr-agent-quota)**

Never hit a quota limit mid-task: see Claude, Codex, Grok and Agy usage live in your Herdr sidebar. 5h and weekly percent remaining. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ondratuma/herdr-status-plugin](https://github.com/ondratuma/herdr-status-plugin)**

Per-pane activity status for herdr agent panes — sidebar icon + live timer showing what each agent pane is doing, plus a pane-rename helper. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[cedrus-8864/herdr-sidebar-numbers](https://github.com/cedrus-8864/herdr-sidebar-numbers)**

herdr plugin: show workspace and agent position numbers in the sidebar, matching the 1..9 shortcut digits. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Coolsik/herdr-codex-cost](https://github.com/Coolsik/herdr-codex-cost)**

Show estimated Codex session cost in the Herdr sidebar. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[samuelbaldwin05/herdr-burn](https://github.com/samuelbaldwin05/herdr-burn)**

Live Claude Code cost/quota per pane in the herdr sidebar, with a workspace-total burn overlay. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[tyler-jewell/herdr-bootstrap](https://github.com/tyler-jewell/herdr-bootstrap)**

Idempotent machine bootstrap for Herdr + Node/ Grok + herdr agent skill. Provides streamlined installation recipes and automated environment provisioning for Herdr.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[mougua/herdr-reasonix](https://github.com/mougua/herdr-reasonix)**

Herdr plugin for detecting and displaying Reasonix agents. Provides streamlined installation recipes and automated environment provisioning for Herdr.

[↑ Back to contents](#contents)

### Packaging › Version Managers (mise, vfox)

![Nix](https://img.shields.io/badge/-555555?logo=nixos&logoColor=white&style=flat-square) **[AodhanHayter/herdr-nix](https://github.com/AodhanHayter/herdr-nix)**

A Nix flake that packages the Herdr CLI for macOS and Linux (Intel and ARM), so you can `nix run` it or wire it into a NixOS overlay or Home Manager config instead of reaching for Homebrew. An hourly GitHub Action watches upstream releases and bumps the version, hashes, and a public Cachix binary cache automatically — so the flake tracks Herdr with no manual upkeep. The canonical path for anyone on a declarative Nix setup.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[lachieh/vfox-herdr](https://github.com/lachieh/vfox-herdr)**

A mise/vfox plugin for installing Herdr that verifies every download against GitHub's published SHA256 digest, supports preview builds via `herdr@preview`, and generates shell completions for bash, zsh, and fish that include live session data. Solves two gaps in Herdr's own self-updater: preview-channel access and completion scripts with dynamic data. For developers on declarative package setups who want versioned, verified Herdr installs outside Homebrew.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[funsaized/herdr-mise](https://github.com/funsaized/herdr-mise)**

Visualizes running Herdr agents as pixel-art line cooks managing tickets and preparing dishes across interactive kitchen stations. Subscribes to Herdr socket events to animate agent actions, tool executions, and blocked states in real time. For developers who want playful ambient awareness of multi-agent workloads on a side monitor.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[natori-hrj/herdr-lazy](https://github.com/natori-hrj/herdr-lazy)**

Brings declarative, lockfile-backed plugin management to Herdr with a dedicated TUI management pane. It syncs plugins from a single list, pins versions to tags or commits, and fetches prebuilt binaries. For developers wanting reproducible Herdr plugin setups across multiple machines.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[chrisjohnson/asdf-herdr](https://github.com/chrisjohnson/asdf-herdr)**

herdr plugin for the asdf version manager. Provides streamlined installation recipes and automated environment provisioning for Herdr.

[↑ Back to contents](#contents)

---

## Work in progress

Scaffolded or announced repos exploring ideas that are not yet daily-driver ready.

### WIP › Experiments, Concepts & Scaffolds

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[rbb/herdr-cursor](https://github.com/rbb/herdr-cursor)**

A planned shim around the Cursor SDK runtime that would report a Cursor agent's idle / working / blocked state back to Herdr, so a Cursor session shows up in your status sidebar like any native agent. Design-stage as of 2026-05 — the repo is a detailed spec with no code written yet, but the integration it sketches is a clean one to watch.

![YAML](https://img.shields.io/badge/-555555?logo=yaml&logoColor=white&style=flat-square) **[shippy/raycast-herdr](https://github.com/shippy/raycast-herdr)**

A Raycast extension meant to add Herdr control commands to Raycast. As of mid-2026 only the build-and-publish workflow is wired up; the `extensions/` directory is still an empty scaffold.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[SuperInstance/herdr-cocapn](https://github.com/SuperInstance/herdr-cocapn)**

A Herdr fork that adds a fleet-management layer on top of CoCapn: each agent pane becomes a tiered "device," and deadband monitors auto-escalate work to a cloud agent under load, then de-escalate to save cost when it goes idle, with a crossfade handoff so nothing drops mid-transition. A genuinely novel idea — but not buildable as shipped, since its `cocapn-core` dependency is referenced by a hardcoded local path rather than bundled.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[rohanthewiz/herdr-web](https://github.com/rohanthewiz/herdr-web)**

An alpha web client that streams Herdr pane frames to the browser with color decode, mouse capture, clipboard, and OSC-8 hyperlinks all validated against a live server. The one blocking gap: the browser→Herdr keyboard and paste path is coded but gated off, so the client is effectively read-only for now — promising as a viewer, not yet a controller.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[Matovidlo/herdr-pr-tracker](https://github.com/Matovidlo/herdr-pr-tracker)**

A polling PR-status board that tracks the GitHub PR each Claude Code session produces using only the `herdr` CLI and `gh`. The idea is solid, but the install instructions still carry an unfilled `<you>` placeholder and the plugin namespace doesn't match the repo owner — not yet finalized for public install.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[makyinmars/muster](https://github.com/makyinmars/muster)**

A planned native macOS command center for coding agents powered by Herdr and Ghostty. As of mid-2026 the repo is an architecture-and-product scaffold — detailed design docs across several markdown files, but no Swift source or build yet. One to watch once an implementation lands.

---

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[eliasstravik/herdr-call](https://github.com/eliasstravik/herdr-call)**

A voice control interface designed to translate spoken commands into Herdr navigation and input actions. Early in development and exploring hands-free agent steering over the local socket. - **Code Evidence**: TypeScript repository prototyping audio capture and dispatching transcribed commands to Herdr's Unix domain socket; currently in active scaffold/design stage.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[hmu332233/herdr-plugins-labs](https://github.com/hmu332233/herdr-plugins-labs)**

An experimental incubator testing candidate Herdr plugins before they graduate into standalone repositories. Includes prototypes for quick agent launching, workspace status metrics, and worktree symlinking. For developers wanting early access to experimental Herdr multiplexer extensions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[malone-c/herdr-pane-balancer](https://github.com/malone-c/herdr-pane-balancer)**

An automatic layout manager in development that dynamically re-balances pane proportions across a tab whenever splits are opened or closed. It aims to prevent nested splits from squeezing existing panes into unreadable viewports. For users who frequently split and collapse panes across multi-agent workflows.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[meerzulee/herdr-float](https://github.com/meerzulee/herdr-float)**

A scaffolded Herdr plugin exploring Zellij-inspired floating pane overlays toggled via Alt+F. It aims to provide quick floating terminal overlays for short commands without modifying the underlying pane grid. Note: in early development and not yet feature-complete.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[shoaibkhanz/herdr-nav-plus](https://github.com/shoaibkhanz/herdr-nav-plus)**

Adds seamless `Ctrl+h/j/k/l` directional navigation across Herdr panes that wraps at workspace boundaries. Designed for vim users who want uninterrupted keyboard movement across their entire workspace layout. Currently in early scaffold and design stage.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[ugurtarlig/herdr-pane-picker](https://github.com/ugurtarlig/herdr-pane-picker)**

Overlays one-character jump hints on visible Herdr panes for instant keyboard-driven focus switching. Designed to streamline rapid pane navigation in complex multi-pane layouts without repeated directional keystrokes. Currently an early prototype.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[wraithyy/herdr-openr](https://github.com/wraithyy/herdr-openr)**

A planned Herdr plugin that scans recent pane scrollback and Claude Code session transcripts to extract mentioned file paths and URLs into an interactive fuzzy finder. Prototype-stage as of mid-2026, aimed at opening referenced files directly in your editor without manual copy-pasting from agent output. ---

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[GoCodeAlone/mission-control-provider-herdr](https://github.com/GoCodeAlone/mission-control-provider-herdr)**

External Herdr session runtime provider for Mission Control. Early-stage or scaffolded implementation exploring Herdr multiplexer capabilities.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[robinbraemer/herdr-axi](https://github.com/robinbraemer/herdr-axi)**

Agent-ergonomic CLI for Herdr terminal workspace operations. Early-stage or scaffolded implementation exploring Herdr multiplexer capabilities.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[yoshimi-I/gengar.nvim](https://github.com/yoshimi-I/gengar.nvim)**

Editor-first Neovim environment built for herdr — agents and diff review (Hunk) live in the multiplexer, Neovim stays an editor. Early-stage or scaffolded implementation exploring Herdr multiplexer capabilities.

[↑ Back to contents](#contents)

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

[↑ Back to contents](#contents)
