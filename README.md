# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of tools built for **[Herdr](https://herdr.dev/)**, the app and runtime for running coding agents on every machine you own.

Official links: [Website](https://herdr.dev/) · [Download](https://herdr.dev/download/) · [GitHub](https://github.com/herdrdev) · [Gallery](https://herdr.dev/gallery/) · [Guide](https://herdr.dev/guide/) · [herdr-core](https://herdr.dev/core/) · [Herdr TUI](https://herdr.dev/tui/) · [TUI Plugins](https://herdr.dev/tui/plugins/) · [Agent Skill](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) · [Socket API](https://herdr.dev/tui/docs/socket-api/)

## Download Herdr

<p>
  <a href="https://releases.herdr.dev/app/Herdr.dmg"><img src="https://img.shields.io/badge/macOS-Download_.dmg-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Download Herdr for macOS" height="40"></a>
  <a href="https://herdr.dev/download/"><img src="https://img.shields.io/badge/Windows-x86__64-0078D4?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0wIDBoMTF2MTFIMHpNMTMgMGgxMXYxMUgxM3pNMCAxM2gxMXYxMUgwek0xMyAxM2gxMXYxMUgxM3oiLz48L3N2Zz4=" alt="Install Herdr on Windows" height="40"></a>
  <a href="https://herdr.dev/download/"><img src="https://img.shields.io/badge/Linux-x86__64_·_arm64-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Install Herdr on Linux" height="40"></a>
</p>

<p>
  <a href="https://apps.apple.com/app/id6828898364"><img src="assets/badges/app-store.svg" alt="Download on the App Store" height="40"></a>
  <a href="https://play.google.com/store/apps/details?id=dev.herdr.app"><img src="assets/badges/google-play.png" alt="Get it on Google Play" height="40"></a>
</p>

```sh
# macOS (Apple silicon) and Linux (x86_64, arm64)
curl -fsSL https://releases.herdr.dev/app/install.sh | sh
# Windows (x86_64), in PowerShell
powershell -c "irm https://releases.herdr.dev/app/install.ps1 | iex"
```

The desktop app installs [herdr-core](https://herdr.dev/core/) and updates itself. The iPhone, iPad, and Android apps connect to herdr-core over SSH. The original terminal app, [Herdr TUI](https://herdr.dev/tui/), installs with `curl -fsSL https://herdr.dev/install.sh | sh`.

---

## Contents

1. [Run and orchestrate agents (630)](#1-run-and-orchestrate-agents)
   - [Official Herdr projects and skill (5)](#official-herdr-projects-and-skill)
   - [Multi-agent fleets and supervisors (123)](#multi-agent-fleets-and-supervisors)
   - [Swarm, mob, and consensus orchestrators (15)](#swarm-mob-and-consensus-orchestrators)
   - [Claude Code multi-agent teams (57)](#claude-code-multi-agent-teams)
   - [Claude Code: Account switchers and auth monitors (9)](#claude-code-account-switchers-and-auth-monitors)
   - [Pi supervisor workflows and extensions (92)](#pi-supervisor-workflows-and-extensions)
   - [Pi: Presence, memory, and status extensions (10)](#pi-presence-memory-and-status-extensions)
   - [Subagent launchers and delegation (104)](#subagent-launchers-and-delegation)
   - [Autonomous coding and pull-request loops (16)](#autonomous-coding-and-pull-request-loops)
   - [Task queues, backlogs, and event triggers (85)](#task-queues-backlogs-and-event-triggers)
   - [Linear, GitHub Issues, and issue-to-PR automation (50)](#linear-github-issues-and-issue-to-pr-automation)
   - [General workflows and skill packs (64)](#general-workflows-and-skill-packs)
2. [Herdr app layouts, mods, and themes (780)](#2-herdr-app-layouts-mods-and-themes)
   - [Herdr app agent boards and mission-control layouts (35)](#herdr-app-agent-boards-and-mission-control-layouts)
   - [Herdr app sidebar and space-organization layouts (51)](#herdr-app-sidebar-and-space-organization-layouts)
   - [Herdr app IDE, editor and Git-panel layouts (33)](#herdr-app-ide-editor-and-git-panel-layouts)
   - [Herdr app palette, glass and desktop-OS themed layouts (55)](#herdr-app-palette-glass-and-desktop-os-themed-layouts)
   - [Herdr app pixel-art, game, anime and cyberpunk layouts (71)](#herdr-app-pixel-art-game-anime-and-cyberpunk-layouts)
   - [Herdr app sidebars, tabs, and visual mods (134)](#herdr-app-sidebars-tabs-and-visual-mods)
   - [Herdr app keys, navigation, and attention alerts (102)](#herdr-app-keys-navigation-and-attention-alerts)
   - [Herdr app usage, quota, and system status displays (50)](#herdr-app-usage-quota-and-system-status-displays)
   - [Herdr app Git, code review, and worktree panels (69)](#herdr-app-git-code-review-and-worktree-panels)
   - [Herdr app file, Markdown, and notes panels (56)](#herdr-app-file-markdown-and-notes-panels)
   - [Herdr app task boards, developer services, and mod bundles (116)](#herdr-app-task-boards-developer-services-and-mod-bundles)
   - [Herdr app themes (8)](#herdr-app-themes)
3. [Connect through MCP and the socket API (333)](#3-connect-through-mcp-and-the-socket-api)
   - [MCP servers (21)](#mcp-servers)
   - [Socket API and herdr-core clients and SDKs (40)](#socket-api-and-herdr-core-clients-and-sdks)
   - [Chat alerts: Telegram, Discord, and Slack (33)](#chat-alerts-telegram-discord-and-slack)
   - [Desktop, mobile, and webhook notifications (72)](#desktop-mobile-and-webhook-notifications)
   - [Telemetry, events, and quota streaming (32)](#telemetry-events-and-quota-streaming)
   - [Voice, hardware, and remote bridges (57)](#voice-hardware-and-remote-bridges)
   - [Protocol and third-party bridges (78)](#protocol-and-third-party-bridges)
4. [Editor integrations (106)](#4-editor-integrations)
   - [Neovim navigation and splits (30)](#neovim-navigation-and-splits)
   - [Full Neovim-hosted workspaces (4)](#full-neovim-hosted-workspaces)
   - [VS Code, Cursor, and dev containers (16)](#vs-code-cursor-and-dev-containers)
   - [Vim, Kakoune, and other editors (13)](#vim-kakoune-and-other-editors)
   - [REPL and code dispatchers (8)](#repl-and-code-dispatchers)
   - [Editor plugins and bridges (35)](#editor-plugins-and-bridges)
5. [Switch and restore sessions (260)](#5-switch-and-restore-sessions)
   - [Fuzzy session switchers and terminal pickers (109)](#fuzzy-session-switchers-and-terminal-pickers)
   - [Persistence, snapshots, and state restoration (68)](#persistence-snapshots-and-state-restoration)
   - [Workspace and multi-session management (83)](#workspace-and-multi-session-management)
6. [Worktrees and terminal experience (1320)](#6-worktrees-and-terminal-experience)
   - [Git worktree automation (135)](#git-worktree-automation)
   - [Workspace lifecycle and multi-repository tools (44)](#workspace-lifecycle-and-multi-repository-tools)
   - [Diff review and code inspection (89)](#diff-review-and-code-inspection)
   - [File viewers, terminal browsers, and markdown previews (81)](#file-viewers-terminal-browsers-and-markdown-previews)
   - [Pane navigation and overlay hints (58)](#pane-navigation-and-overlay-hints)
   - [Pane layout management (44)](#pane-layout-management)
   - [Terminal keybindings and shortcut helpers (86)](#terminal-keybindings-and-shortcut-helpers)
   - [Command palettes and workspace switchers (61)](#command-palettes-and-workspace-switchers)
   - [Status lines and workspace metadata (141)](#status-lines-and-workspace-metadata)
   - [Automatic tab, pane, and workspace names (91)](#automatic-tab-pane-and-workspace-names)
   - [Sidebar grouping, ordering, and filtering (45)](#sidebar-grouping-ordering-and-filtering)
   - [Sidebar badges, tokens, and status indicators (88)](#sidebar-badges-tokens-and-status-indicators)
   - [Status overlays, HUDs, and agent timers (78)](#status-overlays-huds-and-agent-timers)
   - [Context meters and rate-limit gauges (89)](#context-meters-and-rate-limit-gauges)
   - [Output inspection, logs, and transcripts (67)](#output-inspection-logs-and-transcripts)
   - [Agent visualizations and terminal games (34)](#agent-visualizations-and-terminal-games)
   - [Herdr TUI themes and appearance (19)](#herdr-tui-themes-and-appearance)
   - [Security guards and collision detectors (21)](#security-guards-and-collision-detectors)
   - [Plugin collections, frameworks, and ready-made configs (49)](#plugin-collections-frameworks-and-ready-made-configs)
7. [Apps, companion integrations, and installation (481)](#7-apps-companion-integrations-and-installation)
   - [Native desktop and mobile apps (123)](#native-desktop-and-mobile-apps)
   - [Web dashboards and remote viewers (125)](#web-dashboards-and-remote-viewers)
   - [Hardware and ambient displays (47)](#hardware-and-ambient-displays)
   - [Processes, ports, sandboxes, and remote machines (28)](#processes-ports-sandboxes-and-remote-machines)
   - [Agent support, auto-approve, retry, and keep-awake helpers (18)](#agent-support-auto-approve-retry-and-keep-awake-helpers)
   - [Notes, prompts, clipboard, and file helpers (32)](#notes-prompts-clipboard-and-file-helpers)
   - [Developer tool panes and everyday utilities (56)](#developer-tool-panes-and-everyday-utilities)
   - [Setup, packages, and version management (52)](#setup-packages-and-version-management)
8. [Experimental projects (10)](#8-experimental-projects)
   - [Experiments, concepts, and scaffolds (10)](#experiments-concepts-and-scaffolds)
9. [Resources](#resources)
10. [Reference](#reference)

---

## 1. Run and orchestrate agents

*630 projects. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.* The top 10 of each subcategory by stars are below; the full list is in [catalog/01-run-and-orchestrate.md](catalog/01-run-and-orchestrate.md).

### Official Herdr projects and skill

*5 projects. Official Herdr applications, runtimes, integrations, examples, and agent instructions.*

| Project | Stars | What it does |
|---|--:|---|
| [**herdrdev/herdr-app**](https://github.com/herdrdev/herdr-app) | 2,636 | Runs the official Herdr desktop app for terminals and coding agents on macOS, Windows, and Linux. |
| [**herdrdev/herdr-core**](https://github.com/herdrdev/herdr-core) | 588 | Runs persistent terminals and coding agents through the herdr-core runtime, with commands to start, message and wait for work on local or remote machines. |
| [**herdrdev/herdr**](https://github.com/herdrdev/herdr) | 49,988 | Runs the official Herdr TUI for organizing agents and terminals. The official [SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) teaches agents to control its workspaces, tabs, and panes. |
| [**herdrdev/herdr-layout-examples**](https://github.com/herdrdev/herdr-layout-examples) | 15 | Shows a collection of Herdr app window layouts including Board, Chat, Mission, Pasture and Threads, plus a tmux-style prefix mod. |
| [**herdrdev/herdr-nix**](https://github.com/herdrdev/herdr-nix) | 20 | Installs hash-verified Herdr TUI release binaries through Nix and offers a Cachix binary cache. |

### Multi-agent fleets and supervisors

*123 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*

| Project | Stars | What it does |
|---|--:|---|
| [**kunchenguid/firstmate**](https://github.com/kunchenguid/firstmate) | 8,761 | Supervises coding agents in separate Herdr TUI tabs and isolated Git worktrees. Supports Claude Code, Pi, Codex, OpenCode, and other agent harnesses. |
| [**sisyphuslabs/dori-superagent**](https://github.com/sisyphuslabs/dori-superagent) | 232 | Runs a lead agent and parallel coding lanes in Herdr TUI tabs, with resource guards and a gated merge workflow. |
| [**stevenmichaelthomas/numbrone**](https://github.com/stevenmichaelthomas/numbrone) | 114 | Routes requests through a chief agent to project managers and parallel workers in Herdr TUI workspaces and Git worktrees. |
| [**chengyixu/oh-my-herdr**](https://github.com/chengyixu/oh-my-herdr) | 97 | Organizes Codex, Pi, and Claude Code profiles with persistent instructions in shared coding spaces using a separate Herdr-derived runtime. |
| [**wanshuiyin/SuperARIS**](https://github.com/wanshuiyin/SuperARIS) | 73 | Runs a persistent research team in Herdr with a lead agent and engineering and writing roles. |
| [**larcane97/clausona**](https://github.com/larcane97/clausona/blob/main/docs/usecases/herdr-fleet.md) | 61 | Splits a job across Herdr worktrees and panes from one Claude Code or Codex session, routing each worker to one of your accounts by remaining usage or to an API model such as DeepSeek. Part of clausona, a daemon-less multi-account manager that drives Herdr only through its CLI and checks each branch before removing a worktree. |
| [**aorumbayev/herdr-workflows**](https://github.com/aorumbayev/herdr-workflows) | 40 | Runs repeatable development and agent workflows from YAML files. Each manifest defines an ordered sequence of commands and agent interactions to execute inside Herdr workspaces. |
| [**junghan0611/entwurf**](https://github.com/junghan0611/entwurf) | 34 | Connects Pi, Claude Code, Codex, Copilot, OMP, and Antigravity sessions in Herdr or tmux so they can address, message, and open visible siblings without sharing auth, tools, or transcripts. Includes a Herdr integration for pi and Claude Code. |
| [**ericbust/namedrop**](https://github.com/ericbust/namedrop) | 23 | Sends named mentions between agents in Herdr TUI panes and workspaces. |
| [**meviusisback/agent-orchestr**](https://github.com/meviusisback/agent-orchestr) | 19 | Monitors live agent output and orchestrates multi-agent workspaces across Herdr, OpenCode, and Claude sessions. |

**[All 123 projects →](catalog/01-run-and-orchestrate.md#multi-agent-fleets-and-supervisors)**

### Swarm, mob, and consensus orchestrators

*15 projects. Parallel agent swarms, mob-programming groups, and multi-model consensus engines.*

| Project | Stars | What it does |
|---|--:|---|
| [**aliceisjustplaying/swarmchat**](https://github.com/aliceisjustplaying/swarmchat) | 5 | Lets Claude Code and Codex or Astra exchange peer messages in Herdr while a third pane shows their shared log. |
| [**zekierman/herdr-council**](https://github.com/zekierman/herdr-council) | 4 | Asks coding agents in Herdr TUI the same question and combines blind peer rankings with a judge agent verdict. |
| [**enes/herdr-rooms**](https://github.com/enes/herdr-rooms) | 3 | Opens review rooms where Claude Code or Codex agents review each other in Herdr TUI. |
| [**HinchK/stampede**](https://github.com/HinchK/stampede) | 3 | Coordinates coding agents in Herdr TUI with ticket dispatch, independent checks, and a human-controlled integration queue. |
| [**conscientiousness/herdr-pstack-orchestrator**](https://github.com/conscientiousness/herdr-pstack-orchestrator) | 2 | Adds Agent Skills for running visible multi-model coding teams across Pi, Codex and Claude Code in Herdr panes. Adds pstack review loops with a controller and workers. |
| [**neospeed83/herdr-tournament**](https://github.com/neospeed83/herdr-tournament) | 1 | Runs independent Codex or Claude reviews of a branch or pull request, then consolidates findings through an adversarial judge workflow. |
| [**tuanhung303/herdr-swarm**](https://github.com/tuanhung303/herdr-swarm) | 1 | Runs agent waves in Herdr pane grids, routes messages through an optional mailbox, and collects results from multiple harnesses. |
| [**ndemeshchenko/herdr-peer-chat**](https://github.com/ndemeshchenko/herdr-peer-chat) | 1 | Lets Claude Code and Codex exchange messages in one Herdr tab through the agent API. |
| [**xzedx/herdr-derby**](https://github.com/xzedx/herdr-derby) | 1 | Sends one prompt to every agent in the current Herdr TUI tab and races them, with live timers and finishing ranks on pane borders. Can also start fresh agents in separate worktrees. |
| [**ArtMoreno/herdr-swarm**](https://github.com/ArtMoreno/herdr-swarm) | 0 | Races coding agents in Herdr panes and isolated Git worktrees, compare their diffs, and apply a winner. |

**[All 15 projects →](catalog/01-run-and-orchestrate.md#swarm-mob-and-consensus-orchestrators)**

### Claude Code multi-agent teams

*57 projects. Adapters and skills that organize Claude Code sessions into structured teams.*

| Project | Stars | What it does |
|---|--:|---|
| [**caioniehues/herdmates**](https://github.com/caioniehues/herdmates) | 26 | Runs Claude Code multi-agent teams in Herdr through a teammux translation layer. Teammates work in isolated panes while a mission-control view reports their status and task progress. |
| [**mohseenrm/zj-agent-mob**](https://github.com/mohseenrm/zj-agent-mob) | 12 | Monitors coding agent fleets with Herdr-inspired workflows and pane observation. |
| [**neptunix/corral**](https://github.com/neptunix/corral) | 10 | Provides a kanban dashboard and control surface for Claude Code sessions running in herdr. |
| [**overflowy/herdr-adversarial-review**](https://github.com/overflowy/herdr-adversarial-review) | 10 | Provides a Claude Code skill for adversarial code review that spawns an automated reviewer in a Herdr split pane. |
| [**hapo-nghialuu/hod**](https://github.com/hapo-nghialuu/hod) | 6 | Coordinates Codex, Claude Code, and Grok Build agents safely through Herdr. |
| [**wangfan1998-github/herdr-hybrid**](https://github.com/wangfan1998-github/herdr-hybrid) | 6 | Orchestrates Claude Code hybrid teams with high-tier models supervising parallel worker panes in Herdr. |
| [**blaxel-ai/herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) | 5 | Runs coding agents in persistent Blaxel sandboxes from Herdr. |
| [**igor/crew-skill**](https://github.com/igor/crew-skill) | 5 | Coordinates a fleet of AI agents in Herdr where premium models lead and local models handle volume execution. |
| [**david-lutz/herdr-claude-teams**](https://github.com/david-lutz/herdr-claude-teams) | 3 | Maps Claude Code's experimental agent-team commands to Herdr's socket API, so teammates open as native Herdr panes instead of tmux panes. It requires Herdr 0.6.10 and supports Herdr metadata, notifications, and sidebar views. |
| [**rcosteira79/herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue) | 3 | Watches agents for usage-limit walls, badges the countdown to the reset ($wall), and re-prompts the agents you armed once the window reopens. |

**[All 57 projects →](catalog/01-run-and-orchestrate.md#claude-code-multi-agent-teams)**

### Claude Code: Account switchers and auth monitors

*9 projects. Tools for managing Claude multi-account rotation, OAuth keys, and quota monitoring.*

| Project | Stars | What it does |
|---|--:|---|
| [**uwuclxdy/clauth · herdr-plugin**](https://github.com/uwuclxdy/clauth/tree/mommy/herdr-plugin) | 321 | Manages Claude Code accounts and usage from a Herdr TUI popup and tags panes with their active account. |
| [**wazum/herdr-grazr**](https://github.com/wazum/herdr-grazr) | 7 | Provides a simple and reliable auto account switcher for Claude Code: rotates to a fresh account before the 5-hour or weekly rate limit hits, so no pane ever stops at the usage quota. A Herdr plugin. |
| [**rcosteira79/herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch) | 5 | Switches Claude Code and Codex account profiles from a Herdr overlay or keybinding and labels panes with the active account. |
| [**aodanchenko/herdr-claude-usage**](https://github.com/aodanchenko/herdr-claude-usage) | 4 | Shows Claude Code plan usage and reset times in the Herdr TUI tab bar and a multi-account popup dashboard. |
| [**C0R0NELL/herdr-account-hub**](https://github.com/C0R0NELL/herdr-account-hub) | 2 | Switches between saved Codex and Claude Code accounts from one picker in Herdr TUI, shows usage, and applies available Codex resets. Codex switching reloads open chats while keeping their history and titles; Claude Code support is beta. |
| [**nolvane/herdr-multiaccount**](https://github.com/nolvane/herdr-multiaccount) | 1 | Keeps several Claude accounts side by side in Herdr, shows each account's 5-hour and 7-day usage and picks one per space. Moves new sessions to the next account at a limit. |
| [**supex0fan/herdr-claude-swap**](https://github.com/supex0fan/herdr-claude-swap) | 0 | Resumes each Claude Code pane through the claude-swap account that owns its existing session. |
| [**msiric/herdr-auth-picker**](https://github.com/msiric/herdr-auth-picker) | 0 | Switches the logged-in Claude Code or Codex account from a Herdr popup without logging out and back in. Backs up logins first so none is lost along the way. |
| [**johntrandall/herdr-claude-account-watch**](https://github.com/johntrandall/herdr-claude-account-watch) | 0 | Flags Claude Code panes in Herdr TUI that are logged out or have hit a usage limit, which Herdr otherwise shows as idle. |

### Pi supervisor workflows and extensions

*92 projects. Supervision harnesses, task planners, and extensions for Pi agents in Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**ogulcancelik/pi-extensions**](https://github.com/ogulcancelik/pi-extensions) | 573 | Extends Pi with overlays, parallel agent spawners, session recall, and direct Herdr pane control. |
| [**osolmaz/pi-workflows**](https://github.com/osolmaz/pi-workflows) | 361 | Provides a workflow engine, JSON control-flow system, and live terminal viewer for the Pi coding agent in Herdr. |
| [**boadij/pi-herdsman**](https://github.com/boadij/pi-herdsman) | 221 | Delegates work to asynchronous Pi agents in Herdr TUI, with nested delegation and fleet supervision. |
| [**edxeth/pi-subagents**](https://github.com/edxeth/pi-subagents) | 136 | Provides a Pi framework for foreground and background subagents, messaging, and multi-pane orchestration. |
| [**joelhooks/pi-bellwether**](https://github.com/joelhooks/pi-bellwether) | 89 | Exposes Herdr agent, pane, and session controls as Pi slash commands and LLM tools. It provides reusable start, send, read, focus, and stop operations for higher-level Pi workflows. |
| [**electric-dragon-80000v/pi-cowboy**](https://github.com/electric-dragon-80000v/pi-cowboy) | 66 | Runs Pi-supervised coding agents in Herdr TUI panes and isolated Git worktrees, including Claude Code, Codex and OpenCode. |
| [**AndrewJacop/pi-herdr**](https://github.com/AndrewJacop/pi-herdr) | 37 | Lets Pi spawn, steer, and collect results from Pi, Claude Code, Codex, and OpenCode agents in Herdr TUI panes. |
| [**oscabriel/pi-herdr-btw**](https://github.com/oscabriel/pi-herdr-btw) | 26 | Opens a separate Pi side conversation in a Herdr TUI pane without changing the parent transcript. |
| [**jillesme/pi-herdr-squad**](https://github.com/jillesme/pi-herdr-squad) | 25 | Creates visible, strictly read-only investigation teams for Pi inside Herdr. It is intended for parallel research and review tasks that must not modify the workspace. |
| [**ribbons-digital/pi-herd**](https://github.com/ribbons-digital/pi-herd) | 23 | Coordinates visible Pi lead and worker sessions in Herdr TUI panes, isolating code-changing roles in Git worktrees. |

**[All 92 projects →](catalog/01-run-and-orchestrate.md#pi-supervisor-workflows-and-extensions)**

### Pi: Presence, memory, and status extensions

*10 projects. Persistent memory trackers, presence indicators, and live status displays for Pi agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**RamonsDka/gs3-sidebar**](https://github.com/RamonsDka/gs3-sidebar) | 7 | Shows a read-only sidebar for Pi and Gentle Shell in Herdr TUI, including agent status, context, Git and subagents. |
| [**edxeth/herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree) | 4 | Shows Pi agents and their subagents as a Herdr TUI sidebar tree with worktree branches and Git status. |
| [**hanbong5938/herdr-omp-subagents**](https://github.com/hanbong5938/herdr-omp-subagents) | 3 | Shows the active Oh My Pi main-agent and subagent models in the Herdr TUI sidebar. |
| [**spi-ca/pi-herdr-presence**](https://github.com/spi-ca/pi-herdr-presence) | 1 | Extends Pi agent presence indicators and runtime status inside Herdr workspaces. |
| [**mastnacek/pi-herdr-sidebar**](https://github.com/mastnacek/pi-herdr-sidebar) | 1 | Shows Pi agent telemetry in a Herdr TUI pane or popup, including model, context window, tokens, cost, and skill gates read from the Pi session log. Built in Rust with Ratatui. |
| [**ubranch/omp-herdr-neighbors**](https://github.com/ubranch/omp-herdr-neighbors) | 1 | Tells an omp agent which other Herdr agents run beside it, with their status and last reply. Sends hidden context only when it changes and has no runtime dependencies. |
| [**Attamusc/pi-herdr**](https://github.com/Attamusc/pi-herdr) | 0 | Reports Pi lifecycle states to Herdr TUI so its sidebar shows working, blocked, done, and idle agents. |
| [**larryboiNEUQ/pi-herdr-ui-bridge**](https://github.com/larryboiNEUQ/pi-herdr-ui-bridge) | 0 | Reports blocking Pi extension prompts as Herdr agent blocked states so notification plugins can alert users. |
| [**BrianM0330/pi-herdr-snooze**](https://github.com/BrianM0330/pi-herdr-snooze) | 0 | Adds a forced snooze state to Pi agents in Herdr, controlled through `/snooze` or a key binding and independent of the underlying agent type. |
| [**markbrutx/pif-herdr-reporter**](https://github.com/markbrutx/pif-herdr-reporter) | 0 | Reports working and idle states from the pif coding agent to its Herdr TUI pane and releases the agent on exit. |

### Subagent launchers and delegation

*104 projects. Tools that launch workers, delegate tasks, and exchange messages between agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**alvinunreal/oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim) | 10,184 | Assigns OpenCode specialist roles (fixers, librarians, explorers) to dedicated Herdr panes. |
| [**vekexasia/pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows) | 253 | Runs deterministic Pi workflows with on-disk checkpoints and Git worktree isolation in Herdr. |
| [**nidhi-singh02/agent-router**](https://github.com/nidhi-singh02/agent-router) | 124 | Routes tasks to Cursor, Claude Code, Codex or OpenCode and launches the selected agent in a Herdr TUI pane. |
| [**giuseppecrj/pi-herdr-agents**](https://github.com/giuseppecrj/pi-herdr-agents) | 71 | Runs asynchronous Pi subagents and approval-based review workflows entirely inside Herdr. |
| [**e2b-dev/herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox) | 19 | Mirrors a git worktree into an E2B sandbox, one box or a branch-per-agent fleet, with a TUI dashboard. |
| [**mupt-ai/context-drop**](https://github.com/mupt-ai/context-drop) | 19 | Provides a Herdr-backed meta-harness for orchestrating autonomous coding agents. |
| [**vercel-labs/herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin) | 17 | Runs Claude Code, Codex, or OpenCode inside isolated Vercel Sandbox microVMs while showing each session as a Herdr pane. It previews uploads, excludes secrets, and exports agent changes back as Git patches. |
| [**afogel/shepherdr**](https://github.com/afogel/shepherdr) | 11 | Dispatches Claude, Codex, and Cursor coding subagents into visible Herdr TUI panes and lets users resume completed sessions. |
| [**onsails/fork-in**](https://github.com/onsails/fork-in) | 10 | Forks an ongoing Pi or omp conversation into a new Herdr tab while preserving its conversation context. |
| [**transparent-pegasus/herdr-orchestration**](https://github.com/transparent-pegasus/herdr-orchestration) | 10 | Routes coding and review work to sibling Herdr TUI panes using configurable agent roles and composer-safe delegation. |

**[All 104 projects →](catalog/01-run-and-orchestrate.md#subagent-launchers-and-delegation)**

### Autonomous coding and pull-request loops

*16 projects. Long-running workflows that implement changes, open pull requests, review results, and react to CI.*

| Project | Stars | What it does |
|---|--:|---|
| [**jpolec/herdr-plugin-odysseus**](https://github.com/jpolec/herdr-plugin-odysseus) | 11 | Runs governed multi-agent tasks in Herdr TUI panes with checks, retries, review, approvals, and draft pull requests. |
| [**sean1588/herdr-orchestrator**](https://github.com/sean1588/herdr-orchestrator) | 6 | A Go daemon that runs an issue-to-pull-request workflow from a validated YAML state graph. Herdr hosts implementer and reviewer agents, while the daemon checks GitHub's merge gate and can squash-merge, with dry-run enabled by default. |
| [**tomasvarga/herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr) | 6 | Starts an agent in Herdr to perform an initial quality and bug review of a pull request, then writes draft comments into tuicr. It supports Claude, Codex, Cursor, and Grok backends. |
| [**razajamil/herdr-factory**](https://github.com/razajamil/herdr-factory) | 5 | Claims work from Jira or Markdown task files, creates one Herdr worktree per item, and moves Claude Code through a configurable YAML pipeline. It can follow pull requests through CI, review, and merge under a shared concurrency limit. |
| [**night-porter/nightporter**](https://github.com/night-porter/nightporter) | 4 | Runs coding agents on review comments, failing CI, and merge conflicts and opens job worktrees in Herdr TUI. |
| [**zhuravel/magnum**](https://github.com/zhuravel/magnum) | 4 | Runs Claude Code, Codex and other agents in Herdr TUI panes to review pull requests, then uses a judge agent to verify findings and post a consolidated GitHub review. |
| [**robi42/factory**](https://github.com/robi42/factory) | 4 | Runs Claude Code planning and building alongside Codex reviews in Herdr TUI, with Beads tracking tasks. |
| [**firegnu/herdr-loop-lab**](https://github.com/firegnu/herdr-loop-lab) | 3 | Runs bounded coding loops in Herdr TUI with mechanical checks and cross-model review, parallel worktree fleets, and large-goal decomposition. |
| [**MovieHolic-Plex/herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish) | 3 | Starts an omo `/wish` workflow in a new Herdr TUI worktree to implement a request, commit changes, and open a pull request. |
| [**Tudor0404/dual-author**](https://github.com/Tudor0404/dual-author) | 1 | Processes GitHub issues through isolated worktrees, Claude implementation, draft pull requests, and paired Codex and Claude review rounds. A dashboard shows each issue's stage and elapsed time until the change is ready for automatic merging. |

**[All 16 projects →](catalog/01-run-and-orchestrate.md#autonomous-coding-and-pull-request-loops)**

### Task queues, backlogs, and event triggers

*85 projects. Queues and event-driven systems that turn stored work into agent jobs.*

| Project | Stars | What it does |
|---|--:|---|
| [**smarzban/herdr-tsk**](https://github.com/smarzban/herdr-tsk) | 266 | Shares a terminal task board between you and your agents with a TUI for humans and a CLI for agents. |
| [**smarzban/tsk**](https://github.com/smarzban/tsk) | 266 | Opens a shared task board in Herdr TUI and lets agents manage work through a CLI. |
| [**nelsonPires5/herdr-board**](https://github.com/nelsonPires5/herdr-board) | 194 | A Kanban TUI and background service that turns cards into prompts for agents in visible Herdr panes. Moving a card can create an agent, run it in a dedicated tab, and advance the work through review gates. |
| [**deimantasnork/captains-deck**](https://github.com/deimantasnork/captains-deck) | 74 | Displays a read-only Firstmate flow kanban board inside Herdr TUI. |
| [**miiraheart/herdr-beads**](https://github.com/miiraheart/herdr-beads) | 42 | Displays Beads issues as a list, table, or Kanban board in a Herdr sidebar or floating pane. |
| [**DnzzL/herdr-automations**](https://github.com/DnzzL/herdr-automations) | 31 | Schedules recurring prompts and cron jobs that run agents in fresh Herdr worktrees. It supports task-specific MCP settings, collision protection, persistent run history, and a live monitoring board. |
| [**CodeForBreakfast/beady-eye**](https://github.com/CodeForBreakfast/beady-eye) | 27 | Shows, live, which agent works on which bead across your projects next to its Herdr pane, and tells agents and scripts when the beads they wait on change. |
| [**ivanarama/PromptPilot**](https://github.com/ivanarama/PromptPilot) | 22 | Queues and schedules prompts for coding CLIs through a web UI or Telegram bot, with Herdr-backed terminal sessions and retry on rate limits. |
| [**bon5co/bermuda**](https://github.com/bon5co/bermuda) | 13 | Schedules jobs as interactive agents in dedicated Herdr splits. It supports multi-step workflows, shared append-only discussion logs, and exclusive resource claims that remain valid across temporary sessions. |
| [**mrcndz/herdr-routines**](https://github.com/mrcndz/herdr-routines) | 11 | Runs scheduled routines on cron or interval timers by opening a tab in a chosen workspace and executing a command or starting an agent. |

**[All 85 projects →](catalog/01-run-and-orchestrate.md#task-queues-backlogs-and-event-triggers)**

### Linear, GitHub Issues, and issue-to-PR automation

*50 projects. Automated pipelines bridging issue trackers directly to Herdr agent workspaces and PRs.*

| Project | Stars | What it does |
|---|--:|---|
| [**jmwind/issue-herd**](https://github.com/jmwind/issue-herd) | 42 | Watches Linear; when an issue matches a rule, run Claude Code in a herdr workspace and report the PR back to the issue. |
| [**ogulcancelik/herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start) | 17 | Turns a GitHub issue, pull request, or discussion into a prepared agent tab with one key. |
| [**a2u/herdr-jira**](https://github.com/a2u/herdr-jira) | 15 | Adds a Ratatui Jira client to browse, filter, and assign tickets directly to Herdr agent panes. |
| [**Matovidlo/herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker) | 12 | Tracks the GitHub pull request associated with each Claude Code session and offers GitHub actions. |
| [**freethinkel/shepherd**](https://github.com/freethinkel/shepherd) | 12 | Controls plane for coding agents on top of Herdr: tracker task in, pull request out. |
| [**JacquesvanWyk/herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear) | 8 | Opens an fzf-driven Linear panel in a Herdr TUI split or tab to search issues, browse projects, create issues, and change their status. |
| [**mrolafsson/herdr-linear**](https://github.com/mrolafsson/herdr-linear) | 8 | Browses Linear issues and starts agents in issue worktrees from the Herdr app or a Herdr TUI popup. |
| [**mrolafsson/herdr-github**](https://github.com/mrolafsson/herdr-github) | 8 | Reviews and manages GitHub pull requests and starts agents in PR worktrees from the Herdr app or a Herdr TUI popup. |
| [**talent-factory/herdr-linear**](https://github.com/talent-factory/herdr-linear) | 5 | Adds an interactive Linear issue browser to Herdr. Selecting an issue opens a dedicated agent pane and supplies the ticket context so implementation can begin immediately. |
| [**civitaspo/herdr-linear-agent**](https://github.com/civitaspo/herdr-linear-agent) | 5 | Runs a coordinator and repository coding agents in Herdr TUI panes for Linear issues delegated to its app user. |

**[All 50 projects →](catalog/01-run-and-orchestrate.md#linear-github-issues-and-issue-to-pr-automation)**

### General workflows and skill packs

*64 projects. Reusable skills, commands, and opinionated setups for common agent workflows.*

| Project | Stars | What it does |
|---|--:|---|
| [**cloudmanic/herdr-plus**](https://github.com/cloudmanic/herdr-plus) | 379 | A plugin with two launchers: TOML project templates that build complete workspaces from a fuzzy picker, and Quick Actions for running reusable scripts in the current directory. Prebuilt binaries are available. |
| [**oborchers/proqi**](https://github.com/oborchers/proqi) | 46 | Provides a terminal-native prompt composer for power users running multiple coding agents. |
| [**DeevsDeevs/agent-system · skills/hc**](https://github.com/DeevsDeevs/agent-system/tree/main/skills/hc) | 41 | Teaches coding agents to run background work, communicate with peers and operate across machines using herdr-core. |
| [**madarco/agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin) | 34 | Connects AgentBox sandboxes to Herdr through a live overlay, a one-key VM launcher for the current project, and clickable `agentbox://` links. |
| [**sanirudh17/herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff) | 22 | Moves an active coding conversation to a new session using another installed agent CLI. The complete transcript and command history are passed to the replacement agent, avoiding a manual handoff summary. |
| [**arronKler/herdr-skills**](https://github.com/arronKler/herdr-skills) | 21 | Coordinates Herdr coding agents with dispatch, handoff, result collection, and swarm skills. |
| [**transparent-pegasus/herdrpowers**](https://github.com/transparent-pegasus/herdrpowers) | 14 | Coordinates planning, implementation, testing, and review across Herdr TUI agent panes using workflows adapted from Superpowers. |
| [**pbean/bmad-loop-adapter-herdr**](https://github.com/pbean/bmad-loop-adapter-herdr) | 7 | Provides a Herdr terminal-multiplexer backend for bmad-loop. |
| [**juanitourquiza/shipframe · herdr-plugin**](https://github.com/juanitourquiza/shipframe/tree/main/herdr-plugin) | 5 | Opens a ShipFrame workflow pane and checklist in Herdr TUI for Claude Code, Codex, or OpenCode. |
| [**motionharvest/herdr**](https://github.com/motionharvest/herdr) | 4 | A terminal-based agent multiplexer project. The source catalog provides no additional detail beyond its Herdr name and purpose. |

**[All 64 projects →](catalog/01-run-and-orchestrate.md#general-workflows-and-skill-packs)**

---

## 2. Herdr app layouts, mods, and themes

*780 projects. Layouts, mods, and themes for customizing the Herdr desktop app.* The top 10 of each subcategory by stars are below; the full list is in [catalog/02-herdr-app.md](catalog/02-herdr-app.md).

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community extensions.

### Herdr app agent boards and mission-control layouts

*35 projects. Whole-window layouts that put agents on kanban boards, attention inboxes, fleet views and task-driven mission-control screens.*

| Project | Stars | What it does |
|---|--:|---|
| [**eliasstravik/shepherdr**](https://github.com/eliasstravik/shepherdr) | 1,117 | Organizes coding agents in a Herdr app layout with per-space assistants and task cards, running tasks in separate worktrees. |
| [**JinJieBeWater/herdr-t3**](https://github.com/JinJieBeWater/herdr-t3) | 157 | Organizes Herdr app agents in an inbox that groups work by attention state and shows agents across machines. |
| [**quaresc/cockpit**](https://github.com/quaresc/cockpit) | 32 | Shows Herdr agents, their work, and items needing attention in an app layout or TUI plugin. |
| [**simoncrypta/bercail**](https://github.com/simoncrypta/bercail) | 20 | Adds the Bercail layout to the Herdr app for supervising agents across Git worktrees, with a desk pane for each space. |
| [**jlopezlira/herdr-kanso**](https://github.com/jlopezlira/herdr-kanso) | 17 | Adds the Kanso horizontal-agent layout plus Markdown panel and editor-launcher mods to the Herdr app. |
| [**adamentwistle/orchi-build**](https://github.com/adamentwistle/orchi-build) | 13 | Adds an Orchi layout for managing Claude Code agents, tickets, agent status, and orchestration in the Herdr app. |
| [**jkuepker/herdr-layouts**](https://github.com/jkuepker/herdr-layouts) | 12 | Collects Board, LCARS, and Slate layouts for organizing agents and workspaces in the Herdr app. |
| [**sgomez/herdr-triage**](https://github.com/sgomez/herdr-triage) | 9 | Adds a Herdr app layout with an attention inbox, agent replies, worktrees, Git history, pull requests and issues. |
| [**CiprianSpiridon/herdr-mission-control**](https://github.com/CiprianSpiridon/herdr-mission-control) | 7 | Adds Mission Control and Classic Herdr app layouts with mods for agent monitoring, Jira, GitHub, GitLab, sessions, tabs and worktree launches. |
| [**Lakris2407/herdr-mods**](https://github.com/Lakris2407/herdr-mods) | 6 | Adds the Fleet Herdr app layout and mods for agent lists, quotas, build runners, delivery stats and controls. |

**[All 35 projects →](catalog/02-herdr-app.md#herdr-app-agent-boards-and-mission-control-layouts)**

### Herdr app sidebar and space-organization layouts

*51 projects. Layouts that rework the Spaces, Agents and tabs sidebar with trees, folders, machine grouping, worktrees and usage gauges.*

| Project | Stars | What it does |
|---|--:|---|
| [**jankeesvw/herdr-space-folders**](https://github.com/jankeesvw/herdr-space-folders) | 37 | Groups Herdr app spaces into colored, collapsible folders using drag-and-drop or project folder rules. |
| [**shellscape/herdr-whitby**](https://github.com/shellscape/herdr-whitby) | 31 | Organizes Herdr app spaces into a light project sidebar with nested agents, status dots, and an attention bell. |
| [**herunan/herdr-over9k**](https://github.com/herunan/herdr-over9k) | 10 | Collects the Over9k layout and launcher, sidebar, switcher, timeline, to-do, and usage mods for the Herdr app. |
| [**VladTemp27/herdr-orca**](https://github.com/VladTemp27/herdr-orca) | 9 | Adds a Herdr app layout with nested worktrees and agents, GitHub issues and pull requests, usage limits and file panels. |
| [**emoss08/herdr-wsl**](https://github.com/emoss08/herdr-wsl) | 7 | Connects a Windows Herdr app layout to a WSL 2 machine so spaces, terminals and repository panels use Linux paths. |
| [**dissimulate/bettr**](https://github.com/dissimulate/bettr) | 5 | Adds a Herdr app layout with agent and usage sidebars, system statistics, terminals, and file and activity panels. |
| [**ozcberkay/herdr-coban**](https://github.com/ozcberkay/herdr-coban) | 4 | Adds a Herdr app layout and mods for Claude Code usage and session status, per-tab notes and Mac system metrics. |
| [**chelebyy/herdr-agent-workspace**](https://github.com/chelebyy/herdr-agent-workspace) | 3 | Adds a Herdr app layout with agent and resource sidebars, quota gauges, task launchers, and Turkish and English UI options. |
| [**VedangP57/herdr-tui-layout**](https://github.com/VedangP57/herdr-tui-layout) | 3 | Recreates Herdr TUI navigation in the Herdr app with machine-grouped spaces, agent status, tabs, and prefix keys. |
| [**pavlo-petrychenko/herdr-config**](https://github.com/pavlo-petrychenko/herdr-config) | 3 | Installs a Herdr app setup with npx herdr-kit: a flat list of spaces and agents, a queue of agents waiting for you, a Claude Code usage bar, a PRs view, and a worktrees popup. Each piece can be chosen separately. |

**[All 51 projects →](catalog/02-herdr-app.md#herdr-app-sidebar-and-space-organization-layouts)**

### Herdr app IDE, editor and Git-panel layouts

*33 projects. Layouts that make the Herdr app feel like VS Code, Zed, IntelliJ or Neovim, or that dock Git, file, review and pull-request panels beside terminals.*

| Project | Stars | What it does |
|---|--:|---|
| [**munza/herdr-mods**](https://github.com/munza/herdr-mods) | 12 | Adds the Estro layout and a collection of Herdr app mods for Git, files, tabs, settings, Linear, pull requests, staged agent runs and Mac automation. |
| [**carstenlucke/herdr-roundup**](https://github.com/carstenlucke/herdr-roundup) | 6 | Adds the Roundup layout for the Herdr app with custom file browsing, preview, themes, and keyboard shortcuts. |
| [**h3y6e/dotfiles · dot_config/herdr-app**](https://github.com/h3y6e/dotfiles/tree/main/dot_config/herdr-app) | 6 | Adds the Zebra layout for the Herdr app: a flat, editor-style window with spaces and tabs as projects and threads in one sidebar, Files and Changes panels beside the panes, and a thin status bar. Includes the supporting mods and a RECIPE.md brief an agent can rebuild it from. |
| [**dantech99/herdr-zed-layout**](https://github.com/dantech99/herdr-zed-layout) | 5 | Adds a Zed-inspired Herdr app layout with tabs, file and changes panels, agent quotas, and Tokyo Night colors. |
| [**tackcrypto1031/tackbear-herdr-mod**](https://github.com/tackcrypto1031/tackbear-herdr-mod) | 4 | Adds a Herdr app layout with a chat-style input box, file and image attachments, and model and reasoning controls. |
| [**mirkobozzetto/herdr-app-config**](https://github.com/mirkobozzetto/herdr-app-config) | 3 | Adds a keyboard-first Herdr app layout with shortcut menus, agent status, file panels, and code review tools. |
| [**jotyy/herdr-ovis-studio**](https://github.com/jotyy/herdr-ovis-studio) | 3 | Adds an Ovis Studio-inspired Herdr app layout with an agent sidebar, tab bar, status line, and command picker. |
| [**bborrero14/herdr-file-preview**](https://github.com/bborrero14/herdr-file-preview) | 2 | Adds a Herdr app layout with a file tree of the focused terminal folder beside a rendered preview of Markdown with Mermaid diagrams and highlighted source files. Works in local and remote spaces. |
| [**alarboulletmarin/herdr-github**](https://github.com/alarboulletmarin/herdr-github) | 2 | Extends the Herdr app main layout with a GitHub panel for issues, pull requests, CI runs, milestones and projects, and a Zed-style Changes panel. Each item can be copied or started as an agent brief. |
| [**dougcunha/herdr-mods**](https://github.com/dougcunha/herdr-mods) | 1 | Collects Herdr app mods, layouts and themes that dispatch GitHub Actions, follow jobs and show pending repository work, plus agent cards. |

**[All 33 projects →](catalog/02-herdr-app.md#herdr-app-ide-editor-and-git-panel-layouts)**

### Herdr app palette, glass and desktop-OS themed layouts

*55 projects. Windows defined mainly by a color palette, glass or minimal look, or a faithful classic desktop and app skin such as NeXTSTEP, Windows 7 or Catppuccin.*

| Project | Stars | What it does |
|---|--:|---|
| [**shafiqimtiaz/herdr-omarchy**](https://github.com/shafiqimtiaz/herdr-omarchy) | 10 | Adds an Omarchy-inspired Herdr app layout with tiled terminals, agent status, quota, Git panels, themes and wallpapers. |
| [**CodeyPacker/herdr-mods**](https://github.com/CodeyPacker/herdr-mods) | 7 | Adds the Islands Herdr app layout and mods for workspace jumping, process control and agent-guided code tours. |
| [**MarcozVD/herdr-layout-catppuccin**](https://github.com/MarcozVD/herdr-layout-catppuccin) | 4 | Applies a Catppuccin layout to the Herdr app with Mocha and Latte colors that follow the system appearance. |
| [**othavi0/noctua-layout**](https://github.com/othavi0/noctua-layout) | 4 | Adds a graphite Herdr app layout with colored space cards, agent status indicators and Git information. |
| [**kyle-avrett/herdr-square-dracula**](https://github.com/kyle-avrett/herdr-square-dracula) | 4 | Applies a gapless Dracula layout to the Herdr app with compact tabs, a sidebar and file and changes panels. |
| [**Mayloparra24/gentle-herdr**](https://github.com/Mayloparra24/gentle-herdr) | 3 | Adds a Gentle Shell-themed Herdr app layout that syncs its colors with the selected Gentle Shell theme. |
| [**0OZ/coss-design**](https://github.com/0OZ/coss-design) | 2 | Dresses the Herdr app in a calm neutral dark layout inspired by shadcn dashboard-01, with one rounded card for the work area and a dashboard-style sidebar. |
| [**Calonca/herdr-orbit-look**](https://github.com/Calonca/herdr-orbit-look) | 2 | Gives the Herdr app a dark glassy look over a generated space picture, with a color and symbol for each space. |
| [**attractify-logan/herdr-snowleopard**](https://github.com/attractify-logan/herdr-snowleopard) | 2 | Restyles the Herdr app as Mac OS X 10.6 with a menu bar, Aqua windows, a source list and a Dock, where menus and Dock icons run real Herdr commands. Marked beta. |
| [**lamngockhuong/termote-herdr-layouts**](https://github.com/lamngockhuong/termote-herdr-layouts) | 2 | Adds three Herdr app layouts in the Termote neutral, terminal and native styles. Pane headers can open the pane in Termote, copy its link or show a QR code for a phone. |

**[All 55 projects →](catalog/02-herdr-app.md#herdr-app-palette-glass-and-desktop-os-themed-layouts)**

### Herdr app pixel-art, game, anime and cyberpunk layouts

*71 projects. Playful windows that turn agents into pixel-art coworkers, game characters, anime units or neon cyberpunk scenes.*

| Project | Stars | What it does |
|---|--:|---|
| [**franky5440-afk/herdr-traveler**](https://github.com/franky5440-afk/herdr-traveler) | 35 | Turns the Herdr app into a pixel RPG with agent portraits, status bars, and machine buildings. |
| [**DustyPolk/herdr-office**](https://github.com/DustyPolk/herdr-office) | 14 | Shows coding agents as animated coworkers above Herdr app terminals and jumps to their sessions when clicked. |
| [**kevinpardo/world-of-codecraft**](https://github.com/kevinpardo/world-of-codecraft) | 5 | Frames the Herdr app terminal in a high-fantasy MMO style with a pixel-art village that reflects agent activity, with Claude Code and OpenCode activity hooks. |
| [**vib-z/herdr-layouts**](https://github.com/vib-z/herdr-layouts) | 5 | Adds seven Herdr app layouts, including Control Panel, Falling Code, Fleet Tab, Night City, Queue, The Crew Board and The Noir Office. |
| [**isaacin42/herdr-layouts**](https://github.com/isaacin42/herdr-layouts) | 4 | Adds Herdr app layouts including Darkroom, Mixtape, Neon, Orienteering, Orrery, The Desk and The Pass for viewing and steering agents. |
| [**TwoD97/neon-borough**](https://github.com/TwoD97/neon-borough) | 3 | Adds a cyberpunk Herdr app layout with agent activity displays and panels for pull requests, file transfers, and secrets. |
| [**Jiqize/herdr-maid-adv**](https://github.com/Jiqize/herdr-maid-adv) | 3 | Turns the Herdr app into a visual-novel workspace where agent characters queue to speak when they finish or need input. |
| [**adamentwistle/herdr-departures**](https://github.com/adamentwistle/herdr-departures) | 3 | Turns the top of the Herdr app window into an airport split-flap board where each coding agent is a flight and agents that need you show as delayed. |
| [**Dylan0203/herdr-layout-eva**](https://github.com/Dylan0203/herdr-layout-eva) | 2 | Gives the Herdr app a late-90s command-center HUD look with cut-corner plates, live agent counts and seven-segment readouts of the host Mac CPU, memory, network and power. |
| [**evanhickman/herdr-layouts**](https://github.com/evanhickman/herdr-layouts) | 2 | Turns the Herdr app into a Roland TR-808 drum machine on the gruvbox palette, with tabs as colored step keys and agent status on LEDs. |

**[All 71 projects →](catalog/02-herdr-app.md#herdr-app-pixel-art-game-anime-and-cyberpunk-layouts)**

### Herdr app sidebars, tabs, and visual mods

*134 projects. Spaces and agents sidebars, tab naming and groups, pane headers, agent trees, chat views, and playful extras such as pixel pets, games, music players, and voice dictation.*

| Project | Stars | What it does |
|---|--:|---|
| [**sodiumsun/agenttrail · herdr/agenttrail**](https://github.com/sodiumsun/agenttrail/tree/main/herdr/agenttrail) | 1,009 | Shows a read-only project map beside Herdr app terminals, using PLAN.md or inferred Git branches and worktrees. |
| [**mathieucroset/herdr-pokemon-agents**](https://github.com/mathieucroset/herdr-pokemon-agents) | 25 | Shows agents as animated Pokémon in the Herdr app and lets users jump to an agent by clicking its sprite. |
| [**chappse6/herdr-blueprint-app**](https://github.com/chappse6/herdr-blueprint-app) | 14 | Displays agent-written Mermaid flowcharts beside Herdr app sessions and sends clicked diagram changes back to the agent. |
| [**mukiwu/herdr-crew-rpg**](https://github.com/mukiwu/herdr-crew-rpg) | 9 | Displays dispatched agents as pixel-art characters in a Herdr app sidebar and battle scene with status and quota information. |
| [**jonathan-fielding/herdr-project-coordinator**](https://github.com/jonathan-fielding/herdr-project-coordinator) | 8 | Adds a Projects sidebar to the Herdr app where a Claude Code coordinator delegates tasks to isolated workers and tracks their progress. |
| [**ChmaraX/herdr-chat**](https://github.com/ChmaraX/herdr-chat) | 8 | Adds a native chat interface in Herdr app tabs for Pi, Claude Code and Codex, with streamed messages and tool approval cards. |
| [**MarcozVD/herdr-agent-flow**](https://github.com/MarcozVD/herdr-agent-flow) | 7 | Maps agents, subagents and their messages in the current Herdr app space as a live diagram or timeline. |
| [**thuanlm215/herdr-float-space**](https://github.com/thuanlm215/herdr-float-space) | 7 | Adds a floating scratch window with terminal tabs and shared notes to the Herdr app. |
| [**funny-it-worked-last-time-gsv/herdr-sit-and-watch**](https://github.com/funny-it-worked-last-time-gsv/herdr-sit-and-watch) | 5 | Adds a Herdr app sidebar that depicts agents as robots at their desks. |
| [**naruse/herdr-chat**](https://github.com/naruse/herdr-chat) | 4 | Adds a chat interface for Claude Code and Codex agents in the Herdr app, with live replies and terminal access. |

**[All 134 projects →](catalog/02-herdr-app.md#herdr-app-sidebars-tabs-and-visual-mods)**

### Herdr app keys, navigation, and attention alerts

*102 projects. Keyboard shortcuts, pickers and switchers, the + menu agent list, session resume, mod managers, and alerts that tell you when an agent needs you.*

| Project | Stars | What it does |
|---|--:|---|
| [**atuinsh/herdr-atuin-threads**](https://github.com/atuinsh/herdr-atuin-threads) | 33 | Lists Atuin-captured coding-agent threads in the Herdr app and resumes a selected session in a new tab. |
| [**mrolafsson/herdr-recap**](https://github.com/mrolafsson/herdr-recap) | 13 | Lists agent recaps and blocked questions across machines in the Herdr app and Herdr TUI, with replies from the list. |
| [**ergunozyurt/herdr-super-agent**](https://github.com/ergunozyurt/herdr-super-agent) | 11 | Organizes a lead agent’s human decision requests into threaded inbox items in the Herdr app. |
| [**sachin-philip/herdr-agent-ask**](https://github.com/sachin-philip/herdr-agent-ask) | 11 | Collects every question your agents ask in a space, from permission dialogs to plain-text questions, into one side panel of cards in the Herdr app. |
| [**JinJieBeWater/herdr-t3-inbox**](https://github.com/JinJieBeWater/herdr-t3-inbox) | 10 | Adds an attention inbox to the Herdr app sidebar where users can settle finished agents and see them return when work resumes. |
| [**dmazlum/herdr-revive**](https://github.com/dmazlum/herdr-revive) | 9 | Restores supported coding-agent sessions after a Herdr app restart and forks conversations into adjacent panes. |
| [**sachin-philip/herdr-marks-as-unread**](https://github.com/sachin-philip/herdr-marks-as-unread) | 6 | Marks agents as unread in the Herdr TUI or Herdr app sidebar and clears the mark when users return. |
| [**benjaminsicard/herdr-mods**](https://github.com/benjaminsicard/herdr-mods) | 5 | Adds Herdr app mods for desktop notifications and automatic tab and space names. |
| [**CiprianSpiridon/herdr-migration**](https://github.com/CiprianSpiridon/herdr-migration) | 5 | Imports Herdr TUI workspaces, tabs, folders, and terminal splits into the Herdr app with backup and verification. |
| [**jankeesvw/herdr-focus-to-hover**](https://github.com/jankeesvw/herdr-focus-to-hover) | 5 | Focuses the Herdr app pane under the mouse pointer so users can type without clicking. |

**[All 102 projects →](catalog/02-herdr-app.md#herdr-app-keys-navigation-and-attention-alerts)**

### Herdr app usage, quota, and system status displays

*50 projects. Status bars and panels for subscription quota, token cost, context size, and machine resource use.*

| Project | Stars | What it does |
|---|--:|---|
| [**GaganSD/coding-agent-toolkit · herdr-insights**](https://github.com/GaganSD/coding-agent-toolkit/tree/main/herdr-insights) | 49 | Shows local token usage and model activity for Pi, Codex, Claude Code, OpenCode and Antigravity in a Herdr app dashboard. |
| [**nozikov/herdr-usage-limits**](https://github.com/nozikov/herdr-usage-limits) | 6 | Shows Claude Code and Codex subscription limits and session context in the Herdr app status bar. |
| [**mrolafsson/herdr-vitals**](https://github.com/mrolafsson/herdr-vitals) | 6 | Shows machine CPU, memory, disk and network activity in a Herdr app window or Herdr TUI popup, with resource alerts. |
| [**dev-gvs/herdr-claude-usage**](https://github.com/dev-gvs/herdr-claude-usage) | 3 | Shows Claude plan usage and reset times in the Herdr app status bar. |
| [**adamentwistle/limit-runway · herdr**](https://github.com/adamentwistle/limit-runway/tree/main/herdr) | 3 | Adds a Herdr app panel for monitoring Claude Code and Codex plan limits and pausing or resuming agents through the Runway CLI. |
| [**riyhs/herdr-bottom-bar-stats**](https://github.com/riyhs/herdr-bottom-bar-stats) | 2 | Adds a bottom status bar showing the active machine name with CPU, memory, disk and ping, following the active space so remote spaces show their own numbers. |
| [**0xRowdy/herdr-cliproxy**](https://github.com/0xRowdy/herdr-cliproxy) | 2 | Adds two floating windows for a CLIProxyAPI server: one with health, throughput and live provider quota, and a lighter one with account status and everyday account actions. |
| [**adamentwistle/herdr-wrapped**](https://github.com/adamentwistle/herdr-wrapped) | 2 | Opens an overlay in the Herdr app with a shareable card of your Claude Code stats. Shows tokens, cost, busiest day and peak parallel agents, read from local transcripts. |
| [**werlang/herdr-usage-status**](https://github.com/werlang/herdr-usage-status) | 2 | Adds one usage gauge to the Herdr app bottom status bar that opens a panel with every available subscription limit. Covers Claude, Antigravity, and other providers, and hides those without data. |
| [**e-kotov/herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit) | 1 | Shows prompt-cache metrics and expiration alerts in Herdr TUI, with an experimental display-only Herdr app mod. |

**[All 50 projects →](catalog/02-herdr-app.md#herdr-app-usage-quota-and-system-status-displays)**

### Herdr app Git, code review, and worktree panels

*69 projects. Git graphs, diff and branch review, pull-request and merge-request lists, and worktree helpers inside the Herdr app.*

| Project | Stars | What it does |
|---|--:|---|
| [**rabeeh-ta/herdr-git-graph**](https://github.com/rabeeh-ta/herdr-git-graph) | 34 | Shows a Git commit graph in the Herdr app and offers branch, merge, rebase, and other repository actions. |
| [**iampedii/herdr-redline**](https://github.com/iampedii/herdr-redline) | 30 | Reviews GitHub pull requests and GitLab merge requests in the Herdr app with worktree checkout, diffs, and inline comments. |
| [**vytasgavelis/herdr-reviewer**](https://github.com/vytasgavelis/herdr-reviewer) | 16 | Adds syntax-colored diffs and inline review comments to the Herdr app Changes panel and sends comments to an agent. |
| [**jjangsky/herdr-pr-flow**](https://github.com/jjangsky/herdr-pr-flow) | 10 | Shows agent pull requests in a Herdr app panel with CI, review and post-merge workflow status, plus optional merge and diff comments. |
| [**jakub-tucek/herdr-annotator**](https://github.com/jakub-tucek/herdr-annotator) | 9 | Adds code review to the Herdr app with branch and working-tree diffs, inline comments and GitHub pull-request threads for local or SSH worktrees. |
| [**dmazlum/herdr-walkthrough**](https://github.com/dmazlum/herdr-walkthrough) | 9 | Uses Claude Code to turn a repository diff into an ordered, explained walkthrough in the Herdr app. |
| [**LaiqianDS/herdr-mods**](https://github.com/LaiqianDS/herdr-mods) | 6 | Adds a Herdr app Git panel for diffs, staging, commits and branch switching, alongside a file-icons mod. |
| [**aBER0724/herdr-git-changes**](https://github.com/aBER0724/herdr-git-changes) | 5 | Adds a Herdr app Git panel for staging, commits, stashes, history, and diff inspection. |
| [**ashrodan/ship-it**](https://github.com/ashrodan/ship-it) | 3 | Adds pull request status, checks, review threads, and change inspection to the Herdr app. |
| [**lw396/herdr-plugin-github**](https://github.com/lw396/herdr-plugin-github) | 2 | Browses, reads and reviews the Issues and Pull Requests of the current repository in a side panel, modeled on the VS Code GitHub Pull Requests extension. Uses the gh CLI on the machine that hosts the folder. |

**[All 69 projects →](catalog/02-herdr-app.md#herdr-app-git-code-review-and-worktree-panels)**

### Herdr app file, Markdown, and notes panels

*56 projects. Files panels, file previews, Markdown readers, editors, and note-taking panes beside your terminals.*

| Project | Stars | What it does |
|---|--:|---|
| [**CacaoRick/herdr-open-vscode**](https://github.com/CacaoRick/herdr-open-vscode) | 7 | Opens the focused Herdr app terminal folder in VS Code locally or through Remote SSH, including SSH-connected WSL. |
| [**linziyanleo/herdr-mods**](https://github.com/linziyanleo/herdr-mods) | 6 | Adds Herdr app mods for multi-root file browsing, file previews and editing, and mod and layout management. |
| [**Abrahamism/herdr-browser**](https://github.com/Abrahamism/herdr-browser) | 4 | Controls a dedicated Chromium browser through CDP and adds a Herdr app panel for listing and switching its tabs. |
| [**Srv-02/herdr-filerpro**](https://github.com/Srv-02/herdr-filerpro) | 4 | Adds a Herdr app file panel for browsing and transferring files on local and SSH machines. |
| [**anderssonq/herdsidian**](https://github.com/anderssonq/herdsidian) | 4 | Adds an Obsidian vault sidebar to the Herdr app for browsing and editing notes beside agents. |
| [**ryanthedev/herdr-md**](https://github.com/ryanthedev/herdr-md) | 3 | Renders a Markdown file natively in a Herdr app pane with theme colors, real heading sizes, tables, task lists, callouts and images. |
| [**amster93/herdr-file-icons**](https://github.com/amster93/herdr-file-icons) | 2 | Replaces the Files panel with one that shows VS Code Material Icon Theme icons for files and folders. |
| [**vladimiryakimenko/herdr-files-transfer**](https://github.com/vladimiryakimenko/herdr-files-transfer) | 2 | Replaces the Files panel with one that downloads, uploads, renames, moves to Trash or deletes files from a right-click menu, locally and on remote machines over SSH, with VS Code file icons. |
| [**napalmpapalam/herdr-find-in-files**](https://github.com/napalmpapalam/herdr-find-in-files) | 2 | Searches the focused terminal repo with ripgrep in a JetBrains-style dialog, showing hits as you type with a preview of the selected lines. |
| [**vedovato/terminal-browser-qa-walk**](https://github.com/vedovato/terminal-browser-qa-walk) | 2 | Opens a terminal-browser window beside your terminals from a popup where you type a URL and choose where it opens. |

**[All 56 projects →](catalog/02-herdr-app.md#herdr-app-file-markdown-and-notes-panels)**

### Herdr app task boards, developer services, and mod bundles

*116 projects. Issue and task boards, cloud, database, and deployment panels, chat, mail, and remote-machine panels, and multi-mod bundles that add several features at once.*

| Project | Stars | What it does |
|---|--:|---|
| [**runkids/skillshare · herdr/skillshare**](https://github.com/runkids/skillshare/tree/main/herdr/skillshare) | 3,007 | Adds a Herdr app layout with a skillshare panel for viewing, auditing and syncing skills, agents, MCP servers, plugins and hooks. |
| [**fatwang2/Pulse · herdr**](https://github.com/fatwang2/Pulse/tree/main/herdr) | 121 | Adds a stock and crypto watchlist mod and a matching Herdr app layout with a docked price panel. |
| [**wobsoriano/herdr-sim**](https://github.com/wobsoriano/herdr-sim) | 34 | Opens an interactive iOS simulator or Android emulator beside code and terminals in the Herdr app. |
| [**jankeesvw/herdr-issues**](https://github.com/jankeesvw/herdr-issues) | 17 | Adds a GitHub issues panel to the Herdr app for reading, commenting on, assigning, and closing issues. |
| [**SaifHarding/herdr-cloudflare**](https://github.com/SaifHarding/herdr-cloudflare) | 15 | Shows Cloudflare Pages and Workers deployment status in the Herdr app header and reports failed deployments. |
| [**runkids/figlens · herdr**](https://github.com/runkids/figlens/tree/main/herdr) | 15 | Adds a figlens layout and panel for viewing local Figma designs and handing screens to agents in the Herdr app. |
| [**greenflagged/herdr-forge**](https://github.com/greenflagged/herdr-forge) | 12 | Opens GitHub or GitLab project panels in the Herdr app and hands issues or merge requests to agents. |
| [**greenflagged/herdr-greenflagged**](https://github.com/greenflagged/herdr-greenflagged) | 10 | Displays project dependency trees in the Herdr app and optionally marks npm dependencies with Greenflagged review verdicts. |
| [**cybertron288/herdr-mods**](https://github.com/cybertron288/herdr-mods) | 8 | Adds Herdr app mods for file browsing, GitHub Actions, JavaScript scripts, session status, Slack and YouTube Music. |
| [**ernestjsf/herdr-devices**](https://github.com/ernestjsf/herdr-devices) | 6 | Adds a Herdr app side panel for iOS and Android devices and simulators, with device actions and Maestro flow runs. |

**[All 116 projects →](catalog/02-herdr-app.md#herdr-app-task-boards-developer-services-and-mod-bundles)**

### Herdr app themes

*8 projects. Color themes and palettes that recolor the Herdr app window, including theme generators and editors.*

| Project | Stars | What it does |
|---|--:|---|
| [**Codesmith28/gruvbox-herdr-app**](https://github.com/Codesmith28/gruvbox-herdr-app) | 3 | Adds six Gruvbox themes and a contrast-switching mod to the Herdr app. |
| [**alvaroroco/herdr-omarchy-theme**](https://github.com/alvaroroco/herdr-omarchy-theme) | 2 | Adds an omarchy theme to Herdr app Settings that is rewritten from the active Omarchy palette on every theme change, plus a small status pill. |
| [**pedroparra/herdr-monokai**](https://github.com/pedroparra/herdr-monokai) | 1 | Recolors the Herdr desktop app's main window in the classic Monokai palette, with agent states in Monokai yellow, pink and cyan and an orange ring on the focused pane. Adds Monokai and Monokai Dimmed themes that work in any layout, with no mods or code. |
| [**dtellz/dtellz-dark**](https://github.com/dtellz/dtellz-dark) | 1 | Adds a near-black Herdr app theme with white text and vivid syntax colors. Includes a copy of the standard layout that uses it. |
| [**douglasjarquin/sf2-themes**](https://github.com/douglasjarquin/sf2-themes) | 0 | Installs Street Fighter II color themes for the Herdr app and Herdr TUI as well as several other developer tools. |
| [**jdlewin/herdr-omarchy-theme**](https://github.com/jdlewin/herdr-omarchy-theme) | 0 | Generates a Herdr app theme from the active Omarchy theme and refreshes it whenever you run omarchy theme set. Installs a sync hook and a layout that applies the theme. |
| [**agentic-tool-labs/herdr-theme-studio**](https://github.com/agentic-tool-labs/herdr-theme-studio) | 0 | Edits the Herdr app's look in one window: pick or import a theme, adjust its colors, choose terminal and panel fonts, and style the agents list, with a live preview before saving. |
| [**suree33/herdr-app**](https://github.com/suree33/herdr-app) | 0 | Adds Catppuccin themes for the Herdr app in Latte, Frappe, Macchiato, and Mocha, with previews. |

---

## 3. Connect through MCP and the socket API

*333 projects. Protocols, clients, bots, and event bridges that link Herdr to external tools, editors, and messaging apps.* The top 10 of each subcategory by stars are below; the full list is in [catalog/03-mcp-and-socket-api.md](catalog/03-mcp-and-socket-api.md).

### MCP servers

*21 projects. Servers that expose Herdr operations as MCP tools for compatible AI clients.*

| Project | Stars | What it does |
|---|--:|---|
| [**runchr-works/herdr-mesh**](https://github.com/runchr-works/herdr-mesh) | 13 | Connects multiple Herdr instances into a coordinated mesh over Model Context Protocol. |
| [**rmngl/herdr-mesh**](https://github.com/rmngl/herdr-mesh) | 13 | Exposes Herdr pane management, agent messaging, and contextual handoffs through an MCP server. |
| [**whshang/herdr-mcp**](https://github.com/whshang/herdr-mcp) | 10 | Adds a stable MCP and OAuth bridge for remote web planners to inspect and control local Herdr workspaces. |
| [**ryanthedev/herderp**](https://github.com/ryanthedev/herderp) | 5 | Adds Claude Code MCP tools for managing agents and terminals across Herdr TUI and herdr-core, including remote hosts and session history. |
| [**aquaherd/goose-herdr**](https://github.com/aquaherd/goose-herdr) | 3 | Connects Goose to Herdr TUI through an MCP extension and reports Goose lifecycle state to the sidebar. |
| [**eugeneb50/herdr-mcp**](https://github.com/eugeneb50/herdr-mcp) | 2 | Exposes Herdr workspace and pane controls as tools to any Model Context Protocol (MCP) client. |
| [**54rt1n/herdr-simple-mcp**](https://github.com/54rt1n/herdr-simple-mcp) | 2 | Provides a lightweight Model Context Protocol server for driving Herdr from Claude Desktop and Cursor. |
| [**Orange-County-AI/herdr-mcp**](https://github.com/Orange-County-AI/herdr-mcp) | 2 | Exposes Herdr's socket API as a local or remote MCP server. |
| [**thomasfossum/herdr-mcp**](https://github.com/thomasfossum/herdr-mcp) | 2 | Lets MCP clients control a running Herdr session: see agent status, open tabs and panes, start agents, send them work and run worktree-isolated jobs. Runs over stdio or Streamable HTTP in standard-library Python with Docker and client examples. |
| [**nytafar/herdr-spawn**](https://github.com/nytafar/herdr-spawn) | 1 | Exposes an MCP tool that starts coding agents on your machines from a chat prompt, with a Claude Code Remote Control link when available. |

**[All 21 projects →](catalog/03-mcp-and-socket-api.md#mcp-servers)**

### Socket API and herdr-core clients and SDKs

*40 projects. Clients, libraries, and command-line tools for Herdr TUI and herdr-core APIs.*

| Project | Stars | What it does |
|---|--:|---|
| [**backpine/remote-agent-workspace**](https://github.com/backpine/remote-agent-workspace) | 64 | Provides an always-on remote agent environment: edit on macOS, run Herdr work on Linux, synchronize files with Syncthing, and expose services through Cloudflare Tunnel and Caddy. |
| [**dmmulroy/herdr-ts-sdk**](https://github.com/dmmulroy/herdr-ts-sdk) | 57 | Provides an Effect-native TypeScript SDK for Herdr's local protocol-21 socket API. |
| [**0xGosu/herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot) | 31 | Prompts a running coding CLI through the Herdr API. A training mode observes user actions, safety checks block dangerous operations, and an optional autonomous mode can continue prompting after sufficient setup. |
| [**mitkox/dsh-herdr**](https://github.com/mitkox/dsh-herdr) | 17 | Reports DeepSeek Harness agent state to herdr-core via OSC 7501 and displays sessions in a Herdr app panel. |
| [**Mic92/herdr-eternal**](https://github.com/Mic92/herdr-eternal) | 13 | A roaming-friendly transport for `herdr --remote` using QUIC with a WebSocket fallback, exact byte-stream resumption, and OIDC authentication. |
| [**ryonakae/shepherd**](https://github.com/ryonakae/shepherd) | 11 | A worker-observability service and set of runtime bridges for coding agents managed by Herdr. |
| [**TheMetalStorm/herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin) | 10 | Integrates Freebuff agents with Herdr by reading PTY output and local session files, then reporting idle, working, and blocked states through the socket API. |
| [**gejiliang/herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw) | 5 | Treats OpenClaw TUI sessions as Herdr agents, with live state, model information, and token use in the sidebar. A background watcher parses OpenClaw status lines and reports them through the socket API. |
| [**54rt1n/herdr-python-client**](https://github.com/54rt1n/herdr-python-client) | 3 | Provides typed Python bindings and socket utilities for automating Herdr programmatically. |
| [**usrivastava92/herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup) | 3 | Prevents macOS or Linux from sleeping while Herdr agents are working. It enables an operating-system sleep inhibitor when activity begins and releases it when every agent is idle. |

**[All 40 projects →](catalog/03-mcp-and-socket-api.md#socket-api-and-herdr-core-clients-and-sdks)**

### Chat alerts: Telegram, Discord, and Slack

*33 projects. Bot and channel alerts that ping you when agents finish or need input.*

| Project | Stars | What it does |
|---|--:|---|
| [**alexei-led/ccgram**](https://github.com/alexei-led/ccgram) | 289 | Maps forum topics to terminal windows running Claude Code, Codex, Gemini, Pi, or a shell. It relays output and input through Herdr or tmux so sessions remain usable from a phone. |
| [**permgps/herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents) | 87 | Creates a Telegram forum topic for each Herdr agent so users can receive status updates and reply to prompts. |
| [**dcolinmorgan/herdr-push**](https://github.com/dcolinmorgan/herdr-push) | 10 | Forwards agent status changes to the herdr-remote relay using only curl and system Python or jq. A single relay setting enables mobile, menu-bar, or Telegram monitoring, and a test action checks the connection. |
| [**natori-hrj/herdr-hail**](https://github.com/natori-hrj/herdr-hail) | 7 | Connects Herdr to Slack and Discord through a two-way webhook bridge. Blocked-agent alerts can be answered through replies or action buttons without opening a network tunnel. |
| [**gaijinjoe/herdres**](https://github.com/gaijinjoe/herdres) | 7 | Maps every live Herdr pane to a Telegram forum topic. Agent activity appears in the topic, and bot commands can send input back to the matching pane from any device. |
| [**mvallebr/herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin) | 6 | A Telegram bot companion that maps Herdr agents to forum topics and provides remote control without placing an LLM between the user and the pane. |
| [**etinpres/herdr-telegram-remote**](https://github.com/etinpres/herdr-telegram-remote) | 4 | Controls Codex and Claude Code panes in Herdr from Telegram. |
| [**TerrifiedBug/omp-telegram**](https://github.com/TerrifiedBug/omp-telegram) | 4 | Connects Oh My Pi sessions to Telegram and uses Herdr to spawn and manage sessions remotely. |
| [**cokekitten/herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge) | 4 | Sends Telegram notifications when an agent finishes or waits for input. Replies, including files, are delivered to the correct pane without requiring a public server or port tunnel. |
| [**hkdom/herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate) | 3 | Sends blocked Herdr agent approvals to Telegram and supports risk-tiered automatic approval policies. |

**[All 33 projects →](catalog/03-mcp-and-socket-api.md#chat-alerts-telegram-discord-and-slack)**

### Desktop, mobile, and webhook notifications

*72 projects. Desktop notifications, mobile push alerts, and webhook triggers for agent events.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**yankewei/herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify) | 34 | Shows a clickable macOS notification when an unseen pane becomes blocked or finishes. Clicking the alert brings the terminal forward and focuses the exact pane through `alerter`. |
| [**TheMetalStorm/herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin) | 14 | Integrates Command Code as a Herdr agent runtime with process detection, idle, working, and blocked status, session recovery after server restarts, and toast alerts when input is needed. |
| [**dot/herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier) | 13 | Bundles a branded macOS notification app so Herdr alerts use the correct icon and can jump to the relevant pane. The app periodically refreshes its Launch Services registration to recover cleanly after reboots or updates. |
| [**horn553/herdr-ntfy**](https://github.com/horn553/herdr-ntfy) | 9 | Sends ntfy alerts for done and blocked agent states using standard command-line tools and curl. |
| [**zom-2018/herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify) | 8 | Sends structured ntfy alerts when an agent blocks or finishes. Notifications include the workspace, tab, and pane, and the plugin prefers a detected local ntfy server before using the network. |
| [**justinchiasson/herdr-nudge**](https://github.com/justinchiasson/herdr-nudge) | 6 | Sends clickable macOS notifications when an agent is blocked or done, or when a long zsh command finishes, and clicking one focuses that pane in Herdr. Works on Intel and Apple Silicon with nothing else to install, and withdraws notifications for panes that move on or close. |
| [**winoooops/herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher) | 6 | Adds live sidebar cards, lifecycle alerts, and a zero-configuration Claude Code metrics bridge for Herdr agents. |
| [**nhclink16/herdr-announcer**](https://github.com/nhclink16/herdr-announcer) | 5 | Speaks a one-sentence AI summary when an agent finishes or needs input. It supports local text-to-speech, ElevenLabs, or any custom command. |
| [**aclima01/herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows) | 4 | Sends native Windows 11 toast notifications when a Herdr agent finishes a turn or asks for input. |
| [**hmu332233/herdr-pets**](https://github.com/hmu332233/herdr-pets) | 4 | Shows macOS desktop pets for Herdr TUI agents that move to your pointer when an agent is blocked. |

**[All 72 projects →](catalog/03-mcp-and-socket-api.md#desktop-mobile-and-webhook-notifications)**

### Telemetry, events, and quota streaming

*32 projects. Event collectors and monitors for agent state, usage, cost, and runtime activity.*

| Project | Stars | What it does |
|---|--:|---|
| [**DIodide/herdr-telemetry**](https://github.com/DIodide/herdr-telemetry) | 12 | Sends workspace and agent telemetry to an endpoint chosen by the user. It removes tokens, redacts sensitive prompts, and ships as a single binary. |
| [**Ziy1-Tan/herdr-codebuddy**](https://github.com/Ziy1-Tan/herdr-codebuddy) | 7 | Reports CodeBuddy session, working and permission states to Herdr TUI through hooks. |
| [**Gilamonster-Foundation/newt-agent · newt-tui/src/herdr**](https://github.com/Gilamonster-Foundation/newt-agent/tree/main/newt-tui/src/herdr) | 6 | Reports Newt coding-agent lifecycle states to the Herdr TUI from a pane using its socket API. |
| [**leonardoacosta/herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode) | 5 | Reports Jcode working and idle lifecycle states and session identity to Herdr TUI. |
| [**dsh-blue/herdr-agent-state**](https://github.com/dsh-blue/herdr-agent-state) | 2 | Reports DeepSeek Harness lifecycle state, session references, and model metadata to the current Herdr pane. |
| [**CodyBontecou/herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge) | 2 | Streams structured Herdr activity as NDJSON, including pane focus time, detected agent and model details, and local session summaries. Output can go to a file, webhook, or command, and transcript text is hidden by default. |
| [**vishnutskumar/herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics) | 2 | Analyzes memex session history and shows efficiency guidance for Herdr TUI agents. |
| [**cpcloud/herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview) | 2 | Combines active AgentsView sessions across projects, models, and agents, with real-time timelines and metrics inside Herdr. |
| [**akshat12/herdr-muse**](https://github.com/akshat12/herdr-muse) | 2 | Reports Muse Code working, idle, and blocked states to Herdr TUI through lifecycle hooks. |
| [**Comamoca/command-code-herdr**](https://github.com/Comamoca/command-code-herdr) | 2 | Reports Command Code working, idle, and blocked lifecycle states to Herdr TUI through its local socket. |

**[All 32 projects →](catalog/03-mcp-and-socket-api.md#telemetry-events-and-quota-streaming)**

### Voice, hardware, and remote bridges

*57 projects. Interfaces that connect Herdr to spoken input, physical devices, or remote control surfaces.*

| Project | Stars | What it does |
|---|--:|---|
| [**klarluft/pitupitu**](https://github.com/klarluft/pitupitu) | 223 | Connects phone and browser voice conversations to coding agents running in Herdr TUI. |
| [**T0mSIlver/localvoxtral**](https://github.com/T0mSIlver/localvoxtral) | 64 | Fully local, real-time dictation for Apple Silicon Macs. It streams speech into the coding-agent session under the cursor, including Claude Code inside a Herdr pane, and uses that session as context for optional text polishing. |
| [**schacon/micro-manager**](https://github.com/schacon/micro-manager) | 41 | Uses the Creator Micro 2 hardware controller to operate Herdr. |
| [**brogrammerMW/herdr-voice**](https://github.com/brogrammerMW/herdr-voice) | 32 | Lets users speak to agents in Herdr TUI panes and hear replies using local OpenLive or realtime xAI, OpenAI, and Google models. |
| [**kccarlos/herdr-sheepdog**](https://github.com/kccarlos/herdr-sheepdog) | 15 | Monitors and steers Herdr agents by voice from an iPhone app or a Herdr app layout and panel. |
| [**second-state/vibetty**](https://github.com/second-state/vibetty) | 11 | Streams live Herdr terminal screens over MQTT to devices such as VibeKeys and VibeWatch and relays keystrokes back. It includes an MQTT broker and integrates with Herdr's command palette and status bar. |
| [**pawaca/even-better**](https://github.com/pawaca/even-better) | 6 | Mirrors Claude Code and Codex sessions in Herdr TUI to Even Realities G2 glasses and sends prompts back to the pane. |
| [**htlin222/herdr-gamepad**](https://github.com/htlin222/herdr-gamepad) | 6 | Maps Xbox, PlayStation, and 8BitDo controller buttons to Herdr actions through macOS GameController, enabling workspace and pane control away from the keyboard. |
| [**miko-misa/herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd) | 5 | Forwards remote agent development-server ports to the local machine and opens them after confirmation. |
| [**aneym/herdr-voice**](https://github.com/aneym/herdr-voice) | 5 | Controls workspaces, pane splits, and agent dispatch with spoken commands through OpenAI's Realtime API. A floating display shows the transcription and asks for confirmation before sending instructions. |

**[All 57 projects →](catalog/03-mcp-and-socket-api.md#voice-hardware-and-remote-bridges)**

### Protocol and third-party bridges

*78 projects. Adapters between Herdr and other multiplexers, platforms, messaging systems, or automation protocols.*

| Project | Stars | What it does |
|---|--:|---|
| [**openclaw/crabbox**](https://github.com/openclaw/crabbox) | 1,527 | Adds Crabbox sandbox provisioning and remote test execution to Herdr. Plugin actions can prewarm temporary environments, synchronize diffs, and inspect active leases from an overlay. |
| [**27medkamal/tmux-agent-wizard**](https://github.com/27medkamal/tmux-agent-wizard) | 21 | Brings Herdr agent detection and compatible CLI-driven plugins to tmux. |
| [**RaviTharuma/cmux-herdr**](https://github.com/RaviTharuma/cmux-herdr) | 16 | Shows Herdr TUI pane viewers and agent status pills inside cmux using external attachment. |
| [**benkraus/herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay) | 11 | Bridges Herdr TUI socket operations to HTTP and WebSocket clients, including a browser interface and optional Tailscale publishing. |
| [**neon-solutions/neon-herdr**](https://github.com/neon-solutions/neon-herdr) | 11 | Embeds a serverless Postgres dashboard in a Herdr pane. It can create database branches per agent worktree, start or stop compute, and insert connection strings. |
| [**lachieh/herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux) | 11 | Mirrors Herdr TUI agents into the cmux sidebar with status, task text, and click-to-focus navigation. |
| [**HexSleeves/herdr-warp**](https://github.com/HexSleeves/herdr-warp) | 9 | Opens live Herdr TUI agents as native Warp panes on macOS. |
| [**agentwireprotocol/awp · plugin/herdr**](https://github.com/agentwireprotocol/awp/tree/main/plugin/herdr) | 8 | Connects Herdr TUI agents to Agent Wire Protocol messaging with inbox panes, notifications and idle-agent delivery. |
| [**wenxichang/herdr-pal**](https://github.com/wenxichang/herdr-pal) | 7 | Connects Herdr TUI agents across machines to a WeCom bot for session selection, task submission, terminal output, and limited key input. |
| [**Poor-Plebs/herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes) | 7 | Opens SSH terminals for hosts from SSH configuration in separate Herdr TUI workspaces. |

**[All 78 projects →](catalog/03-mcp-and-socket-api.md#protocol-and-third-party-bridges)**

---

## 4. Editor integrations

*106 projects. Bridges and pane synchronizers that let you drive Herdr agents directly from your code editor.* The top 10 of each subcategory by stars are below; the full list is in [catalog/04-editors.md](catalog/04-editors.md).

### Neovim navigation and splits

*30 projects. Plugins that make movement between Neovim windows and Herdr panes feel continuous.*

| Project | Stars | What it does |
|---|--:|---|
| [**paulbkim-dev/vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation) | 115 | Ports vim-tmux-navigator behavior to Herdr. Direction keys move within Vim or Neovim until an edge is reached, then shift focus to the adjacent Herdr pane based on the pane's foreground process. |
| [**lmilojevicc/herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim) | 69 | Bridges Neovim split navigation and smart pane resizing with Herdr terminal panes. |
| [**aimdevlee/herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav) | 22 | Moves between Neovim splits and Herdr TUI panes with shared Ctrl+h/j/k/l bindings and socket-based focus tracking. |
| [**nettlesh/dotfiles**](https://github.com/nettlesh/dotfiles) | 18 | Personal Alacritty, Fish, Herdr, and Neovim dotfiles with workspace navigation and agent-dispatch configuration. |
| [**luneth90/keycade**](https://github.com/luneth90/keycade) | 12 | Provides a shortcut recall arcade for Omarchy, herdr, tmux, Vim, Neovim and LazyVim, six cabinets, each with its own deck, progress and mastery. |
| [**devxplay/herdr.nvim**](https://github.com/devxplay/herdr.nvim) | 11 | Navigates Neovim splits and Herdr TUI panes with Ctrl+h/j/k/l using a pane marker and a companion navigator. |
| [**bojackduy/nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation) | 7 | Applies vim-tmux-navigator-style directional keys across internal splits and surrounding Herdr panes. |
| [**kaar/nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator) | 6 | Uses one set of `Ctrl+h/j/k/l` shortcuts to move through both Neovim splits and Herdr panes. |
| [**willfish/herdr-navigator**](https://github.com/willfish/herdr-navigator) | 4 | Provides the Herdr-side actions needed for shared Vim or Neovim navigation. It checks the active pane process and either forwards the key to the editor or moves Herdr focus. |
| [**odiumuniverse/herdr-smart-nav**](https://github.com/odiumuniverse/herdr-smart-nav) | 4 | Moves between Neovim windows, Herdr TUI panes, tabs and workspaces with directional shortcuts. |

**[All 30 projects →](catalog/04-editors.md#neovim-navigation-and-splits)**

### Full Neovim-hosted workspaces

*4 projects. A deeper integration that uses Neovim as the main interface while Herdr owns the agent processes.*

| Project | Stars | What it does |
|---|--:|---|
| [**raymondware/herdr.nvim**](https://github.com/raymondware/herdr.nvim) | 5 | Opens the Herdr TUI in a Neovim floating terminal and shows agent states in a status window and statusline component. |
| [**MomePP/herd.nvim**](https://github.com/MomePP/herd.nvim) | 3 | Uses Neovim as the primary dashboard to launch, monitor, and control background Herdr agent sessions. |
| [**ctbaum/herdr-deck**](https://github.com/ctbaum/herdr-deck) | 2 | Adds the companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovim, agent, shell, and lazygit deck. |
| [**romerramos/herdr-reviewr-nvim**](https://github.com/romerramos/herdr-reviewr-nvim) | 0 | Opens Reviewr files in the Neovim pane for the current HERDR workspace. |

### VS Code, Cursor, and dev containers

*16 projects. Extensions and environment setups for graphical editors and container-based development.*

| Project | Stars | What it does |
|---|--:|---|
| [**zenbu-labs/terminal-code · herdr-plugin**](https://github.com/zenbu-labs/terminal-code/tree/main/herdr-plugin) | 2,247 | Adds an action that opens terminal-code, a VS Code-style editor for the terminal, in a split to the right of the focused pane in Herdr TUI. The plugin installs the tode binary when it builds. |
| [**scott-the-programmer/vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr) | 16 | Forwards Herdr's Unix socket into VS Code development containers through a loopback TCP bridge, allowing containerized agents to report status and receive commands from the host Herdr instance. |
| [**gambtho/herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer) | 12 | Starts shells and coding agents inside a repository's Dev Container through the official Dev Containers CLI and presents them as normal Herdr panes. |
| [**timofey-TK/herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor) | 5 | Opens the active Herdr workspace in VS Code or Zed with one shortcut. Local and SSH-remote workspaces are translated into the correct editor URI automatically. |
| [**mkellerman/herdex**](https://github.com/mkellerman/herdex) | 3 | Displays Herdr TUI workspaces and agent status in VS Code, with a terminal and editor actions. |
| [**alex-devdone/herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open) | 1 | Opens the focused Herdr pane's project in Cursor or VS Code, including remote panes through the editor's Remote SSH support. |
| [**mrshll/herdr-container-agents**](https://github.com/mrshll/herdr-container-agents) | 1 | Detects coding agents running inside containers and report them as herdr agents. |
| [**phine-apps/herdr-collie**](https://github.com/phine-apps/herdr-collie) | 0 | Bridges VS Code and Herdr to orchestrate AI agents, Git worktrees, and context sharing directly from the editor. |
| [**clement-micol/herdr-bridge**](https://github.com/clement-micol/herdr-bridge) | 0 | Bridges from herdr panes to VS Code: attach herdr terminals via vscode:// URIs. |
| [**endoumame/herdr-vscode**](https://github.com/endoumame/herdr-vscode) | 0 | Adds an inline code-review workflow to VS Code for work associated with Herdr agent sessions. The source description is incomplete beyond writing comments where the code is read. |

**[All 16 projects →](catalog/04-editors.md#vs-code-cursor-and-dev-containers)**

### Vim, Kakoune, and other editors

*13 projects. Navigation and workflow integrations for editors outside Neovim and VS Code.*

| Project | Stars | What it does |
|---|--:|---|
| [**ImArtisann/zed-herdr**](https://github.com/ImArtisann/zed-herdr) | 36 | Keeps Zed projects synchronized with Herdr workspaces by listening to lifecycle events over the Unix socket. It supports reconnection and full snapshot synchronization after interruptions. |
| [**roman/herdr.el**](https://github.com/roman/herdr.el) | 7 | Provides an Emacs porcelain interface for managing Herdr workspaces and agent sessions. |
| [**ionrock/ghostherd**](https://github.com/ionrock/ghostherd) | 3 | Manages Herdr agent terminals from Emacs through ghostel. |
| [**baongoc124/emacs-herdr**](https://github.com/baongoc124/emacs-herdr) | 3 | Runs the Herdr TUI in an Emacs Ghostel buffer and adds agent switching, project launches, and code dispatch. |
| [**Schaitanya535/herdr-config**](https://github.com/Schaitanya535/herdr-config) | 1 | A personal Herdr configuration with custom keys, a theme, and a helper that sends scrollback into Neovim. |
| [**T0mSIlver/hither**](https://github.com/T0mSIlver/hither) | 0 | Opens the active remote Herdr directory in Zed on macOS with a single key chord. |
| [**Yukaii/herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup) | 0 | Runs Kakoune terminal commands in native Herdr popups. |
| [**Yukaii/herdr.kak**](https://github.com/Yukaii/herdr.kak) | 0 | Controls Herdr panes, tabs, focus, and popups from Kakoune. |
| [**AVGVSTVS96/vim-herdr-navigator**](https://github.com/AVGVSTVS96/vim-herdr-navigator) | 0 | Moves between Vim or Neovim splits and Herdr TUI panes with shared directional shortcuts. |
| [**eddof13/herdr.el**](https://github.com/eddof13/herdr.el) | 0 | Controls Herdr from Emacs while hosting Herdr's terminal sessions inside Emacs through ghostel. |

**[All 13 projects →](catalog/04-editors.md#vim-kakoune-and-other-editors)**

### REPL and code dispatchers

*8 projects. Tools for sending code or commands from an editor to a running pane or interactive session.*

| Project | Stars | What it does |
|---|--:|---|
| [**francjpd/broadmand**](https://github.com/francjpd/broadmand) | 3 | Broadcasts shell commands or a selected working directory to panes in the active Herdr TUI workspace. |
| [**exviolet/sendoff**](https://github.com/exviolet/sendoff) | 2 | Edits prompts in a Linux desktop app and sends them to terminal agents running in Herdr, tmux, or Orca. |
| [**jcarlos7121/herdr-sidekick-agents.nvim**](https://github.com/jcarlos7121/herdr-sidekick-agents.nvim) | 1 | Opens Claude Code, Codex, or Grok in side-by-side Herdr panes and forwards Neovim selection context. |
| [**timofey-TK/herdr-yazi-agent**](https://github.com/timofey-TK/herdr-yazi-agent) | 1 | Picks files in Yazi, get their paths in your agent's prompt. |
| [**rytkmt/herdr-send.nvim**](https://github.com/rytkmt/herdr-send.nvim) | 0 | Sends file references and prompts from Neovim to AI agents in the active Herdr workspace. |
| [**luiarthur/herdr.vim**](https://github.com/luiarthur/herdr.vim) | 0 | Starts a language-appropriate REPL in a Herdr pane and sends the current line, whole file, or visual selection from Vim or Neovim. It supports older Vim releases as well as modern Neovim. |
| [**lancodev/herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker) | 0 | Runs Laravel Tinker beside an editor in a Herdr TUI pane or popup and reevaluates the scratch file when saved. |
| [**AbhijithAnirudhan2907/herdr-sidebar**](https://github.com/AbhijithAnirudhan2907/herdr-sidebar) | 0 | A fork of herdr-sidebar that adds an editor inside the pane, including save, syntax highlighting, undo and redo, and find and replace. |

### Editor plugins and bridges

*35 projects. General-purpose bridges that synchronize editor state with Herdr panes and agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**eugenioenko/ttt · herdr-plugin**](https://github.com/eugenioenko/ttt/tree/main/herdr-plugin) | 1,093 | Opens TTT Editor in a Herdr TUI pane for editing files in the active worktree. |
| [**ChmaraX/herdr-nvim**](https://github.com/ChmaraX/herdr-nvim) | 353 | Opens a persistent Neovim sidebar in Herdr with file search and annotations that can be sent to agents. |
| [**makyinmars/herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim) | 16 | Stages Neovim selections, cursor positions, and file details as Markdown context for a Herdr agent. |
| [**ryonakae/zerdr**](https://github.com/ryonakae/zerdr) | 10 | Keeps Herdr TUI workspace focus aligned with the matching Zed checkout and connects Zed terminal threads to Herdr panes. |
| [**mcuste/herdr-context.nvim**](https://github.com/mcuste/herdr-context.nvim) | 7 | Sends the current Neovim buffer, open buffers, or a Visual selection to a Herdr coding agent as a correctly formatted file reference. It targets one workspace agent automatically or opens a fuzzy picker when several agents are in the tab or workspace. |
| [**nwiizo/signalbox.nvim**](https://github.com/nwiizo/signalbox.nvim) | 6 | Controls persistent Herdr coding agents from Neovim with an attention-focused interface. |
| [**WorksOnMyVM/herdr-agent-bridge.nvim**](https://github.com/WorksOnMyVM/herdr-agent-bridge.nvim) | 5 | Stages Neovim editor context for Herdr agent panes. |
| [**ctbaum/herdr-agents.nvim**](https://github.com/ctbaum/herdr-agents.nvim) | 5 | Runs Claude Code, Codex, and Pi in Herdr TUI sibling panes while preserving Neovim editor integration and agent connections. |
| [**Zamua/openloc.nvim**](https://github.com/Zamua/openloc.nvim) | 4 | Opens file references in the Neovim that already belongs to the workspace. |
| [**alexeyco/herdr-open-in**](https://github.com/alexeyco/herdr-open-in) | 4 | Opens the current Herdr TUI workspace in a detected editor, with a picker when several editors are available. |

**[All 35 projects →](catalog/04-editors.md#editor-plugins-and-bridges)**

---

## 5. Switch and restore sessions

*260 projects. Fuzzy switchers, state managers, and layout restoration tools for organizing agent workspaces.* The top 10 of each subcategory by stars are below; the full list is in [catalog/05-sessions.md](catalog/05-sessions.md).

### Fuzzy session switchers and terminal pickers

*109 projects. Interactive pickers for finding and focusing workspaces, tabs, panes, agents, or projects.*

| Project | Stars | What it does |
|---|--:|---|
| [**nicosuave/memex**](https://github.com/nicosuave/memex) | 312 | Indexes conversations from Claude Code, Codex, Pi, OpenCode, and Cursor with hybrid search. A Herdr TUI searches the archive and can resume a selected interaction in a fresh tab. |
| [**jeffarese/herdr-bar**](https://github.com/jeffarese/herdr-bar) | 214 | A dependency-free Python command palette for jumping to any Herdr tab, agent, repository, or branch. |
| [**thanhdat77/herdr-picker-plus**](https://github.com/thanhdat77/herdr-picker-plus) | 188 | A Ratatui overlay that combines workspaces, project templates, directories, zoxide history, SSH hosts, agent panes, and plugin integrations. It reuses matching workspaces and can create or focus remote-host workspaces automatically. |
| [**thanhdat77/herdr-navigator**](https://github.com/thanhdat77/herdr-navigator) | 188 | Searches and switches between active Herdr sessions and workspaces using an interactive fuzzy picker. |
| [**andrewchng/herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer) | 53 | A tmux-sessionizer-style launcher for Herdr. Fzf selects projects or worktrees, while TOML defines tabs, splits, startup commands, repository-specific layouts, and preview panels. |
| [**beyondlex/herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator) | 26 | A Rust popup that tracks recently focused workspaces, tabs, panes, and agents through socket events. It provides a live most-recently-used index, keyboard navigation, and fuzzy search. |
| [**lmilojevicc/seshagy**](https://github.com/lmilojevicc/seshagy) | 23 | Finds projects and tmux or Herdr TUI sessions in a dashboard and shows coding-agent states before attaching. |
| [**dmnkf/herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch) | 12 | Searches live workspace metadata, pane output, and optional archived conversations across the Herdr TUI and app, then jumps to or resumes a match. |
| [**dartyuhov/herdr-blink**](https://github.com/dartyuhov/herdr-blink) | 9 | Opens a fuzzy Herdr TUI agent picker that prioritizes agents needing attention and sorts the rest by recent use. |
| [**hxreborn/herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts) | 8 | Searches past and live coding-agent sessions by title, prompt, reply, or tool call in an fzf popup, then resumes the pick in a new Herdr tab or focuses its pane when it is already running. Covers Claude Code, Codex, OpenCode, Gemini CLI, Droid, Copilot CLI, Kimi Code, and Qwen Code with a pre-warmed index in standard-library Python. |

**[All 109 projects →](catalog/05-sessions.md#fuzzy-session-switchers-and-terminal-pickers)**

### Persistence, snapshots, and state restoration

*68 projects. Tools that record layouts and process context, then rebuild or resume them after a restart.*

| Project | Stars | What it does |
|---|--:|---|
| [**ntindle/herdr-resurrect**](https://github.com/ntindle/herdr-resurrect) | 44 | Captures workspaces, tabs, panes, directories, and running agent processes so a complete Herdr environment can be restored after a crash or restart. |
| [**pattont/RexAgentRestore**](https://github.com/pattont/RexAgentRestore) | 24 | Imports Herdr workspaces into Rex with their tabs, splits, folders, and agent conversations. |
| [**tornikegomareli/herdr2rex**](https://github.com/tornikegomareli/herdr2rex) | 14 | Migrates Herdr TUI workspaces to Rex with tabs, splits, folders, and supported agent conversations. Imports Rex sessions back into Herdr and restores Claude Code conversations. |
| [**iviaxpow3r/herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker) | 13 | Parks active panes and tabs outside the current working layout and restores them later with agent state and prompt progress intact. |
| [**gokay-ai/sheep**](https://github.com/gokay-ai/sheep) | 6 | Records agent-turn checkpoints and restores selected worktree changes after a dry run, with an optional notice to the agent. |
| [**wbarakat/omarchy-session-restore**](https://github.com/wbarakat/omarchy-session-restore) | 5 | Saves Omarchy window and terminal state and restores it after login, with optional Herdr agent-session resume. |
| [**pedroloch/herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close) | 5 | Restores recently closed panes or tabs, including their split hierarchy, directories, labels, and launched agents, through a shortcut or history picker. |
| [**mcc0x/herdr-tether**](https://github.com/mcc0x/herdr-tether) | 5 | Keeps local or SSH-backed terminal workloads running after their Herdr TUI view closes and reconnects to them later. |
| [**andymartinezot/avocado-park**](https://github.com/andymartinezot/avocado-park) | 5 | Parks idle Claude Code, Codex, and OpenCode sessions to free memory and resumes them in the same Herdr TUI pane. |
| [**chandrasekharan98/herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save) | 4 | Saves Herdr workspace layouts and commands for later restoration through an fzf picker. |

**[All 68 projects →](catalog/05-sessions.md#persistence-snapshots-and-state-restoration)**

### Workspace and multi-session management

*83 projects. Managers for creating, grouping, naming, attaching to, and cleaning up several sessions.*

| Project | Stars | What it does |
|---|--:|---|
| [**nikok6/herdr-mirror**](https://github.com/nikok6/herdr-mirror) | 263 | Mirrors remote Herdr workspaces and agent state into a local sidebar over SSH or Docker. Remote panes can be watched and controlled alongside local ones. |
| [**taxueseek/session-digger**](https://github.com/taxueseek/session-digger) | 34 | Indexes conversations from Claude Code, Codex, and other agents in SQLite FTS5. It also tracks token and cache data and creates local HTML reports for review. |
| [**AVGVSTVS96/herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr) | 26 | Uses fzf and the Herdr socket API to move live tabs and panes between workspaces without stopping their processes. |
| [**third774/herdr-last-workspace**](https://github.com/third774/herdr-last-workspace) | 20 | Tracks workspace IDs and toggles between the current and previous workspace with one key. It remains correct after reordering and exits quietly if the earlier workspace was closed. |
| [**wenhanweime/herduck**](https://github.com/wenhanweime/herduck) | 13 | Groups related Claude Code, Codex, OpenCode, and Pi sessions into one Work and keeps its goal, blocker, and next step. Runs as a separate app derived from Herdr, with a thin plugin that opens it from Herdr. |
| [**GiorgiTarsaidze/herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles) | 12 | Groups Herdr TUI spaces and agents into named profiles and switches between them with a popup chooser. |
| [**den-tanui/herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide) | 11 | Uses zoxide's directory history when creating Herdr workspaces, tabs, and panes, making recent project paths quick to open. |
| [**douglascorrea/herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox) | 11 | Shows Herdr TUI agent session titles, runtimes, workspace statistics, and unread state in a central inbox. |
| [**2lab-ai/herdr-mx**](https://github.com/2lab-ai/herdr-mx) | 11 | Connects multiple local and SSH Herdr TUI servers in one sidebar with a downstream multi-remote client. |
| [**lmilojevicc/herdr-last**](https://github.com/lmilojevicc/herdr-last) | 10 | Toggles between the current and previously active Herdr TUI workspace or tab. |

**[All 83 projects →](catalog/05-sessions.md#workspace-and-multi-session-management)**

---

## 6. Worktrees and terminal experience

*1320 projects. Git worktree automation, terminal navigation, status displays, HUDs, and developer environment tools.* The top 10 of each subcategory by stars are below; the full list is in [catalog/06-worktrees-and-terminal.md](catalog/06-worktrees-and-terminal.md).

### Git worktree automation

*135 projects. Tools that create isolated branches and worktrees for agents, then connect them to Herdr workspaces or tabs.*

| Project | Stars | What it does |
|---|--:|---|
| [**devashish2203/herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk) | 197 | Creates, switches, merges, and removes Git worktrees with Worktrunk from Herdr TUI, using Worktrunk lifecycle hooks and an interactive branch picker. |
| [**razajamil/herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager) | 50 | Defines tabs, splits, and startup commands in YAML and applies the layout whenever a new worktree opens. It can run a blocking setup command first and prune worktrees whose upstream branch has been removed. |
| [**NathanFlurry/herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace) | 48 | Adds key bindings for creating and removing Jujutsu workspaces through `jj workspace`, opening the result as a Herdr workspace or tab. |
| [**tdi/herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup) | 31 | Runs repository setup after Herdr creates a worktree, including copying `.env` files and executing commands such as `mise trust` and `direnv allow`, so the environment is ready immediately. |
| [**wyattjoh/herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer) | 22 | Renames numbered tabs from the agent's first prompt and can also rename an automatically linked worktree's branch and workspace. The short task name is generated locally with Apple Foundation Models or Codex. |
| [**tdi/herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear) | 19 | Searches active Linear issues, then creates or focuses a matching Git worktree and Herdr workspace. An optional split shows the issue description and assignee. |
| [**EzraCerpac/jj-waltz**](https://github.com/EzraCerpac/jj-waltz) | 10 | Switches Jujutsu workspaces and maps their directories to Herdr TUI tabs and workspaces. |
| [**freethinkel/herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) | 7 | Runs global YAML-configured shell hooks when Git worktrees are created or removed. Hooks receive paths and event metadata, and executions are recorded durably. |
| [**tdi/herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr) | 7 | Creates an isolated Git worktree from a GitHub pull request and opens it as a new Herdr workspace in one operation. |
| [**hmu332233/herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree) | 7 | Symlinks declared ignored files, environment files, and caches from the main checkout into new worktrees without replacing files that already exist. |

**[All 135 projects →](catalog/06-worktrees-and-terminal.md#git-worktree-automation)**

### Workspace lifecycle and multi-repository tools

*44 projects. Higher-level utilities for starting, tracking, and removing workspaces that span one or more repositories.*

| Project | Stars | What it does |
|---|--:|---|
| [**OliverGilan/herdr-jj**](https://github.com/OliverGilan/herdr-jj) | 5 | Adds Jujutsu workspace creation, remote fetching, bookmark setup, live change metadata, and post-create hooks to Herdr. |
| [**jattento/herdr-multirepo**](https://github.com/jattento/herdr-multirepo) | 3 | Creates a Herdr TUI workspace containing matching feature-branch worktrees from multiple repositories. |
| [**LoriKarikari/kubeflock**](https://github.com/LoriKarikari/kubeflock) | 3 | Creates and connects Kubernetes agent sandboxes to Herdr TUI and manages their lifecycle. |
| [**leoleducq/devflow**](https://github.com/leoleducq/devflow) | 2 | Provisions isolated development environments with databases, ports, environment files, and servers, and synchronizes them with Herdr TUI workspaces. |
| [**alon-z/herdr-devup**](https://github.com/alon-z/herdr-devup) | 2 | Reads `.herdr/dev.toml` to start a project's tabs, panes, and services, refresh an ngrok URL across configured environment files, and close only the tabs it created. |
| [**nicksenap/grove-herdr**](https://github.com/nicksenap/grove-herdr) | 2 | Asks for a name on a key press, runs Grove's gw create and opens the new path as a Herdr workspace. The install script also wires Grove hooks so a Herdr workspace opens and closes with gw create and gw delete. |
| [**dalogax/herdr-agent-hibernate**](https://github.com/dalogax/herdr-agent-hibernate) | 2 | Ends idle, unfocused OpenCode, Claude Code and Codex panes to free memory and relaunches the same session with native resume flags when you focus the pane again. |
| [**alexjyong/herdr-codespaces**](https://github.com/alexjyong/herdr-codespaces) | 2 | Lists your GitHub Codespaces in a picker and adds the chosen one as a Herdr machine in the sidebar next to local workspaces. |
| [**yoyoyeti/multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin) | 1 | Creates and attaches multitrunk task workspaces in Herdr TUI with an agent pane, repository tabs, and interactive popups. |
| [**yavuzhansarmaz/herdr-vps-local**](https://github.com/yavuzhansarmaz/herdr-vps-local) | 1 | Mirrors repos from a VPS or Raspberry Pi saved machine to your laptop with Mutagen. Lets you edit in a local IDE while agents keep running on the remote machine. |

**[All 44 projects →](catalog/06-worktrees-and-terminal.md#workspace-lifecycle-and-multi-repository-tools)**

### Diff review and code inspection

*89 projects. Side-by-side git diff inspection and comment handoff tools for agent reviews.*

| Project | Stars | What it does |
|---|--:|---|
| [**persiyanov/herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr) | 980 | Opens an interactive diff review interface for inspecting agent changes and sending review feedback. |
| [**plannotator/herdr-annotate**](https://github.com/plannotator/herdr-annotate) | 741 | Annotates terminal text, reviews documents and agent replies in Herdr, and returns feedback directly to the running agent. |
| [**jhochenbaum/herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff) | 150 | Displays side-by-side git diffs in an adjacent pane and lets developers leave review comments for agents. |
| [**crittylabs/critty**](https://github.com/crittylabs/critty) | 104 | Shows agent review and approval prompts in the terminal and reports attention status to the Herdr app through OSC 7501. |
| [**osolmaz/ghzinga**](https://github.com/osolmaz/ghzinga) | 90 | Opens a GitHub issue or pull request in a terminal interface with review and comment actions from Herdr TUI links. |
| [**JonasBaeumer/herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator) | 65 | Adds in-editor file annotations for reviewing code while working with agents in Herdr. |
| [**Crokily/herdr-lazygit**](https://github.com/Crokily/herdr-lazygit) | 45 | Runs lazygit in a Herdr sidebar with shortcuts for opening, expanding, and staging changes, plus AI-assisted commit-message generation from the pending diff. |
| [**ChmaraX/herdr-gitview**](https://github.com/ChmaraX/herdr-gitview) | 30 | Reviews Git status and diffs, edits files in Neovim, stages or discards hunks, and commits from a Herdr panel. |
| [**plannotator/herdr-plannotator**](https://github.com/plannotator/herdr-plannotator) | 26 | Embeds Plannotator plan reviews in a dedicated Herdr browser pane so plans can be annotated, discussed, and approved beside active coding sessions. |
| [**tomasvarga/herdr-pickr**](https://github.com/tomasvarga/herdr-pickr) | 20 | Intercepts clicked GitHub pull-request and GitLab merge-request links and opens their diffs in tuicr, Hunk, or a browser, with an optional AI first-pass review. |

**[All 89 projects →](catalog/06-worktrees-and-terminal.md#diff-review-and-code-inspection)**

### File viewers, terminal browsers, and markdown previews

*81 projects. In-terminal file viewers, interactive web browsers, image previews, and markdown rendering panes.*

| Project | Stars | What it does |
|---|--:|---|
| [**zenbu-labs/terminal-browser · herdr-plugin**](https://github.com/zenbu-labs/terminal-browser/tree/main/herdr-plugin) | 4,576 | Opens a terminal browser beside a Herdr TUI pane and supports agent-driven browser interaction. |
| [**smarzban/herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer) | 704 | Opens a read-only file viewer in a Herdr TUI split with Git status, diffs, Markdown, and source previews. |
| [**alexarthurs/herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar) | 541 | Opens a dockable file explorer and source-control panel with previews and AI-drafted commit messages in Herdr TUI. |
| [**ogulcancelik/herdr-browser**](https://github.com/ogulcancelik/herdr-browser) | 360 | Renders an interactive Chromium browser inside a Herdr pane and lets agents automate it through Chrome DevTools Protocol. The project is deprecated in favor of terminal-browser. |
| [**iurysza/termscope**](https://github.com/iurysza/termscope) | 71 | Finds visible file paths and web links on the terminal screen, lets the user select one with fuzzy search, and opens it in a separate split without disturbing the main pane. |
| [**speardragon/herdr-yazi**](https://github.com/speardragon/herdr-yazi) | 35 | Opens the Yazi file manager in a Herdr pane or tab at the current directory while reusing the user's existing Yazi configuration. |
| [**StructuPath/herdr-browser**](https://github.com/StructuPath/herdr-browser) | 33 | Opens a drivable Chromium browser in a Herdr pane for agent automation and manual inspection. |
| [**alexarthurs/herdr-notes**](https://github.com/alexarthurs/herdr-notes) | 23 | Keeps one persistent Markdown note per workspace, with rendered and edit modes, autosave, and restoration after restarts. |
| [**dwarvesf/herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook) | 17 | Previews a file path from the clipboard in an overlay and can expand it into a full terminal viewer, avoiding manual path entry or temporary splits. |
| [**slara/terminal-markdown-renderer**](https://github.com/slara/terminal-markdown-renderer) | 16 | Opens rendered Markdown in a terminal browser from a Herdr TUI plugin. |

**[All 81 projects →](catalog/06-worktrees-and-terminal.md#file-viewers-terminal-browsers-and-markdown-previews)**

### Pane navigation and overlay hints

*58 projects. Direct 1-character overlay hints and smart directional pane jumping.*

| Project | Stars | What it does |
|---|--:|---|
| [**nathan-poncet/herdr-fingers**](https://github.com/nathan-poncet/herdr-fingers) | 14 | Labels visible paths, URLs, hashes, and other text with short hints to copy, paste, or open them in Herdr TUI. |
| [**crierr/herdr-arrange**](https://github.com/crierr/herdr-arrange) | 9 | Rearranges Herdr TUI panes from a popup, including swaps, resizing, layouts, and transfers between tabs. |
| [**husniadil/herdr-swipe**](https://github.com/husniadil/herdr-swipe) | 7 | Adds macOS trackpad gestures for switching Herdr TUI panes, tabs, and spaces and jumping to agents awaiting attention. |
| [**milkyskies/herdr-attention**](https://github.com/milkyskies/herdr-attention) | 6 | Moves focus to the next agent needing attention with one key, checking blocked agents before completed ones. |
| [**81zi/reficus**](https://github.com/81zi/reficus) | 6 | Resizes Herdr TUI panes as focus changes, keeping other panes visible and optionally expanding agents waiting for input. |
| [**xzedx/herdr-easyjump**](https://github.com/xzedx/herdr-easyjump) | 5 | Jumps to any space, agent, pane, or tab using EasyMotion-style hint labels in the Herdr sidebar. |
| [**KonstantinKai/herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon) | 5 | Marks Herdr TUI panes and jumps back to them with numeric shortcuts or a picker. |
| [**meerzulee/herdr-float**](https://github.com/meerzulee/herdr-float) | 4 | Opens a floating shell for the current Herdr TUI space with Option-F or Alt-F, using Herdr's native popup placement so the tiled layout stays visible. Keeps one persistent shell session per space. |
| [**TinyWhite1997/herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker) | 3 | Jumps to Herdr TUI panes using one- or two-letter labels in a workspace and tab picker. |
| [**vjeantet/herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control) | 3 | Opens a full-screen overlay showing every pane of the current workspace as a live tile grouped by tab, with styled ANSI previews and agent status. Arrows or `hjkl` move the selection, `Enter` focuses the pane, and `Backspace` closes it without leaving the overview. |

**[All 58 projects →](catalog/06-worktrees-and-terminal.md#pane-navigation-and-overlay-hints)**

### Pane layout management

*44 projects. Tools that arrange, resize, and manage Herdr TUI panes.*

| Project | Stars | What it does |
|---|--:|---|
| [**thuanlm215/herdr-grid**](https://github.com/thuanlm215/herdr-grid) | 16 | Opens a visual editor for dragging, resizing, and safely rearranging live pane layouts without restarting pane processes. It can add shell panes, apply fixed presets, or build a preset in a new workspace. |
| [**osamahbeig/herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover) | 15 | Moves, re-splits, and swaps Herdr panes through a clickable overlay. |
| [**shibayu36/herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes) | 12 | Automatically equalizes Herdr TUI panes after splits and closures, with an optional manual action. |
| [**iurysza/herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts) | 5 | Adds tmux-style pane resizing and layouts to Herdr. |
| [**edouard-andrei/herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools) | 3 | Rearranges existing panes into main-left, grid, or equalized presets without changing pane IDs, tab IDs, or running processes. |
| [**crierr/herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout) | 3 | Adds tmux-style layout presets for Herdr, including even horizontal, even vertical, main horizontal, main vertical, tiled, cycle, and balance. |
| [**iuhoay/herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane) | 2 | Moves the active pane into a new tab while preserving its process, similar to tmux break-pane. It unzooms complex tabs first and leaves single-pane tabs unchanged. |
| [**federbenjamin/herdr-undo-close**](https://github.com/federbenjamin/herdr-undo-close) | 2 | Reopens the pane you just closed in Herdr in the same split, with its old scrollback above a fresh prompt. A Claude Code pane resumes its conversation, and a command that was running returns typed but not run. |
| [**orcchg/herdr-topstrip**](https://github.com/orcchg/herdr-topstrip) | 2 | Opens every new tab and space as a narrow top shell strip over a wide work pane, and relaunches the strip if you close it. |
| [**ponko2/herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes) | 2 | Automatically equalizes Herdr TUI pane sizes when panes are created, closed, moved, or exit, with an on-demand action. |

**[All 44 projects →](catalog/06-worktrees-and-terminal.md#pane-layout-management)**

### Terminal keybindings and shortcut helpers

*86 projects. Custom keymap packs, leader-key setups, and prefix-free navigation.*

| Project | Stars | What it does |
|---|--:|---|
| [**yuk1ty/herdr-spreader**](https://github.com/yuk1ty/herdr-spreader) | 145 | Builds complete Herdr layouts from YAML, including tabs, splits, directories, startup commands, and dependencies that wait for output patterns before launching later panes. |
| [**sohanemon/herdr-helpr**](https://github.com/sohanemon/herdr-helpr) | 10 | Adds keyboard overlays for naming a workspace before creation, renaming the current workspace, and closing every pane or tab except the focused one. |
| [**CowboyVang/herdr-which-key**](https://github.com/CowboyVang/herdr-which-key) | 6 | Shows Herdr keybindings in a grouped overlay and runs a selected binding. |
| [**ramarivera/herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which) | 6 | Shows searchable Herdr TUI keybindings and launches configured actions from a Ratatui popup. |
| [**Taeyoung96/herdr-dotfiles**](https://github.com/Taeyoung96/herdr-dotfiles) | 6 | A ready-to-use Herdr configuration with prefix-free pane movement, `Ctrl+Space` as the prefix, Catppuccin styling, and a global agent panel. The installer symlinks the file and backs up the previous config. |
| [**johnlindquist/herdr-game**](https://github.com/johnlindquist/herdr-game) | 5 | Teaches Herdr TUI navigation and agent operations through interactive browser lessons backed by isolated Herdr sessions. |
| [**The-Dave-Stack/herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap) | 5 | Displays all Herdr key bindings in an overlay and can run bindings that have an equivalent command-line action. |
| [**markhuot/herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits) | 5 | Balances all split dimensions in the current tab with one shortcut, equalizing panes by rows or columns after manual resizing or new splits. |
| [**jeph/herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer) | 5 | Automatically retile and equalizes Herdr panes whenever a pane is created, closed, or exits. |
| [**cskwork/herdr-cheatsheet**](https://github.com/cskwork/herdr-cheatsheet) | 4 | Summarizes Herdr TUI keybindings and CLI commands in a printable cheatsheet with an agent setup prompt. |

**[All 86 projects →](catalog/06-worktrees-and-terminal.md#terminal-keybindings-and-shortcut-helpers)**

### Command palettes and workspace switchers

*61 projects. Searchable menus for Herdr commands, projects, workspaces, and common actions.*

| Project | Stars | What it does |
|---|--:|---|
| [**fullerzz/herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh) | 52 | A sesh-style Herdr workspace picker with zoxide integration for creating workspaces from frequently used directories. |
| [**JanTvrdik/herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette) | 47 | Opens an fzf overlay containing every action from every installed plugin. It preserves the originating workspace directory, runs the selected action, and removes the temporary overlay afterward. |
| [**speardragon/herdr-command-center**](https://github.com/speardragon/herdr-command-center) | 20 | Runs registered commands from a Herdr TUI popup using a single keybinding, arrow keys, or assigned slots. |
| [**vjeantet/herdr-palette**](https://github.com/vjeantet/herdr-palette) | 20 | Combines Herdr's built-in operations, every installed plugin's actions, user-defined commands, and reusable prompts in one fuzzy Rust/Ratatui palette. It preserves the originating pane context and asks for inputs, selections, or confirmation when an operation needs them. |
| [**mmjang/herdr-omni**](https://github.com/mmjang/herdr-omni) | 14 | Searches Herdr TUI workspaces, actions, and live or saved Claude and Codex sessions, including conversation contents. |
| [**ramarivera/herdr-palette**](https://github.com/ramarivera/herdr-palette) | 12 | A Rust and Ratatui fuzzy command palette for Herdr workspaces. |
| [**enekos/herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions) | 9 | Opens an fzf picker for native Herdr TUI actions and jump targets, showing the configured shortcut for each action. |
| [**cesarferreira/herdr-palette**](https://github.com/cesarferreira/herdr-palette) | 5 | Finds and runs Herdr TUI actions in a popup while showing their effective shortcuts. |
| [**arjenblokzijl/herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher) | 5 | Defines named workflows as `.mjs` files with custom input fields and a `run()` function. Workflows can be launched from a Herdr picker or through `herdr-launcher run`, supporting interactive and scripted use. |
| [**lurepos/herdr-commander**](https://github.com/lurepos/herdr-commander) | 4 | Discovers VS Code tasks and project commands such as npm and Cargo scripts and launches them in Herdr TUI tabs or panes. |

**[All 61 projects →](catalog/06-worktrees-and-terminal.md#command-palettes-and-workspace-switchers)**

### Status lines and workspace metadata

*141 projects. Status lines, external terminal and desktop bars, pane labels, and workspace metadata without sidebar or tab-label displays.*

| Project | Stars | What it does |
|---|--:|---|
| [**fkiene/llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr) | 59 | Activates the llmtrim compression proxy in new Herdr workspaces, shows savings badges in pane rows, and opens llmtrim's dashboard in a split. It also warns when a pane did not inherit the proxy settings. |
| [**jankeesvw/omarchy-herdr**](https://github.com/jankeesvw/omarchy-herdr) | 58 | Runs herdr servers in the Omarchy bar, with every agent inside them, and a click that lands you on the one you picked. |
| [**rjyo/herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync) | 39 | Writes workspace, tab, and agent context to the outer terminal title. It uses pane metadata and status first, then falls back to recent prompts in local Claude Code or Codex session files. |
| [**wenhanweime/herdr-plugin-renamer**](https://github.com/wenhanweime/herdr-plugin-renamer) | 25 | Uses an LLM to name sessions for Claude Code, Codex, Grok, Pi, and OpenCode, with Chinese or English labels and OpenCode Zen as the default engine. |
| [**ezcorp-org/herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status) | 11 | Shows staged, modified, untracked, and conflicted Git files for each workspace beside its branch name. |
| [**njpatel/omaherdr**](https://github.com/njpatel/omaherdr) | 9 | Shows Herdr TUI sessions, spaces, tabs, and agents in the Omarchy bar and jumps to a selected item. |
| [**bcihanc/herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title) | 8 | Copies the Claude Code session title, including `/rename` or automatic summaries, into Herdr pane metadata. |
| [**flowy11/agent-panel**](https://github.com/flowy11/agent-panel) | 8 | Shows the focused Claude Code or Codex session, subagents, messages, references and tasks in a Herdr TUI side panel. |
| [**Phoobobo/herdr-workboard**](https://github.com/Phoobobo/herdr-workboard) | 7 | Shows Herdr TUI workspaces as Kanban boards and moves live panes between task-state tabs. |
| [**Razz21/herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status) | 7 | Detects dev servers in panes via pluggable specs and reports lifecycle status. |

**[All 141 projects →](catalog/06-worktrees-and-terminal.md#status-lines-and-workspace-metadata)**

### Automatic tab, pane, and workspace names

*91 projects. Plugins that rename tabs, panes, and workspaces from the foreground process, directory, git branch, agent session title, or first prompt, plus numbered tab and workspace labels.*

| Project | Stars | What it does |
|---|--:|---|
| [**kryptamine/herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title) | 282 | Updates Herdr tab titles automatically based on active workspace tasks to keep development contexts organized. |
| [**qu8n/herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename) | 230 | Renames tabs from the active foreground process and icon, and prefixes workspaces, tabs, and agents with numbers 1 through 9 for quick visual and keyboard selection. |
| [**iurysza/herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename) | 77 | Uses a lightweight LLM to derive short workspace and tab names from pane activity, replacing generic numbers or directory labels with current task summaries. |
| [**sh1ma/herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title) | 55 | Runs in the background and derives Herdr tab names from the topic and intent of Claude Code or Codex conversations. |
| [**aarsh21/herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title) | 7 | Provides automatic tmux-style tab titles for Herdr. |
| [**wjarka/herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title) | 6 | Writes color-coded counts of working, blocked, done, and idle Herdr agents into Ghostty tab titles. |
| [**killerz3/herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler) | 5 | Auto-titles Herdr tabs using local agy, claude, codex, or opencode harnesses without external API keys. |
| [**kakigakki/herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer) | 5 | Uses Claude Code session titles for agent tabs and directory names for workspaces, providing automatic ChatGPT-style labels across parallel sessions. |
| [**danbuhler/herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync) | 5 | Renames panes and tabs from the active topic or terminal title emitted by Claude Code and Codex, while avoiding rename loops and respecting manual labels. |
| [**lmilojevicc/herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename) | 4 | Renames each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. |

**[All 91 projects →](catalog/06-worktrees-and-terminal.md#automatic-tab-pane-and-workspace-names)**

### Sidebar grouping, ordering, and filtering

*45 projects. Plugins that restructure the Spaces and Agents sidebars into trees, project groups, priority or recency order, filtered views, and compact one-line rows.*

| Project | Stars | What it does |
|---|--:|---|
| [**hhdebb/herdr-radar**](https://github.com/hhdebb/herdr-radar) | 204 | Shows agent activity in the Herdr TUI sidebar, grouping workspaces and worktrees and highlighting waiting or stale sessions. |
| [**ShankyJS/herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents) | 8 | Limits the agent sidebar to workers in the currently focused workspace, reducing unrelated fleet noise when moving between projects. |
| [**kriuchkov/herdr-scope**](https://github.com/kriuchkov/herdr-scope) | 8 | Shows Herdr TUI agent state in a project-grouped sidebar and jumps to agents waiting for input. |
| [**gonzalonicolasr/herdr-bandeja-to-dos**](https://github.com/gonzalonicolasr/herdr-bandeja-to-dos) | 3 | Organizes Herdr TUI agents by attention state in the sidebar and shows to-dos left by agents. |
| [**dboeter/herdr-agent-tree**](https://github.com/dboeter/herdr-agent-tree) | 2 | Docks a narrow pane on the left or right of every tab that shows workspaces as groups and their agents as a live tree with status marks. One key or click jumps to the agent that needs you. |
| [**4242labs/herdr-radar-plus**](https://github.com/4242labs/herdr-radar-plus) | 2 | Sorts Herdr agents by what needs you, with named groups that span connected machines. Adds a model-family mark and a machine row under each agent on top of herdr-radar. |
| [**evanbryant/herdr-covr**](https://github.com/evanbryant/herdr-covr) | 2 | Replaces the Herdr sidebar with a compact Spaces and Agents list, one line per agent sorted by what needs you. A second line appears only when an agent is blocked or just finished, with light and dark layouts. |
| [**ZingerLittleBee/herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins) | 1 | Pins selected Herdr agent sessions to the top of the sidebar and restores their order across server restarts. |
| [**MrBogomips/herdr-tools**](https://github.com/MrBogomips/herdr-tools) | 1 | Sorts the spaces sidebar into top, default and bottom groups, gives every space of one customer the same colour (Space Herder), and names tabs after their folder, repo or branch (auto-tab-name). Also ships herdr-jump, a macOS menu bar picker that lists the agents waiting for you, blocked first and oldest wait first. |
| [**mashhoodr/herdr-space-sidebar**](https://github.com/mashhoodr/herdr-space-sidebar) | 1 | Merges Herdr's Spaces and Agents panels into one list with each agent nested under its space. Shows status symbols and session colors. |

**[All 45 projects →](catalog/06-worktrees-and-terminal.md#sidebar-grouping-ordering-and-filtering)**

### Sidebar badges, tokens, and status indicators

*88 projects. Plugins that add status icons, spinners, colors, model and CPU badges, PR and CI tokens, notes, and other per-row details to the sidebar and tab bar.*

| Project | Stars | What it does |
|---|--:|---|
| [**robbyrussell/herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh) | 86 | Integrates Herdr with Oh My Zsh, displaying slow commands in the sidebar and triggering desktop completion notifications. |
| [**FlorisKr/herdr-openspec**](https://github.com/FlorisKr/herdr-openspec) | 34 | Shows OpenSpec change and task progress in the Herdr TUI sidebar and opens proposals, designs, and specs in a change browser. |
| [**eliasstravik/herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress) | 34 | Shows agent-reported task estimates and activity for Claude Code and Codex in the Herdr TUI sidebar. |
| [**wyattjoh/herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr) | 23 | Shows the GitHub pull-request number and CI state for the focused agent pane's branch in the Herdr sidebar. Updates are rate-limited, with shortcuts for manual refresh and opening the pull request. |
| [**bayoudhi/herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress) | 17 | Adds a live sidebar progress for slow shell commands, not just coding agents. |
| [**qintmb/herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui) | 16 | Adds larger agent icons, status glyphs, and a workspace, tab, and agent tree to the Herdr TUI sidebar. |
| [**testy-cool/herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config) | 13 | Adds a compact workspace, tab, and agent sidebar preset with provider icons to Herdr. |
| [**getpipher/herdr-sysmon**](https://github.com/getpipher/herdr-sysmon) | 9 | Adds CPU, memory, battery, network, and disk measurements to Herdr sidebar tokens, with configurable refresh intervals and macOS-focused probes. |
| [**Numbered-com/herdr-ports**](https://github.com/Numbered-com/herdr-ports) | 7 | Detects TCP listeners started by processes in each workspace and adds a dynamic `$ports` badge to the Herdr sidebar. |
| [**pdalinis/herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model) | 5 | Shows the active model and reasoning effort for Codex, Claude Code, Pi, and Hermes agents in the Herdr TUI sidebar. |

**[All 88 projects →](catalog/06-worktrees-and-terminal.md#sidebar-badges-tokens-and-status-indicators)**

### Status overlays, HUDs, and agent timers

*78 projects. Floating status HUDs, turn timers, and keep-awake utilities.*

| Project | Stars | What it does |
|---|--:|---|
| [**aemrebarut/herdr-dagr**](https://github.com/aemrebarut/herdr-dagr) | 149 | Shows a live directed graph of an agent workflow inside a Herdr split. It reads a structured `run.json` file and displays tasks, retries, review gates, evidence levels, and progress history. |
| [**aigorahub/herdr-lantern**](https://github.com/aigorahub/herdr-lantern) | 74 | Shows which Herdr agents need attention and lets users jump to panes or start agents. |
| [**ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay) | 29 | Shows Linux CPU and memory use per Herdr workspace relative to total capacity. |
| [**Tyru5/herdr-floax**](https://github.com/Tyru5/herdr-floax) | 28 | A tmux-floax-style floating shell with one persistent scratch session per Herdr workspace. |
| [**jeffarese/herdr-agent-grid**](https://github.com/jeffarese/herdr-agent-grid) | 22 | Shows agents, subagents, messages, status, and API cost in a Herdr TUI panel and jumps to selected panes. |
| [**nikok6/herdr-pet**](https://github.com/nikok6/herdr-pet) | 18 | Displays an animated Codex-format pet on Herdr panes that reacts to agent activity and waiting states. |
| [**oronbz/visor · herdr**](https://github.com/oronbz/visor/tree/main/herdr) | 14 | Opens a configurable terminal dashboard over Herdr TUI tabs for GitHub pull requests, Jira issues, calendars, and other widgets. |
| [**maro114510/herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup) | 9 | Toggles a shell overlay above the current Herdr session for quick commands, notes, or plan inspection without rearranging panes. |
| [**natori-hrj/herdr-triage**](https://github.com/natori-hrj/herdr-triage) | 7 | Sorts active Herdr agents by how urgently they need attention. Blocked and stalled workers rise to the top based on their wait and idle time. |
| [**enes/herdr-monitoring**](https://github.com/enes/herdr-monitoring) | 6 | Shows CPU, memory and process trees for Herdr TUI agents in a summary popup or focused-pane monitor. |

**[All 78 projects →](catalog/06-worktrees-and-terminal.md#status-overlays-huds-and-agent-timers)**

### Context meters and rate-limit gauges

*89 projects. Live token headroom meters, quota tracking, and agent cost gauges.*

| Project | Stars | What it does |
|---|--:|---|
| [**levi-qiao/herdr-agent-usage**](https://github.com/levi-qiao/herdr-agent-usage) | 159 | Shows model, context and subscription quota for coding agents in the Herdr TUI agent sidebar. |
| [**levi-qiao/herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota) | 159 | A sidebar quota monitor for Claude, Codex, Grok, and Agy that shows the percentage remaining in five-hour and weekly limits. |
| [**senna-lang/herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage) | 64 | Shows context meters and provider rate limits for agents running in Herdr. |
| [**pinkpixel-dev/quota · herdr-plugin**](https://github.com/pinkpixel-dev/quota/tree/main/herdr-plugin) | 36 | Shows per-pane AI provider usage in the Herdr TUI sidebar for accounts such as Claude Code and Codex. |
| [**Davidcreador/herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard) | 29 | Shows live token use and costs for Pi, OpenCode, Claude Code, and Codex in Herdr TUI, with completion notifications. |
| [**quaywin/agys**](https://github.com/quaywin/agys) | 12 | Isolates Antigravity account profiles in Herdr TUI panes and shows profile, context, and quota telemetry in the sidebar. |
| [**VHemanth45/herdr_agents_tracker**](https://github.com/VHemanth45/herdr_agents_tracker) | 7 | Tracks coding-agent subscription limits and per-agent context in Herdr TUI with usage alerts and a token dashboard. |
| [**oszypczy/herdr-claude-usage**](https://github.com/oszypczy/herdr-claude-usage) | 5 | Shows the focused Claude agent’s context, five-hour usage, and seven-day usage bars in the Herdr TUI sidebar. |
| [**speardragon/herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar) | 4 | Shows Claude Code, Codex, and Grok plan usage in the Herdr tab bar, with optional additional providers. |
| [**Mako-L/account-capacity-dock · herdr-plugin**](https://github.com/Mako-L/account-capacity-dock/tree/main/herdr-plugin) | 4 | Shows Claude, Codex and Cursor account capacity in a Herdr TUI widget and desktop dock. |

**[All 89 projects →](catalog/06-worktrees-and-terminal.md#context-meters-and-rate-limit-gauges)**

### Output inspection, logs, and transcripts

*67 projects. Tools for searching, cleaning, exporting, or reviewing pane output and agent conversations.*

| Project | Stars | What it does |
|---|--:|---|
| [**furkankly/zoetrope · herdr-plugin**](https://github.com/furkankly/zoetrope/tree/main/herdr-plugin) | 1,156 | Shows Claude Code and Codex sessions as live flow graphs and opens the view beside a Herdr TUI pane. |
| [**rmarganti/herdr-pluck**](https://github.com/rmarganti/herdr-pluck) | 25 | Adds one- and two-letter hints for copyable terminal tokens, including URLs, paths, hashes, UUIDs, IP addresses, Kubernetes references, and hexadecimal values. |
| [**BjoernSchotte/agentglass**](https://github.com/BjoernSchotte/agentglass) | 24 | Monitors coding-agent sessions and lets you send prompts to Herdr TUI panes, jump to live agents, and resume sessions in new tabs. Shows Herdr agent states, approval waits, and workspace grouping. |
| [**hotchpotch/herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers) | 16 | Adds tmux-fingers-style labels to visible URLs, commit hashes, and file paths. Typing a short hint copies the selected token without using a mouse. |
| [**wilbeibi/herdr-catchup**](https://github.com/wilbeibi/herdr-catchup) | 12 | Transfers work between Claude Code, Codex, Cursor, Cline, and OpenCode sessions in Herdr. It captures and summarizes a live pane so another agent can continue or branch the task with useful context. |
| [**rsdlt/levi · herdr**](https://github.com/rsdlt/levi/tree/main/herdr) | 8 | Searches Git history and inserts a reference to a selected commit, file and lines into a Herdr TUI agent prompt. |
| [**youguanxinqing/herdr-flash**](https://github.com/youguanxinqing/herdr-flash) | 7 | Searches visible Herdr TUI pane text, jumps to a labeled match, and selects and yanks text with Vim motions. |
| [**AkashJana18/herdr-scratch**](https://github.com/AkashJana18/herdr-scratch) | 6 | Maintains persistent scratch panes that can be shown or hidden without losing shell, note, or REPL state. Scratch areas may be global, workspace-specific, or directory-specific. |
| [**hitaishi2222/herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers) | 4 | Copies paths, URLs, and other identifiers from the focused pane using keyboard hints. |
| [**bigsan/claude-deck**](https://github.com/bigsan/claude-deck) | 4 | Shows Claude Code sessions, scratchpad files, tasks and tool calls in a Herdr TUI viewer. |

**[All 67 projects →](catalog/06-worktrees-and-terminal.md#output-inspection-logs-and-transcripts)**

### Agent visualizations and terminal games

*34 projects. Interactive terminal visualizations and games for following agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**michaellandi/herdr-office**](https://github.com/michaellandi/herdr-office) | 12 | Draws Herdr TUI agents as office characters and signals when an agent needs approval. |
| [**aorumbayev/herdr-canvas**](https://github.com/aorumbayev/herdr-canvas) | 8 | Opens a mouse-driven ASCII diagram canvas in a Herdr split. Humans draw boxes, lines, and text; agents read and edit the same JSON-backed diagrams through the CLI and skill. |
| [**devangchhajed/herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office) | 7 | Shows Herdr TUI agents as pixel-art office characters that change activity with agent status and tool calls. |
| [**takemo101/wave-tui**](https://github.com/takemo101/wave-tui) | 5 | Plays internet radio in a terminal and visualizes Herdr TUI agents in an interactive Agent Planets view. |
| [**Efeguclu1/herdr-town**](https://github.com/Efeguclu1/herdr-town) | 5 | Renders Herdr coding agents as an interactive 8-bit town inside a pane and lets users read or answer them. |
| [**opsydyn/herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer) | 4 | Shows live Herdr TUI agents and their states as a 16-bit fantasy guild. |
| [**JYasha11/herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face) | 4 | Shows an increasingly urgent ASCII-art face when a Herdr agent is blocked and waiting for input, making overlooked approvals difficult to miss. |
| [**suisya-systems/herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office) | 4 | A terminal pixel-art office where Herdr agents appear as animated desk workers, blocked agents raise timed alerts, and selecting a character focuses its pane. |
| [**yuya-take/herdr-starkeep**](https://github.com/yuya-take/herdr-starkeep) | 2 | Draws the agents running in Herdr as knights on an orbital training ship, with one room per space and subagents shown as apprentices. Reads agent state from the Herdr socket and subagent events from a Claude Code hook. |
| [**pvgomes/agent-visualizer**](https://github.com/pvgomes/agent-visualizer) | 2 | Shows coding agents as workers in a pixel-art office, one desk per agent. In herd mode the office lists the agents in Herdr panes, poses them by Herdr state, and can open or start agents in Herdr workspaces. |

**[All 34 projects →](catalog/06-worktrees-and-terminal.md#agent-visualizations-and-terminal-games)**

### Herdr TUI themes and appearance

*19 projects. Themes and visual customizations for the Herdr TUI.*

| Project | Stars | What it does |
|---|--:|---|
| [**qintmb/herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker) | 17 | Applies terminalcolors.com palettes to Herdr TUI interface elements through a popup theme picker. |
| [**promptegrity/grok-themes · herdr**](https://github.com/promptegrity/grok-themes/tree/HEAD/herdr) | 9 | Applies GrokNight or GrokDay colors to the Herdr TUI and adds an optional powerline-style branch indicator. |
| [**ariel-ps/herdr-colors**](https://github.com/ariel-ps/herdr-colors) | 5 | Assigns distinct color slots to Herdr TUI panes and can repaint existing panes. |
| [**magimetal/matrix-themes · herdr**](https://github.com/magimetal/matrix-themes/tree/HEAD/herdr) | 3 | Applies a Matrix-inspired green palette to the Herdr TUI using a configuration snippet. |
| [**AkashJana18/zenbones-herdr**](https://github.com/AkashJana18/zenbones-herdr) | 3 | Adds 23 zenbones color themes with light and dark variants to Herdr TUI. |
| [**s3rgiosan/herdr-theme-synthwave-84**](https://github.com/s3rgiosan/herdr-theme-synthwave-84) | 2 | Applies the Synthwave '84 neon palette to the Herdr TUI by writing theme tables to config.toml after backing up your previous theme. |
| [**nertzy/herdr-flexoki**](https://github.com/nertzy/herdr-flexoki) | 1 | Adds Flexoki light and dark themes to Herdr TUI, including an automatic appearance option. |
| [**sp-night/herdr**](https://github.com/sp-night/herdr) | 1 | Adds three São Paulo-inspired dark color palettes to Herdr TUI. |
| [**codingquark/herdr-modus-themes**](https://github.com/codingquark/herdr-modus-themes) | 0 | Installs the light Modus Operandi and dark Modus Vivendi palettes for the Herdr TUI. |
| [**Young1108/herdr-cyber-style**](https://github.com/Young1108/herdr-cyber-style) | 0 | Applies a dark cyber theme and workspace layout to Herdr TUI on macOS, with a backup of the previous configuration. |

**[All 19 projects →](catalog/06-worktrees-and-terminal.md#herdr-tui-themes-and-appearance)**

### Security guards and collision detectors

*21 projects. Safety monitors that warn of worktree collisions, credential leaks, or destructive edits.*

| Project | Stars | What it does |
|---|--:|---|
| [**termaxa/termaxa · herdr-plugin**](https://github.com/termaxa/termaxa/tree/main/herdr-plugin) | 27 | Runs Claude Code or Codex under Termaxa command policies in Herdr TUI and shows refusals and audit records. |
| [**schemaitat/herdr-nono-plugin**](https://github.com/schemaitat/herdr-nono-plugin) | 6 | Runs OpenCode in nono sandboxes from Herdr TUI on Linux, with separate client and server profiles. |
| [**mcc0x/herdr-redact**](https://github.com/mcc0x/herdr-redact) | 2 | Warns when an agent pane has printed credentials before screenshots, streaming, or chat paste operations occur. |
| [**StructuPath/herdr-guard**](https://github.com/StructuPath/herdr-guard) | 2 | Monitors Herdr TUI panes for configured command-policy violations and can interrupt matching commands. An optional Claude Code hook checks tool calls before execution. |
| [**mcc0x/herdr-collide**](https://github.com/mcc0x/herdr-collide) | 1 | Warns when agents working in separate Git worktrees of the same repository are about to collide or conflict. |
| [**asumaran/asconfirmclose**](https://github.com/asumaran/asconfirmclose) | 1 | Closes an idle Herdr TUI pane immediately but asks for confirmation when a foreground process is running. |
| [**zenodea/fence**](https://github.com/zenodea/fence) | 1 | Turns a Herdr TUI space into a sandboxed pen where every shell can write only the pen folder and reach allowed domains. Uses bubblewrap and nftables on Linux. |
| [**IniZio/nexus · plugins/herdr**](https://github.com/IniZio/nexus/tree/main/plugins/herdr) | 1 | Attaches Herdr TUI to nexus microVM sandboxes, listing and creating them from the plugin, with auto port forwarding. Sandboxes are Cloud Hypervisor VMs on Linux with credentials kept on the host. |
| [**pauljohnchamberlain/herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard) | 0 | Lets coding agents inspect Herdr TUI sessions and make guarded workspace renames or close eligible inactive work. |
| [**cheunglok97/close-guard**](https://github.com/cheunglok97/close-guard) | 0 | Asks for confirmation before closing a Herdr TUI tab or pane. |

**[All 21 projects →](catalog/06-worktrees-and-terminal.md#security-guards-and-collision-detectors)**

### Plugin collections, frameworks, and ready-made configs

*49 projects. Plugin bundles, shared libraries for plugin authors, and ready-made Herdr configurations to install and adapt.*

| Project | Stars | What it does |
|---|--:|---|
| [**ogulcancelik/herdr-plugin-examples**](https://github.com/ogulcancelik/herdr-plugin-examples) | 22 | Shows standalone Herdr TUI plugin examples for Telegram notifications, development layouts, GitHub link previews, and Rust release checks. |
| [**ythx-101/herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass) | 14 | Applies macOS workspace presets and a workflow plugin for a translucent Herdr TUI workspace. |
| [**MIDO-ruby7/herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory) | 12 | A directory of Herdr plugins organized by the task a user wants to accomplish. |
| [**choplin/herdr-plugins**](https://github.com/choplin/herdr-plugins) | 10 | Collects Herdr TUI plugins for agent metadata, agent navigation, text selection, repository identity, and pane splitting as Git submodules. |
| [**Phoobobo/herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager) | 9 | Inventories and manages skills, MCP servers, plugins and hooks across agent configuration directories from a Herdr TUI plugin or CLI. |
| [**vonzelle-vzt/herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions) | 7 | Installs a complete 13-panel developer environment inside Herdr for diagnostics, language-server completion, tests, and in-terminal agent diff review. |
| [**JJLiebig/herdr-plugins**](https://github.com/JJLiebig/herdr-plugins) | 7 | Collects Herdr TUI plugins for GitHub status, cache timing, worktree discovery, agent dispatch and Stream Deck controls. |
| [**vika2603/herdr-plugin-manager**](https://github.com/vika2603/herdr-plugin-manager) | 5 | Browses the Herdr TUI plugin marketplace and installs, enables, disables, and updates plugins from a popup or CLI. |
| [**Newt6611/herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust) | 3 | Builds Herdr TUI plugins in Rust with application state, configuration, event handlers, and a socket client. |
| [**JacobAtchley/herdr-plugins**](https://github.com/JacobAtchley/herdr-plugins) | 3 | Collects Herdr TUI plugins for agent inboxes, command palettes, Git views, project running and zen mode. |

**[All 49 projects →](catalog/06-worktrees-and-terminal.md#plugin-collections-frameworks-and-ready-made-configs)**

---

## 7. Apps, companion integrations, and installation

*481 projects. Native applications, web dashboards, hardware companions, supporting utilities, and setup packages.* The top 10 of each subcategory by stars are below; the full list is in [catalog/07-apps-and-installation.md](catalog/07-apps-and-installation.md).

### Native desktop and mobile apps

*123 projects. Installed applications and launchers that provide a native interface to Herdr on desktop or mobile operating systems.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**sheprd-labs/sheprd**](https://github.com/sheprd-labs/sheprd) | 2,260 | Opens Herdr TUI and herdr-core terminal sessions in a native desktop client. |
| [**ZingerLittleBee/Heeler**](https://github.com/ZingerLittleBee/Heeler) | 860 | Supervises Herdr agents from an iOS console with SSH terminals, QR pairing, and push notifications. |
| [**missuo/herdrm**](https://github.com/missuo/herdrm) | 794 | Adds a native macOS console for Herdr to drive coding agents and monitor live terminals across devices. |
| [**themartianapp/herdrup**](https://github.com/themartianapp/herdrup) | 242 | Monitors Herdr TUI agents and opens their terminals from an iOS app. |
| [**kosumic/whip**](https://github.com/kosumic/whip) | 141 | Connects mobile devices to Herdr as an agent-native SSH client designed specifically for multiplexer workflows. |
| [**kenn-io/ghosthub**](https://github.com/kenn-io/ghosthub) | 108 | Opens local and SSH-hosted Herdr TUI, tmux, and Zellij sessions in a native macOS terminal with worktree creation. |
| [**benkraus/herdr-mobile**](https://github.com/benkraus/herdr-mobile) | 67 | Controls Herdr TUI sessions from iOS or Android through a separately deployed relay. |
| [**cobanov/herdrchat**](https://github.com/cobanov/herdrchat) | 63 | Controls Herdr coding agents from an iPhone or iPad. |
| [**minchenlee/flockbook**](https://github.com/minchenlee/flockbook) | 52 | Shows agent conversations in a native macOS app or Herdr app layout and lets users answer prompts. |
| [**sisyphuslabs/doriterm**](https://github.com/sisyphuslabs/doriterm) | 39 | Connects desktop, browser and phone clients to herdr-core terminals across an encrypted machine mesh. |

**[All 123 projects →](catalog/07-apps-and-installation.md#native-desktop-and-mobile-apps)**

### Web dashboards and remote viewers

*125 projects. Browser-based monitors, remote controls, and visual scenes for following Herdr agents from another screen or device.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**devswha/ovis**](https://github.com/devswha/ovis) | 2,011 | Shows Herdr agent transcripts and terminals in a desktop or phone browser, with approval cards and SSH connections. |
| [**AltanS/collie**](https://github.com/AltanS/collie) | 1,624 | Shows terminal agents in a phone web app and lets users answer them remotely. |
| [**dcolinmorgan/herdr-remote**](https://github.com/dcolinmorgan/herdr-remote) | 449 | Monitors and controls Herdr agents through a macOS menu bar, phone dashboard, and Telegram. |
| [**0cv/herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay) | 375 | Combines Herdr agents from multiple machines in an installable phone web app. |
| [**powerfooI/roamgate**](https://github.com/powerfooI/roamgate) | 325 | Adds a web client for Herdr with mobile optimization, browser terminals, workspace management, and session inspection. |
| [**arronKler/pairfob**](https://github.com/arronKler/pairfob) | 183 | Opens paired Herdr agent sessions from a phone or browser, with optional Android access. |
| [**kcosr/herdr-web**](https://github.com/kcosr/herdr-web) | 165 | Monitors and controls Herdr TUI workspaces and terminal panes from a desktop or mobile browser. |
| [**lamngockhuong/termote**](https://github.com/lamngockhuong/termote) | 71 | Streams Herdr TUI or herdr-core sessions to a self-hosted browser and mobile PWA, with a TUI plugin for opening and sharing panes. |
| [**ragamo/herdr-flock**](https://github.com/ragamo/herdr-flock) | 44 | Represents active Herdr agents as animated sheep and records completed sessions in a persistent graveyard log. |
| [**alecuba16/herdr-webui**](https://github.com/alecuba16/herdr-webui) | 44 | Browses Herdr-compatible workspaces, terminals, worktrees, and Git operations in a web UI. |

**[All 125 projects →](catalog/07-apps-and-installation.md#web-dashboards-and-remote-viewers)**

### Hardware and ambient displays

*47 projects. Keypads, watches, desk devices, and compact displays that turn agent state into physical controls or at-a-glance signals.*

| Project | Stars | What it does |
|---|--:|---|
| [**timvdhoorn/stream-deck-herdr-plugin**](https://github.com/timvdhoorn/stream-deck-herdr-plugin) | 32 | Assigns a key to each agent, displays its state with a color and icon, and focuses the matching Herdr pane when pressed. |
| [**Unayung/herdr-watch**](https://github.com/Unayung/herdr-watch) | 31 | A native Apple Watch companion that shows Herdr agent activity and alerts the wearer when an agent finishes or needs input. |
| [**spencerbull/xeneon-edge-agents**](https://github.com/spencerbull/xeneon-edge-agents) | 14 | An Omarchy and Herdr agent command center designed for the Corsair XENEON EDGE display, with conservative handling when state cannot be confirmed. |
| [**walcew/herdr-assist**](https://github.com/walcew/herdr-assist) | 13 | An ESP32-S3 desk display that shows Herdr session states and sounds a bell when an agent is waiting for a decision or approval. |
| [**mrshu/muxboard**](https://github.com/mrshu/muxboard) | 11 | Shows Herdr agent attention status and CodexBar usage metrics on a Stream Deck+ dashboard. |
| [**alasano/house-of-herdr**](https://github.com/alasano/house-of-herdr) | 8 | Maps Herdr TUI agent status and controls to the Work Louder Codex Micro keypad, dial, and joystick. |
| [**finna/omarchy-herdr-hud**](https://github.com/finna/omarchy-herdr-hud) | 7 | Monitors and prompts Herdr agents from a draggable Omarchy overlay. |
| [**niklasberglund/herdr-logi-plugin**](https://github.com/niklasberglund/herdr-logi-plugin) | 6 | Shows Herdr TUI workspace and agent status on a Logitech MX Keypad and focuses a selected pane on keypress. |
| [**Resilient-Software/herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck) | 4 | Mirrors Herdr TUI workspaces to a Stream Deck with repository, branch and agent-status tiles. |
| [**fedeya/corral**](https://github.com/fedeya/corral) | 3 | Shows Herdr TUI agents as animated critters on a Stream Deck Plus and focuses an agent when its key is tapped. |

**[All 47 projects →](catalog/07-apps-and-installation.md#hardware-and-ambient-displays)**

### Processes, ports, sandboxes, and remote machines

*28 projects. Tools for watching and stopping dev servers and listening ports, cleaning up leftover processes, and running agents or shells in sandboxes, VMs, containers, and remote hosts.*

| Project | Stars | What it does |
|---|--:|---|
| [**dirien/herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin) | 13 | Runs Claude Code, Codex, Gemini CLI, and other coding agents in separate Docker Sandboxes from Herdr TUI. |
| [**sudoeren/herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker) | 7 | Runs lazydocker in a herdr split pane or its own tab. |
| [**dvdksn/sbx-herdr**](https://github.com/dvdksn/sbx-herdr) | 6 | Registers Docker Sandboxes as Herdr TUI SSH machines and identifies sandbox agents in local panes. |
| [**carze/herdr-smolmachine**](https://github.com/carze/herdr-smolmachine) | 5 | Starts coding agents in libkrun or KVM microVMs from Herdr panes and lists running sandboxes. |
| [**ivorpad/herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel) | 1 | Lists local listening ports and opens, copies, or stops public tunnels from a Herdr TUI pane. |
| [**ivorpad/herdr-ports**](https://github.com/ivorpad/herdr-ports) | 1 | Adds a popup that lists listening ports, names the project behind each one, and kills or opens it. |
| [**AZenking/herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center) | 1 | Adds a Herdr popup for monitoring and focusing local Node.js, Bun, and Deno services. |
| [**Slimydog21/herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm) | 1 | Controls an existing NixOS development VM from a Herdr TUI pane, including boot, stop, monitoring, and SSH. |
| [**abcxff/herdr-docker**](https://github.com/abcxff/herdr-docker) | 1 | Keeps track of docker builds like you do with agents for herdr. |
| [**Keepstateai/cli · herdr**](https://github.com/Keepstateai/cli/tree/main/herdr) | 1 | Shows KeepState sessions, agents, saved points and Cruise receipts in Herdr panes through the ks client. Sends a Herdr notification when a Cruise job finishes. |

**[All 28 projects →](catalog/07-apps-and-installation.md#processes-ports-sandboxes-and-remote-machines)**

### Agent support, auto-approve, retry, and keep-awake helpers

*18 projects. Add-ons that teach Herdr about extra coding agents, auto-approve or auto-continue stalled agents after rate limits, and keep the machine awake while agents work.*

| Project | Stars | What it does |
|---|--:|---|
| [**scrappylabsai/podr**](https://github.com/scrappylabsai/podr) | 3 | Adds Reasonix and DeepSeek Harness detection to a Herdr TUI fork and includes a client for attaching to DSH sessions. |
| [**XiangQhello/codex-claude-auto-enter**](https://github.com/XiangQhello/codex-claude-auto-enter) | 3 | Sends repeated Enter presses to a selected Herdr TUI pane and stops when Codex or Claude Code becomes idle. |
| [**RenKoya1/herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all) | 3 | Approves every pending agent permission request in Herdr with one keystroke. |
| [**bestony/herdr-codex-capacity-retry**](https://github.com/bestony/herdr-codex-capacity-retry) | 1 | Automatically continues Codex sessions in Herdr after capacity-related interruptions. |
| [**susomejias/herdr-awake**](https://github.com/susomejias/herdr-awake) | 1 | Keeps the machine awake while Herdr agents are busy. |
| [**ichadhr/herdr-zcode**](https://github.com/ichadhr/herdr-zcode) | 1 | Adds ZCode agent support to Herdr TUI, showing zcode panes in the sidebar with live working, blocked, and idle state. Registers hooks in the zcode settings file. |
| [**jaaacki/herdr-plugin-minimax-code**](https://github.com/jaaacki/herdr-plugin-minimax-code) | 1 | Adds MiniMax Code support to Herdr TUI by launching mcode in a new pane and registering hand-started mcode sessions so they appear as agents. |
| [**jewei/herdr-caffeinated**](https://github.com/jewei/herdr-caffeinated) | 1 | Keeps a Mac awake with caffeinate while a Herdr agent works and lets it sleep after 60 idle seconds. A pause action turns it off. |
| [**scheron/herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep) | 0 | Adds a herdr plugin that puts your Mac to sleep once no coding agent is working any more. Arm it before bed and it waits for every agent to settle, then journals what each one was doing, including the ones that ended up blocked. |
| [**islee23520/herdr-omo-agent**](https://github.com/islee23520/herdr-omo-agent) | 0 | Registers OmO sessions as coding agents on stock Herdr TUI 0.8.2; the author’s OmO-native fork does not need this package. |

**[All 18 projects →](catalog/07-apps-and-installation.md#agent-support-auto-approve-retry-and-keep-awake-helpers)**

### Notes, prompts, clipboard, and file helpers

*32 projects. Per-tab scratchpads and notes, saved prompt decks, task lists, credential pickers, clipboard and image paste, and file transfer or reveal helpers for Herdr panes.*

| Project | Stars | What it does |
|---|--:|---|
| [**Resetnak/herdr-logbook**](https://github.com/Resetnak/herdr-logbook) | 13 | Manages Markdown tasks and decisions in an offline notebook for Herdr workspaces. |
| [**vjeantet/herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad) | 6 | Docks a plain-text scratchpad at the bottom of a tab, one persistent buffer per tab, for composing a prompt where Enter can't send it half-finished. `Ctrl+E` moves it, or just the selection, into an agent of the same tab without submitting; `Ctrl+C` copies over OSC 52. |
| [**kosuketut/herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder) | 5 | Downloads files created or changed in a remote Herdr pane to a local Mac. A plugin action detects paths in the active pane and transfers the selected artifact over the remote connection. |
| [**ddfonseca/herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image) | 5 | Saves an image from the macOS or Linux clipboard to disk and pastes its file path into the active pane for use by multimodal agents. |
| [**mrolafsson/herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer) | 5 | Transfers files between a local machine and a remote Herdr TUI host over SSH and sends their paths to agents. |
| [**ivolkoff/herdr-huddle**](https://github.com/ivolkoff/herdr-huddle) | 4 | Opens rich questions over a Herdr TUI agent pane and returns the answers to the agent as JSON. |
| [**mdetweil/herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask) | 2 | Opens Lazytask in a Herdr TUI split or tab and adds Taskwarrior quick actions. |
| [**WillowMist/herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden) | 2 | Searches a Bitwarden vault from a Herdr TUI popup and copies or pastes selected credentials. |
| [**chrisg32/tsk**](https://github.com/chrisg32/tsk) | 2 | Manages plain-text tasks in a Rust TUI that runs standalone or as a Herdr plugin. |
| [**niceview/mac-finder-quick-actions**](https://github.com/niceview/mac-finder-quick-actions) | 1 | Opens Finder selections in VS Code or a new Herdr TUI workspace through macOS quick actions and a drag-and-drop launcher. |

**[All 32 projects →](catalog/07-apps-and-installation.md#notes-prompts-clipboard-and-file-helpers)**

### Developer tool panes and everyday utilities

*56 projects. Panes that open database, API, CI, Git, and cloud clients, plus translators, media players, calendars, feeds, and other everyday utilities beside your agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**coryshaw1/herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp) | 16 | Opens the cliamp audio player in a floating Herdr TUI pane while playback continues in a detached session. |
| [**pivoshenko/musicforprogramming · plugins/herdr/mfp.player**](https://github.com/pivoshenko/musicforprogramming/tree/main/plugins/herdr/mfp.player) | 12 | Opens the musicforprogramming.net player in a Herdr TUI pane and maps playback controls to actions. |
| [**ablause/herdr-flutter**](https://github.com/ablause/herdr-flutter) | 4 | A Herdr sidebar for watching, hot-reloading, and inspecting a running Flutter app beside the coding agent working on it. |
| [**Tomatio13/herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail) | 3 | Browses Gmail in a Herdr TUI split using fzf and gogcli, with mail actions and background notifications. |
| [**RizRiyz/pixtui**](https://github.com/RizRiyz/pixtui) | 2 | Opens a terminal pixel-art editor in a Herdr TUI pane with layers, animation, and PNG or GIF export. |
| [**Javamomma/herdr-scribe**](https://github.com/Javamomma/herdr-scribe) | 2 | Streams microphone audio to temporary panes and creates meeting notes, policy checks, and draft tickets without saving raw audio. |
| [**neospeed83/herdr-standup**](https://github.com/neospeed83/herdr-standup) | 2 | Builds a daily standup from Git commits and optional notes, then opens the report from a Herdr TUI workspace. |
| [**Tomatio13/herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar) | 2 | Browses Google Calendar events in an fzf panel and creates a Herdr TUI worktree and workspace from an event. |
| [**arhen/devnull-tui**](https://github.com/arhen/devnull-tui) | 2 | Reads the /dev/null developer commit network in a Herdr TUI pane with a feed, threads, replies, stars and an inbox, and opens links in a Herdr browser tab. Also runs as a standalone terminal client. |
| [**wazum/herdr-polyglot**](https://github.com/wazum/herdr-polyglot) | 1 | Translates prompts into English before sending them to an agent pane in Herdr. |

**[All 56 projects →](catalog/07-apps-and-installation.md#developer-tool-panes-and-everyday-utilities)**

### Setup, packages, and version management

*52 projects. Guides, configuration bundles, installers, package definitions, and tools for reproducible Herdr environments.*

| Project | Stars | What it does |
|---|--:|---|
| [**speardragon/herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager) | 86 | A small in-terminal menu for browsing, installing, updating, enabling, and disabling Herdr plugins through the standard plugin command-line interface. |
| [**mifunedev/agro**](https://github.com/mifunedev/agro) | 43 | Runs Herdr inside a Docker workspace for coding agents on a laptop or remote VM, installed with `agro tool install herdr`. Parallel agents use separate git worktrees, work continues after the terminal disconnects, and you choose the harness: Claude Code, Codex, Pi, OpenCode, or T3 Code. |
| [**joeseesun/herdr-guide**](https://github.com/joeseesun/herdr-guide) | 29 | A Chinese-language practical guide that explains what Herdr is useful for and how to get started. |
| [**natori-hrj/herdr-lazy**](https://github.com/natori-hrj/herdr-lazy) | 28 | A declarative Herdr plugin manager with a dedicated terminal interface, a lockfile, version pinning, synchronization from one list, and support for prebuilt binaries. |
| [**Yassimba/loom**](https://github.com/Yassimba/loom) | 13 | A curated collection of agent skills, Pi packages, and Herdr plugins with a single command-line setup tool. |
| [**diegopzz/herdr-updater**](https://github.com/diegopzz/herdr-updater) | 10 | Keeps Herdr and its plugins current across a whole fleet, safely. |
| [**garavitgabriel/claude-remote-kit**](https://github.com/garavitgabriel/claude-remote-kit) | 10 | Sets up Herdr, Tailscale, and Termius for remotely accessing coding agent sessions from a phone. |
| [**pedrogiroldo/agentbox**](https://github.com/pedrogiroldo/agentbox) | 6 | Runs Herdr, Claude Code, Codex, OpenCode, and mobile-friendly Neovim in an Ubuntu container reachable over SSH. |
| [**ram4-dev/herdr-config**](https://github.com/ram4-dev/herdr-config) | 4 | Installs pinned Herdr TUI plugins and portable keybindings with configuration snapshots and rollback. |
| [**hdosys/herdr-sandbox**](https://github.com/hdosys/herdr-sandbox) | 3 | Runs coding agents in disposable Windows Sandbox workstations isolated from the host. |

**[All 52 projects →](catalog/07-apps-and-installation.md#setup-packages-and-version-management)**

---

## 8. Experimental projects

*10 projects. Experimental Herdr projects and prototypes.* The top 10 of each subcategory by stars are below; the full list is in [catalog/08-experimental.md](catalog/08-experimental.md).

### Experiments, concepts, and scaffolds

*10 projects. Ideas and prototypes that are useful to study but may be incomplete, read-only, or not yet installable.*

| Project | Stars | What it does |
|---|--:|---|
| [**eliasstravik/herdr-call**](https://github.com/eliasstravik/herdr-call) | 16 | An early TypeScript prototype for translating spoken commands into Herdr navigation and input through the local socket. |
| [**wraithyy/herdr-openr**](https://github.com/wraithyy/herdr-openr) | 8 | Extracts file paths and URLs from recent pane output and Claude Code transcripts, then presents them in a fuzzy finder for quick opening. |
| [**hmu332233/herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs) | 2 | An experimental plugin laboratory containing early prototypes for agent launching, workspace metrics, and worktree symlinking before they move into separate projects. |
| [**rohanthewiz/herdr-web**](https://github.com/rohanthewiz/herdr-web) | 1 | Renders Herdr pane frames with color, mouse, clipboard, and hyperlink support; keyboard and paste input are currently disabled, so it mainly works as a viewer. |
| [**shoaibkhanz/herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus) | 1 | An early navigation plugin designed to move with Ctrl+h/j/k/l across Herdr panes and wrap at workspace boundaries. |
| [**ugurtarlig/herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker) | 1 | An early pane-picker prototype that overlays one-character hints on visible panes for direct keyboard focus. |
| [**speardragon/herdr-labs**](https://github.com/speardragon/herdr-labs) | 1 | Provides herdr plugin lab, AI-agent plugin idea contests: 9 agents compete, AI judges score. |
| [**malone-c/herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer) | 0 | An in-development layout manager that automatically rebalances pane sizes when splits are opened or closed, reducing cramped nested layouts. |
| [**robinbraemer/herdr-axi**](https://github.com/robinbraemer/herdr-axi) | 0 | An early command-line interface designed to make Herdr workspace operations easier for coding agents to use. |
| [**yoshimi-I/gengar.nvim**](https://github.com/yoshimi-I/gengar.nvim) | 0 | An early Neovim environment that keeps agents and Hunk-based diff review in Herdr while leaving Neovim focused on editing. |

---

## Resources

- **[Herdr Guide](https://herdr.dev/guide/)**: Prompts and first steps for shaping the Herdr app by asking your agent.
- **[Herdr app agent guide](https://github.com/herdrdev/herdr-app/blob/master/defaults/AGENTS.md)**: The `~/.config/herdr-app/AGENTS.md` file that tells an agent every command, file, and setting it can change.
- **[Gallery](https://herdr.dev/gallery/)**: Community layouts and mods for the Herdr app, each installable with one line pasted to your agent.
- **[herdr-core](https://herdr.dev/core/)**: The terminal runtime under the app; agents read its manual with `hc --skill` and its API with `hc schema`.
- **[Herdr TUI documentation](https://herdr.dev/tui/docs/)**: The manual for the original terminal app, covering installation, workspaces, keybindings, and configuration.
- **[Herdr TUI Socket API](https://herdr.dev/tui/docs/socket-api/)**: Protocol documentation for controlling Herdr TUI over its local Unix socket.
- **[Herdr TUI plugin marketplace](https://herdr.dev/tui/plugins/)**: The official directory of Herdr TUI plugins, built from GitHub repositories tagged `herdr-plugin`.
- **[Herdr TUI agent skill](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md)**: Instructions that teach an agent how to drive Herdr TUI.

- **[Field guides](docs/)**: Fact-checked guides in this repo for building on Herdr: [Herdr app](docs/herdr-app.md), [herdr-core](docs/herdr-core.md), and Herdr TUI [socket API](docs/socket-api.md), [configuration](docs/configuration.md), [integrations](docs/integrations.md), and [agent workflows](docs/agent-workflows.md).

## Reference

- **Agent guides:** Point an agent at `~/.config/herdr-app/AGENTS.md` (Herdr app), `hc --skill` (herdr-core), or `SKILL.md` (Herdr TUI) before asking it to change anything.
- **Agent status:** herdr-core reads working, done, and blocked states from programs that emit OSC 7501, the Program Status Protocol: `printf '\e]7501;state=blocked:app=my-agent\e\\'`.
- **Socket client:** Herdr TUI listens on `$XDG_CONFIG_HOME/herdr/herdr.sock` (default `~/.config/herdr/herdr.sock`) for newline-delimited JSON commands that manage tabs, panes, and agents.
- **Git worktrees:** Pair Herdr tabs with isolated git worktrees (`git worktree add`) to run concurrent agents safely.
