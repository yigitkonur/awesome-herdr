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

1. [Run and orchestrate agents (639)](#1-run-and-orchestrate-agents)
   - [Official Herdr projects and skill (5)](#official-herdr-projects-and-skill)
   - [Multi-agent fleets and supervisors (126)](#multi-agent-fleets-and-supervisors)
   - [Swarm, mob, and consensus orchestrators (15)](#swarm-mob-and-consensus-orchestrators)
   - [Claude Code multi-agent teams (58)](#claude-code-multi-agent-teams)
   - [Claude Code: Account switchers and auth monitors (9)](#claude-code-account-switchers-and-auth-monitors)
   - [Pi supervisor workflows and extensions (92)](#pi-supervisor-workflows-and-extensions)
   - [Pi: Presence, memory, and status extensions (10)](#pi-presence-memory-and-status-extensions)
   - [Subagent launchers and delegation (108)](#subagent-launchers-and-delegation)
   - [Autonomous coding and pull-request loops (16)](#autonomous-coding-and-pull-request-loops)
   - [Task queues, backlogs, and event triggers (86)](#task-queues-backlogs-and-event-triggers)
   - [Linear, GitHub Issues, and issue-to-PR automation (50)](#linear-github-issues-and-issue-to-pr-automation)
   - [General workflows and skill packs (64)](#general-workflows-and-skill-packs)
2. [Herdr app layouts, mods, and themes (782)](#2-herdr-app-layouts-mods-and-themes)
   - [Herdr app agent boards and mission-control layouts (35)](#herdr-app-agent-boards-and-mission-control-layouts)
   - [Herdr app sidebar and space-organization layouts (51)](#herdr-app-sidebar-and-space-organization-layouts)
   - [Herdr app IDE, editor and Git-panel layouts (33)](#herdr-app-ide-editor-and-git-panel-layouts)
   - [Herdr app palette, glass and desktop-OS themed layouts (55)](#herdr-app-palette-glass-and-desktop-os-themed-layouts)
   - [Herdr app pixel-art, game, anime and cyberpunk layouts (71)](#herdr-app-pixel-art-game-anime-and-cyberpunk-layouts)
   - [Herdr app sidebars, tabs, and visual mods (135)](#herdr-app-sidebars-tabs-and-visual-mods)
   - [Herdr app keys, navigation, and attention alerts (103)](#herdr-app-keys-navigation-and-attention-alerts)
   - [Herdr app usage, quota, and system status displays (50)](#herdr-app-usage-quota-and-system-status-displays)
   - [Herdr app Git, code review, and worktree panels (69)](#herdr-app-git-code-review-and-worktree-panels)
   - [Herdr app file, Markdown, and notes panels (56)](#herdr-app-file-markdown-and-notes-panels)
   - [Herdr app task boards, developer services, and mod bundles (116)](#herdr-app-task-boards-developer-services-and-mod-bundles)
   - [Herdr app themes (8)](#herdr-app-themes)
3. [Connect through MCP and the socket API (338)](#3-connect-through-mcp-and-the-socket-api)
   - [MCP servers (21)](#mcp-servers)
   - [Socket API and herdr-core clients and SDKs (41)](#socket-api-and-herdr-core-clients-and-sdks)
   - [Chat alerts: Telegram, Discord, and Slack (33)](#chat-alerts-telegram-discord-and-slack)
   - [Desktop, mobile, and webhook notifications (73)](#desktop-mobile-and-webhook-notifications)
   - [Telemetry, events, and quota streaming (34)](#telemetry-events-and-quota-streaming)
   - [Voice, hardware, and remote bridges (57)](#voice-hardware-and-remote-bridges)
   - [Protocol and third-party bridges (79)](#protocol-and-third-party-bridges)
4. [Editor integrations (108)](#4-editor-integrations)
   - [Neovim navigation and splits (30)](#neovim-navigation-and-splits)
   - [Full Neovim-hosted workspaces (4)](#full-neovim-hosted-workspaces)
   - [VS Code, Cursor, and dev containers (16)](#vs-code-cursor-and-dev-containers)
   - [Vim, Kakoune, and other editors (13)](#vim-kakoune-and-other-editors)
   - [REPL and code dispatchers (8)](#repl-and-code-dispatchers)
   - [Editor plugins and bridges (37)](#editor-plugins-and-bridges)
5. [Switch and restore sessions (262)](#5-switch-and-restore-sessions)
   - [Fuzzy session switchers and terminal pickers (111)](#fuzzy-session-switchers-and-terminal-pickers)
   - [Persistence, snapshots, and state restoration (68)](#persistence-snapshots-and-state-restoration)
   - [Workspace and multi-session management (83)](#workspace-and-multi-session-management)
6. [Worktrees and terminal experience (1333)](#6-worktrees-and-terminal-experience)
   - [Git worktree automation (139)](#git-worktree-automation)
   - [Workspace lifecycle and multi-repository tools (45)](#workspace-lifecycle-and-multi-repository-tools)
   - [Diff review and code inspection (89)](#diff-review-and-code-inspection)
   - [File viewers, terminal browsers, and markdown previews (81)](#file-viewers-terminal-browsers-and-markdown-previews)
   - [Pane navigation and overlay hints (60)](#pane-navigation-and-overlay-hints)
   - [Pane layout management (44)](#pane-layout-management)
   - [Terminal keybindings and shortcut helpers (88)](#terminal-keybindings-and-shortcut-helpers)
   - [Command palettes and workspace switchers (62)](#command-palettes-and-workspace-switchers)
   - [Status lines and workspace metadata (142)](#status-lines-and-workspace-metadata)
   - [Automatic tab, pane, and workspace names (92)](#automatic-tab-pane-and-workspace-names)
   - [Sidebar grouping, ordering, and filtering (45)](#sidebar-grouping-ordering-and-filtering)
   - [Sidebar badges, tokens, and status indicators (88)](#sidebar-badges-tokens-and-status-indicators)
   - [Status overlays, HUDs, and agent timers (78)](#status-overlays-huds-and-agent-timers)
   - [Context meters and rate-limit gauges (90)](#context-meters-and-rate-limit-gauges)
   - [Output inspection, logs, and transcripts (67)](#output-inspection-logs-and-transcripts)
   - [Agent visualizations and terminal games (34)](#agent-visualizations-and-terminal-games)
   - [Herdr TUI themes and appearance (19)](#herdr-tui-themes-and-appearance)
   - [Security guards and collision detectors (21)](#security-guards-and-collision-detectors)
   - [Plugin collections, frameworks, and ready-made configs (49)](#plugin-collections-frameworks-and-ready-made-configs)
7. [Apps, companion integrations, and installation (491)](#7-apps-companion-integrations-and-installation)
   - [Native desktop and mobile apps (126)](#native-desktop-and-mobile-apps)
   - [Web dashboards and remote viewers (127)](#web-dashboards-and-remote-viewers)
   - [Hardware and ambient displays (47)](#hardware-and-ambient-displays)
   - [Processes, ports, sandboxes, and remote machines (28)](#processes-ports-sandboxes-and-remote-machines)
   - [Agent support, auto-approve, retry, and keep-awake helpers (20)](#agent-support-auto-approve-retry-and-keep-awake-helpers)
   - [Notes, prompts, clipboard, and file helpers (32)](#notes-prompts-clipboard-and-file-helpers)
   - [Developer tool panes and everyday utilities (56)](#developer-tool-panes-and-everyday-utilities)
   - [Setup, packages, and version management (55)](#setup-packages-and-version-management)
8. [Experimental projects (10)](#8-experimental-projects)
   - [Experiments, concepts, and scaffolds (10)](#experiments-concepts-and-scaffolds)
9. [Resources](#resources)
10. [Reference](#reference)

---

## 1. Run and orchestrate agents

*639 projects. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.* The top 10 of each subcategory by stars are below; the full list is in [catalog/01-run-and-orchestrate.md](catalog/01-run-and-orchestrate.md).

### Official Herdr projects and skill

*5 projects. Official Herdr applications, runtimes, integrations, examples, and agent instructions.*

| Project | What it does |
|---|---|
| [**herdrdev/herdr-app**](https://github.com/herdrdev/herdr-app) | Runs the official Herdr desktop app for terminals and coding agents on macOS, Windows, and Linux. |
| [**herdrdev/herdr-core**](https://github.com/herdrdev/herdr-core) | Runs persistent terminals and coding agents through the herdr-core runtime, with commands to start, message and wait for work on local or remote machines. |
| [**herdrdev/herdr**](https://github.com/herdrdev/herdr) | Runs the official Herdr TUI for organizing agents and terminals. The official [SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) teaches agents to control its workspaces, tabs, and panes. |
| [**herdrdev/herdr-layout-examples**](https://github.com/herdrdev/herdr-layout-examples) | Shows a collection of Herdr app window layouts including Board, Chat, Mission, Pasture and Threads, plus a tmux-style prefix mod. |
| [**herdrdev/herdr-nix**](https://github.com/herdrdev/herdr-nix) | Installs hash-verified Herdr TUI release binaries through Nix and offers a Cachix binary cache. |

### Multi-agent fleets and supervisors

*126 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*

| Project | What it does |
|---|---|
| [**kunchenguid/firstmate**](https://github.com/kunchenguid/firstmate) | Supervises coding agents in separate Herdr TUI tabs and isolated Git worktrees. Supports Claude Code, Pi, Codex, OpenCode, and other agent harnesses. |
| [**sisyphuslabs/dori-superagent**](https://github.com/sisyphuslabs/dori-superagent) | Runs a lead agent and parallel coding lanes in Herdr TUI tabs, with resource guards and a gated merge workflow. |
| [**stevenmichaelthomas/numbrone**](https://github.com/stevenmichaelthomas/numbrone) | Routes requests through a chief agent to project managers and parallel workers in Herdr TUI workspaces and Git worktrees. |
| [**chengyixu/oh-my-herdr**](https://github.com/chengyixu/oh-my-herdr) | Organizes Codex, Pi, and Claude Code profiles with persistent instructions in shared coding spaces using a separate Herdr-derived runtime. |
| [**wanshuiyin/SuperARIS**](https://github.com/wanshuiyin/SuperARIS) | Runs a persistent research team in Herdr with a lead agent and engineering and writing roles. |
| [**larcane97/clausona**](https://github.com/larcane97/clausona/blob/main/docs/usecases/herdr-fleet.md) | Splits a job across Herdr worktrees and panes from one Claude Code or Codex session, routing each worker to one of your accounts by remaining usage or to an API model such as DeepSeek. Part of clausona, a daemon-less multi-account manager that drives Herdr only through its CLI and checks each branch before removing a worktree. |
| [**aorumbayev/herdr-workflows**](https://github.com/aorumbayev/herdr-workflows) | Runs repeatable development and agent workflows from YAML files. Each manifest defines an ordered sequence of commands and agent interactions to execute inside Herdr workspaces. |
| [**junghan0611/entwurf**](https://github.com/junghan0611/entwurf) | Connects Pi, Claude Code, Codex, Copilot, OMP, and Antigravity sessions in Herdr or tmux so they can address, message, and open visible siblings without sharing auth, tools, or transcripts. Includes a Herdr integration for pi and Claude Code. |
| [**ericbust/namedrop**](https://github.com/ericbust/namedrop) | Sends named mentions between agents in Herdr TUI panes and workspaces. |
| [**meviusisback/agent-orchestr**](https://github.com/meviusisback/agent-orchestr) | Monitors live agent output and orchestrates multi-agent workspaces across Herdr, OpenCode, and Claude sessions. |

**[All 126 projects →](catalog/01-run-and-orchestrate.md#multi-agent-fleets-and-supervisors)**

### Swarm, mob, and consensus orchestrators

*15 projects. Parallel agent swarms, mob-programming groups, and multi-model consensus engines.*

| Project | What it does |
|---|---|
| [**aliceisjustplaying/swarmchat**](https://github.com/aliceisjustplaying/swarmchat) | Lets Claude Code and Codex or Astra exchange peer messages in Herdr while a third pane shows their shared log. |
| [**zekierman/herdr-council**](https://github.com/zekierman/herdr-council) | Asks coding agents in Herdr TUI the same question and combines blind peer rankings with a judge agent verdict. |
| [**enes/herdr-rooms**](https://github.com/enes/herdr-rooms) | Opens review rooms where Claude Code or Codex agents review each other in Herdr TUI. |
| [**HinchK/stampede**](https://github.com/HinchK/stampede) | Coordinates coding agents in Herdr TUI with ticket dispatch, independent checks, and a human-controlled integration queue. |
| [**conscientiousness/herdr-pstack-orchestrator**](https://github.com/conscientiousness/herdr-pstack-orchestrator) | Adds Agent Skills for running visible multi-model coding teams across Pi, Codex and Claude Code in Herdr panes. Adds pstack review loops with a controller and workers. |
| [**neospeed83/herdr-tournament**](https://github.com/neospeed83/herdr-tournament) | Runs independent Codex or Claude reviews of a branch or pull request, then consolidates findings through an adversarial judge workflow. |
| [**tuanhung303/herdr-swarm**](https://github.com/tuanhung303/herdr-swarm) | Runs agent waves in Herdr pane grids, routes messages through an optional mailbox, and collects results from multiple harnesses. |
| [**ndemeshchenko/herdr-peer-chat**](https://github.com/ndemeshchenko/herdr-peer-chat) | Lets Claude Code and Codex exchange messages in one Herdr tab through the agent API. |
| [**xzedx/herdr-derby**](https://github.com/xzedx/herdr-derby) | Sends one prompt to every agent in the current Herdr TUI tab and races them, with live timers and finishing ranks on pane borders. Can also start fresh agents in separate worktrees. |
| [**ArtMoreno/herdr-swarm**](https://github.com/ArtMoreno/herdr-swarm) | Races coding agents in Herdr panes and isolated Git worktrees, compare their diffs, and apply a winner. |

**[All 15 projects →](catalog/01-run-and-orchestrate.md#swarm-mob-and-consensus-orchestrators)**

### Claude Code multi-agent teams

*58 projects. Adapters and skills that organize Claude Code sessions into structured teams.*

| Project | What it does |
|---|---|
| [**caioniehues/herdmates**](https://github.com/caioniehues/herdmates) | Runs Claude Code multi-agent teams in Herdr through a teammux translation layer. Teammates work in isolated panes while a mission-control view reports their status and task progress. |
| [**mohseenrm/zj-agent-mob**](https://github.com/mohseenrm/zj-agent-mob) | Monitors coding agent fleets with Herdr-inspired workflows and pane observation. |
| [**neptunix/corral**](https://github.com/neptunix/corral) | Provides a kanban dashboard and control surface for Claude Code sessions running in herdr. |
| [**overflowy/herdr-adversarial-review**](https://github.com/overflowy/herdr-adversarial-review) | Provides a Claude Code skill for adversarial code review that spawns an automated reviewer in a Herdr split pane. |
| [**hapo-nghialuu/hod**](https://github.com/hapo-nghialuu/hod) | Coordinates Codex, Claude Code, and Grok Build agents safely through Herdr. |
| [**wangfan1998-github/herdr-hybrid**](https://github.com/wangfan1998-github/herdr-hybrid) | Orchestrates Claude Code hybrid teams with high-tier models supervising parallel worker panes in Herdr. |
| [**blaxel-ai/herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) | Runs coding agents in persistent Blaxel sandboxes from Herdr. |
| [**igor/crew-skill**](https://github.com/igor/crew-skill) | Coordinates a fleet of AI agents in Herdr where premium models lead and local models handle volume execution. |
| [**david-lutz/herdr-claude-teams**](https://github.com/david-lutz/herdr-claude-teams) | Maps Claude Code's experimental agent-team commands to Herdr's socket API, so teammates open as native Herdr panes instead of tmux panes. It requires Herdr 0.6.10 and supports Herdr metadata, notifications, and sidebar views. |
| [**rcosteira79/herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue) | Watches agents for usage-limit walls, badges the countdown to the reset ($wall), and re-prompts the agents you armed once the window reopens. |

**[All 58 projects →](catalog/01-run-and-orchestrate.md#claude-code-multi-agent-teams)**

### Claude Code: Account switchers and auth monitors

*9 projects. Tools for managing Claude multi-account rotation, OAuth keys, and quota monitoring.*

| Project | What it does |
|---|---|
| [**uwuclxdy/clauth · herdr-plugin**](https://github.com/uwuclxdy/clauth/tree/mommy/herdr-plugin) | Manages Claude Code accounts and usage from a Herdr TUI popup and tags panes with their active account. |
| [**wazum/herdr-grazr**](https://github.com/wazum/herdr-grazr) | Provides a simple and reliable auto account switcher for Claude Code: rotates to a fresh account before the 5-hour or weekly rate limit hits, so no pane ever stops at the usage quota. A Herdr plugin. |
| [**rcosteira79/herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch) | Switches Claude Code and Codex account profiles from a Herdr overlay or keybinding and labels panes with the active account. |
| [**aodanchenko/herdr-claude-usage**](https://github.com/aodanchenko/herdr-claude-usage) | Shows Claude Code plan usage and reset times in the Herdr TUI tab bar and a multi-account popup dashboard. |
| [**C0R0NELL/herdr-account-hub**](https://github.com/C0R0NELL/herdr-account-hub) | Switches between saved Codex and Claude Code accounts from one picker in Herdr TUI, shows usage, and applies available Codex resets. Codex switching reloads open chats while keeping their history and titles; Claude Code support is beta. |
| [**nolvane/herdr-multiaccount**](https://github.com/nolvane/herdr-multiaccount) | Keeps several Claude accounts side by side in Herdr, shows each account's 5-hour and 7-day usage and picks one per space. Moves new sessions to the next account at a limit. |
| [**supex0fan/herdr-claude-swap**](https://github.com/supex0fan/herdr-claude-swap) | Resumes each Claude Code pane through the claude-swap account that owns its existing session. |
| [**msiric/herdr-auth-picker**](https://github.com/msiric/herdr-auth-picker) | Switches the logged-in Claude Code or Codex account from a Herdr popup without logging out and back in. Backs up logins first so none is lost along the way. |
| [**johntrandall/herdr-claude-account-watch**](https://github.com/johntrandall/herdr-claude-account-watch) | Flags Claude Code panes in Herdr TUI that are logged out or have hit a usage limit, which Herdr otherwise shows as idle. |

### Pi supervisor workflows and extensions

*92 projects. Supervision harnesses, task planners, and extensions for Pi agents in Herdr.*

| Project | What it does |
|---|---|
| [**ogulcancelik/pi-extensions**](https://github.com/ogulcancelik/pi-extensions) | Extends Pi with overlays, parallel agent spawners, session recall, and direct Herdr pane control. |
| [**osolmaz/pi-workflows**](https://github.com/osolmaz/pi-workflows) | Provides a workflow engine, JSON control-flow system, and live terminal viewer for the Pi coding agent in Herdr. |
| [**boadij/pi-herdsman**](https://github.com/boadij/pi-herdsman) | Delegates work to asynchronous Pi agents in Herdr TUI, with nested delegation and fleet supervision. |
| [**edxeth/pi-subagents**](https://github.com/edxeth/pi-subagents) | Provides a Pi framework for foreground and background subagents, messaging, and multi-pane orchestration. |
| [**joelhooks/pi-bellwether**](https://github.com/joelhooks/pi-bellwether) | Exposes Herdr agent, pane, and session controls as Pi slash commands and LLM tools. It provides reusable start, send, read, focus, and stop operations for higher-level Pi workflows. |
| [**electric-dragon-80000v/pi-cowboy**](https://github.com/electric-dragon-80000v/pi-cowboy) | Runs Pi-supervised coding agents in Herdr TUI panes and isolated Git worktrees, including Claude Code, Codex and OpenCode. |
| [**AndrewJacop/pi-herdr**](https://github.com/AndrewJacop/pi-herdr) | Lets Pi spawn, steer, and collect results from Pi, Claude Code, Codex, and OpenCode agents in Herdr TUI panes. |
| [**oscabriel/pi-herdr-btw**](https://github.com/oscabriel/pi-herdr-btw) | Opens a separate Pi side conversation in a Herdr TUI pane without changing the parent transcript. |
| [**jillesme/pi-herdr-squad**](https://github.com/jillesme/pi-herdr-squad) | Creates visible, strictly read-only investigation teams for Pi inside Herdr. It is intended for parallel research and review tasks that must not modify the workspace. |
| [**ribbons-digital/pi-herd**](https://github.com/ribbons-digital/pi-herd) | Coordinates visible Pi lead and worker sessions in Herdr TUI panes, isolating code-changing roles in Git worktrees. |

**[All 92 projects →](catalog/01-run-and-orchestrate.md#pi-supervisor-workflows-and-extensions)**

### Pi: Presence, memory, and status extensions

*10 projects. Persistent memory trackers, presence indicators, and live status displays for Pi agents.*

| Project | What it does |
|---|---|
| [**RamonsDka/gs3-sidebar**](https://github.com/RamonsDka/gs3-sidebar) | Shows a read-only sidebar for Pi and Gentle Shell in Herdr TUI, including agent status, context, Git and subagents. |
| [**edxeth/herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree) | Shows Pi agents and their subagents as a Herdr TUI sidebar tree with worktree branches and Git status. |
| [**hanbong5938/herdr-omp-subagents**](https://github.com/hanbong5938/herdr-omp-subagents) | Shows the active Oh My Pi main-agent and subagent models in the Herdr TUI sidebar. |
| [**spi-ca/pi-herdr-presence**](https://github.com/spi-ca/pi-herdr-presence) | Extends Pi agent presence indicators and runtime status inside Herdr workspaces. |
| [**mastnacek/pi-herdr-sidebar**](https://github.com/mastnacek/pi-herdr-sidebar) | Shows Pi agent telemetry in a Herdr TUI pane or popup, including model, context window, tokens, cost, and skill gates read from the Pi session log. Built in Rust with Ratatui. |
| [**ubranch/omp-herdr-neighbors**](https://github.com/ubranch/omp-herdr-neighbors) | Tells an omp agent which other Herdr agents run beside it, with their status and last reply. Sends hidden context only when it changes and has no runtime dependencies. |
| [**Attamusc/pi-herdr**](https://github.com/Attamusc/pi-herdr) | Reports Pi lifecycle states to Herdr TUI so its sidebar shows working, blocked, done, and idle agents. |
| [**larryboiNEUQ/pi-herdr-ui-bridge**](https://github.com/larryboiNEUQ/pi-herdr-ui-bridge) | Reports blocking Pi extension prompts as Herdr agent blocked states so notification plugins can alert users. |
| [**BrianM0330/pi-herdr-snooze**](https://github.com/BrianM0330/pi-herdr-snooze) | Adds a forced snooze state to Pi agents in Herdr, controlled through `/snooze` or a key binding and independent of the underlying agent type. |
| [**markbrutx/pif-herdr-reporter**](https://github.com/markbrutx/pif-herdr-reporter) | Reports working and idle states from the pif coding agent to its Herdr TUI pane and releases the agent on exit. |

### Subagent launchers and delegation

*108 projects. Tools that launch workers, delegate tasks, and exchange messages between agents.*

| Project | What it does |
|---|---|
| [**alvinunreal/oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim) | Assigns OpenCode specialist roles (fixers, librarians, explorers) to dedicated Herdr panes. |
| [**vekexasia/pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows) | Runs deterministic Pi workflows with on-disk checkpoints and Git worktree isolation in Herdr. |
| [**nidhi-singh02/agent-router**](https://github.com/nidhi-singh02/agent-router) | Routes tasks to Cursor, Claude Code, Codex or OpenCode and launches the selected agent in a Herdr TUI pane. |
| [**giuseppecrj/pi-herdr-agents**](https://github.com/giuseppecrj/pi-herdr-agents) | Runs asynchronous Pi subagents and approval-based review workflows entirely inside Herdr. |
| [**e2b-dev/herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox) | Mirrors a git worktree into an E2B sandbox, one box or a branch-per-agent fleet, with a TUI dashboard. |
| [**mupt-ai/context-drop**](https://github.com/mupt-ai/context-drop) | Provides a Herdr-backed meta-harness for orchestrating autonomous coding agents. |
| [**vercel-labs/herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin) | Runs Claude Code, Codex, or OpenCode inside isolated Vercel Sandbox microVMs while showing each session as a Herdr pane. It previews uploads, excludes secrets, and exports agent changes back as Git patches. |
| [**afogel/shepherdr**](https://github.com/afogel/shepherdr) | Dispatches Claude, Codex, and Cursor coding subagents into visible Herdr TUI panes and lets users resume completed sessions. |
| [**onsails/fork-in**](https://github.com/onsails/fork-in) | Forks an ongoing Pi or omp conversation into a new Herdr tab while preserving its conversation context. |
| [**transparent-pegasus/herdr-orchestration**](https://github.com/transparent-pegasus/herdr-orchestration) | Routes coding and review work to sibling Herdr TUI panes using configurable agent roles and composer-safe delegation. |

**[All 108 projects →](catalog/01-run-and-orchestrate.md#subagent-launchers-and-delegation)**

### Autonomous coding and pull-request loops

*16 projects. Long-running workflows that implement changes, open pull requests, review results, and react to CI.*

| Project | What it does |
|---|---|
| [**jpolec/herdr-plugin-odysseus**](https://github.com/jpolec/herdr-plugin-odysseus) | Runs governed multi-agent tasks in Herdr TUI panes with checks, retries, review, approvals, and draft pull requests. |
| [**sean1588/herdr-orchestrator**](https://github.com/sean1588/herdr-orchestrator) | A Go daemon that runs an issue-to-pull-request workflow from a validated YAML state graph. Herdr hosts implementer and reviewer agents, while the daemon checks GitHub's merge gate and can squash-merge, with dry-run enabled by default. |
| [**tomasvarga/herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr) | Starts an agent in Herdr to perform an initial quality and bug review of a pull request, then writes draft comments into tuicr. It supports Claude, Codex, Cursor, and Grok backends. |
| [**razajamil/herdr-factory**](https://github.com/razajamil/herdr-factory) | Claims work from Jira or Markdown task files, creates one Herdr worktree per item, and moves Claude Code through a configurable YAML pipeline. It can follow pull requests through CI, review, and merge under a shared concurrency limit. |
| [**night-porter/nightporter**](https://github.com/night-porter/nightporter) | Runs coding agents on review comments, failing CI, and merge conflicts and opens job worktrees in Herdr TUI. |
| [**zhuravel/magnum**](https://github.com/zhuravel/magnum) | Runs Claude Code, Codex and other agents in Herdr TUI panes to review pull requests, then uses a judge agent to verify findings and post a consolidated GitHub review. |
| [**robi42/factory**](https://github.com/robi42/factory) | Runs Claude Code planning and building alongside Codex reviews in Herdr TUI, with Beads tracking tasks. |
| [**firegnu/herdr-loop-lab**](https://github.com/firegnu/herdr-loop-lab) | Runs bounded coding loops in Herdr TUI with mechanical checks and cross-model review, parallel worktree fleets, and large-goal decomposition. |
| [**MovieHolic-Plex/herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish) | Starts an omo `/wish` workflow in a new Herdr TUI worktree to implement a request, commit changes, and open a pull request. |
| [**Tudor0404/dual-author**](https://github.com/Tudor0404/dual-author) | Processes GitHub issues through isolated worktrees, Claude implementation, draft pull requests, and paired Codex and Claude review rounds. A dashboard shows each issue's stage and elapsed time until the change is ready for automatic merging. |

**[All 16 projects →](catalog/01-run-and-orchestrate.md#autonomous-coding-and-pull-request-loops)**

### Task queues, backlogs, and event triggers

*86 projects. Queues and event-driven systems that turn stored work into agent jobs.*

| Project | What it does |
|---|---|
| [**smarzban/herdr-tsk**](https://github.com/smarzban/herdr-tsk) | Shares a terminal task board between you and your agents with a TUI for humans and a CLI for agents. |
| [**smarzban/tsk**](https://github.com/smarzban/tsk) | Opens a shared task board in Herdr TUI and lets agents manage work through a CLI. |
| [**nelsonPires5/herdr-board**](https://github.com/nelsonPires5/herdr-board) | A Kanban TUI and background service that turns cards into prompts for agents in visible Herdr panes. Moving a card can create an agent, run it in a dedicated tab, and advance the work through review gates. |
| [**deimantasnork/captains-deck**](https://github.com/deimantasnork/captains-deck) | Displays a read-only Firstmate flow kanban board inside Herdr TUI. |
| [**miiraheart/herdr-beads**](https://github.com/miiraheart/herdr-beads) | Displays Beads issues as a list, table, or Kanban board in a Herdr sidebar or floating pane. |
| [**DnzzL/herdr-automations**](https://github.com/DnzzL/herdr-automations) | Schedules recurring prompts and cron jobs that run agents in fresh Herdr worktrees. It supports task-specific MCP settings, collision protection, persistent run history, and a live monitoring board. |
| [**CodeForBreakfast/beady-eye**](https://github.com/CodeForBreakfast/beady-eye) | Shows, live, which agent works on which bead across your projects next to its Herdr pane, and tells agents and scripts when the beads they wait on change. |
| [**ivanarama/PromptPilot**](https://github.com/ivanarama/PromptPilot) | Queues and schedules prompts for coding CLIs through a web UI or Telegram bot, with Herdr-backed terminal sessions and retry on rate limits. |
| [**bon5co/bermuda**](https://github.com/bon5co/bermuda) | Schedules jobs as interactive agents in dedicated Herdr splits. It supports multi-step workflows, shared append-only discussion logs, and exclusive resource claims that remain valid across temporary sessions. |
| [**mrcndz/herdr-routines**](https://github.com/mrcndz/herdr-routines) | Runs scheduled routines on cron or interval timers by opening a tab in a chosen workspace and executing a command or starting an agent. |

**[All 86 projects →](catalog/01-run-and-orchestrate.md#task-queues-backlogs-and-event-triggers)**

### Linear, GitHub Issues, and issue-to-PR automation

*50 projects. Automated pipelines bridging issue trackers directly to Herdr agent workspaces and PRs.*

| Project | What it does |
|---|---|
| [**jmwind/issue-herd**](https://github.com/jmwind/issue-herd) | Watches Linear; when an issue matches a rule, run Claude Code in a herdr workspace and report the PR back to the issue. |
| [**ogulcancelik/herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start) | Turns a GitHub issue, pull request, or discussion into a prepared agent tab with one key. |
| [**a2u/herdr-jira**](https://github.com/a2u/herdr-jira) | Adds a Ratatui Jira client to browse, filter, and assign tickets directly to Herdr agent panes. |
| [**Matovidlo/herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker) | Tracks the GitHub pull request associated with each Claude Code session and offers GitHub actions. |
| [**freethinkel/shepherd**](https://github.com/freethinkel/shepherd) | Controls plane for coding agents on top of Herdr: tracker task in, pull request out. |
| [**JacquesvanWyk/herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear) | Opens an fzf-driven Linear panel in a Herdr TUI split or tab to search issues, browse projects, create issues, and change their status. |
| [**mrolafsson/herdr-linear**](https://github.com/mrolafsson/herdr-linear) | Browses Linear issues and starts agents in issue worktrees from the Herdr app or a Herdr TUI popup. |
| [**mrolafsson/herdr-github**](https://github.com/mrolafsson/herdr-github) | Reviews and manages GitHub pull requests and starts agents in PR worktrees from the Herdr app or a Herdr TUI popup. |
| [**talent-factory/herdr-linear**](https://github.com/talent-factory/herdr-linear) | Adds an interactive Linear issue browser to Herdr. Selecting an issue opens a dedicated agent pane and supplies the ticket context so implementation can begin immediately. |
| [**civitaspo/herdr-linear-agent**](https://github.com/civitaspo/herdr-linear-agent) | Runs a coordinator and repository coding agents in Herdr TUI panes for Linear issues delegated to its app user. |

**[All 50 projects →](catalog/01-run-and-orchestrate.md#linear-github-issues-and-issue-to-pr-automation)**

### General workflows and skill packs

*64 projects. Reusable skills, commands, and opinionated setups for common agent workflows.*

| Project | What it does |
|---|---|
| [**cloudmanic/herdr-plus**](https://github.com/cloudmanic/herdr-plus) | A plugin with two launchers: TOML project templates that build complete workspaces from a fuzzy picker, and Quick Actions for running reusable scripts in the current directory. Prebuilt binaries are available. |
| [**oborchers/proqi**](https://github.com/oborchers/proqi) | Provides a terminal-native prompt composer for power users running multiple coding agents. |
| [**DeevsDeevs/agent-system · skills/hc**](https://github.com/DeevsDeevs/agent-system/tree/main/skills/hc) | Teaches coding agents to run background work, communicate with peers and operate across machines using herdr-core. |
| [**madarco/agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin) | Connects AgentBox sandboxes to Herdr through a live overlay, a one-key VM launcher for the current project, and clickable `agentbox://` links. |
| [**sanirudh17/herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff) | Moves an active coding conversation to a new session using another installed agent CLI. The complete transcript and command history are passed to the replacement agent, avoiding a manual handoff summary. |
| [**arronKler/herdr-skills**](https://github.com/arronKler/herdr-skills) | Coordinates Herdr coding agents with dispatch, handoff, result collection, and swarm skills. |
| [**transparent-pegasus/herdrpowers**](https://github.com/transparent-pegasus/herdrpowers) | Coordinates planning, implementation, testing, and review across Herdr TUI agent panes using workflows adapted from Superpowers. |
| [**pbean/bmad-loop-adapter-herdr**](https://github.com/pbean/bmad-loop-adapter-herdr) | Provides a Herdr terminal-multiplexer backend for bmad-loop. |
| [**juanitourquiza/shipframe · herdr-plugin**](https://github.com/juanitourquiza/shipframe/tree/main/herdr-plugin) | Opens a ShipFrame workflow pane and checklist in Herdr TUI for Claude Code, Codex, or OpenCode. |
| [**motionharvest/herdr**](https://github.com/motionharvest/herdr) | A terminal-based agent multiplexer project. The source catalog provides no additional detail beyond its Herdr name and purpose. |

**[All 64 projects →](catalog/01-run-and-orchestrate.md#general-workflows-and-skill-packs)**

---

## 2. Herdr app layouts, mods, and themes

*782 projects. Layouts, mods, and themes for customizing the Herdr desktop app.* The top 10 of each subcategory by stars are below; the full list is in [catalog/02-herdr-app.md](catalog/02-herdr-app.md).

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community extensions.

### Herdr app agent boards and mission-control layouts

*35 projects. Whole-window layouts that put agents on kanban boards, attention inboxes, fleet views and task-driven mission-control screens.*

| Project | What it does |
|---|---|
| [**eliasstravik/shepherdr**](https://github.com/eliasstravik/shepherdr) | Organizes coding agents in a Herdr app layout with per-space assistants and task cards, running tasks in separate worktrees. |
| [**JinJieBeWater/herdr-t3**](https://github.com/JinJieBeWater/herdr-t3) | Organizes Herdr app agents in an inbox that groups work by attention state and shows agents across machines. |
| [**quaresc/cockpit**](https://github.com/quaresc/cockpit) | Shows Herdr agents, their work, and items needing attention in an app layout or TUI plugin. |
| [**simoncrypta/bercail**](https://github.com/simoncrypta/bercail) | Adds the Bercail layout to the Herdr app for supervising agents across Git worktrees, with a desk pane for each space. |
| [**jlopezlira/herdr-kanso**](https://github.com/jlopezlira/herdr-kanso) | Adds the Kanso horizontal-agent layout plus Markdown panel and editor-launcher mods to the Herdr app. |
| [**adamentwistle/orchi-build**](https://github.com/adamentwistle/orchi-build) | Adds an Orchi layout for managing Claude Code agents, tickets, agent status, and orchestration in the Herdr app. |
| [**jkuepker/herdr-layouts**](https://github.com/jkuepker/herdr-layouts) | Collects Board, LCARS, and Slate layouts for organizing agents and workspaces in the Herdr app. |
| [**sgomez/herdr-triage**](https://github.com/sgomez/herdr-triage) | Adds a Herdr app layout with an attention inbox, agent replies, worktrees, Git history, pull requests and issues. |
| [**CiprianSpiridon/herdr-mission-control**](https://github.com/CiprianSpiridon/herdr-mission-control) | Adds Mission Control and Classic Herdr app layouts with mods for agent monitoring, Jira, GitHub, GitLab, sessions, tabs and worktree launches. |
| [**Lakris2407/herdr-mods**](https://github.com/Lakris2407/herdr-mods) | Adds the Fleet Herdr app layout and mods for agent lists, quotas, build runners, delivery stats and controls. |

**[All 35 projects →](catalog/02-herdr-app.md#herdr-app-agent-boards-and-mission-control-layouts)**

### Herdr app sidebar and space-organization layouts

*51 projects. Layouts that rework the Spaces, Agents and tabs sidebar with trees, folders, machine grouping, worktrees and usage gauges.*

| Project | What it does |
|---|---|
| [**jankeesvw/herdr-space-folders**](https://github.com/jankeesvw/herdr-space-folders) | Groups Herdr app spaces into colored, collapsible folders using drag-and-drop or project folder rules. |
| [**shellscape/herdr-whitby**](https://github.com/shellscape/herdr-whitby) | Organizes Herdr app spaces into a light project sidebar with nested agents, status dots, and an attention bell. |
| [**herunan/herdr-over9k**](https://github.com/herunan/herdr-over9k) | Collects the Over9k layout and launcher, sidebar, switcher, timeline, to-do, and usage mods for the Herdr app. |
| [**VladTemp27/herdr-orca**](https://github.com/VladTemp27/herdr-orca) | Adds a Herdr app layout with nested worktrees and agents, GitHub issues and pull requests, usage limits and file panels. |
| [**emoss08/herdr-wsl**](https://github.com/emoss08/herdr-wsl) | Connects a Windows Herdr app layout to a WSL 2 machine so spaces, terminals and repository panels use Linux paths. |
| [**dissimulate/bettr**](https://github.com/dissimulate/bettr) | Adds a Herdr app layout with agent and usage sidebars, system statistics, terminals, and file and activity panels. |
| [**ozcberkay/herdr-coban**](https://github.com/ozcberkay/herdr-coban) | Adds a Herdr app layout and mods for Claude Code usage and session status, per-tab notes and Mac system metrics. |
| [**chelebyy/herdr-agent-workspace**](https://github.com/chelebyy/herdr-agent-workspace) | Adds a Herdr app layout with agent and resource sidebars, quota gauges, task launchers, and Turkish and English UI options. |
| [**VedangP57/herdr-tui-layout**](https://github.com/VedangP57/herdr-tui-layout) | Recreates Herdr TUI navigation in the Herdr app with machine-grouped spaces, agent status, tabs, and prefix keys. |
| [**abdh01h/herdr-agentee-theme**](https://github.com/abdh01h/herdr-agentee-theme) | Reshapes the Herdr app into a compact Carbon-style workspace with a spaces and agents rail, an icon-tabbed Files, Agents and System panel, diff and blame, and git actions. Includes install scripts for Windows and macOS or Linux. |

**[All 51 projects →](catalog/02-herdr-app.md#herdr-app-sidebar-and-space-organization-layouts)**

### Herdr app IDE, editor and Git-panel layouts

*33 projects. Layouts that make the Herdr app feel like VS Code, Zed, IntelliJ or Neovim, or that dock Git, file, review and pull-request panels beside terminals.*

| Project | What it does |
|---|---|
| [**munza/herdr-mods**](https://github.com/munza/herdr-mods) | Adds the Estro layout and a collection of Herdr app mods for Git, files, tabs, settings, Linear, pull requests, staged agent runs and Mac automation. |
| [**carstenlucke/herdr-roundup**](https://github.com/carstenlucke/herdr-roundup) | Adds the Roundup layout for the Herdr app with custom file browsing, preview, themes, and keyboard shortcuts. |
| [**h3y6e/dotfiles · dot_config/herdr-app**](https://github.com/h3y6e/dotfiles/tree/main/dot_config/herdr-app) | Adds the Zebra layout for the Herdr app: a flat, editor-style window with spaces and tabs as projects and threads in one sidebar, Files and Changes panels beside the panes, and a thin status bar. Includes the supporting mods and a RECIPE.md brief an agent can rebuild it from. |
| [**dantech99/herdr-zed-layout**](https://github.com/dantech99/herdr-zed-layout) | Adds a Zed-inspired Herdr app layout with tabs, file and changes panels, agent quotas, and Tokyo Night colors. |
| [**tackcrypto1031/tackbear-herdr-mod**](https://github.com/tackcrypto1031/tackbear-herdr-mod) | Adds a Herdr app layout with a chat-style input box, file and image attachments, and model and reasoning controls. |
| [**mirkobozzetto/herdr-app-config**](https://github.com/mirkobozzetto/herdr-app-config) | Adds a keyboard-first Herdr app layout with shortcut menus, agent status, file panels, and code review tools. |
| [**jotyy/herdr-ovis-studio**](https://github.com/jotyy/herdr-ovis-studio) | Adds an Ovis Studio-inspired Herdr app layout with an agent sidebar, tab bar, status line, and command picker. |
| [**bborrero14/herdr-file-preview**](https://github.com/bborrero14/herdr-file-preview) | Adds a Herdr app layout with a file tree of the focused terminal folder beside a rendered preview of Markdown with Mermaid diagrams and highlighted source files. Works in local and remote spaces. |
| [**alarboulletmarin/herdr-github**](https://github.com/alarboulletmarin/herdr-github) | Extends the Herdr app main layout with a GitHub panel for issues, pull requests, CI runs, milestones and projects, and a Zed-style Changes panel. Each item can be copied or started as an agent brief. |
| [**dougcunha/herdr-mods**](https://github.com/dougcunha/herdr-mods) | Collects Herdr app mods, layouts and themes that dispatch GitHub Actions, follow jobs and show pending repository work, plus agent cards. |

**[All 33 projects →](catalog/02-herdr-app.md#herdr-app-ide-editor-and-git-panel-layouts)**

### Herdr app palette, glass and desktop-OS themed layouts

*55 projects. Windows defined mainly by a color palette, glass or minimal look, or a faithful classic desktop and app skin such as NeXTSTEP, Windows 7 or Catppuccin.*

| Project | What it does |
|---|---|
| [**shafiqimtiaz/herdr-omarchy**](https://github.com/shafiqimtiaz/herdr-omarchy) | Adds an Omarchy-inspired Herdr app layout with tiled terminals, agent status, quota, Git panels, themes and wallpapers. |
| [**CodeyPacker/herdr-mods**](https://github.com/CodeyPacker/herdr-mods) | Adds the Islands Herdr app layout and mods for workspace jumping, process control and agent-guided code tours. |
| [**MarcozVD/herdr-layout-catppuccin**](https://github.com/MarcozVD/herdr-layout-catppuccin) | Applies a Catppuccin layout to the Herdr app with Mocha and Latte colors that follow the system appearance. |
| [**othavi0/noctua-layout**](https://github.com/othavi0/noctua-layout) | Adds a graphite Herdr app layout with colored space cards, agent status indicators and Git information. |
| [**kyle-avrett/herdr-square-dracula**](https://github.com/kyle-avrett/herdr-square-dracula) | Applies a gapless Dracula layout to the Herdr app with compact tabs, a sidebar and file and changes panels. |
| [**Mayloparra24/gentle-herdr**](https://github.com/Mayloparra24/gentle-herdr) | Adds a Gentle Shell-themed Herdr app layout that syncs its colors with the selected Gentle Shell theme. |
| [**0OZ/coss-design**](https://github.com/0OZ/coss-design) | Dresses the Herdr app in a calm neutral dark layout inspired by shadcn dashboard-01, with one rounded card for the work area and a dashboard-style sidebar. |
| [**Calonca/herdr-orbit-look**](https://github.com/Calonca/herdr-orbit-look) | Gives the Herdr app a dark glassy look over a generated space picture, with a color and symbol for each space. |
| [**attractify-logan/herdr-snowleopard**](https://github.com/attractify-logan/herdr-snowleopard) | Restyles the Herdr app as Mac OS X 10.6 with a menu bar, Aqua windows, a source list and a Dock, where menus and Dock icons run real Herdr commands. Marked beta. |
| [**lamngockhuong/termote-herdr-layouts**](https://github.com/lamngockhuong/termote-herdr-layouts) | Adds three Herdr app layouts in the Termote neutral, terminal and native styles. Pane headers can open the pane in Termote, copy its link or show a QR code for a phone. |

**[All 55 projects →](catalog/02-herdr-app.md#herdr-app-palette-glass-and-desktop-os-themed-layouts)**

### Herdr app pixel-art, game, anime and cyberpunk layouts

*71 projects. Playful windows that turn agents into pixel-art coworkers, game characters, anime units or neon cyberpunk scenes.*

| Project | What it does |
|---|---|
| [**franky5440-afk/herdr-traveler**](https://github.com/franky5440-afk/herdr-traveler) | Turns the Herdr app into a pixel RPG with agent portraits, status bars, and machine buildings. |
| [**DustyPolk/herdr-office**](https://github.com/DustyPolk/herdr-office) | Shows coding agents as animated coworkers above Herdr app terminals and jumps to their sessions when clicked. |
| [**kevinpardo/world-of-codecraft**](https://github.com/kevinpardo/world-of-codecraft) | Frames the Herdr app terminal in a high-fantasy MMO style with a pixel-art village that reflects agent activity, with Claude Code and OpenCode activity hooks. |
| [**vib-z/herdr-layouts**](https://github.com/vib-z/herdr-layouts) | Adds seven Herdr app layouts, including Control Panel, Falling Code, Fleet Tab, Night City, Queue, The Crew Board and The Noir Office. |
| [**isaacin42/herdr-layouts**](https://github.com/isaacin42/herdr-layouts) | Adds Herdr app layouts including Darkroom, Mixtape, Neon, Orienteering, Orrery, The Desk and The Pass for viewing and steering agents. |
| [**TwoD97/neon-borough**](https://github.com/TwoD97/neon-borough) | Adds a cyberpunk Herdr app layout with agent activity displays and panels for pull requests, file transfers, and secrets. |
| [**Jiqize/herdr-maid-adv**](https://github.com/Jiqize/herdr-maid-adv) | Turns the Herdr app into a visual-novel workspace where agent characters queue to speak when they finish or need input. |
| [**adamentwistle/herdr-departures**](https://github.com/adamentwistle/herdr-departures) | Turns the top of the Herdr app window into an airport split-flap board where each coding agent is a flight and agents that need you show as delayed. |
| [**Dylan0203/herdr-layout-eva**](https://github.com/Dylan0203/herdr-layout-eva) | Gives the Herdr app a late-90s command-center HUD look with cut-corner plates, live agent counts and seven-segment readouts of the host Mac CPU, memory, network and power. |
| [**evanhickman/herdr-layouts**](https://github.com/evanhickman/herdr-layouts) | Turns the Herdr app into a Roland TR-808 drum machine on the gruvbox palette, with tabs as colored step keys and agent status on LEDs. |

**[All 71 projects →](catalog/02-herdr-app.md#herdr-app-pixel-art-game-anime-and-cyberpunk-layouts)**

### Herdr app sidebars, tabs, and visual mods

*135 projects. Spaces and agents sidebars, tab naming and groups, pane headers, agent trees, chat views, and playful extras such as pixel pets, games, music players, and voice dictation.*

| Project | What it does |
|---|---|
| [**sodiumsun/agenttrail · herdr/agenttrail**](https://github.com/sodiumsun/agenttrail/tree/main/herdr/agenttrail) | Shows a read-only project map beside Herdr app terminals, using PLAN.md or inferred Git branches and worktrees. |
| [**mathieucroset/herdr-pokemon-agents**](https://github.com/mathieucroset/herdr-pokemon-agents) | Shows agents as animated Pokémon in the Herdr app and lets users jump to an agent by clicking its sprite. |
| [**chappse6/herdr-blueprint-app**](https://github.com/chappse6/herdr-blueprint-app) | Displays agent-written Mermaid flowcharts beside Herdr app sessions and sends clicked diagram changes back to the agent. |
| [**mukiwu/herdr-crew-rpg**](https://github.com/mukiwu/herdr-crew-rpg) | Displays dispatched agents as pixel-art characters in a Herdr app sidebar and battle scene with status and quota information. |
| [**jonathan-fielding/herdr-project-coordinator**](https://github.com/jonathan-fielding/herdr-project-coordinator) | Adds a Projects sidebar to the Herdr app where a Claude Code coordinator delegates tasks to isolated workers and tracks their progress. |
| [**ChmaraX/herdr-chat**](https://github.com/ChmaraX/herdr-chat) | Adds a native chat interface in Herdr app tabs for Pi, Claude Code and Codex, with streamed messages and tool approval cards. |
| [**MarcozVD/herdr-agent-flow**](https://github.com/MarcozVD/herdr-agent-flow) | Maps agents, subagents and their messages in the current Herdr app space as a live diagram or timeline. |
| [**thuanlm215/herdr-float-space**](https://github.com/thuanlm215/herdr-float-space) | Adds a floating scratch window with terminal tabs and shared notes to the Herdr app. |
| [**funny-it-worked-last-time-gsv/herdr-sit-and-watch**](https://github.com/funny-it-worked-last-time-gsv/herdr-sit-and-watch) | Adds a Herdr app sidebar that depicts agents as robots at their desks. |
| [**naruse/herdr-chat**](https://github.com/naruse/herdr-chat) | Adds a chat interface for Claude Code and Codex agents in the Herdr app, with live replies and terminal access. |

**[All 135 projects →](catalog/02-herdr-app.md#herdr-app-sidebars-tabs-and-visual-mods)**

### Herdr app keys, navigation, and attention alerts

*103 projects. Keyboard shortcuts, pickers and switchers, the + menu agent list, session resume, mod managers, and alerts that tell you when an agent needs you.*

| Project | What it does |
|---|---|
| [**atuinsh/herdr-atuin-threads**](https://github.com/atuinsh/herdr-atuin-threads) | Lists Atuin-captured coding-agent threads in the Herdr app and resumes a selected session in a new tab. |
| [**mrolafsson/herdr-recap**](https://github.com/mrolafsson/herdr-recap) | Lists agent recaps and blocked questions across machines in the Herdr app and Herdr TUI, with replies from the list. |
| [**ergunozyurt/herdr-super-agent**](https://github.com/ergunozyurt/herdr-super-agent) | Organizes a lead agent’s human decision requests into threaded inbox items in the Herdr app. |
| [**sachin-philip/herdr-agent-ask**](https://github.com/sachin-philip/herdr-agent-ask) | Collects every question your agents ask in a space, from permission dialogs to plain-text questions, into one side panel of cards in the Herdr app. |
| [**JinJieBeWater/herdr-t3-inbox**](https://github.com/JinJieBeWater/herdr-t3-inbox) | Adds an attention inbox to the Herdr app sidebar where users can settle finished agents and see them return when work resumes. |
| [**dmazlum/herdr-revive**](https://github.com/dmazlum/herdr-revive) | Restores supported coding-agent sessions after a Herdr app restart and forks conversations into adjacent panes. |
| [**sachin-philip/herdr-marks-as-unread**](https://github.com/sachin-philip/herdr-marks-as-unread) | Marks agents as unread in the Herdr TUI or Herdr app sidebar and clears the mark when users return. |
| [**benjaminsicard/herdr-mods**](https://github.com/benjaminsicard/herdr-mods) | Adds Herdr app mods for desktop notifications and automatic tab and space names. |
| [**CiprianSpiridon/herdr-migration**](https://github.com/CiprianSpiridon/herdr-migration) | Imports Herdr TUI workspaces, tabs, folders, and terminal splits into the Herdr app with backup and verification. |
| [**jankeesvw/herdr-focus-to-hover**](https://github.com/jankeesvw/herdr-focus-to-hover) | Focuses the Herdr app pane under the mouse pointer so users can type without clicking. |

**[All 103 projects →](catalog/02-herdr-app.md#herdr-app-keys-navigation-and-attention-alerts)**

### Herdr app usage, quota, and system status displays

*50 projects. Status bars and panels for subscription quota, token cost, context size, and machine resource use.*

| Project | What it does |
|---|---|
| [**GaganSD/coding-agent-toolkit · herdr-insights**](https://github.com/GaganSD/coding-agent-toolkit/tree/main/herdr-insights) | Shows local token usage and model activity for Pi, Codex, Claude Code, OpenCode and Antigravity in a Herdr app dashboard. |
| [**nozikov/herdr-usage-limits**](https://github.com/nozikov/herdr-usage-limits) | Shows Claude Code and Codex subscription limits and session context in the Herdr app status bar. |
| [**mrolafsson/herdr-vitals**](https://github.com/mrolafsson/herdr-vitals) | Shows machine CPU, memory, disk and network activity in a Herdr app window or Herdr TUI popup, with resource alerts. |
| [**dev-gvs/herdr-claude-usage**](https://github.com/dev-gvs/herdr-claude-usage) | Shows Claude plan usage and reset times in the Herdr app status bar. |
| [**adamentwistle/limit-runway · herdr**](https://github.com/adamentwistle/limit-runway/tree/main/herdr) | Adds a Herdr app panel for monitoring Claude Code and Codex plan limits and pausing or resuming agents through the Runway CLI. |
| [**riyhs/herdr-bottom-bar-stats**](https://github.com/riyhs/herdr-bottom-bar-stats) | Adds a bottom status bar showing the active machine name with CPU, memory, disk and ping, following the active space so remote spaces show their own numbers. |
| [**0xRowdy/herdr-cliproxy**](https://github.com/0xRowdy/herdr-cliproxy) | Adds two floating windows for a CLIProxyAPI server: one with health, throughput and live provider quota, and a lighter one with account status and everyday account actions. |
| [**adamentwistle/herdr-wrapped**](https://github.com/adamentwistle/herdr-wrapped) | Opens an overlay in the Herdr app with a shareable card of your Claude Code stats. Shows tokens, cost, busiest day and peak parallel agents, read from local transcripts. |
| [**werlang/herdr-usage-status**](https://github.com/werlang/herdr-usage-status) | Adds one usage gauge to the Herdr app bottom status bar that opens a panel with every available subscription limit. Covers Claude, Antigravity, and other providers, and hides those without data. |
| [**e-kotov/herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit) | Shows prompt-cache metrics and expiration alerts in Herdr TUI, with an experimental display-only Herdr app mod. |

**[All 50 projects →](catalog/02-herdr-app.md#herdr-app-usage-quota-and-system-status-displays)**

### Herdr app Git, code review, and worktree panels

*69 projects. Git graphs, diff and branch review, pull-request and merge-request lists, and worktree helpers inside the Herdr app.*

| Project | What it does |
|---|---|
| [**rabeeh-ta/herdr-git-graph**](https://github.com/rabeeh-ta/herdr-git-graph) | Shows a Git commit graph in the Herdr app and offers branch, merge, rebase, and other repository actions. |
| [**iampedii/herdr-redline**](https://github.com/iampedii/herdr-redline) | Reviews GitHub pull requests and GitLab merge requests in the Herdr app with worktree checkout, diffs, and inline comments. |
| [**vytasgavelis/herdr-reviewer**](https://github.com/vytasgavelis/herdr-reviewer) | Adds syntax-colored diffs and inline review comments to the Herdr app Changes panel and sends comments to an agent. |
| [**jjangsky/herdr-pr-flow**](https://github.com/jjangsky/herdr-pr-flow) | Shows agent pull requests in a Herdr app panel with CI, review and post-merge workflow status, plus optional merge and diff comments. |
| [**jakub-tucek/herdr-annotator**](https://github.com/jakub-tucek/herdr-annotator) | Adds code review to the Herdr app with branch and working-tree diffs, inline comments and GitHub pull-request threads for local or SSH worktrees. |
| [**dmazlum/herdr-walkthrough**](https://github.com/dmazlum/herdr-walkthrough) | Uses Claude Code to turn a repository diff into an ordered, explained walkthrough in the Herdr app. |
| [**LaiqianDS/herdr-mods**](https://github.com/LaiqianDS/herdr-mods) | Adds a Herdr app Git panel for diffs, staging, commits and branch switching, alongside a file-icons mod. |
| [**aBER0724/herdr-git-changes**](https://github.com/aBER0724/herdr-git-changes) | Adds a Herdr app Git panel for staging, commits, stashes, history, and diff inspection. |
| [**ashrodan/ship-it**](https://github.com/ashrodan/ship-it) | Adds pull request status, checks, review threads, and change inspection to the Herdr app. |
| [**lw396/herdr-plugin-github**](https://github.com/lw396/herdr-plugin-github) | Browses, reads and reviews the Issues and Pull Requests of the current repository in a side panel, modeled on the VS Code GitHub Pull Requests extension. Uses the gh CLI on the machine that hosts the folder. |

**[All 69 projects →](catalog/02-herdr-app.md#herdr-app-git-code-review-and-worktree-panels)**

### Herdr app file, Markdown, and notes panels

*56 projects. Files panels, file previews, Markdown readers, editors, and note-taking panes beside your terminals.*

| Project | What it does |
|---|---|
| [**CacaoRick/herdr-open-vscode**](https://github.com/CacaoRick/herdr-open-vscode) | Opens the focused Herdr app terminal folder in VS Code locally or through Remote SSH, including SSH-connected WSL. |
| [**linziyanleo/herdr-mods**](https://github.com/linziyanleo/herdr-mods) | Adds Herdr app mods for multi-root file browsing, file previews and editing, and mod and layout management. |
| [**Abrahamism/herdr-browser**](https://github.com/Abrahamism/herdr-browser) | Controls a dedicated Chromium browser through CDP and adds a Herdr app panel for listing and switching its tabs. |
| [**Srv-02/herdr-filerpro**](https://github.com/Srv-02/herdr-filerpro) | Adds a Herdr app file panel for browsing and transferring files on local and SSH machines. |
| [**anderssonq/herdsidian**](https://github.com/anderssonq/herdsidian) | Adds an Obsidian vault sidebar to the Herdr app for browsing and editing notes beside agents. |
| [**ryanthedev/herdr-md**](https://github.com/ryanthedev/herdr-md) | Renders a Markdown file natively in a Herdr app pane with theme colors, real heading sizes, tables, task lists, callouts and images. |
| [**amster93/herdr-file-icons**](https://github.com/amster93/herdr-file-icons) | Replaces the Files panel with one that shows VS Code Material Icon Theme icons for files and folders. |
| [**vladimiryakimenko/herdr-files-transfer**](https://github.com/vladimiryakimenko/herdr-files-transfer) | Replaces the Files panel with one that downloads, uploads, renames, moves to Trash or deletes files from a right-click menu, locally and on remote machines over SSH, with VS Code file icons. |
| [**napalmpapalam/herdr-find-in-files**](https://github.com/napalmpapalam/herdr-find-in-files) | Searches the focused terminal repo with ripgrep in a JetBrains-style dialog, showing hits as you type with a preview of the selected lines. |
| [**vedovato/terminal-browser-qa-walk**](https://github.com/vedovato/terminal-browser-qa-walk) | Opens a terminal-browser window beside your terminals from a popup where you type a URL and choose where it opens. |

**[All 56 projects →](catalog/02-herdr-app.md#herdr-app-file-markdown-and-notes-panels)**

### Herdr app task boards, developer services, and mod bundles

*116 projects. Issue and task boards, cloud, database, and deployment panels, chat, mail, and remote-machine panels, and multi-mod bundles that add several features at once.*

| Project | What it does |
|---|---|
| [**runkids/skillshare · herdr/skillshare**](https://github.com/runkids/skillshare/tree/main/herdr/skillshare) | Adds a Herdr app layout with a skillshare panel for viewing, auditing and syncing skills, agents, MCP servers, plugins and hooks. |
| [**fatwang2/Pulse · herdr**](https://github.com/fatwang2/Pulse/tree/main/herdr) | Adds a stock and crypto watchlist mod and a matching Herdr app layout with a docked price panel. |
| [**wobsoriano/herdr-sim**](https://github.com/wobsoriano/herdr-sim) | Opens an interactive iOS simulator or Android emulator beside code and terminals in the Herdr app. |
| [**jankeesvw/herdr-issues**](https://github.com/jankeesvw/herdr-issues) | Adds a GitHub issues panel to the Herdr app for reading, commenting on, assigning, and closing issues. |
| [**SaifHarding/herdr-cloudflare**](https://github.com/SaifHarding/herdr-cloudflare) | Shows Cloudflare Pages and Workers deployment status in the Herdr app header and reports failed deployments. |
| [**runkids/figlens · herdr**](https://github.com/runkids/figlens/tree/main/herdr) | Adds a figlens layout and panel for viewing local Figma designs and handing screens to agents in the Herdr app. |
| [**greenflagged/herdr-forge**](https://github.com/greenflagged/herdr-forge) | Opens GitHub or GitLab project panels in the Herdr app and hands issues or merge requests to agents. |
| [**greenflagged/herdr-greenflagged**](https://github.com/greenflagged/herdr-greenflagged) | Displays project dependency trees in the Herdr app and optionally marks npm dependencies with Greenflagged review verdicts. |
| [**cybertron288/herdr-mods**](https://github.com/cybertron288/herdr-mods) | Adds Herdr app mods for file browsing, GitHub Actions, JavaScript scripts, session status, Slack and YouTube Music. |
| [**ernestjsf/herdr-devices**](https://github.com/ernestjsf/herdr-devices) | Adds a Herdr app side panel for iOS and Android devices and simulators, with device actions and Maestro flow runs. |

**[All 116 projects →](catalog/02-herdr-app.md#herdr-app-task-boards-developer-services-and-mod-bundles)**

### Herdr app themes

*8 projects. Color themes and palettes that recolor the Herdr app window, including theme generators and editors.*

| Project | What it does |
|---|---|
| [**Codesmith28/gruvbox-herdr-app**](https://github.com/Codesmith28/gruvbox-herdr-app) | Adds six Gruvbox themes and a contrast-switching mod to the Herdr app. |
| [**alvaroroco/herdr-omarchy-theme**](https://github.com/alvaroroco/herdr-omarchy-theme) | Adds an omarchy theme to Herdr app Settings that is rewritten from the active Omarchy palette on every theme change, plus a small status pill. |
| [**pedroparra/herdr-monokai**](https://github.com/pedroparra/herdr-monokai) | Recolors the Herdr desktop app's main window in the classic Monokai palette, with agent states in Monokai yellow, pink and cyan and an orange ring on the focused pane. Adds Monokai and Monokai Dimmed themes that work in any layout, with no mods or code. |
| [**dtellz/dtellz-dark**](https://github.com/dtellz/dtellz-dark) | Adds a near-black Herdr app theme with white text and vivid syntax colors. Includes a copy of the standard layout that uses it. |
| [**douglasjarquin/sf2-themes**](https://github.com/douglasjarquin/sf2-themes) | Installs Street Fighter II color themes for the Herdr app and Herdr TUI as well as several other developer tools. |
| [**jdlewin/herdr-omarchy-theme**](https://github.com/jdlewin/herdr-omarchy-theme) | Generates a Herdr app theme from the active Omarchy theme and refreshes it whenever you run omarchy theme set. Installs a sync hook and a layout that applies the theme. |
| [**agentic-tool-labs/herdr-theme-studio**](https://github.com/agentic-tool-labs/herdr-theme-studio) | Edits the Herdr app's look in one window: pick or import a theme, adjust its colors, choose terminal and panel fonts, and style the agents list, with a live preview before saving. |
| [**suree33/herdr-app**](https://github.com/suree33/herdr-app) | Adds Catppuccin themes for the Herdr app in Latte, Frappe, Macchiato, and Mocha, with previews. |

---

## 3. Connect through MCP and the socket API

*338 projects. Protocols, clients, bots, and event bridges that link Herdr to external tools, editors, and messaging apps.* The top 10 of each subcategory by stars are below; the full list is in [catalog/03-mcp-and-socket-api.md](catalog/03-mcp-and-socket-api.md).

### MCP servers

*21 projects. Servers that expose Herdr operations as MCP tools for compatible AI clients.*

| Project | What it does |
|---|---|
| [**runchr-works/herdr-mesh**](https://github.com/runchr-works/herdr-mesh) | Connects multiple Herdr instances into a coordinated mesh over Model Context Protocol. |
| [**rmngl/herdr-mesh**](https://github.com/rmngl/herdr-mesh) | Exposes Herdr pane management, agent messaging, and contextual handoffs through an MCP server. |
| [**whshang/herdr-mcp**](https://github.com/whshang/herdr-mcp) | Adds a stable MCP and OAuth bridge for remote web planners to inspect and control local Herdr workspaces. |
| [**ryanthedev/herderp**](https://github.com/ryanthedev/herderp) | Adds Claude Code MCP tools for managing agents and terminals across Herdr TUI and herdr-core, including remote hosts and session history. |
| [**aquaherd/goose-herdr**](https://github.com/aquaherd/goose-herdr) | Connects Goose to Herdr TUI through an MCP extension and reports Goose lifecycle state to the sidebar. |
| [**eugeneb50/herdr-mcp**](https://github.com/eugeneb50/herdr-mcp) | Exposes Herdr workspace and pane controls as tools to any Model Context Protocol (MCP) client. |
| [**54rt1n/herdr-simple-mcp**](https://github.com/54rt1n/herdr-simple-mcp) | Provides a lightweight Model Context Protocol server for driving Herdr from Claude Desktop and Cursor. |
| [**Orange-County-AI/herdr-mcp**](https://github.com/Orange-County-AI/herdr-mcp) | Exposes Herdr's socket API as a local or remote MCP server. |
| [**thomasfossum/herdr-mcp**](https://github.com/thomasfossum/herdr-mcp) | Lets MCP clients control a running Herdr session: see agent status, open tabs and panes, start agents, send them work and run worktree-isolated jobs. Runs over stdio or Streamable HTTP in standard-library Python with Docker and client examples. |
| [**nytafar/herdr-spawn**](https://github.com/nytafar/herdr-spawn) | Exposes an MCP tool that starts coding agents on your machines from a chat prompt, with a Claude Code Remote Control link when available. |

**[All 21 projects →](catalog/03-mcp-and-socket-api.md#mcp-servers)**

### Socket API and herdr-core clients and SDKs

*41 projects. Clients, libraries, and command-line tools for Herdr TUI and herdr-core APIs.*

| Project | What it does |
|---|---|
| [**backpine/remote-agent-workspace**](https://github.com/backpine/remote-agent-workspace) | Provides an always-on remote agent environment: edit on macOS, run Herdr work on Linux, synchronize files with Syncthing, and expose services through Cloudflare Tunnel and Caddy. |
| [**dmmulroy/herdr-ts-sdk**](https://github.com/dmmulroy/herdr-ts-sdk) | Provides an Effect-native TypeScript SDK for Herdr's local protocol-21 socket API. |
| [**0xGosu/herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot) | Prompts a running coding CLI through the Herdr API. A training mode observes user actions, safety checks block dangerous operations, and an optional autonomous mode can continue prompting after sufficient setup. |
| [**mitkox/dsh-herdr**](https://github.com/mitkox/dsh-herdr) | Reports DeepSeek Harness agent state to herdr-core via OSC 7501 and displays sessions in a Herdr app panel. |
| [**Mic92/herdr-eternal**](https://github.com/Mic92/herdr-eternal) | A roaming-friendly transport for `herdr --remote` using QUIC with a WebSocket fallback, exact byte-stream resumption, and OIDC authentication. |
| [**ryonakae/shepherd**](https://github.com/ryonakae/shepherd) | A worker-observability service and set of runtime bridges for coding agents managed by Herdr. |
| [**TheMetalStorm/herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin) | Integrates Freebuff agents with Herdr by reading PTY output and local session files, then reporting idle, working, and blocked states through the socket API. |
| [**gejiliang/herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw) | Treats OpenClaw TUI sessions as Herdr agents, with live state, model information, and token use in the sidebar. A background watcher parses OpenClaw status lines and reports them through the socket API. |
| [**54rt1n/herdr-python-client**](https://github.com/54rt1n/herdr-python-client) | Provides typed Python bindings and socket utilities for automating Herdr programmatically. |
| [**usrivastava92/herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup) | Prevents macOS or Linux from sleeping while Herdr agents are working. It enables an operating-system sleep inhibitor when activity begins and releases it when every agent is idle. |

**[All 41 projects →](catalog/03-mcp-and-socket-api.md#socket-api-and-herdr-core-clients-and-sdks)**

### Chat alerts: Telegram, Discord, and Slack

*33 projects. Bot and channel alerts that ping you when agents finish or need input.*

| Project | What it does |
|---|---|
| [**alexei-led/ccgram**](https://github.com/alexei-led/ccgram) | Maps forum topics to terminal windows running Claude Code, Codex, Gemini, Pi, or a shell. It relays output and input through Herdr or tmux so sessions remain usable from a phone. |
| [**permgps/herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents) | Creates a Telegram forum topic for each Herdr agent so users can receive status updates and reply to prompts. |
| [**dcolinmorgan/herdr-push**](https://github.com/dcolinmorgan/herdr-push) | Forwards agent status changes to the herdr-remote relay using only curl and system Python or jq. A single relay setting enables mobile, menu-bar, or Telegram monitoring, and a test action checks the connection. |
| [**natori-hrj/herdr-hail**](https://github.com/natori-hrj/herdr-hail) | Connects Herdr to Slack and Discord through a two-way webhook bridge. Blocked-agent alerts can be answered through replies or action buttons without opening a network tunnel. |
| [**gaijinjoe/herdres**](https://github.com/gaijinjoe/herdres) | Maps every live Herdr pane to a Telegram forum topic. Agent activity appears in the topic, and bot commands can send input back to the matching pane from any device. |
| [**mvallebr/herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin) | A Telegram bot companion that maps Herdr agents to forum topics and provides remote control without placing an LLM between the user and the pane. |
| [**etinpres/herdr-telegram-remote**](https://github.com/etinpres/herdr-telegram-remote) | Controls Codex and Claude Code panes in Herdr from Telegram. |
| [**TerrifiedBug/omp-telegram**](https://github.com/TerrifiedBug/omp-telegram) | Connects Oh My Pi sessions to Telegram and uses Herdr to spawn and manage sessions remotely. |
| [**cokekitten/herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge) | Sends Telegram notifications when an agent finishes or waits for input. Replies, including files, are delivered to the correct pane without requiring a public server or port tunnel. |
| [**hkdom/herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate) | Sends blocked Herdr agent approvals to Telegram and supports risk-tiered automatic approval policies. |

**[All 33 projects →](catalog/03-mcp-and-socket-api.md#chat-alerts-telegram-discord-and-slack)**

### Desktop, mobile, and webhook notifications

*73 projects. Desktop notifications, mobile push alerts, and webhook triggers for agent events.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | What it does |
|---|---|
| [**yankewei/herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify) | Shows a clickable macOS notification when an unseen pane becomes blocked or finishes. Clicking the alert brings the terminal forward and focuses the exact pane through `alerter`. |
| [**cobanov/herdr-ntfysh**](https://github.com/cobanov/herdr-ntfysh) | Sends ntfy push notifications when a Herdr agent finishes or asks for input. |
| [**TheMetalStorm/herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin) | Integrates Command Code as a Herdr agent runtime with process detection, idle, working, and blocked status, session recovery after server restarts, and toast alerts when input is needed. |
| [**dot/herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier) | Bundles a branded macOS notification app so Herdr alerts use the correct icon and can jump to the relevant pane. The app periodically refreshes its Launch Services registration to recover cleanly after reboots or updates. |
| [**horn553/herdr-ntfy**](https://github.com/horn553/herdr-ntfy) | Sends ntfy alerts for done and blocked agent states using standard command-line tools and curl. |
| [**zom-2018/herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify) | Sends structured ntfy alerts when an agent blocks or finishes. Notifications include the workspace, tab, and pane, and the plugin prefers a detected local ntfy server before using the network. |
| [**justinchiasson/herdr-nudge**](https://github.com/justinchiasson/herdr-nudge) | Sends clickable macOS notifications when an agent is blocked or done, or when a long zsh command finishes, and clicking one focuses that pane in Herdr. Works on Intel and Apple Silicon with nothing else to install, and withdraws notifications for panes that move on or close. |
| [**winoooops/herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher) | Adds live sidebar cards, lifecycle alerts, and a zero-configuration Claude Code metrics bridge for Herdr agents. |
| [**nhclink16/herdr-announcer**](https://github.com/nhclink16/herdr-announcer) | Speaks a one-sentence AI summary when an agent finishes or needs input. It supports local text-to-speech, ElevenLabs, or any custom command. |
| [**aclima01/herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows) | Sends native Windows 11 toast notifications when a Herdr agent finishes a turn or asks for input. |

**[All 73 projects →](catalog/03-mcp-and-socket-api.md#desktop-mobile-and-webhook-notifications)**

### Telemetry, events, and quota streaming

*34 projects. Event collectors and monitors for agent state, usage, cost, and runtime activity.*

| Project | What it does |
|---|---|
| [**DIodide/herdr-telemetry**](https://github.com/DIodide/herdr-telemetry) | Sends workspace and agent telemetry to an endpoint chosen by the user. It removes tokens, redacts sensitive prompts, and ships as a single binary. |
| [**Ziy1-Tan/herdr-codebuddy**](https://github.com/Ziy1-Tan/herdr-codebuddy) | Reports CodeBuddy session, working and permission states to Herdr TUI through hooks. |
| [**Gilamonster-Foundation/newt-agent · newt-tui/src/herdr**](https://github.com/Gilamonster-Foundation/newt-agent/tree/main/newt-tui/src/herdr) | Reports Newt coding-agent lifecycle states to the Herdr TUI from a pane using its socket API. |
| [**leonardoacosta/herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode) | Reports Jcode working and idle lifecycle states and session identity to Herdr TUI. |
| [**dsh-blue/herdr-agent-state**](https://github.com/dsh-blue/herdr-agent-state) | Reports DeepSeek Harness lifecycle state, session references, and model metadata to the current Herdr pane. |
| [**CodyBontecou/herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge) | Streams structured Herdr activity as NDJSON, including pane focus time, detected agent and model details, and local session summaries. Output can go to a file, webhook, or command, and transcript text is hidden by default. |
| [**vishnutskumar/herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics) | Analyzes memex session history and shows efficiency guidance for Herdr TUI agents. |
| [**cpcloud/herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview) | Combines active AgentsView sessions across projects, models, and agents, with real-time timelines and metrics inside Herdr. |
| [**akshat12/herdr-muse**](https://github.com/akshat12/herdr-muse) | Reports Muse Code working, idle, and blocked states to Herdr TUI through lifecycle hooks. |
| [**Comamoca/command-code-herdr**](https://github.com/Comamoca/command-code-herdr) | Reports Command Code working, idle, and blocked lifecycle states to Herdr TUI through its local socket. |

**[All 34 projects →](catalog/03-mcp-and-socket-api.md#telemetry-events-and-quota-streaming)**

### Voice, hardware, and remote bridges

*57 projects. Interfaces that connect Herdr to spoken input, physical devices, or remote control surfaces.*

| Project | What it does |
|---|---|
| [**klarluft/pitupitu**](https://github.com/klarluft/pitupitu) | Connects phone and browser voice conversations to coding agents running in Herdr TUI. |
| [**T0mSIlver/localvoxtral**](https://github.com/T0mSIlver/localvoxtral) | Fully local, real-time dictation for Apple Silicon Macs. It streams speech into the coding-agent session under the cursor, including Claude Code inside a Herdr pane, and uses that session as context for optional text polishing. |
| [**schacon/micro-manager**](https://github.com/schacon/micro-manager) | Uses the Creator Micro 2 hardware controller to operate Herdr. |
| [**brogrammerMW/herdr-voice**](https://github.com/brogrammerMW/herdr-voice) | Lets users speak to agents in Herdr TUI panes and hear replies using local OpenLive or realtime xAI, OpenAI, and Google models. |
| [**kccarlos/herdr-sheepdog**](https://github.com/kccarlos/herdr-sheepdog) | Monitors and steers Herdr agents by voice from an iPhone app or a Herdr app layout and panel. |
| [**second-state/vibetty**](https://github.com/second-state/vibetty) | Streams live Herdr terminal screens over MQTT to devices such as VibeKeys and VibeWatch and relays keystrokes back. It includes an MQTT broker and integrates with Herdr's command palette and status bar. |
| [**pawaca/even-better**](https://github.com/pawaca/even-better) | Mirrors Claude Code and Codex sessions in Herdr TUI to Even Realities G2 glasses and sends prompts back to the pane. |
| [**htlin222/herdr-gamepad**](https://github.com/htlin222/herdr-gamepad) | Maps Xbox, PlayStation, and 8BitDo controller buttons to Herdr actions through macOS GameController, enabling workspace and pane control away from the keyboard. |
| [**miko-misa/herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd) | Forwards remote agent development-server ports to the local machine and opens them after confirmation. |
| [**aneym/herdr-voice**](https://github.com/aneym/herdr-voice) | Controls workspaces, pane splits, and agent dispatch with spoken commands through OpenAI's Realtime API. A floating display shows the transcription and asks for confirmation before sending instructions. |

**[All 57 projects →](catalog/03-mcp-and-socket-api.md#voice-hardware-and-remote-bridges)**

### Protocol and third-party bridges

*79 projects. Adapters between Herdr and other multiplexers, platforms, messaging systems, or automation protocols.*

| Project | What it does |
|---|---|
| [**openclaw/crabbox**](https://github.com/openclaw/crabbox) | Adds Crabbox sandbox provisioning and remote test execution to Herdr. Plugin actions can prewarm temporary environments, synchronize diffs, and inspect active leases from an overlay. |
| [**27medkamal/tmux-agent-wizard**](https://github.com/27medkamal/tmux-agent-wizard) | Brings Herdr agent detection and compatible CLI-driven plugins to tmux. |
| [**RaviTharuma/cmux-herdr**](https://github.com/RaviTharuma/cmux-herdr) | Shows Herdr TUI pane viewers and agent status pills inside cmux using external attachment. |
| [**benkraus/herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay) | Bridges Herdr TUI socket operations to HTTP and WebSocket clients, including a browser interface and optional Tailscale publishing. |
| [**neon-solutions/neon-herdr**](https://github.com/neon-solutions/neon-herdr) | Embeds a serverless Postgres dashboard in a Herdr pane. It can create database branches per agent worktree, start or stop compute, and insert connection strings. |
| [**lachieh/herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux) | Mirrors Herdr TUI agents into the cmux sidebar with status, task text, and click-to-focus navigation. |
| [**HexSleeves/herdr-warp**](https://github.com/HexSleeves/herdr-warp) | Opens live Herdr TUI agents as native Warp panes on macOS. |
| [**agentwireprotocol/awp · plugin/herdr**](https://github.com/agentwireprotocol/awp/tree/main/plugin/herdr) | Connects Herdr TUI agents to Agent Wire Protocol messaging with inbox panes, notifications and idle-agent delivery. |
| [**wenxichang/herdr-pal**](https://github.com/wenxichang/herdr-pal) | Connects Herdr TUI agents across machines to a WeCom bot for session selection, task submission, terminal output, and limited key input. |
| [**Poor-Plebs/herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes) | Opens SSH terminals for hosts from SSH configuration in separate Herdr TUI workspaces. |

**[All 79 projects →](catalog/03-mcp-and-socket-api.md#protocol-and-third-party-bridges)**

---

## 4. Editor integrations

*108 projects. Bridges and pane synchronizers that let you drive Herdr agents directly from your code editor.* The top 10 of each subcategory by stars are below; the full list is in [catalog/04-editors.md](catalog/04-editors.md).

### Neovim navigation and splits

*30 projects. Plugins that make movement between Neovim windows and Herdr panes feel continuous.*

| Project | What it does |
|---|---|
| [**paulbkim-dev/vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation) | Ports vim-tmux-navigator behavior to Herdr. Direction keys move within Vim or Neovim until an edge is reached, then shift focus to the adjacent Herdr pane based on the pane's foreground process. |
| [**lmilojevicc/herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim) | Bridges Neovim split navigation and smart pane resizing with Herdr terminal panes. |
| [**aimdevlee/herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav) | Moves between Neovim splits and Herdr TUI panes with shared Ctrl+h/j/k/l bindings and socket-based focus tracking. |
| [**nettlesh/dotfiles**](https://github.com/nettlesh/dotfiles) | Personal Alacritty, Fish, Herdr, and Neovim dotfiles with workspace navigation and agent-dispatch configuration. |
| [**luneth90/keycade**](https://github.com/luneth90/keycade) | Provides a shortcut recall arcade for Omarchy, herdr, tmux, Vim, Neovim and LazyVim, six cabinets, each with its own deck, progress and mastery. |
| [**devxplay/herdr.nvim**](https://github.com/devxplay/herdr.nvim) | Navigates Neovim splits and Herdr TUI panes with Ctrl+h/j/k/l using a pane marker and a companion navigator. |
| [**bojackduy/nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation) | Applies vim-tmux-navigator-style directional keys across internal splits and surrounding Herdr panes. |
| [**kaar/nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator) | Uses one set of `Ctrl+h/j/k/l` shortcuts to move through both Neovim splits and Herdr panes. |
| [**willfish/herdr-navigator**](https://github.com/willfish/herdr-navigator) | Provides the Herdr-side actions needed for shared Vim or Neovim navigation. It checks the active pane process and either forwards the key to the editor or moves Herdr focus. |
| [**odiumuniverse/herdr-smart-nav**](https://github.com/odiumuniverse/herdr-smart-nav) | Moves between Neovim windows, Herdr TUI panes, tabs and workspaces with directional shortcuts. |

**[All 30 projects →](catalog/04-editors.md#neovim-navigation-and-splits)**

### Full Neovim-hosted workspaces

*4 projects. A deeper integration that uses Neovim as the main interface while Herdr owns the agent processes.*

| Project | What it does |
|---|---|
| [**raymondware/herdr.nvim**](https://github.com/raymondware/herdr.nvim) | Opens the Herdr TUI in a Neovim floating terminal and shows agent states in a status window and statusline component. |
| [**MomePP/herd.nvim**](https://github.com/MomePP/herd.nvim) | Uses Neovim as the primary dashboard to launch, monitor, and control background Herdr agent sessions. |
| [**ctbaum/herdr-deck**](https://github.com/ctbaum/herdr-deck) | Adds the companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovim, agent, shell, and lazygit deck. |
| [**romerramos/herdr-reviewr-nvim**](https://github.com/romerramos/herdr-reviewr-nvim) | Opens Reviewr files in the Neovim pane for the current HERDR workspace. |

### VS Code, Cursor, and dev containers

*16 projects. Extensions and environment setups for graphical editors and container-based development.*

| Project | What it does |
|---|---|
| [**zenbu-labs/terminal-code · herdr-plugin**](https://github.com/zenbu-labs/terminal-code/tree/main/herdr-plugin) | Adds an action that opens terminal-code, a VS Code-style editor for the terminal, in a split to the right of the focused pane in Herdr TUI. The plugin installs the tode binary when it builds. |
| [**scott-the-programmer/vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr) | Forwards Herdr's Unix socket into VS Code development containers through a loopback TCP bridge, allowing containerized agents to report status and receive commands from the host Herdr instance. |
| [**gambtho/herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer) | Starts shells and coding agents inside a repository's Dev Container through the official Dev Containers CLI and presents them as normal Herdr panes. |
| [**timofey-TK/herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor) | Opens the active Herdr workspace in VS Code or Zed with one shortcut. Local and SSH-remote workspaces are translated into the correct editor URI automatically. |
| [**mkellerman/herdex**](https://github.com/mkellerman/herdex) | Displays Herdr TUI workspaces and agent status in VS Code, with a terminal and editor actions. |
| [**alex-devdone/herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open) | Opens the focused Herdr pane's project in Cursor or VS Code, including remote panes through the editor's Remote SSH support. |
| [**mrshll/herdr-container-agents**](https://github.com/mrshll/herdr-container-agents) | Detects coding agents running inside containers and report them as herdr agents. |
| [**phine-apps/herdr-collie**](https://github.com/phine-apps/herdr-collie) | Bridges VS Code and Herdr to orchestrate AI agents, Git worktrees, and context sharing directly from the editor. |
| [**clement-micol/herdr-bridge**](https://github.com/clement-micol/herdr-bridge) | Bridges from herdr panes to VS Code: attach herdr terminals via vscode:// URIs. |
| [**endoumame/herdr-vscode**](https://github.com/endoumame/herdr-vscode) | Adds an inline code-review workflow to VS Code for work associated with Herdr agent sessions. The source description is incomplete beyond writing comments where the code is read. |

**[All 16 projects →](catalog/04-editors.md#vs-code-cursor-and-dev-containers)**

### Vim, Kakoune, and other editors

*13 projects. Navigation and workflow integrations for editors outside Neovim and VS Code.*

| Project | What it does |
|---|---|
| [**ImArtisann/zed-herdr**](https://github.com/ImArtisann/zed-herdr) | Keeps Zed projects synchronized with Herdr workspaces by listening to lifecycle events over the Unix socket. It supports reconnection and full snapshot synchronization after interruptions. |
| [**roman/herdr.el**](https://github.com/roman/herdr.el) | Provides an Emacs porcelain interface for managing Herdr workspaces and agent sessions. |
| [**ionrock/ghostherd**](https://github.com/ionrock/ghostherd) | Manages Herdr agent terminals from Emacs through ghostel. |
| [**baongoc124/emacs-herdr**](https://github.com/baongoc124/emacs-herdr) | Runs the Herdr TUI in an Emacs Ghostel buffer and adds agent switching, project launches, and code dispatch. |
| [**Schaitanya535/herdr-config**](https://github.com/Schaitanya535/herdr-config) | A personal Herdr configuration with custom keys, a theme, and a helper that sends scrollback into Neovim. |
| [**T0mSIlver/hither**](https://github.com/T0mSIlver/hither) | Opens the active remote Herdr directory in Zed on macOS with a single key chord. |
| [**Yukaii/herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup) | Runs Kakoune terminal commands in native Herdr popups. |
| [**Yukaii/herdr.kak**](https://github.com/Yukaii/herdr.kak) | Controls Herdr panes, tabs, focus, and popups from Kakoune. |
| [**AVGVSTVS96/vim-herdr-navigator**](https://github.com/AVGVSTVS96/vim-herdr-navigator) | Moves between Vim or Neovim splits and Herdr TUI panes with shared directional shortcuts. |
| [**eddof13/herdr.el**](https://github.com/eddof13/herdr.el) | Controls Herdr from Emacs while hosting Herdr's terminal sessions inside Emacs through ghostel. |

**[All 13 projects →](catalog/04-editors.md#vim-kakoune-and-other-editors)**

### REPL and code dispatchers

*8 projects. Tools for sending code or commands from an editor to a running pane or interactive session.*

| Project | What it does |
|---|---|
| [**francjpd/broadmand**](https://github.com/francjpd/broadmand) | Broadcasts shell commands or a selected working directory to panes in the active Herdr TUI workspace. |
| [**exviolet/sendoff**](https://github.com/exviolet/sendoff) | Edits prompts in a Linux desktop app and sends them to terminal agents running in Herdr, tmux, or Orca. |
| [**jcarlos7121/herdr-sidekick-agents.nvim**](https://github.com/jcarlos7121/herdr-sidekick-agents.nvim) | Opens Claude Code, Codex, or Grok in side-by-side Herdr panes and forwards Neovim selection context. |
| [**timofey-TK/herdr-yazi-agent**](https://github.com/timofey-TK/herdr-yazi-agent) | Picks files in Yazi, get their paths in your agent's prompt. |
| [**rytkmt/herdr-send.nvim**](https://github.com/rytkmt/herdr-send.nvim) | Sends file references and prompts from Neovim to AI agents in the active Herdr workspace. |
| [**luiarthur/herdr.vim**](https://github.com/luiarthur/herdr.vim) | Starts a language-appropriate REPL in a Herdr pane and sends the current line, whole file, or visual selection from Vim or Neovim. It supports older Vim releases as well as modern Neovim. |
| [**lancodev/herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker) | Runs Laravel Tinker beside an editor in a Herdr TUI pane or popup and reevaluates the scratch file when saved. |
| [**AbhijithAnirudhan2907/herdr-sidebar**](https://github.com/AbhijithAnirudhan2907/herdr-sidebar) | A fork of herdr-sidebar that adds an editor inside the pane, including save, syntax highlighting, undo and redo, and find and replace. |

### Editor plugins and bridges

*37 projects. General-purpose bridges that synchronize editor state with Herdr panes and agents.*

| Project | What it does |
|---|---|
| [**eugenioenko/ttt · herdr-plugin**](https://github.com/eugenioenko/ttt/tree/main/herdr-plugin) | Opens TTT Editor in a Herdr TUI pane for editing files in the active worktree. |
| [**ChmaraX/herdr-nvim**](https://github.com/ChmaraX/herdr-nvim) | Opens a persistent Neovim sidebar in Herdr with file search and annotations that can be sent to agents. |
| [**makyinmars/herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim) | Stages Neovim selections, cursor positions, and file details as Markdown context for a Herdr agent. |
| [**ryonakae/zerdr**](https://github.com/ryonakae/zerdr) | Keeps Herdr TUI workspace focus aligned with the matching Zed checkout and connects Zed terminal threads to Herdr panes. |
| [**mcuste/herdr-context.nvim**](https://github.com/mcuste/herdr-context.nvim) | Sends the current Neovim buffer, open buffers, or a Visual selection to a Herdr coding agent as a correctly formatted file reference. It targets one workspace agent automatically or opens a fuzzy picker when several agents are in the tab or workspace. |
| [**nwiizo/signalbox.nvim**](https://github.com/nwiizo/signalbox.nvim) | Controls persistent Herdr coding agents from Neovim with an attention-focused interface. |
| [**WorksOnMyVM/herdr-agent-bridge.nvim**](https://github.com/WorksOnMyVM/herdr-agent-bridge.nvim) | Stages Neovim editor context for Herdr agent panes. |
| [**ctbaum/herdr-agents.nvim**](https://github.com/ctbaum/herdr-agents.nvim) | Runs Claude Code, Codex, and Pi in Herdr TUI sibling panes while preserving Neovim editor integration and agent connections. |
| [**Zamua/openloc.nvim**](https://github.com/Zamua/openloc.nvim) | Opens file references in the Neovim that already belongs to the workspace. |
| [**alexeyco/herdr-open-in**](https://github.com/alexeyco/herdr-open-in) | Opens the current Herdr TUI workspace in a detected editor, with a picker when several editors are available. |

**[All 37 projects →](catalog/04-editors.md#editor-plugins-and-bridges)**

---

## 5. Switch and restore sessions

*262 projects. Fuzzy switchers, state managers, and layout restoration tools for organizing agent workspaces.* The top 10 of each subcategory by stars are below; the full list is in [catalog/05-sessions.md](catalog/05-sessions.md).

### Fuzzy session switchers and terminal pickers

*111 projects. Interactive pickers for finding and focusing workspaces, tabs, panes, agents, or projects.*

| Project | What it does |
|---|---|
| [**nicosuave/memex**](https://github.com/nicosuave/memex) | Indexes conversations from Claude Code, Codex, Pi, OpenCode, and Cursor with hybrid search. A Herdr TUI searches the archive and can resume a selected interaction in a fresh tab. |
| [**jeffarese/herdr-bar**](https://github.com/jeffarese/herdr-bar) | A dependency-free Python command palette for jumping to any Herdr tab, agent, repository, or branch. |
| [**thanhdat77/herdr-picker-plus**](https://github.com/thanhdat77/herdr-picker-plus) | A Ratatui overlay that combines workspaces, project templates, directories, zoxide history, SSH hosts, agent panes, and plugin integrations. It reuses matching workspaces and can create or focus remote-host workspaces automatically. |
| [**thanhdat77/herdr-navigator**](https://github.com/thanhdat77/herdr-navigator) | Searches and switches between active Herdr sessions and workspaces using an interactive fuzzy picker. |
| [**andrewchng/herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer) | A tmux-sessionizer-style launcher for Herdr. Fzf selects projects or worktrees, while TOML defines tabs, splits, startup commands, repository-specific layouts, and preview panels. |
| [**beyondlex/herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator) | A Rust popup that tracks recently focused workspaces, tabs, panes, and agents through socket events. It provides a live most-recently-used index, keyboard navigation, and fuzzy search. |
| [**lmilojevicc/seshagy**](https://github.com/lmilojevicc/seshagy) | Finds projects and tmux or Herdr TUI sessions in a dashboard and shows coding-agent states before attaching. |
| [**dmnkf/herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch) | Searches live workspace metadata, pane output, and optional archived conversations across the Herdr TUI and app, then jumps to or resumes a match. |
| [**dartyuhov/herdr-blink**](https://github.com/dartyuhov/herdr-blink) | Opens a fuzzy Herdr TUI agent picker that prioritizes agents needing attention and sorts the rest by recent use. |
| [**hxreborn/herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts) | Searches past and live coding-agent sessions by title, prompt, reply, or tool call in an fzf popup, then resumes the pick in a new Herdr tab or focuses its pane when it is already running. Covers Claude Code, Codex, OpenCode, Gemini CLI, Droid, Copilot CLI, Kimi Code, and Qwen Code with a pre-warmed index in standard-library Python. |

**[All 111 projects →](catalog/05-sessions.md#fuzzy-session-switchers-and-terminal-pickers)**

### Persistence, snapshots, and state restoration

*68 projects. Tools that record layouts and process context, then rebuild or resume them after a restart.*

| Project | What it does |
|---|---|
| [**ntindle/herdr-resurrect**](https://github.com/ntindle/herdr-resurrect) | Captures workspaces, tabs, panes, directories, and running agent processes so a complete Herdr environment can be restored after a crash or restart. |
| [**pattont/RexAgentRestore**](https://github.com/pattont/RexAgentRestore) | Imports Herdr workspaces into Rex with their tabs, splits, folders, and agent conversations. |
| [**tornikegomareli/herdr2rex**](https://github.com/tornikegomareli/herdr2rex) | Migrates Herdr TUI workspaces to Rex with tabs, splits, folders, and supported agent conversations. Imports Rex sessions back into Herdr and restores Claude Code conversations. |
| [**iviaxpow3r/herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker) | Parks active panes and tabs outside the current working layout and restores them later with agent state and prompt progress intact. |
| [**gokay-ai/sheep**](https://github.com/gokay-ai/sheep) | Records agent-turn checkpoints and restores selected worktree changes after a dry run, with an optional notice to the agent. |
| [**wbarakat/omarchy-session-restore**](https://github.com/wbarakat/omarchy-session-restore) | Saves Omarchy window and terminal state and restores it after login, with optional Herdr agent-session resume. |
| [**pedroloch/herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close) | Restores recently closed panes or tabs, including their split hierarchy, directories, labels, and launched agents, through a shortcut or history picker. |
| [**mcc0x/herdr-tether**](https://github.com/mcc0x/herdr-tether) | Keeps local or SSH-backed terminal workloads running after their Herdr TUI view closes and reconnects to them later. |
| [**andymartinezot/avocado-park**](https://github.com/andymartinezot/avocado-park) | Parks idle Claude Code, Codex, and OpenCode sessions to free memory and resumes them in the same Herdr TUI pane. |
| [**chandrasekharan98/herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save) | Saves Herdr workspace layouts and commands for later restoration through an fzf picker. |

**[All 68 projects →](catalog/05-sessions.md#persistence-snapshots-and-state-restoration)**

### Workspace and multi-session management

*83 projects. Managers for creating, grouping, naming, attaching to, and cleaning up several sessions.*

| Project | What it does |
|---|---|
| [**nikok6/herdr-mirror**](https://github.com/nikok6/herdr-mirror) | Mirrors remote Herdr workspaces and agent state into a local sidebar over SSH or Docker. Remote panes can be watched and controlled alongside local ones. |
| [**taxueseek/session-digger**](https://github.com/taxueseek/session-digger) | Indexes conversations from Claude Code, Codex, and other agents in SQLite FTS5. It also tracks token and cache data and creates local HTML reports for review. |
| [**AVGVSTVS96/herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr) | Uses fzf and the Herdr socket API to move live tabs and panes between workspaces without stopping their processes. |
| [**third774/herdr-last-workspace**](https://github.com/third774/herdr-last-workspace) | Tracks workspace IDs and toggles between the current and previous workspace with one key. It remains correct after reordering and exits quietly if the earlier workspace was closed. |
| [**wenhanweime/herduck**](https://github.com/wenhanweime/herduck) | Groups related Claude Code, Codex, OpenCode, and Pi sessions into one Work and keeps its goal, blocker, and next step. Runs as a separate app derived from Herdr, with a thin plugin that opens it from Herdr. |
| [**GiorgiTarsaidze/herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles) | Groups Herdr TUI spaces and agents into named profiles and switches between them with a popup chooser. |
| [**den-tanui/herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide) | Uses zoxide's directory history when creating Herdr workspaces, tabs, and panes, making recent project paths quick to open. |
| [**douglascorrea/herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox) | Shows Herdr TUI agent session titles, runtimes, workspace statistics, and unread state in a central inbox. |
| [**2lab-ai/herdr-mx**](https://github.com/2lab-ai/herdr-mx) | Connects multiple local and SSH Herdr TUI servers in one sidebar with a downstream multi-remote client. |
| [**lmilojevicc/herdr-last**](https://github.com/lmilojevicc/herdr-last) | Toggles between the current and previously active Herdr TUI workspace or tab. |

**[All 83 projects →](catalog/05-sessions.md#workspace-and-multi-session-management)**

---

## 6. Worktrees and terminal experience

*1333 projects. Git worktree automation, terminal navigation, status displays, HUDs, and developer environment tools.* The top 10 of each subcategory by stars are below; the full list is in [catalog/06-worktrees-and-terminal.md](catalog/06-worktrees-and-terminal.md).

### Git worktree automation

*139 projects. Tools that create isolated branches and worktrees for agents, then connect them to Herdr workspaces or tabs.*

| Project | What it does |
|---|---|
| [**devashish2203/herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk) | Creates, switches, merges, and removes Git worktrees with Worktrunk from Herdr TUI, using Worktrunk lifecycle hooks and an interactive branch picker. |
| [**razajamil/herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager) | Defines tabs, splits, and startup commands in YAML and applies the layout whenever a new worktree opens. It can run a blocking setup command first and prune worktrees whose upstream branch has been removed. |
| [**NathanFlurry/herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace) | Adds key bindings for creating and removing Jujutsu workspaces through `jj workspace`, opening the result as a Herdr workspace or tab. |
| [**tdi/herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup) | Runs repository setup after Herdr creates a worktree, including copying `.env` files and executing commands such as `mise trust` and `direnv allow`, so the environment is ready immediately. |
| [**wyattjoh/herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer) | Renames numbered tabs from the agent's first prompt and can also rename an automatically linked worktree's branch and workspace. The short task name is generated locally with Apple Foundation Models or Codex. |
| [**tdi/herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear) | Searches active Linear issues, then creates or focuses a matching Git worktree and Herdr workspace. An optional split shows the issue description and assignee. |
| [**EzraCerpac/jj-waltz**](https://github.com/EzraCerpac/jj-waltz) | Switches Jujutsu workspaces and maps their directories to Herdr TUI tabs and workspaces. |
| [**freethinkel/herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) | Runs global YAML-configured shell hooks when Git worktrees are created or removed. Hooks receive paths and event metadata, and executions are recorded durably. |
| [**tdi/herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr) | Creates an isolated Git worktree from a GitHub pull request and opens it as a new Herdr workspace in one operation. |
| [**hmu332233/herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree) | Symlinks declared ignored files, environment files, and caches from the main checkout into new worktrees without replacing files that already exist. |

**[All 139 projects →](catalog/06-worktrees-and-terminal.md#git-worktree-automation)**

### Workspace lifecycle and multi-repository tools

*45 projects. Higher-level utilities for starting, tracking, and removing workspaces that span one or more repositories.*

| Project | What it does |
|---|---|
| [**OliverGilan/herdr-jj**](https://github.com/OliverGilan/herdr-jj) | Adds Jujutsu workspace creation, remote fetching, bookmark setup, live change metadata, and post-create hooks to Herdr. |
| [**jattento/herdr-multirepo**](https://github.com/jattento/herdr-multirepo) | Creates a Herdr TUI workspace containing matching feature-branch worktrees from multiple repositories. |
| [**LoriKarikari/kubeflock**](https://github.com/LoriKarikari/kubeflock) | Creates and connects Kubernetes agent sandboxes to Herdr TUI and manages their lifecycle. |
| [**leoleducq/devflow**](https://github.com/leoleducq/devflow) | Provisions isolated development environments with databases, ports, environment files, and servers, and synchronizes them with Herdr TUI workspaces. |
| [**alon-z/herdr-devup**](https://github.com/alon-z/herdr-devup) | Reads `.herdr/dev.toml` to start a project's tabs, panes, and services, refresh an ngrok URL across configured environment files, and close only the tabs it created. |
| [**nicksenap/grove-herdr**](https://github.com/nicksenap/grove-herdr) | Asks for a name on a key press, runs Grove's gw create and opens the new path as a Herdr workspace. The install script also wires Grove hooks so a Herdr workspace opens and closes with gw create and gw delete. |
| [**dalogax/herdr-agent-hibernate**](https://github.com/dalogax/herdr-agent-hibernate) | Ends idle, unfocused OpenCode, Claude Code and Codex panes to free memory and relaunches the same session with native resume flags when you focus the pane again. |
| [**alexjyong/herdr-codespaces**](https://github.com/alexjyong/herdr-codespaces) | Lists your GitHub Codespaces in a picker and adds the chosen one as a Herdr machine in the sidebar next to local workspaces. |
| [**yoyoyeti/multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin) | Creates and attaches multitrunk task workspaces in Herdr TUI with an agent pane, repository tabs, and interactive popups. |
| [**yavuzhansarmaz/herdr-vps-local**](https://github.com/yavuzhansarmaz/herdr-vps-local) | Mirrors repos from a VPS or Raspberry Pi saved machine to your laptop with Mutagen. Lets you edit in a local IDE while agents keep running on the remote machine. |

**[All 45 projects →](catalog/06-worktrees-and-terminal.md#workspace-lifecycle-and-multi-repository-tools)**

### Diff review and code inspection

*89 projects. Side-by-side git diff inspection and comment handoff tools for agent reviews.*

| Project | What it does |
|---|---|
| [**persiyanov/herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr) | Opens an interactive diff review interface for inspecting agent changes and sending review feedback. |
| [**plannotator/herdr-annotate**](https://github.com/plannotator/herdr-annotate) | Annotates terminal text, reviews documents and agent replies in Herdr, and returns feedback directly to the running agent. |
| [**jhochenbaum/herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff) | Displays side-by-side git diffs in an adjacent pane and lets developers leave review comments for agents. |
| [**crittylabs/critty**](https://github.com/crittylabs/critty) | Shows agent review and approval prompts in the terminal and reports attention status to the Herdr app through OSC 7501. |
| [**osolmaz/ghzinga**](https://github.com/osolmaz/ghzinga) | Opens a GitHub issue or pull request in a terminal interface with review and comment actions from Herdr TUI links. |
| [**JonasBaeumer/herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator) | Adds in-editor file annotations for reviewing code while working with agents in Herdr. |
| [**Crokily/herdr-lazygit**](https://github.com/Crokily/herdr-lazygit) | Runs lazygit in a Herdr sidebar with shortcuts for opening, expanding, and staging changes, plus AI-assisted commit-message generation from the pending diff. |
| [**ChmaraX/herdr-gitview**](https://github.com/ChmaraX/herdr-gitview) | Reviews Git status and diffs, edits files in Neovim, stages or discards hunks, and commits from a Herdr panel. |
| [**plannotator/herdr-plannotator**](https://github.com/plannotator/herdr-plannotator) | Embeds Plannotator plan reviews in a dedicated Herdr browser pane so plans can be annotated, discussed, and approved beside active coding sessions. |
| [**tomasvarga/herdr-pickr**](https://github.com/tomasvarga/herdr-pickr) | Intercepts clicked GitHub pull-request and GitLab merge-request links and opens their diffs in tuicr, Hunk, or a browser, with an optional AI first-pass review. |

**[All 89 projects →](catalog/06-worktrees-and-terminal.md#diff-review-and-code-inspection)**

### File viewers, terminal browsers, and markdown previews

*81 projects. In-terminal file viewers, interactive web browsers, image previews, and markdown rendering panes.*

| Project | What it does |
|---|---|
| [**zenbu-labs/terminal-browser · herdr-plugin**](https://github.com/zenbu-labs/terminal-browser/tree/main/herdr-plugin) | Opens a terminal browser beside a Herdr TUI pane and supports agent-driven browser interaction. |
| [**smarzban/herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer) | Opens a read-only file viewer in a Herdr TUI split with Git status, diffs, Markdown, and source previews. |
| [**alexarthurs/herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar) | Opens a dockable file explorer and source-control panel with previews and AI-drafted commit messages in Herdr TUI. |
| [**ogulcancelik/herdr-browser**](https://github.com/ogulcancelik/herdr-browser) | Renders an interactive Chromium browser inside a Herdr pane and lets agents automate it through Chrome DevTools Protocol. The project is deprecated in favor of terminal-browser. |
| [**iurysza/termscope**](https://github.com/iurysza/termscope) | Finds visible file paths and web links on the terminal screen, lets the user select one with fuzzy search, and opens it in a separate split without disturbing the main pane. |
| [**speardragon/herdr-yazi**](https://github.com/speardragon/herdr-yazi) | Opens the Yazi file manager in a Herdr pane or tab at the current directory while reusing the user's existing Yazi configuration. |
| [**StructuPath/herdr-browser**](https://github.com/StructuPath/herdr-browser) | Opens a drivable Chromium browser in a Herdr pane for agent automation and manual inspection. |
| [**alexarthurs/herdr-notes**](https://github.com/alexarthurs/herdr-notes) | Keeps one persistent Markdown note per workspace, with rendered and edit modes, autosave, and restoration after restarts. |
| [**dwarvesf/herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook) | Previews a file path from the clipboard in an overlay and can expand it into a full terminal viewer, avoiding manual path entry or temporary splits. |
| [**slara/terminal-markdown-renderer**](https://github.com/slara/terminal-markdown-renderer) | Opens rendered Markdown in a terminal browser from a Herdr TUI plugin. |

**[All 81 projects →](catalog/06-worktrees-and-terminal.md#file-viewers-terminal-browsers-and-markdown-previews)**

### Pane navigation and overlay hints

*60 projects. Direct 1-character overlay hints and smart directional pane jumping.*

| Project | What it does |
|---|---|
| [**nathan-poncet/herdr-fingers**](https://github.com/nathan-poncet/herdr-fingers) | Labels visible paths, URLs, hashes, and other text with short hints to copy, paste, or open them in Herdr TUI. |
| [**crierr/herdr-arrange**](https://github.com/crierr/herdr-arrange) | Rearranges Herdr TUI panes from a popup, including swaps, resizing, layouts, and transfers between tabs. |
| [**husniadil/herdr-swipe**](https://github.com/husniadil/herdr-swipe) | Adds macOS trackpad gestures for switching Herdr TUI panes, tabs, and spaces and jumping to agents awaiting attention. |
| [**milkyskies/herdr-attention**](https://github.com/milkyskies/herdr-attention) | Moves focus to the next agent needing attention with one key, checking blocked agents before completed ones. |
| [**81zi/reficus**](https://github.com/81zi/reficus) | Resizes Herdr TUI panes as focus changes, keeping other panes visible and optionally expanding agents waiting for input. |
| [**xzedx/herdr-easyjump**](https://github.com/xzedx/herdr-easyjump) | Jumps to any space, agent, pane, or tab using EasyMotion-style hint labels in the Herdr sidebar. |
| [**KonstantinKai/herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon) | Marks Herdr TUI panes and jumps back to them with numeric shortcuts or a picker. |
| [**meerzulee/herdr-float**](https://github.com/meerzulee/herdr-float) | Opens a floating shell for the current Herdr TUI space with Option-F or Alt-F, using Herdr's native popup placement so the tiled layout stays visible. Keeps one persistent shell session per space. |
| [**TinyWhite1997/herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker) | Jumps to Herdr TUI panes using one- or two-letter labels in a workspace and tab picker. |
| [**vjeantet/herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control) | Opens a full-screen overlay showing every pane of the current workspace as a live tile grouped by tab, with styled ANSI previews and agent status. Arrows or `hjkl` move the selection, `Enter` focuses the pane, and `Backspace` closes it without leaving the overview. |

**[All 60 projects →](catalog/06-worktrees-and-terminal.md#pane-navigation-and-overlay-hints)**

### Pane layout management

*44 projects. Tools that arrange, resize, and manage Herdr TUI panes.*

| Project | What it does |
|---|---|
| [**thuanlm215/herdr-grid**](https://github.com/thuanlm215/herdr-grid) | Opens a visual editor for dragging, resizing, and safely rearranging live pane layouts without restarting pane processes. It can add shell panes, apply fixed presets, or build a preset in a new workspace. |
| [**osamahbeig/herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover) | Moves, re-splits, and swaps Herdr panes through a clickable overlay. |
| [**shibayu36/herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes) | Automatically equalizes Herdr TUI panes after splits and closures, with an optional manual action. |
| [**iurysza/herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts) | Adds tmux-style pane resizing and layouts to Herdr. |
| [**edouard-andrei/herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools) | Rearranges existing panes into main-left, grid, or equalized presets without changing pane IDs, tab IDs, or running processes. |
| [**crierr/herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout) | Adds tmux-style layout presets for Herdr, including even horizontal, even vertical, main horizontal, main vertical, tiled, cycle, and balance. |
| [**iuhoay/herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane) | Moves the active pane into a new tab while preserving its process, similar to tmux break-pane. It unzooms complex tabs first and leaves single-pane tabs unchanged. |
| [**federbenjamin/herdr-undo-close**](https://github.com/federbenjamin/herdr-undo-close) | Reopens the pane you just closed in Herdr in the same split, with its old scrollback above a fresh prompt. A Claude Code pane resumes its conversation, and a command that was running returns typed but not run. |
| [**orcchg/herdr-topstrip**](https://github.com/orcchg/herdr-topstrip) | Opens every new tab and space as a narrow top shell strip over a wide work pane, and relaunches the strip if you close it. |
| [**ponko2/herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes) | Automatically equalizes Herdr TUI pane sizes when panes are created, closed, moved, or exit, with an on-demand action. |

**[All 44 projects →](catalog/06-worktrees-and-terminal.md#pane-layout-management)**

### Terminal keybindings and shortcut helpers

*88 projects. Custom keymap packs, leader-key setups, and prefix-free navigation.*

| Project | What it does |
|---|---|
| [**yuk1ty/herdr-spreader**](https://github.com/yuk1ty/herdr-spreader) | Builds complete Herdr layouts from YAML, including tabs, splits, directories, startup commands, and dependencies that wait for output patterns before launching later panes. |
| [**yigitkonur/native-shortcuts-herd**](https://github.com/yigitkonur/native-shortcuts-herd) | Adds browser-style macOS shortcuts such as `Cmd+T`, `Cmd+W`, and numbered tab selection across Ghostty and Herdr. It uses a separate Ghostty sidecar config, creates backups, and includes a clean uninstall path. |
| [**sohanemon/herdr-helpr**](https://github.com/sohanemon/herdr-helpr) | Adds keyboard overlays for naming a workspace before creation, renaming the current workspace, and closing every pane or tab except the focused one. |
| [**CowboyVang/herdr-which-key**](https://github.com/CowboyVang/herdr-which-key) | Shows Herdr keybindings in a grouped overlay and runs a selected binding. |
| [**ramarivera/herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which) | Shows searchable Herdr TUI keybindings and launches configured actions from a Ratatui popup. |
| [**Taeyoung96/herdr-dotfiles**](https://github.com/Taeyoung96/herdr-dotfiles) | A ready-to-use Herdr configuration with prefix-free pane movement, `Ctrl+Space` as the prefix, Catppuccin styling, and a global agent panel. The installer symlinks the file and backs up the previous config. |
| [**johnlindquist/herdr-game**](https://github.com/johnlindquist/herdr-game) | Teaches Herdr TUI navigation and agent operations through interactive browser lessons backed by isolated Herdr sessions. |
| [**The-Dave-Stack/herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap) | Displays all Herdr key bindings in an overlay and can run bindings that have an equivalent command-line action. |
| [**markhuot/herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits) | Balances all split dimensions in the current tab with one shortcut, equalizing panes by rows or columns after manual resizing or new splits. |
| [**jeph/herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer) | Automatically retile and equalizes Herdr panes whenever a pane is created, closed, or exits. |

**[All 88 projects →](catalog/06-worktrees-and-terminal.md#terminal-keybindings-and-shortcut-helpers)**

### Command palettes and workspace switchers

*62 projects. Searchable menus for Herdr commands, projects, workspaces, and common actions.*

| Project | What it does |
|---|---|
| [**fullerzz/herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh) | A sesh-style Herdr workspace picker with zoxide integration for creating workspaces from frequently used directories. |
| [**JanTvrdik/herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette) | Opens an fzf overlay containing every action from every installed plugin. It preserves the originating workspace directory, runs the selected action, and removes the temporary overlay afterward. |
| [**speardragon/herdr-command-center**](https://github.com/speardragon/herdr-command-center) | Runs registered commands from a Herdr TUI popup using a single keybinding, arrow keys, or assigned slots. |
| [**vjeantet/herdr-palette**](https://github.com/vjeantet/herdr-palette) | Combines Herdr's built-in operations, every installed plugin's actions, user-defined commands, and reusable prompts in one fuzzy Rust/Ratatui palette. It preserves the originating pane context and asks for inputs, selections, or confirmation when an operation needs them. |
| [**mmjang/herdr-omni**](https://github.com/mmjang/herdr-omni) | Searches Herdr TUI workspaces, actions, and live or saved Claude and Codex sessions, including conversation contents. |
| [**ramarivera/herdr-palette**](https://github.com/ramarivera/herdr-palette) | A Rust and Ratatui fuzzy command palette for Herdr workspaces. |
| [**enekos/herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions) | Opens an fzf picker for native Herdr TUI actions and jump targets, showing the configured shortcut for each action. |
| [**cesarferreira/herdr-palette**](https://github.com/cesarferreira/herdr-palette) | Finds and runs Herdr TUI actions in a popup while showing their effective shortcuts. |
| [**arjenblokzijl/herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher) | Defines named workflows as `.mjs` files with custom input fields and a `run()` function. Workflows can be launched from a Herdr picker or through `herdr-launcher run`, supporting interactive and scripted use. |
| [**lurepos/herdr-commander**](https://github.com/lurepos/herdr-commander) | Discovers VS Code tasks and project commands such as npm and Cargo scripts and launches them in Herdr TUI tabs or panes. |

**[All 62 projects →](catalog/06-worktrees-and-terminal.md#command-palettes-and-workspace-switchers)**

### Status lines and workspace metadata

*142 projects. Status lines, external terminal and desktop bars, pane labels, and workspace metadata without sidebar or tab-label displays.*

| Project | What it does |
|---|---|
| [**fkiene/llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr) | Activates the llmtrim compression proxy in new Herdr workspaces, shows savings badges in pane rows, and opens llmtrim's dashboard in a split. It also warns when a pane did not inherit the proxy settings. |
| [**jankeesvw/omarchy-herdr**](https://github.com/jankeesvw/omarchy-herdr) | Runs herdr servers in the Omarchy bar, with every agent inside them, and a click that lands you on the one you picked. |
| [**rjyo/herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync) | Writes workspace, tab, and agent context to the outer terminal title. It uses pane metadata and status first, then falls back to recent prompts in local Claude Code or Codex session files. |
| [**wenhanweime/herdr-plugin-renamer**](https://github.com/wenhanweime/herdr-plugin-renamer) | Uses an LLM to name sessions for Claude Code, Codex, Grok, Pi, and OpenCode, with Chinese or English labels and OpenCode Zen as the default engine. |
| [**ezcorp-org/herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status) | Shows staged, modified, untracked, and conflicted Git files for each workspace beside its branch name. |
| [**njpatel/omaherdr**](https://github.com/njpatel/omaherdr) | Shows Herdr TUI sessions, spaces, tabs, and agents in the Omarchy bar and jumps to a selected item. |
| [**bcihanc/herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title) | Copies the Claude Code session title, including `/rename` or automatic summaries, into Herdr pane metadata. |
| [**flowy11/agent-panel**](https://github.com/flowy11/agent-panel) | Shows the focused Claude Code or Codex session, subagents, messages, references and tasks in a Herdr TUI side panel. |
| [**Phoobobo/herdr-workboard**](https://github.com/Phoobobo/herdr-workboard) | Shows Herdr TUI workspaces as Kanban boards and moves live panes between task-state tabs. |
| [**Razz21/herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status) | Detects dev servers in panes via pluggable specs and reports lifecycle status. |

**[All 142 projects →](catalog/06-worktrees-and-terminal.md#status-lines-and-workspace-metadata)**

### Automatic tab, pane, and workspace names

*92 projects. Plugins that rename tabs, panes, and workspaces from the foreground process, directory, git branch, agent session title, or first prompt, plus numbered tab and workspace labels.*

| Project | What it does |
|---|---|
| [**kryptamine/herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title) | Updates Herdr tab titles automatically based on active workspace tasks to keep development contexts organized. |
| [**qu8n/herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename) | Renames tabs from the active foreground process and icon, and prefixes workspaces, tabs, and agents with numbers 1 through 9 for quick visual and keyboard selection. |
| [**iurysza/herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename) | Uses a lightweight LLM to derive short workspace and tab names from pane activity, replacing generic numbers or directory labels with current task summaries. |
| [**sh1ma/herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title) | Runs in the background and derives Herdr tab names from the topic and intent of Claude Code or Codex conversations. |
| [**aarsh21/herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title) | Provides automatic tmux-style tab titles for Herdr. |
| [**wjarka/herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title) | Writes color-coded counts of working, blocked, done, and idle Herdr agents into Ghostty tab titles. |
| [**killerz3/herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler) | Auto-titles Herdr tabs using local agy, claude, codex, or opencode harnesses without external API keys. |
| [**kakigakki/herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer) | Uses Claude Code session titles for agent tabs and directory names for workspaces, providing automatic ChatGPT-style labels across parallel sessions. |
| [**danbuhler/herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync) | Renames panes and tabs from the active topic or terminal title emitted by Claude Code and Codex, while avoiding rename loops and respecting manual labels. |
| [**lmilojevicc/herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename) | Renames each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. |

**[All 92 projects →](catalog/06-worktrees-and-terminal.md#automatic-tab-pane-and-workspace-names)**

### Sidebar grouping, ordering, and filtering

*45 projects. Plugins that restructure the Spaces and Agents sidebars into trees, project groups, priority or recency order, filtered views, and compact one-line rows.*

| Project | What it does |
|---|---|
| [**hhdebb/herdr-radar**](https://github.com/hhdebb/herdr-radar) | Shows agent activity in the Herdr TUI sidebar, grouping workspaces and worktrees and highlighting waiting or stale sessions. |
| [**ShankyJS/herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents) | Limits the agent sidebar to workers in the currently focused workspace, reducing unrelated fleet noise when moving between projects. |
| [**kriuchkov/herdr-scope**](https://github.com/kriuchkov/herdr-scope) | Shows Herdr TUI agent state in a project-grouped sidebar and jumps to agents waiting for input. |
| [**gonzalonicolasr/herdr-bandeja-to-dos**](https://github.com/gonzalonicolasr/herdr-bandeja-to-dos) | Organizes Herdr TUI agents by attention state in the sidebar and shows to-dos left by agents. |
| [**dboeter/herdr-agent-tree**](https://github.com/dboeter/herdr-agent-tree) | Docks a narrow pane on the left or right of every tab that shows workspaces as groups and their agents as a live tree with status marks. One key or click jumps to the agent that needs you. |
| [**4242labs/herdr-radar-plus**](https://github.com/4242labs/herdr-radar-plus) | Sorts Herdr agents by what needs you, with named groups that span connected machines. Adds a model-family mark and a machine row under each agent on top of herdr-radar. |
| [**evanbryant/herdr-covr**](https://github.com/evanbryant/herdr-covr) | Replaces the Herdr sidebar with a compact Spaces and Agents list, one line per agent sorted by what needs you. A second line appears only when an agent is blocked or just finished, with light and dark layouts. |
| [**ZingerLittleBee/herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins) | Pins selected Herdr agent sessions to the top of the sidebar and restores their order across server restarts. |
| [**MrBogomips/herdr-tools**](https://github.com/MrBogomips/herdr-tools) | Sorts the spaces sidebar into top, default and bottom groups, gives every space of one customer the same colour (Space Herder), and names tabs after their folder, repo or branch (auto-tab-name). Also ships herdr-jump, a macOS menu bar picker that lists the agents waiting for you, blocked first and oldest wait first. |
| [**mashhoodr/herdr-space-sidebar**](https://github.com/mashhoodr/herdr-space-sidebar) | Merges Herdr's Spaces and Agents panels into one list with each agent nested under its space. Shows status symbols and session colors. |

**[All 45 projects →](catalog/06-worktrees-and-terminal.md#sidebar-grouping-ordering-and-filtering)**

### Sidebar badges, tokens, and status indicators

*88 projects. Plugins that add status icons, spinners, colors, model and CPU badges, PR and CI tokens, notes, and other per-row details to the sidebar and tab bar.*

| Project | What it does |
|---|---|
| [**robbyrussell/herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh) | Integrates Herdr with Oh My Zsh, displaying slow commands in the sidebar and triggering desktop completion notifications. |
| [**FlorisKr/herdr-openspec**](https://github.com/FlorisKr/herdr-openspec) | Shows OpenSpec change and task progress in the Herdr TUI sidebar and opens proposals, designs, and specs in a change browser. |
| [**eliasstravik/herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress) | Shows agent-reported task estimates and activity for Claude Code and Codex in the Herdr TUI sidebar. |
| [**wyattjoh/herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr) | Shows the GitHub pull-request number and CI state for the focused agent pane's branch in the Herdr sidebar. Updates are rate-limited, with shortcuts for manual refresh and opening the pull request. |
| [**bayoudhi/herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress) | Adds a live sidebar progress for slow shell commands, not just coding agents. |
| [**qintmb/herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui) | Adds larger agent icons, status glyphs, and a workspace, tab, and agent tree to the Herdr TUI sidebar. |
| [**testy-cool/herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config) | Adds a compact workspace, tab, and agent sidebar preset with provider icons to Herdr. |
| [**getpipher/herdr-sysmon**](https://github.com/getpipher/herdr-sysmon) | Adds CPU, memory, battery, network, and disk measurements to Herdr sidebar tokens, with configurable refresh intervals and macOS-focused probes. |
| [**Numbered-com/herdr-ports**](https://github.com/Numbered-com/herdr-ports) | Detects TCP listeners started by processes in each workspace and adds a dynamic `$ports` badge to the Herdr sidebar. |
| [**pdalinis/herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model) | Shows the active model and reasoning effort for Codex, Claude Code, Pi, and Hermes agents in the Herdr TUI sidebar. |

**[All 88 projects →](catalog/06-worktrees-and-terminal.md#sidebar-badges-tokens-and-status-indicators)**

### Status overlays, HUDs, and agent timers

*78 projects. Floating status HUDs, turn timers, and keep-awake utilities.*

| Project | What it does |
|---|---|
| [**aemrebarut/herdr-dagr**](https://github.com/aemrebarut/herdr-dagr) | Shows a live directed graph of an agent workflow inside a Herdr split. It reads a structured `run.json` file and displays tasks, retries, review gates, evidence levels, and progress history. |
| [**aigorahub/herdr-lantern**](https://github.com/aigorahub/herdr-lantern) | Shows which Herdr agents need attention and lets users jump to panes or start agents. |
| [**ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay) | Shows Linux CPU and memory use per Herdr workspace relative to total capacity. |
| [**Tyru5/herdr-floax**](https://github.com/Tyru5/herdr-floax) | A tmux-floax-style floating shell with one persistent scratch session per Herdr workspace. |
| [**jeffarese/herdr-agent-grid**](https://github.com/jeffarese/herdr-agent-grid) | Shows agents, subagents, messages, status, and API cost in a Herdr TUI panel and jumps to selected panes. |
| [**nikok6/herdr-pet**](https://github.com/nikok6/herdr-pet) | Displays an animated Codex-format pet on Herdr panes that reacts to agent activity and waiting states. |
| [**oronbz/visor · herdr**](https://github.com/oronbz/visor/tree/main/herdr) | Opens a configurable terminal dashboard over Herdr TUI tabs for GitHub pull requests, Jira issues, calendars, and other widgets. |
| [**maro114510/herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup) | Toggles a shell overlay above the current Herdr session for quick commands, notes, or plan inspection without rearranging panes. |
| [**natori-hrj/herdr-triage**](https://github.com/natori-hrj/herdr-triage) | Sorts active Herdr agents by how urgently they need attention. Blocked and stalled workers rise to the top based on their wait and idle time. |
| [**enes/herdr-monitoring**](https://github.com/enes/herdr-monitoring) | Shows CPU, memory and process trees for Herdr TUI agents in a summary popup or focused-pane monitor. |

**[All 78 projects →](catalog/06-worktrees-and-terminal.md#status-overlays-huds-and-agent-timers)**

### Context meters and rate-limit gauges

*90 projects. Live token headroom meters, quota tracking, and agent cost gauges.*

| Project | What it does |
|---|---|
| [**levi-qiao/herdr-agent-usage**](https://github.com/levi-qiao/herdr-agent-usage) | Shows model, context and subscription quota for coding agents in the Herdr TUI agent sidebar. |
| [**levi-qiao/herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota) | A sidebar quota monitor for Claude, Codex, Grok, and Agy that shows the percentage remaining in five-hour and weekly limits. |
| [**senna-lang/herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage) | Shows context meters and provider rate limits for agents running in Herdr. |
| [**pinkpixel-dev/quota · herdr-plugin**](https://github.com/pinkpixel-dev/quota/tree/main/herdr-plugin) | Shows per-pane AI provider usage in the Herdr TUI sidebar for accounts such as Claude Code and Codex. |
| [**Davidcreador/herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard) | Shows live token use and costs for Pi, OpenCode, Claude Code, and Codex in Herdr TUI, with completion notifications. |
| [**quaywin/agys**](https://github.com/quaywin/agys) | Isolates Antigravity account profiles in Herdr TUI panes and shows profile, context, and quota telemetry in the sidebar. |
| [**VHemanth45/herdr_agents_tracker**](https://github.com/VHemanth45/herdr_agents_tracker) | Tracks coding-agent subscription limits and per-agent context in Herdr TUI with usage alerts and a token dashboard. |
| [**oszypczy/herdr-claude-usage**](https://github.com/oszypczy/herdr-claude-usage) | Shows the focused Claude agent’s context, five-hour usage, and seven-day usage bars in the Herdr TUI sidebar. |
| [**speardragon/herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar) | Shows Claude Code, Codex, and Grok plan usage in the Herdr tab bar, with optional additional providers. |
| [**Mako-L/account-capacity-dock · herdr-plugin**](https://github.com/Mako-L/account-capacity-dock/tree/main/herdr-plugin) | Shows Claude, Codex and Cursor account capacity in a Herdr TUI widget and desktop dock. |

**[All 90 projects →](catalog/06-worktrees-and-terminal.md#context-meters-and-rate-limit-gauges)**

### Output inspection, logs, and transcripts

*67 projects. Tools for searching, cleaning, exporting, or reviewing pane output and agent conversations.*

| Project | What it does |
|---|---|
| [**furkankly/zoetrope · herdr-plugin**](https://github.com/furkankly/zoetrope/tree/main/herdr-plugin) | Shows Claude Code and Codex sessions as live flow graphs and opens the view beside a Herdr TUI pane. |
| [**rmarganti/herdr-pluck**](https://github.com/rmarganti/herdr-pluck) | Adds one- and two-letter hints for copyable terminal tokens, including URLs, paths, hashes, UUIDs, IP addresses, Kubernetes references, and hexadecimal values. |
| [**BjoernSchotte/agentglass**](https://github.com/BjoernSchotte/agentglass) | Monitors coding-agent sessions and lets you send prompts to Herdr TUI panes, jump to live agents, and resume sessions in new tabs. Shows Herdr agent states, approval waits, and workspace grouping. |
| [**hotchpotch/herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers) | Adds tmux-fingers-style labels to visible URLs, commit hashes, and file paths. Typing a short hint copies the selected token without using a mouse. |
| [**wilbeibi/herdr-catchup**](https://github.com/wilbeibi/herdr-catchup) | Transfers work between Claude Code, Codex, Cursor, Cline, and OpenCode sessions in Herdr. It captures and summarizes a live pane so another agent can continue or branch the task with useful context. |
| [**rsdlt/levi · herdr**](https://github.com/rsdlt/levi/tree/main/herdr) | Searches Git history and inserts a reference to a selected commit, file and lines into a Herdr TUI agent prompt. |
| [**youguanxinqing/herdr-flash**](https://github.com/youguanxinqing/herdr-flash) | Searches visible Herdr TUI pane text, jumps to a labeled match, and selects and yanks text with Vim motions. |
| [**AkashJana18/herdr-scratch**](https://github.com/AkashJana18/herdr-scratch) | Maintains persistent scratch panes that can be shown or hidden without losing shell, note, or REPL state. Scratch areas may be global, workspace-specific, or directory-specific. |
| [**hitaishi2222/herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers) | Copies paths, URLs, and other identifiers from the focused pane using keyboard hints. |
| [**bigsan/claude-deck**](https://github.com/bigsan/claude-deck) | Shows Claude Code sessions, scratchpad files, tasks and tool calls in a Herdr TUI viewer. |

**[All 67 projects →](catalog/06-worktrees-and-terminal.md#output-inspection-logs-and-transcripts)**

### Agent visualizations and terminal games

*34 projects. Interactive terminal visualizations and games for following agents.*

| Project | What it does |
|---|---|
| [**michaellandi/herdr-office**](https://github.com/michaellandi/herdr-office) | Draws Herdr TUI agents as office characters and signals when an agent needs approval. |
| [**aorumbayev/herdr-canvas**](https://github.com/aorumbayev/herdr-canvas) | Opens a mouse-driven ASCII diagram canvas in a Herdr split. Humans draw boxes, lines, and text; agents read and edit the same JSON-backed diagrams through the CLI and skill. |
| [**devangchhajed/herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office) | Shows Herdr TUI agents as pixel-art office characters that change activity with agent status and tool calls. |
| [**takemo101/wave-tui**](https://github.com/takemo101/wave-tui) | Plays internet radio in a terminal and visualizes Herdr TUI agents in an interactive Agent Planets view. |
| [**Efeguclu1/herdr-town**](https://github.com/Efeguclu1/herdr-town) | Renders Herdr coding agents as an interactive 8-bit town inside a pane and lets users read or answer them. |
| [**opsydyn/herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer) | Shows live Herdr TUI agents and their states as a 16-bit fantasy guild. |
| [**JYasha11/herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face) | Shows an increasingly urgent ASCII-art face when a Herdr agent is blocked and waiting for input, making overlooked approvals difficult to miss. |
| [**suisya-systems/herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office) | A terminal pixel-art office where Herdr agents appear as animated desk workers, blocked agents raise timed alerts, and selecting a character focuses its pane. |
| [**yuya-take/herdr-starkeep**](https://github.com/yuya-take/herdr-starkeep) | Draws the agents running in Herdr as knights on an orbital training ship, with one room per space and subagents shown as apprentices. Reads agent state from the Herdr socket and subagent events from a Claude Code hook. |
| [**pvgomes/agent-visualizer**](https://github.com/pvgomes/agent-visualizer) | Shows coding agents as workers in a pixel-art office, one desk per agent. In herd mode the office lists the agents in Herdr panes, poses them by Herdr state, and can open or start agents in Herdr workspaces. |

**[All 34 projects →](catalog/06-worktrees-and-terminal.md#agent-visualizations-and-terminal-games)**

### Herdr TUI themes and appearance

*19 projects. Themes and visual customizations for the Herdr TUI.*

| Project | What it does |
|---|---|
| [**qintmb/herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker) | Applies terminalcolors.com palettes to Herdr TUI interface elements through a popup theme picker. |
| [**promptegrity/grok-themes · herdr**](https://github.com/promptegrity/grok-themes/tree/HEAD/herdr) | Applies GrokNight or GrokDay colors to the Herdr TUI and adds an optional powerline-style branch indicator. |
| [**ariel-ps/herdr-colors**](https://github.com/ariel-ps/herdr-colors) | Assigns distinct color slots to Herdr TUI panes and can repaint existing panes. |
| [**magimetal/matrix-themes · herdr**](https://github.com/magimetal/matrix-themes/tree/HEAD/herdr) | Applies a Matrix-inspired green palette to the Herdr TUI using a configuration snippet. |
| [**AkashJana18/zenbones-herdr**](https://github.com/AkashJana18/zenbones-herdr) | Adds 23 zenbones color themes with light and dark variants to Herdr TUI. |
| [**s3rgiosan/herdr-theme-synthwave-84**](https://github.com/s3rgiosan/herdr-theme-synthwave-84) | Applies the Synthwave '84 neon palette to the Herdr TUI by writing theme tables to config.toml after backing up your previous theme. |
| [**nertzy/herdr-flexoki**](https://github.com/nertzy/herdr-flexoki) | Adds Flexoki light and dark themes to Herdr TUI, including an automatic appearance option. |
| [**sp-night/herdr**](https://github.com/sp-night/herdr) | Adds three São Paulo-inspired dark color palettes to Herdr TUI. |
| [**codingquark/herdr-modus-themes**](https://github.com/codingquark/herdr-modus-themes) | Installs the light Modus Operandi and dark Modus Vivendi palettes for the Herdr TUI. |
| [**Young1108/herdr-cyber-style**](https://github.com/Young1108/herdr-cyber-style) | Applies a dark cyber theme and workspace layout to Herdr TUI on macOS, with a backup of the previous configuration. |

**[All 19 projects →](catalog/06-worktrees-and-terminal.md#herdr-tui-themes-and-appearance)**

### Security guards and collision detectors

*21 projects. Safety monitors that warn of worktree collisions, credential leaks, or destructive edits.*

| Project | What it does |
|---|---|
| [**termaxa/termaxa · herdr-plugin**](https://github.com/termaxa/termaxa/tree/main/herdr-plugin) | Runs Claude Code or Codex under Termaxa command policies in Herdr TUI and shows refusals and audit records. |
| [**schemaitat/herdr-nono-plugin**](https://github.com/schemaitat/herdr-nono-plugin) | Runs OpenCode in nono sandboxes from Herdr TUI on Linux, with separate client and server profiles. |
| [**mcc0x/herdr-redact**](https://github.com/mcc0x/herdr-redact) | Warns when an agent pane has printed credentials before screenshots, streaming, or chat paste operations occur. |
| [**StructuPath/herdr-guard**](https://github.com/StructuPath/herdr-guard) | Monitors Herdr TUI panes for configured command-policy violations and can interrupt matching commands. An optional Claude Code hook checks tool calls before execution. |
| [**mcc0x/herdr-collide**](https://github.com/mcc0x/herdr-collide) | Warns when agents working in separate Git worktrees of the same repository are about to collide or conflict. |
| [**asumaran/asconfirmclose**](https://github.com/asumaran/asconfirmclose) | Closes an idle Herdr TUI pane immediately but asks for confirmation when a foreground process is running. |
| [**zenodea/fence**](https://github.com/zenodea/fence) | Turns a Herdr TUI space into a sandboxed pen where every shell can write only the pen folder and reach allowed domains. Uses bubblewrap and nftables on Linux. |
| [**IniZio/nexus · plugins/herdr**](https://github.com/IniZio/nexus/tree/main/plugins/herdr) | Attaches Herdr TUI to nexus microVM sandboxes, listing and creating them from the plugin, with auto port forwarding. Sandboxes are Cloud Hypervisor VMs on Linux with credentials kept on the host. |
| [**pauljohnchamberlain/herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard) | Lets coding agents inspect Herdr TUI sessions and make guarded workspace renames or close eligible inactive work. |
| [**cheunglok97/close-guard**](https://github.com/cheunglok97/close-guard) | Asks for confirmation before closing a Herdr TUI tab or pane. |

**[All 21 projects →](catalog/06-worktrees-and-terminal.md#security-guards-and-collision-detectors)**

### Plugin collections, frameworks, and ready-made configs

*49 projects. Plugin bundles, shared libraries for plugin authors, and ready-made Herdr configurations to install and adapt.*

| Project | What it does |
|---|---|
| [**ogulcancelik/herdr-plugin-examples**](https://github.com/ogulcancelik/herdr-plugin-examples) | Shows standalone Herdr TUI plugin examples for Telegram notifications, development layouts, GitHub link previews, and Rust release checks. |
| [**ythx-101/herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass) | Applies macOS workspace presets and a workflow plugin for a translucent Herdr TUI workspace. |
| [**MIDO-ruby7/herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory) | A directory of Herdr plugins organized by the task a user wants to accomplish. |
| [**choplin/herdr-plugins**](https://github.com/choplin/herdr-plugins) | Collects Herdr TUI plugins for agent metadata, agent navigation, text selection, repository identity, and pane splitting as Git submodules. |
| [**Phoobobo/herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager) | Inventories and manages skills, MCP servers, plugins and hooks across agent configuration directories from a Herdr TUI plugin or CLI. |
| [**vonzelle-vzt/herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions) | Installs a complete 13-panel developer environment inside Herdr for diagnostics, language-server completion, tests, and in-terminal agent diff review. |
| [**JJLiebig/herdr-plugins**](https://github.com/JJLiebig/herdr-plugins) | Collects Herdr TUI plugins for GitHub status, cache timing, worktree discovery, agent dispatch and Stream Deck controls. |
| [**vika2603/herdr-plugin-manager**](https://github.com/vika2603/herdr-plugin-manager) | Browses the Herdr TUI plugin marketplace and installs, enables, disables, and updates plugins from a popup or CLI. |
| [**Newt6611/herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust) | Builds Herdr TUI plugins in Rust with application state, configuration, event handlers, and a socket client. |
| [**JacobAtchley/herdr-plugins**](https://github.com/JacobAtchley/herdr-plugins) | Collects Herdr TUI plugins for agent inboxes, command palettes, Git views, project running and zen mode. |

**[All 49 projects →](catalog/06-worktrees-and-terminal.md#plugin-collections-frameworks-and-ready-made-configs)**

---

## 7. Apps, companion integrations, and installation

*491 projects. Native applications, web dashboards, hardware companions, supporting utilities, and setup packages.* The top 10 of each subcategory by stars are below; the full list is in [catalog/07-apps-and-installation.md](catalog/07-apps-and-installation.md).

### Native desktop and mobile apps

*126 projects. Installed applications and launchers that provide a native interface to Herdr on desktop or mobile operating systems.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | What it does |
|---|---|
| [**sheprd-labs/sheprd**](https://github.com/sheprd-labs/sheprd) | Opens Herdr TUI and herdr-core terminal sessions in a native desktop client. |
| [**ZingerLittleBee/Heeler**](https://github.com/ZingerLittleBee/Heeler) | Supervises Herdr agents from an iOS console with SSH terminals, QR pairing, and push notifications. |
| [**missuo/herdrm**](https://github.com/missuo/herdrm) | Adds a native macOS console for Herdr to drive coding agents and monitor live terminals across devices. |
| [**themartianapp/herdrup**](https://github.com/themartianapp/herdrup) | Monitors Herdr TUI agents and opens their terminals from an iOS app. |
| [**kosumic/whip**](https://github.com/kosumic/whip) | Connects mobile devices to Herdr as an agent-native SSH client designed specifically for multiplexer workflows. |
| [**kenn-io/ghosthub**](https://github.com/kenn-io/ghosthub) | Opens local and SSH-hosted Herdr TUI, tmux, and Zellij sessions in a native macOS terminal with worktree creation. |
| [**benkraus/herdr-mobile**](https://github.com/benkraus/herdr-mobile) | Controls Herdr TUI sessions from iOS or Android through a separately deployed relay. |
| [**cobanov/herdrchat**](https://github.com/cobanov/herdrchat) | Controls Herdr coding agents from an iPhone or iPad. |
| [**minchenlee/flockbook**](https://github.com/minchenlee/flockbook) | Shows agent conversations in a native macOS app or Herdr app layout and lets users answer prompts. |
| [**sisyphuslabs/doriterm**](https://github.com/sisyphuslabs/doriterm) | Connects desktop, browser and phone clients to herdr-core terminals across an encrypted machine mesh. |

**[All 126 projects →](catalog/07-apps-and-installation.md#native-desktop-and-mobile-apps)**

### Web dashboards and remote viewers

*127 projects. Browser-based monitors, remote controls, and visual scenes for following Herdr agents from another screen or device.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | What it does |
|---|---|
| [**devswha/ovis**](https://github.com/devswha/ovis) | Shows Herdr agent transcripts and terminals in a desktop or phone browser, with approval cards and SSH connections. |
| [**AltanS/collie**](https://github.com/AltanS/collie) | Shows terminal agents in a phone web app and lets users answer them remotely. |
| [**dcolinmorgan/herdr-remote**](https://github.com/dcolinmorgan/herdr-remote) | Monitors and controls Herdr agents through a macOS menu bar, phone dashboard, and Telegram. |
| [**0cv/herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay) | Combines Herdr agents from multiple machines in an installable phone web app. |
| [**powerfooI/roamgate**](https://github.com/powerfooI/roamgate) | Adds a web client for Herdr with mobile optimization, browser terminals, workspace management, and session inspection. |
| [**arronKler/pairfob**](https://github.com/arronKler/pairfob) | Opens paired Herdr agent sessions from a phone or browser, with optional Android access. |
| [**kcosr/herdr-web**](https://github.com/kcosr/herdr-web) | Monitors and controls Herdr TUI workspaces and terminal panes from a desktop or mobile browser. |
| [**lamngockhuong/termote**](https://github.com/lamngockhuong/termote) | Streams Herdr TUI or herdr-core sessions to a self-hosted browser and mobile PWA, with a TUI plugin for opening and sharing panes. |
| [**ragamo/herdr-flock**](https://github.com/ragamo/herdr-flock) | Represents active Herdr agents as animated sheep and records completed sessions in a persistent graveyard log. |
| [**alecuba16/herdr-webui**](https://github.com/alecuba16/herdr-webui) | Browses Herdr-compatible workspaces, terminals, worktrees, and Git operations in a web UI. |

**[All 127 projects →](catalog/07-apps-and-installation.md#web-dashboards-and-remote-viewers)**

### Hardware and ambient displays

*47 projects. Keypads, watches, desk devices, and compact displays that turn agent state into physical controls or at-a-glance signals.*

| Project | What it does |
|---|---|
| [**timvdhoorn/stream-deck-herdr-plugin**](https://github.com/timvdhoorn/stream-deck-herdr-plugin) | Assigns a key to each agent, displays its state with a color and icon, and focuses the matching Herdr pane when pressed. |
| [**Unayung/herdr-watch**](https://github.com/Unayung/herdr-watch) | A native Apple Watch companion that shows Herdr agent activity and alerts the wearer when an agent finishes or needs input. |
| [**spencerbull/xeneon-edge-agents**](https://github.com/spencerbull/xeneon-edge-agents) | An Omarchy and Herdr agent command center designed for the Corsair XENEON EDGE display, with conservative handling when state cannot be confirmed. |
| [**walcew/herdr-assist**](https://github.com/walcew/herdr-assist) | An ESP32-S3 desk display that shows Herdr session states and sounds a bell when an agent is waiting for a decision or approval. |
| [**mrshu/muxboard**](https://github.com/mrshu/muxboard) | Shows Herdr agent attention status and CodexBar usage metrics on a Stream Deck+ dashboard. |
| [**alasano/house-of-herdr**](https://github.com/alasano/house-of-herdr) | Maps Herdr TUI agent status and controls to the Work Louder Codex Micro keypad, dial, and joystick. |
| [**finna/omarchy-herdr-hud**](https://github.com/finna/omarchy-herdr-hud) | Monitors and prompts Herdr agents from a draggable Omarchy overlay. |
| [**niklasberglund/herdr-logi-plugin**](https://github.com/niklasberglund/herdr-logi-plugin) | Shows Herdr TUI workspace and agent status on a Logitech MX Keypad and focuses a selected pane on keypress. |
| [**Resilient-Software/herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck) | Mirrors Herdr TUI workspaces to a Stream Deck with repository, branch and agent-status tiles. |
| [**fedeya/corral**](https://github.com/fedeya/corral) | Shows Herdr TUI agents as animated critters on a Stream Deck Plus and focuses an agent when its key is tapped. |

**[All 47 projects →](catalog/07-apps-and-installation.md#hardware-and-ambient-displays)**

### Processes, ports, sandboxes, and remote machines

*28 projects. Tools for watching and stopping dev servers and listening ports, cleaning up leftover processes, and running agents or shells in sandboxes, VMs, containers, and remote hosts.*

| Project | What it does |
|---|---|
| [**dirien/herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin) | Runs Claude Code, Codex, Gemini CLI, and other coding agents in separate Docker Sandboxes from Herdr TUI. |
| [**sudoeren/herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker) | Runs lazydocker in a herdr split pane or its own tab. |
| [**dvdksn/sbx-herdr**](https://github.com/dvdksn/sbx-herdr) | Registers Docker Sandboxes as Herdr TUI SSH machines and identifies sandbox agents in local panes. |
| [**carze/herdr-smolmachine**](https://github.com/carze/herdr-smolmachine) | Starts coding agents in libkrun or KVM microVMs from Herdr panes and lists running sandboxes. |
| [**ivorpad/herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel) | Lists local listening ports and opens, copies, or stops public tunnels from a Herdr TUI pane. |
| [**ivorpad/herdr-ports**](https://github.com/ivorpad/herdr-ports) | Adds a popup that lists listening ports, names the project behind each one, and kills or opens it. |
| [**AZenking/herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center) | Adds a Herdr popup for monitoring and focusing local Node.js, Bun, and Deno services. |
| [**Slimydog21/herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm) | Controls an existing NixOS development VM from a Herdr TUI pane, including boot, stop, monitoring, and SSH. |
| [**abcxff/herdr-docker**](https://github.com/abcxff/herdr-docker) | Keeps track of docker builds like you do with agents for herdr. |
| [**Keepstateai/cli · herdr**](https://github.com/Keepstateai/cli/tree/main/herdr) | Shows KeepState sessions, agents, saved points and Cruise receipts in Herdr panes through the ks client. Sends a Herdr notification when a Cruise job finishes. |

**[All 28 projects →](catalog/07-apps-and-installation.md#processes-ports-sandboxes-and-remote-machines)**

### Agent support, auto-approve, retry, and keep-awake helpers

*20 projects. Add-ons that teach Herdr about extra coding agents, auto-approve or auto-continue stalled agents after rate limits, and keep the machine awake while agents work.*

| Project | What it does |
|---|---|
| [**mo-arvan/herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry) | Detects Claude Code stalls caused by rate limits or server errors and safely resumes only idle or blocked panes, leaving actively working agents untouched. |
| [**scrappylabsai/podr**](https://github.com/scrappylabsai/podr) | Adds Reasonix and DeepSeek Harness detection to a Herdr TUI fork and includes a client for attaching to DSH sessions. |
| [**XiangQhello/codex-claude-auto-enter**](https://github.com/XiangQhello/codex-claude-auto-enter) | Sends repeated Enter presses to a selected Herdr TUI pane and stops when Codex or Claude Code becomes idle. |
| [**RenKoya1/herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all) | Approves every pending agent permission request in Herdr with one keystroke. |
| [**gw31415/herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos) | Watches Herdr agent-status events and keeps an Amphetamine session active while agents are working, preventing sleep during long tasks. |
| [**bestony/herdr-codex-capacity-retry**](https://github.com/bestony/herdr-codex-capacity-retry) | Automatically continues Codex sessions in Herdr after capacity-related interruptions. |
| [**susomejias/herdr-awake**](https://github.com/susomejias/herdr-awake) | Keeps the machine awake while Herdr agents are busy. |
| [**ichadhr/herdr-zcode**](https://github.com/ichadhr/herdr-zcode) | Adds ZCode agent support to Herdr TUI, showing zcode panes in the sidebar with live working, blocked, and idle state. Registers hooks in the zcode settings file. |
| [**jaaacki/herdr-plugin-minimax-code**](https://github.com/jaaacki/herdr-plugin-minimax-code) | Adds MiniMax Code support to Herdr TUI by launching mcode in a new pane and registering hand-started mcode sessions so they appear as agents. |
| [**jewei/herdr-caffeinated**](https://github.com/jewei/herdr-caffeinated) | Keeps a Mac awake with caffeinate while a Herdr agent works and lets it sleep after 60 idle seconds. A pause action turns it off. |

**[All 20 projects →](catalog/07-apps-and-installation.md#agent-support-auto-approve-retry-and-keep-awake-helpers)**

### Notes, prompts, clipboard, and file helpers

*32 projects. Per-tab scratchpads and notes, saved prompt decks, task lists, credential pickers, clipboard and image paste, and file transfer or reveal helpers for Herdr panes.*

| Project | What it does |
|---|---|
| [**Resetnak/herdr-logbook**](https://github.com/Resetnak/herdr-logbook) | Manages Markdown tasks and decisions in an offline notebook for Herdr workspaces. |
| [**vjeantet/herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad) | Docks a plain-text scratchpad at the bottom of a tab, one persistent buffer per tab, for composing a prompt where Enter can't send it half-finished. `Ctrl+E` moves it, or just the selection, into an agent of the same tab without submitting; `Ctrl+C` copies over OSC 52. |
| [**kosuketut/herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder) | Downloads files created or changed in a remote Herdr pane to a local Mac. A plugin action detects paths in the active pane and transfers the selected artifact over the remote connection. |
| [**ddfonseca/herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image) | Saves an image from the macOS or Linux clipboard to disk and pastes its file path into the active pane for use by multimodal agents. |
| [**mrolafsson/herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer) | Transfers files between a local machine and a remote Herdr TUI host over SSH and sends their paths to agents. |
| [**ivolkoff/herdr-huddle**](https://github.com/ivolkoff/herdr-huddle) | Opens rich questions over a Herdr TUI agent pane and returns the answers to the agent as JSON. |
| [**mdetweil/herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask) | Opens Lazytask in a Herdr TUI split or tab and adds Taskwarrior quick actions. |
| [**WillowMist/herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden) | Searches a Bitwarden vault from a Herdr TUI popup and copies or pastes selected credentials. |
| [**chrisg32/tsk**](https://github.com/chrisg32/tsk) | Manages plain-text tasks in a Rust TUI that runs standalone or as a Herdr plugin. |
| [**niceview/mac-finder-quick-actions**](https://github.com/niceview/mac-finder-quick-actions) | Opens Finder selections in VS Code or a new Herdr TUI workspace through macOS quick actions and a drag-and-drop launcher. |

**[All 32 projects →](catalog/07-apps-and-installation.md#notes-prompts-clipboard-and-file-helpers)**

### Developer tool panes and everyday utilities

*56 projects. Panes that open database, API, CI, Git, and cloud clients, plus translators, media players, calendars, feeds, and other everyday utilities beside your agents.*

| Project | What it does |
|---|---|
| [**coryshaw1/herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp) | Opens the cliamp audio player in a floating Herdr TUI pane while playback continues in a detached session. |
| [**pivoshenko/musicforprogramming · plugins/herdr/mfp.player**](https://github.com/pivoshenko/musicforprogramming/tree/main/plugins/herdr/mfp.player) | Opens the musicforprogramming.net player in a Herdr TUI pane and maps playback controls to actions. |
| [**ablause/herdr-flutter**](https://github.com/ablause/herdr-flutter) | A Herdr sidebar for watching, hot-reloading, and inspecting a running Flutter app beside the coding agent working on it. |
| [**Tomatio13/herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail) | Browses Gmail in a Herdr TUI split using fzf and gogcli, with mail actions and background notifications. |
| [**RizRiyz/pixtui**](https://github.com/RizRiyz/pixtui) | Opens a terminal pixel-art editor in a Herdr TUI pane with layers, animation, and PNG or GIF export. |
| [**Javamomma/herdr-scribe**](https://github.com/Javamomma/herdr-scribe) | Streams microphone audio to temporary panes and creates meeting notes, policy checks, and draft tickets without saving raw audio. |
| [**neospeed83/herdr-standup**](https://github.com/neospeed83/herdr-standup) | Builds a daily standup from Git commits and optional notes, then opens the report from a Herdr TUI workspace. |
| [**Tomatio13/herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar) | Browses Google Calendar events in an fzf panel and creates a Herdr TUI worktree and workspace from an event. |
| [**arhen/devnull-tui**](https://github.com/arhen/devnull-tui) | Reads the /dev/null developer commit network in a Herdr TUI pane with a feed, threads, replies, stars and an inbox, and opens links in a Herdr browser tab. Also runs as a standalone terminal client. |
| [**wazum/herdr-polyglot**](https://github.com/wazum/herdr-polyglot) | Translates prompts into English before sending them to an agent pane in Herdr. |

**[All 56 projects →](catalog/07-apps-and-installation.md#developer-tool-panes-and-everyday-utilities)**

### Setup, packages, and version management

*55 projects. Guides, configuration bundles, installers, package definitions, and tools for reproducible Herdr environments.*

| Project | What it does |
|---|---|
| [**speardragon/herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager) | A small in-terminal menu for browsing, installing, updating, enabling, and disabling Herdr plugins through the standard plugin command-line interface. |
| [**mifunedev/agro**](https://github.com/mifunedev/agro) | Runs Herdr inside a Docker workspace for coding agents on a laptop or remote VM, installed with `agro tool install herdr`. Parallel agents use separate git worktrees, work continues after the terminal disconnects, and you choose the harness: Claude Code, Codex, Pi, OpenCode, or T3 Code. |
| [**joeseesun/herdr-guide**](https://github.com/joeseesun/herdr-guide) | A Chinese-language practical guide that explains what Herdr is useful for and how to get started. |
| [**natori-hrj/herdr-lazy**](https://github.com/natori-hrj/herdr-lazy) | A declarative Herdr plugin manager with a dedicated terminal interface, a lockfile, version pinning, synchronization from one list, and support for prebuilt binaries. |
| [**Yassimba/loom**](https://github.com/Yassimba/loom) | A curated collection of agent skills, Pi packages, and Herdr plugins with a single command-line setup tool. |
| [**diegopzz/herdr-updater**](https://github.com/diegopzz/herdr-updater) | Keeps Herdr and its plugins current across a whole fleet, safely. |
| [**garavitgabriel/claude-remote-kit**](https://github.com/garavitgabriel/claude-remote-kit) | Sets up Herdr, Tailscale, and Termius for remotely accessing coding agent sessions from a phone. |
| [**pedrogiroldo/agentbox**](https://github.com/pedrogiroldo/agentbox) | Runs Herdr, Claude Code, Codex, OpenCode, and mobile-friendly Neovim in an Ubuntu container reachable over SSH. |
| [**ram4-dev/herdr-config**](https://github.com/ram4-dev/herdr-config) | Installs pinned Herdr TUI plugins and portable keybindings with configuration snapshots and rollback. |
| [**hdosys/herdr-sandbox**](https://github.com/hdosys/herdr-sandbox) | Runs coding agents in disposable Windows Sandbox workstations isolated from the host. |

**[All 55 projects →](catalog/07-apps-and-installation.md#setup-packages-and-version-management)**

---

## 8. Experimental projects

*10 projects. Experimental Herdr projects and prototypes.* The top 10 of each subcategory by stars are below; the full list is in [catalog/08-experimental.md](catalog/08-experimental.md).

### Experiments, concepts, and scaffolds

*10 projects. Ideas and prototypes that are useful to study but may be incomplete, read-only, or not yet installable.*

| Project | What it does |
|---|---|
| [**eliasstravik/herdr-call**](https://github.com/eliasstravik/herdr-call) | An early TypeScript prototype for translating spoken commands into Herdr navigation and input through the local socket. |
| [**wraithyy/herdr-openr**](https://github.com/wraithyy/herdr-openr) | Extracts file paths and URLs from recent pane output and Claude Code transcripts, then presents them in a fuzzy finder for quick opening. |
| [**hmu332233/herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs) | An experimental plugin laboratory containing early prototypes for agent launching, workspace metrics, and worktree symlinking before they move into separate projects. |
| [**rohanthewiz/herdr-web**](https://github.com/rohanthewiz/herdr-web) | Renders Herdr pane frames with color, mouse, clipboard, and hyperlink support; keyboard and paste input are currently disabled, so it mainly works as a viewer. |
| [**shoaibkhanz/herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus) | An early navigation plugin designed to move with Ctrl+h/j/k/l across Herdr panes and wrap at workspace boundaries. |
| [**ugurtarlig/herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker) | An early pane-picker prototype that overlays one-character hints on visible panes for direct keyboard focus. |
| [**speardragon/herdr-labs**](https://github.com/speardragon/herdr-labs) | Provides herdr plugin lab, AI-agent plugin idea contests: 9 agents compete, AI judges score. |
| [**malone-c/herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer) | An in-development layout manager that automatically rebalances pane sizes when splits are opened or closed, reducing cramped nested layouts. |
| [**robinbraemer/herdr-axi**](https://github.com/robinbraemer/herdr-axi) | An early command-line interface designed to make Herdr workspace operations easier for coding agents to use. |
| [**yoshimi-I/gengar.nvim**](https://github.com/yoshimi-I/gengar.nvim) | An early Neovim environment that keeps agents and Hunk-based diff review in Herdr while leaving Neovim focused on editing. |

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
