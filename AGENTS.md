# AGENTS.md

Working rules and language guidelines for anyone — human or agent — editing this repository. It is a curated, plain-English index of the [Herdr](https://github.com/ogulcancelik/herdr) ecosystem. Keep it lean, simple, and immediately useful.

---

## 1. Project Language & Voice Values

The language of this catalog must be simple, direct, and developer-friendly. Follow these core value entities across all descriptions and sections:

### 1.1. Plain-English, Verb-First Prose

- Lead with active verbs (*Adds*, *Teaches*, *Runs*, *Maps*, *Monitors*, *Filters*, *Connects*).
- Avoid passive constructions, convoluted em-dash chains, and marketing buzzwords (*"ultimate"*, *"blazing fast"*, *"revolutionary"*).
- State clearly what a Herdr user can *do* with the tool, not a laundry list of generic features.

### 1.2. The 1–2 Sentence Rule

Every project entry must be strictly 1 or 2 concise sentences:

- **Sentence 1:** What the tool specifically does for a Herdr user.
- **Sentence 2 (optional):** Key capabilities, supported models/agents (Claude, Pi, Codex, OpenCode), or notable workflows.

### 1.3. Subcategory Header Standards

Every subcategory section begins with a count and a 1-sentence summary:

```markdown
### Multi-agent fleets and supervisors

*51 projects. Higher-level systems that coordinate several agents, roles, tasks, or repositories.*
```

---

## 2. Adding a Project

Add new projects in the appropriate subcategory using the compact bullet format:

```markdown
- **[owner/repo](https://github.com/owner/repo)**: Plain-English explanation of what the tool does and who it is for.
```

- Always use the real GitHub repository URL.
- When the repo name is generic (like `skills` or `herdr-plugins`), write the text as `owner/repo` to prevent ambiguity.
- Do not add trailing language badges or install commands inside the blurb (installation instructions live in the target repo).

---

## 3. Canonical Section Structure

Organize projects across the 7 numbered domains and their plain-English micro-categories:

1. **Run and orchestrate agents**
   - Official skill and foundation
   - Multi-agent fleets and supervisors
   - Subagent launchers and delegation
   - Autonomous coding and pull-request loops
   - Task queues, backlogs, and event triggers
   - General workflows and skill packs

2. **Connect through MCP and the socket API**
   - MCP servers
   - Socket API clients and SDKs
   - Push notifications and webhook alerts
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
   - Diff review and file viewers
   - Pane navigation, keymaps, and hints
   - Command palettes and workspace switchers
   - Status lines, sidebars, and tab synchronization
   - Status overlays, HUDs, and agent gauges
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

## 4. The Bar (Inclusion Criteria)

A project belongs here only if it meets all of the following:

- **Public:** Anyone can access the repository and its documentation.
- **Herdr-specific:** Specifically configures, extends, drives, or teaches Herdr (via CLI, socket API, hooks, skills, or plugin manifest), not a generic terminal multiplexer tool.
- **Documented:** A new user can understand what it does and how to get started.
- **Meaningfully distinct:** Not an empty fork or duplicate upload without added functionality.
- **Factual:** Honest, neutral, and clear about current state and limitations.

*Unfinished, announced, or scaffold-only projects belong under **Experimental projects**, never in the main categories.*

---

## 5. Before Committing

1. Run `npx markdownlint-cli2 "**/*.md"` — it must exit clean with **0 issues** (same check CI runs).
2. Ensure every internal anchor link resolves correctly.
3. Commit with the conventional commit format: `docs(awesome-list): <summary>`.
