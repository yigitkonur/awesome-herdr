# Awesome Herdr: Worktrees and terminal experience

The full list for domain 6 of [Awesome Herdr](../README.md#6-worktrees-and-terminal-experience), ordered by GitHub stars.

- [Git worktree automation (139)](#git-worktree-automation)
- [Workspace lifecycle and multi-repository tools (45)](#workspace-lifecycle-and-multi-repository-tools)
- [Diff review and code inspection (89)](#diff-review-and-code-inspection)
- [File viewers, terminal browsers, and markdown previews (81)](#file-viewers-terminal-browsers-and-markdown-previews)
- [Pane navigation and overlay hints (60)](#pane-navigation-and-overlay-hints)
- [Pane layout management (44)](#pane-layout-management)
- [Terminal keybindings and shortcut helpers (88)](#terminal-keybindings-and-shortcut-helpers)
- [Command palettes and workspace switchers (62)](#command-palettes-and-workspace-switchers)
- [Status lines and workspace metadata (142)](#status-lines-and-workspace-metadata)
- [Automatic tab, pane, and workspace names (92)](#automatic-tab-pane-and-workspace-names)
- [Sidebar grouping, ordering, and filtering (45)](#sidebar-grouping-ordering-and-filtering)
- [Sidebar badges, tokens, and status indicators (88)](#sidebar-badges-tokens-and-status-indicators)
- [Status overlays, HUDs, and agent timers (78)](#status-overlays-huds-and-agent-timers)
- [Context meters and rate-limit gauges (90)](#context-meters-and-rate-limit-gauges)
- [Output inspection, logs, and transcripts (67)](#output-inspection-logs-and-transcripts)
- [Agent visualizations and terminal games (34)](#agent-visualizations-and-terminal-games)
- [Herdr TUI themes and appearance (19)](#herdr-tui-themes-and-appearance)
- [Security guards and collision detectors (21)](#security-guards-and-collision-detectors)
- [Plugin collections, frameworks, and ready-made configs (49)](#plugin-collections-frameworks-and-ready-made-configs)

---

## 6. Worktrees and terminal experience

*1333 projects. Git worktree automation, terminal navigation, status displays, HUDs, and developer environment tools.*

### Git worktree automation

*139 projects. Tools that create isolated branches and worktrees for agents, then connect them to Herdr workspaces or tabs.*

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
| [**joshbarrington/jumar**](https://github.com/joshbarrington/jumar) | Lists git worktrees as an editable text buffer where deleting, renaming or adding a line removes, renames or creates a worktree after a review step. Runs as a Herdr plugin in a floating pane with a column for each worktree's agent state and a jump to its Herdr workspace. |
| [**H3xept/herdr-gc**](https://github.com/H3xept/herdr-gc) | Runs your own steps when a git worktree is created, opened, closed or removed in Herdr, each set to run automatically, be suggested or wait for you. An optional classifier decides whether a step applies, for example offering to delete merged checkouts. |
| [**expnn/herdr-plugin-jj-workspace**](https://github.com/expnn/herdr-plugin-jj-workspace) | Creates and removes Jujutsu (jj) workspaces with one keypress, opening each new tab with a coding agent on the left and a terminal on the right. |
| [**codergeek121/herdr-rails**](https://github.com/codergeek121/herdr-rails) | Prepares new Herdr worktrees of Rails apps by running db:prepare and the css and javascript install tasks when cssbundling or jsbundling is present. |
| [**RafaelKC/twig**](https://github.com/RafaelKC/twig) | Creates git worktrees across every repo a task card touches, starts an agent per repo in Herdr and opens a VS Code workspace. One command, `twig new <card>`. |
| [**AdamSiekierski/wtclean**](https://github.com/AdamSiekierski/wtclean) | Removes git worktrees and local branches whose GitHub pull requests were merged, from a CLI, a terminal UI or a Herdr plugin. The plugin sweeps every repo Herdr knows about. |
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
| [**poislagarde/herdr-pr-worktree**](https://github.com/poislagarde/herdr-pr-worktree) | Opens a pasted GitHub pull request URL as a worktree under the matching repository space in Herdr TUI. Reuses existing checkouts with their local commits and changes. |
| [**poislagarde/herdr-worktree-cleanup**](https://github.com/poislagarde/herdr-worktree-cleanup) | Removes disposable files and safe checkouts when a Herdr TUI space closes, and keeps the branch unless a closed or merged PR shows its commits are recoverable. Recreates a deleted checkout when a pane returns after a restart. |
| [**janooh37-hue/hertrees**](https://github.com/janooh37-hue/hertrees) | Lists every git worktree of a project in one popup with its pull request state and running agents. Starts an agent session in an existing or brand-new worktree. |
| [**jiangkoumo/herdr-plugin-layerfs**](https://github.com/jiangkoumo/herdr-plugin-layerfs) | Opens each Herdr TUI workspace as a copy-on-write LayerFS branch of your project. Groups branches under the repo like worktrees and restores them after a restart. |
| [**luizbafilho/herdr-lane**](https://github.com/luizbafilho/herdr-lane) | Opens lane copy-on-write git worktrees as linked workspaces under their repo in Herdr TUI and runs lane lifecycle commands from a popup menu. Removal goes through lane first so its guard on pending notes is kept. |
| [**nickspaargaren/herdr-dog**](https://github.com/nickspaargaren/herdr-dog) | Runs project-defined setup commands from a .herdr/worktrees.yml file after Herdr TUI creates a worktree. Ships as a Go binary with example configs for Node and Postgres. |
| [**LucasPcq/herdr-wtm**](https://github.com/LucasPcq/herdr-wtm) | Runs wtm worktree commands from a Herdr TUI popup and keeps workspaces in sync with worktrees created or removed anywhere. Shows a notification when an on_create hook fails. |
| [**ludoroo/forestr**](https://github.com/ludoroo/forestr) | Lists, opens, creates, and safely removes git worktrees across every repo Herdr TUI knows, from one fzf popup. |
| [**Tarektouati/herdr-pr-modal**](https://github.com/Tarektouati/herdr-pr-modal) | Lists open GitHub pull requests or GitLab merge requests in a popup and opens the chosen one in its own git worktree as a Herdr workspace. |
| [**hlouis/herdr-glab**](https://github.com/hlouis/herdr-glab) | Adds a GitLab merge request panel to Herdr TUI with worktree checkout, review launch, sidebar status and a tab bar count. Uses the glab CLI and never handles a token itself. |
| [**hrudek/herdr-better-worktrees**](https://github.com/hrudek/herdr-better-worktrees) | Opens a popup in Herdr TUI to create, clone, open and inspect git worktrees in an embedded-bare layout where all checkouts live under one repo root. |
| [**SpaceK33z/herdr-worktrees**](https://github.com/SpaceK33z/herdr-worktrees) | Opens a fuzzy picker in Herdr TUI that switches between branches, pull requests and worktrees, and creates or removes worktrees. |
| [**cirdes/herdr-reviewq**](https://github.com/cirdes/herdr-reviewq) | Creates a git worktree and Herdr workspace for each GitHub pull request that requests your review, runs the repo setup commands and removes the worktree after the PR leaves your queue. Adds a Herdr TUI panel with pending reviews, worktree state and CI; panel text is in Portuguese. |
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
| [**piesuke/herdr-worktree-bootstrap**](https://github.com/piesuke/herdr-worktree-bootstrap) | Bootstraps each new Herdr worktree by copying gitignored files like .env, installing dependencies, and running your pre and post commands. |
| [**owpac/herdr-worktrunk**](https://github.com/owpac/herdr-worktrunk) | Gives each task a worktrunk git worktree and its own Herdr workspace, and removes both when the pull request ends. Includes a popup picker and a cleaner for leftovers. |
| [**s3rgiosan/herdr-wp-container**](https://github.com/s3rgiosan/herdr-wp-container) | Gives each Herdr worktree of a WP Container site its own WordPress branch environment, and settles it when the worktree is removed. |
| [**AlphaGodzilla/herdr-plugin-sibling-worktree**](https://github.com/AlphaGodzilla/herdr-plugin-sibling-worktree) | Creates Git worktrees next to the repository instead of under worktrees.directory, naming them from the branch. |
| [**louwers/herdr-submodule-bootstrap**](https://github.com/louwers/herdr-submodule-bootstrap) | Initialises Git submodules in worktrees that Herdr TUI creates, cloning from the main checkout's objects so little needs downloading. |
| [**carandev/herdr-repo-worktrees**](https://github.com/carandev/herdr-repo-worktrees) | Creates Herdr TUI git worktrees at a path inside the repository, by default .claude/worktrees/<branch>, configurable per project. |
| [**jxq0/herdr-worktree-from**](https://github.com/jxq0/herdr-worktree-from) | Opens a Git worktree from a fuzzy-filtered picker of local and remote branches in the Herdr TUI, or creates a new branch from HEAD. |
| [**dorshinar/herdr-worktree-rm**](https://github.com/dorshinar/herdr-worktree-rm) | Deletes a worktree checkout in the background after a confirm popup, with a spinner on the sidebar row, so Herdr TUI does not freeze. |
| [**mpzarde/herdr-hg**](https://github.com/mpzarde/herdr-hg) | Adds Mercurial support to Herdr TUI worktree actions through hg share checkouts and bookmarks, with hg status in the sidebar. Git repos still use the same keys. |
| [**ibedwi/herdr-lifecycle**](https://github.com/ibedwi/herdr-lifecycle) | Runs per-repo setup when a Herdr worktree workspace is created and teardown with safe branch cleanup when it is removed, driven by a small JSON file in each repo. |
| [**Azd325/herdr-treehouse**](https://github.com/Azd325/herdr-treehouse) | Shows the Treehouse worktree slot, state and branch of each workspace on its row in the Herdr TUI sidebar. |
| [**kvoon3/herdr-plugin-worktree-hooks**](https://github.com/kvoon3/herdr-plugin-worktree-hooks) | Runs a repo's herdr-worktree.yaml hooks when a worktree workspace is created, opened or removed, and auto-installs JS dependencies when no config exists. |
| [**tjs0/herdr-repo-worktrees**](https://github.com/tjs0/herdr-repo-worktrees) | Creates and removes git worktrees inside the repo at .worktrees/name and opens each as a worktree workspace grouped under the repo. Needs only bash, git, jq, and Herdr TUI. |
| [**ElliotLuque/herdr-worktree-tools**](https://github.com/ElliotLuque/herdr-worktree-tools) | Opens a Herdr TUI panel that commits unfinished work, merges the selected worktree into the main checkout, and closes its space. Keeps the source branch and pushes nothing. |
| [**marcusjihansson/worktrunk-tui**](https://github.com/marcusjihansson/worktrunk-tui) | Shows a TUI dashboard of worktrunk worktrees for watching agents work, and installs as a Herdr TUI plugin. |
| [**afshimono/symlinkr**](https://github.com/afshimono/symlinkr) | Symlinks gitignored files such as .env and dependency folders from the main checkout into new worktrees. Runs on worktree.created and worktree.opened or from a workspace action. |
| [**rapha4lx/herdr-worktree-stack**](https://github.com/rapha4lx/herdr-worktree-stack) | Mounts an isolated Docker Compose stack when a worktree is created and tears it down when the worktree goes away. |
| [**shved270189/herdr-worktreeinclude-local**](https://github.com/shved270189/herdr-worktreeinclude-local) | Copies gitignored files matching .worktreeinclude and .worktreeinclude.local into every new worktree. |
| [**ruttydm/herdr-espalier**](https://github.com/ruttydm/herdr-espalier) | Runs repo-owned setup and archive scripts when Herdr TUI worktrees are created or removed, read from worktree.yaml or orca.yaml at the repo root. |

### Workspace lifecycle and multi-repository tools

*45 projects. Higher-level utilities for starting, tracking, and removing workspaces that span one or more repositories.*

| Project | What it does |
|---|---|
| [**OliverGilan/herdr-jj**](https://github.com/OliverGilan/herdr-jj) | Adds Jujutsu workspace creation, remote fetching, bookmark setup, live change metadata, and post-create hooks to Herdr. |
| [**jattento/herdr-multirepo**](https://github.com/jattento/herdr-multirepo) | Creates a Herdr TUI workspace containing matching feature-branch worktrees from multiple repositories. |
| [**LoriKarikari/kubeflock**](https://github.com/LoriKarikari/kubeflock) | Creates and connects Kubernetes agent sandboxes to Herdr TUI and manages their lifecycle. |
| [**leoleducq/devflow**](https://github.com/leoleducq/devflow) | Provisions isolated development environments with databases, ports, environment files, and servers, and synchronizes them with Herdr TUI workspaces. |
| [**alon-z/herdr-devup**](https://github.com/alon-z/herdr-devup) | Reads `.herdr/dev.toml` to start a project's tabs, panes, and services, refresh an ngrok URL across configured environment files, and close only the tabs it created. |
| [**nicksenap/grove-herdr**](https://github.com/nicksenap/grove-herdr) | Asks for a name on a key press, runs Grove's gw create and opens the new path as a Herdr workspace. The install script also wires Grove hooks so a Herdr workspace opens and closes with gw create and gw delete. |
| [**dalogax/herdr-agent-hibernate**](https://github.com/dalogax/herdr-agent-hibernate) | Ends idle, unfocused OpenCode, Claude Code and Codex panes to free memory and relaunches the same session with native resume flags when you focus the pane again. |
| [**alexjyong/herdr-codespaces**](https://github.com/alexjyong/herdr-codespaces) | Lists your GitHub Codespaces in a picker and adds the chosen one as a Herdr machine in the sidebar next to local workspaces. |
| [**yoyoyeti/multitrunk-herdr-plugin**](https://github.com/yoyoyeti/multitrunk-herdr-plugin) | Creates and attaches multitrunk task workspaces in Herdr TUI with an agent pane, repository tabs, and interactive popups. |
| [**yavuzhansarmaz/herdr-vps-local**](https://github.com/yavuzhansarmaz/herdr-vps-local) | Mirrors repos from a VPS or Raspberry Pi saved machine to your laptop with Mutagen. Lets you edit in a local IDE while agents keep running on the remote machine. |
| [**Xilis/herdr-plugin-organize**](https://github.com/Xilis/herdr-plugin-organize) | Renames Herdr TUI workspaces after their project folders and groups them by git repository. Handles normal repos, linked worktrees, and bare repos. |
| [**aliaksandr-haurylau-godel/herdr-restart-agents**](https://github.com/aliaksandr-haurylau-godel/herdr-restart-agents) | Restarts coding agents in their Herdr TUI panes and resumes the same session. Restarts one agent or a selected set, optionally updating the agent first. |
| [**bring-shrubbery/herdr-auto-pull-main**](https://github.com/bring-shrubbery/herdr-auto-pull-main) | Fast-forwards the main branch of every repo open in Herdr TUI to its remote on a timer. Skips dirty or diverged branches and logs why. |
| [**chriopter/lazyherd**](https://github.com/chriopter/lazyherd) | Lists every Git repo in one directory with changes and ahead or behind counts, and opens the selected repo in lazygit beside it in a Herdr TUI tab. Adds a cross-repo changes timeline. |
| [**hrudek/herdr-ssh-config-dash**](https://github.com/hrudek/herdr-ssh-config-dash) | Lists host aliases from your ~/.ssh/config in Herdr TUI and lets you add, enable, disable, or remove them as Herdr machines. |
| [**skydiver/herdr-pinned-workspaces**](https://github.com/skydiver/herdr-pinned-workspaces) | Recreates declared workspaces in Herdr TUI when they disappear, in their original sidebar position and at startup. |
| [**joelhooks/herdr-janitor**](https://github.com/joelhooks/herdr-janitor) | Reviews stale Herdr workers and closes eligible panes only after ownership, state, identity, and clean-worktree checks. |
| [**arturodz/dev**](https://github.com/arturodz/dev) | Runs persistent coding workspaces on a Tailscale-connected development VM and reconnects to their Herdr TUI sessions over SSH. |
| [**kody-w/rapp-omarchy**](https://github.com/kody-w/rapp-omarchy) | Combines Herdr terminals, Git worktrees, Tailscale, and RAPP project tools in an Omarchy workbench. |
| [**yordanbuilds/rig**](https://github.com/yordanbuilds/rig) | Starts a project stack in Herdr TUI with configured tabs, panes, and dependent processes. |
| [**andrewdunndev/herdr-estate**](https://github.com/andrewdunndev/herdr-estate) | Tracks long-running campaigns as threads of agent work addressed as estate/campaign, so work outlives each conversation. Agents write a log before a conversation ends and a fresh one picks it up. |
| [**LandonSchropp/herdr-project**](https://github.com/LandonSchropp/herdr-project) | Opens Herdr workspaces and worktrees with preconfigured tabs and commands, in the spirit of tmuxinator. A default project applies to any repository without its own config. |
| [**Runzivo/rzv-herdr-plugin**](https://github.com/Runzivo/rzv-herdr-plugin) | Creates Runzivo cloud sandboxes and adds them to Herdr as machines. Checks status and cost, and sleeps, wakes, or deletes them from Herdr. |
| [**vrwolf1004/herdr-devrun**](https://github.com/vrwolf1004/herdr-devrun) | Starts a project's dev services in separate panes from one dashboard showing status, ports, and recent logs. Adds start, stop, edit, and browser buttons. |
| [**jssda/herdr-tab-autorun-lite**](https://github.com/jssda/herdr-tab-autorun-lite) | Runs a command or starts a coding agent in every new Herdr TUI tab, with rules matched by folder, repo, workspace or tab label. Includes an optional fzf picker. |
| [**prabhatCH/herdr-park**](https://github.com/prabhatCH/herdr-park) | Hibernates idle agent tabs in Herdr TUI to free memory and resumes the exact session later from a searchable picker. |
| [**alexgnq/herdr-workspaces**](https://github.com/alexgnq/herdr-workspaces) | Saves groups of Git repositories as Herdr TUI workspaces and launches Codex, Claude Code, Copilot or Pi with access to all of them. Switches agents in a workspace without repeating the setup. |
| [**favasconcelos/herdr-workspace-template**](https://github.com/favasconcelos/herdr-workspace-template) | Creates a preconfigured set of tabs automatically in every new Herdr TUI workspace, defined in a tabs.json file. |
| [**meta-boy/herdr-shelve**](https://github.com/meta-boy/herdr-shelve) | Keeps only the most recently used agent tabs awake in the Herdr TUI and quits the rest, resuming each agent in the same pane when you focus its tab. Supports Claude Code, Codex and OpenCode. |
| [**MJuma/herdr-copilot-park**](https://github.com/MJuma/herdr-copilot-park) | Parks idle GitHub Copilot CLI tabs in the Herdr TUI to free memory, leaving a small placeholder. Press Enter in the tab to resume the same session. |
| [**iraklisg/herdr-git-sync**](https://github.com/iraklisg/herdr-git-sync) | Fetches every git repo open in your Herdr TUI workspaces, shows what changed upstream, and lets you pick which repos to fast-forward from one popup. |
| [**Delitefully/herdr-auto-claude**](https://github.com/Delitefully/herdr-auto-claude) | Starts Claude Code in the first pane of every new Herdr TUI space while later tabs and splits stay plain shells. |
| [**tedkulp/herdr-kickoff**](https://github.com/tedkulp/herdr-kickoff) | Opens a popup form in the Herdr TUI that creates a workspace from a zoxide directory, a harness, a branch or worktree, and a title, then starts the harness. |
| [**ensi-platform/elc-herdr-plugin**](https://github.com/ensi-platform/elc-herdr-plugin) | Fuzzy-finds ELC components from the Herdr TUI and opens a shell in the component folder as a new pane, tab, or workspace, with elc start, restart, and stop actions. |
| [**ahati/herdr-devcontainer-spaces**](https://github.com/ahati/herdr-devcontainer-spaces) | Detects Docker and Podman devcontainers, creates a Herdr TUI space per container with in-container shells, and shows agents started inside them as Herdr agents. |
| [**ProjectAJ14/herdr-tab-agent**](https://github.com/ProjectAJ14/herdr-tab-agent) | Opens every new Herdr TUI tab straight into a coding agent, Claude Code by default, while the first tab and split panes stay plain shells. |
| [**marvinosswald/herdr-run**](https://github.com/marvinosswald/herdr-run) | Discovers project run commands such as pnpm run dev from config files and runs the chosen or default one in a new Herdr TUI tab. |
| [**harish-zuper/herdr-open-project-with**](https://github.com/harish-zuper/herdr-open-project-with) | Opens the focused Herdr project in Finder, VS Code, IntelliJ IDEA, Android Studio, Xcode, or Terminal from a fuzzy popup. macOS only. |
| [**GODVvVZzz/herdr-workspace-copy**](https://github.com/GODVvVZzz/herdr-workspace-copy) | Copies a workspace folder to a sibling path and opens the copy as a new Herdr workspace, without needing a git worktree. |
| [**echeble/herdr-wayfindr**](https://github.com/echeble/herdr-wayfindr) | Groups scattered repository checkouts, ticket branches, and agent statuses by feature in a sidebar pane, as a list or card grid. |
| [**hrudek/herdr-autofetch**](https://github.com/hrudek/herdr-autofetch) | Runs git fetch on repositories of open workspaces, deduplicating linked worktrees and panes. Never merges or switches branches. |
| [**metcalfc/herdr-exe**](https://github.com/metcalfc/herdr-exe) | Links Herdr TUI workspaces to exe.dev VMs for one-keystroke shells, sidebar VM state, and optional one VM per git worktree. Can lend a VM your Claude subscription and never stops or deletes a VM on its own. |
| [**tmastalirsch/herdr-workspace-board**](https://github.com/tmastalirsch/herdr-workspace-board) | Provides one line per git repository with unfinished work, ranked by how likely it is to be forgotten. |
| [**skinp/herdr-cwd-control**](https://github.com/skinp/herdr-cwd-control) | Provides a herdr plugin for enhanced control over initial working directory for new workspaces, tabs & panes. |
| [**bonanyan/herdr-cwd**](https://github.com/bonanyan/herdr-cwd) | Mirrors the focused Herdr pane's working directory to the host terminal using OSC 7, so file panels, titles, and new splits follow Herdr. |

### Diff review and code inspection

*89 projects. Side-by-side git diff inspection and comment handoff tools for agent reviews.*

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
| [**ExLuna-rs/herdr-git-tree**](https://github.com/ExLuna-rs/herdr-git-tree) | Shows an interactive git graph with colored branch lanes, live diffs and branch management in a Herdr pane. |
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
| [**nolvane/herdr-git-panel**](https://github.com/nolvane/herdr-git-panel) | Lists GitLab merge requests and GitHub pull requests in a Herdr pane, grouped as yours, to review and all open. Uses the installed glab and gh. |
| [**mikhail-angelov/herdr-revdiff**](https://github.com/mikhail-angelov/herdr-revdiff) | Opens revdiff in a full-size Herdr TUI tab with one key. Reviews uncommitted changes on the default branch, or the whole branch against it elsewhere. |
| [**pgen0x/herdr-gitdeck**](https://github.com/pgen0x/herdr-gitdeck) | Reviews diffs across every git repo in a folder, stages or discards hunks, and commits from a Herdr TUI popup. Sends line comments back to the coding agent. |
| [**JTBlink/herdr-work**](https://github.com/JTBlink/herdr-work) | Adds a terminal workbench with a file tree, SCM view, real diffs, staging, and commits for Herdr agents. Saves line-level review comments and sends them back after checking the agent identity. |
| [**Jenish-Shobhit/codeMap**](https://github.com/Jenish-Shobhit/codeMap) | Opens a popup over the agent pane that shows your code as a map and flowcharts. Reviews what coding agents changed in context. |
| [**carlos-anpr/herdr-gitview**](https://github.com/carlos-anpr/herdr-gitview) | Shows a commit graph, diffs, GitHub pull requests, GitLab merge requests, and short AI explanations in a popup over the agent pane. Written in Rust with a Spanish README. |
| [**sjlee06/herdr-git-graph**](https://github.com/sjlee06/herdr-git-graph) | Shows a read-only Git branch and commit graph in the Herdr TUI sidebar. Expands commits to changed files and opens diffs, with a full view for branch filtering. |
| [**winoooops/herdr-hunks**](https://github.com/winoooops/herdr-hunks) | Shows changed files with unified or split diffs in Herdr TUI, with live refresh, hunk staging behind a confirmation, review comments, and dispatch to an agent pane. |
| [**rodeyseijkens/codey**](https://github.com/rodeyseijkens/codey) | Reviews staged and unstaged git diffs with transient line comments, real staging, and a commit log sidebar, beside your agent. Runs standalone or as a Herdr TUI plugin pane. |
| [**sebassdc/herdr-agent-prs**](https://github.com/sebassdc/herdr-agent-prs) | Docks a strip above an agent pane listing every pull request the agent opened or pushed to across repos, with live CI, review, and merge state. |
| [**dkbo/herdr-scm**](https://github.com/dkbo/herdr-scm) | Opens a read-only source-control panel listing every git repo under the current Herdr TUI workspace, with branch, ahead/behind counts, changed files and a diff. |
| [**tareqmlx/herdr-hunk-viewer**](https://github.com/tareqmlx/herdr-hunk-viewer) | Opens Hunk diffs for the current repository from Herdr TUI in a split pane, a tab, an overlay or a popup. |
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
| [**derangga/herdr-review-annotate**](https://github.com/derangga/herdr-review-annotate) | Reviews a diff in a Herdr pane, lets you comment on lines, and sends the comments to Claude Code. Installs a prebuilt binary with checksum verification. |
| [**alexeyco/herdr-git**](https://github.com/alexeyco/herdr-git) | Opens gitui or lazygit in a Herdr pane and reports to the agent what you changed after you quit. Detects which Git TUI is installed. |
| [**Zeppelinpp/herdr-git-panel**](https://github.com/Zeppelinpp/herdr-git-panel) | Adds a Git sidebar to Herdr with searchable branches, working-tree diffs, a commit graph, and GitHub or GitLab merge requests. Sends selected diff lines to an agent pane. |
| [**andpeicunha/herdr-spec-review**](https://github.com/andpeicunha/herdr-spec-review) | Reviews OpenSpec artifacts block by block in a terminal reader and lets you leave AI Notes the agent turns into spec changes. Finds open changes across git worktrees. |
| [**NaturaAurum/herdr-gh-view**](https://github.com/NaturaAurum/herdr-gh-view) | Opens a right-side panel with the focused branch's GitHub pull request, stack, CI checks, and unresolved review comments. |
| [**TarasKovalenko/herdiff**](https://github.com/TarasKovalenko/herdiff) | Shows a live, syntax-highlighted diff of every git repo your Herdr TUI panes sit in, grouped by repo. Runs as a Rust terminal UI in a side pane. |
| [**inkayat/firstpane**](https://github.com/inkayat/firstpane) | Opens a Herdr TUI pane that groups agents by project and shows each one's workspace changes and PR in a Review tab with numbered diffs. Adds a shell in the agent's directory and a browser. |
| [**KnobleChipmunk/collie**](https://github.com/KnobleChipmunk/collie) | Opens a pane beside an agent in the Herdr TUI that renders the exact lines or diff the agent refers to, highlighted with bat and delta. |
| [**kalebhenrique/herdr-interactive-diff**](https://github.com/kalebhenrique/herdr-interactive-diff) | Shows an interactive git diff and artifact viewer in Herdr TUI that opens AI agent splits for multi-lens reviews. Built in Rust with ratatui. |
| [**panuhorsmalahti/herdr-command-center**](https://github.com/panuhorsmalahti/herdr-command-center) | Opens a Herdr TUI pane that lists your open pull requests with their checks, review state, and merge conflicts marked. |
| [**doominkim/herdr-jest**](https://github.com/doominkim/herdr-jest) | Opens a Jest test explorer popup in Herdr TUI to browse the test tree, run a folder, file, or single test, and read failures with their source lines. The README marks it as in development. |
| [**zenodea/graphdiff**](https://github.com/zenodea/graphdiff) | Opens a live browser map of a repository's changes from a Herdr TUI pane, showing touched folders, change size, and dependencies between them. |
| [**odiumuniverse/herdr-diff-viewer**](https://github.com/odiumuniverse/herdr-diff-viewer) | Opens a git diff sidebar in the Herdr TUI that lists changed files with red and green hunks scoped to the agent session. Click jumps to a file and dragging sends lines into the agent prompt. |
| [**ekropotin/herdr-tuicr**](https://github.com/ekropotin/herdr-tuicr) | Runs tuicr code review in a Herdr TUI split pane and sends the finished review back to the agent pane that opened it. |
| [**YmlyZA/herdr-review-pack**](https://github.com/YmlyZA/herdr-review-pack) | Collects a task brief, the current Git diff, and command check receipts in a Herdr TUI review panel, marking receipts stale when code changes afterwards. |
| [**Allianaab2m/herdr-hunk-gh-diff**](https://github.com/Allianaab2m/herdr-hunk-gh-diff) | Opens a Hunk diff in a Herdr TUI split or tab between the current branch and the base branch of its GitHub pull request, found through gh. |
| [**simosako/herdr-annotate-opencode**](https://github.com/simosako/herdr-annotate-opencode) | Opens Herdr Annotate's document review at the current OpenCode session directory instead of the pane's original working directory. |

### File viewers, terminal browsers, and markdown previews

*81 projects. In-terminal file viewers, interactive web browsers, image previews, and markdown rendering panes.*

| Project | What it does |
|---|---|
| [**zenbu-labs/terminal-browser · herdr-plugin**](https://github.com/zenbu-labs/terminal-browser/tree/main/herdr-plugin) | Opens a terminal browser beside a Herdr TUI pane and supports agent-driven browser interaction. |
| [**smarzban/herdr-file-viewer**](https://github.com/smarzban/herdr-file-viewer) | Opens a read-only file viewer in a Herdr TUI split with Git status, diffs, Markdown, and source previews. |
| [**alexarthurs/herdr-sidebar**](https://github.com/alexarthurs/herdr-sidebar) | Opens a dockable file explorer and source-control panel with previews and AI-drafted commit messages in Herdr TUI. |
| [**ogulcancelik/herdr-browser**](https://github.com/ogulcancelik/herdr-browser) | Renders an interactive Chromium browser inside a Herdr pane and lets agents automate it through Chrome DevTools Protocol. The project is deprecated in favor of terminal-browser. |
| [**iurysza/termscope**](https://github.com/iurysza/termscope) | Finds visible file paths and web links on the terminal screen, lets the user select one with fuzzy search, and opens it in a separate split without disturbing the main pane. |
| [**speardragon/herdr-yazi**](https://github.com/speardragon/herdr-yazi) | Opens the Yazi file manager in a Herdr pane or tab at the current directory while reusing the user's existing Yazi configuration. |
| [**StructuPath/herdr-browser**](https://github.com/StructuPath/herdr-browser) | Opens a drivable Chromium browser in a Herdr pane for agent automation and manual inspection. |
| [**alexarthurs/herdr-notes**](https://github.com/alexarthurs/herdr-notes) | Keeps one persistent Markdown note per workspace, with rendered and edit modes, autosave, and restoration after restarts. |
| [**dwarvesf/herdr-quicklook**](https://github.com/dwarvesf/herdr-quicklook) | Previews a file path from the clipboard in an overlay and can expand it into a full terminal viewer, avoiding manual path entry or temporary splits. |
| [**slara/terminal-markdown-renderer**](https://github.com/slara/terminal-markdown-renderer) | Opens rendered Markdown in a terminal browser from a Herdr TUI plugin. |
| [**MattJColes/herdr-web-browser**](https://github.com/MattJColes/herdr-web-browser) | Opens browser previews beside coding agents in Herdr and shares console errors, network requests, screenshots, and selected page content. |
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
| [**g00rek/browsr**](https://github.com/g00rek/browsr) | Keeps a dedicated Chromium tab group for each Herdr workspace so the browser follows the workspace you switch to. Agents in a pane open pages in their own workspace group, and a Herdr panel shows what the browser is doing; Linux only. |
| [**salamituns/herdr-browser**](https://github.com/salamituns/herdr-browser) | Shows the Chrome that Claude Code, Codex, Cursor, Droid or Antigravity drive through chrome-devtools-mcp or Playwright MCP in a Herdr pane beside the agent. You can click and type into the same page, and agents keep their existing browser tools. |
| [**worldnine/ashiato**](https://github.com/worldnine/ashiato) | Browses recently modified files with a terminal picker and uses the Herdr TUI worktree or workspace directory when available. |
| [**aclima01/herdr-edit-windows**](https://github.com/aclima01/herdr-edit-windows) | Opens a Windows text editor in a Herdr split with a directory tree, syntax highlighting, and an uncommitted-diff tab. |
| [**cyperx84/herdr-notes**](https://github.com/cyperx84/herdr-notes) | Creates a separate Markdown scratchpad for each Herdr workspace ID. Notes and prompt drafts open in a side split and stay outside the Git working tree. |
| [**gcaudan/herdr-explorer**](https://github.com/gcaudan/herdr-explorer) | Adds a VS Code-style file explorer, preview, diff, and source-control panes beside your agents. Review notes on diff lines go into the agent's prompt, and the agent can open `file:line` in the preview through a bundled skill. |
| [**pjs-0457/herdr-yazi-explorer**](https://github.com/pjs-0457/herdr-yazi-explorer) | Opens Yazi in a labelled Herdr tab or split at the workspace directory and relaunches it automatically after exit. |
| [**jellespijker/herdr-diagrams**](https://github.com/jellespijker/herdr-diagrams) | Renders Mermaid, PlantUML, Structurizr, D2, and Graphviz diagrams from coding agents as images in a split pane. Uses the Kitty graphics protocol and works with Claude Code, Codex, opencode, and other agents that run shell commands. |
| [**kamil-pociot/herdr-vista**](https://github.com/kamil-pociot/herdr-vista) | Opens the vista terminal file viewer and editor on the current git repo with one key in Herdr TUI. Another key reviews what an agent changed on its branch. |
| [**Freddy-system/file-editor-viewer**](https://github.com/Freddy-system/file-editor-viewer) | Views and edits files in a Herdr pane, rendering Markdown with Mermaid, Graphviz, and LaTeX, highlighting source code, and showing images. Also runs standalone as the fev command. |
| [**mvaios/herdr-scratchdock**](https://github.com/mvaios/herdr-scratchdock) | Docks a Claude Code agent's scratchpad folder in a split beside it in Herdr TUI, with a live tree and text and image previews. |
| [**maynewong/terminal-browser-relay**](https://github.com/maynewong/terminal-browser-relay) | Throttles and downsizes terminal-browser frames so the browser stays usable in a Herdr TUI pane on a remote machine over SSH. |
| [**shindakun/herdr-knapp**](https://github.com/shindakun/herdr-knapp) | Browses a directory of Markdown notes in a Herdr TUI pane, following wikilinks and showing backlinks, broken links, orphans and a local link graph. |
| [**tim80411/herdr-pdf**](https://github.com/tim80411/herdr-pdf) | Renders PDF pages into a Herdr TUI split pane through the pane graphics stream. Ctrl+click a .pdf path in any pane to open it. |
| [**natori-hrj/herdr-docs**](https://github.com/natori-hrj/herdr-docs) | Opens Markdown, PDF and office documents in a consistent reader pane inside Herdr TUI. |
| [**harshagowda/herdr-web**](https://github.com/harshagowda/herdr-web) | Adds a real Chromium web tab over a Herdr pane on macOS that hides when you switch tabs. Every browser can be driven over the Chrome DevTools Protocol, for example with Playwright. |
| [**azihsoyn/herdfold**](https://github.com/azihsoyn/herdfold) | Reads Markdown, EPUB, diffs and other long text as facing pages split across two Herdr panes, with a shelf of books, bookmarks, notes, search and an ask-the-agent key. Shows one page at a time outside Herdr. |
| [**saborrie/grove**](https://github.com/saborrie/grove) | Shows a file tree pinned to one root with live code and image previews in a single Herdr pane. Draws images through Herdr's pane graphics API. |
| [**redsquiggle/herdr-browser**](https://github.com/redsquiggle/herdr-browser) | Keeps Chromium tab groups aligned with Herdr workspaces. |
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
| [**optioni/herdr-openspec**](https://github.com/optioni/herdr-openspec) | Shows a read-only OpenSpec dashboard in a Herdr TUI pane with changes, their artifacts and task progress. Sits beside your agents. |
| [**hamzahraihan/herdr-git-tab**](https://github.com/hamzahraihan/herdr-git-tab) | Opens a Herdr TUI tab with a GitHub terminal UI that shows seven panes in one view. |
| [**fsi044689/herdr-quickview**](https://github.com/fsi044689/herdr-quickview) | Highlights file paths and URLs visible in a Herdr TUI pane and opens a preview with macOS Quick Look or an in-place text or image popup. |
| [**quocdaijr/herdr-open-file**](https://github.com/quocdaijr/herdr-open-file) | Opens a file path Ctrl-clicked in a Herdr TUI pane in your editor at the given line and column, with Zed as the default. |
| [**rcosteira79/herdr-dock**](https://github.com/rcosteira79/herdr-dock) | Adds a per-tab right-hand dock in the Herdr TUI with a git-aware file Explorer and a Processes list of the subagents and shells of the tab's agents. |
| [**TGGgbone/herdr-show-image**](https://github.com/TGGgbone/herdr-show-image) | Lets agents add images to a gallery over MCP and write a link. Ctrl-click opens a side pane in the Herdr TUI that pages through the images using the Kitty graphics protocol. |
| [**Zeus-Deus/herdr-peek**](https://github.com/Zeus-Deus/herdr-peek) | Opens any file an agent mentions in a split with one key, including images, video, PDFs, documents and code, and works across connected machines. |
| [**yiju-zhao/herdr-lens**](https://github.com/yiju-zhao/herdr-lens) | Previews files that Claude Code, Codex or any terminal agent mentions in a read-only Herdr TUI pane. Resolves absolute, relative and file:// paths against the source pane. |
| [**zbyhoo/herdr-image-gallery**](https://github.com/zbyhoo/herdr-image-gallery) | Shows AI-generated images, screenshots, and image folders as a thumbnail grid with a larger preview in a Herdr TUI pane. Includes a Codex and Claude Code skill that sends generated images to the gallery. |
| [**dynaum/maidog**](https://github.com/dynaum/maidog) | Draws Mermaid diagrams as Unicode box art in the terminal. Its Herdr TUI plugin sets up herdr-file-viewer to show diagrams in Markdown files. |
| [**dlv-gold/herdr-md**](https://github.com/dlv-gold/herdr-md) | Opens Markdown files in a Herdr TUI split with live refresh, rendered LaTeX equations, and local PNG figures. Also runs as a standalone viewer in Kitty. |
| [**ezoushen/herdr-plugins · browser-trigger**](https://github.com/ezoushen/herdr-plugins/tree/main/browser-trigger) | Opens HTTP and HTTPS links from Herdr TUI panes in a browser split using the separately installed terminal-browser executable. |
| [**suzuki-junya108/view-and-edit-herdr-plugin**](https://github.com/suzuki-junya108/view-and-edit-herdr-plugin) | Previews, edits, and browses files in a Herdr popup, including Markdown, HTML, images, video, audio, PDF, Office documents, CSV/JSON, and SQLite. macOS only with a Japanese interface. |
| [**WerrySs/herdr-graphical-apps**](https://github.com/WerrySs/herdr-graphical-apps) | Launches graphical terminal apps inside Herdr TUI splits, tabs, and overlays from an app picker. Includes web link opening, graphics diagnostics, and a colour test page. |
| [**Clementtang/herdr-shelf**](https://github.com/Clementtang/herdr-shelf) | Adds a Herdr TUI sidebar that lists every file a Claude Code session sent to you, newest first, and opens each one with a click. Reads the session transcript so files stay listed after they scroll off screen. |
| [**hellower/herdr-plugin-parallax**](https://github.com/hellower/herdr-plugin-parallax) | Opens URLs from Herdr terminal panes in the Parallax browser. |

### Pane navigation and overlay hints

*60 projects. Direct 1-character overlay hints and smart directional pane jumping.*

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
| [**eisenhauer-dev/herdr-crossroads**](https://github.com/eisenhauer-dev/herdr-crossroads) | Searches panes, tabs, workspaces and agent names and focuses the one you pick in Herdr TUI, with linked worktrees grouped beside their workspace. Navigation only: it never creates, moves, renames or deletes anything. |
| [**jeiea/herdr-grid-slide**](https://github.com/jeiea/herdr-grid-slide) | Focuses and moves panes with hjkl-style actions in Herdr TUI, wrapping to the neighboring tab or workspace at an edge. Moving a pane across an edge carries it into the next tab or workspace. |
| [**mcostasilva/herdr-marks**](https://github.com/mcostasilva/herdr-marks) | Marks panes with letters a-z and workspaces with A-Z, jumps back to them by key, and shows the letter as a colored label in the sidebar. |
| [**reobin/herdr-link-hints**](https://github.com/reobin/herdr-link-hints) | Opens a popup that lists every link on screen in Herdr so you can open or copy one with the keyboard. Needs Herdr 0.9.2 or newer. |
| [**reobin/herdr-callsigns**](https://github.com/reobin/herdr-callsigns) | Names every Herdr pane with a short callsign such as neon or mars so you and your agent can refer to panes by name. Installs a skill that resolves callsigns to pane IDs. |
| [**enisbu/herdr-swipe-linux**](https://github.com/enisbu/herdr-swipe-linux) | Adds Linux touchpad gestures for navigating Herdr TUI panes, tabs, and spaces and focusing agents awaiting attention. |
| [**42lizard/herdr-dwm-layout**](https://github.com/42lizard/herdr-dwm-layout) | Rearranges existing Herdr TUI panes into DWM-style master and stack layouts without restarting their processes. |
| [**shadowfax92/herdr-beacon**](https://github.com/shadowfax92/herdr-beacon) | Jumps to unread, working, or recently active agents using Herdr TUI status and sidebar indicators. |
| [**youguanxinqing/herdr-hop**](https://github.com/youguanxinqing/herdr-hop) | Jumps to any visible Herdr pane by pressing a labeled key. |
| [**KadenThomp36/herdr-plugin-switcher**](https://github.com/KadenThomp36/herdr-plugin-switcher) | Cycles through recently used Herdr TUI panes with Ctrl-Tab on macOS. |
| [**maedana/herdr-hint**](https://github.com/maedana/herdr-hint) | Displays Vimium-style single-letter labels over active tabs and agent panes so focus can jump directly to a target without cycling through the layout. |
| [**RooseveltAdvisors/herdr-leap**](https://github.com/RooseveltAdvisors/herdr-leap) | Jumps to visible word starts in Herdr TUI copy mode and adds Vim- and fzf-aware pane navigation. |
| [**qcklex/herdr-spring-load**](https://github.com/qcklex/herdr-spring-load) | Switches Herdr Spaces, tabs, and panes while you hold a dragged file over them, then drops the file in place. Works in Ghostty on macOS, with only pane focus in Terminal.app. |
| [**abroller666/herdr-display-panes**](https://github.com/abroller666/herdr-display-panes) | Brings tmux display-panes to Herdr TUI by labeling every pane in the current tab with a one-key shortcut. Pressing a label focuses that pane. |
| [**killallgit/herdr-alt-tab**](https://github.com/killallgit/herdr-alt-tab) | Cycles through Herdr TUI panes in most-recently-used order with alt+tab and shift+alt+tab. Installs a prebuilt binary and has no options. |
| [**RodrigoEspinosa/herdr-tab-flow**](https://github.com/RodrigoEspinosa/herdr-tab-flow) | Adds next and previous tab actions to Herdr TUI that continue across spaces and wrap around, instead of stopping at the space edge. |
| [**raghu-nandan-bs/herdr-deck-navigation**](https://github.com/raghu-nandan-bs/herdr-deck-navigation) | Opens a workspace and pane navigator for Herdr TUI that walks an attention queue of blocked agents first, then agents that finished unseen. |
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
| [**bagonyi/herdr-file-links**](https://github.com/bagonyi/herdr-file-links) | Opens file links on Ctrl+click in a Herdr pane, such as links printed by ripgrep, delta, ls, or Claude Code. Only safe file types open directly. |
| [**CodeForBreakfast/herdr-pane-links**](https://github.com/CodeForBreakfast/herdr-pane-links) | Focuses a Herdr TUI pane when you Ctrl-click a herdr.invalid pane link. Lets an agent hand you a link to its own pane instead of written directions. |
| [**riogesulgon/herdr-history**](https://github.com/riogesulgon/herdr-history) | Opens a popup that lists panes from every workspace, most recently focused first, with a live preview, and jumps to the one you pick. Works like back history for Herdr TUI panes. |
| [**PascalKraupner/herdr-urlview**](https://github.com/PascalKraupner/herdr-urlview) | Picks, opens and copies URLs from the focused Herdr TUI pane with an fzf picker, newest first and without duplicates. |
| [**justmytwospence/herdr-repeat-navigation**](https://github.com/justmytwospence/herdr-repeat-navigation) | Adds tmux-style timed navigation repeat to Herdr TUI through a client companion that wraps the interactive client's input. Needs a terminal with enhanced keyboard reporting. |
| [**dima-m711/herdr-links**](https://github.com/dima-m711/herdr-links) | Creates session-bound OSC 8 links that jump to Herdr TUI agents, workspaces, tabs and panes. Built for reports written by Pi agents, and any terminal program can print the links. |
| [**kuzco77/herdr-ids**](https://github.com/kuzco77/herdr-ids) | Opens a popup listing the workspace, tab, pane and agent ids of the focused pane in Herdr TUI, and copies the one you pick by number. |
| [**alikayhan/herdr-pane-id-labels**](https://github.com/alikayhan/herdr-pane-id-labels) | Shows each pane's Herdr ID in its border title and copies it with a keybinding, so you can hand an ID to an agent that talks to another pane. |
| [**neilellis/herdr-pane-history**](https://github.com/neilellis/herdr-pane-history) | Adds browser-style back and forward through recently focused panes in Herdr TUI, across tabs and workspaces, with a history list. |
| [**Realtyxxx/herdr-pane-id-tagger**](https://github.com/Realtyxxx/herdr-pane-id-tagger) | Tags Herdr TUI panes and workspaces with their pane and space IDs in the sidebar, so you can point an agent at another pane. |
| [**hosikiti/herdr-open-links**](https://github.com/hosikiti/herdr-open-links) | Lists the web links, file URLs, and wrapped paths in a Herdr TUI pane and opens the one you pick, including URLs that wrap across lines. |
| [**pglira/herdr-image-hints**](https://github.com/pglira/herdr-image-hints) | Puts one-key hints over image paths in a Herdr TUI pane and shows the chosen image in a popup through the Kitty graphics protocol. |
| [**FjedorGaede/herdr-focus-history**](https://github.com/FjedorGaede/herdr-focus-history) | Adds a Vim-style back and forward jumplist over workspace and agent focus history in the Herdr TUI. The author flags it as early and tested on Linux with herdr 0.9.1. |
| [**shunia/herdr-pane-index**](https://github.com/shunia/herdr-pane-index) | Labels each pane's top border with its workspace, tab, and pane index while keeping the existing title. |
| [**julianbonomini/herdr-agent-nav**](https://github.com/julianbonomini/herdr-agent-nav) | Adds an active-agent picker that groups agents by space and jumps to the exact pane, plus a prompt to rename the focused agent. For Herdr TUI 0.9 and newer. |
| [**k-narusawa/herdr-last-tab**](https://github.com/k-narusawa/herdr-last-tab) | Jumps back to the previously focused Herdr TUI tab across workspaces, like tmux last-window. Needs jq. |
| [**calorie/herdr-auto-focus**](https://github.com/calorie/herdr-auto-focus) | Focuses the Herdr agent needing attention after the computer has been idle. |

### Pane layout management

*44 projects. Tools that arrange, resize, and manage Herdr TUI panes.*

| Project | What it does |
|---|---|
| [**thuanlm215/herdr-grid**](https://github.com/thuanlm215/herdr-grid) | Opens a visual editor for dragging, resizing, and safely rearranging live pane layouts without restarting pane processes. It can add shell panes, apply fixed presets, or build a preset in a new workspace. |
| [**osamahbeig/herdr-pane-mover**](https://github.com/osamahbeig/herdr-pane-mover) | Moves, re-splits, and swaps Herdr panes through a clickable overlay. |
| [**shibayu36/herdr-equalize-panes**](https://github.com/shibayu36/herdr-equalize-panes) | Automatically equalizes Herdr TUI panes after splits and closures, with an optional manual action. |
| [**iurysza/herdr-pane-layouts**](https://github.com/iurysza/herdr-pane-layouts) | Adds tmux-style pane resizing and layouts to Herdr. |
| [**edouard-andrei/herdr-layout-tools**](https://github.com/edouard-andrei/herdr-layout-tools) | Rearranges existing panes into main-left, grid, or equalized presets without changing pane IDs, tab IDs, or running processes. |
| [**crierr/herdr-tmux-layout**](https://github.com/crierr/herdr-tmux-layout) | Adds tmux-style layout presets for Herdr, including even horizontal, even vertical, main horizontal, main vertical, tiled, cycle, and balance. |
| [**iuhoay/herdr-break-pane**](https://github.com/iuhoay/herdr-break-pane) | Moves the active pane into a new tab while preserving its process, similar to tmux break-pane. It unzooms complex tabs first and leaves single-pane tabs unchanged. |
| [**federbenjamin/herdr-undo-close**](https://github.com/federbenjamin/herdr-undo-close) | Reopens the pane you just closed in Herdr in the same split, with its old scrollback above a fresh prompt. A Claude Code pane resumes its conversation, and a command that was running returns typed but not run. |
| [**orcchg/herdr-topstrip**](https://github.com/orcchg/herdr-topstrip) | Opens every new tab and space as a narrow top shell strip over a wide work pane, and relaunches the strip if you close it. |
| [**ponko2/herdr-equalize-panes**](https://github.com/ponko2/herdr-equalize-panes) | Automatically equalizes Herdr TUI pane sizes when panes are created, closed, moved, or exit, with an on-demand action. |
| [**carsonjones/herdr-plugin-tiles**](https://github.com/carsonjones/herdr-plugin-tiles) | Adds named split ratios: 60/40 and 40/60 horizontal, 20/80 and 80/20 vertical, plus 50/50 resets. Modifier keys flip the larger side or return to equal sizing. |
| [**willfish/herdr-balance-panes**](https://github.com/willfish/herdr-balance-panes) | Equalizes all panes in the active tab with one key, reproducing tmux `select-layout -E` behavior after repeated splits or resizing. |
| [**jone/herdr-wrangler**](https://github.com/jone/herdr-wrangler) | Adds tmux-style pane layouts and rotation to Herdr. |
| [**Jenish-Shobhit/paneMorph**](https://github.com/Jenish-Shobhit/paneMorph) | Moves live panes between tabs and spaces in Herdr TUI without restarting their processes. Sends a pane anywhere, fetches one here, and undoes any move. |
| [**dimitri4d/herdr-pane-mover**](https://github.com/dimitri4d/herdr-pane-mover) | Moves a running Herdr TUI pane to another tab or workspace through a Workspace, Tab, Pane tree picker. Works with keyboard and mouse and keeps the process alive. |
| [**jaeheonji/herdr-tiling**](https://github.com/jaeheonji/herdr-tiling) | Adds Hyprland-style directional pane movement, split toggling, and tmux-style preset layouts to Herdr TUI. Keeps running processes and scrollback. |
| [**iancharters/herdr-drawer**](https://github.com/iancharters/herdr-drawer) | Toggles a persistent multi-pane bottom terminal drawer in Herdr TUI with Ctrl+/ from Neovim or any pane. Keeps sibling panes unzoomed and visible. |
| [**Rocket-Monsters/herdr-layout**](https://github.com/Rocket-Monsters/herdr-layout) | Opens every new Herdr TUI worktree with panes split and commands running, as defined in a .herdr-layout file at the project root. Works on macOS, Linux, and Windows. |
| [**y4le/herdr-mark**](https://github.com/y4le/herdr-mark) | Marks a pane in Herdr TUI, then joins it beside another pane or swaps the two, like tmux select-pane -m with join-pane and swap-pane. |
| [**RodrigoEspinosa/herdr-agent-panes**](https://github.com/RodrigoEspinosa/herdr-agent-panes) | Sends agents' dev servers and watchers to visible Herdr panes, reusing a pane already running the same command. Ships as a Herdr plugin and Claude Code hook. |
| [**ariel-ps/herdr-layouts**](https://github.com/ariel-ps/herdr-layouts) | Saves and restores Herdr pane layouts and creates grids of coding agents. Adds commands such as herdr-layout-save, herdr-layout-up, and herdr-grid-agents, and opens code, board, and lazygit tabs in new workspaces. |
| [**yuloop/herdr-plugin-pane-move**](https://github.com/yuloop/herdr-plugin-pane-move) | Moves and rearranges Herdr panes across tabs using keyboard shortcuts. |
| [**andpeicunha/herdr-smart-focus**](https://github.com/andpeicunha/herdr-smart-focus) | Grows the focused pane to about 70 percent along its splits, with optional stack layouts. Beta. |
| [**m16khb-org/herdr-powertoys**](https://github.com/m16khb-org/herdr-powertoys) | Equalizes split panes in a tab, snaps a split to half, or cycles it through 1/2, 2/3, and 1/3 with one key. |
| [**cremarch/herdr-select-layout**](https://github.com/cremarch/herdr-select-layout) | Rearranges a tab's panes into even, main, or tiled layouts with one key, like tmux select-layout. |
| [**MMSs/herdr-minimize**](https://github.com/MMSs/herdr-minimize) | Minimizes a Herdr TUI pane to a clickable tray and restores it to its exact position and size without stopping its process. |
| [**shrwnsan/herdr-herder**](https://github.com/shrwnsan/herdr-herder) | Adds a Herdr TUI picker that moves a pane or tab to another place and an action that evens pane widths and heights. |
| [**vrwolf1004/herdr-dock-grid**](https://github.com/vrwolf1004/herdr-dock-grid) | Keeps a shared 2x2 pane grid for dock-style panes in Herdr TUI and tracks which slot each dock plugin uses. Includes commands to list, reconcile, reset and snapshot the dock layout. |
| [**coryfklein/herdr-layout**](https://github.com/coryfklein/herdr-layout) | Gives a Herdr TUI pane a readable width in character columns by adding margin panes around it. Keeps the width and alignment per pane after resizes. |
| [**filipecsweb/herdr-plugins**](https://github.com/filipecsweb/herdr-plugins) | Equalizes the width or height of the panes in the current Herdr TUI tab from one keybinding. Ships as the pane-equalize plugin in a folder-per-plugin repo. |
| [**jorgeraad/herdr-layouts**](https://github.com/jorgeraad/herdr-layouts) | Applies tmux preset layouts such as even-horizontal, main-vertical, and tiled to the panes of the current Herdr TUI tab without restarting them. |
| [**Unayung/herdr-pane-pull**](https://github.com/Unayung/herdr-pane-pull) | Pulls marked panes from any workspace into the current Herdr TUI tab and sends one back out, keeping agents and shells running. |
| [**saiyajosh/herdr-schlepr**](https://github.com/saiyajosh/herdr-schlepr) | Moves live panes and whole tabs between Herdr TUI workspaces from a keyboard-driven popup, choosing the destination pane, split direction, and ratio. |
| [**dalogax/herdr-agent-board**](https://github.com/dalogax/herdr-agent-board) | Tiles every working, waiting, or recently active agent into one board workspace of live panes with one key, and restores them with another. Works with Claude Code, Codex, OpenCode, and any agent Herdr detects. |
| [**JordanBelfort1/herdr-pane-tools**](https://github.com/JordanBelfort1/herdr-pane-tools) | Moves a running pane into another tab as a split through a keyboard and mouse menu, without restarting the session. Windows only. |
| [**0xtiby/herdr-grid-picker**](https://github.com/0xtiby/herdr-grid-picker) | Splits the focused pane into an equal R by C grid chosen from a popup, from 1x2 to 4x6, and can pre-load an agent CLI in each pane. Also has a close-others entry. |
| [**mcostasilva/herdr-smart-split**](https://github.com/mcostasilva/herdr-smart-split) | Splits the focused pane right when it is wide and down when it is tall, and focuses the new pane by default. |
| [**master-g/herdr-panes**](https://github.com/master-g/herdr-panes) | Adds dwindle-style splitting, a master layout, pane promotion, equalizing, and master-width actions while preserving pane geometry. |
| [**wyattjoh/herdr-plugin-move**](https://github.com/wyattjoh/herdr-plugin-move) | Moves the focused Herdr TUI pane to another workspace and tab chosen from a searchable popup. |
| [**dimapanov/herdr-equalize**](https://github.com/dimapanov/herdr-equalize) | Equalizes Herdr TUI split ratios so every pane in a tab gets the same share, on demand or automatically when a pane opens or closes. |
| [**atm028/herdr-panes**](https://github.com/atm028/herdr-panes) | Swaps the active Herdr TUI pane with its neighbor, rotates panes, and applies tmux-style layouts such as even-horizontal, main-vertical, tiled, and golden-ratio from a popup picker. |
| [**macintacos/herdr-reshape**](https://github.com/macintacos/herdr-reshape) | Moves the focused pane around its tab and arranges panes into an even grid. |
| [**shanefully-done/herdr-pane-equalizer**](https://github.com/shanefully-done/herdr-pane-equalizer) | Equalizes Herdr TUI pane dimensions automatically or through manual width and height actions. |
| [**choplin/herdr-split-pane**](https://github.com/choplin/herdr-split-pane) | Opens a caller-provided command directly in a Herdr split pane. |

### Terminal keybindings and shortcut helpers

*88 projects. Custom keymap packs, leader-key setups, and prefix-free navigation.*

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
| [**kamaaina/herdr_sync**](https://github.com/kamaaina/herdr_sync) | Sends the command currently typed in one pane to every other pane in the same tab, providing synchronized-pane behavior for Herdr. |
| [**furuhashin/herdr-synchronize-panes**](https://github.com/furuhashin/herdr-synchronize-panes) | Broadcasts one command to every pane in the current tab, providing a shell-based equivalent of tmux synchronized panes. |
| [**itsmistermoon/bindr**](https://github.com/itsmistermoon/bindr) | Switches between named keybinding profiles and lets users view and edit bindings in a popup. |
| [**JacquesvanWyk/herdr-keys**](https://github.com/JacquesvanWyk/herdr-keys) | Searches keybindings with an fzf cheatsheet and discovers bindings from local configuration files. |
| [**aorumbayev/herdr-hyprland**](https://github.com/aorumbayev/herdr-hyprland) | Adds Hyprland-inspired shortcuts for navigating and manipulating Herdr TUI panes, tabs, and workspaces. |
| [**cyperx84/herdr-tab-jump**](https://github.com/cyperx84/herdr-tab-jump) | Focuses Herdr tab N by position from custom keybindings, splitting the number row between tabs and workspaces. |
| [**pedrobarco/herdr-lastfocus**](https://github.com/pedrobarco/herdr-lastfocus) | Toggles between recently focused Herdr TUI panes, tabs, or workspaces using focus-event history. |
| [**dantehemerson/herdr-last-tab**](https://github.com/dantehemerson/herdr-last-tab) | Tracks tab focus history and returns to the previously active Herdr tab with one keystroke. |
| [**jugyo/herdr-nav-history**](https://github.com/jugyo/herdr-nav-history) | Adds browser-style back and forward navigation across panes, tabs, and workspaces by recording focus changes from the Herdr socket event stream. |
| [**retroaalto/herdr-smartnav**](https://github.com/retroaalto/herdr-smartnav) | Moves geometrically between panes based on their actual position, providing natural up, down, left, and right navigation in irregular Herdr grids. |
| [**shadowfax92/herdr-layouts**](https://github.com/shadowfax92/herdr-layouts) | Adds tmux-style narrow splits and focused-pane equalization to Herdr. |
| [**pgilad/herdr-yank**](https://github.com/pgilad/herdr-yank) | Puts short keyboard hints on every URL, path, git SHA, UUID, and IP address visible in a Herdr TUI pane. Typing a hint copies the text or opens the URL or file. |
| [**ChristianDeckert/herdr-cheatsheet**](https://github.com/ChristianDeckert/herdr-cheatsheet) | Docks a clickable cheat-sheet panel beside Herdr TUI tabs that follows the focused app. Lists recipes plus Herdr and terminal keybindings one click away. |
| [**pradyb/herdr-which-key**](https://github.com/pradyb/herdr-which-key) | Opens a Neovim-style which-key popup in Herdr TUI where a leader key shows the next keys and runs Herdr actions. The key tree is defined in a keys.toml file. |
| [**RodrigoEspinosa/herdr-safe-close**](https://github.com/RodrigoEspinosa/herdr-safe-close) | Closes a Herdr TUI tab or pane right away when only idle shells run, and asks in a popup when an agent, dev server, or editor is still running. |
| [**Fadi729/herdr-terminal-scripts**](https://github.com/Fadi729/herdr-terminal-scripts) | Runs named scripts in Herdr TUI from a popup picker or numbered key slots. Stores scripts in the plugin config directory. |
| [**grooni/herdr-paste-image**](https://github.com/grooni/herdr-paste-image) | Pastes a clipboard image into a Herdr TUI agent pane by saving it as a PNG and typing its path, for Codex, Gemini CLI and Claude Code. Adds clipboard cleanup helpers for text. |
| [**blauerberg/herdr-launch-default-agent**](https://github.com/blauerberg/herdr-launch-default-agent) | Focuses a configured Herdr TUI tab and launches your preferred agent there if none is running, creating the tab when needed. |
| [**circusvoid/herdr-key-hints**](https://github.com/circusvoid/herdr-key-hints) | Shows the matching keybinding after a workspace, tab or pane action in Herdr TUI, with a native overlay on macOS and notifications on Linux. |
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
| [**skipbit/fzf-herdr**](https://github.com/skipbit/fzf-herdr) | Opens fzf in a Herdr TUI popup for shell key bindings such as CTRL-T, CTRL-R and ALT-C and for fuzzy completion, like fzf-tmux does for tmux. |
| [**cwong47/herdr-vim-navigation**](https://github.com/cwong47/herdr-vim-navigation) | Adds vim and screen style window commands to the Herdr TUI, such as moving panes to an edge, closing other panes or tabs, equalizing sizes and jumping between spaces. |
| [**sushisoosh/herdr-buffers**](https://github.com/sushisoosh/herdr-buffers) | Adds named tmux-style paste buffers to the Herdr TUI. Captures copy-mode selections, keeps reusable text and pastes from a searchable popup without the system clipboard. |
| [**abroller666/broadcast-pane**](https://github.com/abroller666/broadcast-pane) | Sends what you type in a small popup to all or chosen panes of the tab, similar to tmux synchronize-panes. |
| [**gysi/my-herdr**](https://github.com/gysi/my-herdr) | Adds small Herdr TUI actions for agent work: jump to the agent that needs you in sidebar order, fork a Claude Code, Codex or OpenCode session into a new tab, and move a pane into its own tab. |
| [**macd2/herdr-keycaps**](https://github.com/macd2/herdr-keycaps) | Shows every Herdr TUI binding currently in effect ordered by use, and adds keys for pane moves herdr leaves to the CLI such as sending a pane to another tab or swapping panes. |
| [**nnabilsayed/herdr-photo-picker**](https://github.com/nnabilsayed/herdr-photo-picker) | Opens the native Windows file picker from a Herdr TUI pane and inserts the chosen image paths into the focused agent's input without submitting it. |
| [**danemarguglio/herdr-copy-last**](https://github.com/danemarguglio/herdr-copy-last) | Copies an agent's last reply as Markdown to the clipboard in the Herdr TUI, from the focused pane or through a picker of all open agents. |
| [**jorgeraad/herdr-repeat**](https://github.com/jorgeraad/herdr-repeat) | Adds tmux-style repeatable keys to the Herdr TUI by opening a short popup that keeps accepting navigation keys within a repeat time. |
| [**koljamaier/herdr-quick-annotate**](https://github.com/koljamaier/herdr-quick-annotate) | Marks passages of agent output in Herdr TUI copy mode without leaving it, then pastes them into the agent prompt as labeled quotes. |
| [**PascalKraupner/herdr-lasttab**](https://github.com/PascalKraupner/herdr-lasttab) | Adds tmux-style last-tab and last-workspace toggles to the Herdr TUI, keeping separate state per workspace. |
| [**Leewonchan14/herdr-smooth-scroll**](https://github.com/Leewonchan14/herdr-smooth-scroll) | Scrolls Herdr TUI pane scrollback line by line with configurable speed and easing, as a port of tmux-smooth-scroll. |
| [**asonas/herdr-input-source-router**](https://github.com/asonas/herdr-input-source-router) | Switches the macOS input source as focus moves between Herdr TUI panes, remembering the last source used in each pane. |
| [**shang-shang95/herdr-keys**](https://github.com/shang-shang95/herdr-keys) | Shows a keybinding cheatsheet next to the tab bar for Herdr and Neovim, with an AI agent you can ask which key does a task. The README is in Japanese. |
| [**BrianVia/herder-address**](https://github.com/BrianVia/herder-address) | Copies the focused pane's full address to the clipboard, including pane id, workspace, tab, agent status, and worktree branch. |
| [**IamGroooooot/herdr-keyboard**](https://github.com/IamGroooooot/herdr-keyboard) | Sends hard-to-type key combinations such as Alt+Up or Shift+Tab from a mobile keyboard to Codex CLI, Claude Code, or any terminal running in Herdr, with custom combos. |
| [**sergiopx/tmurdr**](https://github.com/sergiopx/tmurdr) | Remaps Herdr TUI keys to the tmux keymap, with ctrl+space as the prefix. Backs up config.toml, validates the result, and offers a revert action. |

### Command palettes and workspace switchers

*62 projects. Searchable menus for Herdr commands, projects, workspaces, and common actions.*

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
| [**karanpatel1993/herdr-nav**](https://github.com/karanpatel1993/herdr-nav) | Opens fzf and ripgrep popups for file search, code search and project tree scoped to the current worktree, with jdb helpers for Java debugging. One searchable menu opens on prefix+Space. |
| [**hamzahraihan/herdr-better-workspace**](https://github.com/hamzahraihan/herdr-better-workspace) | Opens an interactive folder picker with mouse, keyboard or typed path and creates a Herdr workspace from the chosen directory. |
| [**abrose/herdr-url-picker**](https://github.com/abrose/herdr-url-picker) | Picks a URL from the current pane with fzf and opens it in the default browser. |
| [**chouxcreams/herdr-url-picker**](https://github.com/chouxcreams/herdr-url-picker) | Picks a URL from the focused pane and opens it in the default browser. |
| [**fabiogaliano/herdr-command-palette**](https://github.com/fabiogaliano/herdr-command-palette) | Opens a searchable Herdr TUI action palette with shortcuts, live agents and installed plugin commands. |
| [**haisi/herdr-plugin-command-palette**](https://github.com/haisi/herdr-plugin-command-palette) | Searches effective Herdr TUI keybindings and custom commands with fzf and runs the selected action. |
| [**barnuri/herdr-command-palette**](https://github.com/barnuri/herdr-command-palette) | Searches and runs installed Herdr plugin actions through a command palette. |
| [**zackshen/herdr-telescope**](https://github.com/zackshen/herdr-telescope) | Searches Herdr TUI native and plugin actions alongside files and live ripgrep results in an fzf popup. |
| [**ningxiaoxiao/herdr-agent-picker**](https://github.com/ningxiaoxiao/herdr-agent-picker) | Enables the user choose an AI agent and working directory before Herdr creates a new tab, split, or workspace. |
| [**EkeMinusYou/herdr-launcher**](https://github.com/EkeMinusYou/herdr-launcher) | Launches frequent commands and jumps between panes and spaces from a searchable picker with live terminal previews. Ships a Go picker for Herdr TUI and a native Launcher mod for the Herdr app. |
| [**phin-tech/herdr-phin-util**](https://github.com/phin-tech/herdr-phin-util) | Opens a project picker in Herdr TUI that jumps to any repo, branch, pull request or issue as a Space and clones repos you do not have yet. Adds saved setups that lay out a whole Space and a command that moves a running Claude session into Herdr. |
| [**MykolaSuprun/herdr-vimnav**](https://github.com/MykolaSuprun/herdr-vimnav) | Switches spaces and agents from a master-detail picker with live pane previews in Herdr TUI. Supports filtering, jump codes, and sidebar badges. |
| [**DevooKim/herdr-cast**](https://github.com/DevooKim/herdr-cast) | Opens a Spotlight-style command palette in Herdr TUI to jump to agents, workspaces, and tabs, run plugin actions, and run configured key commands. README is in Korean with an English version. |
| [**doanhthong/atd-herdr-command-palette**](https://github.com/doanhthong/atd-herdr-command-palette) | Opens a fuzzy command palette in Herdr TUI that jumps to running agents, starts agent tabs in saved projects, and runs any Herdr action. |
| [**mikitahimpel/herdr-launcher**](https://github.com/mikitahimpel/herdr-launcher) | Opens a floating menu from one keybinding that lists your Herdr TUI plugin panels and opens the chosen one over the tab. |
| [**iancharters/herdr-palette**](https://github.com/iancharters/herdr-palette) | Opens a fuzzy command palette for Herdr TUI that lists core commands plus actions discovered from installed plugins. Runs the chosen command in the focused pane or a new split. |
| [**shippy/raycast-herdr · extensions/herdr**](https://github.com/shippy/raycast-herdr/tree/main/extensions/herdr) | Controls Herdr TUI workspaces from Raycast and launches Claude prompts or configured actions. |
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
| [**adhikasp/herdr-command-plugin**](https://github.com/adhikasp/herdr-command-plugin) | Adds a Cmd+K style fuzzy list of every space, tab, agent, pane, and command with kind prefixes. Also adds a command palette and automatic tab titles. |
| [**sudokvn/herdr-project-switcher**](https://github.com/sudokvn/herdr-project-switcher) | Opens an fzf popup to find a project and focus its workspace, or create one if it does not exist. |
| [**HuangYujun-JunkyTalent/herdr-command-palette-all**](https://github.com/HuangYujun-JunkyTalent/herdr-command-palette-all) | Opens a fuzzy-search command palette in the Herdr TUI that lists Herdr commands, plugin actions and jump targets. Each row shows the key bound to the same command. |
| [**zhaoyshine/herdr-custom-commands**](https://github.com/zhaoyshine/herdr-custom-commands) | Adds a panel of your own shell commands beside every workspace; clicking one runs it there without opening a tab or taking over a pane. |
| [**mcavallo/herdr-command-palette**](https://github.com/mcavallo/herdr-command-palette) | Opens an fzf command palette in Herdr TUI to run built-in, plugin and custom actions and jump to agents and panes. |
| [**nnexai/herdr-action-launcher**](https://github.com/nnexai/herdr-action-launcher) | Opens an fzf picker of manual actions configured globally or per repository for the active Herdr workspace. |
| [**owenps/herdr-prs**](https://github.com/owenps/herdr-prs) | Opens a Herdr TUI popup for GitHub pull requests and local branches with fuzzy search, workflow groups, and Markdown previews. Jumps to worktree checkouts and tracks review feedback and checks. |
| [**Seigiard/herdr-command-palette**](https://github.com/Seigiard/herdr-command-palette) | Runs user-owned global or repository commands from a Herdr TUI palette with aliases, fuzzy search, forms, selects, and pane or tab dispatch. |
| [**c7zx/herdr-command-lists**](https://github.com/c7zx/herdr-command-lists) | Lets you browse and run commands from custom Markdown command lists in a Herdr TUI popup on Linux and macOS. |
| [**baeroe/herdr-everything**](https://github.com/baeroe/herdr-everything) | Adds a search-everywhere popup to the Herdr TUI covering agents, spaces, tabs, panes, commands, and plugin actions, plus built-in JSON, UUID, and random string tools. |
| [**akpw/herdr-last-workspace**](https://github.com/akpw/herdr-last-workspace) | Toggles between the current and previous workspace like tmux, restoring each workspace's last active tab. Uses only the Python standard library. |
| [**leonardoacosta/herdr-menu**](https://github.com/leonardoacosta/herdr-menu) | Opens a fuzzy picker in Herdr TUI for pane, tab, and workspace actions such as split, close, swap, zoom, rename, and move. Uses fzf when present and a numbered fallback otherwise. |
| [**RadeJR/herdr-plugins · project-picker**](https://github.com/RadeJR/herdr-plugins/tree/main/project-picker) | Opens a fzf popup of directories under ~/projects in Herdr TUI and focuses or creates the matching workspace, with a second picker to switch among open workspaces. |
| [**Qu4tro/herdr-whichkey**](https://github.com/Qu4tro/herdr-whichkey) | Opens a which-key style hint strip in Herdr TUI where one keystroke triggers each action. Supports nested groups, sticky resize repeat, and defaults adapted to installed plugins. |

### Status lines and workspace metadata

*142 projects. Status lines, external terminal and desktop bars, pane labels, and workspace metadata without sidebar or tab-label displays.*

| Project | What it does |
|---|---|
| [**fkiene/llmtrim-herdr**](https://github.com/fkiene/llmtrim-herdr) | Activates the llmtrim compression proxy in new Herdr workspaces, shows savings badges in pane rows, and opens llmtrim's dashboard in a split. It also warns when a pane did not inherit the proxy settings. |
| [**jankeesvw/omarchy-herdr**](https://github.com/jankeesvw/omarchy-herdr) | Runs herdr servers in the Omarchy bar, with every agent inside them, and a click that lands you on the one you picked. |
| [**rjyo/herdr-window-title-sync**](https://github.com/rjyo/herdr-window-title-sync) | Writes workspace, tab, and agent context to the outer terminal title. It uses pane metadata and status first, then falls back to recent prompts in local Claude Code or Codex session files. |
| [**wenhanweime/herdr-plugin-renamer**](https://github.com/wenhanweime/herdr-plugin-renamer) | Uses an LLM to name sessions for Claude Code, Codex, Grok, Pi, and OpenCode, with Chinese or English labels and OpenCode Zen as the default engine. |
| [**ezcorp-org/herdr-git-status**](https://github.com/ezcorp-org/herdr-git-status) | Shows staged, modified, untracked, and conflicted Git files for each workspace beside its branch name. |
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
| [**ivanvykopal/herdr-slurm**](https://github.com/ivanvykopal/herdr-slurm) | Polls Slurm and PBS clusters over SSH and shows a live job table in a pane, plus a per-machine scheduler token in the Herdr sidebar. |
| [**mahirocoko/mahiro-herdr**](https://github.com/mahirocoko/mahiro-herdr) | Adds per-agent status icons, Git branch state and listening ports to Herdr's Spaces sidebar, plus account usage rows from external cache files. Includes a picker that runs saved project commands in new tabs. |
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
| [**timmo001/agent-checks**](https://github.com/timmo001/agent-checks) | Publishes CI, lint and pull request review status for each Herdr workspace as sidebar tokens. Includes an Omarchy panel; builds from a checkout. |
| [**baleen37/herdr-sim**](https://github.com/baleen37/herdr-sim) | Marks each Claude Code or Codex pane in Herdr with the pull requests its session touched as open, merged or closed icons. Adds a Changes panel and a workspace, worktree and session tree. |
| [**Flyingdot/herdr-pr-status**](https://github.com/Flyingdot/herdr-pr-status) | Shows the GitHub pull request or GitLab merge request of each Space branch in the Herdr TUI sidebar. Uses gh and glab, including self-hosted GitLab. |
| [**ooospooky/herdr-port-labels**](https://github.com/ooospooky/herdr-port-labels) | Shows dev server ports on Herdr TUI tabs, pane borders, and the sidebar. Counts any TCP listener started from a pane, including servers an agent starts. |
| [**huluhuluu/herdr-remark**](https://github.com/huluhuluu/herdr-remark) | Marks finished agent turns as read and adds short notes shown in the Herdr TUI sidebar. Needs no wrappers or Herdr patches. |
| [**ecklf/herdr-plugin-gh**](https://github.com/ecklf/herdr-plugin-gh) | Shows GitHub PR state, CI status, and unresolved review counts in the Herdr TUI Agents sidebar. Opens or creates PRs, reruns failed jobs, and updates PR branches from a popup. |
| [**gosuwtf/herdr-machine-memory**](https://github.com/gosuwtf/herdr-machine-memory) | Shows memory usage in the Herdr TUI tab bar for the local machine and every machine connected over SSH. |
| [**jeffarese/herdr-stats**](https://github.com/jeffarese/herdr-stats) | Shows live CPU, memory, disk, temperature, GPU, power, and network stats in the Herdr TUI tab bar as braille graphs and gauges. |
| [**paniolo-ai/herdr-plugins**](https://github.com/paniolo-ai/herdr-plugins) | Adds per-session status footers to Herdr TUI for Claude Code, Cursor Agent, Codex, and Devin panes, showing model, context, rate limits, and tokens. Includes a plugin that opens Obsidian links. |
| [**macd2/herdr-pane-labels**](https://github.com/macd2/herdr-pane-labels) | Puts each pane's current directory, agent session title, and local or SSH marker into the pane border in Herdr TUI. |
| [**ralphilius/herdr-github-metadata**](https://github.com/ralphilius/herdr-github-metadata) | Shows the pull request each agent works on as a sidebar token in Herdr TUI, resolved from session transcripts, worktrees, and gh. No model calls. |
| [**dk3775/herdr-plugin-omp-state**](https://github.com/dk3775/herdr-plugin-omp-state) | Reports omp agent state to Herdr TUI from the terminal title, for panes where the official omp integration is not reporting. |
| [**lucidstack/herdr-services**](https://github.com/lucidstack/herdr-services) | Discovers dev servers and listening ports running in each Herdr TUI workspace and lists them in the sidebar, one row per service. |
| [**mrzzmrzz/herdr-opendde-harness**](https://github.com/mrzzmrzz/herdr-opendde-harness) | Shows a spinner, lifecycle state and short activity summary for ddeharness in the default Herdr TUI agent row. |
| [**minerado/omaherdrbar**](https://github.com/minerado/omaherdrbar) | Shows Herdr agent status in the Omarchy bar, including which agents need you, are done, or are working. Adds a panel and settings. |
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
| [**netresearch/herdr-bg-activity**](https://github.com/netresearch/herdr-bg-activity) | Marks idle Claude Code agents that still run monitors or background shells. Includes Herdr app mods and a layout with service links. |
| [**njs14/herdr-kiro-pulse**](https://github.com/njs14/herdr-kiro-pulse) | Reports Kiro CLI V3 sessions to the Herdr app and TUI as working, blocked, or done through OSC 7501 instead of showing idle. Distinguishes permission prompts and question panels. |
| [**tomajask/herdr-macos-statusbar**](https://github.com/tomajask/herdr-macos-statusbar) | Adds an iTerm2-style status bar to the Herdr TUI tab bar on macOS with battery, CPU, memory and network segments. A text-only mode replaces the Nerd Font icons. |
| [**arthurgiroux/herdr-azure-devops-plugin**](https://github.com/arthurgiroux/herdr-azure-devops-plugin) | Shows live Azure DevOps builds for the current workspace's repo and branch in the Herdr TUI. Raises a toast when a build finishes. |
| [**riogesulgon/herdr-zoom-indicator**](https://github.com/riogesulgon/herdr-zoom-indicator) | Marks the Herdr TUI tab bar and optionally the Agent and Space sidebar rows when the active pane is zoomed. Installs with a setup action and a small shell script. |
| [**fahrizkyputra/herdr-pane-goal-session**](https://github.com/fahrizkyputra/herdr-pane-goal-session) | Stores a goal per Herdr TUI pane and records the agent's session ID. Copies a ready resume command after a restart or crash. |
| [**Joeb454/herdr-iterm-status**](https://github.com/Joeb454/herdr-iterm-status) | Shows the most urgent agent state across all Herdr TUI spaces, such as needs input, working or done, in the iTerm2 tab subtitle and dot. |
| [**ak-paca/herdr-description**](https://github.com/ak-paca/herdr-description) | Adds persistent descriptions to Herdr TUI spaces, tabs and panes, edited in stacked panes on the right. |
| [**dereknex/herdr-gh-pr**](https://github.com/dereknex/herdr-gh-pr) | Shows the focused agent pane's branch PR status in the Herdr TUI sidebar, including conflicts, CI checks and review feedback. Can send repair prompts to the agent. |
| [**musingfox/herdr-osc7501**](https://github.com/musingfox/herdr-osc7501) | Reports the status of every Herdr TUI pane agent to the outer Rex terminal as OSC 7501 sequences. Works in every session including the default one. |
| [**ubuntudroid/herdr-git-status**](https://github.com/ubuntudroid/herdr-git-status) | Shows live CI and code-review status dots for GitHub and GitLab in the Herdr TUI spaces sidebar. Adds on-demand CI-detail and My PRs panes. |
| [**janosmiko/herdr-cmd-status**](https://github.com/janosmiko/herdr-cmd-status) | Shows running and finished icons in the Herdr TUI Spaces sidebar for long shell commands, including commands over ssh and in VMs. |
| [**shreyanshrana/herdr-spotify**](https://github.com/shreyanshrana/herdr-spotify) | Shows Spotify now-playing text in Herdr TUI's bottom status area with keyboard playback controls and a like toggle. Runs on macOS and Linux. |
| [**migueljfsc/herdr-gh-actions**](https://github.com/migueljfsc/herdr-gh-actions) | Shows GitHub Actions status for each workspace branch and agent worktree in the sidebar, with a pane to drill into runs, jobs and logs, re-run, cancel, dispatch, and hand failures back to an agent. |
| [**mustafaergul/herdr-cowbell**](https://github.com/mustafaergul/herdr-cowbell) | Adds a colored dot next to each Herdr TUI workspace name for every dev server running in it, so you see which workspaces have servers up without switching. |
| [**StateFarmIns/herdr-pane-pwd**](https://github.com/StateFarmIns/herdr-pane-pwd) | Shows each pane's current working directory on its Herdr TUI pane border. |
| [**rsdlt/baa**](https://github.com/rsdlt/baa) | Checks that the project still compiles after each agent turn and shows a check or cross next to the agent in the Herdr TUI sidebar. |
| [**alx-xo/herdr-pr-status**](https://github.com/alx-xo/herdr-pr-status) | Shows GitHub pull request state, CI checks, review decisions, and unresolved threads next to workspace branches in the Herdr TUI sidebar, updated in the background. |
| [**akhilnalliboina/herdr-statusbar**](https://github.com/akhilnalliboina/herdr-statusbar) | Shows local Git changes, GitHub PR statistics, CPU, RAM, battery, weather, and time in the Herdr TUI top or bottom tab bar. |
| [**mkuklis/herdr-launchd**](https://github.com/mkuklis/herdr-launchd) | Lists your scheduled macOS launchd jobs in a Herdr TUI sidebar with status, last and next run, and actions to run a job or read its log. |
| [**itaiin/herdr-wrapped-agent-plugin**](https://github.com/itaiin/herdr-wrapped-agent-plugin) | Detects coding agents running inside docker exec and dev-container sessions that Herdr TUI cannot see on its own, so those panes show agent state. |
| [**FaintGhost/herdr-system-stats**](https://github.com/FaintGhost/herdr-system-stats) | Shows whole-machine CPU, RAM, and disk usage in the Herdr TUI top bar with a switchable percentage or used-total display and an optional live detail pane. |
| [**lukecameron/herdr-spaces**](https://github.com/lukecameron/herdr-spaces) | Adds per-space agent, working, and blocked counts to the Herdr TUI sidebar and periodically asks a model to name new spaces after the work in them. |
| [**vitorpacheco/herdr-track-builds**](https://github.com/vitorpacheco/herdr-track-builds) | Shows running builds and tests as activity lines under each space in the Herdr TUI sidebar. |
| [**danjuls/herdr-ddev**](https://github.com/danjuls/herdr-ddev) | Shows ddev project status badges in the Herdr TUI sidebar and starts, stops, or opens projects from a key or picker. |
| [**unstable-code/herdr-space-branch**](https://github.com/unstable-code/herdr-space-branch) | Shows the git branch and ahead/behind count of the pane you are focused on in the Herdr TUI spaces sidebar, instead of the first tab's repository. |
| [**Resilient-Software/herdr-agent-activity**](https://github.com/Resilient-Software/herdr-agent-activity) | Shows subagents, background tasks, monitors, and scheduled checks of Claude Code and Codex agents in the Herdr sidebar and as metadata tokens, so an idle agent that is still waiting is visible. |
| [**morphysh/herdr-battery**](https://github.com/morphysh/herdr-battery) | Shows battery, CPU, and memory widgets in the Herdr tab bar with a details popup. Reads Linux sysfs and has no dependencies. |
| [**VibrantClouds/herdr-gsd-core**](https://github.com/VibrantClouds/herdr-gsd-core) | Shows GSD-Core project phase and status from .planning/ as sidebar tokens, with notifications, a dashboard, and supervised runs. Reports metadata only and does not control pane lifecycle. |
| [**ponzu07/herdr-git-status**](https://github.com/ponzu07/herdr-git-status) | Shows unstaged, staged, untracked counts and the worktree count in the Herdr spaces sidebar. Linux only and the README is in Japanese. |

### Automatic tab, pane, and workspace names

*92 projects. Plugins that rename tabs, panes, and workspaces from the foreground process, directory, git branch, agent session title, or first prompt, plus numbered tab and workspace labels.*

| Project | What it does |
|---|---|
| [**kryptamine/herdr-auto-title**](https://github.com/kryptamine/herdr-auto-title) | Updates Herdr tab titles automatically based on active workspace tasks to keep development contexts organized. |
| [**qu8n/herdr-automatic-rename**](https://github.com/qu8n/herdr-automatic-rename) | Renames tabs from the active foreground process and icon, and prefixes workspaces, tabs, and agents with numbers 1 through 9 for quick visual and keyboard selection. |
| [**iurysza/herdr-tab-smart-rename**](https://github.com/iurysza/herdr-tab-smart-rename) | Uses a lightweight LLM to derive short workspace and tab names from pane activity, replacing generic numbers or directory labels with current task summaries. |
| [**sh1ma/herdr-auto-title**](https://github.com/sh1ma/herdr-auto-title) | Runs in the background and derives Herdr tab names from the topic and intent of Claude Code or Codex conversations. |
| [**aarsh21/herdr-tab-title**](https://github.com/aarsh21/herdr-tab-title) | Provides automatic tmux-style tab titles for Herdr. |
| [**wjarka/herdr-ghostty-tab-title**](https://github.com/wjarka/herdr-ghostty-tab-title) | Writes color-coded counts of working, blocked, done, and idle Herdr agents into Ghostty tab titles. |
| [**killerz3/herdr-agent-titler**](https://github.com/killerz3/herdr-agent-titler) | Auto-titles Herdr tabs using local agy, claude, codex, or opencode harnesses without external API keys. |
| [**kakigakki/herdr-auto-namer**](https://github.com/kakigakki/herdr-auto-namer) | Uses Claude Code session titles for agent tabs and directory names for workspaces, providing automatic ChatGPT-style labels across parallel sessions. |
| [**danbuhler/herdr-pane-topic-sync**](https://github.com/danbuhler/herdr-pane-topic-sync) | Renames panes and tabs from the active topic or terminal title emitted by Claude Code and Codex, while avoiding rename loops and respecting manual labels. |
| [**lmilojevicc/herdr-tab-rename**](https://github.com/lmilojevicc/herdr-tab-rename) | Renames each Herdr tab to its focused pane's working-directory name. Manually renamed tabs are left alone. |
| [**rohankewal/herdr-nerd-font-tab-name**](https://github.com/rohankewal/herdr-nerd-font-tab-name) | Ports tmux-nerd-font-window-name to Herdr, updating tab icons from the running program and directory context. |
| [**yukikisaku/pi-agent-status · packages/pi-herdr-status**](https://github.com/yukikisaku/pi-agent-status/tree/main/packages/pi-herdr-status) | Adds a working spinner, completion indicator, and AI-generated title to Herdr TUI tabs for Pi sessions. |
| [**Angel-O/herdr-labels**](https://github.com/Angel-O/herdr-labels) | Numbers Herdr TUI tabs and names eligible tabs after their foreground processes while preserving manual labels. |
| [**Xz-FreeMan/herdr-hint**](https://github.com/Xz-FreeMan/herdr-hint) | Adds Pi and Codex session names to Herdr TUI tab titles and reports session metadata, primarily on Windows. |
| [**maedana/herdr-whereami**](https://github.com/maedana/herdr-whereami) | Renames Herdr TUI tabs from the current directory or Git repository and reports a `$gitref` sidebar token. |
| [**ndom91/herdr-ai-tab-name**](https://github.com/ndom91/herdr-ai-tab-name) | Uses a local Ollama model to generate and update descriptive Herdr tab names from recent pane activity. |
| [**toyamarinyon/herdr-thread-to-tab**](https://github.com/toyamarinyon/herdr-thread-to-tab) | Renames single-pane tabs from Claude Code or Codex thread titles through background session updates and the Herdr socket API. |
| [**justcyl/pi-herdr-tab-sync**](https://github.com/justcyl/pi-herdr-tab-sync) | Renames the active Herdr tab to the Pi session name when an agent starts or resumes. It communicates directly with the socket and remains inactive outside Herdr-managed panes. |
| [**davidolrik/herdr-titles**](https://github.com/davidolrik/herdr-titles) | Builds tab and terminal-window titles from foreground processes, agent session names, and workspace status counts using HCL templates. Shell hooks support Bash, Zsh, and Fish, and manual tab names are preserved. |
| [**Only-Moon/herdr-nerd-font-tab-name-windows**](https://github.com/Only-Moon/herdr-nerd-font-tab-name-windows) | Adds contextual Nerd Font icons to tab titles based on directory, project type, or running tool, with support for Windows, macOS, and Linux. |
| [**dvoets/herdr-tagr**](https://github.com/dvoets/herdr-tagr) | Replaces Herdr tab titles with an icon for the running app, the current folder and the git branch. Handles remote directories from the ssh title and ships a default config. |
| [**wxomi/herdr-session-titles**](https://github.com/wxomi/herdr-session-titles) | Reads local session state of Devin, Cursor, Antigravity, Kiro and Claude Code and writes real session titles and task context into the Herdr sidebar and tabs. |
| [**azyu/herdr-agent-auto-naming**](https://github.com/azyu/herdr-agent-auto-naming) | Gives every detected agent a readable two-word name, persisted as the pane label so it survives restarts. |
| [**yersonargotev/tabby**](https://github.com/yersonargotev/tabby) | Labels focused tabs with a Significant Command or Working Directory Basename. |
| [**voice0726/herdr-jump-number**](https://github.com/voice0726/herdr-jump-number) | Displays jump-key numbers on workspaces and tabs without breaking Herdr's automatic workspace labels. |
| [**abrose/herdr-numbered-workspaces**](https://github.com/abrose/herdr-numbered-workspaces) | Puts a number in front of every space in herdr's sidebar, matching the indexed switchworkspace shortcut. |
| [**blurname/herdr-git-tab-name**](https://github.com/blurname/herdr-git-tab-name) | Keeps Herdr tab labels synchronized with the Git branch in the focused pane. |
| [**lucasleon2107/herdr-tab-title-sync**](https://github.com/lucasleon2107/herdr-tab-title-sync) | Updates Herdr tab labels from agent conversation titles and prompt summaries, allowing names to change as the task evolves. |
| [**ryanlewis/herdr-tab-renamer**](https://github.com/ryanlewis/herdr-tab-renamer) | Renames tabs from the active agent's session title or working directory, replacing generic numbers with current task context. |
| [**shantanugoel/herdr-auto-namer**](https://github.com/shantanugoel/herdr-auto-namer) | Names Herdr TUI panes and tabs using deterministic rules without an LLM. |
| [**btorresgil/herdr-hermes-session-title**](https://github.com/btorresgil/herdr-hermes-session-title) | Reads local Hermes Agent SQLite data and publishes descriptive conversation titles in the Herdr sidebar. |
| [**dev-shimada/herdr-auto-tab-name**](https://github.com/dev-shimada/herdr-auto-tab-name) | Keeps tab labels aligned with the focused pane's current directory and updates them on lifecycle and focus events without replacing manually chosen names. |
| [**tmn73/herdr-claude-tab-title**](https://github.com/tmn73/herdr-claude-tab-title) | Uses Claude Code session events to replace generic Herdr tab numbers with active task descriptions. |
| [**malone-c/herdr-agent-smart-rename**](https://github.com/malone-c/herdr-agent-smart-rename) | Renames panes and tabs from the active agent task or prompt by analysing live terminal activity and producing a concise label. |
| [**iko-soy/hermes-herdr-auto-title**](https://github.com/iko-soy/hermes-herdr-auto-title) | Updates Herdr tab titles automatically from the first user prompt using an LLM. |
| [**nolvane/herdr-tab-titles**](https://github.com/nolvane/herdr-tab-titles) | Names Herdr TUI tabs and panes automatically from the working directory, git branch, and what the focused agent is doing. Manual names stay untouched. |
| [**gwenwindflower/heraldr**](https://github.com/gwenwindflower/heraldr) | Labels Herdr TUI tabs with the foreground program and an icon, and adds jump numbers, repository, and worktree tokens to sidebar rows. Manual tab names always win. |
| [**oronbz/herdr-claude-tab-rename**](https://github.com/oronbz/herdr-claude-tab-rename) | Renames each Herdr TUI tab after the title of the Claude Code session in it, following /rename and auto titles. Tabs you named by hand keep their names. |
| [**ProjectAJ14/herdr-claude-title**](https://github.com/ProjectAJ14/herdr-claude-title) | Names Herdr TUI tabs, panes, and workspace rows after the work in them, and has Claude write each Claude Code session title through claude -p. |
| [**ajaykumarMohite/herdr-agent-tab-titles**](https://github.com/ajaykumarMohite/herdr-agent-tab-titles) | Renames each Herdr TUI tab to the task its coding agent reports in the terminal title. Includes a Claude Code hook installer. |
| [**EmmetZ/herdr-tab-smart-rename-rs**](https://github.com/EmmetZ/herdr-tab-smart-rename-rs) | Renames tabs that still have default or numeric labels to short task names derived from the tab and pane context. Written in Rust. |
| [**zhangzujian/herdr-auto-session-title**](https://github.com/zhangzujian/herdr-auto-session-title) | Generates a short title from the first request of an agent session and applies it to the Herdr TUI pane and tab. Also syncs the native Codex thread name. |
| [**riq0h/tab-process-name**](https://github.com/riq0h/tab-process-name) | Labels each Herdr TUI tab with its foreground process name, like tmux automatic-rename. |
| [**hotnugs/herdr-emoji-time**](https://github.com/hotnugs/herdr-emoji-time) | Adds emoji to Herdr TUI space, agent, and tab names to make them easier to identify. |
| [**khatriafaz/herdr-plugin-agent-repo**](https://github.com/khatriafaz/herdr-plugin-agent-repo) | Adds the current agent, repository, and branch names to Herdr pane headers and the sidebar. |
| [**kewah/herdr-tab-titles**](https://github.com/kewah/herdr-tab-titles) | Names panes and tabs automatically based on the first coding-agent prompt. |
| [**hxy91819/herdr-auto-title**](https://github.com/hxy91819/herdr-auto-title) | Names agent tabs automatically from an initial prompt and updates titles when turns settle. |
| [**christiangroth/herdr-tab-title-from-terminal**](https://github.com/christiangroth/herdr-tab-title-from-terminal) | Names Herdr tabs from their agents’ terminal titles while leaving manually named tabs unchanged. |
| [**T0mSIlver/herdr-title-wrap**](https://github.com/T0mSIlver/herdr-title-wrap) | Wraps pane terminal titles across multiple Herdr sidebar rows to fit the available width. |
| [**eduardoborges/herdr-claude-title-hook**](https://github.com/eduardoborges/herdr-claude-title-hook) | Syncs a Claude Code session title to its Herdr tab, including generated titles and `/rename`. |
| [**tiamointer/herdr-title-distill**](https://github.com/tiamointer/herdr-title-distill) | Updates Herdr tab titles automatically based on concise summaries of completed agent tasks. |
| [**sblevins/claude-rename-tab**](https://github.com/sblevins/claude-rename-tab) | Renames the current Herdr TUI tab to a short task-based label from a Claude Code session. |
| [**Ivotter/herdr-tab-session-name-sync**](https://github.com/Ivotter/herdr-tab-session-name-sync) | Synchronizes agent session names with Herdr tab and pane titles. |
| [**martian4202/pi-session-name**](https://github.com/martian4202/pi-session-name) | Names Pi sessions from recent messages and optionally synchronizes the title to the current Herdr TUI tab. |
| [**kazda01/pi-tab-status**](https://github.com/kazda01/pi-tab-status) | Shows live Pi status and generated descriptions in terminal tabs and Herdr sessions. |
| [**walidsi/pi-herdr-tab-namer**](https://github.com/walidsi/pi-herdr-tab-namer) | Adds a Pi extension that renames the current Herdr tab from a short summary of your first prompt in the session. |
| [**kokatsu/herdr-numbering**](https://github.com/kokatsu/herdr-numbering) | Numbers Herdr tabs and sidebar workspaces by their switch position so their keyboard shortcuts are visible. |
| [**longcw/herdr-name-tab**](https://github.com/longcw/herdr-name-tab) | Names Herdr tabs from the first user input and retains the name until the topic changes. |
| [**btj93/herdr-tabline**](https://github.com/btj93/herdr-tabline) | Renders Herdr tab labels with safe templates and project-aware profiles. |
| [**AlexBSoD/herdrtabrenamer**](https://github.com/AlexBSoD/herdrtabrenamer) | Renames Herdr TUI tabs automatically based on their running program, agent or working directory. |
| [**acjackman/herdr-title-rename**](https://github.com/acjackman/herdr-title-rename) | Adds tmux-style window titles and automatic tab/workspace renaming for herdr. |
| [**GladioFeng/herdr-ghostty-title-bridge**](https://github.com/GladioFeng/herdr-ghostty-title-bridge) | Synchronizes Herdr TUI agent names and states to Ghostty tab titles with a socket watcher. |
| [**inonprince/herdr-counting-sheep**](https://github.com/inonprince/herdr-counting-sheep) | Shows live workspace and agent positions in the Herdr TUI sidebar and adds navigation shortcuts. |
| [**yuritada/numberer-manager**](https://github.com/yuritada/numberer-manager) | Prefixes Herdr TUI workspace and tab labels with their current list positions. |
| [**DillonWall/herdr-agent-numbers**](https://github.com/DillonWall/herdr-agent-numbers) | Numbers agents in the Herdr TUI sidebar to match the shortcuts used to focus them. |
| [**oddurs/herdr-namesync**](https://github.com/oddurs/herdr-namesync) | Keeps workspace, tab, and agent names current as the work changes, reading the intent the coding agent already publishes as its terminal title. Applies a rename policy with debouncing, rate limits, and locks for names you set by hand, and runs without a model unless you configure an OpenAI-compatible endpoint for stale titles. |
| [**RickyMarou/herdr-numbered-tabs**](https://github.com/RickyMarou/herdr-numbered-tabs) | Prefixes Herdr TUI tab labels with their current displayed positions and updates them when tabs are reordered. |
| [**edouard-andrei/herdr-smart-rename**](https://github.com/edouard-andrei/herdr-smart-rename) | Names Herdr TUI tabs and panes on demand using agent context and an OpenAI-compatible model. |
| [**elKei24/herdr-title-sync**](https://github.com/elKei24/herdr-title-sync) | A single-instance daemon that copies OSC terminal titles from Claude Code and similar agents into Herdr tab labels and periodically reconciles state through the socket. |
| [**adnichols/herdr-kitty-status**](https://github.com/adnichols/herdr-kitty-status) | Shows live Herdr agent-state counts in Kitty terminal tabs. |
| [**yuhgo/herdr-tab-marker**](https://github.com/yuhgo/herdr-tab-marker) | Automatically adds a task-based title and repository-specific emoji to Claude Code and Codex tabs in Herdr. |
| [**jwbaldwin/herdr-auto-title**](https://github.com/jwbaldwin/herdr-auto-title) | Synchronizes managed Herdr TUI tab titles with OpenCode titles and adds agent status indicators. |
| [**Newt6611/herdr-tab-title**](https://github.com/Newt6611/herdr-tab-title) | Numbers Herdr TUI tab titles within each workspace using a configurable format. |
| [**ralphilius/herdr-pr-tab-renamer**](https://github.com/ralphilius/herdr-pr-tab-renamer) | Renames Herdr TUI tabs with pull request numbers detected in new agent output. |
| [**okonomi/herdr-auto-tab-name**](https://github.com/okonomi/herdr-auto-tab-name) | Renames herdr tabs to the foreground command running in them. |
| [**zee-sh/herdr-auto-rename**](https://github.com/zee-sh/herdr-auto-rename) | Names Herdr tabs and pane borders after each agent's session name, live, including Claude Code's /rename. Includes Herdr app mods. |
| [**hrudek/herdr-simple-tab-names**](https://github.com/hrudek/herdr-simple-tab-names) | Names tabs after their foreground process, like tmux automatic renaming, with a position prefix such as 1:fish or 2:vim. |
| [**shashank19gaurav/herdr-agent-auto-title**](https://github.com/shashank19gaurav/herdr-agent-auto-title) | Syncs Copilot and Pi session names to Herdr TUI tab labels on Local and saved SSH machines on Windows. An optional Pi extension can auto-name sessions. |
| [**pradyb/herdr-session-title**](https://github.com/pradyb/herdr-session-title) | Renames a Herdr space or tab to match a Claude Code session when you /rename it, so you do not rename things twice. |
| [**zcharef/session-topic**](https://github.com/zcharef/session-topic) | Renames each Claude Code session after what it is about, after the first reply, each /clear, and each compaction, and shows the name in Herdr TUI panes. |
| [**nshelia/herdr-session-title**](https://github.com/nshelia/herdr-session-title) | Shows each agent's session title, such as a Claude Code conversation name, in the Herdr TUI Agents sidebar instead of the agent name. |
| [**dawson-design/herdr-tab-titles**](https://github.com/dawson-design/herdr-tab-titles) | Names each Herdr TUI tab after the title that Claude Code or Codex gave the session running in it, following later retitles. |
| [**pauiglesias7/herdr-agent-workspace-names**](https://github.com/pauiglesias7/herdr-agent-workspace-names) | Names each Herdr TUI workspace after the session title of the coding agent inside it. Manual renames always win. |
| [**chappse6/herdr-agent-title**](https://github.com/chappse6/herdr-agent-title) | Labels Herdr TUI agent panes with the agent and its task title on the pane border and sidebar, in any language. Includes a Claude Code and Codex skill to pin titles. |
| [**Tomyail/herdr-auto-agent-rename**](https://github.com/Tomyail/herdr-auto-agent-rename) | Mirrors Herdr TUI tab labels onto the agent rows in the sidebar, including CJK and mixed-case names. Works one way from tab to sidebar, so it pairs with tab auto-naming plugins. |
| [**linjiang82/herdr-ws-numbering**](https://github.com/linjiang82/herdr-ws-numbering) | Shows each workspace's switch number in the Herdr TUI sidebar through custom workspace metadata. |
| [**javid-gulamaliyev/herdr-tabname-sync**](https://github.com/javid-gulamaliyev/herdr-tabname-sync) | Renames the Claude Code or Codex session in a Herdr TUI tab whenever the tab is renamed. |
| [**bonkey/herdr-fm-title**](https://github.com/bonkey/herdr-fm-title) | Names each coding-agent session from its first prompt using on-device Apple Foundation Models and uses the name as the tab label. Supports Claude Code, Codex, and OpenCode on macOS. |
| [**quinnjr/herdr-tab-naming**](https://github.com/quinnjr/herdr-tab-naming) | Keeps tab labels in sync with the repository root and the ticket from the branch name, and follows directory changes. Written in Rust. |
| [**barrychen38/herdr-assemble**](https://github.com/barrychen38/herdr-assemble) | Renames new Herdr TUI spaces and auto-numbered tabs with Marvel-hero codenames instead of numbers, leaving tabs you named yourself alone. |
| [**riq0h/tab-blank-number**](https://github.com/riq0h/tab-blank-number) | Blanks Herdr TUI's default numeric tab label while keeping tabs you named yourself, so tab labels can show something else. |
| [**m2selfA/herdr-alias-setter**](https://github.com/m2selfA/herdr-alias-setter) | Sets a Herdr TUI pane name and agent alias through a quick input or a menu of recent names and presets. |

### Sidebar grouping, ordering, and filtering

*45 projects. Plugins that restructure the Spaces and Agents sidebars into trees, project groups, priority or recency order, filtered views, and compact one-line rows.*

| Project | What it does |
|---|---|
| [**hhdebb/herdr-radar**](https://github.com/hhdebb/herdr-radar) | Shows agent activity in the Herdr TUI sidebar, grouping workspaces and worktrees and highlighting waiting or stale sessions. |
| [**ShankyJS/herdr-space-scoped-agents**](https://github.com/ShankyJS/herdr-space-scoped-agents) | Limits the agent sidebar to workers in the currently focused workspace, reducing unrelated fleet noise when moving between projects. |
| [**kriuchkov/herdr-scope**](https://github.com/kriuchkov/herdr-scope) | Shows Herdr TUI agent state in a project-grouped sidebar and jumps to agents waiting for input. |
| [**gonzalonicolasr/herdr-bandeja-to-dos**](https://github.com/gonzalonicolasr/herdr-bandeja-to-dos) | Organizes Herdr TUI agents by attention state in the sidebar and shows to-dos left by agents. |
| [**dboeter/herdr-agent-tree**](https://github.com/dboeter/herdr-agent-tree) | Docks a narrow pane on the left or right of every tab that shows workspaces as groups and their agents as a live tree with status marks. One key or click jumps to the agent that needs you. |
| [**4242labs/herdr-radar-plus**](https://github.com/4242labs/herdr-radar-plus) | Sorts Herdr agents by what needs you, with named groups that span connected machines. Adds a model-family mark and a machine row under each agent on top of herdr-radar. |
| [**evanbryant/herdr-covr**](https://github.com/evanbryant/herdr-covr) | Replaces the Herdr sidebar with a compact Spaces and Agents list, one line per agent sorted by what needs you. A second line appears only when an agent is blocked or just finished, with light and dark layouts. |
| [**ZingerLittleBee/herdr-agent-pins**](https://github.com/ZingerLittleBee/herdr-agent-pins) | Pins selected Herdr agent sessions to the top of the sidebar and restores their order across server restarts. |
| [**MrBogomips/herdr-tools**](https://github.com/MrBogomips/herdr-tools) | Sorts the spaces sidebar into top, default and bottom groups, gives every space of one customer the same colour (Space Herder), and names tabs after their folder, repo or branch (auto-tab-name). Also ships herdr-jump, a macOS menu bar picker that lists the agents waiting for you, blocked first and oldest wait first. |
| [**mashhoodr/herdr-space-sidebar**](https://github.com/mashhoodr/herdr-space-sidebar) | Merges Herdr's Spaces and Agents panels into one list with each agent nested under its space. Shows status symbols and session colors. |
| [**fujimogn/herdr-lineup**](https://github.com/fujimogn/herdr-lineup) | Draws one Herdr sidebar row per coding agent with vendor logo, state, context, weekly quota and local origin/main commit time. |
| [**mmirus/herdr-agent-inbox**](https://github.com/mmirus/herdr-agent-inbox) | Adds an inbox view to the Herdr TUI Agents sidebar that hides settled and snoozed agents. Lets you settle or snooze an agent until it finishes a turn or asks for input. |
| [**Tomcao1013/herdr-agents-group**](https://github.com/Tomcao1013/herdr-agents-group) | Colors Herdr TUI workspace labels and their agents with one palette and adds named dividers between workspace groups. Changes presentation only. |
| [**albertocoletta/herdr-groups**](https://github.com/albertocoletta/herdr-groups) | Groups the Herdr TUI Agents panel by git repo with a header per group. Puts worktree agents under their main repo and non-git agents under their folder name. |
| [**Ukrian/herdr-agent-tree**](https://github.com/Ukrian/herdr-agent-tree) | Shows the Herdr TUI Agents panel as a tree with each space name above its agents. |
| [**Zeus-Deus/herdr-focus**](https://github.com/Zeus-Deus/herdr-focus) | Relabels the Herdr TUI agent sidebar with Needs you, Working, Done, Unread, and Idle states. Adds settle and unread triage and a watch indicator for background PR checks. |
| [**Algorant/herdr-agent-tree**](https://github.com/Algorant/herdr-agent-tree) | Nests Pi subagents and workers under the agent that spawned them in the Herdr TUI Agents sidebar, across tabs and workspaces. Runs as an external plugin and never changes Pi. |
| [**C0R0NELL/herdr-agents-sidebar**](https://github.com/C0R0NELL/herdr-agents-sidebar) | Adds grouped and priority layouts with per-mode colors to the native Herdr TUI Agents sidebar, with machine and project headings. Needs Linux and Python 3.11. |
| [**scheron/herdr-bottombar**](https://github.com/scheron/herdr-bottombar) | Moves the Herdr TUI spaces and agents list from the left sidebar to a bar along the bottom of each tab for portrait monitors, with a key to swap layouts. |
| [**jeffhuen/herdr-project-sidebar**](https://github.com/jeffhuen/herdr-project-sidebar) | Adds a project, worktree, and agent tree dock and a native sidebar mode with project headers and nested worktrees to Herdr TUI. |
| [**AlexeyKrotkov/herdr-wrapped-tabs**](https://github.com/AlexeyKrotkov/herdr-wrapped-tabs) | Shows every tab of the current workspace on wrapped, clickable lines below the Herdr TUI tab bar. |
| [**iurysza/herdr-mosaic**](https://github.com/iurysza/herdr-mosaic) | Colors Herdr TUI spaces, groups agents in the sidebar, and arranges panes in the current tab. |
| [**ayumu-1212/herdr-pasture**](https://github.com/ayumu-1212/herdr-pasture) | Groups agents by repository and docks them on the left of every Herdr tab. |
| [**bshearrer/herdr-project-filter**](https://github.com/bshearrer/herdr-project-filter) | Filters the Herdr TUI Agents sidebar to agents belonging to one Git repository. |
| [**kazimshah39/herdr-suffix-agent-filter**](https://github.com/kazimshah39/herdr-suffix-agent-filter) | Filters the Herdr agent sidebar to workspaces whose names share a chosen suffix, reducing noise in large multi-repository fleets. |
| [**dm4/herdr-workspace-sidebar**](https://github.com/dm4/herdr-workspace-sidebar) | Provides a Herdr plugin for displaying workspace tabs in a flat list. |
| [**mike-bronner/herdr-plugin-recent-spaces**](https://github.com/mike-bronner/herdr-plugin-recent-spaces) | Keeps the spaces sidebar in most-recently-used order. |
| [**bagonyi/herdr-agent-recency**](https://github.com/bagonyi/herdr-agent-recency) | Orders agents in the agents panel by last activity, latest first, and shows when each was last active. |
| [**tatsuro-ueda/herdr-backlog**](https://github.com/tatsuro-ueda/herdr-backlog) | Sorts the agents sidebar by the mark at the start of each tab name, such as red, yellow, or green circles. |
| [**urit/herdr-claude-background**](https://github.com/urit/herdr-claude-background) | Lists the subagents, monitors and background shells of each Claude Code agent as rows under it in the Herdr TUI sidebar. Shows work that Herdr would otherwise report as idle. |
| [**ryanlewis/herdr-agent-rows**](https://github.com/ryanlewis/herdr-agent-rows) | Shows each Herdr TUI sidebar agent on one line with workspace, branch or PR and time since its last state change. Can group lead and worker agents. |
| [**collinpeters/herdr-spaces-order**](https://github.com/collinpeters/herdr-spaces-order) | Reorders Herdr TUI workspaces to match the Spaces worktree hierarchy, so the Agents panel and workspace numbers follow the sidebar. |
| [**igor-gorohovsky/herdr-agent-groups**](https://github.com/igor-gorohovsky/herdr-agent-groups) | Lets you create named groups such as In Progress or Review and assign Herdr TUI agents to them. Shows the groups in the sidebar Agents panel. |
| [**jffiorillo/herdr-hide-idle**](https://github.com/jffiorillo/herdr-hide-idle) | Hides Herdr TUI agents from the sidebar once they have been idle past a TTL. Pins and orders agents and reports short agent names. |
| [**quocdaijr/herdr-space-kit**](https://github.com/quocdaijr/herdr-space-kit) | Organizes the Herdr TUI sidebar into workspace groups with folding and linked worktrees under their repository. Adds a grouped Agents tab with agent states and Claude and Codex usage. |
| [**TheMoMatthias/herdr-navigator**](https://github.com/TheMoMatthias/herdr-navigator) | Adds a clickable navigator to the Herdr TUI that names workspaces after their Git repo, folds worktrees under them and groups agents and sub-agents by project. Resumes sessions in one click. |
| [**dptty/herdr-collapse-agents**](https://github.com/dptty/herdr-collapse-agents) | Collapses the Herdr TUI sidebar Agents list to a status rollup and the agents waiting on your input. |
| [**tyamanak/herdr-tab-sidebar**](https://github.com/tyamanak/herdr-tab-sidebar) | Turns the Herdr TUI Agents panel into a vertical tab list with one row per agent tab, grouped under each workspace. |
| [**patraianton/herdr-sidebar**](https://github.com/patraianton/herdr-sidebar) | Adds categories, colour stars, jump hotkeys, worktree detach, and alerts to the Herdr TUI Spaces sidebar for people running many agents. |
| [**speardragon/herdr-agent-sidebar**](https://github.com/speardragon/herdr-agent-sidebar) | Compacts the Herdr TUI Agents sidebar with per-agent logo icons, a header per project group, and optionally animated status marks. |
| [**skelz0r/herdr-plugin-space-agents**](https://github.com/skelz0r/herdr-plugin-space-agents) | Narrows the Herdr TUI sidebar Agents list to the current space plus blocked agents from other spaces. |
| [**Sighthesia/herdr-parallel-sessions-display**](https://github.com/Sighthesia/herdr-parallel-sessions-display) | Lists parallel OpenCode, Codex, and Claude Code sessions in the Herdr TUI Agents sidebar, grouped by working directory. |
| [**asermax/herdr-priority-view**](https://github.com/asermax/herdr-priority-view) | Reorders the Herdr TUI agent panel by how much attention each agent needs and lets you mark agents as high or low priority. |
| [**jiang1997/herdr-done-first**](https://github.com/jiang1997/herdr-done-first) | Moves the Space with an unseen finished agent to the front of the Spaces panel and lets you pin Spaces to stay on top. |
| [**SpidySamurai/claude-vezmex-team-tree**](https://github.com/SpidySamurai/claude-vezmex-team-tree) | Shows a subagent tree for Claude Code, Codex, and Pi in the Herdr TUI sidebar, with an expanded dashboard pane. Driven by lifecycle hooks rather than terminal scraping. |

### Sidebar badges, tokens, and status indicators

*88 projects. Plugins that add status icons, spinners, colors, model and CPU badges, PR and CI tokens, notes, and other per-row details to the sidebar and tab bar.*

| Project | What it does |
|---|---|
| [**robbyrussell/herdr-ohmyzsh**](https://github.com/robbyrussell/herdr-ohmyzsh) | Integrates Herdr with Oh My Zsh, displaying slow commands in the sidebar and triggering desktop completion notifications. |
| [**FlorisKr/herdr-openspec**](https://github.com/FlorisKr/herdr-openspec) | Shows OpenSpec change and task progress in the Herdr TUI sidebar and opens proposals, designs, and specs in a change browser. |
| [**eliasstravik/herdr-agent-progress**](https://github.com/eliasstravik/herdr-agent-progress) | Shows agent-reported task estimates and activity for Claude Code and Codex in the Herdr TUI sidebar. |
| [**wyattjoh/herdr-plugin-gh-pr**](https://github.com/wyattjoh/herdr-plugin-gh-pr) | Shows the GitHub pull-request number and CI state for the focused agent pane's branch in the Herdr sidebar. Updates are rate-limited, with shortcuts for manual refresh and opening the pull request. |
| [**bayoudhi/herdr-shell-progress**](https://github.com/bayoudhi/herdr-shell-progress) | Adds a live sidebar progress for slow shell commands, not just coding agents. |
| [**qintmb/herdr-icon-agent-ui**](https://github.com/qintmb/herdr-icon-agent-ui) | Adds larger agent icons, status glyphs, and a workspace, tab, and agent tree to the Herdr TUI sidebar. |
| [**testy-cool/herdr-sidebar-config**](https://github.com/testy-cool/herdr-sidebar-config) | Adds a compact workspace, tab, and agent sidebar preset with provider icons to Herdr. |
| [**getpipher/herdr-sysmon**](https://github.com/getpipher/herdr-sysmon) | Adds CPU, memory, battery, network, and disk measurements to Herdr sidebar tokens, with configurable refresh intervals and macOS-focused probes. |
| [**Numbered-com/herdr-ports**](https://github.com/Numbered-com/herdr-ports) | Detects TCP listeners started by processes in each workspace and adds a dynamic `$ports` badge to the Herdr sidebar. |
| [**pdalinis/herdr-disp-model**](https://github.com/pdalinis/herdr-disp-model) | Shows the active model and reasoning effort for Codex, Claude Code, Pi, and Hermes agents in the Herdr TUI sidebar. |
| [**thewtex/herdr-mem-cpu-load**](https://github.com/thewtex/herdr-mem-cpu-load) | Displays CPU, memory, and load averages in the Herdr TUI workspace sidebar or prints a tmux-compatible status line. |
| [**BjoernSchotte/agentglass-herdr**](https://github.com/BjoernSchotte/agentglass-herdr) | Opens agentglass in a Herdr TUI popup and adds workspace cost and agent alert indicators to the sidebar. |
| [**ilazaridis/herdr-pane-issue**](https://github.com/ilazaridis/herdr-pane-issue) | Shows each Herdr TUI agent pane’s GitHub issue and pull request in the sidebar and opens the linked item. |
| [**Totopo27/hudr2**](https://github.com/Totopo27/hudr2) | Shows OpenCode and Pi agent context, usage, and repository information in a Herdr TUI sidebar. |
| [**hasuwini77/herdr-spinner**](https://github.com/hasuwini77/herdr-spinner) | Animates Herdr TUI working-state pane indicators and offers sidebar theme presets. |
| [**jakekroon/herdr-pr-tracker**](https://github.com/jakekroon/herdr-pr-tracker) | Shows authored pull requests and requests awaiting review in a Herdr TUI widget, with an optional branch PR sidebar token. |
| [**maxguzenski/herdr-pr-watch**](https://github.com/maxguzenski/herdr-pr-watch) | Shows GitHub pull request and CI status for Herdr TUI workspaces and agent panes in the sidebar. |
| [**maromocooo/herdr-doxie**](https://github.com/maromocooo/herdr-doxie) | Replaces sidebar status icons for Herdr agents and spaces with animated dachshunds that run, sit, peek out of a house or sleep by agent state. Includes a bundled font, with configurable animation speed, colors and spacing. |
| [**dannyking/herdr-sidebar-customizer**](https://github.com/dannyking/herdr-sidebar-customizer) | Customizes the Herdr TUI sidebar with a color per space, seven working animations and model, effort and context details for Claude Code, Codex, OpenCode, pi and omp. An interactive settings panel previews changes before applying them. |
| [**rchougule/herdr-agents-info**](https://github.com/rchougule/herdr-agents-info) | Gives each Claude Code row in the Agents sidebar a distinguishing name, model, context percentage and disk footprint. |
| [**jolo-dev/herdr-workspace-icons**](https://github.com/jolo-dev/herdr-workspace-icons) | Adds rule-based workspace icons to expanded Herdr TUI desktop sidebar rows using workspace metadata. |
| [**dkbo/herdr-model-badge**](https://github.com/dkbo/herdr-model-badge) | Shows each agent's model and reasoning effort in the agents sidebar. |
| [**mcc0x/herdr-pulse**](https://github.com/mcc0x/herdr-pulse) | Samples agent lifecycle states and shows per-workspace activity history as sidebar sparklines. |
| [**jpwallace22/herdr-glab-status**](https://github.com/jpwallace22/herdr-glab-status) | Shows GitLab merge request status in each Herdr workspace sidebar row using an `$mr` token. |
| [**jwanga/herdr-plugin-github-status**](https://github.com/jwanga/herdr-plugin-github-status) | Shows GitHub milestones, issues, pull requests, and Actions in a Herdr sidebar pane. |
| [**geshido/icomark**](https://github.com/geshido/icomark) | Marks Herdr TUI tabs with workflow status and optional comments through keybindings or scripts. |
| [**andrewbrannan/herdr-workspace-prs**](https://github.com/andrewbrannan/herdr-workspace-prs) | Displays GitHub pull request status and workspace links or notes in the Herdr TUI sidebar. |
| [**mattyan1053/herdr-compose**](https://github.com/mattyan1053/herdr-compose) | Shows Docker Compose service health for each workspace in the Herdr sidebar, with quick toggles and a service-details popup. Compose stacks are removed when their worktrees are deleted. |
| [**bayoudhi/herdr-prayer-times**](https://github.com/bayoudhi/herdr-prayer-times) | Displays the next Islamic prayer and a live countdown in the Herdr sidebar, with a timetable popup and optional desktop alerts. Schedules are fetched from Al Adhan and cached locally. |
| [**szrenwei/herdr-space-tab-metadata**](https://github.com/szrenwei/herdr-space-tab-metadata) | Adds current tab labels and state indicators to each workspace row in the Herdr sidebar and keeps them synchronized through lifecycle events. |
| [**hasuwini77/herdr-tab-git**](https://github.com/hasuwini77/herdr-tab-git) | Shows the active tab’s Git branch and status in the Herdr TUI Spaces sidebar. |
| [**CrisLottz/herdr-dashboard**](https://github.com/CrisLottz/herdr-dashboard) | Adds a live sidebar with per-agent CPU and RAM, listening dev ports, git worktrees, and system stats including GPU and temperatures. Runs on Windows and Linux. |
| [**APhysickui/herdr-agent-sidebar**](https://github.com/APhysickui/herdr-agent-sidebar) | Shows each agent in the Herdr TUI sidebar with its task, stable pane ID, state, and directory. Adds Pi task labels and Kimi Code support, with English and Chinese docs. |
| [**minhtran3124/herdr-sidekick**](https://github.com/minhtran3124/herdr-sidekick) | Adds side panels for parallel coding agents in Herdr TUI: worktree cards with PR and CI status, changed files with diffs, and Claude Code subagents. |
| [**patrikbraborec/herdr-agent-panel**](https://github.com/patrikbraborec/herdr-agent-panel) | Attaches a live side panel to an agent pane in Herdr TUI that shows session state, context usage, skills, and diffs of changed files. Reads the Claude Code transcript. |
| [**dlepold/herdr-agent-resource-badges**](https://github.com/dlepold/herdr-agent-resource-badges) | Adds green, orange, and red CPU and RAM badges to busy agents in the Herdr TUI sidebar. Written in Rust. |
| [**devicki/herdr-ids**](https://github.com/devicki/herdr-ids) | Shows pane, tab, and workspace ids in the Herdr TUI sidebar and offers a picker that types a reference to any space, tab, or pane into your agent. Needs bash, jq, and fzf. |
| [**varvand/herdr-plugin-agent-spinner**](https://github.com/varvand/herdr-plugin-agent-spinner) | Adds a one-cell braille spinner token to working rows in the Herdr TUI Agents sidebar, since the built-in status mark does not animate. |
| [**adihex/herdr-agent-icons**](https://github.com/adihex/herdr-agent-icons) | Shows real logo icons for each agent in the Herdr TUI sidebar by compiling the logos into a private-use-area font. |
| [**arthurnw/herdr-unread**](https://github.com/arthurnw/herdr-unread) | Adds a manual unread marker to Herdr TUI agent sessions that clears when you focus the pane or the agent status changes. |
| [**poislagarde/herdr-branch-labels**](https://github.com/poislagarde/herdr-branch-labels) | Rewrites git branch labels in the Herdr TUI Spaces sidebar with a regular expression and replacement you configure. |
| [**flowreaction/herdr-state-icons**](https://github.com/flowreaction/herdr-state-icons) | Shows animated, colorable lifecycle icons for working, done, blocked and idle states in the Herdr TUI Spaces and Agents sidebar views. |
| [**ondratuma/herdr-status-plugin**](https://github.com/ondratuma/herdr-status-plugin) | A per-pane activity plugin with sidebar icons, live timers, and a helper for renaming agent panes. |
| [**PegasusWang/herdr-agent-prompt**](https://github.com/PegasusWang/herdr-agent-prompt) | Shows the latest prompt and reply for Claude Code and Codex sessions in the Herdr agent sidebar. |
| [**NachoPal/herdr-pane-agent-unread**](https://github.com/NachoPal/herdr-pane-agent-unread) | Tracks unread agent activity per Herdr pane and displays a sidebar badge when an unfocused agent finishes or needs input. |
| [**ericcparsons/herdr-vitals**](https://github.com/ericcparsons/herdr-vitals) | Shows per-agent CPU and memory use and per-space server ports in the Herdr TUI sidebar, with a pane for stopping servers. |
| [**StarDuster/mimo-code-herdr-plugin**](https://github.com/StarDuster/mimo-code-herdr-plugin) | Shows MiMo Code agent state in herdr's sidebar, a user-level MiMo plugin, no herdr changes required. |
| [**cheoljoo/herdr-space-activity-monitor**](https://github.com/cheoljoo/herdr-space-activity-monitor) | Marks Space sidebar rows as printing / unseen-output / idle via a custom $activity token. |
| [**limars874/herdr-pane-id-metadata**](https://github.com/limars874/herdr-pane-id-metadata) | Shows canonical pane IDs and compact tab and pane metadata in the Herdr sidebar. |
| [**FunnyQ/herdr-tab-bar-llm-quota**](https://github.com/FunnyQ/herdr-tab-bar-llm-quota) | Shows Claude and Codex quota in the herdr tab bar. |
| [**AndresDiagoM/herdr-route-audit**](https://github.com/AndresDiagoM/herdr-route-audit) | Shows under each agent in the sidebar which OmniRoute combo step served it (step 1 or a silent fallback to another model) and marks attributions it had to infer. Reads OmniRoute's call log read-only, pages Telegram once per fallback incident, and includes a report and a self-test. |
| [**bonkey/herdr-pr-emoji**](https://github.com/bonkey/herdr-pr-emoji) | Shows pull request state on Herdr sidebar rows using emoji. |
| [**sfroment/herdr-git-detail**](https://github.com/sfroment/herdr-git-detail) | Adds a `$git_detail` sidebar token with modified, staged, untracked, ahead, behind, and stash counts, refreshed when pane focus changes. |
| [**firew0rks/herdr-ci-tokens**](https://github.com/firew0rks/herdr-ci-tokens) | Shows pull-request, CI, and review state for every worktree in the Herdr sidebar. |
| [**choplin/herdr-repository-identity**](https://github.com/choplin/herdr-repository-identity) | Adds the shared Git repository name to each Herdr TUI workspace sidebar row, including linked worktrees. |
| [**hermanvulkers/herdr-pr-status-plugin**](https://github.com/hermanvulkers/herdr-pr-status-plugin) | Shows each worktree's PR approvals, CI status, and mergeability as colored sidebar tokens. |
| [**timjonez/herdr-agent-notes**](https://github.com/timjonez/herdr-agent-notes) | Adds persistent manual notes to Herdr TUI agent sidebar rows to explain why an agent is idle or blocked. |
| [**jovylle/herdr-pane-mark**](https://github.com/jovylle/herdr-pane-mark) | Adds palette actions and a popup to edit a per-pane mark displayed in the Herdr TUI agent sidebar. |
| [**aiki-sh/aiki-integration-herdr**](https://github.com/aiki-sh/aiki-integration-herdr) | Shows active aiki epics in a live-refreshing Herdr sidebar and installs the companion session-identity hook. |
| [**MorganCollins/herdr-last-used**](https://github.com/MorganCollins/herdr-last-used) | Shows when each herdr agent was last active, colour-coded by age, and filter the Agent sidebar by activity. |
| [**btj93/herdr-tokens**](https://github.com/btj93/herdr-tokens) | Publishes workspace metadata tokens derived from agent status, so sidebar colours can vary by state. |
| [**ubuntudroid/herdr-git-stack**](https://github.com/ubuntudroid/herdr-git-stack) | Shows each space's position in its git branch stack in the spaces sidebar, flags branches whose parent has moved, and keeps stacks contiguous. Local commit graph only, no network, no forge API, no stacking tool. |
| [**Levi-Gillies/herdr-ssh-agents**](https://github.com/Levi-Gillies/herdr-ssh-agents) | Shows AI coding agents running over SSH in Herdr's sidebar. |
| [**sfc-gh-tmeacham/coco-herdr-plugin**](https://github.com/sfc-gh-tmeacham/coco-herdr-plugin) | Shows Cortex Code agent status in the Herdr TUI sidebar. |
| [**CowboyVang/herdr-tab-badges**](https://github.com/CowboyVang/herdr-tab-badges) | Shows a sidebar badge on Herdr TUI spaces containing multiple tabs. |
| [**shimonacarvalho/herdr-github-status**](https://github.com/shimonacarvalho/herdr-github-status) | Shows each Herdr TUI agent pane’s Git branch and repository or pull-request status in the sidebar. |
| [**imtim/herdr-pane-id**](https://github.com/imtim/herdr-pane-id) | Labels Herdr TUI panes with IDs and agent names and adds identifiers to tabs and workspaces. |
| [**RickyMarou/herdr-display-workspace**](https://github.com/RickyMarou/herdr-display-workspace) | Shows the active workspace label on the right side of the tab bar. |
| [**luongnv89/herdr-github**](https://github.com/luongnv89/herdr-github) | Lists the open pull requests and issues of the current repo in a Herdr side pane, with review state, checks, and labels. Works with GitHub, GitLab, and self-hosted instances. |
| [**RheoTommy/herdr-needs-action**](https://github.com/RheoTommy/herdr-needs-action) | Marks an agent pane as needing action when it finishes and keeps the mark until you restart the agent or clear it. Covers work you have seen but not yet handled. |
| [**bagonyi/herdr-claude-subagents**](https://github.com/bagonyi/herdr-claude-subagents) | Shows how many subagents, teammates, and workflow agents each Claude agent has working, in its row in the agents panel. |
| [**massdo/herdr-npm**](https://github.com/massdo/herdr-npm) | Lists npm and pnpm scripts for the current package or workspace in a Herdr TUI sidebar column, with search and one-key run in script tabs. |
| [**dvoraj75/herdr-cowbell**](https://github.com/dvoraj75/herdr-cowbell) | Shows each tab's agent status as an icon before the tab name in the Herdr TUI, with working, blocked and done states. Offers five icon presets. |
| [**xkumiyu/herdr-space-recency**](https://github.com/xkumiyu/herdr-space-recency) | Fades Herdr TUI Space names after 24 hours and 7 days of no use to help you spot unused workspaces. Keeps active and attention-needing Spaces bright. |
| [**Aziffo/herdr-highlight**](https://github.com/Aziffo/herdr-highlight) | Lets you color workspaces and tabs in the Herdr TUI sidebar from a popup picker or direct actions. Choices persist and are reapplied at server startup. |
| [**ExLuna-rs/herdr-indicators**](https://github.com/ExLuna-rs/herdr-indicators) | Shows working, done, blocked and idle icons with a per-agent animated spinner on agent panes and workspaces in the Herdr TUI sidebar. Runs on Windows, macOS and Linux. |
| [**explesy/herdr-agent-task-notes**](https://github.com/explesy/herdr-agent-task-notes) | Adds a live multi-line task and activity summary below the agents list in the Herdr TUI sidebar for the active agent tab. Reads pi, Codex, OpenCode and agy sessions. |
| [**ozkar99/herdr-oiia-status**](https://github.com/ozkar99/herdr-oiia-status) | Replaces the yellow working dot in the Herdr TUI agent sidebar with a spinning OIIA cat and plays its sound while it spins. |
| [**BlockedPath/herdr-agent-icons**](https://github.com/BlockedPath/herdr-agent-icons) | Shows an icon instead of the agent name in the Herdr TUI agent sidebar and reports the harness name as a token. |
| [**Binb1/herdr-ghostty-sidebar**](https://github.com/Binb1/herdr-ghostty-sidebar) | Restyles the Herdr TUI Agents and Spaces sidebars with vendor logos and state-coloured titles, coloured from your Ghostty theme. |
| [**pglira/herdr-devcontainer-agents**](https://github.com/pglira/herdr-devcontainer-agents) | Shows coding agents running inside dev containers as normal Herdr TUI agents with state and notifications, even though the pane's foreground process is the exec client. |
| [**ananianatid/herdr-ssh-sessions**](https://github.com/ananianatid/herdr-ssh-sessions) | Shows ssh and mosh sessions as rows in the Herdr TUI Agent sidebar so remote shells are visible alongside agents. |
| [**shved270189/herdr-worktree-status**](https://github.com/shved270189/herdr-worktree-status) | Assigns a workflow status emoji such as planning, in progress, review, blocked, or done to worktree workspaces and shows it in the sidebar. |
| [**bonkey/herdr-bookmark**](https://github.com/bonkey/herdr-bookmark) | Marks Herdr TUI workspaces with one of three independent bookmarks toggled by keystroke and shown as one sidebar token. Can also sort the worktrees of a repository by their marks. |
| [**azyu/herdr-agent-cli**](https://github.com/azyu/herdr-agent-cli) | Shows which CLI runs in each Herdr TUI pane (claude, codex, and others) as a sidebar token you can colour per agent. |
| [**anthonykimm/herdr-pr-status**](https://github.com/anthonykimm/herdr-pr-status) | Shows each workspace's GitHub PR number, review state, and CI status as Herdr TUI sidebar tokens, refreshed every 60 seconds through gh. |
| [**gregsantos/herdr-agent-kind**](https://github.com/gregsantos/herdr-agent-kind) | Publishes each agent pane's kind (claude, codex, and others) as a coloured $agent_kind token for the Herdr TUI sidebar, even when agents have custom names. |
| [**rstacruz/herdr-workspace-description**](https://github.com/rstacruz/herdr-workspace-description) | Adds a one-line description under each space in the Herdr TUI sidebar through a $description token that survives server restarts. |

### Status overlays, HUDs, and agent timers

*78 projects. Floating status HUDs, turn timers, and keep-awake utilities.*

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
| [**thomashuangth/herdr-eartag**](https://github.com/thomashuangth/herdr-eartag) | Shows a recap panel beside each agent pane in Herdr with the conversation subject, your latest ask, what the agent did and whether it is done. Also lists edited files, context use and 5h and 7d quotas for Claude Code and Codex. |
| [**carsonjones/herdr-agent-dashboard**](https://github.com/carsonjones/herdr-agent-dashboard) | Lists live Herdr agent status in a Bun and React/OpenTUI dashboard that can run as a plugin action or standalone terminal app. |
| [**natori-hrj/herdr-standup**](https://github.com/natori-hrj/herdr-standup) | Summarizes each Herdr agent’s commits and uncommitted work in a digest with a persistent count. |
| [**assawalhy/herdr-stay-awake**](https://github.com/assawalhy/herdr-stay-awake) | Keeps the machine from sleeping while any herdr agent pane is working (Linux, macOS, Windows, and WSL). |
| [**jeffbking/herdr-agent-prompt**](https://github.com/jeffbking/herdr-agent-prompt) | Shows the focused coding agent's original prompt in an overlay for Claude Code, Codex, Antigravity, or Pi. |
| [**sazardev/herdr-pomodoro**](https://github.com/sazardev/herdr-pomodoro) | Runs a theme-adaptive Pomodoro timer in a Herdr TUI drawer, popup, or widget pane. |
| [**happyeric77/agent-keep-awake**](https://github.com/happyeric77/agent-keep-awake) | Uses macOS `caffeinate` while any Herdr agent is working and releases the sleep lock when all agents become idle, blocked, or done. |
| [**shadowfax92/herdr-scratch**](https://github.com/shadowfax92/herdr-scratch) | Gives each Herdr pane a persistent scratch overlay backed by a private tmux session, keeping notes, REPLs, and side commands tied to that pane. |
| [**parker-brown-family/omarchy-crook**](https://github.com/parker-brown-family/omarchy-crook) | Puts Herdr agent state on the Omarchy desktop bar: one icon that turns urgent when an agent is blocked, and a tray listing every agent grouped by whether it needs you. Clicking a row focuses that pane and raises the terminal window on Hyprland. |
| [**oki2a24/herdr-mac-activity-monitor**](https://github.com/oki2a24/herdr-mac-activity-monitor) | Shows macOS memory use and battery level in a Herdr TUI popup and updates the window title. |
| [**johnlindquist/herdr-pane-status**](https://github.com/johnlindquist/herdr-pane-status) | Adds native per-pane agent status and PTY activity cards to a Herdr TUI fork. |
| [**zyrre/corgi**](https://github.com/zyrre/corgi) | Shows a dashboard card per project in Herdr with its supervisor's latest message and worker states, naming every blocked worker. Adds a supervisor that runs them and an Omarchy bar widget. |
| [**thefahien/herdeck**](https://github.com/thefahien/herdeck) | Turns commands, processes, health checks, JSON APIs, and Prometheus queries into live tabs in a Herdr pane, declared in a TOML file. Also ships a native Herdr app mod that shows the same dashboards. |
| [**baeroe/herdr-overview**](https://github.com/baeroe/herdr-overview) | Opens a live tiled overview of all Herdr TUI spaces, every agent, or favorite panes, with each tile mirroring real terminal content and agent state. Enter jumps to the selected pane. |
| [**NoctisHsu/herdr-agent-board**](https://github.com/NoctisHsu/herdr-agent-board) | Shows a live board beside an agent pane with its task list, background subagents, and agents it dispatched to other panes with herdr agent start. Needs Python 3.9 and no third-party packages. |
| [**tdi/herdr-ci-checks**](https://github.com/tdi/herdr-ci-checks) | Shows live CI checks for the current branch in a side pane of Herdr TUI, from GitHub pull requests or GitLab pipelines, with failed logs and re-runs. Can open automatically in new worktrees. |
| [**pinkpixel-dev/herdr-tasks**](https://github.com/pinkpixel-dev/herdr-tasks) | Shows the agent task list in a split pane beside it, with items checked off as the agent finishes them. Any agent can drive it through the herdr-tasks CLI. |
| [**Tyru5/herdr-clock**](https://github.com/Tyru5/herdr-clock) | Opens a popup with the local time in large block glyphs, like tmux clock-mode. Any key dismisses it. |
| [**hanjm93/herdr-plugin-done-timer**](https://github.com/hanjm93/herdr-plugin-done-timer) | Shows a prompt-cache countdown next to each AI agent in the Herdr TUI agents panel, read from the agent transcript. |
| [**sm-steel/herdr-codex-subagents-rs**](https://github.com/sm-steel/herdr-codex-subagents-rs) | Shows a live, collapsible tree of Codex main agents and subagents inside Herdr TUI. Built in Rust for Windows and Linux. |
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
| [**orascope/herdr-tower**](https://github.com/orascope/herdr-tower) | Shows on one screen which Claude Code, Codex, Gemini, and opencode agents in Herdr TUI are working, waiting for you, or finished. Requires Herdr TUI 0.9.0 or newer. |
| [**bagonyi/herdr-claude-cache-timer**](https://github.com/bagonyi/herdr-claude-cache-timer) | Shows in the agents panel when each Claude agent's prompt cache expires, as a bar on its row. |
| [**orgoj/herdr-blocked-hud**](https://github.com/orgoj/herdr-blocked-hud) | Shows an always-on-top Linux X11 window that lists Herdr TUI agents that are blocked or done, with optional sounds, and focuses a pane when you click its row. Starts with the Herdr server as a plugin. |
| [**kristaxox/herdr-agent-dashboard**](https://github.com/kristaxox/herdr-agent-dashboard) | Shows Claude Code agents in the Herdr TUI as a topology of cards by repository and worktree. Each card has status, current activity, model, branch, PR and CI state. |
| [**cmalec/herdr-agent-time**](https://github.com/cmalec/herdr-agent-time) | Shows each agent's current turn runtime in the Herdr TUI sidebar, ticking every second while it works and keeping the final duration after the turn ends. |
| [**seankao31/herdr-pane-status**](https://github.com/seankao31/herdr-pane-status) | Marks panes whose agent finished or needs you on the pane border until you look at them, so the sidebar state also shows on the pane. |
| [**tyler-dot-earth/herdr-hogs**](https://github.com/tyler-dot-earth/herdr-hogs) | Shows live CPU and memory per pane summed over each pane's process tree, with sidebar markers on hot panes and workspaces. Linux only. |
| [**ivanusong/herdr-plugin-agent-overview**](https://github.com/ivanusong/herdr-plugin-agent-overview) | Opens a full-screen grid of live read-only tiles for agents across workspaces, filterable by Working, Done or Idle, with one key to jump to the real pane. Built in Rust with ratatui. |
| [**rsdlt/bottleneck**](https://github.com/rsdlt/bottleneck) | Records every agent state change in Herdr TUI and shows how long your agents sit waiting on you for permission prompts or review. |
| [**alexiob/herdr-prism**](https://github.com/alexiob/herdr-prism) | Opens an eight-view dashboard in the Herdr TUI for Codex, Claude Code, and Pi sessions with agent trees, CPU and memory, processes, git changes, usage limits, and private Markdown notes. Can collect data locally or on each SSH server. |
| [**Yoliani/herdr-resource-manager**](https://github.com/Yoliani/herdr-resource-manager) | Shows a live CPU and memory board for every Herdr TUI workspace, pane, and agent, including orphaned processes. |
| [**murat-saglam/herdr-jev**](https://github.com/murat-saglam/herdr-jev) | Explains why each blocked or finished agent stopped, such as risky approvals, questions, or failed runs, by sending the terminal tail to TypeSafe's Jev model. Shows the result on a board. |
| [**KamalF/herdr-busywatch**](https://github.com/KamalF/herdr-busywatch) | Shows whether any non-agent command in a pane is still running and whether it needs input. Tracks builds and tests through zsh, bash, or fish shell hooks. |
| [**GranamyrBR/ezdras-herdr**](https://github.com/GranamyrBR/ezdras-herdr) | Shows live agent activity and offers pane controls in Herdr. |
| [**ArtMoreno/herdr-glance**](https://github.com/ArtMoreno/herdr-glance) | Provides a live agent dashboard for Herdr, with five themes and a fast prompt segment. |

### Context meters and rate-limit gauges

*90 projects. Live token headroom meters, quota tracking, and agent cost gauges.*

| Project | What it does |
|---|---|
| [**levi-qiao/herdr-agent-usage**](https://github.com/levi-qiao/herdr-agent-usage) | Shows model, context and subscription quota for coding agents in the Herdr TUI agent sidebar. |
| [**levi-qiao/herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota) | A sidebar quota monitor for Claude, Codex, Grok, and Agy that shows the percentage remaining in five-hour and weekly limits. |
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
| [**amali01/herdr-pacer**](https://github.com/amali01/herdr-pacer) | Draws context-window bars under each agent in the Herdr sidebar and a dock with 5h, weekly and optional monthly usage for Claude Code, Codex and OpenCode. A popup shows the same usage on demand. |
| [**nordz0r/herdr-opencodex**](https://github.com/nordz0r/herdr-opencodex) | Adds two plugins for OpenCodex users: a popup with token spend and estimated cost, and a sidebar panel with model, context and remaining 5h and 7d quota. README is in Russian with an English version. |
| [**harpal-singh-qp/herdr-footprint**](https://github.com/harpal-singh-qp/herdr-footprint) | Shows each space's git worktree disk usage and the context window use of its busiest agent in the Herdr sidebar, with a pane to reclaim disk. |
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
| [**agnostk/herdr-ai-usagebar**](https://github.com/agnostk/herdr-ai-usagebar) | Shows plan usage from ai-usagebar for Claude, Codex, Copilot, and other agents in the Herdr TUI sidebar. Each agent row shows its own plan and each workspace row sums its agents. |
| [**mikitahimpel/herdr-agent-tokens**](https://github.com/mikitahimpel/herdr-agent-tokens) | Shows a ratatui dashboard of token usage for every Claude Code and Codex agent in a Herdr TUI session. |
| [**PurrlyDigital/subscription-watcher**](https://github.com/PurrlyDigital/subscription-watcher) | Shows remaining Claude Code and Codex allowance in the Herdr TUI sidebar, refreshed hourly and themed to match. Read-only. |
| [**kalbhor/herdr-usage**](https://github.com/kalbhor/herdr-usage) | Opens a popup in Herdr TUI with one progress bar per rate-limit window and its reset time, for Claude Code and Codex subscriptions. |
| [**Kamyil/herdr-usage-popup**](https://github.com/Kamyil/herdr-usage-popup) | Opens a Herdr TUI popup with plain bars for the quota windows your agent CLIs already track, grouped by provider. |
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
| [**luongnv89/mcc-herdr-plugin**](https://github.com/luongnv89/mcc-herdr-plugin) | Shows the 5-hour and weekly Claude Code usage of every mcc account in a Herdr pane under the agent list. Includes a Herdr app mod. |
| [**NaturaAurum/herdr-ai-usage**](https://github.com/NaturaAurum/herdr-ai-usage) | Opens a right-side Herdr panel showing remaining plan limits for Claude, Codex, OpenCode Go, Cursor, and Grok, with linked extra accounts. |
| [**Audectra/herdr-claude-usage**](https://github.com/Audectra/herdr-claude-usage) | Shows Claude 5-hour and weekly subscription usage in the Herdr tab bar, with a warning mark near the limit. |
| [**turbokast/quotahop · plugins/herdr**](https://github.com/turbokast/quotahop/tree/main/plugins/herdr) | Shows Claude, Codex, and Muse subscription quota remaining in a live Herdr split and suggests which Claude subscription to use next. Needs the QuotaHop command-line tool from the same repository. |
| [**EMRahman/herdr-usage-monitor**](https://github.com/EMRahman/herdr-usage-monitor) | Shows percent of subscription allowance remaining in the Herdr tab bar, with a modal for limits and reset countdowns. Covers Claude Code, Codex, Cursor, Grok, Copilot, and more. |
| [**shaanardev/herdr-godex-cost**](https://github.com/shaanardev/herdr-godex-cost) | Shows estimated cost or credit usage for each Codex pane in Herdr, including nested subagents, from local session data. |
| [**fluzzy/herdr-quotaribbon**](https://github.com/fluzzy/herdr-quotaribbon) | Shows Claude Code and Codex subscription usage and time to reset on the right of the Herdr tab bar, as used or remaining. |
| [**pseudovar/herdr-plugin-token-usage**](https://github.com/pseudovar/herdr-plugin-token-usage) | Shows each agent's spend, GitHub Copilot credits, context gauge, and burn rate in the sidebar. Reads local usage records for several coding agents. |
| [**cduguet/herdr-quota-sidebar**](https://github.com/cduguet/herdr-quota-sidebar) | Shows Claude Code and Codex weekly subscription quota in the Herdr TUI tab bar with a usage bar and time until reset. Can add daily Kataleptic spend. |
| [**cyrill62/herdr-quota-monitor**](https://github.com/cyrill62/herdr-quota-monitor) | Shows usage and quotas for coding agents such as Claude Code and Codex and for LLM provider APIs, in a Herdr TUI tab-bar summary and a dashboard. Runs on Linux, macOS and Windows. |
| [**doldola/herdr-llm-usage**](https://github.com/doldola/herdr-llm-usage) | Shows 5-hour and weekly usage for every saved Claude Code and Codex account in a Herdr TUI panel and the sidebar. Switches accounts live and can auto-switch when a limit is near. |
| [**medden/herdr-agents-usage**](https://github.com/medden/herdr-agents-usage) | Shows Claude and Codex subscription usage in the Herdr TUI tab bar, read from Omarchy agent usage records. |
| [**ontionos/tokenrate**](https://github.com/ontionos/tokenrate) | Shows a terminal dashboard of Claude Code and Codex token use with an API price estimate, hourly or over 7 to 90 days, built on ccusage. Runs as a Herdr TUI overlay or fixed tab. |
| [**vrwolf1004/herdr-ai-feedbag**](https://github.com/vrwolf1004/herdr-ai-feedbag) | Shows Claude Code, GitHub Copilot, OpenAI Codex and Gemini CLI usage in one block at the bottom of the Herdr TUI Agents sidebar, with a dashboard pane. |
| [**tjs0/herdr-agent-usage**](https://github.com/tjs0/herdr-agent-usage) | Shows Claude Code, Codex and agy 5-hour and 7-day rate limits in a popup and the tab bar, and per-pane context fill in the Herdr TUI sidebar. Linux only. |
| [**HungNth/herdr-cliproxyapi-quotas**](https://github.com/HungNth/herdr-cliproxyapi-quotas) | Shows CLIProxyAPI account quotas and version status in a Herdr TUI tab or split, refreshing automatically without using any quota. Written in Go. |
| [**rskull/herdr-ccusage**](https://github.com/rskull/herdr-ccusage) | Shows each Claude Code session's cost and token usage in the Herdr TUI sidebar as pane metadata tokens, computed by ccusage. |
| [**alizdavoodi/herdr-context-usage**](https://github.com/alizdavoodi/herdr-context-usage) | Shows how full each coding agent's context window is in the Herdr TUI sidebar and exposes it through the herdr CLI for other agents. Supports Claude Code, Codex, OpenCode, pi, omp and Hermes. |
| [**akhilnalliboina/claude-usage-statusline**](https://github.com/akhilnalliboina/claude-usage-statusline) | Adds a Claude Code status line with model, prompt-cache countdown, context tokens, session cost, and 5-hour and 7-day usage percentages. Installs and sets up through the Herdr TUI plugin installer. |
| [**martin-saldinger/herdr-claude-limits**](https://github.com/martin-saldinger/herdr-claude-limits) | Polls your Claude plan usage limits and shows a summary in the Herdr TUI tab bar and a popup with all limits. |
| [**varvand/herdr-plugin-quota-sidebar**](https://github.com/varvand/herdr-plugin-quota-sidebar) | Adds Claude Code, Codex and Grok account quota gauges to the last card of the Herdr TUI Agents sidebar on macOS. Takes its numbers from kwanwooi25/herdr-plugin-agent-quota and needs sidebar tokens added to your Herdr config. |
| [**danielleit241/herdr-usage**](https://github.com/danielleit241/herdr-usage) | Shows 5-hour and weekly subscription usage per provider in the Herdr TUI agents sidebar, colored by level with reset times. |
| [**tunaunuvar/herdr_usage_plugin**](https://github.com/tunaunuvar/herdr_usage_plugin) | Opens a Herdr TUI popup that detects 19 AI CLIs and shows live quota bars for Codex, Claude Code, OMP, and OpenRouter, plus reset times. |
| [**EdTheBearded/herdr-usage**](https://github.com/EdTheBearded/herdr-usage) | Shows usage-limit gauges from OAuth logins in the Herdr TUI Agents sidebar, using numbers the provider reports rather than local estimates. |
| [**danielfalci/herdr-codex-auto-retry**](https://github.com/danielfalci/herdr-codex-auto-retry) | Watches Codex panes for a usage-limit message with a reset time, waits, then sends a continuation prompt into the same pane. Does not bypass limits. |
| [**aman0singh/herdr-subs**](https://github.com/aman0singh/herdr-subs) | Detects Claude, Codex, Pi, and OpenCode subscriptions and shows them in the Herdr sidebar. |
| [**ummoftgo/herdr-quota-theme**](https://github.com/ummoftgo/herdr-quota-theme) | Colors the herdr-agent-quota sidebar text with your current Herdr TUI theme palette without modifying the quota plugin. |
| [**caoool/herdr-sidebar-plugin**](https://github.com/caoool/herdr-sidebar-plugin) | Adds a right-hand Herdr TUI sidebar with subscription quota per agent and a live session section for Claude Code, Codex, and Grok. |

### Output inspection, logs, and transcripts

*67 projects. Tools for searching, cleaning, exporting, or reviewing pane output and agent conversations.*

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
| [**dmazlum/herdr-fleece**](https://github.com/dmazlum/herdr-fleece) | Frames the last answer of a Claude Code or Codex agent as rendered Markdown, then copies, saves or sends it. A dock pane lists edited files and the code, commands, paths and links from recent turns, and one key copies or opens each. |
| [**kaar/herdr-fzf-url**](https://github.com/kaar/herdr-fzf-url) | Finds URLs in Herdr TUI pane scrollback with fzf and opens the selected URL. |
| [**ofirgall/extrakto-herdr**](https://github.com/ofirgall/extrakto-herdr) | Extracts paths, URLs, words, and other text from a Herdr TUI pane for fuzzy selection with fzf. |
| [**hunter9x/herdr-logging**](https://github.com/hunter9x/herdr-logging) | Captures, saves, and clears Herdr TUI pane output using pane logging and screen-capture actions. |
| [**rotemb-wond/herdr-copy-hints**](https://github.com/rotemb-wond/herdr-copy-hints) | Places short keyboard labels over visible paths, commit hashes, and URLs. Typing a label copies the matching text to the system clipboard. |
| [**alexjsp/herdr-scrollback-capture**](https://github.com/alexjsp/herdr-scrollback-capture) | Saves the focused pane's scrollback as a colored, self-contained HTML file or plain text, with configurable path, filename, and theme. |
| [**x0d7x/herdr-fzf-url**](https://github.com/x0d7x/herdr-fzf-url) | Reads visible content from every Herdr pane, extracts and deduplicates URLs, and sends them to fzf. Enter opens the selected URL, while `y` copies it. |
| [**silencechung/herdr-subagent-watch**](https://github.com/silencechung/herdr-subagent-watch) | Watches Claude Code sub agents live in a popup viewer and a sidebar tree in Herdr TUI. Reads Claude Code transcripts and needs only Node.js. |
| [**reganpark/maeklog**](https://github.com/reganpark/maeklog) | Adds a Herdr TUI side panel that records decisions, progress, blockers and next actions for Codex sessions, kept per tab, repository and branch. Includes source quotes and timestamps. |
| [**antoniocosta/turnr**](https://github.com/antoniocosta/turnr) | Lists the turns of an agent in a side panel so you can click one to scroll the pane to that prompt. Works with Claude Code, Codex, pi, and Antigravity CLI. |
| [**kkjdaniel/herdr-gh-runs**](https://github.com/kkjdaniel/herdr-gh-runs) | Shows your GitHub Actions runs in a small Herdr TUI pane that follows the repo you work in. Streams live progress, step logs, and notifications. |
| [**shindakun/herdr-testrun**](https://github.com/shindakun/herdr-testrun) | Runs a project test suite in a Herdr TUI pane, lists the failures and sends them to the workspace agent with one key. Supports Go, Cargo, Jest, Vitest, node --test and Pytest. |
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
| [**DieVerwandlungTK/conv-tree**](https://github.com/DieVerwandlungTK/conv-tree) | Shows Claude Code conversations as a tree of prompts in a Herdr pane. Lets you fork from any past prompt or merge a branch into another. |
| [**siyuanseever/statetrail · herdr**](https://github.com/siyuanseever/statetrail/tree/main/herdr) | Docks a trail of each Claude Code turn next to the agent in Herdr, with one row per turn and click to scroll there. The same repo also has a tmux version. |
| [**homur/herdr-recap**](https://github.com/homur/herdr-recap) | Opens a popup recap of what each Claude Code agent in your Herdr session was doing and what comes next, with no AI calls. |
| [**maromocooo/patchreplay**](https://github.com/maromocooo/patchreplay) | Records before and after browser runs of an agent's change and produces a replay GIF and a Markdown block for a PR. Runs automatically when a Herdr agent finishes a turn. |
| [**NazzarenoGiannelli/sidecr**](https://github.com/NazzarenoGiannelli/sidecr) | Summons a companion window showing the Claude Code conversation of the focused pane, with Markdown answers, attachments, and clickable links. Lets you reply from the window and dismiss it. |
| [**levx-me/steading**](https://github.com/levx-me/steading) | Shows an agent's builds, tests, git, deploys, dev servers, and subagents in one live deck beside it in Herdr. |
| [**Icekamonday/herdr-claude-copy**](https://github.com/Icekamonday/herdr-claude-copy) | Copies code blocks from Claude Code answers without screen indent or line breaks. Can paste the commands into Claude's prompt box or a shell in the tab. |
| [**pararang/herdr-subagent-streamer**](https://github.com/pararang/herdr-subagent-streamer) | Streams each OMP subagent's prompts, thinking, tool calls and results into its own Herdr TUI split with a live agent graph. Also works with tmux. |
| [**catlee/herdr-snatch**](https://github.com/catlee/herdr-snatch) | Opens an fzf picker over text visible in Herdr TUI panes, such as paths and URLs. Inserts, copies or opens the selected item. |
| [**huluhuluu/herdr-graph**](https://github.com/huluhuluu/herdr-graph) | Browses saved Codex and Claude Code sessions inside the Herdr TUI, with fork trees, full-text search, a conversation reader and session renaming. |
| [**speardragon/herdr-db**](https://github.com/speardragon/herdr-db) | Shows every MongoDB MCP call made by Claude Code or Codex as a Compass-style view with the query, returned documents and before and after diffs of writes, in a native macOS window. |
| [**tatoalo/herdr-remote-open-url**](https://github.com/tatoalo/herdr-remote-open-url) | Lets you Ctrl+click or pick a URL from a Herdr TUI pane. Opens a browser where the host has one and copies the URL to your local clipboard over SSH. |
| [**lijianding/herdr-prompt-history**](https://github.com/lijianding/herdr-prompt-history) | Adds a prompt history viewer, a workspace and tab tree navigator, and an active agent task syncer to the Herdr TUI. |
| [**tunaunuvar/herdr_skills_plugin**](https://github.com/tunaunuvar/herdr_skills_plugin) | Opens a Herdr TUI popup listing installed AI skills, observed skill usage, tools, and git status for each session, on Windows, macOS, and Linux. |
| [**Somliga/herdr-context**](https://github.com/Somliga/herdr-context) | Draws every Claude Code session in a repo as one tree of sessions, branches, and turns in the Herdr TUI, with editing of session context such as branching from a turn. |
| [**mlalewicz/herdr-explain**](https://github.com/mlalewicz/herdr-explain) | Explains or fixes the last shell error in a pane using a local OpenAI-compatible LLM. The fix is typed into the pane for you to confirm. |
| [**yafeishi/herdr-session-history**](https://github.com/yafeishi/herdr-session-history) | Adds a per-pane rail listing the turns of the current agent session and jumps Grok scrollback to the selected prompt. |
| [**Castrozan/herdr-pace**](https://github.com/Castrozan/herdr-pace) | Turns a completed agent reply into a centered speed reader that opens paused with a countdown and adjustable word speed. |
| [**VulpesZerda27/omarchy-workbench**](https://github.com/VulpesZerda27/omarchy-workbench) | Shows each Herdr TUI thread's agent-written brief, outputs and capture link in a companion pane beside the conversation. Pairs with the Workbench desk for Omarchy, which adds an output shelf, note and screenshot capture, and a GitHub issue desk. |

### Agent visualizations and terminal games

*34 projects. Interactive terminal visualizations and games for following agents.*

| Project | What it does |
|---|---|
| [**michaellandi/herdr-office**](https://github.com/michaellandi/herdr-office) | Draws Herdr TUI agents as office characters and signals when an agent needs approval. |
| [**aorumbayev/herdr-canvas**](https://github.com/aorumbayev/herdr-canvas) | Opens a mouse-driven ASCII diagram canvas in a Herdr split. Humans draw boxes, lines, and text; agents read and edit the same JSON-backed diagrams through the CLI and skill. |
| [**devangchhajed/herdr-pixel-office**](https://github.com/devangchhajed/herdr-pixel-office) | Shows Herdr TUI agents as pixel-art office characters that change activity with agent status and tool calls. |
| [**takemo101/wave-tui**](https://github.com/takemo101/wave-tui) | Plays internet radio in a terminal and visualizes Herdr TUI agents in an interactive Agent Planets view. |
| [**Efeguclu1/herdr-town**](https://github.com/Efeguclu1/herdr-town) | Renders Herdr coding agents as an interactive 8-bit town inside a pane and lets users read or answer them. |
| [**opsydyn/herdr-questmancer**](https://github.com/opsydyn/herdr-questmancer) | Shows live Herdr TUI agents and their states as a 16-bit fantasy guild. |
| [**JYasha11/herdr-in-your-face**](https://github.com/JYasha11/herdr-in-your-face) | Shows an increasingly urgent ASCII-art face when a Herdr agent is blocked and waiting for input, making overlooked approvals difficult to miss. |
| [**suisya-systems/herdr-agent-office**](https://github.com/suisya-systems/herdr-agent-office) | A terminal pixel-art office where Herdr agents appear as animated desk workers, blocked agents raise timed alerts, and selecting a character focuses its pane. |
| [**yuya-take/herdr-starkeep**](https://github.com/yuya-take/herdr-starkeep) | Draws the agents running in Herdr as knights on an orbital training ship, with one room per space and subagents shown as apprentices. Reads agent state from the Herdr socket and subagent events from a Claude Code hook. |
| [**pvgomes/agent-visualizer**](https://github.com/pvgomes/agent-visualizer) | Shows coding agents as workers in a pixel-art office, one desk per agent. In herd mode the office lists the agents in Herdr panes, poses them by Herdr state, and can open or start agents in Herdr workspaces. |
| [**martinkozle/excaliagent**](https://github.com/martinkozle/excaliagent) | Shows your Claude Code, Codex and OpenCode sessions as cards on an Excalidraw canvas. Cards show live status and can jump to the matching Herdr pane. |
| [**SerHappy/herdr-achievements**](https://github.com/SerHappy/herdr-achievements) | Awards achievements and celebrations for completed tasks across your Herdr AI agent herd. |
| [**tatsuro-ueda/recess**](https://github.com/tatsuro-ueda/recess) | Plays a video while your agents work and pauses it to bring you back to the terminal when Herdr TUI calls. Runs on macOS 14 or later. |
| [**KantaKan/herdr-fantasy**](https://github.com/KantaKan/herdr-fantasy) | Shows coding agents as a fantasy RPG party in a Herdr TUI pane that fights slimes and bosses mirroring real agent activity. Agents that need you speak in a JRPG dialogue box. |
| [**madebygrant/herdr-matrix**](https://github.com/madebygrant/herdr-matrix) | Renames Herdr TUI agents after Matrix agents like smith and brown, sets Matrix-style status text, numbers spaces, and runs digital rain when idle. |
| [**giorgiostokje/herdr-arcade**](https://github.com/giorgiostokje/herdr-arcade) | Plays seventeen classic terminal arcade games in a Herdr popup pane that pauses itself when an agent needs attention. Python standard library only. |
| [**chantlong/herdr-habitat**](https://github.com/chantlong/herdr-habitat) | Displays a terminal habitat where plants and wildlife evolve alongside Herdr TUI agent activity. |
| [**marius-se/herdr-brainrot**](https://github.com/marius-se/herdr-brainrot) | Runs terminal games and distraction apps such as DOOM in a dedicated Herdr pane while agents continue working in neighboring panes. Additional apps can be configured through the plugin manifest. |
| [**m16khb-org/herdr-agents-graph**](https://github.com/m16khb-org/herdr-agents-graph) | Shows a live graph of the focused agent pane's session: main agent, spawned subagents, current tools, and failures. Reads Claude Code, Codex, and omp sessions. |
| [**fenixc9/herdr-word-practice**](https://github.com/fenixc9/herdr-word-practice) | Shows one vocabulary card on a key press in the Herdr TUI between coding sessions, with spaced repetition and typing recall. Bundles 7085 words in pure Python. |
| [**NathanFirmo/herdr-agent-meet**](https://github.com/NathanFirmo/herdr-agent-meet) | Shows every Herdr TUI agent as a participant in a video-call UI that summarizes new output and speaks it aloud with captions. |
| [**federbenjamin/sound-mod · herdr-plugin**](https://github.com/federbenjamin/sound-mod/tree/main/herdr-plugin) | Plays a song as four instrument stems that fade in as more agents in Herdr TUI are working. Counts agent panes on this Mac and on saved machines. |
| [**vrwolf1004/herdr-tetris**](https://github.com/vrwolf1004/herdr-tetris) | Adds Tetris, Ladder, Snake and Minesweeper to a Herdr TUI dock workspace, alongside a fake system monitor. |
| [**exterkamp/herdr-tarot**](https://github.com/exterkamp/herdr-tarot) | Draws one pixel-art tarot card a day from the 1909 public-domain deck in a Herdr TUI pane and shows its meaning, including reversed readings. |
| [**lakeinlake/herdr-agent-world**](https://github.com/lakeinlake/herdr-agent-world) | Shows your coding agents as animated characters, with 30 bundled Pokemon and Forest, Coast and Town scenes, reflecting live activity in a Herdr workspace. |
| [**wasamin0130/TeamNest**](https://github.com/wasamin0130/TeamNest) | Turns the agents running in Herdr TUI panes into a visible team with avatars, moods, dialogue, and voice, with Claude Code and Codex adapters. |
| [**AFetisa/herdr-murmur**](https://github.com/AFetisa/herdr-murmur) | Shows running coding agents as a live org chart with who spawned whom, cost by model, context load, instruction files, and hooks. Includes approve and interrupt controls and runs locally with no dependencies. |
| [**Mozart2234/herdr-agent-pulse**](https://github.com/Mozart2234/herdr-agent-pulse) | Animates pane borders, adds state icons to tab labels, and shows a tab-bar summary while coding agents work. Includes iTerm and Naruto themes. |
| [**YungeG/herdr-sketch**](https://github.com/YungeG/herdr-sketch) | Opens an editable graph canvas shared by you and an agent, with comments on nodes and edges, visual revision review, and explicit human acceptance. The README is in Chinese. |
| [**ikundasdas/herdr-**](https://github.com/ikundasdas/herdr-) | Shows a pixel desktop pet that reacts when agents finish, think, or wait for confirmation, and jumps to the latest notified task on click. Windows only and the README is in Chinese. |
| [**corygforsythe/firstmate-herdr-amp**](https://github.com/corygforsythe/firstmate-herdr-amp) | Opens a WinAmp-style pane for playing MP3 and MIDI files with transport controls, seek bar, volume, and a playlist. |
| [**maaalo/herdr-markmap**](https://github.com/maaalo/herdr-markmap) | Builds a live Markmap mind map of an agent's conversation in the browser, merging new turns after each reply without touching the agent's context. Watches Claude Code session files read-only. |
| [**jlapenna/dev · herdr/overview**](https://github.com/jlapenna/dev/tree/main/herdr/overview) | Shows a live grid of every Herdr TUI agent in one tab, across the local session and saved machines, in overview or live-attach mode. Installs with herdr plugin install jlapenna/dev/herdr/overview. |
| [**corygforsythe/herdr-flight-radar**](https://github.com/corygforsythe/herdr-flight-radar) | Provides real-time ADS-B flight radar TUI backed by dump1090. |

### Herdr TUI themes and appearance

*19 projects. Themes and visual customizations for the Herdr TUI.*

| Project | What it does |
|---|---|
| [**qintmb/herdr-theme-picker**](https://github.com/qintmb/herdr-theme-picker) | Applies terminalcolors.com palettes to Herdr TUI interface elements through a popup theme picker. |
| [**promptegrity/grok-themes · herdr**](https://github.com/promptegrity/grok-themes/tree/HEAD/herdr) | Applies GrokNight or GrokDay colors to the Herdr TUI and adds an optional powerline-style branch indicator. |
| [**ariel-ps/herdr-colors**](https://github.com/ariel-ps/herdr-colors) | Assigns distinct color slots to Herdr TUI panes and can repaint existing panes. |
| [**magimetal/matrix-themes · herdr**](https://github.com/magimetal/matrix-themes/tree/HEAD/herdr) | Applies a Matrix-inspired green palette to the Herdr TUI using a configuration snippet. |
| [**AkashJana18/zenbones-herdr**](https://github.com/AkashJana18/zenbones-herdr) | Adds 23 zenbones color themes with light and dark variants to Herdr TUI. |
| [**s3rgiosan/herdr-theme-synthwave-84**](https://github.com/s3rgiosan/herdr-theme-synthwave-84) | Applies the Synthwave '84 neon palette to the Herdr TUI by writing theme tables to config.toml after backing up your previous theme. |
| [**nertzy/herdr-flexoki**](https://github.com/nertzy/herdr-flexoki) | Adds Flexoki light and dark themes to Herdr TUI, including an automatic appearance option. |
| [**sp-night/herdr**](https://github.com/sp-night/herdr) | Adds three São Paulo-inspired dark color palettes to Herdr TUI. |
| [**codingquark/herdr-modus-themes**](https://github.com/codingquark/herdr-modus-themes) | Installs the light Modus Operandi and dark Modus Vivendi palettes for the Herdr TUI. |
| [**Young1108/herdr-cyber-style**](https://github.com/Young1108/herdr-cyber-style) | Applies a dark cyber theme and workspace layout to Herdr TUI on macOS, with a backup of the previous configuration. |
| [**mastnacek/herdr-theme**](https://github.com/mastnacek/herdr-theme) | Switches Herdr TUI themes from a popup picker with live preview and a dark and light toggle. Syncs the host terminal colours over OSC 10 and 11 and can rotate themes by time of day. |
| [**ernsahin/herdr-fonts**](https://github.com/ernsahin/herdr-fonts) | Opens a picker in the Herdr TUI to choose a monospace font and size, with undo and adapters for supported terminals. Runs on macOS and Linux. |
| [**xeno/herdr-neon-ink**](https://github.com/xeno/herdr-neon-ink) | Applies a neon-on-charcoal color theme to the Herdr TUI through a plugin action or a pasteable config snippet. |
| [**pangpond/herdr-theme-cobalt2**](https://github.com/pangpond/herdr-theme-cobalt2) | Applies the Cobalt2 palette to the Herdr TUI chrome and adds harness logo marks to agent rows through a bundled font. |
| [**enisbu/herdr-kitty-theme-sync**](https://github.com/enisbu/herdr-kitty-theme-sync) | Synchronizes the active Herdr TUI theme to kitty’s ANSI palette. |
| [**CydoEntis/chameleon**](https://github.com/CydoEntis/chameleon) | Applies a shared palette to Herdr, Windows Terminal, Oh My Posh, and Claude Code. |
| [**YF-Tobehero/Herdr-palette-probe-for-windows**](https://github.com/YF-Tobehero/Herdr-palette-probe-for-windows) | Measures agent terminal colors and helps choose a Windows Terminal palette for use with Herdr TUI. |
| [**andy-spike/herdr-theme**](https://github.com/andy-spike/herdr-theme) | Syncs the Herdr TUI color palette with the active Omarchy theme and reloads configuration when the theme changes. |
| [**themuuln/herdr-ghostty-theme-sync**](https://github.com/themuuln/herdr-ghostty-theme-sync) | Syncs Herdr TUI colors to the active Ghostty theme and restores sidebar tokens after server restarts. |

### Security guards and collision detectors

*21 projects. Safety monitors that warn of worktree collisions, credential leaks, or destructive edits.*

| Project | What it does |
|---|---|
| [**termaxa/termaxa · herdr-plugin**](https://github.com/termaxa/termaxa/tree/main/herdr-plugin) | Runs Claude Code or Codex under Termaxa command policies in Herdr TUI and shows refusals and audit records. |
| [**schemaitat/herdr-nono-plugin**](https://github.com/schemaitat/herdr-nono-plugin) | Runs OpenCode in nono sandboxes from Herdr TUI on Linux, with separate client and server profiles. |
| [**mcc0x/herdr-redact**](https://github.com/mcc0x/herdr-redact) | Warns when an agent pane has printed credentials before screenshots, streaming, or chat paste operations occur. |
| [**StructuPath/herdr-guard**](https://github.com/StructuPath/herdr-guard) | Monitors Herdr TUI panes for configured command-policy violations and can interrupt matching commands. An optional Claude Code hook checks tool calls before execution. |
| [**mcc0x/herdr-collide**](https://github.com/mcc0x/herdr-collide) | Warns when agents working in separate Git worktrees of the same repository are about to collide or conflict. |
| [**asumaran/asconfirmclose**](https://github.com/asumaran/asconfirmclose) | Closes an idle Herdr TUI pane immediately but asks for confirmation when a foreground process is running. |
| [**zenodea/fence**](https://github.com/zenodea/fence) | Turns a Herdr TUI space into a sandboxed pen where every shell can write only the pen folder and reach allowed domains. Uses bubblewrap and nftables on Linux. |
| [**IniZio/nexus · plugins/herdr**](https://github.com/IniZio/nexus/tree/main/plugins/herdr) | Attaches Herdr TUI to nexus microVM sandboxes, listing and creating them from the plugin, with auto port forwarding. Sandboxes are Cloud Hypervisor VMs on Linux with credentials kept on the host. |
| [**pauljohnchamberlain/herdr-guard**](https://github.com/pauljohnchamberlain/herdr-guard) | Lets coding agents inspect Herdr TUI sessions and make guarded workspace renames or close eligible inactive work. |
| [**cheunglok97/close-guard**](https://github.com/cheunglok97/close-guard) | Asks for confirmation before closing a Herdr TUI tab or pane. |
| [**BlockedPath/herdr-plugin**](https://github.com/BlockedPath/herdr-plugin) | Inspects Herdr TUI plugin execution paths before installation and reports execution evidence and unknowns. |
| [**sangimed/firstmate-homelab**](https://github.com/sangimed/firstmate-homelab) | Provides a self-hosted Docker stack for Firstmate, Herdr and Codex agents. |
| [**stanlee7/lastclick**](https://github.com/stanlee7/lastclick) | Holds irreversible agent steps such as post, send, or pay in a queue with a screenshot and the effect, and shows an approval overlay in Herdr. Approve or reject with a key. |
| [**0xArchiviste/herdr-memory-guard**](https://github.com/0xArchiviste/herdr-memory-guard) | Hibernates long-idle Herdr agent threads on Linux and WSL when memory runs low, keeping native sessions so they can resume. Starts in observation mode and logs the reason for every decision. |
| [**Gustavobelfort/herdr-sudo-askpass**](https://github.com/Gustavobelfort/herdr-sudo-askpass) | Opens the sudo password prompt in a pane beside the agent when a coding agent runs sudo. Works over SSH and from a phone, and Ctrl+C refuses the request. |
| [**nizarfadlan/herdr-kata-plugin**](https://github.com/nizarfadlan/herdr-kata-plugin) | Runs each Herdr agent pane's coding agent, Codex by default, inside its own Kata Containers microVM instead of on the host. Linux only. |
| [**joshka0/pi-vm**](https://github.com/joshka0/pi-vm) | Runs the pi coding agent in a Cloudflare Containers or local VM sandbox where API keys stay outside, and wakes, sleeps and removes those agents as Herdr machines. Targets macOS. |
| [**rubenmarcus/herdr-tower**](https://github.com/rubenmarcus/herdr-tower) | Prevents agents from clobbering the same checkout in the Herdr TUI with atomic checkout leases, a live board of holders, and a settle journal. |
| [**dartyuhov/herdr-safe-close**](https://github.com/dartyuhov/herdr-safe-close) | Asks for confirmation before closing a Herdr TUI tab and restores the most recently closed tab. |
| [**utahta/herdr-codex-confirm**](https://github.com/utahta/herdr-codex-confirm) | Opens a Herdr TUI popup to approve once, deny, or deny with feedback for Codex shell commands that match your patterns, through a Codex PreToolUse hook. |
| [**Javamomma/herdr-approval-gate**](https://github.com/Javamomma/herdr-approval-gate) | Runs a task in its own Herdr TUI pane and blocks it until a human types APPROVE when an independent checker command does not pass cleanly. Writes every outcome to an append-only audit log. |

### Plugin collections, frameworks, and ready-made configs

*49 projects. Plugin bundles, shared libraries for plugin authors, and ready-made Herdr configurations to install and adapt.*

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
| [**peteretelej/herdr-plugins**](https://github.com/peteretelej/herdr-plugins) | Collects four Herdr TUI plugins, each installable on its own: agent-tab-name for topic-based tab names, notify for Telegram alerts, opencode-cost-tokens, and herdr-fleet for dispatching consultation workers as panes. |
| [**thejiajun/jc-herdr-plugins**](https://github.com/thejiajun/jc-herdr-plugins) | Collects Herdr plugins that name workspaces from agent conversations and search or switch between agents. |
| [**shelken/herdr-plugins**](https://github.com/shelken/herdr-plugins) | Collects Herdr TUI plugins for launching Pi agents and resuming Pi sessions. |
| [**narumiruna/herdr-plugins**](https://github.com/narumiruna/herdr-plugins) | Collects independently installable Herdr TUI plugins, including a GitHub pull-request viewer. |
| [**oullin/herdr-plugins**](https://github.com/oullin/herdr-plugins) | Collects independently installable Herdr TUI plugins for navigation, agent awareness, and terminal workflows. |
| [**alastairsounds/herdr-plugins**](https://github.com/alastairsounds/herdr-plugins) | Collects Herdr TUI plugins in independently installable subdirectories. |
| [**crisap94/herdr-plugins**](https://github.com/crisap94/herdr-plugins) | Collects Herdr plugins that install separately with `herdr plugin install crisap94/herdr-plugins/<plugin>`. Currently ships tab-recap, a rolling recap column beside every tab with an agent. |
| [**wellavelino/gaucho**](https://github.com/wellavelino/gaucho) | Bundles bash plugins for guiding many agents: an agent inbox, issue dispatch, fleet board, landing review, second opinion, stuck detector, and worktree cleanup. Includes Herdr app mods and a hub popup with live counts. |
| [**VladPatr96/herdr-plugins**](https://github.com/VladPatr96/herdr-plugins) | Collects Herdr TUI plugins for per-agent hotkeys, delegating tasks to whole agent sessions in their own tab, and a quota board for Claude Code, Codex, OpenCode and DeepSeek. |
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
| [**antonyjaen/herdr-plugins**](https://github.com/antonyjaen/herdr-plugins) | Collects Herdr plugins for Supabase and Vercel CLI menus, declarative workspace layouts, dictation, and a file browser, all running on Windows, macOS, and Linux. |
| [**IMSike/Herdr-Plugins**](https://github.com/IMSike/Herdr-Plugins) | Collects two Herdr TUI plugins: a menu that opens tools like lazygit or gh-dash from a Tools pane or popup, and a sidebar that shows a workspace-to-agents tree with CPU and memory counts. Each installs from its own folder. |
| [**princesshu/herdr-fold**](https://github.com/princesshu/herdr-fold) | Bundles a file sidebar, search, git and GitHub issues, AI session browser, and AI commit messages for Claude Code and Codex in Herdr. Installs for the TUI or as a Herdr app mod and reaches SSH machines. |
| [**kadaliao/herdr-plugins**](https://github.com/kadaliao/herdr-plugins) | Collects sidebar and tab-bar plugins: space and agent numbering for prefix shortcuts, a status bar with network, battery, CPU, and memory, and a yazi file manager toggle. Each installs separately. |
| [**justmytwospence/herdr-plugins**](https://github.com/justmytwospence/herdr-plugins) | Collects four Herdr plugins: compact git status on spaces, undo for closed panes, tabs and spaces, an agent cycle order for next_agent, and alphabetical space sorting. |
| [**Jorgeescribanogarcia/jeg-herdr-toolkit**](https://github.com/Jorgeescribanogarcia/jeg-herdr-toolkit) | Bundles a git-aware file viewer with Markdown preview, agent status icons, paste-as-paths for files and clipboard images, and a plugin marketplace with update checks. |
| [**GravionLabs/herdr-plugins**](https://github.com/GravionLabs/herdr-plugins) | Bundles Herdr TUI plugins for the deliver agent workflow, such as a PR board, agent notifications, worktree cleanup, a command palette and a repo opener. Each plugin installs from its own folder at a release tag. |
| [**nakamotosai/herdr-agent-plugins**](https://github.com/nakamotosai/herdr-agent-plugins) | Bundles three Windows-capable Herdr TUI plugins in plain Node: an omp token and cost pane, an agent conversation log and a recurring task runner. Each installs from its own folder. |
| [**brachkow/herdr-plugins**](https://github.com/brachkow/herdr-plugins) | Collects four Herdr TUI plugins that install separately: workspace listening ports, tab autonaming, uncommitted file counts, and the GitHub pull request number of each branch. |
| [**programmarchy/herdr-plugins**](https://github.com/programmarchy/herdr-plugins) | Collects two Herdr TUI plugins: ambient sound cues for Claude Code and Codex on macOS, and an email bridge that forwards AgentMail messages to a workspace tab. |
| [**therealhieu/herdr-plugins**](https://github.com/therealhieu/herdr-plugins) | Collects two Herdr TUI plugins: stacked panes where the focused pane expands and siblings collapse to strips, and Git worktree sidebar tokens for repo, dirty count, branch, and sync. |
| [**Wyatth7/herdr**](https://github.com/Wyatth7/herdr) | Provides a collection of Herdr configurations and reusable plugins. |
