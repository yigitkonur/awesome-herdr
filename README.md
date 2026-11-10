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

1. [Run and orchestrate agents (505)](#1-run-and-orchestrate-agents)
   - [Official Herdr projects and skill (5)](#official-herdr-projects-and-skill)
   - [Multi-agent fleets and supervisors (87)](#multi-agent-fleets-and-supervisors)
   - [Swarm, mob, and consensus orchestrators (13)](#swarm-mob-and-consensus-orchestrators)
   - [Claude Code multi-agent teams (53)](#claude-code-multi-agent-teams)
   - [Claude Code: Account switchers and auth monitors (5)](#claude-code-account-switchers-and-auth-monitors)
   - [Pi supervisor workflows and extensions (91)](#pi-supervisor-workflows-and-extensions)
   - [Pi: Presence, memory, and status extensions (8)](#pi-presence-memory-and-status-extensions)
   - [Subagent launchers and delegation (81)](#subagent-launchers-and-delegation)
   - [Autonomous coding and pull-request loops (14)](#autonomous-coding-and-pull-request-loops)
   - [Task queues, backlogs, and event triggers (55)](#task-queues-backlogs-and-event-triggers)
   - [Linear, GitHub Issues, and issue-to-PR automation (33)](#linear-github-issues-and-issue-to-pr-automation)
   - [General workflows and skill packs (60)](#general-workflows-and-skill-packs)
2. [Herdr app layouts, mods, and themes (111)](#2-herdr-app-layouts-mods-and-themes)
   - [Herdr app layouts (47)](#herdr-app-layouts)
   - [Herdr app mods and themes (64)](#herdr-app-mods-and-themes)
3. [Connect through MCP and the socket API (238)](#3-connect-through-mcp-and-the-socket-api)
   - [MCP servers (17)](#mcp-servers)
   - [Socket API and herdr-core clients and SDKs (38)](#socket-api-and-herdr-core-clients-and-sdks)
   - [Chat alerts: Telegram, Discord, and Slack (20)](#chat-alerts-telegram-discord-and-slack)
   - [Desktop, mobile, and webhook notifications (40)](#desktop-mobile-and-webhook-notifications)
   - [Telemetry, events, and quota streaming (30)](#telemetry-events-and-quota-streaming)
   - [Voice, hardware, and remote bridges (35)](#voice-hardware-and-remote-bridges)
   - [Protocol and third-party bridges (58)](#protocol-and-third-party-bridges)
4. [Editor integrations (88)](#4-editor-integrations)
   - [Neovim navigation and splits (26)](#neovim-navigation-and-splits)
   - [Full Neovim-hosted workspaces (4)](#full-neovim-hosted-workspaces)
   - [VS Code, Cursor, and dev containers (13)](#vs-code-cursor-and-dev-containers)
   - [Vim, Kakoune, and other editors (13)](#vim-kakoune-and-other-editors)
   - [REPL and code dispatchers (8)](#repl-and-code-dispatchers)
   - [Editor plugins and bridges (24)](#editor-plugins-and-bridges)
5. [Switch and restore sessions (188)](#5-switch-and-restore-sessions)
   - [Fuzzy session switchers and terminal pickers (90)](#fuzzy-session-switchers-and-terminal-pickers)
   - [Persistence, snapshots, and state restoration (37)](#persistence-snapshots-and-state-restoration)
   - [Workspace and multi-session management (61)](#workspace-and-multi-session-management)
6. [Worktrees and terminal experience (788)](#6-worktrees-and-terminal-experience)
   - [Git worktree automation (101)](#git-worktree-automation)
   - [Workspace lifecycle and multi-repository tools (10)](#workspace-lifecycle-and-multi-repository-tools)
   - [Diff review and code inspection (59)](#diff-review-and-code-inspection)
   - [File viewers, terminal browsers, and markdown previews (49)](#file-viewers-terminal-browsers-and-markdown-previews)
   - [Pane navigation and overlay hints (33)](#pane-navigation-and-overlay-hints)
   - [Pane layout management (10)](#pane-layout-management)
   - [Terminal keybindings and shortcut helpers (61)](#terminal-keybindings-and-shortcut-helpers)
   - [Command palettes and workspace switchers (38)](#command-palettes-and-workspace-switchers)
   - [Status lines and workspace metadata (94)](#status-lines-and-workspace-metadata)
   - [Sidebar displays and tab labels (128)](#sidebar-displays-and-tab-labels)
   - [Status overlays, HUDs, and agent timers (52)](#status-overlays-huds-and-agent-timers)
   - [Context meters and rate-limit gauges (53)](#context-meters-and-rate-limit-gauges)
   - [Output inspection, logs, and transcripts (42)](#output-inspection-logs-and-transcripts)
   - [Agent visualizations and terminal games (7)](#agent-visualizations-and-terminal-games)
   - [Herdr TUI themes and appearance (8)](#herdr-tui-themes-and-appearance)
   - [Security guards and collision detectors (10)](#security-guards-and-collision-detectors)
   - [Plugin collections, frameworks, and ready-made configs (33)](#plugin-collections-frameworks-and-ready-made-configs)
7. [Apps, companion integrations, and installation (415)](#7-apps-companion-integrations-and-installation)
   - [Native desktop and mobile apps (109)](#native-desktop-and-mobile-apps)
   - [Web dashboards and remote viewers (101)](#web-dashboards-and-remote-viewers)
   - [Hardware and ambient displays (31)](#hardware-and-ambient-displays)
   - [Plugins and supporting utilities (137)](#plugins-and-supporting-utilities)
   - [Setup, packages, and version management (37)](#setup-packages-and-version-management)
8. [Experimental projects (9)](#8-experimental-projects)
   - [Experiments, concepts, and scaffolds (9)](#experiments-concepts-and-scaffolds)
9. [Resources](#resources)
10. [Reference](#reference)

---

## 1. Run and orchestrate agents

*505 projects. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.*

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

*87 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*

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
| [**vitalysim/herdr-synapse**](https://github.com/vitalysim/herdr-synapse) | Coordinates coding agents in a Herdr TUI session with a shared board and idle-gated message delivery. |
| [**StructuPath/herdr-swarm**](https://github.com/StructuPath/herdr-swarm) | Runs several coding agents in parallel, each with its own branch, worktree, and Herdr pane, making it easy to watch competing implementations, compare changes, and keep the strongest result. |
| [**machine-machine/herdr-factory-loop-skill**](https://github.com/machine-machine/herdr-factory-loop-skill) | Orchestrates coding-agent fleets in Herdr TUI, spawning workers, dispatching tasks, monitoring status, and coordinating fan-out and convergence. |
| [**vib-z/stampede**](https://github.com/vib-z/stampede) | Spins up a team of Claude Code, Codex, and Cursor agents run by one lead in Herdr panes or herdr-core terminals, started locally or from a Grok Bot chat over Tailscale. Sends each gate question back to whoever started the job, on macOS and Linux. |
| [**jlcases/herdr-lcars**](https://github.com/jlcases/herdr-lcars) | Monitors and commands Herdr TUI agent fleets from a browser-based LCARS interface with account quota tracking and context handoffs. |
| [**crestai-labs/feld**](https://github.com/crestai-labs/feld) | Tracks and controls Claude Code and Codex sessions in Herdr with a shared timeline, messages, and scheduled jobs. |
| [**andrebrov/drover**](https://github.com/andrebrov/drover) | Coordinates Claude Code, Codex and other agents in Herdr TUI with task dispatch, isolated worktrees and cross-harness review. |
| [**aashishd/herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger) | Defines a small messaging protocol for agents in separate Herdr panes. Peers use memorable call signs and exchange focused one-line messages, allowing coordination without sharing complete session histories. |
| [**travisjeffery/herdr-quartermaster**](https://github.com/travisjeffery/herdr-quartermaster) | Coordinates Claude Code, Codex or Muse Code workers in separate Herdr TUI worktrees using beads as the task record. |
| [**zanuartri/herdr-rig**](https://github.com/zanuartri/herdr-rig) | Uses a manager agent to dispatch tickets to workers and reviewers in Herdr TUI or the Herdr app, with an optional desktop board. |
| [**Northern-Lighthouse/herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet) | Manages a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispatch, diskless workspaces. |
| [**kylezk777/herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator) | Coordinates Herdr agents through file-based tasks, scoped roles, and review gates using an orchestrator-operator pattern. |
| [**vladzima/herd**](https://github.com/vladzima/herd) | Runs a Claude Code coordinator that delegates tasks to Herdr tabs and collects reports from Claude, Codex, Gemini, or other workers. |
| [**marcvermeeren/chatter**](https://github.com/marcvermeeren/chatter) | Coordinates Claude Code, Codex, Pi, and other agents through shared per-repository chat, tasks, and memory in Herdr. |
| [**JosssphZhou/azir-dispatch**](https://github.com/JosssphZhou/azir-dispatch) | Routes tasks to coding agents in Herdr TUI using JEV and tracks dispatches and completions on a terminal board. |
| [**letya999/workflow-herdr**](https://github.com/letya999/workflow-herdr) | Provides a YAML-configurable workflow for coordinating AI agents in Herdr with customizable roles and state validation. |
| [**wayne930242/straw-boss**](https://github.com/wayne930242/straw-boss) | Coordinates Codex, Claude Code, and Antigravity tasks in Herdr-backed sessions across single-app repositories or monorepos. The repository is archived. |
| [**SimoneDaniotti/horchestra**](https://github.com/SimoneDaniotti/horchestra) | Runs orchestrator-led agent teams in Herdr TUI and displays a live agent map in each tab. |
| [**StructuPath/herdr-conductor**](https://github.com/StructuPath/herdr-conductor) | Coordinates producer and reviewer agents with strict task and report formats, Git compare-and-swap checks, and a passive status board. It is designed for visible, operator-supervised delivery rather than free-form swarming. |
| [**mikeyobrien/herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles) | Provides a data-driven command-line harness and reusable model profiles for agents running through Herdr. |
| [**forsakesoul/herdr-nakama**](https://github.com/forsakesoul/herdr-nakama) | Creates, initializes, and restores Owner, Worker, and Advisor agent teams in Herdr TUI panes. |
| [**Nirvaan05/arda**](https://github.com/Nirvaan05/arda) | Lets Herdr TUI agents discover peers and exchange work across sessions and machines. |
| [**sirkirby/routr**](https://github.com/sirkirby/routr) | Routes coding tasks to Claude Code, Codex, Cursor, Antigravity and Kiro workers in Herdr TUI panes or Herdr app tabs. |
| [**nhype/telegram-harness**](https://github.com/nhype/telegram-harness) | Runs Claude Code tasks from Telegram using Hermes Agent to manage Herdr TUI panes and status events. |
| [**voodootikigod/adlc-herdr**](https://github.com/voodootikigod/adlc-herdr) | Adds Agentic Development Lifecycle gates into Herdr. It shows ticket states, per-pane phases, and backlog boards, and provides actions for unblocking controlled milestones. |
| [**zhenyufu/herdr-cadence**](https://github.com/zhenyufu/herdr-cadence) | Uses a lead agent to sort tasks and start specialized workers in separate Herdr tabs and Git worktrees. It checks for a clean repository state and gives each worker only the context it needs. |
| [**lunoob/mini-orchestrator**](https://github.com/lunoob/mini-orchestrator) | Orchestrates custom Herdr script workflows using TypeScript. |
| [**rarce/herdr-crew**](https://github.com/rarce/herdr-crew) | Starts Claude Code, Codex and Pi roles in Herdr TUI tabs from a versioned crew file and shows a status board. |
| [**GenaroSalomone/foreman-sh**](https://github.com/GenaroSalomone/foreman-sh) | Runs a planning agent and isolated worktree executors with reviews and guards for Claude Code and Pi in Herdr. |
| [**TheMickeyDodger/dodging-infinity**](https://github.com/TheMickeyDodger/dodging-infinity) | Coordinates Herdr engineering agents around approved missions, tracking progress, review evidence, and delivery decisions. |
| [**ohitslaurence/herdr-fleet**](https://github.com/ohitslaurence/herdr-fleet) | Runs coding agents in Herdr TUI worktrees and tracks their tasks and pull requests through review and CI. |
| [**GuitarWag/herdr-shepherd**](https://github.com/GuitarWag/herdr-shepherd) | Runs Claude Code and Codex teams in Herdr TUI panes with boss and worker roles, team discovery, and messaging. |
| [**flaviomartil/herdr-jev**](https://github.com/flaviomartil/herdr-jev) | Routes tasks to coding agents in Herdr TUI panes using Jev triage and AI Harness execution profiles. Runs implementation and independent review stages with optional verification commands. |
| [**ShenghaiWang/helm**](https://github.com/ShenghaiWang/helm) | Provides an agent harness on top of Herdr for coordinating coding workflows. |
| [**hkandala/orchestratr**](https://github.com/hkandala/orchestratr) | Runs and schedules Claude, Codex, and other coding agents in Herdr through a CLI, TypeScript SDK, or installable skill. |
| [**ankitvashisht12/crew**](https://github.com/ankitvashisht12/crew) | Coordinates role-based Claude and Codex workflows in named Herdr TUI tabs with durable tasks and isolated worktrees. |
| [**LittleDrinks/oh-my-herdr**](https://github.com/LittleDrinks/oh-my-herdr) | Organizes CLI-agent work in Herdr tabs using reusable delegation, review, and delivery workflows. |
| [**saxonmurray85-ops/sheprd**](https://github.com/saxonmurray85-ops/sheprd) | Deploys local llama.cpp models and launches specialized agents into Herdr workspaces through a terminal or web interface. |
| [**neospark-sol/agentflock**](https://github.com/neospark-sol/agentflock) | Coordinates coding CLI builders and reviewers in persistent Herdr sessions with milestone approval, evidence checks, and recovery. |
| [**ravikanchikare/herdr-agent-factory**](https://github.com/ravikanchikare/herdr-agent-factory) | Builds and evaluates target agents in a macOS control plane that delegates work to agents in Herdr panes. |
| [**0-CYBERDYNE-SYSTEMS-0/herdr-dev-team**](https://github.com/0-CYBERDYNE-SYSTEMS-0/herdr-dev-team) | Organizes a lead and six scoped workers in Herdr with task packets, worktree isolation, and review gates. |
| [**C1TRuSovo831/herdr-codex-team**](https://github.com/C1TRuSovo831/herdr-codex-team) | Launches isolated Codex planner, coder, and reviewer teams in Herdr with role prompts and team-scoped routing. |
| [**yarrasys/herdr-fleet-plugin**](https://github.com/yarrasys/herdr-fleet-plugin) | Starts, restarts and swaps a named team of coding agents from a per-repository `.herdr/fleet.toml`, tiled into one Herdr workspace. Seats can be Claude, Codex or Gemini; agents message each other with `herdr-fleet send`, and `doctor` checks the fleet and Claude Code permission rules. |
| [**skysilver1223/herdr-agent-harness**](https://github.com/skysilver1223/herdr-agent-harness) | Creates Ubuntu and WSL projects with role and skill templates for coordinating Claude, Codex, and AGY in Herdr. |
| [**SimonMallas/agent-letterbox-herdr**](https://github.com/SimonMallas/agent-letterbox-herdr) | Lets mixed coding-agent teams exchange durable, queryable letters and wake recipients for coordination in Herdr. |
| [**bpcakes/epicd**](https://github.com/bpcakes/epicd) | Orchestrates Codex work on Beads epics with independent review and resumable native Herdr TUI or SDK sessions. |
| [**gdli6177/herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team) | Organizes Herdr agent teams from Markdown definitions. |
| [**gilvanecesar/obra**](https://github.com/gilvanecesar/obra) | Runs Claude Code engineer, QA, reviewer, and pull-request agents in separate Herdr TUI panes and Git worktrees. |
| [**Luisotee/agent-mesh**](https://github.com/Luisotee/agent-mesh) | Lets a Claude Code or Antigravity session hand work in another repository to an agent running inside it, in its own Herdr pane and Git worktree, with mailbox messaging both ways. Larger tasks go through planning, approval, and pull-request review by Claude, Antigravity, or Copilot, and a bundled Herdr plugin sends desktop notifications. |
| [**cowcow02/herdr-agent-orchestrator**](https://github.com/cowcow02/herdr-agent-orchestrator) | Adds event-driven orchestration around one existing controller agent while Herdr observes and reports the work. It avoids replacing the controller with a separate fleet manager. |
| [**hewel/herdr-harness-coordinator**](https://github.com/hewel/herdr-harness-coordinator) | Coordinates autonomous coding-agent harnesses across separate Herdr panes and tracks their active tasks. |
| [**gurronen/herdr-looper**](https://github.com/gurronen/herdr-looper) | Launches repeatable machine-local Pi jobs in fresh Herdr workspaces and worktrees. |
| [**charlieYong/herdr-live**](https://github.com/charlieYong/herdr-live) | Orchestrates live multi-agent harnesses in Herdr, dispatching prompts and streaming status outputs. |
| [**leifarriens/shepherd**](https://github.com/leifarriens/shepherd) | Coordinates coding workers in Herdr with a reusable manager skill, guarded CLI operations, and a task ledger. |
| [**HarshaLakkaraju/herdr-orchestrator-skill**](https://github.com/HarshaLakkaraju/herdr-orchestrator-skill) | Teaches a lead agent to plan tasks, launch Herdr workers, exchange artifacts, review results, and clean up completed panes. |
| [**raystyle/evo-harness**](https://github.com/raystyle/evo-harness) | Coordinates Codex, Kimi, Claude, and Grok through a staged rmux workflow with a Herdr monitor and decision-notification daemon. |
| [**erdostom/herdr-orchestrate**](https://github.com/erdostom/herdr-orchestrate) | Runs a Herdr agent fleet with persistent conductor and watcher roles and short-lived OpenCode task workers. |
| [**andthezhang/herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow) | Runs JavaScript workflows that launch coding agents in Herdr TUI panes, including parallel jobs, isolated worktrees, and SSH hosts. |
| [**theaileverage/marionette**](https://github.com/theaileverage/marionette) | Runs coding-agent workflows in Herdr through a CLI and TypeScript SDK, with durable project state and separate evidence and acceptance states. |
| [**talberthoule/herdr-shepherd**](https://github.com/talberthoule/herdr-shepherd) | Coordinates Claude Code and Codex sessions with ownership rules, audited handoffs, and a Herdr TUI skill. |
| [**thelad-dev/orchaester**](https://github.com/thelad-dev/orchaester) | Runs a Herdr TUI orchestration workflow with Grok Build and Cursor using native agent and worktree commands. |
| [**testy-cool/herdr-agent-control**](https://github.com/testy-cool/herdr-agent-control) | Coordinates Herdr TUI workers using process leases and runbooks to limit delegation drift and unsafe handoffs. |
| [**klahrich/smashhh**](https://github.com/klahrich/smashhh) | Runs planner, coder, and verifier agents in a Herdr TUI workspace to build a project. |
| [**navanchauhan/attractor**](https://github.com/navanchauhan/attractor) | Runs a sequential planning and execution workflow with Codex and Claude Code through the Herdr TUI socket. |
| [**dcadenas/kelpie**](https://github.com/dcadenas/kelpie) | Adds durable inter-agent messaging, reminders, and recovery for agents running in Herdr TUI. |
| [**RodrigoSosa96/workflow-control-plane**](https://github.com/RodrigoSosa96/workflow-control-plane) | Dispatches Pi, Claude, and Codex workers into isolated Git worktrees and manages their Herdr workspaces and handoffs. |
| [**pandore/herdr-work**](https://github.com/pandore/herdr-work) | Routes coding tasks through a model-neutral Herdr orchestration skill that selects roles and keeps one owner accountable. |
| [**brenoperucchi/herdr-mesh-tools**](https://github.com/brenoperucchi/herdr-mesh-tools) | Bootstraps Herdr workspaces and agents, runs parallel reviews, and swaps executors with context handoff. |
| [**w-gitops/herdr-agent-factory**](https://github.com/w-gitops/herdr-agent-factory) | Launches and coordinates multi-agent teams on Herdr independently of the coding harness. |
| [**jirathip-dev/canter**](https://github.com/jirathip-dev/canter) | Plans, reviews, and merges work across Herdr agent fleets using reviewed plans and explicit grants for mutations. |
| [**huynguyen03dev/herdr-agent**](https://github.com/huynguyen03dev/herdr-agent) | Supplies lead, peer, and supervisor role profiles and helper scripts for coordinating agents through Herdr TUI panes. |
| [**ahnsv/maeh**](https://github.com/ahnsv/maeh) | Organizes agent work as plan trees and workspaces with primary and critic agents, using Herdr TUI or tmux as a backend. |
| [**beraterkanelcelik/agent-army**](https://github.com/beraterkanelcelik/agent-army) | Coordinates parallel coding missions through a three-level agent hierarchy using Claude Code, Herdr, and cursor-agent. |
| [**GMakeziG/ninjatronics-ai**](https://github.com/GMakeziG/ninjatronics-ai) | Coordinates specialist engineering agents through Hermes, Herdr, Claude Code, and Codex. |
| [**hung-eggie-do-covergo/delegate-orchestrator**](https://github.com/hung-eggie-do-covergo/delegate-orchestrator) | Starts one isolated Claude Code subagent per repository through Herdr worktrees, with multi-repository coordination, worktree reuse, and session resumption. |
| [**summerKK/herdr-orch**](https://github.com/summerKK/herdr-orch) | Orchestrates Claude, Codex, and AGY agents into phased pipelines for implementation, review, and verification. |
| [**OahMoza/herdr-phalanx**](https://github.com/OahMoza/herdr-phalanx) | Orchestrates multi-agent tasks across parallel Herdr workspaces. |

### Swarm, mob, and consensus orchestrators

*13 projects. Parallel agent swarms, mob-programming groups, and multi-model consensus engines.*

| Project | What it does |
|---|---|
| [**aliceisjustplaying/swarmchat**](https://github.com/aliceisjustplaying/swarmchat) | Lets Claude Code and Codex or Astra exchange peer messages in Herdr while a third pane shows their shared log. |
| [**zekierman/herdr-council**](https://github.com/zekierman/herdr-council) | Asks coding agents in Herdr TUI the same question and combines blind peer rankings with a judge agent verdict. |
| [**enes/herdr-rooms**](https://github.com/enes/herdr-rooms) | Opens review rooms where Claude Code or Codex agents review each other in Herdr TUI. |
| [**HinchK/stampede**](https://github.com/HinchK/stampede) | Coordinates coding agents in Herdr TUI with ticket dispatch, independent checks, and a human-controlled integration queue. |
| [**neospeed83/herdr-tournament**](https://github.com/neospeed83/herdr-tournament) | Runs independent Codex or Claude reviews of a branch or pull request, then consolidates findings through an adversarial judge workflow. |
| [**tuanhung303/herdr-swarm**](https://github.com/tuanhung303/herdr-swarm) | Runs agent waves in Herdr pane grids, routes messages through an optional mailbox, and collects results from multiple harnesses. |
| [**ndemeshchenko/herdr-peer-chat**](https://github.com/ndemeshchenko/herdr-peer-chat) | Lets Claude Code and Codex exchange messages in one Herdr tab through the agent API. |
| [**ArtMoreno/herdr-swarm**](https://github.com/ArtMoreno/herdr-swarm) | Races coding agents in Herdr panes and isolated Git worktrees, compare their diffs, and apply a winner. |
| [**l20250208/herdr-consensus**](https://github.com/l20250208/herdr-consensus) | Combines two isolated agent reviews into a consensus, human decision, fix plan, and worktree-based fix. |
| [**bandoyer/swarm-forge-herdr**](https://github.com/bandoyer/swarm-forge-herdr) | Runs role-based agent swarms in separate Git worktrees with validated handoffs and optional human approval. |
| [**bandoyer/swarm-forge-windows**](https://github.com/bandoyer/swarm-forge-windows) | Provides a Windows distribution of swarm-forge-herdr for running AI agent swarms on the Herdr runtime. |
| [**binthnay1973/deepthink**](https://github.com/binthnay1973/deepthink) | Runs a multi-agent research panel in Herdr panes, cross-checks independent findings, and consolidates a sourced verdict. |
| [**burningportra/vibing-with-herdr**](https://github.com/burningportra/vibing-with-herdr) | Coordinates a same-branch Herdr TUI swarm that drains Beads tasks using exclusive Agent Mail reservations instead of worktrees. |

### Claude Code multi-agent teams

*53 projects. Adapters and skills that organize Claude Code sessions into structured teams.*

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
| [**shaun-agent/herdr-map**](https://github.com/shaun-agent/herdr-map) | Renders visual Mermaid diagrams mapping Herdr architecture, socket APIs, and workspace concepts. |
| [**jmcjm/Hivemind**](https://github.com/jmcjm/Hivemind) | Coordinates a swarm of Claude Code agents in Herdr terminal panels using file-based briefs and asynchronous mail. |
| [**Marie673/herdr-env**](https://github.com/Marie673/herdr-env) | Configures an integrated Herdr, ghq, and Claude Code workspace environment mapping one branch to each agent worktree. |
| [**eliasstravik/herdr-chat**](https://github.com/eliasstravik/herdr-chat) | Provides a live structured chat view for agents running inside Herdr. |
| [**inbeomheo/herdr-orchestra**](https://github.com/inbeomheo/herdr-orchestra) | Coordinates Codex, Grok, Gemini, or Claude worker panes from a central Claude Code controller session. |
| [**LittleDrinks/herdr-orchestrator-skill**](https://github.com/LittleDrinks/herdr-orchestrator-skill) | Turns the main Claude Code session into a coordinator that plans work, starts workers in Herdr panes, and monitors them without editing code itself. It includes Python monitors, a YAML state-machine template, and role prompts. |
| [**alexhooi/herdr-orchestrate**](https://github.com/alexhooi/herdr-orchestrate) | Runs Claude Code, Codex CLI and pi as visible, interruptible terminal-pane agent teams. One orchestrator, cross-model review, review-gated merges. |
| [**lutian/herdr-sdd-harness**](https://github.com/lutian/herdr-sdd-harness) | Provides a Spec-Driven Development harness using Herdr for orchestration. |
| [**izumi0uu/terminal-theme-suite**](https://github.com/izumi0uu/terminal-theme-suite) | Switches iTerm2, OMP, Herdr, and terminal wallpapers as one coordinated theme suite. |
| [**richardadonnell/herdr-claude-manager**](https://github.com/richardadonnell/herdr-claude-manager) | Tiles and manages an N-agent grid of labeled Claude Code panes on Windows and macOS, with menu commands to list, resume, and stop workspaces. |
| [**Elio2000/herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review) | Starts a second coding agent in a split pane to review the current workspace diff. The tool runs a protected review, revision, and decision loop and includes a Claude Code skill for orchestration. |
| [**eciuca/herdr-drover**](https://github.com/eciuca/herdr-drover) | Orchestrates Claude Code, Codex, and Kira CLI agents across tmux-style Herdr workflows. |
| [**terry-li-hm/herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat) | Provides a shared local Herdr room for Pi, Claude Code, Codex, and Grok Build. |
| [**sm-yjr/herdr-coordinator**](https://github.com/sm-yjr/herdr-coordinator) | Coordinates Herdr agent fleets across multiple terminal panes. |
| [**jerryfane/herdr-plan-approve**](https://github.com/jerryfane/herdr-plan-approve) | Approves Claude Code plan-mode dialogs automatically in Herdr so agents can transition to execution without pauses. |
| [**gal-leib/claude-vibe**](https://github.com/gal-leib/claude-vibe) | Provides a /vibe skill: a read-only Claude Code director that spawns, briefs and verifies persistent worker sessions in Herdr panes. |
| [**m-mohamed/sheprd**](https://github.com/m-mohamed/sheprd) | Keeps Pi, Codex, Claude Code, and OpenCode in one visible, isolated Herdr Flok. |
| [**kennethgeerts/herdr-architect**](https://github.com/kennethgeerts/herdr-architect) | Coordinates a Claude Code architect with implementation and independent review agents in separate Herdr tabs. |
| [**qinglang8609/deepseek_herdr**](https://github.com/qinglang8609/deepseek_herdr) | Orchestrates multi-agent teams across Claude, OpenCode, and Codex in Herdr using DeepSeek Harness and shared task boards. |
| [**gnepud/herdr-sbx-box**](https://github.com/gnepud/herdr-sbx-box) | Provides a modular Docker Sandbox (sbx) multi-agent workspace managed by Herdr. |
| [**hunaish-dev/nakama**](https://github.com/hunaish-dev/nakama) | Provides a wrapper, not a harness: coordinates a crew of coding-agent CLIs (starting with Claude Code) on one goal, with live attach via herdr. |
| [**manikbajaj/herdr-configuration**](https://github.com/manikbajaj/herdr-configuration) | Provides a script installation for replicating Herdr settings across multiple computers. |
| [**robertdo/claude-herdr-orchestration**](https://github.com/robertdo/claude-herdr-orchestration) | Uses Claude Code hooks and Herdr TUI orchestration to keep changes in worktrees and route tasks among model tiers. |
| [**ralphcrisostomo/herdr-goal-skill**](https://github.com/ralphcrisostomo/herdr-goal-skill) | Splits a goal among parallel Claude Code leads in Herdr TUI panes and worktrees, then reviews the combined result. |
| [**yigitkonur/herdr-pm**](https://github.com/yigitkonur/herdr-pm) | Adds a technical project manager to each live agent tab that reads session state and guides the agent. Supports Claude, Codex, Pi, and Hermes with optional persistent notes. |
| [**clawsouls/clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin) | Applies ClawSouls persona definitions to agents running in Herdr. It sets role-specific environments and behavioral rules for Claude Code and other supported agents across multiple panes. |
| [**chetanunadkat-lang/herdr-fleet**](https://github.com/chetanunadkat-lang/herdr-fleet) | Runs Claude and Codex workers as a fleet in Herdr panes. The project includes orchestration skills, an `hm` command-line tool, agent definitions, and a Claude Code installer. |
| [**doggyfish/herdr-tuple-plugin**](https://github.com/doggyfish/herdr-tuple-plugin) | Provides a herdr plugin that pairs two coding agents side by side in one tab and moves text between them. |
| [**nicoRomeroCuruchet/agentic-box**](https://github.com/nicoRomeroCuruchet/agentic-box) | Provides an isolated box where Claude Code drives local model agents. |
| [**iagogfe/herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory) | Launches coding agents through ai-memory managed workstreams - cross-agent session continuity. |
| [**steven-terrana/hermes-herdr-plugin**](https://github.com/steven-terrana/hermes-herdr-plugin) | Orchestrates Hermes agent sessions with Claude Code, Codex, and Pi under Herdr. |
| [**inxx/herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review) | Spawns a four-pane pipeline in Herdr with Opus planning, Sonnet coding, and Claude plus Codex review. |
| [**Crush53/pi-herdr-managed-agents**](https://github.com/Crush53/pi-herdr-managed-agents) | Manages native Pi, Claude Code, and Codex agents in auditable Herdr tabs. |
| [**nakamori-naoya/agent-fleet-plugins**](https://github.com/nakamori-naoya/agent-fleet-plugins) | Controls multi-agent roles, task routing, and Herdr execution using declarative fleet specifications. |
| [**ericed11/coding-agents-on-a-vps**](https://github.com/ericed11/coding-agents-on-a-vps) | Moves your Claude Code and Codex work off your laptop onto a private always-on VPS: Tailscale-only access, no public SSH, and four ways in (Herdr, VS Code Remote SSH, Codex desktop, iOS). |
| [**parkbeomsub/herdr_orch**](https://github.com/parkbeomsub/herdr_orch) | Launches AI agent teams in Herdr with team presets, inter-pane messaging, and worktree isolation. |
| [**kil9/claude-auto-retry-herdr**](https://github.com/kil9/claude-auto-retry-herdr) | Retries Claude Code sessions automatically upon rate limits using native Herdr socket APIs. |
| [**Tatendaz/mission-control**](https://github.com/Tatendaz/mission-control) | Provides a self-updating project radar for solo devs: swept from git, PRs, Claude session logs and a watch-dictated idea inbox; launches agents into herdr straight from the board. |
| [**patraianton/teammate**](https://github.com/patraianton/teammate) | Provides one coding agent hires another, a worker Claude Code session in its own herdr tab, with a written brief, a one-line status contract, and a close that refuses to destroy unfinished work. |
| [**aboufama/claude-agents-tmux**](https://github.com/aboufama/claude-agents-tmux) | Runs Claude Code agents side by side in persistent project workspaces using Herdr TUI or tmux. |
| [**maoxiaoke/tmux-agents**](https://github.com/maoxiaoke/tmux-agents) | Displays live agent states in tmux status bars with hotkey jumping for Claude Code sessions. |
| [**ykawase1011/hanchou**](https://github.com/ykawase1011/hanchou) | Provides a durable multi-agent control plane built on Herdr, Beads, Codex, and Claude Code. |
| [**suleymanozkeskin/sheppard**](https://github.com/suleymanozkeskin/sheppard) | Controls plane with collab & communication tools for agents from multiple harnesses, built on herdr api. |

### Claude Code: Account switchers and auth monitors

*5 projects. Tools for managing Claude multi-account rotation, OAuth keys, and quota monitoring.*

| Project | What it does |
|---|---|
| [**uwuclxdy/clauth · herdr-plugin**](https://github.com/uwuclxdy/clauth/tree/mommy/herdr-plugin) | Manages Claude Code accounts and usage from a Herdr TUI popup and tags panes with their active account. |
| [**wazum/herdr-grazr**](https://github.com/wazum/herdr-grazr) | Provides a simple and reliable auto account switcher for Claude Code: rotates to a fresh account before the 5-hour or weekly rate limit hits, so no pane ever stops at the usage quota. A Herdr plugin. |
| [**rcosteira79/herdr-account-switch**](https://github.com/rcosteira79/herdr-account-switch) | Switches Claude Code and Codex account profiles from a Herdr overlay or keybinding and labels panes with the active account. |
| [**aodanchenko/herdr-claude-usage**](https://github.com/aodanchenko/herdr-claude-usage) | Shows Claude Code plan usage and reset times in the Herdr TUI tab bar and a multi-account popup dashboard. |
| [**supex0fan/herdr-claude-swap**](https://github.com/supex0fan/herdr-claude-swap) | Resumes each Claude Code pane through the claude-swap account that owns its existing session. |

### Pi supervisor workflows and extensions

*91 projects. Supervision harnesses, task planners, and extensions for Pi agents in Herdr.*

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
| [**tobi/pi-herdr-workers**](https://github.com/tobi/pi-herdr-workers) | Opens Pi worker agents in neighboring Herdr TUI panes with `/team`, loop wakeups, and monitor tools. |
| [**MikkelKappelPersson/pi-shepherd**](https://github.com/MikkelKappelPersson/pi-shepherd) | Launches and coordinates specialized Pi agents in visible Herdr TUI panes, with shared fieldnotes for context. |
| [**joelhooks/herdr-pings**](https://github.com/joelhooks/herdr-pings) | Adds turn-completion alerts and crash detection for Pi agents in Herdr. A Pi extension and companion wait command track workers, while short call signs make concurrent agents easier to identify. |
| [**July24/pier**](https://github.com/July24/pier) | Adds a todo loop and interactive Pi subagents backed by herdr-core terminals, optionally displayed in the Herdr app. |
| [**sting8k/pi-peer**](https://github.com/sting8k/pi-peer) | Lets Pi sessions exchange peer messages and read recent conversation events within a shared Herdr TUI workspace. |
| [**darjss/herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate) | Orchestrates visible Pi workers in Herdr with a run board, persistent reports, isolated Git worktrees, and model routing. |
| [**Jackliu-miaozi/pi-herdr-workflow-kit**](https://github.com/Jackliu-miaozi/pi-herdr-workflow-kit) | Creates a controlled Pi workflow with separate planner, coder, and reviewer panes. Plans must be approved before coding, each phase is reviewed, and large handoffs are stored in `.pi-herdr/` files instead of pasted into the terminal. |
| [**nourhelmi/pi-meta-harness**](https://github.com/nourhelmi/pi-meta-harness) | Organizes Pi coding work around an advisor, builders, and optional reviewers, using Herdr and Git worktrees for delegation. |
| [**kirel/herdr-subagents**](https://github.com/kirel/herdr-subagents) | Starts each Pi subagent in its own Herdr pane or tab, manages session files, and notifies the parent when work finishes. Panes remain available for follow-up, and different subagents may use different models. |
| [**joshka0/herdr-watcher**](https://github.com/joshka0/herdr-watcher) | Tracks detached or long-running work and resumes the relevant agent when a background task completes. It uses the Herdr socket API to support workflows that must survive disconnects and interrupted sessions. |
| [**leset0ng/pi-todo-herdr**](https://github.com/leset0ng/pi-todo-herdr) | Tracks hierarchical Pi tasks with a live widget and optionally shows the current task in the Herdr TUI sidebar. |
| [**SuzuyaBish/foreman**](https://github.com/SuzuyaBish/foreman) | Runs a Pi foreman that delegates tasks to crew agents in separate Herdr TUI workspaces and Git worktrees. |
| [**NickPittas/pi-herdr-subagents**](https://github.com/NickPittas/pi-herdr-subagents) | Monitors Pi's asynchronous subagents and shows their IDs, tasks, states, and session files in a TUI. It can open or focus a subagent session, or start one in a pane, without changing how Pi runs it. |
| [**YunosukeYoshino/pi-herdr**](https://github.com/YunosukeYoshino/pi-herdr) | Spawns role-based Pi child agents in neighboring Herdr TUI panes for visible delegation and follow-up. |
| [**maxedapps/pi-herdr-sidetrack**](https://github.com/maxedapps/pi-herdr-sidetrack) | Clones a Pi conversation into an interactive Herdr TUI side pane while keeping the same checkout. |
| [**TyRichards/pi-mega-brief**](https://github.com/TyRichards/pi-mega-brief) | Organizes a weekly task list into persistent Pi sessions and Herdr TUI tabs for multi-agent work. |
| [**sfsajid91/omp-orchestrator**](https://github.com/sfsajid91/omp-orchestrator) | Delegates Oh My Pi tasks to isolated workers in Herdr tabs with selectable model routes. |
| [**wayne930242/pi-straw-boss**](https://github.com/wayne930242/pi-straw-boss) | Coordinates Pi agents across Herdr TUI tabs using a main agent per tab and a tower per workspace. Opens a browser view for monitoring agents and answering their questions. |
| [**SecretAardvark/pi-overseer**](https://github.com/SecretAardvark/pi-overseer) | Runs implementer, tester, reviewer, and researcher agents under one supervisor. Each role has command limits, sensitive actions require approval, and task state is saved under `.pi/overseer/` so work can resume after a restart. |
| [**getpipher/cursor**](https://github.com/getpipher/cursor) | Provides a focus-aware, customizable editor cursor for Pi coding agents running across Ghostty, tmux, and Herdr. |
| [**giacolees/plan-herdr-subagents**](https://github.com/giacolees/plan-herdr-subagents) | Provides a unified Pi workflow package combining grilling, pointer plans, sequential workers, and reviewers on Herdr subagents. |
| [**L1aoXingyu/pi-herdr-multi-agent**](https://github.com/L1aoXingyu/pi-herdr-multi-agent) | Launches multi-model agent fleets in visible Herdr TUI panes from Pi and harvests results with a watchdog. |
| [**CarrisHarter/herdr-omp-attach-panes**](https://github.com/CarrisHarter/herdr-omp-attach-panes) | Opens interactive Herdr TUI panes for Oh My Pi Vibe workers, with live transcripts and prompt input. Requires a fork of Oh My Pi with its attach client. |
| [**WyvernMonarch/herdr-cockpit**](https://github.com/WyvernMonarch/herdr-cockpit) | Provides a local-first supervision and control layer for Herdr coding agents. |
| [**aaaxn/pi-herdr-live-agents**](https://github.com/aaaxn/pi-herdr-live-agents) | Runs visible Pi subagents in Herdr TUI panes and returns their results to the parent session. |
| [**anrunt/herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader) | Reloads or restarts idle Pi sessions from a Herdr TUI popup without changing the tiled layout. |
| [**hao1939/herdr-supervisor**](https://github.com/hao1939/herdr-supervisor) | Supervises existing Herdr TUI workers against explicit goals and can wake workers when external events change. |
| [**markpinero/pi-suggested-tasks**](https://github.com/markpinero/pi-suggested-tasks) | Shows suggested parallel tasks in Pi and opens accepted work in a sibling session, optionally using Herdr TUI panes and worktrees. |
| [**ryuzdev/pi-opener**](https://github.com/ryuzdev/pi-opener) | Provides the Pi extension that opens files in your real editor. |
| [**maxedapps/pi-herdr-fork**](https://github.com/maxedapps/pi-herdr-fork) | Forks a Pi conversation into a new focused Herdr TUI pane without interrupting the original session. |
| [**ericjuta/omp-fleet**](https://github.com/ericjuta/omp-fleet) | Observes an existing Oh My Pi worker fleet in Herdr and records durable status and terminal reports. |
| [**reoring/sheltie**](https://github.com/reoring/sheltie) | Coordinates manifest-declared OMP agent teams in Herdr workspaces using durable SQLite messaging. |
| [**xenking/omp-extensible-workflows**](https://github.com/xenking/omp-extensible-workflows) | Supervises dependency-aware Beads tasks with OMP workers in isolated Git worktrees and Herdr tabs. |
| [**jrx2-dev/herdr-sub-agents**](https://github.com/jrx2-dev/herdr-sub-agents) | Lets Pi spawn, message, and close Pi or Claude Code subagents in Herdr TUI and react to their lifecycle events. |
| [**ooiyeefei/pixtension · extensions/pichestrator**](https://github.com/ooiyeefei/pixtension/tree/HEAD/extensions/pichestrator) | Runs guarded Pi subagents in Git worktrees and Herdr TUI, with a bash guard for credentials, production data, and destructive commands. |
| [**neilwashere/herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable) | Watches Pi sessions for terminal-provider failures and attempts recovery automatically. It confirms the problem from transcripts, shows a countdown, and can submit a continue command up to three times. |
| [**muslihudindev/herdr-agent-orchestrator**](https://github.com/muslihudindev/herdr-agent-orchestrator) | Coordinates multiple Pi software-engineering agents across isolated Herdr panes. |
| [**yanekyuk/pi-herdr-orchestrator**](https://github.com/yanekyuk/pi-herdr-orchestrator) | Coordinates project-independent Pi workers in visible Herdr TUI panes using `pi-goal` and lifecycle events. |
| [**alessandrofogli/pi-fleet**](https://github.com/alessandrofogli/pi-fleet) | Delegates Pi tasks to independent Herdr TUI sessions with isolated worktrees and shared task state. |
| [**Jalzn/pi-herdr-agents**](https://github.com/Jalzn/pi-herdr-agents) | Runs bounded autonomous Pi campaigns in Herdr TUI workspaces, including parallel campaigns and read-only observation. |
| [**oldflag2333333/pi-facets**](https://github.com/oldflag2333333/pi-facets) | Delegates Pi tasks to context-isolated specialist profiles in separate Herdr TUI tabs and returns their findings. |
| [**gitUmaru/pi-session-agents**](https://github.com/gitUmaru/pi-session-agents) | Spawns independent Pi subagent sessions in Herdr TUI tabs or as headless background sessions when Herdr is unavailable. |
| [**blisk92/pi-herdr-orchestrator**](https://github.com/blisk92/pi-herdr-orchestrator) | Orchestrates Pi sub-agents as Pi processes running in Herdr panes. Sibling to pi-herdr-agents with deliberate differences. |
| [**geniusgordon/pi-herdr-crew**](https://github.com/geniusgordon/pi-herdr-crew) | Dispatches and manage pi subagents as a Herdr crew. Each member answers through a markdown file, not the terminal. |
| [**MrBenJ/pi-herdr**](https://github.com/MrBenJ/pi-herdr) | Controls Herdr TUI workspaces, tabs, panes, and agents from Pi through agent-callable tools. The README marks the project pre-release and says live smoke testing is pending. |
| [**Pfgoriaux/pi-dispatch**](https://github.com/Pfgoriaux/pi-dispatch) | Delegates Pi tasks to parallel or sequential workers and shows their hierarchy in Herdr TUI. Writer tasks use isolated Git worktrees. |
| [**duskoide/pi-herdr-worker**](https://github.com/duskoide/pi-herdr-worker) | Spawns Pi workers in Herdr TUI tabs or split panes and schedules parallel tasks by their declared file paths. |
| [**itc-steve/pi-herdr**](https://github.com/itc-steve/pi-herdr) | Delegates Pi tasks to named, model-configured workers in Herdr TUI panes, with concurrency and file-ownership controls. |
| [**gbozee/pi-pstack**](https://github.com/gbozee/pi-pstack) | Provides a native Pi port of poteto/pstack with multi-model routing, pi-subagents, Herdr, and Intercom integration. |
| [**dulvac/pi-team-panes**](https://github.com/dulvac/pi-team-panes) | Runs interactive Pi team workers in Herdr TUI panes or iTerm2 splits, with shared tasks and mailbox messages. |
| [**matifuentes2/pi-parallel-go-pr-herdr**](https://github.com/matifuentes2/pi-parallel-go-pr-herdr) | Runs parallel worktree-backed Pi PR agents in background Herdr tabs. |
| [**tigorlazuardi/pi-herdr-sudo-task**](https://github.com/tigorlazuardi/pi-herdr-sudo-task) | Runs reviewed privileged tasks in a dedicated Herdr TUI pane after separate Pi and pane confirmations. |
| [**Gabriel-Cervo/Pi-Herdr-Subagents**](https://github.com/Gabriel-Cervo/Pi-Herdr-Subagents) | Provides a native in-process subagents for Pi with configurable models and smart result joining. |
| [**didy-kpn/pi-herdr-taskforce**](https://github.com/didy-kpn/pi-herdr-taskforce) | Coordinates role-based Pi teams in Herdr TUI workspaces through an asynchronous SQLite message box. |
| [**yanekyuk/pi-plain-herdr**](https://github.com/yanekyuk/pi-plain-herdr) | Creates a Herdr TUI workspace and Git worktree for a Pi writer, then supports independent review and verification. |
| [**chrishiguto/pi-herdr-subagents**](https://github.com/chrishiguto/pi-herdr-subagents) | Launches Pi subagents in dedicated Herdr panes for delegated tasks. |
| [**v3rse/pi-agent-swarm**](https://github.com/v3rse/pi-agent-swarm) | Runs asynchronous Pi subagents in Herdr TUI panes, with tmux, Zellij, and WezTerm backends also supported. |
| [**andrewfung729/pi-herdr-subagents**](https://github.com/andrewfung729/pi-herdr-subagents) | Spawns asynchronous Pi subagents in Herdr TUI panes and steers completed results back to the parent session. |
| [**DeharengOlivier/herdr-cockpit**](https://github.com/DeharengOlivier/herdr-cockpit) | Provides a WezTerm configuration that turns your terminal into a dedicated cockpit for AI coding agents, driven by Herdr. |
| [**itisbryan/pi-blanche**](https://github.com/itisbryan/pi-blanche) | Runs a crew of Pi planner, researcher, worker, and reviewer sessions in Herdr TUI panes using pi-intercom. |
| [**yajiefeng/pi-ticket-dispatcher**](https://github.com/yajiefeng/pi-ticket-dispatcher) | Dispatches approved tickets to Herdr TUI Pi workers for implementation, review, revision, and integration. |
| [**piotrekd00/pi-master-orchestrator**](https://github.com/piotrekd00/pi-master-orchestrator) | Moves one implementation ticket through a visible Pi worker and reviewer pair in Herdr TUI. |
| [**lfsmoura/pi-interactive-subagents-herdr**](https://github.com/lfsmoura/pi-interactive-subagents-herdr) | Runs interactive Oh My Pi subagents concurrently in Herdr TUI panes and returns their results to the parent. |
| [**maxedapps/pi-subagents-herdr**](https://github.com/maxedapps/pi-subagents-herdr) | Delegates Pi work to persistent child sessions in Herdr TUI panes, with agent profiles and optional worktree isolation. |
| [**bstncartwright/pi-bstn-subagents**](https://github.com/bstncartwright/pi-bstn-subagents) | Runs persistent Cursor ACP subagents from Pi with live Herdr viewers. |
| [**Nabsku/herdr-pi-subagents**](https://github.com/Nabsku/herdr-pi-subagents) | Opens a Herdr TUI pane with a read-only Pi child transcript for the matching pi-subagents fork. |
| [**Githubwujinming/pi-guardian**](https://github.com/Githubwujinming/pi-guardian) | Monitors a Herdr TUI worker pane from Pi, responds to recognized prompts, and escalates questions or stalls. |
| [**taecontrol/pi-herdr**](https://github.com/taecontrol/pi-herdr) | Lets Pi inspect and control Herdr TUI workspaces, tabs, panes, agents, and worktrees through callable tools. |
| [**namtx/pi-herd**](https://github.com/namtx/pi-herd) | Lets Pi spawn, prompt, wait for, inspect, and close child agents in Herdr TUI workspaces. |
| [**kodicw/pi-herdr**](https://github.com/kodicw/pi-herdr) | Lets Pi manage Herdr TUI workspaces, tabs, and panes and coordinate agents through callable tools. |
| [**gpxl-dev/pi-herdr-split**](https://github.com/gpxl-dev/pi-herdr-split) | Opens parallel forked Pi sessions in Herdr panes and tabs. |
| [**yaukwan/pi-extensions**](https://github.com/yaukwan/pi-extensions) | Runs persistent shell commands and delegated Pi agents in Herdr panes through installable Pi extensions. |
| [**fpigeonjr/herdr-course**](https://github.com/fpigeonjr/herdr-course) | Provides a self-paced course for herding the pi coding agent with Herdr. |
| [**jhsu/pi-herdr-btw**](https://github.com/jhsu/pi-herdr-btw) | Opens a Pi side conversation in a Herdr split with `/btw` and merges a summary back into the parent session. |
| [**wujunchuan/pi-fork-session-herdr**](https://github.com/wujunchuan/pi-fork-session-herdr) | Provides a Pi extension that forks the current persisted session into a new Herdr pane without replacing or stopping the Pi session in the original pane. |
| [**lalanikarim/herdr-skills**](https://github.com/lalanikarim/herdr-skills) | Teaches Pi to manage Herdr workspaces and run an orchestrator and worker in separate panes. |
| [**caina-barbosa/Herdr-orchestrator-bundle**](https://github.com/caina-barbosa/Herdr-orchestrator-bundle) | Coordinates visible Pi child sessions in Herdr with a watchdog, result handoff, and optional post-compaction resume. |
| [**leoszr/holistic-subagents**](https://github.com/leoszr/holistic-subagents) | Runs persistent Pi delegations in Herdr panes or worktrees with session event logs and authenticated callbacks. |
| [**conpiracy/ep-starter**](https://github.com/conpiracy/ep-starter) | Sets up a minimal Pi agent factory inside Herdr. |
| [**Phoobobo/taya**](https://github.com/Phoobobo/taya) | Initializes a workboard workflow and launches a Pi engineering assistant in Herdr TUI, with scheduled nudges for routine work. |
| [**Vistyy/pi-herdr-agents**](https://github.com/Vistyy/pi-herdr-agents) | Runs user-owned Pi agents in dedicated Herdr tabs. |

### Pi: Presence, memory, and status extensions

*8 projects. Persistent memory trackers, presence indicators, and live status displays for Pi agents.*

| Project | What it does |
|---|---|
| [**RamonsDka/gs3-sidebar**](https://github.com/RamonsDka/gs3-sidebar) | Shows a read-only sidebar for Pi and Gentle Shell in Herdr TUI, including agent status, context, Git and subagents. |
| [**edxeth/herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree) | Shows Pi agents and their subagents as a Herdr TUI sidebar tree with worktree branches and Git status. |
| [**hanbong5938/herdr-omp-subagents**](https://github.com/hanbong5938/herdr-omp-subagents) | Shows the active Oh My Pi main-agent and subagent models in the Herdr TUI sidebar. |
| [**spi-ca/pi-herdr-presence**](https://github.com/spi-ca/pi-herdr-presence) | Extends Pi agent presence indicators and runtime status inside Herdr workspaces. |
| [**Attamusc/pi-herdr**](https://github.com/Attamusc/pi-herdr) | Reports Pi lifecycle states to Herdr TUI so its sidebar shows working, blocked, done, and idle agents. |
| [**larryboiNEUQ/pi-herdr-ui-bridge**](https://github.com/larryboiNEUQ/pi-herdr-ui-bridge) | Reports blocking Pi extension prompts as Herdr agent blocked states so notification plugins can alert users. |
| [**BrianM0330/pi-herdr-snooze**](https://github.com/BrianM0330/pi-herdr-snooze) | Adds a forced snooze state to Pi agents in Herdr, controlled through `/snooze` or a key binding and independent of the underlying agent type. |
| [**markbrutx/pif-herdr-reporter**](https://github.com/markbrutx/pif-herdr-reporter) | Reports working and idle states from the pif coding agent to its Herdr TUI pane and releases the agent on exit. |

### Subagent launchers and delegation

*81 projects. Tools that launch workers, delegate tasks, and exchange messages between agents.*

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
| [**GavinTomlins/herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent) | Mirrors oh-my-openagent delegations into Herdr panes or tabs as they happen. It records live state and full scrollback transcripts, supports split or tabbed layouts, and does not change the agents' execution. |
| [**scotthuang/agent-knock-knock**](https://github.com/scotthuang/agent-knock-knock) | Lets OpenClaw, Pi or DeepSeek Harness delegate to existing Claude Code and Codex sessions in Herdr TUI and follow their progress. |
| [**hungv47/herdr-agent-orchestration**](https://github.com/hungv47/herdr-agent-orchestration) | Provides a captain-and-worker workflow for Hermes, Codex, Grok, OpenCode, and Cline agents in Herdr. |
| [**andybarilla/herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt) | Connects agents in a shared Herdr session chat room with a human-readable TUI. |
| [**jeffory/herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie) | Delegates work from an orchestrator to Claude, OpenCode, or Antigravity sessions in separate Herdr tabs and worktrees. File-based handoffs and completion signals return results to the parent. |
| [**cyperx84/herdr-loop**](https://github.com/cyperx84/herdr-loop) | Runs iterative planner, coder, and reviewer graphs across Claude Code, Codex, OpenCode, and Pi panes. Socket events and pane output are used to pass intermediate results until the workflow reaches its stopping condition. |
| [**IsaiasZc/herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a) | Delegates tasks to Codex, Claude, or OpenCode agents in Herdr through a CLI or the A2A protocol. |
| [**justn-hyeok/brgr**](https://github.com/justn-hyeok/brgr) | Lets a Codex or Claude Code session hand tasks to Claude Code, Codex, Gemini CLI, Copilot CLI, OpenCode, Pi, and other workers in split Herdr panes, answering their trust and update prompts. Each result comes back sealed for the lead agent to accept or reject; deciding closes the pane and removes the worktree when nothing would be lost. |
| [**anhnd3005-infinity/herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) | Dispatches tasks to CLI agent workers via Herdr panes with stateful task tracking, worktree isolation, and diff-based review. |
| [**LZHcode1986/herdr-link**](https://github.com/LZHcode1986/herdr-link) | Connects agents in a Herdr workspace for peer discovery, typed messages, agent startup, and pane cleanup. |
| [**minhtran3124/Brichan**](https://github.com/minhtran3124/Brichan) | A repository-local AI chief of staff for Codex. It keeps project work bounded, coordinates Herdr agents, checks outputs, and stores durable project memory. |
| [**gustavocaiano/opencode-herdr**](https://github.com/gustavocaiano/opencode-herdr) | Opens a Herdr pane when OpenCode creates a subagent and attaches the subagent session for live viewing. |
| [**arvkonstantin/herdr-codex-subagents**](https://github.com/arvkonstantin/herdr-codex-subagents) | Opens temporary read-only Herdr panes for Codex subagents and closes them when their work finishes. |
| [**makyinmars/muster**](https://github.com/makyinmars/muster) | Provides a native macOS command center for coding agents powered by Herdr and Ghostty. |
| [**upstash/herdr-upstash-box**](https://github.com/upstash/herdr-upstash-box) | Runs Claude Code, Codex, or OpenCode in an Upstash Box from a Herdr TUI worktree and applies changes back as a Git patch. |
| [**bekto/omp-herdr-panes**](https://github.com/bekto/omp-herdr-panes) | Opens read-only Herdr TUI panes that stream each oh-my-pi subagent’s tool calls and output until it finishes. |
| [**tinypi-extension/tinysubagent**](https://github.com/tinypi-extension/tinysubagent) | Spawns Pi subagents in Herdr TUI panes from Markdown roles and returns their results to the parent session. |
| [**zqkra/cbds**](https://github.com/zqkra/cbds) | Dispatches tasks between Herdr agent panes and records durable worker reports with bounded waits for results. |
| [**imdigitalashish/pane-sheepdog**](https://github.com/imdigitalashish/pane-sheepdog) | Provides a Codex skill for herding sibling AI coding agents across Herdr panes: fan-out delegation, shared-pane safety, and a supervisor that wakes a sleeping orchestrator. |
| [**FunnyQ/q-workbench**](https://github.com/FunnyQ/q-workbench) | Launches Claude Code, Codex, and OpenCode in Herdr TUI layouts and offers project and SSH pickers and agent restart actions. |
| [**arDaraz/crewboss**](https://github.com/arDaraz/crewboss) | Spawns and supervises coding agents in separate Herdr windows and Git worktrees, with commands to wait, message, and reopen them. |
| [**msadig/herdr-peer-agents-skill**](https://github.com/msadig/herdr-peer-agents-skill) | Teaches Claude, Pi, or Codex to start a named peer agent, assign work, and collect its result. A shell wrapper handles common startup failures and Codex input quirks. |
| [**KarthusLorin/herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator) | Runs an interactive agent turn in a separate Herdr pane and waits locally for the result without repeated model polling. |
| [**peterferguson/herdr-herd-flow**](https://github.com/peterferguson/herdr-herd-flow) | Routes handoffs to Claude, Codex, or OpenCode and launches each in a named Herdr tab, optionally in a worktree. |
| [**asermax/herdr-subagents**](https://github.com/asermax/herdr-subagents) | Lets Claude Code and Pi delegate work to other coding agents spawned as Herdr tabs. |
| [**sefuzhou770801-hub/herdr-dispatch-skill**](https://github.com/sefuzhou770801-hub/herdr-dispatch-skill) | Dispatches tasks to agent workbenches across Herdr panes. |
| [**machine-machine/ask-fable-skill**](https://github.com/machine-machine/ask-fable-skill) | Delegates tasks from Hermes or Claude Code to a Claude Code Fable 5 worker in a separate Herdr pane. |
| [**eliebak/herdr-agent-island**](https://github.com/eliebak/herdr-agent-island) | Coordinates multiple agent loops in separate Herdr panes and tracks their active tasks. |
| [**yigitkonur/claude-code-herdr-plugin**](https://github.com/yigitkonur/claude-code-herdr-plugin) | Controls a Codex subagent from start to finish through one tool backed by the Herdr multiplexer. |
| [**EDMND-SRC/herdr-subagents**](https://github.com/EDMND-SRC/herdr-subagents) | Starts subagents in named Herdr panes. It includes automatic interception, delegation tools, and a grid layout that adapts as workers are added. |
| [**marv1nnnnn/pi-yahe**](https://github.com/marv1nnnnn/pi-yahe) | Provides a composable Pi tool for visible task-based multi-agent work that steers async results back to the parent. |
| [**MinhDuyDEV/pi-subagents**](https://github.com/MinhDuyDEV/pi-subagents) | Provides a Pi delegation runtime with claims, leases, context packs, and diagnostic retry handling in Herdr. |
| [**regenrek/codex-orchestration-herdr**](https://github.com/regenrek/codex-orchestration-herdr) | A reusable Codex Sol/Luna orchestration skill that assigns workers through Herdr and reuses panes in a predictable way. |
| [**sh1ny/herdr-switchyard**](https://github.com/sh1ny/herdr-switchyard) | A human-approved Hermes and Herdr workflow for isolated OMP coding workers, using Beads as the persistent task ledger. |
| [**fuad-daoud/relay**](https://github.com/fuad-daoud/relay) | Automates the plan/report handoff between planner and builder AI coding agent panes running under herdr. |
| [**tamdogood/herdr-orc**](https://github.com/tamdogood/herdr-orc) | Provides a minimal, profile-driven custom orchestrator for Herdr. |
| [**devops-fj/herdr-handoff**](https://github.com/devops-fj/herdr-handoff) | Previews and sends terminal output and Git context between Herdr agents after explicit confirmation. |
| [**maccie01/herdr-axi**](https://github.com/maccie01/herdr-axi) | Delegates and supervises tasks across Herdr worker tabs with bounded concurrency and recoverable handoffs. |
| [**Jiaofeisiling/herdr-task-bridge**](https://github.com/Jiaofeisiling/herdr-task-bridge) | Bridges Windows and NeSI Herdr Sentinel tasks with asynchronous delegation, an SQLite queue, and a PowerShell CLI. |
| [**flotob/herdr-peer**](https://github.com/flotob/herdr-peer) | Sends tasks to existing Herdr agents on other machines over SSH and retrieves explicit replies. |
| [**SuperInstance/herdr-cocapn**](https://github.com/SuperInstance/herdr-cocapn) | Provides herdr + cocapn-core: agent multiplexer meets fleet management. Automatic tier escalation and deadband triggers for herdr agents. |
| [**tuong-nguyen-vn/personal-assistant-template**](https://github.com/tuong-nguyen-vn/personal-assistant-template) | Provides a bootstrap template for a personal coordinator agent with Herdr delegation skills. |
| [**impeterwayne/herdr_launcher**](https://github.com/impeterwayne/herdr_launcher) | Opens a toggleable sidebar to launch coding agents in Herdr TUI. |
| [**phillipleblanc/ad**](https://github.com/phillipleblanc/ad) | Sends messages between local Herdr agent tabs through a filesystem mailbox. |
| [**SynthSwarm/herdr-envoy**](https://github.com/SynthSwarm/herdr-envoy) | Delegates tasks to peer OpenCode agents in isolated Git worktrees and Herdr panes or child workspaces. |
| [**kowloonzh/agenthub**](https://github.com/kowloonzh/agenthub) | Broadcasts messages simultaneously to Codex and Claude Code sessions across Herdr panes via a single-binary TUI. |
| [**vivainio/cop-pilot**](https://github.com/vivainio/cop-pilot) | Delegates coding tasks to GitHub Copilot CLI agents in Herdr panes and collects their results asynchronously. |
| [**regrow1123/herdr-pi-delegation**](https://github.com/regrow1123/herdr-pi-delegation) | Adds a Hermes to Pi delegation workflow across Herdr panes with event-based completion. |
| [**mcdonc/mcdonc-pi-herdr**](https://github.com/mcdonc/mcdonc-pi-herdr) | Makes Pi's background work visible in Herdr. `/bg` moves the current task into a pane, while `/tab` forks the conversation into a new tab through the socket API. |
| [**noor-latif/herd**](https://github.com/noor-latif/herd) | Two scripts that create a project-specific Herdr workspace with a configurable grid of Pi agents. The workspace follows the current directory and restarts dead agents when the project is reopened. |
| [**JLighter/herdr-spawn**](https://github.com/JLighter/herdr-spawn) | Starts coding agents in separate Herdr panes and creates an isolated Git worktree for each one. Commands are provided for assigning work, checking jobs, and collecting completed results. |
| [**thkt/herdr-agentchat**](https://github.com/thkt/herdr-agentchat) | Coordinates a two-agent leader-and-coder conversation between Claude Code and Codex with send-and-wake sync. |
| [**aerain/herdr-agent-orchestration**](https://github.com/aerain/herdr-agent-orchestration) | Provides a pane-based orchestration skill for OMP and Claude Code running in Herdr. |
| [**lucasdeprit/Puppy**](https://github.com/lucasdeprit/Puppy) | A basic multi-agent system built around Claude Code sessions running in the Herdr terminal. |
| [**Sebastiangmz/herdr-plus**](https://github.com/Sebastiangmz/herdr-plus) | Teaches coding agents to operate Herdr and delegate work to subagents in Herdr spaces. |
| [**goatbjh/pi-herdr-claude-subagents**](https://github.com/goatbjh/pi-herdr-claude-subagents) | Enables Pi call Herdr-backed Claude sessions directly as an oracle, reviewer, or planner. |
| [**shimo4228/herdr-toolkit**](https://github.com/shimo4228/herdr-toolkit) | Starts detached Claude Code sessions in Herdr panes and sends prompts to agents with delivery and completion checks. |
| [**Idan-Levin/herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review) | A Herdr workflow in which Codex implements changes, a security scan checks them, and a parent agent performs the final review. |
| [**evancetesha/mini-code-factory**](https://github.com/evancetesha/mini-code-factory) | Provides a deliberately small three-role SDLC software factory: OpenCode agents orchestrated through Herdr for persistent panes, agent state, and file-based handoffs. |
| [**bennettgarcia-hs/herdr-jail**](https://github.com/bennettgarcia-hs/herdr-jail) | Runs coding agents in yolo-jail sandboxes (per-workspace jails, enforcement, sidebar visualization, workspace jail menu). |
| [**weirdry/crew**](https://github.com/weirdry/crew) | Coordinates a lead agent and a different-model worker in sibling Herdr panes across bounded review rounds. |
| [**RooseveltAdvisors/herdr-floax-adapter**](https://github.com/RooseveltAdvisors/herdr-floax-adapter) | Provides tmux-floax-inspired retained floating scratch shell for Herdr. |
| [**TeXmeijin/herdr-codex-handoff**](https://github.com/TeXmeijin/herdr-codex-handoff) | Transfers active sessions directly to Codex in adjacent panes when Claude hits usage limits. |
| [**mahirocoko/direct-cli-skill**](https://github.com/mahirocoko/direct-cli-skill) | Runs Cursor, Antigravity, Codex, or Pi in visible Herdr panes and falls back to tmux when Herdr is unavailable. |
| [**i11v/orchestrate-skill**](https://github.com/i11v/orchestrate-skill) | Provides an Agent Skill for coordinating and actively steering subagents through Herdr across implementation, review, consultation, and log-monitoring workflows. |
| [**softwarecrafts/herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new) | Starts or resumes an agent session in the Herdr TUI workspace matching the current project, from a plugin or standalone CLI. |
| [**MomePP/herdr-agent-tab**](https://github.com/MomePP/herdr-agent-tab) | Opens a coding agent in a new tab of the current herdr space, on the checkout or a fresh git worktree. |
| [**leonho/herdr-new-task**](https://github.com/leonho/herdr-new-task) | Picks a project directory and starts a coding agent in a new Herdr TUI tab. |
| [**AndreGeng/herdr-worktree-dispatcher**](https://github.com/AndreGeng/herdr-worktree-dispatcher) | Dispatches coding tasks into temporary Git worktrees and starts an agent in each checkout. The public entry point is `scripts/dispatch.sh`, backed by a compiled TypeScript command-line implementation. |
| [**abet-v/omarchy-herdr-prompt**](https://github.com/abet-v/omarchy-herdr-prompt) | Opens a centered prompt overlay to start a Claude agent in a Herdr workspace. |
| [**potatoQi/herdr-focused-codex-fork**](https://github.com/potatoQi/herdr-focused-codex-fork) | Forks the Codex session in the focused Herdr TUI pane into a new pane to its right. |

### Autonomous coding and pull-request loops

*14 projects. Long-running workflows that implement changes, open pull requests, review results, and react to CI.*

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
| [**QuentinTorg/stagehand**](https://github.com/QuentinTorg/stagehand) | Coordinates author and reviewer agents across Herdr TUI worktrees and hands reviewed work to GitHub pull requests. |
| [**edbienes/drovr**](https://github.com/edbienes/drovr) | Runs a Herdr-based development loop with isolated implementation, a repository quality gate, two independent reviews, and a human-gated merge. |
| [**sarmientoF/herdr-pr-loop**](https://github.com/sarmientoF/herdr-pr-loop) | Runs tester, coder, and reviewer agents through local task cycles and GitHub pull-request reviews in separate tabs. State is stored in files, while approval gates, logs, a budget limit, and a pause file keep runs controllable. |
| [**henrywang/herdr-workflow**](https://github.com/henrywang/herdr-workflow) | Runs multi-agent Herdr TUI workflows with cross-model planning, adversarial review and bounded iterations toward pull requests. |

### Task queues, backlogs, and event triggers

*55 projects. Queues and event-driven systems that turn stored work into agent jobs.*

| Project | What it does |
|---|---|
| [**smarzban/herdr-tsk**](https://github.com/smarzban/herdr-tsk) | Shares a terminal task board between you and your agents with a TUI for humans and a CLI for agents. |
| [**smarzban/tsk**](https://github.com/smarzban/tsk) | Opens a shared task board in Herdr TUI and lets agents manage work through a CLI. |
| [**nelsonPires5/herdr-board**](https://github.com/nelsonPires5/herdr-board) | A Kanban TUI and background service that turns cards into prompts for agents in visible Herdr panes. Moving a card can create an agent, run it in a dedicated tab, and advance the work through review gates. |
| [**deimantasnork/captains-deck**](https://github.com/deimantasnork/captains-deck) | Displays a read-only Firstmate flow kanban board inside Herdr TUI. |
| [**DnzzL/herdr-automations**](https://github.com/DnzzL/herdr-automations) | Schedules recurring prompts and cron jobs that run agents in fresh Herdr worktrees. It supports task-specific MCP settings, collision protection, persistent run history, and a live monitoring board. |
| [**ivanarama/PromptPilot**](https://github.com/ivanarama/PromptPilot) | Queues and schedules prompts for coding CLIs through a web UI or Telegram bot, with Herdr-backed terminal sessions and retry on rate limits. |
| [**bon5co/bermuda**](https://github.com/bon5co/bermuda) | Schedules jobs as interactive agents in dedicated Herdr splits. It supports multi-step workflows, shared append-only discussion logs, and exclusive resource claims that remain valid across temporary sessions. |
| [**mrcndz/herdr-routines**](https://github.com/mrcndz/herdr-routines) | Runs scheduled routines on cron or interval timers by opening a tab in a chosen workspace and executing a command or starting an agent. |
| [**catoncat/herdr-trail**](https://github.com/catoncat/herdr-trail) | Collects shared agent follow-ups and blockers in a memo list that jumps back to the originating Herdr TUI conversation. |
| [**jasonrr/herdr-tally**](https://github.com/jasonrr/herdr-tally) | Keeps project-scoped todos, scratchpads and plans in a shared ledger for Herdr TUI users and agents. |
| [**marvingygas/spoolway**](https://github.com/marvingygas/spoolway) | Runs queued coding tasks through configurable Herdr TUI agent pipelines for Claude Code, Codex and Pi. |
| [**mikedclarke/herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd) | Runs cron routines, heartbeats, and recurring automation scripts in visible Herdr workspaces so background maintenance remains easy to inspect. |
| [**jwarykowski/shepherd**](https://github.com/jwarykowski/shepherd) | Runs a Markdown-backed task board in a Herdr TUI pane, tab, or overlay for people and coding agents. |
| [**KokiKono/herdr-kanban**](https://github.com/KokiKono/herdr-kanban) | Tracks tasks on a SQLite-backed terminal Kanban board and opens Herdr TUI tabs for in-progress tasks. |
| [**husniadil/herdr-sched**](https://github.com/husniadil/herdr-sched) | Schedules agent actions with cron, webhooks, and file-watcher triggers in Herdr. |
| [**omarjesusperezortiz/herdr-notion**](https://github.com/omarjesusperezortiz/herdr-notion) | Browses a Notion database in a Herdr TUI pane, changes page status, and sends tickets to agents. |
| [**hanbong5938/herdr-tab-autorun**](https://github.com/hanbong5938/herdr-tab-autorun) | Starts a configured shell command or coding agent in new Herdr TUI tabs using repository-scoped TOML rules. |
| [**MatheusBBarni/herdr-tasks**](https://github.com/MatheusBBarni/herdr-tasks) | Runs a kanban task board and `htasks` CLI that launch agents in Herdr panes and track their work. |
| [**GNURub/herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket) | Adds a durable, ordered prompt bucket for coding agents running in Herdr. |
| [**qluto/collie**](https://github.com/qluto/collie) | Adds an unattended-work box for Claude Code sessions on Herdr: toss tasks in by day, spend leftover token quota on them at night, collect the results in the morning. |
| [**rohanthewiz/herdr-todo**](https://github.com/rohanthewiz/herdr-todo) | Queues terminal prompts using Bubble Tea, letting you filter and paste them into Claude Code panes. |
| [**husniadil/herdr-tasks**](https://github.com/husniadil/herdr-tasks) | Tracks agent tasks and notes in Herdr TUI with renewable claims, evidence-backed review, and a human decision gate. |
| [**sazardev/herdr-code-board**](https://github.com/sazardev/herdr-code-board) | Dispatches agent prompts from a kanban queue into Herdr panes, workspaces, and worktrees, with rules that chain cards. |
| [**pjgeutjens/omarchy-feed-the-flock**](https://github.com/pjgeutjens/omarchy-feed-the-flock) | Queues typed or dictated Omarchy notes and delivers them to Herdr TUI agents when they are ready. |
| [**barkerja/herdr-msg**](https://github.com/barkerja/herdr-msg) | Adds persistent mailboxes for agents in Herdr TUI and notifies recipient panes when messages arrive. |
| [**aoprisan/hird**](https://github.com/aoprisan/hird) | Queues cross-harness agent work and stores shared assertions in SQLite. |
| [**husniadil/herdr-dispatch**](https://github.com/husniadil/herdr-dispatch) | Dispatches ready herdr-tasks board items to worker agents in Herdr panes and hands completed work to the review gate. |
| [**huketo/herdr-cron**](https://github.com/huketo/herdr-cron) | Schedules shell commands and coding-agent prompts to run in Herdr panes, with a CLI and terminal interface. |
| [**ram4-dev/herdr-automations**](https://github.com/ram4-dev/herdr-automations) | Runs scheduled or event-triggered agent jobs from cron expressions, intervals, and lifecycle hooks. It prevents overlapping runs, creates fresh Git worktrees, and records complete execution histories. |
| [**Eslsamu/herdr-tasks**](https://github.com/Eslsamu/herdr-tasks) | Keeps an agent-owned task queue linked to each Herdr space, with atomic claims, priorities, dependencies, and durable conversation ownership. An always-visible Herdr summary and local read-only browser view let people follow the work without maintaining cards. |
| [**dkta-labs/agentd**](https://github.com/dkta-labs/agentd) | Adds a minimal local supervisor for scheduled agent jobs and durable run evidence. |
| [**huntergdavis/dunkingsheep**](https://github.com/huntergdavis/dunkingsheep) | Keeps agents active by sending configured text to Herdr panes at regular intervals. |
| [**cantona/herdr-triggers**](https://github.com/cantona/herdr-triggers) | Watches Herdr TUI pane output for configured regular expressions and triggers actions such as notifications, subprocesses, or pane input. |
| [**aneym/unblock**](https://github.com/aneym/unblock) | Collects agent requests for human actions in a local queue, with a Herdr TUI launcher and secret handling outside model context. |
| [**duyet/herdr-desk**](https://github.com/duyet/herdr-desk) | Schedules manager agents in Herdr TUI worktrees to triage and work through repository backlogs. |
| [**yuanying/herdr-tasks**](https://github.com/yuanying/herdr-tasks) | Supervises task execution from start to finish across Herdr workspaces and worktrees. |
| [**AltanS/herdr-pouch**](https://github.com/AltanS/herdr-pouch) | Stores prompts for a Herdr TUI agent and inserts them into its input one at a time without submitting them. |
| [**DerekStride/agent-orchestrator**](https://github.com/DerekStride/agent-orchestrator) | Dispatches a dependency-scoped SQ task graph to OMP workers in Herdr sessions and isolated Git worktrees. |
| [**timjonez/slack-herd**](https://github.com/timjonez/slack-herd) | Starts Herdr-backed work from Slack bot mentions through the herd and slackcli command-line tools. |
| [**lufs-audio/snuze**](https://github.com/lufs-audio/snuze) | Schedules wake-up prompts for Herdr panes after timers, Jules conditions, pane state changes, or external signals. |
| [**lebryk/herdr-events**](https://github.com/lebryk/herdr-events) | Queues local JSON events for Herdr agents using native Codex, Claude Code, Pi, and OpenCode adapters. |
| [**terry-li-hm/herdr-bots**](https://github.com/terry-li-hm/herdr-bots) | Runs scheduled Claude Code or Pi jobs in fresh Herdr worktrees and collects their output in an evidence inbox. |
| [**TsukumiStudio/MornKanban**](https://github.com/TsukumiStudio/MornKanban) | Dispatches file-based Kanban cards to Claude Code and Codex workers in Herdr panes, with isolated worktrees and review. |
| [**lenaertsjan/herdr-factory-demo**](https://github.com/lenaertsjan/herdr-factory-demo) | Provides a small local-first task manager for end-to-end herdr-factory tests. |
| [**EricBois/herdr-nudge**](https://github.com/EricBois/herdr-nudge) | Schedules a continue prompt for a Herdr agent, either at a chosen time or when the agent becomes idle or blocked. |
| [**caner-akca/herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows) | Launches and monitor isolated Atomic workflow tasks, campaign board, sidebar tokens, run ledger, and an optional Telegram cockpit. |
| [**bxuserx/kerdr**](https://github.com/bxuserx/kerdr) | Adds a shared, mouse-driven kanban board for agents in a Herdr TUI space, stored in a `.tickets/` directory. |
| [**alex-devdone/herdr-sched**](https://github.com/alex-devdone/herdr-sched) | Schedules messages or commands for later delivery to a Herdr TUI pane using a persistent macOS LaunchAgent queue. |
| [**husniadil/herdr-mail**](https://github.com/husniadil/herdr-mail) | Sends asynchronous messages between agents in Herdr TUI panes, with tracked asks and replies and pane delivery markers. |
| [**amine2233/herdr-plugin-kanban**](https://github.com/amine2233/herdr-plugin-kanban) | Opens an fzf-driven kanban board in a Herdr TUI split to list and edit cards or draft them with Claude. |
| [**floco/herdr-claude-resume**](https://github.com/floco/herdr-claude-resume) | Detects Claude Code's five-hour rate limit and automatically resumes the session after the limit resets. |
| [**hassox/herdr-kanban**](https://github.com/hassox/herdr-kanban) | Shows Herdr TUI workspace panes as kanban cards, starts agents, and runs scripts when cards change columns. |
| [**aneym/herdr-routines**](https://github.com/aneym/herdr-routines) | Schedules Herdr TUI agent routines with a daemon and CLI. |
| [**zerodice0/herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin) | Schedules Herdr TUI agent prompts and local commands with one-time or recurring runs on macOS and Linux. |
| [**timjonez/herd-orchestrator-cli**](https://github.com/timjonez/herd-orchestrator-cli) | Watches Herdr TUI agents, queues attention events, and notifies you when a human decision is needed. Launches Claude in a new workspace and submits an initial prompt. |

### Linear, GitHub Issues, and issue-to-PR automation

*33 projects. Automated pipelines bridging issue trackers directly to Herdr agent workspaces and PRs.*

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
| [**kukv/octoscope**](https://github.com/kukv/octoscope) | Adds GitHub issue and pull-request management to Herdr, including review, tracking, and assignment of GitHub work to agent tabs from inside the terminal. |
| [**itisbryan/herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks) | Watches pull request CI in a Herdr pane and shows CI and merge status in the sidebar. |
| [**kiitosu/herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board) | Embeds a Jira Kanban board in a Herdr pane with one-key Claude Code session launching and live card status updates. |
| [**hanbong5938/herdr-jira-worktree**](https://github.com/hanbong5938/herdr-jira-worktree) | Opens Jira issues in Herdr TUI and creates Git worktrees or jj workspaces from them. Browse comments, change issue status, and delegate work to an agent. |
| [**tomoasleep/herdr-symphony**](https://github.com/tomoasleep/herdr-symphony) | Reads issues from GitHub Projects, creates `gwq` worktrees, and runs one OpenCode agent per issue inside Herdr workspaces. |
| [**bredebjorhovd/herdr-board**](https://github.com/bredebjorhovd/herdr-board) | Assigns GitHub issues to agents in dedicated Herdr panes and moves completed work into pull-request review. |
| [**matheus3301/herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut) | Lists assigned Shortcut stories in a terminal picker and launches the selected story in a new Herdr agent tab. |
| [**ZviBaratz/herdr-draft**](https://github.com/ZviBaratz/herdr-draft) | Provides a new-session creation dialog unifying Linear issues, worktree creation, agent types, and initial prompts. |
| [**H3xept/herdr-ingest**](https://github.com/H3xept/herdr-ingest) | Turns Sentry, Linear, or GitHub work items into Herdr TUI spaces and Git worktrees with agent briefs, waiting for user confirmation before starting an agent. |
| [**ukwhatn/taskherd**](https://github.com/ukwhatn/taskherd) | Tracks agent sessions, GitHub pull requests, and Jira tickets on a local task board that can jump to Herdr TUI sessions. |
| [**spiritsack/herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree) | Creates or reuses a ticket-specific Git worktree and prefills its Jira ID or URL into a coding agent in Herdr TUI. |
| [**brooswit-factory/butchr**](https://github.com/brooswit-factory/butchr) | Provides the software factory: watches your Jira, runs herdr agents on active tickets, pushes updates to them over MCP. |
| [**nyanyaon/github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin) | Browses the current repository’s open GitHub issues and comment threads in a read-only Herdr TUI pane. |
| [**abtris/herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr) | Checks the current branch's GitHub pull request against linked Jira tickets. It shows ticket state and warns when issue keys are missing or do not match, keeping Jira context visible in Herdr. |
| [**maimuzo/continuo**](https://github.com/maimuzo/continuo) | Turns GitHub Projects v2 cards into a queue for Claude Code workers in Herdr panes and updates board status after execution. |
| [**YuSa0-6/herdr-issue-flow**](https://github.com/YuSa0-6/herdr-issue-flow) | Creates Herdr workspaces and Git worktrees for GitHub issues, with Pi conductor and worker sessions and Hunk review handoff. |
| [**korvyashka/herdr-pr-relay**](https://github.com/korvyashka/herdr-pr-relay) | Picks pull requests and dispatches them to active agent sessions as review prompts. |
| [**hilmimuktitama/herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek) | Finds Jira Cloud issue keys in a Herdr TUI pane and opens read-only issue descriptions and comments alongside it. |
| [**NightingaleMedia/herdr-github-orobo**](https://github.com/NightingaleMedia/herdr-github-orobo) | Runs in a Herdr TUI split or tab and sends work to an existing agent or starts a new one. Its pull-request dashboard is being migrated. |
| [**jeremN/herdr-dispatch-plugin**](https://github.com/jeremN/herdr-dispatch-plugin) | Dispatches tickets through an AI-agent pipeline, one git worktree per ticket, each phase in a named pane, fail-closed, with a human approval gate. |
| [**hdtradeservices/ticketdeck**](https://github.com/hdtradeservices/ticketdeck) | Shows Linear projects and tickets in a terminal dashboard and launches or reattaches Claude Code sessions in Herdr TUI. |
| [**PanchTime/linear-widget**](https://github.com/PanchTime/linear-widget) | Displays Linear issues in an Omarchy bar widget and opens ticket worktrees or agent sessions in Herdr TUI. |
| [**Mamprim-go/sdlc-herdr**](https://github.com/Mamprim-go/sdlc-herdr) | Runs a GitHub issue workflow with Pi agents in Herdr TUI panes for triage, planning, implementation, review, and QA. |

### General workflows and skill packs

*60 projects. Reusable skills, commands, and opinionated setups for common agent workflows.*

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
| [**jwkicklighter/herdr-prompt-library**](https://github.com/jwkicklighter/herdr-prompt-library) | Browses and manages Markdown prompts and inserts their bodies into the focused Herdr TUI pane without submitting them. |
| [**xlinx/herdr-auto-yes-sir**](https://github.com/xlinx/herdr-auto-yes-sir) | Provides herdr-auto-yes-sir for non blocked running when agent ask for approve; like codex. |
| [**yangyang0507/herdr-skill**](https://github.com/yangyang0507/herdr-skill) | Refines Herdr agent coordination by replacing vague status polling with output markers and structured messages. Messages include sender, reply target, and task type, and a dependency-free `herdr-msg` Bash helper is included. |
| [**quan-meng/herdr-slurm**](https://github.com/quan-meng/herdr-slurm) | Connects Slurm allocations to Herdr by creating dedicated workspaces and monitored agent tabs for compute jobs. It tracks queue state and reports job and agent progress in the terminal. |
| [**hewenyu/herdr-agent**](https://github.com/hewenyu/herdr-agent) | An agent focused on managing Herdr and making development conversations easier from a phone. |
| [**calebcauthon/herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork) | Forks an agent session into a new Herdr pane by copying and pasting, either manually or through a hotkey. |
| [**mikhail-angelov/herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop) | Automates a repeated cross-review loop in which one agent writes changes and another reviews them inside the same Herdr workspace. |
| [**playsthisgame/herdr-x**](https://github.com/playsthisgame/herdr-x) | Browses x.com in a terminal split inside herdr, and draft posts in $EDITOR to send yourself. |
| [**jatingargiitk/herdr-memory**](https://github.com/jatingargiitk/herdr-memory) | Builds persistent project memory from agent actions, successful approaches, and earlier decisions across Herdr sessions, then adds relevant context to later prompts to reduce repeated mistakes. |
| [**MarsSall/gentle-herdr**](https://github.com/MarsSall/gentle-herdr) | Applies Gentle Shell themes and task-summary colors to Herdr TUI configurations across machines. |
| [**minqiyang/coordination-standard**](https://github.com/minqiyang/coordination-standard) | Coordinates coding agents in Herdr TUI using defined roles, isolated worker lanes, and review gates. |
| [**shaozk/herdr-shadow-pane**](https://github.com/shaozk/herdr-shadow-pane) | Provides a Herdr plugin, Shadow Clone Panel: Control multiple panels simultaneously. |
| [**agileandy/agent-multiplexer-skills**](https://github.com/agileandy/agent-multiplexer-skills) | Teaches coding agents to control Herdr and tmux panes, launch siblings, watch logs, and manage workspace layouts. |
| [**conpiracy/lzy-ad-factory**](https://github.com/conpiracy/lzy-ad-factory) | Creates a Herdr TUI workspace and Pi workflow for producing UGC ad scripts, prompts, QA, and export bundles. |
| [**jbaham2/herdr-plugin**](https://github.com/jbaham2/herdr-plugin) | Teaches Claude Code to orchestrate Herdr TUI agents, manage sessions and layouts, and monitor agent state. |
| [**zoridos/herdr-skill**](https://github.com/zoridos/herdr-skill) | Teaches coding agents to split Herdr TUI panes, spawn agents, send tasks, read output, and wait for state changes. |
| [**yelsed/herdr-pr**](https://github.com/yelsed/herdr-pr) | Provides a Todo of the pull requests waiting on you, in a herdr pane. Reads everything through the gh CLI. |
| [**macintacos/herdr-scratch**](https://github.com/macintacos/herdr-scratch) | Provides a toggleable scratch shell popup for Herdr backed by tmux state preservation. |
| [**zap0xfce2/herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart) | Runs a configured command in named panes on server startup. |
| [**andorexu/hermes-agent-skills-pack**](https://github.com/andorexu/hermes-agent-skills-pack) | Adds reusable Hermes Agent skills for reasoning, engineering, OCR, and web tasks to supported agents. |
| [**htlin222/herdr-agent-self-reload-skill**](https://github.com/htlin222/herdr-agent-self-reload-skill) | Re-prompts the agent in the current Herdr pane after a chosen delay. |
| [**astwys/herdr-quick-prompt**](https://github.com/astwys/herdr-quick-prompt) | Sends predefined prompts or ad hoc text to a Herdr TUI agent pane. |
| [**friendsfriend/agentic-coding · herdr-manager**](https://github.com/friendsfriend/agentic-coding/tree/main/agent-definitions/skills/herdr-manager) | Teaches an agent to manage OpenSpec implementation workspaces through Herdr TUI. |
| [**oguzcanhuner/shepherd**](https://github.com/oguzcanhuner/shepherd) | Runs configured coding workflows in Herdr panes, combining agent steps, scripts, retries, and recorded decisions. |
| [**parker-brown-family/herdr-auto-warm-cache**](https://github.com/parker-brown-family/herdr-auto-warm-cache) | Keeps an idle agent prompt cache warm by sending a message before it expires, while avoiding panes waiting for user input. |
| [**wazum/herdr-kibitzr**](https://github.com/wazum/herdr-kibitzr) | Asks your coding agent to review the comments it just wrote, so what explains something stays and the noise goes. A herdr plugin for Claude Code, Codex and any other agent, with no human in the loop. |
| [**tmastalirsch/herdr-claude-safe-compact**](https://github.com/tmastalirsch/herdr-claude-safe-compact) | Compacts idle Claude Code panes, but only once a handoff is safely on disk. |
| [**cheahhl814/herdr-lab**](https://github.com/cheahhl814/herdr-lab) | Teaches coding agents safe Herdr delegation, including verified completion and provider preflight. |
| [**creedants/pstack-portable**](https://github.com/creedants/pstack-portable) | Installs portable engineering skills for Codex, Claude Code, Grok Build, and Cursor Agent, including Herdr team coordination. |
| [**tenmomo/fleet-commander**](https://github.com/tenmomo/fleet-commander) | Teaches an operator to coordinate coding-agent fleets across Herdr workspaces, SSH hosts, and tmux panes. |
| [**kanwhile/herdr-skill**](https://github.com/kanwhile/herdr-skill) | Teaches Claude Code to drive Herdr TUI panes and agents using a CLI reference checked against the binary. |
| [**djbclark/claude-orchestration-skills**](https://github.com/djbclark/claude-orchestration-skills) | Teaches Claude Code to coordinate multi-agent handoffs through Herdr TUI and use Ralph TUI with Beads. |
| [**mev15/claude-config · skills/codex-review-loop**](https://github.com/mev15/claude-config/tree/HEAD/skills/codex-review-loop) | Runs external Codex CLI reviews from Claude Code with an interactive Herdr TUI pane or headless `codex exec` and a fix loop. |
| [**abhishek944/astack · skills/pi-herdr-skills**](https://github.com/abhishek944/astack/tree/main/skills/pi-herdr-skills) | Installs reusable Pi skills for planning, implementation, and Herdr-hosted agent workflows. |
| [**zbsdsb/herdr-codex-pi-workflow**](https://github.com/zbsdsb/herdr-codex-pi-workflow) | Installs agent skills for stateful Herdr coding workflows, evidence gates, and post-delivery triage. |
| [**shubham399/herdr-agents-auto-compact**](https://github.com/shubham399/herdr-agents-auto-compact) | Automatically compacts long Claude Code and OpenCode sessions in Herdr so they do not exhaust their context windows. |
| [**mithyer/ry-skill**](https://github.com/mithyer/ry-skill) | Collects Pi skills for Herdr-based workflows. |
| [**nativestrider/agent-control-skills**](https://github.com/nativestrider/agent-control-skills) | Coordinates Codex and Herdr workers with reusable skills for dispatch, lane ownership, reporting, and session recovery. |
| [**luweiCN/herdr-ops**](https://github.com/luweiCN/herdr-ops) | Adds natural-language workspace commands to Herdr's official skill. Requests such as creating a feature worktree are translated into CLI operations, including worktree actions not covered by the upstream skill, with detailed documentation loaded only when needed. |
| [**loopkeep/herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview) | Integrates the loopreview workflow with Herdr as a plugin. |
| [**TheShellLand/herdr-agent**](https://github.com/TheShellLand/herdr-agent) | A Herdr agent project with no further description in the source catalog. |
| [**MartinBspheroid/herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash) | A local, keyboard-first agent board showing active workers, semantic state, effective directory, Git context, and source-labelled activity. |
| [**zerodice0/herdr-agent-labels**](https://github.com/zerodice0/herdr-agent-labels) | Assigns readable color-and-animal names to Herdr agents that do not already have labels. |
| [**hisetu/herdr-agent-skill**](https://github.com/hisetu/herdr-agent-skill) | Adds integration support and dedicated helpers for using an agent skill inside Herdr sessions. |
| [**huketo/herdr-sheep**](https://github.com/huketo/herdr-sheep) | Watches your Herdr coding agents as a flock of animated ASCII sheep. |
| [**MatiasL13/herdr-k9s**](https://github.com/MatiasL13/herdr-k9s) | Runs K9s in its own Herdr tab with an fzf context picker and a read-only guard for production clusters. |
| [**cescofry/fixme**](https://github.com/cescofry/fixme) | Sends a failed shell command and its output to an interactive Pi session in a new Herdr TUI tab. |
| [**agneym/herdr-lfm-finetune**](https://github.com/agneym/herdr-lfm-finetune) | Trains a LiquidAI LFM2-350M LoRA adapter to answer Herdr TUI operation questions using a supplied notebook and data. |
| [**goern/bead-workflow-skills**](https://github.com/goern/bead-workflow-skills) | Starts and closes bead-driven work sessions using Herdr TUI tabs and Worktrunk worktrees, keeping tab and session labels aligned. |
| [**nmogil/agent-skill-patterns · herdr-claude-pr-lane**](https://github.com/nmogil/agent-skill-patterns/tree/main/skills/herdr-claude-pr-lane) | Teaches Claude Code to run pull-request-sized work in a Herdr TUI lane. |

---

## 2. Herdr app layouts, mods, and themes

*111 projects. Layouts, mods, and themes for customizing the Herdr desktop app.*

### Herdr app layouts

*47 projects. Whole-window layouts for organizing agents and workspaces in the Herdr app.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community extensions.

| Project | What it does |
|---|---|
| [**runkids/skillshare · herdr/skillshare**](https://github.com/runkids/skillshare/tree/main/herdr/skillshare) | Adds a Herdr app layout with a skillshare panel for viewing, auditing and syncing skills, agents, MCP servers, plugins and hooks. |
| [**eliasstravik/shepherdr**](https://github.com/eliasstravik/shepherdr) | Organizes coding agents in a Herdr app layout with per-space assistants and task cards, running tasks in separate worktrees. |
| [**JinJieBeWater/herdr-t3**](https://github.com/JinJieBeWater/herdr-t3) | Organizes Herdr app agents in an inbox that groups work by attention state and shows agents across machines. |
| [**jankeesvw/herdr-space-folders**](https://github.com/jankeesvw/herdr-space-folders) | Groups Herdr app spaces into colored, collapsible folders using drag-and-drop or project folder rules. |
| [**franky5440-afk/herdr-traveler**](https://github.com/franky5440-afk/herdr-traveler) | Turns the Herdr app into a pixel RPG with agent portraits, status bars, and machine buildings. |
| [**wobsoriano/herdr-sim**](https://github.com/wobsoriano/herdr-sim) | Opens an interactive iOS simulator or Android emulator beside code and terminals in the Herdr app. |
| [**quaresc/cockpit**](https://github.com/quaresc/cockpit) | Shows Herdr agents, their work, and items needing attention in an app layout or TUI plugin. |
| [**shellscape/herdr-whitby**](https://github.com/shellscape/herdr-whitby) | Organizes Herdr app spaces into a light project sidebar with nested agents, status dots, and an attention bell. |
| [**simoncrypta/bercail**](https://github.com/simoncrypta/bercail) | Adds the Bercail layout to the Herdr app for supervising agents across Git worktrees, with a desk pane for each space. |
| [**jankeesvw/herdr-issues**](https://github.com/jankeesvw/herdr-issues) | Adds a GitHub issues panel to the Herdr app for reading, commenting on, assigning, and closing issues. |
| [**jlopezlira/herdr-kanso**](https://github.com/jlopezlira/herdr-kanso) | Adds the Kanso horizontal-agent layout plus Markdown panel and editor-launcher mods to the Herdr app. |
| [**runkids/figlens · herdr**](https://github.com/runkids/figlens/tree/main/herdr) | Adds a figlens layout and panel for viewing local Figma designs and handing screens to agents in the Herdr app. |
| [**DustyPolk/herdr-office**](https://github.com/DustyPolk/herdr-office) | Shows coding agents as animated coworkers above Herdr app terminals and jumps to their sessions when clicked. |
| [**adamentwistle/orchi-build**](https://github.com/adamentwistle/orchi-build) | Adds an Orchi layout for managing Claude Code agents, tickets, agent status, and orchestration in the Herdr app. |
| [**munza/herdr-mods**](https://github.com/munza/herdr-mods) | Adds the Estro layout and a collection of Herdr app mods for Git, files, tabs, settings, Linear, pull requests, staged agent runs and Mac automation. |
| [**jkuepker/herdr-layouts**](https://github.com/jkuepker/herdr-layouts) | Collects Board, LCARS, and Slate layouts for organizing agents and workspaces in the Herdr app. |
| [**herunan/herdr-over9k**](https://github.com/herunan/herdr-over9k) | Collects the Over9k layout and launcher, sidebar, switcher, timeline, to-do, and usage mods for the Herdr app. |
| [**shafiqimtiaz/herdr-omarchy**](https://github.com/shafiqimtiaz/herdr-omarchy) | Adds an Omarchy-inspired Herdr app layout with tiled terminals, agent status, quota, Git panels, themes and wallpapers. |
| [**sgomez/herdr-triage**](https://github.com/sgomez/herdr-triage) | Adds a Herdr app layout with an attention inbox, agent replies, worktrees, Git history, pull requests and issues. |
| [**VladTemp27/herdr-orca**](https://github.com/VladTemp27/herdr-orca) | Adds a Herdr app layout with nested worktrees and agents, GitHub issues and pull requests, usage limits and file panels. |
| [**CiprianSpiridon/herdr-mission-control**](https://github.com/CiprianSpiridon/herdr-mission-control) | Adds Mission Control and Classic Herdr app layouts with mods for agent monitoring, Jira, GitHub, GitLab, sessions, tabs and worktree launches. |
| [**emoss08/herdr-wsl**](https://github.com/emoss08/herdr-wsl) | Connects a Windows Herdr app layout to a WSL 2 machine so spaces, terminals and repository panels use Linux paths. |
| [**CodeyPacker/herdr-mods**](https://github.com/CodeyPacker/herdr-mods) | Adds the Islands Herdr app layout and mods for workspace jumping, process control and agent-guided code tours. |
| [**Lakris2407/herdr-mods**](https://github.com/Lakris2407/herdr-mods) | Adds the Fleet Herdr app layout and mods for agent lists, quotas, build runners, delivery stats and controls. |
| [**CHO-kr/frieren**](https://github.com/CHO-kr/frieren) | Adds a Windows Herdr app layout for multiple Claude Code and Codex accounts, session lists, and usage gauges. The interface is in Korean. |
| [**carstenlucke/herdr-roundup**](https://github.com/carstenlucke/herdr-roundup) | Adds the Roundup layout for the Herdr app with custom file browsing, preview, themes, and keyboard shortcuts. |
| [**zztalker/herdr-agent-deck**](https://github.com/zztalker/herdr-agent-deck) | Adds a Herdr app layout with agent cards, space summaries, and an overview board for agents and terminals across machines. |
| [**dissimulate/bettr**](https://github.com/dissimulate/bettr) | Adds a Herdr app layout with agent and usage sidebars, system statistics, terminals, and file and activity panels. |
| [**dantech99/herdr-zed-layout**](https://github.com/dantech99/herdr-zed-layout) | Adds a Zed-inspired Herdr app layout with tabs, file and changes panels, agent quotas, and Tokyo Night colors. |
| [**MarcozVD/herdr-layout-catppuccin**](https://github.com/MarcozVD/herdr-layout-catppuccin) | Applies a Catppuccin layout to the Herdr app with Mocha and Latte colors that follow the system appearance. |
| [**tackcrypto1031/tackbear-herdr-mod**](https://github.com/tackcrypto1031/tackbear-herdr-mod) | Adds a Herdr app layout with a chat-style input box, file and image attachments, and model and reasoning controls. |
| [**vib-z/herdr-layouts**](https://github.com/vib-z/herdr-layouts) | Adds seven Herdr app layouts, including Control Panel, Falling Code, Fleet Tab, Night City, Queue, The Crew Board and The Noir Office. |
| [**isaacin42/herdr-layouts**](https://github.com/isaacin42/herdr-layouts) | Adds Herdr app layouts including Darkroom, Mixtape, Neon, Orienteering, Orrery, The Desk and The Pass for viewing and steering agents. |
| [**ozcberkay/herdr-coban**](https://github.com/ozcberkay/herdr-coban) | Adds a Herdr app layout and mods for Claude Code usage and session status, per-tab notes and Mac system metrics. |
| [**othavi0/noctua-layout**](https://github.com/othavi0/noctua-layout) | Adds a graphite Herdr app layout with colored space cards, agent status indicators and Git information. |
| [**johnny4young/herdr-relevo**](https://github.com/johnny4young/herdr-relevo) | Adds a Herdr app layout with Claude account quotas, an agent and pull-request inbox, and a review pane for sending comments to agents. |
| [**kyle-avrett/herdr-square-dracula**](https://github.com/kyle-avrett/herdr-square-dracula) | Applies a gapless Dracula layout to the Herdr app with compact tabs, a sidebar and file and changes panels. |
| [**chelebyy/herdr-agent-workspace**](https://github.com/chelebyy/herdr-agent-workspace) | Adds a Herdr app layout with agent and resource sidebars, quota gauges, task launchers, and Turkish and English UI options. |
| [**Mayloparra24/gentle-herdr**](https://github.com/Mayloparra24/gentle-herdr) | Adds a Gentle Shell-themed Herdr app layout that syncs its colors with the selected Gentle Shell theme. |
| [**VedangP57/herdr-tui-layout**](https://github.com/VedangP57/herdr-tui-layout) | Recreates Herdr TUI navigation in the Herdr app with machine-grouped spaces, agent status, tabs, and prefix keys. |
| [**anderssonq/herdsidian**](https://github.com/anderssonq/herdsidian) | Adds an Obsidian vault sidebar to the Herdr app for browsing and editing notes beside agents. |
| [**mirkobozzetto/herdr-app-config**](https://github.com/mirkobozzetto/herdr-app-config) | Adds a keyboard-first Herdr app layout with shortcut menus, agent status, file panels, and code review tools. |
| [**TwoD97/neon-borough**](https://github.com/TwoD97/neon-borough) | Adds a cyberpunk Herdr app layout with agent activity displays and panels for pull requests, file transfers, and secrets. |
| [**jotyy/herdr-ovis-studio**](https://github.com/jotyy/herdr-ovis-studio) | Adds an Ovis Studio-inspired Herdr app layout with an agent sidebar, tab bar, status line, and command picker. |
| [**pilmokim/herdr-pixel-spaces**](https://github.com/pilmokim/herdr-pixel-spaces) | Adds pixel-art space and agent icons and an agent attention indicator to a Herdr app layout. |
| [**adamentwistle/herdr-territory**](https://github.com/adamentwistle/herdr-territory) | Maps Claude Code agent activity across repository files in a Herdr app layout and warns about file collisions. |
| [**Jiqize/herdr-maid-adv**](https://github.com/Jiqize/herdr-maid-adv) | Turns the Herdr app into a visual-novel workspace where agent characters queue to speak when they finish or need input. |

### Herdr app mods and themes

*64 projects. Feature mods and color themes that customize the Herdr app.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community extensions.

| Project | What it does |
|---|---|
| [**sodiumsun/agenttrail · herdr/agenttrail**](https://github.com/sodiumsun/agenttrail/tree/main/herdr/agenttrail) | Shows a read-only project map beside Herdr app terminals, using PLAN.md or inferred Git branches and worktrees. |
| [**fatwang2/Pulse · herdr**](https://github.com/fatwang2/Pulse/tree/main/herdr) | Adds a stock and crypto watchlist mod and a matching Herdr app layout with a docked price panel. |
| [**GaganSD/coding-agent-toolkit · herdr-insights**](https://github.com/GaganSD/coding-agent-toolkit/tree/main/herdr-insights) | Shows local token usage and model activity for Pi, Codex, Claude Code, OpenCode and Antigravity in a Herdr app dashboard. |
| [**atuinsh/herdr-atuin-threads**](https://github.com/atuinsh/herdr-atuin-threads) | Lists Atuin-captured coding-agent threads in the Herdr app and resumes a selected session in a new tab. |
| [**rabeeh-ta/herdr-git-graph**](https://github.com/rabeeh-ta/herdr-git-graph) | Shows a Git commit graph in the Herdr app and offers branch, merge, rebase, and other repository actions. |
| [**iampedii/herdr-redline**](https://github.com/iampedii/herdr-redline) | Reviews GitHub pull requests and GitLab merge requests in the Herdr app with worktree checkout, diffs, and inline comments. |
| [**mathieucroset/herdr-pokemon-agents**](https://github.com/mathieucroset/herdr-pokemon-agents) | Shows agents as animated Pokémon in the Herdr app and lets users jump to an agent by clicking its sprite. |
| [**vytasgavelis/herdr-reviewer**](https://github.com/vytasgavelis/herdr-reviewer) | Adds syntax-colored diffs and inline review comments to the Herdr app Changes panel and sends comments to an agent. |
| [**SaifHarding/herdr-cloudflare**](https://github.com/SaifHarding/herdr-cloudflare) | Shows Cloudflare Pages and Workers deployment status in the Herdr app header and reports failed deployments. |
| [**chappse6/herdr-blueprint-app**](https://github.com/chappse6/herdr-blueprint-app) | Displays agent-written Mermaid flowcharts beside Herdr app sessions and sends clicked diagram changes back to the agent. |
| [**mrolafsson/herdr-recap**](https://github.com/mrolafsson/herdr-recap) | Lists agent recaps and blocked questions across machines in the Herdr app and Herdr TUI, with replies from the list. |
| [**greenflagged/herdr-forge**](https://github.com/greenflagged/herdr-forge) | Opens GitHub or GitLab project panels in the Herdr app and hands issues or merge requests to agents. |
| [**ergunozyurt/herdr-super-agent**](https://github.com/ergunozyurt/herdr-super-agent) | Organizes a lead agent’s human decision requests into threaded inbox items in the Herdr app. |
| [**greenflagged/herdr-greenflagged**](https://github.com/greenflagged/herdr-greenflagged) | Displays project dependency trees in the Herdr app and optionally marks npm dependencies with Greenflagged review verdicts. |
| [**jjangsky/herdr-pr-flow**](https://github.com/jjangsky/herdr-pr-flow) | Shows agent pull requests in a Herdr app panel with CI, review and post-merge workflow status, plus optional merge and diff comments. |
| [**JinJieBeWater/herdr-t3-inbox**](https://github.com/JinJieBeWater/herdr-t3-inbox) | Adds an attention inbox to the Herdr app sidebar where users can settle finished agents and see them return when work resumes. |
| [**jakub-tucek/herdr-annotator**](https://github.com/jakub-tucek/herdr-annotator) | Adds code review to the Herdr app with branch and working-tree diffs, inline comments and GitHub pull-request threads for local or SSH worktrees. |
| [**dmazlum/herdr-revive**](https://github.com/dmazlum/herdr-revive) | Restores supported coding-agent sessions after a Herdr app restart and forks conversations into adjacent panes. |
| [**mukiwu/herdr-crew-rpg**](https://github.com/mukiwu/herdr-crew-rpg) | Displays dispatched agents as pixel-art characters in a Herdr app sidebar and battle scene with status and quota information. |
| [**dmazlum/herdr-walkthrough**](https://github.com/dmazlum/herdr-walkthrough) | Uses Claude Code to turn a repository diff into an ordered, explained walkthrough in the Herdr app. |
| [**jonathan-fielding/herdr-project-coordinator**](https://github.com/jonathan-fielding/herdr-project-coordinator) | Adds a Projects sidebar to the Herdr app where a Claude Code coordinator delegates tasks to isolated workers and tracks their progress. |
| [**cybertron288/herdr-mods**](https://github.com/cybertron288/herdr-mods) | Adds Herdr app mods for file browsing, GitHub Actions, JavaScript scripts, session status, Slack and YouTube Music. |
| [**ChmaraX/herdr-chat**](https://github.com/ChmaraX/herdr-chat) | Adds a native chat interface in Herdr app tabs for Pi, Claude Code and Codex, with streamed messages and tool approval cards. |
| [**MarcozVD/herdr-agent-flow**](https://github.com/MarcozVD/herdr-agent-flow) | Maps agents, subagents and their messages in the current Herdr app space as a live diagram or timeline. |
| [**thuanlm215/herdr-float-space**](https://github.com/thuanlm215/herdr-float-space) | Adds a floating scratch window with terminal tabs and shared notes to the Herdr app. |
| [**CacaoRick/herdr-open-vscode**](https://github.com/CacaoRick/herdr-open-vscode) | Opens the focused Herdr app terminal folder in VS Code locally or through Remote SSH, including SSH-connected WSL. |
| [**ernestjsf/herdr-devices**](https://github.com/ernestjsf/herdr-devices) | Adds a Herdr app side panel for iOS and Android devices and simulators, with device actions and Maestro flow runs. |
| [**LaiqianDS/herdr-mods**](https://github.com/LaiqianDS/herdr-mods) | Adds a Herdr app Git panel for diffs, staging, commits and branch switching, alongside a file-icons mod. |
| [**linziyanleo/herdr-mods**](https://github.com/linziyanleo/herdr-mods) | Adds Herdr app mods for multi-root file browsing, file previews and editing, and mod and layout management. |
| [**nozikov/herdr-usage-limits**](https://github.com/nozikov/herdr-usage-limits) | Shows Claude Code and Codex subscription limits and session context in the Herdr app status bar. |
| [**sachin-philip/herdr-marks-as-unread**](https://github.com/sachin-philip/herdr-marks-as-unread) | Marks agents as unread in the Herdr TUI or Herdr app sidebar and clears the mark when users return. |
| [**mrolafsson/herdr-vitals**](https://github.com/mrolafsson/herdr-vitals) | Shows machine CPU, memory, disk and network activity in a Herdr app window or Herdr TUI popup, with resource alerts. |
| [**benjaminsicard/herdr-mods**](https://github.com/benjaminsicard/herdr-mods) | Adds Herdr app mods for desktop notifications and automatic tab and space names. |
| [**aBER0724/herdr-git-changes**](https://github.com/aBER0724/herdr-git-changes) | Adds a Herdr app Git panel for staging, commits, stashes, history, and diff inspection. |
| [**CiprianSpiridon/herdr-migration**](https://github.com/CiprianSpiridon/herdr-migration) | Imports Herdr TUI workspaces, tabs, folders, and terminal splits into the Herdr app with backup and verification. |
| [**funny-it-worked-last-time-gsv/herdr-sit-and-watch**](https://github.com/funny-it-worked-last-time-gsv/herdr-sit-and-watch) | Adds a Herdr app sidebar that depicts agents as robots at their desks. |
| [**yacoubb/herdr-app-mods**](https://github.com/yacoubb/herdr-app-mods) | Adds a Herdr app Wayfinder panel that graphs Markdown decision tickets and starts tickets in Claude Code tabs. |
| [**jankeesvw/herdr-focus-to-hover**](https://github.com/jankeesvw/herdr-focus-to-hover) | Focuses the Herdr app pane under the mouse pointer so users can type without clicking. |
| [**naruse/herdr-chat**](https://github.com/naruse/herdr-chat) | Adds a chat interface for Claude Code and Codex agents in the Herdr app, with live replies and terminal access. |
| [**DeevsDeevs/deevs-herdr-kit**](https://github.com/DeevsDeevs/deevs-herdr-kit) | Adds Herdr app mods for viewing and controlling agent-browser sessions and browsing images from agent conversations. |
| [**thuanlm215/herdr-agent-resume**](https://github.com/thuanlm215/herdr-agent-resume) | Resumes agent conversations in restored Herdr app terminals after a restart using a keyboard shortcut or optional automatic resume. |
| [**Abrahamism/herdr-browser**](https://github.com/Abrahamism/herdr-browser) | Controls a dedicated Chromium browser through CDP and adds a Herdr app panel for listing and switching its tabs. |
| [**shihyuho/herdr-recall**](https://github.com/shihyuho/herdr-recall) | Adds a recent and fuzzy switcher for Herdr app spaces, tabs, panes and agents, including their status and location. |
| [**thebends2k/herdr-ssh-hosts**](https://github.com/thebends2k/herdr-ssh-hosts) | Adds a searchable SSH host picker and two-pane SFTP browser to the Herdr app sidebar. |
| [**Srv-02/herdr-filerpro**](https://github.com/Srv-02/herdr-filerpro) | Adds a Herdr app file panel for browsing and transferring files on local and SSH machines. |
| [**wapenshaw/herdr-customize**](https://github.com/wapenshaw/herdr-customize) | Edits settings and keybindings for Herdr TUI and the Herdr app, with theme and extension management. |
| [**VladTemp27/herdr-mods**](https://github.com/VladTemp27/herdr-mods) | Adds Herdr app mods for GitHub issues and pull requests, usage limits, space hibernation, resources, ports, and saved run actions. |
| [**dmazlum/herdr-arena**](https://github.com/dmazlum/herdr-arena) | Runs a task across multiple agents in separate Git worktrees in the Herdr app and compares or combines their results. |
| [**dev-gvs/herdr-claude-usage**](https://github.com/dev-gvs/herdr-claude-usage) | Shows Claude plan usage and reset times in the Herdr app status bar. |
| [**Codesmith28/gruvbox-herdr-app**](https://github.com/Codesmith28/gruvbox-herdr-app) | Adds six Gruvbox themes and a contrast-switching mod to the Herdr app. |
| [**thomasschafer/kiosk**](https://github.com/thomasschafer/kiosk) | Finds Git repositories and branches in the Herdr app and opens them as spaces or worktrees. |
| [**Ghamza-Jd/herdr-lichess**](https://github.com/Ghamza-Jd/herdr-lichess) | Adds a Lichess side panel to the Herdr app for puzzles, live games, and playing opponents or the computer. |
| [**choam2426/herdr-paddock**](https://github.com/choam2426/herdr-paddock) | Groups Herdr app spaces by project and shows agents, their status, sessions, and subagents in a sidebar. |
| [**adamentwistle/limit-runway · herdr**](https://github.com/adamentwistle/limit-runway/tree/main/herdr) | Adds a Herdr app panel for monitoring Claude Code and Codex plan limits and pausing or resuming agents through the Runway CLI. |
| [**choam2426/herdr-session-titles**](https://github.com/choam2426/herdr-session-titles) | Shows agent conversation titles in the Herdr app agents list and pane headers. |
| [**ashrodan/ship-it**](https://github.com/ashrodan/ship-it) | Adds pull request status, checks, review threads, and change inspection to the Herdr app. |
| [**jordan13p/wickline**](https://github.com/jordan13p/wickline) | Displays a stock and crypto watchlist with prices, charts, and freshness indicators in a Herdr app pane. |
| [**AshMcConnell/herdr-openspec**](https://github.com/AshMcConnell/herdr-openspec) | Shows OpenSpec changes and task lists in a Herdr app panel and lets users update tasks or archive changes. |
| [**lntvan166/herdr-pokemon**](https://github.com/lntvan166/herdr-pokemon) | Displays Herdr app agents as animated Pokémon with selectable forms, status reactions, and seasonal scenery. |
| [**LeaveMyYard/herdr-panorama**](https://github.com/LeaveMyYard/herdr-panorama) | Shows Claude Code agent sessions and their subagents in a Herdr TUI swarm view, with native Herdr app sidebar and graph mods. |
| [**pedroparra/herdr-monokai**](https://github.com/pedroparra/herdr-monokai) | Recolors the Herdr desktop app's main window in the classic Monokai palette, with agent states in Monokai yellow, pink and cyan and an orange ring on the focused pane. Adds Monokai and Monokai Dimmed themes that work in any layout, with no mods or code. |
| [**e-kotov/herdr-cache-hit**](https://github.com/e-kotov/herdr-cache-hit) | Shows prompt-cache metrics and expiration alerts in Herdr TUI, with an experimental display-only Herdr app mod. |
| [**douglasjarquin/sf2-themes**](https://github.com/douglasjarquin/sf2-themes) | Installs Street Fighter II color themes for the Herdr app and Herdr TUI as well as several other developer tools. |
| [**flupke/herdr-ruminate**](https://github.com/flupke/herdr-ruminate) | Adds a Herdr app review pane for Git or jj changes with review threads for Claude Code and Codex. |

---

## 3. Connect through MCP and the socket API

*238 projects. Protocols, clients, bots, and event bridges that link Herdr to external tools, editors, and messaging apps.*

### MCP servers

*17 projects. Servers that expose Herdr operations as MCP tools for compatible AI clients.*

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
| [**nytafar/herdr-spawn**](https://github.com/nytafar/herdr-spawn) | Exposes an MCP tool that starts coding agents on your machines from a chat prompt, with a Claude Code Remote Control link when available. |
| [**boozedog/herdr-mcp**](https://github.com/boozedog/herdr-mcp) | Coordinates agents in Herdr TUI panes through a Deno MCP server with configurable workflow roles. |
| [**husniadil/olympus**](https://github.com/husniadil/olympus) | Provides a terminal you can drive from code: create, drive, observe and tear down real terminal sessions on zmx, tmux, meja or herdr, through a Go package, a CLI and a stdio MCP server. |
| [**nativestrider/herdr-mesh-safe**](https://github.com/nativestrider/herdr-mesh-safe) | Exposes lease-scoped Herdr agent coordination through MCP while restricting arbitrary commands and unscoped deletion. |
| [**Kuznetsov-Ilia/agy**](https://github.com/Kuznetsov-Ilia/agy) | Maintains a warm Antigravity worker pool in Herdr and exposes delegation tools to Cursor through an MCP server. |
| [**aelaguiz/herdr-mcp**](https://github.com/aelaguiz/herdr-mcp) | Exposes Herdr TUI workspace inspection, pane control and agent prompting to MCP clients through the Herdr CLI. |
| [**islam3zzat/herdr-mcp**](https://github.com/islam3zzat/herdr-mcp) | An MCP server that lets AI assistants inspect and control coding agents running in Herdr through a socket-based communication bridge. |
| [**bonsai/herdr-mcp**](https://github.com/bonsai/herdr-mcp) | Lets OpenCode rename and blink Herdr TUI tabs or trigger speech through MCP, with additional plugin actions and monitoring. |
| [**simozampa/agent-relay**](https://github.com/simozampa/agent-relay) | Provides a secure, asynchronous MCP gateway for persistent coding agents. |

### Socket API and herdr-core clients and SDKs

*38 projects. Clients, libraries, and command-line tools for Herdr TUI and herdr-core APIs.*

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
| [**egriff38/effect-herdr**](https://github.com/egriff38/effect-herdr) | Controls the Herdr terminal multiplexer through a typed Effect-TS SDK. |
| [**akhileshrangani4/herdr-bridge**](https://github.com/akhileshrangani4/herdr-bridge) | An HTTP bridge with a terminal-friendly control panel for Herdr agents. |
| [**klittle32/letta-herdr-mod**](https://github.com/klittle32/letta-herdr-mod) | Modifies Letta Code so sessions running in Herdr report accurate idle, working, and blocked states to the sidebar. |
| [**uuie/reasonix-herdr**](https://github.com/uuie/reasonix-herdr) | Reports Reasonix agent lifecycle states to Herdr in real time and adds native workspace and pane controls for supervising Reasonix alongside other agents. |
| [**QuiquiMatCom2004/herdr-py**](https://github.com/QuiquiMatCom2004/herdr-py) | Lets Python programs control Herdr workspaces, panes, agents, and other resources through its socket API. |
| [**fabzter/herdrbridge**](https://github.com/fabzter/herdrbridge) | Lets Python bridges drive Herdr agents, track sessions, extract replies, and navigate approval prompts through the CLI and socket API. |
| [**lib-x/herdr-sock-go**](https://github.com/lib-x/herdr-sock-go) | Connects Go programs to the Herdr TUI newline-delimited socket API with typed and raw methods. |
| [**maxandersen/jherdr**](https://github.com/maxandersen/jherdr) | Connects Java programs to the Herdr TUI socket API using a scripting facade, generated typed methods or raw calls. |
| [**cyperx84/herdr-api**](https://github.com/cyperx84/herdr-api) | Connects Go programs to the Herdr TUI socket API with typed agent models and event subscriptions. |
| [**flaricy/herdr-bridge**](https://github.com/flaricy/herdr-bridge) | Reports DeepSeek Harness activity to the Herdr pane that hosts it, including live working, blocked, and idle states, without requiring changes to Herdr. |
| [**vika2603/herdr-client**](https://github.com/vika2603/herdr-client) | Provides a typed Go client and plugin toolkit for Herdr's socket API, generated from the schema the herdr binary prints and covering all 102 methods of protocol 22. Adds a reconnecting session mirror, the pane graphics frame stream, and the manifest parser and entrypoint dispatch a Go plugin needs. |
| [**JefeLabs/herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker) | Adds a self-hosted REST and WebSocket API for Herdr to spawn and steer coding agents with parent-child federation. |
| [**Phoobobo/herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration) | Connects TraeX lifecycle hooks to Herdr's agent-reporting socket methods, giving TraeX panes correct idle, working, and blocked status. |
| [**cdpath/herdr-warp**](https://github.com/cdpath/herdr-warp) | Integrates the Warp Agent CLI with Herdr. It can send prompts, wait for output, approve or reject actions, and infer idle, working, and blocked status from terminal output. |
| [**kevinWangSheng/herdr-kit**](https://github.com/kevinWangSheng/herdr-kit) | Saves and restores declarative Herdr TUI pane layouts, watches events, and calls socket methods. Includes two plugins and an agent skill. |
| [**atnine-ai/herdr-bridge**](https://github.com/atnine-ai/herdr-bridge) | Connects Herdr panes to chat services for communicating with agents outside the terminal. |
| [**aiken884/herdr-bridge**](https://github.com/aiken884/herdr-bridge) | A single command center for sending tasks to several coding agents, following their progress, and checking the final result through Herdr. |
| [**hisetu/pi-herdr-remote**](https://github.com/hisetu/pi-herdr-remote) | Pi-native tools for operating Herdr servers on explicitly approved SSH hosts. |
| [**bradydibble/herdi**](https://github.com/bradydibble/herdi) | A private remote client and relay for Herdr; development moved away from its former public fork. |
| [**alex-devdone/herdr-remote-agent-watch**](https://github.com/alex-devdone/herdr-remote-agent-watch) | Shows a Claude session running behind SSH and tmux as a live Herdr sidebar agent. It also provides more resilient SSH and remote-Herdr wrapper commands. |
| [**AgentWorkforce/herdr-relay-bridge**](https://github.com/AgentWorkforce/herdr-relay-bridge) | A relay bridge intended to connect Herdr agents as a cooperating team. The source catalog gives no further protocol details. |
| [**pinksaucepasta/paperboat-helper**](https://github.com/pinksaucepasta/paperboat-helper) | A remote runtime for Paperboat environments, covering PTYs, Herdr agents, previews, images, activity reporting, and configuration synchronization. |
| [**trillium/herdr-tailscale**](https://github.com/trillium/herdr-tailscale) | Automatically attaches trusted Tailscale peers to Herdr as remote tabs. |
| [**opencharly/plugin-herdr**](https://github.com/opencharly/plugin-herdr) | Controls Herdr terminal multiplexer sessions over its NDJSON socket API using Charly commands. |
| [**rudironsoni/HerdrKit**](https://github.com/rudironsoni/HerdrKit) | Provides a Swift 6 client kit implementing Herdr JSON socket API protocols 17 through 22. |
| [**brooswit-factory/jsHerdrSDK**](https://github.com/brooswit-factory/jsHerdrSDK) | Provides a typed TypeScript client for the herdr socket API, generated from its published JSON Schema. |
| [**brooswit-factory/drovr**](https://github.com/brooswit-factory/drovr) | Wraps a TypeScript Herdr TUI SDK to detect blocked agents and correct reported agent states. |
| [**vinceferro/herdr-tg · crates/herdr-client**](https://github.com/vinceferro/herdr-tg/tree/HEAD/crates/herdr-client) | Reads Herdr TUI state and pane output with a typed Rust client for the socket protocol. |

### Chat alerts: Telegram, Discord, and Slack

*20 projects. Bot and channel alerts that ping you when agents finish or need input.*

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
| [**naturalmoods/herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify) | Sends Telegram alerts when agents finish or need input and routes replies back to Herdr TUI or herdr-core agents. |
| [**revanp/herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence) | Publishes the active Herdr project, current agent, and total active-agent count through Discord Rich Presence using a local RPC service, with no bot or external server required. |
| [**amurru/herdr-whistle**](https://github.com/amurru/herdr-whistle) | Manages Herdr TUI agents from Telegram, including listing agents, reading output, sending text, and starting or closing panes. |
| [**lsisoft/herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge) | Sends blocked-agent alerts to Telegram or Slack and routes replies to the originating Herdr TUI or tmux pane. |
| [**juninaba/herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify) | Sends Slack notifications when Herdr agents finish or become blocked. |
| [**barnuri/herdr-notifications**](https://github.com/barnuri/herdr-notifications) | Sends Telegram, Discord, or Slack alerts when Herdr TUI agents become idle, blocked, or done, with per-status filters. |
| [**egemenyildiz/herdr-slack**](https://github.com/egemenyildiz/herdr-slack) | Connects Slack to local Herdr agents so users can browse sessions, answer prompts, and launch agents without a tunnel. |
| [**dcieslak19973/herdr-slackr**](https://github.com/dcieslak19973/herdr-slackr) | Displays a real-time Slack feed inside a Herdr pane, using Socket Mode with polling as a fallback. |
| [**elkraps/herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify) | Sends configurable Telegram alerts for Herdr TUI agent states, with templates, multiple destinations, and duplicate suppression. |
| [**vsem-azamat/herdr-telegram**](https://github.com/vsem-azamat/herdr-telegram) | Connects Telegram forum topics to stable Herdr agent sessions for ongoing remote conversations. |

### Desktop, mobile, and webhook notifications

*40 projects. Desktop notifications, mobile push alerts, and webhook triggers for agent events.*

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
| [**hmu332233/herdr-pets**](https://github.com/hmu332233/herdr-pets) | Shows macOS desktop pets for Herdr TUI agents that move to your pointer when an agent is blocked. |
| [**ProjectAJ14/herdr-warp**](https://github.com/ProjectAJ14/herdr-warp) | Sends Warp desktop notifications when a Herdr-managed agent finishes or needs attention. |
| [**tkmct/herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify) | Adds a Herdr plugin that shows a Windows desktop toast when an agent (Claude Code, etc.) running under WSL2 becomes done (finished) or blocked (waiting for approval/input). |
| [**happyeric77/agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify) | Posts structured HTTP webhooks when agents block or finish. Payloads can include workspace and pane details, model information, and recent scrollback for use in Slack, Discord, or mobile-alert systems. |
| [**ChrisPachulski/session-sounds**](https://github.com/ChrisPachulski/session-sounds) | Plays distinct per-session sounds for Herdr TUI agent attention and completion on macOS and Linux. |
| [**zgxme/herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify) | Forwards Herdr TUI agent notifications to chat services, ntfy or custom HTTP webhooks. |
| [**fulanto/herdr-oncall**](https://github.com/fulanto/herdr-oncall) | Surfaces blocked agent prompts in a macOS floating panel or Telegram and Feishu messages, allowing replies without returning to the pane. |
| [**tiny-send/tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr) | Emails a one-line summary when an agent blocks, finishes, or fails. Replying to the message sends input to the correct pane, making an email client a simple remote approval interface. |
| [**HikaruEgashira/say-hook**](https://github.com/HikaruEgashira/say-hook) | Reads a one-line status summary aloud when an agent becomes done or blocked, using ElevenLabs or macOS speech through a Herdr state-change hook. |
| [**saeedrahimi/herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl) | Converts Herdr lifecycle events inside WSL into native Windows 11 toast notifications by invoking PowerShell across the WSL boundary. |
| [**zhaoyuheng200/tmux-agent-herd**](https://github.com/zhaoyuheng200/tmux-agent-herd) | Provides tmux plugin: detect coding-agent status (working/blocked/idle) per pane, notify on blocked, jump between agents. Detection ported from herdr. |
| [**gridness/herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds) | Plays random local macOS sounds when Herdr TUI agents need input or finish tasks. |
| [**quinnjr/herdr-notifications**](https://github.com/quinnjr/herdr-notifications) | Sends native desktop notifications when Herdr agent states change on Linux, macOS, Windows, and BSD. |
| [**jaltez/agent-notify**](https://github.com/jaltez/agent-notify) | Monitors local and WSL Herdr sessions in a tray and sends popups, sounds, commands, or webhooks for agent events. |
| [**tdhuan/agent-notify**](https://github.com/tdhuan/agent-notify) | Sends desktop notifications for Claude Code permission requests and completed turns, with clicks focusing the matching Herdr pane. |
| [**y-hirakaw/herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify) | Sends macOS notifications for Claude Code panes in Herdr TUI with the agent’s latest message or question. |
| [**diegopzz/herdr-notify**](https://github.com/diegopzz/herdr-notify) | Sends desktop notifications for Herdr agents on local or remote machines, identifying the host that needs attention. |
| [**huketo/herdr-hitl**](https://github.com/huketo/herdr-hitl) | Blocks a Herdr coding agent on a human decision, delivered to your phone over Telegram or Discord. |
| [**keinstn/drover-notify**](https://github.com/keinstn/drover-notify) | Sends a push alert to the Drover iOS app when a Herdr agent becomes blocked. It uses built-in Node.js features only and stores encrypted pairing information locally. |
| [**ram4-dev/herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center) | Stores notifications from all workspaces in a durable popup inbox. Items can be reviewed, opened in their related pane, cleared when resolved, and retained across restarts. |
| [**jefflau/herdr-webhook**](https://github.com/jefflau/herdr-webhook) | Posts Herdr TUI agent done and blocked events as JSON to a configurable webhook. |
| [**Rockheung/herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell) | Displays visual bell indicators in Kaku tabs when Herdr agents await human input. |
| [**ivorpad/herdr-notify**](https://github.com/ivorpad/herdr-notify) | Notifies users when Herdr TUI agents need attention or finish and queues messages until agents can receive them. |
| [**perlporter/herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin) | Shows a toast in herdr when the currently playing track changes in Apple Music (macOS). |
| [**wicolian/dev-on-call**](https://github.com/wicolian/dev-on-call) | Provides a quiet, local-first macOS menu-bar sentry for developers and their coding agents. |
| [**sandiiarov/tmux-agent-plugin**](https://github.com/sandiiarov/tmux-agent-plugin) | Provides tmux plugin for a Herdr-like AI agent sidebar. |
| [**1smil1/herdr-done-popup**](https://github.com/1smil1/herdr-done-popup) | Shows a persistent desktop popup when a Herdr TUI agent finishes or asks a question. |
| [**advaitbd/herdr-notify**](https://github.com/advaitbd/herdr-notify) | Sends Herdr agent-status notifications through signed Hermes webhooks. |
| [**zerkc/herdr-notify-firebase**](https://github.com/zerkc/herdr-notify-firebase) | Sends Firebase Cloud Messaging push notifications when Herdr agent status changes. |
| [**donghaolicd/herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify) | Sends bounded Microsoft Teams notifications for Herdr agent lifecycle events. |

### Telemetry, events, and quota streaming

*30 projects. Event collectors and monitors for agent state, usage, cost, and runtime activity.*

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
| [**TheRealHaoLiu/dsh-herdr**](https://github.com/TheRealHaoLiu/dsh-herdr) | Reports a DeepSeek Harness root agent’s identity and lifecycle state to its Herdr pane. |
| [**mcc0x/herdr-standup**](https://github.com/mcc0x/herdr-standup) | Generates summaries of agent activity across Herdr workspaces over time, including commits, diff volume, and branches. |
| [**neospeed83/herdr-replay**](https://github.com/neospeed83/herdr-replay) | Records and replay multi-agent Herdr coding sessions as interactive timelines. |
| [**nabutabu/herdr-observr**](https://github.com/nabutabu/herdr-observr) | Exports Herdr TUI agent runtime health, wait times, concurrency, usage, and costs through OpenTelemetry. |
| [**xdagiz/opencode2-herdr**](https://github.com/xdagiz/opencode2-herdr) | Reports OpenCode 2 agent states and session identity to Herdr TUI through its socket. |
| [**HunterStarets/herdr-gitbash-agent-detector**](https://github.com/HunterStarets/herdr-gitbash-agent-detector) | Detects OpenCode sessions running inside Git Bash panes on Windows and reports their state (idle / working). |
| [**Lbryany/dsh-plugins · packages/dsh-herdr**](https://github.com/Lbryany/dsh-plugins/tree/main/packages/dsh-herdr) | Aggregates DeepSeek Harness root and child agent states and reports the resulting lifecycle state to the Herdr pane. |
| [**peria-ai/precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin) | Shows PRECC token-savings telemetry in Herdr panes and runs PRECC setup and diagnostics. |
| [**hoon-ch/herdr-gjc-plugin**](https://github.com/hoon-ch/herdr-gjc-plugin) | Reports agent launch, exit, idle, working, and blocked states to Herdr. |
| [**5qln/5qln-herdr-plugin**](https://github.com/5qln/5qln-herdr-plugin) | Provides the 4+1 cell as a Herdr instrument, sealed podium for human questions, and four agent desks. |
| [**simensollie/aw-watcher-herdr**](https://github.com/simensollie/aw-watcher-herdr) | Records focused Herdr workspaces and concurrent agent activity in ActivityWatch on macOS, for both the Herdr app and Herdr TUI. |
| [**AgentTeamsRun/herdr**](https://github.com/AgentTeamsRun/herdr) | Reports Herdr TUI worktree creation and removal to the AgentTeams registry. |
| [**Howryann/herdr-monitor**](https://github.com/Howryann/herdr-monitor) | Exposes read-only Herdr agent status over HTTP with no runtime dependencies. |
| [**capt-marbles/herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration) | Reports Jcode session and lifecycle state to Herdr. |
| [**TheMetalStorm/herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin) | Makes a plain Cline CLI process appear as a native Herdr agent with lifecycle reporting. |
| [**makgunay/herdr-atomic-reporter**](https://github.com/makgunay/herdr-atomic-reporter) | Reports Atomic agent states and session references to Herdr TUI for Atomic 0.9.18; Atomic 0.9.19 and later include a built-in reporter. |
| [**perorin0418/jcode-herdr-integration**](https://github.com/perorin0418/jcode-herdr-integration) | Reports jcode agent lifecycle states to the Herdr sidebar using hooks. |
| [**Nofuture123/herdr-opencode2-integration**](https://github.com/Nofuture123/herdr-opencode2-integration) | Reports OpenCode 1.x and 2.0 session states to Herdr TUI with per-pane process isolation. |
| [**no-phux/herdr-opencode**](https://github.com/no-phux/herdr-opencode) | Reports OpenCode lifecycle events to Herdr, preserving agent state and restoring pane sessions. |
| [**meuble/Herdr-mistral-vibe**](https://github.com/meuble/Herdr-mistral-vibe) | Reports Mistral Vibe working, idle, and blocked states to Herdr TUI through Vibe hooks. |

### Voice, hardware, and remote bridges

*35 projects. Interfaces that connect Herdr to spoken input, physical devices, or remote control surfaces.*

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
| [**hackerchai/herdr-relay**](https://github.com/hackerchai/herdr-relay) | Shares Herdr TUI sessions with another computer using encrypted pairing over a LAN, tailnet, or relay. |
| [**Vercantez/herdr-voice**](https://github.com/Vercantez/herdr-voice) | Connects an installable iPhone web app to Herdr through a private voice gateway using OpenAI Realtime over WebRTC. |
| [**superfly/herdr-sprites-plugin**](https://github.com/superfly/herdr-sprites-plugin) | Runs Claude Code, Codex, OpenCode or a custom agent in persistent Fly.io Sprites controlled from Herdr TUI panes. |
| [**kvm404/Auren · src/auren/hands/herdr.py**](https://github.com/kvm404/Auren/blob/main/src/auren/hands/herdr.py) | Starts Herdr coding agents through the Auren voice assistant on Omarchy. |
| [**errantpacket/RhubarbTart · tools/rhubarb/herdr.py**](https://github.com/errantpacket/RhubarbTart/blob/main/tools/rhubarb/herdr.py) | Starts scoped security-research agents in Herdr TUI against assigned Tart VM clones with command approval controls. |
| [**jonesy827/mate**](https://github.com/jonesy827/mate) | Controls a Herdr fleet by phone call to start agents, send tasks, check status, and hear Claude Code or Codex replies. |
| [**freewillythe4th/action-button-agent**](https://github.com/freewillythe4th/action-button-agent) | Connects an iPhone Action Button to personal Herdr agents. Voice input passes through an iOS Shortcut, Tailscale, Telegram, and a Claude Agent SDK operator, which starts or targets a Herdr session and returns the response. |
| [**RanolP/herdr-handsfree**](https://github.com/RanolP/herdr-handsfree) | Adds on-device voice dictation and webcam gaze-based cursor movement to Herdr TUI on Apple Silicon Macs. |
| [**radres/herdr-plugin-call-me**](https://github.com/radres/herdr-plugin-call-me) | Calls your phone when a Herdr agent is blocked, reads the question aloud, and sends your spoken answer as a keypress. |
| [**kazuochi/opxy-deck**](https://github.com/kazuochi/opxy-deck) | Maps a Teenage Engineering OP-XY to Claude Code and Codex controls, dictation, and Herdr TUI agent routing. |
| [**giacolees/herdr-openlogi**](https://github.com/giacolees/herdr-openlogi) | Maps Logitech mouse buttons to Herdr navigation commands using OpenLogi overlays. |
| [**PlaneshiftDev/microd**](https://github.com/PlaneshiftDev/microd) | Handles macropad button events, gestures, and RGB controls with an optional Herdr bridge. |
| [**razajamil/herdr-hex-browser-voice-command**](https://github.com/razajamil/herdr-hex-browser-voice-command) | A Chrome extension and local service that sends Hex voice transcripts to the correct Herdr pane based on the browser URL that was focused while speaking. URL patterns are mapped to workspace, tab, and pane targets. |
| [**aliaksandr-haurylau-godel/herdr-voice**](https://github.com/aliaksandr-haurylau-godel/herdr-voice) | Transcribes held-key voice dictation into the focused Herdr TUI agent input, with context-aware rewriting and selectable speech engines. |
| [**Aktrov/herdr-tts**](https://github.com/Aktrov/herdr-tts) | Speaks selected terminal text aloud using Piper neural text-to-speech engines with keyboard controls. |
| [**hashrock/herdr-apc-mini**](https://github.com/hashrock/herdr-apc-mini) | Maps AKAI APC mini mk2 hardware controllers to physical Herdr agent controls. |
| [**shadowfax92/herdr-talon**](https://github.com/shadowfax92/herdr-talon) | Adds spoken Talon labels to visible Herdr targets for hands-free movement between panes. |
| [**ohitslaurence/outridr-server**](https://github.com/ohitslaurence/outridr-server) | Connects the outridr mobile app to Herdr over Tailscale for agent status, transcripts, remote input, and push alerts. |
| [**vgreg/herdr-padio**](https://github.com/vgreg/herdr-padio) | Switches PadIO controller modes automatically based on the app running in herdr's focused pane. |
| [**Drozerah/herdr-voice**](https://github.com/Drozerah/herdr-voice) | Adds early-stage text-to-speech audio feedback for agents working in Herdr TUI panes. |
| [**wtcrowe4/DialDeck**](https://github.com/wtcrowe4/DialDeck) | Uses a Microsoft Surface Dial and an AutoHotkey v2 engine as a keyless control surface for Herdr orchestration, development commands, and modelling macros. |
| [**nickboy/herddeck**](https://github.com/nickboy/herddeck) | Controls local and remote Herdr TUI agent sessions with Stream Deck keys. |
| [**eoinest/convo-history**](https://github.com/eoinest/convo-history) | Turns a recent window of speech into a Codex prompt in a fresh Herdr TUI worktree, triggered by a hotkey or wake word. |
| [**trentwadams/cc-controller**](https://github.com/trentwadams/cc-controller) | Maps SDL game controllers to Herdr socket commands for navigation, scrolling, and voice mode. The controller may be local or connected from another machine over SSH. |
| [**calebcauthon/herdr-riff-relay**](https://github.com/calebcauthon/herdr-riff-relay) | Sends Riff dictation to a chosen Herdr TUI agent pane using hotkeys. |

### Protocol and third-party bridges

*58 projects. Adapters between Herdr and other multiplexers, platforms, messaging systems, or automation protocols.*

| Project | What it does |
|---|---|
| [**openclaw/crabbox**](https://github.com/openclaw/crabbox) | Adds Crabbox sandbox provisioning and remote test execution to Herdr. Plugin actions can prewarm temporary environments, synchronize diffs, and inspect active leases from an overlay. |
| [**27medkamal/tmux-agent-wizard**](https://github.com/27medkamal/tmux-agent-wizard) | Brings Herdr agent detection and compatible CLI-driven plugins to tmux. |
| [**RaviTharuma/cmux-herdr**](https://github.com/RaviTharuma/cmux-herdr) | Shows Herdr TUI pane viewers and agent status pills inside cmux using external attachment. |
| [**benkraus/herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay) | Bridges Herdr TUI socket operations to HTTP and WebSocket clients, including a browser interface and optional Tailscale publishing. |
| [**neon-solutions/neon-herdr**](https://github.com/neon-solutions/neon-herdr) | Embeds a serverless Postgres dashboard in a Herdr pane. It can create database branches per agent worktree, start or stop compute, and insert connection strings. |
| [**HexSleeves/herdr-warp**](https://github.com/HexSleeves/herdr-warp) | Opens live Herdr TUI agents as native Warp panes on macOS. |
| [**agentwireprotocol/awp · plugin/herdr**](https://github.com/agentwireprotocol/awp/tree/main/plugin/herdr) | Connects Herdr TUI agents to Agent Wire Protocol messaging with inbox panes, notifications and idle-agent delivery. |
| [**wenxichang/herdr-pal**](https://github.com/wenxichang/herdr-pal) | Connects Herdr TUI agents across machines to a WeCom bot for session selection, task submission, terminal output, and limited key input. |
| [**Poor-Plebs/herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes) | Opens SSH terminals for hosts from SSH configuration in separate Herdr TUI workspaces. |
| [**detailles/AgentRadio**](https://github.com/detailles/AgentRadio) | Sends direct messages between agents in Herdr panes through a local SQLite-backed relay. |
| [**go-min/herdr-fwd**](https://github.com/go-min/herdr-fwd) | Automatically maintains loopback port forwarding between a remote Herdr session and the local machine, making services started by remote agents available without manual SSH tunnels. |
| [**HowAreAllWell/gpt-agent-bridge**](https://github.com/HowAreAllWell/gpt-agent-bridge) | Connects ChatGPT Web to local agents in Herdr TUI to dispatch tasks and review returned results. |
| [**elonnzhang/Herdrex**](https://github.com/elonnzhang/Herdrex) | Connects Herdr TUI workspaces and terminal panes to Rex desktop and CLI clients, locally or over SSH. |
| [**sunny0826/dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr) | Lets DeepSeek Harness sessions inspect and control Herdr through socket-backed tools and a session-scoped panel. |
| [**wavrin/herdr-ferry**](https://github.com/wavrin/herdr-ferry) | Moves files and clipboard between the Herdr box and your laptop over SSH, no cloud bucket. |
| [**gabriel-laet/herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor) | Lists, streams, and resumes Cursor cloud agents from Herdr TUI panes, with agent state reported to the sidebar. |
| [**ardasevinc/herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge) | Provides a native Herdr pane identity for Codex sessions using a centralized app-server. |
| [**vibegui/vibebook.dev · herdr-plugin**](https://github.com/vibegui/vibebook.dev/tree/main/herdr-plugin) | Connects Vibebook rooms to Herdr TUI and opens a Claude Code session for each room. |
| [**alepar/herdr-threads**](https://github.com/alepar/herdr-threads) | Sends durable messages between Claude Code, Codex, Antigravity and Hermes agents across Herdr TUI sessions and machines. |
| [**fab-agent/community**](https://github.com/fab-agent/community) | Adds teammate presence, departments and direct messages to a Herdr TUI community workspace. |
| [**anaypurohit0907/herdr-opencode-bridge**](https://github.com/anaypurohit0907/herdr-opencode-bridge) | Corrects Herdr TUI OpenCode pane status by aggregating root sessions and avoiding false idle states. |
| [**pisanvs/mc-cc**](https://github.com/pisanvs/mc-cc) | Shows Herdr agent status and Claude Code transcripts inside Minecraft and lets players reply from the game. |
| [**VicenteOlmos/opencode-herdr**](https://github.com/VicenteOlmos/opencode-herdr) | Routes OpenCode V2 beta requests through Herdr TUI adapters for supported agent CLIs. |
| [**getkimchi/herdr-kimchi**](https://github.com/getkimchi/herdr-kimchi) | Reports Kimchi agent state and session references to Herdr TUI for sidebar status and session restoration. |
| [**candypoets/buzzr**](https://github.com/candypoets/buzzr) | Mirrors Herdr workspaces and panes into Buzz channels using Nostr identities. It publishes agent availability and routes channel mentions to the correct terminal pane without exposing the user's private key. |
| [**szrenwei/herdr-traex**](https://github.com/szrenwei/herdr-traex) | Integrates TraeX agent lifecycle states and available model metadata into the Herdr TUI sidebar. |
| [**frankjoshua/herdr-acp**](https://github.com/frankjoshua/herdr-acp) | Exposes a Herdr pane as an Agent Client Protocol (ACP) agent, so any ACP client can prompt Claude Code, Codex, Pi, or a plain shell running in that pane. Streams the pane back to the client as one shared session, including text typed directly at the pane, and reads agent transcripts on Linux without hooks. |
| [**dsh-plugin-collection/dsh-herdr-site**](https://github.com/dsh-plugin-collection/dsh-herdr-site) | Reports dsh/cc-tui agent state (working/idle/blocked) to Herdr over the custom-integration protocol. |
| [**DO-Solutions/herdr-mars-plugin**](https://github.com/DO-Solutions/herdr-mars-plugin) | Starts, attaches to, and manages DigitalOcean Managed Agents sessions from Herdr panes using `doctl`. |
| [**rrojo02/herdr-bridge**](https://github.com/rrojo02/herdr-bridge) | Connects external coding agents to Herdr through its local socket API. |
| [**Liquescent-Development/herdr-a2a**](https://github.com/Liquescent-Development/herdr-a2a) | Connects Pi agents in a Herdr TUI workspace through an A2A broker for peer messages, replies, and team coordination. |
| [**haoliangwu/dsh-herdr**](https://github.com/haoliangwu/dsh-herdr) | Reports dsh session states to the Herdr agent panel through the pane-socket protocol. |
| [**vaclavik-xyz/herdwatch**](https://github.com/vaclavik-xyz/herdwatch) | Keeps a pane marked as working while CI, review, or another background condition is still pending after the agent itself becomes idle. It can run once or as a background service. |
| [**sgnilreutr/herdr-vibe-integration**](https://github.com/sgnilreutr/herdr-vibe-integration) | Reports Mistral Vibe agent states to the Herdr TUI sidebar through Vibe hooks and the socket or CLI. |
| [**ShinoharaHaruna/mimo-code-herdr**](https://github.com/ShinoharaHaruna/mimo-code-herdr) | Integrates MiMo Code agent state and session controls into Herdr TUI, with cleanup on exit and optional OpenCode identity. |
| [**slashv/st2-herdr**](https://github.com/slashv/st2-herdr) | Connects ST2 agent fleets to Herdr workspaces with live attachments, a hierarchy view, and operator-approved agent creation. |
| [**wenhao4126/dsh-herdr**](https://github.com/wenhao4126/dsh-herdr) | Exposes Herdr workspaces, panes, and coding agents as DeepSeek Harness tools. |
| [**tomoya55/cmux-herdr**](https://github.com/tomoya55/cmux-herdr) | Propagates agent status (working / waiting for input / finished) to the cmux sidebar. |
| [**scaccogatto/vite-plugin-herdr**](https://github.com/scaccogatto/vite-plugin-herdr) | Sends a selected browser element and prompt from a Vite app to a Herdr coding agent. |
| [**stfl/herdr-bridge**](https://github.com/stfl/herdr-bridge) | Shows a remote herdr agent inside a local herdr pane, one sidebar, several machines. |
| [**fabzter/hermes-bridge**](https://github.com/fabzter/hermes-bridge) | Lets Claude Code send messages and commands to a local Hermes Agent through Herdr and respond to its approval prompts. |
| [**Fectivnfy112357/claude-code-bridge**](https://github.com/Fectivnfy112357/claude-code-bridge) | Bridges Hermes Agent and Claude Code CLI in print mode and interactive Herdr sessions. |
| [**ardubev16/tmux-herdr**](https://github.com/ardubev16/tmux-herdr) | Adds a Tmux plugin that uses Herdr to manage, aggregate and orchestrate AI Agents. |
| [**Mumega-com/herdr-mupot-bridge**](https://github.com/Mumega-com/herdr-mupot-bridge) | Bridges Mupot and Herdr with flight monitoring, presence reports, and inbox delivery to agent panes. |
| [**m4ttstack/herdr-chat**](https://github.com/m4ttstack/herdr-chat) | Brings rt chat into Herdr TUI panes with broadcasts, presence, unread indicators, and jumps to agent panes. |
| [**LuYanFCP/herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin) | Controls Herdr TUI agents through WeChat, including status updates, prompts and permission responses. |
| [**AlexandreAkao/herdr-bridge-compozy**](https://github.com/AlexandreAkao/herdr-bridge-compozy) | Displays headless CompozyOS agents as Herdr TUI agent rows by forwarding hook events to the socket API. |
| [**sbulav/herdr-relay**](https://github.com/sbulav/herdr-relay) | Relays Herdr TUI agent state to phone, web, and Telegram clients, letting users approve prompts and send terminal input. |
| [**thesimonharms/herdr-cmd-agent-plugin**](https://git.simonharms.com/thesimonharms/herdr-cmd-agent-plugin) | Adds CommandCode agent detection to Herdr TUI, including idle, working, and blocked state in the sidebar. |
| [**junliu-mde/mimo-code-herdr-plugin**](https://github.com/junliu-mde/mimo-code-herdr-plugin) | Combines all subagent states into a stable idle, working, blocked, or done status for Herdr. A watchdog releases stale labels after crashes, and nested MiMo tool calls are ignored. |
| [**stefanahman/mux**](https://github.com/stefanahman/mux) | Lets Go programs manage workspaces, panes, and agent state through a common interface for tmux, Herdr TUI, and cmux. |
| [**OSHEThai/HerdrOps**](https://github.com/OSHEThai/HerdrOps) | Monitors desktop operations for Herdr terminal agents on Windows. |
| [**linvald/herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer) | Syncs cmux's file viewer to the currently focused herdr space. |
| [**Gol-D-Rogger/herdr-code-server-clipboard**](https://github.com/Gol-D-Rogger/herdr-code-server-clipboard) | Forwards Herdr selections to the code-server browser clipboard on macOS. |
| [**tumf/conflux-herdr**](https://github.com/tumf/conflux-herdr) | Runs the Conflux TUI in a Herdr TUI pane and reports idle, working, and blocked states to the Agents list. |
| [**opencharly/pod-herdr**](https://github.com/opencharly/pod-herdr) | Provides the herdr stack box (herdr.dev terminal multiplexer) + the check-herdr-pod R10 bed; herdr candy = pinned binary, supervised server, TCP socket bridge for the herdr: verb / charly herdr CLI. |
| [**edmundmiller/herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview) | Detects GitHub issue and pull-request links in the active pane and opens their details in a neighboring split through the GitHub CLI. |
| [**WerrySs/herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync) | Keeps cmux's graphical file explorer synchronized with the current directory of the focused Herdr pane by listening to focus events without modifying shell sessions. |

---

## 4. Editor integrations

*88 projects. Bridges and pane synchronizers that let you drive Herdr agents directly from your code editor.*

### Neovim navigation and splits

*26 projects. Plugins that make movement between Neovim windows and Herdr panes feel continuous.*

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
| [**cinco/herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim) | Combines ripgrep and fzf for live searching, then opens a selected match in a Neovim split beside the active Herdr agent. |
| [**willfish/herdr-navigator.nvim**](https://github.com/willfish/herdr-navigator.nvim) | Moves between Neovim windows and Herdr TUI panes, pairing with a Herdr-side navigator for movement from terminal panes. |
| [**sebcbi1/herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav) | Unifies directional navigation and resizing across Neovim splits, Herdr panes, tabs, and workspaces. Boundary detection forwards focus to the next surface without changing modes. |
| [**mirkobozzetto/dotfiles**](https://github.com/mirkobozzetto/dotfiles) | A macOS terminal setup using Ghostty with tmux or Herdr, Neovim, and routing that brings the user to whichever coding agent needs attention. |
| [**KoalaVim/herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware) | Routes navigation, split, close, zoom, and scroll shortcuts to Neovim or Herdr TUI according to pane focus. |
| [**jtnovellis/herdr-nvim**](https://github.com/jtnovellis/herdr-nvim) | Opens a persistent Neovim sidebar per Herdr tab and sends selected code and context to an agent. |
| [**RooseveltAdvisors/herdr-open-nvim**](https://github.com/RooseveltAdvisors/herdr-open-nvim) | Extracts readable file links from Herdr TUI pane transcripts and opens selected paths in Neovim. |
| [**luisgui1757/dotfiles**](https://github.com/luisgui1757/dotfiles) | A cross-platform Rose Pine terminal and editor setup for macOS, Linux, WSL2, and Windows. It includes Neovim, Herdr, tmux or psmux, several terminals and shells, Nix on POSIX, and chezmoi-managed configuration. |
| [**RooseveltAdvisors/vim-herdr-navigation**](https://github.com/RooseveltAdvisors/vim-herdr-navigation) | A fork of `vim-herdr-navigation` with shared Ctrl and Alt directional keys across Herdr panes and Vim or Neovim splits. |
| [**joo-was-already-taken/herdr-navigator.nvim**](https://github.com/joo-was-already-taken/herdr-navigator.nvim) | Moves between Neovim splits and Herdr TUI panes using a Neovim plugin and companion navigation CLI. |
| [**rahadur/herdr.nvim**](https://github.com/rahadur/herdr.nvim) | Ports the Ink and Paper color schemes from herdr.dev to Neovim. |
| [**s-0-a-r/copse**](https://github.com/s-0-a-r/copse) | A command-line agent development environment combining Herdr, Neovim, and parallel agent fan-out. |
| [**jakkzz/herdr-setup**](https://github.com/jakkzz/herdr-setup) | A reproducible Herdr and Neovim setup with pinned plugins and a cross-platform installer for macOS, Linux, and WSL. |
| [**solidsnakedev/herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools) | Navigates Neovim windows and Herdr TUI panes and adds directional pane moves and rotation. |
| [**LiroRod/promptr**](https://github.com/LiroRod/promptr) | Provides a really small herdr plugin that integrates nvim with the multiplexer. |
| [**Aerosnail/nvim-herdr-navigator**](https://github.com/Aerosnail/nvim-herdr-navigator) | Navigates between Neovim splits and Herdr panes using a matching plugin pair. |

### Full Neovim-hosted workspaces

*4 projects. A deeper integration that uses Neovim as the main interface while Herdr owns the agent processes.*

| Project | What it does |
|---|---|
| [**raymondware/herdr.nvim**](https://github.com/raymondware/herdr.nvim) | Opens the Herdr TUI in a Neovim floating terminal and shows agent states in a status window and statusline component. |
| [**MomePP/herd.nvim**](https://github.com/MomePP/herd.nvim) | Uses Neovim as the primary dashboard to launch, monitor, and control background Herdr agent sessions. |
| [**ctbaum/herdr-deck**](https://github.com/ctbaum/herdr-deck) | Adds the companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovim, agent, shell, and lazygit deck. |
| [**romerramos/herdr-reviewr-nvim**](https://github.com/romerramos/herdr-reviewr-nvim) | Opens Reviewr files in the Neovim pane for the current HERDR workspace. |

### VS Code, Cursor, and dev containers

*13 projects. Extensions and environment setups for graphical editors and container-based development.*

| Project | What it does |
|---|---|
| [**scott-the-programmer/vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr) | Forwards Herdr's Unix socket into VS Code development containers through a loopback TCP bridge, allowing containerized agents to report status and receive commands from the host Herdr instance. |
| [**gambtho/herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer) | Starts shells and coding agents inside a repository's Dev Container through the official Dev Containers CLI and presents them as normal Herdr panes. |
| [**timofey-TK/herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor) | Opens the active Herdr workspace in VS Code or Zed with one shortcut. Local and SSH-remote workspaces are translated into the correct editor URI automatically. |
| [**mkellerman/herdex**](https://github.com/mkellerman/herdex) | Displays Herdr TUI workspaces and agent status in VS Code, with a terminal and editor actions. |
| [**alex-devdone/herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open) | Opens the focused Herdr pane's project in Cursor or VS Code, including remote panes through the editor's Remote SSH support. |
| [**mrshll/herdr-container-agents**](https://github.com/mrshll/herdr-container-agents) | Detects coding agents running inside containers and report them as herdr agents. |
| [**phine-apps/herdr-collie**](https://github.com/phine-apps/herdr-collie) | Bridges VS Code and Herdr to orchestrate AI agents, Git worktrees, and context sharing directly from the editor. |
| [**clement-micol/herdr-bridge**](https://github.com/clement-micol/herdr-bridge) | Bridges from herdr panes to VS Code: attach herdr terminals via vscode:// URIs. |
| [**endoumame/herdr-vscode**](https://github.com/endoumame/herdr-vscode) | Adds an inline code-review workflow to VS Code for work associated with Herdr agent sessions. The source description is incomplete beyond writing comments where the code is read. |
| [**gogamid/pi-herdr-cursor-focus**](https://github.com/gogamid/pi-herdr-cursor-focus) | Hides the editor cursor in Herdr panes that are not currently focused. |
| [**Andreslvc/herdr_plugin**](https://github.com/Andreslvc/herdr_plugin) | Opens pane folder in VS Code, copy path, and open a folder as a space. |
| [**leoweigand/vsctask**](https://github.com/leoweigand/vsctask) | Runs VS Code tasks.json tasks outside VS Code, in a Herdr pane or a shell. |
| [**DcNiemandd/vscode-worktree**](https://github.com/DcNiemandd/vscode-worktree) | Manages git worktrees and their herdr agent sessions from a VS Code sidebar, no terminal needed. |

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
| [**SamuelCastrillon/tzemed**](https://github.com/SamuelCastrillon/tzemed) | A Windows-native development stack combining Herdr, Neovim, Peri, and Gentle-ai specification-driven development. |
| [**AVGVSTVS96/starter-dotfiles**](https://github.com/AVGVSTVS96/starter-dotfiles) | Minimal, agent-first macOS dotfiles for React and TypeScript development, including Ghostty, Herdr, Claude Code, Codex, LazyVim, Vite+, Nub, and basic shell tooling. |
| [**lhr0909/herdr-bel**](https://github.com/lhr0909/herdr-bel) | Forwards Herdr agent notifications to Zed Terminal Threads using the terminal bell signal. |

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

*24 projects. General-purpose bridges that synchronize editor state with Herdr panes and agents.*

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
| [**AgriciDaniel/obsidian-herdr**](https://github.com/AgriciDaniel/obsidian-herdr) | Runs persistent Herdr TUI agent terminals in Obsidian and lets agents make logged, undoable vault edits. |
| [**nytafar/obsidian-herdr**](https://github.com/nytafar/obsidian-herdr) | Opens Herdr TUI or herdr-core agents as live terminal tabs in Obsidian and renders Claude Code sessions in a native view. |
| [**vonzelle-vzt/herdr-edit**](https://github.com/vonzelle-vzt/herdr-edit) | Edits code in a Herdr TUI pane with language-server diagnostics, completion, navigation, and companion panel integration. |
| [**TianZuo555/herdr.nvim**](https://github.com/TianZuo555/herdr.nvim) | Sends Neovim file and code references to coding agents running in the same Herdr tab. |
| [**utahta/herdr-prompt.nvim**](https://github.com/utahta/herdr-prompt.nvim) | Enables a Neovim user ask a Herdr agent about the code currently being viewed or edited. |
| [**UN-9BOT/sidekick_herdr**](https://github.com/UN-9BOT/sidekick_herdr) | Adds Herdr as a session backend for sidekick.nvim, giving its AI CLI launcher the same workflow available with tmux or Zellij without requiring a fork. |
| [**Osmait/agentline.nvim**](https://github.com/Osmait/agentline.nvim) | Sends Neovim selections and buffers to coding agents through herdr. |
| [**webdavis/herdr-nvim-annotate-extension.nvim**](https://github.com/webdavis/herdr-nvim-annotate-extension.nvim) | Adds herdr-nvim extension: annotate the current line with its diagnostic and blame into the herdr-nvim comment store. |
| [**RaphaelManke/send-to-agent.nvim**](https://github.com/RaphaelManke/send-to-agent.nvim) | Sends visual selections and review comments from Neovim to active AI agent sessions in Herdr. |
| [**Daniel-Steinberger/obsidian-herdr**](https://github.com/Daniel-Steinberger/obsidian-herdr) | Sends the next unchecked Markdown task to an agent in the matching Herdr workspace and marks it complete when the agent finishes. Continuous mode can process an entire checklist. |
| [**agentience/herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump) | Raises the editor window for the focused Herdr TUI pane’s project or lets users select an editor window from a filterable popup. |
| [**jimididit/herdr-open-editor**](https://github.com/jimididit/herdr-open-editor) | Fuzzy-finds a file in the current repository or directory and opens it in the configured editor in a Herdr TUI split pane. |
| [**chenyao0910/herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains) | Opens the active Herdr workspace or worktree in Rider, WebStorm, IntelliJ IDEA, or GoLand. |
| [**qapquiz/herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick) | Toggles a persistent Herdr TUI agent pane beside an editor. A companion Neovim plugin can paste selections into the agent without submitting. |

---

## 5. Switch and restore sessions

*188 projects. Fuzzy switchers, state managers, and layout restoration tools for organizing agent workspaces.*

### Fuzzy session switchers and terminal pickers

*90 projects. Interactive pickers for finding and focusing workspaces, tabs, panes, agents, or projects.*

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
| [**crafts69guy/herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard) | Adds a herdr plugin: fuzzy-switch across running agents, open workspaces, and ghq repositories in one Rust TUI, and open a repo in a new workspace, tab, split, or the current pane. |
| [**mr04vv/herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator) | A fuzzy tree for workspaces, tabs, and panes, sorted by agent urgency. Its preview shows directory, status, and recent scrollback so blocked or completed work can be triaged quickly. |
| [**yoshiori/herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker) | Opens a tree-style Herdr TUI navigator with configurable keys and input-method-friendly shortcuts. |
| [**salkhalil/herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer) | Searches open Herdr TUI workspaces and zoxide directories with fzf, then focuses or creates a workspace with template tabs. |
| [**jeffarese/herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus) | Replaces the normal new-tab action with a directory and project picker that includes autocomplete, recent locations, and an optional agent to start. If the directory is already open, it focuses that workspace instead. |
| [**jorge07RD/herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager) | Saves SSH connections and opens a selected host in a Herdr TUI pane or new tab from a fuzzy popup. |
| [**javoscript/herdr-pickr**](https://github.com/javoscript/herdr-pickr) | Finds Herdr TUI tabs, spaces, agents, and panes with fuzzy pickers and terminal previews. |
| [**martin-ro/herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent) | Jumps to the next agent needing attention, ranked by a configurable status priority. |
| [**maayanyosef/herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm) | Selects a running EC2 instance across AWS profiles and opens `herdr --remote` through AWS SSM. It uses temporary Instance Connect keys and automatic SSH-user detection, so no bastion, public IP, or stored key is required. |
| [**caneppelevitor/herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator) | Navigates Herdr TUI workspaces and tabs through a tmux-style tree with live pane previews. |
| [**vieitesss/contx**](https://github.com/vieitesss/contx) | Finds project directories with Git context and opens them as Herdr TUI workspaces or tmux sessions. |
| [**ugurtarlig/herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency) | Ranks agents and workspaces by the time of their latest real Claude or Codex turn, bringing the most recently finished or stalled sessions to the top. |
| [**haphamdev/herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher) | Fuzzy-searches Herdr TUI workspaces, tabs, and agents and opens projects as workspaces. |
| [**joshuadavidthomas/hrd**](https://github.com/joshuadavidthomas/hrd) | Combines local and remote Herdr sessions with isolated sandboxes for discovery, inspection, and attachment across machines and containers. |
| [**mcuste/herdr-workspacer**](https://github.com/mcuste/herdr-workspacer) | Finds open workspaces and zoxide directories in a most-recently-used picker, then focuses or creates a Herdr TUI workspace. |
| [**emanuel2718/herdscope**](https://github.com/emanuel2718/herdscope) | Finds Herdr TUI agents, terminals and commands with status ranking and live pane previews. |
| [**dardT/herdr-workspaces-manager**](https://github.com/dardT/herdr-workspaces-manager) | Finds local projects and opens them in Herdr TUI workspaces, tabs or panes. |
| [**ofelcan164/muster**](https://github.com/ofelcan164/muster) | Shows agents across Herdr TUI workspaces and jumps to the selected agent or orchestrator. |
| [**purehate/herdr-plugin-picker**](https://github.com/purehate/herdr-plugin-picker) | Finds Herdr TUI spaces, agents, tabs, and panes in a popup, broadcasts to marked panes, and connects to SSH hosts. |
| [**lucasscariot/herdr-inbox**](https://github.com/lucasscariot/herdr-inbox) | Shows Herdr TUI agent threads in an attention-sorted terminal inbox and lets users launch tasks in worktrees across machines. |
| [**mrpbennett/qs-herdr-agents**](https://github.com/mrpbennett/qs-herdr-agents) | Displays Herdr agent panels inside the Omarchy quick-switch menu. |
| [**bkarpinos/herdr-picker**](https://github.com/bkarpinos/herdr-picker) | Adds a fast popup picker for searching and previewing workspaces, agents, and tabs in herdr. |
| [**leonho/herdr-agent-inbox**](https://github.com/leonho/herdr-agent-inbox) | Shows a popup inbox of all agents and their latest recap. Pressing Enter jumps directly to the selected agent's pane. |
| [**cyperx84/herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro) | Picks Herdr TUI workspaces, agents, and zoxide directories in an fzf popup with live previews. |
| [**peterwiebe/herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention) | Jumps to the most recent blocked or finished agent. |
| [**ImArtisann/herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher) | Scans configured project roots and creates or focuses Herdr workspaces with one keyboard action. |
| [**ismaelosuna7824/herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces) | Keeps searchable history of workspace directories, refocuses active workspaces, restores older locations, and includes a filesystem browser for creating new workspaces. |
| [**kenchan/herdr-ghq-open-agent**](https://github.com/kenchan/herdr-ghq-open-agent) | Finds ghq repositories with fzf, opens one in a Herdr TUI workspace or tab, and starts Claude Code there. |
| [**wraithyy/herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint) | Saves frequently used project directories as named waypoints in a small text file and opens them as new Herdr workspaces through fzf. |
| [**j0urneyk/herdrctx**](https://github.com/j0urneyk/herdrctx) | Searches and manages local or SSH-hosted Herdr TUI sessions, including attaching, creating, stopping, and deleting sessions. |
| [**alon-z/herdr-command-palette**](https://github.com/alon-z/herdr-command-palette) | Opens a fuzzy picker for Herdr TUI workspaces and project directories, focusing an existing workspace or creating one. |
| [**dkarter/vellum**](https://github.com/dkarter/vellum) | Opens a customizable menu for Herdr TUI and other terminal multiplexers, with session and agent pickers. |
| [**sagmans/herdr-pickers**](https://github.com/sagmans/herdr-pickers) | Opens fuzzy Herdr TUI popups for switching projects, workspaces, worktrees, and agents. |
| [**jackfrancisdalton/herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette) | Fuzzy-finds Herdr spaces, tabs, agents, or panes and jumps directly to the selected target. |
| [**xheisenbugx/herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh) | Manages Herdr workspaces with a sesh-inspired interface. |
| [**kuwa72/herdr-focus-attention**](https://github.com/kuwa72/herdr-focus-attention) | Cycles through Herdr TUI agents needing attention, ranked by status and recent state change. |
| [**nathnael-desta/herdr-project-sessions**](https://github.com/nathnael-desta/herdr-project-sessions) | Browses Git projects, worktrees, live agent panes, and historical OpenCode sessions in a Herdr TUI overlay on Linux. |
| [**asumaran/asgoto**](https://github.com/asumaran/asgoto) | Searches repositories, worktrees, and panes in a tree-style Herdr TUI workspace switcher. |
| [**yxhta/herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker) | Searches active Herdr TUI agent panes in a popup with live previews and focuses the selected pane. |
| [**dleen/herdr-agents**](https://github.com/dleen/herdr-agents) | Lists all active panes and puts blocked agents first. It shows live previews, jumps to existing workers, and can start new agents with one key. |
| [**Joxtacy/herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault) | Browses earlier Claude Code sessions in a Herdr popup and resumes the selected conversation in a new tab. |
| [**black-atom-industries/helm.herdr**](https://github.com/black-atom-industries/helm.herdr) | Jumps to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator. |
| [**iamgp/herdr-overview**](https://github.com/iamgp/herdr-overview) | Shows a live tiled overview of Herdr TUI workspaces and their focused panes. |
| [**mike-bronner/herdr-plugin-project-finder**](https://github.com/mike-bronner/herdr-plugin-project-finder) | Fuzzy-finds Git repositories and opens them as Herdr TUI workspaces. |
| [**agustinvalencia/herdr-jump**](https://github.com/agustinvalencia/herdr-jump) | Opens separate overlay pickers for Herdr TUI spaces and agents with live status colors. |
| [**42lizard/herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer) | Finds open workspaces and project directories in a fuzzy picker, then focuses or creates a Herdr TUI workspace. |
| [**muscaiu/resume-globally**](https://github.com/muscaiu/resume-globally) | Searches and resumes recent Claude Code, Cursor, OpenCode, Pi, and Hermes sessions in Herdr panes. |
| [**ubuntudroid/herdr-coder-sessions**](https://github.com/ubuntudroid/herdr-coder-sessions) | Browses running Coder agent sessions and opens each in a Herdr workspace with changes mirrored to a local worktree. |
| [**princejoogie/herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker) | Opens Git repositories as Herdr workspaces from an OpenTUI picker. |
| [**kodama24ek/herdr-picker**](https://github.com/kodama24ek/herdr-picker) | Adds an fzf session picker for herdr, as fish functions. |
| [**okonomi/herdr-agent-queue**](https://github.com/okonomi/herdr-agent-queue) | Cycles through stopped or waiting Herdr agents with one key, starting with the agent that has been waiting longest. |
| [**solidsnakedev/herdr-jump**](https://github.com/solidsnakedev/herdr-jump) | Opens fuzzy pickers for Herdr TUI workspaces, tabs, panes, and projects, with a last-workspace toggle. |
| [**utahta/herdr-hop**](https://github.com/utahta/herdr-hop) | Finds repositories, worktrees, and open Herdr TUI workspaces in a popup and can clone repositories or create worktrees. |
| [**codingfragments/herdr-nav**](https://github.com/codingfragments/herdr-nav) | Navigates Herdr workspaces and panes with previews and workspace templates. |
| [**barnuri/herdr-project-manager**](https://github.com/barnuri/herdr-project-manager) | Discovers projects by glob or manual entry and opens a selected project in a Herdr TUI tab or workspace. |
| [**itisvincent/herdr-agent-sessions**](https://github.com/itisvincent/herdr-agent-sessions) | Lists saved coding-agent sessions in a searchable Herdr panel and resumes the selected session in a new pane. |
| [**lancodev/herdr-jump**](https://github.com/lancodev/herdr-jump) | Switches between Herdr workspaces and agents through a two-pane fuzzy picker with Vim keys. |
| [**followbl/herdr-drover**](https://github.com/followbl/herdr-drover) | Cycles recent Herdr TUI tabs with a Super+T hold-and-release shortcut and offers fuzzy search and new-tab creation. |
| [**kakigakki/lazy-claude-herdr**](https://github.com/kakigakki/lazy-claude-herdr) | Lists recent Claude Code sessions from every Herdr space in one fzf popup and resumes the chosen one where it started, focusing its live pane or splitting a pane in the matching space to run `claude -r`. A per-session menu forks the session, opens its PR or copies a review request, reads the transcript, or runs actions defined in TOML. |
| [**ridho9/switchr**](https://github.com/ridho9/switchr) | Browses Herdr TUI sessions and their workspace, tab, and pane trees before attaching. |
| [**adamwangxx/herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume) | Opens Codex's native resume picker in a new Herdr split, preserving the current view while previous Codex sessions are browsed and resumed. |
| [**damianpoole/herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions) | Searches earlier OpenCode sessions by project, title, date, or transcript text. Conversation previews and shortcuts make it possible to resume or fork a result into a new Herdr pane. |
| [**iskwyuki/herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel) | Opens an fzf panel for switching through workspace history, opening paths, and running custom actions in Herdr TUI. |
| [**mikedclarke/herdr-workspaces**](https://github.com/mikedclarke/herdr-workspaces) | Registers frequently used project directories and opens them through a fuzzy picker. Existing workspaces are focused instead of duplicated. |
| [**Duzc01/herdr-session-finder**](https://github.com/Duzc01/herdr-session-finder) | Searches Claude Code sessions across all projects and resumes the selected conversation through a Herdr plugin. |
| [**KazBrekker1/herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr) | Switches, creates, renames, and deletes Herdr TUI agents, tabs, and spaces from a popup picker with live status tracking. |
| [**trapple/herdr-focus**](https://github.com/trapple/herdr-focus) | Focuses the next blocked or completed agent pane and brings the terminal window to the front. |
| [**willfish/herdr-workspacex**](https://github.com/willfish/herdr-workspacex) | Fuzzy-switches Herdr TUI workspaces and creates a workspace from a zoxide directory. |
| [**tp6gw94/herdr-jump**](https://github.com/tp6gw94/herdr-jump) | Opens keyboard-driven pickers to focus a Herdr TUI workspace, tab, pane, or agent. |
| [**josephschmitt/pj-herdr**](https://github.com/josephschmitt/pj-herdr) | Uses the pj project picker to find a project and create or focus its Herdr TUI workspace. |
| [**nicolegros/herdr-launcher**](https://github.com/nicolegros/herdr-launcher) | Searches directories to create or switch Herdr TUI workspaces with a fuzzy picker. |
| [**benbrackenbury/open-project**](https://github.com/benbrackenbury/open-project) | Fuzzy-finds folders under `~/Projects` and creates or focuses a matching Herdr TUI workspace. |
| [**tdi/herdr-recents**](https://github.com/tdi/herdr-recents) | Keeps a history of Herdr TUI workspaces and worktrees and focuses or recreates a selected entry. |
| [**tim-kuntz/workspace-tools**](https://github.com/tim-kuntz/workspace-tools) | Opens a Herdr TUI workspace picker and toggles between the last two focused workspaces. |
| [**nicolasvasquez/herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace) | Switches existing Herdr TUI workspaces or creates them from zoxide directories using an fzf overlay. |
| [**barewalker/herdr-jump**](https://github.com/barewalker/herdr-jump) | Finds, focuses, or moves panes across Herdr TUI workspaces with a fuzzy picker. |
| [**PremModhaOfficial/sessionizer**](https://github.com/PremModhaOfficial/sessionizer) | Picks a project directory and attaches to its existing Herdr TUI workspace or creates one. |
| [**oyuk/herdr_plugin**](https://github.com/oyuk/herdr_plugin) | Jumps to Herdr TUI agents matching a selected status. |
| [**htlcode/herdr-directory-bookmarks**](https://github.com/htlcode/herdr-directory-bookmarks) | Saves directory bookmarks and opens them as Herdr TUI workspaces from a searchable popup. |
| [**bleedingfight/herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager) | Finds Herdr agents and workspaces with fzf and lets users focus or message agents. |

### Persistence, snapshots, and state restoration

*37 projects. Tools that record layouts and process context, then rebuild or resume them after a restart.*

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
| [**dmangla3/herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message) | Forks a Claude Code or Codex conversation from an earlier user message into a new tab, split pane, or workspace without modifying source transcripts. |
| [**bengemine/herdr-hibernate**](https://github.com/bengemine/herdr-hibernate) | Suspends idle Claude Code, Codex, or Grok panes to reduce memory use while keeping pane state and directory context. Pressing Enter resumes a hibernated session. |
| [**hmu332233/herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart) | Restarts an idle Claude Code, Codex, Grok, or AGY agent in the same Herdr pane and resumes its session. |
| [**victor-software-house/herdr-stash**](https://github.com/victor-software-house/herdr-stash) | Stashes Herdr TUI workspaces, stopping their processes while saving pane layouts and agent conversations for later restoration. |
| [**ExLuna-rs/herdr-auto-layout**](https://github.com/ExLuna-rs/herdr-auto-layout) | Applies declarative tabs, panes, commands, and agents to new Herdr TUI workspaces. |
| [**t4t5/herdr-forkr**](https://github.com/t4t5/herdr-forkr) | Forks a Claude Code, Codex, Pi, or OpenCode conversation into another Herdr TUI pane, tab, or workspace. |
| [**momentohq/mo-herdr**](https://github.com/momentohq/mo-herdr) | Runs mo inside herdr panes: session restore after a herdr restart, a launch action, and SIGKILL cleanup. |
| [**yansfil/herdr-remote-handoff**](https://github.com/yansfil/herdr-remote-handoff) | Transfers Claude Code sessions and workspaces between local and remote Herdr machines via a dedicated CLI. |
| [**alex-devdone/herdr-hub**](https://github.com/alex-devdone/herdr-hub) | Describes a herdr session of remote-attach panes as a portable manifest, and rebuild it on any machine. |
| [**asermax/herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace) | Suspends a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker). |
| [**TheThoughtagen/attic**](https://github.com/TheThoughtagen/attic) | Finds idle coding-agent sessions, saves their state, and closes them to reclaim resources while keeping them restorable. A Textual dashboard and Herdr plugin support pinning, snoozing, and reviewing archived workspaces. |
| [**nickmaglowsch/herdr-session-restore**](https://github.com/nickmaglowsch/herdr-session-restore) | Tags Claude Code panes with session IDs, saves the workspace, tab, and directory layout during a clean server stop, and rebuilds it on the next cold start using `claude --resume`. It is intentionally Claude-only and requires a clean shutdown. |
| [**KennethWKZ/herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs) | Detects Claude Code sessions launched through `ccs claude` and restores them through the CCS launcher. |
| [**rrg/herdr-park-agents**](https://github.com/rrg/herdr-park-agents) | Parks a coding-agent pane in herdr: stop the process, close the pane, and resume the session later from a workspace panel. |
| [**victor-software-house/herdr-restore-notice**](https://github.com/victor-software-house/herdr-restore-notice) | Adds compact notices to restored Herdr TUI scrollback so users can click to resume selected agent sessions. |
| [**shaun-agent/herder-shelving-skill**](https://github.com/shaun-agent/herder-shelving-skill) | Guides agents through discovering and safely restoring custom Herdr TUI workspace shelves. |
| [**Angel-O/herdr-agent-resume**](https://github.com/Angel-O/herdr-agent-resume) | Generates the exact resume command for an interrupted Claude Code, Codex, or custom agent session and either copies it or pastes it into a Herdr pane. |
| [**noviadi/herdr-layout**](https://github.com/noviadi/herdr-layout) | Saves Herdr pane splits and arrangements and restores the same workspace geometry later, similar to tmux-resurrect for layouts. |
| [**lancodev/herdr-checkpoint**](https://github.com/lancodev/herdr-checkpoint) | Saves Herdr TUI workspace, tab, pane, directory, and program snapshots and restores them later, closing items outside the checkpoint. |
| [**jovylle/herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name) | Preserves terminal titles and session names across Herdr tab closes. |
| [**Dimon94/herdr-context-locator**](https://github.com/Dimon94/herdr-context-locator) | Copies a self-describing locator for a Herdr agent's canonical native session context. |
| [**pasta-disaster/herdr-nook**](https://github.com/pasta-disaster/herdr-nook) | Opens a floating shell per Herdr TUI workspace and keeps its tmux session running when the popup is hidden. |
| [**aiki-sh/aiki-plugin-herdr**](https://github.com/aiki-sh/aiki-plugin-herdr) | Reports Aiki harness session identities to Herdr TUI panes so native sessions can be restored after a server restart. |
| [**timaliev/herdr-layout**](https://github.com/timaliev/herdr-layout) | Defines session-aware Herdr layouts in YAML, applies them idempotently, and can load them automatically at startup. |
| [**Gareth-Rouse/herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) | Tracks workspace last use and removes inactive workspaces from restored sessions. |
| [**xenking/herdr-omp-sleep**](https://github.com/xenking/herdr-omp-sleep) | Parks idle omp sessions in Herdr TUI panes and restores the same session when the user presses Enter. |
| [**connerohnesorge/vaultr**](https://github.com/connerohnesorge/vaultr) | Captures Claude Code and Codex sessions and forks them into Claude Code, Codex, or Pi. Streams captured Herdr TUI topology snapshots and includes pane actions for viewing and forking sessions. |

### Workspace and multi-session management

*61 projects. Managers for creating, grouping, naming, attaching to, and cleaning up several sessions.*

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
| [**0xyg3n/Daedalus**](https://github.com/0xyg3n/Daedalus) | Manages existing Herdr TUI sessions alongside native terminals and tmux in a Rust workspace manager. |
| [**fru-dev3/glyph**](https://github.com/fru-dev3/glyph) | Names coding-agent sessions and rebuilds Herdr TUI workspaces across machines, with an agent-usage plugin. |
| [**umutciloglu/herdr-session-manager**](https://github.com/umutciloglu/herdr-session-manager) | Browses agent sessions and supports agent-to-agent chat across Claude Code and Codex in Herdr TUI. |
| [**ropali/herdr-compose**](https://github.com/ropali/herdr-compose) | Defines Herdr workspaces, tabs, panes, and startup commands in reusable YAML layouts. |
| [**abdallah/session-hub**](https://github.com/abdallah/session-hub) | Tracks Claude Code sessions across machines and shows their status and inbox in a Herdr TUI sidebar. |
| [**cesmunoz/herdr-workspace-organizer**](https://github.com/cesmunoz/herdr-workspace-organizer) | Reorders Herdr TUI workspaces manually or previews a suggested order based on configurable categories. |
| [**to4iki/herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump) | Jumps to the next Herdr pane needing attention, prioritizing blocked agents before cycling through completed tasks. |
| [**DnzzL/herdr-idle**](https://github.com/DnzzL/herdr-idle) | Stops idle Herdr TUI agents to free memory while keeping panes available to resume their conversations. |
| [**mrolafsson/herdr-snooze**](https://github.com/mrolafsson/herdr-snooze) | Hides Herdr TUI agents or spaces from the Agents panel until a chosen time or event. |
| [**skaftanis/herdr-hermes-manager**](https://github.com/skaftanis/herdr-hermes-manager) | Manages local Hermes Agent profiles, scheduled jobs and bot chats from Herdr TUI workspaces. |
| [**vika2603/herdr-machine-manager**](https://github.com/vika2603/herdr-machine-manager) | Manages saved SSH machines from a Herdr TUI popup, including connecting, disconnecting, and editing targets. |
| [**zackshen/herdr-workspace**](https://github.com/zackshen/herdr-workspace) | Creates a workspace and apply a layout profile from a centered popup. |
| [**willfish/mux**](https://github.com/willfish/mux) | Launches tmuxinator-style project configurations into tmux sessions, Herdr TUI workspaces, or Herdr desktop spaces. |
| [**ronly2460/herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover) | Moves Herdr panes between workspaces with an interactive arrow-key picker. |
| [**tntpgh/herdr-control**](https://github.com/tntpgh/herdr-control) | Routes agents to project workspaces and sorts, colors, and names Herdr tabs by task and branch state. |
| [**DanDo385/cockpit**](https://github.com/DanDo385/cockpit) | Creates a Herdr TUI operating desk with Hermes Kanban, worktree lanes, and separate review and operations workspaces. |
| [**bonkey/herdr-keep-root**](https://github.com/bonkey/herdr-keep-root) | Keeps a repository's main-checkout workspace open while any of its worktree workspaces is open, so the Spaces panel never flattens a worktree group. |
| [**jamescary/mo**](https://github.com/jamescary/mo) | Runs persistent OMP agent sessions on a remote Mac using tmux and Herdr TUI, with SSH access and optional Telegram control. |
| [**mphaxise/omarchy-keepalive**](https://github.com/mphaxise/omarchy-keepalive) | Keeps Herdr agent sessions running on Omarchy with a bar panel, notifications, transcripts, and completion receipts. |
| [**OneNoted/zeshion**](https://github.com/OneNoted/zeshion) | Manages sessions and windows across Herdr TUI, tmux, and Zellij through a common CLI. |
| [**scaryrawr/herdr.fish**](https://github.com/scaryrawr/herdr.fish) | Automatically launches or attaches Herdr TUI from fish based on the current project and synchronizes the terminal window title. |
| [**shadowfax92/herdr-ferry**](https://github.com/shadowfax92/herdr-ferry) | Moves live Herdr TUI panes and tabs between workspaces through a Rust popup without restarting them. |
| [**yojahny55/herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups) | Groups Herdr TUI spaces under named, colored sidebar headers and opens them from a grouped picker. |
| [**frankwiles/hterm**](https://github.com/frankwiles/hterm) | Launches repeatable Herdr TUI workspaces from project definitions using a macOS CLI and bundled Raycast extension. |
| [**mjrusso/herdlord**](https://github.com/mjrusso/herdlord) | Monitors agents across local and remote Herdr TUI sessions and lets users inspect output or attach to a session. |
| [**EdJ/wsp**](https://github.com/EdJ/wsp) | Tracks projects, tasks, notes, and tags alongside live Herdr workspaces and publishes the combined context to the sidebar. |
| [**Rocco-Gossmann/Herdr-Workspace**](https://github.com/Rocco-Gossmann/Herdr-Workspace) | Creates a Herdr workspace with multiple tabs and splits in one command. |
| [**terafin/herdr-restart-always**](https://github.com/terafin/herdr-restart-always) | Supervises processes running in Herdr agent panes and restarts them after a crash. It works with Claude, Hermes, Codex, Pi, OpenCode, and other pane-based agents. |
| [**asermax/herdr-tab-command**](https://github.com/asermax/herdr-tab-command) | Starts an agent or runs a command in a new tab, based on the name you give the tab. |
| [**krzysztoff1/herdr-cull**](https://github.com/krzysztoff1/herdr-cull) | Lists Herdr agent panes, flags stale sessions, and closes only the panes selected for confirmation. |
| [**tfolkman/pi-herdr-workspace-namer**](https://github.com/tfolkman/pi-herdr-workspace-namer) | Synchronizes Pi session task titles to Herdr TUI workspace names. |
| [**HarryZus/herdr-dynamic-agent-workspace**](https://github.com/HarryZus/herdr-dynamic-agent-workspace) | Creates agent tabs when a Herdr workspace opens and coordinates a marker-based Claude and Codex review handoff. |
| [**masakirocorp/gardn**](https://github.com/masakirocorp/gardn) | Manages Herdr workspaces for AI coding agents. |
| [**tombell/tendr**](https://github.com/tombell/tendr) | Starts and manages local or SSH-accessible Herdr TUI sessions from declarative workspace, pane and lifecycle definitions. |
| [**kylescudder/schmerdr**](https://github.com/kylescudder/schmerdr) | Builds Herdr TUI workspaces, tabs, panes and agents from editable per-project shell templates. |
| [**bonkey/herdr-dup-tab**](https://github.com/bonkey/herdr-dup-tab) | Duplicates the focused Herdr TUI pane command and working directory in a new tab. |
| [**acrucetta/herdr-kanban**](https://github.com/acrucetta/herdr-kanban) | Organizes live Herdr agent sessions on a kanban board and opens the selected session beside Neovim. |
| [**fjordlars/herdr-session-manager**](https://github.com/fjordlars/herdr-session-manager) | Lists, creates, opens, renames, stops, and deletes named Herdr TUI sessions from a terminal interface. |
| [**p47t/herdr-sort-workspaces**](https://github.com/p47t/herdr-sort-workspaces) | Sorts and organizes Herdr TUI workspaces through a terminal interface. |
| [**leonho/herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes) | Lists active and idle Herdr TUI panes and lets users jump to active panes or review and close idle ones. |
| [**mike-bronner/herdr-plugin-agentic-panes-layout**](https://github.com/mike-bronner/herdr-plugin-agentic-panes-layout) | Applies a configurable TOML layout of tabs, panes, commands, and agents to Herdr TUI workspaces, including newly created worktrees. |
| [**ivorpad/herdr-reap**](https://github.com/ivorpad/herdr-reap) | Lists agents by lifecycle state in a Herdr TUI popup and closes finished agent panes on request. |
| [**caoer/ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout) | Previews and applies pane layouts in the current Herdr TUI tab, restoring the original layout on cancellation. |
| [**WillHeather/herdr-grid**](https://github.com/WillHeather/herdr-grid) | Moves agent panes into a screen-sized grid in Herdr TUI and restores their original tabs and layouts on request. |
| [**tipok/herdr-layouts**](https://github.com/tipok/herdr-layouts) | Builds complete Herdr workspaces from declarative TOML files defining tabs, panes, split directions, and startup commands. |
| [**phenome/herdr-layout**](https://github.com/phenome/herdr-layout) | Creates or reuses tabs and runs commands from up to three saved Herdr layouts. |
| [**TheHatBoxGhost/herdr-paddocks**](https://github.com/TheHatBoxGhost/herdr-paddocks) | Starts, stops, and switches Herdr TUI project workspaces from an Omarchy bar widget. |
| [**Cainiaooo/sessmark**](https://github.com/Cainiaooo/sessmark) | Tags coding-agent sessions and stores notes, with an optional Herdr TUI plugin. |
| [**alex-devdone/herdrl**](https://github.com/alex-devdone/herdrl) | Reconnects remote Herdr TUI sessions after network drops and mirrors remote agents into the local sidebar. |
| [**chuang861012/nu_herdr_navigate_directory**](https://github.com/chuang861012/nu_herdr_navigate_directory) | Adds a Nushell directory command that reuses idle Herdr TUI panes when navigating to a directory. |
| [**42lizard/workspace-basename**](https://github.com/42lizard/workspace-basename) | Names new Herdr TUI workspaces after the initial working-directory basename while preserving explicit names. |

---

## 6. Worktrees and terminal experience

*788 projects. Git worktree automation, terminal navigation, status displays, HUDs, and developer environment tools.*

### Git worktree automation

*101 projects. Tools that create isolated branches and worktrees for agents, then connect them to Herdr workspaces or tabs.*

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
| [**lamngockhuong/herdr-worktree-setup**](https://github.com/lamngockhuong/herdr-worktree-setup) | Prepares new Herdr TUI worktrees by copying ignored configuration files, linking shared directories and running optional setup commands. |
| [**thomasschafer/herdr-kiosk**](https://github.com/thomasschafer/herdr-kiosk) | Scans repositories and branch checkouts with a fuzzy picker and opens Herdr TUI workspaces or worktrees. |
| [**timofey-TK/herdr-worktree-hooks**](https://github.com/timofey-TK/herdr-worktree-hooks) | Runs custom setup and teardown commands when a Herdr worktree is created, opened, or removed. |
| [**OndrejDrapalik/worktree-management-skills**](https://github.com/OndrejDrapalik/worktree-management-skills) | Creates, opens, removes, and sweeps Git worktrees using a CLI and agent skills with Herdr or tmux. |
| [**jlimas/herdr-worktree-seed**](https://github.com/jlimas/herdr-worktree-seed) | Seeds new Node.js worktrees with copy-on-write `node_modules` and project dotfiles, reducing duplicated storage and setup time for temporary agent branches. |
| [**tanshio/herdr-worktreeinclude**](https://github.com/tanshio/herdr-worktreeinclude) | Copies gitignored environment and configuration files into new worktrees from standard `.worktreeinclude` patterns when Herdr reports creation. |
| [**ditwrd/herdr-remote-worktrunk**](https://github.com/ditwrd/herdr-remote-worktrunk) | Pulls remote branches, pull requests, and issues into Herdr TUI workspaces through Worktrunk. |
| [**persiyanov/herdr-fresh-worktree**](https://github.com/persiyanov/herdr-fresh-worktree) | Updates a newly created worktree branch to `origin HEAD` while protecting any branch with an upstream, a remote counterpart, local changes, or unique commits. Automated tests cover the safety checks and repeat runs. |
| [**JacquesvanWyk/herdr-lazygit**](https://github.com/JacquesvanWyk/herdr-lazygit) | Opens lazygit in a Herdr split or tab and intelligently opens, focuses, or closes it based on the current state, while preserving orientation and working directory. |
| [**danilolucasmd/herdr-clone-layout**](https://github.com/danilolucasmd/herdr-clone-layout) | Uses the currently arranged tabs and splits as a live template and copies that layout into every newly created Herdr worktree, without a separate configuration file. |
| [**khatriafaz/herdr-plugin-cow-worktree**](https://github.com/khatriafaz/herdr-plugin-cow-worktree) | Creates copy-on-write Git worktrees from a Herdr TUI workspace, including ignored files and local dependencies. |
| [**qdentity/herdr-worktree-lifecycle**](https://github.com/qdentity/herdr-worktree-lifecycle) | Routes worktree lifecycle events to setup and teardown scripts stored in the repository itself. Events are serialized per path, so each project owns its provisioning logic while the plugin handles delivery. |
| [**shizlie/herdr-setup-bootstrap**](https://github.com/shizlie/herdr-setup-bootstrap) | Reads `worktree_init.toml` when a worktree is created, runs a configured command, and copies selected ignored files or directories from the main checkout. An idempotency marker prevents repeated setup. |
| [**kkckkc/herdr-plugin-gh-workflow**](https://github.com/kkckkc/herdr-plugin-gh-workflow) | Takes a GitHub issue number, creates a branch and worktree through `gh issue develop`, and builds a Herdr workspace from the repository's `herdr-workspace.yaml` layout. |
| [**SirTenzin/superherd**](https://github.com/SirTenzin/superherd) | Connects the Superset workspace manager to Herdr. One command creates a worktree and Herdr workspace, mirrors Superset setup terminals as tabs, forwards interrupts, and removes the launcher pane when setup completes. |
| [**dkarter/hwt**](https://github.com/dkarter/hwt) | Creates configured Git worktrees and Herdr TUI workspaces, with dependency setup, isolated ports, and pull-request checkout support. |
| [**eightHundreds/herdr-worktreeinclude**](https://github.com/eightHundreds/herdr-worktreeinclude) | Copies gitignored files selected by `.worktreeinclude` into new Herdr worktrees. |
| [**ShoMasegi/herdr-worktree-nav**](https://github.com/ShoMasegi/herdr-worktree-nav) | Finds Herdr TUI panes by repository and worktree and opens branches as worktree panes. |
| [**lost-in-the/grove · integrations/herdr**](https://github.com/lost-in-the/grove/tree/main/integrations/herdr) | Creates and switches Git worktrees with Herdr TUI workspaces and agent status alongside optional tmux support. |
| [**jsutter909/corral**](https://github.com/jsutter909/corral) | Creates isolated Git worktrees and Herdr TUI workspaces for parallel coding agents, with commands to start and clean up sessions. |
| [**mcuste/pi-herdr-worktree**](https://github.com/mcuste/pi-herdr-worktree) | Gives Pi and Oh My Pi a typed tool for managing Herdr TUI worktree workspaces. |
| [**saiashirwad/homestead**](https://github.com/saiashirwad/homestead) | Creates isolated Git worktrees for Herdr with repository configuration, separate ports, environment setup, and teardown. |
| [**mcc0x/herdr-shear**](https://github.com/mcc0x/herdr-shear) | Inventories Herdr TUI worktrees, identifies cleanup candidates, and removes only those the user selects. |
| [**tomasvarga/herdr-e2b**](https://github.com/tomasvarga/herdr-e2b) | Copies the active Git worktree, including uncommitted changes, to an E2B sandbox and opens a remote shell without a push. |
| [**osolmaz/herdr-branch-cleanup**](https://github.com/osolmaz/herdr-branch-cleanup) | Returns idle panes to the default Git branch after a feature branch is merged or deleted on GitHub, but only when the tree is clean and no agent is actively typing. |
| [**mattarau/wt-herdr**](https://github.com/mattarau/wt-herdr) | Keeps Worktrunk worktrees and Herdr workspaces synchronized. Workspace creation, removal, and focus follow Worktrunk changes, with health checks, dry runs, and lifecycle notifications. |
| [**LeonardoTrapani/herdr-js-worktree-bootstrap**](https://github.com/LeonardoTrapani/herdr-js-worktree-bootstrap) | Prepares JavaScript and TypeScript worktrees by detecting lockfiles, installing dependencies, and restoring untracked environment configuration before agents begin work. |
| [**serhii-chernenko/herdr-worktreeinclude**](https://github.com/serhii-chernenko/herdr-worktreeinclude) | Supports custom worktree target locations and copies files matched by `.worktreeinclude`, following Claude CLI behavior for local environment setup. |
| [**crexi/herdr-worktree-copy**](https://github.com/crexi/herdr-worktree-copy) | Reads a `.worktree-copy` manifest when Herdr creates a worktree and copies environment files or symlinks shared directories from the main checkout. |
| [**jal-co/pi-herdr-worktree**](https://github.com/jal-co/pi-herdr-worktree) | Lets Pi list, create, open, and remove Herdr TUI worktrees with project hooks and optional file links. |
| [**disintegrator/trunkr**](https://github.com/disintegrator/trunkr) | Connects Worktrunk worktree operations to persistent Herdr workspaces so creation, switching, and cleanup remain synchronized. |
| [**zerodice0/herdr-plugin-worktree-bootstrap**](https://github.com/zerodice0/herdr-plugin-worktree-bootstrap) | Copies ignored local configuration, environment files, and credentials into new worktrees and runs required setup commands so agent panes can start working immediately. |
| [**steig/worktender**](https://github.com/steig/worktender) | Creates an isolated Git worktree and Herdr agent session for a GitHub issue. One command handles the branch, worktree, agent launch, and final cleanup. |
| [**dev-town/harbr**](https://github.com/dev-town/harbr) | Manages Git projects and worktrees and opens their terminal sessions in tmux or Herdr workspaces. |
| [**DecampsRenan/herdr-plugin-env-sync**](https://github.com/DecampsRenan/herdr-plugin-env-sync) | Sets up new Herdr TUI worktrees by copying environment files, tracking remote branches, and running project commands with a status panel. |
| [**gregorgebhardt/worktrunk-herdr.zsh**](https://github.com/gregorgebhardt/worktrunk-herdr.zsh) | Opens Worktrunk worktrees as Herdr TUI spaces through Zsh commands. |
| [**jtnovellis/herdr-worktree-setup**](https://github.com/jtnovellis/herdr-worktree-setup) | Prepares new Herdr TUI worktrees by copying ignored development files, cloning dependency caches, and running environment setup with a live TUI. |
| [**victor-falcon/git-worktree**](https://github.com/victor-falcon/git-worktree) | Creates and deletes Git worktrees with optional Herdr TUI, Zellij, or Muxy tab automation. |
| [**danieljvdm/herdr-composer**](https://github.com/danieljvdm/herdr-composer) | Composes coding tasks with screenshots and agent settings, then launches them in a new worktree or an existing checkout’s Herdr TUI tab. |
| [**brianstarke/wt**](https://github.com/brianstarke/wt) | Manages Git worktrees through a terminal interface and integrates them with Herdr TUI workspaces. |
| [**noamsiegel/git-wt-herdr**](https://github.com/noamsiegel/git-wt-herdr) | Automates Git worktree creation and lifecycle management by mapping worktrees directly to Herdr tabs. |
| [**peterferguson/herdr-conductor-worktree**](https://github.com/peterferguson/herdr-conductor-worktree) | Creates worktrees in Conductor's expected directory structure, registers them in Conductor's database, and provides a synchronization pane for opening active workspaces and closing archived ones. |
| [**mkdir700/herdr-config**](https://github.com/mkdir700/herdr-config) | A portable Herdr configuration with worktree settings, LazyVim-style keys, and small plugins for diff review, copying workspace paths, opening lazygit, and showing pull-request status. |
| [**bfreed/herdr-corral**](https://github.com/bfreed/herdr-corral) | Creates Git worktrees with environment files, dependencies, and Herdr TUI tabs for agents and development servers. |
| [**Feasy01/herdr-allow**](https://github.com/Feasy01/herdr-allow) | Copies allowlisted, uncommitted files such as secrets, environment settings, and local configuration into new worktrees based on a `.herdr-allow` file. |
| [**kbrdn1/herdr-plugin-gwm**](https://github.com/kbrdn1/herdr-plugin-gwm) | Adds popup menus for the `gwm` worktree CLI, including create, switch, clean, and batch commands, while adopting worktrees as Herdr workspaces and keeping `gwm` as the source of truth. |
| [**mkdir700/herdr-plugin-worktree**](https://github.com/mkdir700/herdr-plugin-worktree) | Creates a Git worktree from a GitHub issue, pull request, or branch name, automatically detecting the input type and using Claude-generated naming where supported. |
| [**tjg184/herdr-worktree**](https://github.com/tjg184/herdr-worktree) | Connects Worktrunk hooks and native Git worktree operations to Herdr workspaces and tabs, including dependency installation and environment propagation for newly created checkouts. |
| [**toyamarinyon/herdr-worktree-setup**](https://github.com/toyamarinyon/herdr-worktree-setup) | Runs a setup script committed to the repository whenever Herdr creates a new worktree. |
| [**tupton/herdr-worktree-include**](https://github.com/tupton/herdr-worktree-include) | Copies or symlinks selected ignored files from the main checkout into new Herdr TUI worktrees. |
| [**alexkarpandrus/herdr-dock**](https://github.com/alexkarpandrus/herdr-dock) | Creates coordinated Herdr workspaces across multiple repositories. |
| [**klukacin/herdr-hub-worktrees**](https://github.com/klukacin/herdr-hub-worktrees) | Mirrors a Herdr hub worktree into nested repository clones and removes the matching worktrees when the lane closes. |
| [**carlory/herdr-worktreeinclude**](https://github.com/carlory/herdr-worktreeinclude) | Copies selected Git-ignored files into new Herdr TUI worktrees using `.worktreeinclude` rules. |
| [**BjoernSchotte/herdr-worktree-picker**](https://github.com/BjoernSchotte/herdr-worktree-picker) | Finds Git worktrees by branch name and opens the selection in a Herdr TUI workspace or split pane. |
| [**danielv14/herdr-treehouse**](https://github.com/danielv14/herdr-treehouse) | Creates Git worktrees as Herdr tabs, applies repository-specific setup, and starts a coding agent. |
| [**caseneuve/herdr-worktree-bootstrap**](https://github.com/caseneuve/herdr-worktree-bootstrap) | Copies selected local files and runs setup commands asynchronously after Herdr TUI creates a worktree. |
| [**agutier6/herdr-paddock**](https://github.com/agutier6/herdr-paddock) | Allocates ports per Herdr TUI worktree and runs repository-defined lifecycle hooks and scripts in panes. |
| [**bonkey/herdr-wt-purpose**](https://github.com/bonkey/herdr-wt-purpose) | Creates a Herdr TUI worktree from a purpose or ticket URL, using an Apple on-device model to name its branch. |
| [**adamazad/remuda**](https://github.com/adamazad/remuda) | Creates a Git worktree, starts a Claude session in a Herdr TUI pane, and sends it a task. |
| [**swheel33/herdr-dev-workflow**](https://github.com/swheel33/herdr-dev-workflow) | Coordinates OpenCode 2 implementation work in disposable Git worktrees from Herdr TUI, with project chat and cleanup. |
| [**0xthc/herdr-plugin-worktree-bootstrap**](https://github.com/0xthc/herdr-plugin-worktree-bootstrap) | Copies configured untracked files and hardlinks dependencies into newly created Herdr TUI worktrees. |
| [**iamfozzy/herdr-stu**](https://github.com/iamfozzy/herdr-stu) | Opens pull requests and remote branches as worktrees, bootstraps them per project, and monitors agent CI states. |
| [**0xthc/herdr-plugin-pr-board**](https://github.com/0xthc/herdr-plugin-pr-board) | Browses GitHub pull requests for the current repository and checks them out as Herdr TUI worktree workspaces. |
| [**dev-shimada/lazyworktree**](https://github.com/dev-shimada/lazyworktree) | Manages Git worktrees in a terminal interface with optional Herdr TUI and GitHub integration. |
| [**beomjungil/herdr-lazygit-overlay**](https://github.com/beomjungil/herdr-lazygit-overlay) | Opens lazygit as an overlay using the focused pane's working directory, then restores the previous focus and zoom state when lazygit exits. |
| [**ynny-github/herdr-event-hook**](https://github.com/ynny-github/herdr-event-hook) | Reads a committed `.herdr-event-hook.toml` and runs configured commands when worktrees are created or removed, making it possible to start and stop per-worktree services automatically. |
| [**asumaran/gotopr**](https://github.com/asumaran/gotopr) | Finds open GitHub pull requests across local repositories and worktrees, then focuses the Herdr workspace that matches the selected review branch. |
| [**langtind/gren-herdr**](https://github.com/langtind/gren-herdr) | Connects the `gren` worktree manager to Herdr for creating, switching, and removing worktrees mapped to tabs, including gren's post-creation setup hooks. |
| [**nimrc/herdr-git-pull**](https://github.com/nimrc/herdr-git-pull) | Runs `git pull` for the active workspace in an overlay. It finds the repository root from subdirectories or linked worktrees and opens an interactive shell if conflicts need attention. |
| [**scoussens-nthplusio/herdr-worktree-include**](https://github.com/scoussens-nthplusio/herdr-worktree-include) | Copies ignored and untracked files into new Herdr worktrees according to repository `.worktreeinclude` rules compatible with Claude Code. |
| [**spirin22/herdr-plugins**](https://github.com/spirin22/herdr-plugins) | Seeds new Herdr TUI worktrees with ignored files and runs per-repository setup steps; includes a worktree removal safety helper. |
| [**kennethkoontz/herdr-worktree-sync**](https://github.com/kennethkoontz/herdr-worktree-sync) | Copies ignored files selected by `.worktreeinclude` into new worktrees, then allows and reloads direnv at the new root. |
| [**arjenblokzijl/herdr-worktree-autosetup**](https://github.com/arjenblokzijl/herdr-worktree-autosetup) | Runs a configured setup command in a visible pane whenever Herdr creates a Git worktree. |
| [**riclib/herdr-worktree-layout**](https://github.com/riclib/herdr-worktree-layout) | Automatically builds a fixed worktree layout containing a file viewer and two shells, using defined 60/40 and 75/25 splits. |
| [**untalfranfernandez/herdr-worktreeinclude**](https://github.com/untalfranfernandez/herdr-worktreeinclude) | Populates every new Herdr worktree with local ignored files such as `.env`, editor settings, and fixtures, using Claude Code-compatible `.worktreeinclude` patterns. |
| [**botonddombi/boti-toolkit**](https://github.com/botonddombi/boti-toolkit) | A personal development toolkit with Herdr worktree helpers, a machine-setup playbook, and a Claude Code setup agent. |
| [**snics/herdr-worktree-from-gitlab**](https://github.com/snics/herdr-worktree-from-gitlab) | Creates a Git worktree and Herdr workspace from a GitLab issue through the `glab` CLI. |
| [**dabeeeenster/herdr-worktree-local-files**](https://github.com/dabeeeenster/herdr-worktree-local-files) | Links ignored local configuration files from the main checkout into newly created Git worktrees. |
| [**wthorp/squeeze-chute**](https://github.com/wthorp/squeeze-chute) | Coordinates GitHub issues through isolated Herdr worktree teams. |
| [**mopeneko/herdr-worktree-hook-plugin**](https://github.com/mopeneko/herdr-worktree-hook-plugin) | Runs user-defined shell commands immediately after a new worktree is created, providing a simple post-create hook for Herdr. |
| [**mholtzscher/herdr-worktree-picker**](https://github.com/mholtzscher/herdr-worktree-picker) | Creates Herdr worktrees from either local or remote Git branches. |
| [**arjenblokzijl/herdr-worktree-provisioner**](https://github.com/arjenblokzijl/herdr-worktree-provisioner) | Runs repository-specific setup in a visible pane inside each new worktree, with a deliberately simple and composable design. |
| [**m1sk9/herdr-worktree-hooks-plugin**](https://github.com/m1sk9/herdr-worktree-hooks-plugin) | Adds configurable lifecycle hooks to Herdr worktree operations. |
| [**sample-usr/herdr-devenv-worktree**](https://github.com/sample-usr/herdr-devenv-worktree) | Provisions isolated devenv services for Herdr TUI worktrees, reserving ports and setting up per-worktree databases and ignored files. |
| [**danieljvdm/herdr-worktrunk**](https://github.com/danieljvdm/herdr-worktrunk) | Integrates Worktrunk worktree management with Herdr as a plugin. |
| [**BASHBOP/otito-herdr-plugin**](https://github.com/BASHBOP/otito-herdr-plugin) | Runs Otito context and deterministic merge evidence inside Herdr agent workspaces. |
| [**nilm987521/herdr-load-worktree**](https://github.com/nilm987521/herdr-load-worktree) | Opens all existing repository Git worktrees as individual Herdr workspaces with one click. |
| [**r-mulder/herdr-workspace-scripts-plugin**](https://github.com/r-mulder/herdr-workspace-scripts-plugin) | Runs repository-specific bootstrap scripts after Herdr TUI creates a worktree. |
| [**rewt/herdr-lanes**](https://github.com/rewt/herdr-lanes) | Creates isolated agent worktree lanes in Herdr TUI and promotes completed work to local main after validation. |
| [**takeaship/herdr-worktree-guard**](https://github.com/takeaship/herdr-worktree-guard) | Tracks and cleans up agent worktrees in Herdr TUI. |
| [**gw31415/herdr-git-parallel-worktrees-skill**](https://github.com/gw31415/herdr-git-parallel-worktrees-skill) | Teaches agents to allocate and validate isolated Git worktrees for parallel Herdr TUI work. |

### Workspace lifecycle and multi-repository tools

*10 projects. Higher-level utilities for starting, tracking, and removing workspaces that span one or more repositories.*

| Project | What it does |
|---|---|
| [**OliverGilan/herdr-jj**](https://github.com/OliverGilan/herdr-jj) | Adds Jujutsu workspace creation, remote fetching, bookmark setup, live change metadata, and post-create hooks to Herdr. |
| [**jattento/herdr-multirepo**](https://github.com/jattento/herdr-multirepo) | Creates a Herdr TUI workspace containing matching feature-branch worktrees from multiple repositories. |
| [**LoriKarikari/kubeflock**](https://github.com/LoriKarikari/kubeflock) | Creates and connects Kubernetes agent sandboxes to Herdr TUI and manages their lifecycle. |
| [**leoleducq/devflow**](https://github.com/leoleducq/devflow) | Provisions isolated development environments with databases, ports, environment files, and servers, and synchronizes them with Herdr TUI workspaces. |
| [**alon-z/herdr-devup**](https://github.com/alon-z/herdr-devup) | Reads `.herdr/dev.toml` to start a project's tabs, panes, and services, refresh an ngrok URL across configured environment files, and close only the tabs it created. |
| [**yoyoyeti/multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin) | Creates and attaches multitrunk task workspaces in Herdr TUI with an agent pane, repository tabs, and interactive popups. |
| [**joelhooks/herdr-janitor**](https://github.com/joelhooks/herdr-janitor) | Reviews stale Herdr workers and closes eligible panes only after ownership, state, identity, and clean-worktree checks. |
| [**arturodz/dev**](https://github.com/arturodz/dev) | Runs persistent coding workspaces on a Tailscale-connected development VM and reconnects to their Herdr TUI sessions over SSH. |
| [**kody-w/rapp-omarchy**](https://github.com/kody-w/rapp-omarchy) | Combines Herdr terminals, Git worktrees, Tailscale, and RAPP project tools in an Omarchy workbench. |
| [**yordanbuilds/rig**](https://github.com/yordanbuilds/rig) | Starts a project stack in Herdr TUI with configured tabs, panes, and dependent processes. |

### Diff review and code inspection

*59 projects. Side-by-side git diff inspection and comment handoff tools for agent reviews.*

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
| [**VedangP57/gitty · herdr-plugin**](https://github.com/VedangP57/gitty/tree/main/herdr-plugin) | Opens the gitty Git TUI in a Herdr TUI popup for the focused pane repository. |
| [**edmundmiller/herdr-plugin-hunk**](https://github.com/edmundmiller/herdr-plugin-hunk) | Adds six Hunk actions for worktree, staged, and branch diffs, each opening in either a split or a new tab. The active workspace and selected Herdr theme are passed to Hunk automatically. |
| [**JeHwanYoo/herdr-git**](https://github.com/JeHwanYoo/herdr-git) | Opens a Git pane in Herdr TUI for staging changes, reviewing diffs, browsing history and creating commits. |
| [**JacquesvanWyk/herdr-hunk**](https://github.com/JacquesvanWyk/herdr-hunk) | Combines an fzf Hunk diff picker with a hook that opens a diff split when an agent finishes. It reuses existing viewers and skips clean repositories. |
| [**scott306lr/herdr-plugin-hunk-autodiff**](https://github.com/scott306lr/herdr-plugin-hunk-autodiff) | Opens Hunk in a companion split whenever an agent finishes a turn with uncommitted changes, while leaving focus on the agent pane. |
| [**flupke/herdr-progressive-reviewer**](https://github.com/flupke/herdr-progressive-reviewer) | Shows changes from each agent turn for incremental diff review in Herdr TUI. |
| [**worldnine/akapen**](https://github.com/worldnine/akapen) | Enables line-by-line commenting on rendered Markdown documents in a TUI and sends review notes back to agents. |
| [**allient/git-graph-tui · integrations/herdr**](https://github.com/allient/git-graph-tui/tree/main/integrations/herdr) | Opens an interactive Git graph in a Herdr TUI tab to inspect commits and run Git operations with context menus. |
| [**elKei24/herdr-co-review**](https://github.com/elKei24/herdr-co-review) | Opens a split-screen pull-request review in Herdr TUI so a person can inspect agent findings against code and approve comments for posting. |
| [**inferst/herdr-review.nvim**](https://github.com/inferst/herdr-review.nvim) | Reviews code in Neovim with Git and Herdr integration. |
| [**speardragon/herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox) | Collects blocked Claude `AskUserQuestion` prompts from all Herdr workspaces into one popup, where pending questions can be reviewed and answered safely. |
| [**yuucu/herdr-hunk**](https://github.com/yuucu/herdr-hunk) | Toggles a live Hunk diff overlay for a Herdr TUI workspace and refreshes it when an agent finishes. |
| [**quantk/herdr-review**](https://github.com/quantk/herdr-review) | Opens the agent's working-tree diff in a split or tab, supports line comments, and drafts the notes into the source agent's prompt without submitting them. It runs on Bun or Node without external diff tools. |
| [**VilfredSikker/easy-review · tools/herdr-easy-review**](https://github.com/VilfredSikker/easy-review/tree/main/tools/herdr-easy-review) | Opens Easy Review in Herdr TUI tabs for branch diffs or GitHub pull requests, including automatically for new worktrees. |
| [**alexeyco/herdr-review**](https://github.com/alexeyco/herdr-review) | Opens revdiff, tuicr or lumen for human diff review and sends annotations to the focused Herdr TUI agent. |
| [**rheech22/herdr-comment-on-copy**](https://github.com/rheech22/herdr-comment-on-copy) | Turns selected terminal text into comments that can be sent individually or together to an agent in Herdr TUI. |
| [**claytonjschneider/huicr**](https://github.com/claytonjschneider/huicr) | Reviews changes commit by commit in Herdr TUI and sends line or file comments to an agent or GitHub pull request. |
| [**cell-observatory/oak-observatory**](https://github.com/cell-observatory/oak-observatory) | Runs a terminal review app with a Herdr TUI backend to inspect agent sessions and keep or undo individual edits. |
| [**dorshinar/hunk-checkpoint**](https://github.com/dorshinar/hunk-checkpoint) | Creates Hunk review checkpoints at Herdr agent turn boundaries so users can review changes since the previous turn. |
| [**IgorWarzocha/herdr-annotations**](https://github.com/IgorWarzocha/herdr-annotations) | Captures notes attached to selected terminal text and stages those annotations for Herdr agents to act on. |
| [**shadowfax92/herdr-comments**](https://github.com/shadowfax92/herdr-comments) | Imports output from a Herdr agent pane into Neovim for line-level comments and organized review notes in editor buffers. |
| [**brianh20/herdr-stagr**](https://github.com/brianh20/herdr-stagr) | Adds a source-control sidebar for staging, unstaging, and discarding changes with side-by-side diffs inside Herdr. |
| [**tareqmlx/herdr-lazygit-viewer**](https://github.com/tareqmlx/herdr-lazygit-viewer) | Opens lazygit at the files, branches, commits, or stash panel, in whichever Herdr surface suits the moment. |
| [**pedroallenrevez/herdr-comments.nvim**](https://github.com/pedroallenrevez/herdr-comments.nvim) | Lets users select code in Neovim, add comments, and send them to a Herdr agent. |
| [**mbillz/shep**](https://github.com/mbillz/shep) | Auto-launches principal-engineer PR reviews in herdr when you're tagged as a reviewer. |
| [**andpeicunha/herdr-output-comment-composer**](https://github.com/andpeicunha/herdr-output-comment-composer) | Adds inline comments directly to AI-agent output in a Herdr pane. |
| [**andschneider/roboherd**](https://github.com/andschneider/roboherd) | Integrates roborev into Herdr TUI to show review status, start reviews, and inspect or comment on completed reviews. |
| [**Shi1xin/herdr-gitui**](https://github.com/Shi1xin/herdr-gitui) | Opens GitUI in a worktree-aware Herdr TUI sidebar pane with toggle and focus controls. |
| [**chasereyn/Vincent**](https://github.com/chasereyn/Vincent) | Reviews and edits agent-written code in a mouse-first terminal client. |
| [**aleslanger/herdr-strays**](https://github.com/aleslanger/herdr-strays) | Shows live changed files across Herdr TUI workspaces, opens diffs, and sends follow-up prompts to Claude. |
| [**baotran01/herdr-agent-diff**](https://github.com/baotran01/herdr-agent-diff) | Shows Git changes and source files in a read-only Herdr TUI review pane. |
| [**jorge-huxley/herdr-git-graph**](https://github.com/jorge-huxley/herdr-git-graph) | Shows a read-only Git commit graph with filters, search, and diffs in a Herdr TUI pane. |
| [**maedana/herdr-agents-preview**](https://github.com/maedana/herdr-agents-preview) | Tiles previews of all active agent panes while giving most of the terminal to the focused worker, preserving awareness of background agents without crowding the main task. |
| [**skellleks/lasso**](https://github.com/skellleks/lasso) | Shows per-agent changes in a Herdr review pane and sends inline comments back to the agent. |
| [**rytkmt/herdr-diff-review.nvim**](https://github.com/rytkmt/herdr-diff-review.nvim) | Reviews AI agent file changes in Neovim diff mode before applying, enabling single-command approve or deny actions. |
| [**spoj/pi-show-herdr**](https://github.com/spoj/pi-show-herdr) | Opens a copy of a text file in an editor inside a Herdr TUI tab and returns the resulting diff to Pi. |
| [**matiasvillaverde/herdr-lumen**](https://github.com/matiasvillaverde/herdr-lumen) | Opens repository diffs in a Herdr TUI review rail and sends line annotations back to the originating agent. |
| [**txmed82/herdr-code-review**](https://github.com/txmed82/herdr-code-review) | Runs a structured AI review of staged and unstaged changes in a Herdr TUI split or tab and sends findings to the source pane. |
| [**dannycroft/hunk-herdr-plugin**](https://github.com/dannycroft/hunk-herdr-plugin) | Opens Hunk diffs for worktree or other changes in a Herdr TUI split pane or tab. |
| [**cevr/herdr-hunk**](https://github.com/cevr/herdr-hunk) | Routes Hunk review notes back to the correct Herdr agent pane. |
| [**devenjarvis/herdr-review**](https://github.com/devenjarvis/herdr-review) | Adds an interactive plan-review stage to Herdr workflows. |
| [**pi-dal/herdr-preview**](https://github.com/pi-dal/herdr-preview) | Shows agent diffs in a Herdr TUI pane and sends line-range comments back as review feedback. |
| [**filafb/pr-deep-review**](https://github.com/filafb/pr-deep-review) | Runs coordinated Claude reviews of a pull request or branch and presents inline findings in a navigable terminal codebook inside Herdr TUI. |
| [**0xfelixli/herdr-notes**](https://github.com/0xfelixli/herdr-notes) | Annotates selected terminal text in a Rust popup textbox, herdr plugin. |
| [**roman/herdr-meat-review**](https://github.com/roman/herdr-meat-review) | Opens human code reviews with tuicr in Herdr TUI and returns review feedback to the agent. |
| [**juninaba/herdr-pr-preview**](https://github.com/juninaba/herdr-pr-preview) | Opens a Herdr split showing the current branch’s GitHub pull request and CI checks. |
| [**goofansu/herdr-hunk**](https://github.com/goofansu/herdr-hunk) | Opens a temporary Hunk overlay for Herdr review actions and restores the workspace on exit. |
| [**rewt/herdr-dia**](https://github.com/rewt/herdr-dia) | Connects Dia or Chromium to Herdr TUI agents for pull-request review and follow-up work from a browser side panel. |
| [**unok/stack-review**](https://github.com/unok/stack-review) | Opens stacked pull-request diffs and descriptions in a Herdr TUI workspace for review before submission. |

### File viewers, terminal browsers, and markdown previews

*49 projects. In-terminal file viewers, interactive web browsers, image previews, and markdown rendering panes.*

| Project | What it does |
|---|---|
| [**zenbu-labs/terminal-browser · herdr-plugin**](https://github.com/zenbu-labs/terminal-browser/tree/main/herdr-plugin) | Opens a terminal browser beside a Herdr TUI pane and supports agent-driven browser interaction. |
| [**smarzban/herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer) | Opens a read-only file viewer in a Herdr TUI split with Git status, diffs, Markdown, and source previews. |
| [**alexarthurs/herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar) | Opens a dockable file explorer and source-control panel with previews and AI-drafted commit messages in Herdr TUI. |
| [**iurysza/termscope**](https://github.com/iurysza/termscope) | Finds visible file paths and web links on the terminal screen, lets the user select one with fuzzy search, and opens it in a separate split without disturbing the main pane. |
| [**speardragon/herdr-yazi**](https://github.com/speardragon/herdr-yazi) | Opens the Yazi file manager in a Herdr pane or tab at the current directory while reusing the user's existing Yazi configuration. |
| [**StructuPath/herdr-browser**](https://github.com/StructuPath/herdr-browser) | Opens a drivable Chromium browser in a Herdr pane for agent automation and manual inspection. |
| [**alexarthurs/herdr-notes**](https://github.com/alexarthurs/herdr-notes) | Keeps one persistent Markdown note per workspace, with rendered and edit modes, autosave, and restoration after restarts. |
| [**dwarvesf/herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook) | Previews a file path from the clipboard in an overlay and can expand it into a full terminal viewer, avoiding manual path entry or temporary splits. |
| [**slara/terminal-markdown-renderer**](https://github.com/slara/terminal-markdown-renderer) | Opens rendered Markdown in a terminal browser from a Herdr TUI plugin. |
| [**thuanlm215/advanced-herdr-file-viewer**](https://github.com/thuanlm215/advanced-herdr-file-viewer) | Opens a Git-aware file viewer in Herdr TUI with workspace search, previews, file icons, and actions for opening workspaces and panes. |
| [**azizuysal/herdr-workbench**](https://github.com/azizuysal/herdr-workbench) | Opens a Herdr TUI sidebar with file browsing, text search, Git status, and previews. |
| [**ismaelosuna7824/herdr-file-viewer**](https://github.com/ismaelosuna7824/herdr-file-viewer) | Browses files, views code, and manages Git from a keyboard-driven Herdr pane. |
| [**rvalledorjr/herdr-fresh**](https://github.com/rvalledorjr/herdr-fresh) | Embeds the Fresh terminal IDE in a side pane and follows the active workspace root for quick file browsing and editing beside agents. |
| [**chappse6/herdr-blueprint**](https://github.com/chappse6/herdr-blueprint) | Shows agent-generated Markdown and Mermaid diagrams beside Claude Code or Codex in Herdr TUI. |
| [**rawnly/bracco**](https://github.com/rawnly/bracco) | Opens a Git-aware fuzzy file picker in a Herdr TUI popup and launches the selected file in an editor pane. |
| [**sebi75/herdr-canvas**](https://github.com/sebi75/herdr-canvas) | Renders agent-updated HTML boards, diagrams and charts into a Herdr TUI pane using headless Chrome. |
| [**arvindparmar-me/herdr-markdown-viewer**](https://github.com/arvindparmar-me/herdr-markdown-viewer) | Previews a selected Markdown file path in a right-hand Herdr split through a single shortcut. |
| [**devskale/herdr-flist**](https://github.com/devskale/herdr-flist) | Opens a narrow directory sidebar beside the focused pane and follows its current directory, including remote SSH shells where the path is parsed from the prompt. Entries are directory-first and include Git status markers. |
| [**jagzmz/herdr-annotations**](https://github.com/jagzmz/herdr-annotations) | Attaches local annotations to selected terminal text and groups them into reusable collections. Line-specific notes can be combined into one feedback prompt for an agent. |
| [**Only-Moon/herdr-yazi-windows**](https://github.com/Only-Moon/herdr-yazi-windows) | Adds a Windows port of herdr-yazi with native Windows pane spawning support via Herdr v0.8+. |
| [**Volpestyle/herdr-plugin-mermaid-preview**](https://github.com/Volpestyle/herdr-plugin-mermaid-preview) | Shows live Mermaid diagram previews for Claude Code and Codex output inside Herdr. |
| [**liambern/herdr-math**](https://github.com/liambern/herdr-math) | Renders inline and display LaTeX equations in Herdr TUI panes using MathJax and terminal graphics. |
| [**TinocoAI/scp-explorer**](https://github.com/TinocoAI/scp-explorer) | Browses an SSH host in a Herdr TUI split pane and uploads or downloads files through the existing connection. |
| [**yakovlevs01/herdr-yazi-links**](https://github.com/yakovlevs01/herdr-yazi-links) | Opens terminal file hyperlinks in a Yazi pane beside the source in Herdr TUI. |
| [**hx-w/herdr-visuals**](https://github.com/hx-w/herdr-visuals) | Previews Mermaid diagrams, LaTeX equations and local images beside agent conversations in Herdr TUI. |
| [**Trolzie/herdr-wherewasi**](https://github.com/Trolzie/herdr-wherewasi) | Shows a live rendered Markdown plan beside Herdr TUI agents and follows the focused repository or worktree. |
| [**to4iki/herdr-fzf-terminal-browser**](https://github.com/to4iki/herdr-fzf-terminal-browser) | Picks URLs from the current Herdr TUI pane with fzf and opens them in a terminal-browser split. |
| [**jomarmontuya/herdr-file-viewer**](https://github.com/jomarmontuya/herdr-file-viewer) | Adds a right-side Herdr TUI file tree with expandable folders, file tabs, and a source-control list. |
| [**bonkey/herdr-link-browser**](https://github.com/bonkey/herdr-link-browser) | Opens Ctrl-clicked HTTP links in a terminal-browser split beside the active Herdr TUI pane. |
| [**yigitkg/herdr-open-local-paths**](https://github.com/yigitkg/herdr-open-local-paths) | Finds file and folder paths mentioned in recent pane output and opens them with the operating system or reveals them in a file manager. When several paths exist, a picker lists files before folders. |
| [**worldnine/ashiato**](https://github.com/worldnine/ashiato) | Browses recently modified files with a terminal picker and uses the Herdr TUI worktree or workspace directory when available. |
| [**aclima01/herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows) | Opens a Windows text editor in a Herdr split with a directory tree, syntax highlighting, and an uncommitted-diff tab. |
| [**cyperx84/herdr-notes**](https://github.com/cyperx84/herdr-notes) | Creates a separate Markdown scratchpad for each Herdr workspace ID. Notes and prompt drafts open in a side split and stay outside the Git working tree. |
| [**gcaudan/herdr-explorer**](https://github.com/gcaudan/herdr-explorer) | Adds a VS Code-style file explorer, preview, diff, and source-control panes beside your agents. Review notes on diff lines go into the agent's prompt, and the agent can open `file:line` in the preview through a bundled skill. |
| [**pjs-0457/herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer) | Opens Yazi in a labelled Herdr tab or split at the workspace directory and relaunches it automatically after exit. |
| [**yukimaru77/herdr-latex-reflow**](https://github.com/yukimaru77/herdr-latex-reflow) | Renders AI-agent LaTeX in Herdr with transparent overlays, terminal-cell replacement, and inline reflow. |
| [**shivammehta25/herdr-file-picker**](https://github.com/shivammehta25/herdr-file-picker) | Opens an fzf file picker and inserts selected paths into the current Herdr pane without submitting the prompt. |
| [**float-ritual-stack/pi-herdr-outliner**](https://github.com/float-ritual-stack/pi-herdr-outliner) | Opens a local SQLite-backed block outliner in Herdr TUI panes for use by people and Pi agents. |
| [**nourhelmi/pi-rich-output**](https://github.com/nourhelmi/pi-rich-output) | Renders Pi images inline in Herdr TUI inside Ghostty and adds links to open originals at full size. |
| [**thanh-dong/herdr-rich-preview**](https://github.com/thanh-dong/herdr-rich-preview) | Previews files changed by Herdr agents in a browser, including Markdown, Mermaid, D2, HTML, and SVG. |
| [**AlexanderMakarov/herdr-preview**](https://github.com/AlexanderMakarov/herdr-preview) | Highlights visible file and directory paths in a Herdr TUI pane and opens a selected path in a file viewer. |
| [**olehsharov/herdr-imgpopup**](https://github.com/olehsharov/herdr-imgpopup) | Opens images from filenames, agents, or the CLI in a zoomable and pannable Herdr TUI overlay. |
| [**mariotmc/herdr-source-control**](https://github.com/mariotmc/herdr-source-control) | Shows changed files, the current branch, and upstream state in a Herdr TUI source-control pane. |
| [**u7chan/herdr-file-viewer**](https://github.com/u7chan/herdr-file-viewer) | Browses files in a read-only Herdr TUI pane with a keyboard-driven directory tree, previews, and configurable file actions. |
| [**linuxing3/herdr-nnn**](https://github.com/linuxing3/herdr-nnn) | Opens the nnn file manager in a Herdr split or tab at the focused pane's current directory. |
| [**Tetat-Chulchue/meadow**](https://github.com/Tetat-Chulchue/meadow) | Opens a mouse-driven file explorer in a Herdr TUI pane. |
| [**goofansu/herdr-notebook**](https://github.com/goofansu/herdr-notebook) | Opens a persistent Markdown notebook for each Herdr TUI workspace in the user’s editor. |
| [**RufusLin/herdr-openmd**](https://github.com/RufusLin/herdr-openmd) | Opens selected markdown in openmd, a rich Qt preview from herdr. |
| [**hidekingerz/herdr-plugin-mado**](https://github.com/hidekingerz/herdr-plugin-mado) | Opens agent-written Markdown in a Mado TUI viewer beside the agent. |

### Pane navigation and overlay hints

*33 projects. Direct 1-character overlay hints and smart directional pane jumping.*

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
| [**navishachiku/herdr-pinpoint**](https://github.com/navishachiku/herdr-pinpoint) | Selects a Herdr TUI space, tab or pane and inserts its identifier into the current agent conversation. |
| [**Hon-Lu/herdr-pane-shift**](https://github.com/Hon-Lu/herdr-pane-shift) | Rearranges Herdr TUI panes with keyboard shortcuts to swap, rotate, move, or break them into tabs. |
| [**AlexanderGrooff/herdr-pane-switcher**](https://github.com/AlexanderGrooff/herdr-pane-switcher) | Cycles through recently focused Herdr TUI panes or jumps to the agent pane needing attention. |
| [**joo-was-already-taken/herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab) | Toggles back to the previously focused Herdr TUI tab or workspace. |
| [**elliotekj/herdr-easymotion**](https://github.com/elliotekj/herdr-easymotion) | Overlays numbered hints on visible panes so users can jump directly to one in the active Herdr TUI tab. |
| [**geshido/herdr-column-layout**](https://github.com/geshido/herdr-column-layout) | Moves and arranges Herdr TUI panes in keyboard-driven columns without restarting processes. |
| [**enisbu/herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux) | Adds Linux touchpad gestures for navigating Herdr TUI panes, tabs, and spaces and focusing agents awaiting attention. |
| [**42lizard/herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout) | Rearranges existing Herdr TUI panes into DWM-style master and stack layouts without restarting their processes. |
| [**shadowfax92/herdr-beacon**](https://github.com/shadowfax92/herdr-beacon) | Jumps to unread, working, or recently active agents using Herdr TUI status and sidebar indicators. |
| [**youguanxinqing/herdr-hop**](https://github.com/youguanxinqing/herdr-hop) | Jumps to any visible Herdr pane by pressing a labeled key. |
| [**KadenThomp36/herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher) | Cycles through recently used Herdr TUI panes with Ctrl-Tab on macOS. |
| [**maedana/herdr-hint**](https://github.com/maedana/herdr-hint) | Displays Vimium-style single-letter labels over active tabs and agent panes so focus can jump directly to a target without cycling through the layout. |
| [**RooseveltAdvisors/herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap) | Jumps to visible word starts in Herdr TUI copy mode and adds Vim- and fzf-aware pane navigation. |
| [**shoaibkhanz/herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump) | Cycles focus through working or blocked Herdr agents in layout order, skipping idle and finished panes. |
| [**newro/herdr-agent-nav**](https://github.com/newro/herdr-agent-nav) | Numbers agent sidebar entries and switches between agents relative to the last focused agent. |
| [**choplin/herdr-quickselect**](https://github.com/choplin/herdr-quickselect) | Labels visible terminal text in Herdr TUI for keyboard selection and configurable actions such as copying or opening URLs. |
| [**dgnsrekt/herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke) | Pairs two existing Herdr TUI tabs side by side and restores the second tab with the same shortcut. |
| [**CaptainVincent/herdr-agent-jump**](https://github.com/CaptainVincent/herdr-agent-jump) | Jumps between Herdr TUI agents across workspaces using EasyMotion-style sidebar hints and a WezTerm key adapter. |
| [**mholtzscher/herdr-focus-or-tab**](https://github.com/mholtzscher/herdr-focus-or-tab) | Moves focus between adjacent Herdr TUI panes and continues into neighboring tabs at the edges. |
| [**hadeson/herdr-harpoon**](https://github.com/hadeson/herdr-harpoon) | Pins Herdr TUI panes to numbered slots and jumps to them across tabs and workspaces, retaining marks across restarts. |
| [**rokrdev/herdr-quick-jump**](https://github.com/rokrdev/herdr-quick-jump) | Displays inline pane-selection labels in a configurable-width picker and launches zoxide directories. |
| [**ultrakorne/herdr-link-hints**](https://github.com/ultrakorne/herdr-link-hints) | Labels links in the focused Herdr TUI pane with keyboard hints so users can open or copy them. |
| [**jmarcelomb/herdr-nav**](https://github.com/jmarcelomb/herdr-nav) | Navigates Herdr TUI panes, tabs, and workspaces through the local socket, crossing tab and workspace boundaries. |

### Pane layout management

*10 projects. Tools that arrange, resize, and manage Herdr TUI panes.*

| Project | What it does |
|---|---|
| [**thuanlm215/herdr-grid**](https://github.com/thuanlm215/herdr-grid) | Opens a visual editor for dragging, resizing, and safely rearranging live pane layouts without restarting pane processes. It can add shell panes, apply fixed presets, or build a preset in a new workspace. |
| [**osamahbeig/herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover) | Moves, re-splits, and swaps Herdr panes through a clickable overlay. |
| [**iurysza/herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts) | Adds tmux-style pane resizing and layouts to Herdr. |
| [**edouard-andrei/herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools) | Rearranges existing panes into main-left, grid, or equalized presets without changing pane IDs, tab IDs, or running processes. |
| [**crierr/herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout) | Adds tmux-style layout presets for Herdr, including even horizontal, even vertical, main horizontal, main vertical, tiled, cycle, and balance. |
| [**iuhoay/herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane) | Moves the active pane into a new tab while preserving its process, similar to tmux break-pane. It unzooms complex tabs first and leaves single-pane tabs unchanged. |
| [**carsonjones/herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles) | Adds named split ratios: 60/40 and 40/60 horizontal, 20/80 and 80/20 vertical, plus 50/50 resets. Modifier keys flip the larger side or return to equal sizing. |
| [**willfish/herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes) | Equalizes all panes in the active tab with one key, reproducing tmux `select-layout -E` behavior after repeated splits or resizing. |
| [**jone/herdr-wrangler**](https://github.com/jone/herdr-wrangler) | Adds tmux-style pane layouts and rotation to Herdr. |
| [**yuloop/herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move) | Moves and rearranges Herdr panes across tabs using keyboard shortcuts. |

### Terminal keybindings and shortcut helpers

*61 projects. Custom keymap packs, leader-key setups, and prefix-free navigation.*

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
| [**cskwork/herdr-cheatsheet**](https://github.com/cskwork/herdr-cheatsheet) | Summarizes Herdr TUI keybindings and CLI commands in a printable cheatsheet with an agent setup prompt. |
| [**maedana/herdr-normal-mode**](https://github.com/maedana/herdr-normal-mode) | Adds Vim-style sidebar navigation for Herdr TUI workspaces, agents, tabs, and numbered panes. |
| [**aliou/herdr-cast**](https://github.com/aliou/herdr-cast) | A macOS plugin combining agent notifications, fuzzy workspace switching, zoxide-based creation, and layout helpers. |
| [**AndresMpa/mu-herdr**](https://github.com/AndresMpa/mu-herdr) | Adds MμVim-style keybindings and a notification plugin to a shareable Herdr TUI configuration. |
| [**ppggff/herdr-plugin**](https://github.com/ppggff/herdr-plugin) | Remembers the macOS keyboard input source used in each Herdr pane and restores it when focus returns, using a bundled Swift helper or macism. |
| [**wraithyy/herdr-hintr**](https://github.com/wraithyy/herdr-hintr) | Shows available Herdr TUI shortcuts in a popup and runs the selected binding. |
| [**devoc09/herdr-equalize-vsplit**](https://github.com/devoc09/herdr-equalize-vsplit) | Splits the active pane vertically and immediately equalizes all column widths through Herdr's layout API. |
| [**Hariketsu/modern-terminal-keybindings**](https://github.com/Hariketsu/modern-terminal-keybindings) | Maps macOS-style shortcuts across Herdr TUI, Kitty, fish, and coding agents. |
| [**poweroutlet2/herdr-confirm-close-pane**](https://github.com/poweroutlet2/herdr-confirm-close-pane) | Provides a herdr plugin that asks for confirmation before closing a pane, like tmux's prefix+x confirm-before. |
| [**sf1tzp/herdr-pane-orientation-switcher**](https://github.com/sf1tzp/herdr-pane-orientation-switcher) | Toggles a two-pane Herdr TUI split between horizontal and vertical layouts while preserving processes, with zoom-aware split actions. |
| [**y4m3/herdr-zen**](https://github.com/y4m3/herdr-zen) | Centers a Herdr TUI pane at an adjustable width and restores its original layout when Zen mode ends. |
| [**malone-c/herdr-keybind-search**](https://github.com/malone-c/herdr-keybind-search) | Parses Herdr key bindings into an fzf overlay for searching and running configured actions without memorizing every shortcut. |
| [**3mmdrew/herdr-layout**](https://github.com/3mmdrew/herdr-layout) | Defines and creates Herdr workspace layouts in plain Lua, including pane splits and startup commands, without YAML or a separate service. |
| [**m4salah/herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last) | Adds tmux-style shortcuts for returning to the previous Herdr tab or workspace. |
| [**choplin/herdr-next-agent**](https://github.com/choplin/herdr-next-agent) | Moves between Herdr agents in configured semantic states. |
| [**itsmistermoon/bindr**](https://github.com/itsmistermoon/bindr) | Switches between named keybinding profiles and lets users view and edit bindings in a popup. |
| [**JacquesvanWyk/herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys) | Searches keybindings with an fzf cheatsheet and discovers bindings from local configuration files. |
| [**aorumbayev/herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland) | Adds Hyprland-inspired shortcuts for navigating and manipulating Herdr TUI panes, tabs, and workspaces. |
| [**cyperx84/herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump) | Focuses Herdr tab N by position from custom keybindings, splitting the number row between tabs and workspaces. |
| [**pedrobarco/herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus) | Toggles between recently focused Herdr TUI panes, tabs, or workspaces using focus-event history. |
| [**dantehemerson/herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab) | Tracks tab focus history and returns to the previously active Herdr tab with one keystroke. |
| [**jugyo/herdr-nav-history**](https://github.com/jugyo/herdr-nav-history) | Adds browser-style back and forward navigation across panes, tabs, and workspaces by recording focus changes from the Herdr socket event stream. |
| [**retroaalto/herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav) | Moves geometrically between panes based on their actual position, providing natural up, down, left, and right navigation in irregular Herdr grids. |
| [**shadowfax92/herdr-layouts**](https://github.com/shadowfax92/herdr-layouts) | Adds tmux-style narrow splits and focused-pane equalization to Herdr. |
| [**Roshvan/herdr-plugin-shortcut-shepherd**](https://github.com/Roshvan/herdr-plugin-shortcut-shepherd) | Tracks Herdr TUI actions and surfaces shortcut statistics and coaching to help users learn keybindings. |
| [**bertverbessem/herdr-last-tab**](https://github.com/bertverbessem/herdr-last-tab) | Toggles between the current and previously focused Herdr TUI tab, keeping history separate per workspace. |
| [**newro/herdr-window-util**](https://github.com/newro/herdr-window-util) | Adds keybindable workspace, tab, and pane management actions with sidebar position numbers. |
| [**GHJQ/capslock-herdr-prefix**](https://github.com/GHJQ/capslock-herdr-prefix) | Maps Caps Lock to the Herdr TUI prefix key on macOS and backs up the configuration before changing it. |
| [**clayton/lernrherdr**](https://github.com/clayton/lernrherdr) | Teaches stock Herdr TUI key chords and CLI commands with browser drills, spaced repetition and timed practice. |
| [**susumutomita/annai.term**](https://github.com/susumutomita/annai.term) | Answers questions about local Ghostty and Herdr TUI keybindings using Apple on-device models on macOS. |
| [**BalajiLeninrajan/herdr-modes**](https://github.com/BalajiLeninrajan/herdr-modes) | Adds user-defined keyboard modes to Herdr TUI so repeated navigation actions can share one prefix press. |
| [**wg1k/live-sync-panes**](https://github.com/wg1k/live-sync-panes) | Broadcasts commands or synchronizes live keystrokes across all panes in a Herdr TUI tab. |
| [**vigneshwerv/herdr-golden-ratio**](https://github.com/vigneshwerv/herdr-golden-ratio) | Resizes the focused Herdr TUI pane to the golden ratio manually or automatically on focus changes. |
| [**artieeez/herdr-which-key**](https://github.com/artieeez/herdr-which-key) | Opens a which-key-style leader menu for Herdr TUI workspace, tab, and pane actions. |
| [**codyhxyz/herdr-chrome-keys**](https://github.com/codyhxyz/herdr-chrome-keys) | Maps Chrome-style workspace and tab shortcuts to Herdr TUI and includes a macOS Ghostty profile to pass the keys through. |
| [**tajdien/herdr-confirm-close**](https://github.com/tajdien/herdr-confirm-close) | Requires confirmation before closing a Herdr pane or tab, reducing accidental termination of long-running agent work. |
| [**ycros/herdr-compass**](https://github.com/ycros/herdr-compass) | Uses consistent directional keys across panes, tabs, and workspaces, moving to the next tab or workspace when the current pane layout has no target in that direction. |
| [**GroepOnline/herdr-plugins**](https://github.com/GroepOnline/herdr-plugins) | A mirrored Herdr plugin collection migrated from OnlineChefGroep/herdr-plugins. |
| [**BryanHeBY/anolisa-herdr-plugin**](https://github.com/BryanHeBY/anolisa-herdr-plugin) | Integrates the ANOLISA tool suite with Herdr terminal workspaces. |
| [**mi2428/herdr-agent-layout**](https://github.com/mi2428/herdr-agent-layout) | Maintains a readable minimum width for a supervisor pane and arranges worker panes around it. |
| [**amiramay/herdr-layout-cycle**](https://github.com/amiramay/herdr-layout-cycle) | Cycles through preset Herdr pane layouts with a tmux-style prefix-and-space action. |
| [**corrius/herdr-numbered-navigation**](https://github.com/corrius/herdr-numbered-navigation) | Deprecated. Its numbered-navigation features moved to herdr-session-organizer version 0.3.0 and later. |
| [**ViSHNUPrABU/herdr-codex**](https://github.com/ViSHNUPrABU/herdr-codex) | An unofficial Herdr-related Codex project. The source catalog contains only version, license, and non-affiliation notices, with no feature description. |
| [**DMelisena/shipmates**](https://github.com/DMelisena/shipmates) | A Hermes plugin offering a preconfigured Kun Chen-style Herdr and OpenCode first-mate workflow. The source catalog does not describe its individual controls. |
| [**juezhong/herdr-positional-tabs**](https://github.com/juezhong/herdr-positional-tabs) | Provides a stable positional tab labels and Alt-number navigation for Herdr. |
| [**andischerer/herdr-plugin-echo**](https://github.com/andischerer/herdr-plugin-echo) | Broadcasts keystrokes from one Herdr TUI pane to selected panes in the same tab. |
| [**brant92good/terminal-workspace**](https://github.com/brant92good/terminal-workspace) | Opens a remote shell and its port forwards in Windows Terminal, with machine-aware shortcuts and optional local or remote Herdr. |
| [**mikedyan/herdrill**](https://github.com/mikedyan/herdrill) | Provides an aim trainer for your Herdr keybindings. 60 seconds to find out if they're muscle memory or wishful thinking. |
| [**gwelican/herdr-keybinds**](https://github.com/gwelican/herdr-keybinds) | Searches configured Herdr TUI keybindings, including plugin actions, and flags collisions in a popup. |
| [**QuantumDancer/herdr-last-tab**](https://github.com/QuantumDancer/herdr-last-tab) | Switches back to the previously focused Herdr tab. |
| [**yuloop/herdr-plugin-win-terminal**](https://github.com/yuloop/herdr-plugin-win-terminal) | Configures Windows Terminal keymaps and profiles for direct Herdr navigation. |

### Command palettes and workspace switchers

*38 projects. Searchable menus for Herdr commands, projects, workspaces, and common actions.*

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
| [**hota911/herdr-command-palette**](https://github.com/hota911/herdr-command-palette) | Opens an fzf popup for Herdr TUI workspace, tab, pane, agent, and configuration commands. |
| [**vika2603/herdr-palette**](https://github.com/vika2603/herdr-palette) | Searches Herdr TUI commands, plugin actions, configured scripts, and open panes from a popup. |
| [**Binb1/herdr-palette**](https://github.com/Binb1/herdr-palette) | Searches Herdr TUI sessions, plugin actions, built-in commands, SSH machines, workspaces, and agents from a popup. |
| [**y-hirakaw/herdr-launcher-pane**](https://github.com/y-hirakaw/herdr-launcher-pane) | Opens a docked Herdr TUI pane or popup for running configured commands against selected workspaces. |
| [**abrose/herdr-url-picker**](https://github.com/abrose/herdr-url-picker) | Picks a URL from the current pane with fzf and opens it in the default browser. |
| [**chouxcreams/herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker) | Picks a URL from the focused pane and opens it in the default browser. |
| [**fabiogaliano/herdr-command-palette**](https://github.com/fabiogaliano/herdr-command-palette) | Opens a searchable Herdr TUI action palette with shortcuts, live agents and installed plugin commands. |
| [**haisi/herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette) | Searches effective Herdr TUI keybindings and custom commands with fzf and runs the selected action. |
| [**barnuri/herdr-command-palette**](https://github.com/barnuri/herdr-command-palette) | Searches and runs installed Herdr plugin actions through a command palette. |
| [**zackshen/herdr-telescope**](https://github.com/zackshen/herdr-telescope) | Searches Herdr TUI native and plugin actions alongside files and live ripgrep results in an fzf popup. |
| [**ningxiaoxiao/herdr-agent-picker**](https://github.com/ningxiaoxiao/herdr-agent-picker) | Enables the user choose an AI agent and working directory before Herdr creates a new tab, split, or workspace. |
| [**oppenheimor/herdr-prompts**](https://github.com/oppenheimor/herdr-prompts) | Saves and searches reusable prompt templates, fills variables, and inserts the result into the focused agent input. |
| [**bkarpinos/herdr-locksmith**](https://github.com/bkarpinos/herdr-locksmith) | Searches and runs Herdr TUI actions, configured commands, and plugin actions from a keybinding-aware command palette. |
| [**dmytr0x/herdr-task-picker**](https://github.com/dmytr0x/herdr-task-picker) | Adds a Herdr plugin that fuzzy-searches and runs built-in or custom go-task commands in the focused workspace. |
| [**nemolize/herdr-plugin-command-palette**](https://github.com/nemolize/herdr-plugin-command-palette) | Fuzzy-searches Herdr TUI commands, plugin actions, and session targets from a popup, including on Termux. |
| [**leonho/herdr-cmd-marks**](https://github.com/leonho/herdr-cmd-marks) | Runs global, project and automatically detected command bookmarks in a separate Herdr TUI popup shell. |
| [**kfujii-6jo/raycast-extensions**](https://github.com/kfujii-6jo/raycast-extensions) | Finds and focuses Herdr TUI workspaces and agents or opens local Git repositories from Raycast. |
| [**TaylorFinklea/herdr-ask**](https://github.com/TaylorFinklea/herdr-ask) | Opens a popup to translate plain-English requests into shell commands, letting you review and insert them into the active pane with Ctrl+Enter. |
| [**phine-apps/mux-prompter**](https://github.com/phine-apps/mux-prompter) | Searches local prompt libraries with fzf and inserts a context-aware template into the active Herdr pane. |
| [**tomotochi/herdr-plugin-picker**](https://github.com/tomotochi/herdr-plugin-picker) | Takes selections from terminal browsers or search tools and inserts them into the pane that opened the picker. |
| [**daltonkyemiller/herdr-plugin-switchboard**](https://github.com/daltonkyemiller/herdr-plugin-switchboard) | Launches Claude, Codex, OpenCode, or Pi from a picker and switches between the remembered agent and the active pane. |
| [**AnnanKhan/herdr-agent-launcher**](https://github.com/AnnanKhan/herdr-agent-launcher) | Adds a clickable agent-launcher pane. Left-click starts the configured default agent, while right-click opens the full list. |
| [**spro/herdr-agent-launcher**](https://github.com/spro/herdr-agent-launcher) | Opens a named Herdr tab running a selected Claude model. |
| [**bkroeze/omherdr**](https://github.com/bkroeze/omherdr) | An Omarchy and Wayland Quickshell status launcher for Herdr. |
| [**lucasleon2107/herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher) | Opens a new Herdr tab with Claude Code already running. |
| [**quinnjr/herdr-claude-profile**](https://github.com/quinnjr/herdr-claude-profile) | Manages and switches `claude-profile` profiles from a Herdr overlay palette. |
| [**reobin/herdr-close-other-panes**](https://github.com/reobin/herdr-close-other-panes) | Closes every Herdr pane except the focused one using Vim-style ctrl-w o navigation. |
| [**matheuseabra/mbtop**](https://github.com/matheuseabra/mbtop) | Provides a tiny, minimal system monitor built to rendered as small herdr/tmux dashboard panes. |

### Status lines and workspace metadata

*94 projects. Status lines, external terminal and desktop bars, pane labels, and workspace metadata without sidebar or tab-label displays.*

| Project | What it does |
|---|---|
| [**fkiene/llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr) | Activates the llmtrim compression proxy in new Herdr workspaces, shows savings badges in pane rows, and opens llmtrim's dashboard in a split. It also warns when a pane did not inherit the proxy settings. |
| [**jankeesvw/omarchy-herdr**](https://github.com/jankeesvw/omarchy-herdr) | Runs herdr servers in the Omarchy bar, with every agent inside them, and a click that lands you on the one you picked. |
| [**rjyo/herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync) | Writes workspace, tab, and agent context to the outer terminal title. It uses pane metadata and status first, then falls back to recent prompts in local Claude Code or Codex session files. |
| [**wenhanweime/herdr-plugin-renamer**](https://github.com/wenhanweime/herdr-plugin-renamer) | Uses an LLM to name sessions for Claude Code, Codex, Grok, Pi, and OpenCode, with Chinese or English labels and OpenCode Zen as the default engine. |
| [**njpatel/omaherdr**](https://github.com/njpatel/omaherdr) | Shows Herdr TUI sessions, spaces, tabs, and agents in the Omarchy bar and jumps to a selected item. |
| [**bcihanc/herdr-claude-session-title**](https://github.com/bcihanc/herdr-claude-session-title) | Copies the Claude Code session title, including `/rename` or automatic summaries, into Herdr pane metadata. |
| [**flowy11/agent-panel**](https://github.com/flowy11/agent-panel) | Shows the focused Claude Code or Codex session, subagents, messages, references and tasks in a Herdr TUI side panel. |
| [**Phoobobo/herdr-workboard**](https://github.com/Phoobobo/herdr-workboard) | Shows Herdr TUI workspaces as Kanban boards and moves live panes between task-state tabs. |
| [**Razz21/herdr-devserver-status**](https://github.com/Razz21/herdr-devserver-status) | Detects dev servers in panes via pluggable specs and reports lifecycle status. |
| [**minhtran3124/herdr-worktree-agents**](https://github.com/minhtran3124/herdr-worktree-agents) | Shows worktrees, agent states, pull-request checks and Git status in a Herdr TUI panel. |
| [**jsmenzies/mergr**](https://github.com/jsmenzies/mergr) | Adds compact GitHub pull-request and review indicators to Herdr workspace rows by periodically checking the branch associated with each workspace. |
| [**krystof018/herdr-git-status**](https://github.com/krystof018/herdr-git-status) | Shows GitHub or GitLab CI state in workspace labels and an on-demand pane. It includes pull-request or merge-request numbers, recent failures, clickable links, and review-state markers. |
| [**briankeefe/herdr-omp**](https://github.com/briankeefe/herdr-omp) | Corrects false-idle Oh My Pi agent states and names Herdr workspaces after tasks. |
| [**carlotran4/omarchy-herdr**](https://github.com/carlotran4/omarchy-herdr) | Adds a native Omarchy bar plugin for live Herdr coding-agent status and one-click focus. |
| [**marcoskichel/herdr-muster**](https://github.com/marcoskichel/herdr-muster) | Labels each Herdr workspace with live agent states such as working or blocked, making attention-heavy workspaces easy to spot. |
| [**cdowell09/herdr-pr-board**](https://github.com/cdowell09/herdr-pr-board) | Combines open pull requests from several repositories and shows CI, review, and branch state beside agent workspaces. |
| [**mroth/herdr-jj-status**](https://github.com/mroth/herdr-jj-status) | Displays Jujutsu bookmarks, working-copy state, and change IDs in Herdr workspace rows and updates them as agents modify or switch workspaces. |
| [**stappmus/Udder**](https://github.com/stappmus/Udder) | Shows Herdr agents in the Omarchy bar, notifies when work finishes, and jumps back to the relevant pane. |
| [**JoanGil/herdr-unread-marker**](https://github.com/JoanGil/herdr-unread-marker) | Marks or unmarks a focused Herdr TUI agent as unread with a keybinding and keeps the flag until manually cleared. |
| [**cdc-lst/herdr-wait**](https://github.com/cdc-lst/herdr-wait) | Examines the process tree of idle or blocked panes and replaces generic state with a specific waiting label, such as a build or external CLI name. |
| [**carlotran4/waybar-herdr**](https://github.com/carlotran4/waybar-herdr) | An event-driven Waybar module for Herdr agent status. |
| [**fabandrade88/tamagoxtix · herdr**](https://github.com/fabandrade88/tamagoxtix/tree/main/herdr) | Adds a pixel-monster status display, usage charts and a powerline-style status line to Herdr TUI. |
| [**ryanlewis/herdr-workspace-renamer**](https://github.com/ryanlewis/herdr-workspace-renamer) | Copies agent session names onto the corresponding Herdr workspace labels. |
| [**Tyru5/herdr-agent-state**](https://github.com/Tyru5/herdr-agent-state) | Shows real-time, human-readable summaries of what each agent in the current Herdr workspace is doing. |
| [**calebcauthon/herdr-theos-settler**](https://github.com/calebcauthon/herdr-theos-settler) | Moves finished Herdr agent tabs and workspaces below active work so completed items stay visible but out of the main path. |
| [**aclima01/herdr-powershell-title-sync**](https://github.com/aclima01/herdr-powershell-title-sync) | Updates a Windows PowerShell terminal title from the focused Herdr workspace and agent state using native console escapes and event listeners. |
| [**panuhorsmalahti/herdr-space-topic**](https://github.com/panuhorsmalahti/herdr-space-topic) | Renames Herdr TUI spaces to match the active topic of their primary agent pane. |
| [**jmarbutt/herdr-spaces-pr-status**](https://github.com/jmarbutt/herdr-spaces-pr-status) | Shows GitHub pull request status on herdr spaces, with a Conductor-style PR board. |
| [**usrivastava92/herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev) | Detects Rovo Dev CLI sessions and reports them as live agents in Herdr. |
| [**iiii1224/herdr-statusline**](https://github.com/iiii1224/herdr-statusline) | Adds a customizable tmux-compatible status line to Herdr TUI sessions, including shell-command segments. |
| [**4Born/herdr-pane-id-labeler**](https://github.com/4Born/herdr-pane-id-labeler) | Keeps pane labels synchronized with public identifiers such as `w1:p2` as panes and workspaces are created, split, or closed. |
| [**nytafar/herdr-cache-ttl**](https://github.com/nytafar/herdr-cache-ttl) | Shows a color-coded countdown for each pane's prompt-cache lifetime and can sort agents by cache urgency so warm sessions are used before expiry. |
| [**b12o/herdr-pane-autorename**](https://github.com/b12o/herdr-pane-autorename) | Autorenames panes with the name of the current running process. |
| [**nengqi/herdr-session-sync**](https://github.com/nengqi/herdr-session-sync) | Synchronizes Claude Code and Codex session names across Herdr pane labels, terminal titles, and compatible mobile views. |
| [**Ghost-LZW/pane-identity**](https://github.com/Ghost-LZW/pane-identity) | Displays pane IDs, hostnames, and labels in Herdr without modifying your agents. |
| [**WSeubring/omarchy-agent-sessions**](https://github.com/WSeubring/omarchy-agent-sessions) | Shows Herdr-hosted coding-agent status, directory, and title in the Omarchy bar. |
| [**daocoding/omarchy-claude-agent**](https://github.com/daocoding/omarchy-claude-agent) | Shows Claude Code lifecycle states and per-pane details in the Omarchy bar using the Herdr lifecycle reporter. |
| [**wujunchuan/pi-rename-pane**](https://github.com/wujunchuan/pi-rename-pane) | Generates Pi session names and synchronizes them to the current Herdr TUI pane. |
| [**jackfrancisdalton/herdr-chromatic-spaces**](https://github.com/jackfrancisdalton/herdr-chromatic-spaces) | Assigns persistent colors and symbols to Herdr TUI spaces, groups agents by space, and optionally tints the interface. |
| [**CristianPeralta/herdr-aws-freetier-bar**](https://github.com/CristianPeralta/herdr-aws-freetier-bar) | Shows AWS spending against a configured cap and per-service Free Tier usage in a persistent Herdr TUI pane. |
| [**rcosteira79/herdr-readpending**](https://github.com/rcosteira79/herdr-readpending) | Marks agents you haven't finished reading. Numbered badge ($read) + a reorderable list pane. |
| [**chouxcreams/herdr-dashboard**](https://github.com/chouxcreams/herdr-dashboard) | Shows pull-request, CI, and approval state across Herdr TUI workspaces and lets users jump to the responsible pane. |
| [**woshahua/herdr-github-pr**](https://github.com/woshahua/herdr-github-pr) | Syncs GitHub PR status, checks, reviews, and comments. |
| [**aclima01/herdr-todos-windows**](https://github.com/aclima01/herdr-todos-windows) | Shows a Herdr TUI agent’s task list and live status in a split pane. |
| [**yansfil/herdr-agent-context-labels**](https://github.com/yansfil/herdr-agent-context-labels) | Adds compact task summaries and runtime status labels to Herdr coding-agent panes. |
| [**rcosteira79/herdr-plugins**](https://github.com/rcosteira79/herdr-plugins) | Contains two separate Herdr plugins: an idle-shell badge and a read-pending indicator. |
| [**winoooops/herdr-agent-title-sync**](https://github.com/winoooops/herdr-agent-title-sync) | Synchronizes pane titles with active Claude Code, Codex, Kimi Code, and OpenCode sessions as their tasks or roles change. |
| [**ferretorres/herdr-plugin-space-colors**](https://github.com/ferretorres/herdr-plugin-space-colors) | Gives each workspace a colour that follows the focused workspace across the Herdr theme, a marker on every agent row and Space row, the pane backgrounds, and the macOS terminal window and its title bar. Rules pin a colour to a path or label; unmatched workspaces are coloured from a hash of their directory. |
| [**Anthodev/herdr-context**](https://github.com/Anthodev/herdr-context) | Opens a project context pane beside a Herdr TUI agent with a file tree, Git status, and conversation history. |
| [**JasonBates/agentdeck-rs**](https://github.com/JasonBates/agentdeck-rs) | Provides a local, model-enriched control surface for people running several coding agents at once. |
| [**matt-shearing/omarchy-herdr**](https://github.com/matt-shearing/omarchy-herdr) | Provides a quiet, security-hardened Herdr companion for the Omarchy bar. |
| [**lixenstrand/omarchy-herdr-drop-plugin**](https://github.com/lixenstrand/omarchy-herdr-drop-plugin) | Shows live Herdr agent status and toggles Herdr Drop from an Omarchy bar widget. |
| [**gcgo/herdr-plugin-pane-id-namer**](https://github.com/gcgo/herdr-plugin-pane-id-namer) | Labels Herdr TUI panes with IDs and names unnamed agents after their working-directory basename. |
| [**vandemaelefelix/herdr-herd**](https://github.com/vandemaelefelix/herdr-herd) | Displays a pixel-art animal for each Herdr TUI agent, changing its animation with the agent lifecycle state. |
| [**mikevalstar/herdr-machine-title**](https://github.com/mikevalstar/herdr-machine-title) | Pins the outer terminal title to the Herdr hostname and active workspace. |
| [**bonkey/herdr-stack-icon**](https://github.com/bonkey/herdr-stack-icon) | Displays technology stack icons beside each workspace based on repository file detection. |
| [**daocoding/herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle) | Reports Claude Code working, blocked, and idle states to Herdr from hooks and writes a state file for an Omarchy widget. |
| [**SpatialNexus/herdr-subagent-state**](https://github.com/SpatialNexus/herdr-subagent-state) | Uses Claude Code, Codex, and Pi hooks to report working state while tools or delegated subagents are active. |
| [**AdamGarceau/herdr-autoname**](https://github.com/AdamGarceau/herdr-autoname) | Names a Herdr pane from a Claude Code session topic using local Ollama and updates it as the topic changes. |
| [**jeremylongshore/omarchy-crew-chief-entry**](https://github.com/jeremylongshore/omarchy-crew-chief-entry) | Shows Herdr TUI agent states in the Omarchy bar and highlights sessions waiting for attention. |
| [**wynemo/herdr-agent-topic**](https://github.com/wynemo/herdr-agent-topic) | Shows the latest user prompt in each Herdr TUI agent card for Claude Code, Codex, Grok, Antigravity, and Pi. |
| [**Mor-dev/herdr-agent-monitor**](https://github.com/Mor-dev/herdr-agent-monitor) | Shows live Herdr TUI and Herdr app agent states in a DankMaterialShell bar widget and focuses an agent on click. |
| [**snaka/kelpie**](https://github.com/snaka/kelpie) | Shows working, blocked, and completed Herdr TUI agent counts in the macOS menu bar. |
| [**pxdl/omp-herdr-auto-name**](https://github.com/pxdl/omp-herdr-auto-name) | Synchronizes Oh My Pi session titles to Herdr TUI pane labels and agent names. |
| [**H3xept/git-shepherd**](https://github.com/H3xept/git-shepherd) | Shows draft, open, merged, or closed pull request status beside each Herdr space. |
| [**Haichiu/herdr-pane-id-border**](https://github.com/Haichiu/herdr-pane-id-border) | Adds a minimal Herdr plugin that shows canonical pane IDs on pane borders. |
| [**michiomochi/herdr-sound-toggle**](https://github.com/michiomochi/herdr-sound-toggle) | Adds a persistent Herdr TUI workspace pane for viewing and toggling sound notifications. |
| [**ThbltLmr/herdr-omarchy-widget**](https://github.com/ThbltLmr/herdr-omarchy-widget) | Shows local Herdr agent status and focuses the terminal from an Omarchy bar widget. |
| [**david-rzepa/omarchy-herdr-workspaces**](https://github.com/david-rzepa/omarchy-herdr-workspaces) | Highlights Omarchy workspace indicators for unread Herdr TUI agent activity and clears them when the exact tab is focused. |
| [**otavioschwanck/omarchy-quick-herdr**](https://github.com/otavioschwanck/omarchy-quick-herdr) | Shows local and SSH-connected Herdr TUI agent statuses in the Omarchy bar and lets users inspect or jump to agents. |
| [**filoozom/herdr-title**](https://github.com/filoozom/herdr-title) | Shows the selected worktree and agent activity in the outer terminal title. |
| [**hodkovickybuh/herdr-colors**](https://github.com/hodkovickybuh/herdr-colors) | Adds workspace color coding and agent attention indicators to a Herdr TUI fork. |
| [**khatriafaz/herdr-plugin-auto-rename**](https://github.com/khatriafaz/herdr-plugin-auto-rename) | Uses the first agent prompt to rename the active Herdr workspace and Git branch so task names remain descriptive without manual editing. |
| [**polidog/herdr-gh-issue-label**](https://github.com/polidog/herdr-gh-issue-label) | Displays corresponding GitHub issue numbers and titles in Herdr workspace status lines. |
| [**viko16/herdr-git-dirty**](https://github.com/viko16/herdr-git-dirty) | Displays uncommitted Git file counts in each Herdr space. |
| [**choplin/herdr-agent-metadata**](https://github.com/choplin/herdr-agent-metadata) | Shows when each Herdr agent's semantic state was last observed changing. |
| [**go-min/herdr-pane-name**](https://github.com/go-min/herdr-pane-name) | Inspects running processes and detected agents to replace numbered pane labels with meaningful command or agent names. |
| [**hasuwini77/herdr-follow-cwd**](https://github.com/hasuwini77/herdr-follow-cwd) | Renames a Herdr workspace from the active pane's current directory, with configurable path boundaries that keep names anchored to the project root. |
| [**michiomochi/herdr-plugin-sidenote**](https://github.com/michiomochi/herdr-plugin-sidenote) | Shows a persistent per-workspace information pane in Herdr TUI. |
| [**mackt/herdr-window-title**](https://github.com/mackt/herdr-window-title) | Writes template-formatted Herdr session and agent state into the outer terminal window title, including whether background agents are working, blocked, or done. |
| [**natori-hrj/herdr-green**](https://github.com/natori-hrj/herdr-green) | Runs a project’s tests when its coding agent finishes and reports per-pane pass or fail in Herdr TUI. |
| [**akhillb/herdr-attention**](https://github.com/akhillb/herdr-attention) | Docks a theme-matched countdown to the next Google Calendar meeting and highlights the pane when the meeting is ten minutes away. |
| [**dnf0/herdr-llm-summary-header**](https://github.com/dnf0/herdr-llm-summary-header) | Creates a one-line LLM summary when an agent finishes and writes it into the pane header so completed work can be scanned without opening scrollback. |
| [**sergeybataev/herdr-codex-session-title**](https://github.com/sergeybataev/herdr-codex-session-title) | Watches Codex session logs and updates Herdr agent labels with the current conversation topic. |
| [**cokekitten/pi-recap**](https://github.com/cokekitten/pi-recap) | Summarizes recent activity and can synchronize session titles with Herdr or tmux. |
| [**scaryrawr/herdr-agent-title**](https://github.com/scaryrawr/herdr-agent-title) | Displays Herdr agent information in the outer terminal window title. |
| [**the-inconvenience-store/herdr-agent-session-title**](https://github.com/the-inconvenience-store/herdr-agent-session-title) | Copies Claude Code or Codex session titles into Herdr pane metadata. |
| [**alex-devdone/raycast-herdr-status-bar**](https://github.com/alex-devdone/raycast-herdr-status-bar) | Shows Herdr agent states, token use, and session duration in the Raycast menu bar. |
| [**GuillermoDSM/hypr-herdr**](https://github.com/GuillermoDSM/hypr-herdr) | Integrates Herdr spaces and panes with Omarchy and Hyprland. |
| [**afokapu/herdr-workspace-agents**](https://github.com/afokapu/herdr-workspace-agents) | Provides a live workspace-scoped agent view for herdr, derived from events.subscribe, since herdr 0.7.4 has no server-side agent filter. |
| [**satoshi-hashimoto52/herdr-custom**](https://github.com/satoshi-hashimoto52/herdr-custom) | Extends Herdr with custom UI elements, status indicators, and resource usage displays. |
| [**tjcelaya/omarchy-modelctl**](https://github.com/tjcelaya/omarchy-modelctl) | Lists coding agents in an Omarchy bar and focuses their Herdr TUI panes. Also controls local llama.cpp and stable-diffusion.cpp servers. |
| [**andreconde21/omarchy-herdr**](https://github.com/andreconde21/omarchy-herdr) | Monitors local and remote Herdr workspaces with native agent status inside the Omarchy top bar. |
| [**Edvardunsvag/herdr-sidebar**](https://github.com/Edvardunsvag/herdr-sidebar) | Shows a narrow Herdr TUI status board for work awaiting attention in a right-hand pane. |

### Sidebar displays and tab labels

*128 projects. Sidebar displays and tab labels, including tab titles, icons, badges, and their synchronization.*

| Project | What it does |
|---|---|
| [**kryptamine/herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title) | Updates Herdr tab titles automatically based on active workspace tasks to keep development contexts organized. |
| [**qu8n/herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename) | Renames tabs from the active foreground process and icon, and prefixes workspaces, tabs, and agents with numbers 1 through 9 for quick visual and keyboard selection. |
| [**hhdebb/herdr-radar**](https://github.com/hhdebb/herdr-radar) | Shows agent activity in the Herdr TUI sidebar, grouping workspaces and worktrees and highlighting waiting or stale sessions. |
| [**robbyrussell/herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh) | Integrates Herdr with Oh My Zsh, displaying slow commands in the sidebar and triggering desktop completion notifications. |
| [**iurysza/herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename) | Uses a lightweight LLM to derive short workspace and tab names from pane activity, replacing generic numbers or directory labels with current task summaries. |
| [**sh1ma/herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title) | Runs in the background and derives Herdr tab names from the topic and intent of Claude Code or Codex conversations. |
| [**FlorisKr/herdr-openspec**](https://github.com/FlorisKr/herdr-openspec) | Shows OpenSpec change and task progress in the Herdr TUI sidebar and opens proposals, designs, and specs in a change browser. |
| [**eliasstravik/herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress) | Shows agent-reported task estimates and activity for Claude Code and Codex in the Herdr TUI sidebar. |
| [**wyattjoh/herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr) | Shows the GitHub pull-request number and CI state for the focused agent pane's branch in the Herdr sidebar. Updates are rate-limited, with shortcuts for manual refresh and opening the pull request. |
| [**bayoudhi/herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress) | Adds a live sidebar progress for slow shell commands, not just coding agents. |
| [**qintmb/herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui) | Adds larger agent icons, status glyphs, and a workspace, tab, and agent tree to the Herdr TUI sidebar. |
| [**testy-cool/herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config) | Adds a compact workspace, tab, and agent sidebar preset with provider icons to Herdr. |
| [**lachieh/herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux) | Mirrors Herdr TUI agents into the cmux sidebar with status, task text, and click-to-focus navigation. |
| [**getpipher/herdr-sysmon**](https://github.com/getpipher/herdr-sysmon) | Adds CPU, memory, battery, network, and disk measurements to Herdr sidebar tokens, with configurable refresh intervals and macOS-focused probes. |
| [**ShankyJS/herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents) | Limits the agent sidebar to workers in the currently focused workspace, reducing unrelated fleet noise when moving between projects. |
| [**kriuchkov/herdr-scope**](https://github.com/kriuchkov/herdr-scope) | Shows Herdr TUI agent state in a project-grouped sidebar and jumps to agents waiting for input. |
| [**aarsh21/herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title) | Provides automatic tmux-style tab titles for Herdr. |
| [**Numbered-com/herdr-ports**](https://github.com/Numbered-com/herdr-ports) | Detects TCP listeners started by processes in each workspace and adds a dynamic `$ports` badge to the Herdr sidebar. |
| [**wjarka/herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title) | Writes color-coded counts of working, blocked, done, and idle Herdr agents into Ghostty tab titles. |
| [**killerz3/herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler) | Auto-titles Herdr tabs using local agy, claude, codex, or opencode harnesses without external API keys. |
| [**kakigakki/herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer) | Uses Claude Code session titles for agent tabs and directory names for workspaces, providing automatic ChatGPT-style labels across parallel sessions. |
| [**danbuhler/herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync) | Renames panes and tabs from the active topic or terminal title emitted by Claude Code and Codex, while avoiding rename loops and respecting manual labels. |
| [**pdalinis/herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model) | Shows the active model and reasoning effort for Codex, Claude Code, Pi, and Hermes agents in the Herdr TUI sidebar. |
| [**lmilojevicc/herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename) | Renames each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. |
| [**rohankewal/herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name) | Ports tmux-nerd-font-window-name to Herdr, updating tab icons from the running program and directory context. |
| [**yukikisaku/pi-agent-status · packages/pi-herdr-status**](https://github.com/yukikisaku/pi-agent-status/tree/main/packages/pi-herdr-status) | Adds a working spinner, completion indicator, and AI-generated title to Herdr TUI tabs for Pi sessions. |
| [**Angel-O/herdr-labels**](https://github.com/Angel-O/herdr-labels) | Numbers Herdr TUI tabs and names eligible tabs after their foreground processes while preserving manual labels. |
| [**thewtex/herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load) | Displays CPU, memory, and load averages in the Herdr TUI workspace sidebar or prints a tmux-compatible status line. |
| [**BjoernSchotte/agentglass-herdr**](https://github.com/BjoernSchotte/agentglass-herdr) | Opens agentglass in a Herdr TUI popup and adds workspace cost and agent alert indicators to the sidebar. |
| [**gonzalonicolasr/herdr-bandeja-to-dos**](https://github.com/gonzalonicolasr/herdr-bandeja-to-dos) | Organizes Herdr TUI agents by attention state in the sidebar and shows to-dos left by agents. |
| [**ilazaridis/herdr-pane-issue**](https://github.com/ilazaridis/herdr-pane-issue) | Shows each Herdr TUI agent pane’s GitHub issue and pull request in the sidebar and opens the linked item. |
| [**Totopo27/hudr2**](https://github.com/Totopo27/hudr2) | Shows OpenCode and Pi agent context, usage, and repository information in a Herdr TUI sidebar. |
| [**hasuwini77/herdr-spinner**](https://github.com/hasuwini77/herdr-spinner) | Animates Herdr TUI working-state pane indicators and offers sidebar theme presets. |
| [**Xz-FreeMan/herdr-hint**](https://github.com/Xz-FreeMan/herdr-hint) | Adds Pi and Codex session names to Herdr TUI tab titles and reports session metadata, primarily on Windows. |
| [**jakekroon/herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker) | Shows authored pull requests and requests awaiting review in a Herdr TUI widget, with an optional branch PR sidebar token. |
| [**maxguzenski/herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch) | Shows GitHub pull request and CI status for Herdr TUI workspaces and agent panes in the sidebar. |
| [**maedana/herdr-whereami**](https://github.com/maedana/herdr-whereami) | Renames Herdr TUI tabs from the current directory or Git repository and reports a `$gitref` sidebar token. |
| [**ndom91/herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name) | Uses a local Ollama model to generate and update descriptive Herdr tab names from recent pane activity. |
| [**toyamarinyon/herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab) | Renames single-pane tabs from Claude Code or Codex thread titles through background session updates and the Herdr socket API. |
| [**justcyl/pi-herdr-tab-sync**](https://github.com/justcyl/pi-herdr-tab-sync) | Renames the active Herdr tab to the Pi session name when an agent starts or resumes. It communicates directly with the socket and remains inactive outside Herdr-managed panes. |
| [**davidolrik/herdr-titles**](https://github.com/davidolrik/herdr-titles) | Builds tab and terminal-window titles from foreground processes, agent session names, and workspace status counts using HCL templates. Shell hooks support Bash, Zsh, and Fish, and manual tab names are preserved. |
| [**Only-Moon/herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows) | Adds contextual Nerd Font icons to tab titles based on directory, project type, or running tool, with support for Windows, macOS, and Linux. |
| [**jolo-dev/herdr-workspace-icons**](https://github.com/jolo-dev/herdr-workspace-icons) | Adds rule-based workspace icons to expanded Herdr TUI desktop sidebar rows using workspace metadata. |
| [**dkbo/herdr-model-badge**](https://github.com/dkbo/herdr-model-badge) | Shows each agent's model and reasoning effort in the agents sidebar. |
| [**ZingerLittleBee/herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins) | Pins selected Herdr agent sessions to the top of the sidebar and restores their order across server restarts. |
| [**mcc0x/herdr-pulse**](https://github.com/mcc0x/herdr-pulse) | Samples agent lifecycle states and shows per-workspace activity history as sidebar sparklines. |
| [**jpwallace22/herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status) | Shows GitLab merge request status in each Herdr workspace sidebar row using an `$mr` token. |
| [**jwanga/herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status) | Shows GitHub milestones, issues, pull requests, and Actions in a Herdr sidebar pane. |
| [**yersonargotev/tabby**](https://github.com/yersonargotev/tabby) | Labels focused tabs with a Significant Command or Working Directory Basename. |
| [**geshido/icomark**](https://github.com/geshido/icomark) | Marks Herdr TUI tabs with workflow status and optional comments through keybindings or scripts. |
| [**voice0726/herdr-jump-number**](https://github.com/voice0726/herdr-jump-number) | Displays jump-key numbers on workspaces and tabs without breaking Herdr's automatic workspace labels. |
| [**andrewbrannan/herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs) | Displays GitHub pull request status and workspace links or notes in the Herdr TUI sidebar. |
| [**abrose/herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces) | Puts a number in front of every space in herdr's sidebar, matching the indexed switchworkspace shortcut. |
| [**blurname/herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name) | Keeps Herdr tab labels synchronized with the Git branch in the focused pane. |
| [**mattyan1053/herdr-compose**](https://github.com/mattyan1053/herdr-compose) | Shows Docker Compose service health for each workspace in the Herdr sidebar, with quick toggles and a service-details popup. Compose stacks are removed when their worktrees are deleted. |
| [**lucasleon2107/herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync) | Updates Herdr tab labels from agent conversation titles and prompt summaries, allowing names to change as the task evolves. |
| [**ryanlewis/herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer) | Renames tabs from the active agent's session title or working directory, replacing generic numbers with current task context. |
| [**shantanugoel/herdr-auto-namer**](https://github.com/shantanugoel/herdr-auto-namer) | Names Herdr TUI panes and tabs using deterministic rules without an LLM. |
| [**bayoudhi/herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times) | Displays the next Islamic prayer and a live countdown in the Herdr sidebar, with a timetable popup and optional desktop alerts. Schedules are fetched from Al Adhan and cached locally. |
| [**btorresgil/herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title) | Reads local Hermes Agent SQLite data and publishes descriptive conversation titles in the Herdr sidebar. |
| [**dev-shimada/herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name) | Keeps tab labels aligned with the focused pane's current directory and updates them on lifecycle and focus events without replacing manually chosen names. |
| [**szrenwei/herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata) | Adds current tab labels and state indicators to each workspace row in the Herdr sidebar and keeps them synchronized through lifecycle events. |
| [**tmn73/herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title) | Uses Claude Code session events to replace generic Herdr tab numbers with active task descriptions. |
| [**malone-c/herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename) | Renames panes and tabs from the active agent task or prompt by analysing live terminal activity and producing a concise label. |
| [**hasuwini77/herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git) | Shows the active tab’s Git branch and status in the Herdr TUI Spaces sidebar. |
| [**MrBogomips/herdr-tools**](https://github.com/MrBogomips/herdr-tools) | Sorts the spaces sidebar into top, default and bottom groups, gives every space of one customer the same colour (Space Herder), and names tabs after their folder, repo or branch (auto-tab-name). Also ships herdr-jump, a macOS menu bar picker that lists the agents waiting for you, blocked first and oldest wait first. |
| [**iko-soy/hermes-herdr-auto-title**](https://github.com/iko-soy/hermes-herdr-auto-title) | Updates Herdr tab titles automatically from the first user prompt using an LLM. |
| [**kewah/herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles) | Names panes and tabs automatically based on the first coding-agent prompt. |
| [**hxy91819/herdr-auto-title**](https://github.com/hxy91819/herdr-auto-title) | Names agent tabs automatically from an initial prompt and updates titles when turns settle. |
| [**christiangroth/herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal) | Names Herdr tabs from their agents’ terminal titles while leaving manually named tabs unchanged. |
| [**PegasusWang/herdr-agent-prompt**](https://github.com/PegasusWang/herdr-agent-prompt) | Shows the latest prompt and reply for Claude Code and Codex sessions in the Herdr agent sidebar. |
| [**T0mSIlver/herdr-title-wrap**](https://github.com/T0mSIlver/herdr-title-wrap) | Wraps pane terminal titles across multiple Herdr sidebar rows to fit the available width. |
| [**eduardoborges/herdr-claude-title-hook**](https://github.com/eduardoborges/herdr-claude-title-hook) | Syncs a Claude Code session title to its Herdr tab, including generated titles and `/rename`. |
| [**tiamointer/herdr-title-distill**](https://github.com/tiamointer/herdr-title-distill) | Updates Herdr tab titles automatically based on concise summaries of completed agent tasks. |
| [**sblevins/claude-rename-tab**](https://github.com/sblevins/claude-rename-tab) | Renames the current Herdr TUI tab to a short task-based label from a Claude Code session. |
| [**Ivotter/herdr-tab-session-name-sync**](https://github.com/Ivotter/herdr-tab-session-name-sync) | Synchronizes agent session names with Herdr tab and pane titles. |
| [**martian4202/pi-session-name**](https://github.com/martian4202/pi-session-name) | Names Pi sessions from recent messages and optionally synchronizes the title to the current Herdr TUI tab. |
| [**kazda01/pi-tab-status**](https://github.com/kazda01/pi-tab-status) | Shows live Pi status and generated descriptions in terminal tabs and Herdr sessions. |
| [**walidsi/pi-herdr-tab-namer**](https://github.com/walidsi/pi-herdr-tab-namer) | Adds a Pi extension that renames the current Herdr tab from a short summary of your first prompt in the session. |
| [**NachoPal/herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread) | Tracks unread agent activity per Herdr pane and displays a sidebar badge when an unfocused agent finishes or needs input. |
| [**kokatsu/herdr-numbering**](https://github.com/kokatsu/herdr-numbering) | Numbers Herdr tabs and sidebar workspaces by their switch position so their keyboard shortcuts are visible. |
| [**longcw/herdr-name-tab**](https://github.com/longcw/herdr-name-tab) | Names Herdr tabs from the first user input and retains the name until the topic changes. |
| [**btj93/herdr-tabline**](https://github.com/btj93/herdr-tabline) | Renders Herdr tab labels with safe templates and project-aware profiles. |
| [**iurysza/herdr-mosaic**](https://github.com/iurysza/herdr-mosaic) | Colors Herdr TUI spaces, groups agents in the sidebar, and arranges panes in the current tab. |
| [**ericcparsons/herdr-vitals**](https://github.com/ericcparsons/herdr-vitals) | Shows per-agent CPU and memory use and per-space server ports in the Herdr TUI sidebar, with a pane for stopping servers. |
| [**AlexBSoD/herdrtabrenamer**](https://github.com/AlexBSoD/herdrtabrenamer) | Renames Herdr TUI tabs automatically based on their running program, agent or working directory. |
| [**acjackman/herdr-title-rename**](https://github.com/acjackman/herdr-title-rename) | Adds tmux-style window titles and automatic tab/workspace renaming for herdr. |
| [**StarDuster/mimo-code-herdr-plugin**](https://github.com/StarDuster/mimo-code-herdr-plugin) | Shows MiMo Code agent state in herdr's sidebar, a user-level MiMo plugin, no herdr changes required. |
| [**cheoljoo/herdr-space-activity-monitor**](https://github.com/cheoljoo/herdr-space-activity-monitor) | Marks Space sidebar rows as printing / unseen-output / idle via a custom $activity token. |
| [**limars874/herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata) | Shows canonical pane IDs and compact tab and pane metadata in the Herdr sidebar. |
| [**FunnyQ/herdr-tab-bar-llm-quota**](https://github.com/FunnyQ/herdr-tab-bar-llm-quota) | Shows Claude and Codex quota in the herdr tab bar. |
| [**AndresDiagoM/herdr-route-audit**](https://github.com/AndresDiagoM/herdr-route-audit) | Shows under each agent in the sidebar which OmniRoute combo step served it (step 1 or a silent fallback to another model) and marks attributions it had to infer. Reads OmniRoute's call log read-only, pages Telegram once per fallback incident, and includes a report and a self-test. |
| [**GladioFeng/herdr-ghostty-title-bridge**](https://github.com/GladioFeng/herdr-ghostty-title-bridge) | Synchronizes Herdr TUI agent names and states to Ghostty tab titles with a socket watcher. |
| [**bonkey/herdr-pr-emoji**](https://github.com/bonkey/herdr-pr-emoji) | Shows pull request state on Herdr sidebar rows using emoji. |
| [**ayumu-1212/herdr-pasture**](https://github.com/ayumu-1212/herdr-pasture) | Groups agents by repository and docks them on the left of every Herdr tab. |
| [**bshearrer/herdr-project-filter**](https://github.com/bshearrer/herdr-project-filter) | Filters the Herdr TUI Agents sidebar to agents belonging to one Git repository. |
| [**inonprince/herdr-counting-sheep**](https://github.com/inonprince/herdr-counting-sheep) | Shows live workspace and agent positions in the Herdr TUI sidebar and adds navigation shortcuts. |
| [**yuritada/numberer-manager**](https://github.com/yuritada/numberer-manager) | Prefixes Herdr TUI workspace and tab labels with their current list positions. |
| [**DillonWall/herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers) | Numbers agents in the Herdr TUI sidebar to match the shortcuts used to focus them. |
| [**oddurs/herdr-namesync**](https://github.com/oddurs/herdr-namesync) | Keeps workspace, tab, and agent names current as the work changes, reading the intent the coding agent already publishes as its terminal title. Applies a rename policy with debouncing, rate limits, and locks for names you set by hand, and runs without a model unless you configure an OpenAI-compatible endpoint for stale titles. |
| [**kazimshah39/herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter) | Filters the Herdr agent sidebar to workspaces whose names share a chosen suffix, reducing noise in large multi-repository fleets. |
| [**sfroment/herdr-git-detail**](https://github.com/sfroment/herdr-git-detail) | Adds a `$git_detail` sidebar token with modified, staged, untracked, ahead, behind, and stash counts, refreshed when pane focus changes. |
| [**firew0rks/herdr-ci-tokens**](https://github.com/firew0rks/herdr-ci-tokens) | Shows pull-request, CI, and review state for every worktree in the Herdr sidebar. |
| [**choplin/herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity) | Adds the shared Git repository name to each Herdr TUI workspace sidebar row, including linked worktrees. |
| [**hermanvulkers/herdr-pr-status-plugin**](https://github.com/hermanvulkers/herdr-pr-status-plugin) | Shows each worktree's PR approvals, CI status, and mergeability as colored sidebar tokens. |
| [**timjonez/herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes) | Adds persistent manual notes to Herdr TUI agent sidebar rows to explain why an agent is idle or blocked. |
| [**RickyMarou/herdr-numbered-tabs**](https://github.com/RickyMarou/herdr-numbered-tabs) | Prefixes Herdr TUI tab labels with their current displayed positions and updates them when tabs are reordered. |
| [**edouard-andrei/herdr-smart-rename**](https://github.com/edouard-andrei/herdr-smart-rename) | Names Herdr TUI tabs and panes on demand using agent context and an OpenAI-compatible model. |
| [**jovylle/herdr-pane-mark**](https://github.com/jovylle/herdr-pane-mark) | Adds palette actions and a popup to edit a per-pane mark displayed in the Herdr TUI agent sidebar. |
| [**aiki-sh/aiki-integration-herdr**](https://github.com/aiki-sh/aiki-integration-herdr) | Shows active aiki epics in a live-refreshing Herdr sidebar and installs the companion session-identity hook. |
| [**elKei24/herdr-title-sync**](https://github.com/elKei24/herdr-title-sync) | A single-instance daemon that copies OSC terminal titles from Claude Code and similar agents into Herdr tab labels and periodically reconciles state through the socket. |
| [**adnichols/herdr-kitty-status**](https://github.com/adnichols/herdr-kitty-status) | Shows live Herdr agent-state counts in Kitty terminal tabs. |
| [**yuhgo/herdr-tab-marker**](https://github.com/yuhgo/herdr-tab-marker) | Automatically adds a task-based title and repository-specific emoji to Claude Code and Codex tabs in Herdr. |
| [**MorganCollins/herdr-last-used**](https://github.com/MorganCollins/herdr-last-used) | Shows when each herdr agent was last active, colour-coded by age, and filter the Agent sidebar by activity. |
| [**btj93/herdr-tokens**](https://github.com/btj93/herdr-tokens) | Publishes workspace metadata tokens derived from agent status, so sidebar colours can vary by state. |
| [**ubuntudroid/herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack) | Shows each space's position in its git branch stack in the spaces sidebar, flags branches whose parent has moved, and keeps stacks contiguous. Local commit graph only, no network, no forge API, no stacking tool. |
| [**Levi-Gillies/herdr-ssh-agents**](https://github.com/Levi-Gillies/herdr-ssh-agents) | Shows AI coding agents running over SSH in Herdr's sidebar. |
| [**dm4/herdr-workspace-sidebar**](https://github.com/dm4/herdr-workspace-sidebar) | Provides a Herdr plugin for displaying workspace tabs in a flat list. |
| [**sfc-gh-tmeacham/coco-herdr-plugin**](https://github.com/sfc-gh-tmeacham/coco-herdr-plugin) | Shows Cortex Code agent status in the Herdr TUI sidebar. |
| [**CowboyVang/herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges) | Shows a sidebar badge on Herdr TUI spaces containing multiple tabs. |
| [**mike-bronner/herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces) | Keeps the spaces sidebar in most-recently-used order. |
| [**jwbaldwin/herdr-auto-title**](https://github.com/jwbaldwin/herdr-auto-title) | Synchronizes managed Herdr TUI tab titles with OpenCode titles and adds agent status indicators. |
| [**shimonacarvalho/herdr-github-status**](https://github.com/shimonacarvalho/herdr-github-status) | Shows each Herdr TUI agent pane’s Git branch and repository or pull-request status in the sidebar. |
| [**Newt6611/herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title) | Numbers Herdr TUI tab titles within each workspace using a configurable format. |
| [**ralphilius/herdr-pr-tab-renamer**](https://github.com/ralphilius/herdr-pr-tab-renamer) | Renames Herdr TUI tabs with pull request numbers detected in new agent output. |
| [**imtim/herdr-pane-id**](https://github.com/imtim/herdr-pane-id) | Labels Herdr TUI panes with IDs and agent names and adds identifiers to tabs and workspaces. |
| [**okonomi/herdr-auto-tab-name**](https://github.com/okonomi/herdr-auto-tab-name) | Renames herdr tabs to the foreground command running in them. |
| [**RickyMarou/herdr-display-workspace**](https://github.com/RickyMarou/herdr-display-workspace) | Shows the active workspace label on the right side of the tab bar. |

### Status overlays, HUDs, and agent timers

*52 projects. Floating status HUDs, turn timers, and keep-awake utilities.*

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
| [**Hanyang-Li/herdr-espresso**](https://github.com/Hanyang-Li/herdr-espresso) | Uses the macOS espresso utility to keep a Mac awake while monitored Herdr agents are working or blocked, then releases the assertion when tasks finish. |
| [**calebcauthon/herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye) | Shows an overview of active agents across Herdr panes. |
| [**AltanS/herdr-cache-alert**](https://github.com/AltanS/herdr-cache-alert) | Shows prompt-cache countdowns and flags cache misses on Herdr agent panes. |
| [**0x5c0f/herdr-insight**](https://github.com/0x5c0f/herdr-insight) | Shows a dockable timeline of agent events across Herdr workspaces with active and blocked states and a seven-day history. |
| [**blavka/agents-tree**](https://github.com/blavka/agents-tree) | Shows coding-agent sessions and nested subagents as a live Herdr TUI overlay with model, context, and status. |
| [**iikjl/herdr-spotify**](https://github.com/iikjl/herdr-spotify) | A macOS Spotify overlay with album art, progress, and playback controls in Herdr. AppleScript provides basic control, while optional Web API access adds search, queueing, and track-change alerts. |
| [**jeromychu23/herdr-popupx**](https://github.com/jeromychu23/herdr-popupx) | Adds persistent floating terminal popups that can be toggled from any workspace without changing the tiled layout or losing scratchpad state. |
| [**andymartinezot/avocado-trope · herdr-plugin**](https://github.com/andymartinezot/avocado-trope/tree/main/herdr-plugin) | Shows Claude Code and Codex session graphs and a fleet view for Herdr TUI agents. |
| [**NexorPL/herdr-jarvis**](https://github.com/NexorPL/herdr-jarvis) | Shows Herdr TUI projects, agent states, threads, timelines and token costs in a mission-control tab. |
| [**H3xept/herdr-aspire-hud**](https://github.com/H3xept/herdr-aspire-hud) | Shows .NET Aspire AppHost health in the Herdr TUI sidebar and opens a popup to inspect or stop AppHosts. |
| [**maedana/herdr-agents-status**](https://github.com/maedana/herdr-agents-status) | Displays Herdr TUI agent states in an always-on-top overlay, highlighting blocked and finished agents. |
| [**Yemeni/herdr-agent-timer**](https://github.com/Yemeni/herdr-agent-timer) | Alternates each agent's status label with the elapsed time spent in that state. |
| [**ArteenHD/herdr-cache-timer**](https://github.com/ArteenHD/herdr-cache-timer) | Tracks prompt-cache windows for active agents and shows live countdowns in the Herdr sidebar, with warnings before a cache expires. |
| [**nwarwick/herdr-caffeinate**](https://github.com/nwarwick/herdr-caffeinate) | Keeps macOS awake while Herdr agents are working and releases the `caffeinate` assertion after a configurable idle grace period. |
| [**JYasha11/herdr-shame-report**](https://github.com/JYasha11/herdr-shame-report) | Keeps a permanent ledger of how long you've left your AI agents waiting. The sheep remember. |
| [**the-inconvenience-store/herdr-tilt**](https://github.com/the-inconvenience-store/herdr-tilt) | Shows and controls Tilt services in a keyboard-driven Herdr dashboard. |
| [**natori-hrj/herdr-standup**](https://github.com/natori-hrj/herdr-standup) | Summarizes each Herdr agent’s commits and uncommitted work in a digest with a persistent count. |
| [**assawalhy/herdr-stay-awake**](https://github.com/assawalhy/herdr-stay-awake) | Keeps the machine from sleeping while any herdr agent pane is working (Linux, macOS, Windows, and WSL). |
| [**jeffbking/herdr-agent-prompt**](https://github.com/jeffbking/herdr-agent-prompt) | Shows the focused coding agent's original prompt in an overlay for Claude Code, Codex, Antigravity, or Pi. |
| [**sazardev/herdr-pomodoro**](https://github.com/sazardev/herdr-pomodoro) | Runs a theme-adaptive Pomodoro timer in a Herdr TUI drawer, popup, or widget pane. |
| [**happyeric77/agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake) | Uses macOS `caffeinate` while any Herdr agent is working and releases the sleep lock when all agents become idle, blocked, or done. |
| [**shadowfax92/herdr-scratch**](https://github.com/shadowfax92/herdr-scratch) | Gives each Herdr pane a persistent scratch overlay backed by a private tmux session, keeping notes, REPLs, and side commands tied to that pane. |
| [**parker-brown-family/omarchy-crook**](https://github.com/parker-brown-family/omarchy-crook) | Puts Herdr agent state on the Omarchy desktop bar: one icon that turns urgent when an agent is blocked, and a tray listing every agent grouped by whether it needs you. Clicking a row focuses that pane and raises the terminal window on Hyprland. |
| [**oki2a24/herdr-mac-activity-monitor**](https://github.com/oki2a24/herdr-mac-activity-monitor) | Shows macOS memory use and battery level in a Herdr TUI popup and updates the window title. |
| [**johnlindquist/herdr-pane-status**](https://github.com/johnlindquist/herdr-pane-status) | Adds native per-pane agent status and PTY activity cards to a Herdr TUI fork. |
| [**heysanil/herdash**](https://github.com/heysanil/herdash) | Shows Herdr agent lifecycle states grouped by repository in a terminal dashboard with LLM-generated activity summaries. |
| [**rcosteira79/herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge) | Marks idle agents that still have background shells running. |
| [**Javamomma/herdr-matter-wall**](https://github.com/Javamomma/herdr-matter-wall) | Opens a live wall of read-only AI status cards summarizing the most active project subdirectories. |
| [**adityamaanas/glance**](https://github.com/adityamaanas/glance) | Adds a live orientation panel for an agent session that integrates with herdr as a split pane. |
| [**1Morganmore/herdr-activity-age**](https://github.com/1Morganmore/herdr-activity-age) | Displays the elapsed time since each agent's last status change in Herdr. |
| [**phin-tech/herdr-phin-board**](https://github.com/phin-tech/herdr-phin-board) | Shows workspace status in a configurable list or kanban board. |
| [**andrewromewo/herdr-lil-office**](https://github.com/andrewromewo/herdr-lil-office) | Visualizes an orchestrator and its subagents as a pixel office in Herdr, with rooms and desks representing active work. |
| [**tgdn/herdr-caffeinated**](https://github.com/tgdn/herdr-caffeinated) | Shows a Herdr TUI sidebar indicator when macOS or Linux keep-awake utilities are active. |
| [**michmos/herdr-pomodoro**](https://github.com/michmos/herdr-pomodoro) | Adds a Pomodoro timer to the Herdr TUI tab bar with break notifications, a control menu, and keybindings. |
| [**im-tabr/herdr-command-center**](https://github.com/im-tabr/herdr-command-center) | Shows Herdr TUI workspaces and agent jobs in an animated pane, with attention indicators and shortcuts to selected agents. |
| [**harshad22491/herdr-agentpanel**](https://github.com/harshad22491/herdr-agentpanel) | Shows Herdr workspace readiness, agent activity, and quota readings in a Windows dashboard. |
| [**zac-dougo/copse**](https://github.com/zac-dougo/copse) | Shows Git worktrees, local issues, live Herdr TUI agents, and Wayfinder maps on a read-only terminal board. |
| [**jrswab/herdr-status**](https://github.com/jrswab/herdr-status) | Displays live Linux machine status, including CPU, memory, load, date, and time, in a Herdr TUI pane. |
| [**zetlen/herdr-hud**](https://github.com/zetlen/herdr-hud) | A floating, customizable HUD for host, network, session, and agent metrics, with support for extra data supplied by shell scripts. |
| [**speardragon/herdr-status-platform**](https://github.com/speardragon/herdr-status-platform) | A Herdr status-platform integration. The source catalog does not explain its displayed data or controls. |
| [**cupsadarius/herdr-pr-glance**](https://github.com/cupsadarius/herdr-pr-glance) | Provides the current branch's pull request, CI checks, reviews and stack at a glance. |
| [**gbaeke/hrdr-azure-plugin**](https://github.com/gbaeke/hrdr-azure-plugin) | Browses Azure resource groups and resources; click a resource to open it in the Azure portal. |

### Context meters and rate-limit gauges

*53 projects. Live token headroom meters, quota tracking, and agent cost gauges.*

| Project | What it does |
|---|---|
| [**levi-qiao/herdr-agent-usage**](https://github.com/levi-qiao/herdr-agent-usage) | Shows model, context and subscription quota for coding agents in the Herdr TUI agent sidebar. |
| [**senna-lang/herdr-agent-usage**](https://github.com/senna-lang/herdr-agent-usage) | Shows context meters and provider rate limits for agents running in Herdr. |
| [**pinkpixel-dev/quota · herdr-plugin**](https://github.com/pinkpixel-dev/quota/tree/main/herdr-plugin) | Shows per-pane AI provider usage in the Herdr TUI sidebar for accounts such as Claude Code and Codex. |
| [**Davidcreador/herdr-token-dashboard**](https://github.com/Davidcreador/herdr-token-dashboard) | Shows live token use and costs for Pi, OpenCode, Claude Code, and Codex in Herdr TUI, with completion notifications. |
| [**quaywin/agys**](https://github.com/quaywin/agys) | Isolates Antigravity account profiles in Herdr TUI panes and shows profile, context, and quota telemetry in the sidebar. |
| [**VHemanth45/herdr_agents_tracker**](https://github.com/VHemanth45/herdr_agents_tracker) | Tracks coding-agent subscription limits and per-agent context in Herdr TUI with usage alerts and a token dashboard. |
| [**oszypczy/herdr-claude-usage**](https://github.com/oszypczy/herdr-claude-usage) | Shows the focused Claude agent’s context, five-hour usage, and seven-day usage bars in the Herdr TUI sidebar. |
| [**speardragon/herdr-status-ui-bar**](https://github.com/speardragon/herdr-status-ui-bar) | Shows Claude Code, Codex, and Grok plan usage in the Herdr tab bar, with optional additional providers. |
| [**Mako-L/account-capacity-dock · herdr-plugin**](https://github.com/Mako-L/account-capacity-dock/tree/main/herdr-plugin) | Shows Claude, Codex and Cursor account capacity in a Herdr TUI widget and desktop dock. |
| [**pdalinis/herdr-ctx-bar**](https://github.com/pdalinis/herdr-ctx-bar) | Displays color-coded context-window usage for Codex, Claude Code, Pi and Hermes Agent in the Herdr TUI sidebar. |
| [**hamidi-dev/herdr-opentab**](https://github.com/hamidi-dev/herdr-opentab) | Shows live per-agent AI spend from OpenTab in the Herdr sidebar. |
| [**alejodelosrios/herdr-claude-usage**](https://github.com/alejodelosrios/herdr-claude-usage) | Shows live Claude plan usage for both the current session and the weekly limit in the Herdr sidebar. It reads Claude Code's own authentication and status data rather than estimating usage. |
| [**yuuta1219/herdr-gekiatsu-plugin**](https://github.com/yuuta1219/herdr-gekiatsu-plugin) | Tracks Claude Code token use with a pachislot-style counter, jackpot animations, and daily resets inside Herdr. |
| [**JunSeo99/herdr-plan-meter**](https://github.com/JunSeo99/herdr-plan-meter) | Shows Claude Code and Codex plan usage in the Herdr TUI tab bar with a detail popup. |
| [**kvkenyon/herdr-quota**](https://github.com/kvkenyon/herdr-quota) | Shows subscription quota and reset times for Claude, Codex, Cursor, Kimi, Grok, and GitHub Copilot in Herdr. |
| [**CristianPeralta/herdr-api-credit-bar**](https://github.com/CristianPeralta/herdr-api-credit-bar) | Shows remaining Alibaba Cloud Model Studio API credit in a persistent Herdr TUI pane. |
| [**ArtMoreno/quota-deck**](https://github.com/ArtMoreno/quota-deck) | Displays live AI quota, model, context, and cache data in a resizable Herdr TUI pane. |
| [**iamhouser/herdr-claude-usage-multi**](https://github.com/iamhouser/herdr-claude-usage-multi) | Adds session and weekly Claude rate-limit gauges, color thresholds, and unblock countdowns to workspace rows. It supports several accounts by matching pane directories to profile folders without using tokens. |
| [**calebcav/token-usage**](https://github.com/calebcav/token-usage) | Shows session tokens, context occupancy, and account limits for Codex, Claude Code, OpenCode, and Pi in Herdr. |
| [**terry-li-hm/herdr-model-lanes**](https://github.com/terry-li-hm/herdr-model-lanes) | Shows Codex and Claude Max subscription capacity in a Herdr workspace row and supports quota-aware agent lanes. |
| [**itisbryan/herdr-usage**](https://github.com/itisbryan/herdr-usage) | Shows Claude Code, Codex, and OpenCode quota windows and local usage trends in a Herdr popup. |
| [**ArnaudRinquin/herdr-quotabar**](https://github.com/ArnaudRinquin/herdr-quotabar) | Displays Claude plan quota windows in the Herdr tab bar or sidebar, with a pluggable provider interface. |
| [**jordanhawkes/herdr-metrics**](https://github.com/jordanhawkes/herdr-metrics) | Shows context occupancy, session tokens, and available account limits for Claude Code, Codex, and TraeX in the Herdr sidebar. |
| [**benkraus/herdr-plugin-codex-subs**](https://github.com/benkraus/herdr-plugin-codex-subs) | Shows Codex subscription quotas, reset times, and credit balances from local CLIProxyAPI credentials in a Herdr popup. |
| [**astkaasa/herdr-tokscale-dashboard**](https://github.com/astkaasa/herdr-tokscale-dashboard) | Opens the existing Tokscale token and cost dashboard in a Herdr split and exposes a JSON quick action without reimplementing Tokscale. |
| [**mgh3326/scopefuel**](https://github.com/mgh3326/scopefuel) | Breaks provider quota and remaining capacity down by account, model, and group, including reset times for five-hour and weekly windows. |
| [**szrenwei/herdr-agent-metrics**](https://github.com/szrenwei/herdr-agent-metrics) | Tracks context-window and token metrics for Claude Code, Codex, and TraeX sessions and summarizes them in a small Herdr overlay. |
| [**EMRahman/herdr-context-monitor**](https://github.com/EMRahman/herdr-context-monitor) | Adds one sidebar row per Claude Code, Codex, or Antigravity CLI agent with its context-window use, from a single dependency-free Python file. Sidebar configuration can turn readings above 50% red. |
| [**cenvu/cen-harness-hud**](https://github.com/cenvu/cen-harness-hud) | Shows coding-agent account, plan, quota, and reset information in a terminal HUD with Herdr status integration. |
| [**taku-hatano/herdr-usage**](https://github.com/taku-hatano/herdr-usage) | Displays Claude Code and Codex rate limits, token usage, and active sessions in the Herdr tab bar or dashboard. |
| [**KeithMoc/herdr-tokenlens**](https://github.com/KeithMoc/herdr-tokenlens) | Shows a live carrying-cost and compaction-breakeven meter for coding agents in a Herdr pane. |
| [**kwanwooi25/herdr-plugin-agent-quota**](https://github.com/kwanwooi25/herdr-plugin-agent-quota) | Displays local token and cost usage for Claude Code, Codex, and Grok in a Herdr dashboard. |
| [**shrivatsas/herdr-model-capacity**](https://github.com/shrivatsas/herdr-model-capacity) | Shows configured Claude, OpenAI, and OpenRouter account quota and credit headroom in a persistent Herdr pane. |
| [**tmastalirsch/herdr-claude-context-meter**](https://github.com/tmastalirsch/herdr-claude-context-meter) | Shows Claude Code context usage per session in the status line and across sessions in a Herdr pane. |
| [**TheBrunoPetkovic/herdr-context-display**](https://github.com/TheBrunoPetkovic/herdr-context-display) | Displays color-coded Claude Code context-window usage on each agent row in the Herdr sidebar. |
| [**Efeguclu1/herdr-usage**](https://github.com/Efeguclu1/herdr-usage) | Shows account-usage marks for Claude Code, Codex, Cursor, and OpenCode in Herdr agent tabs, with session burn for Pi. |
| [**xyanwert/herdr-burnout**](https://github.com/xyanwert/herdr-burnout) | Monitors live Claude token usage and rate limits with animated visual cues in Herdr. |
| [**gecm0/herdr-plugin-agents-usage**](https://github.com/gecm0/herdr-plugin-agents-usage) | Shows provider usage (Claude, Codex, OpenCode Go, Neuralwatt) in a Herdr modal popup. |
| [**w784415/pi-agent-usage**](https://github.com/w784415/pi-agent-usage) | Shows OpenAI Codex quota usage and reset times in Pi, with a Herdr TUI plugin for opening the extension. |
| [**sdillen/pi-usage**](https://github.com/sdillen/pi-usage) | Summarizes Pi token usage and cost from session logs and optionally mirrors live totals into the Herdr TUI sidebar. |
| [**jerryfane/herdr-codex-usage-kit**](https://github.com/jerryfane/herdr-codex-usage-kit) | Shows remaining Codex five-hour and weekly quota in the Herdr sidebar and provides a live shell dashboard. It reads local Codex JSONL logs, refreshes every 30 seconds, and does not call an external API. |
| [**yuuta1219/claude-usage**](https://github.com/yuuta1219/claude-usage) | Reads local Claude Code telemetry and shows session and weekly token-use percentages at the bottom of the Herdr sidebar. |
| [**DongHyunnn/ai-share-usage-herdr**](https://github.com/DongHyunnn/ai-share-usage-herdr) | Shows shared Codex account quota and an individual share in the Herdr TUI sidebar. |
| [**ryus1234/provider-usage**](https://github.com/ryus1234/provider-usage) | Displays local Claude, ChatGPT and Codex, OpenCode Go, and optional Fable usage snapshots in a Herdr TUI pane. |
| [**alkevintan/deepseek-counter-herdr**](https://github.com/alkevintan/deepseek-counter-herdr) | Displays DeepSeek API credit, spending, and usage pace in the Herdr TUI status line. |
| [**kikyous/herdr-claude-usage**](https://github.com/kikyous/herdr-claude-usage) | Shows Claude usage in a Herdr TUI pane and summarizes it in the workspace name. |
| [**chrysa/herdr-rtk-savings**](https://github.com/chrysa/herdr-rtk-savings) | Shows RTK token-savings gauges per project in the Herdr TUI workspace sidebar, with a detailed popup. |
| [**silverwolfdoc/herdr-usage-bar**](https://github.com/silverwolfdoc/herdr-usage-bar) | A compact bar showing live token use, rate-limit ceilings, and context-window fill for agents without occupying a full pane. |
| [**tomys22/herdr-agent-usage-plugin**](https://github.com/tomys22/herdr-agent-usage-plugin) | Displays Claude, Codex, and Gemini API usage, including session and weekly percentages and reset times, in a Herdr split. |
| [**ram4-dev/herdr-codex-usage**](https://github.com/ram4-dev/herdr-codex-usage) | Detects installed agents and shows their usage quotas inside Herdr. |
| [**aorumbayev/herdr-ctx**](https://github.com/aorumbayev/herdr-ctx) | Shows Claude’s remaining context-window capacity in the Herdr sidebar. |
| [**Coolsik/herdr-codex-cost**](https://github.com/Coolsik/herdr-codex-cost) | Shows estimated API-equivalent costs for Codex sessions and descendant agents in the Herdr TUI sidebar. |
| [**samuelbaldwin05/herdr-burn**](https://github.com/samuelbaldwin05/herdr-burn) | Shows Claude Code cost and quota for each pane, plus a total spending overlay for the workspace. |

### Output inspection, logs, and transcripts

*42 projects. Tools for searching, cleaning, exporting, or reviewing pane output and agent conversations.*

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
| [**speardragon/herdr-agents-history**](https://github.com/speardragon/herdr-agents-history) | Combines live tool calls and command output from Claude Code and Codex agents. It reads Herdr's event stream and provides one searchable, filterable activity feed. |
| [**TawfiqAbubaker/scoopr**](https://github.com/TawfiqAbubaker/scoopr) | Copies anything to the terminal without using the mouse, inspired by extrakto for tmux. |
| [**qq88976321/herdr-copy-search**](https://github.com/qq88976321/herdr-copy-search) | Adds incremental regular-expression search to pane history and copies matched URLs, Git hashes, or file paths through OSC 52, combining tmux-copycat and extrakto-style behavior. |
| [**dzwduan/herdr-convo-index**](https://github.com/dzwduan/herdr-convo-index) | Builds a navigable index of user and assistant turns for Claude Code sessions in Herdr, making long conversations easier to review without scrolling through raw terminal history. |
| [**eStudio37/herdr-snip**](https://github.com/eStudio37/herdr-snip) | Selects text from a Herdr TUI pane and sends it with context to another agent. |
| [**jagzmz/herdr-s3-clipboard**](https://github.com/jagzmz/herdr-s3-clipboard) | Uploads a clipboard screenshot to S3-compatible storage and pastes a public or signed URL into the active Herdr pane for use with vision-capable agents. |
| [**napalmpapalam/herdr-quotr**](https://github.com/napalmpapalam/herdr-quotr) | Captures recent agent output in a popup and lets the user select a passage to quote back into the conversation. |
| [**GranamyrBR/herdr-english-coach**](https://github.com/GranamyrBR/herdr-english-coach) | A side-pane English and developer-jargon coach that records grammar corrections and phrasing suggestions while agents work. |
| [**kaar/herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url) | Finds URLs in Herdr TUI pane scrollback with fzf and opens the selected URL. |
| [**ofirgall/extrakto-herdr**](https://github.com/ofirgall/extrakto-herdr) | Extracts paths, URLs, words, and other text from a Herdr TUI pane for fuzzy selection with fzf. |
| [**hunter9x/herdr-logging**](https://github.com/hunter9x/herdr-logging) | Captures, saves, and clears Herdr TUI pane output using pane logging and screen-capture actions. |
| [**rotemb-wond/herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints) | Places short keyboard labels over visible paths, commit hashes, and URLs. Typing a label copies the matching text to the system clipboard. |
| [**alexjsp/herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture) | Saves the focused pane's scrollback as a colored, self-contained HTML file or plain text, with configurable path, filename, and theme. |
| [**x0d7x/herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url) | Reads visible content from every Herdr pane, extracts and deduplicates URLs, and sends them to fzf. Enter opens the selected URL, while `y` copies it. |
| [**waynewu411/herdr-event-log**](https://github.com/waynewu411/herdr-event-log) | Logs Herdr pane agent-status changes to a durable, cursor-resumable event log. |
| [**OmarDadabhoy/herdr-agent-links**](https://github.com/OmarDadabhoy/herdr-agent-links) | Finds hidden Markdown links in Codex and Claude transcripts and opens them from a Herdr popup. |
| [**testy-cool/herdr-copy-conversation**](https://github.com/testy-cool/herdr-copy-conversation) | Copies full terminal scrollback or agent conversations directly to the clipboard in Herdr. |
| [**connerohnesorge/herdr-vaultr**](https://github.com/connerohnesorge/herdr-vaultr) | Searches, copies, displays, and forks captured Claude Code, Codex, and Pi sessions from their Herdr panes using vaultr. |
| [**AlexSamarsky/herdr-simple-prompts**](https://github.com/AlexSamarsky/herdr-simple-prompts) | Shows prompts and final Claude Code or Codex answers in a Herdr pane with a composer, hiding intermediate tool traffic. |
| [**j1nn0/herdr-harvest**](https://github.com/j1nn0/herdr-harvest) | Captures completion outputs from Herdr agent fleets into a persistent result inbox. |
| [**zydou/herdr-screenshot**](https://github.com/zydou/herdr-screenshot) | Renders ANSI text from Herdr panes into PNG screenshots for Telegram sharing. |
| [**codingfragments/herdr-flash**](https://github.com/codingfragments/herdr-flash) | Opens a floating view of Herdr TUI pane scrollback for keyboard-driven text selection, search, and copying. |
| [**RooseveltAdvisors/herdr-extractor**](https://github.com/RooseveltAdvisors/herdr-extractor) | Extracts tokens from the focused pane’s scrollback and filters them for copying with typeahead. |
| [**willian/herdr-fzf-url**](https://github.com/willian/herdr-fzf-url) | Picks URLs from the focused Herdr TUI pane with fzf and opens or copies them. |
| [**jlangston/herdr-clipboard**](https://github.com/jlangston/herdr-clipboard) | Adds tmux-style clipboard history to Herdr, including image entries. |
| [**a-kaibu/copy-last**](https://github.com/a-kaibu/copy-last) | Copies the last command and its output from the focused Herdr TUI pane to the clipboard. |
| [**sd2k/herdr-thumbs**](https://github.com/sd2k/herdr-thumbs) | Picks and copies on-screen text or URLs in Herdr using tmux-thumbs style hints. |
| [**a-curious-coder/herdr-iris**](https://github.com/a-curious-coder/herdr-iris) | Detects the active agent and searches matching skills and rules from Claude `SKILL.md` and Cursor configuration. Selecting an item inserts the formatted command for confirmation. |
| [**Brutheron/Renderd**](https://github.com/Brutheron/Renderd) | Displays completed Claude Code and Codex responses in a clean, scrollable side panel that updates live. It reads structured session files, removes thinking blocks, and renders the answer as Markdown. |
| [**fredrikkvalvik/herdr-scratch**](https://github.com/fredrikkvalvik/herdr-scratch) | A temporary floating shell for quick commands over a Herdr session. |
| [**alanpcurrie/herdr-claude**](https://github.com/alanpcurrie/herdr-claude) | A repository containing Herdr and Claude demonstration output rather than a described tool. |
| [**johnlindquist/herdr-pane-update-timestamps**](https://github.com/johnlindquist/herdr-pane-update-timestamps) | Adds timestamped, scrollable observations of Herdr pane output. |

### Agent visualizations and terminal games

*7 projects. Interactive terminal visualizations and games for following agents.*

| Project | What it does |
|---|---|
| [**michaellandi/herdr-office**](https://github.com/michaellandi/herdr-office) | Draws Herdr TUI agents as office characters and signals when an agent needs approval. |
| [**devangchhajed/herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office) | Shows Herdr TUI agents as pixel-art office characters that change activity with agent status and tool calls. |
| [**takemo101/wave-tui**](https://github.com/takemo101/wave-tui) | Plays internet radio in a terminal and visualizes Herdr TUI agents in an interactive Agent Planets view. |
| [**Efeguclu1/herdr-town**](https://github.com/Efeguclu1/herdr-town) | Renders Herdr coding agents as an interactive 8-bit town inside a pane and lets users read or answer them. |
| [**opsydyn/herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer) | Shows live Herdr TUI agents and their states as a 16-bit fantasy guild. |
| [**chantlong/herdr-habitat**](https://github.com/chantlong/herdr-habitat) | Displays a terminal habitat where plants and wildlife evolve alongside Herdr TUI agent activity. |
| [**marius-se/herdr-brainrot**](https://github.com/marius-se/herdr-brainrot) | Runs terminal games and distraction apps such as DOOM in a dedicated Herdr pane while agents continue working in neighboring panes. Additional apps can be configured through the plugin manifest. |

### Herdr TUI themes and appearance

*8 projects. Themes and visual customizations for the Herdr TUI.*

| Project | What it does |
|---|---|
| [**promptegrity/grok-themes · herdr**](https://github.com/promptegrity/grok-themes/tree/HEAD/herdr) | Applies GrokNight or GrokDay colors to the Herdr TUI and adds an optional powerline-style branch indicator. |
| [**ariel-ps/herdr-colors**](https://github.com/ariel-ps/herdr-colors) | Assigns distinct color slots to Herdr TUI panes and can repaint existing panes. |
| [**magimetal/matrix-themes · herdr**](https://github.com/magimetal/matrix-themes/tree/HEAD/herdr) | Applies a Matrix-inspired green palette to the Herdr TUI using a configuration snippet. |
| [**AkashJana18/zenbones-herdr**](https://github.com/AkashJana18/zenbones-herdr) | Adds 23 zenbones color themes with light and dark variants to Herdr TUI. |
| [**nertzy/herdr-flexoki**](https://github.com/nertzy/herdr-flexoki) | Adds Flexoki light and dark themes to Herdr TUI, including an automatic appearance option. |
| [**sp-night/herdr**](https://github.com/sp-night/herdr) | Adds three São Paulo-inspired dark color palettes to Herdr TUI. |
| [**codingquark/herdr-modus-themes**](https://github.com/codingquark/herdr-modus-themes) | Installs the light Modus Operandi and dark Modus Vivendi palettes for the Herdr TUI. |
| [**Young1108/herdr-cyber-style**](https://github.com/Young1108/herdr-cyber-style) | Applies a dark cyber theme and workspace layout to Herdr TUI on macOS, with a backup of the previous configuration. |

### Security guards and collision detectors

*10 projects. Safety monitors that warn of worktree collisions, credential leaks, or destructive edits.*

| Project | What it does |
|---|---|
| [**termaxa/termaxa · herdr-plugin**](https://github.com/termaxa/termaxa/tree/main/herdr-plugin) | Runs Claude Code or Codex under Termaxa command policies in Herdr TUI and shows refusals and audit records. |
| [**schemaitat/herdr-nono-plugin**](https://github.com/schemaitat/herdr-nono-plugin) | Runs OpenCode in nono sandboxes from Herdr TUI on Linux, with separate client and server profiles. |
| [**mcc0x/herdr-redact**](https://github.com/mcc0x/herdr-redact) | Warns when an agent pane has printed credentials before screenshots, streaming, or chat paste operations occur. |
| [**StructuPath/herdr-guard**](https://github.com/StructuPath/herdr-guard) | Monitors Herdr TUI panes for configured command-policy violations and can interrupt matching commands. An optional Claude Code hook checks tool calls before execution. |
| [**mcc0x/herdr-collide**](https://github.com/mcc0x/herdr-collide) | Warns when agents working in separate Git worktrees of the same repository are about to collide or conflict. |
| [**asumaran/asconfirmclose**](https://github.com/asumaran/asconfirmclose) | Closes an idle Herdr TUI pane immediately but asks for confirmation when a foreground process is running. |
| [**pauljohnchamberlain/herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard) | Lets coding agents inspect Herdr TUI sessions and make guarded workspace renames or close eligible inactive work. |
| [**cheunglok97/close-guard**](https://github.com/cheunglok97/close-guard) | Asks for confirmation before closing a Herdr TUI tab or pane. |
| [**BlockedPath/herdr-plugin**](https://github.com/BlockedPath/herdr-plugin) | Inspects Herdr TUI plugin execution paths before installation and reports execution evidence and unknowns. |
| [**sangimed/firstmate-homelab**](https://github.com/sangimed/firstmate-homelab) | Provides a self-hosted Docker stack for Firstmate, Herdr and Codex agents. |

### Plugin collections, frameworks, and ready-made configs

*33 projects. Plugin bundles, shared libraries for plugin authors, and ready-made Herdr configurations to install and adapt.*

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
| [**klinter007/herdr-macos-plugins**](https://github.com/klinter007/herdr-macos-plugins) | Collects macOS Herdr TUI plugins for opening files, keeping the computer awake, monitoring resources and managing Jev sessions. |
| [**thejiajun/jc-herdr-plugins**](https://github.com/thejiajun/jc-herdr-plugins) | Collects Herdr plugins that name workspaces from agent conversations and search or switch between agents. |
| [**shelken/herdr-plugins**](https://github.com/shelken/herdr-plugins) | Collects Herdr TUI plugins for launching Pi agents and resuming Pi sessions. |
| [**narumiruna/herdr-plugins**](https://github.com/narumiruna/herdr-plugins) | Collects independently installable Herdr TUI plugins, including a GitHub pull-request viewer. |
| [**oullin/herdr-plugins**](https://github.com/oullin/herdr-plugins) | Collects independently installable Herdr TUI plugins for navigation, agent awareness, and terminal workflows. |
| [**alastairsounds/herdr-plugins**](https://github.com/alastairsounds/herdr-plugins) | Collects Herdr TUI plugins in independently installable subdirectories. |
| [**mcc0x/herdr-crook**](https://github.com/mcc0x/herdr-crook) | Shares a library of common functionality for Herdr TUI plugins. |
| [**marcjfj-vmlyr/quickTUI**](https://github.com/marcjfj-vmlyr/quickTUI) | Adds a Herdr TUI plugin and agent skill for building interactive terminal interfaces from OpenTUI components. |
| [**pdjsh/herdr-plugins**](https://github.com/pdjsh/herdr-plugins) | Displays agents in a radial map and reorders workspaces with two Rust plugins. |
| [**j1nn0/herdr-plugin-sdk**](https://github.com/j1nn0/herdr-plugin-sdk) | Builds Herdr TUI plugins in TypeScript with a typed CLI client, event parsing and in-memory test fixtures. |
| [**stevederico/herdr-plugins**](https://github.com/stevederico/herdr-plugins) | Adds a dockable file explorer, sidebar, Git badges, and other Herdr TUI workspace helpers. |
| [**jvsteiner/herdr-plugins**](https://github.com/jvsteiner/herdr-plugins) | Collects Herdr TUI plugins for running project development servers and picking Git branches. |
| [**tomaszhanc/herdr-plugins**](https://github.com/tomaszhanc/herdr-plugins) | Collects independently packaged Herdr TUI plugins in one repository. |
| [**paulrobello/par-herdr-plugins**](https://github.com/paulrobello/par-herdr-plugins) | Collects independently installable Herdr TUI plugins in a monorepo. |
| [**a-curious-coder/herdr-plugin-manager**](https://github.com/a-curious-coder/herdr-plugin-manager) | Finds, installs, updates, enables, and disables Herdr TUI plugins from an fzf interface. |
| [**petitviolet/herdr-plugins**](https://github.com/petitviolet/herdr-plugins) | Collects independently installable Herdr TUI plugins in separate directories. |
| [**SeanRoberts/herdr-plugins**](https://github.com/SeanRoberts/herdr-plugins) | Collects Herdr TUI plugins for fuzzy tab navigation and Claude Code usage displays. |
| [**lliwi/herdr-plugins**](https://github.com/lliwi/herdr-plugins) | Collects Herdr TUI plugins for OpenClaw and Hermes sessions, persistent notes, and automatic Python virtual environment activation. |
| [**boooowy/herdr_plugins**](https://github.com/boooowy/herdr_plugins) | Collects Herdr TUI plugins for copying terminal hints, monitoring agent quotas, and viewing Bitbucket pull requests. |
| [**shubham-cpp/herdr-plugins**](https://github.com/shubham-cpp/herdr-plugins) | Adds Herdr TUI plugins for automatic tab and agent naming and directional pane focus. |
| [**VinhLe1410/herdr-agent-priority**](https://github.com/VinhLe1410/herdr-agent-priority) | Configures how Herdr agent states are prioritized. |
| [**masatokawano/to-herdr**](https://github.com/masatokawano/to-herdr) | Configuration and notes for migrating a terminal setup from Zellij to Herdr. |
| [**mike-bronner/herdr-plugin-kit**](https://github.com/mike-bronner/herdr-plugin-kit) | Helps developers build Herdr TUI plugins with generated API types, a Rust socket client, and shared runtime helpers. |

---

## 7. Apps, companion integrations, and installation

*415 projects. Native applications, web dashboards, hardware companions, supporting utilities, and setup packages.*

### Native desktop and mobile apps

*109 projects. Installed applications and launchers that provide a native interface to Herdr on desktop or mobile operating systems.*

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
| [**JoseValencia125/agents-pixel-dungeon**](https://github.com/JoseValencia125/agents-pixel-dungeon) | Displays Herdr agents as interactive pixel-art dungeon characters on desktop and lets users answer prompts. |
| [**Ozymandes/TENDRIL**](https://github.com/Ozymandes/TENDRIL) | Controls persistent Herdr sessions from an Android device with Tailscale, Mosh, and agent notifications. |
| [**tuan3w/herdr-mobile**](https://github.com/tuan3w/herdr-mobile) | Monitors and answers Herdr agents across machines from an Android client connected over SSH. |
| [**DanielOu1208/agentslate**](https://github.com/DanielOu1208/agentslate) | Supervises Herdr coding agents from an iPhone keypad over Tailscale. |
| [**weekitmo/herdr-pocket**](https://github.com/weekitmo/herdr-pocket) | Monitors Herdr agents and opens their terminals from a Flutter client over SSH on mobile and desktop. |
| [**undivisible/herdr-gui**](https://github.com/undivisible/herdr-gui) | Renders Herdr TUI sessions and an embedded terminal in a native macOS GPUI client. |
| [**buldezir/Herdglass**](https://github.com/buldezir/Herdglass) | Connects to remote Herdr servers from a native macOS interface with a GPU-accelerated terminal and session status drawer. |
| [**paulmillr/dispatch**](https://github.com/paulmillr/dispatch) | Maps Herdr sessions to native macOS tabs and spaces and offers a chat view for agents. |
| [**Tomyail/herdr-connect**](https://github.com/Tomyail/herdr-connect) | Monitors and controls Herdr agents from an iPhone over the local network. |
| [**AkinoKaede/Termind**](https://github.com/AkinoKaede/Termind) | Reconnects to Herdr sessions from a remote workspace app for Mac, iPhone, and iPad. |
| [**multiplex-term/Multiplex**](https://github.com/multiplex-term/Multiplex) | Connects to Herdr and tmux sessions over SSH from Apple Vision Pro, iPad, or iPhone. |
| [**ventz/moo-mac-terminal**](https://github.com/ventz/moo-mac-terminal) | Tracks Herdr agents in a native macOS terminal and shows notifications when they need attention. |
| [**rarce/wooloo**](https://github.com/rarce/wooloo) | Connects a native macOS client to Herdr sessions with terminals, file browsing, editing, and Git tools. |
| [**herdr-go/herdr-go**](https://github.com/herdr-go/herdr-go) | Controls Herdr coding agents from a native mobile client using a peer-to-peer connection. |
| [**osuki-dev/muqun-app**](https://github.com/osuki-dev/muqun-app) | Connects iPhone, iPad, and Android users to Herdr TUI terminals through Muqun Gateway. |
| [**v1k45/bigtty**](https://github.com/v1k45/bigtty) | Connects a native macOS client to Herdr sessions with Ghostty-rendered terminals, spaces, browser panes, and file panes. |
| [**VoidLight00/termweave**](https://github.com/VoidLight00/termweave) | Connects browser and macOS interfaces to Herdr sessions with docked panes, workspace navigation, and agent status. |
| [**getshepherd/shepherd**](https://github.com/getshepherd/shepherd) | Runs a native macOS and Linux interface for Herdr TUI workspaces and agent status, with experimental herdr-core support. |
| [**marcelormendes/drover**](https://github.com/marcelormendes/drover) | Opens a native desktop interface for Herdr TUI workspaces, terminals, and agents. |
| [**theam/shepherdr**](https://github.com/theam/shepherdr) | Shows a prioritized queue of coding agents across Herdr machines in a native macOS client. |
| [**gigq/OmarchyRemote**](https://github.com/gigq/OmarchyRemote) | Accesses Herdr agents and an Omarchy desktop from mobile devices, desktop apps, or a browser over a private network. |
| [**patricio0312rev/anyssh**](https://github.com/patricio0312rev/anyssh) | Connects an iPhone or iPad to Herdr TUI sessions over SSH, with terminal, file and Git views. |
| [**skeletor-js/bessie**](https://github.com/skeletor-js/bessie) | Controls Herdr TUI workspaces and agents from a native macOS client. |
| [**glattziehen/hirte**](https://github.com/glattziehen/hirte) | Connects an iPhone or iPad to herdr-core over SSH to inspect agent status, answer prompts and use terminals. |
| [**quicktui/quicktui-herdr**](https://github.com/quicktui/quicktui-herdr) | Pairs QuickTUI on iPhone, iPad or Android with Herdr TUI to view sessions, answer agents and control terminals. |
| [**NakiriYuuzu/Yuzora**](https://github.com/NakiriYuuzu/Yuzora) | Runs persistent Herdr TUI sessions alongside an editor, Git tools and remote connections in a macOS or Windows desktop workspace. |
| [**YogevKr/rai**](https://github.com/YogevKr/rai) | Opens Herdr TUI sessions in a native macOS client with terminal panes, agent notifications, and an iPhone companion. |
| [**abhishek944/pet-town**](https://github.com/abhishek944/pet-town) | Shows live Herdr agents as animated characters in a desktop village. |
| [**cryks/shepherd**](https://github.com/cryks/shepherd) | Monitors local and remote Herdr agents from the macOS menu bar. |
| [**MrMySQL/uherdr**](https://github.com/MrMySQL/uherdr) | Runs a native macOS interface for Herdr workspaces, terminal panes, and agents. |
| [**InsaneArts/herdrbar**](https://github.com/InsaneArts/herdrbar) | Shows Herdr TUI agents in the macOS menu bar, sends notifications and jumps to their terminal panes. |
| [**cunderw/driverr**](https://github.com/cunderw/driverr) | Connects iPhone and iPad to Herdr TUI or herdr-core over SSH to view agents, answer prompts and use terminals. |
| [**anomius/nerv-magi**](https://github.com/anomius/nerv-magi) | Displays Herdr TUI agent and system telemetry in a fullscreen dashboard, terminal board or Omarchy widget. |
| [**LoneExile/merino**](https://github.com/LoneExile/merino) | Shows Herdr TUI agent status and pane output in a macOS menu bar and a paired phone dashboard. |
| [**lucasscariot/herdie**](https://github.com/lucasscariot/herdie) | Connects an iPhone or iPad to Herdr hosts over SSH to inspect agents, read terminal output, and send commands. |
| [**jgwesterlund/agent-view**](https://github.com/jgwesterlund/agent-view) | Shows Herdr agent status as animated pixel-art characters in a macOS app and focuses selected panes. |
| [**bsorescu/herdr-mobile**](https://github.com/bsorescu/herdr-mobile) | Shows a phone-friendly Herdr TUI over SSH for inspecting agent output and answering prompts. |
| [**speardragon/herdr-island**](https://github.com/speardragon/herdr-island) | Shows agent activity and lets users answer prompts from a macOS notch or menu-bar panel. |
| [**finik/shepherd**](https://github.com/finik/shepherd) | Connects an Android phone to Herdr TUI or herdr-core over SSH to read agent conversations and answer prompts. |
| [**keinstn/drover**](https://github.com/keinstn/drover) | Supervises Herdr TUI and herdr-core agents over SSH from an iOS or macOS app, including chat and permission prompts. |
| [**itsmaleen/merry**](https://github.com/itsmaleen/merry) | Controls Herdr TUI or cmux workspaces from an iPhone, including notifications, file and photo input, and voice commands. |
| [**JinJieBeWater/herdling**](https://github.com/JinJieBeWater/herdling) | Monitors Herdr TUI and herdr-core agents from the macOS menu bar and opens their sessions. |
| [**inferenceaftermath/remotly**](https://github.com/inferenceaftermath/remotly) | Controls Herdr TUI sessions from an iPhone or Android phone, with live panes and agent permission prompts. |
| [**pierre-charles/herdr-menu**](https://github.com/pierre-charles/herdr-menu) | Adds a macOS menu bar for viewing Herdr TUI agents and running pane, tab, and workspace actions. |
| [**zhiyao/herdcats**](https://github.com/zhiyao/herdcats) | Connects an iPhone or iPad to Herdr TUI or herdr-core over SSH to browse agents and send terminal input. |
| [**lewtec/rterm**](https://github.com/lewtec/rterm) | Attaches to local or SSH-hosted Herdr, tmux, and screen sessions from saved tabs in a desktop app. |
| [**teasec4/herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app) | Streams live agent terminal output to mobile devices, displays status updates, and dispatches prompts over LAN or Tailscale. |
| [**re2zero/zenix**](https://github.com/re2zero/zenix) | Manages Herdr TUI workspaces, tabs, and panes in a native GPUI desktop client. |
| [**mohamed-essam/herdr-mobile**](https://github.com/mohamed-essam/herdr-mobile) | Monitors Herdr agents and answers blocked prompts from an Android app backed by a Go daemon. |
| [**speardragon/herdr-bot**](https://github.com/speardragon/herdr-bot) | Turns Herdr TUI agents into chat participants that can message each other in a macOS app. |
| [**IGUNUBLUE/lerdr-rust-kotlin**](https://github.com/IGUNUBLUE/lerdr-rust-kotlin) | Connects an Android app to Herdr TUI sessions through a Rust relay over Tailscale. |
| [**Gudals0320/atrium**](https://github.com/Gudals0320/atrium) | Shows Herdr TUI agent terminals and their states on a Windows desktop canvas. |
| [**erikedling/herdquarters**](https://github.com/erikedling/herdquarters) | Runs a desktop team of Claude Code, Pi or Codex agents in Herdr TUI worktrees with a task board. |
| [**bigbug16/herdr-topbar**](https://github.com/bigbug16/herdr-topbar) | Shows Herdr TUI agent attention in the macOS menu bar and opens sessions or projects. |
| [**hmu332233/herdr-menu-bar**](https://github.com/hmu332233/herdr-menu-bar) | Shows Herdr agent status by workspace in a macOS menu bar and focuses selected panes. |
| [**fcoury/hoshi**](https://github.com/fcoury/hoshi) | Connects iPhone and iPad users to Herdr sessions over SSH or Mosh and shows agent status. |
| [**sxp4931/herdr-manager**](https://github.com/sxp4931/herdr-manager) | Shows Herdr agent status and approval prompts in a macOS menu-bar app with optional session control and usage estimates. |
| [**leescot/herdr-remote-ios**](https://github.com/leescot/herdr-remote-ios) | Enables remote control of Mac-hosted Herdr coding agents from iOS devices over SSH. |
| [**joshuaswarren/allward**](https://github.com/joshuaswarren/allward) | Runs a native macOS terminal for coding agents across machines. |
| [**OcHub-team/OcHerdr**](https://github.com/OcHub-team/OcHerdr) | Connects to Herdr from a native macOS, Linux, or Windows interface. |
| [**benngarcia/herdr-macos**](https://github.com/benngarcia/herdr-macos) | Runs a locally built native Herdr terminal for macOS using Ghostty. |
| [**seascheng/herdr-gui**](https://github.com/seascheng/herdr-gui) | Opens a native macOS front end for Herdr TUI sessions, panes, and agents. |
| [**likangmax/KodeWork**](https://github.com/likangmax/KodeWork) | Connects a Windows workbench to remote Linux hosts over SSH and reattaches to Herdr TUI sessions. |
| [**deex2/herdroid**](https://github.com/deex2/herdroid) | Connects an Android device to Herdr sessions over SSH and displays live workspace state. |
| [**bonanyan/herdrbell**](https://github.com/bonanyan/herdrbell) | Shows Herdr agent states in the macOS menu bar and opens the selected agent pane in a terminal. |
| [**joshuaswarren/omarchy-fleet-shepherd**](https://github.com/joshuaswarren/omarchy-fleet-shepherd) | Shows read-only Herdr agent status and OMP usage across local and SSH-connected machines in an Omarchy panel. |
| [**lightheaded/kari**](https://github.com/lightheaded/kari) | Shows Claude Code sessions on a macOS or Windows tray kanban board and can launch them in Herdr panes. |
| [**alejodelosrios/kelpie**](https://github.com/alejodelosrios/kelpie) | Connects an Omarchy desktop console to Herdr TUI with an agent sidebar and terminal. |
| [**dbrain/kampr**](https://github.com/dbrain/kampr) | Controls Herdr sessions remotely through a browser or Android app with streamed terminal frames and agent transcripts. |
| [**simfor99/herdr-night-watch**](https://github.com/simfor99/herdr-night-watch) | Monitors Herdr agents from a Windows tray app and can sleep or shut down the machine after work finishes. |
| [**jirathip-dev/corral**](https://github.com/jirathip-dev/corral) | Monitors Herdr TUI agents on an iPhone with a read-only fleet board and optional state-change notifications. |
| [**openalon-org/herdr-bar**](https://github.com/openalon-org/herdr-bar) | Shows Herdr TUI agent status in a menu bar and jumps to agents that need attention. |
| [**Tresnanda/mustr**](https://github.com/Tresnanda/mustr) | Opens local and remote Herdr TUI sessions in a native macOS client with pane grids and agent status. |
| [**KUKARAF/collie_voice_commands**](https://github.com/KUKARAF/collie_voice_commands) | Sends voice commands from Android to Collie or Herdr sessions and produces spoken summaries. |
| [**arvmaan/herdr-glance**](https://github.com/arvmaan/herdr-glance) | Shows live Herdr TUI agent status in an always-on-top macOS widget and focuses selected agents locally or over SSH. |
| [**SirBrother/herdr-launcher**](https://github.com/SirBrother/herdr-launcher) | Adds a Windows Explorer action that opens a folder in Herdr TUI by focusing or creating a matching workspace. |
| [**pavel-snyk/herdry**](https://github.com/pavel-snyk/herdry) | Shows blocked agents in a macOS menu bar and opens their Herdr TUI sessions. |
| [**Codem0nky87/multi-session-ai-manager**](https://github.com/Codem0nky87/multi-session-ai-manager) | Runs the Herdr TUI on an iPad over SSH, with host tabs, file transfers, and port forwarding. |
| [**lixenstrand/omarchy-herdr-drop**](https://github.com/lixenstrand/omarchy-herdr-drop) | Opens a persistent Herdr client in a drop-down Hyprland window. |
| [**re2zero/mudi**](https://github.com/re2zero/mudi) | Adds a desktop companion for Herdr with agent notifications and navigation. |
| [**muhammedenesb100/herdrm**](https://github.com/muhammedenesb100/herdrm) | Manages coding agents on local and remote machines from a native macOS console. |
| [**kyokosawada/viu**](https://github.com/kyokosawada/viu) | Lets developers monitor Herdr agent fleets and respond to workers by voice or keyboard from a mobile phone. |
| [**AsgardMuninn/asgardmuninn.ainoch**](https://github.com/AsgardMuninn/asgardmuninn.ainoch) | Shows blocked Herdr agent questions in a macOS notch panel and sends selected answers back to the pane. |
| [**SandroHub013/herdr-mobile**](https://github.com/SandroHub013/herdr-mobile) | Controls a Windows Herdr session from Android, iPhone, or a browser through a token-protected local bridge. |
| [**jellyfishmobile/herdup**](https://github.com/jellyfishmobile/herdup) | Launches template-based Herdr TUI agent teams in desktop workspaces with role-specific panes. |
| [**LamplitIsles/kepos-herdr-mobile**](https://github.com/LamplitIsles/kepos-herdr-mobile) | Opens one Herdr terminal on a Mac over SSH from an Android client with explicit host-key trust. |
| [**nourhelmi/herdr-mobile**](https://github.com/nourhelmi/herdr-mobile) | Controls Herdr agents and terminal panes from an iPhone app through a Bun sidecar. |
| [**marcelpanse/herdr-osx-menubar**](https://github.com/marcelpanse/herdr-osx-menubar) | Shows Herdr agents in the macOS menu bar and jumps to a selected session or project. |
| [**MarceloEmilioRiveraC/pitwall**](https://github.com/MarceloEmilioRiveraC/pitwall) | Opens a portable Windows terminal workspace with a Herdr TUI agent sidebar and a Git-aware file viewer with live diffs. |
| [**pistelak/Paddock**](https://github.com/pistelak/Paddock) | Wraps Herdr sessions in a native macOS window with a Ghostty tab per session. |
| [**sendhil/herdr-menubar**](https://github.com/sendhil/herdr-menubar) | Monitors agent status from the macOS menu bar and jumps to the relevant Herdr pane. |
| [**WoodardDigital/herdr-remote**](https://github.com/WoodardDigital/herdr-remote) | Streams Herdr TUI sessions to an Android client with touch controls and agent push notifications. |
| [**gustavocaiano/herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher) | Launches or focuses configured local and SSH Herdr TUI desktops using a macOS Ghostty companion and plugin. |
| [**huahaimaker/herdr-mac**](https://github.com/huahaimaker/herdr-mac) | Runs the Herdr TUI in unofficial native macOS and Windows clients. |
| [**Tatendaz/herdr-launcher**](https://github.com/Tatendaz/herdr-launcher) | Opens or focuses the Herdr terminal interface from a macOS Dock icon. |
| [**3loc/herden**](https://github.com/3loc/herden) | Connects an iPhone console to a persistent Herdr-derived agent host using SSH pairing. |
| [**ralfkuh-lab/sheepdock**](https://github.com/ralfkuh-lab/sheepdock) | Opens Herdr in a dedicated Kitty window with its own macOS Dock icon. |
| [**cagriy/herdr-notch-releases**](https://github.com/cagriy/herdr-notch-releases) | Distributes macOS Herdr Notch release downloads and its update feed. |
| [**kingbywork-ui/issh-plugin-herdr**](https://github.com/kingbywork-ui/issh-plugin-herdr) | Adds workspace creation, session binding, and runtime health to the issh desktop client for Herdr workspaces. |

### Web dashboards and remote viewers

*101 projects. Browser-based monitors, remote controls, and visual scenes for following Herdr agents from another screen or device.*

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
| [**IvoryHeart/herdr-world**](https://github.com/IvoryHeart/herdr-world) | Connects local and SSH Herdr TUI hosts to a web control plane for viewing agents, terminals, files, and changes on desktop or mobile. |
| [**riba2534/herdrx**](https://github.com/riba2534/herdrx) | Opens a self-hosted Herdr web workbench for desktop and mobile with multi-host terminals. |
| [**BlackAngel242/MyTeam**](https://github.com/BlackAngel242/MyTeam) | Shows Herdr agents in a local pixel-art office where users can send instructions and read replies. |
| [**code-yeongyu/web-terminal**](https://github.com/code-yeongyu/web-terminal) | Runs a self-hosted mobile-first web terminal with persistent sessions, file browsing, and Herdr integration. |
| [**erwins-enkel/shepherd**](https://github.com/erwins-enkel/shepherd) | Hosts a browser control panel for parallel Claude Code and Codex sessions in isolated worktree panes. |
| [**luiscleto/shepherdr**](https://github.com/luiscleto/shepherdr) | Adds a phone-friendly web interface for Herdr: monitor agents, receive notifications, open real terminals, and send files. |
| [**hmu332233/herdr-f1**](https://github.com/hmu332233/herdr-f1) | A web visualization that represents active Herdr agents as Formula 1 cars, using race and pit-stop states to show whether agents are running, blocked, or finished. |
| [**fivetaku/whosup**](https://github.com/fivetaku/whosup) | Shows agents across Herdr TUI sessions on a local browser board and jumps to panes needing attention. |
| [**mikro-design/super-herdr**](https://github.com/mikro-design/super-herdr) | Monitors and controls Herdr sessions across machines from a terminal interface or paired phone browser. |
| [**barnuri/herdr-web**](https://github.com/barnuri/herdr-web) | Adds a mobile-first web interface for Herdr to monitor and drive coding agents from any device browser. |
| [**afloury/wherdr**](https://github.com/afloury/wherdr) | Runs a self-hosted web client for following Herdr sessions, using terminals, and replying to agents from a browser or phone. |
| [**dipeshdulal/gothalo**](https://github.com/dipeshdulal/gothalo) | Controls Herdr coding agents from a self-hosted mobile remote over Tailscale. |
| [**nixfred/shepr**](https://github.com/nixfred/shepr) | Shows and replies to Herdr agent sessions across hosts from an iPhone home-screen web app over Tailscale. |
| [**neyham/herdr-paddock**](https://github.com/neyham/herdr-paddock) | Displays a phone-friendly terminal feed of Herdr agents over SSH and supports prompt replies. |
| [**transparent-pegasus/herdr-remote**](https://github.com/transparent-pegasus/herdr-remote) | Lets users inspect Herdr TUI panes and send prompts from a phone browser through a self-hosted server. |
| [**lntvan166/paddock**](https://github.com/lntvan166/paddock) | Groups Herdr agents by state in a phone-sized dashboard and lets users answer prompts. |
| [**Hybridhash/relaydeck**](https://github.com/Hybridhash/relaydeck) | Controls Herdr TUI sessions from a phone, tablet or browser over a private Tailscale network. |
| [**eyalev/herdr-web**](https://github.com/eyalev/herdr-web) | Shows and controls Herdr TUI agents through a mobile-first browser interface with live terminal views and status. |
| [**osuki-dev/muqun-gateway**](https://github.com/osuki-dev/muqun-gateway) | Connects the Muqun mobile app to Herdr over encrypted peer-to-peer connections for remote viewing, approvals, and prompts. |
| [**zlxlabs/herdweb**](https://github.com/zlxlabs/herdweb) | Monitors and drives coding agents from mobile devices, supporting voice input, image pasting, webhooks, and multi-device servers. |
| [**NikNovo/deathstar**](https://github.com/NikNovo/deathstar) | Displays Linux host memory pressure and optional Herdr and OMP session data in a local observability dashboard. |
| [**allmight-ai/herdr-pet**](https://github.com/allmight-ai/herdr-pet) | A retro virtual-pet display that reacts to live Herdr agent states and creates a persistent pet identity from the user's GitHub ID. |
| [**kauakdev/kauak**](https://github.com/kauakdev/kauak) | Shows Herdr TUI agents in an interactive isometric office where users can read and answer terminal sessions. |
| [**loofare/herdr-portal**](https://github.com/loofare/herdr-portal) | Shows Herdr agents on a live terminal board and a browser dashboard with navigation and replies. |
| [**hrdle/hrdle**](https://github.com/hrdle/hrdle) | Controls Herdr TUI coding agents through a phone browser or Even Realities G2 glasses. |
| [**matheus3301/herdr-phone**](https://github.com/matheus3301/herdr-phone) | Monitors and controls a Herdr session from a phone through a web interface. |
| [**aviz85/herdr-controller**](https://github.com/aviz85/herdr-controller) | A Next.js dashboard for Herdr with a live agent grid, terminal mirror, messaging, agent spawning, and an optional 3D office view driven through the Herdr CLI. |
| [**arcnessai/arcdr**](https://github.com/arcnessai/arcdr) | Shows Herdr agents on a phone or browser over Tailscale and lets users answer prompts. |
| [**AnnasCookies/bordr**](https://github.com/AnnasCookies/bordr) | Opens a mobile web workspace over Tailscale for reading and controlling Herdr agents and panes. |
| [**dark2momo/herdr-tty**](https://github.com/dark2momo/herdr-tty) | Adds a mobile-friendly web terminal for Herdr powered by ttyd. |
| [**kkunkunya/herdr-remote-phone**](https://github.com/kkunkunya/herdr-remote-phone) | Controls Herdr from a phone-focused web interface with Mac profiles and conversation views. |
| [**luiscleto/weherd**](https://github.com/luiscleto/weherd) | Visualizes local Herdr agents in an interactive Three.js office. |
| [**mejiasd3v/herdr-farm**](https://github.com/mejiasd3v/herdr-farm) | A Three.js dashboard that represents Herdr workspaces and agents as a 3D farm, with animal animations tied to live idle, working, and blocked states. |
| [**funsaized/herdr-mise**](https://github.com/funsaized/herdr-mise) | Represents Herdr agents as line cooks and animates their work, tool use, and blocked states from live socket events. |
| [**misty-step/kelpie**](https://github.com/misty-step/kelpie) | Adds a phone-first PWA and desktop cockpit for checking and triaging OMP agents in Herdr workspaces. |
| [**dibin666/herdr-remote**](https://github.com/dibin666/herdr-remote) | Controls Herdr workspaces and agent terminals from a desktop or phone browser. |
| [**spad-0x/herdr-mobile-pro**](https://github.com/spad-0x/herdr-mobile-pro) | Controls Herdr and coding agents from a mobile-first web dashboard with speech input and image uploads. |
| [**JeremiahChurch/herd-remote**](https://github.com/JeremiahChurch/herd-remote) | Controls Herdr TUI agent sessions from a phone-friendly web interface, including prompts and approval actions. |
| [**derekr/wherdr**](https://github.com/derekr/wherdr) | Mirrors Herdr TUI workspaces and terminal panes in a browser, with input and agent approval controls for desktop or phone. |
| [**patraianton/sheepdog**](https://github.com/patraianton/sheepdog) | Shows Herdr coding-agent sessions on a live kanban board and lets a user dispatch work. |
| [**tlamadon/herdr-hq**](https://github.com/tlamadon/herdr-hq) | Displays Herdr agent status and per-agent resource usage across SSH-connected machines in a web dashboard. |
| [**StructuPath/herdr-suite-site · console**](https://github.com/StructuPath/herdr-suite-site/tree/main/console) | Shows read-only Herdr Suite workflow, worktree, and readiness information in a local browser console. |
| [**iYassr/shahi**](https://github.com/iYassr/shahi) | Lets users read agent conversations, answer permission prompts, and manage Herdr sessions from a phone or browser. |
| [**chano-gpt/setnet**](https://github.com/chano-gpt/setnet) | Supervises Claude Code, Codex, Pi, OpenCode, AGY, and OMO agents from a phone browser over Tailscale. |
| [**carsol/herdr-mobile**](https://github.com/carsol/herdr-mobile) | Adds a mobile-first web UI for Herdr: see your agents, attach to panes, chat with Claude Code and Codex from your phone. |
| [**lifez/herdr-agent-dashboard**](https://github.com/lifez/herdr-agent-dashboard) | Shows read-only Herdr agent activity on a touch-friendly local web dashboard for devices such as a Boox. |
| [**vantt/herdr-go**](https://github.com/vantt/herdr-go) | Controls Herdr coding agents from a phone using a web-first gateway. |
| [**damozhang/dsh-herdr-bridge**](https://github.com/damozhang/dsh-herdr-bridge) | Lets the web interface discover, start, prompt, and monitor Pi, Claude, Codex, and other agents running under Herdr. |
| [**zbysir/herdr-web**](https://github.com/zbysir/herdr-web) | Opens a browser terminal and voice prompt interface for Herdr, with mobile QR access. |
| [**tigorlazuardi/herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui) | Opens a Herdr session in a browser or installable web app with terminal input and mobile controls. |
| [**gabrielbarretoo/herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval) | A Three.js visualization that turns Herdr workspaces into medieval camps and panes into animated adventurers whose behavior reflects each agent's state. |
| [**Eden-Sun/agents-manager**](https://github.com/Eden-Sun/agents-manager) | Manages multiple coding-agent CLIs running in Herdr panes via a Rust Axum daemon and React frontend. |
| [**SimplicityGuy/herdr-corral**](https://github.com/SimplicityGuy/herdr-corral) | Edits Herdr TUI configuration in a browser with a live layout preview and local import and export. |
| [**scttymn/ranchr**](https://github.com/scttymn/ranchr) | Connects a phone or desktop PWA to a local Herdr session through a gateway, with optional tunnel access. |
| [**fellnerse/herdr-mobile**](https://github.com/fellnerse/herdr-mobile) | Adds a minimal mobile web interface for Herdr agent management. |
| [**Lawofaveragesproterozoicaeon236/web-terminal**](https://github.com/Lawofaveragesproterozoicaeon236/web-terminal) | Runs a self-hosted web terminal with persistent sessions, file browsing, and Herdr workspace and agent status. |
| [**Orchard-Robotics/herdview**](https://github.com/Orchard-Robotics/herdview) | Mirrors running Herdr agents in a phone-friendly web UI for reading transcripts, answering prompts, and sending input. |
| [**frizynn/nenu**](https://github.com/frizynn/nenu) | Adds a self-hosted web workbench for supervising Herdr coding agents from desktop or phone. |
| [**JasonBates/agentdeck**](https://github.com/JasonBates/agentdeck) | Shows Herdr agent status and transcript summaries in a browser on your Tailscale network, with tap-to-focus. |
| [**deanbaker/herdr-remote**](https://github.com/deanbaker/herdr-remote) | Displays Herdr TUI agents and live panes in a browser and sends prompts or interactive terminal input through a host bridge. |
| [**DanyGoT/herdr-companion**](https://github.com/DanyGoT/herdr-companion) | Serves a phone-friendly Herdr TUI companion with live agent status, terminal mirroring, input and image upload. |
| [**montagao/herdr-story**](https://github.com/montagao/herdr-story) | Shows Herdr TUI agents in a pixel-art office and lets users jump into conversations. |
| [**GoldenRegulus/herdr-web**](https://github.com/GoldenRegulus/herdr-web) | Opens existing Herdr TUI sessions in a local browser terminal. |
| [**Blankeos/herdr-serve**](https://github.com/Blankeos/herdr-serve) | Streams a Herdr TUI agent terminal to a phone browser with keyboard controls. |
| [**cnyarx/shelt**](https://github.com/cnyarx/shelt) | Opens a browser terminal for a Herdr session or login shell with clipboard image paste. |
| [**hmu332233/herdr-visual-lab**](https://github.com/hmu332233/herdr-visual-lab) | Shows live Herdr agent activity as animated galaxies, races, raids, and other scenes. |
| [**ihubanov/herdr-web**](https://github.com/ihubanov/herdr-web) | Opens a local browser client for Herdr sessions through a token-protected loopback bridge and socket API. |
| [**harlanljones/herdr-outpost**](https://github.com/harlanljones/herdr-outpost) | Adds a remote dashboard and relay gateway for Herdr sessions. |
| [**gregmcausland/herdr-control**](https://github.com/gregmcausland/herdr-control) | Adds a browser control and orchestration surface for Herdr panes. |
| [**bbgo19/herdr-web**](https://github.com/bbgo19/herdr-web) | Offers a browser interface for managing Herdr workspaces, panes, and multiple coding agents. |
| [**jwgung/HerdRabbit**](https://github.com/jwgung/HerdRabbit) | Adds a personal PWA for controlling your Herdr sessions. |
| [**radityasurya/tautan**](https://github.com/radityasurya/tautan) | Adds a mobile-first PWA hub for herdr and tmux: see every coding agent's state from your phone and reply, over Tailscale. |
| [**jclement/herdrer**](https://github.com/jclement/herdrer) | Shows a review inbox and terminal for Herdr agents that users can answer from a phone. |
| [**YannickHerrero/kelpie**](https://github.com/YannickHerrero/kelpie) | Opens a messaging-style PWA for Pi agents running in Herdr. |
| [**screenagers-io/bullpen**](https://github.com/screenagers-io/bullpen) | Shows Herdr TUI coding agents in a browser-based 3D voxel office. |
| [**stefanopineda/herdr-web**](https://github.com/stefanopineda/herdr-web) | Opens Herdr TUI sessions and agents from a phone-friendly browser over Tailscale. |
| [**kody-w/nerf-herdr-control-tower**](https://github.com/kody-w/nerf-herdr-control-tower) | Opens a local browser dashboard for a Herdr fleet and exports context or sends manual Horn broadcasts. |
| [**evsinev/herdr-watch**](https://github.com/evsinev/herdr-watch) | Monitors local and SSH-connected Herdr servers in a read-only web dashboard with workspace and agent status. |
| [**y011d4/herdr-plugin-agentweb**](https://github.com/y011d4/herdr-plugin-agentweb) | Monitors and controls Herdr TUI agents from a mobile-first web app backed by a local bridge. |
| [**narumiruna/herdr-web**](https://github.com/narumiruna/herdr-web) | Opens a browser workbench for viewing and operating the Herdr agent runtime. |
| [**NolanHo/DSH-herdr**](https://github.com/NolanHo/DSH-herdr) | Adds a DSH web view for inspecting Herdr TUI workspaces and agents, reading pane output and sending prompts. |
| [**maedana/herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge) | Serves a phone-friendly Herdr TUI agent dashboard with status tabs, output, text input and key sending via QR connection. |
| [**sina85/herdr-mobile**](https://github.com/sina85/herdr-mobile) | Controls a local Herdr session from a mobile-first web panel through Cloudflare Tunnel and Access. |
| [**pepperhorn/herdr-remote**](https://github.com/pepperhorn/herdr-remote) | Displays Herdr TUI workspaces, panes and agent status in a remote browser dashboard and switches focused tabs. |
| [**shaunbntan-create/vgpt-app**](https://github.com/shaunbntan-create/vgpt-app) | Monitors and controls Herdr TUI agents from a phone browser over Tailscale, with terminal mirrors and a command palette. |
| [**crabfishxy/awaytome**](https://github.com/crabfishxy/awaytome) | Monitors and operates Herdr TUI agents from an Android phone through a Tailscale-connected PWA with terminal mirroring. |
| [**snowkiss13/herdr-habitat**](https://github.com/snowkiss13/herdr-habitat) | Shows Herdr TUI agent states and recent terminal activity in a local animated browser view. |
| [**sh1ftmaker/herdr-term**](https://github.com/sh1ftmaker/herdr-term) | Bridges Herdr sessions to browser interfaces with read-only file exploration and Hyprland desktop streaming. |
| [**carter2099/herdr-web-client**](https://github.com/carter2099/herdr-web-client) | Attaches to Herdr terminals through a self-hosted browser client. |
| [**4noha/herdr-drover**](https://github.com/4noha/herdr-drover) | Syncs Herdr TUI sessions across machines and connects browser or phone terminals through a cloud relay. |
| [**BlazzzPlay/herdr-office**](https://github.com/BlazzzPlay/herdr-office) | Visualizes Herdr agents and their activity in a read-only pixel-art office. |

### Hardware and ambient displays

*31 projects. Keypads, watches, desk devices, and compact displays that turn agent state into physical controls or at-a-glance signals.*

| Project | What it does |
|---|---|
| [**timvdhoorn/stream-deck-herdr-plugin**](https://github.com/timvdhoorn/stream-deck-herdr-plugin) | Assigns a key to each agent, displays its state with a color and icon, and focuses the matching Herdr pane when pressed. |
| [**Unayung/herdr-watch**](https://github.com/Unayung/herdr-watch) | A native Apple Watch companion that shows Herdr agent activity and alerts the wearer when an agent finishes or needs input. |
| [**spencerbull/xeneon-edge-agents**](https://github.com/spencerbull/xeneon-edge-agents) | An Omarchy and Herdr agent command center designed for the Corsair XENEON EDGE display, with conservative handling when state cannot be confirmed. |
| [**walcew/herdr-assist**](https://github.com/walcew/herdr-assist) | An ESP32-S3 desk display that shows Herdr session states and sounds a bell when an agent is waiting for a decision or approval. |
| [**mrshu/muxboard**](https://github.com/mrshu/muxboard) | Shows Herdr agent attention status and CodexBar usage metrics on a Stream Deck+ dashboard. |
| [**alasano/house-of-herdr**](https://github.com/alasano/house-of-herdr) | Maps Herdr TUI agent status and controls to the Work Louder Codex Micro keypad, dial, and joystick. |
| [**niklasberglund/herdr-logi-plugin**](https://github.com/niklasberglund/herdr-logi-plugin) | Shows Herdr TUI workspace and agent status on a Logitech MX Keypad and focuses a selected pane on keypress. |
| [**Resilient-Software/herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck) | Mirrors Herdr TUI workspaces to a Stream Deck with repository, branch and agent-status tiles. |
| [**fedeya/corral**](https://github.com/fedeya/corral) | Shows Herdr TUI agents as animated critters on a Stream Deck Plus and focuses an agent when its key is tapped. |
| [**chenxin-yan/herdr-micro**](https://github.com/chenxin-yan/herdr-micro) | Controls and monitors Herdr coding agents from a physical MacroPad. |
| [**dkarter/foreman**](https://github.com/dkarter/foreman) | Shows live Herdr TUI agents on a Raspberry Pi touchscreen and focuses their panes by tap. |
| [**vaclavik-xyz/herdeck**](https://github.com/vaclavik-xyz/herdeck) | Controls Herdr agents from a Stream Deck, a native desktop window, or a browser dashboard. |
| [**rkbkosp/agent-beacon**](https://github.com/rkbkosp/agent-beacon) | Displays Herdr agent state, Codex quota, and alerts on an ESP32-S3 beacon through a macOS bridge. |
| [**bowlofsoup/herdr-stoplight**](https://github.com/bowlofsoup/herdr-stoplight) | An Arduino integration that uses a physical traffic light to show aggregate Herdr status: green for working, red for blocked or failed, and yellow for idle. |
| [**third774/herdr-sidepulse**](https://github.com/third774/herdr-sidepulse) | A USB hardware integration for SidePulse Pro and Dot devices that turns combined Herdr agent states into ambient LED patterns, including prominent alerts for blocked agents. |
| [**omerturhan/herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar) | Shows working and blocked Herdr agents and jumps to a selected agent's tab when tapped. |
| [**johnendean/herdrkeys**](https://github.com/johnendean/herdrkeys) | Uses Pimoroni Keybow 2040 as a way of monitoring and switching between agents running in Herdr, inspired by the Codex Micro/Creator Micro2. |
| [**so1omon563/herdr-control-stream-deck**](https://github.com/so1omon563/herdr-control-stream-deck) | Navigates Herdr TUI workspaces, tabs, panes, and agents from an Elgato Stream Deck. |
| [**dghelm/herdy**](https://github.com/dghelm/herdy) | Provides a hurdy-gurdy for your agent herd: MIDI hardware control surface for herdr and Omarchy (Arturia Keylab 61). |
| [**imbriaco/herdr-deck**](https://github.com/imbriaco/herdr-deck) | Streams Deck plugin for Herdr: live agent status lights and one-key focus. |
| [**pnomolos/herdr-kontrol**](https://github.com/pnomolos/herdr-kontrol) | Shows Herdr TUI agent status and focuses panes using a Maschine MK3 or Plus controller on macOS. |
| [**dghelm/omarchy-herdy**](https://github.com/dghelm/omarchy-herdy) | Configures the herdy MIDI controller for Herdr agent workspaces from an Omarchy bar panel. |
| [**lfsmoura/led-agent-status**](https://github.com/lfsmoura/led-agent-status) | Shows your AI agents' status on a BLE LED strip, blue working, blinking red blocked, green done. |
| [**sigma/sd-mux**](https://github.com/sigma/sd-mux) | Shows agents needing attention on a Stream Deck button and cycles through them when pressed. |
| [**gpando/herdr-sense**](https://github.com/gpando/herdr-sense) | Displays Herdr agent states on a Raspberry Pi Sense HAT LED matrix using MQTT events from herdr-telegram. |
| [**tmcinerney/beckon**](https://github.com/tmcinerney/beckon) | Binds Herdr TUI agent panes to navigation keys and displays agent states on a wired Glove80. |
| [**AlexBSoD/qubeherd**](https://github.com/AlexBSoD/qubeherd) | A hardware integration that shows Herdr agent state, the host clock, and keyboard layout on an Ergohaven Qube dongle display. |
| [**8-BitRhyon/bantay-tui**](https://github.com/8-BitRhyon/bantay-tui) | A macOS notch HUD that combines Herdr approvals, live usage and cost data, a file shelf, task tracking, Apple Reminders sync, and session controls. |
| [**zhongpei/herdr-ulanzi-deck**](https://github.com/zhongpei/herdr-ulanzi-deck) | A Ulanzi D200X keypad integration that shows live, priority-sorted Herdr agent states on LCD keys and can monitor several Herdr machines over SSH. |
| [**walcew/herdr-avatars**](https://github.com/walcew/herdr-avatars) | Adds downloadable avatar packages for the Herdr Assist hardware dashboard, including agent-state animations. |
| [**zanellig/keyblink**](https://github.com/zanellig/keyblink) | Blinks the HyperX Alloy Origins Core Game Mode indicator on Herdr TUI agent status changes on Linux. |

### Plugins and supporting utilities

*137 projects. Small integrations for notifications, status, tasks, scheduling, agent management, and everyday desktop behavior.*

| Project | What it does |
|---|---|
| [**ogulcancelik/herdr-browser**](https://github.com/ogulcancelik/herdr-browser) | Renders an interactive Chromium browser inside a Herdr pane and lets agents automate it through Chrome DevTools Protocol. The project is deprecated in favor of terminal-browser. |
| [**levi-qiao/herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota) | A sidebar quota monitor for Claude, Codex, Grok, and Agy that shows the percentage remaining in five-hour and weekly limits. |
| [**speardragon/herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager) | A small in-terminal menu for browsing, installing, updating, enabling, and disabling Herdr plugins through the standard plugin command-line interface. |
| [**miiraheart/herdr-beads**](https://github.com/miiraheart/herdr-beads) | Displays Beads issues as a list, table, or Kanban board in a Herdr sidebar or floating pane. |
| [**natori-hrj/herdr-lazy**](https://github.com/natori-hrj/herdr-lazy) | A declarative Herdr plugin manager with a dedicated terminal interface, a lockfile, version pinning, synchronization from one list, and support for prebuilt binaries. |
| [**CodeForBreakfast/beady-eye**](https://github.com/CodeForBreakfast/beady-eye) | Shows, live, which agent works on which bead across your projects next to its Herdr pane, and tells agents and scripts when the beads they wait on change. |
| [**qintmb/herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker) | Applies terminalcolors.com palettes to Herdr TUI interface elements through a popup theme picker. |
| [**coryshaw1/herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp) | Opens the cliamp audio player in a floating Herdr TUI pane while playback continues in a detached session. |
| [**mo-arvan/herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry) | Detects Claude Code stalls caused by rate limits or server errors and safely resumes only idle or blocked panes, leaving actively working agents untouched. |
| [**Resetnak/herdr-logbook**](https://github.com/Resetnak/herdr-logbook) | Manages Markdown tasks and decisions in an offline notebook for Herdr workspaces. |
| [**dirien/herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin) | Runs Claude Code, Codex, Gemini CLI, and other coding agents in separate Docker Sandboxes from Herdr TUI. |
| [**shibayu36/herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes) | Automatically equalizes Herdr TUI panes after splits and closures, with an optional manual action. |
| [**pivoshenko/musicforprogramming · plugins/herdr/mfp.player**](https://github.com/pivoshenko/musicforprogramming/tree/main/plugins/herdr/mfp.player) | Opens the musicforprogramming.net player in a Herdr TUI pane and maps playback controls to actions. |
| [**ezcorp-org/herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status) | Shows staged, modified, untracked, and conflicted Git files for each workspace beside its branch name. |
| [**MattJColes/herdr-web-browser**](https://github.com/MattJColes/herdr-web-browser) | Opens browser previews beside coding agents in Herdr and shares console errors, network requests, screenshots, and selected page content. |
| [**aorumbayev/herdr-canvas**](https://github.com/aorumbayev/herdr-canvas) | Opens a mouse-driven ASCII diagram canvas in a Herdr split. Humans draw boxes, lines, and text; agents read and edit the same JSON-backed diagrams through the CLI and skill. |
| [**finna/omarchy-herdr-hud**](https://github.com/finna/omarchy-herdr-hud) | Monitors and prompts Herdr agents from a draggable Omarchy overlay. |
| [**sudoeren/herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker) | Runs lazydocker in a herdr split pane or its own tab. |
| [**vjeantet/herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad) | Docks a plain-text scratchpad at the bottom of a tab, one persistent buffer per tab, for composing a prompt where Enter can't send it half-finished. `Ctrl+E` moves it, or just the selection, into an agent of the same tab without submitting; `Ctrl+C` copies over OSC 52. |
| [**dvdksn/sbx-herdr**](https://github.com/dvdksn/sbx-herdr) | Registers Docker Sandboxes as Herdr TUI SSH machines and identifies sandbox agents in local panes. |
| [**carze/herdr-smolmachine**](https://github.com/carze/herdr-smolmachine) | Starts coding agents in libkrun or KVM microVMs from Herdr panes and lists running sandboxes. |
| [**kosuketut/herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder) | Downloads files created or changed in a remote Herdr pane to a local Mac. A plugin action detects paths in the active pane and transfers the selected artifact over the remote connection. |
| [**ddfonseca/herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image) | Saves an image from the macOS or Linux clipboard to disk and pastes its file path into the active pane for use by multimodal agents. |
| [**mrolafsson/herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer) | Transfers files between a local machine and a remote Herdr TUI host over SSH and sends their paths to agents. |
| [**JYasha11/herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face) | Shows an increasingly urgent ASCII-art face when a Herdr agent is blocked and waiting for input, making overlooked approvals difficult to miss. |
| [**ablause/herdr-flutter**](https://github.com/ablause/herdr-flutter) | A Herdr sidebar for watching, hot-reloading, and inspecting a running Flutter app beside the coding agent working on it. |
| [**ivolkoff/herdr-huddle**](https://github.com/ivolkoff/herdr-huddle) | Opens rich questions over a Herdr TUI agent pane and returns the answers to the agent as JSON. |
| [**scrappylabsai/podr**](https://github.com/scrappylabsai/podr) | Adds Reasonix and DeepSeek Harness detection to a Herdr TUI fork and includes a client for attaching to DSH sessions. |
| [**XiangQhello/codex-claude-auto-enter**](https://github.com/XiangQhello/codex-claude-auto-enter) | Sends repeated Enter presses to a selected Herdr TUI pane and stops when Codex or Claude Code becomes idle. |
| [**RenKoya1/herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all) | Approves every pending agent permission request in Herdr with one keystroke. |
| [**Tomatio13/herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail) | Browses Gmail in a Herdr TUI split using fzf and gogcli, with mail actions and background notifications. |
| [**hexsprite/herdr-beads**](https://github.com/hexsprite/herdr-beads) | Opens Beads issue details in a Herdr TUI split when an issue ID is Ctrl-clicked. |
| [**suisya-systems/herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office) | A terminal pixel-art office where Herdr agents appear as animated desk workers, blocked agents raise timed alerts, and selecting a character focuses its pane. |
| [**RizRiyz/pixtui**](https://github.com/RizRiyz/pixtui) | Opens a terminal pixel-art editor in a Herdr TUI pane with layers, animation, and PNG or GIF export. |
| [**Javamomma/herdr-scribe**](https://github.com/Javamomma/herdr-scribe) | Streams microphone audio to temporary panes and creates meeting notes, policy checks, and draft tickets without saving raw audio. |
| [**neospeed83/herdr-standup**](https://github.com/neospeed83/herdr-standup) | Builds a daily standup from Git commits and optional notes, then opens the report from a Herdr TUI workspace. |
| [**carsonjones/herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard) | Lists live Herdr agent status in a Bun and React/OpenTUI dashboard that can run as a plugin action or standalone terminal app. |
| [**mdetweil/herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask) | Opens Lazytask in a Herdr TUI split or tab and adds Taskwarrior quick actions. |
| [**WillowMist/herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden) | Searches a Bitwarden vault from a Herdr TUI popup and copies or pastes selected credentials. |
| [**Tomatio13/herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar) | Browses Google Calendar events in an fzf panel and creates a Herdr TUI worktree and workspace from an event. |
| [**eszanon/omarchy-herdr**](https://github.com/eszanon/omarchy-herdr) | Shows Herdr coding agents in the Omarchy bar and flags the ones waiting on you. |
| [**kamaaina/herdr_sync**](https://github.com/kamaaina/herdr_sync) | Sends the command currently typed in one pane to every other pane in the same tab, providing synchronized-pane behavior for Herdr. |
| [**chrisg32/tsk**](https://github.com/chrisg32/tsk) | Manages plain-text tasks in a Rust TUI that runs standalone or as a Herdr plugin. |
| [**furuhashin/herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes) | Broadcasts one command to every pane in the current tab, providing a shell-based equivalent of tmux synchronized panes. |
| [**A1exthegreat/herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify) | Sends desktop notifications when agents finish, request confirmation, or become idle. |
| [**dio16/herdr-auto-update**](https://github.com/dio16/herdr-auto-update) | Checks installed Herdr plugins for newer upstream commits and reinstalls updated versions automatically. |
| [**gw31415/herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos) | Watches Herdr agent-status events and keeps an Amphetamine session active while agents are working, preventing sleep during long tasks. |
| [**ponko2/herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes) | Automatically equalizes Herdr TUI pane sizes when panes are created, closed, moved, or exit, with an on-demand action. |
| [**azyu/herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming) | Gives every detected agent a readable two-word name, persisted as the pane label so it survives restarts. |
| [**SerHappy/herdr-achievements**](https://github.com/SerHappy/herdr-achievements) | Awards achievements and celebrations for completed tasks across your Herdr AI agent herd. |
| [**salemsayed/omaherd**](https://github.com/salemsayed/omaherd) | Shows local and SSH-accessible Herdr agent states in the Omarchy bar and jumps to a selected pane. |
| [**wazum/herdr-polyglot**](https://github.com/wazum/herdr-polyglot) | Translates prompts into English before sending them to an agent pane in Herdr. |
| [**Dolliwyx/herdr-rpc**](https://github.com/Dolliwyx/herdr-rpc) | Publishes the focused Herdr workspace and agent counts to Discord Rich Presence from a Windows WSL2 setup. |
| [**zackshen/herdr-translate**](https://github.com/zackshen/herdr-translate) | Translates mouse-selected Herdr TUI text in a centered popover using a local model or Google fallback. |
| [**ivorpad/herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel) | Lists local listening ports and opens, copies, or stops public tunnels from a Herdr TUI pane. |
| [**ivorpad/herdr-ports**](https://github.com/ivorpad/herdr-ports) | Adds a popup that lists listening ports, names the project behind each one, and kills or opens it. |
| [**DeepRuparel/herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify) | Controls Spotify playback and playlist queues directly from Herdr terminal panes. |
| [**shippy/raycast-herdr · extensions/herdr**](https://github.com/shippy/raycast-herdr/tree/main/extensions/herdr) | Controls Herdr TUI workspaces from Raycast and launches Claude prompts or configured actions. |
| [**AZenking/herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center) | Adds a Herdr popup for monitoring and focusing local Node.js, Bun, and Deno services. |
| [**smanickam01/herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin) | Opens Atuin history search in a Herdr TUI popup and inserts or runs the selected command in the originating pane. |
| [**niceview/mac-finder-quick-actions**](https://github.com/niceview/mac-finder-quick-actions) | Opens Finder selections in VS Code or a new Herdr TUI workspace through macOS quick actions and a drag-and-drop launcher. |
| [**fraction12/herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog) | Opens Rainfrog in a managed Herdr TUI pane with a connection picker and workspace-scoped pane reuse. |
| [**tkuchiki/herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context) | Opens Herdr tabs with isolated Kubernetes contexts and namespaces. |
| [**hotnugs/herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time) | Adds emoji to Herdr TUI space, agent, and tab names to make them easier to identify. |
| [**d4rken/herdr-mint-applet**](https://github.com/d4rken/herdr-mint-applet) | Displays Cinnamon desktop panel applets showing idle, busy, or blocked Herdr agent sessions. |
| [**Slimydog21/herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm) | Controls an existing NixOS development VM from a Herdr TUI pane, including boot, stop, monitoring, and SSH. |
| [**Royal-lobster/herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup) | Shows a configurable launcher in every new Herdr tab. Tools are defined in JSON and start directly in the selected pane with normal agent detection. |
| [**Sawakee/herdr-imebox**](https://github.com/Sawakee/herdr-imebox) | Opens an IME-friendly popup for composing CJK text and sending it to a Herdr TUI agent pane. |
| [**bestony/herdr-codex-capacity-retry**](https://github.com/bestony/herdr-codex-capacity-retry) | Automatically continues Codex sessions in Herdr after capacity-related interruptions. |
| [**playsthisgame/herdr-api-client**](https://github.com/playsthisgame/herdr-api-client) | Opens the Ichigo terminal REST client in a split or tab and scopes it to the current project's request collection. |
| [**khatriafaz/herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo) | Adds the current agent, repository, and branch names to Herdr pane headers and the sidebar. |
| [**ondratuma/herdr-status-plugin**](https://github.com/ondratuma/herdr-status-plugin) | A per-pane activity plugin with sidebar icons, live timers, and a helper for renaming agent panes. |
| [**susomejias/herdr-awake**](https://github.com/susomejias/herdr-awake) | Keeps the machine awake while Herdr agents are busy. |
| [**redsquiggle/herdr-browser**](https://github.com/redsquiggle/herdr-browser) | Keeps Chromium tab groups aligned with Herdr workspaces. |
| [**wine-fall/herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id) | Copies the focused pane's id to the clipboard, or show every pane's id on its border. |
| [**joelhooks/herdr-brain**](https://github.com/joelhooks/herdr-brain) | Renders Brain SVX documents as native OpenTUI views in Herdr panes. |
| [**speardragon/herdr-labs**](https://github.com/speardragon/herdr-labs) | Provides herdr plugin lab, AI-agent plugin idea contests: 9 agents compete, AI judges score. |
| [**abcxff/herdr-docker**](https://github.com/abcxff/herdr-docker) | Keeps track of docker builds like you do with agents for herdr. |
| [**rigelstpierre/herdr-devin-board**](https://github.com/rigelstpierre/herdr-devin-board) | Lists your Devin Cloud sessions in a herdr tab with live GitHub PR, CI, and review status. Attaches to a session in a new tab with `devin --cloud --resume`, opens `devin ssh` in a pane, or archives it. |
| [**TinocoAI/herdr-checkpoint-health**](https://github.com/TinocoAI/herdr-checkpoint-health) | Runs read-only Check Point GAiA health checks over SSH from a Herdr TUI plugin and summarizes gateway status. |
| [**dpulpeiro/omarchy-herdr-collie**](https://github.com/dpulpeiro/omarchy-herdr-collie) | Monitors and controls the Collie Herdr web UI and its Tailscale Serve endpoint from the Omarchy bar. |
| [**enisbu/herdr-kitty-theme-sync**](https://github.com/enisbu/herdr-kitty-theme-sync) | Synchronizes the active Herdr TUI theme to kitty’s ANSI palette. |
| [**VoidAxon/herdr-lens**](https://github.com/VoidAxon/herdr-lens) | Translates and explains selected pane text, including words, identifiers, and build output, using an AI provider. |
| [**Efeguclu1/herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard) | Identifies processes started by agents by workspace and pane, explains suspected leftovers, and previews process trees before stopping them. |
| [**CydoEntis/chameleon**](https://github.com/CydoEntis/chameleon) | Applies a shared palette to Herdr, Windows Terminal, Oh My Posh, and Claude Code. |
| [**YF-Tobehero/Herdr-palette-probe-for-windows**](https://github.com/YF-Tobehero/Herdr-palette-probe-for-windows) | Measures agent terminal colors and helps choose a Windows Terminal palette for use with Herdr TUI. |
| [**andy-spike/herdr-theme**](https://github.com/andy-spike/herdr-theme) | Syncs the Herdr TUI color palette with the active Omarchy theme and reloads configuration when the theme changes. |
| [**themuuln/herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync) | Syncs Herdr TUI colors to the active Ghostty theme and restores sidebar tokens after server restarts. |
| [**Austinsuyoyo/herdr-autoreload**](https://github.com/Austinsuyoyo/herdr-autoreload) | Reloads the Herdr TUI configuration when `config.toml` changes and displays diagnostics for rejected edits. |
| [**macintacos/herdr-reshape**](https://github.com/macintacos/herdr-reshape) | Moves the focused pane around its tab and arranges panes into an even grid. |
| [**GranamyrBR/ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr) | Shows live agent activity and offers pane controls in Herdr. |
| [**hitaishi2222/herdr-llama**](https://github.com/hitaishi2222/herdr-llama) | Controls llama-server models and lifecycle from Herdr TUI and shows server and token-rate status. |
| [**abelfubu/herdr-popup**](https://github.com/abelfubu/herdr-popup) | Opens ad-hoc shell commands in Herdr TUI popup panes from a keybinding, CLI or agent tool. |
| [**scheron/herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep) | Adds a herdr plugin that puts your Mac to sleep once no coding agent is working any more. Arm it before bed and it waits for every agent to settle, then journals what each one was doing, including the ones that ended up blocked. |
| [**alexanderop/prefix-dojo**](https://github.com/alexanderop/prefix-dojo) | Teaches tmux and Herdr TUI workflows through interactive lessons and timed drills in a simulated terminal. |
| [**WorksOnMyVM/herdr-sounds**](https://github.com/WorksOnMyVM/herdr-sounds) | Discovers, previews, installs, and switches Herdr notification sound packs. |
| [**nkwork9999/ayatsumugi · integrations/herdr**](https://github.com/nkwork9999/ayatsumugi/tree/HEAD/integrations/herdr) | Opens a React DOM and application-state inspector in a Herdr TUI pane and checks the runtime; a private sidecar is required. |
| [**benbrackenbury/herder-zsh-refresh**](https://github.com/benbrackenbury/herder-zsh-refresh) | Refreshes idle zsh panes in Herdr TUI after shell configuration changes while leaving running foreground programs alone. |
| [**islee23520/herdr-omo-agent**](https://github.com/islee23520/herdr-omo-agent) | Registers OmO sessions as coding agents on stock Herdr TUI 0.8.2; the author’s OmO-native fork does not need this package. |
| [**brenzim/herdr-db**](https://github.com/brenzim/herdr-db) | Opens lazysql in Herdr with database connection discovery for the current project. |
| [**asumaran/asdemokit**](https://github.com/asumaran/asdemokit) | Records the README demo GIFs of herdr plugins (asciinema + agg, scripted against an isolated herdr session). |
| [**aneym/herdr-gcal**](https://github.com/aneym/herdr-gcal) | Shows a Google Calendar agenda, month grid, event previews, and calendar toggles in an fzf-driven Herdr TUI panel. |
| [**aneym/cull**](https://github.com/aneym/cull) | Shows macOS compute use in a menu bar monitor and helps terminate processes, including those attributed to Herdr sessions. |
| [**tamdogood/herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow) | Prompts the focused agent to create or merge the current branch’s pull request through a Herdr TUI action. |
| [**carellano/herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers) | Detects development servers running in Herdr panes, records their ports and process state, and can focus or safely stop orphaned services. |
| [**AsgardMuninn/herdr-plugin-orbstack**](https://github.com/AsgardMuninn/herdr-plugin-orbstack) | Creates and manages OrbStack Linux virtual machines as Herdr workspaces, using native shell attachment with SSH fallback and synchronized state. |
| [**iQua/herdr-flakes**](https://github.com/iQua/herdr-flakes) | Mirrors and controls Flakes runs from a local Herdr session. |
| [**tigorlazuardi/herdr-claude-retry**](https://github.com/tigorlazuardi/herdr-claude-retry) | Detects Claude usage-limit banners and resumes Herdr TUI panes when the limit resets. |
| [**wenPKtalk/herdr-translate**](https://github.com/wenPKtalk/herdr-translate) | Translates selected Herdr TUI pane text with translate-shell and displays the result in a popup. |
| [**cndreisbach/herdr-gitu**](https://github.com/cndreisbach/herdr-gitu) | Opens the gitu Git client in a Herdr TUI split or tab with toggle-to-close shortcuts. |
| [**MartinKei/herdr-tab-notes**](https://github.com/MartinKei/herdr-tab-notes) | Opens a popup editor for notes stored separately for each Herdr TUI tab. |
| [**kedwards/herdr-awst**](https://github.com/kedwards/herdr-awst) | Selects AWS profiles and opens awst connections from Herdr TUI while showing account and instance details. |
| [**spywhere/herdr-now-playing**](https://github.com/spywhere/herdr-now-playing) | Adds a music player and playback controls through Herdr keybindings. |
| [**cxnmai/dms-herdr-plugin**](https://github.com/cxnmai/dms-herdr-plugin) | A DankMaterialShell widget for viewing Herdr agent states and accessing basic controls from the desktop shell. |
| [**calorie/herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus) | Focuses the Herdr agent needing attention after the computer has been idle. |
| [**miya10kei/herdr-plugin-sidebar**](https://github.com/miya10kei/herdr-plugin-sidebar) | Displays Google Calendar events and GitHub Actions run status in a split pane styled as a sidebar. |
| [**mougua/herdr-reasonix**](https://github.com/mougua/herdr-reasonix) | Detects Reasonix agents and displays their status correctly. |
| [**ArtMoreno/herdr-glance**](https://github.com/ArtMoreno/herdr-glance) | Provides a live agent dashboard for Herdr, with five themes and a fast prompt segment. |
| [**corygforsythe/herdr-flight-radar**](https://github.com/corygforsythe/herdr-flight-radar) | Provides real-time ADS-B flight radar TUI backed by dump1090. |
| [**fantoine/herdr-run-targets**](https://github.com/fantoine/herdr-run-targets) | Opens a Herdr TUI dashboard to start, stop, and restart repository-defined development services in named tabs. |
| [**tmastalirsch/herdr-workspace-board**](https://github.com/tmastalirsch/herdr-workspace-board) | Provides one line per git repository with unfinished work, ranked by how likely it is to be forgotten. |
| [**m2selfA/herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter) | Sets a Herdr TUI pane name and agent alias through a quick input or a menu of recent names and presets. |
| [**klukacin/herdr-finder-reveal**](https://github.com/klukacin/herdr-finder-reveal) | Reveals OSC 8-linked local file paths from Herdr TUI panes in macOS Finder. |
| [**hellower/herdr-plugin-parallax**](https://github.com/hellower/herdr-plugin-parallax) | Opens URLs from Herdr terminal panes in the Parallax browser. |
| [**skinp/herdr-cwd-control**](https://github.com/skinp/herdr-cwd-control) | Provides a herdr plugin for enhanced control over initial working directory for new workspaces, tabs & panes. |
| [**shanefully-done/herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer) | Equalizes Herdr TUI pane dimensions automatically or through manual width and height actions. |
| [**choplin/herdr-split-pane**](https://github.com/choplin/herdr-split-pane) | Opens a caller-provided command directly in a Herdr split pane. |
| [**atomsbaza/herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin) | Runs an on-demand iOS build and test from a Herdr TUI pane and records a simulator screenshot on failure. |
| [**tobi404/herdr-share-session**](https://github.com/tobi404/herdr-share-session) | Provides one-click view-only tmux session sharing between Macs (Mac 2 shares read-only, Mac 1 drives over SSH). |
| [**n-jc/herdr-opencode**](https://github.com/n-jc/herdr-opencode) | Provides a set up to use Opencode within Apple Containers as a sandbox and manage via Herdr on a Mac OS host machine. |
| [**gaiagent0/ct304-hermes-bots**](https://github.com/gaiagent0/ct304-hermes-bots) | Provides a Hermes bot network coordinating agents across Herdr workspaces with capability-based model distribution. |
| [**kody-w/rapp-herdr**](https://github.com/kody-w/rapp-herdr) | Manages RAPP Twin neighborhoods as supervised Herdr workspaces. |
| [**andrewmcodes/overhrd**](https://github.com/andrewmcodes/overhrd) | Provides a Procfile process manager for herdr users, a herdr-backed reimplementation of Overmind. |
| [**Wyatth7/herdr**](https://github.com/Wyatth7/herdr) | Provides a collection of Herdr configurations and reusable plugins. |
| [**paddock-sh/paddock-herdr**](https://github.com/paddock-sh/paddock-herdr) | Provides a Herdr integration plugin for the Paddock platform. |
| [**AndresDiagoM/herdr-wsl-tab**](https://github.com/AndresDiagoM/herdr-wsl-tab) | Opens a Herdr tab or split that runs a WSL distro on Windows, starting in the focused pane's directory, and passes the `HERDR_*` variables through so Claude Code, Codex, or opencode inside WSL can drive Herdr. Restores those panes after a Herdr restart, and an optional setup action installs Claude Code hooks so the session shows its state. |
| [**leddt/plasma-cliamp**](https://github.com/leddt/plasma-cliamp) | Adds a Plasma 6 panel widget that controls cliamp and attaches to its Herdr TUI session. |

### Setup, packages, and version management

*37 projects. Guides, configuration bundles, installers, package definitions, and tools for reproducible Herdr environments.*

| Project | What it does |
|---|---|
| [**mifunedev/agro**](https://github.com/mifunedev/agro) | Runs Herdr inside a Docker workspace for coding agents on a laptop or remote VM, installed with `agro tool install herdr`. Parallel agents use separate git worktrees, work continues after the terminal disconnects, and you choose the harness: Claude Code, Codex, Pi, OpenCode, or T3 Code. |
| [**joeseesun/herdr-guide**](https://github.com/joeseesun/herdr-guide) | A Chinese-language practical guide that explains what Herdr is useful for and how to get started. |
| [**Yassimba/loom**](https://github.com/Yassimba/loom) | A curated collection of agent skills, Pi packages, and Herdr plugins with a single command-line setup tool. |
| [**diegopzz/herdr-updater**](https://github.com/diegopzz/herdr-updater) | Keeps Herdr and its plugins current across a whole fleet, safely. |
| [**garavitgabriel/claude-remote-kit**](https://github.com/garavitgabriel/claude-remote-kit) | Sets up Herdr, Tailscale, and Termius for remotely accessing coding agent sessions from a phone. |
| [**pedrogiroldo/agentbox**](https://github.com/pedrogiroldo/agentbox) | Runs Herdr, Claude Code, Codex, OpenCode, and mobile-friendly Neovim in an Ubuntu container reachable over SSH. |
| [**ram4-dev/herdr-config**](https://github.com/ram4-dev/herdr-config) | Installs pinned Herdr TUI plugins and portable keybindings with configuration snapshots and rollback. |
| [**hdosys/herdr-sandbox**](https://github.com/hdosys/herdr-sandbox) | Runs coding agents in disposable Windows Sandbox workstations isolated from the host. |
| [**kevinpita/herdr-nix**](https://github.com/kevinpita/herdr-nix) | Installs Nix packages for the Herdr app, herdr-core, and Herdr TUI, with Home Manager and NixOS modules for the TUI. |
| [**Ra77a3l3-jar/herdnix**](https://github.com/Ra77a3l3-jar/herdnix) | Installs Herdr plugins and configuration through a Nix module. |
| [**sohilladhani/tmux2herdr**](https://github.com/sohilladhani/tmux2herdr) | Converts tmux 3.x configuration to Herdr TUI configuration and reports unsupported or partially translated settings. |
| [**GoldenBerry-SO/devbox**](https://github.com/GoldenBerry-SO/devbox) | Provisions a Hetzner development server with Ansible and Herdr TUI for persistent remote agent sessions. |
| [**nklmilojevic/herdr-flake**](https://github.com/nklmilojevic/herdr-flake) | Installs official Herdr TUI release binaries with a Nix flake and optional Home Manager module. |
| [**AodhanHayter/herdr-nix**](https://github.com/AodhanHayter/herdr-nix) | A Nix flake for installing Herdr on Intel and ARM macOS or Linux, with automated upstream release tracking and a Cachix binary cache. |
| [**lachieh/vfox-herdr**](https://github.com/lachieh/vfox-herdr) | Installs stable or preview Herdr TUI releases through mise with checksum verification and shell completions. |
| [**patdx/sido-askpass**](https://github.com/patdx/sido-askpass) | Opens a temporary Herdr TUI pane for sudo password prompts when an agent lacks an interactive TTY. |
| [**conda-forge/herdr-feedstock**](https://github.com/conda-forge/herdr-feedstock) | Packages Herdr TUI for installation through conda-forge. |
| [**orange4664/herdr-remote-workspace**](https://github.com/orange4664/herdr-remote-workspace) | Runs Herdr locally while agents work on an SSH host with Mutagen-synchronized projects. |
| [**giannisp09/herdr-tailscale-setup**](https://github.com/giannisp09/herdr-tailscale-setup) | Sets up a Linux VM to keep Herdr coding-agent sessions running remotely over Tailscale. |
| [**narrowstacks/pxe-agent-box**](https://github.com/narrowstacks/pxe-agent-box) | Creates a configurable Proxmox Debian development VM with a persistent Herdr TUI session, coding agents, and remote access tools. |
| [**jedarden/agentists-quickstart**](https://github.com/jedarden/agentists-quickstart) | Bootstraps a headless server with Herdr TUI, Claude Code, and Codex, then starts the selected agent in a persistent session. |
| [**barnuri/herdr-auto-update**](https://github.com/barnuri/herdr-auto-update) | Keeps herdr always up to date, auto patch/minor/major updates with live handoff. |
| [**Production-Grade/herdr-setup**](https://github.com/Production-Grade/herdr-setup) | Offers a reusable Herdr TUI starter configuration, team workspace conventions, and a first-session walkthrough. |
| [**adams100111/omarchy-themed-devtools**](https://github.com/adams100111/omarchy-themed-devtools) | Applies Omarchy theme colors to Herdr TUI and other command-line tools. |
| [**maxart/uniterm-benchmark**](https://github.com/maxart/uniterm-benchmark) | Benchmarks Herdr TUI, Uniterm, and optionally tmux with equivalent terminal workloads and reproducible reports. |
| [**latest-debs/herdr-debian**](https://github.com/latest-debs/herdr-debian) | Packages Herdr TUI for Debian as a `.deb`. |
| [**spr-networks/spr-herdr**](https://github.com/spr-networks/spr-herdr) | Runs a Herdr TUI inside an SPR-managed KVM microVM. |
| [**hao-github-0216/remote-workspace-setup**](https://github.com/hao-github-0216/remote-workspace-setup) | Sets up persistent remote Herdr TUI workspaces over SSH and Mosh, including recovery after reboot. |
| [**YiannisDermitzakis/herdr-setup**](https://github.com/YiannisDermitzakis/herdr-setup) | Copies and synchronizes Herdr TUI configuration across machines and prepares coding agents for session restoration. |
| [**harveyfullstack/herdr-dist**](https://github.com/harveyfullstack/herdr-dist) | Distributes a pinned Herdr TUI Linux binary for the Box runtime. |
| [**yigitkonur/herdr-wezterm-setup**](https://github.com/yigitkonur/herdr-wezterm-setup) | A macOS terminal configuration that uses Herdr as the multiplexer and WezTerm as the keyboard-routing layer. |
| [**DavidTWhitlatch/dotfiles-template**](https://github.com/DavidTWhitlatch/dotfiles-template) | A shareable macOS dotfiles template with zsh, Oh My Zsh, Oh My Posh, Herdr, Git template hooks, and a symlink-based setup. |
| [**chrisjohnson/asdf-herdr**](https://github.com/chrisjohnson/asdf-herdr) | Installs and switches Herdr TUI versions with asdf using prebuilt macOS and Linux binaries. |
| [**ccyisafool/herdr-terminal**](https://github.com/ccyisafool/herdr-terminal) | Provides a thin, branded Ghostty client that starts Herdr by default. |
| [**2lab-ai/homebrew-tap · Formula**](https://github.com/2lab-ai/homebrew-tap/tree/main/Formula) | Installs the Herdr-derived herdr-mx distribution through Homebrew stable and preview formulae. |
| [**RobLoach/asdf-herdr**](https://github.com/RobLoach/asdf-herdr) | Installs Herdr TUI releases with asdf, including explicitly selected preview builds. |
| [**shaiu/ha-herdr**](https://github.com/shaiu/ha-herdr) | Runs a Herdr server with Claude Code as a Home Assistant app (formerly add-on), so the HA box appears as a saved SSH machine in your Herdr client. Includes key-only SSH, an ingress panel attached to the same session, and Home Assistant tools through ha-mcp. |

---

## 8. Experimental projects

*9 projects. Experimental Herdr projects and prototypes.*

### Experiments, concepts, and scaffolds

*9 projects. Ideas and prototypes that are useful to study but may be incomplete, read-only, or not yet installable.*

| Project | What it does |
|---|---|
| [**eliasstravik/herdr-call**](https://github.com/eliasstravik/herdr-call) | An early TypeScript prototype for translating spoken commands into Herdr navigation and input through the local socket. |
| [**wraithyy/herdr-openr**](https://github.com/wraithyy/herdr-openr) | Extracts file paths and URLs from recent pane output and Claude Code transcripts, then presents them in a fuzzy finder for quick opening. |
| [**hmu332233/herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs) | An experimental plugin laboratory containing early prototypes for agent launching, workspace metrics, and worktree symlinking before they move into separate projects. |
| [**rohanthewiz/herdr-web**](https://github.com/rohanthewiz/herdr-web) | Renders Herdr pane frames with color, mouse, clipboard, and hyperlink support; keyboard and paste input are currently disabled, so it mainly works as a viewer. |
| [**shoaibkhanz/herdr-nav-plus**](https://github.com/shoaibkhanz/herdr-nav-plus) | An early navigation plugin designed to move with Ctrl+h/j/k/l across Herdr panes and wrap at workspace boundaries. |
| [**ugurtarlig/herdr-pane-picker**](https://github.com/ugurtarlig/herdr-pane-picker) | An early pane-picker prototype that overlays one-character hints on visible panes for direct keyboard focus. |
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

## Reference

- **Agent guides:** Point an agent at `~/.config/herdr-app/AGENTS.md` (Herdr app), `hc --skill` (herdr-core), or `SKILL.md` (Herdr TUI) before asking it to change anything.
- **Agent status:** herdr-core reads working, done, and blocked states from programs that emit OSC 7501, the Program Status Protocol: `printf '\e]7501;state=blocked:app=my-agent\e\\'`.
- **Socket client:** Herdr TUI listens on `$XDG_CONFIG_HOME/herdr/herdr.sock` (default `~/.config/herdr/herdr.sock`) for newline-delimited JSON commands that manage tabs, panes, and agents.
- **Git worktrees:** Pair Herdr tabs with isolated git worktrees (`git worktree add`) to run concurrent agents safely.
