# Awesome Herdr: Run and orchestrate agents

The full list for domain 1 of [Awesome Herdr](../README.md#1-run-and-orchestrate-agents), ordered by GitHub stars.

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

---

## 1. Run and orchestrate agents

*639 projects. Supervisors, delegation tools, coding loops, queues, and reusable workflow packs for running one or many agents.*

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
| [**LeaveMyYard/herdr-inbox**](https://github.com/LeaveMyYard/herdr-inbox) | Collects the open questions of Claude Code agents running in Herdr into one popup inbox, so agents ask once and keep working while you answer later. Each answer is delivered back to the pane that asked, through an MCP server and Claude Code plugin. |
| [**Kvmyk/herdr-foreman**](https://github.com/Kvmyk/herdr-foreman) | Turns one plain-language task into a plan that a lead agent splits across your installed coding agents, each running in its own Herdr pane and git worktree. Workers first only propose changes, and nothing lands on your branch until you approve a numbered list. |
| [**gronare/kebbie**](https://github.com/gronare/kebbie) | Runs trunk-based development for Claude Code in Herdr: a lead session plans tasks from your backlog, each task gets an agent in its own worktree, and one board shows what each needs from you. Reviewed commits go straight onto main instead of through pull requests. |
| [**navishachiku/herdr-mailbox**](https://github.com/navishachiku/herdr-mailbox) | Gives each receiving agent a mailbox in Herdr so worker reports merge into one stream and decision questions are answered in a side pane instead of interrupting the leader. Ships a send skill and a CLI for claiming, delivering and withdrawing letters. |
| [**ellingtonsp/herdr-orch**](https://github.com/ellingtonsp/herdr-orch) | Adds a coordination layer on Herdr so one agent runs a team of others: a mailbox, blocking ask and reply, tasks with dependencies, tracked dispatch, decision gates and verified worker release. Agents and you drive it through the horch CLI. |
| [**mohaphez/herdr-flow**](https://github.com/mohaphez/herdr-flow) | Coordinates a planning agent and separate implement, review and repair sessions in a task-specific git worktree, with a file-backed state and guarded worktree cleanup. Works with Claude Code, Codex, OpenCode and Pi, and never commits or merges automatically. |
| [**hasuwini77/worktree-fleet**](https://github.com/hasuwini77/worktree-fleet) | Adds /fleet and /crew skills that split a task into file-disjoint buckets, run one Claude Code or Codex agent per bucket in its own Herdr tab and worktree, and merge the results. Includes a live fleet board popup. |
| [**EvanBatten/firstmate-for-windows**](https://github.com/EvanBatten/firstmate-for-windows) | Runs Claude Code crewmates in their own Herdr tabs and git worktrees on Windows 11 under Git Bash. Watches the crew and returns finished pull requests and reports. |
| [**floor/teamcli**](https://github.com/floor/teamcli) | Runs a roster of agents from different vendors as a team in Herdr panes from a Node CLI. Watches for idle seats and nudges the operator. |
| [**CristianonCarvalho/meisterrouter**](https://github.com/CristianonCarvalho/meisterrouter) | Splits a plan into tasks and runs them in parallel on Copilot, Claude, Codex, Gemini and Kiro CLIs with a test gate before merge. Can open each worker in a visible Herdr tab as an optional Herdr plugin. |
| [**duncanam/mustr**](https://github.com/duncanam/mustr) | Runs a coordination hub in a Herdr tab per space where Pi agents join with roles, exchange addressed messages and own tasks. Includes a self-contained `mustr --ai-help` reference. |
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
| [**avery20024/herdr-async-message-relay**](https://github.com/avery20024/herdr-async-message-relay) | Queues messages between Herdr agents in SQLite and delivers each one when the recipient role is idle. Routes by stable role name and includes a terminal UI for message history. |
| [**alexlayton/herdr-bots**](https://github.com/alexlayton/herdr-bots) | Lets coding agents in Herdr TUI panes find each other, send messages, and delegate tasks. Nudges an idle bot by typing a one-line prompt into its pane. |
| [**zeromountain/herdr-roles**](https://github.com/zeromountain/herdr-roles) | Assigns roles to Herdr TUI panes, spawns a team of role panes from the main pane, and hands work between roles. Korean README. |
| [**est7/herdr-amq-adapter**](https://github.com/est7/herdr-amq-adapter) | Lets coding agents in Herdr TUI panes message each other by name over AMQ with no manual setup. Wakes the receiving agent through herdr agent prompt. |
| [**youssef-tharwat/agent-mail**](https://github.com/youssef-tharwat/agent-mail) | Gives Codex and Claude Code agents local task assignment, messages, and review cycles stored in SQLite, with optional Herdr TUI delivery that wakes the right agent pane. Ships a Herdr plugin manifest. |
| [**viswassaripalli/agxchat**](https://github.com/viswassaripalli/agxchat) | Lets Claude and Codex sessions in different repos send each other threaded requests through a local mailbox, with Herdr waking the target pane and a terminal view of threads. Includes deadlock guards and stall detection. |
| [**harry81/herdr-team**](https://github.com/harry81/herdr-team) | Starts a four-pane planner, worker, and reviewer crew in Herdr with one command. Includes role agents and workflow presets. |
| [**Dtenwolde/herdr-orchestrator**](https://github.com/Dtenwolde/herdr-orchestrator) | Shows a live priority board of Herdr workspaces, agents, git state, and GitHub PRs ranked by what needs you next. Pairs it with a read-only Claude Code session that keeps a TODO and writes a morning briefing. |
| [**slogsdon/herdbot**](https://github.com/slogsdon/herdbot) | Runs persistent AI bots on your machine, each in its own Herdr workspace, with subagents opened in panes next to them. Routes tasks across Claude, Codex, Cursor, and Pi subscriptions. |
| [**DailybotHQ/herdr-peers**](https://github.com/DailybotHQ/herdr-peers) | Lets any agent in a Herdr pane ask an agent in another pane or on another machine and get one authorized reply back. |
| [**sfrangulov/prorab**](https://github.com/sfrangulov/prorab) | Turns one Claude Code session into a foreman that issues work orders to crews of Claude Code sessions, each in its own Herdr pane and git worktree. Tracks budgets, answers crew questions, and writes a morning report. |
| [**zachristmas/baa-ton**](https://github.com/zachristmas/baa-ton) | Steers work across Herdr workspaces from a Codex control layer, dispatching Claude Code, Pi, OpenCode, or Codex workers with scoped goals, a CLI, and a stdio MCP server. Setup runs through a reviewed installer. |
| [**HYPERVAPOR/herdr-pair-coding**](https://github.com/HYPERVAPOR/herdr-pair-coding) | Runs worker and reviewer agent pairs in Herdr panes, each pair in its own worktree, with a watchdog that keeps the pair moving. Installs as agent skills and works with pi. |
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
| [**pparitoshh/herdr-hive**](https://github.com/pparitoshh/herdr-hive) | Runs one brain agent and several workers per workspace, each worker in its own git worktree, talking over a local SQLite message bus. A review bench tab shows each worker's diff. |
| [**mandoworks/roostr**](https://github.com/mandoworks/roostr) | Opens a live board pane with one row per agent showing tag, name, model, state, and blocked alerts. Adds context compaction warnings, task editing, and workspace recovery with backups. |
| [**Ejlonn/herdr-supervisor**](https://github.com/Ejlonn/herdr-supervisor) | Supervises durable Claude and Codex workflows in Herdr with human approval steps, quota waiting, and remote control through Telegram. Preserves native sessions and rechecks limits without spending tokens. |
| [**mvschwarz/herdr-openrig**](https://github.com/mvschwarz/herdr-openrig) | Opens an OpenRig agent team's operator and advisor from Herdr, shows what needs you, follows tasks between agents, and sends messages to any agent. |
| [**pelayomendez/watchmen**](https://github.com/pelayomendez/watchmen) | Keeps a long-lived Claude Code companion session beside your work that tracks tickets, merge requests, and worker sessions. In Herdr it summons the session and shows a sidebar token. |
| [**Sakib75/herdr-hq**](https://github.com/Sakib75/herdr-hq) | Opens one Claude Code agent in a Herdr TUI popup that hands your requests to the agents already working in your tabs and follows up on them. |
| [**Siregar/herdr-review-relay**](https://github.com/Siregar/herdr-review-relay) | Sends an Engineering agent's PR to every QA agent in a Herdr TUI tab, waits for their reviews and returns them to Engineering in one prompt. Supports Claude Code and OpenCode. |
| [**mrrobot-ec/pod**](https://github.com/mrrobot-ec/pod) | Lets a coordinating agent in the Herdr TUI run a team of Claude Code, Codex and Grok workers in their own tabs and worktrees. Adds reviewers, advisors and a board, with usage tracked for Claude and Codex. |
| [**Phoobobo/herdr-bot**](https://github.com/Phoobobo/herdr-bot) | Runs a team of named Grok or pi bots, such as a lead, engineer and researcher, from an overlay in the Herdr TUI with DMs and channels. Ties each team to one Herdr session and resumes it. |
| [**heywji/aiboard**](https://github.com/heywji/aiboard) | Splits a task into lanes that Claude Code hands to Codex, Grok, Kimi, Gemini and Claude, each running headless in a Herdr pane you can take over. Passes work between models as files and sends security findings to another vendor for review. |
| [**SRHSolution/srh-session-broker**](https://github.com/SRHSolution/srh-session-broker) | Lets Claude Code and Codex sessions hand work to each other by name or role, typing the message into the target Herdr pane. Adds a safety gate for risky requests, an MCP server, and a terminal and web dashboard. |
| [**GustavoGomez092/herdr-dots**](https://github.com/GustavoGomez092/herdr-dots) | Attaches specialist agents called dots, such as security or frontend reviewers, to Claude Code or Codex sessions in Herdr TUI. Each dot checks every turn and speaks up only when needed, and dots can convene as a council. |
| [**cabra-lat/herdr-plugin-amq**](https://github.com/cabra-lat/herdr-plugin-amq) | Coordinates turn-based coding agents with Maildir messaging, lifecycle-aware doorbells, a task bus, and a content-addressed evidence store. Adds a web dashboard for mail threads and agent presence. |
| [**gaiagent0/ct304-hermes-bots**](https://github.com/gaiagent0/ct304-hermes-bots) | Provides a Hermes bot network coordinating agents across Herdr workspaces with capability-based model distribution. |
| [**kody-w/rapp-herdr**](https://github.com/kody-w/rapp-herdr) | Manages RAPP Twin neighborhoods as supervised Herdr workspaces. |

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
| [**l20250208/herdr-consensus**](https://github.com/l20250208/herdr-consensus) | Combines two isolated agent reviews into a consensus, human decision, fix plan, and worktree-based fix. |
| [**bandoyer/swarm-forge-herdr**](https://github.com/bandoyer/swarm-forge-herdr) | Runs role-based agent swarms in separate Git worktrees with validated handoffs and optional human approval. |
| [**bandoyer/swarm-forge-windows**](https://github.com/bandoyer/swarm-forge-windows) | Provides a Windows distribution of swarm-forge-herdr for running AI agent swarms on the Herdr runtime. |
| [**binthnay1973/deepthink**](https://github.com/binthnay1973/deepthink) | Runs a multi-agent research panel in Herdr panes, cross-checks independent findings, and consolidates a sourced verdict. |
| [**burningportra/vibing-with-herdr**](https://github.com/burningportra/vibing-with-herdr) | Coordinates a same-branch Herdr TUI swarm that drains Beads tasks using exclusive Agent Mail reservations instead of worktrees. |

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
| [**shaun-agent/herdr-map**](https://github.com/shaun-agent/herdr-map) | Renders visual Mermaid diagrams mapping Herdr architecture, socket APIs, and workspace concepts. |
| [**jmcjm/Hivemind**](https://github.com/jmcjm/Hivemind) | Coordinates a swarm of Claude Code agents in Herdr terminal panels using file-based briefs and asynchronous mail. |
| [**Marie673/herdr-env**](https://github.com/Marie673/herdr-env) | Configures an integrated Herdr, ghq, and Claude Code workspace environment mapping one branch to each agent worktree. |
| [**eliasstravik/herdr-chat**](https://github.com/eliasstravik/herdr-chat) | Provides a live structured chat view for agents running inside Herdr. |
| [**inbeomheo/herdr-orchestra**](https://github.com/inbeomheo/herdr-orchestra) | Coordinates Codex, Grok, Gemini, or Claude worker panes from a central Claude Code controller session. |
| [**LittleDrinks/herdr-orchestrator-skill**](https://github.com/LittleDrinks/herdr-orchestrator-skill) | Turns the main Claude Code session into a coordinator that plans work, starts workers in Herdr panes, and monitors them without editing code itself. It includes Python monitors, a YAML state-machine template, and role prompts. |
| [**alexhooi/herdr-orchestrate**](https://github.com/alexhooi/herdr-orchestrate) | Runs Claude Code, Codex CLI and pi as visible, interruptible terminal-pane agent teams. One orchestrator, cross-model review, review-gated merges. |
| [**lutian/herdr-sdd-harness**](https://github.com/lutian/herdr-sdd-harness) | Provides a Spec-Driven Development harness using Herdr for orchestration. |
| [**izumi0uu/terminal-theme-suite**](https://github.com/izumi0uu/terminal-theme-suite) | Switches iTerm2, OMP, Herdr, and terminal wallpapers as one coordinated theme suite. |
| [**combinaut/ai-agent-orchestration**](https://github.com/combinaut/ai-agent-orchestration) | Installs a Coordinator, architects and workers team of Claude Code and Codex agents in visible Herdr panes. Includes a Herdr todo plugin and a one-line installer. |
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
| [**kamil-pociot/herdr-claude-agents**](https://github.com/kamil-pociot/herdr-claude-agents) | Shows Claude Code background sessions as Herdr agents, one tab each in the project space. Reports live state and notifications for sessions that run in the Claude daemon. |
| [**rephol/wt-pack**](https://github.com/rephol/wt-pack) | Runs a team of Claude Code agents that plan, build, review, and ship tickets, each in its own git worktree. Agents run as Herdr panes. |
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
| [**wasamin0130/TeamNestReferenceFlow**](https://github.com/wasamin0130/TeamNestReferenceFlow) | Runs a six-role team of Claude Code agents in Herdr TUI panes with parallel planning and review waves, handoff files, and an Orchestrator skill. Needs TeamNest and a Team Pack with matching role ids. |
| [**ClockworkNet/herdr-claude-tmux-swarm**](https://github.com/ClockworkNet/herdr-claude-tmux-swarm) | Opens a Claude Code tmux-mode teammate swarm in a split pane beside the spawning Claude pane and closes it when the swarm ends. |

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
| [**lucas-codes/pi-herdr-mentions**](https://github.com/lucas-codes/pi-herdr-mentions) | Adds @-mention completion of Herdr workspaces, tabs, and agents to the pi prompt, and swaps the chosen name for the Herdr id the agent can act on. |
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
| [**Qingswe/herdr-router**](https://github.com/Qingswe/herdr-router) | Picks the coding agent, model and reasoning effort for a task from an editable difficulty policy, then starts that agent in a new Herdr pane and sends the task. Explains each decision and includes a web policy editor. |
| [**guiand888/herdr-mistral-vibe**](https://github.com/guiand888/herdr-mistral-vibe) | Starts Mistral Vibe sessions in Herdr panes through an action and a pane entrypoint, since Herdr has no built-in agent kind for it. Pairs with herdr-vibe, which reports Vibe state and resume commands. |
| [**zekierman/orkestra**](https://github.com/zekierman/orkestra) | Teaches Claude Code to lead Codex and Antigravity workers running in the same Herdr workspace. A session-start hook tells Claude who is in the room; README is Turkish with an English version. |
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
| [**Herdanis/the-cat-concerto**](https://github.com/Herdanis/the-cat-concerto) | Installs an orchestrator prompt and worker contract that spawns a Herdr pane per sibling repo and delegates work to a worker agent. Reviews each result. |
| [**BlockedPath/herdr-amp-orbs**](https://github.com/BlockedPath/herdr-amp-orbs) | Runs Amp orbs, which are remote Amp agents, in Herdr TUI panes as amp agents. Herdr detection then shows their state and sends done notifications. |
| [**jsabo/herdr-beams**](https://github.com/jsabo/herdr-beams) | Launches agents on Teleport Beams runtimes from the Herdr TUI sidebar. Creates workspaces, picks per-launch agent profiles, and shows agent status next to local work. |
| [**varvand/herdr-plugin-agent-spawn**](https://github.com/varvand/herdr-plugin-agent-spawn) | Opens several panes of one coding agent from a single prompt like claude 3 in a popup, tiled in a new tab with Herdr agent names. |
| [**GODVvVZzz/herdr-agent-chat**](https://github.com/GODVvVZzz/herdr-agent-chat) | Lets a main Claude Code session delegate work to persistent worker agents in sibling panes or other workspaces without blocking. Workers report back over a message channel and a watcher flags workers that die. |
| [**ahqrt/dsh-herdr**](https://github.com/ahqrt/dsh-herdr) | Delegates DeepSeek Harness subtasks to coding agents running in Herdr panes, then collects the exact results for review in DSH. Lets you pick the model and keep the terminal visible. |
| [**Arluigi/my-skills · herdr-delegate**](https://github.com/Arluigi/my-skills/tree/HEAD/herdr-delegate) | Lets an expensive model orchestrate cheaper Claude, GPT, and Gemini helpers, each shown as a Herdr pane nested under its orchestrator. Includes a Herdr plugin panel and usage-aware routing. |
| [**boriscardano/herdr-jev-router**](https://github.com/boriscardano/herdr-jev-router) | Lets a parent agent describe a task and have the Jev routing service pick the harness, model and effort for the child agent from the task and remaining subscription capacity. Needs a TypeSafe API key, installs with herdr plugin install and is advisory only. |
| [**IGUNUBLUE/hirc**](https://github.com/IGUNUBLUE/hirc) | Lets agents in Herdr panes message each other IRC-style with roster, send, ask, read and wait, across agent kinds and saved SSH machines. Installs an agent skill into detected skill directories; the repo is archived. |
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
| [**benediktneumayer2-tech/aqt-sensei-herdr**](https://github.com/benediktneumayer2-tech/aqt-sensei-herdr) | Pairs the focused Herdr agent with a read-only advisor from another vendor and asks you to approve each message in a popup. Logs every step to an evidence ledger. |
| [**owpac/herdr-fork**](https://github.com/owpac/herdr-fork) | Forks the Claude Code or Codex session of the focused pane into a new split or tab. The original conversation stays unchanged. |
| [**maromocooo/herdr-second-opinion**](https://github.com/maromocooo/herdr-second-opinion) | Opens a second coding agent in a split to review the latest output or diff of the one you work with. Lets you send back only the findings you adopt. |
| [**charlesberret/herdr-cowbell**](https://github.com/charlesberret/herdr-cowbell) | Opens a popup picker that launches or relaunches a coding agent in the current directory with chosen settings and shows the exact command first. Can also bind itself to a Herdr key. |
| [**qivyn/herdr-broadcast**](https://github.com/qivyn/herdr-broadcast) | Sends one prompt to several coding agents and shows their live terminals in a browser page. Continues in rounds on local or saved SSH machines. |
| [**moonquddus/lookout**](https://github.com/moonquddus/lookout) | Shows each Claude Code subagent and background shell in its own pane with prompt, tool calls, and live output. Closes panes shortly after the work stops. |
| [**zenodea/lodestar**](https://github.com/zenodea/lodestar) | Lets one leader agent split a request into tasks, start crewmate agents, and merge their results, inside Herdr, tmux, or Rex. Mixes Claude Code, Codex, and pi. |
| [**Taanviir/herdr-quick-prompt**](https://github.com/Taanviir/herdr-quick-prompt) | Picks a coding agent and prompt with one key, then launches it in a new tab, split, workspace, or worktree. Can also send follow-ups to a running agent. |
| [**calebcauthon/handoff**](https://github.com/calebcauthon/handoff) | Copies a Claude Code conversation from one pane and pastes it as a fork into another pane or a new split. Ships as a Herdr TUI plugin and as a Herdr app mod. |
| [**abroller666/agent-relay**](https://github.com/abroller666/agent-relay) | Sends the last finished answer of the agent in one Herdr TUI pane, plus your instruction, to the agent in another pane. Supports Claude Code, Codex and Devin CLI on either side. |
| [**Crabor/herdr-clone-agent**](https://github.com/Crabor/herdr-clone-agent) | Clones the coding agent of a Herdr TUI pane into a new right or down pane that resumes a fork of its session. Supports pi and Claude Code. |
| [**xhluca-agent/herdr-docker-agents**](https://github.com/xhluca-agent/herdr-docker-agents) | Runs coding agents such as pi and opencode inside Docker containers while Herdr TUI agent start, prompt and wait commands and status keep working. |
| [**SkymanOne/herdr-boxd**](https://github.com/SkymanOne/herdr-boxd) | Starts a boxd machine from a snapshot and attaches it in a Herdr TUI pane. Other agents can use it to run coding subagents inside boxd machines and track them. |
| [**aalvarezdeliveryhub/herdr-lock**](https://github.com/aalvarezdeliveryhub/herdr-lock) | Makes every worker agent that Claude Code starts open in its own tab of the same Herdr TUI workspace and folder as the session that spawned it. |
| [**candidosales/herdr-laya-router**](https://github.com/candidosales/herdr-laya-router) | Classifies a task with a local Laya model, then picks Claude Code, Codex, or OpenCode plus model and effort and launches it in Herdr. Runs classification on your machine. |

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
| [**QuentinTorg/stagehand**](https://github.com/QuentinTorg/stagehand) | Coordinates author and reviewer agents across Herdr TUI worktrees and hands reviewed work to GitHub pull requests. |
| [**UN-9BOT/herdr-codex-autoresume**](https://github.com/UN-9BOT/herdr-codex-autoresume) | Resumes a Codex CLI /goal automatically after the usage limit resets by typing the resume command into the pane. Records the reset time and restores the original model. |
| [**HigorAlves/luna-tui**](https://github.com/HigorAlves/luna-tui) | Adds a Herdr plugin board where you plan tickets that move through a fixed pipeline of agents in Docker containers. Stops at approval gates for your sign-off. |
| [**edbienes/drovr**](https://github.com/edbienes/drovr) | Runs a Herdr-based development loop with isolated implementation, a repository quality gate, two independent reviews, and a human-gated merge. |
| [**sarmientoF/herdr-pr-loop**](https://github.com/sarmientoF/herdr-pr-loop) | Runs tester, coder, and reviewer agents through local task cycles and GitHub pull-request reviews in separate tabs. State is stored in files, while approval gates, logs, a budget limit, and a pause file keep runs controllable. |
| [**henrywang/herdr-workflow**](https://github.com/henrywang/herdr-workflow) | Runs multi-agent Herdr TUI workflows with cross-model planning, adversarial review and bounded iterations toward pull requests. |

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
| [**hexsprite/herdr-beads**](https://github.com/hexsprite/herdr-beads) | Opens Beads issue details in a Herdr TUI split when an issue ID is Ctrl-clicked. |
| [**GNURub/herdr-prompt-bucket**](https://github.com/GNURub/herdr-prompt-bucket) | Adds a durable, ordered prompt bucket for coding agents running in Herdr. |
| [**qluto/collie**](https://github.com/qluto/collie) | Adds an unattended-work box for Claude Code sessions on Herdr: toss tasks in by day, spend leftover token quota on them at night, collect the results in the morning. |
| [**rohanthewiz/herdr-todo**](https://github.com/rohanthewiz/herdr-todo) | Queues terminal prompts using Bubble Tea, letting you filter and paste them into Claude Code panes. |
| [**husniadil/herdr-tasks**](https://github.com/husniadil/herdr-tasks) | Tracks agent tasks and notes in Herdr TUI with renewable claims, evidence-backed review, and a human decision gate. |
| [**sazardev/herdr-code-board**](https://github.com/sazardev/herdr-code-board) | Dispatches agent prompts from a kanban queue into Herdr panes, workspaces, and worktrees, with rules that chain cards. |
| [**pjgeutjens/omarchy-feed-the-flock**](https://github.com/pjgeutjens/omarchy-feed-the-flock) | Queues typed or dictated Omarchy notes and delivers them to Herdr TUI agents when they are ready. |
| [**barkerja/herdr-msg**](https://github.com/barkerja/herdr-msg) | Adds persistent mailboxes for agents in Herdr TUI and notifies recipient panes when messages arrive. |
| [**guidodinello/herdr-routines**](https://github.com/guidodinello/herdr-routines) | Runs scheduled routines that spawn a Herdr pane, start Claude Code or OpenCode and send it one prompt, driven by a systemd user timer and a YAML job list. The plugin adds actions to run a job and check its status from inside Herdr. |
| [**nicholasjstock/paneyard**](https://github.com/nicholasjstock/paneyard) | Queues well-scoped coding tasks for Claude Code and Codex and runs them in parallel, each on its own branch and worktree as a live agent session in Herdr. You can watch, steer and resume each session and get a report when the work is ready. |
| [**m0hdrar/kanban_tui**](https://github.com/m0hdrar/kanban_tui) | Runs a keyboard-first kanban board with per-project cards in a Herdr pane and jumps to it with a bound key. A status command prints open work for the Herdr tab bar, and agents can manage cards from the shell. |
| [**virtualboard/herdr-virtualboard**](https://github.com/virtualboard/herdr-virtualboard) | Shows VirtualBoard feature specs as a kanban board inside Herdr, where moving a card runs the vb CLI. Dispatching a card starts a VirtualBoard role agent in a visible pane. |
| [**salmonumbrella/herdr-kata**](https://github.com/salmonumbrella/herdr-kata) | Runs Kata cron jobs and workflows as agents and commands on herdr-core and reports each run back to Kata. Works as a headless worker with no UI of its own. |
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
| [**larrychannon/herdr-job-board**](https://github.com/larrychannon/herdr-job-board) | Opens a board in a Herdr split pane for work handed to coding agents, grouped as waiting on you, doing, queue, to do and done. A coordinator agent writes cards with a small CLI. |
| [**philals/mission-control-capcom**](https://github.com/philals/mission-control-capcom) | Breaks a Jira story into PR-sized tasks and shows tasks, draft PRs and CI stages on a terminal board. An optional Herdr plugin opens the board by key and launches agents in Herdr panes. |
| [**DnzzL/herdr-docket**](https://github.com/DnzzL/herdr-docket) | Runs a task queue where a named agent turns a card into one pull request and a second agent verifies it. Merges through a merge gate in code or hands the PR to you. |
| [**connerohnesorge/herdr-agent-queue**](https://github.com/connerohnesorge/herdr-agent-queue) | Queues prompts for Claude Code and other agents in Herdr TUI and submits each as a new turn after the current turn ends. |
| [**schemaitat/herdr-aven-plugin**](https://github.com/schemaitat/herdr-aven-plugin) | Dispatches Aven tasks to OpenCode agents in Git worktrees through herdr-core and supervises them from your terminal. Adds optional Herdr app mods with a task panel and a kanban board. |
| [**DanielFGray/foreman**](https://github.com/DanielFGray/foreman) | Dispatches coding agents across a task backlog through a pipeline you draw: author, review, and land, with approval gates. Includes a Herdr app pane that shows the pipeline and tasks. |
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
| [**calvinp0/herdr-htask**](https://github.com/calvinp0/herdr-htask) | Shows a Herdr side panel of what coding agents have done, are doing, and have blocked, from a shared SQLite task store. Agents add tasks with the htask command. |
| [**GumbyEnder/herdr-devboards**](https://github.com/GumbyEnder/herdr-devboards) | Shows Dev Boards missions in a Herdr pane across all lanes and binds running missions to agent panes. Claims, delivers, escalates, and dispatches missions to idle agents. |
| [**dj-skn/schedule-send**](https://github.com/dj-skn/schedule-send) | Schedules prompts, files, or key presses to agent or shell panes at a chosen time, or after a Claude Code or Codex usage limit resets. Runs jobs through systemd or launchd timers so the terminal can close. |
| [**Zeotyn/spec-kanban**](https://github.com/Zeotyn/spec-kanban) | Shows OpenSpec changes or Spec Kit features as a kanban board in a Herdr pane. |
| [**chmouel/herdr-taskr**](https://github.com/chmouel/herdr-taskr) | Picks and runs Just, Make, Taskfile, npm, and Cargo tasks from a fuzzy finder and sends failing output to the agent. |
| [**Adroz/herdr-feedr**](https://github.com/Adroz/herdr-feedr) | Shows a markdown-backed to-do sidebar in Herdr TUI that you and your coding agents share. Agents claim items, add their own and report back through one file. |
| [**federbenjamin/herdr-desk**](https://github.com/federbenjamin/herdr-desk) | Adds a task board pane to the Herdr TUI where you and your agents track tasks. Includes a coordinator, a runner that starts tasks and a session journal. |
| [**thientrile/herdr-hjob**](https://github.com/thientrile/herdr-hjob) | Runs a long command in the background so an agent need not poll it. When it ends, hjob wakes the agent pane with the result through herdr-wake. |
| [**Wormav/herdr-queue**](https://github.com/Wormav/herdr-queue) | Lets you draft, reorder and queue prompts in a dedicated terminal panel beside an agent in Herdr TUI, then send the one you want. |
| [**qselle/herdr-todo**](https://github.com/qselle/herdr-todo) | Opens a task popup in Herdr TUI to capture plans, mark current work, review finished tasks, and link tasks to workspaces. Keeps history on disk. |
| [**Operator-create/herdr-kitchen-brigade**](https://github.com/Operator-create/herdr-kitchen-brigade) | Runs your repository checks when a Herdr TUI coding agent finishes, writes a local report, and sends the agent a short failure message. Needs no Python dependencies. |
| [**tyz-works/herdr-task-graph**](https://github.com/tyz-works/herdr-task-graph) | Shows a live terminal dependency graph of tasks in the Herdr TUI with agent state and which work is ready to run in parallel. |
| [**bestony/herdr-auto-retry**](https://github.com/bestony/herdr-auto-retry) | Continues Herdr TUI agents automatically when they stop on rate-limit, overload, or capacity errors. |
| [**saforem2/herdr-hermes-kanban**](https://github.com/saforem2/herdr-hermes-kanban) | Shows a Hermes Kanban board in a Herdr TUI pane with a quick-capture popup. Uses only the hermes kanban CLI. |
| [**zamarrowski/herdr-tasks**](https://github.com/zamarrowski/herdr-tasks) | Opens a plain to-do list in a Herdr popup to add, check, edit, reorder, and delete tasks. Includes a CLI so coding agents can add tasks too. |
| [**dlv-gold/herdr-tasks**](https://github.com/dlv-gold/herdr-tasks) | Adds a right-side task panel to Herdr TUI with daily tasks, weekly missions, and per-space reports. Codex or Claude can summarize each space and suggest tasks to add. |
| [**thientrile/herdr-wake**](https://github.com/thientrile/herdr-wake) | Queues wake-up events on disk and delivers them to an idle Herdr agent pane through herdr agent prompt, retrying until the agent is free. Installs as a Herdr TUI plugin with a systemd user worker on Linux. |

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
| [**kukv/octoscope**](https://github.com/kukv/octoscope) | Adds GitHub issue and pull-request management to Herdr, including review, tracking, and assignment of GitHub work to agent tabs from inside the terminal. |
| [**itisbryan/herdr-gh-checks**](https://github.com/itisbryan/herdr-gh-checks) | Watches pull request CI in a Herdr pane and shows CI and merge status in the sidebar. |
| [**kiitosu/herdr-jira-board**](https://github.com/kiitosu/herdr-jira-board) | Embeds a Jira Kanban board in a Herdr pane with one-key Claude Code session launching and live card status updates. |
| [**hanbong5938/herdr-jira-worktree**](https://github.com/hanbong5938/herdr-jira-worktree) | Opens Jira issues in Herdr TUI and creates Git worktrees or jj workspaces from them. Browse comments, change issue status, and delegate work to an agent. |
| [**tomoasleep/herdr-symphony**](https://github.com/tomoasleep/herdr-symphony) | Reads issues from GitHub Projects, creates `gwq` worktrees, and runs one OpenCode agent per issue inside Herdr workspaces. |
| [**bredebjorhovd/herdr-board**](https://github.com/bredebjorhovd/herdr-board) | Assigns GitHub issues to agents in dedicated Herdr panes and moves completed work into pull-request review. |
| [**tferreira/herdr-pr-ops**](https://github.com/tferreira/herdr-pr-ops) | Shows your pull requests and review requests on one board in a popup over your panes, grouped by state and repo. One key starts a coding agent in its own Herdr pane to review, re-check or ship a PR. |
| [**juscribe/herdr-plugin**](https://github.com/juscribe/herdr-plugin) | Files and transitions Juscribe tickets from a Herdr pane and moves a ticket to started when an agent begins working. Shows which ticket each agent is on, using the signed-in jus CLI so the plugin never handles your token. |
| [**zamarrowski/herdr-issues**](https://github.com/zamarrowski/herdr-issues) | Lists GitHub issues of the current repo plus Linear issues and Shortcut stories, and hands one to any coding agent in its own git worktree. Works with Claude Code, Codex, Gemini CLI, Pi, OpenCode and other agents Herdr can start. |
| [**seandavi/factory-control-ref**](https://github.com/seandavi/factory-control-ref) | Turns GitHub issues into a work queue for pi agents running in Herdr sessions, with a web UI and actions API served over Tailscale. Surfaces blocked questions, PRs ready to merge and failed runs. |
| [**matheus3301/herdr-shortcut**](https://github.com/matheus3301/herdr-shortcut) | Lists assigned Shortcut stories in a terminal picker and launches the selected story in a new Herdr agent tab. |
| [**ZviBaratz/herdr-draft**](https://github.com/ZviBaratz/herdr-draft) | Provides a new-session creation dialog unifying Linear issues, worktree creation, agent types, and initial prompts. |
| [**H3xept/herdr-ingest**](https://github.com/H3xept/herdr-ingest) | Turns Sentry, Linear, or GitHub work items into Herdr TUI spaces and Git worktrees with agent briefs, waiting for user confirmation before starting an agent. |
| [**ukwhatn/taskherd**](https://github.com/ukwhatn/taskherd) | Tracks agent sessions, GitHub pull requests, and Jira tickets on a local task board that can jump to Herdr TUI sessions. |
| [**spiritsack/herdr-jira-worktree**](https://github.com/spiritsack/herdr-jira-worktree) | Creates or reuses a ticket-specific Git worktree and prefills its Jira ID or URL into a coding agent in Herdr TUI. |
| [**brooswit-factory/butchr**](https://github.com/brooswit-factory/butchr) | Provides the software factory: watches your Jira, runs herdr agents on active tickets, pushes updates to them over MCP. |
| [**nyanyaon/github-issue-herdr-plugin**](https://github.com/nyanyaon/github-issue-herdr-plugin) | Browses the current repository’s open GitHub issues and comment threads in a read-only Herdr TUI pane. |
| [**abtris/herdr-plugin-jira-pr**](https://github.com/abtris/herdr-plugin-jira-pr) | Checks the current branch's GitHub pull request against linked Jira tickets. It shows ticket state and warns when issue keys are missing or do not match, keeping Jira context visible in Herdr. |
| [**ssk090/herdr-clickup**](https://github.com/ssk090/herdr-clickup) | Browses ClickUp sprints, lists, and tasks in a Herdr TUI tab and starts an agent on a task in its own worktree. Reports back when the agent finishes. |
| [**khanal-samir/herdr-jira-workspace**](https://github.com/khanal-samir/herdr-jira-workspace) | Opens a Jira Kanban board, calendar worklogs, comments, and attachments inside Herdr TUI. Sends Herdr notifications for ticket activity. |
| [**rigelstpierre/herdr-devin-board**](https://github.com/rigelstpierre/herdr-devin-board) | Lists your Devin Cloud sessions in a herdr tab with live GitHub PR, CI, and review status. Attaches to a session in a new tab with `devin --cloud --resume`, opens `devin ssh` in a pane, or archives it. |
| [**maimuzo/continuo**](https://github.com/maimuzo/continuo) | Turns GitHub Projects v2 cards into a queue for Claude Code workers in Herdr panes and updates board status after execution. |
| [**YuSa0-6/herdr-issue-flow**](https://github.com/YuSa0-6/herdr-issue-flow) | Creates Herdr workspaces and Git worktrees for GitHub issues, with Pi conductor and worker sessions and Hunk review handoff. |
| [**korvyashka/herdr-pr-relay**](https://github.com/korvyashka/herdr-pr-relay) | Picks pull requests and dispatches them to active agent sessions as review prompts. |
| [**hilmimuktitama/herdr-jira-peek**](https://github.com/hilmimuktitama/herdr-jira-peek) | Finds Jira Cloud issue keys in a Herdr TUI pane and opens read-only issue descriptions and comments alongside it. |
| [**NightingaleMedia/herdr-github-orobo**](https://github.com/NightingaleMedia/herdr-github-orobo) | Runs in a Herdr TUI split or tab and sends work to an existing agent or starts a new one. Its pull-request dashboard is being migrated. |
| [**jeremN/herdr-dispatch-plugin**](https://github.com/jeremN/herdr-dispatch-plugin) | Dispatches tickets through an AI-agent pipeline, one git worktree per ticket, each phase in a named pane, fail-closed, with a human approval gate. |
| [**hdtradeservices/ticketdeck**](https://github.com/hdtradeservices/ticketdeck) | Shows Linear projects and tickets in a terminal dashboard and launches or reattaches Claude Code sessions in Herdr TUI. |
| [**PanchTime/linear-widget**](https://github.com/PanchTime/linear-widget) | Displays Linear issues in an Omarchy bar widget and opens ticket worktrees or agent sessions in Herdr TUI. |
| [**Mamprim-go/sdlc-herdr**](https://github.com/Mamprim-go/sdlc-herdr) | Runs a GitHub issue workflow with Pi agents in Herdr TUI panes for triage, planning, implementation, review, and QA. |
| [**solcreek/linear-tui · herdr-plugin**](https://github.com/solcreek/linear-tui/tree/main/herdr-plugin) | Opens linear-tui, a terminal UI for Linear issues with inline images, over, beside or as a popup on the focused Herdr TUI pane. Ctrl-click on a Linear issue link opens it there, and a demo action needs no account. |
| [**U5K492/herdr-new-workspace-extended**](https://github.com/U5K492/herdr-new-workspace-extended) | Extends new workspace in the Herdr TUI so you can start from a GitHub issue or pull request with gh and fzf, from a branch name, or from a plain name. |
| [**manoel-freitas/herdr-kanban**](https://github.com/manoel-freitas/herdr-kanban) | Opens a Kanban board of the current workspace's GitHub issues in Herdr TUI, showing the live agent or human assignee on each card and letting you move cards between columns. |
| [**jenthous/herdr-linear**](https://github.com/jenthous/herdr-linear) | Searches Linear issues as you type in a Herdr TUI popup or side pane, renders issue bodies and comments as Markdown, and copies issue and PR links. Pins the issue matching the current branch. |
| [**alfonsodg/herdr-glab-tasks**](https://github.com/alfonsodg/herdr-glab-tasks) | Adds a GitLab issues panel grouped by status label to the Herdr TUI, with an action that creates an issue and its branch and handling for issue links. |
| [**drewbitt/herdr-jiratui**](https://github.com/drewbitt/herdr-jiratui) | Opens JiraTUI in a Herdr TUI tab and sends the selected Jira issue's key, summary, link, and description to a running agent. |
| [**jacksonpires/herdr-app-reviewq**](https://github.com/jacksonpires/herdr-app-reviewq) | Turns GitHub review requests into ready Herdr app spaces by creating a git worktree per pull request and running its setup commands. Adds a status-bar counter, toasts and a queue panel, and removes untouched worktrees after the PR leaves your queue. |
| [**ChristianDeckert/herdr-jira-light**](https://github.com/ChristianDeckert/herdr-jira-light) | Shows a Jira pane in the Herdr TUI whose filters follow the current tab's directory, with project, board and sprint browsing and issue details. Runs on zsh, curl and jq with no build step. |
| [**haoyuant/tomrade-plugins · herdr**](https://github.com/haoyuant/tomrade-plugins/tree/main/herdr) | Opens Tomrade tickets from the Herdr TUI by Ctrl-clicking a ticket key and claims a pane's agent to a ticket. Offers a claim when a new worktree is created. |
| [**PolyphonyRequiem/twig-herdr**](https://github.com/PolyphonyRequiem/twig-herdr) | Opens a Twig work-item panel in Herdr TUI with a tree and table, scrollable item detail, and digest-based proposal review. Needs Twig 0.93.0 or newer and Node.js 22. |

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
| [**eteplus/agent-workbench**](https://github.com/eteplus/agent-workbench) | Defines a multi-agent workflow where Claude Code or Pi acts as Main and delegates sub-tasks to Pi agents through Herdr. Covers task grading, model routing and review gates; docs are Chinese. |
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
| [**fveracoechea/operator**](https://github.com/fveracoechea/operator) | Adds skills and a CLI that let one coordinating agent dispatch worker agents in OpenCode and Claude Code through Herdr. Tracks assignments, worktrees, pull requests, and reports so each agent gets its next action. |
| [**ptshih/fsd**](https://github.com/ptshih/fsd) | Coordinates coding agents from implementation through review and integration using Herdr tabs, Git worktrees, and filesystem handoffs. Installs as a Claude Code plugin or Pi skill. |
| [**nyjin/herdr-skills**](https://github.com/nyjin/herdr-skills) | Adds Claude Code skills that run parallel coding agents in git worktrees and show each worker in the Herdr sidebar. Installs as a Claude Code plugin or per skill. |
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
