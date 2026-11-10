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

1. [Run and orchestrate agents (592)](#1-run-and-orchestrate-agents)
   - [Official Herdr projects and skill (5)](catalog/01-run-and-orchestrate.md#official-herdr-projects-and-skill)
   - [Skills that teach agents to operate Herdr (10)](catalog/01-run-and-orchestrate.md#skills-that-teach-agents-to-operate-herdr)
   - [Orchestration skills for lead agents (26)](catalog/01-run-and-orchestrate.md#orchestration-skills-for-lead-agents)
   - [Lead-agent coordinators with worker tabs (30)](catalog/01-run-and-orchestrate.md#lead-agent-coordinators-with-worker-tabs)
   - [Fleet control planes and CLI harnesses (40)](catalog/01-run-and-orchestrate.md#fleet-control-planes-and-cli-harnesses)
   - [Role-based agent teams with planners and reviewers (28)](catalog/01-run-and-orchestrate.md#role-based-agent-teams-with-planners-and-reviewers)
   - [Agent team definitions and role profiles (10)](catalog/01-run-and-orchestrate.md#agent-team-definitions-and-role-profiles)
   - [Swarm orchestrators for parallel agent waves (8)](catalog/01-run-and-orchestrate.md#swarm-orchestrators-for-parallel-agent-waves)
   - [Live panes for native Claude Code, Codex and OpenCode subagents (10)](catalog/01-run-and-orchestrate.md#live-panes-for-native-claude-code-codex-and-opencode-subagents)
   - [Task delegation to other coding agents (24)](catalog/01-run-and-orchestrate.md#task-delegation-to-other-coding-agents)
   - [Task routers that pick the agent and model (8)](catalog/01-run-and-orchestrate.md#task-routers-that-pick-the-agent-and-model)
   - [Popup pickers that launch a coding agent in a new tab (16)](catalog/01-run-and-orchestrate.md#popup-pickers-that-launch-a-coding-agent-in-a-new-tab)
   - [Scripts that spawn grids of agents in worktrees (7)](catalog/01-run-and-orchestrate.md#scripts-that-spawn-grids-of-agents-in-worktrees)
   - [Sending agent tasks to other machines and clusters (4)](catalog/01-run-and-orchestrate.md#sending-agent-tasks-to-other-machines-and-clusters)
   - [Handoffs of work and context between agent panes (6)](catalog/01-run-and-orchestrate.md#handoffs-of-work-and-context-between-agent-panes)
   - [Terminal dashboards and mission-control tabs for agent fleets (23)](catalog/01-run-and-orchestrate.md#terminal-dashboards-and-mission-control-tabs-for-agent-fleets)
   - [Side panels with worktree, PR and diff cards per agent (6)](catalog/01-run-and-orchestrate.md#side-panels-with-worktree-pr-and-diff-cards-per-agent)
   - [Durable mailboxes and message queues for agents (13)](catalog/01-run-and-orchestrate.md#durable-mailboxes-and-message-queues-for-agents)
   - [Peer messaging, mentions and relays between agent panes (12)](catalog/01-run-and-orchestrate.md#peer-messaging-mentions-and-relays-between-agent-panes)
   - [Shared chat rooms and group channels for agent teams (8)](catalog/01-run-and-orchestrate.md#shared-chat-rooms-and-group-channels-for-agent-teams)
   - [Agent networks and meshes across machines and people (9)](catalog/01-run-and-orchestrate.md#agent-networks-and-meshes-across-machines-and-people)
   - [Human-decision queues for blocked agents (6)](catalog/01-run-and-orchestrate.md#human-decision-queues-for-blocked-agents)
   - [Second-opinion reviewers in a split pane (9)](catalog/01-run-and-orchestrate.md#second-opinion-reviewers-in-a-split-pane)
   - [Writer and reviewer agent pairs (7)](catalog/01-run-and-orchestrate.md#writer-and-reviewer-agent-pairs)
   - [Consensus and judge panels of several agents (4)](catalog/01-run-and-orchestrate.md#consensus-and-judge-panels-of-several-agents)
   - [Pull-request review dispatchers (4)](catalog/01-run-and-orchestrate.md#pull-request-review-dispatchers)
   - [Agent races and side-by-side comparisons (5)](catalog/01-run-and-orchestrate.md#agent-races-and-side-by-side-comparisons)
   - [Workflow engines and scripted agent pipelines (12)](catalog/01-run-and-orchestrate.md#workflow-engines-and-scripted-agent-pipelines)
   - [Spec-driven and SDLC process frameworks (6)](catalog/01-run-and-orchestrate.md#spec-driven-and-sdlc-process-frameworks)
   - [Autonomous coding loops that end in pull requests (11)](catalog/01-run-and-orchestrate.md#autonomous-coding-loops-that-end-in-pull-requests)
   - [Tracker-driven agent factories (14)](catalog/01-run-and-orchestrate.md#tracker-driven-agent-factories)
   - [Herdr TUI plugins that turn Linear issues into agent runs (7)](catalog/01-run-and-orchestrate.md#herdr-tui-plugins-that-turn-linear-issues-into-agent-runs)
   - [Herdr TUI Jira boards and ticket launchers (9)](catalog/01-run-and-orchestrate.md#herdr-tui-jira-boards-and-ticket-launchers)
   - [Herdr TUI GitHub issue and pull-request browsers that start agents (7)](catalog/01-run-and-orchestrate.md#herdr-tui-github-issue-and-pull-request-browsers-that-start-agents)
   - [GitLab, ClickUp, Shortcut, Notion and other tracker clients (11)](catalog/01-run-and-orchestrate.md#gitlab-clickup-shortcut-notion-and-other-tracker-clients)
   - [Kanban boards that dispatch agents (11)](catalog/01-run-and-orchestrate.md#kanban-boards-that-dispatch-agents)
   - [Shared task boards for people and agents (10)](catalog/01-run-and-orchestrate.md#shared-task-boards-for-people-and-agents)
   - [Task claims and ledgers that agents share (9)](catalog/01-run-and-orchestrate.md#task-claims-and-ledgers-that-agents-share)
   - [Beads task tracker integrations (4)](catalog/01-run-and-orchestrate.md#beads-task-tracker-integrations)
   - [Scheduled agent routines and cron jobs (15)](catalog/01-run-and-orchestrate.md#scheduled-agent-routines-and-cron-jobs)
   - [Prompt queues and delayed prompt delivery (11)](catalog/01-run-and-orchestrate.md#prompt-queues-and-delayed-prompt-delivery)
   - [Event triggers and agent wake-ups (7)](catalog/01-run-and-orchestrate.md#event-triggers-and-agent-wake-ups)
   - [Queued task runners with review gates (7)](catalog/01-run-and-orchestrate.md#queued-task-runners-with-review-gates)
   - [Usage-limit auto-resume and retry (9)](catalog/01-run-and-orchestrate.md#usage-limit-auto-resume-and-retry)
   - [Claude Code and Codex login switchers and auth monitors (9)](catalog/01-run-and-orchestrate.md#claude-code-and-codex-login-switchers-and-auth-monitors)
   - [Context compaction and agent memory (4)](catalog/01-run-and-orchestrate.md#context-compaction-and-agent-memory)
   - [Pi subagent tools that return results to the parent session (24)](catalog/01-run-and-orchestrate.md#pi-subagent-tools-that-return-results-to-the-parent-session)
   - [Pi foremen and crews that coordinate and supervise several workers (24)](catalog/01-run-and-orchestrate.md#pi-foremen-and-crews-that-coordinate-and-supervise-several-workers)
   - [Pi planner, coder and reviewer teams (11)](catalog/01-run-and-orchestrate.md#pi-planner-coder-and-reviewer-teams)
   - [Pi extensions that control Herdr (8)](catalog/01-run-and-orchestrate.md#pi-extensions-that-control-herdr)
   - [Pi sidebars, trees and subagent viewers (5)](catalog/01-run-and-orchestrate.md#pi-sidebars-trees-and-subagent-viewers)
   - [Oh My Pi orchestration and viewers (9)](catalog/01-run-and-orchestrate.md#oh-my-pi-orchestration-and-viewers)
2. [Herdr app layouts, mods, and themes (781)](#2-herdr-app-layouts-mods-and-themes)
   - [Herdr app multi-layout packs (11)](catalog/02-herdr-app.md#herdr-app-multi-layout-packs)
   - [Herdr app multi-mod bundles and personal collections (29)](catalog/02-herdr-app.md#herdr-app-multi-mod-bundles-and-personal-collections)
   - [Herdr app status-column boards such as Needs you, Working and Done (7)](catalog/02-herdr-app.md#herdr-app-status-column-boards-such-as-needs-you-working-and-done)
   - [Herdr app multi-agent orchestration and supervisor panels (19)](catalog/02-herdr-app.md#herdr-app-multi-agent-orchestration-and-supervisor-panels)
   - [Herdr app Spaces sidebars with worktrees, branches and agent status (17)](catalog/02-herdr-app.md#herdr-app-spaces-sidebars-with-worktrees-branches-and-agent-status)
   - [Herdr app one-list sidebars merging Spaces, tabs and agents (11)](catalog/02-herdr-app.md#herdr-app-one-list-sidebars-merging-spaces-tabs-and-agents)
   - [Herdr app sidebars grouped by machine and host (8)](catalog/02-herdr-app.md#herdr-app-sidebars-grouped-by-machine-and-host)
   - [Herdr app compact sidebar and borderless window layouts (15)](catalog/02-herdr-app.md#herdr-app-compact-sidebar-and-borderless-window-layouts)
   - [Herdr app layouts with built-in usage and system panels (6)](catalog/02-herdr-app.md#herdr-app-layouts-with-built-in-usage-and-system-panels)
   - [Herdr app layouts that look like a code editor (14)](catalog/02-herdr-app.md#herdr-app-layouts-that-look-like-a-code-editor)
   - [Herdr app layouts with Files, Changes and Git panels (15)](catalog/02-herdr-app.md#herdr-app-layouts-with-files-changes-and-git-panels)
   - [Herdr app dark and monochrome minimal layouts (9)](catalog/02-herdr-app.md#herdr-app-dark-and-monochrome-minimal-layouts)
   - [Herdr app layouts in named color palettes such as Catppuccin, Nord and Dracula (20)](catalog/02-herdr-app.md#herdr-app-layouts-in-named-color-palettes-such-as-catppuccin-nord-and-dracula)
   - [Herdr app glass, islands and floating-card layouts (12)](catalog/02-herdr-app.md#herdr-app-glass-islands-and-floating-card-layouts)
   - [Herdr app layouts that imitate other desktops, apps and devices (19)](catalog/02-herdr-app.md#herdr-app-layouts-that-imitate-other-desktops-apps-and-devices)
   - [Herdr app cyberpunk, sci-fi and anime layouts (21)](catalog/02-herdr-app.md#herdr-app-cyberpunk-sci-fi-and-anime-layouts)
   - [Herdr app pixel-art RPG, retro game and franchise layouts (13)](catalog/02-herdr-app.md#herdr-app-pixel-art-rpg-retro-game-and-franchise-layouts)
   - [Herdr app pixel-art offices, buildings and coworker scenes (12)](catalog/02-herdr-app.md#herdr-app-pixel-art-offices-buildings-and-coworker-scenes)
   - [Herdr app animated pets, creatures and farm scenes (16)](catalog/02-herdr-app.md#herdr-app-animated-pets-creatures-and-farm-scenes)
   - [Herdr app airport, sports and ship scene layouts (9)](catalog/02-herdr-app.md#herdr-app-airport-sports-and-ship-scene-layouts)
   - [Herdr app automatic tab and space namers (15)](catalog/02-herdr-app.md#herdr-app-automatic-tab-and-space-namers)
   - [Herdr app space folders, groups and tab groups (17)](catalog/02-herdr-app.md#herdr-app-space-folders-groups-and-tab-groups)
   - [Herdr app space icons, avatars and sidebar branding (8)](catalog/02-herdr-app.md#herdr-app-space-icons-avatars-and-sidebar-branding)
   - [Herdr app pane headers, terminal IDs and agent labels (10)](catalog/02-herdr-app.md#herdr-app-pane-headers-terminal-ids-and-agent-labels)
   - [Herdr app closing, pinning and archiving spaces and tabs (11)](catalog/02-herdr-app.md#herdr-app-closing-pinning-and-archiving-spaces-and-tabs)
   - [Herdr app interface tweaks and translations (7)](catalog/02-herdr-app.md#herdr-app-interface-tweaks-and-translations)
   - [Herdr app inboxes of agents waiting on you (21)](catalog/02-herdr-app.md#herdr-app-inboxes-of-agents-waiting-on-you)
   - [Herdr app desktop and phone alerts for finished agents (5)](catalog/02-herdr-app.md#herdr-app-desktop-and-phone-alerts-for-finished-agents)
   - [Herdr app go-to popups and number shortcuts for spaces, tabs and agents (7)](catalog/02-herdr-app.md#herdr-app-go-to-popups-and-number-shortcuts-for-spaces-tabs-and-agents)
   - [Herdr app pane focus, movement and resize keys (12)](catalog/02-herdr-app.md#herdr-app-pane-focus-movement-and-resize-keys)
   - [Herdr app dialogs that open a repository or branch as a new space (12)](catalog/02-herdr-app.md#herdr-app-dialogs-that-open-a-repository-or-branch-as-a-new-space)
   - [Herdr app docks, floating terminals and command launchers (12)](catalog/02-herdr-app.md#herdr-app-docks-floating-terminals-and-command-launchers)
   - [Herdr app agent restart, resume and session restore (12)](catalog/02-herdr-app.md#herdr-app-agent-restart-resume-and-session-restore)
   - [Herdr app past-session search and history browsers (6)](catalog/02-herdr-app.md#herdr-app-past-session-search-and-history-browsers)
   - [Herdr app plan-usage gauges in the status bar (16)](catalog/02-herdr-app.md#herdr-app-plan-usage-gauges-in-the-status-bar)
   - [Herdr app per-provider quota panels and Claude account switchers (16)](catalog/02-herdr-app.md#herdr-app-per-provider-quota-panels-and-claude-account-switchers)
   - [Herdr app token, cost and context usage dashboards (10)](catalog/02-herdr-app.md#herdr-app-token-cost-and-context-usage-dashboards)
   - [Herdr app machine vitals and resource monitors (7)](catalog/02-herdr-app.md#herdr-app-machine-vitals-and-resource-monitors)
   - [Herdr app live diagrams of agents and their helpers (10)](catalog/02-herdr-app.md#herdr-app-live-diagrams-of-agents-and-their-helpers)
   - [Herdr app chat views for agent terminals (7)](catalog/02-herdr-app.md#herdr-app-chat-views-for-agent-terminals)
   - [Herdr app prompt history, turn summaries and agent timelines (9)](catalog/02-herdr-app.md#herdr-app-prompt-history-turn-summaries-and-agent-timelines)
   - [Herdr app Git sidebar for staging, stashing and branch switching (15)](catalog/02-herdr-app.md#herdr-app-git-sidebar-for-staging-stashing-and-branch-switching)
   - [Herdr app branch-graph overlays with merge and rebase actions (5)](catalog/02-herdr-app.md#herdr-app-branch-graph-overlays-with-merge-and-rebase-actions)
   - [Herdr app code-review panes with inline comments and threads (21)](catalog/02-herdr-app.md#herdr-app-code-review-panes-with-inline-comments-and-threads)
   - [Herdr app Plannotator, Roborev and plan-review panes (7)](catalog/02-herdr-app.md#herdr-app-plannotator-roborev-and-plan-review-panes)
   - [Herdr app GitHub and GitLab pull request panels (17)](catalog/02-herdr-app.md#herdr-app-github-and-gitlab-pull-request-panels)
   - [Herdr app worktree setup and per-worktree helpers (7)](catalog/02-herdr-app.md#herdr-app-worktree-setup-and-per-worktree-helpers)
   - [Herdr app file explorers and Files panel upgrades (13)](catalog/02-herdr-app.md#herdr-app-file-explorers-and-files-panel-upgrades)
   - [Herdr app Markdown readers and file previewers (14)](catalog/02-herdr-app.md#herdr-app-markdown-readers-and-file-previewers)
   - [Herdr app file and content search dialogs (4)](catalog/02-herdr-app.md#herdr-app-file-and-content-search-dialogs)
   - [Herdr app editors and open-in-editor actions (8)](catalog/02-herdr-app.md#herdr-app-editors-and-open-in-editor-actions)
   - [Herdr app note-taking panes and scratchpads (9)](catalog/02-herdr-app.md#herdr-app-note-taking-panes-and-scratchpads)
   - [Herdr app embedded browsers and window viewers (5)](catalog/02-herdr-app.md#herdr-app-embedded-browsers-and-window-viewers)
   - [Herdr app diagram, drawing and generated-UI panes (5)](catalog/02-herdr-app.md#herdr-app-diagram-drawing-and-generated-ui-panes)
   - [Herdr app copy, quote, selection and dictation helpers (12)](catalog/02-herdr-app.md#herdr-app-copy-quote-selection-and-dictation-helpers)
   - [Herdr app Linear issue panels (7)](catalog/02-herdr-app.md#herdr-app-linear-issue-panels)
   - [Herdr app GitHub, Jira and self-hosted issue panels (10)](catalog/02-herdr-app.md#herdr-app-github-jira-and-self-hosted-issue-panels)
   - [Herdr app spec, plan-file and ticket-file panels (8)](catalog/02-herdr-app.md#herdr-app-spec-plan-file-and-ticket-file-panels)
   - [Herdr app project task boards and to-do lists (13)](catalog/02-herdr-app.md#herdr-app-project-task-boards-and-to-do-lists)
   - [Herdr app deployment, CI and monitoring panels (7)](catalog/02-herdr-app.md#herdr-app-deployment-ci-and-monitoring-panels)
   - [Herdr app container, database and cloud browsers (8)](catalog/02-herdr-app.md#herdr-app-container-database-and-cloud-browsers)
   - [Herdr app task runners, simulators and device launchers (5)](catalog/02-herdr-app.md#herdr-app-task-runners-simulators-and-device-launchers)
   - [Herdr app dialogs for connecting spaces to other machines (7)](catalog/02-herdr-app.md#herdr-app-dialogs-for-connecting-spaces-to-other-machines)
   - [Herdr app panels for design, API and developer tools (8)](catalog/02-herdr-app.md#herdr-app-panels-for-design-api-and-developer-tools)
   - [Herdr app listening-port viewers (4)](catalog/02-herdr-app.md#herdr-app-listening-port-viewers)
   - [Herdr app now-playing bars and media players (6)](catalog/02-herdr-app.md#herdr-app-now-playing-bars-and-media-players)
   - [Herdr app games, timers and break-time extras (6)](catalog/02-herdr-app.md#herdr-app-games-timers-and-break-time-extras)
   - [Herdr app mail, calendar, chat and watchlist panels (11)](catalog/02-herdr-app.md#herdr-app-mail-calendar-chat-and-watchlist-panels)
   - [Herdr app mod managers, updaters and launchers (14)](catalog/02-herdr-app.md#herdr-app-mod-managers-updaters-and-launchers)
   - [Herdr app color themes and theme generators (8)](catalog/02-herdr-app.md#herdr-app-color-themes-and-theme-generators)
   - [Herdr app file-icon themes for the Files panel (4)](catalog/02-herdr-app.md#herdr-app-file-icon-themes-for-the-files-panel)
3. [Connect through MCP and the socket API (322)](#3-connect-through-mcp-and-the-socket-api)
   - [MCP servers for controlling Herdr panes and agents (10)](catalog/03-mcp-and-socket-api.md#mcp-servers-for-controlling-herdr-panes-and-agents)
   - [MCP bridges for ChatGPT, Claude Desktop and web assistants (6)](catalog/03-mcp-and-socket-api.md#mcp-bridges-for-chatgpt-claude-desktop-and-web-assistants)
   - [MCP and ACP adapters for specific agent hosts (4)](catalog/03-mcp-and-socket-api.md#mcp-and-acp-adapters-for-specific-agent-hosts)
   - [Socket API client libraries by language (12)](catalog/03-mcp-and-socket-api.md#socket-api-client-libraries-by-language)
   - [Socket API automation toolkits and drivers (6)](catalog/03-mcp-and-socket-api.md#socket-api-automation-toolkits-and-drivers)
   - [HTTP and WebSocket bridges that expose Herdr (5)](catalog/03-mcp-and-socket-api.md#http-and-websocket-bridges-that-expose-herdr)
   - [Bridges to third-party agent platforms (8)](catalog/03-mcp-and-socket-api.md#bridges-to-third-party-agent-platforms)
   - [Agent-state correctors and background-work markers (9)](catalog/03-mcp-and-socket-api.md#agent-state-correctors-and-background-work-markers)
   - [OpenCode status reporters and bridges (6)](catalog/03-mcp-and-socket-api.md#opencode-status-reporters-and-bridges)
   - [DeepSeek Harness and Reasonix integrations (13)](catalog/03-mcp-and-socket-api.md#deepseek-harness-and-reasonix-integrations)
   - [Pi and Oh My Pi status reporters (8)](catalog/03-mcp-and-socket-api.md#pi-and-oh-my-pi-status-reporters)
   - [Hermes Agent status reporters and Claude Code bridges (4)](catalog/03-mcp-and-socket-api.md#hermes-agent-status-reporters-and-claude-code-bridges)
   - [Hermes Agent workflows, kanban and bot networks (9)](catalog/03-mcp-and-socket-api.md#hermes-agent-workflows-kanban-and-bot-networks)
   - [Command Code, Cline and Freebuff status reporters (5)](catalog/03-mcp-and-socket-api.md#command-code-cline-and-freebuff-status-reporters)
   - [TraeX, MiMo Code, CodeBuddy, ZCode and MiniMax status reporters (9)](catalog/03-mcp-and-socket-api.md#traex-mimo-code-codebuddy-zcode-and-minimax-status-reporters)
   - [Mistral Vibe and Goose status reporters (5)](catalog/03-mcp-and-socket-api.md#mistral-vibe-and-goose-status-reporters)
   - [Status reporters for Amp, Auggie, Junie, Kiro, Rovo Dev and Cortex Code (7)](catalog/03-mcp-and-socket-api.md#status-reporters-for-amp-auggie-junie-kiro-rovo-dev-and-cortex-code)
   - [Jcode status reporters (4)](catalog/03-mcp-and-socket-api.md#jcode-status-reporters)
   - [Status reporters for smaller and open-source agent CLIs (12)](catalog/03-mcp-and-socket-api.md#status-reporters-for-smaller-and-open-source-agent-clis)
   - [Telegram bots for agent alerts (6)](catalog/03-mcp-and-socket-api.md#telegram-bots-for-agent-alerts)
   - [Telegram bots for remote commands and approvals (6)](catalog/03-mcp-and-socket-api.md#telegram-bots-for-remote-commands-and-approvals)
   - [Telegram bridges that map agents to forum topics (6)](catalog/03-mcp-and-socket-api.md#telegram-bridges-that-map-agents-to-forum-topics)
   - [Slack notifications and bots (7)](catalog/03-mcp-and-socket-api.md#slack-notifications-and-bots)
   - [Discord and workplace-messenger bridges (7)](catalog/03-mcp-and-socket-api.md#discord-and-workplace-messenger-bridges)
   - [Two-way chat bridges for several services (7)](catalog/03-mcp-and-socket-api.md#two-way-chat-bridges-for-several-services)
   - [Alert routers that fan out to chat, push and webhooks (5)](catalog/03-mcp-and-socket-api.md#alert-routers-that-fan-out-to-chat-push-and-webhooks)
   - [macOS notification banners (9)](catalog/03-mcp-and-socket-api.md#macos-notification-banners)
   - [Windows and WSL toast notifications (4)](catalog/03-mcp-and-socket-api.md#windows-and-wsl-toast-notifications)
   - [Cross-platform and remote-host desktop notifiers (4)](catalog/03-mcp-and-socket-api.md#cross-platform-and-remote-host-desktop-notifiers)
   - [Persistent popups, inboxes and screen cues for waiting agents (6)](catalog/03-mcp-and-socket-api.md#persistent-popups-inboxes-and-screen-cues-for-waiting-agents)
   - [Agent-done sounds and sound packs (9)](catalog/03-mcp-and-socket-api.md#agent-done-sounds-and-sound-packs)
   - [Spoken summaries and text-to-speech alerts (6)](catalog/03-mcp-and-socket-api.md#spoken-summaries-and-text-to-speech-alerts)
   - [Phone push alerts through ntfy (6)](catalog/03-mcp-and-socket-api.md#phone-push-alerts-through-ntfy)
   - [Phone push through Gotify, Bark and iPhone companion apps (5)](catalog/03-mcp-and-socket-api.md#phone-push-through-gotify-bark-and-iphone-companion-apps)
   - [Webhook, email and hosted-push notifiers (10)](catalog/03-mcp-and-socket-api.md#webhook-email-and-hosted-push-notifiers)
   - [Telemetry exporters and presence feeds (10)](catalog/03-mcp-and-socket-api.md#telemetry-exporters-and-presence-feeds)
   - [Standalone dashboards for agent time, cost and session health (8)](catalog/03-mcp-and-socket-api.md#standalone-dashboards-for-agent-time-cost-and-session-health)
   - [Speech-to-text dictation into panes (10)](catalog/03-mcp-and-socket-api.md#speech-to-text-dictation-into-panes)
   - [Voice assistants and spoken commands at your desk (6)](catalog/03-mcp-and-socket-api.md#voice-assistants-and-spoken-commands-at-your-desk)
   - [Phone calls and phone-based voice control for agents (6)](catalog/03-mcp-and-socket-api.md#phone-calls-and-phone-based-voice-control-for-agents)
   - [Remote access over SSH, Tailscale and QUIC (9)](catalog/03-mcp-and-socket-api.md#remote-access-over-ssh-tailscale-and-quic)
   - [Remote port forwarding, link opening and file transfer (10)](catalog/03-mcp-and-socket-api.md#remote-port-forwarding-link-opening-and-file-transfer)
   - [Browser selections, notes and photos sent to agents (4)](catalog/03-mcp-and-socket-api.md#browser-selections-notes-and-photos-sent-to-agents)
   - [Warp terminal integrations (4)](catalog/03-mcp-and-socket-api.md#warp-terminal-integrations)
   - [cmux integrations (5)](catalog/03-mcp-and-socket-api.md#cmux-integrations)
   - [tmux plugins with Herdr agent detection (5)](catalog/03-mcp-and-socket-api.md#tmux-plugins-with-herdr-agent-detection)
4. [Editor integrations (110)](#4-editor-integrations)
   - [Vim and Neovim pane navigation and focus handling (13)](catalog/04-editors.md#vim-and-neovim-pane-navigation-and-focus-handling)
   - [Edge-aware navigation across tabs, workspaces and resizing (6)](catalog/04-editors.md#edge-aware-navigation-across-tabs-workspaces-and-resizing)
   - [Send Neovim selections, file references and prompts to agents (10)](catalog/04-editors.md#send-neovim-selections-file-references-and-prompts-to-agents)
   - [Prompt editors and Yazi, Helix or lazygit senders for agents (4)](catalog/04-editors.md#prompt-editors-and-yazi-helix-or-lazygit-senders-for-agents)
   - [Neovim dashboards and agent control panels (8)](catalog/04-editors.md#neovim-dashboards-and-agent-control-panels)
   - [Review agent changes and send comments from the editor (8)](catalog/04-editors.md#review-agent-changes-and-send-comments-from-the-editor)
   - [Open paths from pane output in a running editor (10)](catalog/04-editors.md#open-paths-from-pane-output-in-a-running-editor)
   - [Open a Herdr workspace in JetBrains, VS Code, Cursor and other editors (9)](catalog/04-editors.md#open-a-herdr-workspace-in-jetbrains-vs-code-cursor-and-other-editors)
   - [VS Code, Cursor and dev container bridges (8)](catalog/04-editors.md#vs-code-cursor-and-dev-container-bridges)
   - [Zed integrations and workspace sync (7)](catalog/04-editors.md#zed-integrations-and-workspace-sync)
   - [Obsidian vault integrations (4)](catalog/04-editors.md#obsidian-vault-integrations)
   - [Terminal editors hosted in Herdr panes (4)](catalog/04-editors.md#terminal-editors-hosted-in-herdr-panes)
   - [Emacs and Kakoune integrations (6)](catalog/04-editors.md#emacs-and-kakoune-integrations)
   - [REPLs and task runners from the editor (4)](catalog/04-editors.md#repls-and-task-runners-from-the-editor)
   - [Dotfiles, starter kits and editor-plus-Herdr environments (9)](catalog/04-editors.md#dotfiles-starter-kits-and-editor-plus-herdr-environments)
5. [Switch and restore sessions (338)](#5-switch-and-restore-sessions)
   - [Fuzzy jump pickers for workspaces, tabs and agents (16)](catalog/05-sessions.md#fuzzy-jump-pickers-for-workspaces-tabs-and-agents)
   - [Tree and preview navigators for workspaces and panes (10)](catalog/05-sessions.md#tree-and-preview-navigators-for-workspaces-and-panes)
   - [Agent pickers ranked by status and recency (16)](catalog/05-sessions.md#agent-pickers-ranked-by-status-and-recency)
   - [Jump to the next blocked or finished agent (13)](catalog/05-sessions.md#jump-to-the-next-blocked-or-finished-agent)
   - [Last-tab and last-workspace toggles (11)](catalog/05-sessions.md#last-tab-and-last-workspace-toggles)
   - [Focus history, back and forward jumps and recent-pane cyclers (14)](catalog/05-sessions.md#focus-history-back-and-forward-jumps-and-recent-pane-cyclers)
   - [Claude Code session finders and resume pickers (4)](catalog/05-sessions.md#claude-code-session-finders-and-resume-pickers)
   - [Multi-agent conversation search and resume pickers (12)](catalog/05-sessions.md#multi-agent-conversation-search-and-resume-pickers)
   - [Project folder finders that open or focus a workspace (13)](catalog/05-sessions.md#project-folder-finders-that-open-or-focus-a-workspace)
   - [Zoxide directory workspace pickers (7)](catalog/05-sessions.md#zoxide-directory-workspace-pickers)
   - [Git repository and worktree pickers (9)](catalog/05-sessions.md#git-repository-and-worktree-pickers)
   - [Saved project lists and bookmarked directories (4)](catalog/05-sessions.md#saved-project-lists-and-bookmarked-directories)
   - [Directory pickers for new workspaces and tabs (6)](catalog/05-sessions.md#directory-pickers-for-new-workspaces-and-tabs)
   - [Sessionizer-style project launchers with tab templates (5)](catalog/05-sessions.md#sessionizer-style-project-launchers-with-tab-templates)
   - [Shell and tab shortcuts that start or reuse panes (4)](catalog/05-sessions.md#shell-and-tab-shortcuts-that-start-or-reuse-panes)
   - [SSH host, cloud instance and remote machine pickers (14)](catalog/05-sessions.md#ssh-host-cloud-instance-and-remote-machine-pickers)
   - [Named Herdr session managers (6)](catalog/05-sessions.md#named-herdr-session-managers)
   - [Session managers shared across Herdr, tmux, sesh and Zellij (6)](catalog/05-sessions.md#session-managers-shared-across-herdr-tmux-sesh-and-zellij)
   - [Multi-server sidebars that mirror remote Herdr machines (9)](catalog/05-sessions.md#multi-server-sidebars-that-mirror-remote-herdr-machines)
   - [Workspace groups, profiles and focus filters (9)](catalog/05-sessions.md#workspace-groups-profiles-and-focus-filters)
   - [Workspace sorters by name, recent use or category (9)](catalog/05-sessions.md#workspace-sorters-by-name-recent-use-or-category)
   - [Move panes and tabs between workspaces (14)](catalog/05-sessions.md#move-panes-and-tabs-between-workspaces)
   - [Session labels, notes and context locators (7)](catalog/05-sessions.md#session-labels-notes-and-context-locators)
   - [Declarative workspace layouts in YAML, TOML and Lua (12)](catalog/05-sessions.md#declarative-workspace-layouts-in-yaml-toml-and-lua)
   - [tmuxinator-style project launchers (8)](catalog/05-sessions.md#tmuxinator-style-project-launchers)
   - [Saved layout snapshots and screen grids (4)](catalog/05-sessions.md#saved-layout-snapshots-and-screen-grids)
   - [Full workspace save and restore after restart (10)](catalog/05-sessions.md#full-workspace-save-and-restore-after-restart)
   - [Pane command relaunchers after restart (7)](catalog/05-sessions.md#pane-command-relaunchers-after-restart)
   - [Agent auto-resume after a server restart (14)](catalog/05-sessions.md#agent-auto-resume-after-a-server-restart)
   - [Idle agent parking and hibernation (15)](catalog/05-sessions.md#idle-agent-parking-and-hibernation)
   - [Stale and idle agent cleanup (5)](catalog/05-sessions.md#stale-and-idle-agent-cleanup)
   - [Workspace stash, suspend and archive (9)](catalog/05-sessions.md#workspace-stash-suspend-and-archive)
   - [Undo close and reopen closed panes (6)](catalog/05-sessions.md#undo-close-and-reopen-closed-panes)
   - [Fork Claude Code, Codex and OpenCode conversations into a new pane (11)](catalog/05-sessions.md#fork-claude-code-codex-and-opencode-conversations-into-a-new-pane)
   - [Pi side conversations and session forks (8)](catalog/05-sessions.md#pi-side-conversations-and-session-forks)
   - [Moving sessions and workspaces to another machine or app (5)](catalog/05-sessions.md#moving-sessions-and-workspaces-to-another-machine-or-app)
   - [Crash-proof and always-on sessions (6)](catalog/05-sessions.md#crash-proof-and-always-on-sessions)
6. [Worktrees and terminal experience (1120)](#6-worktrees-and-terminal-experience)
   - [Plugin collections you install one by one (37)](catalog/06-worktrees-and-terminal.md#plugin-collections-you-install-one-by-one)
   - [Fuzzy command palettes for Herdr actions and plugins (25)](catalog/06-worktrees-and-terminal.md#fuzzy-command-palettes-for-herdr-actions-and-plugins)
   - [Custom command and script launchers (12)](catalog/06-worktrees-and-terminal.md#custom-command-and-script-launchers)
   - [One-command worktree and agent session starters (10)](catalog/06-worktrees-and-terminal.md#one-command-worktree-and-agent-session-starters)
   - [Worktrees created in one step from a pull request, issue or ticket (15)](catalog/06-worktrees-and-terminal.md#worktrees-created-in-one-step-from-a-pull-request-issue-or-ticket)
   - [Worktree manager CLIs and TUIs wired into Herdr (14)](catalog/06-worktrees-and-terminal.md#worktree-manager-clis-and-tuis-wired-into-herdr)
   - [Worktrunk integrations (9)](catalog/06-worktrees-and-terminal.md#worktrunk-integrations)
   - [Browsers and listers for existing worktrees (9)](catalog/06-worktrees-and-terminal.md#browsers-and-listers-for-existing-worktrees)
   - [Worktree setup scripts and lifecycle hooks (19)](catalog/06-worktrees-and-terminal.md#worktree-setup-scripts-and-lifecycle-hooks)
   - [Worktreeinclude and ignored-file copiers (23)](catalog/06-worktrees-and-terminal.md#worktreeinclude-and-ignored-file-copiers)
   - [Layouts applied to new worktrees (4)](catalog/06-worktrees-and-terminal.md#layouts-applied-to-new-worktrees)
   - [Worktree locations and repository layouts (4)](catalog/06-worktrees-and-terminal.md#worktree-locations-and-repository-layouts)
   - [Per-worktree ports, containers and databases (6)](catalog/06-worktrees-and-terminal.md#per-worktree-ports-containers-and-databases)
   - [Worktree merge, cleanup and safe removal (8)](catalog/06-worktrees-and-terminal.md#worktree-merge-cleanup-and-safe-removal)
   - [Multi-repository workspaces and worktrees (7)](catalog/06-worktrees-and-terminal.md#multi-repository-workspaces-and-worktrees)
   - [Jujutsu, Mercurial, copy-on-write and copied workspaces (9)](catalog/06-worktrees-and-terminal.md#jujutsu-mercurial-copy-on-write-and-copied-workspaces)
   - [Background Git fetch and repository sync (4)](catalog/06-worktrees-and-terminal.md#background-git-fetch-and-repository-sync)
   - [Defaults for new tabs and spaces: directory, agent and startup command (5)](catalog/06-worktrees-and-terminal.md#defaults-for-new-tabs-and-spaces-directory-agent-and-startup-command)
   - [Live diff viewers for agent changes (21)](catalog/06-worktrees-and-terminal.md#live-diff-viewers-for-agent-changes)
   - [Hunk diff launchers (11)](catalog/06-worktrees-and-terminal.md#hunk-diff-launchers)
   - [tuicr, revdiff and lumen review launchers (7)](catalog/06-worktrees-and-terminal.md#tuicr-revdiff-and-lumen-review-launchers)
   - [Pull request, stacked-diff and plan review sessions (10)](catalog/06-worktrees-and-terminal.md#pull-request-stacked-diff-and-plan-review-sessions)
   - [Source-control panels with staging and commits (10)](catalog/06-worktrees-and-terminal.md#source-control-panels-with-staging-and-commits)
   - [lazygit, gitui and other Git TUI launchers (8)](catalog/06-worktrees-and-terminal.md#lazygit-gitui-and-other-git-tui-launchers)
   - [Git graph and commit history panes (4)](catalog/06-worktrees-and-terminal.md#git-graph-and-commit-history-panes)
   - [Git branch and dirty-file counts in the sidebar (10)](catalog/06-worktrees-and-terminal.md#git-branch-and-dirty-file-counts-in-the-sidebar)
   - [Pull request and CI status tokens on workspaces (26)](catalog/06-worktrees-and-terminal.md#pull-request-and-ci-status-tokens-on-workspaces)
   - [Pull request, issue and spec boards (17)](catalog/06-worktrees-and-terminal.md#pull-request-issue-and-spec-boards)
   - [CI check and build run panes (4)](catalog/06-worktrees-and-terminal.md#ci-check-and-build-run-panes)
   - [Test and build runners that report back to agents (5)](catalog/06-worktrees-and-terminal.md#test-and-build-runners-that-report-back-to-agents)
   - [File-tree sidebars with previews and Git status (14)](catalog/06-worktrees-and-terminal.md#file-tree-sidebars-with-previews-and-git-status)
   - [Yazi, nnn and other terminal file managers (9)](catalog/06-worktrees-and-terminal.md#yazi-nnn-and-other-terminal-file-managers)
   - [Path hints that preview files agents mention (9)](catalog/06-worktrees-and-terminal.md#path-hints-that-preview-files-agents-mention)
   - [Fuzzy file pickers that insert or open paths (5)](catalog/06-worktrees-and-terminal.md#fuzzy-file-pickers-that-insert-or-open-paths)
   - [URL pickers and link openers (14)](catalog/06-worktrees-and-terminal.md#url-pickers-and-link-openers)
   - [Markdown and document previews beside agents (11)](catalog/06-worktrees-and-terminal.md#markdown-and-document-previews-beside-agents)
   - [Image, PDF and gallery previews (6)](catalog/06-worktrees-and-terminal.md#image-pdf-and-gallery-previews)
   - [Mermaid, LaTeX and diagram renderers (8)](catalog/06-worktrees-and-terminal.md#mermaid-latex-and-diagram-renderers)
   - [Terminal browsers and drivable Chromium panes for Herdr TUI (9)](catalog/06-worktrees-and-terminal.md#terminal-browsers-and-drivable-chromium-panes-for-herdr-tui)
   - [Shared canvases, mind maps and workflow graphs (5)](catalog/06-worktrees-and-terminal.md#shared-canvases-mind-maps-and-workflow-graphs)
   - [Pane focus that wraps into neighboring tabs and workspaces (8)](catalog/06-worktrees-and-terminal.md#pane-focus-that-wraps-into-neighboring-tabs-and-workspaces)
   - [EasyMotion-style jump hints for panes, tabs and agents (9)](catalog/06-worktrees-and-terminal.md#easymotion-style-jump-hints-for-panes-tabs-and-agents)
   - [Pane marks and harpoon-style bookmarks (5)](catalog/06-worktrees-and-terminal.md#pane-marks-and-harpoon-style-bookmarks)
   - [Numbered tabs and workspaces that match jump shortcuts (12)](catalog/06-worktrees-and-terminal.md#numbered-tabs-and-workspaces-that-match-jump-shortcuts)
   - [Pane IDs and indexes for pointing agents at panes (16)](catalog/06-worktrees-and-terminal.md#pane-ids-and-indexes-for-pointing-agents-at-panes)
   - [Pane equalizers and auto-resize (11)](catalog/06-worktrees-and-terminal.md#pane-equalizers-and-auto-resize)
   - [Focus-driven resizing, zen width and smart splits (9)](catalog/06-worktrees-and-terminal.md#focus-driven-resizing-zen-width-and-smart-splits)
   - [tmux-style layout presets and tiling layouts (13)](catalog/06-worktrees-and-terminal.md#tmux-style-layout-presets-and-tiling-layouts)
   - [Swap, rotate and rearrange panes in a tab (7)](catalog/06-worktrees-and-terminal.md#swap-rotate-and-rearrange-panes-in-a-tab)
   - [Pane grids and visual layout editors (4)](catalog/06-worktrees-and-terminal.md#pane-grids-and-visual-layout-editors)
   - [Live tiled overviews of all panes (6)](catalog/06-worktrees-and-terminal.md#live-tiled-overviews-of-all-panes)
   - [Broadcast input to several panes (7)](catalog/06-worktrees-and-terminal.md#broadcast-input-to-several-panes)
   - [Scratch shells and floating popup terminals (11)](catalog/06-worktrees-and-terminal.md#scratch-shells-and-floating-popup-terminals)
   - [Confirm-before-close prompts (6)](catalog/06-worktrees-and-terminal.md#confirm-before-close-prompts)
   - [Which-key menus and keybinding cheat sheets (15)](catalog/06-worktrees-and-terminal.md#which-key-menus-and-keybinding-cheat-sheets)
   - [Keymap presets that mimic tmux, Chrome and Hyprland (7)](catalog/06-worktrees-and-terminal.md#keymap-presets-that-mimic-tmux-chrome-and-hyprland)
   - [Repeatable keys, key modes and extra keybindable actions (7)](catalog/06-worktrees-and-terminal.md#repeatable-keys-key-modes-and-extra-keybindable-actions)
   - [Touchpad, scrolling, cursor and input-source helpers (8)](catalog/06-worktrees-and-terminal.md#touchpad-scrolling-cursor-and-input-source-helpers)
   - [Keybinding trainers and tutorials (7)](catalog/06-worktrees-and-terminal.md#keybinding-trainers-and-tutorials)
   - [All-in-one status bars and footers (6)](catalog/06-worktrees-and-terminal.md#all-in-one-status-bars-and-footers)
   - [Agent logos, kind and model badges in the sidebar (11)](catalog/06-worktrees-and-terminal.md#agent-logos-kind-and-model-badges-in-the-sidebar)
   - [Animated state icons, counts and spinners on rows (10)](catalog/06-worktrees-and-terminal.md#animated-state-icons-counts-and-spinners-on-rows)
   - [Descriptions, notes and status marks on workspace and agent rows (7)](catalog/06-worktrees-and-terminal.md#descriptions-notes-and-status-marks-on-workspace-and-agent-rows)
   - [Latest prompt and task summaries on agent rows and pane headers (6)](catalog/06-worktrees-and-terminal.md#latest-prompt-and-task-summaries-on-agent-rows-and-pane-headers)
   - [Workspace colors, icons and highlights (8)](catalog/06-worktrees-and-terminal.md#workspace-colors-icons-and-highlights)
   - [Unread and needs-action markers (7)](catalog/06-worktrees-and-terminal.md#unread-and-needs-action-markers)
   - [Overlays and trackers for blocked agents (7)](catalog/06-worktrees-and-terminal.md#overlays-and-trackers-for-blocked-agents)
   - [Elapsed-time and last-activity timers (7)](catalog/06-worktrees-and-terminal.md#elapsed-time-and-last-activity-timers)
   - [Long-running command and build progress (5)](catalog/06-worktrees-and-terminal.md#long-running-command-and-build-progress)
   - [Agent activity timelines, event logs and sparklines (7)](catalog/06-worktrees-and-terminal.md#agent-activity-timelines-event-logs-and-sparklines)
   - [Prompt-cache countdown timers and warmers (7)](catalog/06-worktrees-and-terminal.md#prompt-cache-countdown-timers-and-warmers)
   - [Agents grouped by repository or project (7)](catalog/06-worktrees-and-terminal.md#agents-grouped-by-repository-or-project)
   - [Agents sorted by attention and priority (9)](catalog/06-worktrees-and-terminal.md#agents-sorted-by-attention-and-priority)
   - [Filters that limit the agent list (7)](catalog/06-worktrees-and-terminal.md#filters-that-limit-the-agent-list)
   - [Alternative tab lists and compact sidebars (14)](catalog/06-worktrees-and-terminal.md#alternative-tab-lists-and-compact-sidebars)
   - [Herdr TUI sidebar tree of projects, worktrees and agents (5)](catalog/06-worktrees-and-terminal.md#herdr-tui-sidebar-tree-of-projects-worktrees-and-agents)
   - [Workspace and repository status boards (5)](catalog/06-worktrees-and-terminal.md#workspace-and-repository-status-boards)
   - [Herdr TUI tab names written by an AI from prompts and pane activity (21)](catalog/06-worktrees-and-terminal.md#herdr-tui-tab-names-written-by-an-ai-from-prompts-and-pane-activity)
   - [Herdr TUI tab names copied from Claude Code and Codex session titles (29)](catalog/06-worktrees-and-terminal.md#herdr-tui-tab-names-copied-from-claude-code-and-codex-session-titles)
   - [Herdr TUI tab names synced from Pi, OpenCode, Hermes, Copilot and other agent sessions (14)](catalog/06-worktrees-and-terminal.md#herdr-tui-tab-names-synced-from-pi-opencode-hermes-copilot-and-other-agent-sessions)
   - [Herdr TUI tab names from the foreground process (13)](catalog/06-worktrees-and-terminal.md#herdr-tui-tab-names-from-the-foreground-process)
   - [Herdr TUI tab names from the working directory and Git branch (11)](catalog/06-worktrees-and-terminal.md#herdr-tui-tab-names-from-the-working-directory-and-git-branch)
   - [Tab icons, emoji and codename labels (7)](catalog/06-worktrees-and-terminal.md#tab-icons-emoji-and-codename-labels)
   - [Pane border labels and agent aliases (7)](catalog/06-worktrees-and-terminal.md#pane-border-labels-and-agent-aliases)
   - [Outer terminal and window title sync (11)](catalog/06-worktrees-and-terminal.md#outer-terminal-and-window-title-sync)
   - [Herdr TUI subscription quota gauges in the sidebar (23)](catalog/06-worktrees-and-terminal.md#herdr-tui-subscription-quota-gauges-in-the-sidebar)
   - [Herdr TUI subscription quota in the tab bar (13)](catalog/06-worktrees-and-terminal.md#herdr-tui-subscription-quota-in-the-tab-bar)
   - [Herdr TUI quota popups and dashboard panes (18)](catalog/06-worktrees-and-terminal.md#herdr-tui-quota-popups-and-dashboard-panes)
   - [Herdr TUI quota trackers that compare several accounts and profiles (7)](catalog/06-worktrees-and-terminal.md#herdr-tui-quota-trackers-that-compare-several-accounts-and-profiles)
   - [Herdr TUI API credit and provider balance meters (5)](catalog/06-worktrees-and-terminal.md#herdr-tui-api-credit-and-provider-balance-meters)
   - [Herdr TUI token spend and cost meters for agents (17)](catalog/06-worktrees-and-terminal.md#herdr-tui-token-spend-and-cost-meters-for-agents)
   - [Herdr TUI context-window meters per agent (8)](catalog/06-worktrees-and-terminal.md#herdr-tui-context-window-meters-per-agent)
   - [Machine CPU, memory, battery and network stats (10)](catalog/06-worktrees-and-terminal.md#machine-cpu-memory-battery-and-network-stats)
   - [Per-agent and per-workspace CPU, memory and disk use (8)](catalog/06-worktrees-and-terminal.md#per-agent-and-per-workspace-cpu-memory-and-disk-use)
   - [Agent reply and conversation viewers (11)](catalog/06-worktrees-and-terminal.md#agent-reply-and-conversation-viewers)
   - [Agent task lists and progress panes (8)](catalog/06-worktrees-and-terminal.md#agent-task-lists-and-progress-panes)
   - [Recaps, summaries and explanations of recent work (7)](catalog/06-worktrees-and-terminal.md#recaps-summaries-and-explanations-of-recent-work)
   - [Conversation turn indexes and fork trees (10)](catalog/06-worktrees-and-terminal.md#conversation-turn-indexes-and-fork-trees)
   - [Subagent trees and session flow graphs (13)](catalog/06-worktrees-and-terminal.md#subagent-trees-and-session-flow-graphs)
   - [Copy and capture agent replies and scrollback (8)](catalog/06-worktrees-and-terminal.md#copy-and-capture-agent-replies-and-scrollback)
   - [Copy hints and text pickers in the style of tmux-fingers (16)](catalog/06-worktrees-and-terminal.md#copy-hints-and-text-pickers-in-the-style-of-tmux-fingers)
   - [Quote and reference agent output in prompts (4)](catalog/06-worktrees-and-terminal.md#quote-and-reference-agent-output-in-prompts)
   - [Annotating terminal text and documents for agents (10)](catalog/06-worktrees-and-terminal.md#annotating-terminal-text-and-documents-for-agents)
   - [Herdr TUI palettes such as Modus, Flexoki and Synthwave (10)](catalog/06-worktrees-and-terminal.md#herdr-tui-palettes-such-as-modus-flexoki-and-synthwave)
   - [Theme pickers, font choosers and color tools (5)](catalog/06-worktrees-and-terminal.md#theme-pickers-font-choosers-and-color-tools)
   - [Theme sync with Ghostty, kitty, Omarchy and other apps (8)](catalog/06-worktrees-and-terminal.md#theme-sync-with-ghostty-kitty-omarchy-and-other-apps)
   - [Command policies and approval gates (9)](catalog/06-worktrees-and-terminal.md#command-policies-and-approval-gates)
   - [Collision, secret and plugin-safety warnings (4)](catalog/06-worktrees-and-terminal.md#collision-secret-and-plugin-safety-warnings)
   - [Agent detection inside SSH sessions and dev containers (7)](catalog/06-worktrees-and-terminal.md#agent-detection-inside-ssh-sessions-and-dev-containers)
   - [Project run commands and dev-service runners (7)](catalog/06-worktrees-and-terminal.md#project-run-commands-and-dev-service-runners)
   - [Plugin SDKs, libraries and project starters (7)](catalog/06-worktrees-and-terminal.md#plugin-sdks-libraries-and-project-starters)
   - [Portable Herdr TUI setups and migration notes (8)](catalog/06-worktrees-and-terminal.md#portable-herdr-tui-setups-and-migration-notes)
7. [Apps, companion integrations, and installation (644)](#7-apps-companion-integrations-and-installation)
   - [Native macOS terminal clients for Herdr (19)](catalog/07-apps-and-installation.md#native-macos-terminal-clients-for-herdr)
   - [Windows desktop clients and workbenches (6)](catalog/07-apps-and-installation.md#windows-desktop-clients-and-workbenches)
   - [Linux and cross-platform desktop clients (11)](catalog/07-apps-and-installation.md#linux-and-cross-platform-desktop-clients)
   - [Desktop apps with chat views and agent-team workspaces (8)](catalog/07-apps-and-installation.md#desktop-apps-with-chat-views-and-agent-team-workspaces)
   - [Launchers, Dock icons and desktop entry points (6)](catalog/07-apps-and-installation.md#launchers-dock-icons-and-desktop-entry-points)
   - [iPhone and iPad apps for Herdr (20)](catalog/07-apps-and-installation.md#iphone-and-ipad-apps-for-herdr)
   - [Android apps for Herdr (11)](catalog/07-apps-and-installation.md#android-apps-for-herdr)
   - [Cross-platform mobile clients, relays and gateways (14)](catalog/07-apps-and-installation.md#cross-platform-mobile-clients-relays-and-gateways)
   - [macOS menu bar agent trackers (22)](catalog/07-apps-and-installation.md#macos-menu-bar-agent-trackers)
   - [Notch panels and floating macOS widgets (6)](catalog/07-apps-and-installation.md#notch-panels-and-floating-macos-widgets)
   - [Omarchy bar widgets for agent status (22)](catalog/07-apps-and-installation.md#omarchy-bar-widgets-for-agent-status)
   - [Omarchy overlays, consoles and remote dashboards (8)](catalog/07-apps-and-installation.md#omarchy-overlays-consoles-and-remote-dashboards)
   - [KDE Plasma, Cinnamon and DankMaterialShell widgets (5)](catalog/07-apps-and-installation.md#kde-plasma-cinnamon-and-dankmaterialshell-widgets)
   - [Browser workbenches and control panels for desktop (17)](catalog/07-apps-and-installation.md#browser-workbenches-and-control-panels-for-desktop)
   - [Web boards showing every agent's state across sessions and machines (15)](catalog/07-apps-and-installation.md#web-boards-showing-every-agents-state-across-sessions-and-machines)
   - [Self-hosted web terminals for Herdr sessions (22)](catalog/07-apps-and-installation.md#self-hosted-web-terminals-for-herdr-sessions)
   - [Phone web dashboards that list agents and answer prompts (39)](catalog/07-apps-and-installation.md#phone-web-dashboards-that-list-agents-and-answer-prompts)
   - [Chat-style phone web apps with transcripts, approvals and voice input (11)](catalog/07-apps-and-installation.md#chat-style-phone-web-apps-with-transcripts-approvals-and-voice-input)
   - [Live session sharing, Cloudflare tunnels and cloud relays (9)](catalog/07-apps-and-installation.md#live-session-sharing-cloudflare-tunnels-and-cloud-relays)
   - [Stream Deck, OpenDeck and Ulanzi agent key grids (13)](catalog/07-apps-and-installation.md#stream-deck-opendeck-and-ulanzi-agent-key-grids)
   - [Macro pads, dials and programmable keyboards (13)](catalog/07-apps-and-installation.md#macro-pads-dials-and-programmable-keyboards)
   - [MIDI controllers and pad surfaces (5)](catalog/07-apps-and-installation.md#midi-controllers-and-pad-surfaces)
   - [Game controllers as Herdr remotes (4)](catalog/07-apps-and-installation.md#game-controllers-as-herdr-remotes)
   - [LED lights and microcontroller status beacons (8)](catalog/07-apps-and-installation.md#led-lights-and-microcontroller-status-beacons)
   - [Smartwatches, glasses, touchscreens and other secondary displays (11)](catalog/07-apps-and-installation.md#smartwatches-glasses-touchscreens-and-other-secondary-displays)
   - [Pixel-art and 3D office views outside the Herdr app (13)](catalog/07-apps-and-installation.md#pixel-art-and-3d-office-views-outside-the-herdr-app)
   - [Pets, farms, races and other game worlds outside the Herdr app (27)](catalog/07-apps-and-installation.md#pets-farms-races-and-other-game-worlds-outside-the-herdr-app)
   - [Terminal arcade games, video, drawing and daily cards for idle time (7)](catalog/07-apps-and-installation.md#terminal-arcade-games-video-drawing-and-daily-cards-for-idle-time)
   - [Docker Sandboxes and container sandboxes for agents (10)](catalog/07-apps-and-installation.md#docker-sandboxes-and-container-sandboxes-for-agents)
   - [Local microVMs and virtual machines for agents (9)](catalog/07-apps-and-installation.md#local-microvms-and-virtual-machines-for-agents)
   - [Cloud sandboxes and microVM boxes for agents (13)](catalog/07-apps-and-installation.md#cloud-sandboxes-and-microvm-boxes-for-agents)
   - [Hosted agent runtimes and cloud agent sessions (6)](catalog/07-apps-and-installation.md#hosted-agent-runtimes-and-cloud-agent-sessions)
   - [SSH helpers, Wake-on-LAN, WSL tabs and phone-sized SSH views (7)](catalog/07-apps-and-installation.md#ssh-helpers-wake-on-lan-wsl-tabs-and-phone-sized-ssh-views)
   - [Server and VM provisioning for always-on remote agents (10)](catalog/07-apps-and-installation.md#server-and-vm-provisioning-for-always-on-remote-agents)
   - [Container images that host Herdr for agents (9)](catalog/07-apps-and-installation.md#container-images-that-host-herdr-for-agents)
   - [Listening ports, dev servers and leftover processes (12)](catalog/07-apps-and-installation.md#listening-ports-dev-servers-and-leftover-processes)
   - [Dev-service dashboards and process managers (7)](catalog/07-apps-and-installation.md#dev-service-dashboards-and-process-managers)
   - [Docker, Kubernetes, cluster, cloud and scheduler operations panes (14)](catalog/07-apps-and-installation.md#docker-kubernetes-cluster-cloud-and-scheduler-operations-panes)
   - [Auto-approve and auto-enter helpers for agent prompts (6)](catalog/07-apps-and-installation.md#auto-approve-and-auto-enter-helpers-for-agent-prompts)
   - [Keep-awake and sleep control while agents work (11)](catalog/07-apps-and-installation.md#keep-awake-and-sleep-control-while-agents-work)
   - [Per-tab, per-pane and per-workspace notes and scratchpads (11)](catalog/07-apps-and-installation.md#per-tab-per-pane-and-per-workspace-notes-and-scratchpads)
   - [Markdown notebooks, outliners and searchable note managers (5)](catalog/07-apps-and-installation.md#markdown-notebooks-outliners-and-searchable-note-managers)
   - [To-do lists and task logs in a pane or popup (9)](catalog/07-apps-and-installation.md#to-do-lists-and-task-logs-in-a-pane-or-popup)
   - [Prompt libraries, composers and snippets (10)](catalog/07-apps-and-installation.md#prompt-libraries-composers-and-snippets)
   - [Clipboard history, paste buffers and file or image attachments (9)](catalog/07-apps-and-installation.md#clipboard-history-paste-buffers-and-file-or-image-attachments)
   - [Password, secret and credential pickers (4)](catalog/07-apps-and-installation.md#password-secret-and-credential-pickers)
   - [Finder and file-manager openers (5)](catalog/07-apps-and-installation.md#finder-and-file-manager-openers)
   - [Translation and text-explanation popups (6)](catalog/07-apps-and-installation.md#translation-and-text-explanation-popups)
   - [Agent skill, MCP and instruction-file tooling (7)](catalog/07-apps-and-installation.md#agent-skill-mcp-and-instruction-file-tooling)
   - [Git clients, activity heatmaps and GitHub Actions panes (7)](catalog/07-apps-and-installation.md#git-clients-activity-heatmaps-and-github-actions-panes)
   - [Database and API client panes (6)](catalog/07-apps-and-installation.md#database-and-api-client-panes)
   - [Mobile app simulators, emulators and build panes (4)](catalog/07-apps-and-installation.md#mobile-app-simulators-emulators-and-build-panes)
   - [Build systems, dbt and web-app inspection panes (5)](catalog/07-apps-and-installation.md#build-systems-dbt-and-web-app-inspection-panes)
   - [Google Calendar and Gmail panes (5)](catalog/07-apps-and-installation.md#google-calendar-and-gmail-panes)
   - [Music, radio and Spotify controls in Herdr TUI panes (13)](catalog/07-apps-and-installation.md#music-radio-and-spotify-controls-in-herdr-tui-panes)
   - [Clocks, Pomodoro and countdown timers in Herdr TUI panes (5)](catalog/07-apps-and-installation.md#clocks-pomodoro-and-countdown-timers-in-herdr-tui-panes)
   - [Feeds, stock tickers, chat and widget dashboards in Herdr TUI panes (6)](catalog/07-apps-and-installation.md#feeds-stock-tickers-chat-and-widget-dashboards-in-herdr-tui-panes)
   - [Shell, history and config-reload helpers (6)](catalog/07-apps-and-installation.md#shell-history-and-config-reload-helpers)
   - [Package-manager installs and distro packages (10)](catalog/07-apps-and-installation.md#package-manager-installs-and-distro-packages)
   - [Setup wizards, config syncing and getting-started guides (10)](catalog/07-apps-and-installation.md#setup-wizards-config-syncing-and-getting-started-guides)
   - [Herdr TUI plugin managers and marketplaces (9)](catalog/07-apps-and-installation.md#herdr-tui-plugin-managers-and-marketplaces)
   - [Automatic updaters for Herdr, plugins and agent CLIs (6)](catalog/07-apps-and-installation.md#automatic-updaters-for-herdr-plugins-and-agent-clis)
8. [Experimental projects (12)](#8-experimental-projects)
   - [Plugin labs and alternative interface experiments (6)](catalog/08-experimental.md#plugin-labs-and-alternative-interface-experiments)
   - [Courses, maps and side projects built around Herdr (6)](catalog/08-experimental.md#courses-maps-and-side-projects-built-around-herdr)
9. [Resources](#resources)
10. [Reference](#reference)

---

## 1. Run and orchestrate agents

*592 projects in 52 subcategories. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.* The 10 most-starred are below; browse every subcategory in [catalog/01-run-and-orchestrate.md](catalog/01-run-and-orchestrate.md).

| Project | Stars | What it does |
|---|--:|---|
| [**herdrdev/herdr**](https://github.com/herdrdev/herdr) | 49,988 | Runs the official Herdr TUI for organizing agents and terminals. The official [SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) teaches agents to control its workspaces, tabs, and panes. |
| [**alvinunreal/oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim) | 10,184 | Assigns OpenCode specialist roles (fixers, librarians, explorers) to dedicated Herdr panes. |
| [**kunchenguid/firstmate**](https://github.com/kunchenguid/firstmate) | 8,761 | Supervises coding agents in separate Herdr TUI tabs and isolated Git worktrees. Supports Claude Code, Pi, Codex, OpenCode, and other agent harnesses. |
| [**herdrdev/herdr-app**](https://github.com/herdrdev/herdr-app) | 2,636 | Runs the official Herdr desktop app for terminals and coding agents on macOS, Windows, and Linux. |
| [**herdrdev/herdr-core**](https://github.com/herdrdev/herdr-core) | 588 | Runs persistent terminals and coding agents through the herdr-core runtime, with commands to start, message and wait for work on local or remote machines. |
| [**ogulcancelik/pi-extensions**](https://github.com/ogulcancelik/pi-extensions) | 573 | Extends Pi with overlays, parallel agent spawners, session recall, and direct Herdr pane control. |
| [**cloudmanic/herdr-plus**](https://github.com/cloudmanic/herdr-plus) | 379 | A plugin with two launchers: TOML project templates that build complete workspaces from a fuzzy picker, and Quick Actions for running reusable scripts in the current directory. Prebuilt binaries are available. |
| [**osolmaz/pi-workflows**](https://github.com/osolmaz/pi-workflows) | 361 | Provides a workflow engine, JSON control-flow system, and live terminal viewer for the Pi coding agent in Herdr. |
| [**uwuclxdy/clauth · herdr-plugin**](https://github.com/uwuclxdy/clauth/tree/mommy/herdr-plugin) | 321 | Manages Claude Code accounts and usage from a Herdr TUI popup and tags panes with their active account. |
| [**smarzban/herdr-tsk**](https://github.com/smarzban/herdr-tsk) | 266 | Shares a terminal task board between you and your agents with a TUI for humans and a CLI for agents. |

**[All 592 projects in 52 subcategories →](catalog/01-run-and-orchestrate.md)**

---

## 2. Herdr app layouts, mods, and themes

*781 projects in 71 subcategories. Layouts, mods, and themes for customizing the Herdr desktop app.* The 10 most-starred are below; browse every subcategory in [catalog/02-herdr-app.md](catalog/02-herdr-app.md).

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**runkids/skillshare · herdr/skillshare**](https://github.com/runkids/skillshare/tree/main/herdr/skillshare) | 3,007 | Adds a Herdr app layout with a skillshare panel for viewing, auditing and syncing skills, agents, MCP servers, plugins and hooks. |
| [**eliasstravik/shepherdr**](https://github.com/eliasstravik/shepherdr) | 1,117 | Organizes coding agents in a Herdr app layout with per-space assistants and task cards, running tasks in separate worktrees. |
| [**sodiumsun/agenttrail · herdr/agenttrail**](https://github.com/sodiumsun/agenttrail/tree/main/herdr/agenttrail) | 1,009 | Shows a read-only project map beside Herdr app terminals, using PLAN.md or inferred Git branches and worktrees. |
| [**JinJieBeWater/herdr-t3**](https://github.com/JinJieBeWater/herdr-t3) | 157 | Organizes Herdr app agents in an inbox that groups work by attention state and shows agents across machines. |
| [**fatwang2/Pulse · herdr**](https://github.com/fatwang2/Pulse/tree/main/herdr) | 121 | Adds a stock and crypto watchlist mod and a matching Herdr app layout with a docked price panel. |
| [**GaganSD/coding-agent-toolkit · herdr-insights**](https://github.com/GaganSD/coding-agent-toolkit/tree/main/herdr-insights) | 49 | Shows local token usage and model activity for Pi, Codex, Claude Code, OpenCode and Antigravity in a Herdr app dashboard. |
| [**jankeesvw/herdr-space-folders**](https://github.com/jankeesvw/herdr-space-folders) | 37 | Groups Herdr app spaces into colored, collapsible folders using drag-and-drop or project folder rules. |
| [**franky5440-afk/herdr-traveler**](https://github.com/franky5440-afk/herdr-traveler) | 35 | Turns the Herdr app into a pixel RPG with agent portraits, status bars, and machine buildings. |
| [**rabeeh-ta/herdr-git-graph**](https://github.com/rabeeh-ta/herdr-git-graph) | 34 | Shows a Git commit graph in the Herdr app and offers branch, merge, rebase, and other repository actions. |
| [**wobsoriano/herdr-sim**](https://github.com/wobsoriano/herdr-sim) | 34 | Opens an interactive iOS simulator or Android emulator beside code and terminals in the Herdr app. |

**[All 781 projects in 71 subcategories →](catalog/02-herdr-app.md)**

---

## 3. Connect through MCP and the socket API

*322 projects in 46 subcategories. Protocols, clients, bots, and event bridges that link Herdr to external tools, editors, and messaging apps.* The 10 most-starred are below; browse every subcategory in [catalog/03-mcp-and-socket-api.md](catalog/03-mcp-and-socket-api.md).

| Project | Stars | What it does |
|---|--:|---|
| [**alexei-led/ccgram**](https://github.com/alexei-led/ccgram) | 289 | Maps forum topics to terminal windows running Claude Code, Codex, Gemini, Pi, or a shell. It relays output and input through Herdr or tmux so sessions remain usable from a phone. |
| [**klarluft/pitupitu**](https://github.com/klarluft/pitupitu) | 223 | Connects phone and browser voice conversations to coding agents running in Herdr TUI. |
| [**permgps/herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents) | 87 | Creates a Telegram forum topic for each Herdr agent so users can receive status updates and reply to prompts. |
| [**T0mSIlver/localvoxtral**](https://github.com/T0mSIlver/localvoxtral) | 64 | Fully local, real-time dictation for Apple Silicon Macs. It streams speech into the coding-agent session under the cursor, including Claude Code inside a Herdr pane, and uses that session as context for optional text polishing. |
| [**dmmulroy/herdr-ts-sdk**](https://github.com/dmmulroy/herdr-ts-sdk) | 57 | Provides an Effect-native TypeScript SDK for Herdr's local protocol-21 socket API. |
| [**yankewei/herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify) | 34 | Shows a clickable macOS notification when an unseen pane becomes blocked or finishes. Clicking the alert brings the terminal forward and focuses the exact pane through `alerter`. |
| [**brogrammerMW/herdr-voice**](https://github.com/brogrammerMW/herdr-voice) | 32 | Lets users speak to agents in Herdr TUI panes and hear replies using local OpenLive or realtime xAI, OpenAI, and Google models. |
| [**0xGosu/herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot) | 31 | Prompts a running coding CLI through the Herdr API. A training mode observes user actions, safety checks block dangerous operations, and an optional autonomous mode can continue prompting after sufficient setup. |
| [**27medkamal/tmux-agent-wizard**](https://github.com/27medkamal/tmux-agent-wizard) | 21 | Brings Herdr agent detection and compatible CLI-driven plugins to tmux. |
| [**mitkox/dsh-herdr**](https://github.com/mitkox/dsh-herdr) | 17 | Reports DeepSeek Harness agent state to herdr-core via OSC 7501 and displays sessions in a Herdr app panel. |

**[All 322 projects in 46 subcategories →](catalog/03-mcp-and-socket-api.md)**

---

## 4. Editor integrations

*110 projects in 15 subcategories. Bridges and pane synchronizers that let you drive Herdr agents directly from your code editor.* The 10 most-starred are below; browse every subcategory in [catalog/04-editors.md](catalog/04-editors.md).

| Project | Stars | What it does |
|---|--:|---|
| [**zenbu-labs/terminal-code · herdr-plugin**](https://github.com/zenbu-labs/terminal-code/tree/main/herdr-plugin) | 2,247 | Adds an action that opens terminal-code, a VS Code-style editor for the terminal, in a split to the right of the focused pane in Herdr TUI. The plugin installs the tode binary when it builds. |
| [**eugenioenko/ttt · herdr-plugin**](https://github.com/eugenioenko/ttt/tree/main/herdr-plugin) | 1,093 | Opens TTT Editor in a Herdr TUI pane for editing files in the active worktree. |
| [**ChmaraX/herdr-nvim**](https://github.com/ChmaraX/herdr-nvim) | 353 | Opens a persistent Neovim sidebar in Herdr with file search and annotations that can be sent to agents. |
| [**paulbkim-dev/vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation) | 115 | Ports vim-tmux-navigator behavior to Herdr. Direction keys move within Vim or Neovim until an edge is reached, then shift focus to the adjacent Herdr pane based on the pane's foreground process. |
| [**lmilojevicc/herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim) | 69 | Bridges Neovim split navigation and smart pane resizing with Herdr terminal panes. |
| [**ImArtisann/zed-herdr**](https://github.com/ImArtisann/zed-herdr) | 36 | Keeps Zed projects synchronized with Herdr workspaces by listening to lifecycle events over the Unix socket. It supports reconnection and full snapshot synchronization after interruptions. |
| [**aimdevlee/herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav) | 22 | Moves between Neovim splits and Herdr TUI panes with shared Ctrl+h/j/k/l bindings and socket-based focus tracking. |
| [**nettlesh/dotfiles**](https://github.com/nettlesh/dotfiles) | 18 | Personal Alacritty, Fish, Herdr, and Neovim dotfiles with workspace navigation and agent-dispatch configuration. |
| [**makyinmars/herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim) | 16 | Stages Neovim selections, cursor positions, and file details as Markdown context for a Herdr agent. |
| [**scott-the-programmer/vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr) | 16 | Forwards Herdr's Unix socket into VS Code development containers through a loopback TCP bridge, allowing containerized agents to report status and receive commands from the host Herdr instance. |

**[All 110 projects in 15 subcategories →](catalog/04-editors.md)**

---

## 5. Switch and restore sessions

*338 projects in 37 subcategories. Fuzzy switchers, state managers, and layout restoration tools for organizing agent workspaces.* The 10 most-starred are below; browse every subcategory in [catalog/05-sessions.md](catalog/05-sessions.md).

| Project | Stars | What it does |
|---|--:|---|
| [**nicosuave/memex**](https://github.com/nicosuave/memex) | 312 | Indexes conversations from Claude Code, Codex, Pi, OpenCode, and Cursor with hybrid search. A Herdr TUI searches the archive and can resume a selected interaction in a fresh tab. |
| [**nikok6/herdr-mirror**](https://github.com/nikok6/herdr-mirror) | 263 | Mirrors remote Herdr workspaces and agent state into a local sidebar over SSH or Docker. Remote panes can be watched and controlled alongside local ones. |
| [**jeffarese/herdr-bar**](https://github.com/jeffarese/herdr-bar) | 214 | A dependency-free Python command palette for jumping to any Herdr tab, agent, repository, or branch. |
| [**thanhdat77/herdr-navigator**](https://github.com/thanhdat77/herdr-navigator) | 188 | Searches and switches between active Herdr sessions and workspaces using an interactive fuzzy picker. |
| [**thanhdat77/herdr-picker-plus**](https://github.com/thanhdat77/herdr-picker-plus) | 188 | A Ratatui overlay that combines workspaces, project templates, directories, zoxide history, SSH hosts, agent panes, and plugin integrations. It reuses matching workspaces and can create or focus remote-host workspaces automatically. |
| [**yuk1ty/herdr-spreader**](https://github.com/yuk1ty/herdr-spreader) | 145 | Builds complete Herdr layouts from YAML, including tabs, splits, directories, startup commands, and dependencies that wait for output patterns before launching later panes. |
| [**andrewchng/herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer) | 53 | A tmux-sessionizer-style launcher for Herdr. Fzf selects projects or worktrees, while TOML defines tabs, splits, startup commands, repository-specific layouts, and preview panels. |
| [**fullerzz/herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh) | 52 | A sesh-style Herdr workspace picker with zoxide integration for creating workspaces from frequently used directories. |
| [**ntindle/herdr-resurrect**](https://github.com/ntindle/herdr-resurrect) | 44 | Captures workspaces, tabs, panes, directories, and running agent processes so a complete Herdr environment can be restored after a crash or restart. |
| [**taxueseek/session-digger**](https://github.com/taxueseek/session-digger) | 34 | Indexes conversations from Claude Code, Codex, and other agents in SQLite FTS5. It also tracks token and cache data and creates local HTML reports for review. |

**[All 338 projects in 37 subcategories →](catalog/05-sessions.md)**

---

## 6. Worktrees and terminal experience

*1120 projects in 112 subcategories. Git worktree automation, terminal navigation, status displays, HUDs, and developer environment tools.* The 10 most-starred are below; browse every subcategory in [catalog/06-worktrees-and-terminal.md](catalog/06-worktrees-and-terminal.md).

| Project | Stars | What it does |
|---|--:|---|
| [**zenbu-labs/terminal-browser · herdr-plugin**](https://github.com/zenbu-labs/terminal-browser/tree/main/herdr-plugin) | 4,576 | Opens a terminal browser beside a Herdr TUI pane and supports agent-driven browser interaction. |
| [**furkankly/zoetrope · herdr-plugin**](https://github.com/furkankly/zoetrope/tree/main/herdr-plugin) | 1,156 | Shows Claude Code and Codex sessions as live flow graphs and opens the view beside a Herdr TUI pane. |
| [**persiyanov/herdr-reviewr**](https://github.com/persiyanov/herdr-reviewr) | 980 | Opens an interactive diff review interface for inspecting agent changes and sending review feedback. |
| [**plannotator/herdr-annotate**](https://github.com/plannotator/herdr-annotate) | 741 | Annotates terminal text, reviews documents and agent replies in Herdr, and returns feedback directly to the running agent. |
| [**smarzban/herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer) | 704 | Opens a read-only file viewer in a Herdr TUI split with Git status, diffs, Markdown, and source previews. |
| [**alexarthurs/herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar) | 541 | Opens a dockable file explorer and source-control panel with previews and AI-drafted commit messages in Herdr TUI. |
| [**kryptamine/herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title) | 282 | Updates Herdr tab titles automatically based on active workspace tasks to keep development contexts organized. |
| [**qu8n/herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename) | 230 | Renames tabs from the active foreground process and icon, and prefixes workspaces, tabs, and agents with numbers 1 through 9 for quick visual and keyboard selection. |
| [**hhdebb/herdr-radar**](https://github.com/hhdebb/herdr-radar) | 204 | Shows agent activity in the Herdr TUI sidebar, grouping workspaces and worktrees and highlighting waiting or stale sessions. |
| [**devashish2203/herdr-worktrunk**](https://github.com/devashish2203/herdr-worktrunk) | 197 | Creates, switches, merges, and removes Git worktrees with Worktrunk from Herdr TUI, using Worktrunk lifecycle hooks and an interactive branch picker. |

**[All 1120 projects in 112 subcategories →](catalog/06-worktrees-and-terminal.md)**

---

## 7. Apps, companion integrations, and installation

*644 projects in 62 subcategories. Native applications, web dashboards, hardware companions, supporting utilities, and setup packages.* The 10 most-starred are below; browse every subcategory in [catalog/07-apps-and-installation.md](catalog/07-apps-and-installation.md).

| Project | Stars | What it does |
|---|--:|---|
| [**sheprd-labs/sheprd**](https://github.com/sheprd-labs/sheprd) | 2,260 | Opens Herdr TUI and herdr-core terminal sessions in a native desktop client. |
| [**devswha/ovis**](https://github.com/devswha/ovis) | 2,011 | Shows Herdr agent transcripts and terminals in a desktop or phone browser, with approval cards and SSH connections. |
| [**AltanS/collie**](https://github.com/AltanS/collie) | 1,624 | Shows terminal agents in a phone web app and lets users answer them remotely. |
| [**openclaw/crabbox**](https://github.com/openclaw/crabbox) | 1,527 | Adds Crabbox sandbox provisioning and remote test execution to Herdr. Plugin actions can prewarm temporary environments, synchronize diffs, and inspect active leases from an overlay. |
| [**ZingerLittleBee/Heeler**](https://github.com/ZingerLittleBee/Heeler) | 860 | Supervises Herdr agents from an iOS console with SSH terminals, QR pairing, and push notifications. |
| [**missuo/herdrm**](https://github.com/missuo/herdrm) | 794 | Adds a native macOS console for Herdr to drive coding agents and monitor live terminals across devices. |
| [**dcolinmorgan/herdr-remote**](https://github.com/dcolinmorgan/herdr-remote) | 449 | Monitors and controls Herdr agents through a macOS menu bar, phone dashboard, and Telegram. |
| [**0cv/herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay) | 375 | Combines Herdr agents from multiple machines in an installable phone web app. |
| [**powerfooI/roamgate**](https://github.com/powerfooI/roamgate) | 325 | Adds a web client for Herdr with mobile optimization, browser terminals, workspace management, and session inspection. |
| [**themartianapp/herdrup**](https://github.com/themartianapp/herdrup) | 242 | Monitors Herdr TUI agents and opens their terminals from an iOS app. |

**[All 644 projects in 62 subcategories →](catalog/07-apps-and-installation.md)**

---

## 8. Experimental projects

*12 projects in 2 subcategories. Experimental Herdr projects and prototypes.* The 10 most-starred are below; browse every subcategory in [catalog/08-experimental.md](catalog/08-experimental.md).

| Project | Stars | What it does |
|---|--:|---|
| [**eliasstravik/herdr-call**](https://github.com/eliasstravik/herdr-call) | 16 | An early TypeScript prototype for translating spoken commands into Herdr navigation and input through the local socket. |
| [**shaun-agent/herdr-map**](https://github.com/shaun-agent/herdr-map) | 3 | Renders visual Mermaid diagrams mapping Herdr architecture, socket APIs, and workspace concepts. |
| [**playsthisgame/herdr-x**](https://github.com/playsthisgame/herdr-x) | 3 | Browses x.com in a terminal split inside herdr, and draft posts in $EDITOR to send yourself. |
| [**hmu332233/herdr-plugins-labs**](https://github.com/hmu332233/herdr-plugins-labs) | 2 | An experimental plugin laboratory containing early prototypes for agent launching, workspace metrics, and worktree symlinking before they move into separate projects. |
| [**rohanthewiz/herdr-web**](https://github.com/rohanthewiz/herdr-web) | 1 | Renders Herdr pane frames with color, mouse, clipboard, and hyperlink support; keyboard and paste input are currently disabled, so it mainly works as a viewer. |
| [**speardragon/herdr-labs**](https://github.com/speardragon/herdr-labs) | 1 | Provides herdr plugin lab, AI-agent plugin idea contests: 9 agents compete, AI judges score. |
| [**conpiracy/lzy-ad-factory**](https://github.com/conpiracy/lzy-ad-factory) | 1 | Creates a Herdr TUI workspace and Pi workflow for producing UGC ad scripts, prompts, QA, and export bundles. |
| [**5qln/5qln-herdr-plugin**](https://github.com/5qln/5qln-herdr-plugin) | 0 | Provides the 4+1 cell as a Herdr instrument, sealed podium for human questions, and four agent desks. |
| [**robinbraemer/herdr-axi**](https://github.com/robinbraemer/herdr-axi) | 0 | An early command-line interface designed to make Herdr workspace operations easier for coding agents to use. |
| [**fpigeonjr/herdr-course**](https://github.com/fpigeonjr/herdr-course) | 0 | Provides a self-paced course for herding the pi coding agent with Herdr. |

**[All 12 projects in 2 subcategories →](catalog/08-experimental.md)**

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
