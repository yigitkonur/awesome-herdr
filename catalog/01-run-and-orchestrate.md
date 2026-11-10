# Awesome Herdr: Run and orchestrate agents

The full list for domain 1 of [Awesome Herdr](../README.md#1-run-and-orchestrate-agents), ordered by GitHub stars.

- [Official Herdr projects and skill (5)](#official-herdr-projects-and-skill)
- [Skills that teach agents to operate Herdr (10)](#skills-that-teach-agents-to-operate-herdr)
- [Orchestration skills for lead agents (26)](#orchestration-skills-for-lead-agents)
- [Lead-agent coordinators with worker tabs (30)](#lead-agent-coordinators-with-worker-tabs)
- [Fleet control planes and CLI harnesses (40)](#fleet-control-planes-and-cli-harnesses)
- [Role-based agent teams with planners and reviewers (28)](#role-based-agent-teams-with-planners-and-reviewers)
- [Agent team definitions and role profiles (10)](#agent-team-definitions-and-role-profiles)
- [Swarm orchestrators for parallel agent waves (8)](#swarm-orchestrators-for-parallel-agent-waves)
- [Live panes for native Claude Code, Codex and OpenCode subagents (10)](#live-panes-for-native-claude-code-codex-and-opencode-subagents)
- [Task delegation to other coding agents (24)](#task-delegation-to-other-coding-agents)
- [Task routers that pick the agent and model (8)](#task-routers-that-pick-the-agent-and-model)
- [Popup pickers that launch a coding agent in a new tab (16)](#popup-pickers-that-launch-a-coding-agent-in-a-new-tab)
- [Scripts that spawn grids of agents in worktrees (7)](#scripts-that-spawn-grids-of-agents-in-worktrees)
- [Sending agent tasks to other machines and clusters (4)](#sending-agent-tasks-to-other-machines-and-clusters)
- [Handoffs of work and context between agent panes (6)](#handoffs-of-work-and-context-between-agent-panes)
- [Terminal dashboards and mission-control tabs for agent fleets (23)](#terminal-dashboards-and-mission-control-tabs-for-agent-fleets)
- [Side panels with worktree, PR and diff cards per agent (6)](#side-panels-with-worktree-pr-and-diff-cards-per-agent)
- [Durable mailboxes and message queues for agents (13)](#durable-mailboxes-and-message-queues-for-agents)
- [Peer messaging, mentions and relays between agent panes (12)](#peer-messaging-mentions-and-relays-between-agent-panes)
- [Shared chat rooms and group channels for agent teams (8)](#shared-chat-rooms-and-group-channels-for-agent-teams)
- [Agent networks and meshes across machines and people (9)](#agent-networks-and-meshes-across-machines-and-people)
- [Human-decision queues for blocked agents (6)](#human-decision-queues-for-blocked-agents)
- [Second-opinion reviewers in a split pane (9)](#second-opinion-reviewers-in-a-split-pane)
- [Writer and reviewer agent pairs (7)](#writer-and-reviewer-agent-pairs)
- [Consensus and judge panels of several agents (4)](#consensus-and-judge-panels-of-several-agents)
- [Pull-request review dispatchers (4)](#pull-request-review-dispatchers)
- [Agent races and side-by-side comparisons (5)](#agent-races-and-side-by-side-comparisons)
- [Workflow engines and scripted agent pipelines (12)](#workflow-engines-and-scripted-agent-pipelines)
- [Spec-driven and SDLC process frameworks (6)](#spec-driven-and-sdlc-process-frameworks)
- [Autonomous coding loops that end in pull requests (11)](#autonomous-coding-loops-that-end-in-pull-requests)
- [Tracker-driven agent factories (14)](#tracker-driven-agent-factories)
- [Herdr TUI plugins that turn Linear issues into agent runs (7)](#herdr-tui-plugins-that-turn-linear-issues-into-agent-runs)
- [Herdr TUI Jira boards and ticket launchers (9)](#herdr-tui-jira-boards-and-ticket-launchers)
- [Herdr TUI GitHub issue and pull-request browsers that start agents (7)](#herdr-tui-github-issue-and-pull-request-browsers-that-start-agents)
- [GitLab, ClickUp, Shortcut, Notion and other tracker clients (11)](#gitlab-clickup-shortcut-notion-and-other-tracker-clients)
- [Kanban boards that dispatch agents (11)](#kanban-boards-that-dispatch-agents)
- [Shared task boards for people and agents (10)](#shared-task-boards-for-people-and-agents)
- [Task claims and ledgers that agents share (9)](#task-claims-and-ledgers-that-agents-share)
- [Beads task tracker integrations (4)](#beads-task-tracker-integrations)
- [Scheduled agent routines and cron jobs (15)](#scheduled-agent-routines-and-cron-jobs)
- [Prompt queues and delayed prompt delivery (11)](#prompt-queues-and-delayed-prompt-delivery)
- [Event triggers and agent wake-ups (7)](#event-triggers-and-agent-wake-ups)
- [Queued task runners with review gates (7)](#queued-task-runners-with-review-gates)
- [Usage-limit auto-resume and retry (9)](#usage-limit-auto-resume-and-retry)
- [Claude Code and Codex login switchers and auth monitors (9)](#claude-code-and-codex-login-switchers-and-auth-monitors)
- [Context compaction and agent memory (4)](#context-compaction-and-agent-memory)
- [Pi subagent tools that return results to the parent session (24)](#pi-subagent-tools-that-return-results-to-the-parent-session)
- [Pi foremen and crews that coordinate and supervise several workers (24)](#pi-foremen-and-crews-that-coordinate-and-supervise-several-workers)
- [Pi planner, coder and reviewer teams (11)](#pi-planner-coder-and-reviewer-teams)
- [Pi extensions that control Herdr (8)](#pi-extensions-that-control-herdr)
- [Pi sidebars, trees and subagent viewers (5)](#pi-sidebars-trees-and-subagent-viewers)
- [Oh My Pi orchestration and viewers (9)](#oh-my-pi-orchestration-and-viewers)

---

## 1. Run and orchestrate agents

*592 projects. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.*

### Official Herdr projects and skill

*5 projects. Official Herdr apps, runtime, TUI, skill, layout examples and Nix packaging from the herdrdev organization.*

| Project | Stars | What it does |
|---|--:|---|
| [**herdrdev/herdr-app**](https://github.com/herdrdev/herdr-app) | 2,636 | Runs the official Herdr desktop app for terminals and coding agents on macOS, Windows, and Linux. |
| [**herdrdev/herdr-core**](https://github.com/herdrdev/herdr-core) | 588 | Runs persistent terminals and coding agents through the herdr-core runtime, with commands to start, message and wait for work on local or remote machines. |
| [**herdrdev/herdr**](https://github.com/herdrdev/herdr) | 49,988 | Runs the official Herdr TUI for organizing agents and terminals. The official [SKILL.md](https://github.com/herdrdev/herdr/blob/master/skills/herdr/SKILL.md) teaches agents to control its workspaces, tabs, and panes. |
| [**herdrdev/herdr-layout-examples**](https://github.com/herdrdev/herdr-layout-examples) | 15 | Shows a collection of Herdr app window layouts including Board, Chat, Mission, Pasture and Threads, plus a tmux-style prefix mod. |
| [**herdrdev/herdr-nix**](https://github.com/herdrdev/herdr-nix) | 20 | Installs hash-verified Herdr TUI release binaries through Nix and offers a Cachix binary cache. |

### Skills that teach agents to operate Herdr

*10 projects. Skills and CLI references that show an agent how to split panes, spawn agents, send input, read output and wait for state changes.*

| Project | Stars | What it does |
|---|--:|---|
| [**DeevsDeevs/agent-system · skills/hc**](https://github.com/DeevsDeevs/agent-system/tree/main/skills/hc) | 41 | Teaches coding agents to run background work, communicate with peers and operate across machines using herdr-core. |
| [**yangyang0507/herdr-skill**](https://github.com/yangyang0507/herdr-skill) | 3 | Refines Herdr agent coordination by replacing vague status polling with output markers and structured messages. Messages include sender, reply target, and task type, and a dependency-free `herdr-msg` Bash helper is included. |
| [**agileandy/agent-multiplexer-skills**](https://github.com/agileandy/agent-multiplexer-skills) | 1 | Teaches coding agents to control Herdr and tmux panes, launch siblings, watch logs, and manage workspace layouts. |
| [**jbaham2/herdr-plugin**](https://github.com/jbaham2/herdr-plugin) | 1 | Teaches Claude Code to orchestrate Herdr TUI agents, manage sessions and layouts, and monitor agent state. |
| [**zoridos/herdr-skill**](https://github.com/zoridos/herdr-skill) | 1 | Teaches coding agents to split Herdr TUI panes, spawn agents, send tasks, read output, and wait for state changes. |
| [**Sebastiangmz/herdr-plus**](https://github.com/Sebastiangmz/herdr-plus) | 0 | Teaches coding agents to operate Herdr and delegate work to subagents in Herdr spaces. |
| [**cheahhl814/herdr-lab**](https://github.com/cheahhl814/herdr-lab) | 0 | Teaches coding agents safe Herdr delegation, including verified completion and provider preflight. |
| [**kanwhile/herdr-skill**](https://github.com/kanwhile/herdr-skill) | 0 | Teaches Claude Code to drive Herdr TUI panes and agents using a CLI reference checked against the binary. |
| [**luweiCN/herdr-ops**](https://github.com/luweiCN/herdr-ops) | 0 | Adds natural-language workspace commands to Herdr's official skill. Requests such as creating a feature worktree are translated into CLI operations, including worktree actions not covered by the upstream skill, with detailed documentation loaded only when needed. |
| [**hisetu/herdr-agent-skill**](https://github.com/hisetu/herdr-agent-skill) | 0 | Adds integration support and dedicated helpers for using an agent skill inside Herdr sessions. |

### Orchestration skills for lead agents

*26 projects. Skills and prompt packs you install into a lead agent such as Claude Code, Codex or Pi so it plans work and runs Herdr workers itself; the deliverable is instructions, not a separate program.*

| Project | Stars | What it does |
|---|--:|---|
| [**arronKler/herdr-skills**](https://github.com/arronKler/herdr-skills) | 21 | Coordinates Herdr coding agents with dispatch, handoff, result collection, and swarm skills. |
| [**LittleDrinks/herdr-orchestrator-skill**](https://github.com/LittleDrinks/herdr-orchestrator-skill) | 2 | Turns the main Claude Code session into a coordinator that plans work, starts workers in Herdr panes, and monitors them without editing code itself. It includes Python monitors, a YAML state-machine template, and role prompts. |
| [**imdigitalashish/pane-sheepdog**](https://github.com/imdigitalashish/pane-sheepdog) | 2 | Provides a Codex skill for herding sibling AI coding agents across Herdr panes: fan-out delegation, shared-pane safety, and a supervisor that wakes a sleeping orchestrator. |
| [**zekierman/orkestra**](https://github.com/zekierman/orkestra) | 2 | Teaches Claude Code to lead Codex and Antigravity workers running in the same Herdr workspace. A session-start hook tells Claude who is in the room; README is Turkish with an English version. |
| [**eteplus/agent-workbench**](https://github.com/eteplus/agent-workbench) | 2 | Defines a multi-agent workflow where Claude Code or Pi acts as Main and delegates sub-tasks to Pi agents through Herdr. Covers task grading, model routing and review gates; docs are Chinese. |
| [**gal-leib/claude-vibe**](https://github.com/gal-leib/claude-vibe) | 1 | Provides a /vibe skill: a read-only Claude Code director that spawns, briefs and verifies persistent worker sessions in Herdr panes. |
| [**ralphcrisostomo/herdr-goal-skill**](https://github.com/ralphcrisostomo/herdr-goal-skill) | 1 | Splits a goal among parallel Claude Code leads in Herdr TUI panes and worktrees, then reviews the combined result. |
| [**msadig/herdr-peer-agents-skill**](https://github.com/msadig/herdr-peer-agents-skill) | 1 | Teaches Claude, Pi, or Codex to start a named peer agent, assign work, and collect its result. A shell wrapper handles common startup failures and Codex input quirks. |
| [**regenrek/codex-orchestration-herdr**](https://github.com/regenrek/codex-orchestration-herdr) | 1 | A reusable Codex Sol/Luna orchestration skill that assigns workers through Herdr and reuses panes in a predictable way. |
| [**tuong-nguyen-vn/personal-assistant-template**](https://github.com/tuong-nguyen-vn/personal-assistant-template) | 1 | Provides a bootstrap template for a personal coordinator agent with Herdr delegation skills. |
| [**Herdanis/the-cat-concerto**](https://github.com/Herdanis/the-cat-concerto) | 1 | Installs an orchestrator prompt and worker contract that spawns a Herdr pane per sibling repo and delegates work to a worker agent. Reviews each result. |
| [**friendsfriend/agentic-coding · herdr-manager**](https://github.com/friendsfriend/agentic-coding/tree/main/agent-definitions/skills/herdr-manager) | 1 | Teaches an agent to manage OpenSpec implementation workspaces through Herdr TUI. |
| [**ptshih/fsd**](https://github.com/ptshih/fsd) | 1 | Coordinates coding agents from implementation through review and integration using Herdr tabs, Git worktrees, and filesystem handoffs. Installs as a Claude Code plugin or Pi skill. |
| [**nyjin/herdr-skills**](https://github.com/nyjin/herdr-skills) | 1 | Adds Claude Code skills that run parallel coding agents in git worktrees and show each worker in the Herdr sidebar. Installs as a Claude Code plugin or per skill. |
| [**HarshaLakkaraju/herdr-orchestrator-skill**](https://github.com/HarshaLakkaraju/herdr-orchestrator-skill) | 0 | Teaches a lead agent to plan tasks, launch Herdr workers, exchange artifacts, review results, and clean up completed panes. |
| [**pandore/herdr-work**](https://github.com/pandore/herdr-work) | 0 | Routes coding tasks through a model-neutral Herdr orchestration skill that selects roles and keeps one owner accountable. |
| [**aerain/herdr-agent-orchestration**](https://github.com/aerain/herdr-agent-orchestration) | 0 | Provides a pane-based orchestration skill for OMP and Claude Code running in Herdr. |
| [**i11v/orchestrate-skill**](https://github.com/i11v/orchestrate-skill) | 0 | Provides an Agent Skill for coordinating and actively steering subagents through Herdr across implementation, review, consultation, and log-monitoring workflows. |
| [**creedants/pstack-portable**](https://github.com/creedants/pstack-portable) | 0 | Installs portable engineering skills for Codex, Claude Code, Grok Build, and Cursor Agent, including Herdr team coordination. |
| [**tenmomo/fleet-commander**](https://github.com/tenmomo/fleet-commander) | 0 | Teaches an operator to coordinate coding-agent fleets across Herdr workspaces, SSH hosts, and tmux panes. |
| [**djbclark/claude-orchestration-skills**](https://github.com/djbclark/claude-orchestration-skills) | 0 | Teaches Claude Code to coordinate multi-agent handoffs through Herdr TUI and use Ralph TUI with Beads. |
| [**abhishek944/astack · skills/pi-herdr-skills**](https://github.com/abhishek944/astack/tree/main/skills/pi-herdr-skills) | 0 | Installs reusable Pi skills for planning, implementation, and Herdr-hosted agent workflows. |
| [**zbsdsb/herdr-codex-pi-workflow**](https://github.com/zbsdsb/herdr-codex-pi-workflow) | 0 | Installs agent skills for stateful Herdr coding workflows, evidence gates, and post-delivery triage. |
| [**mithyer/ry-skill**](https://github.com/mithyer/ry-skill) | 0 | Collects Pi skills for Herdr-based workflows. |
| [**nativestrider/agent-control-skills**](https://github.com/nativestrider/agent-control-skills) | 0 | Coordinates Codex and Herdr workers with reusable skills for dispatch, lane ownership, reporting, and session recovery. |
| [**nmogil/agent-skill-patterns · herdr-claude-pr-lane**](https://github.com/nmogil/agent-skill-patterns/tree/main/skills/herdr-claude-pr-lane) | 0 | Teaches Claude Code to run pull-request-sized work in a Herdr TUI lane. |

### Lead-agent coordinators with worker tabs

*30 projects. Runnable coordinators where one lead agent session or chief plans the work and starts worker agents in their own Herdr tabs and worktrees; the lead agent is the brain.*

| Project | Stars | What it does |
|---|--:|---|
| [**kunchenguid/firstmate**](https://github.com/kunchenguid/firstmate) | 8,761 | Supervises coding agents in separate Herdr TUI tabs and isolated Git worktrees. Supports Claude Code, Pi, Codex, OpenCode, and other agent harnesses. |
| [**sisyphuslabs/dori-superagent**](https://github.com/sisyphuslabs/dori-superagent) | 232 | Runs a lead agent and parallel coding lanes in Herdr TUI tabs, with resource guards and a gated merge workflow. |
| [**stevenmichaelthomas/numbrone**](https://github.com/stevenmichaelthomas/numbrone) | 114 | Routes requests through a chief agent to project managers and parallel workers in Herdr TUI workspaces and Git worktrees. |
| [**larcane97/clausona**](https://github.com/larcane97/clausona/blob/main/docs/usecases/herdr-fleet.md) | 61 | Splits a job across Herdr worktrees and panes from one Claude Code or Codex session, routing each worker to one of your accounts by remaining usage or to an API model such as DeepSeek. Part of clausona, a daemon-less multi-account manager that drives Herdr only through its CLI and checks each branch before removing a worktree. |
| [**andrebrov/drover**](https://github.com/andrebrov/drover) | 10 | Coordinates Claude Code, Codex and other agents in Herdr TUI with task dispatch, isolated worktrees and cross-harness review. |
| [**travisjeffery/herdr-quartermaster**](https://github.com/travisjeffery/herdr-quartermaster) | 8 | Coordinates Claude Code, Codex or Muse Code workers in separate Herdr TUI worktrees using beads as the task record. |
| [**vladzima/herd**](https://github.com/vladzima/herd) | 7 | Runs a Claude Code coordinator that delegates tasks to Herdr tabs and collects reports from Claude, Codex, Gemini, or other workers. |
| [**wangfan1998-github/herdr-hybrid**](https://github.com/wangfan1998-github/herdr-hybrid) | 6 | Orchestrates Claude Code hybrid teams with high-tier models supervising parallel worker panes in Herdr. |
| [**igor/crew-skill**](https://github.com/igor/crew-skill) | 5 | Coordinates a fleet of AI agents in Herdr where premium models lead and local models handle volume execution. |
| [**minhtran3124/Brichan**](https://github.com/minhtran3124/Brichan) | 4 | A repository-local AI chief of staff for Codex. It keeps project work bounded, coordinates Herdr agents, checks outputs, and stores durable project memory. |
| [**zhenyufu/herdr-cadence**](https://github.com/zhenyufu/herdr-cadence) | 3 | Uses a lead agent to sort tasks and start specialized workers in separate Herdr tabs and Git worktrees. It checks for a clean repository state and gives each worker only the context it needs. |
| [**GenaroSalomone/foreman-sh**](https://github.com/GenaroSalomone/foreman-sh) | 3 | Runs a planning agent and isolated worktree executors with reviews and guards for Claude Code and Pi in Herdr. |
| [**GuitarWag/herdr-shepherd**](https://github.com/GuitarWag/herdr-shepherd) | 3 | Runs Claude Code and Codex teams in Herdr TUI panes with boss and worker roles, team discovery, and messaging. |
| [**Kvmyk/herdr-foreman**](https://github.com/Kvmyk/herdr-foreman) | 2 | Turns one plain-language task into a plan that a lead agent splits across your installed coding agents, each running in its own Herdr pane and git worktree. Workers first only propose changes, and nothing lands on your branch until you approve a numbered list. |
| [**gronare/kebbie**](https://github.com/gronare/kebbie) | 2 | Runs trunk-based development for Claude Code in Herdr: a lead session plans tasks from your backlog, each task gets an agent in its own worktree, and one board shows what each needs from you. Reviewed commits go straight onto main instead of through pull requests. |
| [**ellingtonsp/herdr-orch**](https://github.com/ellingtonsp/herdr-orch) | 2 | Adds a coordination layer on Herdr so one agent runs a team of others: a mailbox, blocking ask and reply, tasks with dependencies, tracked dispatch, decision gates and verified worker release. Agents and you drive it through the horch CLI. |
| [**hasuwini77/worktree-fleet**](https://github.com/hasuwini77/worktree-fleet) | 2 | Adds /fleet and /crew skills that split a task into file-disjoint buckets, run one Claude Code or Codex agent per bucket in its own Herdr tab and worktree, and merge the results. Includes a live fleet board popup. |
| [**EvanBatten/firstmate-for-windows**](https://github.com/EvanBatten/firstmate-for-windows) | 2 | Runs Claude Code crewmates in their own Herdr tabs and git worktrees on Windows 11 under Git Bash. Watches the crew and returns finished pull requests and reports. |
| [**inbeomheo/herdr-orchestra**](https://github.com/inbeomheo/herdr-orchestra) | 2 | Coordinates Codex, Grok, Gemini, or Claude worker panes from a central Claude Code controller session. |
| [**alexhooi/herdr-orchestrate**](https://github.com/alexhooi/herdr-orchestrate) | 2 | Runs Claude Code, Codex CLI and pi as visible, interruptible terminal-pane agent teams. One orchestrator, cross-model review, review-gated merges. |
| [**sfrangulov/prorab**](https://github.com/sfrangulov/prorab) | 1 | Turns one Claude Code session into a foreman that issues work orders to crews of Claude Code sessions, each in its own Herdr pane and git worktree. Tracks budgets, answers crew questions, and writes a morning report. |
| [**m-mohamed/sheprd**](https://github.com/m-mohamed/sheprd) | 1 | Keeps Pi, Codex, Claude Code, and OpenCode in one visible, isolated Herdr Flok. |
| [**cowcow02/herdr-agent-orchestrator**](https://github.com/cowcow02/herdr-agent-orchestrator) | 0 | Adds event-driven orchestration around one existing controller agent while Herdr observes and reports the work. It avoids replacing the controller with a separate fleet manager. |
| [**beraterkanelcelik/agent-army**](https://github.com/beraterkanelcelik/agent-army) | 0 | Coordinates parallel coding missions through a three-level agent hierarchy using Claude Code, Herdr, and cursor-agent. |
| [**hung-eggie-do-covergo/delegate-orchestrator**](https://github.com/hung-eggie-do-covergo/delegate-orchestrator) | 0 | Starts one isolated Claude Code subagent per repository through Herdr worktrees, with multi-repository coordination, worktree reuse, and session resumption. |
| [**pparitoshh/herdr-hive**](https://github.com/pparitoshh/herdr-hive) | 0 | Runs one brain agent and several workers per workspace, each worker in its own git worktree, talking over a local SQLite message bus. A review bench tab shows each worker's diff. |
| [**pelayomendez/watchmen**](https://github.com/pelayomendez/watchmen) | 0 | Keeps a long-lived Claude Code companion session beside your work that tracks tickets, merge requests, and worker sessions. In Herdr it summons the session and shows a sidebar token. |
| [**Sakib75/herdr-hq**](https://github.com/Sakib75/herdr-hq) | 0 | Opens one Claude Code agent in a Herdr TUI popup that hands your requests to the agents already working in your tabs and follows up on them. |
| [**heywji/aiboard**](https://github.com/heywji/aiboard) | 0 | Splits a task into lanes that Claude Code hands to Codex, Grok, Kimi, Gemini and Claude, each running headless in a Herdr pane you can take over. Passes work between models as files and sends security findings to another vendor for review. |
| [**zenodea/lodestar**](https://github.com/zenodea/lodestar) | 0 | Lets one leader agent split a request into tasks, start crewmate agents, and merge their results, inside Herdr, tmux, or Rex. Mixes Claude Code, Codex, and pi. |

### Fleet control planes and CLI harnesses

*40 projects. Standalone CLIs, daemons, SDKs and harnesses outside any agent session that start, track and supervise whole fleets of coding agents through Herdr; the program, not an agent, is in charge.*

| Project | Stars | What it does |
|---|--:|---|
| [**meviusisback/agent-orchestr**](https://github.com/meviusisback/agent-orchestr) | 19 | Monitors live agent output and orchestrates multi-agent workspaces across Herdr, OpenCode, and Claude sessions. |
| [**mupt-ai/context-drop**](https://github.com/mupt-ai/context-drop) | 19 | Provides a Herdr-backed meta-harness for orchestrating autonomous coding agents. |
| [**machine-machine/herdr-factory-loop-skill**](https://github.com/machine-machine/herdr-factory-loop-skill) | 11 | Orchestrates coding-agent fleets in Herdr TUI, spawning workers, dispatching tasks, monitoring status, and coordinating fan-out and convergence. |
| [**hapo-nghialuu/hod**](https://github.com/hapo-nghialuu/hod) | 6 | Coordinates Codex, Claude Code, and Grok Build agents safely through Herdr. |
| [**ohitslaurence/herdr-fleet**](https://github.com/ohitslaurence/herdr-fleet) | 3 | Runs coding agents in Herdr TUI worktrees and tracks their tasks and pull requests through review and CI. |
| [**ShenghaiWang/helm**](https://github.com/ShenghaiWang/helm) | 2 | Provides an agent harness on top of Herdr for coordinating coding workflows. |
| [**hkandala/orchestratr**](https://github.com/hkandala/orchestratr) | 2 | Runs and schedules Claude, Codex, and other coding agents in Herdr through a CLI, TypeScript SDK, or installable skill. |
| [**LittleDrinks/oh-my-herdr**](https://github.com/LittleDrinks/oh-my-herdr) | 2 | Organizes CLI-agent work in Herdr tabs using reusable delegation, review, and delivery workflows. |
| [**floor/teamcli**](https://github.com/floor/teamcli) | 2 | Runs a roster of agents from different vendors as a team in Herdr panes from a Node CLI. Watches for idle seats and nudges the operator. |
| [**CristianonCarvalho/meisterrouter**](https://github.com/CristianonCarvalho/meisterrouter) | 2 | Splits a plan into tasks and runs them in parallel on Copilot, Claude, Codex, Gemini and Kiro CLIs with a test gate before merge. Can open each worker in a visible Herdr tab as an optional Herdr plugin. |
| [**saxonmurray85-ops/sheprd**](https://github.com/saxonmurray85-ops/sheprd) | 1 | Deploys local llama.cpp models and launches specialized agents into Herdr workspaces through a terminal or web interface. |
| [**ravikanchikare/herdr-agent-factory**](https://github.com/ravikanchikare/herdr-agent-factory) | 1 | Builds and evaluates target agents in a macOS control plane that delegates work to agents in Herdr panes. |
| [**bpcakes/epicd**](https://github.com/bpcakes/epicd) | 1 | Orchestrates Codex work on Beads epics with independent review and resumable native Herdr TUI or SDK sessions. |
| [**slogsdon/herdbot**](https://github.com/slogsdon/herdbot) | 1 | Runs persistent AI bots on your machine, each in its own Herdr workspace, with subagents opened in panes next to them. Routes tasks across Claude, Codex, Cursor, and Pi subscriptions. |
| [**eciuca/herdr-drover**](https://github.com/eciuca/herdr-drover) | 1 | Orchestrates Claude Code, Codex, and Kira CLI agents across tmux-style Herdr workflows. |
| [**sm-yjr/herdr-coordinator**](https://github.com/sm-yjr/herdr-coordinator) | 1 | Coordinates Herdr agent fleets across multiple terminal panes. |
| [**qinglang8609/deepseek_herdr**](https://github.com/qinglang8609/deepseek_herdr) | 1 | Orchestrates multi-agent teams across Claude, OpenCode, and Codex in Herdr using DeepSeek Harness and shared task boards. |
| [**hunaish-dev/nakama**](https://github.com/hunaish-dev/nakama) | 1 | Provides a wrapper, not a harness: coordinates a crew of coding-agent CLIs (starting with Claude Code) on one goal, with live attach via herdr. |
| [**robertdo/claude-herdr-orchestration**](https://github.com/robertdo/claude-herdr-orchestration) | 1 | Uses Claude Code hooks and Herdr TUI orchestration to keep changes in worktrees and route tasks among model tiers. |
| [**WyvernMonarch/herdr-cockpit**](https://github.com/WyvernMonarch/herdr-cockpit) | 1 | Provides a local-first supervision and control layer for Herdr coding agents. |
| [**hao1939/herdr-supervisor**](https://github.com/hao1939/herdr-supervisor) | 1 | Supervises existing Herdr TUI workers against explicit goals and can wake workers when external events change. |
| [**eliebak/herdr-agent-island**](https://github.com/eliebak/herdr-agent-island) | 1 | Coordinates multiple agent loops in separate Herdr panes and tracks their active tasks. |
| [**tamdogood/herdr-orc**](https://github.com/tamdogood/herdr-orc) | 1 | Provides a minimal, profile-driven custom orchestrator for Herdr. |
| [**hewel/herdr-harness-coordinator**](https://github.com/hewel/herdr-harness-coordinator) | 0 | Coordinates autonomous coding-agent harnesses across separate Herdr panes and tracks their active tasks. |
| [**gurronen/herdr-looper**](https://github.com/gurronen/herdr-looper) | 0 | Launches repeatable machine-local Pi jobs in fresh Herdr workspaces and worktrees. |
| [**charlieYong/herdr-live**](https://github.com/charlieYong/herdr-live) | 0 | Orchestrates live multi-agent harnesses in Herdr, dispatching prompts and streaming status outputs. |
| [**leifarriens/shepherd**](https://github.com/leifarriens/shepherd) | 0 | Coordinates coding workers in Herdr with a reusable manager skill, guarded CLI operations, and a task ledger. |
| [**raystyle/evo-harness**](https://github.com/raystyle/evo-harness) | 0 | Coordinates Codex, Kimi, Claude, and Grok through a staged rmux workflow with a Herdr monitor and decision-notification daemon. |
| [**thelad-dev/orchaester**](https://github.com/thelad-dev/orchaester) | 0 | Runs a Herdr TUI orchestration workflow with Grok Build and Cursor using native agent and worktree commands. |
| [**testy-cool/herdr-agent-control**](https://github.com/testy-cool/herdr-agent-control) | 0 | Coordinates Herdr TUI workers using process leases and runbooks to limit delegation drift and unsafe handoffs. |
| [**RodrigoSosa96/workflow-control-plane**](https://github.com/RodrigoSosa96/workflow-control-plane) | 0 | Dispatches Pi, Claude, and Codex workers into isolated Git worktrees and manages their Herdr workspaces and handoffs. |
| [**brenoperucchi/herdr-mesh-tools**](https://github.com/brenoperucchi/herdr-mesh-tools) | 0 | Bootstraps Herdr workspaces and agents, runs parallel reviews, and swaps executors with context handoff. |
| [**w-gitops/herdr-agent-factory**](https://github.com/w-gitops/herdr-agent-factory) | 0 | Launches and coordinates multi-agent teams on Herdr independently of the coding harness. |
| [**OahMoza/herdr-phalanx**](https://github.com/OahMoza/herdr-phalanx) | 0 | Orchestrates multi-agent tasks across parallel Herdr workspaces. |
| [**Ejlonn/herdr-supervisor**](https://github.com/Ejlonn/herdr-supervisor) | 0 | Supervises durable Claude and Codex workflows in Herdr with human approval steps, quota waiting, and remote control through Telegram. Preserves native sessions and rechecks limits without spending tokens. |
| [**chetanunadkat-lang/herdr-fleet**](https://github.com/chetanunadkat-lang/herdr-fleet) | 0 | Runs Claude and Codex workers as a fleet in Herdr panes. The project includes orchestration skills, an `hm` command-line tool, agent definitions, and a Claude Code installer. |
| [**Crush53/pi-herdr-managed-agents**](https://github.com/Crush53/pi-herdr-managed-agents) | 0 | Manages native Pi, Claude Code, and Codex agents in auditable Herdr tabs. |
| [**ykawase1011/hanchou**](https://github.com/ykawase1011/hanchou) | 0 | Provides a durable multi-agent control plane built on Herdr, Beads, Codex, and Claude Code. |
| [**suleymanozkeskin/sheppard**](https://github.com/suleymanozkeskin/sheppard) | 0 | Controls plane with collab & communication tools for agents from multiple harnesses, built on herdr api. |
| [**lucasdeprit/Puppy**](https://github.com/lucasdeprit/Puppy) | 0 | A basic multi-agent system built around Claude Code sessions running in the Herdr terminal. |

### Role-based agent teams with planners and reviewers

*28 projects. Fixed teams where each agent has a named role such as planner, coder, tester or reviewer, with handoffs between roles; the roles, not a lead agent or a program, are the point.*

| Project | Stars | What it does |
|---|--:|---|
| [**wanshuiyin/SuperARIS**](https://github.com/wanshuiyin/SuperARIS) | 73 | Runs a persistent research team in Herdr with a lead agent and engineering and writing roles. |
| [**zanuartri/herdr-rig**](https://github.com/zanuartri/herdr-rig) | 8 | Uses a manager agent to dispatch tickets to workers and reviewers in Herdr TUI or the Herdr app, with an optional desktop board. |
| [**kylezk777/herdr-orchestrator**](https://github.com/kylezk777/herdr-orchestrator) | 7 | Coordinates Herdr agents through file-based tasks, scoped roles, and review gates using an orchestrator-operator pattern. |
| [**SimoneDaniotti/horchestra**](https://github.com/SimoneDaniotti/horchestra) | 5 | Runs orchestrator-led agent teams in Herdr TUI and displays a live agent map in each tab. |
| [**StructuPath/herdr-conductor**](https://github.com/StructuPath/herdr-conductor) | 4 | Coordinates producer and reviewer agents with strict task and report formats, Git compare-and-swap checks, and a passive status board. It is designed for visible, operator-supervised delivery rather than free-form swarming. |
| [**forsakesoul/herdr-nakama**](https://github.com/forsakesoul/herdr-nakama) | 4 | Creates, initializes, and restores Owner, Worker, and Advisor agent teams in Herdr TUI panes. |
| [**TheMickeyDodger/dodging-infinity**](https://github.com/TheMickeyDodger/dodging-infinity) | 3 | Coordinates Herdr engineering agents around approved missions, tracking progress, review evidence, and delivery decisions. |
| [**ankitvashisht12/crew**](https://github.com/ankitvashisht12/crew) | 2 | Coordinates role-based Claude and Codex workflows in named Herdr TUI tabs with durable tasks and isolated worktrees. |
| [**combinaut/ai-agent-orchestration**](https://github.com/combinaut/ai-agent-orchestration) | 2 | Installs a Coordinator, architects and workers team of Claude Code and Codex agents in visible Herdr panes. Includes a Herdr todo plugin and a one-line installer. |
| [**minqiyang/coordination-standard**](https://github.com/minqiyang/coordination-standard) | 2 | Coordinates coding agents in Herdr TUI using defined roles, isolated worker lanes, and review gates. |
| [**neospark-sol/agentflock**](https://github.com/neospark-sol/agentflock) | 1 | Coordinates coding CLI builders and reviewers in persistent Herdr sessions with milestone approval, evidence checks, and recovery. |
| [**0-CYBERDYNE-SYSTEMS-0/herdr-dev-team**](https://github.com/0-CYBERDYNE-SYSTEMS-0/herdr-dev-team) | 1 | Organizes a lead and six scoped workers in Herdr with task packets, worktree isolation, and review gates. |
| [**C1TRuSovo831/herdr-codex-team**](https://github.com/C1TRuSovo831/herdr-codex-team) | 1 | Launches isolated Codex planner, coder, and reviewer teams in Herdr with role prompts and team-scoped routing. |
| [**gilvanecesar/obra**](https://github.com/gilvanecesar/obra) | 1 | Runs Claude Code engineer, QA, reviewer, and pull-request agents in separate Herdr TUI panes and Git worktrees. |
| [**zeromountain/herdr-roles**](https://github.com/zeromountain/herdr-roles) | 1 | Assigns roles to Herdr TUI panes, spawns a team of role panes from the main pane, and hands work between roles. Korean README. |
| [**harry81/herdr-team**](https://github.com/harry81/herdr-team) | 1 | Starts a four-pane planner, worker, and reviewer crew in Herdr with one command. Includes role agents and workflow presets. |
| [**zachristmas/baa-ton**](https://github.com/zachristmas/baa-ton) | 1 | Steers work across Herdr workspaces from a Codex control layer, dispatching Claude Code, Pi, OpenCode, or Codex workers with scoped goals, a CLI, and a stdio MCP server. Setup runs through a reviewed installer. |
| [**kennethgeerts/herdr-architect**](https://github.com/kennethgeerts/herdr-architect) | 1 | Coordinates a Claude Code architect with implementation and independent review agents in separate Herdr tabs. |
| [**rephol/wt-pack**](https://github.com/rephol/wt-pack) | 1 | Runs a team of Claude Code agents that plan, build, review, and ship tickets, each in its own git worktree. Agents run as Herdr panes. |
| [**erdostom/herdr-orchestrate**](https://github.com/erdostom/herdr-orchestrate) | 0 | Runs a Herdr agent fleet with persistent conductor and watcher roles and short-lived OpenCode task workers. |
| [**talberthoule/herdr-shepherd**](https://github.com/talberthoule/herdr-shepherd) | 0 | Coordinates Claude Code and Codex sessions with ownership rules, audited handoffs, and a Herdr TUI skill. |
| [**klahrich/smashhh**](https://github.com/klahrich/smashhh) | 0 | Runs planner, coder, and verifier agents in a Herdr TUI workspace to build a project. |
| [**ahnsv/maeh**](https://github.com/ahnsv/maeh) | 0 | Organizes agent work as plan trees and workspaces with primary and critic agents, using Herdr TUI or tmux as a backend. |
| [**GMakeziG/ninjatronics-ai**](https://github.com/GMakeziG/ninjatronics-ai) | 0 | Coordinates specialist engineering agents through Hermes, Herdr, Claude Code, and Codex. |
| [**mrrobot-ec/pod**](https://github.com/mrrobot-ec/pod) | 0 | Lets a coordinating agent in the Herdr TUI run a team of Claude Code, Codex and Grok workers in their own tabs and worktrees. Adds reviewers, advisors and a board, with usage tracked for Claude and Codex. |
| [**Phoobobo/herdr-bot**](https://github.com/Phoobobo/herdr-bot) | 0 | Runs a team of named Grok or pi bots, such as a lead, engineer and researcher, from an overlay in the Herdr TUI with DMs and channels. Ties each team to one Herdr session and resumes it. |
| [**GustavoGomez092/herdr-dots**](https://github.com/GustavoGomez092/herdr-dots) | 0 | Attaches specialist agents called dots, such as security or frontend reviewers, to Claude Code or Codex sessions in Herdr TUI. Each dot checks every turn and speaks up only when needed, and dots can convene as a council. |
| [**wasamin0130/TeamNestReferenceFlow**](https://github.com/wasamin0130/TeamNestReferenceFlow) | 0 | Runs a six-role team of Claude Code agents in Herdr TUI panes with parallel planning and review waves, handoff files, and an Orchestrator skill. Needs TeamNest and a Team Pack with matching role ids. |

### Agent team definitions and role profiles

*10 projects. Config files, presets and persona profiles that only describe which agents make up a team and how each one behaves, for another tool to launch.*

| Project | Stars | What it does |
|---|--:|---|
| [**chengyixu/oh-my-herdr**](https://github.com/chengyixu/oh-my-herdr) | 97 | Organizes Codex, Pi, and Claude Code profiles with persistent instructions in shared coding spaces using a separate Herdr-derived runtime. |
| [**mikeyobrien/herdr-agent-profiles**](https://github.com/mikeyobrien/herdr-agent-profiles) | 4 | Provides a data-driven command-line harness and reusable model profiles for agents running through Herdr. |
| [**rarce/herdr-crew**](https://github.com/rarce/herdr-crew) | 3 | Starts Claude Code, Codex and Pi roles in Herdr TUI tabs from a versioned crew file and shows a status board. |
| [**yarrasys/herdr-fleet-plugin**](https://github.com/yarrasys/herdr-fleet-plugin) | 1 | Starts, restarts and swaps a named team of coding agents from a per-repository `.herdr/fleet.toml`, tiled into one Herdr workspace. Seats can be Claude, Codex or Gemini; agents message each other with `herdr-fleet send`, and `doctor` checks the fleet and Claude Code permission rules. |
| [**skysilver1223/herdr-agent-harness**](https://github.com/skysilver1223/herdr-agent-harness) | 1 | Creates Ubuntu and WSL projects with role and skill templates for coordinating Claude, Codex, and AGY in Herdr. |
| [**gdli6177/herdr-agent-team**](https://github.com/gdli6177/herdr-agent-team) | 1 | Organizes Herdr agent teams from Markdown definitions. |
| [**huynguyen03dev/herdr-agent**](https://github.com/huynguyen03dev/herdr-agent) | 0 | Supplies lead, peer, and supervisor role profiles and helper scripts for coordinating agents through Herdr TUI panes. |
| [**clawsouls/clawsouls-herdr-plugin**](https://github.com/clawsouls/clawsouls-herdr-plugin) | 0 | Applies ClawSouls persona definitions to agents running in Herdr. It sets role-specific environments and behavioral rules for Claude Code and other supported agents across multiple panes. |
| [**nakamori-naoya/agent-fleet-plugins**](https://github.com/nakamori-naoya/agent-fleet-plugins) | 0 | Controls multi-agent roles, task routing, and Herdr execution using declarative fleet specifications. |
| [**parkbeomsub/herdr_orch**](https://github.com/parkbeomsub/herdr_orch) | 0 | Launches AI agent teams in Herdr with team presets, inter-pane messaging, and worktree isolation. |

### Swarm orchestrators for parallel agent waves

*8 projects. Swarm-style orchestrators that run many agents in parallel waves across Herdr panes, branches or worktrees.*

| Project | Stars | What it does |
|---|--:|---|
| [**vib-z/stampede**](https://github.com/vib-z/stampede) | 10 | Spins up a team of Claude Code, Codex, and Cursor agents run by one lead in Herdr panes or herdr-core terminals, started locally or from a Grok Bot chat over Tailscale. Sends each gate question back to whoever started the job, on macOS and Linux. |
| [**HinchK/stampede**](https://github.com/HinchK/stampede) | 3 | Coordinates coding agents in Herdr TUI with ticket dispatch, independent checks, and a human-controlled integration queue. |
| [**jmcjm/Hivemind**](https://github.com/jmcjm/Hivemind) | 3 | Coordinates a swarm of Claude Code agents in Herdr terminal panels using file-based briefs and asynchronous mail. |
| [**conscientiousness/herdr-pstack-orchestrator**](https://github.com/conscientiousness/herdr-pstack-orchestrator) | 2 | Adds Agent Skills for running visible multi-model coding teams across Pi, Codex and Claude Code in Herdr panes. Adds pstack review loops with a controller and workers. |
| [**tuanhung303/herdr-swarm**](https://github.com/tuanhung303/herdr-swarm) | 1 | Runs agent waves in Herdr pane grids, routes messages through an optional mailbox, and collects results from multiple harnesses. |
| [**bandoyer/swarm-forge-herdr**](https://github.com/bandoyer/swarm-forge-herdr) | 0 | Runs role-based agent swarms in separate Git worktrees with validated handoffs and optional human approval. |
| [**bandoyer/swarm-forge-windows**](https://github.com/bandoyer/swarm-forge-windows) | 0 | Provides a Windows distribution of swarm-forge-herdr for running AI agent swarms on the Herdr runtime. |
| [**burningportra/vibing-with-herdr**](https://github.com/burningportra/vibing-with-herdr) | 0 | Coordinates a same-branch Herdr TUI swarm that drains Beads tasks using exclusive Agent Mail reservations instead of worktrees. |

### Live panes for native Claude Code, Codex and OpenCode subagents

*10 projects. Bridges that show an agent's own built-in teammates and subagents as live Herdr panes instead of hidden background processes.*

| Project | Stars | What it does |
|---|--:|---|
| [**alvinunreal/oh-my-opencode-slim**](https://github.com/alvinunreal/oh-my-opencode-slim) | 10,184 | Assigns OpenCode specialist roles (fixers, librarians, explorers) to dedicated Herdr panes. |
| [**caioniehues/herdmates**](https://github.com/caioniehues/herdmates) | 26 | Runs Claude Code multi-agent teams in Herdr through a teammux translation layer. Teammates work in isolated panes while a mission-control view reports their status and task progress. |
| [**GavinTomlins/herdr-oh-my-agent**](https://github.com/GavinTomlins/herdr-oh-my-agent) | 7 | Mirrors oh-my-openagent delegations into Herdr panes or tabs as they happen. It records live state and full scrollback transcripts, supports split or tabbed layouts, and does not change the agents' execution. |
| [**gustavocaiano/opencode-herdr**](https://github.com/gustavocaiano/opencode-herdr) | 4 | Opens a Herdr pane when OpenCode creates a subagent and attaches the subagent session for live viewing. |
| [**arvkonstantin/herdr-codex-subagents**](https://github.com/arvkonstantin/herdr-codex-subagents) | 4 | Opens temporary read-only Herdr panes for Codex subagents and closes them when their work finishes. |
| [**david-lutz/herdr-claude-teams**](https://github.com/david-lutz/herdr-claude-teams) | 3 | Maps Claude Code's experimental agent-team commands to Herdr's socket API, so teammates open as native Herdr panes instead of tmux panes. It requires Herdr 0.6.10 and supports Herdr metadata, notifications, and sidebar views. |
| [**kamil-pociot/herdr-claude-agents**](https://github.com/kamil-pociot/herdr-claude-agents) | 1 | Shows Claude Code background sessions as Herdr agents, one tab each in the project space. Reports live state and notifications for sessions that run in the Claude daemon. |
| [**ClockworkNet/herdr-claude-tmux-swarm**](https://github.com/ClockworkNet/herdr-claude-tmux-swarm) | 0 | Opens a Claude Code tmux-mode teammate swarm in a split pane beside the spawning Claude pane and closes it when the swarm ends. |
| [**moonquddus/lookout**](https://github.com/moonquddus/lookout) | 0 | Shows each Claude Code subagent and background shell in its own pane with prompt, tool calls, and live output. Closes panes shortly after the work stops. |
| [**aalvarezdeliveryhub/herdr-lock**](https://github.com/aalvarezdeliveryhub/herdr-lock) | 0 | Makes every worker agent that Claude Code starts open in its own tab of the same Herdr TUI workspace and folder as the session that spawned it. |

### Task delegation to other coding agents

*24 projects. Tools and skills that let one agent hand a single task to a separate agent in another pane or tab and get the result back, without a standing lead, fleet or team.*

| Project | Stars | What it does |
|---|--:|---|
| [**afogel/shepherdr**](https://github.com/afogel/shepherdr) | 11 | Dispatches Claude, Codex, and Cursor coding subagents into visible Herdr TUI panes and lets users resume completed sessions. |
| [**transparent-pegasus/herdr-orchestration**](https://github.com/transparent-pegasus/herdr-orchestration) | 10 | Routes coding and review work to sibling Herdr TUI panes using configurable agent roles and composer-safe delegation. |
| [**scotthuang/agent-knock-knock**](https://github.com/scotthuang/agent-knock-knock) | 7 | Lets OpenClaw, Pi or DeepSeek Harness delegate to existing Claude Code and Codex sessions in Herdr TUI and follow their progress. |
| [**jeffory/herdr-walkietalkie**](https://github.com/jeffory/herdr-walkietalkie) | 5 | Delegates work from an orchestrator to Claude, OpenCode, or Antigravity sessions in separate Herdr tabs and worktrees. File-based handoffs and completion signals return results to the parent. |
| [**IsaiasZc/herdr-a2a**](https://github.com/IsaiasZc/herdr-a2a) | 5 | Delegates tasks to Codex, Claude, or OpenCode agents in Herdr through a CLI or the A2A protocol. |
| [**justn-hyeok/brgr**](https://github.com/justn-hyeok/brgr) | 5 | Lets a Codex or Claude Code session hand tasks to Claude Code, Codex, Gemini CLI, Copilot CLI, OpenCode, Pi, and other workers in split Herdr panes, answering their trust and update prompts. Each result comes back sealed for the lead agent to accept or reject; deciding closes the pane and removes the worktree when nothing would be lost. |
| [**anhnd3005-infinity/herdr-worker-orchestrator**](https://github.com/anhnd3005-infinity/herdr-worker-orchestrator) | 4 | Dispatches tasks to CLI agent workers via Herdr panes with stateful task tracking, worktree isolation, and diff-based review. |
| [**zqkra/cbds**](https://github.com/zqkra/cbds) | 2 | Dispatches tasks between Herdr agent panes and records durable worker reports with bounded waits for results. |
| [**arDaraz/crewboss**](https://github.com/arDaraz/crewboss) | 1 | Spawns and supervises coding agents in separate Herdr windows and Git worktrees, with commands to wait, message, and reopen them. |
| [**KarthusLorin/herdr-turn-coordinator**](https://github.com/KarthusLorin/herdr-turn-coordinator) | 1 | Runs an interactive agent turn in a separate Herdr pane and waits locally for the result without repeated model polling. |
| [**peterferguson/herdr-herd-flow**](https://github.com/peterferguson/herdr-herd-flow) | 1 | Routes handoffs to Claude, Codex, or OpenCode and launches each in a named Herdr tab, optionally in a worktree. |
| [**asermax/herdr-subagents**](https://github.com/asermax/herdr-subagents) | 1 | Lets Claude Code and Pi delegate work to other coding agents spawned as Herdr tabs. |
| [**machine-machine/ask-fable-skill**](https://github.com/machine-machine/ask-fable-skill) | 1 | Delegates tasks from Hermes or Claude Code to a Claude Code Fable 5 worker in a separate Herdr pane. |
| [**EDMND-SRC/herdr-subagents**](https://github.com/EDMND-SRC/herdr-subagents) | 1 | Starts subagents in named Herdr panes. It includes automatic interception, delegation tools, and a grid layout that adapts as workers are added. |
| [**maccie01/herdr-axi**](https://github.com/maccie01/herdr-axi) | 1 | Delegates and supervises tasks across Herdr worker tabs with bounded concurrency and recoverable handoffs. |
| [**GODVvVZzz/herdr-agent-chat**](https://github.com/GODVvVZzz/herdr-agent-chat) | 1 | Lets a main Claude Code session delegate work to persistent worker agents in sibling panes or other workspaces without blocking. Workers report back over a message channel and a watcher flags workers that die. |
| [**ahqrt/dsh-herdr**](https://github.com/ahqrt/dsh-herdr) | 1 | Delegates DeepSeek Harness subtasks to coding agents running in Herdr panes, then collects the exact results for review in DSH. Lets you pick the model and keep the terminal visible. |
| [**Arluigi/my-skills · herdr-delegate**](https://github.com/Arluigi/my-skills/tree/HEAD/herdr-delegate) | 1 | Lets an expensive model orchestrate cheaper Claude, GPT, and Gemini helpers, each shown as a Herdr pane nested under its orchestrator. Includes a Herdr plugin panel and usage-aware routing. |
| [**fveracoechea/operator**](https://github.com/fveracoechea/operator) | 1 | Adds skills and a CLI that let one coordinating agent dispatch worker agents in OpenCode and Claude Code through Herdr. Tracks assignments, worktrees, pull requests, and reports so each agent gets its next action. |
| [**patraianton/teammate**](https://github.com/patraianton/teammate) | 0 | Provides one coding agent hires another, a worker Claude Code session in its own herdr tab, with a written brief, a one-line status contract, and a close that refuses to destroy unfinished work. |
| [**SynthSwarm/herdr-envoy**](https://github.com/SynthSwarm/herdr-envoy) | 0 | Delegates tasks to peer OpenCode agents in isolated Git worktrees and Herdr panes or child workspaces. |
| [**vivainio/cop-pilot**](https://github.com/vivainio/cop-pilot) | 0 | Delegates coding tasks to GitHub Copilot CLI agents in Herdr panes and collects their results asynchronously. |
| [**shimo4228/herdr-toolkit**](https://github.com/shimo4228/herdr-toolkit) | 0 | Starts detached Claude Code sessions in Herdr panes and sends prompts to agents with delivery and completion checks. |
| [**ViSHNUPrABU/herdr-codex**](https://github.com/ViSHNUPrABU/herdr-codex) | 0 | An unofficial Herdr-related Codex project. The source catalog contains only version, license, and non-affiliation notices, with no feature description. |

### Task routers that pick the agent and model

*8 projects. Routers that look at a task and choose which coding agent, model and effort level should run it in a new Herdr pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**nidhi-singh02/agent-router**](https://github.com/nidhi-singh02/agent-router) | 124 | Routes tasks to Cursor, Claude Code, Codex or OpenCode and launches the selected agent in a Herdr TUI pane. |
| [**JosssphZhou/azir-dispatch**](https://github.com/JosssphZhou/azir-dispatch) | 6 | Routes tasks to coding agents in Herdr TUI using JEV and tracks dispatches and completions on a terminal board. |
| [**sirkirby/routr**](https://github.com/sirkirby/routr) | 4 | Routes coding tasks to Claude Code, Codex, Cursor, Antigravity and Kiro workers in Herdr TUI panes or Herdr app tabs. |
| [**flaviomartil/herdr-jev**](https://github.com/flaviomartil/herdr-jev) | 3 | Routes tasks to coding agents in Herdr TUI panes using Jev triage and AI Harness execution profiles. Runs implementation and independent review stages with optional verification commands. |
| [**Qingswe/herdr-router**](https://github.com/Qingswe/herdr-router) | 2 | Picks the coding agent, model and reasoning effort for a task from an editable difficulty policy, then starts that agent in a new Herdr pane and sends the task. Explains each decision and includes a web policy editor. |
| [**SuperInstance/herdr-cocapn**](https://github.com/SuperInstance/herdr-cocapn) | 1 | Provides herdr + cocapn-core: agent multiplexer meets fleet management. Automatic tier escalation and deadband triggers for herdr agents. |
| [**boriscardano/herdr-jev-router**](https://github.com/boriscardano/herdr-jev-router) | 1 | Lets a parent agent describe a task and have the Jev routing service pick the harness, model and effort for the child agent from the task and remaining subscription capacity. Needs a TypeSafe API key, installs with herdr plugin install and is advisory only. |
| [**candidosales/herdr-laya-router**](https://github.com/candidosales/herdr-laya-router) | 0 | Classifies a task with a local Laya model, then picks Claude Code, Codex, or OpenCode plus model and effort and launches it in Herdr. Runs classification on your machine. |

### Popup pickers that launch a coding agent in a new tab

*16 projects. Popups, sidebars and key bindings that pick a project and agent and start it in a new Herdr tab, split or worktree.*

| Project | Stars | What it does |
|---|--:|---|
| [**cloudmanic/herdr-plus**](https://github.com/cloudmanic/herdr-plus) | 379 | A plugin with two launchers: TOML project templates that build complete workspaces from a fuzzy picker, and Quick Actions for running reusable scripts in the current directory. Prebuilt binaries are available. |
| [**hanbong5938/herdr-tab-autorun**](https://github.com/hanbong5938/herdr-tab-autorun) | 4 | Starts a configured shell command or coding agent in new Herdr TUI tabs using repository-scoped TOML rules. |
| [**FunnyQ/q-workbench**](https://github.com/FunnyQ/q-workbench) | 1 | Launches Claude Code, Codex, and OpenCode in Herdr TUI layouts and offers project and SSH pickers and agent restart actions. |
| [**impeterwayne/herdr_launcher**](https://github.com/impeterwayne/herdr_launcher) | 1 | Opens a toggleable sidebar to launch coding agents in Herdr TUI. |
| [**ZviBaratz/herdr-draft**](https://github.com/ZviBaratz/herdr-draft) | 1 | Provides a new-session creation dialog unifying Linear issues, worktree creation, agent types, and initial prompts. |
| [**ningxiaoxiao/herdr-agent-picker**](https://github.com/ningxiaoxiao/herdr-agent-picker) | 1 | Enables the user choose an AI agent and working directory before Herdr creates a new tab, split, or workspace. |
| [**softwarecrafts/herdr-tab-new**](https://github.com/softwarecrafts/herdr-tab-new) | 0 | Starts or resumes an agent session in the Herdr TUI workspace matching the current project, from a plugin or standalone CLI. |
| [**MomePP/herdr-agent-tab**](https://github.com/MomePP/herdr-agent-tab) | 0 | Opens a coding agent in a new tab of the current herdr space, on the checkout or a fresh git worktree. |
| [**leonho/herdr-new-task**](https://github.com/leonho/herdr-new-task) | 0 | Picks a project directory and starts a coding agent in a new Herdr TUI tab. |
| [**abet-v/omarchy-herdr-prompt**](https://github.com/abet-v/omarchy-herdr-prompt) | 0 | Opens a centered prompt overlay to start a Claude agent in a Herdr workspace. |
| [**charlesberret/herdr-cowbell**](https://github.com/charlesberret/herdr-cowbell) | 0 | Opens a popup picker that launches or relaunches a coding agent in the current directory with chosen settings and shows the exact command first. Can also bind itself to a Herdr key. |
| [**Taanviir/herdr-quick-prompt**](https://github.com/Taanviir/herdr-quick-prompt) | 0 | Picks a coding agent and prompt with one key, then launches it in a new tab, split, workspace, or worktree. Can also send follow-ups to a running agent. |
| [**AnnanKhan/herdr-agent-launcher**](https://github.com/AnnanKhan/herdr-agent-launcher) | 0 | Adds a clickable agent-launcher pane. Left-click starts the configured default agent, while right-click opens the full list. |
| [**daltonkyemiller/herdr-plugin-switchboard**](https://github.com/daltonkyemiller/herdr-plugin-switchboard) | 0 | Launches Claude, Codex, OpenCode, or Pi from a picker and switches between the remembered agent and the active pane. |
| [**lucasleon2107/herdr-claude-launcher**](https://github.com/lucasleon2107/herdr-claude-launcher) | 0 | Opens a new Herdr tab with Claude Code already running. |
| [**spro/herdr-agent-launcher**](https://github.com/spro/herdr-agent-launcher) | 0 | Opens a named Herdr tab running a selected Claude model. |

### Scripts that spawn grids of agents in worktrees

*7 projects. Scripts and commands that start several agents at once in a pane grid or one worktree each, then track and collect their results.*

| Project | Stars | What it does |
|---|--:|---|
| [**richardadonnell/herdr-claude-manager**](https://github.com/richardadonnell/herdr-claude-manager) | 1 | Tiles and manages an N-agent grid of labeled Claude Code panes on Windows and macOS, with menu commands to list, resume, and stop workspaces. |
| [**varvand/herdr-plugin-agent-spawn**](https://github.com/varvand/herdr-plugin-agent-spawn) | 1 | Opens several panes of one coding agent from a single prompt like claude 3 in a popup, tiled in a new tab with Herdr agent names. |
| [**aboufama/claude-agents-tmux**](https://github.com/aboufama/claude-agents-tmux) | 0 | Runs Claude Code agents side by side in persistent project workspaces using Herdr TUI or tmux. |
| [**noor-latif/herd**](https://github.com/noor-latif/herd) | 0 | Two scripts that create a project-specific Herdr workspace with a configurable grid of Pi agents. The workspace follows the current directory and restarts dead agents when the project is reopened. |
| [**JLighter/herdr-spawn**](https://github.com/JLighter/herdr-spawn) | 0 | Starts coding agents in separate Herdr panes and creates an isolated Git worktree for each one. Commands are provided for assigning work, checking jobs, and collecting completed results. |
| [**mahirocoko/direct-cli-skill**](https://github.com/mahirocoko/direct-cli-skill) | 0 | Runs Cursor, Antigravity, Codex, or Pi in visible Herdr panes and falls back to tmux when Herdr is unavailable. |
| [**AndreGeng/herdr-worktree-dispatcher**](https://github.com/AndreGeng/herdr-worktree-dispatcher) | 0 | Dispatches coding tasks into temporary Git worktrees and starts an agent in each checkout. The public entry point is `scripts/dispatch.sh`, backed by a compiled TypeScript command-line implementation. |

### Sending agent tasks to other machines and clusters

*4 projects. Tools that send agent tasks to agents on other machines, SSH hosts or Slurm compute clusters and bring back the results.*

| Project | Stars | What it does |
|---|--:|---|
| [**Northern-Lighthouse/herdr-fleet**](https://github.com/Northern-Lighthouse/herdr-fleet) | 7 | Manages a fleet of herdr machines over Tailscale: dashboard plugin, auto-discovery, capacity-aware agent dispatch, diskless workspaces. |
| [**quan-meng/herdr-slurm**](https://github.com/quan-meng/herdr-slurm) | 3 | Connects Slurm allocations to Herdr by creating dedicated workspaces and monitored agent tabs for compute jobs. It tracks queue state and reports job and agent progress in the terminal. |
| [**Jiaofeisiling/herdr-task-bridge**](https://github.com/Jiaofeisiling/herdr-task-bridge) | 1 | Bridges Windows and NeSI Herdr Sentinel tasks with asynchronous delegation, an SQLite queue, and a PowerShell CLI. |
| [**flotob/herdr-peer**](https://github.com/flotob/herdr-peer) | 1 | Sends tasks to existing Herdr agents on other machines over SSH and retrieves explicit replies. |

### Handoffs of work and context between agent panes

*6 projects. Tools that pass a conversation, plan or last answer from one agent pane to another agent, or to a different agent CLI, with context.*

| Project | Stars | What it does |
|---|--:|---|
| [**sanirudh17/herdr-agent-handoff**](https://github.com/sanirudh17/herdr-agent-handoff) | 22 | Moves an active coding conversation to a new session using another installed agent CLI. The complete transcript and command history are passed to the replacement agent, avoiding a manual handoff summary. |
| [**fuad-daoud/relay**](https://github.com/fuad-daoud/relay) | 1 | Automates the plan/report handoff between planner and builder AI coding agent panes running under herdr. |
| [**devops-fj/herdr-handoff**](https://github.com/devops-fj/herdr-handoff) | 1 | Previews and sends terminal output and Git context between Herdr agents after explicit confirmation. |
| [**doggyfish/herdr-tuple-plugin**](https://github.com/doggyfish/herdr-tuple-plugin) | 0 | Provides a herdr plugin that pairs two coding agents side by side in one tab and moves text between them. |
| [**TeXmeijin/herdr-codex-handoff**](https://github.com/TeXmeijin/herdr-codex-handoff) | 0 | Transfers active sessions directly to Codex in adjacent panes when Claude hits usage limits. |
| [**abroller666/agent-relay**](https://github.com/abroller666/agent-relay) | 0 | Sends the last finished answer of the agent in one Herdr TUI pane, plus your instruction, to the agent in another pane. Supports Claude Code, Codex and Devin CLI on either side. |

### Terminal dashboards and mission-control tabs for agent fleets

*23 projects. Panes, tabs and boards in Herdr TUI that show every agent's state, tasks and blockers in one live overview.*

| Project | Stars | What it does |
|---|--:|---|
| [**deimantasnork/captains-deck**](https://github.com/deimantasnork/captains-deck) | 74 | Displays a read-only Firstmate flow kanban board inside Herdr TUI. |
| [**jeffarese/herdr-agent-grid**](https://github.com/jeffarese/herdr-agent-grid) | 22 | Shows agents, subagents, messages, status, and API cost in a Herdr TUI panel and jumps to selected panes. |
| [**mohseenrm/zj-agent-mob**](https://github.com/mohseenrm/zj-agent-mob) | 12 | Monitors coding agent fleets with Herdr-inspired workflows and pane observation. |
| [**crestai-labs/feld**](https://github.com/crestai-labs/feld) | 10 | Tracks and controls Claude Code and Codex sessions in Herdr with a shared timeline, messages, and scheduled jobs. |
| [**neptunix/corral**](https://github.com/neptunix/corral) | 10 | Provides a kanban dashboard and control surface for Claude Code sessions running in herdr. |
| [**calebcauthon/herdr-birdseye**](https://github.com/calebcauthon/herdr-birdseye) | 5 | Shows an overview of active agents across Herdr panes. |
| [**NexorPL/herdr-jarvis**](https://github.com/NexorPL/herdr-jarvis) | 3 | Shows Herdr TUI projects, agent states, threads, timelines and token costs in a mission-control tab. |
| [**carsonjones/herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard) | 2 | Lists live Herdr agent status in a Bun and React/OpenTUI dashboard that can run as a plugin action or standalone terminal app. |
| [**Dtenwolde/herdr-orchestrator**](https://github.com/Dtenwolde/herdr-orchestrator) | 1 | Shows a live priority board of Herdr workspaces, agents, git state, and GitHub PRs ranked by what needs you next. Pairs it with a read-only Claude Code session that keeps a TODO and writes a morning briefing. |
| [**JasonBates/agentdeck-rs**](https://github.com/JasonBates/agentdeck-rs) | 1 | Provides a local, model-enriched control surface for people running several coding agents at once. |
| [**zyrre/corgi**](https://github.com/zyrre/corgi) | 1 | Shows a dashboard card per project in Herdr with its supervisor's latest message and worker states, naming every blocked worker. Adds a supervisor that runs them and an Omarchy bar widget. |
| [**mandoworks/roostr**](https://github.com/mandoworks/roostr) | 0 | Opens a live board pane with one row per agent showing tag, name, model, state, and blocked alerts. Adds context compaction warnings, task editing, and workspace recovery with backups. |
| [**mvschwarz/herdr-openrig**](https://github.com/mvschwarz/herdr-openrig) | 0 | Opens an OpenRig agent team's operator and advisor from Herdr, shows what needs you, follows tasks between agents, and sends messages to any agent. |
| [**Tatendaz/mission-control**](https://github.com/Tatendaz/mission-control) | 0 | Provides a self-updating project radar for solo devs: swept from git, PRs, Claude session logs and a watch-dictated idea inbox; launches agents into herdr straight from the board. |
| [**MartinBspheroid/herdr-agent-dash**](https://github.com/MartinBspheroid/herdr-agent-dash) | 0 | A local, keyboard-first agent board showing active workers, semantic state, effective directory, Git context, and source-labelled activity. |
| [**Edvardunsvag/herdr-sidebar**](https://github.com/Edvardunsvag/herdr-sidebar) | 0 | Shows a narrow Herdr TUI status board for work awaiting attention in a right-hand pane. |
| [**ArtMoreno/herdr-glance**](https://github.com/ArtMoreno/herdr-glance) | 0 | Provides a live agent dashboard for Herdr, with five themes and a fast prompt segment. |
| [**GranamyrBR/ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr) | 0 | Shows live agent activity and offers pane controls in Herdr. |
| [**alexiob/herdr-prism**](https://github.com/alexiob/herdr-prism) | 0 | Opens an eight-view dashboard in the Herdr TUI for Codex, Claude Code, and Pi sessions with agent trees, CPU and memory, processes, git changes, usage limits, and private Markdown notes. Can collect data locally or on each SSH server. |
| [**harshad22491/herdr-agentpanel**](https://github.com/harshad22491/herdr-agentpanel) | 0 | Shows Herdr workspace readiness, agent activity, and quota readings in a Windows dashboard. |
| [**heysanil/herdash**](https://github.com/heysanil/herdash) | 0 | Shows Herdr agent lifecycle states grouped by repository in a terminal dashboard with LLM-generated activity summaries. |
| [**im-tabr/herdr-command-center**](https://github.com/im-tabr/herdr-command-center) | 0 | Shows Herdr TUI workspaces and agent jobs in an animated pane, with attention indicators and shortcuts to selected agents. |
| [**orascope/herdr-tower**](https://github.com/orascope/herdr-tower) | 0 | Shows on one screen which Claude Code, Codex, Gemini, and opencode agents in Herdr TUI are working, waiting for you, or finished. Requires Herdr TUI 0.9.0 or newer. |

### Side panels with worktree, PR and diff cards per agent

*6 projects. Side panels that attach to a Herdr agent and show its worktree, branch, pull request and CI status, changed files and subagents next to the conversation.*

| Project | Stars | What it does |
|---|--:|---|
| [**minhtran3124/herdr-worktree-agents**](https://github.com/minhtran3124/herdr-worktree-agents) | 7 | Shows worktrees, agent states, pull-request checks and Git status in a Herdr TUI panel. |
| [**BjoernSchotte/agentglass-herdr**](https://github.com/BjoernSchotte/agentglass-herdr) | 3 | Opens agentglass in a Herdr TUI popup and adds workspace cost and agent alert indicators to the sidebar. |
| [**minhtran3124/herdr-sidekick**](https://github.com/minhtran3124/herdr-sidekick) | 1 | Adds side panels for parallel coding agents in Herdr TUI: worktree cards with PR and CI status, changed files with diffs, and Claude Code subagents. |
| [**patrikbraborec/herdr-agent-panel**](https://github.com/patrikbraborec/herdr-agent-panel) | 1 | Attaches a live side panel to an agent pane in Herdr TUI that shows session state, context usage, skills, and diffs of changed files. Reads the Claude Code transcript. |
| [**inkayat/firstpane**](https://github.com/inkayat/firstpane) | 0 | Opens a Herdr TUI pane that groups agents by project and shows each one's workspace changes and PR in a Review tab with numbered diffs. Adds a shell in the agent's directory and a browser. |
| [**kristaxox/herdr-agent-dashboard**](https://github.com/kristaxox/herdr-agent-dashboard) | 0 | Shows Claude Code agents in the Herdr TUI as a topology of cards by repository and worktree. Each card has status, current activity, model, branch, PR and CI state. |

### Durable mailboxes and message queues for agents

*13 projects. Persistent mailboxes, queues and message buses that store messages for agents in different Herdr panes and wake the recipient when one arrives.*

| Project | Stars | What it does |
|---|--:|---|
| [**detailles/AgentRadio**](https://github.com/detailles/AgentRadio) | 7 | Sends direct messages between agents in Herdr panes through a local SQLite-backed relay. |
| [**barkerja/herdr-msg**](https://github.com/barkerja/herdr-msg) | 2 | Adds persistent mailboxes for agents in Herdr TUI and notifies recipient panes when messages arrive. |
| [**SimonMallas/agent-letterbox-herdr**](https://github.com/SimonMallas/agent-letterbox-herdr) | 1 | Lets mixed coding-agent teams exchange durable, queryable letters and wake recipients for coordination in Herdr. |
| [**avery20024/herdr-async-message-relay**](https://github.com/avery20024/herdr-async-message-relay) | 1 | Queues messages between Herdr agents in SQLite and delivers each one when the recipient role is idle. Routes by stable role name and includes a terminal UI for message history. |
| [**est7/herdr-amq-adapter**](https://github.com/est7/herdr-amq-adapter) | 1 | Lets coding agents in Herdr TUI panes message each other by name over AMQ with no manual setup. Wakes the receiving agent through herdr agent prompt. |
| [**youssef-tharwat/agent-mail**](https://github.com/youssef-tharwat/agent-mail) | 1 | Gives Codex and Claude Code agents local task assignment, messages, and review cycles stored in SQLite, with optional Herdr TUI delivery that wakes the right agent pane. Ships a Herdr plugin manifest. |
| [**viswassaripalli/agxchat**](https://github.com/viswassaripalli/agxchat) | 1 | Lets Claude and Codex sessions in different repos send each other threaded requests through a local mailbox, with Herdr waking the target pane and a terminal view of threads. Includes deadlock guards and stall detection. |
| [**phillipleblanc/ad**](https://github.com/phillipleblanc/ad) | 1 | Sends messages between local Herdr agent tabs through a filesystem mailbox. |
| [**dcadenas/kelpie**](https://github.com/dcadenas/kelpie) | 0 | Adds durable inter-agent messaging, reminders, and recovery for agents running in Herdr TUI. |
| [**cabra-lat/herdr-plugin-amq**](https://github.com/cabra-lat/herdr-plugin-amq) | 0 | Coordinates turn-based coding agents with Maildir messaging, lifecycle-aware doorbells, a task bus, and a content-addressed evidence store. Adds a web dashboard for mail threads and agent presence. |
| [**husniadil/herdr-mail**](https://github.com/husniadil/herdr-mail) | 0 | Sends asynchronous messages between agents in Herdr TUI panes, with tracked asks and replies and pane delivery markers. |
| [**feelautom/herdr-reliable-messaging**](https://github.com/feelautom/herdr-reliable-messaging) | 0 | Delivers long messages to named Herdr panes with verification that the terminal actually submitted them, so a Codex composer does not keep staged text. Windows only and ships an agent skill. |
| [**adihex/herdr-ipc**](https://github.com/adihex/herdr-ipc) | 0 | Adds workspace-scoped Unix-socket messaging for pane workers, carrying blocker reasons, artifacts, and handoffs beyond Herdr's lifecycle states. Also ships an Agent Plugin manifest with hooks. |

### Peer messaging, mentions and relays between agent panes

*12 projects. Direct agent-to-agent messaging between Herdr panes through call signs, named mentions, peer discovery, relays and gateways, without a stored mailbox as the main idea.*

| Project | Stars | What it does |
|---|--:|---|
| [**junghan0611/entwurf**](https://github.com/junghan0611/entwurf) | 34 | Connects Pi, Claude Code, Codex, Copilot, OMP, and Antigravity sessions in Herdr or tmux so they can address, message, and open visible siblings without sharing auth, tools, or transcripts. Includes a Herdr integration for pi and Claude Code. |
| [**ericbust/namedrop**](https://github.com/ericbust/namedrop) | 23 | Sends named mentions between agents in Herdr TUI panes and workspaces. |
| [**aashishd/herdr-agent-messenger**](https://github.com/aashishd/herdr-agent-messenger) | 9 | Defines a small messaging protocol for agents in separate Herdr panes. Peers use memorable call signs and exchange focused one-line messages, allowing coordination without sharing complete session histories. |
| [**agentwireprotocol/awp · plugin/herdr**](https://github.com/agentwireprotocol/awp/tree/main/plugin/herdr) | 8 | Connects Herdr TUI agents to Agent Wire Protocol messaging with inbox panes, notifications and idle-agent delivery. |
| [**LZHcode1986/herdr-link**](https://github.com/LZHcode1986/herdr-link) | 4 | Connects agents in a Herdr workspace for peer discovery, typed messages, agent startup, and pane cleanup. |
| [**alexlayton/herdr-bots**](https://github.com/alexlayton/herdr-bots) | 1 | Lets coding agents in Herdr TUI panes find each other, send messages, and delegate tasks. Nudges an idle bot by typing a one-line prompt into its pane. |
| [**Liquescent-Development/herdr-a2a**](https://github.com/Liquescent-Development/herdr-a2a) | 1 | Connects Pi agents in a Herdr TUI workspace through an A2A broker for peer messages, replies, and team coordination. |
| [**Luisotee/agent-mesh**](https://github.com/Luisotee/agent-mesh) | 0 | Lets a Claude Code or Antigravity session hand work in another repository to an agent running inside it, in its own Herdr pane and Git worktree, with mailbox messaging both ways. Larger tasks go through planning, approval, and pull-request review by Claude, Antigravity, or Copilot, and a bundled Herdr plugin sends desktop notifications. |
| [**SRHSolution/srh-session-broker**](https://github.com/SRHSolution/srh-session-broker) | 0 | Lets Claude Code and Codex sessions hand work to each other by name or role, typing the message into the target Herdr pane. Adds a safety gate for risky requests, an MCP server, and a terminal and web dashboard. |
| [**nativestrider/herdr-mesh-safe**](https://github.com/nativestrider/herdr-mesh-safe) | 0 | Exposes lease-scoped Herdr agent coordination through MCP while restricting arbitrary commands and unscoped deletion. |
| [**simozampa/agent-relay**](https://github.com/simozampa/agent-relay) | 0 | Provides a secure, asynchronous MCP gateway for persistent coding agents. |
| [**AgentWorkforce/herdr-relay-bridge**](https://github.com/AgentWorkforce/herdr-relay-bridge) | 0 | A relay bridge intended to connect Herdr agents as a cooperating team. The source catalog gives no further protocol details. |

### Shared chat rooms and group channels for agent teams

*8 projects. Shared rooms, boards and group chats where several agents in one Herdr session post to a common log and read what the others said.*

| Project | Stars | What it does |
|---|--:|---|
| [**vitalysim/herdr-synapse**](https://github.com/vitalysim/herdr-synapse) | 16 | Coordinates coding agents in a Herdr TUI session with a shared board and idle-gated message delivery. |
| [**sting8k/pi-peer**](https://github.com/sting8k/pi-peer) | 8 | Lets Pi sessions exchange peer messages and read recent conversation events within a shared Herdr TUI workspace. |
| [**marcvermeeren/chatter**](https://github.com/marcvermeeren/chatter) | 7 | Coordinates Claude Code, Codex, Pi, and other agents through shared per-repository chat, tasks, and memory in Herdr. |
| [**andybarilla/herdr-scuttlebutt**](https://github.com/andybarilla/herdr-scuttlebutt) | 6 | Connects agents in a shared Herdr session chat room with a human-readable TUI. |
| [**aliceisjustplaying/swarmchat**](https://github.com/aliceisjustplaying/swarmchat) | 5 | Lets Claude Code and Codex or Astra exchange peer messages in Herdr while a third pane shows their shared log. |
| [**duncanam/mustr**](https://github.com/duncanam/mustr) | 2 | Runs a coordination hub in a Herdr tab per space where Pi agents join with roles, exchange addressed messages and own tasks. Includes a self-contained `mustr --ai-help` reference. |
| [**ndemeshchenko/herdr-peer-chat**](https://github.com/ndemeshchenko/herdr-peer-chat) | 1 | Lets Claude Code and Codex exchange messages in one Herdr tab through the agent API. |
| [**terry-li-hm/herdr-group-chat**](https://github.com/terry-li-hm/herdr-group-chat) | 1 | Provides a shared local Herdr room for Pi, Claude Code, Codex, and Grok Build. |

### Agent networks and meshes across machines and people

*9 projects. Meshes, hosted networks and shared workspaces that let Herdr agents on different machines, and other people's agents, find each other, exchange messages and keep a presence.*

| Project | Stars | What it does |
|---|--:|---|
| [**runchr-works/herdr-mesh**](https://github.com/runchr-works/herdr-mesh) | 13 | Connects multiple Herdr instances into a coordinated mesh over Model Context Protocol. |
| [**Nirvaan05/arda**](https://github.com/Nirvaan05/arda) | 4 | Lets Herdr TUI agents discover peers and exchange work across sessions and machines. |
| [**alepar/herdr-threads**](https://github.com/alepar/herdr-threads) | 3 | Sends durable messages between Claude Code, Codex, Antigravity and Hermes agents across Herdr TUI sessions and machines. |
| [**fab-agent/community**](https://github.com/fab-agent/community) | 3 | Adds teammate presence, departments and direct messages to a Herdr TUI community workspace. |
| [**vibegui/vibebook.dev · herdr-plugin**](https://github.com/vibegui/vibebook.dev/tree/main/herdr-plugin) | 3 | Connects Vibebook rooms to Herdr TUI and opens a Claude Code session for each room. |
| [**candypoets/buzzr**](https://github.com/candypoets/buzzr) | 2 | Mirrors Herdr workspaces and panes into Buzz channels using Nostr identities. It publishes agent availability and routes channel mentions to the correct terminal pane without exposing the user's private key. |
| [**DailybotHQ/herdr-peers**](https://github.com/DailybotHQ/herdr-peers) | 1 | Lets any agent in a Herdr pane ask an agent in another pane or on another machine and get one authorized reply back. |
| [**Mumega-com/herdr-mupot-bridge**](https://github.com/Mumega-com/herdr-mupot-bridge) | 0 | Bridges Mupot and Herdr with flight monitoring, presence reports, and inbox delivery to agent panes. |
| [**muretai/muretai-herdr-plugin**](https://github.com/muretai/muretai-herdr-plugin) | 0 | Gives Herdr TUI agents addresses on the Muretai network so they can exchange signed messages across machines and with other people's agents. Adds an inbox, invites, and send actions. |

### Human-decision queues for blocked agents

*6 projects. Queues and popups that collect the questions and decisions agents need from you so they ask once and keep working, not markers on rows or keys that jump to the blocked agent.*

| Project | Stars | What it does |
|---|--:|---|
| [**catoncat/herdr-trail**](https://github.com/catoncat/herdr-trail) | 9 | Collects shared agent follow-ups and blockers in a memo list that jumps back to the originating Herdr TUI conversation. |
| [**speardragon/herdr-ask-inbox**](https://github.com/speardragon/herdr-ask-inbox) | 3 | Collects blocked Claude `AskUserQuestion` prompts from all Herdr workspaces into one popup, where pending questions can be reviewed and answered safely. |
| [**LeaveMyYard/herdr-inbox**](https://github.com/LeaveMyYard/herdr-inbox) | 2 | Collects the open questions of Claude Code agents running in Herdr into one popup inbox, so agents ask once and keep working while you answer later. Each answer is delivered back to the pane that asked, through an MCP server and Claude Code plugin. |
| [**navishachiku/herdr-mailbox**](https://github.com/navishachiku/herdr-mailbox) | 2 | Gives each receiving agent a mailbox in Herdr so worker reports merge into one stream and decision questions are answered in a side pane instead of interrupting the leader. Ships a send skill and a CLI for claiming, delivering and withdrawing letters. |
| [**aneym/unblock**](https://github.com/aneym/unblock) | 1 | Collects agent requests for human actions in a local queue, with a Herdr TUI launcher and secret handling outside model context. |
| [**timjonez/herd-orchestrator-cli**](https://github.com/timjonez/herd-orchestrator-cli) | 0 | Watches Herdr TUI agents, queues attention events, and notifies you when a human decision is needed. Launches Claude in a new workspace and submits an initial prompt. |

### Second-opinion reviewers in a split pane

*9 projects. A second coding agent opens in a split pane to review the work, diff or comments of the one you are using, and only the findings you adopt go back.*

| Project | Stars | What it does |
|---|--:|---|
| [**overflowy/herdr-adversarial-review**](https://github.com/overflowy/herdr-adversarial-review) | 10 | Provides a Claude Code skill for adversarial code review that spawns an automated reviewer in a Herdr split pane. |
| [**enes/herdr-rooms**](https://github.com/enes/herdr-rooms) | 3 | Opens review rooms where Claude Code or Codex agents review each other in Herdr TUI. |
| [**Elio2000/herdr-peer-review**](https://github.com/Elio2000/herdr-peer-review) | 1 | Starts a second coding agent in a split pane to review the current workspace diff. The tool runs a protected review, revision, and decision loop and includes a Claude Code skill for orchestration. |
| [**goatbjh/pi-herdr-claude-subagents**](https://github.com/goatbjh/pi-herdr-claude-subagents) | 0 | Enables Pi call Herdr-backed Claude sessions directly as an oracle, reviewer, or planner. |
| [**benediktneumayer2-tech/aqt-sensei-herdr**](https://github.com/benediktneumayer2-tech/aqt-sensei-herdr) | 0 | Pairs the focused Herdr agent with a read-only advisor from another vendor and asks you to approve each message in a popup. Logs every step to an evidence ledger. |
| [**maromocooo/herdr-second-opinion**](https://github.com/maromocooo/herdr-second-opinion) | 0 | Opens a second coding agent in a split to review the latest output or diff of the one you work with. Lets you send back only the findings you adopt. |
| [**wazum/herdr-kibitzr**](https://github.com/wazum/herdr-kibitzr) | 0 | Asks your coding agent to review the comments it just wrote, so what explains something stays and the noise goes. A herdr plugin for Claude Code, Codex and any other agent, with no human in the loop. |
| [**mev15/claude-config · skills/codex-review-loop**](https://github.com/mev15/claude-config/tree/HEAD/skills/codex-review-loop) | 0 | Runs external Codex CLI reviews from Claude Code with an interactive Herdr TUI pane or headless `codex exec` and a fix loop. |
| [**loopkeep/herdr-plugin-loopreview**](https://github.com/loopkeep/herdr-plugin-loopreview) | 0 | Integrates the loopreview workflow with Herdr as a plugin. |

### Writer and reviewer agent pairs

*7 projects. Fixed writer-and-reviewer or planner-coder-reviewer pipelines where one agent writes and another reviews in bounded rounds.*

| Project | Stars | What it does |
|---|--:|---|
| [**mikhail-angelov/herdr-review-loop**](https://github.com/mikhail-angelov/herdr-review-loop) | 3 | Automates a repeated cross-review loop in which one agent writes changes and another reviews them inside the same Herdr workspace. |
| [**HYPERVAPOR/herdr-pair-coding**](https://github.com/HYPERVAPOR/herdr-pair-coding) | 1 | Runs worker and reviewer agent pairs in Herdr panes, each pair in its own worktree, with a watchdog that keeps the pair moving. Installs as agent skills and works with pi. |
| [**inxx/herdr-plan-code-review**](https://github.com/inxx/herdr-plan-code-review) | 0 | Spawns a four-pane pipeline in Herdr with Opus planning, Sonnet coding, and Claude plus Codex review. |
| [**thkt/herdr-agentchat**](https://github.com/thkt/herdr-agentchat) | 0 | Coordinates a two-agent leader-and-coder conversation between Claude Code and Codex with send-and-wake sync. |
| [**Idan-Levin/herdr-implement-review**](https://github.com/Idan-Levin/herdr-implement-review) | 0 | A Herdr workflow in which Codex implements changes, a security scan checks them, and a parent agent performs the final review. |
| [**weirdry/crew**](https://github.com/weirdry/crew) | 0 | Coordinates a lead agent and a different-model worker in sibling Herdr panes across bounded review rounds. |
| [**HarryZus/herdr-dynamic-agent-workspace**](https://github.com/HarryZus/herdr-dynamic-agent-workspace) | 0 | Creates agent tabs when a Herdr workspace opens and coordinates a marker-based Claude and Codex review handoff. |

### Consensus and judge panels of several agents

*4 projects. Several agents answer or review independently, then a judge or consensus step combines their findings into one verdict.*

| Project | Stars | What it does |
|---|--:|---|
| [**zekierman/herdr-council**](https://github.com/zekierman/herdr-council) | 4 | Asks coding agents in Herdr TUI the same question and combines blind peer rankings with a judge agent verdict. |
| [**neospeed83/herdr-tournament**](https://github.com/neospeed83/herdr-tournament) | 1 | Runs independent Codex or Claude reviews of a branch or pull request, then consolidates findings through an adversarial judge workflow. |
| [**l20250208/herdr-consensus**](https://github.com/l20250208/herdr-consensus) | 0 | Combines two isolated agent reviews into a consensus, human decision, fix plan, and worktree-based fix. |
| [**binthnay1973/deepthink**](https://github.com/binthnay1973/deepthink) | 0 | Runs a multi-agent research panel in Herdr panes, cross-checks independent findings, and consolidates a sourced verdict. |

### Pull-request review dispatchers

*4 projects. Tools that take a pull request and hand it to review agents in Herdr panes, then collect or post the findings.*

| Project | Stars | What it does |
|---|--:|---|
| [**tomasvarga/herdr-sniffr**](https://github.com/tomasvarga/herdr-sniffr) | 6 | Starts an agent in Herdr to perform an initial quality and bug review of a pull request, then writes draft comments into tuicr. It supports Claude, Codex, Cursor, and Grok backends. |
| [**zhuravel/magnum**](https://github.com/zhuravel/magnum) | 4 | Runs Claude Code, Codex and other agents in Herdr TUI panes to review pull requests, then uses a judge agent to verify findings and post a consolidated GitHub review. |
| [**Siregar/herdr-review-relay**](https://github.com/Siregar/herdr-review-relay) | 0 | Sends an Engineering agent's PR to every QA agent in a Herdr TUI tab, waits for their reviews and returns them to Engineering in one prompt. Supports Claude Code and OpenCode. |
| [**korvyashka/herdr-pr-relay**](https://github.com/korvyashka/herdr-pr-relay) | 0 | Picks pull requests and dispatches them to active agent sessions as review prompts. |

### Agent races and side-by-side comparisons

*5 projects. Tools that send one prompt to several agents at once so you can race them and compare their results.*

| Project | Stars | What it does |
|---|--:|---|
| [**StructuPath/herdr-swarm**](https://github.com/StructuPath/herdr-swarm) | 12 | Runs several coding agents in parallel, each with its own branch, worktree, and Herdr pane, making it easy to watch competing implementations, compare changes, and keep the strongest result. |
| [**xzedx/herdr-derby**](https://github.com/xzedx/herdr-derby) | 1 | Sends one prompt to every agent in the current Herdr TUI tab and races them, with live timers and finishing ranks on pane borders. Can also start fresh agents in separate worktrees. |
| [**ArtMoreno/herdr-swarm**](https://github.com/ArtMoreno/herdr-swarm) | 0 | Races coding agents in Herdr panes and isolated Git worktrees, compare their diffs, and apply a winner. |
| [**kowloonzh/agenthub**](https://github.com/kowloonzh/agenthub) | 0 | Broadcasts messages simultaneously to Codex and Claude Code sessions across Herdr panes via a single-binary TUI. |
| [**qivyn/herdr-broadcast**](https://github.com/qivyn/herdr-broadcast) | 0 | Sends one prompt to several coding agents and shows their live terminals in a browser page. Continues in rounds on local or saved SSH machines. |

### Workflow engines and scripted agent pipelines

*12 projects. Engines that run agent work from YAML, TypeScript or JavaScript definitions with ordered steps, retries and recorded decisions.*

| Project | Stars | What it does |
|---|--:|---|
| [**osolmaz/pi-workflows**](https://github.com/osolmaz/pi-workflows) | 361 | Provides a workflow engine, JSON control-flow system, and live terminal viewer for the Pi coding agent in Herdr. |
| [**vekexasia/pi-extensible-workflows**](https://github.com/vekexasia/pi-extensible-workflows) | 253 | Runs deterministic Pi workflows with on-disk checkpoints and Git worktree isolation in Herdr. |
| [**aorumbayev/herdr-workflows**](https://github.com/aorumbayev/herdr-workflows) | 40 | Runs repeatable development and agent workflows from YAML files. Each manifest defines an ordered sequence of commands and agent interactions to execute inside Herdr workspaces. |
| [**letya999/workflow-herdr**](https://github.com/letya999/workflow-herdr) | 5 | Provides a YAML-configurable workflow for coordinating AI agents in Herdr with customizable roles and state validation. |
| [**lunoob/mini-orchestrator**](https://github.com/lunoob/mini-orchestrator) | 3 | Orchestrates custom Herdr script workflows using TypeScript. |
| [**mohaphez/herdr-flow**](https://github.com/mohaphez/herdr-flow) | 2 | Coordinates a planning agent and separate implement, review and repair sessions in a task-specific git worktree, with a file-backed state and guarded worktree cleanup. Works with Claude Code, Codex, OpenCode and Pi, and never commits or merges automatically. |
| [**andthezhang/herdr-dynamic-workflow**](https://github.com/andthezhang/herdr-dynamic-workflow) | 0 | Runs JavaScript workflows that launch coding agents in Herdr TUI panes, including parallel jobs, isolated worktrees, and SSH hosts. |
| [**theaileverage/marionette**](https://github.com/theaileverage/marionette) | 0 | Runs coding-agent workflows in Herdr through a CLI and TypeScript SDK, with durable project state and separate evidence and acceptance states. |
| [**navanchauhan/attractor**](https://github.com/navanchauhan/attractor) | 0 | Runs a sequential planning and execution workflow with Codex and Claude Code through the Herdr TUI socket. |
| [**summerKK/herdr-orch**](https://github.com/summerKK/herdr-orch) | 0 | Orchestrates Claude, Codex, and AGY agents into phased pipelines for implementation, review, and verification. |
| [**caner-akca/herdr-plugin-atomic-workflows**](https://github.com/caner-akca/herdr-plugin-atomic-workflows) | 0 | Launches and monitor isolated Atomic workflow tasks, campaign board, sidebar tokens, run ledger, and an optional Telegram cockpit. |
| [**oguzcanhuner/shepherd**](https://github.com/oguzcanhuner/shepherd) | 0 | Runs configured coding workflows in Herdr panes, combining agent steps, scripts, retries, and recorded decisions. |

### Spec-driven and SDLC process frameworks

*6 projects. Software-lifecycle frameworks that move work through specs, plans, gates and reviews with agents running in Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**transparent-pegasus/herdrpowers**](https://github.com/transparent-pegasus/herdrpowers) | 14 | Coordinates planning, implementation, testing, and review across Herdr TUI agent panes using workflows adapted from Superpowers. |
| [**pbean/bmad-loop-adapter-herdr**](https://github.com/pbean/bmad-loop-adapter-herdr) | 7 | Provides a Herdr terminal-multiplexer backend for bmad-loop. |
| [**juanitourquiza/shipframe · herdr-plugin**](https://github.com/juanitourquiza/shipframe/tree/main/herdr-plugin) | 5 | Opens a ShipFrame workflow pane and checklist in Herdr TUI for Claude Code, Codex, or OpenCode. |
| [**voodootikigod/adlc-herdr**](https://github.com/voodootikigod/adlc-herdr) | 3 | Adds Agentic Development Lifecycle gates into Herdr. It shows ticket states, per-pane phases, and backlog boards, and provides actions for unblocking controlled milestones. |
| [**lutian/herdr-sdd-harness**](https://github.com/lutian/herdr-sdd-harness) | 2 | Provides a Spec-Driven Development harness using Herdr for orchestration. |
| [**evancetesha/mini-code-factory**](https://github.com/evancetesha/mini-code-factory) | 0 | Provides a deliberately small three-role SDLC software factory: OpenCode agents orchestrated through Herdr for persistent panes, agent state, and file-based handoffs. |

### Autonomous coding loops that end in pull requests

*11 projects. Bounded implement, review and fix loops that run unattended and finish with a reviewed commit or pull request.*

| Project | Stars | What it does |
|---|--:|---|
| [**jpolec/herdr-plugin-odysseus**](https://github.com/jpolec/herdr-plugin-odysseus) | 11 | Runs governed multi-agent tasks in Herdr TUI panes with checks, retries, review, approvals, and draft pull requests. |
| [**cyperx84/herdr-loop**](https://github.com/cyperx84/herdr-loop) | 5 | Runs iterative planner, coder, and reviewer graphs across Claude Code, Codex, OpenCode, and Pi panes. Socket events and pane output are used to pass intermediate results until the workflow reaches its stopping condition. |
| [**night-porter/nightporter**](https://github.com/night-porter/nightporter) | 4 | Runs coding agents on review comments, failing CI, and merge conflicts and opens job worktrees in Herdr TUI. |
| [**robi42/factory**](https://github.com/robi42/factory) | 4 | Runs Claude Code planning and building alongside Codex reviews in Herdr TUI, with Beads tracking tasks. |
| [**firegnu/herdr-loop-lab**](https://github.com/firegnu/herdr-loop-lab) | 3 | Runs bounded coding loops in Herdr TUI with mechanical checks and cross-model review, parallel worktree fleets, and large-goal decomposition. |
| [**MovieHolic-Plex/herdr-wish**](https://github.com/MovieHolic-Plex/herdr-wish) | 3 | Starts an omo `/wish` workflow in a new Herdr TUI worktree to implement a request, commit changes, and open a pull request. |
| [**QuentinTorg/stagehand**](https://github.com/QuentinTorg/stagehand) | 1 | Coordinates author and reviewer agents across Herdr TUI worktrees and hands reviewed work to GitHub pull requests. |
| [**HigorAlves/luna-tui**](https://github.com/HigorAlves/luna-tui) | 1 | Adds a Herdr plugin board where you plan tickets that move through a fixed pipeline of agents in Docker containers. Stops at approval gates for your sign-off. |
| [**edbienes/drovr**](https://github.com/edbienes/drovr) | 0 | Runs a Herdr-based development loop with isolated implementation, a repository quality gate, two independent reviews, and a human-gated merge. |
| [**sarmientoF/herdr-pr-loop**](https://github.com/sarmientoF/herdr-pr-loop) | 0 | Runs tester, coder, and reviewer agents through local task cycles and GitHub pull-request reviews in separate tabs. State is stored in files, while approval gates, logs, a budget limit, and a pause file keep runs controllable. |
| [**henrywang/herdr-workflow**](https://github.com/henrywang/herdr-workflow) | 0 | Runs multi-agent Herdr TUI workflows with cross-model planning, adversarial review and bounded iterations toward pull requests. |

### Tracker-driven agent factories

*14 projects. Pipelines that watch an issue tracker or project board, run agents on each ticket in its own worktree and report the pull request back.*

| Project | Stars | What it does |
|---|--:|---|
| [**jmwind/issue-herd**](https://github.com/jmwind/issue-herd) | 42 | Watches Linear; when an issue matches a rule, run Claude Code in a herdr workspace and report the PR back to the issue. |
| [**freethinkel/shepherd**](https://github.com/freethinkel/shepherd) | 12 | Controls plane for coding agents on top of Herdr: tracker task in, pull request out. |
| [**sean1588/herdr-orchestrator**](https://github.com/sean1588/herdr-orchestrator) | 6 | A Go daemon that runs an issue-to-pull-request workflow from a validated YAML state graph. Herdr hosts implementer and reviewer agents, while the daemon checks GitHub's merge gate and can squash-merge, with dry-run enabled by default. |
| [**razajamil/herdr-factory**](https://github.com/razajamil/herdr-factory) | 5 | Claims work from Jira or Markdown task files, creates one Herdr worktree per item, and moves Claude Code through a configurable YAML pipeline. It can follow pull requests through CI, review, and merge under a shared concurrency limit. |
| [**civitaspo/herdr-linear-agent**](https://github.com/civitaspo/herdr-linear-agent) | 5 | Runs a coordinator and repository coding agents in Herdr TUI panes for Linear issues delegated to its app user. |
| [**tomoasleep/herdr-symphony**](https://github.com/tomoasleep/herdr-symphony) | 2 | Reads issues from GitHub Projects, creates `gwq` worktrees, and runs one OpenCode agent per issue inside Herdr workspaces. |
| [**bredebjorhovd/herdr-board**](https://github.com/bredebjorhovd/herdr-board) | 2 | Assigns GitHub issues to agents in dedicated Herdr panes and moves completed work into pull-request review. |
| [**seandavi/factory-control-ref**](https://github.com/seandavi/factory-control-ref) | 2 | Turns GitHub issues into a work queue for pi agents running in Herdr sessions, with a web UI and actions API served over Tailscale. Surfaces blocked questions, PRs ready to merge and failed runs. |
| [**Tudor0404/dual-author**](https://github.com/Tudor0404/dual-author) | 1 | Processes GitHub issues through isolated worktrees, Claude implementation, draft pull requests, and paired Codex and Claude review rounds. A dashboard shows each issue's stage and elapsed time until the change is ready for automatic merging. |
| [**brooswit-factory/butchr**](https://github.com/brooswit-factory/butchr) | 1 | Provides the software factory: watches your Jira, runs herdr agents on active tickets, pushes updates to them over MCP. |
| [**maimuzo/continuo**](https://github.com/maimuzo/continuo) | 0 | Turns GitHub Projects v2 cards into a queue for Claude Code workers in Herdr panes and updates board status after execution. |
| [**YuSa0-6/herdr-issue-flow**](https://github.com/YuSa0-6/herdr-issue-flow) | 0 | Creates Herdr workspaces and Git worktrees for GitHub issues, with Pi conductor and worker sessions and Hunk review handoff. |
| [**jeremN/herdr-dispatch-plugin**](https://github.com/jeremN/herdr-dispatch-plugin) | 0 | Dispatches tickets through an AI-agent pipeline, one git worktree per ticket, each phase in a named pane, fail-closed, with a human approval gate. |
| [**Mamprim-go/sdlc-herdr**](https://github.com/Mamprim-go/sdlc-herdr) | 0 | Runs a GitHub issue workflow with Pi agents in Herdr TUI panes for triage, planning, implementation, review, and QA. |

### Herdr TUI plugins that turn Linear issues into agent runs

*7 projects. Plugins that browse and search Linear issues inside Herdr and start an agent on the chosen issue.*

| Project | Stars | What it does |
|---|--:|---|
| [**JacquesvanWyk/herdr-linear**](https://github.com/JacquesvanWyk/herdr-linear) | 8 | Opens an fzf-driven Linear panel in a Herdr TUI split or tab to search issues, browse projects, create issues, and change their status. |
| [**mrolafsson/herdr-linear**](https://github.com/mrolafsson/herdr-linear) | 8 | Browses Linear issues and starts agents in issue worktrees from the Herdr app or a Herdr TUI popup. |
| [**talent-factory/herdr-linear**](https://github.com/talent-factory/herdr-linear) | 5 | Adds an interactive Linear issue browser to Herdr. Selecting an issue opens a dedicated agent pane and supplies the ticket context so implementation can begin immediately. |
| [**hdtradeservices/ticketdeck**](https://github.com/hdtradeservices/ticketdeck) | 0 | Shows Linear projects and tickets in a terminal dashboard and launches or reattaches Claude Code sessions in Herdr TUI. |
| [**PanchTime/linear-widget**](https://github.com/PanchTime/linear-widget) | 0 | Displays Linear issues in an Omarchy bar widget and opens ticket worktrees or agent sessions in Herdr TUI. |
| [**solcreek/linear-tui · herdr-plugin**](https://github.com/solcreek/linear-tui/tree/main/herdr-plugin) | 0 | Opens linear-tui, a terminal UI for Linear issues with inline images, over, beside or as a popup on the focused Herdr TUI pane. Ctrl-click on a Linear issue link opens it there, and a demo action needs no account. |
| [**jenthous/herdr-linear**](https://github.com/jenthous/herdr-linear) | 0 | Searches Linear issues as you type in a Herdr TUI popup or side pane, renders issue bodies and comments as Markdown, and copies issue and PR links. Pins the issue matching the current branch. |

### Herdr TUI Jira boards and ticket launchers

*9 projects. Plugins that show Jira boards, tickets and worklogs in a Herdr pane and open worktrees or agents for the selected issue.*

| Project | Stars | What it does |
|---|--:|---|
| [**a2u/herdr-jira**](https://github.com/a2u/herdr-jira) | 15 | Adds a Ratatui Jira client to browse, filter, and assign tickets directly to Herdr agent panes. |
| [**kiitosu/herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board) | 3 | Embeds a Jira Kanban board in a Herdr pane with one-key Claude Code session launching and live card status updates. |
| [**hanbong5938/herdr-jira-worktree**](https://github.com/hanbong5938/herdr-jira-worktree) | 3 | Opens Jira issues in Herdr TUI and creates Git worktrees or jj workspaces from them. Browse comments, change issue status, and delegate work to an agent. |
| [**spiritsack/herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree) | 1 | Creates or reuses a ticket-specific Git worktree and prefills its Jira ID or URL into a coding agent in Herdr TUI. |
| [**abtris/herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr) | 1 | Checks the current branch's GitHub pull request against linked Jira tickets. It shows ticket state and warns when issue keys are missing or do not match, keeping Jira context visible in Herdr. |
| [**khanal-samir/herdr-jira-workspace**](https://github.com/khanal-samir/herdr-jira-workspace) | 1 | Opens a Jira Kanban board, calendar worklogs, comments, and attachments inside Herdr TUI. Sends Herdr notifications for ticket activity. |
| [**hilmimuktitama/herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek) | 0 | Finds Jira Cloud issue keys in a Herdr TUI pane and opens read-only issue descriptions and comments alongside it. |
| [**drewbitt/herdr-jiratui**](https://github.com/drewbitt/herdr-jiratui) | 0 | Opens JiraTUI in a Herdr TUI tab and sends the selected Jira issue's key, summary, link, and description to a running agent. |
| [**ChristianDeckert/herdr-jira-light**](https://github.com/ChristianDeckert/herdr-jira-light) | 0 | Shows a Jira pane in the Herdr TUI whose filters follow the current tab's directory, with project, board and sprint browsing and issue details. Runs on zsh, curl and jq with no build step. |

### Herdr TUI GitHub issue and pull-request browsers that start agents

*7 projects. Plugins that browse GitHub issues, pull requests and discussions and turn one into a prepared agent tab or worktree.*

| Project | Stars | What it does |
|---|--:|---|
| [**ogulcancelik/herdr-plugin-github-start**](https://github.com/ogulcancelik/herdr-plugin-github-start) | 17 | Turns a GitHub issue, pull request, or discussion into a prepared agent tab with one key. |
| [**mrolafsson/herdr-github**](https://github.com/mrolafsson/herdr-github) | 8 | Reviews and manages GitHub pull requests and starts agents in PR worktrees from the Herdr app or a Herdr TUI popup. |
| [**kukv/octoscope**](https://github.com/kukv/octoscope) | 4 | Adds GitHub issue and pull-request management to Herdr, including review, tracking, and assignment of GitHub work to agent tabs from inside the terminal. |
| [**nyanyaon/github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin) | 1 | Browses the current repository’s open GitHub issues and comment threads in a read-only Herdr TUI pane. |
| [**NightingaleMedia/herdr-github-orobo**](https://github.com/NightingaleMedia/herdr-github-orobo) | 0 | Runs in a Herdr TUI split or tab and sends work to an existing agent or starts a new one. Its pull-request dashboard is being migrated. |
| [**U5K492/herdr-new-workspace-extended**](https://github.com/U5K492/herdr-new-workspace-extended) | 0 | Extends new workspace in the Herdr TUI so you can start from a GitHub issue or pull request with gh and fzf, from a branch name, or from a plain name. |
| [**manoel-freitas/herdr-kanban**](https://github.com/manoel-freitas/herdr-kanban) | 0 | Opens a Kanban board of the current workspace's GitHub issues in Herdr TUI, showing the live agent or human assignee on each card and letting you move cards between columns. |

### GitLab, ClickUp, Shortcut, Notion and other tracker clients

*11 projects. Clients for GitLab, ClickUp, Shortcut, Notion, Devin and other trackers that hand a ticket to a Herdr agent.*

| Project | Stars | What it does |
|---|--:|---|
| [**omarjesusperezortiz/herdr-notion**](https://github.com/omarjesusperezortiz/herdr-notion) | 5 | Browses a Notion database in a Herdr TUI pane, changes page status, and sends tickets to agents. |
| [**juscribe/herdr-plugin**](https://github.com/juscribe/herdr-plugin) | 2 | Files and transitions Juscribe tickets from a Herdr pane and moves a ticket to started when an agent begins working. Shows which ticket each agent is on, using the signed-in jus CLI so the plugin never handles your token. |
| [**zamarrowski/herdr-issues**](https://github.com/zamarrowski/herdr-issues) | 2 | Lists GitHub issues of the current repo plus Linear issues and Shortcut stories, and hands one to any coding agent in its own git worktree. Works with Claude Code, Codex, Gemini CLI, Pi, OpenCode and other agents Herdr can start. |
| [**matheus3301/herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut) | 1 | Lists assigned Shortcut stories in a terminal picker and launches the selected story in a new Herdr agent tab. |
| [**H3xept/herdr-ingest**](https://github.com/H3xept/herdr-ingest) | 1 | Turns Sentry, Linear, or GitHub work items into Herdr TUI spaces and Git worktrees with agent briefs, waiting for user confirmation before starting an agent. |
| [**ukwhatn/taskherd**](https://github.com/ukwhatn/taskherd) | 1 | Tracks agent sessions, GitHub pull requests, and Jira tickets on a local task board that can jump to Herdr TUI sessions. |
| [**ssk090/herdr-clickup**](https://github.com/ssk090/herdr-clickup) | 1 | Browses ClickUp sprints, lists, and tasks in a Herdr TUI tab and starts an agent on a task in its own worktree. Reports back when the agent finishes. |
| [**rigelstpierre/herdr-devin-board**](https://github.com/rigelstpierre/herdr-devin-board) | 1 | Lists your Devin Cloud sessions in a herdr tab with live GitHub PR, CI, and review status. Attaches to a session in a new tab with `devin --cloud --resume`, opens `devin ssh` in a pane, or archives it. |
| [**alfonsodg/herdr-glab-tasks**](https://github.com/alfonsodg/herdr-glab-tasks) | 0 | Adds a GitLab issues panel grouped by status label to the Herdr TUI, with an action that creates an issue and its branch and handling for issue links. |
| [**haoyuant/tomrade-plugins · herdr**](https://github.com/haoyuant/tomrade-plugins/tree/main/herdr) | 0 | Opens Tomrade tickets from the Herdr TUI by Ctrl-clicking a ticket key and claims a pane's agent to a ticket. Offers a claim when a new worktree is created. |
| [**PolyphonyRequiem/twig-herdr**](https://github.com/PolyphonyRequiem/twig-herdr) | 0 | Opens a Twig work-item panel in Herdr TUI with a tree and table, scrollable item detail, and digest-based proposal review. Needs Twig 0.93.0 or newer and Node.js 22. |

### Kanban boards that dispatch agents

*11 projects. Kanban boards in a Herdr pane where moving or dispatching a card starts or feeds a coding agent.*

| Project | Stars | What it does |
|---|--:|---|
| [**nelsonPires5/herdr-board**](https://github.com/nelsonPires5/herdr-board) | 194 | A Kanban TUI and background service that turns cards into prompts for agents in visible Herdr panes. Moving a card can create an agent, run it in a dedicated tab, and advance the work through review gates. |
| [**KokiKono/herdr-kanban**](https://github.com/KokiKono/herdr-kanban) | 6 | Tracks tasks on a SQLite-backed terminal Kanban board and opens Herdr TUI tabs for in-progress tasks. |
| [**MatheusBBarni/herdr-tasks**](https://github.com/MatheusBBarni/herdr-tasks) | 3 | Runs a kanban task board and `htasks` CLI that launch agents in Herdr panes and track their work. |
| [**sazardev/herdr-code-board**](https://github.com/sazardev/herdr-code-board) | 2 | Dispatches agent prompts from a kanban queue into Herdr panes, workspaces, and worktrees, with rules that chain cards. |
| [**virtualboard/herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard) | 2 | Shows VirtualBoard feature specs as a kanban board inside Herdr, where moving a card runs the vb CLI. Dispatching a card starts a VirtualBoard role agent in a visible pane. |
| [**philals/mission-control-capcom**](https://github.com/philals/mission-control-capcom) | 1 | Breaks a Jira story into PR-sized tasks and shows tasks, draft PRs and CI stages on a terminal board. An optional Herdr plugin opens the board by key and launches agents in Herdr panes. |
| [**TsukumiStudio/MornKanban**](https://github.com/TsukumiStudio/MornKanban) | 0 | Dispatches file-based Kanban cards to Claude Code and Codex workers in Herdr panes, with isolated worktrees and review. |
| [**hassox/herdr-kanban**](https://github.com/hassox/herdr-kanban) | 0 | Shows Herdr TUI workspace panes as kanban cards, starts agents, and runs scripts when cards change columns. |
| [**GumbyEnder/herdr-devboards**](https://github.com/GumbyEnder/herdr-devboards) | 0 | Shows Dev Boards missions in a Herdr pane across all lanes and binds running missions to agent panes. Claims, delivers, escalates, and dispatches missions to idle agents. |
| [**federbenjamin/herdr-desk**](https://github.com/federbenjamin/herdr-desk) | 0 | Adds a task board pane to the Herdr TUI where you and your agents track tasks. Includes a coordinator, a runner that starts tasks and a session journal. |
| [**acrucetta/herdr-kanban**](https://github.com/acrucetta/herdr-kanban) | 0 | Organizes live Herdr agent sessions on a kanban board and opens the selected session beside Neovim. |

### Shared task boards for people and agents

*10 projects. Task boards and dependency graphs in a Herdr pane that you and your agents both read and update, without necessarily launching agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**smarzban/herdr-tsk**](https://github.com/smarzban/herdr-tsk) | 266 | Shares a terminal task board between you and your agents with a TUI for humans and a CLI for agents. |
| [**smarzban/tsk**](https://github.com/smarzban/tsk) | 266 | Opens a shared task board in Herdr TUI and lets agents manage work through a CLI. |
| [**jwarykowski/shepherd**](https://github.com/jwarykowski/shepherd) | 6 | Runs a Markdown-backed task board in a Herdr TUI pane, tab, or overlay for people and coding agents. |
| [**m0hdrar/kanban_tui**](https://github.com/m0hdrar/kanban_tui) | 2 | Runs a keyboard-first kanban board with per-project cards in a Herdr pane and jumps to it with a bound key. A status command prints open work for the Herdr tab bar, and agents can manage cards from the shell. |
| [**larrychannon/herdr-job-board**](https://github.com/larrychannon/herdr-job-board) | 1 | Opens a board in a Herdr split pane for work handed to coding agents, grouped as waiting on you, doing, queue, to do and done. A coordinator agent writes cards with a small CLI. |
| [**bxuserx/kerdr**](https://github.com/bxuserx/kerdr) | 0 | Adds a shared, mouse-driven kanban board for agents in a Herdr TUI space, stored in a `.tickets/` directory. |
| [**amine2233/herdr-plugin-kanban**](https://github.com/amine2233/herdr-plugin-kanban) | 0 | Opens an fzf-driven kanban board in a Herdr TUI split to list and edit cards or draft them with Claude. |
| [**calvinp0/herdr-htask**](https://github.com/calvinp0/herdr-htask) | 0 | Shows a Herdr side panel of what coding agents have done, are doing, and have blocked, from a shared SQLite task store. Agents add tasks with the htask command. |
| [**Zeotyn/spec-kanban**](https://github.com/Zeotyn/spec-kanban) | 0 | Shows OpenSpec changes or Spec Kit features as a kanban board in a Herdr pane. |
| [**tyz-works/herdr-task-graph**](https://github.com/tyz-works/herdr-task-graph) | 0 | Shows a live terminal dependency graph of tasks in the Herdr TUI with agent state and which work is ready to run in parallel. |

### Task claims and ledgers that agents share

*9 projects. Shared to-do lists and ledgers where agents claim items, add their own and report back, with dependencies and review status.*

| Project | Stars | What it does |
|---|--:|---|
| [**jasonrr/herdr-tally**](https://github.com/jasonrr/herdr-tally) | 8 | Keeps project-scoped todos, scratchpads and plans in a shared ledger for Herdr TUI users and agents. |
| [**leset0ng/pi-todo-herdr**](https://github.com/leset0ng/pi-todo-herdr) | 3 | Tracks hierarchical Pi tasks with a live widget and optionally shows the current task in the Herdr TUI sidebar. |
| [**husniadil/herdr-tasks**](https://github.com/husniadil/herdr-tasks) | 2 | Tracks agent tasks and notes in Herdr TUI with renewable claims, evidence-backed review, and a human decision gate. |
| [**aoprisan/hird**](https://github.com/aoprisan/hird) | 1 | Queues cross-harness agent work and stores shared assertions in SQLite. |
| [**Eslsamu/herdr-tasks**](https://github.com/Eslsamu/herdr-tasks) | 1 | Keeps an agent-owned task queue linked to each Herdr space, with atomic claims, priorities, dependencies, and durable conversation ownership. An always-visible Herdr summary and local read-only browser view let people follow the work without maintaining cards. |
| [**yuanying/herdr-tasks**](https://github.com/yuanying/herdr-tasks) | 1 | Supervises task execution from start to finish across Herdr workspaces and worktrees. |
| [**lenaertsjan/herdr-factory-demo**](https://github.com/lenaertsjan/herdr-factory-demo) | 0 | Provides a small local-first task manager for end-to-end herdr-factory tests. |
| [**Adroz/herdr-feedr**](https://github.com/Adroz/herdr-feedr) | 0 | Shows a markdown-backed to-do sidebar in Herdr TUI that you and your coding agents share. Agents claim items, add their own and report back through one file. |
| [**andrewdunndev/herdr-estate**](https://github.com/andrewdunndev/herdr-estate) | 0 | Tracks long-running campaigns as threads of agent work addressed as estate/campaign, so work outlives each conversation. Agents write a log before a conversation ends and a fresh one picks it up. |

### Beads task tracker integrations

*4 projects. Integrations that show Beads issues in Herdr or tie bead-driven work sessions to Herdr tabs and worktrees.*

| Project | Stars | What it does |
|---|--:|---|
| [**miiraheart/herdr-beads**](https://github.com/miiraheart/herdr-beads) | 42 | Displays Beads issues as a list, table, or Kanban board in a Herdr sidebar or floating pane. |
| [**CodeForBreakfast/beady-eye**](https://github.com/CodeForBreakfast/beady-eye) | 27 | Shows, live, which agent works on which bead across your projects next to its Herdr pane, and tells agents and scripts when the beads they wait on change. |
| [**hexsprite/herdr-beads**](https://github.com/hexsprite/herdr-beads) | 3 | Opens Beads issue details in a Herdr TUI split when an issue ID is Ctrl-clicked. |
| [**goern/bead-workflow-skills**](https://github.com/goern/bead-workflow-skills) | 0 | Starts and closes bead-driven work sessions using Herdr TUI tabs and Worktrunk worktrees, keeping tab and session labels aligned. |

### Scheduled agent routines and cron jobs

*15 projects. Schedulers that start agent prompts or commands on cron expressions, intervals or timers in fresh Herdr panes.*

| Project | Stars | What it does |
|---|--:|---|
| [**DnzzL/herdr-automations**](https://github.com/DnzzL/herdr-automations) | 31 | Schedules recurring prompts and cron jobs that run agents in fresh Herdr worktrees. It supports task-specific MCP settings, collision protection, persistent run history, and a live monitoring board. |
| [**bon5co/bermuda**](https://github.com/bon5co/bermuda) | 13 | Schedules jobs as interactive agents in dedicated Herdr splits. It supports multi-step workflows, shared append-only discussion logs, and exclusive resource claims that remain valid across temporary sessions. |
| [**mrcndz/herdr-routines**](https://github.com/mrcndz/herdr-routines) | 11 | Runs scheduled routines on cron or interval timers by opening a tab in a chosen workspace and executing a command or starting an agent. |
| [**mikedclarke/herdr-shepherd**](https://github.com/mikedclarke/herdr-shepherd) | 7 | Runs cron routines, heartbeats, and recurring automation scripts in visible Herdr workspaces so background maintenance remains easy to inspect. |
| [**husniadil/herdr-sched**](https://github.com/husniadil/herdr-sched) | 5 | Schedules agent actions with cron, webhooks, and file-watcher triggers in Herdr. |
| [**qluto/collie**](https://github.com/qluto/collie) | 2 | Adds an unattended-work box for Claude Code sessions on Herdr: toss tasks in by day, spend leftover token quota on them at night, collect the results in the morning. |
| [**guidodinello/herdr-routines**](https://github.com/guidodinello/herdr-routines) | 2 | Runs scheduled routines that spawn a Herdr pane, start Claude Code or OpenCode and send it one prompt, driven by a systemd user timer and a YAML job list. The plugin adds actions to run a job and check its status from inside Herdr. |
| [**salmonumbrella/herdr-kata**](https://github.com/salmonumbrella/herdr-kata) | 2 | Runs Kata cron jobs and workflows as agents and commands on herdr-core and reports each run back to Kata. Works as a headless worker with no UI of its own. |
| [**huketo/herdr-cron**](https://github.com/huketo/herdr-cron) | 1 | Schedules shell commands and coding-agent prompts to run in Herdr panes, with a CLI and terminal interface. |
| [**ram4-dev/herdr-automations**](https://github.com/ram4-dev/herdr-automations) | 1 | Runs scheduled or event-triggered agent jobs from cron expressions, intervals, and lifecycle hooks. It prevents overlapping runs, creates fresh Git worktrees, and records complete execution histories. |
| [**duyet/herdr-desk**](https://github.com/duyet/herdr-desk) | 1 | Schedules manager agents in Herdr TUI worktrees to triage and work through repository backlogs. |
| [**Phoobobo/taya**](https://github.com/Phoobobo/taya) | 0 | Initializes a workboard workflow and launches a Pi engineering assistant in Herdr TUI, with scheduled nudges for routine work. |
| [**terry-li-hm/herdr-bots**](https://github.com/terry-li-hm/herdr-bots) | 0 | Runs scheduled Claude Code or Pi jobs in fresh Herdr worktrees and collects their output in an evidence inbox. |
| [**aneym/herdr-routines**](https://github.com/aneym/herdr-routines) | 0 | Schedules Herdr TUI agent routines with a daemon and CLI. |
| [**zerodice0/herdr-booking-task-plugin**](https://github.com/zerodice0/herdr-booking-task-plugin) | 0 | Schedules Herdr TUI agent prompts and local commands with one-time or recurring runs on macOS and Linux. |

### Prompt queues and delayed prompt delivery

*11 projects. Queues, buckets and timers that hold prompts and deliver them to an agent pane when it is idle or at a set time.*

| Project | Stars | What it does |
|---|--:|---|
| [**ivanarama/PromptPilot**](https://github.com/ivanarama/PromptPilot) | 22 | Queues and schedules prompts for coding CLIs through a web UI or Telegram bot, with Herdr-backed terminal sessions and retry on rate limits. |
| [**GNURub/herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket) | 2 | Adds a durable, ordered prompt bucket for coding agents running in Herdr. |
| [**pjgeutjens/omarchy-feed-the-flock**](https://github.com/pjgeutjens/omarchy-feed-the-flock) | 2 | Queues typed or dictated Omarchy notes and delivers them to Herdr TUI agents when they are ready. |
| [**huntergdavis/dunkingsheep**](https://github.com/huntergdavis/dunkingsheep) | 1 | Keeps agents active by sending configured text to Herdr panes at regular intervals. |
| [**AltanS/herdr-pouch**](https://github.com/AltanS/herdr-pouch) | 1 | Stores prompts for a Herdr TUI agent and inserts them into its input one at a time without submitting them. |
| [**connerohnesorge/herdr-agent-queue**](https://github.com/connerohnesorge/herdr-agent-queue) | 1 | Queues prompts for Claude Code and other agents in Herdr TUI and submits each as a new turn after the current turn ends. |
| [**htlin222/herdr-agent-self-reload-skill**](https://github.com/htlin222/herdr-agent-self-reload-skill) | 1 | Re-prompts the agent in the current Herdr pane after a chosen delay. |
| [**EricBois/herdr-nudge**](https://github.com/EricBois/herdr-nudge) | 0 | Schedules a continue prompt for a Herdr agent, either at a chosen time or when the agent becomes idle or blocked. |
| [**alex-devdone/herdr-sched**](https://github.com/alex-devdone/herdr-sched) | 0 | Schedules messages or commands for later delivery to a Herdr TUI pane using a persistent macOS LaunchAgent queue. |
| [**dj-skn/schedule-send**](https://github.com/dj-skn/schedule-send) | 0 | Schedules prompts, files, or key presses to agent or shell panes at a chosen time, or after a Claude Code or Codex usage limit resets. Runs jobs through systemd or launchd timers so the terminal can close. |
| [**Wormav/herdr-queue**](https://github.com/Wormav/herdr-queue) | 0 | Lets you draft, reorder and queue prompts in a dedicated terminal panel beside an agent in Herdr TUI, then send the one you want. |

### Event triggers and agent wake-ups

*7 projects. Hooks that watch pane output, background jobs or events and wake an agent or run an action when something happens.*

| Project | Stars | What it does |
|---|--:|---|
| [**joshka0/herdr-watcher**](https://github.com/joshka0/herdr-watcher) | 3 | Tracks detached or long-running work and resumes the relevant agent when a background task completes. It uses the Herdr socket API to support workflows that must survive disconnects and interrupted sessions. |
| [**cantona/herdr-triggers**](https://github.com/cantona/herdr-triggers) | 1 | Watches Herdr TUI pane output for configured regular expressions and triggers actions such as notifications, subprocesses, or pane input. |
| [**lufs-audio/snuze**](https://github.com/lufs-audio/snuze) | 0 | Schedules wake-up prompts for Herdr panes after timers, Jules conditions, pane state changes, or external signals. |
| [**lebryk/herdr-events**](https://github.com/lebryk/herdr-events) | 0 | Queues local JSON events for Herdr agents using native Codex, Claude Code, Pi, and OpenCode adapters. |
| [**thientrile/herdr-hjob**](https://github.com/thientrile/herdr-hjob) | 0 | Runs a long command in the background so an agent need not poll it. When it ends, hjob wakes the agent pane with the result through herdr-wake. |
| [**Operator-create/herdr-kitchen-brigade**](https://github.com/Operator-create/herdr-kitchen-brigade) | 0 | Runs your repository checks when a Herdr TUI coding agent finishes, writes a local report, and sends the agent a short failure message. Needs no Python dependencies. |
| [**thientrile/herdr-wake**](https://github.com/thientrile/herdr-wake) | 0 | Queues wake-up events on disk and delivers them to an idle Herdr agent pane through herdr agent prompt, retrying until the agent is free. Installs as a Herdr TUI plugin with a systemd user worker on Linux. |

### Queued task runners with review gates

*7 projects. Runners that take ready tasks from a backlog, execute them with worker agents in worktrees and stop at review or merge gates.*

| Project | Stars | What it does |
|---|--:|---|
| [**marvingygas/spoolway**](https://github.com/marvingygas/spoolway) | 8 | Runs queued coding tasks through configurable Herdr TUI agent pipelines for Claude Code, Codex and Pi. |
| [**nicholasjstock/paneyard**](https://github.com/nicholasjstock/paneyard) | 2 | Queues well-scoped coding tasks for Claude Code and Codex and runs them in parallel, each on its own branch and worktree as a live agent session in Herdr. You can watch, steer and resume each session and get a report when the work is ready. |
| [**husniadil/herdr-dispatch**](https://github.com/husniadil/herdr-dispatch) | 1 | Dispatches ready herdr-tasks board items to worker agents in Herdr panes and hands completed work to the review gate. |
| [**DnzzL/herdr-docket**](https://github.com/DnzzL/herdr-docket) | 1 | Runs a task queue where a named agent turns a card into one pull request and a second agent verifies it. Merges through a merge gate in code or hands the PR to you. |
| [**schemaitat/herdr-aven-plugin**](https://github.com/schemaitat/herdr-aven-plugin) | 1 | Dispatches Aven tasks to OpenCode agents in Git worktrees through herdr-core and supervises them from your terminal. Adds optional Herdr app mods with a task panel and a kanban board. |
| [**DanielFGray/foreman**](https://github.com/DanielFGray/foreman) | 1 | Dispatches coding agents across a task backlog through a pipeline you draw: author, review, and land, with approval gates. Includes a Herdr app pane that shows the pipeline and tasks. |
| [**DerekStride/agent-orchestrator**](https://github.com/DerekStride/agent-orchestrator) | 0 | Dispatches a dependency-scoped SQ task graph to OMP workers in Herdr sessions and isolated Git worktrees. |

### Usage-limit auto-resume and retry

*9 projects. Helpers that notice a rate or usage limit, wait for the reset and continue or retry the agent session automatically.*

| Project | Stars | What it does |
|---|--:|---|
| [**rcosteira79/herdr-autocontinue**](https://github.com/rcosteira79/herdr-autocontinue) | 3 | Watches agents for usage-limit walls, badges the countdown to the reset ($wall), and re-prompts the agents you armed once the window reopens. |
| [**UN-9BOT/herdr-codex-autoresume**](https://github.com/UN-9BOT/herdr-codex-autoresume) | 1 | Resumes a Codex CLI /goal automatically after the usage limit resets by typing the resume command into the pane. Records the reset time and restores the original model. |
| [**bestony/herdr-codex-capacity-retry**](https://github.com/bestony/herdr-codex-capacity-retry) | 1 | Automatically continues Codex sessions in Herdr after capacity-related interruptions. |
| [**kil9/claude-auto-retry-herdr**](https://github.com/kil9/claude-auto-retry-herdr) | 0 | Retries Claude Code sessions automatically upon rate limits using native Herdr socket APIs. |
| [**neilwashere/herdr-unrecoverable**](https://github.com/neilwashere/herdr-unrecoverable) | 0 | Watches Pi sessions for terminal-provider failures and attempts recovery automatically. It confirms the problem from transcripts, shows a countdown, and can submit a continue command up to three times. |
| [**floco/herdr-claude-resume**](https://github.com/floco/herdr-claude-resume) | 0 | Detects Claude Code's five-hour rate limit and automatically resumes the session after the limit resets. |
| [**bestony/herdr-auto-retry**](https://github.com/bestony/herdr-auto-retry) | 0 | Continues Herdr TUI agents automatically when they stop on rate-limit, overload, or capacity errors. |
| [**danielfalci/herdr-codex-auto-retry**](https://github.com/danielfalci/herdr-codex-auto-retry) | 0 | Watches Codex panes for a usage-limit message with a reset time, waits, then sends a continuation prompt into the same pane. Does not bypass limits. |
| [**tigorlazuardi/herdr-claude-retry**](https://github.com/tigorlazuardi/herdr-claude-retry) | 0 | Detects Claude usage-limit banners and resumes Herdr TUI panes when the limit resets. |

### Claude Code and Codex login switchers and auth monitors

*9 projects. Switchers and monitors that change the logged-in Claude Code or Codex account, label panes with it and flag logged-out or capped sessions.*

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

### Context compaction and agent memory

*4 projects. Helpers that compact long sessions safely and carry project memory across agent sessions.*

| Project | Stars | What it does |
|---|--:|---|
| [**jatingargiitk/herdr-memory**](https://github.com/jatingargiitk/herdr-memory) | 3 | Builds persistent project memory from agent actions, successful approaches, and earlier decisions across Herdr sessions, then adds relevant context to later prompts to reduce repeated mistakes. |
| [**iagogfe/herdr-ai-memory**](https://github.com/iagogfe/herdr-ai-memory) | 0 | Launches coding agents through ai-memory managed workstreams - cross-agent session continuity. |
| [**tmastalirsch/herdr-claude-safe-compact**](https://github.com/tmastalirsch/herdr-claude-safe-compact) | 0 | Compacts idle Claude Code panes, but only once a handoff is safely on disk. |
| [**shubham399/herdr-agents-auto-compact**](https://github.com/shubham399/herdr-agents-auto-compact) | 0 | Automatically compacts long Claude Code and OpenCode sessions in Herdr so they do not exhaust their context windows. |

### Pi subagent tools that return results to the parent session

*24 projects. Pi extensions that let a running Pi session hand a task to a child agent in its own Herdr pane or tab and bring the result back to the parent, with no standing crew, run board or fleet (the Pi groups close this section).*

| Project | Stars | What it does |
|---|--:|---|
| [**edxeth/pi-subagents**](https://github.com/edxeth/pi-subagents) | 136 | Provides a Pi framework for foreground and background subagents, messaging, and multi-pane orchestration. |
| [**giuseppecrj/pi-herdr-agents**](https://github.com/giuseppecrj/pi-herdr-agents) | 71 | Runs asynchronous Pi subagents and approval-based review workflows entirely inside Herdr. |
| [**AndrewJacop/pi-herdr**](https://github.com/AndrewJacop/pi-herdr) | 37 | Lets Pi spawn, steer, and collect results from Pi, Claude Code, Codex, and OpenCode agents in Herdr TUI panes. |
| [**July24/pier**](https://github.com/July24/pier) | 8 | Adds a todo loop and interactive Pi subagents backed by herdr-core terminals, optionally displayed in the Herdr app. |
| [**kirel/herdr-subagents**](https://github.com/kirel/herdr-subagents) | 3 | Starts each Pi subagent in its own Herdr pane or tab, manages session files, and notifies the parent when work finishes. Panes remain available for follow-up, and different subagents may use different models. |
| [**tinypi-extension/tinysubagent**](https://github.com/tinypi-extension/tinysubagent) | 3 | Spawns Pi subagents in Herdr TUI panes from Markdown roles and returns their results to the parent session. |
| [**YunosukeYoshino/pi-herdr**](https://github.com/YunosukeYoshino/pi-herdr) | 2 | Spawns role-based Pi child agents in neighboring Herdr TUI panes for visible delegation and follow-up. |
| [**aaaxn/pi-herdr-live-agents**](https://github.com/aaaxn/pi-herdr-live-agents) | 1 | Runs visible Pi subagents in Herdr TUI panes and returns their results to the parent session. |
| [**markpinero/pi-suggested-tasks**](https://github.com/markpinero/pi-suggested-tasks) | 1 | Shows suggested parallel tasks in Pi and opens accepted work in a sibling session, optionally using Herdr TUI panes and worktrees. |
| [**marv1nnnnn/pi-yahe**](https://github.com/marv1nnnnn/pi-yahe) | 1 | Provides a composable Pi tool for visible task-based multi-agent work that steers async results back to the parent. |
| [**MinhDuyDEV/pi-subagents**](https://github.com/MinhDuyDEV/pi-subagents) | 1 | Provides a Pi delegation runtime with claims, leases, context packs, and diagnostic retry handling in Herdr. |
| [**jrx2-dev/herdr-sub-agents**](https://github.com/jrx2-dev/herdr-sub-agents) | 0 | Lets Pi spawn, message, and close Pi or Claude Code subagents in Herdr TUI and react to their lifecycle events. |
| [**oldflag2333333/pi-facets**](https://github.com/oldflag2333333/pi-facets) | 0 | Delegates Pi tasks to context-isolated specialist profiles in separate Herdr TUI tabs and returns their findings. |
| [**gitUmaru/pi-session-agents**](https://github.com/gitUmaru/pi-session-agents) | 0 | Spawns independent Pi subagent sessions in Herdr TUI tabs or as headless background sessions when Herdr is unavailable. |
| [**Gabriel-Cervo/Pi-Herdr-Subagents**](https://github.com/Gabriel-Cervo/Pi-Herdr-Subagents) | 0 | Provides a native in-process subagents for Pi with configurable models and smart result joining. |
| [**chrishiguto/pi-herdr-subagents**](https://github.com/chrishiguto/pi-herdr-subagents) | 0 | Launches Pi subagents in dedicated Herdr panes for delegated tasks. |
| [**v3rse/pi-agent-swarm**](https://github.com/v3rse/pi-agent-swarm) | 0 | Runs asynchronous Pi subagents in Herdr TUI panes, with tmux, Zellij, and WezTerm backends also supported. |
| [**andrewfung729/pi-herdr-subagents**](https://github.com/andrewfung729/pi-herdr-subagents) | 0 | Spawns asynchronous Pi subagents in Herdr TUI panes and steers completed results back to the parent session. |
| [**maxedapps/pi-subagents-herdr**](https://github.com/maxedapps/pi-subagents-herdr) | 0 | Delegates Pi work to persistent child sessions in Herdr TUI panes, with agent profiles and optional worktree isolation. |
| [**bstncartwright/pi-bstn-subagents**](https://github.com/bstncartwright/pi-bstn-subagents) | 0 | Runs persistent Cursor ACP subagents from Pi with live Herdr viewers. |
| [**namtx/pi-herd**](https://github.com/namtx/pi-herd) | 0 | Lets Pi spawn, prompt, wait for, inspect, and close child agents in Herdr TUI workspaces. |
| [**yaukwan/pi-extensions**](https://github.com/yaukwan/pi-extensions) | 0 | Runs persistent shell commands and delegated Pi agents in Herdr panes through installable Pi extensions. |
| [**leoszr/holistic-subagents**](https://github.com/leoszr/holistic-subagents) | 0 | Runs persistent Pi delegations in Herdr panes or worktrees with session event logs and authenticated callbacks. |
| [**Vistyy/pi-herdr-agents**](https://github.com/Vistyy/pi-herdr-agents) | 0 | Runs user-owned Pi agents in dedicated Herdr tabs. |

### Pi foremen and crews that coordinate and supervise several workers

*24 projects. Pi extensions where a lead, foreman or supervisor runs several workers as a crew, with run boards, shared task state, parallel scheduling, model routing, watchdogs or fleet supervision, rather than handing off one task.*

| Project | Stars | What it does |
|---|--:|---|
| [**boadij/pi-herdsman**](https://github.com/boadij/pi-herdsman) | 221 | Delegates work to asynchronous Pi agents in Herdr TUI, with nested delegation and fleet supervision. |
| [**electric-dragon-80000v/pi-cowboy**](https://github.com/electric-dragon-80000v/pi-cowboy) | 66 | Runs Pi-supervised coding agents in Herdr TUI panes and isolated Git worktrees, including Claude Code, Codex and OpenCode. |
| [**tobi/pi-herdr-workers**](https://github.com/tobi/pi-herdr-workers) | 14 | Opens Pi worker agents in neighboring Herdr TUI panes with `/team`, loop wakeups, and monitor tools. |
| [**MikkelKappelPersson/pi-shepherd**](https://github.com/MikkelKappelPersson/pi-shepherd) | 9 | Launches and coordinates specialized Pi agents in visible Herdr TUI panes, with shared fieldnotes for context. |
| [**darjss/herdr-orchestrate**](https://github.com/darjss/herdr-orchestrate) | 7 | Orchestrates visible Pi workers in Herdr with a run board, persistent reports, isolated Git worktrees, and model routing. |
| [**SuzuyaBish/foreman**](https://github.com/SuzuyaBish/foreman) | 3 | Runs a Pi foreman that delegates tasks to crew agents in separate Herdr TUI workspaces and Git worktrees. |
| [**TyRichards/pi-mega-brief**](https://github.com/TyRichards/pi-mega-brief) | 2 | Organizes a weekly task list into persistent Pi sessions and Herdr TUI tabs for multi-agent work. |
| [**wayne930242/pi-straw-boss**](https://github.com/wayne930242/pi-straw-boss) | 2 | Coordinates Pi agents across Herdr TUI tabs using a main agent per tab and a tower per workspace. Opens a browser view for monitoring agents and answering their questions. |
| [**L1aoXingyu/pi-herdr-multi-agent**](https://github.com/L1aoXingyu/pi-herdr-multi-agent) | 1 | Launches multi-model agent fleets in visible Herdr TUI panes from Pi and harvests results with a watchdog. |
| [**ooiyeefei/pixtension · extensions/pichestrator**](https://github.com/ooiyeefei/pixtension/tree/HEAD/extensions/pichestrator) | 0 | Runs guarded Pi subagents in Git worktrees and Herdr TUI, with a bash guard for credentials, production data, and destructive commands. |
| [**muslihudindev/herdr-agent-orchestrator**](https://github.com/muslihudindev/herdr-agent-orchestrator) | 0 | Coordinates multiple Pi software-engineering agents across isolated Herdr panes. |
| [**yanekyuk/pi-herdr-orchestrator**](https://github.com/yanekyuk/pi-herdr-orchestrator) | 0 | Coordinates project-independent Pi workers in visible Herdr TUI panes using `pi-goal` and lifecycle events. |
| [**alessandrofogli/pi-fleet**](https://github.com/alessandrofogli/pi-fleet) | 0 | Delegates Pi tasks to independent Herdr TUI sessions with isolated worktrees and shared task state. |
| [**Jalzn/pi-herdr-agents**](https://github.com/Jalzn/pi-herdr-agents) | 0 | Runs bounded autonomous Pi campaigns in Herdr TUI workspaces, including parallel campaigns and read-only observation. |
| [**blisk92/pi-herdr-orchestrator**](https://github.com/blisk92/pi-herdr-orchestrator) | 0 | Orchestrates Pi sub-agents as Pi processes running in Herdr panes. Sibling to pi-herdr-agents with deliberate differences. |
| [**Pfgoriaux/pi-dispatch**](https://github.com/Pfgoriaux/pi-dispatch) | 0 | Delegates Pi tasks to parallel or sequential workers and shows their hierarchy in Herdr TUI. Writer tasks use isolated Git worktrees. |
| [**gbozee/pi-pstack**](https://github.com/gbozee/pi-pstack) | 0 | Provides a native Pi port of poteto/pstack with multi-model routing, pi-subagents, Herdr, and Intercom integration. |
| [**dulvac/pi-team-panes**](https://github.com/dulvac/pi-team-panes) | 0 | Runs interactive Pi team workers in Herdr TUI panes or iTerm2 splits, with shared tasks and mailbox messages. |
| [**matifuentes2/pi-parallel-go-pr-herdr**](https://github.com/matifuentes2/pi-parallel-go-pr-herdr) | 0 | Runs parallel worktree-backed Pi PR agents in background Herdr tabs. |
| [**caina-barbosa/Herdr-orchestrator-bundle**](https://github.com/caina-barbosa/Herdr-orchestrator-bundle) | 0 | Coordinates visible Pi child sessions in Herdr with a watchdog, result handoff, and optional post-compaction resume. |
| [**conpiracy/ep-starter**](https://github.com/conpiracy/ep-starter) | 0 | Sets up a minimal Pi agent factory inside Herdr. |
| [**geniusgordon/pi-herdr-crew**](https://github.com/geniusgordon/pi-herdr-crew) | 0 | Dispatches and manage pi subagents as a Herdr crew. Each member answers through a markdown file, not the terminal. |
| [**duskoide/pi-herdr-worker**](https://github.com/duskoide/pi-herdr-worker) | 0 | Spawns Pi workers in Herdr TUI tabs or split panes and schedules parallel tasks by their declared file paths. |
| [**itc-steve/pi-herdr**](https://github.com/itc-steve/pi-herdr) | 0 | Delegates Pi tasks to named, model-configured workers in Herdr TUI panes, with concurrency and file-ownership controls. |

### Pi planner, coder and reviewer teams

*11 projects. Pi workflows with named planner, coder, tester and reviewer roles, often with plan approval and review gates.*

| Project | Stars | What it does |
|---|--:|---|
| [**jillesme/pi-herdr-squad**](https://github.com/jillesme/pi-herdr-squad) | 25 | Creates visible, strictly read-only investigation teams for Pi inside Herdr. It is intended for parallel research and review tasks that must not modify the workspace. |
| [**ribbons-digital/pi-herd**](https://github.com/ribbons-digital/pi-herd) | 23 | Coordinates visible Pi lead and worker sessions in Herdr TUI panes, isolating code-changing roles in Git worktrees. |
| [**Jackliu-miaozi/pi-herdr-workflow-kit**](https://github.com/Jackliu-miaozi/pi-herdr-workflow-kit) | 5 | Creates a controlled Pi workflow with separate planner, coder, and reviewer panes. Plans must be approved before coding, each phase is reviewed, and large handoffs are stored in `.pi-herdr/` files instead of pasted into the terminal. |
| [**nourhelmi/pi-meta-harness**](https://github.com/nourhelmi/pi-meta-harness) | 4 | Organizes Pi coding work around an advisor, builders, and optional reviewers, using Herdr and Git worktrees for delegation. |
| [**SecretAardvark/pi-overseer**](https://github.com/SecretAardvark/pi-overseer) | 1 | Runs implementer, tester, reviewer, and researcher agents under one supervisor. Each role has command limits, sensitive actions require approval, and task state is saved under `.pi/overseer/` so work can resume after a restart. |
| [**giacolees/plan-herdr-subagents**](https://github.com/giacolees/plan-herdr-subagents) | 1 | Provides a unified Pi workflow package combining grilling, pointer plans, sequential workers, and reviewers on Herdr subagents. |
| [**didy-kpn/pi-herdr-taskforce**](https://github.com/didy-kpn/pi-herdr-taskforce) | 0 | Coordinates role-based Pi teams in Herdr TUI workspaces through an asynchronous SQLite message box. |
| [**yanekyuk/pi-plain-herdr**](https://github.com/yanekyuk/pi-plain-herdr) | 0 | Creates a Herdr TUI workspace and Git worktree for a Pi writer, then supports independent review and verification. |
| [**itisbryan/pi-blanche**](https://github.com/itisbryan/pi-blanche) | 0 | Runs a crew of Pi planner, researcher, worker, and reviewer sessions in Herdr TUI panes using pi-intercom. |
| [**yajiefeng/pi-ticket-dispatcher**](https://github.com/yajiefeng/pi-ticket-dispatcher) | 0 | Dispatches approved tickets to Herdr TUI Pi workers for implementation, review, revision, and integration. |
| [**piotrekd00/pi-master-orchestrator**](https://github.com/piotrekd00/pi-master-orchestrator) | 0 | Moves one implementation ticket through a visible Pi worker and reviewer pair in Herdr TUI. |

### Pi extensions that control Herdr

*8 projects. Pi extensions and skills that give Pi tools or commands to inspect and drive Herdr workspaces, tabs, panes and agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**ogulcancelik/pi-extensions**](https://github.com/ogulcancelik/pi-extensions) | 573 | Extends Pi with overlays, parallel agent spawners, session recall, and direct Herdr pane control. |
| [**joelhooks/pi-bellwether**](https://github.com/joelhooks/pi-bellwether) | 89 | Exposes Herdr agent, pane, and session controls as Pi slash commands and LLM tools. It provides reusable start, send, read, focus, and stop operations for higher-level Pi workflows. |
| [**anrunt/herdr-pi-reloader**](https://github.com/anrunt/herdr-pi-reloader) | 1 | Reloads or restarts idle Pi sessions from a Herdr TUI popup without changing the tiled layout. |
| [**lucas-codes/pi-herdr-mentions**](https://github.com/lucas-codes/pi-herdr-mentions) | 1 | Adds @-mention completion of Herdr workspaces, tabs, and agents to the pi prompt, and swaps the chosen name for the Herdr id the agent can act on. |
| [**MrBenJ/pi-herdr**](https://github.com/MrBenJ/pi-herdr) | 0 | Controls Herdr TUI workspaces, tabs, panes, and agents from Pi through agent-callable tools. The README marks the project pre-release and says live smoke testing is pending. |
| [**taecontrol/pi-herdr**](https://github.com/taecontrol/pi-herdr) | 0 | Lets Pi inspect and control Herdr TUI workspaces, tabs, panes, agents, and worktrees through callable tools. |
| [**kodicw/pi-herdr**](https://github.com/kodicw/pi-herdr) | 0 | Lets Pi manage Herdr TUI workspaces, tabs, and panes and coordinate agents through callable tools. |
| [**lalanikarim/herdr-skills**](https://github.com/lalanikarim/herdr-skills) | 0 | Teaches Pi to manage Herdr workspaces and run an orchestrator and worker in separate panes. |

### Pi sidebars, trees and subagent viewers

*5 projects. Pi extensions and viewers that show Pi agents, subagents, telemetry and subagent transcripts in a Herdr sidebar, tree or pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**RamonsDka/gs3-sidebar**](https://github.com/RamonsDka/gs3-sidebar) | 7 | Shows a read-only sidebar for Pi and Gentle Shell in Herdr TUI, including agent status, context, Git and subagents. |
| [**edxeth/herdr-pi-tree**](https://github.com/edxeth/herdr-pi-tree) | 4 | Shows Pi agents and their subagents as a Herdr TUI sidebar tree with worktree branches and Git status. |
| [**NickPittas/pi-herdr-subagents**](https://github.com/NickPittas/pi-herdr-subagents) | 2 | Monitors Pi's asynchronous subagents and shows their IDs, tasks, states, and session files in a TUI. It can open or focus a subagent session, or start one in a pane, without changing how Pi runs it. |
| [**mastnacek/pi-herdr-sidebar**](https://github.com/mastnacek/pi-herdr-sidebar) | 1 | Shows Pi agent telemetry in a Herdr TUI pane or popup, including model, context window, tokens, cost, and skill gates read from the Pi session log. Built in Rust with Ratatui. |
| [**Nabsku/herdr-pi-subagents**](https://github.com/Nabsku/herdr-pi-subagents) | 0 | Opens a Herdr TUI pane with a read-only Pi child transcript for the matching pi-subagents fork. |

### Oh My Pi orchestration and viewers

*9 projects. Tools built for Oh My Pi (OMP) that delegate work, attach live panes and watch OMP workers in Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**hanbong5938/herdr-omp-subagents**](https://github.com/hanbong5938/herdr-omp-subagents) | 3 | Shows the active Oh My Pi main-agent and subagent models in the Herdr TUI sidebar. |
| [**bekto/omp-herdr-panes**](https://github.com/bekto/omp-herdr-panes) | 3 | Opens read-only Herdr TUI panes that stream each oh-my-pi subagent’s tool calls and output until it finishes. |
| [**sfsajid91/omp-orchestrator**](https://github.com/sfsajid91/omp-orchestrator) | 2 | Delegates Oh My Pi tasks to isolated workers in Herdr tabs with selectable model routes. |
| [**CarrisHarter/herdr-omp-attach-panes**](https://github.com/CarrisHarter/herdr-omp-attach-panes) | 1 | Opens interactive Herdr TUI panes for Oh My Pi Vibe workers, with live transcripts and prompt input. Requires a fork of Oh My Pi with its attach client. |
| [**ericjuta/omp-fleet**](https://github.com/ericjuta/omp-fleet) | 1 | Observes an existing Oh My Pi worker fleet in Herdr and records durable status and terminal reports. |
| [**ubranch/omp-herdr-neighbors**](https://github.com/ubranch/omp-herdr-neighbors) | 1 | Tells an omp agent which other Herdr agents run beside it, with their status and last reply. Sends hidden context only when it changes and has no runtime dependencies. |
| [**reoring/sheltie**](https://github.com/reoring/sheltie) | 0 | Coordinates manifest-declared OMP agent teams in Herdr workspaces using durable SQLite messaging. |
| [**xenking/omp-extensible-workflows**](https://github.com/xenking/omp-extensible-workflows) | 0 | Supervises dependency-aware Beads tasks with OMP workers in isolated Git worktrees and Herdr tabs. |
| [**lfsmoura/pi-interactive-subagents-herdr**](https://github.com/lfsmoura/pi-interactive-subagents-herdr) | 0 | Runs interactive Oh My Pi subagents concurrently in Herdr TUI panes and returns their results to the parent. |
