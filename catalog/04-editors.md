# Awesome Herdr: Editor integrations

The full list for domain 4 of [Awesome Herdr](../README.md#4-editor-integrations), ordered by GitHub stars.

- [Neovim navigation and splits (30)](#neovim-navigation-and-splits)
- [Full Neovim-hosted workspaces (4)](#full-neovim-hosted-workspaces)
- [VS Code, Cursor, and dev containers (16)](#vs-code-cursor-and-dev-containers)
- [Vim, Kakoune, and other editors (13)](#vim-kakoune-and-other-editors)
- [REPL and code dispatchers (8)](#repl-and-code-dispatchers)
- [Editor plugins and bridges (35)](#editor-plugins-and-bridges)

---

## 4. Editor integrations

*106 projects. Bridges and pane synchronizers that let you drive Herdr agents directly from your code editor.*

### Neovim navigation and splits

*30 projects. Plugins that make movement between Neovim windows and Herdr panes feel continuous.*

| Project | Stars | What it does |
|---|--:|---|
| [**paulbkim-dev/vim-herdr-navigation**](https://github.com/paulbkim-dev/vim-herdr-navigation) | 115 | Ports vim-tmux-navigator behavior to Herdr. Direction keys move within Vim or Neovim until an edge is reached, then shift focus to the adjacent Herdr pane based on the pane's foreground process. |
| [**lmilojevicc/herdr-splits.nvim**](https://github.com/lmilojevicc/herdr-splits.nvim) | 69 | Bridges Neovim split navigation and smart pane resizing with Herdr terminal panes. |
| [**aimdevlee/herdr-nvim-nav**](https://github.com/aimdevlee/herdr-nvim-nav) | 22 | Moves between Neovim splits and Herdr TUI panes with shared Ctrl+h/j/k/l bindings and socket-based focus tracking. |
| [**nettlesh/dotfiles**](https://github.com/nettlesh/dotfiles) | 18 | Personal Alacritty, Fish, Herdr, and Neovim dotfiles with workspace navigation and agent-dispatch configuration. |
| [**luneth90/keycade**](https://github.com/luneth90/keycade) | 12 | Provides a shortcut recall arcade for Omarchy, herdr, tmux, Vim, Neovim and LazyVim, six cabinets, each with its own deck, progress and mastery. |
| [**devxplay/herdr.nvim**](https://github.com/devxplay/herdr.nvim) | 11 | Navigates Neovim splits and Herdr TUI panes with Ctrl+h/j/k/l using a pane marker and a companion navigator. |
| [**bojackduy/nvim-herdr-navigation**](https://github.com/bojackduy/nvim-herdr-navigation) | 7 | Applies vim-tmux-navigator-style directional keys across internal splits and surrounding Herdr panes. |
| [**kaar/nvim-herdr-navigator**](https://github.com/kaar/nvim-herdr-navigator) | 6 | Uses one set of `Ctrl+h/j/k/l` shortcuts to move through both Neovim splits and Herdr panes. |
| [**willfish/herdr-navigator**](https://github.com/willfish/herdr-navigator) | 4 | Provides the Herdr-side actions needed for shared Vim or Neovim navigation. It checks the active pane process and either forwards the key to the editor or moves Herdr focus. |
| [**odiumuniverse/herdr-smart-nav**](https://github.com/odiumuniverse/herdr-smart-nav) | 4 | Moves between Neovim windows, Herdr TUI panes, tabs and workspaces with directional shortcuts. |
| [**cinco/herdr-grep-nvim**](https://github.com/cinco/herdr-grep-nvim) | 3 | Combines ripgrep and fzf for live searching, then opens a selected match in a Neovim split beside the active Herdr agent. |
| [**willfish/herdr-navigator.nvim**](https://github.com/willfish/herdr-navigator.nvim) | 3 | Moves between Neovim windows and Herdr TUI panes, pairing with a Herdr-side navigator for movement from terminal panes. |
| [**suderman/edger**](https://github.com/suderman/edger) | 2 | Moves between Herdr panes and Neovim, Emacs or tmux splits with the same alt-hjkl keys. At the edge of a tab or workspace it continues into the neighboring Herdr tab or workspace. |
| [**sebcbi1/herdr-edge-nav**](https://github.com/sebcbi1/herdr-edge-nav) | 1 | Unifies directional navigation and resizing across Neovim splits, Herdr panes, tabs, and workspaces. Boundary detection forwards focus to the next surface without changing modes. |
| [**mirkobozzetto/dotfiles**](https://github.com/mirkobozzetto/dotfiles) | 1 | A macOS terminal setup using Ghostty with tmux or Herdr, Neovim, and routing that brings the user to whichever coding agent needs attention. |
| [**KoalaVim/herdr-nvim-aware**](https://github.com/KoalaVim/herdr-nvim-aware) | 1 | Routes navigation, split, close, zoom, and scroll shortcuts to Neovim or Herdr TUI according to pane focus. |
| [**jtnovellis/herdr-nvim**](https://github.com/jtnovellis/herdr-nvim) | 0 | Opens a persistent Neovim sidebar per Herdr tab and sends selected code and context to an agent. |
| [**RooseveltAdvisors/herdr-open-nvim**](https://github.com/RooseveltAdvisors/herdr-open-nvim) | 0 | Extracts readable file links from Herdr TUI pane transcripts and opens selected paths in Neovim. |
| [**luisgui1757/dotfiles**](https://github.com/luisgui1757/dotfiles) | 0 | A cross-platform Rose Pine terminal and editor setup for macOS, Linux, WSL2, and Windows. It includes Neovim, Herdr, tmux or psmux, several terminals and shells, Nix on POSIX, and chezmoi-managed configuration. |
| [**RooseveltAdvisors/vim-herdr-navigation**](https://github.com/RooseveltAdvisors/vim-herdr-navigation) | 0 | A fork of `vim-herdr-navigation` with shared Ctrl and Alt directional keys across Herdr panes and Vim or Neovim splits. |
| [**joo-was-already-taken/herdr-navigator.nvim**](https://github.com/joo-was-already-taken/herdr-navigator.nvim) | 0 | Moves between Neovim splits and Herdr TUI panes using a Neovim plugin and companion navigation CLI. |
| [**rahadur/herdr.nvim**](https://github.com/rahadur/herdr.nvim) | 0 | Ports the Ink and Paper color schemes from herdr.dev to Neovim. |
| [**s-0-a-r/copse**](https://github.com/s-0-a-r/copse) | 0 | A command-line agent development environment combining Herdr, Neovim, and parallel agent fan-out. |
| [**jakkzz/herdr-setup**](https://github.com/jakkzz/herdr-setup) | 0 | A reproducible Herdr and Neovim setup with pinned plugins and a cross-platform installer for macOS, Linux, and WSL. |
| [**solidsnakedev/herdr-pane-tools**](https://github.com/solidsnakedev/herdr-pane-tools) | 0 | Navigates Neovim windows and Herdr TUI panes and adds directional pane moves and rotation. |
| [**LiroRod/promptr**](https://github.com/LiroRod/promptr) | 0 | Provides a really small herdr plugin that integrates nvim with the multiplexer. |
| [**Aerosnail/nvim-herdr-navigator**](https://github.com/Aerosnail/nvim-herdr-navigator) | 0 | Navigates between Neovim splits and Herdr panes using a matching plugin pair. |
| [**kremeshnoi/herdr-nvim-sessions**](https://github.com/kremeshnoi/herdr-nvim-sessions) | 0 | Lists every running Neovim session across Herdr TUI workspaces in a sidebar pane. Jumps to an editor with a key or click. |
| [**webdavis/herdr-smart-nav**](https://github.com/webdavis/herdr-smart-nav) | 0 | Moves with Ctrl-h/j/k/l inside Neovim splits and across to the neighbouring Herdr pane when Neovim has nowhere left to go. |
| [**NathanymousFu/nvim-ascii-on-focus**](https://github.com/NathanymousFu/nvim-ascii-on-focus) | 0 | Switches macOS to a Latin input source when a Herdr pane running Neovim gains focus outside Insert or Replace mode. |

### Full Neovim-hosted workspaces

*4 projects. A deeper integration that uses Neovim as the main interface while Herdr owns the agent processes.*

| Project | Stars | What it does |
|---|--:|---|
| [**raymondware/herdr.nvim**](https://github.com/raymondware/herdr.nvim) | 5 | Opens the Herdr TUI in a Neovim floating terminal and shows agent states in a status window and statusline component. |
| [**MomePP/herd.nvim**](https://github.com/MomePP/herd.nvim) | 3 | Uses Neovim as the primary dashboard to launch, monitor, and control background Herdr agent sessions. |
| [**ctbaum/herdr-deck**](https://github.com/ctbaum/herdr-deck) | 2 | Adds the companion workspace launcher for herdr-agents.nvim: open or resume Claude and Codex in a ready-made Neovim, agent, shell, and lazygit deck. |
| [**romerramos/herdr-reviewr-nvim**](https://github.com/romerramos/herdr-reviewr-nvim) | 0 | Opens Reviewr files in the Neovim pane for the current HERDR workspace. |

### VS Code, Cursor, and dev containers

*16 projects. Extensions and environment setups for graphical editors and container-based development.*

| Project | Stars | What it does |
|---|--:|---|
| [**zenbu-labs/terminal-code · herdr-plugin**](https://github.com/zenbu-labs/terminal-code/tree/main/herdr-plugin) | 2,247 | Adds an action that opens terminal-code, a VS Code-style editor for the terminal, in a split to the right of the focused pane in Herdr TUI. The plugin installs the tode binary when it builds. |
| [**scott-the-programmer/vscode-devcontainers-herdr**](https://github.com/scott-the-programmer/vscode-devcontainers-herdr) | 16 | Forwards Herdr's Unix socket into VS Code development containers through a loopback TCP bridge, allowing containerized agents to report status and receive commands from the host Herdr instance. |
| [**gambtho/herdr-devcontainer**](https://github.com/gambtho/herdr-devcontainer) | 12 | Starts shells and coding agents inside a repository's Dev Container through the official Dev Containers CLI and presents them as normal Herdr panes. |
| [**timofey-TK/herdr-open-in-editor**](https://github.com/timofey-TK/herdr-open-in-editor) | 5 | Opens the active Herdr workspace in VS Code or Zed with one shortcut. Local and SSH-remote workspaces are translated into the correct editor URI automatically. |
| [**mkellerman/herdex**](https://github.com/mkellerman/herdex) | 3 | Displays Herdr TUI workspaces and agent status in VS Code, with a terminal and editor actions. |
| [**alex-devdone/herdr-cursor-open**](https://github.com/alex-devdone/herdr-cursor-open) | 1 | Opens the focused Herdr pane's project in Cursor or VS Code, including remote panes through the editor's Remote SSH support. |
| [**mrshll/herdr-container-agents**](https://github.com/mrshll/herdr-container-agents) | 1 | Detects coding agents running inside containers and report them as herdr agents. |
| [**phine-apps/herdr-collie**](https://github.com/phine-apps/herdr-collie) | 0 | Bridges VS Code and Herdr to orchestrate AI agents, Git worktrees, and context sharing directly from the editor. |
| [**clement-micol/herdr-bridge**](https://github.com/clement-micol/herdr-bridge) | 0 | Bridges from herdr panes to VS Code: attach herdr terminals via vscode:// URIs. |
| [**endoumame/herdr-vscode**](https://github.com/endoumame/herdr-vscode) | 0 | Adds an inline code-review workflow to VS Code for work associated with Herdr agent sessions. The source description is incomplete beyond writing comments where the code is read. |
| [**gogamid/pi-herdr-cursor-focus**](https://github.com/gogamid/pi-herdr-cursor-focus) | 0 | Hides the editor cursor in Herdr panes that are not currently focused. |
| [**Andreslvc/herdr_plugin**](https://github.com/Andreslvc/herdr_plugin) | 0 | Opens pane folder in VS Code, copy path, and open a folder as a space. |
| [**leoweigand/vsctask**](https://github.com/leoweigand/vsctask) | 0 | Runs VS Code tasks.json tasks outside VS Code, in a Herdr pane or a shell. |
| [**DcNiemandd/vscode-worktree**](https://github.com/DcNiemandd/vscode-worktree) | 0 | Manages git worktrees and their herdr agent sessions from a VS Code sidebar, no terminal needed. |
| [**leonardoacosta/hitch**](https://github.com/leonardoacosta/hitch) | 0 | Adds a VS Code and Cursor terminal profile that opens a Herdr pane for the workspace folder and attaches to it. Targets Herdr TUI panes on Linux workspace hosts. |
| [**sriharirao92/vscode-herdr-cockpit**](https://github.com/sriharirao92/vscode-herdr-cockpit) | 0 | Brings Herdr spaces, agents and shells into one VS Code window, with a sidebar of agent status and plan usage, and a companion Herdr plugin that opens the current space from the terminal. Also works in Cursor, Kiro and Positron. |

### Vim, Kakoune, and other editors

*13 projects. Navigation and workflow integrations for editors outside Neovim and VS Code.*

| Project | Stars | What it does |
|---|--:|---|
| [**ImArtisann/zed-herdr**](https://github.com/ImArtisann/zed-herdr) | 36 | Keeps Zed projects synchronized with Herdr workspaces by listening to lifecycle events over the Unix socket. It supports reconnection and full snapshot synchronization after interruptions. |
| [**roman/herdr.el**](https://github.com/roman/herdr.el) | 7 | Provides an Emacs porcelain interface for managing Herdr workspaces and agent sessions. |
| [**ionrock/ghostherd**](https://github.com/ionrock/ghostherd) | 3 | Manages Herdr agent terminals from Emacs through ghostel. |
| [**baongoc124/emacs-herdr**](https://github.com/baongoc124/emacs-herdr) | 3 | Runs the Herdr TUI in an Emacs Ghostel buffer and adds agent switching, project launches, and code dispatch. |
| [**Schaitanya535/herdr-config**](https://github.com/Schaitanya535/herdr-config) | 1 | A personal Herdr configuration with custom keys, a theme, and a helper that sends scrollback into Neovim. |
| [**T0mSIlver/hither**](https://github.com/T0mSIlver/hither) | 0 | Opens the active remote Herdr directory in Zed on macOS with a single key chord. |
| [**Yukaii/herdr-kakoune-popup**](https://github.com/Yukaii/herdr-kakoune-popup) | 0 | Runs Kakoune terminal commands in native Herdr popups. |
| [**Yukaii/herdr.kak**](https://github.com/Yukaii/herdr.kak) | 0 | Controls Herdr panes, tabs, focus, and popups from Kakoune. |
| [**AVGVSTVS96/vim-herdr-navigator**](https://github.com/AVGVSTVS96/vim-herdr-navigator) | 0 | Moves between Vim or Neovim splits and Herdr TUI panes with shared directional shortcuts. |
| [**eddof13/herdr.el**](https://github.com/eddof13/herdr.el) | 0 | Controls Herdr from Emacs while hosting Herdr's terminal sessions inside Emacs through ghostel. |
| [**SamuelCastrillon/tzemed**](https://github.com/SamuelCastrillon/tzemed) | 0 | A Windows-native development stack combining Herdr, Neovim, Peri, and Gentle-ai specification-driven development. |
| [**AVGVSTVS96/starter-dotfiles**](https://github.com/AVGVSTVS96/starter-dotfiles) | 0 | Minimal, agent-first macOS dotfiles for React and TypeScript development, including Ghostty, Herdr, Claude Code, Codex, LazyVim, Vite+, Nub, and basic shell tooling. |
| [**lhr0909/herdr-bel**](https://github.com/lhr0909/herdr-bel) | 0 | Forwards Herdr agent notifications to Zed Terminal Threads using the terminal bell signal. |

### REPL and code dispatchers

*8 projects. Tools for sending code or commands from an editor to a running pane or interactive session.*

| Project | Stars | What it does |
|---|--:|---|
| [**francjpd/broadmand**](https://github.com/francjpd/broadmand) | 3 | Broadcasts shell commands or a selected working directory to panes in the active Herdr TUI workspace. |
| [**exviolet/sendoff**](https://github.com/exviolet/sendoff) | 2 | Edits prompts in a Linux desktop app and sends them to terminal agents running in Herdr, tmux, or Orca. |
| [**jcarlos7121/herdr-sidekick-agents.nvim**](https://github.com/jcarlos7121/herdr-sidekick-agents.nvim) | 1 | Opens Claude Code, Codex, or Grok in side-by-side Herdr panes and forwards Neovim selection context. |
| [**timofey-TK/herdr-yazi-agent**](https://github.com/timofey-TK/herdr-yazi-agent) | 1 | Picks files in Yazi, get their paths in your agent's prompt. |
| [**rytkmt/herdr-send.nvim**](https://github.com/rytkmt/herdr-send.nvim) | 0 | Sends file references and prompts from Neovim to AI agents in the active Herdr workspace. |
| [**luiarthur/herdr.vim**](https://github.com/luiarthur/herdr.vim) | 0 | Starts a language-appropriate REPL in a Herdr pane and sends the current line, whole file, or visual selection from Vim or Neovim. It supports older Vim releases as well as modern Neovim. |
| [**lancodev/herdr-laravel-tinker**](https://github.com/lancodev/herdr-laravel-tinker) | 0 | Runs Laravel Tinker beside an editor in a Herdr TUI pane or popup and reevaluates the scratch file when saved. |
| [**AbhijithAnirudhan2907/herdr-sidebar**](https://github.com/AbhijithAnirudhan2907/herdr-sidebar) | 0 | A fork of herdr-sidebar that adds an editor inside the pane, including save, syntax highlighting, undo and redo, and find and replace. |

### Editor plugins and bridges

*35 projects. General-purpose bridges that synchronize editor state with Herdr panes and agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**eugenioenko/ttt · herdr-plugin**](https://github.com/eugenioenko/ttt/tree/main/herdr-plugin) | 1,093 | Opens TTT Editor in a Herdr TUI pane for editing files in the active worktree. |
| [**ChmaraX/herdr-nvim**](https://github.com/ChmaraX/herdr-nvim) | 353 | Opens a persistent Neovim sidebar in Herdr with file search and annotations that can be sent to agents. |
| [**makyinmars/herdr-context.nvim**](https://github.com/makyinmars/herdr-context.nvim) | 16 | Stages Neovim selections, cursor positions, and file details as Markdown context for a Herdr agent. |
| [**ryonakae/zerdr**](https://github.com/ryonakae/zerdr) | 10 | Keeps Herdr TUI workspace focus aligned with the matching Zed checkout and connects Zed terminal threads to Herdr panes. |
| [**mcuste/herdr-context.nvim**](https://github.com/mcuste/herdr-context.nvim) | 7 | Sends the current Neovim buffer, open buffers, or a Visual selection to a Herdr coding agent as a correctly formatted file reference. It targets one workspace agent automatically or opens a fuzzy picker when several agents are in the tab or workspace. |
| [**nwiizo/signalbox.nvim**](https://github.com/nwiizo/signalbox.nvim) | 6 | Controls persistent Herdr coding agents from Neovim with an attention-focused interface. |
| [**WorksOnMyVM/herdr-agent-bridge.nvim**](https://github.com/WorksOnMyVM/herdr-agent-bridge.nvim) | 5 | Stages Neovim editor context for Herdr agent panes. |
| [**ctbaum/herdr-agents.nvim**](https://github.com/ctbaum/herdr-agents.nvim) | 5 | Runs Claude Code, Codex, and Pi in Herdr TUI sibling panes while preserving Neovim editor integration and agent connections. |
| [**Zamua/openloc.nvim**](https://github.com/Zamua/openloc.nvim) | 4 | Opens file references in the Neovim that already belongs to the workspace. |
| [**alexeyco/herdr-open-in**](https://github.com/alexeyco/herdr-open-in) | 4 | Opens the current Herdr TUI workspace in a detected editor, with a picker when several editors are available. |
| [**AgriciDaniel/obsidian-herdr**](https://github.com/AgriciDaniel/obsidian-herdr) | 4 | Runs persistent Herdr TUI agent terminals in Obsidian and lets agents make logged, undoable vault edits. |
| [**nytafar/obsidian-herdr**](https://github.com/nytafar/obsidian-herdr) | 3 | Opens Herdr TUI or herdr-core agents as live terminal tabs in Obsidian and renders Claude Code sessions in a native view. |
| [**vonzelle-vzt/herdr-edit**](https://github.com/vonzelle-vzt/herdr-edit) | 3 | Edits code in a Herdr TUI pane with language-server diagnostics, completion, navigation, and companion panel integration. |
| [**TianZuo555/herdr.nvim**](https://github.com/TianZuo555/herdr.nvim) | 2 | Sends Neovim file and code references to coding agents running in the same Herdr tab. |
| [**utahta/herdr-prompt.nvim**](https://github.com/utahta/herdr-prompt.nvim) | 2 | Enables a Neovim user ask a Herdr agent about the code currently being viewed or edited. |
| [**Osmait/agentline.nvim**](https://github.com/Osmait/agentline.nvim) | 1 | Sends Neovim selections and buffers to coding agents through herdr. |
| [**RaphaelManke/send-to-agent.nvim**](https://github.com/RaphaelManke/send-to-agent.nvim) | 1 | Sends visual selections and review comments from Neovim to active AI agent sessions in Herdr. |
| [**Daniel-Steinberger/obsidian-herdr**](https://github.com/Daniel-Steinberger/obsidian-herdr) | 1 | Sends the next unchecked Markdown task to an agent in the matching Herdr workspace and marks it complete when the agent finishes. Continuous mode can process an entire checklist. |
| [**agentience/herdr-plugin-ide-jump**](https://github.com/agentience/herdr-plugin-ide-jump) | 1 | Raises the editor window for the focused Herdr TUI pane’s project or lets users select an editor window from a filterable popup. |
| [**jimididit/herdr-open-editor**](https://github.com/jimididit/herdr-open-editor) | 1 | Fuzzy-finds a file in the current repository or directory and opens it in the configured editor in a Herdr TUI split pane. |
| [**chenyao0910/herdr-jetbrains**](https://github.com/chenyao0910/herdr-jetbrains) | 1 | Opens the active Herdr workspace or worktree in Rider, WebStorm, IntelliJ IDEA, or GoLand. |
| [**dlwr/herdr-zed-follow**](https://github.com/dlwr/herdr-zed-follow) | 1 | Brings the Zed window for the focused workspace forward whenever you switch workspaces in Herdr TUI. |
| [**hungryhorace/selx**](https://github.com/hungryhorace/selx) | 1 | Sends a Helix or lazygit selection to a coding agent as a file and line reference. In Herdr it types the reference into the agent's pane, moves focus there and opens lazygit files in the running Helix. |
| [**qapquiz/herdr-sidekick.nvim**](https://github.com/qapquiz/herdr-sidekick.nvim) | 1 | Pastes a visual selection from Neovim into a coding agent's chatbox in a Herdr pane without submitting it. Needs the companion herdr-sidekick plugin. |
| [**qapquiz/herdr-sidekick**](https://github.com/qapquiz/herdr-sidekick) | 0 | Toggles a persistent Herdr TUI agent pane beside an editor. A companion Neovim plugin can paste selections into the agent without submitting. |
| [**aksh1618/herdr-vimnotate**](https://github.com/aksh1618/herdr-vimnotate) | 0 | Opens an agent's reply in Neovim so you can mark paragraphs as good, delete them or comment with vim motions. Sends the review to the agent's composer. |
| [**delimce/herdr-zed-tasks**](https://github.com/delimce/herdr-zed-tasks) | 0 | Lists the project's Zed tasks from .zed/tasks.json in a fuzzy picker and runs the chosen task in the Herdr TUI pane that was focused. |
| [**surajt02/herdr-here**](https://github.com/surajt02/herdr-here) | 0 | Attaches Herdr TUI to the workspace that owns a directory when Zed opens a terminal thread, and brings that workspace's checkout to the front in Zed through the zed-route plugin. |
| [**carandev/herdr-user-secrets**](https://github.com/carandev/herdr-user-secrets) | 0 | Opens the .NET user secrets secrets.json of the focused project in your editor, with a picker when the solution has several projects. |
| [**upnorthmedia/herdr-open-in-editor**](https://github.com/upnorthmedia/herdr-open-in-editor) | 0 | Opens file paths printed by an agent, or the whole workspace folder, in Zed, VS Code, Cursor, or Sublime Text at the exact line from the Herdr TUI. |
| [**gadenbuie/herdr-positron**](https://github.com/gadenbuie/herdr-positron) | 0 | Opens the current Herdr TUI space's directory in Positron, using the focused pane's working directory. |
| [**tangentyh/herdr-dog-ear**](https://github.com/tangentyh/herdr-dog-ear) | 0 | Opens a ctrl-clicked file link or selected path in $EDITOR from the Herdr TUI, reusing a vi-family pane in the tab or splitting a new one. |
| [**darjss/herdr-zed**](https://github.com/darjss/herdr-zed) | 0 | Opens the focused folder in Zed from the Herdr TUI, using ssh:// remote projects when a remote machine is selected. |
| [**ciokyyy/deictic**](https://github.com/ciokyyy/deictic) | 0 | Lets you Alt-click an element in a running Vite app, type a comment, and sends the source of the line that rendered it to a coding agent in Herdr. |
| [**XicuM/herdr-obsidian**](https://github.com/XicuM/herdr-obsidian) | 0 | Runs Herdr inside Obsidian on desktop and mobile with embedded terminal tabs, live agent status, and drag-and-drop file references. Lets agents open vault notes through herdr-bridge. |
