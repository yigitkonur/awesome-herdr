# AGENTS.md

Working rules and language guidelines for anyone — human or agent — editing this repository. It is a curated, plain-English index of the [Herdr](https://herdr.dev/) ecosystem: the Herdr app, herdr-core, Herdr TUI, and the mobile apps, all under [herdrdev](https://github.com/herdrdev). Keep it lean, minimalist, and immediately useful.

---

## 1. Project Philosophy & Minimalist Structure

- **No Onboarding Tutorials:** Do not add introductory installation essays, "how to choose your layer" tables, or getting-started walkthroughs to the catalog root. Keep the README strictly minimalist: title, official links, the Download Herdr block (platform badges, official store badges in `assets/badges/`, and the install one-liners from herdr.dev/download), the Table of Contents with counts (each subcategory links into its catalog file), and per domain the 10 most-starred projects with a link to the full list.
- **The catalog lives in `catalog/`:** one file per domain (`catalog/NN-*.md`) holds every entry. Edit those files, never the README tables: `scripts/sync-counts.py` regenerates the README from them. GitHub stops rendering a markdown file past 512 KB, so no single file may hold the whole catalog.
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

Every subcategory begins with a count and a 1-sentence summary, followed by a 3-column markdown table ordered by GitHub stars:

```markdown
### Pane equalizers and auto-resize

*11 projects. Plugins that give every pane in a tab the same share of space, on a key press or automatically.*

| Project | Stars | What it does |
|---|--:|---|
| [**owner/repo**](https://github.com/owner/repo) | 12 | Plain-English explanation of what the tool does and who it is for. |
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

The catalog has 8 numbered domains, one file each in `catalog/`:

1. **Run and orchestrate agents** — `catalog/01-run-and-orchestrate.md`, 52 subcategories
2. **Herdr app layouts, mods, and themes** — `catalog/02-herdr-app.md`, 71 subcategories
3. **Connect through MCP and the socket API** — `catalog/03-mcp-and-socket-api.md`, 46 subcategories
4. **Editor integrations** — `catalog/04-editors.md`, 15 subcategories
5. **Switch and restore sessions** — `catalog/05-sessions.md`, 37 subcategories
6. **Worktrees and terminal experience** — `catalog/06-worktrees-and-terminal.md`, 112 subcategories
7. **Apps, companion integrations, and installation** — `catalog/07-apps-and-installation.md`, 62 subcategories
8. **Experimental projects** — `catalog/08-experimental.md`, 2 subcategories

Inside a domain, subcategories group genuinely similar tools so a reader can compare them side by side (for example, every pane equalizer sits in "Pane equalizers and auto-resize"). The subcategory headings in the catalog files are the canonical list. Rules:

- Put a new project in the existing subcategory whose rows it most resembles. Similar or near-identical tools stay listed and go in the same subcategory; they are not removed for being similar.
- Create a subcategory only when at least 4 projects share it and no existing one fits. Titles are plain English, sentence case, and name what the tools do; no "Misc" or "Other". Domain 2 titles start with "Herdr app". No title repeats another domain's title.
- Split a subcategory that grows past about 60 rows along a clear line (what the tools do, or which product they target).
- Domain 2 opens with the `> Herdr has an official desktop app ... and an official iPhone, iPad, and Android app ...` note under its count line; subcategories elsewhere that collect desktop UIs, mobile clients, web or remote viewers, or phone notifications carry the same note. Keep the note at the domain or subcategory level, never inside a row.
- Tables are ordered by GitHub stars, highest first, except the official subcategory. Archived, deleted, and self-declared deprecated projects are removed, not tagged.

---

## 5. Before Committing

1. Run `python3 scripts/refresh-stars.py` (updates stars, removes archived or deleted repos into `scripts/skipped.txt`, re-sorts tables), then `python3 scripts/sync-counts.py` (rewrites every count, regenerates the README, lists duplicate repos). CI runs `sync-counts.py --check`.
2. Run `npx markdownlint-cli2 "**/*.md"` — it must exit clean with **0 issues** (same check CI runs).
3. Ensure every internal anchor link resolves correctly.
4. Commit with the conventional commit format: `docs(awesome-list): <summary>`.

---

## 6. Finding New Projects

Run `python3 scripts/discover.py` (add `--since YYYY-MM-DD` for the last run date). It writes every Herdr repo that is not in `catalog/` or `scripts/skipped.txt` yet to `.tmp/candidates.json`, sorted by stars, from three sources:

| Source | What it holds | Product |
|---|---|---|
| `assets.herdr.dev/plugins/index.json` | The TUI plugin marketplace: GitHub repos tagged `herdr-plugin` with a valid `herdr-plugin.toml` | Herdr TUI |
| `herdr.dev/gallery/` | Layouts and mods for the Herdr app; one repo can hold many | Herdr app |
| GitHub topics `herdr`, `herdr-layout`, `herdr-mod`, `herdr-app` | Everything else, including clients, SDKs, and dotfiles | Mixed |

Then triage in batches of about 25 candidates per agent:

1. Read the repo README and file tree. Apply section 3: personal dotfiles, stubs, and thin wrappers are excluded even with many stars.
2. Pick the subcategory from section 4 and write a 1–2 sentence description that follows section 2.
3. Group a gallery repo's layouts and mods into one entry for the repo.
4. Insert the rows in the right `catalog/` file, add every skipped repo with its reason to `scripts/skipped.txt`, run `python3 scripts/sync-counts.py`, lint, and commit.

Open pull requests go through the same checks; correct the description or section and merge rather than ask the author.
