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
| Terminal UX | ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) [herdr-leap](#worktrees-config--terminal-ux) | EasyMotion jump + copy any screen region |
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

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[ogulcancelik/herdr-plugin-github-start](https://github.com/ogulcancelik/herdr-plugin-github-start)**

An official plugin from Herdr's creator that turns a GitHub issue, PR, or discussion into a ready-to-work agent tab — it creates the tab, starts Codex or Claude, renames the session, and sends a structured prompt describing the linked item, all from one bound keypress. It accepts short references like `#614` or `issue 614` as well as full URLs. For developers who kick off agent sessions straight from a GitHub ticket without assembling the context by hand.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[cloudmanic/herdr-plus](https://github.com/cloudmanic/herdr-plus)**

A first-class Herdr plugin built around two accelerators: Projects, declarative TOML templates that spin up an entire workspace — every tab, pane, and startup command — from a fuzzy picker in one keypress; and Quick Actions, a fuzzy launcher for one-off scripts in the current directory. It installs with or without a local Go toolchain and ships prebuilt binaries. For power users who want one-keypress environment setup across many repositories and a fast palette for recurring tasks.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[firegnu/herdr-loop-lab](https://github.com/firegnu/herdr-loop-lab)**

A loop-engineering toolkit that layers three kinds of bounded agent iteration on Herdr: an inner loop that converges a single task through a mechanical gate and an adversarial cross-model judge, a fleet layer that runs batches of tasks in parallel worktrees, and an epic layer that decomposes a large goal and integrates the results into a branch. All state lives on disk so an interrupted run resumes cleanly. For developers who want auditable, convergence-checked agent loops rather than open-ended runs that stall silently.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[Tudor0404/dual-author](https://github.com/Tudor0404/dual-author)**

A Claude Code skill that processes GitHub issues end-to-end inside Herdr: each issue gets its own worktree, a Claude worker implements and pushes a draft PR, then paired Codex and Claude reviewers in split panes run fix-and-review rounds until the diff is clean and auto-merge is armed. A dashboard pane tracks per-issue stage and elapsed time across everything running in parallel. For teams who want a hands-off issue-to-merge pipeline that stays observable in the terminal.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[razajamil/herdr-factory](https://github.com/razajamil/herdr-factory)**

An autonomous coding factory that claims items from Jira or local markdown task files, spins up a Herdr worktree per item, and runs Claude Code through an ordered pipeline of steps (fix → review → PR, or a custom belt), riding each PR through CI and review to merge under a global concurrency cap. Belts are YAML-configured with their source, steps, match predicates, and priority. For teams who want a walk-away pipeline built on Herdr's workspace and worktree primitives.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[tomoasleep/herdr-symphony](https://github.com/tomoasleep/herdr-symphony)**

A headless orchestrator (docs in Japanese) that polls a GitHub Projects board for candidate issues, creates worktrees with `gwq`, and runs an `opencode` agent per issue in a Herdr pane, using `herdr agent wait` to detect completion. Agent state and logs live entirely in Herdr workspaces rather than a separate dashboard. For teams who want a background issue-to-PR pipeline driven from a project board.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[madarco/agentbox-herdr-plugin](https://github.com/madarco/agentbox-herdr-plugin)**

Brings the AgentBox sandbox into a Herdr session: a live overlay on `prefix+a`, a one-key shortcut to start a sandboxed VM in the current project, and an `agentbox://` Ctrl-click link handler. The plugin installs from the Herdr marketplace and wires its keybindings through a generated shim so the manifest stays static. For Herdr users who run agents in AgentBox sandboxes and want to reach them without leaving the terminal.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[joelhooks/pi-bellwether](https://github.com/joelhooks/pi-bellwether)**

A Pi package that exposes Herdr's agent, pane, and session control surface as Pi slash commands and LLM tools — start, send, read, focus, and stop agents without leaving a Pi conversation. It's deliberately generic runtime plumbing that product-specific loop extensions can build on rather than reimplement. For Pi users who want to drive Herdr orchestration from inside Pi.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[NickPittas/pi-herdr-subagents](https://github.com/NickPittas/pi-herdr-subagents)**

A Pi extension that hooks Pi's async subagent event bus, tracking each run's id, task, status, and session file, and exposes a TUI dashboard where you can browse live subagents, open their session in a new tab, focus an existing pane, or spawn one directly into a pane. Unlike the shared-pane model of `aldrickdev/herdr_subagents`, it watches without changing how subagents run. For Pi users with many concurrent subagents who want one navigable view of the whole fleet.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[kirel/herdr-subagents](https://github.com/kirel/herdr-subagents)**

A Pi extension that spawns each subagent into its own Herdr pane or tab, manages the session files, and notifies the parent session on completion so the orchestrator picks up results without polling. Child panes stay open after reporting back, leaving room for follow-up work, and each subagent can run on a different model. A dedicated-pane alternative to the shared-pane `aldrickdev/herdr_subagents`.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[gustavocaiano/opencode-herdr](https://github.com/gustavocaiano/opencode-herdr)**

An OpenCode plugin that watches for subagent session creation and automatically splits a new Herdr pane running `opencode attach` for each one, tiling them in a row-based grid to keep the layout readable. Panes can close automatically on idle, deletion, or error. For OpenCode users who want live visibility into every active subagent without splitting panes by hand.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[machine-machine/herdr-factory-loop-skill](https://github.com/machine-machine/herdr-factory-loop-skill)**

An installable skill that teaches Claude Code or Hermes to orchestrate a fleet of coding agents through Herdr — discovery, spawn, dispatch, fan-out/converge, approval unblocking, and spec-driven loops where `tasks.md` markers map directly to parallel workers. An onboarding TUI sets up the whole factory in one pass across Claude, Hermes, or Cursor. Broader than a coordinator-only skill: it adds steered and meta-orchestration tiers and integrates spec-kit.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[machine-machine/ask-fable-skill](https://github.com/machine-machine/ask-fable-skill)**

A Hermes and Claude Code skill that spawns an interactive Claude Code (Fable 5) worker inside Herdr, hands it the prompt through a file, and reads the complete answer back — sidestepping TUI scraping and output truncation. The worker's session UUID is surfaced so a follow-up can resume the same conversation. For users whose primary agent is a lighter tier who want to route deep-reasoning tasks to a more capable model without switching sessions.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[yangyang0507/herdr-skill](https://github.com/yangyang0507/herdr-skill)**

A refinement of the default Herdr coordination patterns that swaps vague `wait agent-status done` polling for output-marker waits and structured messages carrying sender pane, reply-to metadata, and task kind — so a receiver can answer directly without the sender blocking. Ships a dependency-free `herdr-msg` Bash helper and a CLI reference behind progressive disclosure. For multi-agent workflows where blocking waits create needless stalls between sibling agents.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[bakescakes/claude-orchestration](https://github.com/bakescakes/claude-orchestration)**

A Claude Code plugin bundling five orchestration skills — a full-lifecycle "boss-mode" conductor, a one-shot Herdr fan-out, the Herdr CLI reference, an end-of-session durability auditor, and a docs scaffolder — alongside hooks that guard worktree hygiene, route prompt events, and report session state. Boss-mode owns a backlog of parallel initiatives end-to-end: spawn, build, QA gate, merge, deploy, verify-live, teardown. For Claude Code users who want a pre-wired multi-skill setup rather than assembling the pieces.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[0x5c0f/herdr-insight](https://github.com/0x5c0f/herdr-insight)**

A live timeline panel — dockable at the bottom or right — that aggregates agent task events across every Herdr workspace, showing working and blocked states, session IDs, and a deduplicated 7-day history, with individually togglable columns. It follows agents across workspace switches without a manual refresh. For anyone running several agents at once who wants a single panel to see which are active, blocked, or idle.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[rohanthewiz/herdr-todo](https://github.com/rohanthewiz/herdr-todo)**

A Bubble Tea TUI for prompts you want to run later: jot multi-line entries with optional titles, fuzzy-filter them, then press Enter to paste one into a running Claude Code pane or spin up a fresh `claude` tab in the current workspace. Per-repo backlogs live under `<repo>/.herdr-todo/` so they travel with the project, alongside a global backlog visible everywhere. For engineers who accumulate follow-up prompts mid-session and want to queue them without interrupting the agent.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[freewillythe4th/action-button-agent](https://github.com/freewillythe4th/action-button-agent)**

A bridge that turns an iPhone Action Button into a remote for your own Herdr agents: a bundled iOS Shortcut with Whisper dictation sends a voice-transcribed task over Tailscale through a personal Telegram bot to a Claude Agent SDK operator, which starts or targets the right Herdr lane and replies in Telegram. A self-bootstrapping skill handles the one-time setup. For developers who want to assign work to their Herdr-backed agents from anywhere without opening a laptop.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[erwins-enkel/shepherd](https://github.com/erwins-enkel/shepherd)**

Self-hosted mission control for interactive coding agents: spawn, watch, and steer many real Claude Code or Codex sessions in parallel from a browser or phone, each running in its own git-worktree pane that Herdr multiplexes. Plan-review, PR-critic, and merge-train gates layer engineering discipline on top of the parallelism. For teams running several agents at once who want a supervised fleet rather than a wall of terminals.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[carze/herdr-smolmachine](https://github.com/carze/herdr-smolmachine)**

Launches a coding agent fully sandboxed in a libkrun/KVM microVM straight from a Herdr pane, while Herdr keeps its usual multiplexing and detach/reattach UX around the isolated process. A baked agent image and a shell dispatch pipeline handle the VM lifecycle. For Linux users who want hardware-level isolation per agent without giving up Herdr's pane control.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[sean1588/herdr-orchestrator](https://github.com/sean1588/herdr-orchestrator)**

A Go control-plane daemon that drives the issue-to-PR loop from a declarative YAML state-graph, using Herdr as the execution backend — it spawns an implementer agent in a worktree, then a reviewer, then polls GitHub's merge gate before squash-merging (dry-run by default). Workflow configs are JSON-Schema-validated and checked with a `validate` subcommand. For teams who want a deterministic, auditable pipeline around agent-driven PRs.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[saiashirwad/homestead](https://github.com/saiashirwad/homestead)**

Provisions an isolated worktree per branch or GitHub issue — its own ports, `.env`, and setup — and boots a coding agent into a Herdr pane for each, then tracks status, lands finished branches, and tears them down. It shells out to the Herdr CLI and only runs inside an active Herdr session. For developers running several agents or issues in parallel who are tired of services fighting over port 3000.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[noor-latif/herd](https://github.com/noor-latif/herd)**

Two companion scripts that spin up a project-scoped Herdr workspace with an N-agent grid (default 2×2, one Pi agent per pane) keyed to the current directory, and relaunch any dead agents when you return. For anyone who wants a repeatable one-command "start a grid of agents for this repo" setup.

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

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[54rt1n/herdr-simple-mcp](https://github.com/54rt1n/herdr-simple-mcp)**

A single-binary MCP server that exposes Herdr's socket API as MCP tools with no state of its own — each call opens a fresh socket, sends one request, and returns. It covers 75 methods across workspace, tab, pane, agent, layout, and plugin surfaces, with named profiles (`coordinator`, `client`, `observer`) to scope the tool set per agent role and `HERDR_MCP_DENY` globs for finer removal; an unknown profile falls back to read-only. A leaner, role-aware alternative to the recipe-engine `herdr-mcp` for wiring agents straight to Herdr.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[lib-x/herdr-sock-go](https://github.com/lib-x/herdr-sock-go)**

A Go module that speaks Herdr's newline-delimited JSON socket protocol directly, generated against the 0.7.0 surface, with typed helpers for common calls (current pane, pane read, agent-status subscribe) and a `Call`/`CallRaw` escape hatch for the rest. Socket resolution follows the standard env-var and default-path chain. The Go counterpart to the existing Python socket client, for developers writing plugins, CLIs, or automation in Go.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[CodyBontecou/herdr-telemetry-bridge](https://github.com/CodyBontecou/herdr-telemetry-bridge)**

A plugin that listens to Herdr lifecycle events and emits an NDJSON stream of pane focus intervals, detected agent and model metadata, and local session-trace summaries to a file, an HTTP webhook, or any command's stdin. Raw transcript text is redacted by default, with opt-in controls for trusted local sinks. For developers building menu-bar apps, time-trackers, or dashboards who want structured Herdr activity without writing their own socket client.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[junliu-mde/mimo-code-herdr-plugin](https://github.com/junliu-mde/mimo-code-herdr-plugin)**

A user-level MiMo Code plugin that reports idle / working / blocked / done state to Herdr's sidebar via `pane.report_agent`, using an aggregate state machine across all MiMo subagent sessions to avoid flicker during multi-session runs. A detached watchdog releases the pane label on any exit — including `kill -9` and hard crashes — and a subprocess guard suppresses the plugin when MiMo runs as a tool call inside another pane. For MiMo Code users who want their agent's status visible in Herdr without waiting for native support.

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

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[razajamil/herdr-hex-browser-voice-command](https://github.com/razajamil/herdr-hex-browser-voice-command)**

A Chrome extension plus local daemon that watches which browser URL was focused while you spoke to the Hex voice transcriber, then routes the resulting transcript to the matching Herdr workspace and pane — no manual focus switch. Routing rules map URL patterns to workspace/tab/pane triples and are configured in the extension popup. For developers who dictate to several Claude Code panes and want each spoken instruction to land in the right agent automatically.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[klittle32/letta-herdr-mod](https://github.com/klittle32/letta-herdr-mod)**

A Letta Code modification that reports accurate idle / working / blocked state to Herdr's socket when the agent runs inside a Herdr pane, so a Letta session shows up in the status sidebar like any native agent. For Letta Code users who want the same pane-status visibility Herdr already gives other agent CLIs.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[Phoobobo/herdr-traex-integration](https://github.com/Phoobobo/herdr-traex-integration)**

Wires TraeX's lifecycle hooks to Herdr's `pane.report_agent` / `pane.release_agent` socket calls, so a TraeX pane shows correct idle / working / blocked status in the sidebar even though Herdr ships no built-in detector for it. For anyone running the TraeX CLI agent inside Herdr panes.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[vaclavik-xyz/herdwatch](https://github.com/vaclavik-xyz/herdwatch)**

Keeps a Herdr pane flagged as working — with a ⏳ label — while background CI, review, or manual-marker work is still pending after the agent itself has gone idle, so a finished-looking pane isn't mistaken for done. Runs standalone or as a background service. For anyone whose agent wraps up a turn before the checks it triggered actually complete.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[carsonjones/herdr-agent-dashboard](https://github.com/carsonjones/herdr-agent-dashboard)**

A diff-rendered terminal dashboard (Bun + React/opentui) that lists every running Herdr agent with live status, reachable as a keybound plugin action or run standalone. For anyone managing many concurrent agent panes who wants one glanceable table instead of tabbing through workspaces.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[alexei-led/ccgram](https://github.com/alexei-led/ccgram)**

A Telegram bridge that maps each forum topic to one terminal window running an agent — Claude Code, Codex, Gemini, Pi, or a shell — and relays keystrokes and output over the multiplexer, with Herdr as a first-class backend alongside tmux. For developers who want to walk away mid-session and keep monitoring or replying to their Herdr agent panes from a phone.

---

## Editor integrations

Bringing Herdr into the editor you already live in.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) ![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[devxplay/herdr.nvim](https://github.com/devxplay/herdr.nvim)**

Unifies pane navigation between Neovim and Herdr: the same `Ctrl+h/j/k/l` that moves between Vim splits flows straight into the adjacent Herdr pane when you hit an edge, and back again. A small Rust helper talks to the socket for focus, splits, and layout, and it coexists with vim-tmux-navigator — Neovim detects whether it's inside Herdr or tmux and routes accordingly. For Neovim users who want one set of muscle memory across editor and multiplexer.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[MomePP/herd.nvim](https://github.com/MomePP/herd.nvim)**

Makes Neovim the top-level UI for Herdr coding agents: spawn an agent into a fullscreen floating terminal, toggle it with one key, and push the current visual selection straight to the active agent without submitting. Herdr stays the backend process owner, so its status hooks and grouped dashboard keep working. For Neovim-first developers who want editor-native agent UX without giving up Herdr's orchestration layer.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[paulbkim-dev/vim-herdr-navigation](https://github.com/paulbkim-dev/vim-herdr-navigation)**

A port of vim-tmux-navigator to Herdr: `Ctrl+h/j/k/l` flows between Vim/Neovim splits and adjacent Herdr panes, crossing the boundary at an edge in either direction. It runs as a real Herdr plugin action, checking the pane's foreground process via `herdr pane process-info` to decide whether to forward the key or move pane focus. For developers with vim-tmux-navigator muscle memory who want it working identically in Herdr.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[lmilojevicc/herdr-splits.nvim](https://github.com/lmilojevicc/herdr-splits.nvim)**

A port of smart-splits.nvim to Herdr that adds resizing to the navigation story: the same `Alt+h/j/k/l` that resizes Neovim splits delegates to Herdr when a window fills the terminal edge, and movement likewise crosses the boundary. Ships configurable at-edge behaviors (wrap, stop, split, custom callback), count-prefix support, and auto-unzoom on navigate. For Neovim users who want both navigation and resize parity between editor and multiplexer.

![Vim Script](https://img.shields.io/badge/-555555?logo=vim&logoColor=white&style=flat-square) **[luiarthur/herdr.vim](https://github.com/luiarthur/herdr.vim)**

A Vim and Neovim plugin that spawns a language-appropriate REPL in a Herdr pane and sends the current line, the whole file, or a visual selection to it with one key. Supports Vim 7.4 through 9 and Neovim 0.5+, with remappable defaults. For data scientists and scripters who want a send-to-REPL workflow inside Herdr without leaving the editor.

![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square) **[UN-9BOT/sidekick_herdr](https://github.com/UN-9BOT/sidekick_herdr)**

Adds Herdr as a first-class session backend to sidekick.nvim, the Neovim plugin for AI CLI tools that already supports tmux and zellij — drop it in alongside sidekick.nvim and set `herdr` as the session provider, no fork or upstream patch required. For sidekick.nvim users who run Herdr as their multiplexer and want the same agent-launcher UX they'd get with tmux.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[Daniel-Steinberger/obsidian-herdr](https://github.com/Daniel-Steinberger/obsidian-herdr)**

An Obsidian desktop plugin that sends the next unchecked to-do from a markdown checklist to an agent running in the matching Herdr workspace and ticks the box when the agent finishes; a continuous mode works through a whole list unattended. For people who plan work in Obsidian notes and want Herdr to execute it directly.

---

## Sessions: switch & restore

Finding the session you want, attaching to it, and getting it all back after a reboot.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[ridho9/switchr](https://github.com/ridho9/switchr)**

A full-screen session picker for Herdr: it lists every session next to its workspace / tab / pane tree, and you attach to the one you want with a keypress. Wire it up as your terminal's startup command and it greets you on each new window; it also spots an incompatible daemon and offers an in-place restart. For anyone juggling several named sessions who wants a fast visual switchboard.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[j0urneyk/herdrctx](https://github.com/j0urneyk/herdrctx)**

A keyboard-driven TUI for the housekeeping side of sessions — attach, stop, delete, create, and search, without copying names out of `herdr session list`. It ships through a Homebrew tap with prebuilt macOS and Linux binaries and refuses to launch nested when you're already inside a Herdr pane. For developers managing sessions across many projects who want a faster daily driver than the raw CLI.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[nickmaglowsch/herdr-session-restore](https://github.com/nickmaglowsch/herdr-session-restore)**

Tags every Claude Code pane with a session ID, then snapshots your workspace / tab / cwd layout on a clean `herdr server stop` and replays it on the next cold boot — `claude --resume` and all — so your conversations come back where you left them. Claude-only and clean-shutdown-only by design, it's the answer to losing your agent setup to a reboot.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[thanhdat77/herdr-picker-plus](https://github.com/thanhdat77/herdr-picker-plus)**

A single ratatui overlay — no fzf dependency — that surfaces open workspaces, Herdr Plus project templates, filesystem roots, zoxide frecency, SSH hosts, agent panes, and configured plugin integrations in one place. Selecting an SSH host creates or re-focuses a `server: NAME` workspace and runs the connection in its tab; selecting a directory checks for an existing workspace at that path before making a new one. For power users who want one keystroke to reach anything in their Herdr session.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[andrewchng/herdr-sessionizer](https://github.com/andrewchng/herdr-sessionizer)**

A tmux-sessionizer-style workflow for Herdr: `fzf` over your project roots to open a workspace, or over your git worktrees to reopen one, with a TOML config defining the tabs, pane splits, and per-pane startup commands that appear. Ships a README-preview panel, per-repo layout overrides, and a `bat`-powered file preview. For developers who want one keypress to land in a fully arranged workspace rather than building it each time.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[alon-z/herdr-command-palette](https://github.com/alon-z/herdr-command-palette)**

A minimal palette — no Rust build step — that merges open workspaces, configured project roots, and optionally zoxide frecency into one fuzzy list; selecting a directory focuses an existing workspace for that path or creates one. Deliberately lighter than herdr-picker-plus: no SSH, no agent panes, no plugin contract, just workspace and directory navigation. For users who want a small standalone switcher without the full picker surface.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[third774/herdr-last-workspace](https://github.com/third774/herdr-last-workspace)**

Stores the last two focused workspace IDs (not positional numbers, so it survives reordering) and binds one key to toggle focus between the current and previous workspace; if the previous one was closed, it exits cleanly with no error toast. For keyboard-heavy users who bounce between two workspaces and want a single `prefix+Tab` to do it.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[maayanyosef/herdr-aws-ssm](https://github.com/maayanyosef/herdr-aws-ssm)**

Fuzzy-pick a running EC2 instance across your AWS profiles and drop into a full `herdr --remote` session tunneled over AWS SSM, using ephemeral EC2 Instance Connect keys and auto-detected SSH users — no bastion, public IP, or long-lived keys. For teams who want Herdr's remote thin-client session on private-subnet EC2 boxes.

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

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[qdentity/herdr-worktree-lifecycle](https://github.com/qdentity/herdr-worktree-lifecycle)**

Dispatches `worktree.created`, `worktree.opened`, and `worktree.removed` to executable wrappers the repo ships itself (`scripts/worktree-setup` and `scripts/worktree-teardown`), serializing concurrent events per worktree path and notifying on completion. Unlike plugins that run a fixed command or read a TOML, the provisioning logic lives inside the repo being developed — the plugin is just the wiring. For teams who want reproducible per-repo setup checked into source control alongside the code it prepares.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[shizlie/herdr-setup-bootstrap](https://github.com/shizlie/herdr-setup-bootstrap)**

Reads `worktree_init.toml` from the main repo root and, for each new worktree, runs the configured command and copies the listed glob patterns (`.env*`, `.wrangler`, `public/`, …) from the primary checkout into the new one, preserving each file's repo-relative path. It hooks both the CLI and UI creation paths and writes an idempotency marker so a checkout is bootstrapped only once. For monorepos where gitignored locals need to travel to every worktree, not be re-created from scratch.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[persiyanov/herdr-fresh-worktree](https://github.com/persiyanov/herdr-fresh-worktree)**

On `worktree.created` it fetches `origin HEAD` and hard-resets the new worktree's branch to it — but only when the branch has no upstream, no same-named remote branch, a clean tree, and no commits that live nowhere else, so it freshens a genuinely new branch without ever moving real work. A `node --test` suite exercises every guard and idempotency path against throwaway repos. For developers who keep getting worktrees based on a stale local main and want each new branch to start from the real upstream tip.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[razajamil/herdr-plugin-workspace-manager](https://github.com/razajamil/herdr-plugin-workspace-manager)**

Define tabs, pane splits, and per-pane startup commands once in YAML, point a repo at a layout, and every new worktree — created from the CLI or the TUI — opens straight into it. Supports a one-off blocking setup command (e.g. `npm install`) before the layout spawns, and ships a `remove-gone` command that prunes worktrees whose upstream branch was deleted after a merge. For developers who rebuild the same working view by hand every time they start a feature branch.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[alon-z/herdr-devup](https://github.com/alon-z/herdr-devup)**

Drop a `.herdr/dev.toml` into a project and three actions handle the dev stack: `up` opens the declared tabs and panes running each service, `sync` re-pulls the ngrok tunnel URL and rewrites every env file that bakes it in, and `down` closes exactly the tabs `up` created. The sync step is the differentiator — tunnel URLs rotate, and hand-updating four `.env` files before restarting is the usual time-sink. For full-stack developers who run a tunnel alongside local services and want the URL propagated automatically.

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

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[arjenblokzijl/herdr-launcher](https://github.com/arjenblokzijl/herdr-launcher)**

Defines named workflows as `.mjs` files, each declaring an arbitrary set of input fields and a `run()` function — filling the gap that single-input Quick Actions leaves open. The same workflows are reachable from a Herdr picker overlay or a plain `herdr-launcher run <name>` CLI call, so they fit interactive and scripted use alike. For teams who want config-as-code workflow menus without a dedicated dashboard.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[JanTvrdik/herdr-command-palette](https://github.com/JanTvrdik/herdr-command-palette)**

Opens an `fzf` overlay listing every action exposed by every installed plugin, so you can fuzzy-search and invoke any of them without memorizing keybindings. It routes around the no-TTY constraint of plugin actions by spawning an overlay pane that carries the originating workspace's cwd, then tears down cleanly after selection. For users with many plugins who want a single `prefix+p` to reach any action.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[smarzban/herdr-file-viewer](https://github.com/smarzban/herdr-file-viewer)**

A read-only TUI that lives in a Herdr split: the left pane is a git-status directory tree (M/A/D/? markers, changed-files filter, merge-base or HEAD baseline) and the right pane renders diffs, Markdown, or syntax-highlighted code chosen automatically by file state. In-pane fuzzy search, per-file search, a worktree switcher, and zoom ship out of the box, delegating to `delta`/`bat`/`glow` when present and degrading gracefully when not. For developers who want to review an agent's working tree without switching context.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[devskale/herdr-flist](https://github.com/devskale/herdr-flist)**

Splits a narrow sidebar to the right of the focused pane and keeps it in sync with that pane's working directory as you `cd` — including inside SSH sessions, where the remote cwd is parsed from the shell prompt because Herdr doesn't propagate OSC 7 over SSH. Entries are dirs-first with git-status tags and polled on a configurable interval. A lighter glance than the full content-rendering herdr-file-viewer, for users who just want to see where they are.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[x0d7x/herdr-fzf-url](https://github.com/x0d7x/herdr-fzf-url)**

Iterates every Herdr pane, captures visible content, extracts URLs by regex, deduplicates them, and pipes the list to `fzf` — Enter opens in a browser, `y` copies to the clipboard. A native-Herdr rewrite of tmux-fzf-url. For users whose agent or build panes emit URLs they'd rather not hunt for in scrollback.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[rmarganti/herdr-pluck](https://github.com/rmarganti/herdr-pluck)**

Mirrors tmux-fingers in Herdr: the bound key overlays one- and two-letter hints on every copyable token in the focused pane — URLs, paths, commit SHAs, UUIDs, IPs, Kubernetes refs, hex literals — and typing a hint copies that token to the clipboard, no mouse. A complement to herdr-fzf-url's URL-only scope. For anyone who copies long identifiers out of terminal output dozens of times a day.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[RooseveltAdvisors/herdr-leap](https://github.com/RooseveltAdvisors/herdr-leap)**

EasyMotion/leap-style motion for Herdr: press the key, type a character, and one- and two-letter hints land on every occurrence of it in the focused pane — jump to one, then pick a second to copy the arbitrary region between them. Where token pickers (herdr-pluck, herdr-fzf-url) only hit detected URLs/paths/SHAs, herdr-leap targets any character and any span, so you can grab prose, log lines, or a half-word. For anyone who wants tmux-jump and extrakto-style reach from the keyboard, not just token copy.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[beomjungil/herdr-lazygit-overlay](https://github.com/beomjungil/herdr-lazygit-overlay)**

A two-file plugin: a manifest that declares a lazygit pane with `overlay` placement, and a launcher that forwards the focused pane's cwd via `--cwd` before opening it. Herdr's overlay mode zooms lazygit over the active pane and restores focus and zoom state on exit. For users who want one binding to inspect git state without rearranging their layout.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[edmundmiller/herdr-plugin-hunk](https://github.com/edmundmiller/herdr-plugin-hunk)**

Six actions — worktree, staged, and branch diffs, each in a split pane or a new tab — that launch the Hunk diff viewer scoped to the active workspace, with `HUNK_THEME` passing a named theme so it stays visually consistent with your Herdr theme. For teams already running Hunk who want diff panes without leaving their session.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[carsonjones/herdr-plugin-tiles](https://github.com/carsonjones/herdr-plugin-tiles)**

Adds six named split actions — 60/40 and 40/60 horizontals, 20/80 and 80/20 verticals, and 50/50 resets per axis — that override Herdr's default even split, with `shift` flipping which side is large and `alt` resetting to even. For users who routinely stage a sidebar or narrow reference pane and want consistent ratios without the mouse.

![Zig](https://img.shields.io/badge/-555555?logo=zig&logoColor=white&style=flat-square) **[kamaaina/herdr_sync](https://github.com/kamaaina/herdr_sync)**

Type a command in your pane, then trigger the plugin action instead of Enter and herdr_sync sends the text to every other pane in the current tab at once — the synchronize-panes idea, rebuilt for Herdr in Zig. For users who need to run the same command across several concurrent agent or shell panes without copy-pasting across splits.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[twadams21/cc-controller](https://github.com/twadams21/cc-controller)**

Maps game-controller inputs (Switch Pro, Xbox, DualSense, or any SDL pad) to Herdr socket commands — switching workspaces, tabs, and panes, scrolling, and triggering voice mode without touching the keyboard. Works locally or with the controller on one machine and Herdr on another over SSH, dispatching every action through the socket so no OS-level input injection is needed. For developers who want hands-free navigation from a couch, a standing desk, or a headless remote box.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[rjyo/herdr-window-title-sync](https://github.com/rjyo/herdr-window-title-sync)**

A plugin that writes the focused workspace, tab, and agent name to the outer terminal window or tab title, pulling from pane metadata, agent status, or the most recent user prompt in local Codex/Claude Code session files as a fallback. Especially handy in terminals like Moshi that show session titles for quick reconnect. For Herdr users juggling many sessions who want at-a-glance context in their terminal chrome.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[krystof018/herdr-git-status](https://github.com/krystof018/herdr-git-status)**

Surfaces CI/CD status inside Herdr two ways: a background poller prefixes each space's sidebar label with a colored dot and open MR/PR number, and an on-demand pane shows the latest run, recent failures, and clickable OSC 8 links — auto-detecting GitLab vs GitHub from each repo's `origin`. Review-state glyphs flag approved, changes-requested, and conflict states in the label itself. For developers who want fleet-wide CI awareness without leaving Herdr.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[sohanemon/herdr-helpr](https://github.com/sohanemon/herdr-helpr)**

Adds keyboard-driven overlays for tasks Herdr doesn't expose by default: name a new workspace before it opens, rename the current one in place, and close every tab or pane except the focused one. Bindable as plugin actions in `config.toml` and installable from the marketplace. For Herdr users who manage many workspaces and want naming and cleanup without the mouse or a long command.

![PowerShell](https://img.shields.io/badge/-555555?logo=powershell&logoColor=white&style=flat-square) **[fkiene/llmtrim-herdr](https://github.com/fkiene/llmtrim-herdr)**

Wires the llmtrim token-compression proxy into every Herdr pane on `workspace.created`, then pushes a compact savings badge into each pane's sidebar segment and exposes llmtrim's live TUI dashboard as a split. It reads llmtrim's own session data without extra API calls, and a routing check warns once if the proxy environment wasn't inherited. For users already running llmtrim who want token savings surfaced inside Herdr.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[Davidcreador/herdr-token-dashboard](https://github.com/Davidcreador/herdr-token-dashboard)**

A Bubble Tea dashboard that reads Pi session JSONL and the OpenCode server API to track live token spend, session cost, model, message count, and per-tool breakdowns across all active panes, refreshing every few seconds; when an agent goes done it fires a native Herdr toast with the cost and token summary. It falls back to disk-stored message files for completed OpenCode sessions. For Pi or OpenCode users who want spend visibility and finish alerts without leaving the workspace.

![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square) **[wyattjoh/herdr-plugin-renamer](https://github.com/wyattjoh/herdr-plugin-renamer)**

Automatically renames a numbered Herdr tab — and, when it's an auto-generated linked worktree, the git branch and workspace too — to a short slug derived from the agent's first prompt, computed on-device via Apple FoundationModels or Codex. For anyone running many numbered tabs who wants them to self-label instead of staying "1", "2", "3".

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[ynny-github/herdr-event-hook](https://github.com/ynny-github/herdr-event-hook)**

A Herdr plugin that reads a committed `.herdr-event-hook.toml` and runs commands — e.g. `docker compose up -d` and `down` — on the `worktree.created` and `worktree.removed` events, so a new worktree's service stack starts automatically and tears down when the worktree is removed. For developers whose per-worktree dev environment needs a database or other background service.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[mkdir700/herdr-config](https://github.com/mkdir700/herdr-config)**

A portable Herdr config pack: a `config.toml` with worktree settings and a full LazyVim-aligned keybinding remap, bundled with four small local plugins (diff review, copy-workspace-path, a lazygit tab, and a PR-status dot). For Vim users who want their Herdr bindings and layout to feel like their editor.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[alexjsp/herdr-scrollback-capture](https://github.com/alexjsp/herdr-scrollback-capture)**

Captures the focused pane's scrollback via `herdr pane read` and writes it to disk as a self-contained colored HTML file or plain text, with output directory, filename, and theme configurable. For anyone who wants to save an agent session transcript to share or archive.

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[akhillb/herdr-attention](https://github.com/akhillb/herdr-attention)**

Docks a pane that counts down to your next calendar meeting and highlights when it's ten minutes away, pulling data through gcalcli and coloring itself to match your Herdr theme. For developers who want meeting awareness without leaving the terminal session.

![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square) **[ppggff/herdr-plugin](https://github.com/ppggff/herdr-plugin)**

Remembers which macOS input source (e.g. English vs. Pinyin) was active in each Herdr pane and restores it automatically when focus returns, via a bundled Swift helper or the `macism` backend. For anyone who switches languages or input methods across different agent panes and is tired of fixing it by hand.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[astkaasa/herdr-tokscale-dashboard](https://github.com/astkaasa/herdr-tokscale-dashboard)**

Wires the Tokscale token/cost dashboard into Herdr as a split pane and a JSON-emitting quick action, without bundling or reimplementing Tokscale itself. For developers who already track spend with Tokscale and want it one keypress away.

![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square) **[aiki-sh/aiki-integration-herdr](https://github.com/aiki-sh/aiki-integration-herdr)**

Opens a live-refreshing sidebar pane listing your in-flight aiki epics inside Herdr, and its install step bootstraps the companion aiki session-identity hook. For teams already using the aiki task tracker who want epic status visible alongside their agent panes.

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

![JavaScript](https://img.shields.io/badge/-555555?logo=javascript&logoColor=white&style=flat-square) **[alecuba16/herdr-webui](https://github.com/alecuba16/herdr-webui)**

A standalone browser UI that connects to a running Herdr backend over its JSON API and terminal-attach sockets, exposing workspace and worktree navigation, agent status, and live terminal interaction from any browser. Ships with macOS and Linux service helpers (install/start/stop/restart) for persistent background use. For developers who want a browser window into their Herdr session alongside the native terminal.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[dcolinmorgan/herdr-remote](https://github.com/dcolinmorgan/herdr-remote)**

A remote monitoring suite — a mobile-friendly web app (installable as a PWA, with Apple Watch notifications), a macOS menu-bar app, and a Telegram bot — that lets you watch live agent status and approve a blocked agent from your phone with one tap, routed through a zero-config Cloudflare tunnel so no SSH to the agent machine is required. The mobile UI shows a per-agent terminal view and yes/no/trust buttons, and auto-detects agent type for matching icons. Pairs with the herdr-push plugin that feeds it events. For developers who want to approve agents from a phone or watch.

![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square) **[zackbart/herdr-ios](https://github.com/zackbart/herdr-ios)**

A native SwiftUI iOS app (TestFlight beta) that connects directly to a remote Herdr instance over SSH — speaking Herdr's JSON-RPC over an SSH exec channel — so live event subscriptions work from your phone with no relay or server-side component beyond SSH access. Covers workspaces, ANSI-stripped live scrollback, and a text input bar with quick-key extras; host keys are remembered on first connect. For iOS users who want a native phone client to browse workspaces and drive agents over an existing SSH connection.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[aviz85/herdr-controller](https://github.com/aviz85/herdr-controller)**

A Next.js dashboard in front of a running Herdr instance — live agent grid over SSE, terminal mirror, message box, and agent spawn — plus a first-person 3D office mode where each agent is a character at a desk with working/idle/blocked/done animations and a speech bubble of its last message (shoot a character three times to close its pane). The server talks to Herdr only through the CLI, so it runs on the same machine with no extra backend. For developers who want a visual web dashboard to supervise their fleet.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[timvdhoorn/stream-deck-herdr-plugin](https://github.com/timvdhoorn/stream-deck-herdr-plugin)**

An Elgato Stream Deck plugin that assigns one physical key per agent, encoding status as color and glyph (orange working, red blocked, green done, grey idle) so you read your fleet at a glance. Pressing a key runs `herdr agent focus` and raises the terminal; a morphing pager key cycles through agents that need attention. Tested on the 6-key Mini. For Stream Deck users who want hardware-backed ambient awareness and one-press pane focus.

![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square) **[zhongpei/herdr-ulanzi-deck](https://github.com/zhongpei/herdr-ulanzi-deck)**

Pushes live agent status to the LCD keys of a Ulanzi D200X macro keypad, with brand-color-coded per-agent displays, priority sorting (blocked first), and support for multiple Herdr instances on different machines over SSH. A three-process design separates state polling from display rendering so the keypad only redraws on actual state changes. For developers with a Ulanzi D200X who want a physical status panel for a multi-machine fleet.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[jgwesterlund/agent-view](https://github.com/jgwesterlund/agent-view)**

A cyberpunk pixel-art macOS app (built on Electrobun) where each running agent is a character in a neon shared office — working agents type at a holo-desk, blocked ones raise a hand, idle ones drift to the couch, and a cat named Daemon walks over to a blocked agent's desk if you ignore it. Double-clicking a character focuses its pane; the window is a frameless always-on-top widget. For Herdr users who want ambient agent awareness as a living scene rather than a status list.

![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square) **[AltanS/collie](https://github.com/AltanS/collie)**

A Herdr plugin plus Bun/TypeScript bridge that serves a PWA over your Tailscale network, so you can check which agent needs you and reply from your phone's own keyboard instead of SSHing in and wrestling a TUI. It mirrors each pane in color and adds a slash-command palette and a special-keys pad. Built for a single operator on one tailnet — served privately, never the public internet.

---

## Work in progress

Announced or scaffolded, but not yet usable — listed so submitters know they exist, without endorsing them as ready.

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
