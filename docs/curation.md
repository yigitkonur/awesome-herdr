# Curation Guide

This repo is an awesome-list for the Herdr ecosystem, not a general terminal, tmux, or AI-tools directory.

## Inclusion Rules

A project should meet all of these:

1. Public repo or public documentation.
2. Uses Herdr directly, configures Herdr, teaches agents to use Herdr, or integrates with Herdr's socket/CLI/config model.
3. Has enough documentation for a new user to understand setup and value.
4. Is not malware, spam, or pure marketing.
5. Is meaningfully different from projects already listed.

## Strong Signals

| Signal | Why it helps |
|---|---|
| Uses `HERDR_ENV`, `HERDR_SOCKET_PATH`, or Herdr CLI wrappers | Clear Herdr integration |
| Implements socket API calls | Useful ecosystem primitive |
| Provides agent hooks or skills | Extends Herdr's agent awareness |
| Ships reusable config or keymaps | Helps users adopt Herdr faster |
| Documents supported Herdr versions | Reduces breakage |

## Entry Format

```md
- [owner/repo](https://github.com/owner/repo) - Neutral, specific description that says what Herdr surface it uses and who should care. `Language`
```

Examples:

```md
- [54rt1n/herdr-python-client](https://github.com/54rt1n/herdr-python-client) - Lightweight Python client for Herdr's Unix socket API with request envelopes, typed errors, pane reads, waits, and subscriptions. `Python`
```

## Description Style

Do:

- Start with the concrete thing the project does.
- Mention the Herdr integration surface.
- Keep descriptions factual and specific.
- Include caveats when a project is alpha, experimental, or partial.

Avoid:

- "Best", "ultimate", "revolutionary", or other hype.
- Repeating the repository name as the description.
- Vague phrases like "tool for Herdr".
- Private repos or links that cannot be evaluated.

## Categories

Projects may appear in more than one category when that helps discovery. For example, `native-shortcuts-herd` belongs in both Featured and Terminal UX.

Prefer the section where the user would look for the project, not where the author would file it.
