# AGENTS.md

Working rules and language guidelines for anyone — human or agent — editing this repository. It is a curated, plain-English index of the [Herdr](https://github.com/ogulcancelik/herdr) ecosystem. Keep it lean, minimalist, and immediately useful.

---

## 1. Project Philosophy & Minimalist Structure

- **No Onboarding Tutorials:** Do not add introductory installation essays, "how to choose your layer" tables, or getting-started walkthroughs to the catalog root. Keep the README strictly minimalist: title, official links, Table of Contents with counts, and direct jump links into the tables.
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

Organize projects across the 7 numbered domains and their plain-English micro-categories:

1. **Run and orchestrate agents**
   - Official skill and foundation
   - Multi-agent fleets and supervisors
   - Claude Code multi-agent teams
   - Pi supervisor workflows and extensions
   - Subagent launchers and delegation
   - Autonomous coding and pull-request loops
   - Task queues, backlogs, and event triggers
   - General workflows and skill packs

2. **Connect through MCP and the socket API**
   - MCP servers
   - Socket API clients and SDKs
   - Chat alerts: Telegram, Discord, and Slack
   - Desktop, mobile, and webhook notifications
   - Telemetry, events, and quota streaming
   - Voice, hardware, and remote bridges
   - Protocol and third-party bridges

3. **Editor integrations**
   - Neovim navigation and splits
   - Full Neovim-hosted workspaces
   - VS Code, Cursor, and dev containers
   - Vim, Kakoune, and other editors
   - REPL and code dispatchers
   - Editor plugins and bridges

4. **Switch and restore sessions**
   - Fuzzy session switchers and terminal pickers
   - Persistence, snapshots, and state restoration
   - Workspace and multi-session management

5. **Worktrees and terminal experience**
   - Git worktree automation
   - Workspace lifecycle and multi-repository tools
   - Diff review and code inspection
   - File viewers and markdown previews
   - Pane navigation and overlay hints
   - Terminal keybindings and shortcut helpers
   - Command palettes and workspace switchers
   - Status lines, sidebars, and tab synchronization
   - Status overlays, HUDs, and agent timers
   - Context meters and rate-limit gauges
   - Output inspection, logs, and transcripts
   - Dotfiles and ready-made configuration
   - Plugin collections and developer frameworks

6. **Apps, companion integrations, and installation**
   - Native desktop and mobile apps
   - Web dashboards and remote viewers
   - Hardware and ambient displays
   - Plugins and supporting utilities
   - Setup, packages, and version management

7. **Experimental projects**
   - Experiments, concepts, and scaffolds

---

## 5. Before Committing

1. Run `npx markdownlint-cli2 "**/*.md"` — it must exit clean with **0 issues** (same check CI runs).
2. Ensure every internal anchor link resolves correctly.
3. Commit with the conventional commit format: `docs(awesome-list): <summary>`.
