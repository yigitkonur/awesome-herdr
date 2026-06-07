# AGENTS.md

Working rules for anyone — human or agent — editing this repo. It is a curated index of the [Herdr](https://github.com/ogulcancelik/herdr) ecosystem. Keep it lean and scannable.

## Adding a project

Add it in **two** places:

**1. The `## At a glance` table** — one scannable row:

```md
| Group | ![Lang](badge) [repo](https://github.com/owner/repo) | ≤8-word hook |
```

The first cell is a 1–2 word **group** tag — reuse an existing one (Orchestrate · Connect · Editor · Sessions · Worktrees · Terminal UX · Desktop · Packaging) so the column keeps clustering by category.

**2. A blurb under the right showcase section:**

```md
![Lang](badge) **[owner/repo](https://github.com/owner/repo)**

Two or three sentences on what it lets a Herdr user *do* and who it's for — not a feature list. No inline install commands (those live in the linked repo).
```

Lead with the language badge(s), then the link — icons aligned on the left scan faster. Use the project's real GitHub link, and when the bare repo name is generic (like `skills`), write the text as `owner/repo` so it stays unambiguous if someone adds a similarly-named project later. Don't add a trailing `` `Language` `` — the badge carries the language.

## Sections

Put a project where a *user* would look for it, not where the author would file it:

- **Run & orchestrate agents** — spawning, pairing, or coordinating multiple agents.
- **Connect over socket & MCP** — socket clients and MCP servers.
- **Editor integrations** — bringing Herdr into Neovim, Cursor, and other editors.
- **Sessions: switch & restore** — finding, attaching to, and restoring sessions.
- **Worktrees, config & terminal UX** — layout bridges, config/keymap packs, terminal polish.
- **Desktop apps & packaging** — GUI/menu-bar apps and install/distribution (Nix, `.deb`).
- **Work in progress** — announced or scaffolded but not yet usable (keep the caveat).

## Language badges

```md
![Rust](https://img.shields.io/badge/-555555?logo=rust&logoColor=white&style=flat-square)
![Python](https://img.shields.io/badge/-555555?logo=python&logoColor=white&style=flat-square)
![TypeScript](https://img.shields.io/badge/-555555?logo=typescript&logoColor=white&style=flat-square)
![Go](https://img.shields.io/badge/-555555?logo=go&logoColor=white&style=flat-square)
![Lua](https://img.shields.io/badge/-555555?logo=lua&logoColor=white&style=flat-square)
![Swift](https://img.shields.io/badge/-555555?logo=swift&logoColor=white&style=flat-square)
![C++](https://img.shields.io/badge/-555555?logo=cplusplus&logoColor=white&style=flat-square)
![Shell](https://img.shields.io/badge/-555555?logo=gnubash&logoColor=white&style=flat-square)
![Nix](https://img.shields.io/badge/-555555?logo=nixos&logoColor=white&style=flat-square)
![YAML](https://img.shields.io/badge/-555555?logo=yaml&logoColor=white&style=flat-square)
```

Every badge uses the same gray (`555555`) and a white icon — only the `logo` slug changes, so a row reads as one consistent monochrome strip. Keep it that way. A repo with a helper in another language (e.g. a Rust-backed `.nvim`) can carry two badges. Pick the [Simple Icons](https://simpleicons.org) slug for any language not listed here.

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
