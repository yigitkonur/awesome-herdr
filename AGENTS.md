# AGENTS.md

Working rules and language guidelines for anyone — human or agent — editing this repository. It is a curated, plain-English index of the [Herdr](https://herdr.dev/) ecosystem: the Herdr app, herdr-core, Herdr TUI, and the mobile apps, all under [herdrdev](https://github.com/herdrdev). Keep it lean, minimalist, and immediately useful.

---

## 1. Project Philosophy & Minimalist Structure

- **No Onboarding Tutorials:** Do not add introductory installation essays, "how to choose your layer" tables, or getting-started walkthroughs to the catalog root. Keep the README strictly minimalist: title, official links, the Download Herdr block (platform badges, official store badges in `assets/badges/`, and the install one-liners from herdr.dev/download), Table of Contents with counts, and direct jump links into the tables.
- **Fast Jump Navigation:** Readers should jump straight to the relevant problem domain from the Table of Contents in 1 click.

---

## 2. Project Language & Voice Values

The language of this catalog must be simple, direct, and developer-friendly:

### 2.1. Plain-English, Verb-First Prose

- Lead with active verbs (*Adds*, *Teaches*, *Runs*, *Maps*, *Monitors*, *Filters*, *Connects*, *Orchestrates*, *Embeds*, *Extends*, *Dispatches*).
- Avoid passive constructions, convoluted em-dash chains, and marketing buzzwords (*"ultimate"*, *"blazing fast"*, *"revolutionary"*).
- State clearly what a Herdr user can *do* with the tool, not a laundry list of generic features.

### 2.2. The 1–2 Sentence Rule

Every project entry must be strictly 1 or 2 concise sentences:

- **Sentence 1:** What the tool specifically does for a Herdr user.
- **Sentence 2 (optional):** Key capabilities, supported models/agents (Claude, Pi, Codex, OpenCode), or notable workflows.

### 2.3. Subcategory Header & Table Standards

Every subcategory begins with a count and a 1-sentence summary, followed by a clean 2-column markdown table:

```markdown
### Multi-agent fleets and supervisors

*20 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*

| Project | What it does |
|---|---|
| [**owner/repo**](https://github.com/owner/repo) | Plain-English explanation of what the tool does and who it is for. |
```

---

## 3. Strict Exclusion Criteria (What NEVER Belongs Here)

To maintain a high-signal catalog, the following must **never** be added:

1. **NO Personal Dotfiles:** Generic personal `~/.dotfiles`, chezmoi/stow repos, or personal machine configurations with a `.herdr` config file. Only standalone, packaged, reusable plugins or shareable templates belong in this index.
2. **NO Empty Scaffolds or Incomplete Stubs:** Repositories without working command implementations, design-only documents, or broken builds.
3. **NO Trivial Copy-Paste Wrappers:** Near-duplicate forks or minimal shims without substantive standalone utility.
4. **NO Marketing Hype or AI Filler:** Descriptions must remain factual, concise, and neutral.

---

## 4. Canonical Section Structure

Organize projects across the 8 numbered domains and their plain-English micro-categories:

1. **Run and orchestrate agents**
   - Official Herdr projects and skill
   - Multi-agent fleets and supervisors
   - Swarm, mob, and consensus orchestrators
   - Claude Code multi-agent teams
   - Claude Code: Account switchers and auth monitors
   - Pi supervisor workflows and extensions
   - Pi: Presence, memory, and status extensions
   - Subagent launchers and delegation
   - Autonomous coding and pull-request loops
   - Task queues, backlogs, and event triggers
   - Linear, GitHub Issues, and issue-to-PR automation
   - General workflows and skill packs

2. **Herdr app layouts, mods, and themes**
   - Herdr app layouts
   - Herdr app mods and themes

3. **Connect through MCP and the socket API**
   - MCP servers
   - Socket API and herdr-core clients and SDKs
   - Chat alerts: Telegram, Discord, and Slack
   - Desktop, mobile, and webhook notifications
   - Telemetry, events, and quota streaming
   - Voice, hardware, and remote bridges
   - Protocol and third-party bridges

4. **Editor integrations**
   - Neovim navigation and splits
   - Full Neovim-hosted workspaces
   - VS Code, Cursor, and dev containers
   - Vim, Kakoune, and other editors
   - REPL and code dispatchers
   - Editor plugins and bridges

5. **Switch and restore sessions**
   - Fuzzy session switchers and terminal pickers
   - Persistence, snapshots, and state restoration
   - Workspace and multi-session management

6. **Worktrees and terminal experience**
   - Git worktree automation
   - Workspace lifecycle and multi-repository tools
   - Diff review and code inspection
   - File viewers, terminal browsers, and markdown previews
   - Pane navigation and overlay hints
   - Pane layout management
   - Terminal keybindings and shortcut helpers
   - Command palettes and workspace switchers
   - Status lines and workspace metadata
   - Sidebar displays and tab labels
   - Status overlays, HUDs, and agent timers
   - Context meters and rate-limit gauges
   - Output inspection, logs, and transcripts
   - Agent visualizations and terminal games
   - Herdr TUI themes and appearance
   - Security guards and collision detectors
   - Plugin collections, frameworks, and ready-made configs

7. **Apps, companion integrations, and installation**
   - Native desktop and mobile apps
   - Web dashboards and remote viewers
   - Hardware and ambient displays
   - Plugins and supporting utilities
   - Setup, packages, and version management

8. **Experimental projects**
   - Experiments, concepts, and scaffolds

Herdr app layouts, mods, and themes go in domain 2. Subcategories that collect desktop UIs, mobile clients, web viewers, phone notifications, or app extensions open with a `> Herdr has an official desktop app ... and an official iPhone, iPad, and Android app ...` note under their count line; keep that note at the subcategory level, never inside a row. Tables are ordered by GitHub stars, highest first, except the official subcategory.

---

## 5. Before Committing

1. Run `python3 scripts/sync-counts.py` after adding, moving, or removing rows; it rewrites every count from the tables and lists duplicate repos.
2. Run `npx markdownlint-cli2 "**/*.md"` — it must exit clean with **0 issues** (same check CI runs).
3. Ensure every internal anchor link resolves correctly.
4. Commit with the conventional commit format: `docs(awesome-list): <summary>`.

---

## 6. Finding New Projects

Run `python3 scripts/discover.py` (add `--since YYYY-MM-DD` for the last run date). It writes every Herdr repo that is not in the README yet to `.tmp/candidates.json`, sorted by stars, from three sources:

| Source | What it holds | Product |
|---|---|---|
| `assets.herdr.dev/plugins/index.json` | The TUI plugin marketplace: GitHub repos tagged `herdr-plugin` with a valid `herdr-plugin.toml` | Herdr TUI |
| `herdr.dev/gallery/` | Layouts and mods for the Herdr app; one repo can hold many | Herdr app |
| GitHub topics `herdr`, `herdr-layout`, `herdr-mod`, `herdr-app` | Everything else, including clients, SDKs, and dotfiles | Mixed |

Then triage in batches of about 25 candidates per agent:

1. Read the repo README and file tree. Apply section 3: personal dotfiles, stubs, and thin wrappers are excluded even with many stars.
2. Pick the subcategory from section 4 and write a 1–2 sentence description that follows section 2.
3. Group a gallery repo's layouts and mods into one entry for the repo.
4. Insert the rows, run `python3 scripts/sync-counts.py`, lint, and commit one subcategory batch at a time.

Open pull requests go through the same checks; correct the description or section and merge rather than ask the author.
