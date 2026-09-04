# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of tools built for **[Herdr](https://herdr.dev/)**, the terminal-native agent multiplexer.

Official links: [Website](https://herdr.dev/) · [GitHub](https://github.com/ogulcancelik/herdr) · [Documentation](https://herdr.dev/docs/) · [Plugin Marketplace](https://herdr.dev/plugins/) · [Agent Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) · [Socket API](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md)

---

## Contents

1. [Run and orchestrate agents (157)](#1-run-and-orchestrate-agents)
   - [Official skill and foundation (1)](#official-skill-and-foundation)
   - [Multi-agent fleets and supervisors (20)](#multi-agent-fleets-and-supervisors)
   - [Claude Code multi-agent teams (19)](#claude-code-multi-agent-teams)
   - [Pi supervisor workflows and extensions (13)](#pi-supervisor-workflows-and-extensions)
   - [Subagent launchers and delegation (39)](#subagent-launchers-and-delegation)
   - [Autonomous coding and pull-request loops (10)](#autonomous-coding-and-pull-request-loops)
   - [Task queues, backlogs, and event triggers (6)](#task-queues-backlogs-and-event-triggers)
   - [General workflows and skill packs (49)](#general-workflows-and-skill-packs)
2. [Connect through MCP and the socket API (106)](#2-connect-through-mcp-and-the-socket-api)
   - [MCP servers (6)](#mcp-servers)
   - [Socket API clients and SDKs (54)](#socket-api-clients-and-sdks)
   - [Chat alerts: Telegram, Discord, and Slack (14)](#chat-alerts-telegram-discord-and-slack)
   - [Desktop, mobile, and webhook notifications (13)](#desktop-mobile-and-webhook-notifications)
   - [Telemetry, events, and quota streaming (7)](#telemetry-events-and-quota-streaming)
   - [Voice, hardware, and remote bridges (1)](#voice-hardware-and-remote-bridges)
   - [Protocol and third-party bridges (11)](#protocol-and-third-party-bridges)
3. [Editor integrations (54)](#3-editor-integrations)
   - [Neovim navigation and splits (30)](#neovim-navigation-and-splits)
   - [Full Neovim-hosted workspaces (1)](#full-neovim-hosted-workspaces)
   - [VS Code, Cursor, and dev containers (9)](#vs-code-cursor-and-dev-containers)
   - [Vim, Kakoune, and other editors (11)](#vim-kakoune-and-other-editors)
   - [REPL and code dispatchers (1)](#repl-and-code-dispatchers)
   - [Editor plugins and bridges (2)](#editor-plugins-and-bridges)
4. [Switch and restore sessions (64)](#4-switch-and-restore-sessions)
   - [Fuzzy session switchers and terminal pickers (46)](#fuzzy-session-switchers-and-terminal-pickers)
   - [Persistence, snapshots, and state restoration (11)](#persistence-snapshots-and-state-restoration)
   - [Workspace and multi-session management (7)](#workspace-and-multi-session-management)
5. [Worktrees and terminal experience (360)](#5-worktrees-and-terminal-experience)
   - [Git worktree automation (99)](#git-worktree-automation)
   - [Workspace lifecycle and multi-repository tools (4)](#workspace-lifecycle-and-multi-repository-tools)
   - [Diff review and code inspection (21)](#diff-review-and-code-inspection)
   - [File viewers and markdown previews (19)](#file-viewers-and-markdown-previews)
   - [Pane navigation and overlay hints (12)](#pane-navigation-and-overlay-hints)
   - [Terminal keybindings and shortcut helpers (81)](#terminal-keybindings-and-shortcut-helpers)
   - [Command palettes and workspace switchers (14)](#command-palettes-and-workspace-switchers)
   - [Status lines, sidebars, and tab synchronization (70)](#status-lines-sidebars-and-tab-synchronization)
   - [Status overlays, HUDs, and agent timers (15)](#status-overlays-huds-and-agent-timers)
   - [Context meters and rate-limit gauges (7)](#context-meters-and-rate-limit-gauges)
   - [Output inspection, logs, and transcripts (9)](#output-inspection-logs-and-transcripts)
   - [Dotfiles and ready-made configuration (6)](#dotfiles-and-ready-made-configuration)
   - [Plugin collections and developer frameworks (3)](#plugin-collections-and-developer-frameworks)
6. [Apps, companion integrations, and installation (75)](#6-apps-companion-integrations-and-installation)
   - [Native desktop and mobile apps (11)](#native-desktop-and-mobile-apps)
   - [Web dashboards and remote viewers (16)](#web-dashboards-and-remote-viewers)
   - [Hardware and ambient displays (12)](#hardware-and-ambient-displays)
   - [Plugins and supporting utilities (27)](#plugins-and-supporting-utilities)
   - [Setup, packages, and version management (9)](#setup-packages-and-version-management)
7. [Experimental projects (12)](#7-experimental-projects)
   - [Experiments, concepts, and scaffolds (12)](#experiments-concepts-and-scaffolds)
8. [Resources](#resources)
9. [Reference](#reference)

---

## 1. Run and orchestrate agents

*157 projects. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.*

### Official skill and foundation

*1 project. The official instructions that teach an agent how to understand and control Herdr.**

| Project | What it does |
|---|---|
| [**ogulcancelik/herdr · SKILL.md**](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) | Teaches an agent inside a Herdr pane how to inspect workspaces, tabs, and panes, start helpers, send input, and wait for status changes. |

### Multi-agent fleets and supervisors

*20 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*

| Project | What it does |
|---|---|
| [**aemrebarut/herdr-dagr**](https://github.com/aemrebarut/herdr-dagr) | Shows a live directed graph of an agent workflow inside a Herdr split. It reads a structured `run.json` file and displays tasks, retries, review gates, evidence levels, and progress history. |
| [**aorumbayev/herdr-workflows**](https://github.com/aorumbayev/herdr-workflows) | Runs repeatable development and agent workflows from YAML files. Each manifest defines an ordered sequence of commands and agent interactions to execute inside Herdr workspaces. |
| [**StructuPath/herdr-browser**](https://github.com/StructuPath/herdr-browser) | Renders an interactive Chromium browser inside a Herdr pane with Playwright automation and manual control. |
| [**natori-hrj/herdr-triage**](https://github.com/natori-hrj/herdr-triage) | Sorts active Herdr agents by how urgently they need attention. Blocked and stalled workers rise to the top based on their wait and idle time. |
| [**StructuPath/herdr-swarm**](https://github.com/StructuPath/herdr-swarm) | Runs several coding agents in parallel, each with its own branch, worktree, and Herdr pane, making it easy to watch competing implementations, compare changes, and keep the strongest result. |
| [**aashishd/herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger) | Defines a small messaging protocol for agents in separate Herdr panes. Peers use memorable call signs and exchange focused one-line messages, allowing coordination without sharing complete session histories. |
| [**voodootikigod/adlc-herdr**](https://github.com/voodootikigod/adlc-herdr) | Adds Agentic Development Lifecycle gates into Herdr. It shows ticket states, per-pane phases, and backlog boards, and provides actions for unblocking controlled milestones. |
| [**tomoasleep/herdr-symphony**](https://github.com/tomoasleep/herdr-symphony) | Reads issues from GitHub Projects, creates `gwq` worktrees, and runs one OpenCode agent per issue inside Herdr workspaces. |
| [**bredebjorhovd/herdr-board**](https://github.com/bredebjorhovd/herdr-board) | Assigns GitHub issues to agents in dedicated Herdr panes and moves completed work into pull-request review. |
| [**kay-ws/herdr-island**](https://github.com/kay-ws/herdr-island) | Filters Herdr's agent view to show only workers that are blocked or waiting for human input. It also reports the reason each agent stopped, making large fleets easier to triage. |
| [**natori-hrj/herdr-standup**](https://github.com/natori-hrj/herdr-standup) | Builds a stand-up summary from recent commits and uncommitted changes across active agent workspaces. It provides one view of completed and ongoing work without opening every repository. |
| [**steig/worktender**](https://github.com/steig/worktender) | Creates an isolated Git worktree and Herdr agent session for a GitHub issue. One command handles the branch, worktree, agent launch, and final cleanup. |
| [**StructuPath/herdr-conductor**](https://github.com/StructuPath/herdr-conductor) | Coordinates producer and reviewer agents with strict task and report formats, Git compare-and-swap checks, and a passive status board. It is designed for visible, operator-supervised delivery rather than free-form swarming. |
| [**zhenyufu/herdr-cadence**](https://github.com/zhenyufu/herdr-cadence) | Uses a lead agent to sort tasks and start specialized workers in separate Herdr tabs and Git worktrees. It checks for a clean repository state and gives each worker only the context it needs. |
| [**misty-step/kelpie**](https://github.com/misty-step/kelpie) | Provides a phone-first mobile console for checking and triaging OMP coding agents in Herdr workspaces. |
| [**cowcow02/herdr-agent-orchestrator**](https://github.com/cowcow02/herdr-agent-orchestrator) | Adds event-driven orchestration around one existing controller agent while Herdr observes and reports the work. It avoids replacing the controller with a separate fleet manager. |
| [**mikeyobrien/herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles) | Provides a data-driven command-line harness and reusable model profiles for agents running through Herdr. |
| [**persinac/agents-nexus**](https://github.com/persinac/agents-nexus) | Operates agent fleets on Herdr with runtime components, plugins, memory and observability tools, and conductor missions. |
| [**kyokosawada/viu**](https://github.com/kyokosawada/viu) | Lets developers monitor Herdr agent fleets and respond to workers by voice or keyboard from a mobile phone. |
| [**hewel/herdr-harness-coordinator**](https://github.com/hewel/herdr-harness-coordinator) | Coordinates autonomous coding-agent harnesses across separate Herdr panes and tracks their active tasks. |

### Claude Code multi-agent teams

*19 projects. Adapters and skills that organize Claude Code sessions into structured teams.*

| Project | What it does |
|---|---|
| [**richardadonnell/herdr-claude-manager**](https://github.com/richardadonnell/herdr-claude-manager) | Tiles and manages an N-agent grid of labeled Claude Code panes on Windows and macOS, with menu commands to list, resume, and stop workspaces. |
| [**caioniehues/herdmates**](https://github.com/caioniehues/herdmates) | Runs Claude Code multi-agent teams in Herdr through a teammux translation layer. Teammates work in isolated panes while a mission-control view reports their status and task progress. |
| [**erwins-enkel/shepherd**](https://github.com/erwins-enkel/shepherd) | Hosts a browser and mobile control panel for parallel Claude Code or Codex sessions in isolated worktree panes. |
| [**vinicius91carvalho/harness-engineering**](https://github.com/vinicius91carvalho/harness-engineering) | Provides shared harness-engineering patterns for running and coordinating Claude Code, Codex, OpenCode, and Pi in Herdr. |
| [**wilbeibi/herdr-catchup**](https://github.com/wilbeibi/herdr-catchup) | Transfers work between Claude Code, Codex, Cursor, Cline, and OpenCode sessions in Herdr. It captures and summarizes a live pane so another agent can continue or branch the task with useful context. |
| [**hcaiano/skills**](https://github.com/hcaiano/skills) | Provides a `herdr-pair` skill that pairs Claude and Codex as equal collaborative partners in one tab. |
| [**jeffory/herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie) | Enables an orchestrator delegate work to Claude, OpenCode, or Antigravity sessions in separate Herdr tabs and worktrees. File-based handoffs and structured completion signals keep the parent context small. |
| [**david-lutz/herdr-claude-teams**](https://github.com/david-lutz/herdr-claude-teams) | Maps Claude Code's experimental agent-team commands to Herdr's socket API, so teammates open as native Herdr panes instead of tmux panes. It requires Herdr 0.6.10 and supports Herdr metadata, notifications, and sidebar views. |
| [**inbeomheo/herdr-orchestra**](https://github.com/inbeomheo/herdr-orchestra) | Coordinates Codex, Grok, Gemini, or Claude worker panes from a central Claude Code controller session. |
| [**msadig/herdr-peer-agents-skill**](https://github.com/msadig/herdr-peer-agents-skill) | Teaches Claude, Pi, or Codex to start a named peer agent, assign work, and collect its result. A shell wrapper handles common startup failures and Codex input quirks. |
| [**Elio2000/herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review) | Starts a second coding agent in a split pane to review the current workspace diff. The tool runs a protected review, revision, and decision loop and includes a Claude Code skill for orchestration. |
| [**eciuca/herdr-drover**](https://github.com/eciuca/herdr-drover) | Orchestrates Claude Code, Codex, and Kira CLI agents across tmux-style Herdr workflows. |
| [**yigitkonur/herdr-pm**](https://github.com/yigitkonur/herdr-pm) | Adds a technical project manager to each live agent tab. The manager reads the session and Git state, ranks possible actions, and guides the existing agent. It supports Claude, Codex, Pi, and Hermes, with optional persistent notes. |
| [**LittleDrinks/herdr-orchestrator-skill**](https://github.com/LittleDrinks/herdr-orchestrator-skill) | Turns the main Claude Code session into a coordinator that plans work, starts workers in Herdr panes, and monitors them without editing code itself. It includes Python monitors, a YAML state-machine template, and role prompts. |
| [**bakescakes/claude-orchestration**](https://github.com/bakescakes/claude-orchestration) | Provides five orchestration skills and hooks for Claude Code to manage parallel backlogs from QA to deployment. |
| [**clawsouls/clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin) | Applies ClawSouls persona definitions to agents running in Herdr. It sets role-specific environments and behavioral rules for Claude Code and other supported agents across multiple panes. |
| [**kiitosu/herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board) | Embeds a Jira Kanban board in a Herdr pane with one-key Claude Code session launching and live card status updates. |
| [**chetanunadkat-lang/herdr-fleet**](https://github.com/chetanunadkat-lang/herdr-fleet) | Runs Claude and Codex workers as a fleet in Herdr panes. The project includes orchestration skills, an `hm` command-line tool, agent definitions, and a Claude Code installer. |
| [**terafin/herdr-restart-always**](https://github.com/terafin/herdr-restart-always) | Supervises processes running in Herdr agent panes and restarts them after a crash. It works with Claude, Hermes, Codex, Pi, OpenCode, and other pane-based agents. |

### Pi supervisor workflows and extensions

*13 projects. Supervision harnesses, task planners, and extensions for Pi agents in Herdr.*

| Project | What it does |
|---|---|
| [**ogulcancelik/pi-extensions**](https://github.com/ogulcancelik/pi-extensions) | Extends Pi with overlays, parallel agent spawners, session recall, and direct Herdr pane control. |
| [**edxeth/pi-subagents**](https://github.com/edxeth/pi-subagents) | Provides a Pi framework for foreground and background subagents, messaging, and multi-pane orchestration. |
| [**joelhooks/pi-bellwether**](https://github.com/joelhooks/pi-bellwether) | Exposes Herdr agent, pane, and session controls as Pi slash commands and LLM tools. It provides reusable start, send, read, focus, and stop operations for higher-level Pi workflows. |
| [**jillesme/pi-herdr-squad**](https://github.com/jillesme/pi-herdr-squad) | Creates visible, strictly read-only investigation teams for Pi inside Herdr. It is intended for parallel research and review tasks that must not modify the workspace. |
| [**joelhooks/herdr-pings**](https://github.com/joelhooks/herdr-pings) | Adds turn-completion alerts and crash detection for Pi agents in Herdr. A Pi extension and companion wait command track workers, while short call signs make concurrent agents easier to identify. |
| [**kirel/herdr-subagents**](https://github.com/kirel/herdr-subagents) | Starts each Pi subagent in its own Herdr pane or tab, manages session files, and notifies the parent when work finishes. Panes remain available for follow-up, and different subagents may use different models. |
| [**Jackliu-miaozi/pi-herdr-workflow-kit**](https://github.com/Jackliu-miaozi/pi-herdr-workflow-kit) | Creates a controlled Pi workflow with separate planner, coder, and reviewer panes. Plans must be approved before coding, each phase is reviewed, and large handoffs are stored in `.pi-herdr/` files instead of pasted into the terminal. |
| [**NickPittas/pi-herdr-subagents**](https://github.com/NickPittas/pi-herdr-subagents) | Monitors Pi's asynchronous subagents and shows their IDs, tasks, states, and session files in a TUI. It can open or focus a subagent session, or start one in a pane, without changing how Pi runs it. |
| [**SecretAardvark/pi-overseer**](https://github.com/SecretAardvark/pi-overseer) | Runs implementer, tester, reviewer, and researcher agents under one supervisor. Each role has command limits, sensitive actions require approval, and task state is saved under `.pi/overseer/` so work can resume after a restart. |
| [**joshka0/herdr-watcher**](https://github.com/joshka0/herdr-watcher) | Tracks detached or long-running work and resumes the relevant agent when a background task completes. It uses the Herdr socket API to support workflows that must survive disconnects and interrupted sessions. |
| [**neilwashere/herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable) | Watches Pi sessions for terminal-provider failures and attempts recovery automatically. It confirms the problem from transcripts, shows a countdown, and can submit a continue command up to three times. |
| [**muslihudindev/herdr-agent-orchestrator**](https://github.com/muslihudindev/herdr-agent-orchestrator) | Coordinates multiple Pi software-engineering agents across isolated Herdr panes. |
| [**yanekyuk/pi-herdr-orchestrator**](https://github.com/yanekyuk/pi-herdr-orchestrator) | Provides project-independent orchestration for Pi agents running in Herdr, with work distributed across visible panes. |

### Subagent launchers and delegation

*39 projects. Tools for launching workers in separate panes and passing work between a lead agent and its helpers.**

| Project | What it does |
|---|---|
| [**alvinunreal/oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim) | Assigns OpenCode specialist roles (fixers, librarians, explorers) to dedicated Herdr panes. |
| [**vekexasia/pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows) | Runs deterministic Pi workflows with on-disk checkpoints and Git worktree isolation in Herdr. |
| [**ogulcancelik/herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start) | Turns a GitHub issue, pull request, or discussion into a prepared agent tab with one key. |
| [**a2u/herdr-jira**](https://github.com/a2u/herdr-jira) | Provides a Ratatui Jira client to browse, filter, and assign tickets directly to Herdr agent panes. |
| [**vercel-labs/herdr-vercel-sandbox-plugin**](https://github.com/vercel-labs/herdr-vercel-sandbox-plugin) | Runs Claude Code, Codex, or OpenCode inside isolated Vercel Sandbox microVMs while showing each session as a Herdr pane. It previews uploads, excludes secrets, and exports agent changes back as Git patches. |
| [**hungv47/herdr-agent-orchestration**](https://github.com/hungv47/herdr-agent-orchestration) | Provides a captain-and-worker workflow for Hermes, Codex, Grok, OpenCode, and Cline agents in Herdr. |
| [**minhtran3124/Brichan**](https://github.com/minhtran3124/Brichan) | A repository-local AI chief of staff for Codex. It keeps project work bounded, coordinates Herdr agents, checks outputs, and stores durable project memory. |
| [**gustavocaiano/opencode-herdr**](https://github.com/gustavocaiano/opencode-herdr) | Opens a new Herdr pane whenever OpenCode creates a subagent session, then attaches OpenCode and arranges the panes in a readable grid. Panes may close automatically when a task becomes idle, fails, or is deleted. |
| [**rohanthewiz/herdr-todo**](https://github.com/rohanthewiz/herdr-todo) | Queues terminal prompts using Bubble Tea, letting you filter and paste them into Claude Code panes. |
| [**darjss/herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate) | Provides Pi-native orchestration with visible workers, a live run board, persistent state, and isolated Git worktrees. Model and reasoning profiles can route simple evidence gathering separately from deeper analysis and review. |
| [**GavinTomlins/herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent) | Mirrors oh-my-openagent delegations into Herdr panes or tabs as they happen. It records live state and full scrollback transcripts, supports split or tabbed layouts, and does not change the agents' execution. |
| [**giuseppecrj/pi-herdr-agents**](https://github.com/giuseppecrj/pi-herdr-agents) | Runs asynchronous Pi subagents and approval-based review workflows entirely inside Herdr. |
| [**machine-machine/ask-fable-skill**](https://github.com/machine-machine/ask-fable-skill) | Delegates tasks from Hermes or Claude Code to a Claude Code Fable 5 worker in a separate Herdr pane. |
| [**freewillythe4th/action-button-agent**](https://github.com/freewillythe4th/action-button-agent) | Connects an iPhone Action Button to personal Herdr agents. Voice input passes through an iOS Shortcut, Tailscale, Telegram, and a Claude Agent SDK operator, which starts or targets a Herdr session and returns the response. |
| [**cyperx84/herdr-loop**](https://github.com/cyperx84/herdr-loop) | Runs iterative planner, coder, and reviewer graphs across Claude Code, Codex, OpenCode, and Pi panes. Socket events and pane output are used to pass intermediate results until the workflow reaches its stopping condition. |
| [**jbaham2/herdr-plugin**](https://github.com/jbaham2/herdr-plugin) | Provides Claude Code skills for Herdr orchestration, layouts, agent monitoring, and session management. |
| [**eliebak/herdr-agent-island**](https://github.com/eliebak/herdr-agent-island) | Coordinates multiple agent loops in separate Herdr panes and tracks their active tasks. |
| [**yigitkonur/claude-code-herdr-plugin**](https://github.com/yigitkonur/claude-code-herdr-plugin) | Controls a Codex subagent from start to finish through one tool backed by the Herdr multiplexer. |
| [**EDMND-SRC/herdr-subagents**](https://github.com/EDMND-SRC/herdr-subagents) | Starts subagents in named Herdr panes. It includes automatic interception, delegation tools, and a grid layout that adapts as workers are added. |
| [**mcdonc/mcdonc-pi-herdr**](https://github.com/mcdonc/mcdonc-pi-herdr) | Makes Pi's background work visible in Herdr. `/bg` moves the current task into a pane, while `/tab` forks the conversation into a new tab through the socket API. |
| [**aldrickdev/herdr_subagents**](https://github.com/aldrickdev/herdr_subagents) | Enables a Pi session create, guide, and inspect named subagents in a shared Herdr tab. Each delegated task remains visible, and the parent can read the worker's output after it becomes idle. |
| [**noor-latif/herd**](https://github.com/noor-latif/herd) | Two scripts that create a project-specific Herdr workspace with a configurable grid of Pi agents. The workspace follows the current directory and restarts dead agents when the project is reopened. |
| [**JLighter/herdr-spawn**](https://github.com/JLighter/herdr-spawn) | Starts coding agents in separate Herdr panes and creates an isolated Git worktree for each one. Commands are provided for assigning work, checking jobs, and collecting completed results. |
| [**noctaIO/herdr-plugin-aos**](https://github.com/noctaIO/herdr-plugin-aos) | Starts Agentic OS-enabled Claude Code agents in a Herdr pane from any workspace without modifying the surrounding project setup. |
| [**lalanikarim/herdr-skills**](https://github.com/lalanikarim/herdr-skills) | Provides Pi skills for creating, navigating, and managing Herdr terminal workspaces. |
| [**marv1nnnnn/pi-yahe**](https://github.com/marv1nnnnn/pi-yahe) | Provides a composable Pi tool for visible task-based multi-agent work that steers async results back to the parent. |
| [**MinhDuyDEV/pi-subagents**](https://github.com/MinhDuyDEV/pi-subagents) | Provides a Pi delegation runtime with claims, leases, context packs, and diagnostic retry handling in Herdr. |
| [**thkt/herdr-agentchat**](https://github.com/thkt/herdr-agentchat) | Coordinates a two-agent leader-and-coder conversation between Claude Code and Codex with send-and-wake sync. |
| [**aerain/herdr-agent-orchestration**](https://github.com/aerain/herdr-agent-orchestration) | Provides a pane-based orchestration skill for OMP and Claude Code running in Herdr. |
| [**shubham399/herdr-agents-auto-compact**](https://github.com/shubham399/herdr-agents-auto-compact) | Automatically compacts long Claude Code and OpenCode sessions in Herdr so they do not exhaust their context windows. |
| [**lucasdeprit/Puppy**](https://github.com/lucasdeprit/Puppy) | A basic multi-agent system built around Claude Code sessions running in the Herdr terminal. |
| [**Sebastiangmz/herdr-plus**](https://github.com/Sebastiangmz/herdr-plus) | Teaches coding agents to operate Herdr and delegate work to subagents in Herdr spaces. |
| [**goatbjh/pi-herdr-claude-subagents**](https://github.com/goatbjh/pi-herdr-claude-subagents) | Enables Pi call Herdr-backed Claude sessions directly as an oracle, reviewer, or planner. |
| [**BrianM0330/pi-herdr-snooze**](https://github.com/BrianM0330/pi-herdr-snooze) | Adds a forced snooze state to Pi agents in Herdr, controlled through `/snooze` or a key binding and independent of the underlying agent type. |
| [**shimo4228/herdr-toolkit**](https://github.com/shimo4228/herdr-toolkit) | Provides tools for cross-vendor delegation on Herdr. It adds acceptance checks intended to reduce fabricated results and can start detached sessions from a phone. |
| [**Idan-Levin/herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review) | A Herdr workflow in which Codex implements changes, a security scan checks them, and a parent agent performs the final review. |
| [**mithyer/ry-skill**](https://github.com/mithyer/ry-skill) | A personal collection of Pi skills for faster Herdr-based workflows. |
| [**regenrek/codex-orchestration-herdr**](https://github.com/regenrek/codex-orchestration-herdr) | A reusable Codex Sol/Luna orchestration skill that assigns workers through Herdr and reuses panes in a predictable way. |
| [**sh1ny/herdr-switchyard**](https://github.com/sh1ny/herdr-switchyard) | A human-approved Hermes and Herdr workflow for isolated OMP coding workers, using Beads as the persistent task ledger. |

### Autonomous coding and pull-request loops

*10 projects. Long-running workflows that implement changes, open pull requests, review results, and react to CI.**

| Project | What it does |
|---|---|
| [**machine-machine/herdr-factory-loop-skill**](https://github.com/machine-machine/herdr-factory-loop-skill) | Provides tools for running Claude Code or Hermes agent fleets through Herdr. It covers discovery, spawning, dispatch, fan-out and convergence, approvals, `tasks.md`-driven workers, spec-kit integration, and guided setup through a TUI. |
| [**sean1588/herdr-orchestrator**](https://github.com/sean1588/herdr-orchestrator) | A Go daemon that runs an issue-to-pull-request workflow from a validated YAML state graph. Herdr hosts implementer and reviewer agents, while the daemon checks GitHub's merge gate and can squash-merge, with dry-run enabled by default. |
| [**razajamil/herdr-factory**](https://github.com/razajamil/herdr-factory) | Claims work from Jira or Markdown task files, creates one Herdr worktree per item, and moves Claude Code through a configurable YAML pipeline. It can follow pull requests through CI, review, and merge under a shared concurrency limit. |
| [**talent-factory/herdr-linear**](https://github.com/talent-factory/herdr-linear) | Adds an interactive Linear issue browser to Herdr. Selecting an issue opens a dedicated agent pane and supplies the ticket context so implementation can begin immediately. |
| [**firegnu/herdr-loop-lab**](https://github.com/firegnu/herdr-loop-lab) | Provides bounded agent loops at three levels: one-task convergence with mechanical and cross-model checks, parallel worktree fleets, and large-goal decomposition with branch integration. All state is saved on disk for clean recovery. |
| [**Tudor0404/dual-author**](https://github.com/Tudor0404/dual-author) | Processes GitHub issues through isolated worktrees, Claude implementation, draft pull requests, and paired Codex and Claude review rounds. A dashboard shows each issue's stage and elapsed time until the change is ready for automatic merging. |
| [**tomasvarga/herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr) | Starts an agent in Herdr to perform an initial quality and bug review of a pull request, then writes draft comments into tuicr. It supports Claude, Codex, Cursor, and Grok backends. |
| [**w-gitops/herdr-agent-factory**](https://github.com/w-gitops/herdr-agent-factory) | A Herdr-native launcher and control plane for multi-agent teams that works independently of the underlying coding harness. |
| [**sarmientoF/herdr-pr-loop**](https://github.com/sarmientoF/herdr-pr-loop) | Runs tester, coder, and reviewer agents through local task cycles and GitHub pull-request reviews in separate tabs. State is stored in files, while approval gates, logs, a budget limit, and a pause file keep runs controllable. |
| [**conpiracy/ep-starter**](https://github.com/conpiracy/ep-starter) | A minimal, extensible starter setup for running Pi as an agent factory inside Herdr. |

### Task queues, backlogs, and event triggers

*6 projects. Queues and event-driven systems that turn stored work into agent jobs.**

| Project | What it does |
|---|---|
| [**nelsonPires5/herdr-board**](https://github.com/nelsonPires5/herdr-board) | A Kanban TUI and background service that turns cards into prompts for agents in visible Herdr panes. Moving a card can create an agent, run it in a dedicated tab, and advance the work through review gates. |
| [**0x5c0f/herdr-insight**](https://github.com/0x5c0f/herdr-insight) | A dockable timeline that combines agent events from every Herdr workspace. It shows active and blocked states, session IDs, configurable columns, and a deduplicated seven-day history that remains current across workspace changes. |
| [**carze/herdr-smolmachine**](https://github.com/carze/herdr-smolmachine) | Starts a coding agent inside a libkrun/KVM microVM from a Herdr pane. A prepared image and shell pipeline manage the VM, while Herdr still provides normal pane control, detaching, and reattaching. |
| [**saiashirwad/homestead**](https://github.com/saiashirwad/homestead) | Creates an isolated worktree for each branch or GitHub issue, including separate ports, environment files, and setup. It launches an agent in Herdr, tracks progress, lands completed branches, and removes finished environments. |
| [**DnzzL/herdr-automations**](https://github.com/DnzzL/herdr-automations) | Schedules recurring prompts and cron jobs that run agents in fresh Herdr worktrees. It supports task-specific MCP settings, collision protection, persistent run history, and a live monitoring board. |
| [**ram4-dev/herdr-automations**](https://github.com/ram4-dev/herdr-automations) | Runs scheduled or event-triggered agent jobs from cron expressions, intervals, and lifecycle hooks. It prevents overlapping runs, creates fresh Git worktrees, and records complete execution histories. |

### General workflows and skill packs

*49 projects. Reusable skills, commands, and opinionated setups for common agent workflows.**

| Project | What it does |
|---|---|
| [**cloudmanic/herdr-plus**](https://github.com/cloudmanic/herdr-plus) | A plugin with two launchers: TOML project templates that build complete workspaces from a fuzzy picker, and Quick Actions for running reusable scripts in the current directory. Prebuilt binaries are available. |
| [**jhochenbaum/herdr-hunk-diff**](https://github.com/jhochenbaum/herdr-hunk-diff) | Displays side-by-side git diffs in an adjacent pane and lets developers leave review comments for agents. |
| [**madarco/agentbox-herdr-plugin**](https://github.com/madarco/agentbox-herdr-plugin) | Connects AgentBox sandboxes to Herdr through a live overlay, a one-key VM launcher for the current project, and clickable `agentbox://` links. |
| [**cobanov/herdr-ntfysh**](https://github.com/cobanov/herdr-ntfysh) | Sends ntfy push notifications when a Herdr agent finishes or asks for input. |
| [**transparent-pegasus/herdrpowers**](https://github.com/transparent-pegasus/herdrpowers) | Provides adding advanced agent workflows to pane-based Herdr sessions. The source description does not list specific features. |
| [**sanirudh17/herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff) | Moves an active coding conversation to a new session using another installed agent CLI. The complete transcript and command history are passed to the replacement agent, avoiding a manual handoff summary. |
| [**pbean/bmad-loop-adapter-herdr**](https://github.com/pbean/bmad-loop-adapter-herdr) | Provides a Herdr terminal-multiplexer backend for bmad-loop. |
| [**bon5co/bermuda**](https://github.com/bon5co/bermuda) | Schedules jobs as interactive agents in dedicated Herdr splits. It supports multi-step workflows, shared append-only discussion logs, and exclusive resource claims that remain valid across temporary sessions. |
| [**wenxichang/herdr-pal**](https://github.com/wenxichang/herdr-pal) | Provides instant-messaging control of Herdr-based AI agents. |
| [**motionharvest/herdr**](https://github.com/motionharvest/herdr) | A terminal-based agent multiplexer project. The source catalog provides no additional detail beyond its Herdr name and purpose. |
| [**nhclink16/herdr-announcer**](https://github.com/nhclink16/herdr-announcer) | Speaks a one-sentence AI summary when an agent finishes or needs input. It supports local text-to-speech, ElevenLabs, or any custom command. |
| [**yangyang0507/herdr-skill**](https://github.com/yangyang0507/herdr-skill) | Refines Herdr agent coordination by replacing vague status polling with output markers and structured messages. Messages include sender, reply target, and task type, and a dependency-free `herdr-msg` Bash helper is included. |
| [**quan-meng/herdr-slurm**](https://github.com/quan-meng/herdr-slurm) | Connects Slurm allocations to Herdr by creating dedicated workspaces and monitored agent tabs for compute jobs. It tracks queue state and reports job and agent progress in the terminal. |
| [**hewenyu/herdr-agent**](https://github.com/hewenyu/herdr-agent) | An agent focused on managing Herdr and making development conversations easier from a phone. |
| [**calebcauthon/herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork) | Forks an agent session into a new Herdr pane by copying and pasting, either manually or through a hotkey. |
| [**leonho/herdr-agent-inbox**](https://github.com/leonho/herdr-agent-inbox) | Shows a popup inbox of all agents and their latest recap. Pressing Enter jumps directly to the selected agent's pane. |
| [**eyalev/herdr-web**](https://github.com/eyalev/herdr-web) | Provides tools for viewing and controlling Herdr agents from a phone. |
| [**RenKoya1/herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all) | Approves every pending agent permission request in Herdr with one keystroke. |
| [**mikedclarke/herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd) | Runs cron routines, heartbeats, and recurring automation scripts in visible Herdr workspaces so background maintenance remains easy to inspect. |
| [**zoridos/herdr-skill**](https://github.com/zoridos/herdr-skill) | Provides tools for controlling Herdr panes, starting agents, and coordinating multi-agent work from inside a Herdr session. |
| [**lifez/herdr-agent-dashboard**](https://github.com/lifez/herdr-agent-dashboard) | Provides tools for standard `herdr agent` processes. It runs on macOS and serves a touch-friendly page that devices such as a Boox can open over the same local network. |
| [**Xz-FreeMan/herdr-hint**](https://github.com/Xz-FreeMan/herdr-hint) | Adds agent-session hints to Herdr. |
| [**jwkicklighter/herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library) | Provides browsing, organizing, and inserting reusable Markdown prompts into the focused pane. Prompt libraries may be local to a project or shared globally. |
| [**andpeicunha/herdr-output-comment-composer**](https://github.com/andpeicunha/herdr-output-comment-composer) | Adds inline comments directly to AI-agent output in a Herdr pane. |
| [**luweiCN/herdr-ops**](https://github.com/luweiCN/herdr-ops) | Adds natural-language workspace commands to Herdr's official skill. Requests such as creating a feature worktree are translated into CLI operations, including worktree actions not covered by the upstream skill, with detailed documentation loaded only when needed. |
| [**marcjfj-vmlyr/quickTUI**](https://github.com/marcjfj-vmlyr/quickTUI) | Provides OpenTUI components and a `/quicktui` skill for building interactive terminal interfaces in Herdr panes, including dashboards, status views, and form prompts. |
| [**pdjsh/herdr-plugins**](https://github.com/pdjsh/herdr-plugins) | A pair of Rust plugins for Herdr: one displays agents in a radial map, and the other reorders workspaces from the keyboard. |
| [**loopkeep/herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview) | Integrates the loopreview workflow with Herdr as a plugin. |
| [**y011d4/herdr-plugin-agentweb**](https://github.com/y011d4/herdr-plugin-agentweb) | Provides tools for monitoring and controlling sessions through a small local bridge server. |
| [**TheShellLand/herdr-agent**](https://github.com/TheShellLand/herdr-agent) | A Herdr agent project with no further description in the source catalog. |
| [**huynguyen03dev/herdr-agent**](https://github.com/huynguyen03dev/herdr-agent) | Provides agent-independent role profiles for operating an AI technical department over the Herdr protocol. |
| [**MartinBspheroid/herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash) | A local, keyboard-first agent board showing active workers, semantic state, effective directory, Git context, and source-labelled activity. |
| [**zerodice0/herdr-agent-labels**](https://github.com/zerodice0/herdr-agent-labels) | Assigns readable color-and-animal names to Herdr agents that do not already have labels. |
| [**okonomi/herdr-agent-queue**](https://github.com/okonomi/herdr-agent-queue) | Cycles through stopped or waiting Herdr agents with one key, starting with the agent that has been waiting longest. |
| [**hisetu/herdr-agent-skill**](https://github.com/hisetu/herdr-agent-skill) | Adds integration support and dedicated helpers for using an agent skill inside Herdr sessions. |
| [**ahnsv/maeh**](https://github.com/ahnsv/maeh) | Provides tools for hmph and Herdr agent orchestration. |
| [**dkarter/foreman**](https://github.com/dkarter/foreman) | Provides tools for monitoring Herdr agents. |
| [**BlazzzPlay/herdr-office**](https://github.com/BlazzzPlay/herdr-office) | A read-only pixel-art office that visualizes Herdr agents and their activity. |
| [**mikhail-angelov/herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop) | Automates a repeated cross-review loop in which one agent writes changes and another reviews them inside the same Herdr workspace. |
| [**masakirocorp/oh-my-herdr**](https://github.com/masakirocorp/oh-my-herdr) | A terminal workspace manager for AI coding agents built around Herdr. |
| [**egriff38/effect-herdr**](https://github.com/egriff38/effect-herdr) | A typed Effect-TS SDK for controlling the Herdr terminal agent multiplexer. |
| [**Drozerah/herdr-voice**](https://github.com/Drozerah/herdr-voice) | Provides tools for Herdr with audio-stream management for several agents working in the same workspace. |
| [**hoon-ch/herdr-gjc-plugin**](https://github.com/hoon-ch/herdr-gjc-plugin) | Reports agent launch, exit, idle, working, and blocked states to Herdr. |
| [**narumiruna/herdr-web**](https://github.com/narumiruna/herdr-web) | A terminal-focused browser workbench for viewing and operating the Herdr agent runtime. |
| [**wtcrowe4/DialDeck**](https://github.com/wtcrowe4/DialDeck) | Uses a Microsoft Surface Dial and an AutoHotkey v2 engine as a keyless control surface for Herdr orchestration, development commands, and modelling macros. |
| [**IgorWarzocha/herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations) | Captures notes attached to selected terminal text and stages those annotations for Herdr agents to act on. |
| [**huntergdavis/dunkingsheep**](https://github.com/huntergdavis/dunkingsheep) | Keeps agents active by sending configured text to Herdr panes at regular intervals. |
| [**EricBois/herdr-nudge**](https://github.com/EricBois/herdr-nudge) | Schedules a continue prompt for a Herdr agent, either at a chosen time or when the agent becomes idle or blocked. |
| [**ryanlewis/herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer) | Copies agent session names onto the corresponding Herdr workspace labels. |

---

## 2. Connect through MCP and the socket API

*106 projects. MCP servers, socket clients, notifications, telemetry, hardware links, and bridges to other protocols or services.*

### MCP servers

*6 projects. Servers that expose Herdr operations as MCP tools for compatible AI clients.**

| Project | What it does |
|---|---|
| [**Phoobobo/herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager) | Provides tools for auditing and managing skills, MCP servers, plugins, and lifecycle hooks across workspaces. A central manifest helps keep agent configuration consistent. |
| [**runchr-works/herdr-mesh**](https://github.com/runchr-works/herdr-mesh) | Connects multiple Herdr instances into a coordinated mesh over Model Context Protocol. |
| [**eugeneb50/herdr-mcp**](https://github.com/eugeneb50/herdr-mcp) | Exposes Herdr workspace and pane controls as tools to any Model Context Protocol (MCP) client. |
| [**54rt1n/herdr-simple-mcp**](https://github.com/54rt1n/herdr-simple-mcp) | Provides a lightweight Model Context Protocol server for driving Herdr from Claude Desktop and Cursor. |
| [**islam3zzat/herdr-mcp**](https://github.com/islam3zzat/herdr-mcp) | An MCP server that lets AI assistants inspect and control coding agents running in Herdr through a socket-based communication bridge. |
| [**bonsai/herdr-mcp**](https://github.com/bonsai/herdr-mcp) | Provides Herdr tab control from OpenCode through MCP and also works as a Herdr plugin. |

### Socket API clients and SDKs

*54 projects. Libraries, command-line clients, and services that communicate with Herdr through its local socket.**

| Project | What it does |
|---|---|
| [**backpine/remote-agent-workspace**](https://github.com/backpine/remote-agent-workspace) | Provides an always-on remote agent environment: edit on macOS, run Herdr work on Linux, synchronize files with Syncthing, and expose services through Cloudflare Tunnel and Caddy. |
| [**DanielOu1208/agentslate**](https://github.com/DanielOu1208/agentslate) | An iPhone remote keypad for supervising Herdr coding agents over Tailscale. |
| [**schacon/micro-manager**](https://github.com/schacon/micro-manager) | Uses the Creator Micro 2 hardware controller to operate Herdr. |
| [**0xGosu/herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot) | Prompts a running coding CLI through the Herdr API. A training mode observes user actions, safety checks block dangerous operations, and an optional autonomous mode can continue prompting after sufficient setup. |
| [**benkraus/herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay) | Provides mobile-relay integration. The source catalog does not describe its controls in more detail. |
| [**LoneExile/merino**](https://github.com/LoneExile/merino) | Provides tools for viewing and controlling Herdr agents. |
| [**ryonakae/shepherd**](https://github.com/ryonakae/shepherd) | A worker-observability service and set of runtime bridges for coding agents managed by Herdr. |
| [**Tomyail/herdr-connect**](https://github.com/Tomyail/herdr-connect) | An open-source LAN companion app that discovers nearby Herdr installations and connects to them. |
| [**kkunkunya/herdr-remote-phone**](https://github.com/kkunkunya/herdr-remote-phone) | A phone-focused fork of herdr-remote with profiles for several Macs, a conversation view, and model and command pickers designed for small screens. |
| [**Mic92/herdr-eternal**](https://github.com/Mic92/herdr-eternal) | A roaming-friendly transport for `herdr --remote` using QUIC with a WebSocket fallback, exact byte-stream resumption, and OIDC authentication. |
| [**cryks/shepherd**](https://github.com/cryks/shepherd) | Monitors Herdr agents on local and remote machines from the macOS menu bar. |
| [**54rt1n/herdr-python-client**](https://github.com/54rt1n/herdr-python-client) | Provides typed Python bindings and socket utilities for automating Herdr programmatically. |
| [**CodyBontecou/herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge) | Streams structured Herdr activity as NDJSON, including pane focus time, detected agent and model details, and local session summaries. Output can go to a file, webhook, or command, and transcript text is hidden by default. |
| [**speardragon/herdr-agents-history**](https://github.com/speardragon/herdr-agents-history) | Combines live tool calls and command output from Claude Code and Codex agents. It reads Herdr's event stream and provides one searchable, filterable activity feed. |
| [**TheMetalStorm/herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin) | Integrates Freebuff agents with Herdr by reading PTY output and local session files, then reporting idle, working, and blocked states through the socket API. |
| [**usrivastava92/herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup) | Prevents macOS or Linux from sleeping while Herdr agents are working. It enables an operating-system sleep inhibitor when activity begins and releases it when every agent is idle. |
| [**vantt/herdr-go**](https://github.com/vantt/herdr-go) | A web-first remote gateway and supervisor for controlling Herdr coding agents from a phone. |
| [**akhileshrangani4/herdr-bridge**](https://github.com/akhileshrangani4/herdr-bridge) | An HTTP bridge with a terminal-friendly control panel for Herdr agents. |
| [**lib-x/herdr-sock-go**](https://github.com/lib-x/herdr-sock-go) | Provides tools for Herdr's newline-delimited JSON socket protocol, generated for the 0.7.0 API. It includes typed helpers for common operations and raw call methods for the full surface. |
| [**klittle32/letta-herdr-mod**](https://github.com/klittle32/letta-herdr-mod) | Modifies Letta Code so sessions running in Herdr report accurate idle, working, and blocked states to the sidebar. |
| [**aneym/herdr-voice**](https://github.com/aneym/herdr-voice) | Controls workspaces, pane splits, and agent dispatch with spoken commands through OpenAI's Realtime API. A floating display shows the transcription and asks for confirmation before sending instructions. |
| [**benkraus/herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs) | A Bubble Tea popup that reads local CLIProxyAPI credentials and displays Codex subscription quota, reset times, and credit balances for multiple accounts. |
| [**gejiliang/herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw) | Treats OpenClaw TUI sessions as Herdr agents, with live state, model information, and token use in the sidebar. A background watcher parses OpenClaw status lines and reports them through the socket API. |
| [**uuie/reasonix-herdr**](https://github.com/uuie/reasonix-herdr) | Reports Reasonix agent lifecycle states to Herdr in real time and adds native workspace and pane controls for supervising Reasonix alongside other agents. |
| [**maxandersen/jherdr**](https://github.com/maxandersen/jherdr) | Provides tools for the Herdr socket API. |
| [**damozhang/dsh-herdr-bridge**](https://github.com/damozhang/dsh-herdr-bridge) | Lets the web interface discover, start, prompt, and monitor Pi, Claude, Codex, and other agents running under Herdr. |
| [**jerryfane/herdr-codex-usage-kit**](https://github.com/jerryfane/herdr-codex-usage-kit) | Shows remaining Codex five-hour and weekly quota in the Herdr sidebar and provides a live shell dashboard. It reads local Codex JSONL logs, refreshes every 30 seconds, and does not call an external API. |
| [**Phoobobo/herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration) | Connects TraeX lifecycle hooks to Herdr's agent-reporting socket methods, giving TraeX panes correct idle, working, and blocked status. |
| [**cdpath/herdr-warp**](https://github.com/cdpath/herdr-warp) | Integrates the Warp Agent CLI with Herdr. It can send prompts, wait for output, approve or reject actions, and infer idle, working, and blocked status from terminal output. |
| [**kevinWangSheng/herdr-kit**](https://github.com/kevinWangSheng/herdr-kit) | Provides building Herdr integrations, with declarative layouts, an event-watcher service, plugin helpers, and a typed socket client exposing streaming and low-level features beyond the standard CLI. |
| [**scott-the-programmer/vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr) | Forwards Herdr's Unix socket into VS Code development containers through a loopback TCP bridge, allowing containerized agents to report status and receive commands from the host Herdr instance. |
| [**yuuta1219/claude-usage**](https://github.com/yuuta1219/claude-usage) | Reads local Claude Code telemetry and shows session and weekly token-use percentages at the bottom of the Herdr sidebar. |
| [**nyanyaon/github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin) | Provides tools for organizing and dispatching work from GitHub issues through Herdr. |
| [**maedana/herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge) | Provides tools for Herdr agents that runs a web server and uses a QR code for easy connection. |
| [**cyperx84/herdr-api**](https://github.com/cyperx84/herdr-api) | Provides tools for Herdr protocol 19, with transport handling, event streaming, and a typed agent model. |
| [**thanh-dong/herdr-rich-preview**](https://github.com/thanh-dong/herdr-rich-preview) | A browser preview for files changed by agents in Herdr. It renders Markdown, Mermaid, D2, HTML, and SVG and works with SSH and remote Herdr sessions. |
| [**flaricy/herdr-bridge**](https://github.com/flaricy/herdr-bridge) | Reports DeepSeek Harness activity to the Herdr pane that hosts it, including live working, blocked, and idle states, without requiring changes to Herdr. |
| [**PlaneshiftDev/microd**](https://github.com/PlaneshiftDev/microd) | A companion service for the Codex Micro macropad that handles button events, gestures, and RGB control over a Unix socket, with an optional Herdr bridge. |
| [**atnine-ai/herdr-bridge**](https://github.com/atnine-ai/herdr-bridge) | Connects Herdr panes to chat services for communicating with agents outside the terminal. |
| [**aiken884/herdr-bridge**](https://github.com/aiken884/herdr-bridge) | A single command center for sending tasks to several coding agents, following their progress, and checking the final result through Herdr. |
| [**sina85/herdr-mobile**](https://github.com/sina85/herdr-mobile) | A password-protected, mobile-first Next.js panel for a local Herdr session, published through Cloudflare Tunnel and Access. |
| [**pepperhorn/herdr-remote**](https://github.com/pepperhorn/herdr-remote) | Provides tools for a running Herdr server. |
| [**deanbaker/herdr-remote**](https://github.com/deanbaker/herdr-remote) | Provides tools for inspecting and controlling Herdr workspaces remotely. |
| [**hisetu/pi-herdr-remote**](https://github.com/hisetu/pi-herdr-remote) | Pi-native tools for operating Herdr servers on explicitly approved SSH hosts. |
| [**bradydibble/herdi**](https://github.com/bradydibble/herdi) | A private remote client and relay for Herdr; development moved away from its former public fork. |
| [**alex-devdone/herdr-remote-agent-watch**](https://github.com/alex-devdone/herdr-remote-agent-watch) | Shows a Claude session running behind SSH and tmux as a live Herdr sidebar agent. It also provides more resilient SSH and remote-Herdr wrapper commands. |
| [**georgolden/herdr-remote-setup**](https://github.com/georgolden/herdr-remote-setup) | Provides tools for multi-project Herdr development with remote phone access. |
| [**AgentWorkforce/herdr-relay-bridge**](https://github.com/AgentWorkforce/herdr-relay-bridge) | A relay bridge intended to connect Herdr agents as a cooperating team. The source catalog gives no further protocol details. |
| [**pinksaucepasta/paperboat-helper**](https://github.com/pinksaucepasta/paperboat-helper) | A remote runtime for Paperboat environments, covering PTYs, Herdr agents, previews, images, activity reporting, and configuration synchronization. |
| [**shaunbntan-create/vgpt-app**](https://github.com/shaunbntan-create/vgpt-app) | Provides tools for a Herdr agent fleet, served over Tailscale and based on AltanS/collie. |
| [**shaunbntan-create/vgpt**](https://github.com/shaunbntan-create/vgpt) | Provides tools for viewing and controlling a Herdr agent fleet, maintained as a fork of AltanS/collie. |
| [**crabfishxy/awaytome**](https://github.com/crabfishxy/awaytome) | Provides tools for monitoring and controlling Herdr agents from a phone, with full terminal mirroring. |
| [**LuYanFCP/herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin) | Provides tools for remote control through WeChat. |
| [**trillium/herdr-tailscale**](https://github.com/trillium/herdr-tailscale) | Automatically attaches trusted Tailscale peers to Herdr as remote tabs. |

### Chat alerts: Telegram, Discord, and Slack

*14 projects. Bot and channel alerts that ping you when agents finish or need input.*

| Project | What it does |
|---|---|
| [**alexei-led/ccgram**](https://github.com/alexei-led/ccgram) | Maps forum topics to terminal windows running Claude Code, Codex, Gemini, Pi, or a shell. It relays output and input through Herdr or tmux so sessions remain usable from a phone. |
| [**ogulcancelik/herdr-plugin-examples**](https://github.com/ogulcancelik/herdr-plugin-examples) | Official sample plugins showing four common patterns: Telegram notifications, development layouts, GitHub link previews, and Rust release tracking. Each example is a standalone package meant to be adapted when building a new plugin. |
| [**dcolinmorgan/herdr-push**](https://github.com/dcolinmorgan/herdr-push) | Forwards agent status changes to the herdr-remote relay using only curl and system Python or jq. A single relay setting enables mobile, menu-bar, or Telegram monitoring, and a test action checks the connection. |
| [**luminexord/herdres**](https://github.com/luminexord/herdres) | Provides tools for monitoring and messaging Herdr coding agents. |
| [**natori-hrj/herdr-hail**](https://github.com/natori-hrj/herdr-hail) | Connects Herdr to Slack and Discord through a two-way webhook bridge. Blocked-agent alerts can be answered through replies or action buttons without opening a network tunnel. |
| [**gaijinjoe/herdres**](https://github.com/gaijinjoe/herdres) | Maps every live Herdr pane to a Telegram forum topic. Agent activity appears in the topic, and bot commands can send input back to the matching pane from any device. |
| [**cokekitten/herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge) | Sends Telegram notifications when an agent finishes or waits for input. Replies, including files, are delivered to the correct pane without requiring a public server or port tunnel. |
| [**mvallebr/herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin) | A Telegram bot companion that maps Herdr agents to forum topics and provides remote control without placing an LLM between the user and the pane. |
| [**blockshiftnetwork/herdr-telegram-attention**](https://github.com/blockshiftnetwork/herdr-telegram-attention) | Sends Telegram alerts for blocked, finished, or approval-waiting Herdr agents and supports quick replies for unblocking them remotely. |
| [**happyeric77/agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify) | Posts structured HTTP webhooks when agents block or finish. Payloads can include workspace and pane details, model information, and recent scrollback for use in Slack, Discord, or mobile-alert systems. |
| [**revanp/herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence) | Publishes the active Herdr project, current agent, and total active-agent count through Discord Rich Presence using a local RPC service, with no bot or external server required. |
| [**juninaba/herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify) | Sends Slack notifications when Herdr agents finish or become blocked. |
| [**dcieslak19973/herdr-slackr**](https://github.com/dcieslak19973/herdr-slackr) | Displays a real-time Slack feed inside a Herdr pane, using Socket Mode with polling as a fallback. |
| [**sbulav/herdr-relay**](https://github.com/sbulav/herdr-relay) | Provides monitoring and approving Herdr agents from a phone, menu bar, or Telegram without using SSH. |

### Desktop, mobile, and webhook notifications

*13 projects. System toasts, ntfy pings, and webhook triggers for agent events.*

| Project | What it does |
|---|---|
| [**cedrus-8864/herdr-prompt-reply**](https://github.com/cedrus-8864/herdr-prompt-reply) | Posts blocked agent permission prompts as interactive macOS notifications with action buttons, allowing responses without switching back to the terminal. |
| [**yankewei/herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify) | Shows a clickable macOS notification when an unseen pane becomes blocked or finishes. Clicking the alert brings the terminal forward and focuses the exact pane through `alerter`. |
| [**zom-2018/herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify) | Sends structured ntfy alerts when an agent blocks or finishes. Notifications include the workspace, tab, and pane, and the plugin prefers a detected local ntfy server before using the network. |
| [**dot/herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier) | Bundles a branded macOS notification app so Herdr alerts use the correct icon and can jump to the relevant pane. The app periodically refreshes its Launch Services registration to recover cleanly after reboots or updates. |
| [**horn553/herdr-ntfy**](https://github.com/horn553/herdr-ntfy) | Sends ntfy alerts for done and blocked agent states using standard command-line tools and curl. |
| [**TheMetalStorm/herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin) | Integrates Command Code as a Herdr agent runtime with process detection, idle, working, and blocked status, session recovery after server restarts, and toast alerts when input is needed. |
| [**tiny-send/tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr) | Emails a one-line summary when an agent blocks, finishes, or fails. Replying to the message sends input to the correct pane, making an email client a simple remote approval interface. |
| [**HikaruEgashira/say-hook**](https://github.com/HikaruEgashira/say-hook) | Reads a one-line status summary aloud when an agent becomes done or blocked, using ElevenLabs or macOS speech through a Herdr state-change hook. |
| [**saeedrahimi/herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl) | Converts Herdr lifecycle events inside WSL into native Windows 11 toast notifications by invoking PowerShell across the WSL boundary. |
| [**rkbkosp/agent-beacon**](https://github.com/rkbkosp/agent-beacon) | An ESP32-S3 desktop beacon showing Codex quota, Herdr agent state, weather, and full-screen alerts through a macOS bridge. |
| [**keinstn/drover-notify**](https://github.com/keinstn/drover-notify) | Sends a push alert to the Drover iOS app when a Herdr agent becomes blocked. It uses built-in Node.js features only and stores encrypted pairing information locally. |
| [**ram4-dev/herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center) | Stores notifications from all workspaces in a durable popup inbox. Items can be reviewed, opened in their related pane, cleared when resolved, and retained across restarts. |
| [**winoooops/herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher) | Adds live sidebar cards, lifecycle alerts, and a zero-configuration Claude Code metrics bridge for Herdr agents. |

### Telemetry, events, and quota streaming

*7 projects. Event collectors and monitors for agent state, usage, cost, and runtime activity.**

| Project | What it does |
|---|---|
| [**DIodide/herdr-telemetry**](https://github.com/DIodide/herdr-telemetry) | Sends workspace and agent telemetry to an endpoint chosen by the user. It removes tokens, redacts sensitive prompts, and ships as a single binary. |
| [**second-state/vibetty**](https://github.com/second-state/vibetty) | Streams live Herdr terminal screens over MQTT to devices such as VibeKeys and VibeWatch and relays keystrokes back. It includes an MQTT broker and integrates with Herdr's command palette and status bar. |
| [**alejodelosrios/herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage) | Shows live Claude plan usage for both the current session and the weekly limit in the Herdr sidebar. It reads Claude Code's own authentication and status data rather than estimating usage. |
| [**amurru/herdr-whistle**](https://github.com/amurru/herdr-whistle) | Provides tools for monitoring and controlling agents across remote Herdr daemon instances. It streams lifecycle updates and sends commands without taking over the terminal session. |
| [**Javamomma/herdr-scribe**](https://github.com/Javamomma/herdr-scribe) | Streams microphone audio into temporary in-memory transcript and analysis panes. When recording ends, it creates structured meeting notes, policy checks, and draft task tickets without saving the raw audio. |
| [**kosuketut/herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder) | Downloads files created or changed in a remote Herdr pane to a local Mac. A plugin action detects paths in the active pane and transfers the selected artifact over the remote connection. |
| [**iamhouser/herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi) | Adds session and weekly Claude rate-limit gauges, color thresholds, and unblock countdowns to workspace rows. It supports several accounts by matching pane directories to profile folders without using tokens. |

### Voice, hardware, and remote bridges

*1 project. Interfaces that connect Herdr to spoken input, physical devices, or remote control surfaces.**

| Project | What it does |
|---|---|
| [**razajamil/herdr-hex-browser-voice-command**](https://github.com/razajamil/herdr-hex-browser-voice-command) | A Chrome extension and local service that sends Hex voice transcripts to the correct Herdr pane based on the browser URL that was focused while speaking. URL patterns are mapped to workspace, tab, and pane targets. |

### Protocol and third-party bridges

*11 projects. Adapters between Herdr and other multiplexers, platforms, messaging systems, or automation protocols.**

| Project | What it does |
|---|---|
| [**openclaw/crabbox**](https://github.com/openclaw/crabbox) | Adds Crabbox sandbox provisioning and remote test execution to Herdr. Plugin actions can prewarm temporary environments, synchronize diffs, and inspect active leases from an overlay. |
| [**neon-solutions/neon-herdr**](https://github.com/neon-solutions/neon-herdr) | Embeds a serverless Postgres dashboard in a Herdr pane. It can create database branches per agent worktree, start or stop compute, and insert connection strings. |
| [**JYasha11/herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face) | Shows an increasingly urgent ASCII-art face when a Herdr agent is blocked and waiting for input, making overlooked approvals difficult to miss. |
| [**kukv/herdr-plugin-github-dash**](https://github.com/kukv/herdr-plugin-github-dash) | Adds GitHub issue and pull-request management to Herdr, including review, tracking, and assignment of GitHub work to agent tabs from inside the terminal. |
| [**carsonjones/herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard) | A Bun and React/OpenTUI dashboard that lists all running Herdr agents with live status. It can be opened as a key-bound plugin action or run as a standalone terminal app. |
| [**go-min/herdr-fwd**](https://github.com/go-min/herdr-fwd) | Automatically maintains loopback port forwarding between a remote Herdr session and the local machine, making services started by remote agents available without manual SSH tunnels. |
| [**vaclavik-xyz/herdwatch**](https://github.com/vaclavik-xyz/herdwatch) | Keeps a pane marked as working while CI, review, or another background condition is still pending after the agent itself becomes idle. It can run once or as a background service. |
| [**jatingargiitk/herdr-memory**](https://github.com/jatingargiitk/herdr-memory) | Builds persistent project memory from agent actions, successful approaches, and earlier decisions across Herdr sessions, then adds relevant context to later prompts to reduce repeated mistakes. |
| [**junliu-mde/mimo-code-herdr-plugin**](https://github.com/junliu-mde/mimo-code-herdr-plugin) | Combines all subagent states into a stable idle, working, blocked, or done status for Herdr. A watchdog releases stale labels after crashes, and nested MiMo tool calls are ignored. |
| [**abtris/herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr) | Checks the current branch's GitHub pull request against linked Jira tickets. It shows ticket state and warns when issue keys are missing or do not match, keeping Jira context visible in Herdr. |
| [**candypoets/buzzr**](https://github.com/candypoets/buzzr) | Mirrors Herdr workspaces and panes into Buzz channels using Nostr identities. It publishes agent availability and routes channel mentions to the correct terminal pane without exposing the user's private key. |

---

## 3. Editor integrations

*54 projects. Tools that connect Herdr with Neovim, VS Code, Cursor, Vim, Kakoune, REPLs, and other editing environments.*

### Neovim navigation and splits

*30 projects. Plugins that make movement between Neovim windows and Herdr panes feel continuous.**

| Project | What it does |
|---|---|
| [**paulbkim-dev/vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation) | Ports vim-tmux-navigator behavior to Herdr. Direction keys move within Vim or Neovim until an edge is reached, then shift focus to the adjacent Herdr pane based on the pane's foreground process. |
| [**lmilojevicc/herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim) | Bridges Neovim split navigation and smart pane resizing with Herdr terminal panes. |
| [**chmarax/herdr-nvim**](https://github.com/chmarax/herdr-nvim) | A Neovim bridge with a Rust core and Lua configuration for inspecting Herdr panes, starting agent sessions, and sending editor selections to active panes. |
| [**aimdevlee/herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav) | Provides shared `Ctrl+h/j/k/l` navigation between Neovim splits and Herdr panes using socket-based focus tracking. |
| [**nettlesh/dotfiles**](https://github.com/nettlesh/dotfiles) | Personal Alacritty, Fish, Herdr, and Neovim dotfiles with workspace navigation and agent-dispatch configuration. |
| [**devxplay/herdr.nvim**](https://github.com/devxplay/herdr.nvim) | Provides seamless directional split navigation (Ctrl+h/j/k/l) between Neovim and Herdr panes. |
| [**makyinmars/herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim) | A two-pane Neovim composer that turns selections, cursor positions, and file details into structured Markdown context for a Herdr agent. The prompt is staged for review rather than submitted automatically. |
| [**nwiizo/signalbox.nvim**](https://github.com/nwiizo/signalbox.nvim) | An attention-focused Neovim control surface for persistent coding agents running in Herdr. |
| [**cinco/herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim) | Combines ripgrep and fzf for live searching, then opens a selected match in a Neovim split beside the active Herdr agent. |
| [**willfish/herdr-navigator**](https://github.com/willfish/herdr-navigator) | Provides the Herdr-side actions needed for shared Vim or Neovim navigation. It checks the active pane process and either forwards the key to the editor or moves Herdr focus. |
| [**kaar/nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator) | Uses one set of `Ctrl+h/j/k/l` shortcuts to move through both Neovim splits and Herdr panes. |
| [**inferst/herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim) | A Neovim code-review interface with Git and Herdr integration. |
| [**bojackduy/nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation) | Applies vim-tmux-navigator-style directional keys across internal splits and surrounding Herdr panes. |
| [**shadowfax92/herdr-comments**](https://github.com/shadowfax92/herdr-comments) | Imports output from a Herdr agent pane into Neovim for line-level comments and organized review notes in editor buffers. |
| [**ctbaum/herdr-agents.nvim**](https://github.com/ctbaum/herdr-agents.nvim) | Provides tools for starting and working with editor-integrated coding agents in Herdr panes. |
| [**willfish/herdr-navigator.nvim**](https://github.com/willfish/herdr-navigator.nvim) | Provides unified movement between Neovim windows and Herdr panes. |
| [**TianZuo555/herdr.nvim**](https://github.com/TianZuo555/herdr.nvim) | Sends Neovim file and code references to coding agents running in the same Herdr tab. |
| [**sebcbi1/herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav) | Unifies directional navigation and resizing across Neovim splits, Herdr panes, tabs, and workspaces. Boundary detection forwards focus to the next surface without changing modes. |
| [**kbroomstd/herdr.nvim**](https://github.com/kbroomstd/herdr.nvim) | Provides Neovim key bindings for controlling the Herdr agent multiplexer. |
| [**luiarthur/herdr.vim**](https://github.com/luiarthur/herdr.vim) | Starts a language-appropriate REPL in a Herdr pane and sends the current line, whole file, or visual selection from Vim or Neovim. It supports older Vim releases as well as modern Neovim. |
| [**UN-9BOT/sidekick_herdr**](https://github.com/UN-9BOT/sidekick_herdr) | Adds Herdr as a session backend for sidekick.nvim, giving its AI CLI launcher the same workflow available with tmux or Zellij without requiring a fork. |
| [**luisgui1757/dotfiles**](https://github.com/luisgui1757/dotfiles) | A cross-platform Rose Pine terminal and editor setup for macOS, Linux, WSL2, and Windows. It includes Neovim, Herdr, tmux or psmux, several terminals and shells, Nix on POSIX, and chezmoi-managed configuration. |
| [**RooseveltAdvisors/vim-herdr-navigation**](https://github.com/RooseveltAdvisors/vim-herdr-navigation) | A fork of `vim-herdr-navigation` with shared Ctrl and Alt directional keys across Herdr panes and Vim or Neovim splits. |
| [**joo-was-already-taken/herdr-navigator.nvim**](https://github.com/joo-was-already-taken/herdr-navigator.nvim) | Provides tools for navigating between editor splits and surrounding Herdr panes. |
| [**utahta/herdr-prompt.nvim**](https://github.com/utahta/herdr-prompt.nvim) | Enables a Neovim user ask a Herdr agent about the code currently being viewed or edited. |
| [**ocyedwin/editor**](https://github.com/ocyedwin/editor) | A portable development setup combining Ghostty, Herdr, Vim, Neovim, and VSCodeVim. |
| [**rahadur/herdr.nvim**](https://github.com/rahadur/herdr.nvim) | Ports the Ink and Paper color schemes from herdr.dev to Neovim. |
| [**s-0-a-r/copse**](https://github.com/s-0-a-r/copse) | A command-line agent development environment combining Herdr, Neovim, and parallel agent fan-out. |
| [**jakkzz/herdr-setup**](https://github.com/jakkzz/herdr-setup) | A reproducible Herdr and Neovim setup with pinned plugins and a cross-platform installer for macOS, Linux, and WSL. |
| [**mirkobozzetto/dotfiles**](https://github.com/mirkobozzetto/dotfiles) | A macOS terminal setup using Ghostty with tmux or Herdr, Neovim, and routing that brings the user to whichever coding agent needs attention. |

### Full Neovim-hosted workspaces

*1 project. A deeper integration that uses Neovim as the main interface while Herdr owns the agent processes.**

| Project | What it does |
|---|---|
| [**MomePP/herd.nvim**](https://github.com/MomePP/herd.nvim) | Uses Neovim as the primary dashboard to launch, monitor, and control background Herdr agent sessions. |

### VS Code, Cursor, and dev containers

*9 projects. Extensions and environment setups for graphical editors and container-based development.**

| Project | What it does |
|---|---|
| [**T0mSIlver/localvoxtral**](https://github.com/T0mSIlver/localvoxtral) | Fully local, real-time dictation for Apple Silicon Macs. It streams speech into the coding-agent session under the cursor, including Claude Code inside a Herdr pane, and uses that session as context for optional text polishing. |
| [**timofey-TK/herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor) | Opens the active Herdr workspace in VS Code or Zed with one shortcut. Local and SSH-remote workspaces are translated into the correct editor URI automatically. |
| [**lurepos/herdr-vscode-tasks**](https://github.com/lurepos/herdr-vscode-tasks) | Provides tools for projects that use a `.vscode` directory and VS Code task configuration. The source catalog provides no further detail. |
| [**magimetal/matrix-themes**](https://github.com/magimetal/matrix-themes) | Provides Pi Coding Agent, Ghostty, Herdr, VS Code, and Zed. |
| [**andorexu/hermes-agent-skills-pack**](https://github.com/andorexu/hermes-agent-skills-pack) | A pack of 28 Hermes Agent skills covering decision methods, reasoning workflows, engineering tools, OCR, and web tasks, with support for Hermes, Claude Code, Herdr, and Cursor. |
| [**endoumame/herdr-vscode**](https://github.com/endoumame/herdr-vscode) | Adds an inline code-review workflow to VS Code for work associated with Herdr agent sessions. The source description is incomplete beyond writing comments where the code is read. |
| [**alex-devdone/herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open) | Opens the focused Herdr pane's project in Cursor or VS Code, including remote panes through the editor's Remote SSH support. |
| [**gogamid/pi-herdr-cursor-focus**](https://github.com/gogamid/pi-herdr-cursor-focus) | Hides the editor cursor in Herdr panes that are not currently focused. |
| [**beraterkanelcelik/agent-army**](https://github.com/beraterkanelcelik/agent-army) | A three-level agent hierarchy for parallel coding missions under one human operator, using Claude Code, Herdr, cursor-agent, and files as the command channel. |

### Vim, Kakoune, and other editors

*11 projects. Navigation and workflow integrations for editors outside Neovim and VS Code.**

| Project | What it does |
|---|---|
| [**ImArtisann/zed-herdr**](https://github.com/ImArtisann/zed-herdr) | Keeps Zed projects synchronized with Herdr workspaces by listening to lifecycle events over the Unix socket. It supports reconnection and full snapshot synchronization after interruptions. |
| [**ChmaraX/herdr-gitview**](https://github.com/ChmaraX/herdr-gitview) | A Git status and diff panel for Herdr with file editing in Neovim, hunk staging and discarding, and commits from inside the terminal. |
| [**Schaitanya535/herdr-config**](https://github.com/Schaitanya535/herdr-config) | A personal Herdr configuration with custom keys, a theme, and a helper that sends scrollback into Neovim. |
| [**ionrock/ghostherd**](https://github.com/ionrock/ghostherd) | Manages Herdr agent terminals from Emacs through ghostel. |
| [**Aerosnail/nvim-herdr-navigator**](https://github.com/Aerosnail/nvim-herdr-navigator) | A matching plugin pair for moving smoothly between Neovim splits and Herdr panes. |
| [**AVGVSTVS96/vim-herdr-navigator**](https://github.com/AVGVSTVS96/vim-herdr-navigator) | Provides unified directional navigation between Herdr panes and Vim or Neovim splits. |
| [**eddof13/herdr.el**](https://github.com/eddof13/herdr.el) | Controls Herdr from Emacs while hosting Herdr's terminal sessions inside Emacs through ghostel. |
| [**SamuelCastrillon/tzemed**](https://github.com/SamuelCastrillon/tzemed) | A Windows-native development stack combining Herdr, Neovim, Peri, and Gentle-ai specification-driven development. |
| [**GMakeziG/ninjatronics-ai**](https://github.com/GMakeziG/ninjatronics-ai) | An AI operating environment for coordinating specialist engineering agents through Hermes, Herdr, Claude Code, and Codex. |
| [**AVGVSTVS96/starter-dotfiles**](https://github.com/AVGVSTVS96/starter-dotfiles) | Minimal, agent-first macOS dotfiles for React and TypeScript development, including Ghostty, Herdr, Claude Code, Codex, LazyVim, Vite+, Nub, and basic shell tooling. |
| [**lhr0909/herdr-bel**](https://github.com/lhr0909/herdr-bel) | Forwards Herdr agent notifications to Zed Terminal Threads using the terminal bell signal. |

### REPL and code dispatchers

*1 project. Tools for sending code or commands from an editor to a running pane or interactive session.**

| Project | What it does |
|---|---|
| [**AbhijithAnirudhan2907/herdr-sidebar**](https://github.com/AbhijithAnirudhan2907/herdr-sidebar) | A fork of herdr-sidebar that adds an editor inside the pane, including save, syntax highlighting, undo and redo, and find and replace. |

### Editor plugins and bridges

*2 projects. General-purpose bridges that synchronize editor state with Herdr panes and agents.**

| Project | What it does |
|---|---|
| [**Daniel-Steinberger/obsidian-herdr**](https://github.com/Daniel-Steinberger/obsidian-herdr) | Sends the next unchecked Markdown task to an agent in the matching Herdr workspace and marks it complete when the agent finishes. Continuous mode can process an entire checklist. |
| [**aclima01/herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows) | A small Windows text editor that opens in a Herdr split, with a directory tree, syntax highlighting, and an uncommitted-diff tab. Files can be edited and staged without leaving the multiplexer. |

---

## 4. Switch and restore sessions

*64 projects. Pickers, switchers, snapshots, restoration tools, and managers for moving among persistent Herdr sessions.*

### Fuzzy session switchers and terminal pickers

*46 projects. Interactive pickers for finding and focusing workspaces, tabs, panes, agents, or projects.**

| Project | What it does |
|---|---|
| [**nicosuave/memex**](https://github.com/nicosuave/memex) | Indexes conversations from Claude Code, Codex, Pi, OpenCode, and Cursor with hybrid search. A Herdr TUI searches the archive and can resume a selected interaction in a fresh tab. |
| [**thanhdat77/herdr-picker-plus**](https://github.com/thanhdat77/herdr-picker-plus) | A Ratatui overlay that combines workspaces, project templates, directories, zoxide history, SSH hosts, agent panes, and plugin integrations. It reuses matching workspaces and can create or focus remote-host workspaces automatically. |
| [**thanhdat77/herdr-navigator**](https://github.com/thanhdat77/herdr-navigator) | Searches and switches between active Herdr sessions and workspaces using an interactive fuzzy picker. |
| [**andrewchng/herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer) | A tmux-sessionizer-style launcher for Herdr. Fzf selects projects or worktrees, while TOML defines tabs, splits, startup commands, repository-specific layouts, and preview panels. |
| [**code-yeongyu/web-terminal**](https://github.com/code-yeongyu/web-terminal) | A self-hosted, mobile-first web terminal built on Ghostty WASM, with sessions that survive disconnects, a file explorer, and Herdr integration. |
| [**jeffarese/herdr-bar**](https://github.com/jeffarese/herdr-bar) | A dependency-free Python command palette for jumping to any Herdr tab, agent, repository, or branch. |
| [**lmilojevicc/seshagy**](https://github.com/lmilojevicc/seshagy) | Provides tools for repositories, tmux sessions, and Herdr workspaces. It also shows running agent state before the user attaches. |
| [**AVGVSTVS96/herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr) | Uses fzf and the Herdr socket API to move live tabs and panes between workspaces without stopping their processes. |
| [**beyondlex/herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator) | A Rust popup that tracks recently focused workspaces, tabs, panes, and agents through socket events. It provides a live most-recently-used index, keyboard navigation, and fuzzy search. |
| [**marcoskichel/herdr-muster**](https://github.com/marcoskichel/herdr-muster) | Labels each Herdr workspace with live agent states such as working or blocked, making attention-heavy workspaces easy to spot. |
| [**maayanyosef/herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm) | Selects a running EC2 instance across AWS profiles and opens `herdr --remote` through AWS SSM. It uses temporary Instance Connect keys and automatic SSH-user detection, so no bastion, public IP, or stored key is required. |
| [**mr04vv/herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator) | A fuzzy tree for workspaces, tabs, and panes, sorted by agent urgency. Its preview shows directory, status, and recent scrollback so blocked or completed work can be triaged quickly. |
| [**ugurtarlig/herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency) | Ranks agents and workspaces by the time of their latest real Claude or Codex turn, bringing the most recently finished or stalled sessions to the top. |
| [**yoshiori/herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker) | A tree-style Herdr navigator with fully configurable keys, designed for shortcut layouts that conflict with input methods such as Japanese IMEs. |
| [**salkhalil/herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer) | A Herdr sessionizer that uses fzf to search open workspaces and zoxide directories, then creates or focuses a workspace with template tabs. |
| [**haphamdev/herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher) | Provides tools for active Herdr workspaces, tabs, and agents. Selecting an item immediately focuses the matching location. |
| [**ImArtisann/herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher) | Scans configured project roots and creates or focuses Herdr workspaces with one keyboard action. |
| [**ismaelosuna7824/herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces) | Keeps searchable history of workspace directories, refocuses active workspaces, restores older locations, and includes a filesystem browser for creating new workspaces. |
| [**kenchan/herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent) | Provides tools for ghq repositories that opens the selected project in a Herdr workspace or tab and starts Claude Code in that directory. |
| [**wraithyy/herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint) | Saves frequently used project directories as named waypoints in a small text file and opens them as new Herdr workspaces through fzf. |
| [**iiii1224/herdr-statusline**](https://github.com/iiii1224/herdr-statusline) | A configurable status line for Herdr sessions. |
| [**pawaca/even-better**](https://github.com/pawaca/even-better) | Mirrors live Claude Code and Codex sessions from Herdr to Even Realities G2 glasses using the even-terminal-compatible protocol. |
| [**j0urneyk/herdrctx**](https://github.com/j0urneyk/herdrctx) | A keyboard-driven TUI for finding, attaching to, creating, stopping, and deleting Herdr sessions. Prebuilt macOS and Linux binaries are available, and it prevents accidental nested launch from inside a Herdr pane. |
| [**alon-z/herdr-command-palette**](https://github.com/alon-z/herdr-command-palette) | A small fuzzy palette for open workspaces, configured project roots, and optional zoxide history. It focuses an existing workspace for a directory or creates one, without SSH or plugin-management features. |
| [**asumaran/herdr-goto**](https://github.com/asumaran/herdr-goto) | A Bubble Tea workspace switcher organized by repository and worktree. It supports fuzzy search, optional pane expansion, and automatic installation of prebuilt binaries. |
| [**joshuadavidthomas/hrd**](https://github.com/joshuadavidthomas/hrd) | Combines local and remote Herdr sessions with isolated sandboxes for discovery, inspection, and attachment across machines and containers. |
| [**pedroloch/herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close) | Restores recently closed panes or tabs, including their split hierarchy, directories, labels, and launched agents, through a shortcut or history picker. |
| [**shadowfax92/herdr-ferry**](https://github.com/shadowfax92/herdr-ferry) | A native Rust popup for moving running panes or whole tabs between Herdr workspaces without restarting them or requiring fzf or Node.js. |
| [**TheThoughtagen/attic**](https://github.com/TheThoughtagen/attic) | Finds idle coding-agent sessions, saves their state, and closes them to reclaim resources while keeping them restorable. A Textual dashboard and Herdr plugin support pinning, snoozing, and reviewing archived workspaces. |
| [**yxhta/herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker) | A Ratatui fuzzy-search popup with live previews of active agent panes. Pressing Enter focuses the selected session. |
| [**htlin222/herdr-agent-self-reload-skill**](https://github.com/htlin222/herdr-agent-self-reload-skill) | Re-prompts the agent in the current Herdr pane after a chosen delay. |
| [**KUKARAF/collie_voice_commands**](https://github.com/KUKARAF/collie_voice_commands) | A Rust and Tauri Android app that sends voice commands to Collie or Herdr sessions and produces spoken summaries through OpenRouter. |
| [**ridho9/switchr**](https://github.com/ridho9/switchr) | A full-screen Herdr session selector that shows each session with its workspace, tab, and pane tree. It can run at terminal startup and can offer to restart an incompatible daemon before attaching. |
| [**adamwangxx/herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume) | Opens Codex's native resume picker in a new Herdr split, preserving the current view while previous Codex sessions are browsed and resumed. |
| [**damianpoole/herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions) | Searches earlier OpenCode sessions by project, title, date, or transcript text. Conversation previews and shortcuts make it possible to resume or fork a result into a new Herdr pane. |
| [**dleen/herdr-agents**](https://github.com/dleen/herdr-agents) | Lists all active panes and puts blocked agents first. It shows live previews, jumps to existing workers, and can start new agents with one key. |
| [**iskwyuki/herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel) | A no-build popup panel using fzf to switch through workspace history, open paths, and run custom actions from Herdr key bindings. |
| [**mikedclarke/herdr-workspaces**](https://github.com/mikedclarke/herdr-workspaces) | Registers frequently used project directories and opens them through a fuzzy picker. Existing workspaces are focused instead of duplicated. |
| [**Joxtacy/herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault) | Browses earlier Claude Code sessions in a Herdr popup and resumes the selected conversation in a new tab. |
| [**vsem-azamat/herdr-telegram**](https://github.com/vsem-azamat/herdr-telegram) | Connects Telegram forum topics to stable Herdr agent sessions for ongoing remote conversations. |
| [**BradleyLWood/herdr-sessions**](https://github.com/BradleyLWood/herdr-sessions) | Provides managing Herdr sessions. The source catalog provides no specific feature list. |
| [**fjordlars/herdr-session-manager**](https://github.com/fjordlars/herdr-session-manager) | Provides tools for creating and managing named Herdr sessions. |
| [**Duzc01/herdr-session-finder**](https://github.com/Duzc01/herdr-session-finder) | Searches Claude Code sessions across all projects and resumes the selected conversation through a Herdr plugin. |
| [**JeremiahChurch/herd-remote**](https://github.com/JeremiahChurch/herd-remote) | Provides tools for starting, watching, and controlling Claude or Codex sessions in Herdr. |
| [**nickboy/herddeck**](https://github.com/nickboy/herddeck) | A Stream Deck control surface for local and remote Herdr agent sessions. |
| [**lsisoft/herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge) | Provides tools for Herdr sessions. It sends blocked-agent alerts and routes chat replies back to Herdr or tmux panes. |

### Persistence, snapshots, and state restoration

*11 projects. Tools that record layouts and process context, then rebuild or resume them after a restart.**

| Project | What it does |
|---|---|
| [**dmangla3/herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message) | Forks a Claude Code or Codex conversation from an earlier user message into a new tab, split pane, or workspace without modifying source transcripts. |
| [**nikok6/herdr-mirror**](https://github.com/nikok6/herdr-mirror) | Mirrors remote Herdr workspaces and agent state into a local sidebar over SSH or Docker. Remote panes can be watched and controlled alongside local ones. |
| [**ntindle/herdr-resurrect**](https://github.com/ntindle/herdr-resurrect) | Captures workspaces, tabs, panes, directories, and running agent processes so a complete Herdr environment can be restored after a crash or restart. |
| [**mo-arvan/herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry) | Detects Claude Code stalls caused by rate limits or server errors and safely resumes only idle or blocked panes, leaving actively working agents untouched. |
| [**iviaxpow3r/herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker) | Parks active panes and tabs outside the current working layout and restores them later with agent state and prompt progress intact. |
| [**moneycaringcoder/herdr-tether**](https://github.com/moneycaringcoder/herdr-tether) | Moves long-running terminal commands into background services so local or remote tasks continue after the main Herdr window closes. |
| [**bengemine/herdr-hibernate**](https://github.com/bengemine/herdr-hibernate) | Suspends idle Claude Code, Codex, or Grok panes to reduce memory use while keeping pane state and directory context. Pressing Enter resumes a hibernated session. |
| [**tomasvarga/herdr-e2b**](https://github.com/tomasvarga/herdr-e2b) | Copies the active Git worktree, including uncommitted changes, into an temporary E2B cloud sandbox and starts a remote agent there without requiring a push or remote branch. |
| [**nickmaglowsch/herdr-session-restore**](https://github.com/nickmaglowsch/herdr-session-restore) | Tags Claude Code panes with session IDs, saves the workspace, tab, and directory layout during a clean server stop, and rebuilds it on the next cold start using `claude --resume`. It is intentionally Claude-only and requires a clean shutdown. |
| [**Angel-O/herdr-agent-resume**](https://github.com/Angel-O/herdr-agent-resume) | Generates the exact resume command for an interrupted Claude Code, Codex, or custom agent session and either copies it or pastes it into a Herdr pane. |
| [**noviadi/herdr-layout**](https://github.com/noviadi/herdr-layout) | Saves Herdr pane splits and arrangements and restores the same workspace geometry later, similar to tmux-resurrect for layouts. |

### Workspace and multi-session management

*7 projects. Managers for creating, grouping, naming, attaching to, and cleaning up several sessions.**

| Project | What it does |
|---|---|
| [**third774/herdr-last-workspace**](https://github.com/third774/herdr-last-workspace) | Tracks workspace IDs and toggles between the current and previous workspace with one key. It remains correct after reordering and exits quietly if the earlier workspace was closed. |
| [**taxueseek/session-digger**](https://github.com/taxueseek/session-digger) | Indexes conversations from Claude Code, Codex, and other agents in SQLite FTS5. It also tracks token and cache data and creates local HTML reports for review. |
| [**den-tanui/herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide) | Uses zoxide's directory history when creating Herdr workspaces, tabs, and panes, making recent project paths quick to open. |
| [**douglascorrea/herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox) | A central inbox for Herdr agents that combines run time, workspace statistics, session titles, and unread state into one triage view. |
| [**to4iki/herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump) | Jumps to the next Herdr pane needing attention, prioritizing blocked agents before cycling through completed tasks. |
| [**dantehemerson/herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab) | Tracks tab focus history and returns to the previously active Herdr tab with one keystroke. |
| [**osamahbeig/herdr-grove**](https://github.com/osamahbeig/herdr-grove) | Displays projects and directories as a grouped tree in a Herdr popup and opens the selected workspace or folder by key or click. |

---

## 5. Worktrees and terminal experience

*359 projects. Git worktree automation, diff review, navigation, status displays, logs, and ready-made terminal configurations.*

### Git worktree automation

*99 projects. Tools that create isolated branches and worktrees for agents, then connect them to Herdr workspaces or tabs.**

| Project | What it does |
|---|---|
| [**persiyanov/herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr) | Provides an interactive diff review interface for inspecting agent changes and dispatching review feedback. |
| [**smarzban/herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer) | A read-only split-pane file viewer with a Git-status tree and automatic rendering for diffs, Markdown, or source code. It includes search, worktree switching, and optional integration with delta, bat, and glow. |
| [**devashish2203/herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk) | Provides tools for Worktrunk inside Herdr. It switches to existing worktrees or creates a branch with Worktrunk hooks, and its removal action checks for dirty or unmerged work first. |
| [**kenn-io/ghosthub**](https://github.com/kenn-io/ghosthub) | A power terminal for local and remote sessions that supports tmux, Herdr, and Zellij, with built-in Git worktree creation, isolation, and repository-specific setup. |
| [**alexarthurs/herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar) | A persistent sidebar combining a file explorer and Git controls. It includes syntax-highlighted previews, visual diffs, detailed change information, and AI-generated commit messages. |
| [**NathanFlurry/herdr-plugin-jj-workspace**](https://github.com/NathanFlurry/herdr-plugin-jj-workspace) | Adds key bindings for creating and removing Jujutsu workspaces through `jj workspace`, opening the result as a Herdr workspace or tab. |
| [**razajamil/herdr-plugin-workspace-manager**](https://github.com/razajamil/herdr-plugin-workspace-manager) | Defines tabs, splits, and startup commands in YAML and applies the layout whenever a new worktree opens. It can run a blocking setup command first and prune worktrees whose upstream branch has been removed. |
| [**tdi/herdr-worktree-setup**](https://github.com/tdi/herdr-worktree-setup) | Runs repository setup after Herdr creates a worktree, including copying `.env` files and executing commands such as `mise trust` and `direnv allow`, so the environment is ready immediately. |
| [**Crokily/herdr-lazygit**](https://github.com/Crokily/herdr-lazygit) | Runs lazygit in a Herdr sidebar with shortcuts for opening, expanding, and staging changes, plus AI-assisted commit-message generation from the pending diff. |
| [**wyattjoh/herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr) | Shows the GitHub pull-request number and CI state for the focused agent pane's branch in the Herdr sidebar. Updates are rate-limited, with shortcuts for manual refresh and opening the pull request. |
| [**ribbons-digital/pi-herd**](https://github.com/ribbons-digital/pi-herd) | Provides visible Pi session orchestration through Herdr panes and isolated Git worktrees. |
| [**edmundmiller/herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk) | Adds six Hunk actions for worktree, staged, and branch diffs, each opening in either a split or a new tab. The active workspace and selected Herdr theme are passed to Hunk automatically. |
| [**tdi/herdr-worktree-from-linear**](https://github.com/tdi/herdr-worktree-from-linear) | Searches active Linear issues, then creates or focuses a matching Git worktree and Herdr workspace. An optional split shows the issue description and assignee. |
| [**wyattjoh/herdr-plugin-renamer**](https://github.com/wyattjoh/herdr-plugin-renamer) | Renames numbered tabs from the agent's first prompt and can also rename an automatically linked worktree's branch and workspace. The short task name is generated locally with Apple Foundation Models or Codex. |
| [**dwarvesf/herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook) | Previews a file path from the clipboard in an overlay and can expand it into a full terminal viewer, avoiding manual path entry or temporary splits. |
| [**EzraCerpac/jj-waltz**](https://github.com/EzraCerpac/jj-waltz) | An interactive Jujutsu workspace switcher that maps `jj` workspace directories to Herdr tabs and workspaces for parallel version-control tasks. |
| [**freethinkel/herdr-plugin-git-worktree-hooks**](https://github.com/freethinkel/herdr-plugin-git-worktree-hooks) | Runs global YAML-configured shell hooks when Git worktrees are created or removed. Hooks receive paths and event metadata, and executions are recorded durably. |
| [**hotchpotch/herdr-tiny-fingers**](https://github.com/hotchpotch/herdr-tiny-fingers) | Adds tmux-fingers-style labels to visible URLs, commit hashes, and file paths. Typing a short hint copies the selected token without using a mouse. |
| [**tdi/herdr-worktree-from-pr**](https://github.com/tdi/herdr-worktree-from-pr) | Creates an isolated Git worktree from a GitHub pull request and opens it as a new Herdr workspace in one operation. |
| [**scott306lr/herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff) | Opens Hunk in a companion split whenever an agent finishes a turn with uncommitted changes, while leaving focus on the agent pane. |
| [**simoncrypta/agentic-dev-setup**](https://github.com/simoncrypta/agentic-dev-setup) | A shareable development layout combining Herdr and Worktrunk for agent-oriented coding workflows. |
| [**persiyanov/herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree) | Updates a newly created worktree branch to `origin HEAD` while protecting any branch with an upstream, a remote counterpart, local changes, or unique commits. Automated tests cover the safety checks and repeat runs. |
| [**hmu332233/herdr-symlink-worktree**](https://github.com/hmu332233/herdr-symlink-worktree) | Symlinks declared ignored files, environment files, and caches from the main checkout into new worktrees without replacing files that already exist. |
| [**jlimas/herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed) | Seeds new Node.js worktrees with copy-on-write `node_modules` and project dotfiles, reducing duplicated storage and setup time for temporary agent branches. |
| [**tanshio/herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude) | Copies gitignored environment and configuration files into new worktrees from standard `.worktreeinclude` patterns when Herdr reports creation. |
| [**qdentity/herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle) | Routes worktree lifecycle events to setup and teardown scripts stored in the repository itself. Events are serialized per path, so each project owns its provisioning logic while the plugin handles delivery. |
| [**shizlie/herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap) | Reads `worktree_init.toml` when a worktree is created, runs a configured command, and copies selected ignored files or directories from the main checkout. An idempotency marker prevents repeated setup. |
| [**kkckkc/herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow) | Takes a GitHub issue number, creates a branch and worktree through `gh issue develop`, and builds a Herdr workspace from the repository's `herdr-workspace.yaml` layout. |
| [**azizuysal/herdr-workbench**](https://github.com/azizuysal/herdr-workbench) | An IDE-style Herdr sidebar with collapsible files, live text search, Git status groups, syntax-highlighted previews, editor handoff, and quick-look views. |
| [**cdowell09/herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board) | Combines open pull requests from several repositories and shows CI, review, and branch state beside agent workspaces. |
| [**JacquesvanWyk/herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit) | Opens lazygit in a Herdr split or tab and intelligently opens, focuses, or closes it based on the current state, while preserving orientation and working directory. |
| [**osolmaz/herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup) | Returns idle panes to the default Git branch after a feature branch is merged or deleted on GitHub, but only when the tree is clean and no agent is actively typing. |
| [**qq88976321/herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search) | Adds incremental regular-expression search to pane history and copies matched URLs, Git hashes, or file paths through OSC 52, combining tmux-copycat and extrakto-style behavior. |
| [**thomasschafer/herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk) | A fuzzy launcher that scans local repositories and branch checkouts and opens them as Herdr workspaces or worktrees. TOML settings control scan depth, key overlays, and startup pane recipes. |
| [**timofey-TK/herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks) | Runs custom setup and teardown commands when a Herdr worktree is created, opened, or removed. |
| [**SirTenzin/superherd**](https://github.com/SirTenzin/superherd) | Connects the Superset workspace manager to Herdr. One command creates a worktree and Herdr workspace, mirrors Superset setup terminals as tabs, forwards interrupts, and removes the launcher pane when setup completes. |
| [**mattarau/wt-herdr**](https://github.com/mattarau/wt-herdr) | Keeps Worktrunk worktrees and Herdr workspaces synchronized. Workspace creation, removal, and focus follow Worktrunk changes, with health checks, dry runs, and lifecycle notifications. |
| [**danilolucasmd/herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout) | Uses the currently arranged tabs and splits as a live template and copies that layout into every newly created Herdr worktree, without a separate configuration file. |
| [**JacquesvanWyk/herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk) | Combines an fzf Hunk diff picker with a hook that opens a diff split when an agent finishes. It reuses existing viewers and skips clean repositories. |
| [**jsmenzies/mergr**](https://github.com/jsmenzies/mergr) | Adds compact GitHub pull-request and review indicators to Herdr workspace rows by periodically checking the branch associated with each workspace. |
| [**LeonardoTrapani/herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) | Prepares JavaScript and TypeScript worktrees by detecting lockfiles, installing dependencies, and restoring untracked environment configuration before agents begin work. |
| [**mroth/herdr-jj-status**](https://github.com/mroth/herdr-jj-status) | Displays Jujutsu bookmarks, working-copy state, and change IDs in Herdr workspace rows and updates them as agents modify or switch workspaces. |
| [**serhii-chernenko/herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude) | Supports custom worktree target locations and copies files matched by `.worktreeinclude`, following Claude CLI behavior for local environment setup. |
| [**dkarter/hwt**](https://github.com/dkarter/hwt) | Provides tools for simplifying Herdr worktree orchestration. The source catalog provides no detailed feature list. |
| [**ditwrd/herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk) | A remote Herdr workspace setup built around Worktrunk. The source catalog does not describe the workflow further. |
| [**noamsiegel/git-wt-herdr**](https://github.com/noamsiegel/git-wt-herdr) | Automates Git worktree creation and lifecycle management by mapping worktrees directly to Herdr tabs. |
| [**peterferguson/herdr-conductor-worktree**](https://github.com/peterferguson/herdr-conductor-worktree) | Creates worktrees in Conductor's expected directory structure, registers them in Conductor's database, and provides a synchronization pane for opening active workspaces and closing archived ones. |
| [**mkdir700/herdr-config**](https://github.com/mkdir700/herdr-config) | A portable Herdr configuration with worktree settings, LazyVim-style keys, and small plugins for diff review, copying workspace paths, opening lazygit, and showing pull-request status. |
| [**aleslanger/herdr-strays**](https://github.com/aleslanger/herdr-strays) | Provides tools for finding and removing abandoned Git worktrees from parallel agent runs. It shows project trees and live diffs and can send follow-up prompts to Claude Code panes. |
| [**baotran01/herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff) | An in-pane viewer for reviewing unstaged Git and filesystem changes made by agents before approval, with clean patch summaries beside the agent output. |
| [**bfreed/herdr-corral**](https://github.com/bfreed/herdr-corral) | A Herdr-focused replacement for workmux that creates Git worktrees, branch-specific environment files, dependencies, and tabs for agents, shells, and development servers, with merge-aware cleanup. |
| [**blurname/herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name) | Keeps Herdr tab labels synchronized with the Git branch in the focused pane. |
| [**brianh20/herdr-stagr**](https://github.com/brianh20/herdr-stagr) | Adds a source-control sidebar for staging, unstaging, and discarding changes with side-by-side diffs inside Herdr. |
| [**chouxcreams/herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard) | A Ratatui pull-request dashboard covering all workspaces and panes. A background service caches CI and approval state, and keyboard actions jump to the responsible pane or open the pull request. |
| [**crexi/herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy) | Reads a `.worktree-copy` manifest when Herdr creates a worktree and copies environment files or symlinks shared directories from the main checkout. |
| [**cyperx84/herdr-notes**](https://github.com/cyperx84/herdr-notes) | Creates a separate Markdown scratchpad for each Herdr workspace ID. Notes and prompt drafts open in a side split and stay outside the Git working tree. |
| [**Feasy01/herdr-allow**](https://github.com/Feasy01/herdr-allow) | Copies allowlisted, uncommitted files such as secrets, environment settings, and local configuration into new worktrees based on a `.herdr-allow` file. |
| [**jorge-huxley/herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph) | A read-only commit-graph TUI with ASCII branch lanes, branch filters, commit search, and on-demand diffs inside a Herdr pane. |
| [**kbrdn1/herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm) | Adds popup menus for the `gwm` worktree CLI, including create, switch, clean, and batch commands, while adopting worktrees as Herdr workspaces and keeping `gwm` as the source of truth. |
| [**mattyan1053/herdr-compose**](https://github.com/mattyan1053/herdr-compose) | Shows Docker Compose service health for each workspace in the Herdr sidebar, with quick toggles and a service-details popup. Compose stacks are removed when their worktrees are deleted. |
| [**rotemb-wond/herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints) | Places short keyboard labels over visible paths, commit hashes, and URLs. Typing a label copies the matching text to the system clipboard. |
| [**mkdir700/herdr-plugin-worktree**](https://github.com/mkdir700/herdr-plugin-worktree) | Creates a Git worktree from a GitHub issue, pull request, or branch name, automatically detecting the input type and using Claude-generated naming where supported. |
| [**jal-co/pi-herdr-worktree**](https://github.com/jal-co/pi-herdr-worktree) | Provides tools for managing Git worktrees through Herdr's native API, with project-level hooks before removal and after creation. |
| [**ralphcrisostomo/herdr-goal-skill**](https://github.com/ralphcrisostomo/herdr-goal-skill) | Provides tools for splitting a goal among parallel lead agents in Herdr worktrees, with model tiering and self-updating coordination. |
| [**beomjungil/herdr-lazygit-overlay**](https://github.com/beomjungil/herdr-lazygit-overlay) | Opens lazygit as an overlay using the focused pane's working directory, then restores the previous focus and zoom state when lazygit exits. |
| [**ynny-github/herdr-event-hook**](https://github.com/ynny-github/herdr-event-hook) | Reads a committed `.herdr-event-hook.toml` and runs configured commands when worktrees are created or removed, making it possible to start and stop per-worktree services automatically. |
| [**asumaran/gotopr**](https://github.com/asumaran/gotopr) | Finds open GitHub pull requests across local repositories and worktrees, then focuses the Herdr workspace that matches the selected review branch. |
| [**disintegrator/trunkr**](https://github.com/disintegrator/trunkr) | Connects Worktrunk worktree operations to persistent Herdr workspaces so creation, switching, and cleanup remain synchronized. |
| [**kazimshah39/herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter) | Filters the Herdr agent sidebar to workspaces whose names share a chosen suffix, reducing noise in large multi-repository fleets. |
| [**khatriafaz/herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename) | Uses the first agent prompt to rename the active Herdr workspace and Git branch so task names remain descriptive without manual editing. |
| [**langtind/gren-herdr**](https://github.com/langtind/gren-herdr) | Connects the `gren` worktree manager to Herdr for creating, switching, and removing worktrees mapped to tabs, including gren's post-creation setup hooks. |
| [**mariotmc/herdr-source-control**](https://github.com/mariotmc/herdr-source-control) | A lightweight source-control pane showing changed files, the current branch, and upstream synchronization. Background polling and focus events keep the display current. |
| [**nimrc/herdr-git-pull**](https://github.com/nimrc/herdr-git-pull) | Runs `git pull` for the active workspace in an overlay. It finds the repository root from subdirectories or linked worktrees and opens an interactive shell if conflicts need attention. |
| [**scoussens-nthplusio/herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include) | Copies ignored and untracked files into new Herdr worktrees according to repository `.worktreeinclude` rules compatible with Claude Code. |
| [**sfroment/herdr-git-detail**](https://github.com/sfroment/herdr-git-detail) | Adds a `$git_detail` sidebar token with modified, staged, untracked, ahead, behind, and stash counts, refreshed when pane focus changes. |
| [**tjg184/herdr-worktree**](https://github.com/tjg184/herdr-worktree) | Connects Worktrunk hooks and native Git worktree operations to Herdr workspaces and tabs, including dependency installation and environment propagation for newly created checkouts. |
| [**zerodice0/herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) | Copies ignored local configuration, environment files, and credentials into new worktrees and runs required setup commands so agent panes can start working immediately. |
| [**spirin22/herdr-plugins**](https://github.com/spirin22/herdr-plugins) | Provides seeding new worktrees with ignored files and running project-specific setup steps. |
| [**kennethkoontz/herdr-worktree-sync**](https://github.com/kennethkoontz/herdr-worktree-sync) | Copies ignored files selected by `.worktreeinclude` into new worktrees, then allows and reloads direnv at the new root. |
| [**arjenblokzijl/herdr-worktree-autosetup**](https://github.com/arjenblokzijl/herdr-worktree-autosetup) | Runs a configured setup command in a visible pane whenever Herdr creates a Git worktree. |
| [**eightHundreds/herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude) | Copies gitignored files selected by `.worktreeinclude` into new Herdr worktrees. |
| [**riclib/herdr-worktree-layout**](https://github.com/riclib/herdr-worktree-layout) | Automatically builds a fixed worktree layout containing a file viewer and two shells, using defined 60/40 and 75/25 splits. |
| [**untalfranfernandez/herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude) | Populates every new Herdr worktree with local ignored files such as `.env`, editor settings, and fixtures, using Claude Code-compatible `.worktreeinclude` patterns. |
| [**botonddombi/boti-toolkit**](https://github.com/botonddombi/boti-toolkit) | A personal development toolkit with Herdr worktree helpers, a machine-setup playbook, and a Claude Code setup agent. |
| [**snics/herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab) | Creates a Git worktree and Herdr workspace from a GitLab issue through the `glab` CLI. |
| [**dabeeeenster/herdr-worktree-local-files**](https://github.com/dabeeeenster/herdr-worktree-local-files) | Links ignored local configuration files from the main checkout into newly created Git worktrees. |
| [**toyamarinyon/herdr-worktree-setup**](https://github.com/toyamarinyon/herdr-worktree-setup) | Runs a setup script committed to the repository whenever Herdr creates a new worktree. |
| [**AndreGeng/herdr-worktree-dispatcher**](https://github.com/AndreGeng/herdr-worktree-dispatcher) | Dispatches coding tasks into temporary Git worktrees and starts an agent in each checkout. The public entry point is `scripts/dispatch.sh`, backed by a compiled TypeScript command-line implementation. |
| [**wthorp/squeeze-chute**](https://github.com/wthorp/squeeze-chute) | Coordinates GitHub issues through isolated Herdr worktree teams. |
| [**mopeneko/herdr-worktree-hook-plugin**](https://github.com/mopeneko/herdr-worktree-hook-plugin) | Runs user-defined shell commands immediately after a new worktree is created, providing a simple post-create hook for Herdr. |
| [**mholtzscher/herdr-worktree-picker**](https://github.com/mholtzscher/herdr-worktree-picker) | Creates Herdr worktrees from either local or remote Git branches. |
| [**arjenblokzijl/herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner) | Runs repository-specific setup in a visible pane inside each new worktree, with a deliberately simple and composable design. |
| [**hung-eggie-do-covergo/delegate-orchestrator**](https://github.com/hung-eggie-do-covergo/delegate-orchestrator) | Starts one isolated Claude Code subagent per repository through Herdr worktrees, with multi-repository coordination, worktree reuse, and session resumption. |
| [**m1sk9/herdr-worktree-hooks-plugin**](https://github.com/m1sk9/herdr-worktree-hooks-plugin) | Adds configurable lifecycle hooks to Herdr worktree operations. |
| [**QuentinTorg/stagehand**](https://github.com/QuentinTorg/stagehand) | A human-guided workflow connecting Herdr worktrees, author and reviewer agents, Hunk feedback, and GitHub pull-request handoff. |
| [**eoinest/convo-history**](https://github.com/eoinest/convo-history) | A voice scratchpad that turns a recent window of speech into a Codex prompt in a fresh Herdr worktree, triggered by a hotkey or wake word. |
| [**firew0rks/herdr-ci-tokens**](https://github.com/firew0rks/herdr-ci-tokens) | Shows pull-request, CI, and review state for every worktree in the Herdr sidebar. |
| [**sample-usr/herdr-devenv-worktree**](https://github.com/sample-usr/herdr-devenv-worktree) | Provides tools for using devenv inside Git worktrees. |
| [**danieljvdm/herdr-worktrunk**](https://github.com/danieljvdm/herdr-worktrunk) | Integrates Worktrunk worktree management with Herdr as a plugin. |

### Workspace lifecycle and multi-repository tools

*4 projects. Higher-level utilities for starting, tracking, and removing workspaces that span one or more repositories.**

| Project | What it does |
|---|---|
| [**tomaszhanc/herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins) | A monorepo of Herdr plugins, each packaged in its own directory with a manifest and executable. |
| [**tyler-jewell/herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins) | A standard-library-first monorepo of Herdr plugins written entirely in Rust. |
| [**shelken/herdr-plugins**](https://github.com/shelken/herdr-plugins) | A Herdr plugin monorepo that includes an auto-Pi launcher by area and a session picker. |
| [**paulrobello/par-herdr-plugins**](https://github.com/paulrobello/par-herdr-plugins) | A monorepo of custom Herdr plugins. The source catalog does not list the individual plugins. |

### Diff review and code inspection

*21 projects. Side-by-side git diff inspection and comment handoff tools for agent reviews.*

| Project | What it does |
|---|---|
| [**osolmaz/ghzinga**](https://github.com/osolmaz/ghzinga) | A focused TUI for one GitHub issue or pull request. Clicked GitHub links in Herdr can open in a side split with review and comment actions. |
| [**plannotator/herdr-plannotator**](https://github.com/plannotator/herdr-plannotator) | Embeds Plannotator plan reviews in a dedicated Herdr browser pane so plans can be annotated, discussed, and approved beside active coding sessions. |
| [**tomasvarga/herdr-pickr**](https://github.com/tomasvarga/herdr-pickr) | Intercepts clicked GitHub pull-request and GitLab merge-request links and opens their diffs in tuicr, Hunk, or a browser, with an optional AI first-pass review. |
| [**krystof018/herdr-git-status**](https://github.com/krystof018/herdr-git-status) | Shows GitHub or GitLab CI state in workspace labels and an on-demand pane. It includes pull-request or merge-request numbers, recent failures, clickable links, and review-state markers. |
| [**flupke/herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer) | A turn-by-turn diff reviewer that presents the changes from each agent cycle for incremental inspection before another run is approved. |
| [**arvindparmar-me/herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer) | Previews a selected Markdown file path in a right-hand Herdr split through a single shortcut. |
| [**dzwduan/herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index) | Builds a navigable index of user and assistant turns for Claude Code sessions in Herdr, making long conversations easier to review without scrolling through raw terminal history. |
| [**speardragon/herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox) | Collects blocked Claude `AskUserQuestion` prompts from all Herdr workspaces into one popup, where pending questions can be reviewed and answered safely. |
| [**Tomatio13/herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail) | A keyboard-driven Gmail browser inside a Herdr split, using `gogcli` and fzf to navigate mail and render HTML messages as readable text previews. |
| [**yuucu/herdr-hunk**](https://github.com/yuucu/herdr-hunk) | Provides tools for browsing modified files and opening interactive diffs in a split or tab, optionally whenever an agent finishes with uncommitted changes. |
| [**Volpestyle/herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview) | Shows live Mermaid diagram previews for Claude Code and Codex output inside Herdr. |
| [**edmundmiller/herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview) | Detects GitHub issue and pull-request links in the active pane and opens their details in a neighboring split through the GitHub CLI. |
| [**maedana/herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview) | Tiles previews of all active agent panes while giving most of the terminal to the focused worker, preserving awareness of background agents without crowding the main task. |
| [**quantk/herdr-review**](https://github.com/quantk/herdr-review) | Opens the agent's working-tree diff in a split or tab, supports line comments, and drafts the notes into the source agent's prompt without submitting them. It runs on Bun or Node without external diff tools. |
| [**robert-flo/herdr-terminal-file-manager**](https://github.com/robert-flo/herdr-terminal-file-manager) | Finds the focused pane's directory and opens the Elio terminal file manager there, providing previews, inline images, and batch file operations inside the workspace. |
| [**CyPack/herdr-plugins**](https://github.com/CyPack/herdr-plugins) | File-manager extensions for the CyPack Herdr fork that preview spreadsheets, images, PDFs, and text files. |
| [**dannycroft/hunk-herdr-plugin**](https://github.com/dannycroft/hunk-herdr-plugin) | Provides tools for opening Hunk diffs in either a Herdr split or a tab. |
| [**cevr/herdr-hunk**](https://github.com/cevr/herdr-hunk) | Routes Hunk review notes back to the correct Herdr agent pane. |
| [**caoer/ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout) | Provides tools for Herdr with live previews. |
| [**devenjarvis/herdr-review**](https://github.com/devenjarvis/herdr-review) | Adds an interactive plan-review stage to Herdr workflows. |
| [**pi-dal/herdr-preview**](https://github.com/pi-dal/herdr-preview) | A diff-first review pane with restricted file browsing, comments, and image previews. |

### File viewers and markdown previews

*19 projects. In-terminal file browsers, image previews, and markdown rendering panes.*

| Project | What it does |
|---|---|
| [**sh1ma/herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title) | Runs in the background and derives Herdr tab names from the topic and intent of Claude Code or Codex conversations. |
| [**iurysza/termscope**](https://github.com/iurysza/termscope) | Finds visible file paths and web links on the terminal screen, lets the user select one with fuzzy search, and opens it in a separate split without disturbing the main pane. |
| [**alexarthurs/herdr-notes**](https://github.com/alexarthurs/herdr-notes) | Keeps one persistent Markdown note per workspace, with rendered and edit modes, autosave, and restoration after restarts. |
| [**Phoobobo/herdr-workboard**](https://github.com/Phoobobo/herdr-workboard) | A Kanban-style TUI that represents Herdr workspaces as boards, task states as tabs, and active agent sessions as panes, with direct navigation from cards to terminals. |
| [**devskale/herdr-flist**](https://github.com/devskale/herdr-flist) | Opens a narrow directory sidebar beside the focused pane and follows its current directory, including remote SSH shells where the path is parsed from the prompt. Entries are directory-first and include Git status markers. |
| [**jagzmz/herdr-annotations**](https://github.com/jagzmz/herdr-annotations) | Attaches local annotations to selected terminal text and groups them into reusable collections. Line-specific notes can be combined into one feedback prompt for an agent. |
| [**takemo101/wave-tui**](https://github.com/takemo101/wave-tui) | A terminal internet-radio player with an Agent Planets view, where Herdr agents orbit an audio visualizer according to live state and panes remain directly accessible. |
| [**opsydyn/herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer) | A 16-bit fantasy guild overlay for live agent sessions. Working agents appear on quests, blocked agents request help, and completed runs return to the guild according to real Herdr state. |
| [**ShankyJS/herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents) | Limits the agent sidebar to workers in the currently focused workspace, reducing unrelated fleet noise when moving between projects. |
| [**alon-z/herdr-devup**](https://github.com/alon-z/herdr-devup) | Reads `.herdr/dev.toml` to start a project's tabs, panes, and services, refresh an ngrok URL across configured environment files, and close only the tabs it created. |
| [**ramarivera/herdr-pretty-which**](https://github.com/ramarivera/herdr-pretty-which) | A Rust and Ratatui which-key popup that combines default and custom Herdr bindings. It supports searchable tree and list views with themes that adapt to terminal contrast. |
| [**rvalledorjr/herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh) | Embeds the Fresh terminal IDE in a side pane and follows the active workspace root for quick file browsing and editing beside agents. |
| [**ppggff/herdr-plugin**](https://github.com/ppggff/herdr-plugin) | Remembers the macOS keyboard input source used in each Herdr pane and restores it when focus returns, using a bundled Swift helper or macism. |
| [**lucasleon2107/herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync) | Updates Herdr tab labels from agent conversation titles and prompt summaries, allowing names to change as the task evolves. |
| [**narumiruna/herdr-plugins**](https://github.com/narumiruna/herdr-plugins) | A collection of independently installable, dependency-free Rust plugins for Herdr, including a popup GitHub pull-request viewer. |
| [**Royal-lobster/herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup) | Shows a configurable launcher in every new Herdr tab. Tools are defined in JSON and start directly in the selected pane with normal agent detection. |
| [**ryanlewis/herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer) | Renames tabs from the active agent's session title or working directory, replacing generic numbers with current task context. |
| [**carellano/herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers) | Detects development servers running in Herdr panes, records their ports and process state, and can focus or safely stop orphaned services. |
| [**cpcloud/herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview) | Combines active AgentsView sessions across projects, models, and agents, with real-time timelines and metrics inside Herdr. |

### Pane navigation and overlay hints

*12 projects. Direct 1-character overlay hints and smart directional pane jumping.*

| Project | What it does |
|---|---|
| [**JanTvrdik/herdr-command-palette**](https://github.com/JanTvrdik/herdr-command-palette) | Opens an fzf overlay containing every action from every installed plugin. It preserves the originating workspace directory, runs the selected action, and removes the temporary overlay afterward. |
| [**rmarganti/herdr-pluck**](https://github.com/rmarganti/herdr-pluck) | Adds one- and two-letter hints for copyable terminal tokens, including URLs, paths, hashes, UUIDs, IP addresses, Kubernetes references, and hexadecimal values. |
| [**KonstantinKai/herdr-harpoon**](https://github.com/KonstantinKai/herdr-harpoon) | Provides tools for frequently used Herdr panes. Numeric shortcuts jump to saved panes, using only shell scripts and the Herdr CLI. |
| [**The-Dave-Stack/herdr-keymap**](https://github.com/The-Dave-Stack/herdr-keymap) | Displays all Herdr key bindings in an overlay and can run bindings that have an equivalent command-line action. |
| [**malone-c/herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search) | Parses Herdr key bindings into an fzf overlay for searching and running configured actions without memorizing every shortcut. |
| [**jeffarese/herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus) | Replaces the normal new-tab action with a directory and project picker that includes autocomplete, recent locations, and an optional agent to start. If the directory is already open, it focuses that workspace instead. |
| [**maedana/herdr-hint**](https://github.com/maedana/herdr-hint) | Displays Vimium-style single-letter labels over active tabs and agent panes so focus can jump directly to a target without cycling through the layout. |
| [**wraithyy/herdr-hintr**](https://github.com/wraithyy/herdr-hintr) | An early which-key-style popup that shows available Herdr shortcuts and can run the selected action. |
| [**yigitkg/herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths) | Finds file and folder paths mentioned in recent pane output and opens them with the operating system or reveals them in a file manager. When several paths exist, a picker lists files before folders. |
| [**RooseveltAdvisors/herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap) | Provides EasyMotion or Leap-style character jumps and selection-to-copy inside Herdr terminal panes. |
| [**stappmus/Udder**](https://github.com/stappmus/Udder) | Shows Herdr agents in the Omarchy bar, notifies when work finishes, and jumps back to the relevant pane. |
| [**vjeantet/herdr-mission-control**](https://github.com/vjeantet/herdr-mission-control) | Opens a full-screen overlay showing every pane of the current workspace as a live tile grouped by tab, with styled ANSI previews and agent status. Arrows or `hjkl` move the selection, `Enter` focuses the pane, and `Backspace` closes it without leaving the overview. |

### Terminal keybindings and shortcut helpers

*81 projects. Custom keymap packs, leader-key setups, and prefix-free navigation.*

| Project | What it does |
|---|---|
| [**yuk1ty/herdr-spreader**](https://github.com/yuk1ty/herdr-spreader) | Builds complete Herdr layouts from YAML, including tabs, splits, directories, startup commands, and dependencies that wait for output patterns before launching later panes. |
| [**benkraus/herdr-mobile**](https://github.com/benkraus/herdr-mobile) | A native iOS and Android control surface for persistent Herdr sessions. The source description is incomplete beyond its mobile-control purpose. |
| [**qu8n/herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename) | Renames tabs from the active foreground process and icon, and prefixes workspaces, tabs, and agents with numbers 1 through 9 for quick visual and keyboard selection. |
| [**yigitkonur/native-shortcuts-herd**](https://github.com/yigitkonur/native-shortcuts-herd) | Adds browser-style macOS shortcuts such as `Cmd+T`, `Cmd+W`, and numbered tab selection across Ghostty and Herdr. It uses a separate Ghostty sidecar config, creates backups, and includes a clean uninstall path. |
| [**oscabriel/pi-herdr-btw**](https://github.com/oscabriel/pi-herdr-btw) | A Pi extension distributed as `pi-herdr-btw`. The source catalog does not describe its features beyond the install command. |
| [**speardragon/herdr-yazi**](https://github.com/speardragon/herdr-yazi) | Opens the Yazi file manager in a Herdr pane or tab at the current directory while reusing the user's existing Yazi configuration. |
| [**Davidcreador/herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard) | Provides tools for Pi and OpenCode token use, cost, model, messages, and tool breakdowns across panes. It refreshes live and shows a Herdr toast with the final cost when an agent finishes. |
| [**Taeyoung96/herdr-dotfiles**](https://github.com/Taeyoung96/herdr-dotfiles) | A ready-to-use Herdr configuration with prefix-free pane movement, `Ctrl+Space` as the prefix, Catppuccin styling, and a global agent panel. The installer symlinks the file and backs up the previous config. |
| [**markhuot/herdr-equalize-splits**](https://github.com/markhuot/herdr-equalize-splits) | Balances all split dimensions in the current tab with one shortcut, equalizing panes by rows or columns after manual resizing or new splits. |
| [**aliou/herdr-cast**](https://github.com/aliou/herdr-cast) | A macOS plugin combining agent notifications, fuzzy workspace switching, zoxide-based creation, and layout helpers. |
| [**htlin222/herdr-gamepad**](https://github.com/htlin222/herdr-gamepad) | Maps Xbox, PlayStation, and 8BitDo controller buttons to Herdr actions through macOS GameController, enabling workspace and pane control away from the keyboard. |
| [**aclima01/herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows) | Sends native Windows 11 toast notifications when a Herdr agent finishes a turn or asks for input. |
| [**hrdle/hrdle**](https://github.com/hrdle/hrdle) | Web frontend tools for `hrdle` or Herdr. The source catalog provides no additional explanation. |
| [**milkyskies/herdr-attention**](https://github.com/milkyskies/herdr-attention) | Moves focus to the next agent needing attention with one key, checking blocked agents before completed ones. |
| [**kamaaina/herdr_sync**](https://github.com/kamaaina/herdr_sync) | Sends the command currently typed in one pane to every other pane in the same tab, providing synchronized-pane behavior for Herdr. |
| [**devoc09/herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit) | Splits the active pane vertically and immediately equalizes all column widths through Herdr's layout API. |
| [**HexSleeves/herdr-warp**](https://github.com/HexSleeves/herdr-warp) | Opens Herdr workspaces as native Warp tabs and splits on macOS, using Warp's window controls while Herdr continues to manage the underlying agents. |
| [**jagzmz/herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard) | Uploads a clipboard screenshot to S3-compatible storage and pastes a public or signed URL into the active Herdr pane for use with vision-capable agents. |
| [**StructuPath/herdr-guard**](https://github.com/StructuPath/herdr-guard) | Applies command-safety rules across Herdr panes and blocks dangerous operations such as force pushes, recursive deletion, and arbitrary base64 execution before they run. |
| [**Tyru5/herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state) | Shows real-time, human-readable summaries of what each agent in the current Herdr workspace is doing. |
| [**jeph/herdr-pane-balancer**](https://github.com/jeph/herdr-pane-balancer) | Automatically retile and equalizes Herdr panes whenever a pane is created, closed, or exits. |
| [**astkaasa/herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard) | Opens the existing Tokscale token and cost dashboard in a Herdr split and exposes a JSON quick action without reimplementing Tokscale. |
| [**3mmdrew/herdr-layout**](https://github.com/3mmdrew/herdr-layout) | Defines and creates Herdr workspace layouts in plain Lua, including pane splits and startup commands, without YAML or a separate service. |
| [**aclima01/herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows) | A Windows task panel that follows agent `TaskCreate` and `TaskUpdate` events and shows planned stages and current progress in real time. |
| [**jugyo/herdr-nav-history**](https://github.com/jugyo/herdr-nav-history) | Adds browser-style back and forward navigation across panes, tabs, and workspaces by recording focus changes from the Herdr socket event stream. |
| [**retroaalto/herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav) | Moves geometrically between panes based on their actual position, providing natural up, down, left, and right navigation in irregular Herdr grids. |
| [**Sawakee/herdr-imebox**](https://github.com/Sawakee/herdr-imebox) | Provides an IME-friendly popup for composing Japanese, Chinese, and other multibyte text before sending the completed string to an agent pane through the socket API. |
| [**shadowfax92/herdr-talon**](https://github.com/shadowfax92/herdr-talon) | Adds spoken Talon labels to visible Herdr targets for hands-free movement between panes. |
| [**yuuta1219/herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin) | Tracks Claude Code token use with a pachislot-style counter, jackpot animations, and daily resets inside Herdr. |
| [**shadowfax92/herdr-layouts**](https://github.com/shadowfax92/herdr-layouts) | Adds tmux-style narrow splits and focused-pane equalization to Herdr. |
| [**bestony/herdr-codex-capacity-retry**](https://github.com/bestony/herdr-codex-capacity-retry) | Automatically continues Codex sessions in Herdr after capacity-related interruptions. |
| [**twadams21/cc-controller**](https://github.com/twadams21/cc-controller) | Maps SDL game controllers to Herdr socket commands for navigation, scrolling, and voice mode. The controller may be local or connected from another machine over SSH. |
| [**a-curious-coder/herdr-plugin-manager**](https://github.com/a-curious-coder/herdr-plugin-manager) | An fzf plugin manager for finding, installing, updating, enabling, and disabling Herdr plugins from the public registry. It also stops orphaned background services when a plugin is turned off. |
| [**AsgardMuninn/herdr-plugin-orbstack**](https://github.com/AsgardMuninn/herdr-plugin-orbstack) | Creates and manages OrbStack Linux virtual machines as Herdr workspaces, using native shell attachment with SSH fallback and synchronized state. |
| [**chantlong/herdr-habitat**](https://github.com/chantlong/herdr-habitat) | A terminal habitat where plants and wildlife evolve as Herdr agents work and consume tokens, providing ambient visual feedback in a pane. |
| [**gambtho/herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer) | Starts shells and coding agents inside a repository's Dev Container through the official Dev Containers CLI and presents them as normal Herdr panes. |
| [**go-min/herdr-pane-name**](https://github.com/go-min/herdr-pane-name) | Inspects running processes and detected agents to replace numbered pane labels with meaningful command or agent names. |
| [**hasuwini77/herdr-follow-cwd**](https://github.com/hasuwini77/herdr-follow-cwd) | Renames a Herdr workspace from the active pane's current directory, with configurable path boundaries that keep names anchored to the project root. |
| [**linuxing3/herdr-nnn**](https://github.com/linuxing3/herdr-nnn) | Opens the nnn file manager in a Herdr split or tab at the focused pane's current directory. |
| [**marius-se/herdr-brainrot**](https://github.com/marius-se/herdr-brainrot) | Runs terminal games and distraction apps such as DOOM in a dedicated Herdr pane while agents continue working in neighboring panes. Additional apps can be configured through the plugin manifest. |
| [**oullin/herdr-plugins**](https://github.com/oullin/herdr-plugins) | A collection of small, independently installable Herdr plugins focused on navigation, agent awareness, and terminal workflow improvements. |
| [**tajdien/herdr-confirm-close**](https://github.com/tajdien/herdr-confirm-close) | Requires confirmation before closing a Herdr pane or tab, reducing accidental termination of long-running agent work. |
| [**WerrySs/herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync) | Keeps cmux's graphical file explorer synchronized with the current directory of the focused Herdr pane by listening to focus events without modifying shell sessions. |
| [**ycros/herdr-compass**](https://github.com/ycros/herdr-compass) | Uses consistent directional keys across panes, tabs, and workspaces, moving to the next tab or workspace when the current pane layout has no target in that direction. |
| [**petitviolet/herdr-plugins**](https://github.com/petitviolet/herdr-plugins) | A collection of Herdr plugins. The source catalog does not list the included tools. |
| [**oyuk/herdr_plugin**](https://github.com/oyuk/herdr_plugin) | A Herdr plugin repository whose source description contains only an incomplete action table. |
| [**alastairsounds/herdr-plugins**](https://github.com/alastairsounds/herdr-plugins) | A repository of plugins for Herdr, without a feature list in the source catalog. |
| [**GroepOnline/herdr-plugins**](https://github.com/GroepOnline/herdr-plugins) | A mirrored Herdr plugin collection migrated from OnlineChefGroep/herdr-plugins. |
| [**SeanRoberts/herdr-plugins**](https://github.com/SeanRoberts/herdr-plugins) | A repository of Herdr plugins. The source catalog provides no individual descriptions. |
| [**lliwi/herdr-plugins**](https://github.com/lliwi/herdr-plugins) | A personal collection of Herdr plugins. |
| [**aiki-sh/aiki-plugin-herdr**](https://github.com/aiki-sh/aiki-plugin-herdr) | Provides tools for Aiki integration. |
| [**boooowy/herdr_plugins**](https://github.com/boooowy/herdr_plugins) | A Herdr plugin collection with no specific features described in the source catalog. |
| [**BlockedPath/herdr-plugin**](https://github.com/BlockedPath/herdr-plugin) | A Herdr plugin project with no specific features described in the source catalog. |
| [**michiomochi/herdr-plugin-sidenote**](https://github.com/michiomochi/herdr-plugin-sidenote) | A TUI plugin intended to remain in the right pane of a main Herdr workspace. The source description ends before explaining the per-workspace behavior. |
| [**amine2233/herdr-plugin-kanban**](https://github.com/amine2233/herdr-plugin-kanban) | Adds a Kanban interface to Herdr. |
| [**BryanHeBY/anolisa-herdr-plugin**](https://github.com/BryanHeBY/anolisa-herdr-plugin) | Integrates the ANOLISA tool suite with Herdr terminal workspaces. |
| [**m4salah/herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last) | Adds tmux-style shortcuts for returning to the previous Herdr tab or workspace. |
| [**mi2428/herdr-agent-layout**](https://github.com/mi2428/herdr-agent-layout) | Maintains a readable minimum width for a supervisor pane and arranges worker panes around it. |
| [**yansfil/herdr-agent-context-labels**](https://github.com/yansfil/herdr-agent-context-labels) | Adds compact task summaries and runtime status labels to Herdr coding-agent panes. |
| [**advaitbd/herdr-notify**](https://github.com/advaitbd/herdr-notify) | Sends Herdr agent-status notifications through signed Hermes webhooks. |
| [**spr-networks/spr-herdr**](https://github.com/spr-networks/spr-herdr) | Runs a Herdr TUI inside an SPR-managed KVM microVM. |
| [**amiramay/herdr-layout-cycle**](https://github.com/amiramay/herdr-layout-cycle) | Cycles through preset Herdr pane layouts with a tmux-style prefix-and-space action. |
| [**jmarcelomb/herdr-nav**](https://github.com/jmarcelomb/herdr-nav) | Provides tools for Herdr panes, tabs, and workspaces. |
| [**iQua/herdr-flakes**](https://github.com/iQua/herdr-flakes) | Mirrors and controls Flakes runs from a local Herdr session. |
| [**corrius/herdr-numbered-navigation**](https://github.com/corrius/herdr-numbered-navigation) | Deprecated. Its numbered-navigation features moved to herdr-session-organizer version 0.3.0 and later. |
| [**jrswab/herdr-status**](https://github.com/jrswab/herdr-status) | An ambient Linux machine-status pane for Herdr. |
| [**markbrutx/pif-herdr-reporter**](https://github.com/markbrutx/pif-herdr-reporter) | Provides tools for the pif coding agent. |
| [**Tetat-Chulchue/meadow**](https://github.com/Tetat-Chulchue/meadow) | A mouse-driven file explorer that runs in a Herdr pane. |
| [**jlangston/herdr-clipboard**](https://github.com/jlangston/herdr-clipboard) | Adds tmux-style clipboard history to Herdr, including image entries. |
| [**supex0fan/herdr-claude-swap**](https://github.com/supex0fan/herdr-claude-swap) | Resumes each Claude Code pane through the claude-swap account that owns its existing session. |
| [**kikyous/herdr-claude-usage**](https://github.com/kikyous/herdr-claude-usage) | Opens a Claude usage panel in a chosen Herdr workspace. The source description does not explain the displayed metrics further. |
| [**tigorlazuardi/herdr-claude-retry**](https://github.com/tigorlazuardi/herdr-claude-retry) | Watches Claude CLI panes for Anthropic-related interruptions. The source description is incomplete before explaining the recovery behavior. |
| [**floco/herdr-claude-resume**](https://github.com/floco/herdr-claude-resume) | Detects Claude Code's five-hour rate limit and automatically resumes the session after the limit resets. |
| [**ViSHNUPrABU/herdr-codex**](https://github.com/ViSHNUPrABU/herdr-codex) | An unofficial Herdr-related Codex project. The source catalog contains only version, license, and non-affiliation notices, with no feature description. |
| [**jievince/herdr-codex-app**](https://github.com/jievince/herdr-codex-app) | Turns Herdr into a terminal-first Codex interface for synchronizing projects and resuming conversations. |
| [**Howryann/herdr-monitor**](https://github.com/Howryann/herdr-monitor) | A read-only HTTP monitor for Herdr agent state with no runtime dependencies. |
| [**gadgj/agent-state-changed-bell**](https://github.com/gadgj/agent-state-changed-bell) | Rings a bell when a Herdr agent changes state. |
| [**zerkc/herdr-notify-firebase**](https://github.com/zerkc/herdr-notify-firebase) | Sends Firebase Cloud Messaging push notifications when Herdr agent status changes. |
| [**donghaolicd/herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify) | Sends bounded Microsoft Teams notifications for Herdr agent lifecycle events. |
| [**capt-marbles/herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration) | Reports Jcode session and lifecycle state to Herdr. |
| [**DMelisena/shipmates**](https://github.com/DMelisena/shipmates) | A Hermes plugin offering a preconfigured Kun Chen-style Herdr and OpenCode first-mate workflow. The source catalog does not describe its individual controls. |

### Command palettes and workspace switchers

*14 projects. Searchable menus for Herdr commands, projects, workspaces, and common actions.**

| Project | What it does |
|---|---|
| [**TaylorFinklea/herdr-ask**](https://github.com/TaylorFinklea/herdr-ask) | Opens a popup to translate plain-English requests into shell commands, letting you review and insert them into the active pane with Ctrl+Enter. |
| [**fullerzz/herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh) | A sesh-style Herdr workspace picker with zoxide integration for creating workspaces from frequently used directories. |
| [**ramarivera/herdr-palette**](https://github.com/ramarivera/herdr-palette) | A Rust and Ratatui fuzzy command palette for Herdr workspaces. |
| [**arjenblokzijl/herdr-launcher**](https://github.com/arjenblokzijl/herdr-launcher) | Defines named workflows as `.mjs` files with custom input fields and a `run()` function. Workflows can be launched from a Herdr picker or through `herdr-launcher run`, supporting interactive and scripted use. |
| [**ningxiaoxiao/herdr-agent-picker**](https://github.com/ningxiaoxiao/herdr-agent-picker) | Enables the user choose an AI agent and working directory before Herdr creates a new tab, split, or workspace. |
| [**mackt/herdr-window-title**](https://github.com/mackt/herdr-window-title) | Writes template-formatted Herdr session and agent state into the outer terminal window title, including whether background agents are working, blocked, or done. |
| [**phine-apps/mux-prompter**](https://github.com/phine-apps/mux-prompter) | Searches local prompt libraries with fzf and inserts a context-aware template into the active Herdr pane. |
| [**tomotochi/herdr-plugin-picker**](https://github.com/tomotochi/herdr-plugin-picker) | Takes selections from terminal browsers or search tools and inserts them into the pane that opened the picker. |
| [**daltonkyemiller/herdr-plugin-switchboard**](https://github.com/daltonkyemiller/herdr-plugin-switchboard) | A Herdr plugin built for one focused switchboard workflow. The source catalog does not describe that workflow. |
| [**AnnanKhan/herdr-agent-launcher**](https://github.com/AnnanKhan/herdr-agent-launcher) | Adds a clickable agent-launcher pane. Left-click starts the configured default agent, while right-click opens the full list. |
| [**spro/herdr-agent-launcher**](https://github.com/spro/herdr-agent-launcher) | Opens a named Herdr tab running a selected Claude model. |
| [**bkroeze/omherdr**](https://github.com/bkroeze/omherdr) | An Omarchy and Wayland Quickshell status launcher for Herdr. |
| [**lucasleon2107/herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher) | Opens a new Herdr tab with Claude Code already running. |
| [**quinnjr/herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile) | Manages and switches `claude-profile` profiles from a Herdr overlay palette. |

### Status lines, sidebars, and tab synchronization

*70 projects. Persistent interface elements that show agent state, repository context, quotas, tasks, or synchronized tab information.**

| Project | What it does |
|---|---|
| [**iurysza/herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename) | Uses a lightweight LLM to derive short workspace and tab names from pane activity, replacing generic numbers or directory labels with current task summaries. |
| [**fkiene/llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr) | Activates the llmtrim compression proxy in new Herdr workspaces, shows savings badges in pane rows, and opens llmtrim's dashboard in a split. It also warns when a pane did not inherit the proxy settings. |
| [**rjyo/herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync) | Writes workspace, tab, and agent context to the outer terminal title. It uses pane metadata and status first, then falls back to recent prompts in local Claude Code or Codex session files. |
| [**wenhanweime/herdr-plugin-renamer**](https://github.com/wenhanweime/herdr-plugin-renamer) | Uses an LLM to name sessions for Claude Code, Codex, Grok, Pi, and OpenCode, with Chinese or English labels and OpenCode Zen as the default engine. |
| [**Resetnak/herdr-logbook**](https://github.com/Resetnak/herdr-logbook) | An offline Bubble Tea notebook for Herdr workspaces. It manages Markdown task files, records decisions, and builds local activity heatmaps and stand-up summaries without a database or cloud service. |
| [**mrcndz/herdr-routines**](https://github.com/mrcndz/herdr-routines) | Runs scheduled routines on cron or interval timers by opening a tab in a chosen workspace and executing a command or starting an agent. |
| [**aarsh21/herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title) | Provides automatic tmux-style tab titles for Herdr. |
| [**bcihanc/herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title) | Copies the Claude Code session title, including `/rename` or automatic summaries, into Herdr pane metadata. |
| [**kakigakki/herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer) | Uses Claude Code session titles for agent tabs and directory names for workspaces, providing automatic ChatGPT-style labels across parallel sessions. |
| [**wjarka/herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title) | Writes color-coded counts of working, blocked, done, and idle Herdr agents into Ghostty tab titles. |
| [**cdc-lst/herdr-wait**](https://github.com/cdc-lst/herdr-wait) | Examines the process tree of idle or blocked panes and replaces generic state with a specific waiting label, such as a build or external CLI name. |
| [**edouard-andrei/herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools) | Rearranges existing panes into main-left, grid, or equalized presets without changing pane IDs, tab IDs, or running processes. |
| [**getpipher/herdr-sysmon**](https://github.com/getpipher/herdr-sysmon) | Adds CPU, memory, battery, network, and disk measurements to Herdr sidebar tokens, with configurable refresh intervals and macOS-focused probes. |
| [**rohankewal/herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name) | Ports tmux-nerd-font-window-name to Herdr, updating tab icons from the running program and directory context. |
| [**lachieh/herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux) | Mirrors every Herdr agent into the cmux sidebar. |
| [**calebcauthon/herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler) | Moves finished Herdr agent tabs and workspaces below active work so completed items stay visible but out of the main path. |
| [**4Born/herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler) | Keeps pane labels synchronized with public identifiers such as `w1:p2` as panes and workspaces are created, split, or closed. |
| [**furuhashin/herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes) | Broadcasts one command to every pane in the current tab, providing a shell-based equivalent of tmux synchronized panes. |
| [**ndom91/herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name) | Uses a local Ollama model to generate and update descriptive Herdr tab names from recent pane activity. |
| [**nytafar/herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl) | Shows a color-coded countdown for each pane's prompt-cache lifetime and can sort agents by cache urgency so warm sessions are used before expiry. |
| [**toyamarinyon/herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab) | Renames single-pane tabs from Claude Code or Codex thread titles through background session updates and the Herdr socket API. |
| [**varelaseb/tabherd**](https://github.com/varelaseb/tabherd) | Adds pinned agents, color-coded session tabs, and collapsible workspace folders to Herdr. |
| [**justcyl/pi-herdr-tab-sync**](https://github.com/justcyl/pi-herdr-tab-sync) | Renames the active Herdr tab to the Pi session name when an agent starts or resumes. It communicates directly with the socket and remains inactive outside Herdr-managed panes. |
| [**liu-qingyuan/herdr-tmux-local-config**](https://github.com/liu-qingyuan/herdr-tmux-local-config) | A workstation configuration combining Herdr, Codex lifecycle hooks, and Oh My Tmux. Codex hooks report agent state to the Herdr sidebar, and install scripts document how to combine the components. |
| [**carsonjones/herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles) | Adds named split ratios: 60/40 and 40/60 horizontal, 20/80 and 80/20 vertical, plus 50/50 resets. Modifier keys flip the larger side or return to equal sizing. |
| [**alexjsp/herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture) | Saves the focused pane's scrollback as a colored, self-contained HTML file or plain text, with configurable path, filename, and theme. |
| [**aclima01/herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync) | Updates a Windows PowerShell terminal title from the focused Herdr workspace and agent state using native console escapes and event listeners. |
| [**bayoudhi/herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times) | Displays the next Islamic prayer and a live countdown in the Herdr sidebar, with a timetable popup and optional desktop alerts. Schedules are fetched from Al Adhan and cached locally. |
| [**btorresgil/herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title) | Reads local Hermes Agent SQLite data and publishes descriptive conversation titles in the Herdr sidebar. |
| [**danbuhler/herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync) | Renames panes and tabs from the active topic or terminal title emitted by Claude Code and Codex, while avoiding rename loops and respecting manual labels. |
| [**davidolrik/herdr-titles**](https://github.com/davidolrik/herdr-titles) | Builds tab and terminal-window titles from foreground processes, agent session names, and workspace status counts using HCL templates. Shell hooks support Bash, Zsh, and Fish, and manual tab names are preserved. |
| [**dev-shimada/herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name) | Keeps tab labels aligned with the focused pane's current directory and updates them on lifecycle and focus events without replacing manually chosen names. |
| [**iuhoay/herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane) | Moves the active pane into a new tab while preserving its process, similar to tmux break-pane. It unzooms complex tabs first and leaves single-pane tabs unchanged. |
| [**Numbered-com/herdr-ports**](https://github.com/Numbered-com/herdr-ports) | Detects TCP listeners started by processes in each workspace and adds a dynamic `$ports` badge to the Herdr sidebar. |
| [**Only-Moon/herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows) | Adds contextual Nerd Font icons to tab titles based on directory, project type, or running tool, with support for Windows, macOS, and Linux. |
| [**pjs-0457/herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer) | Opens Yazi in a labelled Herdr tab or split at the workspace directory and relaunches it automatically after exit. |
| [**playsthisgame/herdr-api-client**](https://github.com/playsthisgame/herdr-api-client) | Opens the Ichigo terminal REST client in a split or tab and scopes it to the current project's request collection. |
| [**ropali/herdr-compose**](https://github.com/ropali/herdr-compose) | A standalone YAML layout manager for workspaces, tabs, splits, and startup commands, with active switching, starter templates, and terminal inspection of the layout tree. |
| [**szrenwei/herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata) | Adds current tab labels and state indicators to each workspace row in the Herdr sidebar and keeps them synchronized through lifecycle events. |
| [**tmn73/herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title) | Uses Claude Code session events to replace generic Herdr tab numbers with active task descriptions. |
| [**rcosteira79/herdr-plugins**](https://github.com/rcosteira79/herdr-plugins) | Contains two separate Herdr plugins: an idle-shell badge and a read-pending indicator. |
| [**jfdg01/herdr-claude-setup**](https://github.com/jfdg01/herdr-claude-setup) | A reproducible personal Herdr and Claude Code setup with status lines, automatic compaction, night-light behavior, and named workflow variants. |
| [**phillipleblanc/ad**](https://github.com/phillipleblanc/ad) | A command-line dispatcher for sending messages between local Herdr agent tabs. |
| [**akhillb/herdr-attention**](https://github.com/akhillb/herdr-attention) | Docks a theme-matched countdown to the next Google Calendar meeting and highlights the pane when the meeting is ten minutes away. |
| [**aiki-sh/aiki-integration-herdr**](https://github.com/aiki-sh/aiki-integration-herdr) | Shows active aiki epics in a live-refreshing Herdr sidebar and installs the companion session-identity hook. |
| [**dnf0/herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header) | Creates a one-line LLM summary when an agent finishes and writes it into the pane header so completed work can be scanned without opening scrollback. |
| [**eabadim/herdr-context-namer**](https://github.com/eabadim/herdr-context-namer) | Reads active OpenCode context through Herdr and renames tabs and workspaces to match the current task. |
| [**elKei24/herdr-title-sync**](https://github.com/elKei24/herdr-title-sync) | A single-instance daemon that copies OSC terminal titles from Claude Code and similar agents into Herdr tab labels and periodically reconciles state through the socket. |
| [**malone-c/herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename) | Renames panes and tabs from the active agent task or prompt by analysing live terminal activity and producing a concise label. |
| [**OliverGilan/herdr-jj**](https://github.com/OliverGilan/herdr-jj) | Adds Jujutsu workspace creation, remote fetching, bookmark setup, live change metadata, and post-create hooks to Herdr. |
| [**sergeybataev/herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title) | Watches Codex session logs and updates Herdr agent labels with the current conversation topic. |
| [**willfish/herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes) | Equalizes all panes in the active tab with one key, reproducing tmux `select-layout -E` behavior after repeated splits or resizing. |
| [**winoooops/herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync) | Synchronizes pane titles with active Claude Code, Codex, Kimi Code, and OpenCode sessions as their tasks or roles change. |
| [**cokekitten/pi-recap**](https://github.com/cokekitten/pi-recap) | Summarizes recent activity and can synchronize session titles with Herdr or tmux. |
| [**bleedingfight/herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager) | An fzf-based fuzzy finder for Herdr workspaces, tabs, panes, and agents. |
| [**scaryrawr/herdr-agent-title**](https://github.com/scaryrawr/herdr-agent-title) | Displays Herdr agent information in the outer terminal window title. |
| [**Vistyy/pi-herdr-agents**](https://github.com/Vistyy/pi-herdr-agents) | Runs user-owned Pi agents in dedicated Herdr tabs. |
| [**the-inconvenience-store/herdr-agent-session-title**](https://github.com/the-inconvenience-store/herdr-agent-session-title) | Copies Claude Code or Codex session titles into Herdr pane metadata. |
| [**adnichols/herdr-kitty-status**](https://github.com/adnichols/herdr-kitty-status) | Shows live Herdr agent-state counts in Kitty terminal tabs. |
| [**carlotran4/waybar-herdr**](https://github.com/carlotran4/waybar-herdr) | An event-driven Waybar module for Herdr agent status. |
| [**tipok/herdr-layouts**](https://github.com/tipok/herdr-layouts) | Builds complete Herdr workspaces from declarative TOML files defining tabs, panes, split directions, and startup commands. |
| [**timaliev/herdr-layout**](https://github.com/timaliev/herdr-layout) | Defines session-aware Herdr layouts in YAML, applies them idempotently, and can load them automatically at startup. |
| [**phenome/herdr-layout**](https://github.com/phenome/herdr-layout) | A small Herdr plugin with three saved tab layouts. |
| [**alex-devdone/raycast-herdr-status-bar**](https://github.com/alex-devdone/raycast-herdr-status-bar) | A Raycast menu-bar extension showing local Claude and Codex agents, their states, token use, and session duration. |
| [**yuhgo/herdr-tab-marker**](https://github.com/yuhgo/herdr-tab-marker) | Automatically adds a task-based title and repository-specific emoji to Claude Code and Codex tabs in Herdr. |
| [**allexborysov/herdr-claude-auto-title**](https://github.com/allexborysov/herdr-claude-auto-title) | Summarizes the first Claude Code message into a short kebab-case session title and shows it in Herdr's agent sidebar. |
| [**TheMetalStorm/herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin) | Makes a plain Cline CLI process appear as a native Herdr agent with lifecycle reporting. |
| [**MartinKei/herdr-tab-notes**](https://github.com/MartinKei/herdr-tab-notes) | Provides tools for taking notes. |
| [**QuantumDancer/herdr-last-tab**](https://github.com/QuantumDancer/herdr-last-tab) | Switches back to the previously focused Herdr tab. |
| [**nmogil/agent-skill-patterns**](https://github.com/nmogil/agent-skill-patterns) | Provides Claude Code, Hermes, and Herdr workflows. |

### Status overlays, HUDs, and agent timers

*15 projects. Floating status HUDs, turn timers, and keep-awake utilities.*

| Project | What it does |
|---|---|
| [**Tyru5/herdr-floax**](https://github.com/Tyru5/herdr-floax) | A tmux-floax-style floating shell with one persistent scratch session per Herdr workspace. |
| [**osamahbeig/herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover) | A clickable overlay for moving, re-splitting, and swapping panes across Herdr tabs and workspaces. |
| [**sohanemon/herdr-helpr**](https://github.com/sohanemon/herdr-helpr) | Adds keyboard overlays for naming a workspace before creation, renaming the current workspace, and closing every pane or tab except the focused one. |
| [**maro114510/herdr-toggle-popup**](https://github.com/maro114510/herdr-toggle-popup) | Toggles a shell overlay above the current Herdr session for quick commands, notes, or plan inspection without rearranging panes. |
| [**iikjl/herdr-spotify**](https://github.com/iikjl/herdr-spotify) | A macOS Spotify overlay with album art, progress, and playback controls in Herdr. AppleScript provides basic control, while optional Web API access adds search, queueing, and track-change alerts. |
| [**jeromychu23/herdr-popupx**](https://github.com/jeromychu23/herdr-popupx) | Adds persistent floating terminal popups that can be toggled from any workspace without changing the tiled layout or losing scratchpad state. |
| [**maedana/herdr-agents-status**](https://github.com/maedana/herdr-agents-status) | An always-on-top overlay for Herdr agent status. |
| [**Yemeni/herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer) | Alternates each agent's status label with the elapsed time spent in that state. |
| [**ArteenHD/herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer) | Tracks prompt-cache windows for active agents and shows live countdowns in the Herdr sidebar, with warnings before a cache expires. |
| [**happyeric77/agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake) | Uses macOS `caffeinate` while any Herdr agent is working and releases the sleep lock when all agents become idle, blocked, or done. |
| [**napalmpapalam/herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr) | Captures recent agent output in a popup and lets the user select a passage to quote back into the conversation. |
| [**nwarwick/herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate) | Keeps macOS awake while Herdr agents are working and releases the `caffeinate` assertion after a configurable idle grace period. |
| [**shadowfax92/herdr-scratch**](https://github.com/shadowfax92/herdr-scratch) | Gives each Herdr pane a persistent scratch overlay backed by a private tmux session, keeping notes, REPLs, and side commands tied to that pane. |
| [**zetlen/herdr-hud**](https://github.com/zetlen/herdr-hud) | A floating, customizable HUD for host, network, session, and agent metrics, with support for extra data supplied by shell scripts. |
| [**speardragon/herdr-status-platform**](https://github.com/speardragon/herdr-status-platform) | A Herdr status-platform integration. The source catalog does not explain its displayed data or controls. |

### Context meters and rate-limit gauges

*7 projects. Live token headroom meters, quota tracking, and agent cost gauges.*

| Project | What it does |
|---|---|
| [**senna-lang/herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage) | Shows context meters and provider rate limits for agents running in Herdr. |
| [**ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay**](https://github.com/ezcorp-org/herdr-pc-ram-and-cpu-usage-overlay) | A Linux-focused Rust plugin showing CPU and memory use per workspace relative to total system capacity. |
| [**mgh3326/scopefuel**](https://github.com/mgh3326/scopefuel) | Breaks provider quota and remaining capacity down by account, model, and group, including reset times for five-hour and weekly windows. |
| [**silverwolfdoc/herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar) | A compact bar showing live token use, rate-limit ceilings, and context-window fill for agents without occupying a full pane. |
| [**szrenwei/herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics) | Tracks context-window and token metrics for Claude Code, Codex, and TraeX sessions and summarizes them in a small Herdr overlay. |
| [**tomys22/herdr-agent-usage-plugin**](https://github.com/tomys22/herdr-agent-usage-plugin) | Displays Claude, Codex, and Gemini API usage, including session and weekly percentages and reset times, in a Herdr split. |
| [**ram4-dev/herdr-codex-usage**](https://github.com/ram4-dev/herdr-codex-usage) | Detects installed agents and shows their usage quotas inside Herdr. |

### Output inspection, logs, and transcripts

*9 projects. Tools for searching, cleaning, exporting, or reviewing pane output and agent conversations.**

| Project | What it does |
|---|---|
| [**AkashJana18/herdr-scratch**](https://github.com/AkashJana18/herdr-scratch) | Maintains persistent scratch panes that can be shown or hidden without losing shell, note, or REPL state. Scratch areas may be global, workspace-specific, or directory-specific. |
| [**Hanyang-Li/herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso) | Uses the macOS espresso utility to keep a Mac awake while monitored Herdr agents are working or blocked, then releases the assertion when tasks finish. |
| [**GranamyrBR/herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach) | A side-pane English and developer-jargon coach that records grammar corrections and phrasing suggestions while agents work. |
| [**x0d7x/herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url) | Reads visible content from every Herdr pane, extracts and deduplicates URLs, and sends them to fzf. Enter opens the selected URL, while `y` copies it. |
| [**a-curious-coder/herdr-iris**](https://github.com/a-curious-coder/herdr-iris) | Detects the active agent and searches matching skills and rules from Claude `SKILL.md` and Cursor configuration. Selecting an item inserts the formatted command for confirmation. |
| [**Brutheron/Renderd**](https://github.com/Brutheron/Renderd) | Displays completed Claude Code and Codex responses in a clean, scrollable side panel that updates live. It reads structured session files, removes thinking blocks, and renders the answer as Markdown. |
| [**fredrikkvalvik/herdr-scratch**](https://github.com/fredrikkvalvik/herdr-scratch) | A temporary floating shell for quick commands over a Herdr session. |
| [**alanpcurrie/herdr-claude**](https://github.com/alanpcurrie/herdr-claude) | A repository containing Herdr and Claude demonstration output rather than a described tool. |
| [**johnlindquist/herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps) | Adds timestamped, scrollable observations of Herdr pane output. |

### Dotfiles and ready-made configuration

*6 projects. Complete or partial Herdr configurations that can be installed and adapted instead of written from zero.**

| Project | What it does |
|---|---|
| [**ogulcancelik/herdr-browser**](https://github.com/ogulcancelik/herdr-browser) | Renders an interactive Chromium browser inside a Herdr pane through the Kitty graphics protocol. Chrome DevTools Protocol support lets agents automate the browser while humans observe and intervene with keyboard or mouse. |
| [**multiplex-term/Multiplex**](https://github.com/multiplex-term/Multiplex) | An SSH, tmux, and Herdr terminal client for Apple Vision Pro and iPad. |
| [**ddfonseca/herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image) | Saves an image from the macOS or Linux clipboard to disk and pastes its file path into the active pane for use by multimodal agents. |
| [**crierr/herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout) | Adds tmux-style layout presets for Herdr, including even horizontal, even vertical, main horizontal, main vertical, tiled, cycle, and balance. |
| [**VinhLe1410/herdr-agent-priority**](https://github.com/VinhLe1410/herdr-agent-priority) | Configures how Herdr agent states are prioritized. |
| [**masatokawano/to-herdr**](https://github.com/masatokawano/to-herdr) | Configuration and notes for migrating a terminal setup from Zellij to Herdr. |

### Plugin collections and developer frameworks

*3 projects. Collections and scaffolding for discovering, creating, or maintaining several Herdr extensions.**

| Project | What it does |
|---|---|
| [**vonzelle-vzt/herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions) | Installs a complete 13-panel developer environment inside Herdr for diagnostics, language-server completion, tests, and in-terminal agent diff review. |
| [**MIDO-ruby7/herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory) | A directory of Herdr plugins organized by the task a user wants to accomplish. |
| [**Newt6611/herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust) | Provides tools for developing Herdr plugins. |

---

## 6. Apps, companion integrations, and installation

*75 projects. Desktop and mobile clients, browser dashboards, physical status devices, supporting plugins, and reproducible installation tools.*

### Native desktop and mobile apps

*11 projects. Installed applications and launchers that provide a native interface to Herdr on desktop or mobile operating systems.**

| Project | What it does |
|---|---|
| [**skeletor-js/bessie**](https://github.com/skeletor-js/bessie) | Provides tools for Herdr. |
| [**undivisible/herdr-gui**](https://github.com/undivisible/herdr-gui) | Provides tools for Herdr and related development tools. |
| [**jgwesterlund/agent-view**](https://github.com/jgwesterlund/agent-view) | A playful macOS status app that represents agents as pixel-art office characters, changes their behavior with agent state, and focuses a pane when its character is opened. |
| [**bsorescu/herdr-mobile**](https://github.com/bsorescu/herdr-mobile) | Connects to Herdr over SSH and provides mobile-friendly status cards, filtered scrollback, and quick approval actions. |
| [**hmu332233/herdr-menu-bar**](https://github.com/hmu332233/herdr-menu-bar) | A macOS menu-bar app showing agent state by workspace. Selecting an agent can return directly to its Herdr pane. |
| [**re2zero/zenix**](https://github.com/re2zero/zenix) | Provides tools for Herdr with workspace controls, live system metrics, built-in themes, CJK input support, and an isolated bundled Herdr binary. |
| [**mohamed-essam/herdr-mobile**](https://github.com/mohamed-essam/herdr-mobile) | An Android companion made from a Go daemon and a Kotlin Compose app for monitoring Herdr agents and answering blocked prompts from a phone. |
| [**re2zero/deepin-herdr**](https://github.com/re2zero/deepin-herdr) | A native Deepin Linux and UOS desktop app that embeds Herdr in a Qt terminal, installs the binary on first launch, and is distributed as a Debian package. |
| [**zackbart/herdr-ios**](https://github.com/zackbart/herdr-ios) | Connects to Herdr over SSH, lists workspaces, displays live scrollback, subscribes to events, and sends terminal input without a relay service. |
| [**sunnoy/livis**](https://github.com/sunnoy/livis) | Provides tools for monitoring agents over SSH or Mosh, working with Herdr or tmux, and sending approval alerts to a phone. |
| [**Tatendaz/herdr-launcher**](https://github.com/Tatendaz/herdr-launcher) | An unofficial macOS Dock launcher that opens the Herdr terminal interface with one click. |

### Web dashboards and remote viewers

*16 projects. Browser-based monitors, remote controls, and visual scenes for following Herdr agents from another screen or device.**

| Project | What it does |
|---|---|
| [**AltanS/collie**](https://github.com/AltanS/collie) | A Herdr plugin and private Tailscale web app that mirrors panes, shows which agent needs attention, and supports replies from a phone without opening an SSH terminal. |
| [**dcolinmorgan/herdr-remote**](https://github.com/dcolinmorgan/herdr-remote) | A remote monitoring suite with a mobile web app, macOS menu-bar app, Telegram bot, push notifications, terminal views, and one-tap responses to blocked agents through a Cloudflare tunnel. |
| [**kcosr/herdr-web**](https://github.com/kcosr/herdr-web) | Provides tools for viewing and controlling Herdr from a desktop or mobile browser, including live pane state, terminal attachment, and event updates. |
| [**0cv/herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay) | A mobile web app and relay for monitoring Herdr, approving blocked actions, pairing by QR code, receiving push alerts, and combining several machines in one dashboard. |
| [**KaminariOS/whip**](https://github.com/KaminariOS/whip) | A remote-control project for checking and directing Herdr agents running on a home machine while travelling. |
| [**ragamo/herdr-flock**](https://github.com/ragamo/herdr-flock) | Represents active Herdr agents as animated sheep and records completed sessions in a persistent graveyard log. |
| [**alecuba16/herdr-webui**](https://github.com/alecuba16/herdr-webui) | Provides tools for Herdr with workspace and worktree navigation, agent status, live terminal access, and service scripts for persistent macOS or Linux use. |
| [**hmu332233/herdr-f1**](https://github.com/hmu332233/herdr-f1) | A web visualization that represents active Herdr agents as Formula 1 cars, using race and pit-stop states to show whether agents are running, blocked, or finished. |
| [**osuki-dev/muqun-gateway**](https://github.com/osuki-dev/muqun-gateway) | A local-first gateway that links Herdr to the Muqun mobile app over encrypted peer-to-peer connections, allowing private remote viewing, approvals, and prompts without cloud accounts. |
| [**mejiasd3v/herdr-farm**](https://github.com/mejiasd3v/herdr-farm) | A Three.js dashboard that represents Herdr workspaces and agents as a 3D farm, with animal animations tied to live idle, working, and blocked states. |
| [**allmight-ai/herdr-pet**](https://github.com/allmight-ai/herdr-pet) | A retro virtual-pet display that reacts to live Herdr agent states and creates a persistent pet identity from the user's GitHub ID. |
| [**matheus3301/herdr-phone**](https://github.com/matheus3301/herdr-phone) | A mobile remote console built from a Go relay and an embedded PWA, with Cloudflare Tunnel and Access for secure status viewing, scrollback inspection, and prompt responses. |
| [**aviz85/herdr-controller**](https://github.com/aviz85/herdr-controller) | A Next.js dashboard for Herdr with a live agent grid, terminal mirror, messaging, agent spawning, and an optional 3D office view driven through the Herdr CLI. |
| [**tigorlazuardi/herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui) | A lightweight browser and progressive web app client for daemon-mode Herdr, with terminal viewing, pane navigation, and plugin launching on desktop or mobile devices. |
| [**funsaized/herdr-mise**](https://github.com/funsaized/herdr-mise) | Represents Herdr agents as line cooks and animates their work, tool use, and blocked states from live socket events. |
| [**gabrielbarretoo/herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval) | A Three.js visualization that turns Herdr workspaces into medieval camps and panes into animated adventurers whose behavior reflects each agent's state. |

### Hardware and ambient displays

*12 projects. Keypads, watches, desk devices, and compact displays that turn agent state into physical controls or at-a-glance signals.**

| Project | What it does |
|---|---|
| [**Unayung/herdr-watch**](https://github.com/Unayung/herdr-watch) | A native Apple Watch companion that shows Herdr agent activity and alerts the wearer when an agent finishes or needs input. |
| [**timvdhoorn/stream-deck-herdr-plugin**](https://github.com/timvdhoorn/stream-deck-herdr-plugin) | Assigns a key to each agent, displays its state with a color and icon, and focuses the matching Herdr pane when pressed. |
| [**spencerbull/xeneon-edge-agents**](https://github.com/spencerbull/xeneon-edge-agents) | An Omarchy and Herdr agent command center designed for the Corsair XENEON EDGE display, with conservative handling when state cannot be confirmed. |
| [**walcew/herdr-assist**](https://github.com/walcew/herdr-assist) | An ESP32-S3 desk display that shows Herdr session states and sounds a bell when an agent is waiting for a decision or approval. |
| [**alasano/house-of-herdr**](https://github.com/alasano/house-of-herdr) | Provides tools for the Work Louder Codex Micro keypad that maps Herdr events to status lights, dials, shortcuts, and approval controls. |
| [**Pimpmuckl/herdr-streamdeck**](https://github.com/Pimpmuckl/herdr-streamdeck) | A Stream Deck+ integration that maps Herdr agent states and actions to LCD keys, touch controls, and dials for quick status checks and pane switching. |
| [**bowlofsoup/herdr-stoplight**](https://github.com/bowlofsoup/herdr-stoplight) | An Arduino integration that uses a physical traffic light to show aggregate Herdr status: green for working, red for blocked or failed, and yellow for idle. |
| [**third774/herdr-sidepulse**](https://github.com/third774/herdr-sidepulse) | A USB hardware integration for SidePulse Pro and Dot devices that turns combined Herdr agent states into ambient LED patterns, including prominent alerts for blocked agents. |
| [**AlexBSoD/qubeherd**](https://github.com/AlexBSoD/qubeherd) | A hardware integration that shows Herdr agent state, the host clock, and keyboard layout on an Ergohaven Qube dongle display. |
| [**8-BitRhyon/bantay-tui**](https://github.com/8-BitRhyon/bantay-tui) | A macOS notch HUD that combines Herdr approvals, live usage and cost data, a file shelf, task tracking, Apple Reminders sync, and session controls. |
| [**omerturhan/herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar) | Shows working and blocked Herdr agents and jumps to a selected agent's tab when tapped. |
| [**zhongpei/herdr-ulanzi-deck**](https://github.com/zhongpei/herdr-ulanzi-deck) | A Ulanzi D200X keypad integration that shows live, priority-sorted Herdr agent states on LCD keys and can monitor several Herdr machines over SSH. |

### Plugins and supporting utilities

*27 projects. Small integrations for notifications, status, tasks, scheduling, agent management, and everyday desktop behavior.**

| Project | What it does |
|---|---|
| [**natori-hrj/herdr-lazy**](https://github.com/natori-hrj/herdr-lazy) | A declarative Herdr plugin manager with a dedicated terminal interface, a lockfile, version pinning, synchronization from one list, and support for prebuilt binaries. |
| [**speardragon/herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager) | A small in-terminal menu for browsing, installing, updating, enabling, and disabling Herdr plugins through the standard plugin command-line interface. |
| [**miiraheart/herdr-beads**](https://github.com/miiraheart/herdr-beads) | Displays Beads issues as a list, table, or Kanban board in a Herdr sidebar or floating pane. |
| [**ezcorp-org/herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status) | Shows staged, modified, untracked, and conflicted Git files for each workspace beside its branch name. |
| [**afogel/shepherdr**](https://github.com/afogel/shepherdr) | Provides tools for launching delegated coding agents in visible panes that can be watched, resumed, audited, or taken over manually. |
| [**A1exthegreat/herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify) | Sends desktop notifications when agents finish, request confirmation, or become idle. |
| [**leset0ng/pi-todo-herdr**](https://github.com/leset0ng/pi-todo-herdr) | Provides tools for Pi with a live task widget and integration with the Herdr sidebar. |
| [**neefrehman/herdr-caffeinate**](https://github.com/neefrehman/herdr-caffeinate) | Prevents sleep while any Herdr agent pane is actively working, including when the laptop lid is closed. |
| [**dio16/herdr-auto-update**](https://github.com/dio16/herdr-auto-update) | Checks installed Herdr plugins for newer upstream commits and reinstalls updated versions automatically. |
| [**gw31415/herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos) | Watches Herdr agent-status events and keeps an Amphetamine session active while agents are working, preventing sleep during long tasks. |
| [**suisya-systems/herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office) | A terminal pixel-art office where Herdr agents appear as animated desk workers, blocked agents raise timed alerts, and selecting a character focuses its pane. |
| [**levi-qiao/herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota) | A sidebar quota monitor for Claude, Codex, Grok, and Agy that shows the percentage remaining in five-hour and weekly limits. |
| [**cxnmai/dms-herdr-plugin**](https://github.com/cxnmai/dms-herdr-plugin) | A DankMaterialShell widget for viewing Herdr agent states and accessing basic controls from the desktop shell. |
| [**TianZuo555/pi-herdr-agents**](https://github.com/TianZuo555/pi-herdr-agents) | Starts role-guided peer coding agents in separate Herdr panes. |
| [**hbacheller-tribe/herdrStatusWidget**](https://github.com/hbacheller-tribe/herdrStatusWidget) | A Herdr status widget that highlights tabs containing agents that are waiting for approval. |
| [**zerodice0/herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin) | Provides sending prompts to Herdr agents or running local command-line tasks at chosen times on macOS and Linux. |
| [**calorie/herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus) | Focuses the Herdr agent needing attention after the computer has been idle. |
| [**quinnjr/herdr-notifications**](https://github.com/quinnjr/herdr-notifications) | Sends native desktop notifications when Herdr agent states change on Linux, macOS, Windows, and BSD. |
| [**ablause/herdr-flutter**](https://github.com/ablause/herdr-flutter) | A Herdr sidebar for watching, hot-reloading, and inspecting a running Flutter app beside the coding agent working on it. |
| [**aorumbayev/herdr-ctx**](https://github.com/aorumbayev/herdr-ctx) | A Herdr sidebar indicator that shows Claude's remaining context-window capacity. |
| [**miya10kei/herdr-plugin-sidebar**](https://github.com/miya10kei/herdr-plugin-sidebar) | Displays Google Calendar events and GitHub Actions run status in a split pane styled as a sidebar. |
| [**khatriafaz/herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo) | Adds the current agent, repository, and branch names to Herdr pane headers and the sidebar. |
| [**ondratuma/herdr-status-plugin**](https://github.com/ondratuma/herdr-status-plugin) | A per-pane activity plugin with sidebar icons, live timers, and a helper for renaming agent panes. |
| [**cedrus-8864/herdr-sidebar-numbers**](https://github.com/cedrus-8864/herdr-sidebar-numbers) | Shows workspace and agent position numbers matching Herdr's numbered shortcuts. |
| [**Coolsik/herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost) | Estimates the cost of the current Codex session. |
| [**samuelbaldwin05/herdr-burn**](https://github.com/samuelbaldwin05/herdr-burn) | Shows Claude Code cost and quota for each pane, plus a total spending overlay for the workspace. |
| [**mougua/herdr-reasonix**](https://github.com/mougua/herdr-reasonix) | Detects Reasonix agents and displays their status correctly. |

### Setup, packages, and version management

*9 projects. Guides, configuration bundles, installers, package definitions, and tools for reproducible Herdr environments.**

| Project | What it does |
|---|---|
| [**joeseesun/herdr-guide**](https://github.com/joeseesun/herdr-guide) | A Chinese-language practical guide that explains what Herdr is useful for and how to get started. |
| [**Yassimba/loom**](https://github.com/Yassimba/loom) | A curated collection of agent skills, Pi packages, and Herdr plugins with a single command-line setup tool. |
| [**maxto/dotfiles**](https://github.com/maxto/dotfiles) | Provides tools for a human-and-agent terminal environment using Herdr, broot, Micro, shell configuration, a symlink installer, and a ready-made layout. |
| [**AodhanHayter/herdr-nix**](https://github.com/AodhanHayter/herdr-nix) | A Nix flake for installing Herdr on Intel and ARM macOS or Linux, with automated upstream release tracking and a Cachix binary cache. |
| [**lachieh/vfox-herdr**](https://github.com/lachieh/vfox-herdr) | Provides tools for versioned Herdr releases, verified downloads, preview builds, and shell completions that can include live session data. |
| [**yigitkonur/herdr-wezterm-setup**](https://github.com/yigitkonur/herdr-wezterm-setup) | A macOS terminal configuration that uses Herdr as the multiplexer and WezTerm as the keyboard-routing layer. |
| [**DavidTWhitlatch/dotfiles-template**](https://github.com/DavidTWhitlatch/dotfiles-template) | A shareable macOS dotfiles template with zsh, Oh My Zsh, Oh My Posh, Herdr, Git template hooks, and a symlink-based setup. |
| [**tyler-jewell/herdr-bootstrap**](https://github.com/tyler-jewell/herdr-bootstrap) | An idempotent machine-bootstrap script for Herdr, Node tooling, Grok, and the Herdr agent skill. |
| [**chrisjohnson/asdf-herdr**](https://github.com/chrisjohnson/asdf-herdr) | Provides tools for installing and switching between Herdr versions. |

---

## 7. Experimental projects

*12 projects. Early experiments, design documents, and incomplete prototypes. Check each repository before relying on one in daily work.*

### Experiments, concepts, and scaffolds

*12 projects. Ideas and prototypes that are useful to study but may be incomplete, read-only, or not yet installable.**

| Project | What it does |
|---|---|
| [**eliasstravik/herdr-call**](https://github.com/eliasstravik/herdr-call) | An early TypeScript prototype for translating spoken commands into Herdr navigation and input through the local socket. |
| [**meerzulee/herdr-float**](https://github.com/meerzulee/herdr-float) | An early plugin scaffold exploring Zellij-style floating terminal panes that can be toggled without changing the main Herdr grid. |
| [**wraithyy/herdr-openr**](https://github.com/wraithyy/herdr-openr) | Extracts file paths and URLs from recent pane output and Claude Code transcripts, then presents them in a fuzzy finder for quick opening. |
| [**rohanthewiz/herdr-web**](https://github.com/rohanthewiz/herdr-web) | Renders Herdr pane frames with color, mouse, clipboard, and hyperlink support; keyboard and paste input are currently disabled, so it mainly works as a viewer. |
| [**hmu332233/herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs) | An experimental plugin laboratory containing early prototypes for agent launching, workspace metrics, and worktree symlinking before they move into separate projects. |
| [**shoaibkhanz/herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus) | An early navigation plugin designed to move with Ctrl+h/j/k/l across Herdr panes and wrap at workspace boundaries. |
| [**ugurtarlig/herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker) | An early pane-picker prototype that overlays one-character hints on visible panes for direct keyboard focus. |
| [**rbb/herdr-cursor**](https://github.com/rbb/herdr-cursor) | A design-stage Cursor integration intended to report Cursor agent states to Herdr so they appear alongside other agents in the status interface. |
| [**malone-c/herdr-pane-balancer**](https://github.com/malone-c/herdr-pane-balancer) | An in-development layout manager that automatically rebalances pane sizes when splits are opened or closed, reducing cramped nested layouts. |
| [**GoCodeAlone/mission-control-provider-herdr**](https://github.com/GoCodeAlone/mission-control-provider-herdr) | An early Mission Control provider intended to use Herdr sessions as an external runtime. |
| [**robinbraemer/herdr-axi**](https://github.com/robinbraemer/herdr-axi) | An early command-line interface designed to make Herdr workspace operations easier for coding agents to use. |
| [**yoshimi-I/gengar.nvim**](https://github.com/yoshimi-I/gengar.nvim) | An early Neovim environment that keeps agents and Hunk-based diff review in Herdr while leaving Neovim focused on editing. |

---

## Resources

- **[Herdr Documentation](https://herdr.dev/docs/)**: The official manual covering installation, workspaces, keybindings, and configuration.
- **[Herdr Socket API Reference](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md)**: Protocol documentation for controlling Herdr programmatically over Unix domain sockets.
- **[Herdr Plugin Marketplace](https://herdr.dev/plugins/)**: The official directory of community plugins and integrations.
- **[Herdr Official Agent Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md)**: Standard instructions teaching LLM agents how to interact with Herdr.

## Reference

- **Agent Skill (`SKILL.md`):** Teach Claude, Pi, Codex, or OpenCode how to drive Herdr without external runtime dependencies.
- **Socket Client (`SOCKET_API.md`):** Connect to `~/.herdr/herdr.sock` using JSON commands to manage tabs, panes, and agents.
- **MCP Server:** Expose Herdr commands as tools to any Model Context Protocol host application.
- **Git Worktrees:** Pair Herdr tabs with isolated git worktrees (`git worktree add`) to run concurrent agents safely.
