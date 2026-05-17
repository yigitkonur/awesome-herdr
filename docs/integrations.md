# Herdr Integrations

Herdr works without hooks or plugins. It can detect many agents by foreground process and screen heuristics. Integrations improve quality by forwarding semantic state over the local socket API when the agent runtime exposes useful lifecycle hooks.

Canonical source: [INTEGRATIONS.md](https://github.com/ogulcancelik/herdr/blob/master/INTEGRATIONS.md). Last reviewed: 2026-05-17.

## Built-In Integration Installers

```sh
herdr integration install pi
herdr integration install claude
herdr integration install codex
herdr integration install opencode
```

These integrations report state such as `working`, `blocked`, and `idle` over Herdr's local socket API.

Important caveat from the official docs: process detection remains the source of pane identity and liveness. Hooks and plugins do not become the source of truth for pane ownership.

## Integration Paths

| Runtime | Files / environment |
|---|---|
| Pi | `~/.pi/agent/extensions/herdr-agent-state.ts`, `$PI_CODING_AGENT_DIR/extensions/herdr-agent-state.ts` |
| Claude Code | `~/.claude/hooks/herdr-agent-state.sh`, `~/.claude/settings.json`, `$CLAUDE_CONFIG_DIR` |
| Codex | `~/.codex/herdr-agent-state.sh`, `~/.codex/hooks.json`, `~/.codex/config.toml`, `$CODEX_HOME` |
| OpenCode | `~/.config/opencode/plugins/herdr-agent-state.js` |

Herdr `v0.5.10` fixed integration installers so they respect `PI_CODING_AGENT_DIR`, `CLAUDE_CONFIG_DIR`, and `CODEX_HOME`.

## Integration Patterns

| Pattern | Use when |
|---|---|
| Built-in installer | The runtime is Pi, Claude Code, Codex, or OpenCode |
| Hook-owned status label | The runtime can report short visual states like `indexing` without changing semantic status |
| Socket status reporting | The runtime exposes lifecycle hooks and you need robust state in the sidebar |
| Heuristic-only fallback | The runtime has incomplete or no hooks |
| Tab/session sync | The runtime has useful session names that should appear in Herdr UI |

## Projects

- [justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync) - Pi extension that syncs Pi session names into Herdr tab labels and only activates when `HERDR_ENV=1`.
- [hcaiano/skills](https://github.com/hcaiano/skills) - Includes `herdr-pair`, a collaboration skill that depends on Herdr CLI pane primitives and the upstream Herdr skill.

## Custom Integration Checklist

1. Detect `HERDR_ENV=1` before assuming the process is running inside Herdr.
2. Prefer Herdr CLI wrappers first; drop to raw socket only when needed.
3. Report semantic state separately from custom labels.
4. Do not invent leases or TTL ownership if the runtime hook surface is incomplete.
5. Leave process detection as the ownership fallback.
6. Document which config files and environment variables you write.
