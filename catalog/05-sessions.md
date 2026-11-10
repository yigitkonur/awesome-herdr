# Awesome Herdr: Switch and restore sessions

The full list for domain 5 of [Awesome Herdr](../README.md#5-switch-and-restore-sessions), ordered by GitHub stars.

- [Fuzzy jump pickers for workspaces, tabs and agents (16)](#fuzzy-jump-pickers-for-workspaces-tabs-and-agents)
- [Tree and preview navigators for workspaces and panes (10)](#tree-and-preview-navigators-for-workspaces-and-panes)
- [Agent pickers ranked by status and recency (16)](#agent-pickers-ranked-by-status-and-recency)
- [Jump to the next blocked or finished agent (13)](#jump-to-the-next-blocked-or-finished-agent)
- [Last-tab and last-workspace toggles (11)](#last-tab-and-last-workspace-toggles)
- [Focus history, back and forward jumps and recent-pane cyclers (14)](#focus-history-back-and-forward-jumps-and-recent-pane-cyclers)
- [Claude Code session finders and resume pickers (4)](#claude-code-session-finders-and-resume-pickers)
- [Multi-agent conversation search and resume pickers (12)](#multi-agent-conversation-search-and-resume-pickers)
- [Project folder finders that open or focus a workspace (13)](#project-folder-finders-that-open-or-focus-a-workspace)
- [Zoxide directory workspace pickers (7)](#zoxide-directory-workspace-pickers)
- [Git repository and worktree pickers (9)](#git-repository-and-worktree-pickers)
- [Saved project lists and bookmarked directories (4)](#saved-project-lists-and-bookmarked-directories)
- [Directory pickers for new workspaces and tabs (6)](#directory-pickers-for-new-workspaces-and-tabs)
- [Sessionizer-style project launchers with tab templates (5)](#sessionizer-style-project-launchers-with-tab-templates)
- [Shell and tab shortcuts that start or reuse panes (4)](#shell-and-tab-shortcuts-that-start-or-reuse-panes)
- [SSH host, cloud instance and remote machine pickers (14)](#ssh-host-cloud-instance-and-remote-machine-pickers)
- [Named Herdr session managers (6)](#named-herdr-session-managers)
- [Session managers shared across Herdr, tmux, sesh and Zellij (6)](#session-managers-shared-across-herdr-tmux-sesh-and-zellij)
- [Multi-server sidebars that mirror remote Herdr machines (9)](#multi-server-sidebars-that-mirror-remote-herdr-machines)
- [Workspace groups, profiles and focus filters (9)](#workspace-groups-profiles-and-focus-filters)
- [Workspace sorters by name, recent use or category (9)](#workspace-sorters-by-name-recent-use-or-category)
- [Move panes and tabs between workspaces (14)](#move-panes-and-tabs-between-workspaces)
- [Session labels, notes and context locators (7)](#session-labels-notes-and-context-locators)
- [Declarative workspace layouts in YAML, TOML and Lua (12)](#declarative-workspace-layouts-in-yaml-toml-and-lua)
- [tmuxinator-style project launchers (8)](#tmuxinator-style-project-launchers)
- [Saved layout snapshots and screen grids (4)](#saved-layout-snapshots-and-screen-grids)
- [Full workspace save and restore after restart (10)](#full-workspace-save-and-restore-after-restart)
- [Pane command relaunchers after restart (7)](#pane-command-relaunchers-after-restart)
- [Agent auto-resume after a server restart (14)](#agent-auto-resume-after-a-server-restart)
- [Idle agent parking and hibernation (15)](#idle-agent-parking-and-hibernation)
- [Stale and idle agent cleanup (5)](#stale-and-idle-agent-cleanup)
- [Workspace stash, suspend and archive (9)](#workspace-stash-suspend-and-archive)
- [Undo close and reopen closed panes (6)](#undo-close-and-reopen-closed-panes)
- [Fork Claude Code, Codex and OpenCode conversations into a new pane (11)](#fork-claude-code-codex-and-opencode-conversations-into-a-new-pane)
- [Pi side conversations and session forks (8)](#pi-side-conversations-and-session-forks)
- [Moving sessions and workspaces to another machine or app (5)](#moving-sessions-and-workspaces-to-another-machine-or-app)
- [Crash-proof and always-on sessions (6)](#crash-proof-and-always-on-sessions)

---

## 5. Switch and restore sessions

*338 projects. Fuzzy switchers, state managers, and layout restoration tools for organizing agent workspaces.*

### Fuzzy jump pickers for workspaces, tabs and agents

*16 projects. General-purpose fuzzy pickers that list workspaces, tabs, panes, and agents in one popup and jump to the one you choose.*

| Project | Stars | What it does |
|---|--:|---|
| [**jeffarese/herdr-bar**](https://github.com/jeffarese/herdr-bar) | 214 | A dependency-free Python command palette for jumping to any Herdr tab, agent, repository, or branch. |
| [**thanhdat77/herdr-navigator**](https://github.com/thanhdat77/herdr-navigator) | 188 | Searches and switches between active Herdr sessions and workspaces using an interactive fuzzy picker. |
| [**haphamdev/herdr-simple-switcher**](https://github.com/haphamdev/herdr-simple-switcher) | 3 | Fuzzy-searches Herdr TUI workspaces, tabs, and agents and opens projects as workspaces. |
| [**purehate/herdr-plugin-picker**](https://github.com/purehate/herdr-plugin-picker) | 3 | Finds Herdr TUI spaces, agents, tabs, and panes in a popup, broadcasts to marked panes, and connects to SSH hosts. |
| [**jackfrancisdalton/herdr-turbo-palette**](https://github.com/jackfrancisdalton/herdr-turbo-palette) | 1 | Fuzzy-finds Herdr spaces, tabs, agents, or panes and jumps directly to the selected target. |
| [**black-atom-industries/helm.herdr**](https://github.com/black-atom-industries/helm.herdr) | 1 | Jumps to any Herdr workspace, agent, project, session, remote, directory, or action from one fuzzy navigator. |
| [**agustinvalencia/herdr-jump**](https://github.com/agustinvalencia/herdr-jump) | 1 | Opens separate overlay pickers for Herdr TUI spaces and agents with live status colors. |
| [**shippy/raycast-herdr · extensions/herdr**](https://github.com/shippy/raycast-herdr/tree/main/extensions/herdr) | 1 | Controls Herdr TUI workspaces from Raycast and launches Claude prompts or configured actions. |
| [**kodama24ek/herdr-picker**](https://github.com/kodama24ek/herdr-picker) | 0 | Adds an fzf session picker for herdr, as fish functions. |
| [**solidsnakedev/herdr-jump**](https://github.com/solidsnakedev/herdr-jump) | 0 | Opens fuzzy pickers for Herdr TUI workspaces, tabs, panes, and projects, with a last-workspace toggle. |
| [**lancodev/herdr-jump**](https://github.com/lancodev/herdr-jump) | 0 | Switches between Herdr workspaces and agents through a two-pane fuzzy picker with Vim keys. |
| [**KazBrekker1/herdr-hasr**](https://github.com/KazBrekker1/herdr-hasr) | 0 | Switches, creates, renames, and deletes Herdr TUI agents, tabs, and spaces from a popup picker with live status tracking. |
| [**tp6gw94/herdr-jump**](https://github.com/tp6gw94/herdr-jump) | 0 | Opens keyboard-driven pickers to focus a Herdr TUI workspace, tab, pane, or agent. |
| [**trebsoj/herdr-fzf-tab-switcher**](https://github.com/trebsoj/herdr-fzf-tab-switcher) | 0 | Opens an fzf picker in a popup listing every Herdr tab as space > tab and focuses the one you select. |
| [**Tranceh2/shep**](https://github.com/Tranceh2/shep) | 0 | Jumps to any Herdr TUI workspace, project, or folder from one fuzzy picker with blocked agents first and a preview of git state, files, and panes. Renames or closes items and opens new worktrees from the same popup. |
| [**kfujii-6jo/raycast-extensions**](https://github.com/kfujii-6jo/raycast-extensions) | 0 | Finds and focuses Herdr TUI workspaces and agents or opens local Git repositories from Raycast. |

### Tree and preview navigators for workspaces and panes

*10 projects. Popup navigators that show workspaces, tabs, and panes as a tree or live overview beside a preview of the selected pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**mr04vv/herdr-pane-navigator**](https://github.com/mr04vv/herdr-pane-navigator) | 5 | A fuzzy tree for workspaces, tabs, and panes, sorted by agent urgency. Its preview shows directory, status, and recent scrollback so blocked or completed work can be triaged quickly. |
| [**yoshiori/herdr-configurable-picker**](https://github.com/yoshiori/herdr-configurable-picker) | 5 | Opens a tree-style Herdr TUI navigator with configurable keys and input-method-friendly shortcuts. |
| [**javoscript/herdr-pickr**](https://github.com/javoscript/herdr-pickr) | 5 | Finds Herdr TUI tabs, spaces, agents, and panes with fuzzy pickers and terminal previews. |
| [**caneppelevitor/herdr-tmux-session-navigator**](https://github.com/caneppelevitor/herdr-tmux-session-navigator) | 4 | Navigates Herdr TUI workspaces and tabs through a tmux-style tree with live pane previews. |
| [**bkarpinos/herdr-picker**](https://github.com/bkarpinos/herdr-picker) | 2 | Adds a fast popup picker for searching and previewing workspaces, agents, and tabs in herdr. |
| [**iamgp/herdr-overview**](https://github.com/iamgp/herdr-overview) | 1 | Shows a live tiled overview of Herdr TUI workspaces and their focused panes. |
| [**wrn14897/herdr-plugins · herdr-picker**](https://github.com/wrn14897/herdr-plugins/tree/main/herdr-picker) | 1 | Searches Herdr TUI workspaces, screens, and agent conversations in a fuzzy picker with live preview. |
| [**EkeMinusYou/herdr-launcher**](https://github.com/EkeMinusYou/herdr-launcher) | 1 | Launches frequent commands and jumps between panes and spaces from a searchable picker with live terminal previews. Ships a Go picker for Herdr TUI and a native Launcher mod for the Herdr app. |
| [**MykolaSuprun/herdr-vimnav**](https://github.com/MykolaSuprun/herdr-vimnav) | 1 | Switches spaces and agents from a master-detail picker with live pane previews in Herdr TUI. Supports filtering, jump codes, and sidebar badges. |
| [**ryutaro-asada/herdr-nav-with-preview**](https://github.com/ryutaro-asada/herdr-nav-with-preview) | 0 | Opens a full-screen popup with a workspace, tab, and pane tree beside a live preview of the selected pane. Jumps to the pane on Enter, like tmux Ctrl+b w. |

### Agent pickers ranked by status and recency

*16 projects. Switchers that list only coding agents, ordered by urgency, recency or last message, and focus the one you pick, unlike pickers of general focus history.*

| Project | Stars | What it does |
|---|--:|---|
| [**douglascorrea/herdr-agent-inbox**](https://github.com/douglascorrea/herdr-agent-inbox) | 11 | Shows Herdr TUI agent session titles, runtimes, workspace statistics, and unread state in a central inbox. |
| [**dartyuhov/herdr-blink**](https://github.com/dartyuhov/herdr-blink) | 9 | Opens a fuzzy Herdr TUI agent picker that prioritizes agents needing attention and sorts the rest by recent use. |
| [**umutciloglu/herdr-session-manager**](https://github.com/umutciloglu/herdr-session-manager) | 5 | Browses agent sessions and supports agent-to-agent chat across Claude Code and Codex in Herdr TUI. |
| [**emanuel2718/herdscope**](https://github.com/emanuel2718/herdscope) | 3 | Finds Herdr TUI agents, terminals and commands with status ranking and live pane previews. |
| [**ugurtarlig/herdr-agent-recency**](https://github.com/ugurtarlig/herdr-agent-recency) | 3 | Ranks agents and workspaces by the time of their latest real Claude or Codex turn, bringing the most recently finished or stalled sessions to the top. |
| [**ofelcan164/muster**](https://github.com/ofelcan164/muster) | 3 | Shows agents across Herdr TUI workspaces and jumps to the selected agent or orchestrator. |
| [**mrpbennett/qs-herdr-agents**](https://github.com/mrpbennett/qs-herdr-agents) | 2 | Displays Herdr agent panels inside the Omarchy quick-switch menu. |
| [**leonho/herdr-agent-inbox**](https://github.com/leonho/herdr-agent-inbox) | 2 | Shows a popup inbox of all agents and their latest recap. Pressing Enter jumps directly to the selected agent's pane. |
| [**yxhta/herdr-agents-picker**](https://github.com/yxhta/herdr-agents-picker) | 1 | Searches active Herdr TUI agent panes in a popup with live previews and focuses the selected pane. |
| [**dleen/herdr-agents**](https://github.com/dleen/herdr-agents) | 1 | Lists all active panes and puts blocked agents first. It shows live previews, jumps to existing workers, and can start new agents with one key. |
| [**2ykwang/herdr-finder**](https://github.com/2ykwang/herdr-finder) | 0 | Finds running Herdr agents and terminals by name or visible output, previews the selected screen, and jumps to the session. |
| [**bleedingfight/herdr-agent-manager**](https://github.com/bleedingfight/herdr-agent-manager) | 0 | Finds Herdr agents and workspaces with fzf and lets users focus or message agents. |
| [**Benny93/herdr-quick-bar**](https://github.com/Benny93/herdr-quick-bar) | 0 | Opens an fzf popup over all running agent sessions and jumps to the selected pane. |
| [**cgardner/herdr-switcher-plus**](https://github.com/cgardner/herdr-switcher-plus) | 0 | Lists every coding agent in Herdr TUI with five orderings, filters as you type, and jumps to the pane you pick. Sorts by each session's last real message by default. |
| [**julianbonomini/herdr-agent-nav**](https://github.com/julianbonomini/herdr-agent-nav) | 0 | Adds an active-agent picker that groups agents by space and jumps to the exact pane, plus a prompt to rename the focused agent. For Herdr TUI 0.9 and newer. |
| [**newro/herdr-agent-nav**](https://github.com/newro/herdr-agent-nav) | 0 | Numbers agent sidebar entries and switches between agents relative to the last focused agent. |

### Jump to the next blocked or finished agent

*13 projects. One-key commands that jump straight to the agent that most needs attention, such as blocked, waiting or just-finished panes, rather than listing or marking them.*

| Project | Stars | What it does |
|---|--:|---|
| [**milkyskies/herdr-attention**](https://github.com/milkyskies/herdr-attention) | 6 | Moves focus to the next agent needing attention with one key, checking blocked agents before completed ones. |
| [**martin-ro/herdr-next-agent**](https://github.com/martin-ro/herdr-next-agent) | 4 | Jumps to the next agent needing attention, ranked by a configurable status priority. |
| [**to4iki/herdr-unread-jump**](https://github.com/to4iki/herdr-unread-jump) | 3 | Jumps to the next Herdr pane needing attention, prioritizing blocked agents before cycling through completed tasks. |
| [**peterwiebe/herdr-plugin-agent-attention**](https://github.com/peterwiebe/herdr-plugin-agent-attention) | 2 | Jumps to the most recent blocked or finished agent. |
| [**choplin/herdr-next-agent**](https://github.com/choplin/herdr-next-agent) | 2 | Moves between Herdr agents in configured semantic states. |
| [**kuwa72/herdr-focus-attention**](https://github.com/kuwa72/herdr-focus-attention) | 1 | Cycles through Herdr TUI agents needing attention, ranked by status and recent state change. |
| [**raghu-nandan-bs/herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation) | 1 | Opens a workspace and pane navigator for Herdr TUI that walks an attention queue of blocked agents first, then agents that finished unseen. |
| [**shadowfax92/herdr-beacon**](https://github.com/shadowfax92/herdr-beacon) | 1 | Jumps to unread, working, or recently active agents using Herdr TUI status and sidebar indicators. |
| [**okonomi/herdr-agent-queue**](https://github.com/okonomi/herdr-agent-queue) | 0 | Cycles through stopped or waiting Herdr agents with one key, starting with the agent that has been waiting longest. |
| [**trapple/herdr-focus**](https://github.com/trapple/herdr-focus) | 0 | Focuses the next blocked or completed agent pane and brings the terminal window to the front. |
| [**oyuk/herdr_plugin**](https://github.com/oyuk/herdr_plugin) | 0 | Jumps to Herdr TUI agents matching a selected status. |
| [**calorie/herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus) | 0 | Focuses the Herdr agent needing attention after the computer has been idle. |
| [**shoaibkhanz/herdr-active-agent-jump**](https://github.com/shoaibkhanz/herdr-active-agent-jump) | 0 | Cycles focus through working or blocked Herdr agents in layout order, skipping idle and finished panes. |

### Last-tab and last-workspace toggles

*11 projects. One-key toggles between exactly two places, the previously focused tab or workspace, like tmux last-window, often with separate history per workspace.*

| Project | Stars | What it does |
|---|--:|---|
| [**third774/herdr-last-workspace**](https://github.com/third774/herdr-last-workspace) | 20 | Tracks workspace IDs and toggles between the current and previous workspace with one key. It remains correct after reordering and exits quietly if the earlier workspace was closed. |
| [**lmilojevicc/herdr-last**](https://github.com/lmilojevicc/herdr-last) | 10 | Toggles between the current and previously active Herdr TUI workspace or tab. |
| [**joo-was-already-taken/herdr-prevtab**](https://github.com/joo-was-already-taken/herdr-prevtab) | 2 | Toggles back to the previously focused Herdr TUI tab or workspace. |
| [**m4salah/herdr-plugin-last**](https://github.com/m4salah/herdr-plugin-last) | 2 | Adds tmux-style shortcuts for returning to the previous Herdr tab or workspace. |
| [**dantehemerson/herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab) | 1 | Tracks tab focus history and returns to the previously active Herdr tab with one keystroke. |
| [**tim-kuntz/workspace-tools**](https://github.com/tim-kuntz/workspace-tools) | 0 | Opens a Herdr TUI workspace picker and toggles between the last two focused workspaces. |
| [**akpw/herdr-last-workspace**](https://github.com/akpw/herdr-last-workspace) | 0 | Toggles between the current and previous workspace like tmux, restoring each workspace's last active tab. Uses only the Python standard library. |
| [**k-narusawa/herdr-last-tab**](https://github.com/k-narusawa/herdr-last-tab) | 0 | Jumps back to the previously focused Herdr TUI tab across workspaces, like tmux last-window. Needs jq. |
| [**PascalKraupner/herdr-lasttab**](https://github.com/PascalKraupner/herdr-lasttab) | 0 | Adds tmux-style last-tab and last-workspace toggles to the Herdr TUI, keeping separate state per workspace. |
| [**QuantumDancer/herdr-last-tab**](https://github.com/QuantumDancer/herdr-last-tab) | 0 | Switches back to the previously focused Herdr tab. |
| [**bertverbessem/herdr-last-tab**](https://github.com/bertverbessem/herdr-last-tab) | 0 | Toggles between the current and previously focused Herdr TUI tab, keeping history separate per workspace. |

### Focus history, back and forward jumps and recent-pane cyclers

*14 projects. Tools with a longer memory than a two-way toggle: browser-style back and forward, most-recently-used cycling and history lists across panes, tabs and workspaces.*

| Project | Stars | What it does |
|---|--:|---|
| [**beyondlex/herdr-recent-navigator**](https://github.com/beyondlex/herdr-recent-navigator) | 26 | A Rust popup that tracks recently focused workspaces, tabs, panes, and agents through socket events. It provides a live most-recently-used index, keyboard navigation, and fuzzy search. |
| [**AlexanderGrooff/herdr-pane-switcher**](https://github.com/AlexanderGrooff/herdr-pane-switcher) | 3 | Cycles through recently focused Herdr TUI panes or jumps to the agent pane needing attention. |
| [**ismaelosuna7824/herdr-recent-workspaces**](https://github.com/ismaelosuna7824/herdr-recent-workspaces) | 2 | Keeps searchable history of workspace directories, refocuses active workspaces, restores older locations, and includes a filesystem browser for creating new workspaces. |
| [**KadenThomp36/herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher) | 1 | Cycles through recently used Herdr TUI panes with Ctrl-Tab on macOS. |
| [**killallgit/herdr-alt-tab**](https://github.com/killallgit/herdr-alt-tab) | 1 | Cycles through Herdr TUI panes in most-recently-used order with alt+tab and shift+alt+tab. Installs a prebuilt binary and has no options. |
| [**jugyo/herdr-nav-history**](https://github.com/jugyo/herdr-nav-history) | 1 | Adds browser-style back and forward navigation across panes, tabs, and workspaces by recording focus changes from the Herdr socket event stream. |
| [**pedrobarco/herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus) | 1 | Toggles between recently focused Herdr TUI panes, tabs, or workspaces using focus-event history. |
| [**sushidesu/herdr-tabpick**](https://github.com/sushidesu/herdr-tabpick) | 0 | Lists every tab across all workspaces, most recently used first, in an fzf picker with a live pane preview. Tabs with several panes open into a pane tree. |
| [**followbl/herdr-drover**](https://github.com/followbl/herdr-drover) | 0 | Cycles recent Herdr TUI tabs with a Super+T hold-and-release shortcut and offers fuzzy search and new-tab creation. |
| [**iskwyuki/herdr-control-panel**](https://github.com/iskwyuki/herdr-control-panel) | 0 | Opens an fzf panel for switching through workspace history, opening paths, and running custom actions in Herdr TUI. |
| [**tdi/herdr-recents**](https://github.com/tdi/herdr-recents) | 0 | Keeps a history of Herdr TUI workspaces and worktrees and focuses or recreates a selected entry. |
| [**FjedorGaede/herdr-focus-history**](https://github.com/FjedorGaede/herdr-focus-history) | 0 | Adds a Vim-style back and forward jumplist over workspace and agent focus history in the Herdr TUI. The author flags it as early and tested on Linux with herdr 0.9.1. |
| [**neilellis/herdr-pane-history**](https://github.com/neilellis/herdr-pane-history) | 0 | Adds browser-style back and forward through recently focused panes in Herdr TUI, across tabs and workspaces, with a history list. |
| [**riogesulgon/herdr-history**](https://github.com/riogesulgon/herdr-history) | 0 | Opens a popup that lists panes from every workspace, most recently focused first, with a live preview, and jumps to the one you pick. Works like back history for Herdr TUI panes. |

### Claude Code session finders and resume pickers

*4 projects. Pickers that list earlier Claude Code sessions across projects and resume the chosen conversation in a new Herdr tab or pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**Joxtacy/herdr-plugin-vault**](https://github.com/Joxtacy/herdr-plugin-vault) | 1 | Browses earlier Claude Code sessions in a Herdr popup and resumes the selected conversation in a new tab. |
| [**kakigakki/lazy-claude-herdr**](https://github.com/kakigakki/lazy-claude-herdr) | 0 | Lists recent Claude Code sessions from every Herdr space in one fzf popup and resumes the chosen one where it started, focusing its live pane or splitting a pane in the matching space to run `claude -r`. A per-session menu forks the session, opens its PR or copies a review request, reads the transcript, or runs actions defined in TOML. |
| [**Duzc01/herdr-session-finder**](https://github.com/Duzc01/herdr-session-finder) | 0 | Searches Claude Code sessions across all projects and resumes the selected conversation through a Herdr plugin. |
| [**AIToolSharing/anyresume**](https://github.com/AIToolSharing/anyresume) | 0 | Lists every Claude Code session in one picker and resumes the chosen one in its original folder, in any terminal or as a Herdr TUI plugin. |

### Multi-agent conversation search and resume pickers

*12 projects. Searchable archives of earlier conversations and live pane output from Claude Code, Codex, OpenCode, Pi, and other agents that resume the match in Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**nicosuave/memex**](https://github.com/nicosuave/memex) | 312 | Indexes conversations from Claude Code, Codex, Pi, OpenCode, and Cursor with hybrid search. A Herdr TUI searches the archive and can resume a selected interaction in a fresh tab. |
| [**taxueseek/session-digger**](https://github.com/taxueseek/session-digger) | 34 | Indexes conversations from Claude Code, Codex, and other agents in SQLite FTS5. It also tracks token and cache data and creates local HTML reports for review. |
| [**dmnkf/herdr-omnisearch**](https://github.com/dmnkf/herdr-omnisearch) | 12 | Searches live workspace metadata, pane output, and optional archived conversations across the Herdr TUI and app, then jumps to or resumes a match. |
| [**hxreborn/herdr-transcripts**](https://github.com/hxreborn/herdr-transcripts) | 8 | Searches past and live coding-agent sessions by title, prompt, reply, or tool call in an fzf popup, then resumes the pick in a new Herdr tab or focuses its pane when it is already running. Covers Claude Code, Codex, OpenCode, Gemini CLI, Droid, Copilot CLI, Kimi Code, and Qwen Code with a pre-warmed index in standard-library Python. |
| [**nathnael-desta/herdr-project-sessions**](https://github.com/nathnael-desta/herdr-project-sessions) | 1 | Browses Git projects, worktrees, live agent panes, and historical OpenCode sessions in a Herdr TUI overlay on Linux. |
| [**muscaiu/resume-globally**](https://github.com/muscaiu/resume-globally) | 0 | Searches and resumes recent Claude Code, Cursor, OpenCode, Pi, and Hermes sessions in Herdr panes. |
| [**itisvincent/herdr-agent-sessions**](https://github.com/itisvincent/herdr-agent-sessions) | 0 | Lists saved coding-agent sessions in a searchable Herdr panel and resumes the selected session in a new pane. |
| [**adamwangxx/herdr-codex-resume**](https://github.com/adamwangxx/herdr-codex-resume) | 0 | Opens Codex's native resume picker in a new Herdr split, preserving the current view while previous Codex sessions are browsed and resumed. |
| [**damianpoole/herdr-opencode-sessions**](https://github.com/damianpoole/herdr-opencode-sessions) | 0 | Searches earlier OpenCode sessions by project, title, date, or transcript text. Conversation previews and shortcuts make it possible to resume or fork a result into a new Herdr pane. |
| [**tlpinney/herdr-atuin-resume**](https://github.com/tlpinney/herdr-atuin-resume) | 0 | Picks a coding-agent thread captured by Atuin and resumes it in a new Herdr TUI tab. |
| [**AymanZahran/herdr-ai9s**](https://github.com/AymanZahran/herdr-ai9s) | 0 | Opens the ai9s session finder in a Herdr TUI sidebar and starts the selected agent in a new tab of the current workspace. Needs the ai9s program installed. |
| [**GeorgGroenendaal/herdr-content-picker**](https://github.com/GeorgGroenendaal/herdr-content-picker) | 0 | Searches the terminal output of open Herdr TUI agent panes and past Pi and Claude Code sessions, then jumps to the match with a line preview. |

### Project folder finders that open or focus a workspace

*13 projects. Pick these to scan project roots or globs, fuzzy-find a directory and focus or create its Herdr workspace, without zoxide, Git awareness or a saved list as the main idea.*

| Project | Stars | What it does |
|---|--:|---|
| [**dardT/herdr-workspaces-manager**](https://github.com/dardT/herdr-workspaces-manager) | 3 | Finds local projects and opens them in Herdr TUI workspaces, tabs or panes. |
| [**alon-z/herdr-command-palette**](https://github.com/alon-z/herdr-command-palette) | 2 | Opens a fuzzy picker for Herdr TUI workspaces and project directories, focusing an existing workspace or creating one. |
| [**ImArtisann/herdr-workspace-launcher**](https://github.com/ImArtisann/herdr-workspace-launcher) | 2 | Scans configured project roots and creates or focuses Herdr workspaces with one keyboard action. |
| [**42lizard/herdr-sessionizer**](https://github.com/42lizard/herdr-sessionizer) | 1 | Finds open workspaces and project directories in a fuzzy picker, then focuses or creates a Herdr TUI workspace. |
| [**nicolegros/herdr-launcher**](https://github.com/nicolegros/herdr-launcher) | 0 | Searches directories to create or switch Herdr TUI workspaces with a fuzzy picker. |
| [**benbrackenbury/open-project**](https://github.com/benbrackenbury/open-project) | 0 | Fuzzy-finds folders under `~/Projects` and creates or focuses a matching Herdr TUI workspace. |
| [**EskelinenAntti/zipln**](https://github.com/EskelinenAntti/zipln) | 0 | Fuzzy-finds any file or folder and jumps into its Herdr workspace, creating the workspace if needed. |
| [**barnuri/herdr-project-manager**](https://github.com/barnuri/herdr-project-manager) | 0 | Discovers projects by glob or manual entry and opens a selected project in a Herdr TUI tab or workspace. |
| [**josephschmitt/pj-herdr**](https://github.com/josephschmitt/pj-herdr) | 0 | Uses the pj project picker to find a project and create or focus its Herdr TUI workspace. |
| [**PremModhaOfficial/sessionizer**](https://github.com/PremModhaOfficial/sessionizer) | 0 | Picks a project directory and attaches to its existing Herdr TUI workspace or creates one. |
| [**RadeJR/herdr-plugins · project-picker**](https://github.com/RadeJR/herdr-plugins/tree/main/project-picker) | 0 | Opens a fzf popup of directories under ~/projects in Herdr TUI and focuses or creates the matching workspace, with a second picker to switch among open workspaces. |
| [**sudokvn/herdr-project-switcher**](https://github.com/sudokvn/herdr-project-switcher) | 0 | Opens an fzf popup to find a project and focus its workspace, or create one if it does not exist. |
| [**ensi-platform/elc-herdr-plugin**](https://github.com/ensi-platform/elc-herdr-plugin) | 0 | Fuzzy-finds ELC components from the Herdr TUI and opens a shell in the component folder as a new pane, tab, or workspace, with elc start, restart, and stop actions. |

### Zoxide directory workspace pickers

*7 projects. Pick these when zoxide or folder-visit history is the source of candidates, usually merged with open workspaces in one fuzzy list.*

| Project | Stars | What it does |
|---|--:|---|
| [**fullerzz/herdr-plugin-sesh**](https://github.com/fullerzz/herdr-plugin-sesh) | 52 | A sesh-style Herdr workspace picker with zoxide integration for creating workspaces from frequently used directories. |
| [**mcuste/herdr-workspacer**](https://github.com/mcuste/herdr-workspacer) | 3 | Finds open workspaces and zoxide directories in a most-recently-used picker, then focuses or creates a Herdr TUI workspace. |
| [**cyperx84/herdr-sesh-bro**](https://github.com/cyperx84/herdr-sesh-bro) | 2 | Picks Herdr TUI workspaces, agents, and zoxide directories in an fzf popup with live previews. |
| [**adriankarlen/yeet**](https://github.com/adriankarlen/yeet) | 1 | Opens a one-line-per-workspace picker in Herdr TUI that merges active workspaces, config-defined sessions and zoxide directories. Filters with gum or fzf. |
| [**phillipahereza/herdr-ws**](https://github.com/phillipahereza/herdr-ws) | 0 | Opens a floating fuzzy finder in Herdr TUI for jumping between workspaces, tabs, agent panes, and zoxide directories. |
| [**willfish/herdr-workspacex**](https://github.com/willfish/herdr-workspacex) | 0 | Fuzzy-switches Herdr TUI workspaces and creates a workspace from a zoxide directory. |
| [**nicolasvasquez/herdr-smart-workspace**](https://github.com/nicolasvasquez/herdr-smart-workspace) | 0 | Switches existing Herdr TUI workspaces or creates them from zoxide directories using an fzf overlay. |

### Git repository and worktree pickers

*9 projects. Pick these when the candidates are Git repositories, ghq checkouts, branches or worktrees and the pick opens as a workspace.*

| Project | Stars | What it does |
|---|--:|---|
| [**crafts69guy/herdr-switchboard**](https://github.com/crafts69guy/herdr-switchboard) | 7 | Adds a herdr plugin: fuzzy-switch across running agents, open workspaces, and ghq repositories in one Rust TUI, and open a repo in a new workspace, tab, split, or the current pane. |
| [**vieitesss/contx**](https://github.com/vieitesss/contx) | 4 | Finds project directories with Git context and opens them as Herdr TUI workspaces or tmux sessions. |
| [**sagmans/herdr-pickers**](https://github.com/sagmans/herdr-pickers) | 1 | Opens fuzzy Herdr TUI popups for switching projects, workspaces, worktrees, and agents. |
| [**asumaran/asgoto**](https://github.com/asumaran/asgoto) | 1 | Searches repositories, worktrees, and panes in a tree-style Herdr TUI workspace switcher. |
| [**mike-bronner/herdr-plugin-project-finder**](https://github.com/mike-bronner/herdr-plugin-project-finder) | 1 | Fuzzy-finds Git repositories and opens them as Herdr TUI workspaces. |
| [**phin-tech/herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util) | 1 | Opens a project picker in Herdr TUI that jumps to any repo, branch, pull request or issue as a Space and clones repos you do not have yet. Adds saved setups that lay out a whole Space and a command that moves a running Claude session into Herdr. |
| [**princejoogie/herdr-repo-picker**](https://github.com/princejoogie/herdr-repo-picker) | 0 | Opens Git repositories as Herdr workspaces from an OpenTUI picker. |
| [**utahta/herdr-hop**](https://github.com/utahta/herdr-hop) | 0 | Finds repositories, worktrees, and open Herdr TUI workspaces in a popup and can clone repositories or create worktrees. |
| [**mayaton/herdr-repo-picker**](https://github.com/mayaton/herdr-repo-picker) | 0 | Opens a Herdr TUI popup to fuzzy-search ghq repositories and jumps to the matching workspace. |

### Saved project lists and bookmarked directories

*4 projects. Pick these when you keep the project list by hand as waypoints, bookmarks or a registry and open entries as workspaces.*

| Project | Stars | What it does |
|---|--:|---|
| [**wraithyy/herdr-waypoint**](https://github.com/wraithyy/herdr-waypoint) | 2 | Saves frequently used project directories as named waypoints in a small text file and opens them as new Herdr workspaces through fzf. |
| [**mikedclarke/herdr-workspaces**](https://github.com/mikedclarke/herdr-workspaces) | 0 | Registers frequently used project directories and opens them through a fuzzy picker. Existing workspaces are focused instead of duplicated. |
| [**htlcode/herdr-directory-bookmarks**](https://github.com/htlcode/herdr-directory-bookmarks) | 0 | Saves directory bookmarks and opens them as Herdr TUI workspaces from a searchable popup. |
| [**ricardofelixb/herdr-project-picker**](https://github.com/ricardofelixb/herdr-project-picker) | 0 | Opens a searchable project popup in Herdr TUI with one tab per machine and starts the chosen project as a new workspace. |

### Directory pickers for new workspaces and tabs

*6 projects. Pick these when you want the New workspace or New tab action itself to ask for a folder, with path completion, history, an agent or a form.*

| Project | Stars | What it does |
|---|--:|---|
| [**den-tanui/herdr-zoxide**](https://github.com/den-tanui/herdr-zoxide) | 11 | Uses zoxide's directory history when creating Herdr workspaces, tabs, and panes, making recent project paths quick to open. |
| [**jeffarese/herdr-newtab-plus**](https://github.com/jeffarese/herdr-newtab-plus) | 5 | Replaces the normal new-tab action with a directory and project picker that includes autocomplete, recent locations, and an optional agent to start. If the directory is already open, it focuses that workspace instead. |
| [**hamzahraihan/herdr-better-workspace**](https://github.com/hamzahraihan/herdr-better-workspace) | 2 | Opens an interactive folder picker with mouse, keyboard or typed path and creates a Herdr workspace from the chosen directory. |
| [**Hon-Lu/herdr-new-workspace**](https://github.com/Hon-Lu/herdr-new-workspace) | 1 | Opens a new Herdr TUI workspace in any folder picked from a popup with fuzzy path completion or project search. |
| [**bethanyj28/herdr-new-workspace**](https://github.com/bethanyj28/herdr-new-workspace) | 0 | Opens a popup in Herdr TUI to pick a project directory from pinned and open projects, then an agent, before it creates the workspace. |
| [**tedkulp/herdr-kickoff**](https://github.com/tedkulp/herdr-kickoff) | 0 | Opens a popup form in the Herdr TUI that creates a workspace from a zoxide directory, a harness, a branch or worktree, and a title, then starts the harness. |

### Sessionizer-style project launchers with tab templates

*5 projects. Pick these when opening a project should also build its tabs, splits and startup commands from a template, as tmux-sessionizer does.*

| Project | Stars | What it does |
|---|--:|---|
| [**thanhdat77/herdr-picker-plus**](https://github.com/thanhdat77/herdr-picker-plus) | 188 | A Ratatui overlay that combines workspaces, project templates, directories, zoxide history, SSH hosts, agent panes, and plugin integrations. It reuses matching workspaces and can create or focus remote-host workspaces automatically. |
| [**andrewchng/herdr-sessionizer**](https://github.com/andrewchng/herdr-sessionizer) | 53 | A tmux-sessionizer-style launcher for Herdr. Fzf selects projects or worktrees, while TOML defines tabs, splits, startup commands, repository-specific layouts, and preview panels. |
| [**salkhalil/herdr-sessionizer**](https://github.com/salkhalil/herdr-sessionizer) | 5 | Searches open Herdr TUI workspaces and zoxide directories with fzf, then focuses or creates a workspace with template tabs. |
| [**codingfragments/herdr-nav**](https://github.com/codingfragments/herdr-nav) | 0 | Navigates Herdr workspaces and panes with previews and workspace templates. |
| [**favasconcelos/herdr-workspace-template**](https://github.com/favasconcelos/herdr-workspace-template) | 0 | Creates a preconfigured set of tabs automatically in every new Herdr TUI workspace, defined in a tabs.json file. |

### Shell and tab shortcuts that start or reuse panes

*4 projects. Small helpers that run a command by tab name, duplicate a tab, reuse idle panes, or launch Herdr from the shell.*

| Project | Stars | What it does |
|---|--:|---|
| [**scaryrawr/herdr.fish**](https://github.com/scaryrawr/herdr.fish) | 1 | Automatically launches or attaches Herdr TUI from fish based on the current project and synchronizes the terminal window title. |
| [**asermax/herdr-tab-command**](https://github.com/asermax/herdr-tab-command) | 0 | Starts an agent or runs a command in a new tab, based on the name you give the tab. |
| [**bonkey/herdr-dup-tab**](https://github.com/bonkey/herdr-dup-tab) | 0 | Duplicates the focused Herdr TUI pane command and working directory in a new tab. |
| [**chuang861012/nu_herdr_navigate_directory**](https://github.com/chuang861012/nu_herdr_navigate_directory) | 0 | Adds a Nushell directory command that reuses idle Herdr TUI panes when navigating to a directory. |

### SSH host, cloud instance and remote machine pickers

*14 projects. Pickers and registries that save, group and connect to SSH hosts, GitHub Codespaces, exe.dev and other cloud VMs and remote machines from inside Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**jorge07RD/herdr-ssh-manager**](https://github.com/jorge07RD/herdr-ssh-manager) | 5 | Saves SSH connections and opens a selected host in a Herdr TUI pane or new tab from a fuzzy popup. |
| [**maayanyosef/herdr-aws-ssm**](https://github.com/maayanyosef/herdr-aws-ssm) | 4 | Selects a running EC2 instance across AWS profiles and opens `herdr --remote` through AWS SSM. It uses temporary Instance Connect keys and automatic SSH-user detection, so no bastion, public IP, or stored key is required. |
| [**vika2603/herdr-machine-manager**](https://github.com/vika2603/herdr-machine-manager) | 3 | Manages saved SSH machines from a Herdr TUI popup, including connecting, disconnecting, and editing targets. |
| [**webframp/shelley-herdr**](https://github.com/webframp/shelley-herdr) | 2 | Runs Shelley conversations on exe.dev VMs as native Herdr agents, each in a pane with live state, a title from the conversation slug and a resume command. Drives shelley client over SSH and reports state through herdr pane report-agent. |
| [**alexjyong/herdr-codespaces**](https://github.com/alexjyong/herdr-codespaces) | 2 | Lists your GitHub Codespaces in a picker and adds the chosen one as a Herdr machine in the sidebar next to local workspaces. |
| [**ecylmz/herdr-hosts**](https://github.com/ecylmz/herdr-hosts) | 1 | Opens a hierarchical SSH host picker in Herdr TUI that reads folders, notes and connection details from ~/.ssh/config and opens the chosen host in its own tab. |
| [**hrudek/herdr-ssh-config-dash**](https://github.com/hrudek/herdr-ssh-config-dash) | 1 | Lists host aliases from your ~/.ssh/config in Herdr TUI and lets you add, enable, disable, or remove them as Herdr machines. |
| [**yavuzhansarmaz/herdr-vps-local**](https://github.com/yavuzhansarmaz/herdr-vps-local) | 1 | Mirrors repos from a VPS or Raspberry Pi saved machine to your laptop with Mutagen. Lets you edit in a local IDE while agents keep running on the remote machine. |
| [**Weicoz/herdr-machine-groups**](https://github.com/Weicoz/herdr-machine-groups) | 0 | Tags, groups, folds, and sorts saved SSH machines in a TUI popup so the sidebar can focus on one cluster. Avoids repeated SSH reconnects from disabling machines. |
| [**fclebio/herdr-ssh-machines**](https://github.com/fclebio/herdr-ssh-machines) | 0 | Adds and removes SSH machines from inside the Herdr TUI using an fzf picker over the SSH config, with groups and client labels. |
| [**DailybotHQ/herdr-machine-groups**](https://github.com/DailybotHQ/herdr-machine-groups) | 0 | Groups saved SSH machines into named groups and focuses one group at a time in the Herdr sidebar. |
| [**ubuntudroid/herdr-coder-sessions**](https://github.com/ubuntudroid/herdr-coder-sessions) | 0 | Browses running Coder agent sessions and opens each in a Herdr workspace with changes mirrored to a local worktree. |
| [**arturodz/dev**](https://github.com/arturodz/dev) | 0 | Runs persistent coding workspaces on a Tailscale-connected development VM and reconnects to their Herdr TUI sessions over SSH. |
| [**metcalfc/herdr-exe**](https://github.com/metcalfc/herdr-exe) | 0 | Links Herdr TUI workspaces to exe.dev VMs for one-keystroke shells, sidebar VM state, and optional one VM per git worktree. Can lend a VM your Claude subscription and never stops or deletes a VM on its own. |

### Named Herdr session managers

*6 projects. Managers that list, create, attach, rename, stop, and delete named Herdr sessions and workspaces.*

| Project | Stars | What it does |
|---|--:|---|
| [**j0urneyk/herdrctx**](https://github.com/j0urneyk/herdrctx) | 2 | Searches and manages local or SSH-hosted Herdr TUI sessions, including attaching, creating, stopping, and deleting sessions. |
| [**xheisenbugx/herdr-sesh**](https://github.com/xheisenbugx/herdr-sesh) | 1 | Manages Herdr workspaces with a sesh-inspired interface. |
| [**ridho9/switchr**](https://github.com/ridho9/switchr) | 0 | Browses Herdr TUI sessions and their workspace, tab, and pane trees before attaching. |
| [**nicosantux/herdr-hop**](https://github.com/nicosantux/herdr-hop) | 0 | Lists, attaches, creates, and deletes Herdr sessions from fzf popups, and opens project folders as workspaces with a git preview. |
| [**masakirocorp/gardn**](https://github.com/masakirocorp/gardn) | 0 | Manages Herdr workspaces for AI coding agents. |
| [**fjordlars/herdr-session-manager**](https://github.com/fjordlars/herdr-session-manager) | 0 | Lists, creates, opens, renames, stops, and deletes named Herdr TUI sessions from a terminal interface. |

### Session managers shared across Herdr, tmux, sesh and Zellij

*6 projects. Session managers and dashboards that work across Herdr, tmux, sesh, and Zellij from one interface.*

| Project | Stars | What it does |
|---|--:|---|
| [**lmilojevicc/seshagy**](https://github.com/lmilojevicc/seshagy) | 23 | Finds projects and tmux or Herdr TUI sessions in a dashboard and shows coding-agent states before attaching. |
| [**0xyg3n/Daedalus**](https://github.com/0xyg3n/Daedalus) | 7 | Manages existing Herdr TUI sessions alongside native terminals and tmux in a Rust workspace manager. |
| [**dkarter/vellum**](https://github.com/dkarter/vellum) | 2 | Opens a customizable menu for Herdr TUI and other terminal multiplexers, with session and agent pickers. |
| [**fedeya/herdr-sesh**](https://github.com/fedeya/herdr-sesh) | 1 | Opens an fzf picker in Herdr TUI to jump between workspaces and agents or open sesh configs, zoxide, and fd directories, with a last-workspace toggle. |
| [**OneNoted/zeshion**](https://github.com/OneNoted/zeshion) | 1 | Manages sessions and windows across Herdr TUI, tmux, and Zellij through a common CLI. |
| [**vieitesss/nexo**](https://github.com/vieitesss/nexo) | 0 | Jumps between Git projects, tmux or Herdr sessions and the coding agents waiting on you, locally or over SSH. Runs as a CLI and TUI on top of tmux or Herdr. |

### Multi-server sidebars that mirror remote Herdr machines

*9 projects. Sidebars and dashboards that pull workspaces and agents from several local, SSH, or shared Herdr servers into one view.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**nikok6/herdr-mirror**](https://github.com/nikok6/herdr-mirror) | 263 | Mirrors remote Herdr workspaces and agent state into a local sidebar over SSH or Docker. Remote panes can be watched and controlled alongside local ones. |
| [**2lab-ai/herdr-mx**](https://github.com/2lab-ai/herdr-mx) | 11 | Connects multiple local and SSH Herdr TUI servers in one sidebar with a downstream multi-remote client. |
| [**abdallah/session-hub**](https://github.com/abdallah/session-hub) | 4 | Tracks Claude Code sessions across machines and shows their status and inbox in a Herdr TUI sidebar. |
| [**joshuadavidthomas/hrd**](https://github.com/joshuadavidthomas/hrd) | 3 | Combines local and remote Herdr sessions with isolated sandboxes for discovery, inspection, and attachment across machines and containers. |
| [**mjrusso/herdlord**](https://github.com/mjrusso/herdlord) | 1 | Monitors agents across local and remote Herdr TUI sessions and lets users inspect output or attach to a session. |
| [**tlpinney/herdr-remuda**](https://github.com/tlpinney/herdr-remuda) | 1 | Mirrors panes from this machine or any saved SSH machine into one Herdr TUI view that you can watch or drive. Saves named views and surfaces agents that need input. |
| [**deepshape-ai/herdr-hive**](https://github.com/deepshape-ai/herdr-hive) | 1 | Shares selected Herdr TUI sessions with team members through a shared Hive server, with a Bee plugin to join and choose sessions. Members get full control of shared sessions. |
| [**alex-devdone/herdrl**](https://github.com/alex-devdone/herdrl) | 0 | Reconnects remote Herdr TUI sessions after network drops and mirrors remote agents into the local sidebar. |
| [**premeq/paddock**](https://github.com/premeq/paddock) | 0 | Shows every machine, space, agent, and pane of a Herdr TUI fleet on one home screen, with blocked and finished agents on top. Lets you open any pane, create spaces and worktrees, and rename or close them. |

### Workspace groups, profiles and focus filters

*9 projects. Tools that group, color, hide, snooze, or pin sets of workspaces so the sidebar can focus on one project or profile.*

| Project | Stars | What it does |
|---|--:|---|
| [**GiorgiTarsaidze/herdr-profiles**](https://github.com/GiorgiTarsaidze/herdr-profiles) | 12 | Groups Herdr TUI spaces and agents into named profiles and switches between them with a popup chooser. |
| [**mrolafsson/herdr-snooze**](https://github.com/mrolafsson/herdr-snooze) | 3 | Hides Herdr TUI agents or spaces from the Agents panel until a chosen time or event. |
| [**bonkey/herdr-keep-root**](https://github.com/bonkey/herdr-keep-root) | 1 | Keeps a repository's main-checkout workspace open while any of its worktree workspaces is open, so the Spaces panel never flattens a worktree group. |
| [**yojahny55/herdr-space-groups**](https://github.com/yojahny55/herdr-space-groups) | 1 | Groups Herdr TUI spaces under named, colored sidebar headers and opens them from a grouped picker. |
| [**mrvnklm/herdr-space-groups**](https://github.com/mrvnklm/herdr-space-groups) | 0 | Groups spaces in the Herdr TUI sidebar by drag and drop, and shows all agents of a group side by side when you click the header. |
| [**kwanwooi25/herdr-plugin-workspace-groups**](https://github.com/kwanwooi25/herdr-plugin-workspace-groups) | 0 | Groups related workspaces from the keyboard, adds colored group badges to the sidebar, and makes linked worktrees inherit the parent group. |
| [**AmoabaKelvin/herdr-focus**](https://github.com/AmoabaKelvin/herdr-focus) | 0 | Hides every project except the ones you pick in Herdr TUI by parking other panes in a single space, then restores layouts, ratios, and worktrees when you exit. Parked shells and agents keep running. |
| [**igor-gorohovsky/herdr-agent-groups**](https://github.com/igor-gorohovsky/herdr-agent-groups) | 0 | Lets you create named groups such as In Progress or Review and assign Herdr TUI agents to them. Shows the groups in the sidebar Agents panel. |
| [**patraianton/herdr-sidebar**](https://github.com/patraianton/herdr-sidebar) | 0 | Adds categories, colour stars, jump hotkeys, worktree detach, and alerts to the Herdr TUI Spaces sidebar for people running many agents. |

### Workspace sorters by name, recent use or category

*9 projects. Plugins that sort sidebar workspaces by label, recent use, or category, manually or automatically.*

| Project | Stars | What it does |
|---|--:|---|
| [**cesmunoz/herdr-workspace-organizer**](https://github.com/cesmunoz/herdr-workspace-organizer) | 4 | Reorders Herdr TUI workspaces manually or previews a suggested order based on configurable categories. |
| [**tntpgh/herdr-control**](https://github.com/tntpgh/herdr-control) | 1 | Routes agents to project workspaces and sorts, colors, and names Herdr tabs by task and branch state. |
| [**Yggdrasill501/border-collie**](https://github.com/Yggdrasill501/border-collie) | 1 | Sorts Herdr TUI spaces by recent use, pins favorite spaces, adds an agent picker, and names tabs and agents after their work. |
| [**MrBogomips/herdr-tools**](https://github.com/MrBogomips/herdr-tools) | 1 | Sorts the spaces sidebar into top, default and bottom groups, gives every space of one customer the same colour (Space Herder), and names tabs after their folder, repo or branch (auto-tab-name). Also ships herdr-jump, a macOS menu bar picker that lists the agents waiting for you, blocked first and oldest wait first. |
| [**ZingerLittleBee/herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins) | 1 | Pins selected Herdr agent sessions to the top of the sidebar and restores their order across server restarts. |
| [**p47t/herdr-sort-workspaces**](https://github.com/p47t/herdr-sort-workspaces) | 0 | Sorts and organizes Herdr TUI workspaces through a terminal interface. |
| [**dorzey/herdr-sort-spaces-plugin**](https://github.com/dorzey/herdr-sort-spaces-plugin) | 0 | Sorts Herdr TUI workspaces alphabetically by label from the workspace context menu, or automatically whenever a workspace is created or renamed. |
| [**collinpeters/herdr-spaces-order**](https://github.com/collinpeters/herdr-spaces-order) | 0 | Reorders Herdr TUI workspaces to match the Spaces worktree hierarchy, so the Agents panel and workspace numbers follow the sidebar. |
| [**mike-bronner/herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces) | 0 | Keeps the spaces sidebar in most-recently-used order. |

### Move panes and tabs between workspaces

*14 projects. Pickers that move live panes and tabs to another workspace without stopping their processes.*

| Project | Stars | What it does |
|---|--:|---|
| [**AVGVSTVS96/herdr-drovr**](https://github.com/AVGVSTVS96/herdr-drovr) | 26 | Uses fzf and the Herdr socket API to move live tabs and panes between workspaces without stopping their processes. |
| [**ronly2460/herdr-pane-mover**](https://github.com/ronly2460/herdr-pane-mover) | 2 | Moves Herdr panes between workspaces with an interactive arrow-key picker. |
| [**iuhoay/herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane) | 2 | Moves the active pane into a new tab while preserving its process, similar to tmux break-pane. It unzooms complex tabs first and leaves single-pane tabs unchanged. |
| [**shadowfax92/herdr-ferry**](https://github.com/shadowfax92/herdr-ferry) | 1 | Moves live Herdr TUI panes and tabs between workspaces through a Rust popup without restarting them. |
| [**Jenish-Shobhit/paneMorph**](https://github.com/Jenish-Shobhit/paneMorph) | 1 | Moves live panes between tabs and spaces in Herdr TUI without restarting their processes. Sends a pane anywhere, fetches one here, and undoes any move. |
| [**dimitri4d/herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover) | 1 | Moves a running Herdr TUI pane to another tab or workspace through a Workspace, Tab, Pane tree picker. Works with keyboard and mouse and keeps the process alive. |
| [**barewalker/herdr-jump**](https://github.com/barewalker/herdr-jump) | 0 | Finds, focuses, or moves panes across Herdr TUI workspaces with a fuzzy picker. |
| [**JordanBelfort1/herdr-pane-tools**](https://github.com/JordanBelfort1/herdr-pane-tools) | 0 | Moves a running pane into another tab as a split through a keyboard and mouse menu, without restarting the session. Windows only. |
| [**Unayung/herdr-pane-pull**](https://github.com/Unayung/herdr-pane-pull) | 0 | Pulls marked panes from any workspace into the current Herdr TUI tab and sends one back out, keeping agents and shells running. |
| [**saiyajosh/herdr-schlepr**](https://github.com/saiyajosh/herdr-schlepr) | 0 | Moves live panes and whole tabs between Herdr TUI workspaces from a keyboard-driven popup, choosing the destination pane, split direction, and ratio. |
| [**shrwnsan/herdr-herder**](https://github.com/shrwnsan/herdr-herder) | 0 | Adds a Herdr TUI picker that moves a pane or tab to another place and an action that evens pane widths and heights. |
| [**wyattjoh/herdr-plugin-move**](https://github.com/wyattjoh/herdr-plugin-move) | 0 | Moves the focused Herdr TUI pane to another workspace and tab chosen from a searchable popup. |
| [**yuloop/herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move) | 0 | Moves and rearranges Herdr panes across tabs using keyboard shortcuts. |
| [**dgnsrekt/herdr-yoke**](https://github.com/dgnsrekt/herdr-yoke) | 0 | Pairs two existing Herdr TUI tabs side by side and restores the second tab with the same shortcut. |

### Session labels, notes and context locators

*7 projects. Tools that name, tag, annotate, or locate agent sessions so they are easier to find later.*

| Project | Stars | What it does |
|---|--:|---|
| [**wenhanweime/herduck**](https://github.com/wenhanweime/herduck) | 13 | Groups related Claude Code, Codex, OpenCode, and Pi sessions into one Work and keeps its goal, blocker, and next step. Runs as a separate app derived from Herdr, with a thin plugin that opens it from Herdr. |
| [**fru-dev3/glyph**](https://github.com/fru-dev3/glyph) | 6 | Names coding-agent sessions and rebuilds Herdr TUI workspaces across machines, with an agent-usage plugin. |
| [**ariel-ps/herdr-sessions**](https://github.com/ariel-ps/herdr-sessions) | 1 | Keeps Herdr agent names and pane labels in sync and adds commands to list and link agent sessions. Adds short launcher commands such as claude-danger and codex-danger that start many agent CLIs with permission prompts bypassed. |
| [**jovylle/herdr-session-title-name**](https://github.com/jovylle/herdr-session-title-name) | 0 | Preserves terminal titles and session names across Herdr tab closes. |
| [**Dimon94/herdr-context-locator**](https://github.com/Dimon94/herdr-context-locator) | 0 | Copies a self-describing locator for a Herdr agent's canonical native session context. |
| [**EdJ/wsp**](https://github.com/EdJ/wsp) | 0 | Tracks projects, tasks, notes, and tags alongside live Herdr workspaces and publishes the combined context to the sidebar. |
| [**Cainiaooo/sessmark**](https://github.com/Cainiaooo/sessmark) | 0 | Tags coding-agent sessions and stores notes, with an optional Herdr TUI plugin. |

### Declarative workspace layouts in YAML, TOML and Lua

*12 projects. Config-file layouts that build or recreate workspaces from declared tabs, panes, commands, and agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**yuk1ty/herdr-spreader**](https://github.com/yuk1ty/herdr-spreader) | 145 | Builds complete Herdr layouts from YAML, including tabs, splits, directories, startup commands, and dependencies that wait for output patterns before launching later panes. |
| [**ropali/herdr-compose**](https://github.com/ropali/herdr-compose) | 4 | Defines Herdr workspaces, tabs, panes, and startup commands in reusable YAML layouts. |
| [**ExLuna-rs/herdr-auto-layout**](https://github.com/ExLuna-rs/herdr-auto-layout) | 3 | Applies declarative tabs, panes, commands, and agents to new Herdr TUI workspaces. |
| [**zackshen/herdr-workspace**](https://github.com/zackshen/herdr-workspace) | 2 | Creates a workspace and apply a layout profile from a centered popup. |
| [**3mmdrew/herdr-layout**](https://github.com/3mmdrew/herdr-layout) | 2 | Defines and creates Herdr workspace layouts in plain Lua, including pane splits and startup commands, without YAML or a separate service. |
| [**skydiver/herdr-pinned-workspaces**](https://github.com/skydiver/herdr-pinned-workspaces) | 1 | Recreates declared workspaces in Herdr TUI when they disappear, in their original sidebar position and at startup. |
| [**timaliev/herdr-layout**](https://github.com/timaliev/herdr-layout) | 0 | Defines session-aware Herdr layouts in YAML, applies them idempotently, and can load them automatically at startup. |
| [**CedarVerse/herdr-vergent**](https://github.com/CedarVerse/herdr-vergent) | 0 | Declares Herdr TUI workspaces, tabs, and panes in a TOML file and converges the running session to it at every server start. Re-runs are idempotent and never delete live state. |
| [**Rocco-Gossmann/Herdr-Workspace**](https://github.com/Rocco-Gossmann/Herdr-Workspace) | 0 | Creates a Herdr workspace with multiple tabs and splits in one command. |
| [**mike-bronner/herdr-plugin-agentic-panes-layout**](https://github.com/mike-bronner/herdr-plugin-agentic-panes-layout) | 0 | Applies a configurable TOML layout of tabs, panes, commands, and agents to Herdr TUI workspaces, including newly created worktrees. |
| [**tipok/herdr-layouts**](https://github.com/tipok/herdr-layouts) | 0 | Builds complete Herdr workspaces from declarative TOML files defining tabs, panes, split directions, and startup commands. |
| [**phenome/herdr-layout**](https://github.com/phenome/herdr-layout) | 0 | Creates or reuses tabs and runs commands from up to three saved Herdr layouts. |

### tmuxinator-style project launchers

*8 projects. Launchers that start whole project workspaces from tmuxinator-like project definitions or templates.*

| Project | Stars | What it does |
|---|--:|---|
| [**willfish/mux**](https://github.com/willfish/mux) | 2 | Launches tmuxinator-style project configurations into tmux sessions, Herdr TUI workspaces, or Herdr desktop spaces. |
| [**mhernandezve/herdinator**](https://github.com/mhernandezve/herdinator) | 2 | Manages named Herdr workspaces from tmuxinator-style project files, mapping windows to tabs. Starts an existing matching workspace instead of creating a duplicate; early stage targeting Herdr 0.9.1. |
| [**alon-z/herdr-devup**](https://github.com/alon-z/herdr-devup) | 2 | Reads `.herdr/dev.toml` to start a project's tabs, panes, and services, refresh an ngrok URL across configured environment files, and close only the tabs it created. |
| [**frankwiles/hterm**](https://github.com/frankwiles/hterm) | 1 | Launches repeatable Herdr TUI workspaces from project definitions using a macOS CLI and bundled Raycast extension. |
| [**tombell/tendr**](https://github.com/tombell/tendr) | 0 | Starts and manages local or SSH-accessible Herdr TUI sessions from declarative workspace, pane and lifecycle definitions. |
| [**kylescudder/schmerdr**](https://github.com/kylescudder/schmerdr) | 0 | Builds Herdr TUI workspaces, tabs, panes and agents from editable per-project shell templates. |
| [**LandonSchropp/herdr-project**](https://github.com/LandonSchropp/herdr-project) | 0 | Opens Herdr workspaces and worktrees with preconfigured tabs and commands, in the spirit of tmuxinator. A default project applies to any repository without its own config. |
| [**yordanbuilds/rig**](https://github.com/yordanbuilds/rig) | 0 | Starts a project stack in Herdr TUI with configured tabs, panes, and dependent processes. |

### Saved layout snapshots and screen grids

*4 projects. Tools that save, preview, or rearrange pane geometry and restore it on request.*

| Project | Stars | What it does |
|---|--:|---|
| [**noviadi/herdr-layout**](https://github.com/noviadi/herdr-layout) | 0 | Saves Herdr pane splits and arrangements and restores the same workspace geometry later, similar to tmux-resurrect for layouts. |
| [**caoer/ccc-herdr-layout**](https://github.com/caoer/ccc-herdr-layout) | 0 | Previews and applies pane layouts in the current Herdr TUI tab, restoring the original layout on cancellation. |
| [**WillHeather/herdr-grid**](https://github.com/WillHeather/herdr-grid) | 0 | Moves agent panes into a screen-sized grid in Herdr TUI and restores their original tabs and layouts on request. |
| [**scantinibudden/herdr-copycat**](https://github.com/scantinibudden/herdr-copycat) | 0 | Saves a Herdr TUI workspace as a named space with its tabs, splits, folders and programs, and opens fresh copies of it with one key. |

### Full workspace save and restore after restart

*10 projects. Snapshot tools that capture workspaces, tabs, panes, directories, and programs, then rebuild them after a restart or crash.*

| Project | Stars | What it does |
|---|--:|---|
| [**ntindle/herdr-resurrect**](https://github.com/ntindle/herdr-resurrect) | 44 | Captures workspaces, tabs, panes, directories, and running agent processes so a complete Herdr environment can be restored after a crash or restart. |
| [**wbarakat/omarchy-session-restore**](https://github.com/wbarakat/omarchy-session-restore) | 5 | Saves Omarchy window and terminal state and restores it after login, with optional Herdr agent-session resume. |
| [**chandrasekharan98/herdr-workspace-save**](https://github.com/chandrasekharan98/herdr-workspace-save) | 4 | Saves Herdr workspace layouts and commands for later restoration through an fzf picker. |
| [**cantona/herdr-revive**](https://github.com/cantona/herdr-revive) | 2 | Saves the programs, working directories, layouts and agent conversations in your panes, then relaunches them after a Herdr restart from retained snapshots or reusable named workspaces. Runs as a Herdr TUI plugin and as a Herdr app mod with a dialog for saving and relaunching. |
| [**momentohq/mo-herdr**](https://github.com/momentohq/mo-herdr) | 1 | Runs mo inside herdr panes: session restore after a herdr restart, a launch action, and SIGKILL cleanup. |
| [**nickmaglowsch/herdr-session-restore**](https://github.com/nickmaglowsch/herdr-session-restore) | 1 | Tags Claude Code panes with session IDs, saves the workspace, tab, and directory layout during a clean server stop, and rebuilds it on the next cold start using `claude --resume`. It is intentionally Claude-only and requires a clean shutdown. |
| [**lancodev/herdr-checkpoint**](https://github.com/lancodev/herdr-checkpoint) | 0 | Saves Herdr TUI workspace, tab, pane, directory, and program snapshots and restores them later, closing items outside the checkpoint. |
| [**e-denny/herdr-continuum**](https://github.com/e-denny/herdr-continuum) | 0 | Snapshots every Herdr TUI pane's layout, folder and running program every five minutes and relaunches them after a restart. Restores nvim from its session file. |
| [**Wartafak/herdr-cwd-restore**](https://github.com/Wartafak/herdr-cwd-restore) | 0 | Tracks each tab's live working directory and restores it after a Herdr server restart, keeping the workspace layout in one auto-saved project file. |
| [**zlj-zz/herdr-harbor**](https://github.com/zlj-zz/herdr-harbor) | 0 | Captures a live Herdr TUI workspace (tabs, splits, pane commands, agent sessions) into a layout store, relaunches it later, and syncs it in the background. A single Rust binary. |

### Pane command relaunchers after restart

*7 projects. Tools that remember the commands in each pane, such as dev servers and TUIs, and run them again after a restart.*

| Project | Stars | What it does |
|---|--:|---|
| [**zap0xfce2/herdr-pane-restart**](https://github.com/zap0xfce2/herdr-pane-restart) | 1 | Runs a configured command in named panes on server startup. |
| [**unstable-code/herdr-pane-resurrect**](https://github.com/unstable-code/herdr-pane-resurrect) | 1 | Saves the commands running in Herdr TUI panes and restores them after a restart, like tmux-resurrect. |
| [**devicki/herdr-respawn**](https://github.com/devicki/herdr-respawn) | 1 | Relaunches lazygit, editors, and other allowlisted TUIs in their panes after a Herdr TUI server restart or reboot. |
| [**joao-carmassi/herdr-respawn**](https://github.com/joao-carmassi/herdr-respawn) | 0 | Remembers long-running pane processes such as dev servers and re-runs them in their original panes when Herdr restarts. Creates a new tab when the saved pane is gone and skips panes running agents. |
| [**PascalKraupner/herdr-resurrect**](https://github.com/PascalKraupner/herdr-resurrect) | 0 | Records commands running in Herdr TUI panes and relaunches them after a server restart. Ships a prebuilt Go binary with checksum verification. |
| [**tlpinney/herdr-keep**](https://github.com/tlpinney/herdr-keep) | 0 | Runs terminal apps such as lazygit, btop and yazi so Herdr TUI starts them again in their panes after a restart or reboot. |
| [**bagonyi/herdr-restore-commands**](https://github.com/bagonyi/herdr-restore-commands) | 0 | Relaunches commands you list, such as gh dash and lnav, in their Herdr TUI panes when a session restarts. |

### Agent auto-resume after a server restart

*14 projects. Plugins that bring dead or interrupted agent panes back into their previous conversations after Herdr restarts.*

| Project | Stars | What it does |
|---|--:|---|
| [**hmu332233/herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart) | 3 | Restarts an idle Claude Code, Codex, Grok, or AGY agent in the same Herdr pane and resumes its session. |
| [**codergeek121/herdr-continue**](https://github.com/codergeek121/herdr-continue) | 1 | Tells every idle agent to continue its work after Herdr TUI restarts and restores sessions. Needs jq. |
| [**matthewjfberry/herdr-claude-resume**](https://github.com/matthewjfberry/herdr-claude-resume) | 1 | Reopens Claude Code conversations in their Herdr terminals after a reboot. Ships as a Herdr app mod plus a Claude Code plugin with hooks. |
| [**aliaksandr-haurylau-godel/herdr-restart-agents**](https://github.com/aliaksandr-haurylau-godel/herdr-restart-agents) | 1 | Restarts coding agents in their Herdr TUI panes and resumes the same session. Restarts one agent or a selected set, optionally updating the agent first. |
| [**KennethWKZ/herdr-ccs**](https://github.com/KennethWKZ/herdr-ccs) | 0 | Detects Claude Code sessions launched through `ccs claude` and restores them through the CCS launcher. |
| [**victor-software-house/herdr-restore-notice**](https://github.com/victor-software-house/herdr-restore-notice) | 0 | Adds compact notices to restored Herdr TUI scrollback so users can click to resume selected agent sessions. |
| [**Angel-O/herdr-agent-resume**](https://github.com/Angel-O/herdr-agent-resume) | 0 | Generates the exact resume command for an interrupted Claude Code, Codex, or custom agent session and either copies it or pastes it into a Herdr pane. |
| [**aiki-sh/aiki-plugin-herdr**](https://github.com/aiki-sh/aiki-plugin-herdr) | 0 | Reports Aiki harness session identities to Herdr TUI panes so native sessions can be restored after a server restart. |
| [**ninanoV/herdr-lazy-resume**](https://github.com/ninanoV/herdr-lazy-resume) | 0 | Resumes Claude Code sessions one pane at a time on first focus after a Herdr server restart, instead of starting all together. |
| [**atuinsh/herdr-atuin**](https://github.com/atuinsh/herdr-atuin) | 0 | Resumes agent panes through Atuin threads after a Herdr restart, instead of each agent's own resume command. Matches each pane to its own session. |
| [**Hai-Fai-Solutions/herdr-pig**](https://github.com/Hai-Fai-Solutions/herdr-pig) | 0 | Shows PiG sessions in Herdr TUI as an agent with idle, working and blocked state and reopens the same PiG session after a server restart. |
| [**quinnjr/herdr-auto-resume**](https://github.com/quinnjr/herdr-auto-resume) | 0 | Relaunches dead agent panes such as Claude Code, opencode and kiro-cli into their previous sessions after a Herdr TUI restart. |
| [**seankao31/herdr-autoresume**](https://github.com/seankao31/herdr-autoresume) | 0 | Continues only interrupted agents after Herdr restarts, lets idle agents restore background work, and restarts kept commands. |
| [**yavuzhansarmaz/herdr-muse-resume**](https://github.com/yavuzhansarmaz/herdr-muse-resume) | 0 | Resumes Muse agent sessions automatically in restored Herdr TUI panes after a server restart. |

### Idle agent parking and hibernation

*15 projects. Tools that stop idle agents to free memory and resume the same conversation when you return to the pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**andymartinezot/avocado-park**](https://github.com/andymartinezot/avocado-park) | 5 | Parks idle Claude Code, Codex, and OpenCode sessions to free memory and resumes them in the same Herdr TUI pane. |
| [**bengemine/herdr-hibernate**](https://github.com/bengemine/herdr-hibernate) | 4 | Suspends idle Claude Code, Codex, or Grok panes to reduce memory use while keeping pane state and directory context. Pressing Enter resumes a hibernated session. |
| [**DnzzL/herdr-idle**](https://github.com/DnzzL/herdr-idle) | 3 | Stops idle Herdr TUI agents to free memory while keeping panes available to resume their conversations. |
| [**dalogax/herdr-agent-hibernate**](https://github.com/dalogax/herdr-agent-hibernate) | 2 | Ends idle, unfocused OpenCode, Claude Code and Codex panes to free memory and relaunches the same session with native resume flags when you focus the pane again. |
| [**TheThoughtagen/attic**](https://github.com/TheThoughtagen/attic) | 1 | Finds idle coding-agent sessions, saves their state, and closes them to reclaim resources while keeping them restorable. A Textual dashboard and Herdr plugin support pinning, snoozing, and reviewing archived workspaces. |
| [**rrg/herdr-park-agents**](https://github.com/rrg/herdr-park-agents) | 0 | Parks a coding-agent pane in herdr: stop the process, close the pane, and resume the session later from a workspace panel. |
| [**xenking/herdr-omp-sleep**](https://github.com/xenking/herdr-omp-sleep) | 0 | Parks idle omp sessions in Herdr TUI panes and restores the same session when the user presses Enter. |
| [**novarii/claude-hibernate**](https://github.com/novarii/claude-hibernate) | 0 | Puts idle Claude Code sessions to sleep to free memory and resumes them on the first keystroke. Ships a Herdr plugin hook. |
| [**pandore/herdr-sleep**](https://github.com/pandore/herdr-sleep) | 0 | Puts idle Claude Code agents to sleep after a day and leaves a summary page in the tab; Enter resumes the same conversation. Summaries are in Ukrainian and the plugin is beta. |
| [**common-resources/herdr-autopark**](https://github.com/common-resources/herdr-autopark) | 0 | Parks coding agents that have been idle for an hour to free their RAM, keeps the pane showing the conversation, and resumes the agent on Enter. |
| [**haretoke/herdr-agent-parking**](https://github.com/haretoke/herdr-agent-parking) | 0 | Parks idle Claude Code sessions in Herdr TUI to free memory and resumes them in place with a note you left, grouped by workspace. |
| [**0xArchiviste/herdr-memory-guard**](https://github.com/0xArchiviste/herdr-memory-guard) | 0 | Hibernates long-idle Herdr agent threads on Linux and WSL when memory runs low, keeping native sessions so they can resume. Starts in observation mode and logs the reason for every decision. |
| [**MJuma/herdr-copilot-park**](https://github.com/MJuma/herdr-copilot-park) | 0 | Parks idle GitHub Copilot CLI tabs in the Herdr TUI to free memory, leaving a small placeholder. Press Enter in the tab to resume the same session. |
| [**meta-boy/herdr-shelve**](https://github.com/meta-boy/herdr-shelve) | 0 | Keeps only the most recently used agent tabs awake in the Herdr TUI and quits the rest, resuming each agent in the same pane when you focus its tab. Supports Claude Code, Codex and OpenCode. |
| [**prabhatCH/herdr-park**](https://github.com/prabhatCH/herdr-park) | 0 | Hibernates idle agent tabs in Herdr TUI to free memory and resumes the exact session later from a searchable picker. |

### Stale and idle agent cleanup

*5 projects. Lists that flag idle or inactive agent panes and workspaces and close the ones you confirm.*

| Project | Stars | What it does |
|---|--:|---|
| [**Gareth-Rouse/herdr-plugin-session-pruner**](https://github.com/Gareth-Rouse/herdr-plugin-session-pruner) | 0 | Tracks workspace last use and removes inactive workspaces from restored sessions. |
| [**krzysztoff1/herdr-cull**](https://github.com/krzysztoff1/herdr-cull) | 0 | Lists Herdr agent panes, flags stale sessions, and closes only the panes selected for confirmation. |
| [**leonho/herdr-idle-panes**](https://github.com/leonho/herdr-idle-panes) | 0 | Lists active and idle Herdr TUI panes and lets users jump to active panes or review and close idle ones. |
| [**ivorpad/herdr-reap**](https://github.com/ivorpad/herdr-reap) | 0 | Lists agents by lifecycle state in a Herdr TUI popup and closes finished agent panes on request. |
| [**joelhooks/herdr-janitor**](https://github.com/joelhooks/herdr-janitor) | 0 | Reviews stale Herdr workers and closes eligible panes only after ownership, state, identity, and clean-worktree checks. |

### Workspace stash, suspend and archive

*9 projects. Tools that snapshot a workspace, tab, or parked panes, close them, and bring them back later from a picker.*

| Project | Stars | What it does |
|---|--:|---|
| [**iviaxpow3r/herdr-session-parker**](https://github.com/iviaxpow3r/herdr-session-parker) | 13 | Parks active panes and tabs outside the current working layout and restores them later with agent state and prompt progress intact. |
| [**victor-software-house/herdr-stash**](https://github.com/victor-software-house/herdr-stash) | 3 | Stashes Herdr TUI workspaces, stopping their processes while saving pane layouts and agent conversations for later restoration. |
| [**asermax/herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace) | 1 | Suspends a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker). |
| [**Keepstateai/cli · herdr**](https://github.com/Keepstateai/cli/tree/main/herdr) | 1 | Shows KeepState sessions, agents, saved points and Cruise receipts in Herdr panes through the ks client. Sends a Herdr notification when a Cruise job finishes. |
| [**shaun-agent/herder-shelving-skill**](https://github.com/shaun-agent/herder-shelving-skill) | 0 | Guides agents through discovering and safely restoring custom Herdr TUI workspace shelves. |
| [**anilkmr-a2z/herdr-shelf**](https://github.com/anilkmr-a2z/herdr-shelf) | 0 | Archives agent tabs inactive for days and restores them later with the conversation resumed. |
| [**yavuzhansarmaz/herdr-archive**](https://github.com/yavuzhansarmaz/herdr-archive) | 0 | Archives Herdr TUI tabs as named restore points with layout, working directories, and agent sessions to free memory, and restores them by hand or after idle days. |
| [**frega/herdr-suspenders**](https://github.com/frega/herdr-suspenders) | 0 | Suspends a single Herdr tab by snapshotting its layout and agent sessions, closing it, and reviving it later in the same workspace. |
| [**AndrijaSkontra/herdr-stash**](https://github.com/AndrijaSkontra/herdr-stash) | 0 | Hides a Herdr TUI workspace by saving its tabs, splits, working directories and labels, then closing it. Restores all hidden workspaces with their layout later. |

### Undo close and reopen closed panes

*6 projects. Browser-style undo for closed panes, tabs, and workspaces, restoring layout, directory, and running agent.*

| Project | Stars | What it does |
|---|--:|---|
| [**pedroloch/herdr-undo-close**](https://github.com/pedroloch/herdr-undo-close) | 5 | Restores recently closed panes or tabs, including their split hierarchy, directories, labels, and launched agents, through a shortcut or history picker. |
| [**federbenjamin/herdr-undo-close**](https://github.com/federbenjamin/herdr-undo-close) | 2 | Reopens the pane you just closed in Herdr in the same split, with its old scrollback above a fresh prompt. A Claude Code pane resumes its conversation, and a command that was running returns typed but not run. |
| [**rchougule/herdr-pane-reopen**](https://github.com/rchougule/herdr-pane-reopen) | 1 | Reopens the last closed pane, tab or workspace in Herdr TUI with its position, directory and split layout, and resumes the coding agent that was running in it. |
| [**postrednik/herdr-last-pane-guard**](https://github.com/postrednik/herdr-last-pane-guard) | 0 | Reopens a Herdr TUI workspace or tab with its label, folder and position when its last shell exits. Ignores workspace, tab and pane closes made on purpose through the API. |
| [**LucHayward/herdr-undo-close**](https://github.com/LucHayward/herdr-undo-close) | 0 | Keeps closed panes and tabs alive in a holding workspace for a grace period so you can undo a close, like iTerm2. |
| [**chirichidi/herdr-reopen-closed**](https://github.com/chirichidi/herdr-reopen-closed) | 0 | Reopens the most recently closed Claude Code or Codex session in a new tab with its resume command, like Cmd+Shift+T in a browser. Repeat the key to go further back. |

### Fork Claude Code, Codex and OpenCode conversations into a new pane

*11 projects. Plugins that fork the conversation of the focused Claude Code, Codex, OpenCode or other agent into a new pane, tab or workspace while the original keeps running.*

| Project | Stars | What it does |
|---|--:|---|
| [**dmangla3/herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message) | 4 | Forks a Claude Code or Codex conversation from an earlier user message into a new tab, split pane, or workspace without modifying source transcripts. |
| [**calebcauthon/herdr-agent-copy-paste-fork**](https://github.com/calebcauthon/herdr-agent-copy-paste-fork) | 3 | Forks an agent session into a new Herdr pane by copying and pasting, either manually or through a hotkey. |
| [**t4t5/herdr-forkr**](https://github.com/t4t5/herdr-forkr) | 3 | Forks a Claude Code, Codex, Pi, or OpenCode conversation into another Herdr TUI pane, tab, or workspace. |
| [**potatoQi/herdr-focused-codex-fork**](https://github.com/potatoQi/herdr-focused-codex-fork) | 0 | Forks the Codex session in the focused Herdr TUI pane into a new pane to its right. |
| [**owpac/herdr-fork**](https://github.com/owpac/herdr-fork) | 0 | Forks the Claude Code or Codex session of the focused pane into a new split or tab. The original conversation stays unchanged. |
| [**calebcauthon/handoff**](https://github.com/calebcauthon/handoff) | 0 | Copies a Claude Code conversation from one pane and pastes it as a fork into another pane or a new split. Ships as a Herdr TUI plugin and as a Herdr app mod. |
| [**Crabor/herdr-clone-agent**](https://github.com/Crabor/herdr-clone-agent) | 0 | Clones the coding agent of a Herdr TUI pane into a new right or down pane that resumes a fork of its session. Supports pi and Claude Code. |
| [**connerohnesorge/vaultr**](https://github.com/connerohnesorge/vaultr) | 0 | Captures Claude Code and Codex sessions and forks them into Claude Code, Codex, or Pi. Streams captured Herdr TUI topology snapshots and includes pane actions for viewing and forking sessions. |
| [**mackt/herdr-session-fork**](https://github.com/mackt/herdr-session-fork) | 0 | Forks the focused Claude Code, Codex, Pi, or Grok conversation into another workspace or worktree chosen from a fuzzy list. |
| [**mcostasilva/herdr-sidebar**](https://github.com/mcostasilva/herdr-sidebar) | 0 | Forks the current OpenCode V2 conversation into a right-hand Herdr pane with one shortcut and returns to it with the same shortcut. Written in Rust. |
| [**DanielGnzlzVll/herdr-session-fork**](https://github.com/DanielGnzlzVll/herdr-session-fork) | 0 | Forks the focused agent session into a sibling pane with one keystroke, so both copies keep the conversation and working directory. |

### Pi side conversations and session forks

*8 projects. Pi extensions that open a side conversation or fork the current Pi session into a new Herdr pane or tab without stopping the original.*

| Project | Stars | What it does |
|---|--:|---|
| [**oscabriel/pi-herdr-btw**](https://github.com/oscabriel/pi-herdr-btw) | 26 | Opens a separate Pi side conversation in a Herdr TUI pane without changing the parent transcript. |
| [**onsails/fork-in**](https://github.com/onsails/fork-in) | 10 | Forks an ongoing Pi or omp conversation into a new Herdr tab while preserving its conversation context. |
| [**maxedapps/pi-herdr-sidetrack**](https://github.com/maxedapps/pi-herdr-sidetrack) | 2 | Clones a Pi conversation into an interactive Herdr TUI side pane while keeping the same checkout. |
| [**maxedapps/pi-herdr-fork**](https://github.com/maxedapps/pi-herdr-fork) | 1 | Forks a Pi conversation into a new focused Herdr TUI pane without interrupting the original session. |
| [**gpxl-dev/pi-herdr-split**](https://github.com/gpxl-dev/pi-herdr-split) | 0 | Opens parallel forked Pi sessions in Herdr panes and tabs. |
| [**jhsu/pi-herdr-btw**](https://github.com/jhsu/pi-herdr-btw) | 0 | Opens a Pi side conversation in a Herdr split with `/btw` and merges a summary back into the parent session. |
| [**wujunchuan/pi-fork-session-herdr**](https://github.com/wujunchuan/pi-fork-session-herdr) | 0 | Provides a Pi extension that forks the current persisted session into a new Herdr pane without replacing or stopping the Pi session in the original pane. |
| [**mcdonc/mcdonc-pi-herdr**](https://github.com/mcdonc/mcdonc-pi-herdr) | 0 | Makes Pi's background work visible in Herdr. `/bg` moves the current task into a pane, while `/tab` forks the conversation into a new tab through the socket API. |

### Moving sessions and workspaces to another machine or app

*5 projects. Tools that move sessions and workspaces to another machine, Herdr instance, or app such as Rex.*

| Project | Stars | What it does |
|---|--:|---|
| [**pattont/RexAgentRestore**](https://github.com/pattont/RexAgentRestore) | 24 | Imports Herdr workspaces into Rex with their tabs, splits, folders, and agent conversations. |
| [**tornikegomareli/herdr2rex**](https://github.com/tornikegomareli/herdr2rex) | 14 | Migrates Herdr TUI workspaces to Rex with tabs, splits, folders, and supported agent conversations. Imports Rex sessions back into Herdr and restores Claude Code conversations. |
| [**yansfil/herdr-remote-handoff**](https://github.com/yansfil/herdr-remote-handoff) | 1 | Transfers Claude Code sessions and workspaces between local and remote Herdr machines via a dedicated CLI. |
| [**alex-devdone/herdr-hub**](https://github.com/alex-devdone/herdr-hub) | 1 | Describes a herdr session of remote-attach panes as a portable manifest, and rebuild it on any machine. |
| [**virgile-men/herdr-claude-handoff**](https://github.com/virgile-men/herdr-claude-handoff) | 0 | Moves Claude Code sessions between Herdr TUI panes, Claude Code background sessions, and claude remote-control sessions. |

### Crash-proof and always-on sessions

*6 projects. Tools that keep terminals and agents alive across disconnects, crashes, and closed views.*

| Project | Stars | What it does |
|---|--:|---|
| [**mcc0x/herdr-tether**](https://github.com/mcc0x/herdr-tether) | 5 | Keeps local or SSH-backed terminal workloads running after their Herdr TUI view closes and reconnects to them later. |
| [**jamescary/mo**](https://github.com/jamescary/mo) | 1 | Runs persistent OMP agent sessions on a remote Mac using tmux and Herdr TUI, with SSH access and optional Telegram control. |
| [**mphaxise/omarchy-keepalive**](https://github.com/mphaxise/omarchy-keepalive) | 1 | Keeps Herdr agent sessions running on Omarchy with a bar panel, notifications, transcripts, and completion receipts. |
| [**pasta-disaster/herdr-nook**](https://github.com/pasta-disaster/herdr-nook) | 0 | Opens a floating shell per Herdr TUI workspace and keeps its tmux session running when the popup is hidden. |
| [**rezzminator/herdr-shield**](https://github.com/rezzminator/herdr-shield) | 0 | Keeps Herdr pane shells and coding agents alive across Herdr server crashes by running them in systemd user services. Linux only. |
| [**terafin/herdr-restart-always**](https://github.com/terafin/herdr-restart-always) | 0 | Supervises processes running in Herdr agent panes and restarts them after a crash. It works with Claude, Hermes, Codex, Pi, OpenCode, and other pane-based agents. |
