# Awesome Herdr [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated plain-English index of tools built for **[Herdr](https://herdr.dev/)**, the terminal-native agent multiplexer.

Official links: [Website](https://herdr.dev/) · [GitHub](https://github.com/ogulcancelik/herdr) · [Documentation](https://herdr.dev/docs/) · [Plugin Marketplace](https://herdr.dev/plugins/) · [Agent Skill](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) · [Socket API](https://github.com/ogulcancelik/herdr/blob/master/SOCKET_API.md)

---

## Contents

1. [Run and orchestrate agents (853)](#1-run-and-orchestrate-agents)
   - [Official skill and foundation (1)](#official-skill-and-foundation)
   - [Multi-agent fleets and supervisors (106)](#multi-agent-fleets-and-supervisors)
   - [Swarm, mob, and consensus orchestrators (44)](#swarm-mob-and-consensus-orchestrators)
   - [Claude Code multi-agent teams (260)](#claude-code-multi-agent-teams)
   - [Claude Code: Account switchers and auth monitors (3)](#claude-code-account-switchers-and-auth-monitors)
   - [Pi supervisor workflows and extensions (133)](#pi-supervisor-workflows-and-extensions)
   - [Pi: Presence, memory, and status extensions (5)](#pi-presence-memory-and-status-extensions)
   - [Subagent launchers and delegation (114)](#subagent-launchers-and-delegation)
   - [Autonomous coding and pull-request loops (10)](#autonomous-coding-and-pull-request-loops)
   - [Task queues, backlogs, and event triggers (14)](#task-queues-backlogs-and-event-triggers)
   - [Linear, GitHub Issues, and issue-to-PR automation (25)](#linear-github-issues-and-issue-to-pr-automation)
   - [General workflows and skill packs (138)](#general-workflows-and-skill-packs)
2. [Connect through MCP and the socket API (237)](#2-connect-through-mcp-and-the-socket-api)
   - [MCP servers (14)](#mcp-servers)
   - [Socket API clients and SDKs (74)](#socket-api-clients-and-sdks)
   - [Chat alerts: Telegram, Discord, and Slack (22)](#chat-alerts-telegram-discord-and-slack)
   - [Desktop, mobile, and webhook notifications (48)](#desktop-mobile-and-webhook-notifications)
   - [Push notifications, APNs, and mobile alerts (2)](#push-notifications-apns-and-mobile-alerts)
   - [Telemetry, events, and quota streaming (18)](#telemetry-events-and-quota-streaming)
   - [Voice, hardware, and remote bridges (9)](#voice-hardware-and-remote-bridges)
   - [Protocol and third-party bridges (50)](#protocol-and-third-party-bridges)
3. [Editor integrations (121)](#3-editor-integrations)
   - [Neovim navigation and splits (43)](#neovim-navigation-and-splits)
   - [Full Neovim-hosted workspaces (16)](#full-neovim-hosted-workspaces)
   - [VS Code, Cursor, and dev containers (22)](#vs-code-cursor-and-dev-containers)
   - [Vim, Kakoune, and other editors (17)](#vim-kakoune-and-other-editors)
   - [REPL and code dispatchers (21)](#repl-and-code-dispatchers)
   - [Editor plugins and bridges (2)](#editor-plugins-and-bridges)
4. [Switch and restore sessions (175)](#4-switch-and-restore-sessions)
   - [Fuzzy session switchers and terminal pickers (130)](#fuzzy-session-switchers-and-terminal-pickers)
   - [Persistence, snapshots, and state restoration (30)](#persistence-snapshots-and-state-restoration)
   - [Workspace and multi-session management (15)](#workspace-and-multi-session-management)
5. [Worktrees and terminal experience (500)](#5-worktrees-and-terminal-experience)
   - [Git worktree automation (129)](#git-worktree-automation)
   - [Workspace lifecycle and multi-repository tools (4)](#workspace-lifecycle-and-multi-repository-tools)
   - [Diff review and code inspection (30)](#diff-review-and-code-inspection)
   - [File viewers and markdown previews (20)](#file-viewers-and-markdown-previews)
   - [Pane navigation and overlay hints (12)](#pane-navigation-and-overlay-hints)
   - [Terminal keybindings and shortcut helpers (105)](#terminal-keybindings-and-shortcut-helpers)
   - [Command palettes and workspace switchers (26)](#command-palettes-and-workspace-switchers)
   - [Status lines, sidebars, and tab synchronization (109)](#status-lines-sidebars-and-tab-synchronization)
   - [Status overlays, HUDs, and agent timers (24)](#status-overlays-huds-and-agent-timers)
   - [Context meters and rate-limit gauges (7)](#context-meters-and-rate-limit-gauges)
   - [Output inspection, logs, and transcripts (18)](#output-inspection-logs-and-transcripts)
   - [Security guards and collision detectors (4)](#security-guards-and-collision-detectors)
   - [Dotfiles and ready-made configuration (6)](#dotfiles-and-ready-made-configuration)
   - [Plugin collections and developer frameworks (6)](#plugin-collections-and-developer-frameworks)
6. [Apps, companion integrations, and installation (185)](#6-apps-companion-integrations-and-installation)
   - [Native desktop and mobile apps (14)](#native-desktop-and-mobile-apps)
   - [Web dashboards and remote viewers (22)](#web-dashboards-and-remote-viewers)
   - [Hardware and ambient displays (22)](#hardware-and-ambient-displays)
   - [Plugins and supporting utilities (103)](#plugins-and-supporting-utilities)
   - [Setup, packages, and version management (24)](#setup-packages-and-version-management)
7. [Experimental projects (15)](#7-experimental-projects)
   - [Experiments, concepts, and scaffolds (15)](#experiments-concepts-and-scaffolds)
8. [Resources](#resources)
9. [Reference](#reference)

---

## 1. Run and orchestrate agents

*853 projects. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.*

### Official skill and foundation

*1 project. The official instructions that teach an agent how to understand and control Herdr.*

| Project | What it does |
|---|---|
| [**ogulcancelik/herdr · SKILL.md**](https://github.com/ogulcancelik/herdr/blob/master/SKILL.md) | Teaches an agent inside a Herdr pane how to inspect workspaces, tabs, and panes, start helpers, send input, and wait for status changes. |

### Multi-agent fleets and supervisors

*106 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*

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
| [**meviusisback/agent-orchestr**](https://github.com/meviusisback/agent-orchestr) | Monitors live agent output and orchestrates multi-agent workspaces across Herdr, OpenCode, and Claude sessions. |
| [**hhdebb/herdr-radar**](https://github.com/hhdebb/herdr-radar) | Provides Readable Herdr sidebar: which agent is working, waiting on you, or abandoned, with groups, worktree trees and activity order, herdr plugins. |
| [**qintmb/herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui) | Renders Agent icon, vertically-aligned monochrome icons in the Herdr sidebar. rendered via a custom font with non-uniform glyph scaling that matches terminal cap-height sit flush with agent names, tabs, and workspace labels instead of appearing as tiny squares. |
| [**husniadil/herdr-swipe**](https://github.com/husniadil/herdr-swipe) | Provides Trackpad gestures for Herdr: move between panes, tabs and spaces, and jump to the agent waiting on you. |
| [**YogevKr/rai**](https://github.com/YogevKr/rai) | Provides Shepherd your coding-agent flock, a native macOS window for herdr: who's working, who's stuck, who's bleating for approval. |
| [**abhishek944/herdr-pets**](https://github.com/abhishek944/herdr-pets) | Provides a transparent desktop village for live Herdr agents. |
| [**Northern-Lighthouse/herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet) | Manages a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispatch, diskless workspaces. |
| [**enisbu/herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux) | Provides Trackpad gestures for Herdr on Linux: swipe between panes, tabs and spaces, tap to jump to the waiting agent. |
| [**jwarykowski/shepherd**](https://github.com/jwarykowski/shepherd) | Provides your todos herded. |
| [**husniadil/herdr-sched**](https://github.com/husniadil/herdr-sched) | Schedules and triggers for coding agents on Herdr - cron jobs and webhook/file-watcher triggers firing actions into the sibling plugins, each act signed by its principal, in one Go binary. |
| [**saxonmurray85-ops/sheprd**](https://github.com/saxonmurray85-ops/sheprd) | Provides Web UI and CLI llama.cpp agent deployer & Herdr workspace integration. |
| [**bonanyan/herdrbell**](https://github.com/bonanyan/herdrbell) | Provides Shepherd Your Agents-- Bell for Herdr APP. |
| [**fulanto/herdr-oncall**](https://github.com/fulanto/herdr-oncall) | Provides ping Telegram when an agent is blocked. |
| [**assawalhy/herdr-stay-awake**](https://github.com/assawalhy/herdr-stay-awake) | Keeps the machine from sleeping while any herdr agent pane is working (Linux, macOS, Windows, and WSL). |
| [**neospark-sol/agentflock**](https://github.com/neospark-sol/agentflock) | Provides AI-coordinated builder and reviewer groups with durable milestone control. |
| [**FunnyQ/q-workbench**](https://github.com/FunnyQ/q-workbench) | Provides agent launcher, project/SSH pickers, in-place agent restart. |
| [**vandemaelefelix/herdr-herd**](https://github.com/vandemaelefelix/herdr-herd) | Provides Herd your herd of AI agents, a pixel-art sheep for each, showing its live state at a glance. |
| [**sxp4931/herdr-manager**](https://github.com/sxp4931/herdr-manager) | Provides macos menu-bar app + MCP server for monitoring AI coding agents via herdr. |
| [**ihubanov/herdr-web**](https://github.com/ihubanov/herdr-web) | Provides Local web UI for the herdr agent runtime, over its socket API. |
| [**hkdom/herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate) | Provides Telegram approval inbox + risk-tiered auto-approval for your herdr AI agent fleet, blocked agents surface as Telegram cards with Approve/Deny buttons (zero-dependency Node.js). |
| [**gurronen/herdr-looper**](https://github.com/gurronen/herdr-looper) | Launches repeatable machine-local Pi jobs in fresh Herdr workspaces and worktrees. |
| [**waynewu411/herdr-event-log**](https://github.com/waynewu411/herdr-event-log) | Logs pane.agentstatuschanged (and future event types) to a durable, cursor-resumable global log any parent agent can tail. |
| [**chenxin-yan/herdr-micro**](https://github.com/chenxin-yan/herdr-micro) | Provides a physical MacroPad control deck for monitoring and controlling your coding agents in herdr. |
| [**heysanil/herdash**](https://github.com/heysanil/herdash) | Provides Terminal dashboard for herdr agent fleets: live agent status grouped by repo, with LLM-written summaries and an attention panel. |
| [**ShenghaiWang/helm**](https://github.com/ShenghaiWang/helm) | Provides an agent harness on top of Herdr for coordinating coding workflows. |
| [**moneycaringcoder/herdr-crook**](https://github.com/moneycaringcoder/herdr-crook) | Provides the shepherd's staff: shared library for herdr plugins. |
| [**slashv/st2-herdr**](https://github.com/slashv/st2-herdr) | Provides Herdr control plane integration for ST2 agent workspaces. |
| [**charlieYong/herdr-live**](https://github.com/charlieYong/herdr-live) | Orchestrates live multi-agent harnesses in Herdr, dispatching prompts and streaming status outputs. |
| [**EdJ/wsp**](https://github.com/EdJ/wsp) | Provides Herdr project workspaces. |
| [**dsh-blue/herdr-agent-state**](https://github.com/dsh-blue/herdr-agent-state) | Provides dsh plugin: report agent state (working/blocked/idle) and session ref to Herdr's pane socket integration. |
| [**oguzcanhuner/shepherd**](https://github.com/oguzcanhuner/shepherd) | Provides an agent OS for herdr. |
| [**joelhooks/herdr-janitor**](https://github.com/joelhooks/herdr-janitor) | Provides Guarded Terra judgment and stale-worker cleanup for Herdr. |
| [**lunoob/mini-orchestrator**](https://github.com/lunoob/mini-orchestrator) | Orchestrates custom Herdr script workflows using TypeScript. |
| [**mikro-design/super-herdr**](https://github.com/mikro-design/super-herdr) | Provides a multi-host TUI and paired browser control plane for persistent Herdr clusters across remote servers. |
| [**leifarriens/shepherd**](https://github.com/leifarriens/shepherd) | Provides Herdr Flock Manager. |
| [**HarshaLakkaraju/herdr-orchestrator-skill**](https://github.com/HarshaLakkaraju/herdr-orchestrator-skill) | Provides Agent Skill for orchestrating multi-agent coding workflows in Herdr with planning, model routing, shared artifacts, review, testing, and pane cleanup. |
| [**TinocoAI/herdr-checkpoint-health**](https://github.com/TinocoAI/herdr-checkpoint-health) | Provides Read-only Check Point GAiA health check as a Herdr plugin (cpwdadmin + top + fw ver). Cross-platform. |
| [**shoaibkhanz/herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump) | Provides cycle focus forward/backward through in-flight (working/blocked) agents in layout order, the vim-motion complement to attention-jump. |
| [**derekr/wherdr**](https://github.com/derekr/wherdr) | Provides a web UI for herdr. |
| [**lewtec/rterm**](https://github.com/lewtec/rterm) | Provides Mac supervisor for detachable herdr, tmux, and screen sessions. |
| [**Roshvan/herdr-plugin-shortcut-shepherd**](https://github.com/Roshvan/herdr-plugin-shortcut-shepherd) | Provides Shortcut insights and gentle coaching for Herdr. |
| [**raystyle/evo-harness**](https://github.com/raystyle/evo-harness) | Provides Six-stage Graph-of-Loops orchestrator driving codex/kimi/claude in rmux panes. Control plane rmux x ops plane herdr: single-pane console + decision-injection daemon, non-blocking human-in-the-loop. |
| [**hdosys/herdr-sandbox**](https://github.com/hdosys/herdr-sandbox) | Provides a windows-native counterpart to a dev container. |
| [**scrappylabsai/podr**](https://github.com/scrappylabsai/podr) | Provides Pod, herdr for whale bros: reasonix (voice) + evolv (DeepSeek Harness) batteries included. |
| [**harlanljones/herdr-outpost**](https://github.com/harlanljones/herdr-outpost) | Provides a remote dashboard and relay gateway for Herdr sessions. |
| [**TheRealHaoLiu/dsh-herdr**](https://github.com/TheRealHaoLiu/dsh-herdr) | Provides DeepSeek Harness lifecycle reporting for Herdr panes. |
| [**SimplicityGuy/herdr-corral**](https://github.com/SimplicityGuy/herdr-corral) | Provides Visual editor for herdr's config.toml. Corral your agents' layout, keys, and theme, then download the file. |
| [**patraianton/sheepdog**](https://github.com/patraianton/sheepdog) | Provides a live kanban board that herds your coding-agent fleet, one card per herdr session, columns by what needs you, cards move by themselves, one human operator. |
| [**ravikanchikare/herdr-agent-factory**](https://github.com/ravikanchikare/herdr-agent-factory) | Provides Agent Factory is the control plane for building, running, and evaluating AI agents on Herdr. |
| [**letya999/workflow-herdr**](https://github.com/letya999/workflow-herdr) | Provides a YAML-configurable workflow for coordinating AI agents in Herdr with customizable roles and state validation. |
| [**dev-town/harbr**](https://github.com/dev-town/harbr) | Provides Harbour TUI. |
| [**rohanthewiz/cats**](https://github.com/rohanthewiz/cats) | Provides Like herdr, but Go and web flavored. |
| [**joshuaswarren/omarchy-fleet-shepherd**](https://github.com/joshuaswarren/omarchy-fleet-shepherd) | Provides Read-only Herdr agent operations and OMP usage telemetry across an Omarchy connector fleet. |
| [**mrpbennett/qs-herdr-agents**](https://github.com/mrpbennett/qs-herdr-agents) | Displays Herdr agent panels inside the Omarchy quick-switch menu. |
| [**jaltez/agent-notify**](https://github.com/jaltez/agent-notify) | Provides Tray companion for AI coding agents. Live herdr session status, attention popups, and webhooks. |
| [**0-CYBERDYNE-SYSTEMS-0/herdr-dev-team**](https://github.com/0-CYBERDYNE-SYSTEMS-0/herdr-dev-team) | Provides reusable seven-agent development team orchestration for Herdr. |
| [**gregmcausland/herdr-control**](https://github.com/gregmcausland/herdr-control) | Provides a browser control and orchestration surface for Herdr panes. |
| [**tlamadon/herdr-hq**](https://github.com/tlamadon/herdr-hq) | Provides Web dashboard for herdr agents across machines: status, per-agent CPU/memory, git state, listening ports, and a live terminal per pane. |
| [**DerekStride/agent-orchestrator**](https://github.com/DerekStride/agent-orchestrator) | Provides Agent orchestrator that drives one dependency-scoped task graph. |
| [**dinhlongviolin1/arco**](https://github.com/dinhlongviolin1/arco) | Provides arco, a self-hosted daemon that supervises a fleet of coding-agent workers (clavis + herdr). Pre-alpha / design phase. |
| [**mikevalstar/herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title) | Pins the outer terminal title to the Herdr hostname and active workspace. |
| [**C1TRuSovo831/herdr-codex-team**](https://github.com/C1TRuSovo831/herdr-codex-team) | Provides Turn Herdr into a multi-team Codex development workspace with isolated Planner, Coder, and Reviewer agents. |
| [**wenhao4126/dsh-herdr**](https://github.com/wenhao4126/dsh-herdr) | Exposes Herdr workspaces, panes, and coding agents as DeepSeek Harness tools. |
| [**nativestrider/herdr-mesh-safe**](https://github.com/nativestrider/herdr-mesh-safe) | Provides Safety-scoped MCP bridge for lease-managed Herdr agents. |
| [**erdostom/herdr-orchestrate**](https://github.com/erdostom/herdr-orchestrate) | Provides User herdr and opencode to manage a fleet of AIs to help with development. |
| [**kylezk777/herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator) | Provides Herdr-orch is a file-based agent orchestration tool that runs on top of Herdr. |
| [**possibilities/agentkeys**](https://github.com/possibilities/agentkeys) | Audits keyboard shortcuts across Karabiner, skhd, Ghostty, Orca, tmux, herdr, and Neovim. |
| [**bbgo19/herdr-web**](https://github.com/bbgo19/herdr-web) | Provides a herdr web ui. |
| [**reoring/sheltie**](https://github.com/reoring/sheltie) | Provides Manifest-declared local orchestration for OMP Agents in Herdr workspaces. |
| [**cenvu/cen-harness-hud**](https://github.com/cenvu/cen-harness-hud) | Provides Local-first terminal HUD for AI coding agents, account, quota, balance, and Herdr status integrations. |
| [**morpheus-sh/panopticon**](https://github.com/morpheus-sh/panopticon) | Provides Vibecoded Herdr-compatible, tmux-based agent supervisor. |
| [**Vinal-Vin/rig**](https://github.com/Vinal-Vin/rig) | Provides Cross-platform setup script for Herdr, Wexterm, Firstmate, and axi tooling. |
| [**ai-meow/felix**](https://github.com/ai-meow/felix) | Provides Talk to one cat, ship with the clowder, an LLM orchestrator running a crew of agents in git worktrees, visualized in herdr. Per-repo, standards-first. |
| [**m4ttyk/captain-bridge**](https://github.com/m4ttyk/captain-bridge) | Provides Local agent orchestration for Herdr and OMP-Pi. |
| [**hkandala/orchestratr**](https://github.com/hkandala/orchestratr) | Provides cross-provider orchestrator for agents, built on herdr. |
| [**Lbryany/dsh-herdr**](https://github.com/Lbryany/dsh-herdr) | Provides Herdr lifecycle status integration for DeepSeek Harness. |
| [**timjonez/slack-herd**](https://github.com/timjonez/slack-herd) | Launches Herdr work from Slack @mentions. |
| [**xenking/omp-extensible-workflows**](https://github.com/xenking/omp-extensible-workflows) | Provides OMP-native Beads supervisor for dependency-aware workers in isolated Herdr workspaces. |
| [**AsgardMuninn/asgardmuninn.ainoch**](https://github.com/AsgardMuninn/asgardmuninn.ainoch) | Provides AI Notch, Dynamic Island for herdr harnesses (macOS, SwiftUI). |
| [**scttymn/ranchr**](https://github.com/scttymn/ranchr) | Provides Ranch hand for coding agents on your PC. Local Herdr PWA first; remote relay next. |
| [**sunny0826/dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr) | Provides Herdr control-plane plugin for DeepSeek Harness (DSH): observe and drive Herdr, a terminal workspace manager for AI coding agents, from DSH sessions. |
| [**ankurCES/minim-coder**](https://github.com/ankurCES/minim-coder) | Provides minim-coder, local-only agentic coding harness (llama.cpp + openbmb/MiniCPM5-1B-GGUF). herdr-aesthetic TUI, LAN WebSocket UI, thinking on by default, goal-based self-healing execution. |
| [**Nunley-Media-Group/nmg-visuals**](https://github.com/Nunley-Media-Group/nmg-visuals) | Provides Local-first visual artifacts for Oh My Pi, Herdr, and Tailscale. |
| [**lufs-audio/snuze**](https://github.com/lufs-audio/snuze) | Provides Agent alarm clock in Rust: set timers, watch Jules sessions and herdr pane states, listen for webhook signals, get woken up. No polling, so fewer wasted tokens. |
| [**TonyPorj/boss-mad**](https://github.com/TonyPorj/boss-mad) | Provides Boss/MAD: give it a goal, Hermes spawns a crew in Herdr tabs, they work in parallel, Hermes verifies and hands off. Local Windows-native multi-agent orchestration. |
| [**Rocco-Gossmann/Herdr-Workspace**](https://github.com/Rocco-Gossmann/Herdr-Workspace) | Creates a Herdr-Workspace with multiple Tabs + Splits in one command in your default session. |

### Swarm, mob, and consensus orchestrators

*44 projects. Parallel agent swarms, mob-programming groups, and multi-model consensus engines.*

| Project | What it does |
|---|---|
| [**powerfooI/herdr-studio**](https://github.com/powerfooI/herdr-studio) | Provides a web client for Herdr with mobile optimization, browser terminals, workspace management, and session inspection. |
| [**arronKler/pairfob**](https://github.com/arronKler/pairfob) | Provides a phone companion surface for Herdr to monitor Codex, Claude, and Grok runs remotely. |
| [**barnuri/herdr-web**](https://github.com/barnuri/herdr-web) | Provides a mobile-first web interface for Herdr to monitor and drive coding agents from any device browser. |
| [**zlxlabs/herdweb**](https://github.com/zlxlabs/herdweb) | Monitors and drives coding agents from mobile devices, supporting voice input, image pasting, webhooks, and multi-device servers. |
| [**luiscleto/shepherdr**](https://github.com/luiscleto/shepherdr) | Provides a phone-friendly web interface for Herdr: monitor agents, receive notifications, open real terminals, and send files. |
| [**herdr-go/herdr-go**](https://github.com/herdr-go/herdr-go) | Controls your herdr coding agents from anywhere, private, P2P, EasyTier-secured. |
| [**TinocoAI/scp-explorer**](https://github.com/TinocoAI/scp-explorer) | Provides MobaXterm-style SCP file explorer herdr plugin (cross-platform macOS/Linux/Windows). |
| [**gabriel-laet/herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor) | Provides Cursor cloud agents as first-class herdr panes. |
| [**jmarbutt/herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status) | Shows GitHub pull request status on herdr spaces, with a Conductor-style PR board. |
| [**jolo-dev/herdr-workspace-icons**](https://github.com/jolo-dev/herdr-workspace-icons) | Provides Herdr extension that adds icons to Workspace sidebar items. |
| [**kosumic/whip**](https://github.com/kosumic/whip) | Connects mobile devices to Herdr as an agent-native SSH client designed specifically for multiplexer workflows. |
| [**dibin666/herdr-remote**](https://github.com/dibin666/herdr-remote) | Provides Remote browser access to your Herdr terminal workspaces. |
| [**bonkey/herdr-stack-icon**](https://github.com/bonkey/herdr-stack-icon) | Displays technology stack icons beside each workspace based on repository file detection. |
| [**ArtMoreno/herdr-swarm**](https://github.com/ArtMoreno/herdr-swarm) | Races coding agents in Herdr panes and isolated Git worktrees, compare their diffs, and apply a winner. |
| [**neospeed83/herdr-tournament**](https://github.com/neospeed83/herdr-tournament) | Provides adversarial multi-agent code reviews for Herdr. |
| [**JefeLabs/herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker) | Provides a self-hosted REST and WebSocket API for Herdr to spawn and steer coding agents with parent-child federation. |
| [**dark2momo/herdr-tty**](https://github.com/dark2momo/herdr-tty) | Provides a mobile-friendly web terminal for Herdr powered by ttyd. |
| [**fellnerse/herdr-mobile**](https://github.com/fellnerse/herdr-mobile) | Provides a minimal mobile web interface for Herdr agent management. |
| [**SandroHub013/herdr-mobile**](https://github.com/SandroHub013/herdr-mobile) | Provides Remote control for Herdr from Android, iPhone and the browser: live terminals, prompts and files over Tailscale, with a token-protected bridge on the PC. |
| [**Lawofaveragesproterozoicaeon236/web-terminal**](https://github.com/Lawofaveragesproterozoicaeon236/web-terminal) | Provides Self-hosted, mobile-first web terminal with Ghostty's VT engine, persistent sessions, file explorer, and herdr integration. |
| [**momentohq/mo-herdr**](https://github.com/momentohq/mo-herdr) | Runs mo inside herdr panes: session restore after a herdr restart, a launch action, and SIGKILL cleanup. |
| [**l20250208/herdr-consensus**](https://github.com/l20250208/herdr-consensus) | Provides Herdr Consensus: dual-agent review consensus, human adjudication, locked fix plan, isolated worktree fix, and unified reporting. |
| [**cobanov/herdrchat**](https://github.com/cobanov/herdrchat) | Controls your herdr coding agents from your phone (iOS + Android). |
| [**klukacin/herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees) | Provides mirror a hub worktree into every nested sub-repo clone. |
| [**Orchard-Robotics/herdview**](https://github.com/Orchard-Robotics/herdview) | Views your herd from the web. |
| [**bandoyer/swarm-forge-herdr**](https://github.com/bandoyer/swarm-forge-herdr) | Provides Disciplined AI agent swarms on herdr, a port of the swarm-forge philosophy. |
| [**SoMaCoSF/colloquy**](https://github.com/SoMaCoSF/colloquy) | Provides Self-addressing, ephemerally-cached causal DAG audit logs and telemetry for agent swarms. |
| [**teasec4/herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app) | Streams live agent terminal output to mobile devices, displays status updates, and dispatches prompts over LAN or Tailscale. |
| [**ultivis-iot/HerdRabbit**](https://github.com/ultivis-iot/HerdRabbit) | Provides a personal PWA for controlling your Herdr sessions. |
| [**keinstn/drover**](https://github.com/keinstn/drover) | Provides Drive your Herdr AI agents from your phone. |
| [**jellyfishmobile/herdup**](https://github.com/jellyfishmobile/herdup) | Provides Desktop launcher for herdr agent teams: template-driven multi-agent workspaces with preflight, staged sign-in, and role briefings. |
| [**agrestisdavid/terminal-cards**](https://github.com/agrestisdavid/terminal-cards) | Provides Herdr-inspired terminal-style Lovelace card bundle for Home Assistant. |
| [**pbogut/opencode-pocket**](https://github.com/pbogut/opencode-pocket) | Provides Mobile first, web based inteface to interact with your local OpenCode sessions. |
| [**arDaraz/crewboss**](https://github.com/arDaraz/crewboss) | Provides Spawn isolated agent sessions (Claude, Codex, .) in dedicated git worktrees and drive them from your current session via herdr + worktrunk. |
| [**LamplitIsles/kepos-herdr-mobile**](https://github.com/LamplitIsles/kepos-herdr-mobile) | Provides mobile your herdr anywhere. |
| [**bandoyer/swarm-forge-windows**](https://github.com/bandoyer/swarm-forge-windows) | Provides a Windows distribution of swarm-forge-herdr for running AI agent swarms on the Herdr runtime. |
| [**tuanhung303/herdr-swarm**](https://github.com/tuanhung303/herdr-swarm) | Provides Visible multi-harness agent orchestration in Herdr tabs, canonical pane grids, comm.md mailbox routing, wait/collect lifecycle. |
| [**dpulpeiro/omarchy-herdr-collie**](https://github.com/dpulpeiro/omarchy-herdr-collie) | Provides Omarchy bar widget to monitor and control Collie over Tailscale. |
| [**SynthSwarm/herdr-envoy**](https://github.com/SynthSwarm/herdr-envoy) | Provides opencode plugin: dispatch bounded tasks to real peer opencode agents (envoys) in their own git worktrees, spawned as split panes in herdr. Auto-verify + optional auto-merge. |
| [**StructuPath/herdr-suite-site**](https://github.com/StructuPath/herdr-suite-site) | Provides Landing page for the StructuPath Herdr Suite, herdr.structupath.ai. |
| [**radityasurya/taut**](https://github.com/radityasurya/taut) | Provides a mobile-first PWA hub for herdr and tmux: see every coding agent's state from your phone and reply, over Tailscale. |
| [**nourhelmi/herdr-mobile**](https://github.com/nourhelmi/herdr-mobile) | Provides Herdr Mobile, iOS client and Bun sidecar for controlling Herdr agents over Tailscale. |
| [**herdr-go/herdr-go.github.io**](https://github.com/herdr-go/herdr-go.github.io) | Provides Official website for HerdrGo, the mobile companion for Herdr coding agents. |
| [**tliuyx/tliuyx.github.io**](https://github.com/tliuyx/tliuyx.github.io) | Provides Private operator PWA for Herdr Mobile Relay. |

### Claude Code multi-agent teams

*260 projects. Adapters and skills that organize Claude Code sessions into structured teams.*

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
| [**yigitkonur/herdr-pm**](https://github.com/yigitkonur/herdr-pm) | Adds a technical project manager to each live agent tab that reads session state and guides the agent. Supports Claude, Codex, Pi, and Hermes with optional persistent notes. |
| [**LittleDrinks/herdr-orchestrator-skill**](https://github.com/LittleDrinks/herdr-orchestrator-skill) | Turns the main Claude Code session into a coordinator that plans work, starts workers in Herdr panes, and monitors them without editing code itself. It includes Python monitors, a YAML state-machine template, and role prompts. |
| [**bakescakes/claude-orchestration**](https://github.com/bakescakes/claude-orchestration) | Provides five orchestration skills and hooks for Claude Code to manage parallel backlogs from QA to deployment. |
| [**clawsouls/clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin) | Applies ClawSouls persona definitions to agents running in Herdr. It sets role-specific environments and behavioral rules for Claude Code and other supported agents across multiple panes. |
| [**kiitosu/herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board) | Embeds a Jira Kanban board in a Herdr pane with one-key Claude Code session launching and live card status updates. |
| [**chetanunadkat-lang/herdr-fleet**](https://github.com/chetanunadkat-lang/herdr-fleet) | Runs Claude and Codex workers as a fleet in Herdr panes. The project includes orchestration skills, an `hm` command-line tool, agent definitions, and a Claude Code installer. |
| [**terafin/herdr-restart-always**](https://github.com/terafin/herdr-restart-always) | Supervises processes running in Herdr agent panes and restarts them after a crash. It works with Claude, Hermes, Codex, Pi, OpenCode, and other pane-based agents. |
| [**aigorahub/herdr-lantern**](https://github.com/aigorahub/herdr-lantern) | Illuminates active Herdr agents in the field and highlights who needs input and what they are working toward. |
| [**missuo/herdrm**](https://github.com/missuo/herdrm) | Provides a native macOS console for Herdr to drive coding agents and monitor live terminals across devices. |
| [**permgps/herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents) | Provides Drive your coding agents from Telegram like from the terminal. A topic per agent, live status in the topic icon, two-way chat with inline buttons for choices. |
| [**neptunix/corral**](https://github.com/neptunix/corral) | Provides a kanban dashboard and control surface for Claude Code sessions running in herdr. |
| [**testy-cool/herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config) | Provides a workspace to tab to agent sidebar preset for Herdr with compact tab groups and provider icons. |
| [**nikok6/herdr-pet**](https://github.com/nikok6/herdr-pet) | Provides Tiny desk pet on your herdr panes: types, waits, and celebrates with your agent. Works with any Codex pet. |
| [**Matovidlo/herdr-pr-tracker**](https://github.com/Matovidlo/herdr-pr-tracker) | Tracks the GitHub PR each Claude Code session produces, with gh state + actions. |
| [**killerz3/herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler) | Auto-titles Herdr tabs using local agy, claude, codex, or opencode harnesses without external API keys. |
| [**AltanS/herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert) | Provides prompt-cache countdown on every agent pane, with every cache rule sourced and dated. |
| [**speardragon/herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar) | Provides AI agent plan-usage gauges (Claude Code / Codex / Grok) in the herdr tab bar. |
| [**anhnd3005-infinity/herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) | Dispatches tasks to CLI agent workers via Herdr panes with stateful task tracking, worktree isolation, and diff-based review. |
| [**kvkenyon/herdr-quota**](https://github.com/kvkenyon/herdr-quota) | Provides See Claude, Codex, Cursor, and Kimi subscription quota at a glance in Herdr. |
| [**loofare/herdr-portal**](https://github.com/loofare/herdr-portal) | Provides Mission-control dashboard for herdr, aggregates every workspace/tab/pane agent into a live TUI kanban (keyboard + mouse) plus a web big-screen: structured progress, Ctrl+B A to open, click-to-jump, reply to agents from the browser. |
| [**calebcav/token-usage**](https://github.com/calebcav/token-usage) | Provides Local token usage dashboard for Herdr across Codex, Claude Code, OpenCode, and custom coding harnesses. |
| [**ProjectAJ14/herdr-warp**](https://github.com/ProjectAJ14/herdr-warp) | Provides which lets Herdr send notification via Warp. |
| [**dkbo/herdr-model-badge**](https://github.com/dkbo/herdr-model-badge) | Shows each agent's model and reasoning effort in the agents sidebar. |
| [**jeffbking/herdr-agent-prompt**](https://github.com/jeffbking/herdr-agent-prompt) | Views the focused coding agent's original prompt (Claude Code, Codex, Antigravity, Pi) in an overlay on prefix+p. |
| [**tntpgh/herdr-control**](https://github.com/tntpgh/herdr-control) | Provides Multi-agent orchestration for herdr: spawn/route AI coding agents into tabs and worktrees, sort/colour tabs by branch state, and a 2-way Slack bridge so agents can push you a question and take your reply. Bash + Python, no framework, no install step. |
| [**rcosteira79/herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch) | Provides Hot-swap Claude Code / Codex logins without re-authenticating. Overlay picker, cycle-to-next keybinding, and a per-pane account badge ($acct). |
| [**rcosteira79/herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue) | Watches agents for usage-limit walls, badges the countdown to the reset ($wall), and re-prompts the agents you armed once the window reopens. |
| [**naturalmoods/herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify) | Provides Telegram notification when an agent finishes or gets blocked, session title, project, duration, token use and its last message, and your reply in the chat goes back to that agent. |
| [**LZHcode1986/herdr-link**](https://github.com/LZHcode1986/herdr-link) | Provides Faster, token-efficient, and zero-reasoning cross-agent interoperability for Herdr sessions. Replaces heavyweight skills with a unified contract for peer discovery, messaging, and pane lifecycle. |
| [**nengqi/herdr-session-sync**](https://github.com/nengqi/herdr-session-sync) | Provides Auto-sync Claude Code, Codex & Agent session names across Herdr pane labels, PTY window titles, and mobile companion apps (Heeler). |
| [**salemsayed/omaherd**](https://github.com/salemsayed/omaherd) | Provides Your coding agents, in the Omarchy bar: who needs you, what each HerdR agent is doing, local and remote. |
| [**KarthusLorin/herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator) | Provides Preserve interactive Herdr agent TUIs without model-driven status polling. |
| [**hamidi-dev/herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab) | Provides a live per-agent AI spend from OpenTab in the Herdr sidebar. |
| [**miko-misa/herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd) | Provides Automatic SSH port forwarding for coding agents on remote machines: Ctrl+click the localhost URL your agent printed and the page opens on your machine, same port. A Herdr plugin. |
| [**terry-li-hm/herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat) | Provides a shared local Herdr room for Pi, Claude Code, Codex, and Grok Build. |
| [**terry-li-hm/herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes) | Provides Codex, Claude Max and Grok quota in the workspace row, plus quota-aware model-class lanes (ag) for new agents. |
| [**HalloSouf/subherd**](https://github.com/HalloSouf/subherd) | Provides a herdr plugin that shows what every Claude Code subagent is doing, grouped by the workspace its session runs in. |
| [**blaxel-ai/herdr-blaxel-sandbox-plugin**](https://github.com/blaxel-ai/herdr-blaxel-sandbox-plugin) | Runs coding agents in persistent Blaxel sandboxes from Herdr. |
| [**itisbryan/herdr-usage**](https://github.com/itisbryan/herdr-usage) | Provides Claude, Codex, and OpenCode usage quotas. |
| [**sm-yjr/herdr-coordinator**](https://github.com/sm-yjr/herdr-coordinator) | Coordinates Herdr agent fleets across multiple terminal panes. |
| [**vaclavik-xyz/herdeck**](https://github.com/vaclavik-xyz/herdeck) | Controls panel for AI coding agents running under herdr, on a hardware Stream Deck (Ulanzi D200 or Elgato), a native desktop app, or a browser simulator. See blocked agents at a glance; Approve / Deny / Stop with one press. |
| [**frizynn/nenu**](https://github.com/frizynn/nenu) | Provides a self-hosted web workbench for supervising Herdr coding agents from desktop or phone. |
| [**ctbaum/herdr-deck**](https://github.com/ctbaum/herdr-deck) | Provides the companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovim, agent, shell, and lazygit deck. |
| [**iYassr/shahi**](https://github.com/iYassr/shahi) | Reads agent conversations, answer permission prompts, and manage herdr sessions from your phone or browser. |
| [**e-kotov/herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit) | Provides Prompt-cache HUD tokens, real-time expiration alerts, and dynamic agent sorting for Herdr. |
| [**marcelpanse/herdr-osx-menubar**](https://github.com/marcelpanse/herdr-osx-menubar) | Provides macos menu bar icon for herdr - jump back to your session, open a project, and see which agent is waiting for input. |
| [**DO-Solutions/herdr-mars-plugin**](https://github.com/DO-Solutions/herdr-mars-plugin) | Provides DigitalOcean Managed Agents (Mars): start, attach, and manage sessions from Herdr panes. |
| [**ArnaudRinquin/herdr-quotabar**](https://github.com/ArnaudRinquin/herdr-quotabar) | Provides Claude plan quotas (5h / 7d / per-model) as one compact line in the Herdr tab bar. Provider-pluggable. |
| [**lebryk/herdr-events**](https://github.com/lebryk/herdr-events) | Provides Durable external events for Herdr agents through native Codex, Claude Code, Pi, and OpenCode adapters. |
| [**taku-hatano/herdr-usage**](https://github.com/taku-hatano/herdr-usage) | Provides Claude Code / Codex usage sidebar tokens and dashboard plugin for herdr. |
| [**tkmct/herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify) | Provides a Herdr plugin that shows a Windows desktop toast when an agent (Claude Code, etc.) running under WSL2 becomes done (finished) or blocked (waiting for approval/input). |
| [**kewah/herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles) | Names panes and tabs automatically based on the first coding-agent prompt. |
| [**jtnovellis/herdr-nvim**](https://github.com/jtnovellis/herdr-nvim) | Provides Neovim inside Herdr: a per-tab full-height sidebar, and a real round trip with your coding agent, ask about the code you're looking at, read the answer without leaving Neovim, and step through the edits it made. |
| [**arvemy/herdr-convo**](https://github.com/arvemy/herdr-convo) | Reads another coding agent's conversation as normalized turns, one shape across Claude Code, Codex, OpenCode and Pi. |
| [**Ghost-LZW/pane-identity**](https://github.com/Ghost-LZW/pane-identity) | Displays pane IDs, hostnames, and labels in Herdr without modifying your agents. |
| [**KeithMoc/herdr-tokenlens**](https://github.com/KeithMoc/herdr-tokenlens) | Provides a live carrying-cost and compact-breakeven meter for AI coding agents, as a herdr pane. |
| [**parker-brown-family/herdr-auto-warm-cache**](https://github.com/parker-brown-family/herdr-auto-warm-cache) | Provides a herdr plugin that keeps an idle agent's prompt cache warm before the one-hour TTL expires, 20x cheaper than letting it lapse. Asks before it types, and never types into a pane that is waiting on you. |
| [**wazum/herdr-kibitzr**](https://github.com/wazum/herdr-kibitzr) | Asks your coding agent to review the comments it just wrote, so what explains something stays and the noise goes. A herdr plugin for Claude Code, Codex and any other agent, with no human in the loop. |
| [**chandrasekharan98/herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save) | Provides Save a Herdr workspace, layout, cwds, agent sessions, running commands, and reopen it later from an fzf picker. |
| [**GNURub/herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket) | Provides a durable, ordered prompt bucket for coding agents running in Herdr. |
| [**wazum/herdr-polyglot**](https://github.com/wazum/herdr-polyglot) | Provides Write coding-agent prompts in your own language, DeepL or Google Cloud Translate translates them to English and delivers them into Claude Code, Codex or any herdr agent pane. |
| [**enisbu/herdr-kitty-theme-sync**](https://github.com/enisbu/herdr-kitty-theme-sync) | Provides Push Herdr's active theme into kitty's ANSI palette, so pane content matches Herdr's chrome. |
| [**hxy91819/herdr-auto-title**](https://github.com/hxy91819/herdr-auto-title) | Provides automatic task titles for agent tabs - event-driven, T0 draft on first prompt + T1 final on turn settle. |
| [**peria-ai/precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin) | Provides PRECC plugin for herdr: cross-agent token-savings telemetry + one-touch PRECC setup. |
| [**asermax/herdr-tab-command**](https://github.com/asermax/herdr-tab-command) | Starts an agent or runs a command in a new tab, based on the name you give the tab. |
| [**terry-li-hm/herdr-bots**](https://github.com/terry-li-hm/herdr-bots) | Provides Local scheduled coding agents for Herdr, with pinned routes, isolated runs, and an evidence-backed inbox. |
| [**skellleks/lasso**](https://github.com/skellleks/lasso) | Provides Review pane for herdr: per-agent diffs with syntax highlighting and inline comments sent back to the agent. |
| [**tmastalirsch/herdr-claude-safe-compact**](https://github.com/tmastalirsch/herdr-claude-safe-compact) | Compacts idle Claude Code panes, but only once a handoff is safely on disk. |
| [**jordanhawkes/herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics) | Provides Context, session-token and account-limit metrics for Claude Code, Codex and TraeX in the Herdr sidebar. Maintained continuation of szrenwei/herdr-agent-metrics. |
| [**kwanwooi25/herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota) | Provides Agent quota for Herdr, token & cost dashboard, sidebar quota gauges, and tab bar summary for Claude Code, Codex, and Grok. |
| [**andthezhang/herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow) | Provides JavaScript workflows for orchestrating coding-agent CLIs in Herdr. |
| [**tomoya55/cmux-herdr**](https://github.com/tomoya55/cmux-herdr) | Propagates agent status (working / waiting for input / finished) to the cmux sidebar. |
| [**chano-gpt/setnet**](https://github.com/chano-gpt/setnet) | Provides Herd multi-harness coding agents from your phone, a Herdr plugin. |
| [**hapo-nghialuu/hod**](https://github.com/hapo-nghialuu/hod) | Coordinates Codex, Claude Code, and Grok Build agents safely through Herdr. |
| [**KennethWKZ/herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs) | Provides Make ccs claude behave like native Claude Code in Herdr: pane detection + launcher-aware restore through ccs. |
| [**jerryfane/herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve) | Approves Claude Code plan-mode dialogs automatically in Herdr so agents can transition to execution without pauses. |
| [**shrivatsas/herdr-model-capacity**](https://github.com/shrivatsas/herdr-model-capacity) | Provides Herdr pane for account-level Claude, Codex/OpenAI, and OpenRouter capacity. |
| [**yukimaru77/herdr-latex-reflow**](https://github.com/yukimaru77/herdr-latex-reflow) | Renders AI-agent LaTeX in Herdr with transparent overlays, terminal-cell replacement, and inline reflow. |
| [**oppenheimor/herdr-prompts**](https://github.com/oppenheimor/herdr-prompts) | Provides Save, search, fill, and reuse prompt templates across coding agents in Herdr. Inspired by my friend: bingguanqi. |
| [**tmastalirsch/herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter) | Provides Claude Code context usage as a bar, in the status line and in a herdr pane. |
| [**shaun-agent/herdr-map**](https://github.com/shaun-agent/herdr-map) | Renders visual Mermaid diagrams mapping Herdr architecture, socket APIs, and workspace concepts. |
| [**qluto/collie**](https://github.com/qluto/collie) | Provides an unattended-work box for Claude Code sessions on Herdr: toss tasks in by day, spend leftover token quota on them at night, collect the results in the morning. |
| [**sushi-killer/sushiAI**](https://github.com/sushi-killer/sushiAI) | Provides Your agents. One workspace. |
| [**TheBrunoPetkovic/herdr-context-display**](https://github.com/TheBrunoPetkovic/herdr-context-display) | Provides Colour-coded context window usage on every Claude Code agent row in herdr. |
| [**rcosteira79/herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge) | Marks idle agents that still have background shells running. |
| [**jmcjm/Hivemind**](https://github.com/jmcjm/Hivemind) | Coordinates a swarm of Claude Code agents in Herdr terminal panels using file-based briefs and asynchronous mail. |
| [**Marie673/herdr-env**](https://github.com/Marie673/herdr-env) | Configures an integrated Herdr, ghq, and Claude Code workspace environment mapping one branch to each agent worktree. |
| [**scaccogatto/vite-plugin-herdr**](https://github.com/scaccogatto/vite-plugin-herdr) | Picks a DOM element in your Vite app and send it, with a prompt, to a coding agent running in herdr. |
| [**radres/herdr-plugin-call-me**](https://github.com/radres/herdr-plugin-call-me) | Provides Ring your real phone when a herdr agent is blocked, answer by voice, and your answer becomes the keypress the agent was waiting for. |
| [**christiangroth/herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal) | Provides Name every Herdr tab after the terminal title of the agent inside it. One /rename in Claude Code names your session and the tab. |
| [**VoidAxon/herdr-lens**](https://github.com/VoidAxon/herdr-lens) | Provides Select text in a Herdr pane, press a key, read it in your own language. Translation, dictionary, identifier lookup and summaries, stdlib-only, zero config. |
| [**Efeguclu1/herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard) | Provides Explain and safely stop dev servers left running by coding agents. |
| [**nytafar/herdr-spawn**](https://github.com/nytafar/herdr-spawn) | Provides One MCP tool that hands a prompt from a chat to a real Claude Code session on one of your hosts, with Remote Control on. |
| [**eliasstravik/herdr-chat**](https://github.com/eliasstravik/herdr-chat) | Provides a live structured chat view for agents running inside Herdr. |
| [**binthnay1973/deepthink**](https://github.com/binthnay1973/deepthink) | Provides Multi-agent deep research + human-led decisions as Claude Code slash commands, Fable 5 orchestrates Opus, Codex & Grok on Herdr to research, cross-verify, and deliver a sourced verdict. |
| [**stfl/herdr-bridge**](https://github.com/stfl/herdr-bridge) | Shows a remote herdr agent inside a local herdr pane, one sidebar, several machines. |
| [**T0mSIlver/hither**](https://github.com/T0mSIlver/hither) | Opens the active remote Herdr directory in Zed on macOS with a single key chord. |
| [**yansfil/herdr-remote-handoff**](https://github.com/yansfil/herdr-remote-handoff) | Transfers Claude Code sessions and workspaces between local and remote Herdr machines via a dedicated CLI. |
| [**PegasusWang/herdr-agent-prompt**](https://github.com/PegasusWang/herdr-agent-prompt) | Provides herdr-agent-prompt. |
| [**ndemeshchenko/herdr-peer-chat**](https://github.com/ndemeshchenko/herdr-peer-chat) | Provides Let Claude Code and Codex hold a conversation with each other in one herdr tab. |
| [**rytkmt/herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim) | Reviews AI agent file changes in Neovim diff mode before applying, enabling single-command approve or deny actions. |
| [**martebytes/herdr-mobile**](https://github.com/martebytes/herdr-mobile) | Provides a mobile-first web UI for Herdr: see your agents, attach to panes, chat with Claude Code and Codex from your phone. |
| [**daocoding/herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle) | Provides Hook-first Claude Code lifecycle for herdr + Omarchy: working/blocked/idle from Claude's own hooks, verify after every Claude Code update. |
| [**gal-leib/claude-vibe**](https://github.com/gal-leib/claude-vibe) | Provides a /vibe skill: a read-only Claude Code director that spawns, briefs and verifies persistent worker sessions in Herdr panes. |
| [**usrivastava92/herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev) | Detects Rovo Dev CLI sessions and reports them as live agents in Herdr. |
| [**Efeguclu1/herdr-usage**](https://github.com/Efeguclu1/herdr-usage) | Provides Compact account-usage marks on Herdr agent tabs for Claude, Codex, Cursor, OpenCode, and Pi. |
| [**skysilver1223/herdr-agent-harness**](https://github.com/skysilver1223/herdr-agent-harness) | Provides Agent/Skills-based Herdr harness for orchestrating Claude, Codex and AGY on Ubuntu/WSL. |
| [**ivanarama/PromptPilot**](https://github.com/ivanarama/PromptPilot) | Provides Background task queue for Claude Code and other AI CLIs, web UI + Telegram bot. |
| [**matheus3301/herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut) | Provides Shortcut task picker and coding-agent launcher for Herdr. |
| [**tdhuan/agent-notify**](https://github.com/tdhuan/agent-notify) | Provides Desktop notifications for coding agents, Claude Code first. Click a notification to raise kitty, open herdr's tab, and focus the exact agent pane. |
| [**aoprisan/hird**](https://github.com/aoprisan/hird) | Provides a cross-harness agent work queue and shared assertion memory backed by SQLite. |
| [**doggyfish/herdr-tuple-plugin**](https://github.com/doggyfish/herdr-tuple-plugin) | Provides a herdr plugin that pairs two coding agents side by side in one tab and moves text between them. |
| [**alexhooi/herdr-orchestrate**](https://github.com/alexhooi/herdr-orchestrate) | Runs Claude Code, Codex CLI and pi as visible, interruptible terminal-pane agent teams. One orchestrator, cross-model review, review-gated merges. |
| [**T0mSIlver/herdr-title-wrap**](https://github.com/T0mSIlver/herdr-title-wrap) | Provides wrap Claude Code session titles across multiple sidebar rows, auto-fitting the sidebar width. |
| [**ohitslaurence/outridr-server**](https://github.com/ohitslaurence/outridr-server) | Provides Ride flank on your coding agents, herdr tailnet server for the outridr app. |
| [**jclement/herdrer**](https://github.com/jclement/herdrer) | Provides a review inbox and a terminal for one developer box. Answer your agents from your phone. |
| [**jcarlos7121/herdr-sidekick-agents.nvim**](https://github.com/jcarlos7121/herdr-sidekick-agents.nvim) | Opens Claude Code, Codex, or Grok in side-by-side Herdr panes and forwards Neovim selection context. |
| [**nicoRomeroCuruchet/agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box) | Provides an isolated box where Claude Code drives local model agents. |
| [**jonesy827/mate**](https://github.com/jonesy827/mate) | Provides Phone-call voice supervisor for a herdr fleet of coding agents, code-enforced confirmation rail, LiveKit SIP, local STT/LLM/TTS. |
| [**QuiquiMatCom2004/herdr-py**](https://github.com/QuiquiMatCom2004/herdr-py) | Provides Unofficial Python client for Herdr's Socket API. |
| [**vgreg/herdr-padio**](https://github.com/vgreg/herdr-padio) | Switches PadIO controller modes automatically based on the app running in herdr's focused pane. |
| [**YannickHerrero/kelpie**](https://github.com/YannickHerrero/kelpie) | Provides a messaging-style PWA for Pi agents running inside Herdr. |
| [**shivammehta25/herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker) | Provides Vibecoded port of tmux-file-picker to herdr. |
| [**xyanwert/herdr-burnout**](https://github.com/xyanwert/herdr-burnout) | Monitors live Claude token usage and rate limits with animated visual cues in Herdr. |
| [**gecm0/herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage) | Shows provider usage (Claude, Codex, OpenCode Go, Neuralwatt) in a Herdr modal popup. |
| [**m-mohamed/sheprd**](https://github.com/m-mohamed/sheprd) | Keeps Pi, Codex, Claude Code, and OpenCode in one visible, isolated Herdr Flok. |
| [**peterferguson/herdr-herd-flow**](https://github.com/peterferguson/herdr-herd-flow) | Provides Route agent handoffs to coding harnesses (claude/codex/opencode) as named herdr tabs. |
| [**iagogfe/herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory) | Launches coding agents through ai-memory managed workstreams - cross-agent session continuity. |
| [**TsukumiStudio/MornKanban**](https://github.com/TsukumiStudio/MornKanban) | Provides Visible file-based Kanban dispatch for Claude Code and Codex agents. |
| [**steven-terrana/hermes-herdr-plugin**](https://github.com/steven-terrana/hermes-herdr-plugin) | Orchestrates Hermes agent sessions with Claude Code, Codex, and Pi under Herdr. |
| [**mohseenrm/zj-agent-mob**](https://github.com/mohseenrm/zj-agent-mob) | Monitors coding agent fleets with Herdr-inspired workflows and pane observation. |
| [**pisanvs/mc-cc**](https://github.com/pisanvs/mc-cc) | Provides Play Minecraft while your Claude Code agents work, a client-side Fabric 26.2 mod bridging herdr into Minecraft (notify on blocked/done, read history, reply in-game). |
| [**wadehuangdeveloper/pane-teams**](https://github.com/wadehuangdeveloper/pane-teams) | Provides Claude Code plugin: delegate independent, costly subtasks to teammate sessions running in real terminal panes (cmux or herdr), with git worktree isolation and leader-side patch reconciliation. |
| [**cheahhl814/herdr-skill-plus**](https://github.com/cheahhl814/herdr-skill-plus) | Provides herdr-skill+, workflow skill for coding agents: safe herdr delegation (pane-first launch, verified completion, provider/model preflight, task-tier matching). |
| [**krzysztoff1/herdr-cull**](https://github.com/krzysztoff1/herdr-cull) | Provides Review and close idle agent panes in herdr, fzf multi-select, nothing closes without confirmation. |
| [**Javamomma/herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall) | Provides tile the most-active subdirectories of a project as a live wall of read-only AI status cards. |
| [**lfsmoura/led-agent-status**](https://github.com/lfsmoura/led-agent-status) | Shows your AI agents' status on a BLE LED strip, blue working, blinking red blocked, green done. |
| [**inxx/herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review) | Spawns a four-pane pipeline in Herdr with Opus planning, Sonnet coding, and Claude plus Codex review. |
| [**edbienes/drovr**](https://github.com/edbienes/drovr) | Provides Multi-agent dev loop with a human-gated merge, drives coding agents through worktree isolation, a repo-declared gate, and two independent review lenses, inside herdr. |
| [**kowloonzh/agenthub**](https://github.com/kowloonzh/agenthub) | Broadcasts messages simultaneously to Codex and Claude Code sessions across Herdr panes via a single-binary TUI. |
| [**pedrogiroldo/agentbox**](https://github.com/pedrogiroldo/agentbox) | Provides Your personal coding-agent VM in a container: Ubuntu + Herdr + Claude Code/Codex/opencode + a mobile-friendly Neovim, over SSH. |
| [**agileandy/agent-multiplexer-skills**](https://github.com/agileandy/agent-multiplexer-skills) | Provides Agent skills for driving terminal multiplexers from inside them, herdr and native tmux control plus live-safe window managers. |
| [**OmarDadabhoy/herdr-agent-links**](https://github.com/OmarDadabhoy/herdr-agent-links) | Opens links hidden behind Markdown labels in Codex and Claude output inside Herdr. |
| [**wangfan1998-github/herdr-hybrid**](https://github.com/wangfan1998-github/herdr-hybrid) | Orchestrates Claude Code hybrid teams with high-tier models supervising parallel worker panes in Herdr. |
| [**wayne930242/straw-boss**](https://github.com/wayne930242/straw-boss) | Provides Task coordination for Codex CLI and Claude Code: carry bounded work directly or dispatch Herdr-backed sessions rooted in each app, from single-app repos to monorepos. |
| [**eduardoborges/herdr-claude-title-hook**](https://github.com/eduardoborges/herdr-claude-title-hook) | Provides Claude Code plugin that syncs the session title to the Herdr tab title. |
| [**vivainio/cop-pilot**](https://github.com/vivainio/cop-pilot) | Provides Delegate coding tasks to GitHub Copilot CLI agents via Herdr, and collect results asynchronously. |
| [**dipeshdulal/gothalo**](https://github.com/dipeshdulal/gothalo) | Provides a self-hosted mobile remote for Herdr, control your coding agents from your phone, over your own Tailscale network. |
| [**hmu332233/herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart) | Provides Restart agents in Herdr with one shortcut when their display breaks, and continue the same conversation. |
| [**SpatialNexus/herdr-subagent-state**](https://github.com/SpatialNexus/herdr-subagent-state) | Provides Community Herdr plugin that bridges native agent hooks to report tool and sub-agent activity as working state. |
| [**pedroallenrevez/herdr-comments.nvim**](https://github.com/pedroallenrevez/herdr-comments.nvim) | Provides a minimal herdr-reviewr-style commenting for herdr-context.nvim: select code, comment, send. |
| [**lutian/herdr-sdd-harness**](https://github.com/lutian/herdr-sdd-harness) | Provides a Spec-Driven Development harness using Herdr for orchestration. |
| [**kennethgeerts/herdr-architect**](https://github.com/kennethgeerts/herdr-architect) | Provides Claude Code skill: one architect session, Codex implements, Fable reviews, all in Herdr tabs. |
| [**overflowy/herdr-adversarial-review**](https://github.com/overflowy/herdr-adversarial-review) | Provides a Claude Code skill for adversarial code review that spawns an automated reviewer in a Herdr split pane. |
| [**tiamointer/herdr-title-distill**](https://github.com/tiamointer/herdr-title-distill) | Updates Herdr tab titles automatically based on concise summaries of completed agent tasks. |
| [**rrojo02/herdr-bridge**](https://github.com/rrojo02/herdr-bridge) | Connects external coding agents to Herdr through its local socket API. |
| [**thejiajun/herdr-autoname**](https://github.com/thejiajun/herdr-autoname) | Provides Automatically name Herdr workspaces, tabs, and panes from recent agent sessions. |
| [**SimonMallas/agent-letterbox-herdr**](https://github.com/SimonMallas/agent-letterbox-herdr) | Provides Agent-to-agent mail for multi-agent AI coding teams in Herdr, durable letters for coordination and team memory. Teach Claude Code, Codex, Gemini CLI or other terminal agents to use it. |
| [**asermax/herdr-subagents**](https://github.com/asermax/herdr-subagents) | Manages subagents as herdr tabs. |
| [**exviolet/sendoff**](https://github.com/exviolet/sendoff) | Provides Linux-native Tauri shell for Sendoff with tmux, Herdr, and Orca integration. |
| [**testy-cool/herdr-copy-conversation**](https://github.com/testy-cool/herdr-copy-conversation) | Copies full terminal scrollback or agent conversations directly to the clipboard in Herdr. |
| [**fabzter/herdrbridge**](https://github.com/fabzter/herdrbridge) | Provides Stdlib-only Python library for driving coding agents through herdr (shared by the Claude Code <-> Hermes Agent bridges). |
| [**leescot/herdr-remote-ios**](https://github.com/leescot/herdr-remote-ios) | Enables remote control of Mac-hosted Herdr coding agents from iOS devices over SSH. |
| [**regrow1123/herdr-pi-delegation**](https://github.com/regrow1123/herdr-pi-delegation) | Provides a Hermes to Pi delegation workflow across Herdr panes with event-based completion. |
| [**wbarakat/omarchy-session-restore**](https://github.com/wbarakat/omarchy-session-restore) | Provides Session save & restore for Omarchy, dual-boot friendly workspace persistence with optional herdr agent resume. |
| [**connerohnesorge/herdr-vaultr**](https://github.com/connerohnesorge/herdr-vaultr) | Provides Official herdr plugin for vaultr, copy, show, fork, and search captured agent sessions from the pane they ran in. |
| [**qinglang8609/deepseek_herdr**](https://github.com/qinglang8609/deepseek_herdr) | Orchestrates multi-agent teams across Claude, OpenCode, and Codex in Herdr using DeepSeek Harness and shared task boards. |
| [**igor/crew-skill**](https://github.com/igor/crew-skill) | Coordinates a fleet of AI agents in Herdr where premium models lead and local models handle volume execution. |
| [**muscaiu/resume-globally**](https://github.com/muscaiu/resume-globally) | Browses and resume recent sessions across Claude Code, Cursor, and OpenCode. |
| [**vladzima/herd**](https://github.com/vladzima/herd) | Provides Multi-agent coordinator for herdr: a head Claude Code agent that delegates tasks to worker agents (claude, codex, gemini, .) in their own tabs. |
| [**izumi0uu/terminal-theme-suite**](https://github.com/izumi0uu/terminal-theme-suite) | Switches iTerm2, OMP, Herdr, and terminal wallpapers as one coordinated theme suite. |
| [**theaileverage/marionette**](https://github.com/theaileverage/marionette) | Provides Persistent outcome-driven orchestration for Codex, Claude Code, and AGY agents in Herdr. |
| [**Crush53/pi-herdr-managed-agents**](https://github.com/Crush53/pi-herdr-managed-agents) | Manages native Pi, Claude Code, and Codex agents in auditable Herdr tabs. |
| [**douglasjarquin/sf2-themes**](https://github.com/douglasjarquin/sf2-themes) | Provides Street Fighter II color themes for WezTerm and Herdr. |
| [**giannisp09/herdr-tailscale-setup**](https://github.com/giannisp09/herdr-tailscale-setup) | Provides Bootstrap script + helpers to turn a fresh Linux VM into an always-on box for running Claude Code agents over Tailscale + herdr. |
| [**lightheaded/kari**](https://github.com/lightheaded/kari) | Provides a kanban board for Claude Code sessions with quota-aware scheduling. macOS tray app. |
| [**phine-apps/herdr-collie**](https://github.com/phine-apps/herdr-collie) | Bridges VS Code and Herdr to orchestrate AI agents, Git worktrees, and context sharing directly from the editor. |
| [**tonoid/agent-loop**](https://github.com/tonoid/agent-loop) | Schedules autonomous coding agents across provider accounts and runs them as herdr agents in herdr panes. |
| [**CydoEntis/chameleon**](https://github.com/CydoEntis/chameleon) | Provides One command retints your whole terminal - Windows Terminal, Oh My Posh and Herdr - from a single palette. |
| [**nytafar/obsidian-herdr**](https://github.com/nytafar/obsidian-herdr) | Provides Herdr agents and terminals inside Obsidian. |
| [**gnepud/herdr-sbx-box**](https://github.com/gnepud/herdr-sbx-box) | Provides a modular Docker Sandbox (sbx) multi-agent workspace managed by Herdr. |
| [**JasonBates/agentdeck**](https://github.com/JasonBates/agentdeck) | Provides Glanceable dashboard for Herdr coding-agent sessions, served from a Mac to any device on your tailnet. |
| [**maimuzo/continuo**](https://github.com/maimuzo/continuo) | Provides orchestration system. continuo = OpenAI symphony + claude code + herdr + Github Project v2. |
| [**nakamori-naoya/agent-fleet-plugins**](https://github.com/nakamori-naoya/agent-fleet-plugins) | Controls multi-agent roles, task routing, and Herdr execution using declarative fleet specifications. |
| [**mgibson0708/pstack-portable**](https://github.com/mgibson0708/pstack-portable) | Provides Portable pstack engineering skills for Codex, Claude Code, Grok Build, and Cursor, with Herdr multi-agent coordination. |
| [**aliceisjustplaying/swarmchat**](https://github.com/aliceisjustplaying/swarmchat) | Provides Equal-peer chat for Claude Code and Codex in Herdr, with a shared conversation log. |
| [**AdamGarceau/herdr-autoname**](https://github.com/AdamGarceau/herdr-autoname) | Provides a Claude Code UserPromptSubmit hook that auto-names your herdr pane from the session's live topic using local Ollama, and renames it when the topic changes. Adds zero prompt latency. |
| [**mshubitidze/pstack-herdr**](https://github.com/mshubitidze/pstack-herdr) | Provides a port of Poteto's pstack for Herdr, Pi, and Claude Code. |
| [**fabzter/hermes-bridge**](https://github.com/fabzter/hermes-bridge) | Provides Claude Code plugin: drive a local Hermes Agent through herdr (agent-to-agent chat, approvals, crash-resume). |
| [**adityamaanas/glance**](https://github.com/adityamaanas/glance) | Provides a live orientation panel for an agent session that integrates with herdr as a split pane. |
| [**WSeubring/omarchy-agent-sessions**](https://github.com/WSeubring/omarchy-agent-sessions) | Provides a live coding-agent sessions (Claude Code, pi, anything herdr hosts) in the Omarchy bar: blocked, working, done or idle, with directory and title. |
| [**tenmomo/fleet-commander**](https://github.com/tenmomo/fleet-commander) | Provides Field-tested fleet command discipline for coding agents, tmux, herdr, and remote seats. Every rule carries the date it was forged from a real incident. |
| [**jeremylongshore/omarchy-crew-chief-entry**](https://github.com/jeremylongshore/omarchy-crew-chief-entry) | Provides Crew Chief turns Claude Code, Codex, Herdr, and other command-capable agent sessions into a local attention queue. See working, blocked, and done; put NEEDS YOU first; dismiss stale rows; and focus the project window. |
| [**MarceloEmilioRiveraC/pitwall**](https://github.com/MarceloEmilioRiveraC/pitwall) | Provides Portable Windows control room for AI coding agents. One folder, no install, no admin: an agent sidebar, your agent, and a git-aware file viewer with live diffs and an in-pane editor. |
| [**ryanthedev/herderp**](https://github.com/ryanthedev/herderp) | Provides Claude Code plugin: MCP tools for the herdr CLI + session necromancy (revive a previous Claude Code agent session from a herdr space). |
| [**ericed11/coding-agents-on-a-vps**](https://github.com/ericed11/coding-agents-on-a-vps) | Moves your Claude Code and Codex work off your laptop onto a private always-on VPS: Tailscale-only access, no public SSH, and four ways in (Herdr, VS Code Remote SSH, Codex desktop, iOS). |
| [**narrowstacks/pxe-agent-box**](https://github.com/narrowstacks/pxe-agent-box) | Provides One-command disposable Proxmox dev boxes for agent workflows (bun, agent CLIs, Chrome, herdr/moshi). |
| [**wynemo/herdr-agent-topic**](https://github.com/wynemo/herdr-agent-topic) | Shows your latest user prompt in each agent card. |
| [**etinpres/herdr-telegram-remote**](https://github.com/etinpres/herdr-telegram-remote) | Controls Codex and Claude Code panes in Herdr from Telegram. |
| [**bertverbessem/herdr-last-tab**](https://github.com/bertverbessem/herdr-last-tab) | Provides toggle between the current and previously focused tab (per workspace). |
| [**carlory/herdr-worktree**](https://github.com/carlory/herdr-worktree) | Provides Enhance Herdr worktrees with lifecycle capabilities missing from core Herdr. |
| [**mbillz/shep**](https://github.com/mbillz/shep) | Auto-launches principal-engineer PR reviews in herdr when you're tagged as a reviewer. |
| [**parkbeomsub/herdr_orch**](https://github.com/parkbeomsub/herdr_orch) | Launches AI agent teams in Herdr with team presets, inter-pane messaging, and worktree isolation. |
| [**rytkmt/herdr-send.nvim**](https://github.com/rytkmt/herdr-send.nvim) | Sends file references and prompts from Neovim to AI agents in the active Herdr workspace. |
| [**ankitvashisht12/crew**](https://github.com/ankitvashisht12/crew) | Provides Role-based multi-agent orchestration for Herdr with durable task state, parallel worktrees, and cross-vendor review. |
| [**talberthoule/herdr-shepherd**](https://github.com/talberthoule/herdr-shepherd) | Provides Audited coordination and safe handoffs for Codex and Claude Code sessions running through Herdr. |
| [**hunaish-dev/nakama**](https://github.com/hunaish-dev/nakama) | Provides a wrapper, not a harness: coordinates a crew of coding-agent CLIs (starting with Claude Code) on one goal, with live attach via herdr. |
| [**quangdang46/herdctl**](https://github.com/quangdang46/herdctl) | Provides Named multi-agent control plane on Herdr (NTM-style orchestration, Herdr backend instead of tmux). |
| [**jrx2-dev/herdr-sub-agents**](https://github.com/jrx2-dev/herdr-sub-agents) | Provides Herdr subagents extension for pi. |
| [**kil9/claude-auto-retry-herdr**](https://github.com/kil9/claude-auto-retry-herdr) | Retries Claude Code sessions automatically upon rate limits using native Herdr socket APIs. |
| [**Fectivnfy112357/claude-code-bridge**](https://github.com/Fectivnfy112357/claude-code-bridge) | Bridges Hermes Agent and Claude Code CLI in print mode and interactive Herdr sessions. |
| [**thelad-dev/orchaester**](https://github.com/thelad-dev/orchaester) | Provides Orchaester, a Herdr-first conductor distribution treating Grok Build and Cursor as equal principals. |
| [**jsutter909/corral**](https://github.com/jsutter909/corral) | Provides Isolated AI-agent workspaces on top of herdr, one worktree, one workspace, one agent. |
| [**kanwhile/herdr-skill**](https://github.com/kanwhile/herdr-skill) | Provides Claude Code skill for driving herdr terminal panes and sibling agents, verified against the binary, not its docs. |
| [**hiroshi57/corral**](https://github.com/hiroshi57/corral) | Commands multiple Claude Code and Codex agents from a unified web orchestrator with worktree isolation and diff reviews. |
| [**YF-Tobehero/Herdr-palette-probe-for-windows**](https://github.com/YF-Tobehero/Herdr-palette-probe-for-windows) | Provides Measure the colours your coding agents bake into their binaries, then pick a Windows Terminal palette that absorbs them instead of fighting them. |
| [**Tatendaz/mission-control**](https://github.com/Tatendaz/mission-control) | Provides a self-updating project radar for solo devs: swept from git, PRs, Claude session logs and a watch-dictated idea inbox; launches agents into herdr straight from the board. |
| [**testy-cool/herdr-agent-control**](https://github.com/testy-cool/herdr-agent-control) | Provides Deterministic multi-agent orchestration, process leases, and drift prevention for Herdr. |
| [**nathanestone-alt/herdr-workstation-bootstrap**](https://github.com/nathanestone-alt/herdr-workstation-bootstrap) | Provides Reproducible Windows 11, WSL2, Herdr, Codex, Claude, Excel COM, and remote-access bootstrap for the MS-A2 workstation. |
| [**klahrich/smashhh**](https://github.com/klahrich/smashhh) | Provides Multi-agent orchestrator: planner/coder/verifier coding agents in a Herdr workspace. |
| [**sblevins/claude-rename-tab**](https://github.com/sblevins/claude-rename-tab) | Provides Claude Code skill: rename the herdr tab an agent runs in to a short (<=3 word) label based on its current task. |
| [**kazuochi/opxy-deck**](https://github.com/kazuochi/opxy-deck) | Provides Turn a Teenage Engineering OP-XY into a physical control deck for AI coding agents (Claude Code, Codex, herdr), dictation PTT, model/effort knobs, per-agent routing, JSON profiles with hot-reload. |
| [**manikbajaj/herdr-configuration**](https://github.com/manikbajaj/herdr-configuration) | Provides a script installation for replicating Herdr settings across multiple computers. |
| [**navanchauhan/attractor**](https://github.com/navanchauhan/attractor) | Provides Sequential Codex + Claude Code megaplan-and-execute over the herdr API. |
| [**patraianton/teammate**](https://github.com/patraianton/teammate) | Provides one coding agent hires another, a worker Claude Code session in its own herdr tab, with a written brief, a one-line status contract, and a close that refuses to destroy unfinished work. |
| [**y-hirakaw/herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify) | Provides macos notifications for Claude Code, shows the agent's real last message, not just "done". |
| [**aboufama/claude-agents-tmux**](https://github.com/aboufama/claude-agents-tmux) | Provides Tmux and herdr mission control for running many AI coding agents in one session. |
| [**maoxiaoke/tmux-agents**](https://github.com/maoxiaoke/tmux-agents) | Displays live agent states in tmux status bars with hotkey jumping for Claude Code sessions. |
| [**djbclark/claude-orchestration-skills**](https://github.com/djbclark/claude-orchestration-skills) | Provides Claude Code skills for orchestrating multi-agent work via Herdr and Ralph TUI + Beads. |
| [**burningportra/vibing-with-herdr**](https://github.com/burningportra/vibing-with-herdr) | Provides Same-branch Herdr swarm skill: drain beads with exclusive Agent Mail reservations, no worktrees. |
| [**ykawase1011/hanchou**](https://github.com/ykawase1011/hanchou) | Provides a durable multi-agent control plane built on Herdr, Beads, Codex, and Claude Code. |
| [**GoldenBerry-SO/devbox**](https://github.com/GoldenBerry-SO/devbox) | Provides One-command Hetzner dev box via Ansible. Your laptop can sleep, your agents don't. |
| [**mev15/claude-config**](https://github.com/mev15/claude-config) | Provides Claude Code skill: external Codex CLI review gate with a priority-based fix loop. Interactive herdr pane mode + headless codex exec mode. |
| [**tdragon/swiftbar-claude**](https://github.com/tdragon/swiftbar-claude) | Provides Menu-bar monitor for Claude/Codex agent sessions in WezTerm, status, notifications, and click/hotkey jump. herdr-style, no hooks. |
| [**XiangQhello/codex-claude-auto-enter**](https://github.com/XiangQhello/codex-claude-auto-enter) | Provides Herdr-aware auto Enter for Codex and Claude Code: target exact panes and stop when the agent goes idle. |
| [**Zamua/openloc.nvim**](https://github.com/Zamua/openloc.nvim) | Opens file references in the Neovim that already belongs to the workspace. |
| [**ardubev16/tmux-herdr**](https://github.com/ardubev16/tmux-herdr) | Provides a Tmux plugin that uses Herdr to manage, aggregate and orchestrate AI Agents. |
| [**VicenteOlmos/opencode-herdr**](https://github.com/VicenteOlmos/opencode-herdr) | Provides OpenCode plugin: route agents through Herdr as herdr/<adapter>/<model>. |
| [**jedarden/agentists-quickstart**](https://github.com/jedarden/agentists-quickstart) | Provides Bootstrap a bare VPS into a Claude Code + herdr coding environment. |
| [**joyehuang/memory-dashboard**](https://github.com/joyehuang/memory-dashboard) | Displays agent memory usage and token consumption dashboards for Pi agents in Herdr with daily updates. |
| [**Mor-dev/herdr-agent-monitor**](https://github.com/Mor-dev/herdr-agent-monitor) | Provides DankMaterialShell bar widget showing live herdr agent status. |
| [**sefuzhou770801-hub/herdr-dispatch-skill**](https://github.com/sefuzhou770801-hub/herdr-dispatch-skill) | Dispatches tasks to agent workbenches across Herdr panes. |
| [**daocoding/omarchy-claude-agent**](https://github.com/daocoding/omarchy-claude-agent) | Provides Omarchy bar widget: live Claude Code state (working / blocked / idle) from Claude's own hooks via herdr-claude-lifecycle. |
| [**mitchnick/ai-dev-environment**](https://github.com/mitchnick/ai-dev-environment) | Provides Sanitized Claude Code, Pi, Herdr, and Ghostty configuration. |
| [**suleymanozkeskin/sheppard**](https://github.com/suleymanozkeskin/sheppard) | Controls plane with collab & communication tools for agents from multiple harnesses, built on herdr api. |
| [**alexisweeren-tribe/herdr-spaces**](https://github.com/alexisweeren-tribe/herdr-spaces) | Provides Auto-name Herdr workspaces from Claude Code agent context. |
| [**KennethJefferson/HerdrPlus**](https://github.com/KennethJefferson/HerdrPlus) | Provides Rust-based terminal workspace manager for AI coding agents - a Windows-first extension of herdr. |
| [**ooiyeefei/pixtension**](https://github.com/ooiyeefei/pixtension) | Provides pichestrator: parallel-work orchestrator for pi, guarded sub-agents in git worktrees + herdr, with a fail-closed prod-data/credential/rm bash guard. |

### Claude Code: Account switchers and auth monitors

*3 projects. Tools for managing Claude multi-account rotation, OAuth keys, and quota monitoring.*

| Project | What it does |
|---|---|
| [**quaywin/agys**](https://github.com/quaywin/agys) | Provides multi-profile isolation and real-time quota tracking for Antigravity CLI in Herdr using sandboxed workspaces. |
| [**wazum/herdr-grazr**](https://github.com/wazum/herdr-grazr) | Provides a simple and reliable auto account switcher for Claude Code: rotates to a fresh account before the 5-hour or weekly rate limit hits, so no pane ever stops at the usage quota. A Herdr plugin. |
| [**anyaachan/herdr-claude-usage**](https://github.com/anyaachan/herdr-claude-usage) | Provides Global Claude Code plan usage in Herdr: tab-bar summary + popup dashboard. statusLine-powered, multi-account aware. |

### Pi supervisor workflows and extensions

*133 projects. Supervision harnesses, task planners, and extensions for Pi agents in Herdr.*

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
| [**osolmaz/pi-workflows**](https://github.com/osolmaz/pi-workflows) | Provides a workflow engine, JSON control-flow system, and live terminal viewer for the Pi coding agent in Herdr. |
| [**IvoryHeart/herdr-world**](https://github.com/IvoryHeart/herdr-world) | Provides Herdr World, a multi-surface web experience for Herdr. |
| [**qintmb/herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker) | Provides Theme picker for herdr UI based terminalcolors scheme and your customization. |
| [**tobi/pi-herdr-workers**](https://github.com/tobi/pi-herdr-workers) | Provides Pi + Herdr: /team worker panes, /loop re-wakes, and MonitorCreate/List/Stop. |
| [**sagmans/herdr-pickers**](https://github.com/sagmans/herdr-pickers) | Provides Several custom, pop-up pickers for agents, worktrees, workspaces and projects. |
| [**Efeguclu1/herdr-town**](https://github.com/Efeguclu1/herdr-town) | Watches your Herdr coding agents as an 8-bit town. Read and answer them without leaving it. |
| [**Only-Moon/herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows) | Provides a Windows port of herdr-yazi with native Windows pane spawning support via Herdr v0.8+. |
| [**plotarmordev/tendwire**](https://github.com/plotarmordev/tendwire) | Provides Local API for Herdr: connect coding agents to apps, automations, and any local system. |
| [**July24/pier**](https://github.com/July24/pier) | Provides Pi is the coding-agent carrier; Herdr is a terminal workspace manager. pier adds the two capabilities pi deliberately leaves out, a todo list loop and interactive subagents and gives them the herdr pane/tab layer as their visual and interactive substrate. |
| [**hasuwini77/herdr-spinner**](https://github.com/hasuwini77/herdr-spinner) | Provides Animated braille spinner for Herdr panes in the working state, via display-only pane metadata. |
| [**float-ritual-stack/pi-herdr-outliner**](https://github.com/float-ritual-stack/pi-herdr-outliner) | Provides Local-first Roam-style outliner integrated with Pi and Herdr. |
| [**ubuntudroid/herdr-coder-sessions**](https://github.com/ubuntudroid/herdr-coder-sessions) | Browses running Coder agent sessions in herdr and open each as its own workspace: agentty on the session, its changes mirrored into a local worktree for review. |
| [**sting8k/pi-peer**](https://github.com/sting8k/pi-peer) | Provides Standalone peer-to-peer Pi communication over a Herdr workspace. |
| [**getpipher/cursor**](https://github.com/getpipher/cursor) | Provides a focus-aware, customizable editor cursor for Pi coding agents running across Ghostty, tmux, and Herdr. |
| [**snaka/kelpie**](https://github.com/snaka/kelpie) | Provides Menu bar app showing live herdr agent status. |
| [**dcadenas/kelpie**](https://github.com/dcadenas/kelpie) | Provides Durable inter-agent coordination layer for Herdr-managed agents. |
| [**worldnine/ashiato**](https://github.com/worldnine/ashiato) | Provides See what your agent just touched, a TUI file picker sorted by mtime, with time clusters and syntax-highlighted preview. |
| [**BjoernSchotte/herdr-worktree-picker**](https://github.com/BjoernSchotte/herdr-worktree-picker) | Provides Fuzzy Git worktree picker for Herdr, type the branch name instead of worktree-rapid-river-6486. Opens as a grouped workspace or as a split pane. |
| [**alessandrofogli/pi-fleet**](https://github.com/alessandrofogli/pi-fleet) | Provides Visible herdr-tab sub-agents for pi-coding-agent, delegation with isolated worktrees and captain-only wake. |
| [**RizRiyz/pixtui**](https://github.com/RizRiyz/pixtui) | Provides Pixel Art Editor on Terminal. |
| [**sfroment/pi-herdr**](https://github.com/sfroment/pi-herdr) | Provides Pi extension for the Herdr CLI, control workspaces, tabs, panes, and coding agents via a typed tool (direct CLI, requires HERDRENV=1). |
| [**princejoogie/herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker) | Opens Git repositories as Herdr workspaces from an OpenTUI picker. |
| [**giacolees/plan-herdr-subagents**](https://github.com/giacolees/plan-herdr-subagents) | Provides a unified Pi workflow package combining grilling, pointer plans, sequential workers, and reviewers on Herdr subagents. |
| [**mcuste/pi-herdr-worktree**](https://github.com/mcuste/pi-herdr-worktree) | Provides Herdr worktree workspaces as one tool for Pi and Oh My Pi agents. |
| [**L1aoXingyu/pi-herdr-multi-agent**](https://github.com/L1aoXingyu/pi-herdr-multi-agent) | Provides Multi-model interactive Pi TUI fleets via Herdr (launch, watchdog harvest, auto-close). |
| [**Jalzn/pi-herdr-agents**](https://github.com/Jalzn/pi-herdr-agents) | Provides Bounded agent orchestration for Pi running in Herdr. |
| [**oldflag2333333/pi-facets**](https://github.com/oldflag2333333/pi-facets) | Provides reusable Pi capability profiles with context-isolated subagent delegation and Herdr integration. |
| [**gitUmaru/pi-session-agents**](https://github.com/gitUmaru/pi-session-agents) | Provides Pi extension: every subagent is a genuine independent Pi session (visible Herdr tab or headless background Pi). |
| [**blisk92/pi-herdr-orchestrator**](https://github.com/blisk92/pi-herdr-orchestrator) | Orchestrates Pi sub-agents as Pi processes running in Herdr panes. Sibling to pi-herdr-agents with deliberate differences. |
| [**itayo-m/herdr-tab-session-name-sync**](https://github.com/itayo-m/herdr-tab-session-name-sync) | Syncs agent session name with herdr tabs and panes title. |
| [**geniusgordon/pi-herdr-crew**](https://github.com/geniusgordon/pi-herdr-crew) | Dispatches and manage pi subagents as a Herdr crew. Each member answers through a markdown file, not the terminal. |
| [**MrBenJ/pi-herdr**](https://github.com/MrBenJ/pi-herdr) | Provides Standalone pi tools for controlling the hosting Herdr session. |
| [**CarrisHarter/herdr-omp-attach-panes**](https://github.com/CarrisHarter/herdr-omp-attach-panes) | Provides Interactive Herdr panes for omp (Oh My Pi) Vibe workers. |
| [**Pfgoriaux/pi-dispatch**](https://github.com/Pfgoriaux/pi-dispatch) | Provides Parallel sub-agent fan-out for the pi coding agent, hermetic workers, model rosters, git-worktree write tier with merge-back, Herdr arborescence. |
| [**WyvernMonarch/herdr-cockpit**](https://github.com/WyvernMonarch/herdr-cockpit) | Provides a local-first supervision and control layer for Herdr coding agents. |
| [**duskoide/pi-herdr-worker**](https://github.com/duskoide/pi-herdr-worker) | Provides Spawn pi agents in isolated Herdr panes for parallel task execution. |
| [**aaaxn/pi-herdr-live-agents**](https://github.com/aaaxn/pi-herdr-live-agents) | Provides Visible Pi (sub)agents that run as real, live Pi sessions in Herdr panes. |
| [**itc-steve/pi-herdr**](https://github.com/itc-steve/pi-herdr) | Provides Pi extension for Herdr-visible subagent herds - default-local workers, optional ranked-frontier think, markdown handoff. |
| [**gbozee/pi-pstack**](https://github.com/gbozee/pi-pstack) | Provides a native Pi port of poteto/pstack with multi-model routing, pi-subagents, Herdr, and Intercom integration. |
| [**YunosukeYoshino/pi-herdr**](https://github.com/YunosukeYoshino/pi-herdr) | Provides Spawn role-based Pi subagents in Herdr panes. |
| [**anrunt/herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader) | Provides Reload or restart idle Pi agent sessions from a Herdr overlay TUI. |
| [**bkarpinos/herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith) | Provides keybinding command palette for herdr. |
| [**dulvac/pi-team-panes**](https://github.com/dulvac/pi-team-panes) | Provides Split-pane workers for pi-agent-teams: herdr panes inside herdr, iTerm2 panes via it2 otherwise. |
| [**matifuentes2/pi-parallel-go-pr-herdr**](https://github.com/matifuentes2/pi-parallel-go-pr-herdr) | Runs parallel worktree-backed Pi PR agents in background Herdr tabs. |
| [**tigorlazuardi/pi-herdr-sudo-task**](https://github.com/tigorlazuardi/pi-herdr-sudo-task) | Provides Blocking, two-consent sudo tasks in dedicated Herdr panes for Pi. |
| [**abrose/herdr-url-picker**](https://github.com/abrose/herdr-url-picker) | Picks a URL printed in the current pane with fzf and open it in the default browser. |
| [**TinyWhite1997/herdr-flash-picker**](https://github.com/TinyWhite1997/herdr-flash-picker) | Provides Fast pane picker for Herdr with aligned one- or two-letter jump labels. |
| [**MikkelKappelPersson/pi-shepherd**](https://github.com/MikkelKappelPersson/pi-shepherd) | Controls agents and subagents in herdr. |
| [**Gabriel-Cervo/Pi-Herdr-Subagents**](https://github.com/Gabriel-Cervo/Pi-Herdr-Subagents) | Provides a native in-process subagents for Pi with configurable models and smart result joining. |
| [**bkarpinos/herdr-picker**](https://github.com/bkarpinos/herdr-picker) | Provides a fast popup picker for searching and previewing workspaces, agents, and tabs in herdr. |
| [**CristianPeralta/herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar) | Provides remaining credit for pay-as-you-go API providers, starting with Alibaba Cloud Model Studio. |
| [**dmytr0x/herdr-task-picker**](https://github.com/dmytr0x/herdr-task-picker) | Provides a Herdr plugin that fuzzy-searches and runs built-in or custom go-task commands in the focused workspace. |
| [**getkimchi/herdr-kimchi**](https://github.com/getkimchi/herdr-kimchi) | Provides Herdr lifecycle bridge for Kimchi. |
| [**didy-kpn/pi-herdr-taskforce**](https://github.com/didy-kpn/pi-herdr-taskforce) | Provides Async multi-agent taskforce for pi + Herdr (sqlite message box + pi extension + skill). |
| [**nourhelmi/pi-meta-harness**](https://github.com/nourhelmi/pi-meta-harness) | Provides Portable, reproducible Pi advisor and Herdr setup. |
| [**abhishek944/pi-herdr-skills**](https://github.com/abhishek944/pi-herdr-skills) | Provides reusable global Pi skills for Herdr-backed planning, implementation, and review. |
| [**Liquescent-Development/herdr-a2a**](https://github.com/Liquescent-Development/herdr-a2a) | Provides A2A communication for Herdr. |
| [**kevinpita/herdr-nix**](https://github.com/kevinpita/herdr-nix) | Provides Nix flake for herdr. Updated hourly. |
| [**martian4202/pi-session-name**](https://github.com/martian4202/pi-session-name) | Provides Pi extension: LLM-generated session names from recent user messages, with optional Herdr tab sync. |
| [**hao1939/herdr-supervisor**](https://github.com/hao1939/herdr-supervisor) | Provides One Pi agent that supervises existing Herdr workers against explicit goals, without adding a second task system. |
| [**yanekyuk/pi-plain-herdr**](https://github.com/yanekyuk/pi-plain-herdr) | Provides Visible, worktree-isolated Herdr implementation workflow for Pi. |
| [**bpcakes/epicd**](https://github.com/bpcakes/epicd) | Provides Durable Codex orchestration for dependency-safe Beads epics with independent review, exact-commit verification, and resumable SDK or Herdr sessions. |
| [**chouxcreams/herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker) | Picks a URL from the focused pane and open it in your browser. |
| [**fyc0451/agent-cockpit**](https://github.com/fyc0451/agent-cockpit) | Provides a web cockpit for CLI coding agents running under Herdr, featuring kanban boards, live terminals, and an inbox. |
| [**artmsilva/agent-tools**](https://github.com/artmsilva/agent-tools) | Provides open-source tools for AI-agent workflows: Pi extensions and Herdr plugins. |
| [**boadij/pi-herdsman**](https://github.com/boadij/pi-herdsman) | Provides asynchronous Pi subagents with nested delegation, parallel multi-agent orchestration, and supervision in herdr. |
| [**ronnie3786/herdr-companion**](https://github.com/ronnie3786/herdr-companion) | Provides a native Mac and iPhone apps with a standalone companion server for Herdr. |
| [**kazda01/pi-tab-status**](https://github.com/kazda01/pi-tab-status) | Provides a live Pi status and short AI-generated descriptions for terminal tabs, sessions, tmux, herdr, and zellij. |
| [**w784415/pi-agent-usage**](https://github.com/w784415/pi-agent-usage) | Provides Pi extension that displays OpenAI Codex quota and reset times, with Herdr plugin support. |
| [**briankeefe/herdr-omp**](https://github.com/briankeefe/herdr-omp) | Provides herdr + Oh My Pi: fixes the false-idle agent state and auto-names workspaces after the task. |
| [**nourhelmi/pi-rich-output**](https://github.com/nourhelmi/pi-rich-output) | Provides Inline images and clickable full-size image links for Pi in Ghostty and Herdr. |
| [**pistelak/Paddock**](https://github.com/pistelak/Paddock) | Provides a paddock for your herdr sessions: a lean native macOS window around herdr, one Ghostty tab per session. |
| [**ali-abassi/boss**](https://github.com/ali-abassi/boss) | Manages coding agents across repositories from one Pi conversation, with persistent workers, delivery checks, and an inbox for owner decisions. A star is appreciated!. |
| [**screenagers-io/bullpen**](https://github.com/screenagers-io/bullpen) | Provides Bullpen: a 3D voxel office that shows what the coding agents inside Herdr are doing. |
| [**tfolkman/pi-herdr-workspace-namer**](https://github.com/tfolkman/pi-herdr-workspace-namer) | Provides Automatically name Herdr workspaces from native Pi session task titles. |
| [**pxdl/omp-herdr-auto-name**](https://github.com/pxdl/omp-herdr-auto-name) | Provides OMP extension that publishes native session titles to Herdr. |
| [**chrishiguto/pi-herdr-subagents**](https://github.com/chrishiguto/pi-herdr-subagents) | Launches Pi subagents in dedicated Herdr panes for delegated tasks. |
| [**v3rse/pi-agent-swarm**](https://github.com/v3rse/pi-agent-swarm) | Provides Async subagents for pi across herdr/tmux/zellij/wezterm. Herdr-first port of HazAT/pi-interactive-subagents. |
| [**andrewfung729/pi-herdr-subagents**](https://github.com/andrewfung729/pi-herdr-subagents) | Provides Async subagents for pi, running in herdr panes, spawn, orchestrate, and steer results back without blocking the main session. |
| [**DeharengOlivier/herdr-cockpit**](https://github.com/DeharengOlivier/herdr-cockpit) | Provides a WezTerm configuration that turns your terminal into a dedicated cockpit for AI coding agents, driven by Herdr. |
| [**houz42/omarchy-keyboard-remapper**](https://github.com/houz42/omarchy-keyboard-remapper) | Provides Omarchy shell plugin: tap the physical Alt key alone to emit F13 (for herdr/tmux-style prefixes), while holding Alt still works normally. |
| [**itisbryan/pi-blanche**](https://github.com/itisbryan/pi-blanche) | Provides Spin up a crew of pi sessions (planner, worker, qa, verifier, advisor) in herdr panes, coordinating over pi-intercom. |
| [**markpinero/pi-suggested-tasks**](https://github.com/markpinero/pi-suggested-tasks) | Provides Suggested task cards for the Pi coding agent, the model offers independent side work; accept spawns a sibling session (Herdr panes/worktrees, or parked sessions). |
| [**ryuzdev/pi-opener**](https://github.com/ryuzdev/pi-opener) | Provides the Pi extension that opens files in your real editor. |
| [**yajiefeng/pi-ticket-dispatcher**](https://github.com/yajiefeng/pi-ticket-dispatcher) | Provides Pi package: dispatch approved to-tickets to Herdr-managed Pi workers (implement, review, integrate, recover). |
| [**piotrekd00/pi-master-orchestrator**](https://github.com/piotrekd00/pi-master-orchestrator) | Provides Drive one implementation ticket through a visible worker+reviewer pair in herdr. |
| [**zbsdsb/herdr-codex-pi-workflow**](https://github.com/zbsdsb/herdr-codex-pi-workflow) | Provides Evidence-driven stateful workflow and post-delivery triage Skills for Pi and coding agents. |
| [**minqiyang/herdr-pi-coordinator**](https://github.com/minqiyang/herdr-pi-coordinator) | Provides Herdr + Pi coordinator standard: core, runtime, and routing table (v6.2-draft). |
| [**DanDo385/cockpit**](https://github.com/DanDo385/cockpit) | Provides CLI-first Herdr and Hermes Kanban operating desk for legible multi-agent delegation. |
| [**lfsmoura/pi-interactive-subagents-herdr**](https://github.com/lfsmoura/pi-interactive-subagents-herdr) | Provides Interactive OMP subagents running in Herdr-managed panes. |
| [**akmarwah03/pi-herdr-config**](https://github.com/akmarwah03/pi-herdr-config) | Provides Portable pi coding-agent + Herdr config bootstrap. |
| [**86label/minimalist-pi-orchestrator**](https://github.com/86label/minimalist-pi-orchestrator) | Provides Minimalist Linux orchestration for visible Pi sessions in Herdr tabs and isolated Treehouse worktrees. |
| [**maxedapps/pi-subagents-herdr**](https://github.com/maxedapps/pi-subagents-herdr) | Provides Make Pi use and control subagents via herdr. |
| [**bstncartwright/pi-bstn-subagents**](https://github.com/bstncartwright/pi-bstn-subagents) | Runs persistent Cursor ACP subagents from Pi with live Herdr viewers. |
| [**Nabsku/herdr-pi-subagents**](https://github.com/Nabsku/herdr-pi-subagents) | Provides Standalone Herdr pane runtime for pi-subagents. |
| [**maxedapps/pi-herdr-sidetrack**](https://github.com/maxedapps/pi-herdr-sidetrack) | Provides Easily start side conversations with Pi and herdr. |
| [**stefanopineda/herdr-web**](https://github.com/stefanopineda/herdr-web) | Provides Herdr Web, Tailnet phone client for Herdr sessions. |
| [**Githubwujinming/pi-guardian**](https://github.com/Githubwujinming/pi-guardian) | Provides Pi extension for monitoring herdr panes, auto-responds to askuserquestion and natural-language prompts. |
| [**kodama24ek/herdr-picker**](https://github.com/kodama24ek/herdr-picker) | Provides an fzf session picker for herdr, as fish functions. |
| [**Attamusc/pi-herdr**](https://github.com/Attamusc/pi-herdr) | Provides Pi extension that reports agent state to herdr. |
| [**TyRichards/pi-mega-brief**](https://github.com/TyRichards/pi-mega-brief) | Provides Weekly multi-agent orchestration for Pi with Herdr and tmux support. |
| [**conpiracy/lzy-ad-factory**](https://github.com/conpiracy/lzy-ad-factory) | Provides Pi + Herdr workspace package for creating UGC ads from product briefs, references, Gemini Omni prompts, QA, and export bundles. |
| [**taecontrol/pi-herdr**](https://github.com/taecontrol/pi-herdr) | Provides Give pi access to herdr. |
| [**yuki-kisaku/pi-agent-status**](https://github.com/yuki-kisaku/pi-agent-status) | Provides Terminal status extensions for the Pi coding agent (tmux, Zed, Orca, Herdr). |
| [**wujunchuan/pi-rename-pane**](https://github.com/wujunchuan/pi-rename-pane) | Provides Generate pi session names and rename the current Herdr pane. |
| [**alejodelosrios/kelpie**](https://github.com/alejodelosrios/kelpie) | Provides Consola nativa de Omarchy para herdr: sidebar de agentes por urgencia, notificaciones clickeables y terminal real. Zig + libghostty-vt + GTK4. |
| [**maxedapps/pi-herdr-fork**](https://github.com/maxedapps/pi-herdr-fork) | Uses Pi, create a fork in a new herdr window. |
| [**namtx/pi-herd**](https://github.com/namtx/pi-herd) | Provides pi extension: herdr sub-agent management, spawn, prompt, wait, read, and tear down sub-agents in herdr workspaces. |
| [**kodicw/pi-herdr**](https://github.com/kodicw/pi-herdr) | Provides Herdr integration for pi coding agent, manage workspaces, tabs, panes, and coordinate agents. |
| [**sdillen/pi-usage**](https://github.com/sdillen/pi-usage) | Provides Token & cost analytics for the pi coding agent: spend per model, provider, project, day and session, straight from the session logs in ~/.pi/agent/sessions/. Zero dependencies, no setup. |
| [**spoj/pi-show-herdr**](https://github.com/spoj/pi-show-herdr) | Provides a Pi tool that presents files in Herdr. |
| [**larryboiNEUQ/pi-herdr-ui-bridge**](https://github.com/larryboiNEUQ/pi-herdr-ui-bridge) | Bridges Pi blocking UI prompts into Herdr's blocked agent state for desktop notifications. |
| [**gpxl-dev/pi-herdr-split**](https://github.com/gpxl-dev/pi-herdr-split) | Opens parallel forked Pi sessions in Herdr panes and tabs. |
| [**andy-spike/herdr-theme**](https://github.com/andy-spike/herdr-theme) | Syncs the active Omarchy theme with Herdr. |
| [**yaukwan/pi-extensions**](https://github.com/yaukwan/pi-extensions) | Provides Monorepo for Pi extensions built on Herdr. |
| [**toasterman234/pi-herdr-firstmate**](https://github.com/toasterman234/pi-herdr-firstmate) | Provides Isolated Pi, Herdr, Moshi, and Firstmate fleet evaluation. |
| [**walidsi/pi-herdr-tab-namer**](https://github.com/walidsi/pi-herdr-tab-namer) | Provides a Pi extension that renames the current Herdr tab from a short summary of your first prompt in the session. |
| [**fpigeonjr/herdr-course**](https://github.com/fpigeonjr/herdr-course) | Provides a self-paced course for herding the pi coding agent with Herdr. |
| [**jhsu/pi-herdr-btw**](https://github.com/jhsu/pi-herdr-btw) | Provides pi extension to spawn a split pane with the current conversation using /btw and allow merging back to the parent with /btw merge. |
| [**wujunchuan/pi-fork-session-herdr**](https://github.com/wujunchuan/pi-fork-session-herdr) | Provides a Pi extension that forks the current persisted session into a new Herdr pane without replacing or stopping the Pi session in the original pane. |

### Pi: Presence, memory, and status extensions

*5 projects. Persistent memory trackers, presence indicators, and live status displays for Pi agents.*

| Project | What it does |
|---|---|
| [**ZingerLittleBee/herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins) | Provides Persistently pin Herdr agent sessions to the top of the Agents sidebar. |
| [**Mumega-com/herdr-mupot-bridge**](https://github.com/Mumega-com/herdr-mupot-bridge) | Provides herdr<->mupot bridge: flight monitor (Loom semantics), presence report, inbox deliver hop. Gate: kasra VERIFIED. |
| [**m4ttstack/herdr-chat**](https://github.com/m4ttstack/herdr-chat) | Provides rt chat where the agents live (broadcast, presence, jump-to-pane). |
| [**Dolliwyx/herdr-rpc**](https://github.com/Dolliwyx/herdr-rpc) | Provides Discord RPC for Herdr. |
| [**spi-ca/pi-herdr-presence**](https://github.com/spi-ca/pi-herdr-presence) | Extends Pi agent presence indicators and runtime status inside Herdr workspaces. |

### Subagent launchers and delegation

*114 projects. Tools for launching workers in separate panes and passing work between a lead agent and its helpers.*

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
| [**JonasBaeumer/herdr-file-annotator**](https://github.com/JonasBaeumer/herdr-file-annotator) | Maximizes agentic development without losing touch with the codebase through in-editor file annotations in Herdr. |
| [**e2b-dev/herdr-e2b-sandbox**](https://github.com/e2b-dev/herdr-e2b-sandbox) | Mirrors a git worktree into an E2B sandbox, one box or a branch-per-agent fleet, with a TUI dashboard. |
| [**diegopzz/herdr-updater**](https://github.com/diegopzz/herdr-updater) | Keeps Herdr and its plugins current across a whole fleet, safely. |
| [**IsaiasZc/herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a) | Provides Reliable agent-to-agent delegation layer for Herdr via A2A. |
| [**dbrain/kampr**](https://github.com/dbrain/kampr) | Provides Multi-device remote control for herdr. |
| [**moneycaringcoder/herdr-redact**](https://github.com/moneycaringcoder/herdr-redact) | Warns when an agent pane has printed credentials before screenshots, streaming, or chat paste operations occur. |
| [**marcvermeeren/chatter**](https://github.com/marcvermeeren/chatter) | Provides n experiment in cross-harness agent collaboration: a shared group chat and context layer for agents working on the same Git repository in Herdr. |
| [**husniadil/herdr-dispatch**](https://github.com/husniadil/herdr-dispatch) | Provides Dispatcher for the herdr-tasks board - a worker agent pane per ready task, the goal delivered, the worker tracked, and a stop at review, in one Go binary. |
| [**moneycaringcoder/herdr-pulse**](https://github.com/moneycaringcoder/herdr-pulse) | Provides Per-workspace agent activity history for herdr, rendered as a sidebar sparkline. |
| [**moneycaringcoder/herdr-collide**](https://github.com/moneycaringcoder/herdr-collide) | Warns when agents working in separate Git worktrees of the same repository are about to collide or conflict. |
| [**zackshen/herdr-translate**](https://github.com/zackshen/herdr-translate) | Provides translate mouse-selected terminal text in a centered popover. |
| [**fuad-daoud/relay**](https://github.com/fuad-daoud/relay) | Automates the plan/report handoff between planner and builder AI coding agent panes running under herdr. |
| [**AlexSamarsky/herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts) | Provides Only your prompts and the final answers from Codex or Claude, with a working composer. |
| [**newro/herdr-agent-nav**](https://github.com/newro/herdr-agent-nav) | Provides Sidebar index numbers for herdr spaces and agents, plus agent switching that pivots on the agent you were last in. |
| [**newro/herdr-window-util**](https://github.com/newro/herdr-window-util) | Provides Window management utilities for herdr: create, arrange, resize, and move between workspaces, tabs, and panes, with sidebar index numbers. |
| [**rrg/herdr-park-agents**](https://github.com/rrg/herdr-park-agents) | Parks a coding-agent pane in herdr: stop the process, close the pane, and resume the session later from a workspace panel. |
| [**YuSa0-6/herdr-issue-flow**](https://github.com/YuSa0-6/herdr-issue-flow) | Provides Herdr plugin: GitHub Issue worktrees, pi conductor/worker, and explicit Hunk review handoff. |
| [**kody-w/nerf-herdr-control-tower**](https://github.com/kody-w/nerf-herdr-control-tower) | Provides glanceable GUI dashboard, full-context .json export, bounded nurse policy, manual Horn broadcasts. |
| [**huketo/herdr-cron**](https://github.com/huketo/herdr-cron) | Provides Schedule automated work for coding agents: shell commands and prompts to coding agents in Herdr panes. |
| [**NachoPal/herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread) | Provides Per-pane 'unread' notifier + sidebar badge for herdr - surfaces agents that finish or need input in panes you aren't viewing (herdr tracks 'seen' per tab, not per pane). |
| [**zqkra/cbds**](https://github.com/zqkra/cbds) | Provides Reliable multi-agent orchestration for the Herdr herd. Durable tasks, authoritative worker reports, and a wait that cannot hang. |
| [**diegopzz/herdr-notify**](https://github.com/diegopzz/herdr-notify) | Provides Desktop notifications for herdr agents, including the ones running on other machines. |
| [**1Morganmore/herdr-activity-age**](https://github.com/1Morganmore/herdr-activity-age) | Displays the elapsed time since each agent's last status change in Herdr. |
| [**tamdogood/herdr-orc**](https://github.com/tamdogood/herdr-orc) | Provides a minimal, profile-driven custom orchestrator for Herdr. |
| [**kokatsu/herdr-tab-numbers**](https://github.com/kokatsu/herdr-tab-numbers) | Provides Prefix each tab name with its switchtab position. |
| [**devops-fj/herdr-handoff**](https://github.com/devops-fj/herdr-handoff) | Provides Preview and securely hand off local working context between Herdr coding agents. |
| [**imdigitalashish/pane-sheepdog**](https://github.com/imdigitalashish/pane-sheepdog) | Provides a Codex skill for herding sibling AI coding agents across Herdr panes: fan-out delegation, shared-pane safety, and a supervisor that wakes a sleeping orchestrator. |
| [**H3xept/git-shepherd**](https://github.com/H3xept/git-shepherd) | Provides Draft/open/merged/closed pull request state as an icon next to every Herdr Space. |
| [**egemenyildiz/herdr-slack**](https://github.com/egemenyildiz/herdr-slack) | Provides Drive your local herdr agents from Slack, browse, prompt, and launch from your phone. No tunnel. |
| [**evsinev/herdr-watch**](https://github.com/evsinev/herdr-watch) | Provides One-screen live monitor for herdr AI-agent sessions (local + SSH). |
| [**LittleDrinks/oh-my-herdr**](https://github.com/LittleDrinks/oh-my-herdr) | Provides Mission-command orchestration for CLI agents in Herdr tabs. |
| [**mupt-ai/context-drop**](https://github.com/mupt-ai/context-drop) | Provides a Herdr-backed meta-harness for orchestrating autonomous coding agents. |
| [**themuuln/herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync) | Provides Adapt herdr's theme and sidebar colors to the active Ghostty theme; keeps sidebar tokens alive across herdr restarts. herdr.dev plugin. |
| [**evancetesha/mini-code-factory**](https://github.com/evancetesha/mini-code-factory) | Provides a deliberately small three-role SDLC software factory: OpenCode agents orchestrated through Herdr for persistent panes, agent state, and file-based handoffs. |
| [**bennettgarcia-hs/herdr-jail**](https://github.com/bennettgarcia-hs/herdr-jail) | Runs coding agents in yolo-jail sandboxes (per-workspace jails, enforcement, sidebar visualization, workspace jail menu). |
| [**phin-tech/herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board) | Provides a status board over your spaces, todo, in progress, waiting on someone, done, plus any status you invent. List or kanban. |
| [**arvkonstantin/herdr-codex-subagents**](https://github.com/arvkonstantin/herdr-codex-subagents) | Provides Disposable, focus-safe Herdr panes for Codex subagents. |
| [**weirdry/crew**](https://github.com/weirdry/crew) | Provides Bounded multi-model collaboration skill for Herdr: a lead agent scopes, delegates to a different-model worker in a sibling pane, supervises, and reviews across bounded rounds. |
| [**sfsajid91/omp-orchestrator**](https://github.com/sfsajid91/omp-orchestrator) | Provides Multi-agent subagent orchestration for Oh My Pi (OMP) using Herdr terminal workspaces. |
| [**barnuri/herdr-auto-update**](https://github.com/barnuri/herdr-auto-update) | Keeps herdr always up to date, auto patch/minor/major updates with live handoff. |
| [**whshang/herdr-mcp**](https://github.com/whshang/herdr-mcp) | Provides a stable MCP and OAuth bridge for remote web planners to inspect and control local Herdr workspaces. |
| [**caina-barbosa/Herdr-orchestrator-bundle**](https://github.com/caina-barbosa/Herdr-orchestrator-bundle) | Provides Pi skill, watchdog, and extensions for orchestrating standalone Pi sessions in Herdr. |
| [**ericjuta/omp-fleet**](https://github.com/ericjuta/omp-fleet) | Provides Bounded Herdr supervisor control for Oh My Pi. |
| [**Austinsuyoyo/herdr-autoreload**](https://github.com/Austinsuyoyo/herdr-autoreload) | Provides Reload herdr's config.toml the moment you save it, and toast the diagnostics when an edit is rejected. |
| [**andrewromewo/herdr-lil-office**](https://github.com/andrewromewo/herdr-lil-office) | Provides your Claude sessions and their agents as a lil pixel tower, one floor per session, rooms grow as agents take jobs. |
| [**simoncrypta/bercail**](https://github.com/simoncrypta/bercail) | Provides Herdr-based agentic development environment. |
| [**RooseveltAdvisors/herdr-floax-adapter**](https://github.com/RooseveltAdvisors/herdr-floax-adapter) | Provides tmux-floax-inspired retained floating scratch shell for Herdr. |
| [**TeXmeijin/herdr-codex-handoff**](https://github.com/TeXmeijin/herdr-codex-handoff) | Transfers active sessions directly to Codex in adjacent panes when Claude hits usage limits. |
| [**haoliangwu/dsh-herdr**](https://github.com/haoliangwu/dsh-herdr) | Provides herdr multiplexer. |
| [**Kuznetsov-Ilia/agy**](https://github.com/Kuznetsov-Ilia/agy) | Provides warm agy pool + Cursor MCP. |
| [**maccie01/herdr-axi**](https://github.com/maccie01/herdr-axi) | Provides Agent-ergonomic CLI for herdr fleet supervision and orchestration. |
| [**Jiaofeisiling/herdr-task-bridge**](https://github.com/Jiaofeisiling/herdr-task-bridge) | Bridges Windows and NeSI Herdr Sentinel tasks with asynchronous delegation, an SQLite queue, and a PowerShell CLI. |
| [**TerrifiedBug/omp-telegram**](https://github.com/TerrifiedBug/omp-telegram) | Provides Owner-controlled Telegram bridge and herdr control plane for omp sessions. |
| [**simfor99/herdr-night-watch**](https://github.com/simfor99/herdr-night-watch) | Provides Fail-closed Windows tray watcher for overnight Herdr sessions: sleep/shutdown, live dashboard, system metrics, weather, moon phases, and Windows media timeline. |
| [**SheetMetalConnect/dsh-herdr**](https://github.com/SheetMetalConnect/dsh-herdr) | Provides DeepSeek Harness in your terminal, wired into Herdr: interactive ACP client with live pane state and one-key handoff to the harness web UI. |
| [**ruddyscent/codex-config**](https://github.com/ruddyscent/codex-config) | Provides reusable Codex instructions and skills for delegated open-source workflows, with worktree isolation and herdr pane management. |
| [**flotob/herdr-peer**](https://github.com/flotob/herdr-peer) | Provides Cross-machine task delegation and explicit replies for Herdr agents over SSH. |
| [**longcw/herdr-name-tab**](https://github.com/longcw/herdr-name-tab) | Provides One-word Herdr tab names, from the first thing you type in the tab. |
| [**leoszr/holistic-subagents**](https://github.com/leoszr/holistic-subagents) | Provides Persistent Pi delegations orchestrated through Herdr. |
| [**penggin/gsd-herdr**](https://github.com/penggin/gsd-herdr) | Provides yeeeeeeee. |
| [**Production-Grade/herdr-setup**](https://github.com/Production-Grade/herdr-setup) | Provides Herdr starter configuration, team workspace conventions and a first-session walkthrough from Production Grade. |
| [**RodrigoSosa96/workflow-control-plane**](https://github.com/RodrigoSosa96/workflow-control-plane) | Provides Deterministic control plane for AI-assisted development workflows across Pi, Claude, Codex, and Herdr. |
| [**HarryZus/herdr-dynamic-agent-workspace**](https://github.com/HarryZus/herdr-dynamic-agent-workspace) | Provides Dynamic Herdr workspace tabs and agent handoffs. |
| [**pandore/herdr-work**](https://github.com/pandore/herdr-work) | Provides Model-neutral coding-agent orchestration skill built around Herdr. |
| [**nativestrider/agent-control-skills**](https://github.com/nativestrider/agent-control-skills) | Provides Portable coordination skills for project control planes using Codex, Herdr, Git and GitHub. |
| [**mahirocoko/direct-cli-skill**](https://github.com/mahirocoko/direct-cli-skill) | Provides Pane-first Agent Skill for running Cursor, Antigravity, Codex, and Pi through Herdr or tmux. |
| [**YYHCOPPOLO/herdr-collab**](https://github.com/YYHCOPPOLO/herdr-collab) | Provides Agent skill: orchestrate herdr multi-workspace work, name panes, push messages between agents, dispatch tickets to workers, hand finish packages to an executor clerk. Push, never poll. |
| [**mingrath/fanout**](https://github.com/mingrath/fanout) | Provides Three frontier models attempt one task in parallel Herdr panes, blind-evaluated and merged into one tested result. |
| [**SuperInstance/herdr-cocapn**](https://github.com/SuperInstance/herdr-cocapn) | Provides herdr + cocapn-core: agent multiplexer meets fleet management. Automatic tier escalation and deadband triggers for herdr agents. |
| [**brenoperucchi/herdr-mesh-tools**](https://github.com/brenoperucchi/herdr-mesh-tools) | Provides Automation layer on top of Herdr: workspace/agent bootstrap, background notifications, blind/parallel review cycle, and executor swap with context handoff. |
| [**i11v/orchestrate-skill**](https://github.com/i11v/orchestrate-skill) | Provides an Agent Skill for coordinating and actively steering subagents through Herdr across implementation, review, consultation, and log-monitoring workflows. |
| [**tuong-nguyen-vn/personal-assistant-template**](https://github.com/tuong-nguyen-vn/personal-assistant-template) | Provides a bootstrap template for a personal coordinator agent with Herdr delegation skills. |
| [**makyinmars/muster**](https://github.com/makyinmars/muster) | Provides a native macOS command center for coding agents powered by Herdr and Ghostty. |
| [**olakara/handoff**](https://github.com/olakara/handoff) | Provides trying agent handoff in herdr. |
| [**txchen/tmux-rail**](https://github.com/txchen/tmux-rail) | Provides herdr, but in tmux. |

### Autonomous coding and pull-request loops

*10 projects. Long-running workflows that implement changes, open pull requests, review results, and react to CI.*

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

*14 projects. Queues and event-driven systems that turn stored work into agent jobs.*

| Project | What it does |
|---|---|
| [**nelsonPires5/herdr-board**](https://github.com/nelsonPires5/herdr-board) | A Kanban TUI and background service that turns cards into prompts for agents in visible Herdr panes. Moving a card can create an agent, run it in a dedicated tab, and advance the work through review gates. |
| [**0x5c0f/herdr-insight**](https://github.com/0x5c0f/herdr-insight) | A dockable timeline that combines agent events from every Herdr workspace. It shows active and blocked states, session IDs, configurable columns, and a deduplicated seven-day history that remains current across workspace changes. |
| [**carze/herdr-smolmachine**](https://github.com/carze/herdr-smolmachine) | Starts a coding agent inside a libkrun/KVM microVM from a Herdr pane. A prepared image and shell pipeline manage the VM, while Herdr still provides normal pane control, detaching, and reattaching. |
| [**saiashirwad/homestead**](https://github.com/saiashirwad/homestead) | Creates an isolated worktree for each branch or GitHub issue, including separate ports, environment files, and setup. It launches an agent in Herdr, tracks progress, lands completed branches, and removes finished environments. |
| [**DnzzL/herdr-automations**](https://github.com/DnzzL/herdr-automations) | Schedules recurring prompts and cron jobs that run agents in fresh Herdr worktrees. It supports task-specific MCP settings, collision protection, persistent run history, and a live monitoring board. |
| [**ram4-dev/herdr-automations**](https://github.com/ram4-dev/herdr-automations) | Runs scheduled or event-triggered agent jobs from cron expressions, intervals, and lifecycle hooks. It prevents overlapping runs, creates fresh Git worktrees, and records complete execution histories. |
| [**Eslsamu/herdr-tasks**](https://github.com/Eslsamu/herdr-tasks) | Keeps an agent-owned task queue linked to each Herdr space, with atomic claims, priorities, dependencies, and durable conversation ownership. An always-visible Herdr summary and local read-only browser view let people follow the work without maintaining cards. |
| [**husniadil/herdr-tasks**](https://github.com/husniadil/herdr-tasks) | Provides Task backlog and notes board for coding agents on Herdr - claims with leases, evidence-backed review, and a human decision gate, in one Go binary. |
| [**sazardev/herdr-code-board**](https://github.com/sazardev/herdr-code-board) | Provides a kanban queue for agentic prompts inside Herdr: cards dispatch real agents into panes, worktrees and workspaces, with rules that chain one card to the next. |
| [**chris-yyau/hermes-herdr-auto-reconcile**](https://github.com/chris-yyau/hermes-herdr-auto-reconcile) | Provides Gateway liveness plugin for Hermes supervisors watching Herdr panes. |
| [**MatheusBBarni/herdr-tasks**](https://github.com/MatheusBBarni/herdr-tasks) | Provides a kanban task runner for Herdr: OpenTUI board plus htasks CLI. |
| [**btj93/herdr-tabline**](https://github.com/btj93/herdr-tabline) | Renders Herdr tab labels with safe templates and project-aware profiles. |
| [**carlotran4/omarchy-herdr**](https://github.com/carlotran4/omarchy-herdr) | Provides a native Omarchy bar plugin for live Herdr coding-agent status and one-click focus. |
| [**lenaertsjan/herdr-factory-demo**](https://github.com/lenaertsjan/herdr-factory-demo) | Provides a small local-first task manager for end-to-end herdr-factory tests. |

### Linear, GitHub Issues, and issue-to-PR automation

*25 projects. Automated pipelines bridging issue trackers directly to Herdr agent workspaces and PRs.*

| Project | What it does |
|---|---|
| [**spad-0x/herdr-mobile-pro**](https://github.com/spad-0x/herdr-mobile-pro) | Provides a high-performance, mobile-first PWA dashboard with a Cyber-Dark design for orchestrating Herdr and autonomous AI agents directly from your smartphone. Features secure HTTPS, speech-to-text dictation, vision uploads, and real-time semantic parsing of terminal outputs into a chat-centric interface. |
| [**leoleducq/devflow**](https://github.com/leoleducq/devflow) | Provides Give a git worktree everything it needs to run: seeded Postgres, ports, .env files, deps and dev servers. Built for herdr workspaces and coding agents. |
| [**ivorpad/herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel) | Provides put a local port on the public internet, copy the URL, take it down again. |
| [**ZviBaratz/herdr-draft**](https://github.com/ZviBaratz/herdr-draft) | Provides a new-session creation dialog unifying Linear issues, worktree creation, agent types, and initial prompts. |
| [**korvyashka/herdr-pr-relay**](https://github.com/korvyashka/herdr-pr-relay) | Picks pull requests and dispatches them to active agent sessions as review prompts. |
| [**hilmimuktitama/herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek) | Provides Read-only Jira Cloud previews from your current Herdr pane. |
| [**NightingaleMedia/herdr-github-orobo**](https://github.com/NightingaleMedia/herdr-github-orobo) | Provides plugin for herdr to see open PRs and take actions. |
| [**JacquesvanWyk/herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear) | Provides fzf-driven Linear panel in a herdr split pane or tab: search issues, drill into projects, create issues, change status. |
| [**danielv14/herdr-treehouse**](https://github.com/danielv14/herdr-treehouse) | Provides a herdr plugin to manage git worktrees with repo specific setup configurations. |
| [**ivorpad/herdr-ports**](https://github.com/ivorpad/herdr-ports) | Provides a popup that lists listening ports, names the project behind each one, and kills or opens it. |
| [**mkmah/herdr-frontier**](https://github.com/mkmah/herdr-frontier) | Provides Terminal-first issue frontier for herdr, triage, claim, and herd agent work. |
| [**H3xept/herdr-ingest**](https://github.com/H3xept/herdr-ingest) | Provides workflows for starting and resuming work sessions with Herdr. |
| [**ukwhatn/taskherd**](https://github.com/ukwhatn/taskherd) | Provides Task board linked to herdr agent sessions, PRs, and Jira tickets. |
| [**jirathip-dev/corral**](https://github.com/jirathip-dev/corral) | Provides Read-only fleet monitor for herdr coding agents. |
| [**jeremN/herdr-dispatch-plugin**](https://github.com/jeremN/herdr-dispatch-plugin) | Dispatches tickets through an AI-agent pipeline, one git worktree per ticket, each phase in a named pane, fail-closed, with a human approval gate. |
| [**spiritsack/herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree) | Provides prompt for a Jira ticket, open/reuse a matching git worktree, and prefill it into a fresh Claude Code session. |
| [**brooswit-factory/butchr**](https://github.com/brooswit-factory/butchr) | Provides the software factory: watches your Jira, runs herdr agents on active tickets, pushes updates to them over MCP. |
| [**dkta-labs/agentd**](https://github.com/dkta-labs/agentd) | Provides a minimal local supervisor for scheduled agent jobs and durable run evidence. |
| [**jmwind/issue-herd**](https://github.com/jmwind/issue-herd) | Watches Linear; when an issue matches a rule, run Claude Code in a herdr workspace and report the PR back to the issue. |
| [**jirathip-dev/herdr-fleet**](https://github.com/jirathip-dev/herdr-fleet) | Provides Typed, plan-first CLI for operating Herdr coding-agent fleets. |
| [**hdtradeservices/ticketdeck**](https://github.com/hdtradeservices/ticketdeck) | Provides Terminal dashboard for your assigned Linear tickets, launches/re-attaches a Claude Code session per ticket, on top of herdr. |
| [**PanchTime/linear-widget**](https://github.com/PanchTime/linear-widget) | Provides Omarchy bar widget for Linear issues, Herdr worktrees, and GitLab/GitHub MR links. |
| [**freethinkel/shepherd**](https://github.com/freethinkel/shepherd) | Controls plane for coding agents on top of Herdr: tracker task in, pull request out. |
| [**robertdo/claude-herdr-orchestration**](https://github.com/robertdo/claude-herdr-orchestration) | Provides Worktree-per-change git hygiene for Claude Code, enforced by hooks. Main is deployable by construction, not by discipline. |
| [**glasner/shipyard**](https://github.com/glasner/shipyard) | Provides plugin stacks and skills for Cursor and Grok agents integrating with Herdr multiplexer panes. |

### General workflows and skill packs

*138 projects. Reusable skills, commands, and opinionated setups for common agent workflows.*

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
| [**robbyrussell/herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh) | Integrates Herdr with Oh My Zsh, displaying slow commands in the sidebar and triggering desktop completion notifications. |
| [**bayoudhi/herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress) | Provides a live sidebar progress for slow shell commands, not just coding agents. |
| [**crafts69guy/herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard) | Provides a herdr plugin: fuzzy-switch across running agents, open workspaces, and ghq repositories in one Rust TUI, and open a repo in a new workspace, tab, split, or the current pane. |
| [**itsmaleen/merry**](https://github.com/itsmaleen/merry) | Provides iPhone companion for AI coding agents, mirror notifications, control workspaces and surfaces, paste photos/files, and send voice commands from your phone. Fronts cmux and herdr. |
| [**speardragon/herdr-command-center**](https://github.com/speardragon/herdr-command-center) | Provides One keybinding for every command, a herdr popup that lists the commands you registered, runs them by arrow key or number, and closes itself before the command fires. |
| [**jakekroon/herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker) | Provides Every open pull request you have authored, docked and colour-coded by what needs you. A Herdr plugin. |
| [**thuanlm215/advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer) | Provides Git-aware file viewer for Herdr: full-text and file search (workspace or folder), context actions that open workspaces and panes, Unicode/Nerd icons, independent tree scrolling. |
| [**cyperx84/herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro) | Provides sesh-style fuzzy session picker for Herdr, workspaces, agents, and zoxide dirs in one fzf popup with live previews. |
| [**maxguzenski/herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch) | Provides GitHub PR status of each workspace and agent pane in the sidebar. |
| [**elKei24/herdr-co-review**](https://github.com/elKei24/herdr-co-review) | Provides Split-screen PR review in herdr: your agent finds issues, you triage each one next to its code in a TUI, the agent posts what you approve. |
| [**Binb1/herdr-palette**](https://github.com/Binb1/herdr-palette) | Provides Command palette for Herdr. Jump to workspaces and agents, run plugin actions, run Herdr commands. |
| [**jpwallace22/herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status) | Provides a [Herdr]( plugin that shows each workspace's GitLab merge request status in the spaces sidebar, as a $mr token on the workspace row:. |
| [**ArtMoreno/quota-deck**](https://github.com/ArtMoreno/quota-deck) | Provides quota-deck: credential-scoped AI quota and context for Herdr on Windows, macOS, and Linux. |
| [**andschneider/roboherd**](https://github.com/andschneider/roboherd) | Provides roborev review status and actions inside your herdr workspace. |
| [**moneycaringcoder/herdr-shear**](https://github.com/moneycaringcoder/herdr-shear) | Provides Find the git worktrees that are safe to delete, and delete those. A worktree janitor for herdr. |
| [**playsthisgame/herdr-x**](https://github.com/playsthisgame/herdr-x) | Browses x.com in a terminal split inside herdr, and draft posts in $EDITOR to send yourself. |
| [**42lizard/herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout) | Provides DWM-style master/stack layouts for Herdr. |
| [**cantona/herdr-triggers**](https://github.com/cantona/herdr-triggers) | Provides Resident regex triggers over pane output: automated logins and other regex-driven terminal triggers. |
| [**zackshen/herdr-workspace**](https://github.com/zackshen/herdr-workspace) | Creates a workspace and apply a layout profile from a centered popup. |
| [**jackfrancisdalton/herdr-chromatic-spaces**](https://github.com/jackfrancisdalton/herdr-chromatic-spaces) | Provides Give every Herdr Space its own colour and emoji: coloured sidebar dots, grouped agents, and optional chrome tint on space switch. |
| [**yelsed/herdr-pr**](https://github.com/yelsed/herdr-pr) | Provides a Todo of the pull requests waiting on you, in a herdr pane. Reads everything through the gh CLI. |
| [**moneycaringcoder/herdr-standup**](https://github.com/moneycaringcoder/herdr-standup) | Generates summaries of agent activity across Herdr workspaces over time, including commits, diff volume, and branches. |
| [**DeepRuparel/herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify) | Controls Spotify playback and playlist queues directly from Herdr terminal panes. |
| [**Angel-O/herdr-labels**](https://github.com/Angel-O/herdr-labels) | Provides automatically names and numbers tabs while preserving manual labels. |
| [**macintacos/herdr-scratch**](https://github.com/macintacos/herdr-scratch) | Provides a toggleable scratch shell popup for Herdr backed by tmux state preservation. |
| [**giacolees/herdr-openlogi**](https://github.com/giacolees/herdr-openlogi) | Maps Logitech mouse buttons to Herdr navigation commands using OpenLogi overlays. |
| [**sazardev/herdr-pomodoro**](https://github.com/sazardev/herdr-pomodoro) | Provides Minimal, elegant, theme-adaptive Pomodoro timer plugin for Herdr. |
| [**iurysza/herdr-mosaic**](https://github.com/iurysza/herdr-mosaic) | Provides Experimental Herdr plugin for space colors, agent grouping, and pane layouts. |
| [**nemolize/herdr-plugin-command-palette**](https://github.com/nemolize/herdr-plugin-command-palette) | Provides a command palette plugin for herdr. |
| [**j1nn0/herdr-harvest**](https://github.com/j1nn0/herdr-harvest) | Captures completion outputs from Herdr agent fleets into a persistent result inbox. |
| [**bonkey/herdr-keep-root**](https://github.com/bonkey/herdr-keep-root) | Keeps a repository's main-checkout workspace open while any of its worktree workspaces is open, so the Spaces panel never flattens a worktree group. |
| [**huketo/herdr-hitl**](https://github.com/huketo/herdr-hitl) | Blocks a Herdr coding agent on a human decision, delivered to your phone over Telegram or Discord. |
| [**jackfrancisdalton/herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette) | Fuzzy-finds any Herdr space, tab, agent or pane and jump straight to it. |
| [**victor-software-house/herdr-restore-notice**](https://github.com/victor-software-house/herdr-restore-notice) | Provides Compact Herdr restore notices with click-to-resume agent sessions. |
| [**xheisenbugx/herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh) | Provides a smart herdr workspace manager inspired by sesh. |
| [**xlinx/herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir) | Provides herdr-auto-yes-sir for non blocked running when agent ask for approve; like codex. |
| [**y-hirakaw/herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane) | Provides Docked click-to-launch pane for herdr, Finder/Explorer, VS Code, or any command you configure, per workspace. |
| [**huketo/herdr-sheep**](https://github.com/huketo/herdr-sheep) | Watches your Herdr coding agents as a flock of animated ASCII sheep. |
| [**jwanga/herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status) | Provides a real-time GitHub project status pane (milestones, issues, PRs, Actions) docked on the right at sidebar width. |
| [**pauljohnchamberlain/herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard) | Provides Guarded external control for Herdr from Codex, Claude, and other coding agents. |
| [**macintacos/herdr-reshape**](https://github.com/macintacos/herdr-reshape) | Provides a herdr plugin that moves the focused pane around its tab and squares the tab up into an even grid. |
| [**hota911/herdr-command-palette**](https://github.com/hota911/herdr-command-palette) | Provides fzf command palette for herdr's built-in operations, workspaces, tabs, panes, agents. |
| [**caseneuve/herdr-worktree-bootstrap**](https://github.com/caseneuve/herdr-worktree-bootstrap) | Provides seeding newly created Git worktrees. |
| [**caner-akca/herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows) | Launches and monitor isolated Atomic workflow tasks, campaign board, sidebar tokens, run ledger, and an optional Telegram cockpit. |
| [**DecampsRenan/herdr-plugin-env-sync**](https://github.com/DecampsRenan/herdr-plugin-env-sync) | Provides Herdr plugins: env-sync sets up new Git worktrees (.env copy, remote branch tracking, setup commands) with a live status panel. |
| [**tgdn/herdr-caffeinated**](https://github.com/tgdn/herdr-caffeinated) | Provides Herdr sidebar indicator that shows when caffeinate is keeping your machine awake. |
| [**choplin/herdr-quickselect**](https://github.com/choplin/herdr-quickselect) | Provides Select visible terminal text and run configurable actions in Herdr. |
| [**bxuserx/kerdr**](https://github.com/bxuserx/kerdr) | Provides Herdr fork with a agentic kanban board. |
| [**victor-software-house/herdr-stash**](https://github.com/victor-software-house/herdr-stash) | Provides Stash a Herdr workspace: stop its agents, keep its shape and their conversations, and restore it later from a clickable two-column popup. |
| [**oborchers/proqi**](https://github.com/oborchers/proqi) | Provides a terminal-native prompt composer for power users running multiple coding agents. |
| [**yersonargotev/tabby**](https://github.com/yersonargotev/tabby) | Labels focused tabs with a Significant Command or Working Directory Basename. |
| [**codingfragments/herdr-zextract**](https://github.com/codingfragments/herdr-zextract) | Provides Port of zextract (Zellij plugin) to run as a native Herdr plugin. |
| [**Haichiu/herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border) | Provides a minimal Herdr plugin that shows canonical pane IDs on pane borders. |
| [**j1nn0/herdr-plugin-sdk**](https://github.com/j1nn0/herdr-plugin-sdk) | Provides Unofficial TypeScript SDK and toolkit for building, testing, and integrating Herdr plugins. |
| [**agutier6/herdr-paddock**](https://github.com/agutier6/herdr-paddock) | Provides every worktree gets its own pasture. Allocates a contiguous port block per worktree, runs repo-owned setup/teardown on worktree.created/opened/removed, and launches dev/test/build scripts in their own panes, all declared in one .pastr.toml. |
| [**GHJQ/capslock-herdr-prefix**](https://github.com/GHJQ/capslock-herdr-prefix) | Provides Make Caps Lock the herdr prefix key on macOS. |
| [**zap0xfce2/herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart) | Runs a configured command in named panes on server startup. |
| [**GranamyrBR/ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr) | Provides a live multi-agent observability and pane controls for Herdr. |
| [**dgnsrekt/herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke) | Provides get yoked, two tabs side by side, one key. Chrome's split view for herdr. |
| [**ericcparsons/herdr-vitals**](https://github.com/ericcparsons/herdr-vitals) | Provides macos herdr plugin: CPU/RAM per agent and active dev server ports per space, in the sidebar, plus a popup to kill them. |
| [**MatiasL13/herdr-k9s**](https://github.com/MatiasL13/herdr-k9s) | Runs K9s in its own Herdr tab with an fzf context picker and a read-only guard for production clusters. |
| [**aquaherd/goose-herdr**](https://github.com/aquaherd/goose-herdr) | Provides goose integration for Herdr: MCP extension + agent-state hook. |
| [**fabiogaliano/herdr-command-palette**](https://github.com/fabiogaliano/herdr-command-palette) | Provides Fuzzy command palette for Herdr, search every action, see its shortcut, run it. |
| [**hitaishi2222/herdr-llama**](https://github.com/hitaishi2222/herdr-llama) | Controls your llama-server from your fingertips. |
| [**Shi1xin/herdr-gitui**](https://github.com/Shi1xin/herdr-gitui) | Provides gitui in a sidebar pane, open/toggle, expand, light/dark themes. |
| [**shaozk/herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane) | Provides a Herdr plugin, Shadow Clone Panel: Control multiple panels simultaneously. |
| [**patricio0312rev/anyssh**](https://github.com/patricio0312rev/anyssh) | Provides open-source SSH client for iPhone and iPad: terminal, remote git and files, tmux and herdr. No backend, no telemetry. |
| [**NolanHo/DSH-herdr**](https://github.com/NolanHo/DSH-herdr) | Provides DSH plugin: herdr workspace view, structured spaces/agents/panes control from the DSH web GUI (app view). |
| [**pjgeutjens/omarchy-feed-the-flock**](https://github.com/pjgeutjens/omarchy-feed-the-flock) | Provides Keyboard-first Omarchy prompt capture and paced Herdr delivery. |
| [**abelfubu/herdr-popup**](https://github.com/abelfubu/herdr-popup) | Provides Generic Herdr popup pane plugin for ad-hoc shell commands. |
| [**haisi/herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette) | Provides Fuzzy-searchable command palette for herdr, backed by fzf. |
| [**leonho/herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks) | Provides per-project command bookmarks popup. Run bookmarked commands in a separate shell while your agent is busy (global, project, and smart sections). |
| [**geshido/icomark**](https://github.com/geshido/icomark) | Provides Workflow status and comment markers for Zellij, agterm, and Herdr tabs. |
| [**NikNovo/deathstar**](https://github.com/NikNovo/deathstar) | Provides Local-first observability dashboard for host memory pressure and OMP/Herdr sessions. |
| [**arturodz/dev**](https://github.com/arturodz/dev) | Provides Persistent remote development workspaces with Herdr, Tailscale, systemd, Caddy, and PostgreSQL. |
| [**sigma/sd-herdr**](https://github.com/sigma/sd-herdr) | Streams Deck plugin for managing herdr status. |
| [**Yukaii/herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup) | Runs Kakoune terminal commands in native Herdr popups. |
| [**cescofry/fixme**](https://github.com/cescofry/fixme) | Provides fix problems from previous commands (uses herdr and pi). |
| [**henrywang/herdr-workflow**](https://github.com/henrywang/herdr-workflow) | Provides Opinionated multi-agent workflows for herdr, with cross-model planning, adversarial code review, bounded iteration, Git worktrees, and automated pull-request delivery. |
| [**Yukaii/herdr.kak**](https://github.com/Yukaii/herdr.kak) | Provides a native Herdr panes, tabs, focus navigation, and popups from Kakoune. |
| [**tombell/tendr**](https://github.com/tombell/tendr) | Provides Go CLI for declaratively managing local Herdr projects. |
| [**aelaguiz/herdr-mcp**](https://github.com/aelaguiz/herdr-mcp) | Provides MCP server exposing control and inspection of a running herdr session (thin stdio bridge over the herdr CLI). |
| [**kylescudder/schmerdr**](https://github.com/kylescudder/schmerdr) | Provides Template-driven workspace launcher for herdr, one editable layout per project that builds tabs, panes, commands, and AI agents (like shmux, for the herdr AI-agent terminal). |
| [**Phoobobo/taya**](https://github.com/Phoobobo/taya) | Provides True Assistant for software engineers, powered by Pi, Herdr, and herdr-workboard. |
| [**gregorgebhardt/worktrunk-herdr.zsh**](https://github.com/gregorgebhardt/worktrunk-herdr.zsh) | Provides Zsh commands for opening Worktrunk worktrees as Herdr spaces. |
| [**clayton/lernrherdr**](https://github.com/clayton/lernrherdr) | Provides Learn stock Herdr key chords and CLI commands. |
| [**cskwork/herdr-cheatsheet**](https://github.com/cskwork/herdr-cheatsheet) | Provides Single-page Herdr cheatsheet: keybindings, CLI, and an agent setup prompt. GitHub Pages landing. |
| [**shaun-agent/herder-shelving-skill**](https://github.com/shaun-agent/herder-shelving-skill) | Provides Public-safe agent skill for discovering and restoring custom Herdr workspace shelves. |
| [**shippy/raycast-herdr**](https://github.com/shippy/raycast-herdr) | Provides Raycast extension for controlling herdr. |

---

## 2. Connect through MCP and the socket API

*237 projects. Protocols, clients, bots, and event bridges that link Herdr to external tools, editors, and messaging apps.*

### MCP servers

*14 projects. Servers that expose Herdr operations as MCP tools for compatible AI clients.*

| Project | What it does |
|---|---|
| [**Phoobobo/herdr-agent-config-manager**](https://github.com/Phoobobo/herdr-agent-config-manager) | Provides tools for auditing and managing skills, MCP servers, plugins, and lifecycle hooks across workspaces. A central manifest helps keep agent configuration consistent. |
| [**runchr-works/herdr-mesh**](https://github.com/runchr-works/herdr-mesh) | Connects multiple Herdr instances into a coordinated mesh over Model Context Protocol. |
| [**eugeneb50/herdr-mcp**](https://github.com/eugeneb50/herdr-mcp) | Exposes Herdr workspace and pane controls as tools to any Model Context Protocol (MCP) client. |
| [**54rt1n/herdr-simple-mcp**](https://github.com/54rt1n/herdr-simple-mcp) | Provides a lightweight Model Context Protocol server for driving Herdr from Claude Desktop and Cursor. |
| [**islam3zzat/herdr-mcp**](https://github.com/islam3zzat/herdr-mcp) | An MCP server that lets AI assistants inspect and control coding agents running in Herdr through a socket-based communication bridge. |
| [**bonsai/herdr-mcp**](https://github.com/bonsai/herdr-mcp) | Provides Herdr tab control from OpenCode through MCP and also works as a Herdr plugin. |
| [**jasonrr/herdr-tally**](https://github.com/jasonrr/herdr-tally) | Provides Project-scoped todos & scratchpads for you and your agents. |
| [**Orange-County-AI/herdr-mcp**](https://github.com/Orange-County-AI/herdr-mcp) | Exposes Herdr's socket API as a local or remote MCP server. |
| [**aneym/unblock**](https://github.com/aneym/unblock) | Provides One queue for everything your agents need from you. Blockers need an action, grills need a judgement; secrets never enter the model's context. |
| [**boozedog/herdr-mcp**](https://github.com/boozedog/herdr-mcp) | Provides MCP server for Herdr agent coordination (Deno + Effect). |
| [**husniadil/olympus**](https://github.com/husniadil/olympus) | Provides a terminal you can drive from code: create, drive, observe and tear down real terminal sessions on zmx, tmux, meja or herdr, through a Go package, a CLI and a stdio MCP server. |
| [**bonkey/herdr-dup-tab**](https://github.com/bonkey/herdr-dup-tab) | Provides duplicate the focused pane's running command into a new tab. |
| [**simozampa/agent-relay**](https://github.com/simozampa/agent-relay) | Provides a secure, asynchronous MCP gateway for persistent coding agents. |
| [**joshuaswarren/allward**](https://github.com/joshuaswarren/allward) | Provides a native macOS terminal for people who run coding agents across machines. |

### Socket API clients and SDKs

*74 projects. Libraries, command-line clients, and services that communicate with Herdr through its local socket.*

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
| [**dmmulroy/herdr-ts-sdk**](https://github.com/dmmulroy/herdr-ts-sdk) | Provides an Effect-native TypeScript SDK for Herdr's local protocol-21 socket API. |
| [**AlexandreAkao/herdr-bridge-compozy**](https://github.com/AlexandreAkao/herdr-bridge-compozy) | Provides compozyos extension that surfaces your agents as agent rows in herdr, with a colorized log pane. |
| [**AlexBSoD/herdrtabrenamer**](https://github.com/AlexBSoD/herdrtabrenamer) | Provides Automatic tab naming for herdr: names tabs after the program, agent or directory running inside them. |
| [**sendhil/herdr-menubar**](https://github.com/sendhil/herdr-menubar) | Provides a native macOS menu-bar companion for Herdr. See which coding agents are working, blocked, or done; jump directly to the relevant pane; and stay aware of agents needing attention while working in other apps. |
| [**AZenking/herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center) | Provides a Herdr popup for monitoring and focusing local Node.js, Bun, and Deno services. |
| [**mkellerman/herdex**](https://github.com/mkellerman/herdex) | Provides Herdex, a native VS Code client for Herdr: manage AI coding agents, workspaces, and their live state without leaving the editor (unofficial). |
| [**clement-micol/herdr-bridge**](https://github.com/clement-micol/herdr-bridge) | Bridges from herdr panes to VS Code: attach herdr terminals via vscode:// URIs. |
| [**acjackman/herdr-title-rename**](https://github.com/acjackman/herdr-title-rename) | Provides tmux-style window titles and automatic tab/workspace renaming for herdr. |
| [**RooseveltAdvisors/herdr-open-nvim**](https://github.com/RooseveltAdvisors/herdr-open-nvim) | Provides extract file links from the session transcript and open them in nvim (prefix+e). |
| [**opencharly/plugin-herdr**](https://github.com/opencharly/plugin-herdr) | Controls Herdr terminal multiplexer sessions over its NDJSON socket API using Charly commands. |
| [**OcHub-team/OcHerdr**](https://github.com/OcHub-team/OcHerdr) | Provides a native macOS GUI client for Herdr, built with ochub-ui and libghostty-vt. |
| [**rudironsoni/HerdrKit**](https://github.com/rudironsoni/HerdrKit) | Provides a Swift 6 client kit implementing Herdr JSON socket API protocols 17 through 22. |
| [**brooswit-factory/jsHerdrSDK**](https://github.com/brooswit-factory/jsHerdrSDK) | Provides a typed TypeScript client for the herdr socket API, generated from its published JSON Schema. |
| [**DanyGoT/herdr-companion**](https://github.com/DanyGoT/herdr-companion) | Adds a web-based sidecar for herdr. |
| [**brooswit-factory/drovr**](https://github.com/brooswit-factory/drovr) | Provides Wrapper around the herdr SDK: catches block situations herdr does not report, and overrides herdr's reporting where it is wrong. |
| [**michiomochi/herdr-sound-toggle**](https://github.com/michiomochi/herdr-sound-toggle) | Provides Toggle herdr's ui.sound.enabled from a persistent bottom pane, auto-opened on workspace.created. |
| [**johnlindquist/herdr-game**](https://github.com/johnlindquist/herdr-game) | Provides Interactive game for learning Herdr shortcuts, workflows, and agent operations. |
| [**bryandph/herdr-client**](https://github.com/bryandph/herdr-client) | Provides a typed Rust client for Herdr's socket API. |
| [**StarDuster/mimo-code-herdr-plugin**](https://github.com/StarDuster/mimo-code-herdr-plugin) | Shows MiMo Code agent state in herdr's sidebar, a user-level MiMo plugin, no herdr changes required. |
| [**vika2603/herdr-client**](https://github.com/vika2603/herdr-client) | Provides a typed Go client and plugin toolkit for Herdr's socket API, generated from the schema the herdr binary prints and covering all 102 methods of protocol 22. Adds a reconnecting session mirror, the pane graphics frame stream, and the manifest parser and entrypoint dispatch a Go plugin needs. |

### Chat alerts: Telegram, Discord, and Slack

*22 projects. Bot and channel alerts that ping you when agents finish or need input.*

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
| [**barnuri/herdr-notifications**](https://github.com/barnuri/herdr-notifications) | Provides Telegram notifications when an agent goes idle, gets blocked, or finishes. |
| [**elkraps/herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify) | Provides Customizable Telegram notifications for Herdr agent state changes, with status filters, templates, multi-chat delivery, deduplication, Codex approval buttons, completion summaries, and built-in diagnostics. |
| [**barnuri/herdr-command-palette**](https://github.com/barnuri/herdr-command-palette) | Provides an F1-style command palette for Herdr to fuzzy-search and execute actions across installed plugins. |
| [**jamescary/mo**](https://github.com/jamescary/mo) | Provides Persistent omp coding-agent sessions on a remote Mac, over SSH: tmux + herdr + optional Telegram control from your phone. |
| [**alex-devdone/herdr-sched**](https://github.com/alex-devdone/herdr-sched) | Provides schedule messages to be typed into a herdr pane later, Slack-style. |
| [**gpando/herdr-sense**](https://github.com/gpando/herdr-sense) | Provides Raspberry Pi Sense HAT agent status indicator (MQTT subscriber companion for herdr-telegram). |
| [**vinceferro/herdr-tg**](https://github.com/vinceferro/herdr-tg) | Provides Telegram front door for herdr agent herds - one bot per workspace, chat-native ask/answer, deterministic routing, single Rust binary. |
| [**zydou/herdr-screenshot**](https://github.com/zydou/herdr-screenshot) | Renders ANSI text from Herdr panes into PNG screenshots for Telegram sharing. |

### Desktop, mobile, and webhook notifications

*48 projects. System toasts, ntfy pings, and webhook triggers for agent events.*

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
| [**coryshaw1/herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp) | Provides Floating cliamp for herdr that keeps playing when hidden: the player lives in a detached herdr session, so closing the float only detaches. |
| [**bigbug16/herdr-topbar**](https://github.com/bigbug16/herdr-topbar) | Provides macos menu bar icon for herdr, jump back to your session, open a project, and see which agent is waiting for input. |
| [**wavrin/herdr-ferry**](https://github.com/wavrin/herdr-ferry) | Moves files and clipboard between the Herdr box and your laptop over SSH, no cloud bucket. |
| [**michmos/herdr-pomodoro**](https://github.com/michmos/herdr-pomodoro) | Provides Pomodoro inside herdr's status bar. |
| [**bonkey/herdr-wt-purpose**](https://github.com/bonkey/herdr-wt-purpose) | Provides worktree from a purpose or ticket URL, branch named by Apple's on-device model, scaffolded in the background. |
| [**cheoljoo/herdr-space-activity-monitor**](https://github.com/cheoljoo/herdr-space-activity-monitor) | Marks Space sidebar rows as printing / unseen-output / idle via a custom $activity token. |
| [**jefflau/herdr-webhook**](https://github.com/jefflau/herdr-webhook) | Posts agent done/blocked events to a webhook. |
| [**Rockheung/herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell) | Displays visual bell indicators in Kaku tabs when Herdr agents await human input. |
| [**thesimonharms/herdr-cmd-agent-plugin**](https://github.com/thesimonharms/herdr-cmd-agent-plugin) | Provides recognize CommandCode (cmd) as an agent, idle/working/blocked detection via screen manifest + cmd mod. |
| [**itsmistermoon/bindr**](https://github.com/itsmistermoon/bindr) | Switches between named keybinding profiles and viewing/editing keybinds in a popup. |
| [**jtnovellis/herdr-worktree-setup**](https://github.com/jtnovellis/herdr-worktree-setup) | Provides make a new git worktree immediately usable, copy .env & dev state, clone dependency caches (APFS/reflink), mise trust, direnv allow, install deps, with a live TUI. |
| [**im-tabr/herdr-command-center**](https://github.com/im-tabr/herdr-command-center) | Provides Animated Herdr command center for monitoring workspaces and agent jobs. |
| [**ivorpad/herdr-notify**](https://github.com/ivorpad/herdr-notify) | Provides know when an agent needs you or finishes, and queue messages agents cannot receive yet. |
| [**ThbltLmr/herdr-omarchy-widget**](https://github.com/ThbltLmr/herdr-omarchy-widget) | Provides a native Omarchy Quattro bar widget for local Herdr agent status and terminal focus. |
| [**ChrisPachulski/session-sounds**](https://github.com/ChrisPachulski/session-sounds) | Provides Distinct per-agent completion and attention sounds for Herdr on macOS and Linux. |
| [**perlporter/herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin) | Shows a toast in herdr when the currently playing track changes in Apple Music (macOS). |
| [**scheron/herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep) | Provides a herdr plugin that puts your Mac to sleep once no coding agent is working any more. Arm it before bed and it waits for every agent to settle, then journals what each one was doing, including the ones that ended up blocked. |
| [**buldezir/Herdglass**](https://github.com/buldezir/Herdglass) | Provides a native macOS GUI client for remote Herdr servers with a GPU-accelerated terminal and session status drawer. |
| [**openalon-org/herdr-bar**](https://github.com/openalon-org/herdr-bar) | Provides macos menu bar for Herdr. Live agent counts. |
| [**peterwiebe/herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention) | Jumps to the most recent blocked or finished agent. |
| [**kuwa72/herdr-focus-attention**](https://github.com/kuwa72/herdr-focus-attention) | Provides cycle through agents needing attention. |
| [**limars874/herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata) | Provides a minimal Herdr plugin for canonical pane IDs and compact tab/pane sidebar metadata. |
| [**martin-ro/herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent) | Jumps to the next agent needing attention, ranked by a configurable status priority. |
| [**wicolian/dev-on-call**](https://github.com/wicolian/dev-on-call) | Provides a quiet, local-first macOS menu-bar sentry for developers and their coding agents. |
| [**mphaxise/omarchy-keepalive**](https://github.com/mphaxise/omarchy-keepalive) | Provides Keepalive: coding agents that stay running on your Omarchy desktop. Named sessions on top of Herdr, with a bar panel, notifications, receipts, and permission modes. |
| [**alexanderop/prefix-dojo**](https://github.com/alexanderop/prefix-dojo) | Provides Interactive tmux and Herdr course in a simulated terminal. |
| [**WorksOnMyVM/herdr-sounds**](https://github.com/WorksOnMyVM/herdr-sounds) | Provides an open-source sound pack manager for Herdr: discover, preview, install, and switch notification sounds. |
| [**zhaoyuheng200/tmux-agent-herd**](https://github.com/zhaoyuheng200/tmux-agent-herd) | Provides tmux plugin: detect coding-agent status (working/blocked/idle) per pane, notify on blocked, jump between agents. Detection ported from herdr. |
| [**gridness/herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds) | Provides play random notification sounds per agent status in herdr on macOS. |
| [**Tresnanda/mustr**](https://github.com/Tresnanda/mustr) | Provides Mustr: a native macOS desktop client for herdr, the terminal runtime for AI coding agents. |
| [**ntheanh201/herdr-notify**](https://github.com/ntheanh201/herdr-notify) | Provides a native macOS notifications for Herdr, real app identity, custom emoji icon, and click a banner to focus the pane that fired it. |
| [**david-rzepa/omarchy-herdr-workspaces**](https://github.com/david-rzepa/omarchy-herdr-workspaces) | Provides Theme-accent Omarchy workspace indicators for unread Herdr agent activity, cleared by exact-tab focus. |
| [**benngarcia/herdr-macos**](https://github.com/benngarcia/herdr-macos) | Provides a native Herdr.app for macOS, built locally from Ghostty. |
| [**sandiiarov/tmux-agent-plugin**](https://github.com/sandiiarov/tmux-agent-plugin) | Provides tmux plugin for a Herdr-like AI agent sidebar. |
| [**Vercantez/herdr-voice**](https://github.com/Vercantez/herdr-voice) | Provides Private Herdr voice interface with an installable WebRTC PWA. |

### Push notifications, APNs, and mobile alerts

*2 projects. Direct mobile push notifications, Apple Push Notification service (APNs), and remote device alerts.*

| Project | What it does |
|---|---|
| [**ZingerLittleBee/Heeler**](https://github.com/ZingerLittleBee/Heeler) | Provides a native iOS agent console for Herdr with live SSH terminals, QR pairing, and push notifications. |
| [**WoodardDigital/herdr-remote**](https://github.com/WoodardDigital/herdr-remote) | Provides Integrated Herdr remote sessions. |

### Telemetry, events, and quota streaming

*18 projects. Event collectors and monitors for agent state, usage, cost, and runtime activity.*

| Project | What it does |
|---|---|
| [**DIodide/herdr-telemetry**](https://github.com/DIodide/herdr-telemetry) | Sends workspace and agent telemetry to an endpoint chosen by the user. It removes tokens, redacts sensitive prompts, and ships as a single binary. |
| [**second-state/vibetty**](https://github.com/second-state/vibetty) | Streams live Herdr terminal screens over MQTT to devices such as VibeKeys and VibeWatch and relays keystrokes back. It includes an MQTT broker and integrates with Herdr's command palette and status bar. |
| [**alejodelosrios/herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage) | Shows live Claude plan usage for both the current session and the weekly limit in the Herdr sidebar. It reads Claude Code's own authentication and status data rather than estimating usage. |
| [**amurru/herdr-whistle**](https://github.com/amurru/herdr-whistle) | Provides tools for monitoring and controlling agents across remote Herdr daemon instances. It streams lifecycle updates and sends commands without taking over the terminal session. |
| [**Javamomma/herdr-scribe**](https://github.com/Javamomma/herdr-scribe) | Streams microphone audio into temporary in-memory transcript and analysis panes. When recording ends, it creates structured meeting notes, policy checks, and draft task tickets without saving the raw audio. |
| [**kosuketut/herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder) | Downloads files created or changed in a remote Herdr pane to a local Mac. A plugin action detects paths in the active pane and transfers the selected artifact over the remote connection. |
| [**iamhouser/herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi) | Adds session and weekly Claude rate-limit gauges, color thresholds, and unblock countdowns to workspace rows. It supports several accounts by matching pane directories to profile folders without using tokens. |
| [**neospeed83/herdr-standup**](https://github.com/neospeed83/herdr-standup) | Provides Evidence-backed daily standups from Git activity and Herdr context. |
| [**1smil1/herdr-done-popup**](https://github.com/1smil1/herdr-done-popup) | Provides Persistent desktop popup when a Herdr AI agent finishes a task or asks a question. |
| [**DongHyunnn/ai-share-usage-herdr**](https://github.com/DongHyunnn/ai-share-usage-herdr) | Provides AI Share Usage: shared Codex quota tracking in the herdr terminal. |
| [**5qln/5qln-herdr-plugin**](https://github.com/5qln/5qln-herdr-plugin) | Provides the 4+1 cell as a Herdr instrument, sealed podium for human questions, and four agent desks. |
| [**ryus1234/provider-usage**](https://github.com/ryus1234/provider-usage) | Provides Provider usage and quota bar for Herdr. |
| [**neospeed83/herdr-replay**](https://github.com/neospeed83/herdr-replay) | Records and replay multi-agent Herdr coding sessions as interactive timelines. |
| [**CristianPeralta/herdr-aws-freetier-bar**](https://github.com/CristianPeralta/herdr-aws-freetier-bar) | Provides aws spend tripwire + per-service Free Tier quota usage, in a small persistent Herdr pane. |
| [**nabutabu/herdr-scribe**](https://github.com/nabutabu/herdr-scribe) | Provides Scribe for herdr. |
| [**harshad22491/herdr-agentpanel**](https://github.com/harshad22491/herdr-agentpanel) | Provides Self-healing AI-agent dashboard for Herdr terminal workspaces: every-tab agent catalogue with live quota coloring, auto-layout watcher, plain-English team status board. |
| [**FunnyQ/herdr-tab-bar-llm-quota**](https://github.com/FunnyQ/herdr-tab-bar-llm-quota) | Shows Claude and Codex quota in the herdr tab bar. |
| [**susumutomita/annai.term**](https://github.com/susumutomita/annai.term) | Provides Ask about your Ghostty and Herdr keybindings in plain language, answered on-device on your Mac. Swift-native, Apple Foundation Models, no cloud. |

### Voice, hardware, and remote bridges

*9 projects. Interfaces that connect Herdr to spoken input, physical devices, or remote control surfaces.*

| Project | What it does |
|---|---|
| [**razajamil/herdr-hex-browser-voice-command**](https://github.com/razajamil/herdr-hex-browser-voice-command) | A Chrome extension and local service that sends Hex voice transcripts to the correct Herdr pane based on the browser URL that was focused while speaking. URL patterns are mapped to workspace, tab, and pane targets. |
| [**aliaksandr-haurylau-godel/herdr-voice**](https://github.com/aliaksandr-haurylau-godel/herdr-voice) | Provides Voice dictation for herdr: hold a key, speak, and the text lands in your agent's input box, context-aware, with swappable speech and rewrite engines. |
| [**voice0726/herdr-jump-number**](https://github.com/voice0726/herdr-jump-number) | Displays jump-key numbers on workspaces and tabs without breaking Herdr's automatic workspace labels. |
| [**Aktrov/herdr-tts**](https://github.com/Aktrov/herdr-tts) | Speaks selected terminal text aloud using Piper neural text-to-speech engines with keyboard controls. |
| [**zbysir/herdr-web**](https://github.com/zbysir/herdr-web) | Provides an in-browser Herdr terminal and voice prompt interface accessible via mobile QR scanning. |
| [**RanolP/herdr-handsfree**](https://github.com/RanolP/herdr-handsfree) | Provides Hands-free herdr plugin: voice dictation (whisper.cpp) + webcam gaze mouse for macOS. |
| [**JinJieBeWater/herdling**](https://github.com/JinJieBeWater/herdling) | Provides macos menu bar companion for monitoring and opening local or SSH-hosted Herdr agents in Ghostty. |
| [**adamazad/remuda**](https://github.com/adamazad/remuda) | Provides One command opens a git worktree, starts a Claude session in a herdr pane, and hands it the task. |
| [**snowkiss13/herdr-habitat**](https://github.com/snowkiss13/herdr-habitat) | Provides Animated, local-first companion for monitoring AI coding agents in Herdr. |

### Protocol and third-party bridges

*50 projects. Adapters between Herdr and other multiplexers, platforms, messaging systems, or automation protocols.*

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
| [**Poor-Plebs/herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes) | Provides Work on other machines from one Herdr: pick a machine from a menu, get a terminal on it. Optional experimental two-way mirroring. |
| [**ardasevinc/herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge) | Provides a native Herdr pane identity for Codex sessions using a centralized app-server. |
| [**RaviTharuma/cmux-herdr**](https://github.com/RaviTharuma/cmux-herdr) | Provides cmux plugin for Herdr: live sidebar status pills, tab/pane mirroring, nested agents CLI. |
| [**luiscleto/weherd**](https://github.com/luiscleto/weherd) | Provides a playable Three.js office for local Herdr agents, with live terminals, coffee breaks, and a shotgun. |
| [**alex-devdone/herdr-hub**](https://github.com/alex-devdone/herdr-hub) | Describes a herdr session of remote-attach panes as a portable manifest, and rebuild it on any machine. |
| [**WorksOnMyVM/herdr-agent-bridge.nvim**](https://github.com/WorksOnMyVM/herdr-agent-bridge.nvim) | Provides a Neovim bridge for staging Sidekick-style editor context in Herdr-native agent panes. |
| [**hashrock/herdr-apc-mini**](https://github.com/hashrock/herdr-apc-mini) | Maps AKAI APC mini mk2 hardware controllers to physical Herdr agent controls. |
| [**codingfragments/herdr-flash**](https://github.com/codingfragments/herdr-flash) | Provides Port of zellij-flash (Zellij plugin) to run as a native Herdr plugin. |
| [**stefanahman/mux**](https://github.com/stefanahman/mux) | Provides Go drivers for the terminal multiplexers that hold coding agents: tmux, herdr, cmux. |
| [**sh1ftmaker/herdr-term**](https://github.com/sh1ftmaker/herdr-term) | Bridges Herdr sessions to browser interfaces with read-only file exploration and Hyprland desktop streaming. |
| [**BalajiLeninrajan/herdr-modes**](https://github.com/BalajiLeninrajan/herdr-modes) | Provides modal navigation for herdr. |
| [**szrenwei/herdr-traex**](https://github.com/szrenwei/herdr-traex) | Provides Herdr Marketplace integration for TraeX agent lifecycle and metadata. |
| [**carter2099/herdr-web-client**](https://github.com/carter2099/herdr-web-client) | Provides a self-hosted browser terminal attachment for Herdr. |
| [**CaptainVincent/herdr-agent-jump**](https://github.com/CaptainVincent/herdr-agent-jump) | Provides Fast EasyMotion-style, cross-workspace Agent jumping for Herdr. |
| [**smanickam01/herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin) | Provides Atuin shell history search in a herdr popup, press prefix+a, Enter to run or Tab to edit. Binds itself on install. |
| [**OSHEThai/HerdrOps**](https://github.com/OSHEThai/HerdrOps) | Monitors desktop operations for Herdr terminal agents on Windows. |
| [**sgnilreutr/herdr-vibe-integration**](https://github.com/sgnilreutr/herdr-vibe-integration) | Provides Herdr integration adapter for Mistral Vibe. |
| [**kody-w/rapp-omarchy**](https://github.com/kody-w/rapp-omarchy) | Provides Standalone Omarchy workbench with Herdr, Tailscale, and native RAPP Projects/Workspace. |
| [**linvald/herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer) | Syncs cmux's file viewer to the currently focused herdr space. |
| [**GladioFeng/herdr-ghostty-title-bridge**](https://github.com/GladioFeng/herdr-ghostty-title-bridge) | Provides Detailed per-agent Ghostty titles for Herdr with one watcher per server socket. |
| [**ShinoharaHaruna/mimo-code-herdr**](https://github.com/ShinoharaHaruna/mimo-code-herdr) | Provides MiMo Code <-> herdr custom-agent bridge: lifecycle state in the sidebar, crash-proof exit cleanup, one-command spawn. |
| [**agneym/herdr-lfm-finetune**](https://github.com/agneym/herdr-lfm-finetune) | Provides Fine-tune a LFM 350M model into a Herdr terminal-multiplexer expert (LoRA adapter + Colab training notebook). |
| [**timofey-TK/herdr-yazi-agent**](https://github.com/timofey-TK/herdr-yazi-agent) | Picks files in Yazi, get their paths in your agent's prompt. |
| [**wg1k/live-sync-panes**](https://github.com/wg1k/live-sync-panes) | Provides broadcast a command, or live-sync keystrokes, to every pane in a tab. |
| [**tenequm/build-workflow**](https://github.com/tenequm/build-workflow) | Provides Bernstein + herdr build workflow: skills, herdr adapter, gates, templates. |
| [**finna/omarchy-herdr-hud**](https://github.com/finna/omarchy-herdr-hud) | Monitors and prompt Herdr agents from a draggable Omarchy overlay, without leaving your game. |
| [**baileyrosen3/omarchy-terminals**](https://github.com/baileyrosen3/omarchy-terminals) | Provides Omarchy bar widget for managing Zellij, tmux, and herdr terminal sessions. |
| [**tmcinerney/beckon**](https://github.com/tmcinerney/beckon) | Provides Glove80 status display and Herdr pane navigation. |
| [**OneNoted/zeshion**](https://github.com/OneNoted/zeshion) | Provides Session manager for herdr, tmux and Zellij. |
| [**victor-falcon/git-worktree**](https://github.com/victor-falcon/git-worktree) | Provides Small zsh helper to create and delete Git worktrees, with optional tab automation for Herdr, Zellij and Muxy. |
| [**Gol-D-Rogger/herdr-code-server-clipboard**](https://github.com/Gol-D-Rogger/herdr-code-server-clipboard) | Forwards Herdr selections to the code-server browser clipboard on macOS. |
| [**PolyphonyRequiem/omp-herdr-bridge**](https://github.com/PolyphonyRequiem/omp-herdr-bridge) | Provides Portable rich OMP and Herdr integration. |
| [**mholtzscher/herdr-focus-or-tab**](https://github.com/mholtzscher/herdr-focus-or-tab) | Provides Cycle through Herdr panes across tab boundaries. |
| [**tumf/conflux-herdr**](https://github.com/tumf/conflux-herdr) | Provides Herdr plugin pane for running the Conflux TUI and reporting its lifecycle state. |
| [**smeltery/mav**](https://github.com/smeltery/mav) | Integrates Zed, Herdr, and cmux into a unified agent coding workbench. |
| [**nkwork9999/ayatsumugi**](https://github.com/nkwork9999/ayatsumugi) | Provides Local-first React DOM, Fiber, and state graph visualization for Ayatori and Tsumugi. |
| [**black-atom-industries/herdr**](https://github.com/black-atom-industries/herdr) | Provides the Black Atom adapter for Herdr agent orchestration. |
| [**opencharly/pod-herdr**](https://github.com/opencharly/pod-herdr) | Provides the herdr stack box (herdr.dev terminal multiplexer) + the check-herdr-pod R10 bed; herdr candy = pinned binary, supervised server, TCP socket bridge for the herdr: verb / charly herdr CLI. |
| [**FrancoEscob/mc-agent-deck**](https://github.com/FrancoEscob/mc-agent-deck) | Provides Client-only Minecraft Control Deck for local AI agents (herdr/WSL bridge). |

---

## 3. Editor integrations

*121 projects. Bridges and pane synchronizers that let you drive Herdr agents directly from your code editor.*

### Neovim navigation and splits

*43 projects. Plugins that make movement between Neovim windows and Herdr panes feel continuous.*

| Project | What it does |
|---|---|
| [**paulbkim-dev/vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation) | Ports vim-tmux-navigator behavior to Herdr. Direction keys move within Vim or Neovim until an edge is reached, then shift focus to the adjacent Herdr pane based on the pane's foreground process. |
| [**lmilojevicc/herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim) | Bridges Neovim split navigation and smart pane resizing with Herdr terminal panes. |
| [**chmarax/herdr-nvim**](https://github.com/chmarax/herdr-nvim) | A Neovim bridge with a Rust core and Lua configuration for inspecting Herdr panes, starting agent sessions, and sending editor selections to active panes. |
| [**aimdevlee/herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav) | Provides shared `Ctrl+h/j/k/l` navigation between Neovim splits and Herdr panes using socket-based focus tracking. |
| [**nettlesh/dotfiles**](https://github.com/nettlesh/dotfiles) | Personal Alacritty, Fish, Herdr, and Neovim dotfiles with workspace navigation and agent-dispatch configuration. |
| [**devxplay/herdr.nvim**](https://github.com/devxplay/herdr.nvim) | Provides direct directional split navigation (Ctrl+h/j/k/l) between Neovim and Herdr panes. |
| [**makyinmars/herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim) | A two-pane Neovim composer that turns selections, cursor positions, and file details into structured Markdown context for a Herdr agent. The prompt is staged for review rather than submitted automatically. |
| [**mcuste/herdr-context.nvim**](https://github.com/mcuste/herdr-context.nvim) | Sends the current Neovim buffer, open buffers, or a Visual selection to a Herdr coding agent as a correctly formatted file reference. It targets one workspace agent automatically or opens a fuzzy picker when several agents are in the tab or workspace. |
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
| [**solidsnakedev/herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools) | Provides Vim-aware pane navigation, aerospace-style pane moves and tmux-style rotation for herdr. |
| [**KoalaVim/herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware) | Provides Nvim-aware keybindings for herdr: navigation, splits, close, zoom. |
| [**qapquiz/herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick) | Provides Toggleable sidekick AI-agent pane for Herdr, paste code selections into the agent's composer without submitting. Pairs with qapquiz/herdr-sidekick.nvim. |
| [**JacquesvanWyk/herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys) | Provides Fuzzy-searchable keybinding cheatsheet for herdr (packs, discovery, personal overrides). |
| [**luneth90/keycade**](https://github.com/luneth90/keycade) | Provides a shortcut recall arcade for Omarchy, herdr, tmux, Vim, Neovim and LazyVim, six cabinets, each with its own deck, progress and mastery. |
| [**LiroRod/promptr**](https://github.com/LiroRod/promptr) | Provides a really small herdr plugin that integrates nvim with the multiplexer. |
| [**promptegrity/grok-themes**](https://github.com/promptegrity/grok-themes) | Provides Grok Night/Day themes for Ghostty, Nushell, Herdr, Neovim and Starship (from xai-org/grok-build). |
| [**Osmait/agentline.nvim**](https://github.com/Osmait/agentline.nvim) | Sends Neovim selections and buffers to coding agents through herdr. |
| [**acrucetta/herdr-kanban**](https://github.com/acrucetta/herdr-kanban) | Provides a kanban board plugin for Herdr agent sessions. |
| [**webdavis/herdr-nvim-annotate-extension.nvim**](https://github.com/webdavis/herdr-nvim-annotate-extension.nvim) | Provides herdr-nvim extension: annotate the current line with its diagnostic and blame into the herdr-nvim comment store. |
| [**RaphaelManke/send-to-agent.nvim**](https://github.com/RaphaelManke/send-to-agent.nvim) | Sends visual selections and review comments from Neovim to active AI agent sessions in Herdr. |
| [**makyinmars/herdr-config**](https://github.com/makyinmars/herdr-config) | Provides Herdr config with tmux-style keybindings, Vim navigation, and Gruvbox Dark Hard. |

### Full Neovim-hosted workspaces

*16 projects. A deeper integration that uses Neovim as the main interface while Herdr owns the agent processes.*

| Project | What it does |
|---|---|
| [**MomePP/herd.nvim**](https://github.com/MomePP/herd.nvim) | Uses Neovim as the primary dashboard to launch, monitor, and control background Herdr agent sessions. |
| [**itisbryan/herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks) | Watches & review the current PR's CI in a pane; CI/merge status on sidebar rows. Go + Bubble Tea. |
| [**youguanxinqing/herdr-flash**](https://github.com/youguanxinqing/herdr-flash) | Provides flash.nvim-style search, select, and yank for Herdr panes. |
| [**xzedx/herdr-easyjump**](https://github.com/xzedx/herdr-easyjump) | Jumps to any space, agent, pane, or tab using EasyMotion-style hint labels in the Herdr sidebar. |
| [**solidsnakedev/herdr-jump**](https://github.com/solidsnakedev/herdr-jump) | Provides Fuzzy workspace, pane and tab pickers for herdr, plus a last-workspace toggle. |
| [**utahta/herdr-hop**](https://github.com/utahta/herdr-hop) | Provides hop to a repository, worktree or workspace from one popup. |
| [**aorumbayev/herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland) | Provides Hyprland inspired controls for herdr. |
| [**swheel33/herdr-dev-workflow**](https://github.com/swheel33/herdr-dev-workflow) | Provides Portable Herdr plugin for managed Git worktrees and development tools. |
| [**lmilojevicc/herdr-last**](https://github.com/lmilojevicc/herdr-last) | Provides Toggle back to the previously active workspace or tab in Herdr. |
| [**CowboyVang/herdr-which-key**](https://github.com/CowboyVang/herdr-which-key) | Provides a which-key-style keymap overlay for herdr. Press one key, see every binding under your prefix grouped and labelled, press a second key to run it. |
| [**hadeson/herdr-harpoon**](https://github.com/hadeson/herdr-harpoon) | Provides Harpoon-style pane marks for herdr: pin panes to slots 1-9 and jump straight to them, across tabs and workspaces. |
| [**lmilojevicc/herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename) | Renames each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. |
| [**raymondware/herdr.nvim**](https://github.com/raymondware/herdr.nvim) | Provides Floating terminal and agent-state visibility for herdr, the agent multiplexer: status float, lualine component, background polling. |
| [**lancodev/herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker) | Provides Split-style Laravel tinker REPL for herdr, editor beside live results, as a pane or popup. |
| [**benbrackenbury/herder-zsh-refresh**](https://github.com/benbrackenbury/herder-zsh-refresh) | Provides exec zsh in every idle zsh pane. |
| [**romerramos/herdr-reviewr-nvim**](https://github.com/romerramos/herdr-reviewr-nvim) | Opens Reviewr files in the Neovim pane for the current HERDR workspace. |

### VS Code, Cursor, and dev containers

*22 projects. Extensions and environment setups for graphical editors and container-based development.*

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
| [**ismaelosuna7824/herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer) | Provides a keyboard-driven file explorer, code viewer, and Git client in a single Herdr pane using Bubble Tea. |
| [**maedana/herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode) | Provides Vim-style normal mode for the herdr sidebar: j/k rows, h/l tabs, 0-9 panes. |
| [**codingfragments/herdr-nav**](https://github.com/codingfragments/herdr-nav) | Provides herdr Workspaces and pane navigation, modern version of herdr-navigation with better preview support and new workspace template handling. |
| [**barnuri/herdr-project-manager**](https://github.com/barnuri/herdr-project-manager) | Provides Project manager plugin for herdr, glob/manual project discovery, fuzzy picker, open as tab or workspace. |
| [**mrshll/herdr-container-agents**](https://github.com/mrshll/herdr-container-agents) | Detects coding agents running inside containers and report them as herdr agents. |
| [**itisvincent/herdr-agent-sessions**](https://github.com/itisvincent/herdr-agent-sessions) | Browses and resume on-disk agent sessions, including Orca-managed Codex sessions. |
| [**Andreslvc/herdr_plugin**](https://github.com/Andreslvc/herdr_plugin) | Opens pane folder in VS Code, copy path, and open a folder as a space. |
| [**leoweigand/vsctask**](https://github.com/leoweigand/vsctask) | Runs VS Code tasks.json tasks outside VS Code, in a Herdr pane or a shell. |
| [**vonzelle-vzt/herdr-edit**](https://github.com/vonzelle-vzt/herdr-edit) | Provides Mouse-first terminal code editor with a real LSP client: diagnostics, autocomplete, hover, go-to-definition, rename, find-references and an outline. Plus a diff view, inline git blame, bookmarks and a command palette. |
| [**stevederico/herdr-plugins**](https://github.com/stevederico/herdr-plugins) | Provides Local herdr plugins (sidebar, git-badge, explorer). |
| [**niceview/mac-finder-quick-actions**](https://github.com/niceview/mac-finder-quick-actions) | Provides Finder quick actions to open files/folders in VS Code or a new herdr workspace, plus a toolbar droplet. |
| [**DcNiemandd/vscode-worktree**](https://github.com/DcNiemandd/vscode-worktree) | Manages git worktrees and their herdr agent sessions from a VS Code sidebar, no terminal needed. |
| [**islee23520/herdr-omo-agent**](https://github.com/islee23520/herdr-omo-agent) | Provides Register OmO sessions as Herdr coding agents. |

### Vim, Kakoune, and other editors

*17 projects. Navigation and workflow integrations for editors outside Neovim and VS Code.*

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
| [**roman/herdr.el**](https://github.com/roman/herdr.el) | Provides an Emacs porcelain interface for managing Herdr workspaces and agent sessions. |
| [**lancodev/herdr-jump**](https://github.com/lancodev/herdr-jump) | Provides a two-pane fuzzy switcher for herdr workspaces and agents, with vim keys. |
| [**asumaran/herdr-confirm-close**](https://github.com/asumaran/herdr-confirm-close) | Provides close the focused pane, asking first only when a process is running in it. |
| [**vigneshwerv/herdr-golden-ratio**](https://github.com/vigneshwerv/herdr-golden-ratio) | Provides Resize the focused Herdr pane to the golden ratio (~61.8%). |
| [**codingquark/herdr-modus-themes**](https://github.com/codingquark/herdr-modus-themes) | Provides Installable Modus Operandi and Modus Vivendi palettes for Herdr, with optional Modus-only Omarchy integration. |
| [**artieeez/herdr-which-key**](https://github.com/artieeez/herdr-which-key) | Provides which-key/leader-key menu engine for Herdr, prefix + space, then one mnemonic letter per group (lazy.vim style). |

### REPL and code dispatchers

*21 projects. Tools for sending code or commands from an editor to a running pane or interactive session.*

| Project | What it does |
|---|---|
| [**AbhijithAnirudhan2907/herdr-sidebar**](https://github.com/AbhijithAnirudhan2907/herdr-sidebar) | A fork of herdr-sidebar that adds an editor inside the pane, including save, syntax highlighting, undo and redo, and find and replace. |
| [**plannotator/herdr-annotate**](https://github.com/plannotator/herdr-annotate) | Annotates terminal text, reviews documents and agent replies in Herdr, and returns feedback directly to the running agent. |
| [**thewtex/herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load) | Provides CPU, memory, and load average monitor for herdr. |
| [**enekos/herdr-quick-actions**](https://github.com/enekos/herdr-quick-actions) | Provides fzf picker for herdr's native tab/pane/workspace actions, ranked by usage, stop memorizing keybindings. |
| [**chasereyn/Vincent**](https://github.com/chasereyn/Vincent) | Provides a mouse-first terminal client for reviewing code that AI agents wrote, and fixing it in place. |
| [**bonkey/herdr-pr-emoji**](https://github.com/bonkey/herdr-pr-emoji) | Provides one emoji per sidebar row with the branch's PR state; only-optional-checks-failing still reads as mergeable. |
| [**asermax/herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace) | Suspends a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker). |
| [**followbl/herdr-drover**](https://github.com/followbl/herdr-drover) | Provides Cattle-dog tab switcher for Herdr: hold Super+T to cycle, release to land. |
| [**husniadil/herdr-mail**](https://github.com/husniadil/herdr-mail) | Provides Async mail between coding agents on Herdr - a store-authoritative mailbox, a one-line pane marker as the hint, and ask/reply with a tracked obligation, in one Go binary. |
| [**mdetweil/herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask) | Provides Lazytask in a herdr split pane (open/focus/toggle) plus Taskwarrior quick actions. |
| [**brenzim/herdr-db**](https://github.com/brenzim/herdr-db) | Provides a Herdr plugin that wraps lazysql and provides connection discovery for your current project. |
| [**nathnael-desta/herdr-project-sessions**](https://github.com/nathnael-desta/herdr-project-sessions) | Provides browsing Git projects, worktrees, live agent panes, and historical OpenCode sessions in one keyboard-driven overlay. |
| [**jomarmontuya/herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer) | Provides Right-side Herdr file tree plugin with file tabs, cwd following, git decorations, and clickable links. |
| [**0xthc/herdr-plugin-worktree-bootstrap**](https://github.com/0xthc/herdr-plugin-worktree-bootstrap) | Provides Seed new herdr worktrees with .env files and nodemodules the moment they open. |
| [**sf1tzp/herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher) | Provides Workflow Ergonomics for Split Panes in Herdr. |
| [**y4m3/herdr-zen**](https://github.com/y4m3/herdr-zen) | Provides Zen mode for Herdr with an adjustable centered pane width. |
| [**jerryfane/herdrup**](https://github.com/jerryfane/herdrup) | Provides ios herdr client, a herdr client that contains a terminal (design: jerryfane/herdr#28). |
| [**cheunglok97/close-guard**](https://github.com/cheunglok97/close-guard) | Provides confirm before closing tab/pane, like tmux confirm-before. |
| [**asumaran/herdr-demokit**](https://github.com/asumaran/herdr-demokit) | Records the README demo GIFs of herdr plugins (asciinema + agg, scripted against an isolated herdr session). |
| [**scaryrawr/herdr.fish**](https://github.com/scaryrawr/herdr.fish) | Provides herdr auto start wrapper. |
| [**willfish/mux**](https://github.com/willfish/mux) | Provides Fast, dependency-free tmuxinator replacement for tmux and Herdr. |

### Editor plugins and bridges

*2 projects. General-purpose bridges that synchronize editor state with Herdr panes and agents.*

| Project | What it does |
|---|---|
| [**Daniel-Steinberger/obsidian-herdr**](https://github.com/Daniel-Steinberger/obsidian-herdr) | Sends the next unchecked Markdown task to an agent in the matching Herdr workspace and marks it complete when the agent finishes. Continuous mode can process an entire checklist. |
| [**aclima01/herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows) | A small Windows text editor that opens in a Herdr split, with a directory tree, syntax highlighting, and an uncommitted-diff tab. Files can be edited and staged without leaving the multiplexer. |

---

## 4. Switch and restore sessions

*175 projects. Fuzzy switchers, state managers, and layout restoration tools for organizing agent workspaces.*

### Fuzzy session switchers and terminal pickers

*130 projects. Interactive pickers for finding and focusing workspaces, tabs, panes, agents, or projects.*

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
| [**dmnkf/herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch) | Provides Fast local search and navigation for Herdr workspaces, panes, and archived agent sessions. |
| [**mcuste/herdr-workspacer**](https://github.com/mcuste/herdr-workspacer) | Provides Find projects with zoxide, then switch or create Herdr workspaces. |
| [**TawfiqAbubaker/scoopr**](https://github.com/TawfiqAbubaker/scoopr) | Copies anything to the terminal without using the mouse, inspired by extrakto for tmux. |
| [**arvmaan/herdr-glance**](https://github.com/arvmaan/herdr-glance) | Provides desktop widget to view the status of your agents. |
| [**catoncat/herdr-trail**](https://github.com/catoncat/herdr-trail) | Provides Herd-wide shared memos for herdr: agents jot follow-ups, humans manage one global list, every entry jumps back to its source conversation. |
| [**shadowfax92/herdr-beacon**](https://github.com/shadowfax92/herdr-beacon) | Jumps to the newest unread agent in Herdr. |
| [**andrewbrannan/herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs) | Tracks workspace GitHub pull requests. |
| [**black-atom-industries/helm.herdr**](https://github.com/black-atom-industries/helm.herdr) | Jumps to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator. |
| [**agentience/herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump) | Provides Get back to your IDE: raise the editor window for the focused pane's project, or pick one from a filterable popup. A Herdr plugin. |
| [**iamgp/herdr-overview**](https://github.com/iamgp/herdr-overview) | Provides a Mission Control tiled overview of every active Herdr workspace. |
| [**rcosteira79/herdr-readpending**](https://github.com/rcosteira79/herdr-readpending) | Marks agents you haven't finished reading. Numbered badge ($read) + a reorderable list pane. |
| [**mike-bronner/herdr-plugin-project-finder**](https://github.com/mike-bronner/herdr-plugin-project-finder) | Provides fuzzy-pick git repos and open them as workspaces. |
| [**ayumu-1212/herdr-pasture**](https://github.com/ayumu-1212/herdr-pasture) | Groups agents by repository and docks them on the left of every Herdr tab. |
| [**RooseveltAdvisors/herdr-extractor**](https://github.com/RooseveltAdvisors/herdr-extractor) | Provides extrakto-inspired visible-buffer token extraction for Herdr. |
| [**danieljvdm/herdr-composer**](https://github.com/danieljvdm/herdr-composer) | Provides Compose tasks, attach context, and launch coding agents in isolated Herdr workspaces. |
| [**youguanxinqing/herdr-hop**](https://github.com/youguanxinqing/herdr-hop) | Jumps to any visible Herdr pane by pressing a labeled key. |
| [**bshearrer/herdr-project-filter**](https://github.com/bshearrer/herdr-project-filter) | Provides Scope herdr's Agents sidebar to one git repository at a time. |
| [**zackshen/herdr-telescope**](https://github.com/zackshen/herdr-telescope) | Provides fzf command telescope for herdr: native actions, plugin actions, file finder (@), and live ripgrep search (/). |
| [**KadenThomp36/herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher) | Provides Hold Ctrl, tap Tab to cycle herdr panes MRU-style. Arc/Zen-style pane switcher for herdr on macOS. |
| [**fraction12/herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog) | Opens Rainfrog in a managed HerdR pane. |
| [**iamfozzy/herdr-stu**](https://github.com/iamfozzy/herdr-stu) | Opens pull requests and remote branches as worktrees, bootstraps them per project, and monitors agent CI states. |
| [**tkuchiki/herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context) | Opens Herdr tabs with isolated Kubernetes contexts and namespaces. |
| [**softwarecrafts/herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new) | Provides Resume or start an agent session in the herdr workspace for this project, a herdr plugin, and a CLI for terminals outside herdr. |
| [**WillowMist/herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden) | Provides Fuzzy-search your Bitwarden vault and paste/copy credentials, a herdr port of tmux-bitwarden. |
| [**gustavocaiano/herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher) | Provides Experimental macOS desktop switcher for Herdr. |
| [**0xthc/herdr-plugin-pr-board**](https://github.com/0xthc/herdr-plugin-pr-board) | Provides GitHub PRs for the current repo inside herdr: browse them in a pane, check one out as a worktree workspace, and safely collect merged ones. |
| [**cesarferreira/herdr-palette**](https://github.com/cesarferreira/herdr-palette) | Provides Popup command palette for Herdr. |
| [**p47t/herdr-sort-workspaces**](https://github.com/p47t/herdr-sort-workspaces) | Provides Herdr Workspace Sorter plugin in modern C++23 with FTXUI and CLI11. |
| [**jimididit/herdr-open-editor**](https://github.com/jimididit/herdr-open-editor) | Provides Fuzzy-pick a file with fzf and open it in your configured editor. |
| [**kaar/herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url) | Fuzzy-finds and open URLs from your herdr pane scrollback, a port of tmux-fzf-url. |
| [**AlexanderMakarov/herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview) | Provides highligh visible file/folder paths on hotkey and open them in file-viewer. Works in agents and terminal. |
| [**hitaishi2222/herdr-fingers**](https://github.com/hitaishi2222/herdr-fingers) | Provides a smart overlay to pick and copy information from the current pane to the clipboard. |
| [**rokrdev/herdr-quick-jump**](https://github.com/rokrdev/herdr-quick-jump) | Provides Inline-label pane picker for Herdr with configurable width. |
| [**yojahny55/herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups) | Provides group Spaces into named, colored groups, picker popup (mouse + keyboard), sidebar group headers, automatic ordering. |
| [**agustinvalencia/herdr-jump**](https://github.com/agustinvalencia/herdr-jump) | Provides Separate overlay pickers for herdr spaces and agents, jump to any workspace or agent, with live status colours. |
| [**willian/herdr-fzf-url**](https://github.com/willian/herdr-fzf-url) | Picks URLs from the focused pane with fzf, then open or copy them. |
| [**cyperx84/herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump) | Focuses Herdr tab N by position from custom keybindings, splitting the number row between tabs and workspaces. |
| [**astwys/herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt) | Provides a Herdr plugin to send predefined prompts to an agent pane. |
| [**pedrobarco/herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus) | Provides tmux-style last-active pane/tab/workspace toggles for herdr, via a focus-event history daemon. |
| [**abrose/herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces) | Puts a number in front of every space in herdr's sidebar, matching the indexed switchworkspace shortcut. |
| [**KazBrekker1/herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr) | Provides Hasr, a goto-style popup switcher for Herdr to switch, rename, delete, and create agents, tabs, and spaces with real-time tracking. |
| [**trapple/herdr-focus**](https://github.com/trapple/herdr-focus) | Focuses the next blocked or completed agent pane and brings the terminal window to the front. |
| [**njpatel/omaherdr**](https://github.com/njpatel/omaherdr) | Provides herdr in the Omarchy bar. |
| [**willfish/herdr-workspacex**](https://github.com/willfish/herdr-workspacex) | Provides Rust-native fuzzy Herdr workspace switcher with zoxide-backed workspace creation. |
| [**inonprince/herdr-counting-sheep**](https://github.com/inonprince/herdr-counting-sheep) | Provides a live Space and Agent indexes for Herdr, with shortcuts for jumping to the last tab, Space, or Agent. |
| [**Tomatio13/herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar) | Provides herdr-gog-calendar is a Google Calendar integration plugin for herdr, a terminal workspace tool. |
| [**dev-shimada/lazyworktree**](https://github.com/dev-shimada/lazyworktree) | Provides a TUI for managing git worktrees, with optional herdr and GitHub integration. |
| [**joo-was-already-taken/herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab) | Switches to the previously focused tab. |
| [**hotnugs/herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time) | Provides Emoji for your Herdr spaces, agents and tabs. Inject some fun into your terminal. |
| [**OndrejDrapalik/worktree-management-skills**](https://github.com/OndrejDrapalik/worktree-management-skills) | Provides Worktree management skills: a wt CLI plus agent skills for creating, opening, removing, and sweeping git worktrees in herdr or tmux. |
| [**ofirgall/extrakto-herdr**](https://github.com/ofirgall/extrakto-herdr) | Provides Extract text tokens from herdr panes with fzf. Inspired by extrakto for tmux. |
| [**tp6gw94/herdr-jump**](https://github.com/tp6gw94/herdr-jump) | Provides Keyboard navigation for Herdr workspaces, tabs, panes, and agents. |
| [**josephschmitt/pj-herdr**](https://github.com/josephschmitt/pj-herdr) | Uses the PJ picker to open a new workspace. |
| [**ronly2460/herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover) | Moves Herdr panes between workspaces with an interactive arrow-key picker. |
| [**aneym/herdr-gcal**](https://github.com/aneym/herdr-gcal) | Provides Agenda-first Google Calendar panel for herdr (fzf-driven). |
| [**montagao/herdr-story**](https://github.com/montagao/herdr-story) | Provides a pixel-art office for Herdr agents, project progress, and revenue. |
| [**GoldenRegulus/herdr-web**](https://github.com/GoldenRegulus/herdr-web) | Provides a local browser terminal for Herdr sessions. |
| [**frankwiles/hterm**](https://github.com/frankwiles/hterm) | Provides Customized herdr workspace control system. |
| [**younesdahdouh/Hyprland-Keybind-manager**](https://github.com/younesdahdouh/Hyprland-Keybind-manager) | Provides Rebind Hyprland and Herdr keys by pressing them. No config editing, no collisions. |
| [**nicolegros/herdr-launcher**](https://github.com/nicolegros/herdr-launcher) | Provides a herdr plugin that provides a fuzzy directory picker for quickly creating or switching to workspaces. |
| [**benbrackenbury/open-project**](https://github.com/benbrackenbury/open-project) | Provides fuzzy-pick a project and open it as a workspace. |
| [**d4rken/herdr-mint-applet**](https://github.com/d4rken/herdr-mint-applet) | Displays Cinnamon desktop panel applets showing idle, busy, or blocked Herdr agent sessions. |
| [**MomePP/herdr-agent-tab**](https://github.com/MomePP/herdr-agent-tab) | Opens a coding agent in a new tab of the current herdr space, on the checkout or a fresh git worktree. |
| [**adams100111/omarchy-themed-devtools**](https://github.com/adams100111/omarchy-themed-devtools) | Provides Extend Omarchy's theming engine to the dev tools it doesn't cover, herdr, starship, lazygit, bat, fzf, eza, for every theme, not just one. |
| [**WuJiaoJue/dsh-herdr-site**](https://github.com/WuJiaoJue/dsh-herdr-site) | Reports dsh/cc-tui agent state (working/idle/blocked) to Herdr over the custom-integration protocol. |
| [**yuritada/numberer-manager**](https://github.com/yuritada/numberer-manager) | Provides a Herdr plugin that automatically prefixes workspace and tab labels with their current list position (e.g., 1: space and 1: tab). |
| [**elliotekj/herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion) | Jumps directly between Herdr panes. |
| [**codyhxyz/herdr-chrome-keys**](https://github.com/codyhxyz/herdr-chrome-keys) | Provides Chrome-style keybindings for herdr: cmd for workspaces, ctrl for tabs, prefix for panes. Includes the Ghostty profile that makes them reach herdr on macOS. |
| [**otavioschwanck/omarchy-quick-herdr**](https://github.com/otavioschwanck/omarchy-quick-herdr) | Provides Herdr agents in your Omarchy bar: how many are running, waiting on you, or idle. Across every machine you connect over SSH. |
| [**leonho/herdr-new-task**](https://github.com/leonho/herdr-new-task) | Provides one keystroke to pick a project dir and launch claude in a new tab, with noun-first tab labels. |
| [**tdi/herdr-recents**](https://github.com/tdi/herdr-recents) | Provides History of recently touched workspaces and worktrees, reopenable from a picker. |
| [**SirBrother/herdr-launcher**](https://github.com/SirBrother/herdr-launcher) | Provides Right-click a folder and open it in Herdr: jumps to the workspace matching that path, or creates one. Windows Explorer context menu, PowerShell only, no admin. |
| [**tim-kuntz/workspace-tools**](https://github.com/tim-kuntz/workspace-tools) | Manages herdr workspaces. |
| [**nicolasvasquez/herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace) | Provides quickly switching workspaces within a session or creating new ones from zoxide with an overlay fzf picker. |
| [**brianstarke/wt**](https://github.com/brianstarke/wt) | Provides git worktree manager with a slick TUI + herdr workspace integration (Go, bubbletea/lipgloss). |
| [**eszanon/omarchy-herdr**](https://github.com/eszanon/omarchy-herdr) | Shows Herdr coding agents in the Omarchy bar and flags the ones waiting on you. |
| [**lucasscariot/herdie**](https://github.com/lucasscariot/herdie) | Provides open-source Herdr client for iPhone and iPad with a portable Rust core. |
| [**barewalker/herdr-jump**](https://github.com/barewalker/herdr-jump) | Provides Fuzzy-jump to any pane across all Herdr workspaces in one key. |
| [**pavel-snyk/herdry**](https://github.com/pavel-snyk/herdry) | Jumps into your Herdr sessions from the macOS menu bar. |
| [**JacobStephens2/herdr-config**](https://github.com/JacobStephens2/herdr-config) | Provides Herdr terminal workspace manager configuration. |
| [**jvsteiner/herdr-plugins**](https://github.com/jvsteiner/herdr-plugins) | Provides Small herdr plugins: background dev servers, and a git branch picker. |
| [**kfujii-6jo/raycast-extensions**](https://github.com/kfujii-6jo/raycast-extensions) | Provides Raycast extension for herdr: jump to workspaces, agents and local git repositories. |
| [**dkarter/vellum**](https://github.com/dkarter/vellum) | Provides fast, customizable menu for terminal multiplexers (like herdr and tmux). |
| [**s-hiraoku/herdr-toolkit**](https://github.com/s-hiraoku/herdr-toolkit) | Provides herdr configuration & plugins toolkit, config.toml, dispatch plugin (local/worktree agent launcher), setup scripts. |

### Persistence, snapshots, and state restoration

*30 projects. Tools that record layouts and process context, then rebuild or resume them after a restart.*

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
| [**vishnutskumar/herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics) | Provides session efficiency analytics and realtime agent guidance, powered by memex history. |
| [**alkevintan/deepseek-counter-herdr**](https://github.com/alkevintan/deepseek-counter-herdr) | Provides DeepSeek API credit in the herdr statusline, top-up spent, balance left, and today's pace toward a level month. |
| [**lancodev/herdr-checkpoint**](https://github.com/lancodev/herdr-checkpoint) | Provides tmux-resurrect for herdr, save exact session checkpoints and restore them, closing anything not in the checkpoint. |
| [**DillonWall/herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers) | Provides Number herdr's agents panel to match focusagent (prefix+1.9). |
| [**matiasvillaverde/herdr-lumen**](https://github.com/matiasvillaverde/herdr-lumen) | Provides Local-first Lumen diff review and agent activity panel for Herdr. |
| [**jovylle/herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name) | Preserves terminal titles and session names across Herdr tab closes. |
| [**Slimydog21/herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm) | Provides the NixOS VM pane for herdr, boot, stop, watch, and ssh into your Hashimoto-style dev VM. Requires the nixos-vm kit. |
| [**hunter9x/herdr-logging**](https://github.com/hunter9x/herdr-logging) | Provides Easy logging and screen capturing for herdr. |
| [**filoozom/herdr-title**](https://github.com/filoozom/herdr-title) | Provides a Herdr plugin that shows the selected worktree and agent activity in your terminal tab title. |
| [**seascheng/herdr-gui**](https://github.com/seascheng/herdr-gui) | Provides a native macOS front end for herdr: agents, workspaces, remote server. |
| [**leonho/herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes) | Provides popup checklist to review and close panes sitting at an idle shell. |
| [**Dimon94/herdr-context-locator**](https://github.com/Dimon94/herdr-context-locator) | Copies a self-describing locator for a Herdr agent's canonical native session context. |
| [**42lizard/herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer) | Provides tmux-sessionizer style plugin for herdr. |
| [**maxart/uniterm-benchmark**](https://github.com/maxart/uniterm-benchmark) | Provides a reproducible benchmark for Uniterm, Herdr, and tmux with fair workloads and sanitized reports. |
| [**zac-dougo/copse**](https://github.com/zac-dougo/copse) | Provides Terminal view of Git worktrees, GitHub issues, and Wayfinder maps for Herdr. |
| [**ram4-dev/herdr-config**](https://github.com/ram4-dev/herdr-config) | Provides Reproducible Herdr setup with pinned plugins, portable keybindings, snapshots, and rollback. |
| [**aneym/cull**](https://github.com/aneym/cull) | Provides a native macOS menu bar compute monitor and process culler, with herdr session attribution. |
| [**851-labs/sheep**](https://github.com/851-labs/sheep) | Provides a native macOS client for Herdr. |
| [**PremModhaOfficial/sessionizer**](https://github.com/PremModhaOfficial/sessionizer) | Provides tmux-sessionizer UX for herdr, one static Go binary. |

### Workspace and multi-session management

*15 projects. Managers for creating, grouping, naming, attaching to, and cleaning up several sessions.*

| Project | What it does |
|---|---|
| [**third774/herdr-last-workspace**](https://github.com/third774/herdr-last-workspace) | Tracks workspace IDs and toggles between the current and previous workspace with one key. It remains correct after reordering and exits quietly if the earlier workspace was closed. |
| [**taxueseek/session-digger**](https://github.com/taxueseek/session-digger) | Indexes conversations from Claude Code, Codex, and other agents in SQLite FTS5. It also tracks token and cache data and creates local HTML reports for review. |
| [**den-tanui/herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide) | Uses zoxide's directory history when creating Herdr workspaces, tabs, and panes, making recent project paths quick to open. |
| [**douglascorrea/herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox) | A central inbox for Herdr agents that combines run time, workspace statistics, session titles, and unread state into one triage view. |
| [**to4iki/herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump) | Jumps to the next Herdr pane needing attention, prioritizing blocked agents before cycling through completed tasks. |
| [**dantehemerson/herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab) | Tracks tab focus history and returns to the previously active Herdr tab with one keystroke. |
| [**osamahbeig/herdr-grove**](https://github.com/osamahbeig/herdr-grove) | Displays projects and directories as a grouped tree in a Herdr popup and opens the selected workspace or folder by key or click. |
| [**oddurs/herdr-namesync**](https://github.com/oddurs/herdr-namesync) | Keeps workspace, tab, and agent names current as the work changes, reading the intent the coding agent already publishes as its terminal title. Applies a rename policy with debouncing, rate limits, and locks for names you set by hand, and runs without a model unless you configure an OpenAI-compatible endpoint for stale titles. |
| [**Codem0nky87/multi-session-ai-manager**](https://github.com/Codem0nky87/multi-session-ai-manager) | Provides AI Manager, a native iPad client for Herdr, the terminal agent manager, over plain SSH. |
| [**pasta-disaster/herdr-nook**](https://github.com/pasta-disaster/herdr-nook) | Provides Toggleable popup panel for herdr which persists the session across invocations. |
| [**olehsharov/herdr-imgpopup**](https://github.com/olehsharov/herdr-imgpopup) | Provides Zoomable image viewer for the Herdr terminal workspace manager. |
| [**simensollie/aw-watcher-herdr**](https://github.com/simensollie/aw-watcher-herdr) | Provides ActivityWatch watcher recording herdr workspace attention and concurrent agent activity (macOS). |
| [**ultrakorne/herdr-link-hints**](https://github.com/ultrakorne/herdr-link-hints) | Provides EasyMotion-style keyboard link hints for the herdr terminal workspace manager. |
| [**latest-debs/herdr-debian**](https://github.com/latest-debs/herdr-debian) | Provides herdr (agent multiplexer) .deb packages for Debian. |
| [**hodkovickybuh/herdr-colors**](https://github.com/hodkovickybuh/herdr-colors) | Provides herdr fork with a scannable sidebar: per-workspace colors, auto color by project, red = agent needs you. |

---

## 5. Worktrees and terminal experience

*500 projects. Git worktree automation, terminal navigation, status displays, HUDs, and developer environment tools.*

### Git worktree automation

*129 projects. Tools that create isolated branches and worktrees for agents, then connect them to Herdr workspaces or tabs.*

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
| [**MovieHolic-Plex/herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish) | Provides Herdr plugin. Make a wish and omo commits a PR. |
| [**tupton/herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include) | Provides Symlink or copy untracked files to git worktrees created by herdr. |
| [**yoyoyeti/multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin) | Provides multitrunk task workspaces. |
| [**mike-bronner/herdr-plugin-agentic-panes-layout**](https://github.com/mike-bronner/herdr-plugin-agentic-panes-layout) | Provides lay out a newly created worktree workspace with an agent and a shell. |
| [**duyet/herdr-desk**](https://github.com/duyet/herdr-desk) | Provides unattended repo maintenance. |
| [**alexkarpandrus/herdr-dock**](https://github.com/alexkarpandrus/herdr-dock) | Creates coordinated Herdr workspaces across multiple repositories. |
| [**chenyao0910/herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains) | Opens the active Herdr workspace or worktree in Rider, WebStorm, IntelliJ IDEA, or GoLand. |
| [**polidog/herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label) | Displays corresponding GitHub issue numbers and titles in Herdr workspace status lines. |
| [**BASHBOP/otito-herdr-plugin**](https://github.com/BASHBOP/otito-herdr-plugin) | Runs Otito context and deterministic merge evidence inside Herdr agent workspaces. |
| [**AgentTeamsRun/herdr**](https://github.com/AgentTeamsRun/herdr) | Provides Report herdr worktree lifecycle events to the AgentTeams registry. |
| [**jattento/herdr-multirepo**](https://github.com/jattento/herdr-multirepo) | Provides One feature branch across many repositories, in one Herdr workspace. |
| [**ivorpad/herdr-reap**](https://github.com/ivorpad/herdr-reap) | Provides every agent's lifecycle state, and one keystroke to close the finished ones. |
| [**woshahua/herdr-github-pr**](https://github.com/woshahua/herdr-github-pr) | Syncs GitHub PR status, checks, reviews, and comments. |
| [**maedana/herdr-whereami**](https://github.com/maedana/herdr-whereami) | Renames tabs and report a $gitref sidebar token from git repo/branch or directory name. |
| [**tamdogood/herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow) | Provides a Herdr action that prompts the focused agent to safely create or merge the current branch's pull request. |
| [**marcelormendes/drover**](https://github.com/marcelormendes/drover) | Provides an independent native workspace for Herdr-powered agents, terminals, worktrees, and live sessions. |
| [**choplin/herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity) | Provides Report each Herdr workspace's shared Git repository identity. |
| [**hermanvulkers/herdr-pr-status-plugin**](https://github.com/hermanvulkers/herdr-pr-status-plugin) | Shows each worktree's PR approvals, CI status, and mergeability as colored sidebar tokens. |
| [**gokay-ai/sheep**](https://github.com/gokay-ai/sheep) | Provides Undo for AI coding agents. Every agent turn becomes a restorable checkpoint. |
| [**nilm987521/herdr-load-worktree**](https://github.com/nilm987521/herdr-load-worktree) | Opens all existing repository Git worktrees as individual Herdr workspaces with one click. |
| [**ryonakae/zerdr**](https://github.com/ryonakae/zerdr) | Keeps Herdr and Zed workspaces in sync. |
| [**viko16/herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty) | Displays uncommitted Git file counts in each Herdr space. |
| [**txmed82/herdr-code-review**](https://github.com/txmed82/herdr-code-review) | Provides Structured AI code review plugin for Herdr. |
| [**goern/bead-workflow-skills**](https://github.com/goern/bead-workflow-skills) | Provides agent skills for bead-driven work sessions across Herdr workspaces and worktrees. |
| [**huahaimaker/herdr-mac**](https://github.com/huahaimaker/herdr-mac) | Provides Unofficial native macOS and Windows clients for Herdr, built with SwiftUI, AppKit and WinUI 3. |
| [**r-mulder/herdr-workspace-scripts-plugin**](https://github.com/r-mulder/herdr-workspace-scripts-plugin) | Provides Plugin to execute bash scripts on workspace hooks. |
| [**rewt/herdr-lanes**](https://github.com/rewt/herdr-lanes) | Provides Git worktree lanes for coding agents with Herdr workspaces and validated fast-forward promotion. |
| [**yuanying/herdr-tasks**](https://github.com/yuanying/herdr-tasks) | Supervises task execution from start to finish across Herdr workspaces and worktrees. |
| [**kellen-miller/herdr-intellij**](https://github.com/kellen-miller/herdr-intellij) | Provides IntelliJ command center for Herdr coding agents. |
| [**takeaship/herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard) | Provides a safety-focused Herdr plugin for tracking and cleaning up agent worktrees. |

### Workspace lifecycle and multi-repository tools

*4 projects. Higher-level utilities for starting, tracking, and removing workspaces that span one or more repositories.*

| Project | What it does |
|---|---|
| [**tomaszhanc/herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins) | A monorepo of Herdr plugins, each packaged in its own directory with a manifest and executable. |
| [**tyler-jewell/herdr-plugins**](https://github.com/tyler-jewell/herdr-plugins) | A standard-library-first monorepo of Herdr plugins written entirely in Rust. |
| [**shelken/herdr-plugins**](https://github.com/shelken/herdr-plugins) | A Herdr plugin monorepo that includes an auto-Pi launcher by area and a session picker. |
| [**paulrobello/par-herdr-plugins**](https://github.com/paulrobello/par-herdr-plugins) | A monorepo of custom Herdr plugins. The source catalog does not list the individual plugins. |

### Diff review and code inspection

*30 projects. Side-by-side git diff inspection and comment handoff tools for agent reviews.*

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
| [**filafb/pr-deep-review**](https://github.com/filafb/pr-deep-review) | Provides Deep PR review with coordinated Claude agents, presented as a navigable codebook, Herdr plugin and standalone CLI. |
| [**worldnine/akapen**](https://github.com/worldnine/akapen) | Enables line-by-line commenting on rendered Markdown documents in a TUI and sends review notes back to agents. |
| [**choplin/herdr-agent-metadata**](https://github.com/choplin/herdr-agent-metadata) | Shows when each Herdr agent's semantic state was last observed changing. |
| [**bonkey/herdr-link-browser**](https://github.com/bonkey/herdr-link-browser) | Provides Ctrl-click an http(s) URL to open it in terminal-browser as a split beside the pane. |
| [**timjonez/herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes) | Provides sticky notes on agents so you can see why one is idle. |
| [**VilfredSikker/easy-review**](https://github.com/VilfredSikker/easy-review) | Provides Git diff review for AI-assisted coding. Terminal TUI and Tauri desktop app. |
| [**0xfelixli/herdr-notes**](https://github.com/0xfelixli/herdr-notes) | Annotates selected terminal text in a Rust popup textbox, herdr plugin. |
| [**roman/herdr-meat-review**](https://github.com/roman/herdr-meat-review) | Provides Code reviews inside herdr. |
| [**choplin/herdr-plugins**](https://github.com/choplin/herdr-plugins) | Provides Focused plugins for Herdr terminal workflows. |

### File viewers and markdown previews

*20 projects. In-terminal file browsers, image previews, and markdown rendering panes.*

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
| [**u7chan/herdr-file-viewer**](https://github.com/u7chan/herdr-file-viewer) | Provides Read-only file viewer plugin for Herdr, a TUI built with Go and Bubble Tea. |

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

*105 projects. Custom keymap packs, leader-key setups, and prefix-free navigation.*

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
| [**vjeantet/herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad) | Docks a plain-text scratchpad at the bottom of a tab, one persistent buffer per tab, for composing a prompt where Enter can't send it half-finished. `Ctrl+E` moves it, or just the selection, into an agent of the same tab without submitting; `Ctrl+C` copies over OSC 52. |
| [**AltanS/herdr-pouch**](https://github.com/AltanS/herdr-pouch) | Provides stash prompts for an agent ahead of time and insert them when it's ready. |
| [**chrysa/herdr-rtk-savings**](https://github.com/chrysa/herdr-rtk-savings) | Provides RTK token-savings gauges in the herdr spaces sidebar. |
| [**RickyMarou/herdr-numbered-tabs**](https://github.com/RickyMarou/herdr-numbered-tabs) | Provides prefix every tab label with its current displayed position/shortcut number. |
| [**WillHeather/herdr-grid**](https://github.com/WillHeather/herdr-grid) | Provides Tile a herdr workspace's agent panes into a screen-sized grid, and put them back. |
| [**juezhong/herdr-positional-tabs**](https://github.com/juezhong/herdr-positional-tabs) | Provides a stable positional tab labels and Alt-number navigation for Herdr. |
| [**hassox/herdr-kanban**](https://github.com/hassox/herdr-kanban) | Provides Workspace panes as a kanban board. |
| [**edouard-andrei/herdr-smart-rename**](https://github.com/edouard-andrei/herdr-smart-rename) | Provides AI names for tabs and panes from agent transcripts, one keypress, any OpenAI-compatible model. |
| [**andischerer/herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo) | Provides broadcast keystrokes from one pane to multiple marked panes. |
| [**JoanGil/herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker) | Provides Mark/unmark the focused agent unread with a keybinding, manual only. |
| [**Blankeos/herdr-serve**](https://github.com/Blankeos/herdr-serve) | Provides Remotely use herdr agents anywhere, no plugin, just works. |
| [**goofansu/herdr-notebook**](https://github.com/goofansu/herdr-notebook) | Provides One permanent Markdown notebook per workspace, opened in your editor over the active pane. |
| [**htlcode/herdr-directory-bookmarks**](https://github.com/htlcode/herdr-directory-bookmarks) | Provides Save and Use Directory Bookmarks. |
| [**wenPKtalk/herdr-translate**](https://github.com/wenPKtalk/herdr-translate) | Provides translate the selected text in a pane with translate-shell, shown in a floating popup (macOS and Linux). |
| [**cndreisbach/herdr-gitu**](https://github.com/cndreisbach/herdr-gitu) | Provides gitu in a herdr split pane or tab, with toggle-to-close keybindings. |
| [**Hariketsu/modern-terminal-keybindings**](https://github.com/Hariketsu/modern-terminal-keybindings) | Provides Modern keyboard shortcuts for Kitty, fish, Herdr, and coding agents. |
| [**brant92good/terminal-workspace**](https://github.com/brant92good/terminal-workspace) | Opens a remote shell and its port forwards in Windows Terminal, with machine-aware shortcuts and optional local or remote Herdr. |
| [**poweroutlet2/herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane) | Provides a herdr plugin that asks for confirmation before closing a pane, like tmux's prefix+x confirm-before. |
| [**impeterwayne/herdr_launcher**](https://github.com/impeterwayne/herdr_launcher) | Provides Fast agent launcher for Herdr. |
| [**yuloop/herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move) | Moves and rearranges Herdr panes across tabs using keyboard shortcuts. |
| [**yashikota/copy-last**](https://github.com/yashikota/copy-last) | Copies the last prompt, command, and output. |
| [**juninaba/herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview) | Provides a Herdr plugin for previewing the current branch's GitHub pull request in a split pane. |
| [**mikedyan/herdrill**](https://github.com/mikedyan/herdrill) | Provides an aim trainer for your Herdr keybindings. 60 seconds to find out if they're muscle memory or wishful thinking. |
| [**karanmrn/karan-herdr-shortcut-setup**](https://github.com/karanmrn/karan-herdr-shortcut-setup) | Provides Mac terminal, shell, and agent setup: WezTerm, Ghostty, herdr, starship, FirstMate entry point. |

### Command palettes and workspace switchers

*26 projects. Searchable menus for Herdr commands, projects, workspaces, and common actions.*

| Project | What it does |
|---|---|
| [**TaylorFinklea/herdr-ask**](https://github.com/TaylorFinklea/herdr-ask) | Opens a popup to translate plain-English requests into shell commands, letting you review and insert them into the active pane with Ctrl+Enter. |
| [**fullerzz/herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh) | A sesh-style Herdr workspace picker with zoxide integration for creating workspaces from frequently used directories. |
| [**ramarivera/herdr-palette**](https://github.com/ramarivera/herdr-palette) | A Rust and Ratatui fuzzy command palette for Herdr workspaces. |
| [**vjeantet/herdr-palette**](https://github.com/vjeantet/herdr-palette) | Combines Herdr's built-in operations, every installed plugin's actions, user-defined commands, and reusable prompts in one fuzzy Rust/Ratatui palette. It preserves the originating pane context and asks for inputs, selections, or confirmation when an operation needs them. |
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
| [**chrisg32/tsk**](https://github.com/chrisg32/tsk) | Provides a plain-text task TUI in Rust that runs standalone or as an integrated Herdr plugin. |
| [**shantanugoel/herdr-auto-namer**](https://github.com/shantanugoel/herdr-auto-namer) | Provides Deterministic, LLM-free automatic names for Herdr panes and tabs. |
| [**tareqmlx/herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer) | Opens lazygit at the files, branches, commits, or stash panel, in whichever Herdr surface suits the moment. |
| [**jovylle/herdr-pane-mark**](https://github.com/jovylle/herdr-pane-mark) | Provides Herdr plugin, custom $mark under Agents via palette/popup (no fork). |
| [**gwelican/herdr-keybinds**](https://github.com/gwelican/herdr-keybinds) | Provides listing/searching all keybinds, including plugins. |
| [**natori-hrj/herdr-green**](https://github.com/natori-hrj/herdr-green) | Provides Per-agent test status for herdr, run a project's tests when its agent finishes and show pass/fail. |
| [**nertzy/herdr-flexoki**](https://github.com/nertzy/herdr-flexoki) | Provides Flexoki light and dark themes for Herdr, with automatic appearance switching. |
| [**maxBRT/herdr-omarchy-theme-sync**](https://github.com/maxBRT/herdr-omarchy-theme-sync) | Synchronizes Herdr's UI palette with the active Omarchy theme. |
| [**reobin/herdr-close-other-panes**](https://github.com/reobin/herdr-close-other-panes) | Closes every Herdr pane except the focused one using Vim-style ctrl-w o navigation. |
| [**sp-night/herdr**](https://github.com/sp-night/herdr) | Provides SP Night for Herdr, a dark colour scheme inspired by Sao Paulo. |
| [**matheuseabra/mbtop**](https://github.com/matheuseabra/mbtop) | Provides a tiny, minimal system monitor built to rendered as small herdr/tmux dashboard panes. |

### Status lines, sidebars, and tab synchronization

*109 projects. Persistent interface elements that show agent state, repository context, quotas, tasks, or synchronized tab information.*

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
| [**thuanlm215/herdr-grid**](https://github.com/thuanlm215/herdr-grid) | Opens a visual editor for dragging, resizing, and safely rearranging live pane layouts without restarting pane processes. It can add shell panes, apply fixed presets, or build a preset in a new workspace. |
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
| [**ferretorres/herdr-plugin-space-colors**](https://github.com/ferretorres/herdr-plugin-space-colors) | Gives each workspace a colour that follows the focused workspace across the Herdr theme, a marker on every agent row and Space row, the pane backgrounds, and the macOS terminal window and its title bar. Rules pin a colour to a path or label; unmatched workspaces are coloured from a hash of their directory. |
| [**kryptamine/herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title) | Updates Herdr tab titles automatically based on active workspace tasks to keep development contexts organized. |
| [**ythx-101/herdr-social-glass**](https://github.com/ythx-101/herdr-social-glass) | Provides Screenshot-friendly Social Glass theme and workflow plugin for Herdr on macOS. |
| [**Razz21/herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status) | Detects dev servers in panes via pluggable specs and reports lifecycle status. |
| [**MorganCollins/herdr-last-used**](https://github.com/MorganCollins/herdr-last-used) | Shows when each herdr agent was last active, colour-coded by age, and filter the Agent sidebar by activity. |
| [**btj93/herdr-tokens**](https://github.com/btj93/herdr-tokens) | Publishes workspace metadata tokens derived from agent status, so sidebar colours can vary by state. |
| [**ubuntudroid/herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack) | Shows each space's position in its git branch stack in the spaces sidebar, flags branches whose parent has moved, and keeps stacks contiguous. Local commit graph only, no network, no forge API, no stacking tool. |
| [**Anthodev/herdr-context**](https://github.com/Anthodev/herdr-context) | Provides Project context dock for herdr, file tree with git status and LLM conversation history, always at your agent's side. |
| [**Levi-Gillies/herdr-ssh-agents**](https://github.com/Levi-Gillies/herdr-ssh-agents) | Shows AI coding agents running over SSH in Herdr's sidebar. |
| [**MrMySQL/uherdr**](https://github.com/MrMySQL/uherdr) | Provides a native macOS client for herdr: workspaces, terminal panes, and coding agents. |
| [**GuillermoDSM/hypr-herdr**](https://github.com/GuillermoDSM/hypr-herdr) | Integrates Herdr spaces and panes with Omarchy and Hyprland. |
| [**jankeesvw/omarchy-herdr**](https://github.com/jankeesvw/omarchy-herdr) | Runs herdr servers in the Omarchy bar, with every agent inside them, and a click that lands you on the one you picked. |
| [**dm4/herdr-workspace-sidebar**](https://github.com/dm4/herdr-workspace-sidebar) | Provides a Herdr plugin for displaying workspace tabs in a flat list. |
| [**choplin/herdr-next-agent**](https://github.com/choplin/herdr-next-agent) | Moves between Herdr agents in configured semantic states. |
| [**Gareth-Rouse/herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) | Tracks workspace last-use, show the age in the Spaces sidebar, and keep cold workspaces out of the restored session. |
| [**abet-v/omarchy-herdr-prompt**](https://github.com/abet-v/omarchy-herdr-prompt) | Provides a centered prompt overlay that starts a fresh Claude agent in any Herdr workspace. |
| [**hasuwini77/herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git) | Provides Git branch and status in the Herdr Spaces sidebar that follow the active tab instead of the first one. |
| [**afokapu/herdr-workspace-agents**](https://github.com/afokapu/herdr-workspace-agents) | Provides a live workspace-scoped agent view for herdr, derived from events.subscribe, since herdr 0.7.4 has no server-side agent filter. |
| [**sfc-gh-tmeacham/coco-herdr-plugin**](https://github.com/sfc-gh-tmeacham/coco-herdr-plugin) | Provides Cortex Code plugin: live status in the Herdr sidebar with no Herdr source changes. |
| [**CowboyVang/herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges) | Provides Sidebar badge on herdr spaces that hold more than one tab. |
| [**mike-bronner/herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces) | Keeps the spaces sidebar in most-recently-used order. |
| [**jwbaldwin/herdr-auto-title**](https://github.com/jwbaldwin/herdr-auto-title) | Provides Herdr automatic tab titling. |
| [**Risingtides-dev/ocean-herdr**](https://github.com/Risingtides-dev/ocean-herdr) | Provides Ocean agent integration for Herdr. |
| [**JasonBates/agentdeck-rs**](https://github.com/JasonBates/agentdeck-rs) | Provides a local, model-enriched control surface for people running several coding agents at once. |
| [**lixenstrand/omarchy-herdr-drop**](https://github.com/lixenstrand/omarchy-herdr-drop) | Provides a persistent, theme-aware Herdr drop-down for Omarchy and Hyprland. |
| [**shimonacarvalho/herdr-github-status**](https://github.com/shimonacarvalho/herdr-github-status) | Provides a herdr plugin to show github status. |
| [**Newt6611/herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title) | Provides Herdr Tab Title automatically renames Herdr tabs with clean, workspace-local numbering like 1. Codex, 2. |
| [**yordanbuilds/rig**](https://github.com/yordanbuilds/rig) | Provides Project stacks for Herdr, an Omarchy shell plugin. One command and the whole workspace is up. |
| [**TheHatBoxGhost/herdr-paddocks**](https://github.com/TheHatBoxGhost/herdr-paddocks) | Provides WIP / early development. Omarchy bar widget to start, stop and switch between herdr project workspaces. |
| [**satoshi-hashimoto52/herdr-custom**](https://github.com/satoshi-hashimoto52/herdr-custom) | Extends Herdr with custom UI elements, status indicators, and resource usage displays. |
| [**tjcelaya/omarchy-modelctl**](https://github.com/tjcelaya/omarchy-modelctl) | Provides Omarchy bar plugin: on-demand local llama.cpp / stable-diffusion.cpp model control + live herdr agent list. |
| [**matt-shearing/omarchy-herdr**](https://github.com/matt-shearing/omarchy-herdr) | Provides a quiet, security-hardened Herdr companion for the Omarchy bar. |
| [**andreconde21/omarchy-herdr**](https://github.com/andreconde21/omarchy-herdr) | Monitors local and remote Herdr workspaces with native agent status inside the Omarchy top bar. |
| [**Edvardunsvag/herdr-sidebar**](https://github.com/Edvardunsvag/herdr-sidebar) | Provides Calm status board for a narrow right-hand Herdr pane: what is waiting for you, at a glance. |
| [**lixenstrand/omarchy-herdr-drop-plugin**](https://github.com/lixenstrand/omarchy-herdr-drop-plugin) | Provides Theme-aware Omarchy bar widget and live agent status for Herdr Drop. |
| [**Ra77a3l3-jar/herdnix**](https://github.com/Ra77a3l3-jar/herdnix) | Provides herdr plugins and configuration module in Nix. |
| [**shubham-cpp/herdr-plugins**](https://github.com/shubham-cpp/herdr-plugins) | Provides Herdr plugins for tab/agent naming and directional pane focus. |
| [**cxnmai/plexr**](https://github.com/cxnmai/plexr) | Provides tmux but tui version inspired by herdr. |

### Status overlays, HUDs, and agent timers

*24 projects. Floating status HUDs, turn timers, and keep-awake utilities.*

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
| [**parker-brown-family/omarchy-crook**](https://github.com/parker-brown-family/omarchy-crook) | Puts Herdr agent state on the Omarchy desktop bar: one icon that turns urgent when an agent is blocked, and a tray listing every agent grouped by whether it needs you. Clicking a row focuses that pane and raises the terminal window on Hyprland. |
| [**cupsadarius/herdr-pr-glance**](https://github.com/cupsadarius/herdr-pr-glance) | Provides the current branch's pull request, CI checks, reviews and stack at a glance. |
| [**aneym/herdr-routines**](https://github.com/aneym/herdr-routines) | Provides Scheduled-routine daemon and CLI for herdr. |
| [**sd2k/herdr-thumbs**](https://github.com/sd2k/herdr-thumbs) | Picks and copies on-screen text or URLs in Herdr using tmux-thumbs style hints. |
| [**JYasha11/herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report) | Keeps a permanent ledger of how long you've left your AI agents waiting. The sheep remember. |
| [**KokiKono/herdr-kanban**](https://github.com/KokiKono/herdr-kanban) | Provides Terminal Kanban board that links tasks to herdr tabs, persisted in SQLite. |
| [**goofansu/herdr-hunk**](https://github.com/goofansu/herdr-hunk) | Provides quick Herdr review actions that open a temporary Hunk overlay. Quitting Hunk closes the overlay and restores your workspace. |
| [**gbaeke/hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin) | Browses Azure resource groups and resources; click a resource to open it in the Azure portal. |
| [**nklmilojevic/herdr-flake**](https://github.com/nklmilojevic/herdr-flake) | Provides Nix flake packaging herdr from official release binaries. |

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

*18 projects. Tools for searching, cleaning, exporting, or reviewing pane output and agent conversations.*

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
| [**crierr/herdr-arrange**](https://github.com/crierr/herdr-arrange) | Provides Interactive popup UI for herdr pane move / swap / re-split / layout. |
| [**geshido/herdr-column-layout**](https://github.com/geshido/herdr-column-layout) | Provides wmii-inspired column-oriented pane management for Herdr. |
| [**jone/herdr-wrangler**](https://github.com/jone/herdr-wrangler) | Provides tmux-style pane layouts and rotation for herdr. |
| [**hexsprite/herdr-beads**](https://github.com/hexsprite/herdr-beads) | Provides Ctrl-click a beads issue ID in Herdr to open its details in a split pane. |
| [**calebcauthon/herdr-riff-relay**](https://github.com/calebcauthon/herdr-riff-relay) | Provides relay riff dictation directly into your agent. |
| [**iurysza/herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts) | Provides tmux-style pane resizing and layouts for Herdr. |
| [**georgedakoul/herdr-phone**](https://github.com/georgedakoul/herdr-phone) | Provides a phone-sized web view of the Herdr session on your desktop. |
| [**Cainiaooo/sessmark**](https://github.com/Cainiaooo/sessmark) | Provides Local session tags and notes for coding agents, with an optional HerdR plugin. |
| [**ralphilius/herdr-pr-tab-renamer**](https://github.com/ralphilius/herdr-pr-tab-renamer) | Renames tabs with detected pull request numbers. |

### Security guards and collision detectors

*4 projects. Safety monitors that warn of worktree collisions, credential leaks, or destructive edits.*

| Project | What it does |
|---|---|
| [**kedwards/herdr-awst**](https://github.com/kedwards/herdr-awst) | Provides AWST integration with herdr. |
| [**friendsfriend/agentic-coding**](https://github.com/friendsfriend/agentic-coding) | Provides My custom agentic coding workflow evolving around openspec and pi with a custom workflow engine and tui using herdr. |
| [**gw31415/herdr-git-parallel-worktrees-skill**](https://github.com/gw31415/herdr-git-parallel-worktrees-skill) | Provides Agent-neutral SKILL.md source for safe Herdr Git worktree allocation. |
| [**sangimed/firstmate-homelab**](https://github.com/sangimed/firstmate-homelab) | Provides a self-hosted Docker stack for Firstmate, Herdr and Codex agents. |

### Dotfiles and ready-made configuration

*6 projects. Complete or partial Herdr configurations that can be installed and adapted instead of written from zero.*

| Project | What it does |
|---|---|
| [**ogulcancelik/herdr-browser**](https://github.com/ogulcancelik/herdr-browser) | Renders an interactive Chromium browser inside a Herdr pane through the Kitty graphics protocol. Chrome DevTools Protocol support lets agents automate the browser while humans observe and intervene with keyboard or mouse. |
| [**multiplex-term/Multiplex**](https://github.com/multiplex-term/Multiplex) | An SSH, tmux, and Herdr terminal client for Apple Vision Pro and iPad. |
| [**ddfonseca/herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image) | Saves an image from the macOS or Linux clipboard to disk and pastes its file path into the active pane for use by multimodal agents. |
| [**crierr/herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout) | Adds tmux-style layout presets for Herdr, including even horizontal, even vertical, main horizontal, main vertical, tiled, cycle, and balance. |
| [**VinhLe1410/herdr-agent-priority**](https://github.com/VinhLe1410/herdr-agent-priority) | Configures how Herdr agent states are prioritized. |
| [**masatokawano/to-herdr**](https://github.com/masatokawano/to-herdr) | Configuration and notes for migrating a terminal setup from Zellij to Herdr. |

### Plugin collections and developer frameworks

*6 projects. Collections and scaffolding for discovering, creating, or maintaining several Herdr extensions.*

| Project | What it does |
|---|---|
| [**vonzelle-vzt/herdr-extensions**](https://github.com/vonzelle-vzt/herdr-extensions) | Installs a complete 13-panel developer environment inside Herdr for diagnostics, language-server completion, tests, and in-terminal agent diff review. |
| [**MIDO-ruby7/herdr-plugins-directory**](https://github.com/MIDO-ruby7/herdr-plugins-directory) | A directory of Herdr plugins organized by the task a user wants to accomplish. |
| [**Newt6611/herdr-plugin-rust**](https://github.com/Newt6611/herdr-plugin-rust) | Provides tools for developing Herdr plugins. |
| [**andybarilla/herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt) | Provides a herdr plugin that gives the agents in a herdr session a shared chat room. |
| [**spywhere/herdr-now-playing**](https://github.com/spywhere/herdr-now-playing) | Adds music player with music control through key bindings to herdr. |
| [**calebcauthon/herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye) | Provides a bird's-eye overview of active agents across Herdr panes. |

---

## 6. Apps, companion integrations, and installation

*185 projects. Native applications, web dashboards, hardware companions, supporting utilities, and setup packages.*

### Native desktop and mobile apps

*14 projects. Installed applications and launchers that provide a native interface to Herdr on desktop or mobile operating systems.*

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
| [**muhammedenesb100/herdrm**](https://github.com/muhammedenesb100/herdrm) | Manages every coding agent on your Mac and remote machines from one native terminal. |
| [**3loc/herden**](https://github.com/3loc/herden) | Provides Persistent coding-agent runtime with a native iOS console, built from herdr and Heeler, with secure pairing over SSH. |
| [**ralfkuh-lab/sheepdock**](https://github.com/ralfkuh-lab/sheepdock) | Provides a native macOS launcher that opens herdr in its own kitty window, with its own Dock icon. |

### Web dashboards and remote viewers

*22 projects. Browser-based monitors, remote controls, and visual scenes for following Herdr agents from another screen or device.*

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
| [**neyham/herdr-paddock**](https://github.com/neyham/herdr-paddock) | Shows every Herdr agent as a card in a scrollable waterfall feed over plain SSH, with blocked agents pinned to the top and cleaned pane output on each card. Runs standalone or as a Herdr plugin popup, responsive down to a 40-column phone terminal, with no relay or web server. |
| [**lntvan166/paddock**](https://github.com/lntvan166/paddock) | Groups Herdr agents into needs-you, working, and idle in a phone-sized web dashboard, and answers a blocked agent using the prompt's own option labels instead of a guessed keystroke. Ships as a single binary that speaks Herdr's socket protocol directly, installs to the iOS Home Screen as an app, and sends a Telegram alert once an agent's state has held. |
| [**4noha/herdr-drover**](https://github.com/4noha/herdr-drover) | Provides claude shim (auto-attach / new-Tab landing) + cloud sync via drover-cloud (web/phone viewing, near-$0). |
| [**riba2534/herdrx**](https://github.com/riba2534/herdrx) | Provides a self-hosted, multi-user Herdr remote terminal workbench with multi-host split panes, mobile access, and Tailscale support. |
| [**Eden-Sun/agents-manager**](https://github.com/Eden-Sun/agents-manager) | Manages multiple coding-agent CLIs running in Herdr panes via a Rust Axum daemon and React frontend. |
| [**hao-github-0216/remote-workspace-setup**](https://github.com/hao-github-0216/remote-workspace-setup) | Provides Cross-platform persistent remote terminal workspace (herdr + mosh/ssh). Survives lid-close, roaming, and reboot. |

### Hardware and ambient displays

*22 projects. Keypads, watches, desk devices, and compact displays that turn agent state into physical controls or at-a-glance signals.*

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
| [**jorge07RD/herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager) | Provides Save SSH hosts and reconnect from a fuzzy popup inside Herdr, Enter hands the popup straight to ssh. |
| [**johnendean/herdrkeys**](https://github.com/johnendean/herdrkeys) | Uses Pimoroni Keybow 2040 as a way of monitoring and switching between agents running in Herdr, inspired by the Codex Micro/Creator Micro2. |
| [**so1omon563/herdr-control-stream-deck**](https://github.com/so1omon563/herdr-control-stream-deck) | Provides Herdr workspace, tab, pane, and agent controls for Elgato Stream Deck hardware. |
| [**dghelm/herdy**](https://github.com/dghelm/herdy) | Provides a hurdy-gurdy for your agent herd: MIDI hardware control surface for herdr and Omarchy (Arturia Keylab 61). |
| [**imbriaco/herdr-deck**](https://github.com/imbriaco/herdr-deck) | Streams Deck plugin for Herdr: live agent status lights and one-key focus. |
| [**pnomolos/herdr-kontrol**](https://github.com/pnomolos/herdr-kontrol) | Provides Maschine MK3 glance+focus surface for herdr. |
| [**alex-devdone/herdrl**](https://github.com/alex-devdone/herdrl) | Provides Auto-reconnecting wrapper for remote herdr sessions, with agent mirroring into the local sidebar. |
| [**dghelm/omarchy-herdy**](https://github.com/dghelm/omarchy-herdy) | Provides Omarchy Shell configuration panel for the herdy MIDI controller. |
| [**Mamprim-go/sdlc-herdr**](https://github.com/Mamprim-go/sdlc-herdr) | Provides GitHub Issue SDLC automation using Pi Dynamic Workflows, HERDR and agent-browser. |
| [**iSlyy0717/omapad**](https://github.com/iSlyy0717/omapad) | Provides Omakase for your hands: drive Omarchy and Herdr from a Steam Controller. |

### Plugins and supporting utilities

*103 projects. Small integrations for notifications, status, tasks, scheduling, agent management, and everyday desktop behavior.*

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
| [**aorumbayev/herdr-canvas**](https://github.com/aorumbayev/herdr-canvas) | Opens a mouse-driven ASCII diagram canvas in a Herdr split. Humans draw boxes, lines, and text; agents read and edit the same JSON-backed diagrams through the CLI and skill. |
| [**aorumbayev/herdr-ctx**](https://github.com/aorumbayev/herdr-ctx) | A Herdr sidebar indicator that shows Claude's remaining context-window capacity. |
| [**miya10kei/herdr-plugin-sidebar**](https://github.com/miya10kei/herdr-plugin-sidebar) | Displays Google Calendar events and GitHub Actions run status in a split pane styled as a sidebar. |
| [**khatriafaz/herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo) | Adds the current agent, repository, and branch names to Herdr pane headers and the sidebar. |
| [**ondratuma/herdr-status-plugin**](https://github.com/ondratuma/herdr-status-plugin) | A per-pane activity plugin with sidebar icons, live timers, and a helper for renaming agent panes. |
| [**cedrus-8864/herdr-sidebar-numbers**](https://github.com/cedrus-8864/herdr-sidebar-numbers) | Shows workspace and agent position numbers matching Herdr's numbered shortcuts. |
| [**Coolsik/herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost) | Estimates the cost of the current Codex session. |
| [**samuelbaldwin05/herdr-burn**](https://github.com/samuelbaldwin05/herdr-burn) | Shows Claude Code cost and quota for each pane, plus a total spending overlay for the workspace. |
| [**mougua/herdr-reasonix**](https://github.com/mougua/herdr-reasonix) | Detects Reasonix agents and displays their status correctly. |
| [**sudoeren/herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker) | Runs lazydocker in a herdr split pane or its own tab. |
| [**akshat12/herdr-muse**](https://github.com/akshat12/herdr-muse) | Provides Herdr integration for Muse Code: idle/working/blocked pane state via lifecycle hooks (no Herdr fork needed). |
| [**ponko2/herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes) | Provides Automatically keeps panes in each tab evenly sized as panes are created, closed, moved, or exited. |
| [**ArtMoreno/herdr-glance**](https://github.com/ArtMoreno/herdr-glance) | Provides a live agent dashboard for Herdr, with five themes and a fast prompt segment. |
| [**Young1108/herdr-cyber-style**](https://github.com/Young1108/herdr-cyber-style) | Provides Black-terminal-native cyber workspace theme for Herdr on macOS. Tailored from herdr-social-glass Island Glass. |
| [**azyu/herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming) | Gives every detected agent a readable two-word name, persisted as the pane label so it survives restarts. |
| [**cnyarx/shelt**](https://github.com/cnyarx/shelt) | Provides a minimal, self-contained web terminal for Herdr or your login shell, with Unicode-safe rendering and clipboard image paste. |
| [**leonardoacosta/herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode) | Provides Standalone Herdr plugin that reports Jcode working/idle lifecycle state plus session identity. Independent implementation; no fork dependency. |
| [**corygforsythe/herdr-flight-radar**](https://github.com/corygforsythe/herdr-flight-radar) | Provides real-time ADS-B flight radar TUI backed by dump1090. |
| [**rudironsoni/herdr-orca**](https://github.com/rudironsoni/herdr-orca) | Attaches stock Orca tabs to Herdr-owned terminals. |
| [**fantoine/herdr-run-targets**](https://github.com/fantoine/herdr-run-targets) | Provides Launch, stop and restart a repository's dev services from a dashboard pane in Herdr. |
| [**tmastalirsch/herdr-workspace-board**](https://github.com/tmastalirsch/herdr-workspace-board) | Provides one line per git repository with unfinished work, ranked by how likely it is to be forgotten. |
| [**imtim/herdr-pane-id**](https://github.com/imtim/herdr-pane-id) | Provides label panes with their ID and agent name, plus tab and workspace id labels, so you and your agents can address any pane or agent by id. Works best with the herdr agent skill. |
| [**rewt/herdr-dia**](https://github.com/rewt/herdr-dia) | Provides Give Dia hands: review and update the pull requests in your brief with Herdr agents. |
| [**m2selfA/herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter) | Provides set pane name + agent alias (quick type-in or full menu). |
| [**okonomi/herdr-auto-tab-name**](https://github.com/okonomi/herdr-auto-tab-name) | Renames herdr tabs to the foreground command running in them. |
| [**SerHappy/herdr-achievements**](https://github.com/SerHappy/herdr-achievements) | Awards achievements and celebrations for completed tasks across your Herdr AI agent herd. |
| [**klukacin/herdr-finder-reveal**](https://github.com/klukacin/herdr-finder-reveal) | Provides Click a local file path in a Herdr pane, get it revealed in Finder (macOS). |
| [**sohilladhani/tmux2herdr**](https://github.com/sohilladhani/tmux2herdr) | Provides Migrate your tmux setup to herdr in one command. |
| [**potatoQi/herdr-focused-codex-fork**](https://github.com/potatoQi/herdr-focused-codex-fork) | Provides Fork the Codex session in the focused Herdr pane into a right-hand pane. |
| [**susomejias/herdr-awake**](https://github.com/susomejias/herdr-awake) | Keeps the machine awake while Herdr agents are busy. |
| [**llzx373/reasonix_herdr**](https://github.com/llzx373/reasonix_herdr) | Provides reasonix integration for herdr. |
| [**redsquiggle/herdr-browser**](https://github.com/redsquiggle/herdr-browser) | Keeps Chromium tab groups aligned with Herdr workspaces. |
| [**hellower/herdr-plugin-parallax**](https://github.com/hellower/herdr-plugin-parallax) | Opens URLs from Herdr terminal panes in the Parallax browser. |
| [**makgunay/herdr-atomic-reporter**](https://github.com/makgunay/herdr-atomic-reporter) | Provides Community Herdr reporter extension for Atomic, live working/idle/blocked pane states, pending the official integration. |
| [**shibayu36/herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes) | Provides automatically equalizes pane sizes on split and close (tmux select-layout -E, but automatic). |
| [**summerKK/herdr-orch**](https://github.com/summerKK/herdr-orch) | Orchestrates Claude, Codex, and AGY agents into phased pipelines for implementation, review, and verification. |
| [**barkerja/herdr-msg**](https://github.com/barkerja/herdr-msg) | Provides Durable mailboxes for AI agents running under herdr, cross-agent messaging for Claude, Codex, Gemini and every other kind herdr supports. |
| [**gdli6177/herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team) | Provides a Herdr plugin for Markdown-defined agent teams. |
| [**chuang861012/nu_herdr_navigate_directory**](https://github.com/chuang861012/nu_herdr_navigate_directory) | Provides Herdr-aware directory navigation for Nushell. |
| [**skinp/herdr-cwd-control**](https://github.com/skinp/herdr-cwd-control) | Provides a herdr plugin for enhanced control over initial working directory for new workspaces, tabs & panes. |
| [**perorin0418/jcode-herdr-integration**](https://github.com/perorin0418/jcode-herdr-integration) | Reports jcode agent lifecycle states to the Herdr sidebar using hooks. |
| [**shanefully-done/herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer) | Provides Resize herdr panes equally; automatically or manually. |
| [**OahMoza/herdr-phalanx**](https://github.com/OahMoza/herdr-phalanx) | Orchestrates multi-agent tasks across parallel Herdr workspaces. |
| [**CodeForBreakfast/beady-eye**](https://github.com/CodeForBreakfast/beady-eye) | Keeps an eye on your agents as they work on your beads. |
| [**transparent-pegasus/herdr-remote**](https://github.com/transparent-pegasus/herdr-remote) | Provides a remote controller for herdr panes. |
| [**wine-fall/herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id) | Copies the focused pane's id to the clipboard, or show every pane's id on its border. |
| [**oki2a24/herdr-mac-activity-monitor**](https://github.com/oki2a24/herdr-mac-activity-monitor) | Provides macos Activity Monitor for Herdr popup. |
| [**RufusLin/herdr-openmd**](https://github.com/RufusLin/herdr-openmd) | Opens selected markdown in openmd, a rich Qt preview from herdr. |
| [**osuki-dev/muqun-app**](https://github.com/osuki-dev/muqun-app) | Provides Muqun, a structured terminal companion for a Gateway you run on your own computer. |
| [**b12o/herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename) | Autorenames panes with the name of the current running process. |
| [**likangmax/KodeWork**](https://github.com/likangmax/KodeWork) | Provides Fast, local-first Windows workbench for private Linux coding sessions over SSH, Tailscale, Herdr, and tmux. |
| [**choplin/herdr-split-pane**](https://github.com/choplin/herdr-split-pane) | Opens a caller-provided command directly in a Herdr split pane. |
| [**atomsbaza/herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin) | Provides On-demand iOS build+test status pane for Herdr, with failure screenshots. |
| [**tobi404/herdr-share-session**](https://github.com/tobi404/herdr-share-session) | Provides one-click view-only tmux session sharing between Macs (Mac 2 shares read-only, Mac 1 drives over SSH). |
| [**gcgo/herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer) | Provides Automatically generate an agent name and display it in the terminal. |
| [**xenking/herdr-omp-sleep**](https://github.com/xenking/herdr-omp-sleep) | Provides Sleep mode for idle omp coding-agent sessions in herdr panes: park at ~4 MB instead of ~400 MB, wake on ENTER. |
| [**hidekingerz/herdr-plugin-mado**](https://github.com/hidekingerz/herdr-plugin-mado) | Provides herdr plugins that open agent-written markdown in mado, a TUI viewer, beside the agent writing it. |
| [**mjrusso/herdlord**](https://github.com/mjrusso/herdlord) | Provides Herdr multiplexer: monitor agents across multiple Herdr sessions. |
| [**deex2/herdroid**](https://github.com/deex2/herdroid) | Provides a native Android client for Herdr sessions over SSH with live workspace states. |
| [**yuloop/herdr-plugin-win-terminal**](https://github.com/yuloop/herdr-plugin-win-terminal) | Configures Windows Terminal keymaps and profiles for direct Herdr navigation. |
| [**n-jc/herdr-opencode**](https://github.com/n-jc/herdr-opencode) | Provides a set up to use Opencode within Apple Containers as a sandbox and manage via Herdr on a Mac OS host machine. |
| [**gaiagent0/ct304-hermes-bots**](https://github.com/gaiagent0/ct304-hermes-bots) | Provides a Hermes bot network coordinating agents across Herdr workspaces with capability-based model distribution. |
| [**Nofuture123/herdr-opencode2-integration**](https://github.com/Nofuture123/herdr-opencode2-integration) | Provides Dual-version compatible integration for Herdr and OpenCode (1.x & 2.0) with ACK-driven state machine and process isolation. |
| [**42lizard/workspace-basename**](https://github.com/42lizard/workspace-basename) | Provides set the workspace name based on the basename of the cwd the workspace was created. |
| [**kody-w/rapp-herdr**](https://github.com/kody-w/rapp-herdr) | Manages RAPP Twin neighborhoods as supervised Herdr workspaces. |
| [**gilvanecesar/obra**](https://github.com/gilvanecesar/obra) | Provides Crew de agentes de IA em paineis do herdr: engenheiro, QA, revisor e PR sobre a mesma tarefa, cada um numa copia isolada do repositorio. |
| [**chengyixu/oh-my-herdr**](https://github.com/chengyixu/oh-my-herdr) | Provides OhMyHerdr native agent profiles and visual workspace runtime. |
| [**joelhooks/herdr-brain**](https://github.com/joelhooks/herdr-brain) | Renders Brain SVX documents as native OpenTUI views in Herdr panes. |
| [**andrewmcodes/overhrd**](https://github.com/andrewmcodes/overhrd) | Provides a Procfile process manager for herdr users, a herdr-backed reimplementation of Overmind. |
| [**johnlindquist/herdr-pane-status**](https://github.com/johnlindquist/herdr-pane-status) | Provides Herdr with native per-pane agent status and PTY activity cards. |
| [**chrisg32/Ninjasana**](https://github.com/chrisg32/Ninjasana) | Provides Mouse-native terminal UI for Asana, inspired by herdr. |
| [**speardragon/herdr-labs**](https://github.com/speardragon/herdr-labs) | Provides herdr plugin lab, AI-agent plugin idea contests: 9 agents compete, AI judges score. |
| [**walcew/herdr-avatars**](https://github.com/walcew/herdr-avatars) | Provides downloadable avatar packages for the Herdr assist dashboard. |
| [**ilyakooo0/hermes-herdr-auto-title**](https://github.com/ilyakooo0/hermes-herdr-auto-title) | Updates Herdr tab titles automatically from the first user prompt using an LLM. |
| [**nottzaid/fx-herdr-jobsearch**](https://github.com/nottzaid/fx-herdr-jobsearch) | Provides a compact, agent-native workspace for evidence-driven job search and truthful application materials. |
| [**YiannisDermitzakis/herdr-setup**](https://github.com/YiannisDermitzakis/herdr-setup) | Provides Reproduce and sync a Herdr setup across machines, and onboard the coding agents on each host so a restart resumes their sessions. |
| [**cagriy/herdr-notch-releases**](https://github.com/cagriy/herdr-notch-releases) | Provides release feeds and DMGs for the Herdr Notch companion app. |
| [**xdagiz/opencode2-herdr**](https://github.com/xdagiz/opencode2-herdr) | Provides opencode2 plugin for herdr. |
| [**harveyfullstack/herdr-dist**](https://github.com/harveyfullstack/herdr-dist) | Provides Pinned Herdr binaries for Box runtime distribution. |
| [**Wyatth7/herdr**](https://github.com/Wyatth7/herdr) | Provides a collection of Herdr configurations and reusable plugins. |
| [**GranamyrBR/LunaCrab**](https://github.com/GranamyrBR/LunaCrab) | Provides Reserved for a separate project. |
| [**paddock-sh/paddock-herdr**](https://github.com/paddock-sh/paddock-herdr) | Provides a Herdr integration plugin for the Paddock platform. |
| [**abcxff/herdr-docker**](https://github.com/abcxff/herdr-docker) | Keeps track of docker builds like you do with agents for herdr. |
| [**zanellig/keyblink**](https://github.com/zanellig/keyblink) | Provides HyperX Game Mode LED control for Linux and Herdr. |

### Setup, packages, and version management

*24 projects. Guides, configuration bundles, installers, package definitions, and tools for reproducible Herdr environments.*

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
| [**the-inconvenience-store/herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt) | Provides a keyboard-driven Tilt dashboard for Herdr. |
| [**HunterStarets/herdr-gitbash-agent-detector**](https://github.com/HunterStarets/herdr-gitbash-agent-detector) | Detects OpenCode sessions running inside Git Bash panes on Windows and reports their state (idle / working). |
| [**no-phux/herdr-opencode**](https://github.com/no-phux/herdr-opencode) | Reports OpenCode lifecycle events to Herdr, preserving agent state and restoring pane sessions. |
| [**patdx/sido-askpass**](https://github.com/patdx/sido-askpass) | Provides sudoaskpass shim for headless agent environments (tmux, Herdr, GUI, TTY), npm package. |
| [**herdrdev/herdr-nix**](https://github.com/herdrdev/herdr-nix) | Pushes herdr releases to cachix. |
| [**meuble/Herdr-mistral-vibe**](https://github.com/meuble/Herdr-mistral-vibe) | Provides Herdr integration for Mistral Vibe. |
| [**conda-forge/herdr-feedstock**](https://github.com/conda-forge/herdr-feedstock) | Provides a conda-smithy repository for herdr. |
| [**ehcastroh-teach/Herdr_AI_Dev_Environment**](https://github.com/ehcastroh-teach/Herdr_AI_Dev_Environment) | Provides Declarative, reproducible and version-controlled system for building with AI Coding Agents. |
| [**orange4664/herdr-remote-workspace**](https://github.com/orange4664/herdr-remote-workspace) | Runs Herdr locally while agents work on an SSH host with Mutagen-synchronized projects. |
| [**ccyisafool/herdr-terminal**](https://github.com/ccyisafool/herdr-terminal) | Provides a thin, branded Ghostty client that starts Herdr by default. |
| [**2lab-ai/homebrew-tap**](https://github.com/2lab-ai/homebrew-tap) | Provides Homebrew formulae for installing Herdr extensions and companion packages. |
| [**Comamoca/command-code-herdr**](https://github.com/Comamoca/command-code-herdr) | Provides Integration of command code header. |
| [**unok/stack-review**](https://github.com/unok/stack-review) | Provides Preflight review for stacked PRs: builds a herdr workspace and opens each layer's diff in hunk before gh stack submit. |
| [**kingbywork-ui/issh-plugin-herdr**](https://github.com/kingbywork-ui/issh-plugin-herdr) | Provides issh terminal herdr workspace plugin. |
| [**RobLoach/asdf-herdr**](https://github.com/RobLoach/asdf-herdr) | Provides Herdr for the asdf version manager. |

---

## 7. Experimental projects

*15 projects. Early experiments, design documents, and incomplete prototypes. Check each repository before relying on one in daily work.*

### Experiments, concepts, and scaffolds

*15 projects. Ideas and prototypes that are useful to study but may be incomplete, read-only, or not yet installable.*

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
| [**RickyMarou/herdr-display-workspace**](https://github.com/RickyMarou/herdr-display-workspace) | Shows the active workspace label on the right side of the tab bar. |
| [**leddt/plasma-cliamp**](https://github.com/leddt/plasma-cliamp) | Provides Experimental Plasma 6 plasmoid for cliamp (herdr-hosted TUI + spectrum). |
| [**hmu332233/herdr-visual-lab**](https://github.com/hmu332233/herdr-visual-lab) | Provides a playful live dashboard that reimagines your Herdr coding agents as galaxies, races, raids, kanban boards, and more. |

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
