# Contributing

Thanks for improving Awesome Herdr.

This list is curated. A good entry should help someone discover a high-quality Herdr-related tool, config, skill, client, integration, or workflow.

## Before Opening a Pull Request

Check that your entry is:

1. Publicly accessible.
2. Related to Herdr specifically.
3. Documented enough for a new user to install or understand.
4. Placed in the most useful section.
5. Written in neutral, specific language.

## Entry Format

Use this format:

```md
- [owner/repo](https://github.com/owner/repo) - What it does, which Herdr surface it uses, and who should care. `Language`
```

Descriptions should be one sentence. Mention the integration surface when useful:

- Herdr CLI
- `HERDR_ENV`
- `HERDR_SOCKET_PATH`
- `config.toml`
- `[keys]` / `[keys.indexed]`
- socket methods such as `pane.read` or `events.subscribe`
- agent hooks or skills

## Quality Bar

Prefer:

- working tools
- useful docs
- clear install instructions
- version compatibility notes
- small focused integrations
- projects that demonstrate a reusable pattern

Avoid:

- abandoned empty repos
- private links
- duplicate forks with no new value
- generated filler descriptions
- unsourced claims of official support

## Pull Request Checklist

- [ ] I read [docs/curation.md](./docs/curation.md).
- [ ] The project is Herdr-specific.
- [ ] The entry uses the standard format.
- [ ] The description is factual and specific.
- [ ] Links work.
- [ ] New docs, if any, cite the official upstream source.
