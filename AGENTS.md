# AGENTS.md

Working rules for anyone — human or agent — editing this repo. It is a curated index of the [Herdr](https://github.com/ogulcancelik/herdr) ecosystem. Keep it lean and scannable.

## Adding a project

Add it in **two** places:

**1. The `## At a glance` table** — one scannable row:

```md
| [repo](https://github.com/owner/repo) ![Lang](badge) | ≤8-word hook |
```

**2. A blurb under the right showcase section:**

```md
**[owner/repo](https://github.com/owner/repo)** ![Lang](badge)

Two or three sentences on what it lets a Herdr user *do* and who it's for — not a feature list. No inline install commands (those live in the linked repo).
```

Use the project's real GitHub link. Don't add a trailing `` `Language` `` — the badge carries the language.

## Sections

Put a project where a *user* would look for it, not where the author would file it:

- **Core & forks** — Herdr itself and standalone forks.
- **Run & orchestrate agents** — spawning, pairing, or coordinating multiple agents.
- **Connect over socket & MCP** — clients, editor bridges, MCP servers.
- **Persist & restore sessions** — surviving restarts and reboots.
- **Worktrees & terminal UX** — layout bridges, keymaps, terminal polish.
- **Work in progress** — announced or scaffolded but not yet usable (keep the caveat).

## Language badges

```md
![Rust](https://img.shields.io/badge/-Rust-DEA584?logo=rust&logoColor=black&style=flat-square)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white&style=flat-square)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnubash&logoColor=white&style=flat-square)
![YAML](https://img.shields.io/badge/-YAML-CB171E?logo=yaml&logoColor=white&style=flat-square)
```

## The bar

A project belongs here only if it is:

- **Public** — repo or docs anyone can open.
- **Herdr-specific** — uses, configures, or teaches Herdr (socket/CLI/config/hooks/skills), not a generic terminal or AI tool.
- **Documented** — a new user can understand its setup and value.
- **Meaningfully distinct** — not a near-duplicate fork with no added value.
- **Factual** — neutral, specific prose. No hype ("best", "ultimate"), no affiliate links, no generated filler, no repeating the repo name as the description.

Scaffold-only or not-yet-usable repos go in **Work in progress**, not the main list.

## Before committing

- Run `npx markdownlint-cli2 "**/*.md"` — it must exit clean (same check CI runs).
- Confirm links work and the project appears in both the table and a section.
- Commit as `docs(awesome-list): <summary>`.
