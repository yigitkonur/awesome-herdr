# Awesome Herdr: Switch and restore sessions

The full list for domain 5 of [Awesome Herdr](../README.md#5-switch-and-restore-sessions), ordered by GitHub stars.

- [Fuzzy session switchers and terminal pickers (111)](#fuzzy-session-switchers-and-terminal-pickers)
- [Persistence, snapshots, and state restoration (68)](#persistence-snapshots-and-state-restoration)
- [Workspace and multi-session management (83)](#workspace-and-multi-session-management)

---

## 5. Switch and restore sessions

*262 projects. Fuzzy switchers, state managers, and layout restoration tools for organizing agent workspaces.*

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
| [**wrn14897/herdr-plugins · herdr-picker**](https://github.com/wrn14897/herdr-plugins/tree/main/herdr-picker) | Searches Herdr TUI workspaces, screens, and agent conversations in a fuzzy picker with live preview. |
| [**fedeya/herdr-sesh**](https://github.com/fedeya/herdr-sesh) | Opens an fzf picker in Herdr TUI to jump between workspaces and agents or open sesh configs, zoxide, and fd directories, with a last-workspace toggle. |
| [**adriankarlen/yeet**](https://github.com/adriankarlen/yeet) | Opens a one-line-per-workspace picker in Herdr TUI that merges active workspaces, config-defined sessions and zoxide directories. Filters with gum or fzf. |
| [**ecylmz/herdr-hosts**](https://github.com/ecylmz/herdr-hosts) | Opens a hierarchical SSH host picker in Herdr TUI that reads folders, notes and connection details from ~/.ssh/config and opens the chosen host in its own tab. |
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
| [**nicosantux/herdr-hop**](https://github.com/nicosantux/herdr-hop) | Lists, attaches, creates, and deletes Herdr sessions from fzf popups, and opens project folders as workspaces with a git preview. |
| [**2ykwang/herdr-finder**](https://github.com/2ykwang/herdr-finder) | Finds running Herdr agents and terminals by name or visible output, previews the selected screen, and jumps to the session. |
| [**ryutaro-asada/herdr-nav-with-preview**](https://github.com/ryutaro-asada/herdr-nav-with-preview) | Opens a full-screen popup with a workspace, tab, and pane tree beside a live preview of the selected pane. Jumps to the pane on Enter, like tmux Ctrl+b w. |
| [**sushidesu/herdr-tabpick**](https://github.com/sushidesu/herdr-tabpick) | Lists every tab across all workspaces, most recently used first, in an fzf picker with a live pane preview. Tabs with several panes open into a pane tree. |
| [**Benny93/herdr-quick-bar**](https://github.com/Benny93/herdr-quick-bar) | Opens an fzf popup over all running agent sessions and jumps to the selected pane. |
| [**EskelinenAntti/zipln**](https://github.com/EskelinenAntti/zipln) | Fuzzy-finds any file or folder and jumps into its Herdr workspace, creating the workspace if needed. |
| [**mayaton/herdr-repo-picker**](https://github.com/mayaton/herdr-repo-picker) | Opens a Herdr TUI popup to fuzzy-search ghq repositories and jumps to the matching workspace. |
| [**tlpinney/herdr-atuin-resume**](https://github.com/tlpinney/herdr-atuin-resume) | Picks a coding-agent thread captured by Atuin and resumes it in a new Herdr TUI tab. |
| [**vieitesss/nexo**](https://github.com/vieitesss/nexo) | Jumps between Git projects, tmux or Herdr sessions and the coding agents waiting on you, locally or over SSH. Runs as a CLI and TUI on top of tmux or Herdr. |
| [**trebsoj/herdr-fzf-tab-switcher**](https://github.com/trebsoj/herdr-fzf-tab-switcher) | Opens an fzf picker in a popup listing every Herdr tab as space > tab and focuses the one you select. |
| [**AymanZahran/herdr-ai9s**](https://github.com/AymanZahran/herdr-ai9s) | Opens the ai9s session finder in a Herdr TUI sidebar and starts the selected agent in a new tab of the current workspace. Needs the ai9s program installed. |
| [**phillipahereza/herdr-ws**](https://github.com/phillipahereza/herdr-ws) | Opens a floating fuzzy finder in Herdr TUI for jumping between workspaces, tabs, agent panes, and zoxide directories. |
| [**cgardner/herdr-switcher-plus**](https://github.com/cgardner/herdr-switcher-plus) | Lists every coding agent in Herdr TUI with five orderings, filters as you type, and jumps to the pane you pick. Sorts by each session's last real message by default. |
| [**ricardofelixb/herdr-project-picker**](https://github.com/ricardofelixb/herdr-project-picker) | Opens a searchable project popup in Herdr TUI with one tab per machine and starts the chosen project as a new workspace. |
| [**Tranceh2/shep**](https://github.com/Tranceh2/shep) | Jumps to any Herdr TUI workspace, project, or folder from one fuzzy picker with blocked agents first and a preview of git state, files, and panes. Renames or closes items and opens new worktrees from the same popup. |
| [**GeorgGroenendaal/herdr-content-picker**](https://github.com/GeorgGroenendaal/herdr-content-picker) | Searches the terminal output of open Herdr TUI agent panes and past Pi and Claude Code sessions, then jumps to the match with a line preview. |
| [**AIToolSharing/anyresume**](https://github.com/AIToolSharing/anyresume) | Lists every Claude Code session in one picker and resumes the chosen one in its original folder, in any terminal or as a Herdr TUI plugin. |

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
| [**dmangla3/herdr-fork-from-message**](https://github.com/dmangla3/herdr-fork-from-message) | Forks a Claude Code or Codex conversation from an earlier user message into a new tab, split pane, or workspace without modifying source transcripts. |
| [**bengemine/herdr-hibernate**](https://github.com/bengemine/herdr-hibernate) | Suspends idle Claude Code, Codex, or Grok panes to reduce memory use while keeping pane state and directory context. Pressing Enter resumes a hibernated session. |
| [**hmu332233/herdr-agent-restart**](https://github.com/hmu332233/herdr-agent-restart) | Restarts an idle Claude Code, Codex, Grok, or AGY agent in the same Herdr pane and resumes its session. |
| [**victor-software-house/herdr-stash**](https://github.com/victor-software-house/herdr-stash) | Stashes Herdr TUI workspaces, stopping their processes while saving pane layouts and agent conversations for later restoration. |
| [**ExLuna-rs/herdr-auto-layout**](https://github.com/ExLuna-rs/herdr-auto-layout) | Applies declarative tabs, panes, commands, and agents to new Herdr TUI workspaces. |
| [**t4t5/herdr-forkr**](https://github.com/t4t5/herdr-forkr) | Forks a Claude Code, Codex, Pi, or OpenCode conversation into another Herdr TUI pane, tab, or workspace. |
| [**cantona/herdr-revive**](https://github.com/cantona/herdr-revive) | Saves the programs, working directories, layouts and agent conversations in your panes, then relaunches them after a Herdr restart from retained snapshots or reusable named workspaces. Runs as a Herdr TUI plugin and as a Herdr app mod with a dialog for saving and relaunching. |
| [**momentohq/mo-herdr**](https://github.com/momentohq/mo-herdr) | Runs mo inside herdr panes: session restore after a herdr restart, a launch action, and SIGKILL cleanup. |
| [**yansfil/herdr-remote-handoff**](https://github.com/yansfil/herdr-remote-handoff) | Transfers Claude Code sessions and workspaces between local and remote Herdr machines via a dedicated CLI. |
| [**alex-devdone/herdr-hub**](https://github.com/alex-devdone/herdr-hub) | Describes a herdr session of remote-attach panes as a portable manifest, and rebuild it on any machine. |
| [**asermax/herdr-suspend-workspace**](https://github.com/asermax/herdr-suspend-workspace) | Suspends a herdr workspace (snapshot layout + agents, close it, restore later from a popup picker). |
| [**TheThoughtagen/attic**](https://github.com/TheThoughtagen/attic) | Finds idle coding-agent sessions, saves their state, and closes them to reclaim resources while keeping them restorable. A Textual dashboard and Herdr plugin support pinning, snoozing, and reviewing archived workspaces. |
| [**nickmaglowsch/herdr-session-restore**](https://github.com/nickmaglowsch/herdr-session-restore) | Tags Claude Code panes with session IDs, saves the workspace, tab, and directory layout during a clean server stop, and rebuilds it on the next cold start using `claude --resume`. It is intentionally Claude-only and requires a clean shutdown. |
| [**unstable-code/herdr-pane-resurrect**](https://github.com/unstable-code/herdr-pane-resurrect) | Saves the commands running in Herdr TUI panes and restores them after a restart, like tmux-resurrect. |
| [**devicki/herdr-respawn**](https://github.com/devicki/herdr-respawn) | Relaunches lazygit, editors, and other allowlisted TUIs in their panes after a Herdr TUI server restart or reboot. |
| [**codergeek121/herdr-continue**](https://github.com/codergeek121/herdr-continue) | Tells every idle agent to continue its work after Herdr TUI restarts and restores sessions. Needs jq. |
| [**rchougule/herdr-pane-reopen**](https://github.com/rchougule/herdr-pane-reopen) | Reopens the last closed pane, tab or workspace in Herdr TUI with its position, directory and split layout, and resumes the coding agent that was running in it. |
| [**matthewjfberry/herdr-claude-resume**](https://github.com/matthewjfberry/herdr-claude-resume) | Reopens Claude Code conversations in their Herdr terminals after a reboot. Ships as a Herdr app mod plus a Claude Code plugin with hooks. |
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
| [**novarii/claude-hibernate**](https://github.com/novarii/claude-hibernate) | Puts idle Claude Code sessions to sleep to free memory and resumes them on the first keystroke. Ships a Herdr plugin hook. |
| [**ninanoV/herdr-lazy-resume**](https://github.com/ninanoV/herdr-lazy-resume) | Resumes Claude Code sessions one pane at a time on first focus after a Herdr server restart, instead of starting all together. |
| [**pandore/herdr-sleep**](https://github.com/pandore/herdr-sleep) | Puts idle Claude Code agents to sleep after a day and leaves a summary page in the tab; Enter resumes the same conversation. Summaries are in Ukrainian and the plugin is beta. |
| [**rezzminator/herdr-shield**](https://github.com/rezzminator/herdr-shield) | Keeps Herdr pane shells and coding agents alive across Herdr server crashes by running them in systemd user services. Linux only. |
| [**joao-carmassi/herdr-respawn**](https://github.com/joao-carmassi/herdr-respawn) | Remembers long-running pane processes such as dev servers and re-runs them in their original panes when Herdr restarts. Creates a new tab when the saved pane is gone and skips panes running agents. |
| [**atuinsh/herdr-atuin**](https://github.com/atuinsh/herdr-atuin) | Resumes agent panes through Atuin threads after a Herdr restart, instead of each agent's own resume command. Matches each pane to its own session. |
| [**PascalKraupner/herdr-resurrect**](https://github.com/PascalKraupner/herdr-resurrect) | Records commands running in Herdr TUI panes and relaunches them after a server restart. Ships a prebuilt Go binary with checksum verification. |
| [**postrednik/herdr-last-pane-guard**](https://github.com/postrednik/herdr-last-pane-guard) | Reopens a Herdr TUI workspace or tab with its label, folder and position when its last shell exits. Ignores workspace, tab and pane closes made on purpose through the API. |
| [**Hai-Fai-Solutions/herdr-pig**](https://github.com/Hai-Fai-Solutions/herdr-pig) | Shows PiG sessions in Herdr TUI as an agent with idle, working and blocked state and reopens the same PiG session after a server restart. |
| [**tlpinney/herdr-keep**](https://github.com/tlpinney/herdr-keep) | Runs terminal apps such as lazygit, btop and yazi so Herdr TUI starts them again in their panes after a restart or reboot. |
| [**e-denny/herdr-continuum**](https://github.com/e-denny/herdr-continuum) | Snapshots every Herdr TUI pane's layout, folder and running program every five minutes and relaunches them after a restart. Restores nvim from its session file. |
| [**bagonyi/herdr-restore-commands**](https://github.com/bagonyi/herdr-restore-commands) | Relaunches commands you list, such as gh dash and lnav, in their Herdr TUI panes when a session restarts. |
| [**quinnjr/herdr-auto-resume**](https://github.com/quinnjr/herdr-auto-resume) | Relaunches dead agent panes such as Claude Code, opencode and kiro-cli into their previous sessions after a Herdr TUI restart. |
| [**seankao31/herdr-autoresume**](https://github.com/seankao31/herdr-autoresume) | Continues only interrupted agents after Herdr restarts, lets idle agents restore background work, and restarts kept commands. |
| [**Wartafak/herdr-cwd-restore**](https://github.com/Wartafak/herdr-cwd-restore) | Tracks each tab's live working directory and restores it after a Herdr server restart, keeping the workspace layout in one auto-saved project file. |
| [**anilkmr-a2z/herdr-shelf**](https://github.com/anilkmr-a2z/herdr-shelf) | Archives agent tabs inactive for days and restores them later with the conversation resumed. |
| [**LucHayward/herdr-undo-close**](https://github.com/LucHayward/herdr-undo-close) | Keeps closed panes and tabs alive in a holding workspace for a grace period so you can undo a close, like iTerm2. |
| [**common-resources/herdr-autopark**](https://github.com/common-resources/herdr-autopark) | Parks coding agents that have been idle for an hour to free their RAM, keeps the pane showing the conversation, and resumes the agent on Enter. |
| [**chirichidi/herdr-reopen-closed**](https://github.com/chirichidi/herdr-reopen-closed) | Reopens the most recently closed Claude Code or Codex session in a new tab with its resume command, like Cmd+Shift+T in a browser. Repeat the key to go further back. |
| [**haretoke/herdr-agent-parking**](https://github.com/haretoke/herdr-agent-parking) | Parks idle Claude Code sessions in Herdr TUI to free memory and resumes them in place with a note you left, grouped by workspace. |
| [**yavuzhansarmaz/herdr-archive**](https://github.com/yavuzhansarmaz/herdr-archive) | Archives Herdr TUI tabs as named restore points with layout, working directories, and agent sessions to free memory, and restores them by hand or after idle days. |
| [**yavuzhansarmaz/herdr-muse-resume**](https://github.com/yavuzhansarmaz/herdr-muse-resume) | Resumes Muse agent sessions automatically in restored Herdr TUI panes after a server restart. |
| [**frega/herdr-suspenders**](https://github.com/frega/herdr-suspenders) | Suspends a single Herdr tab by snapshotting its layout and agent sessions, closing it, and reviving it later in the same workspace. |
| [**CedarVerse/herdr-vergent**](https://github.com/CedarVerse/herdr-vergent) | Declares Herdr TUI workspaces, tabs, and panes in a TOML file and converges the running session to it at every server start. Re-runs are idempotent and never delete live state. |
| [**zlj-zz/herdr-harbor**](https://github.com/zlj-zz/herdr-harbor) | Captures a live Herdr TUI workspace (tabs, splits, pane commands, agent sessions) into a layout store, relaunches it later, and syncs it in the background. A single Rust binary. |

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
| [**mhernandezve/herdinator**](https://github.com/mhernandezve/herdinator) | Manages named Herdr workspaces from tmuxinator-style project files, mapping windows to tabs. Starts an existing matching workspace instead of creating a duplicate; early stage targeting Herdr 0.9.1. |
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
| [**tlpinney/herdr-remuda**](https://github.com/tlpinney/herdr-remuda) | Mirrors panes from this machine or any saved SSH machine into one Herdr TUI view that you can watch or drive. Saves named views and surfaces agents that need input. |
| [**denera/herdr-crook**](https://github.com/denera/herdr-crook) | Lets Herdr TUI detect and manage coding agents that run inside Slurm allocations and containers on an HPC login node. |
| [**Yggdrasill501/border-collie**](https://github.com/Yggdrasill501/border-collie) | Sorts Herdr TUI spaces by recent use, pins favorite spaces, adds an agent picker, and names tabs and agents after their work. |
| [**Hon-Lu/herdr-new-workspace**](https://github.com/Hon-Lu/herdr-new-workspace) | Opens a new Herdr TUI workspace in any folder picked from a popup with fuzzy path completion or project search. |
| [**deepshape-ai/herdr-hive**](https://github.com/deepshape-ai/herdr-hive) | Shares selected Herdr TUI sessions with team members through a shared Hive server, with a Bee plugin to join and choose sessions. Members get full control of shared sessions. |
| [**ariel-ps/herdr-sessions**](https://github.com/ariel-ps/herdr-sessions) | Keeps Herdr agent names and pane labels in sync and adds commands to list and link agent sessions. Adds short launcher commands such as claude-danger and codex-danger that start many agent CLIs with permission prompts bypassed. |
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
| [**mrvnklm/herdr-space-groups**](https://github.com/mrvnklm/herdr-space-groups) | Groups spaces in the Herdr TUI sidebar by drag and drop, and shows all agents of a group side by side when you click the header. |
| [**Weicoz/herdr-machine-groups**](https://github.com/Weicoz/herdr-machine-groups) | Tags, groups, folds, and sorts saved SSH machines in a TUI popup so the sidebar can focus on one cluster. Avoids repeated SSH reconnects from disabling machines. |
| [**scantinibudden/herdr-copycat**](https://github.com/scantinibudden/herdr-copycat) | Saves a Herdr TUI workspace as a named space with its tabs, splits, folders and programs, and opens fresh copies of it with one key. |
| [**AndrijaSkontra/herdr-stash**](https://github.com/AndrijaSkontra/herdr-stash) | Hides a Herdr TUI workspace by saving its tabs, splits, working directories and labels, then closing it. Restores all hidden workspaces with their layout later. |
| [**fclebio/herdr-ssh-machines**](https://github.com/fclebio/herdr-ssh-machines) | Adds and removes SSH machines from inside the Herdr TUI using an fzf picker over the SSH config, with groups and client labels. |
| [**bethanyj28/herdr-new-workspace**](https://github.com/bethanyj28/herdr-new-workspace) | Opens a popup in Herdr TUI to pick a project directory from pinned and open projects, then an agent, before it creates the workspace. |
| [**premeq/paddock**](https://github.com/premeq/paddock) | Shows every machine, space, agent, and pane of a Herdr TUI fleet on one home screen, with blocked and finished agents on top. Lets you open any pane, create spaces and worktrees, and rename or close them. |
| [**virgile-men/herdr-claude-handoff**](https://github.com/virgile-men/herdr-claude-handoff) | Moves Claude Code sessions between Herdr TUI panes, Claude Code background sessions, and claude remote-control sessions. |
| [**mackt/herdr-session-fork**](https://github.com/mackt/herdr-session-fork) | Forks the focused Claude Code, Codex, Pi, or Grok conversation into another workspace or worktree chosen from a fuzzy list. |
| [**mcostasilva/herdr-sidebar**](https://github.com/mcostasilva/herdr-sidebar) | Forks the current OpenCode V2 conversation into a right-hand Herdr pane with one shortcut and returns to it with the same shortcut. Written in Rust. |
| [**DailybotHQ/herdr-machine-groups**](https://github.com/DailybotHQ/herdr-machine-groups) | Groups saved SSH machines into named groups and focuses one group at a time in the Herdr sidebar. |
| [**DanielGnzlzVll/herdr-session-fork**](https://github.com/DanielGnzlzVll/herdr-session-fork) | Forks the focused agent session into a sibling pane with one keystroke, so both copies keep the conversation and working directory. |
| [**kwanwooi25/herdr-plugin-workspace-groups**](https://github.com/kwanwooi25/herdr-plugin-workspace-groups) | Groups related workspaces from the keyboard, adds colored group badges to the sidebar, and makes linked worktrees inherit the parent group. |
| [**dorzey/herdr-sort-spaces-plugin**](https://github.com/dorzey/herdr-sort-spaces-plugin) | Sorts Herdr TUI workspaces alphabetically by label from the workspace context menu, or automatically whenever a workspace is created or renamed. |
| [**AmoabaKelvin/herdr-focus**](https://github.com/AmoabaKelvin/herdr-focus) | Hides every project except the ones you pick in Herdr TUI by parking other panes in a single space, then restores layouts, ratios, and worktrees when you exit. Parked shells and agents keep running. |
