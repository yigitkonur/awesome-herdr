# Herdr TUI Integrations

How Herdr TUI learns what an agent is doing, which agents ship an installer, and how to report your own agent to Herdr from your own code.

Canonical sources: [Integrations](https://herdr.dev/tui/docs/integrations/), [Agents](https://herdr.dev/tui/docs/agents/), [Add Herdr support to your agent](https://herdr.dev/tui/docs/add-herdr-support/), [Plugins](https://herdr.dev/tui/docs/plugins/), [Session state and restore](https://herdr.dev/tui/docs/session-state/). Last reviewed: 2026-11-10.

Covers Herdr TUI v0.9.5 (stable, released 2026-10-14). It does not cover the Herdr app, herdr-core (`hc`), or the mobile apps; for those see the guides listed at the end.

## Detection first, integrations second

Herdr detects the agents it supports on its own. It finds the agent's process in each pane and reads the live bottom of the pane. Rules in a detection manifest decide whether that screen means `idle`, `working`, or `blocked`. An integration adds two things on top:

- **Session resume.** Every built-in integration tells Herdr which session the agent is in, so Herdr can resume it after a server restart. Turn this off with `[session] resume_agents_on_restore = false`.
- **State reports (some agents only).** When an integration also reports state, Herdr uses those reports instead of reading the screen.

Only Pi, OMP, Kimi Code CLI, OpenCode, Kilo Code CLI, and MastraCode report state. Every other built-in integration reports session identity only; their state still comes from screen detection.

Blocked detection is strict. Herdr marks `blocked` only when the screen matches a known approval, question, or permission prompt. For a known agent with no matching rule it falls back to `idle`. An unusual new prompt can therefore look `idle`, so do not treat `idle` as permission to send input.

## Install, uninstall, check

```bash
herdr integration install claude
herdr integration uninstall claude
herdr integration status [--outdated-only]
```

You can also install from the integrations tab in Herdr settings, which offers recommended integrations for agents found on your `PATH`. `herdr integration status` prints one line per target with its state (`not installed`, `current`, `outdated`, or `needs repair`), its version, and the file it checks. Reinstall an outdated one with `herdr integration install <agent>`.

```text
claude: current (v11) (~/.claude/hooks/herdr-agent-state.sh)
pi: not installed (~/.pi/agent/extensions/herdr-agent-state.ts)
letta (experimental): not installed (~/.letta/hooks/herdr-agent-session.sh)
```

(Sample output on Herdr 0.9.5. Integration version numbers change between releases, so check `status` instead of a table.)

## Built-in installers (v0.9.5)

The install name is the argument to `herdr integration install`. "Reports" is what the integration sends to Herdr. Most installers need the agent's config directory to exist already; MastraCode creates it when missing, and Pi and OMP need the agent directory to exist.

| Agent | Install name | Reports | What it writes |
| --- | --- | --- | --- |
| Pi | `pi` | state, session | `~/.pi/agent/extensions/herdr-agent-state.ts`, or `$PI_CODING_AGENT_DIR/extensions/herdr-agent-state.ts` |
| OMP | `omp` | state, session | `~/.omp/agent/extensions/herdr-omp-agent-state.ts`; `PI_CODING_AGENT_DIR` (whole agent directory) or `$HOME/$PI_CONFIG_DIR/agent` override it |
| Claude Code | `claude` | session | `hooks/herdr-agent-state.sh` and `settings.json` in `~/.claude` or `CLAUDE_CONFIG_DIR` |
| Codex | `codex` | session | `herdr-agent-state.sh`, `hooks.json`, and `[features] hooks = true` in `config.toml`, in `~/.codex` or `CODEX_HOME` |
| GitHub Copilot CLI | `copilot` | session | `hooks/herdr-agent-state.sh` and `settings.json` in `~/.copilot` or `COPILOT_HOME` |
| Devin CLI | `devin` | session | `herdr-agent-state.sh` and `config.json` in `$XDG_CONFIG_HOME/devin`, else `~/.config/devin` |
| Droid | `droid` | session | `hooks/herdr-agent-state.sh` and `settings.json` in `~/.factory` |
| Kimi Code CLI | `kimi` | state, session | `hooks/herdr-agent-state.sh` and `config.toml` in `~/.kimi-code` or `KIMI_CODE_HOME`; needs Kimi Code CLI `0.14.0`+ |
| OpenCode | `opencode` | state, session | `~/.config/opencode/plugins/herdr-agent-state.js` plus TUI plugin files |
| Kilo Code CLI | `kilo` | state, session | `~/.config/kilo/plugin/herdr-agent-state.js` |
| Hermes Agent | `hermes` | session | `plugins/herdr-agent-state/` under `HERMES_HOME` (default `~/.hermes` on Unix), enabled in `config.yaml` |
| Qoder CLI | `qodercli` | session | `hooks/herdr-agent-state.sh` and `settings.json` in `~/.qoder` or `QODER_CONFIG_DIR` |
| Qwen Code | `qwen` | session | `hooks/herdr-agent-session.sh` and `settings.json` in `~/.qwen` or `QWEN_HOME` |
| Letta Code | `letta` | session | `hooks/herdr-agent-session.sh` and `settings.json` in `~/.letta`; experimental, CLI-only |
| Cursor Agent CLI | `cursor` | session | `herdr-agent-state.sh` and `hooks.json` in `~/.cursor` or `CURSOR_CONFIG_DIR` |
| MastraCode | `mastracode` | state, session | `hooks/herdr-agent-state.sh` and `hooks.json` in `~/.mastracode` |
| Antigravity CLI | `antigravity-cli` | session | `hooks/herdr-agent-state.sh` and a `herdr` block in `hooks.json`, in `~/.gemini/config/` or `ANTIGRAVITY_CLI_CONFIG_DIR` |
| Grok CLI | `grok` | session | `hooks/herdr.json` and `hooks/herdr-agent-state.sh` in `~/.grok` or `GROK_HOME` |

Notes from the docs:

- OMP and Pi can resolve to the same extension directory. Herdr then refuses the OMP install so Pi cannot load the OMP extension.
- Letta is not in the Settings integrations screen or the JSON integration API, and `herdr integration status` lists it as `letta (experimental)`.
- MastraCode has no screen-detection fallback; its state comes only from the hook. For OMP the agents page says state requires the integration too.
- After installing, restart the agent: OpenCode (the TUI, and any shared OpenCode servers after an update) and Hermes Agent load the plugin only on start.
- `antigravity_cli` is accepted as an alias for `antigravity-cli` (`src/cli/integration.rs`).
- Uninstall removes the Herdr hook or plugin file and the Herdr entries it added. Codex uninstall leaves `config.toml` unchanged.
- Installers honor each agent's config-directory variable shown in the table. Pi, Claude Code, and Codex have done so since v0.5.10.

Agents Herdr detects but that have no installer: Amp, Kiro CLI, Maki, Gemini CLI, and Cline (the last two are less tested). Command Code, Crush, Kiro CLI, Muse Code, and Prime Agent report their own state to Herdr, so there is nothing to install. See [Agents](https://herdr.dev/tui/docs/agents/) for the current list and notes.

## Fixing wrong detection

| Situation | What to use |
| --- | --- |
| Pane shows the wrong state | `herdr agent explain <target>` (or `herdr agent explain --file screen.txt --agent codex --json`) |
| A wrapper such as a sandbox hides the real agent process (Linux and macOS) | Set `HERDR_AGENT=<agent>` on the wrapper command, for example `HERDR_AGENT=claude fence -- claude`. It applies only to that foreground process, and Herdr cannot see it if you set it only inside a VM or container |
| Restricted Linux runtime has no foreground process group | Start the Herdr server with `HERDR_PROCESS_DETECTION=child-groups` |
| Override a detection manifest | `~/.config/herdr/agent-detection/<agent>.toml`, then `herdr server reload-agent-manifests` |
| Stop remote manifest updates | `[update] manifest_check = false` |

Herdr checks herdr.dev for remote manifest updates, and `herdr server update-agent-manifests` fetches them immediately. Remote manifests only patch rules for agents Herdr already knows; a brand-new agent needs a Herdr binary update.

## Integrations vs plugins

These are different things.

| | Integration | Herdr plugin |
| --- | --- | --- |
| Purpose | Tell Herdr what one coding agent is doing and how to resume it | Reusable workflow: actions, event hooks, panes, link handlers |
| Installed with | `herdr integration install <agent>` | `herdr plugin install owner/repo[/subdir]` or `herdr plugin link <path>` |
| Defined by | A hook or extension written into the agent's own config | A directory with a `herdr-plugin.toml` manifest |
| Talks to Herdr via | `pane report-agent` and related calls | The full Herdr CLI, through `HERDR_BIN_PATH` |

A plugin is ordinary code running as your user; Herdr validates the manifest but does not sandbox it. For plugin authoring, see [Plugins](https://herdr.dev/tui/docs/plugins/). Note that OpenCode, Kilo Code CLI, and Hermes Agent integrations install a plugin into that agent, not a Herdr plugin.

## Report your own agent

You do not need a pull request to Herdr or a Herdr release. Every process in a Herdr pane inherits these variables:

| Variable | Meaning |
| --- | --- |
| `HERDR_ENV` | `1` inside Herdr |
| `HERDR_PANE_ID` | The pane your agent runs in |
| `HERDR_BIN_PATH` | The Herdr binary that owns this pane |
| `HERDR_SOCKET_PATH` | Herdr's API socket |

Your agent makes three kinds of report through `"$HERDR_BIN_PATH"`: state, resume command, release.

```bash
# state
"$HERDR_BIN_PATH" pane report-agent "$HERDR_PANE_ID" \
  --source my-agent \
  --agent my-agent \
  --state working \
  --seq 1

# state plus resume command (after --)
"$HERDR_BIN_PATH" pane report-agent "$HERDR_PANE_ID" \
  --source my-agent \
  --agent my-agent \
  --state idle \
  --seq 2 \
  --agent-session-id "$SESSION_ID" \
  -- my-agent --resume "$SESSION_ID" --model my-model

# release on exit
"$HERDR_BIN_PATH" pane release-agent "$HERDR_PANE_ID" \
  --source my-agent \
  --agent my-agent \
  --seq 3
```

Rules from the docs:

- `--state` is `idle`, `working`, `blocked`, or `unknown`. `--message` explains a block.
- `--agent` is the name users see. Use your own agent's name, not the name of an agent Herdr already supports.
- `--source` must be stable and unique, and must not start with `herdr:` (Herdr's own integrations use that prefix).
- `--seq` is optional but recommended. It must increase with every report from your source, across sessions and restarts. Herdr ignores reports that are not higher than the last accepted one.
- Resume command: the first word is a plain command name on `PATH` (not a path), no argument has an apostrophe or control character, at most 64 arguments and 8 KiB in total. A bad command fails with `invalid_resume_argv` and the report is not applied.
- Your source must hold the pane first (send a `report-agent` before or with the command), otherwise Herdr answers `resume_not_accepted`.
- `pane report-agent-session` updates the native session identity without reporting lifecycle state. It takes the same `--source`, `--agent`, `--seq`, `--agent-session-id`, and `-- RESUME_COMMAND...`, plus `--agent-session-path` and `--session-start-source`.
- Resume commands need Herdr 0.9.2 or later; older versions ignore them.
- Release only when the user really quits. If your agent exits without releasing, Herdr clears it once the pane is back at an idle shell prompt.
- Do not slow your agent down: send reports in the background or with a short timeout, ignore failures, and send only the latest state.
- Raw socket equivalents are `pane.report_agent`, `pane.report_agent_session`, and `pane.release_agent`; the resume command goes in the `resume_argv` array. The CLI is the portable choice, including on Windows.

### Custom integration checklist

1. Act only when `HERDR_ENV=1` and the other variables are set; outside Herdr, do nothing.
2. Call `"$HERDR_BIN_PATH"` rather than the raw socket unless you need direct IPC.
3. Report `working` at turn start, `idle` when ready for input, `blocked` when the user must decide.
4. Use a stable `--source` that does not start with `herdr:`, and an increasing `--seq`.
5. Report the resume command, and again whenever the session changes.
6. Release on real exit, not on session replacement.
7. Document the files and environment variables your integration writes or reads.
8. Test it (below).

### Test it

```bash
herdr pane get "$HERDR_PANE_ID"
herdr agent list
```

To test restore without touching your normal session: run `herdr --session my-agent-test` and your agent in a pane, stop it with `herdr session stop my-agent-test`, then start `herdr --session my-agent-test` again. The pane should run your resume command.

## Labels without taking over state

Integrations report semantic state only. Titles, display names, state labels, and tokens go through separate metadata calls. They are visual only; waits, notifications, and rollups still use the semantic state.

```bash
herdr pane report-metadata "$HERDR_PANE_ID" \
  --source user:claude-title \
  --agent claude \
  --title "Refactor auth middleware" \
  --display-agent "Claude: auth" \
  --token summary="refactor auth" \
  --state-label working="refactoring auth" \
  --ttl-ms 3600000
```

`--state-label` takes `STATUS=TEXT` with `idle`, `working`, `blocked`, `done`, or `unknown`. `--ttl-ms` (1 to 86400000) makes metadata expire. `--agent` and `--applies-to-source` guard only `--title`, `--display-agent`, and `--state-label`; token patches always apply, and their reporter owns clearing them. Tokens appear in Agent sidebar rows as `$name` (for example `$summary`). Use `report-metadata`, not `report-agent`, in user hooks that sit next to a Herdr-managed integration.

## Community projects

Projects from the [awesome-herdr list](../README.md). Descriptions follow the list.

Agents that report their own state to Herdr TUI through the calls above:

| Project | What it does |
| --- | --- |
| [Ziy1-Tan/herdr-codebuddy](https://github.com/Ziy1-Tan/herdr-codebuddy) | Reports CodeBuddy session, working and permission states to Herdr TUI through hooks. |
| [leonardoacosta/herdr-jcode](https://github.com/leonardoacosta/herdr-jcode) | Reports Jcode working and idle lifecycle states and session identity to Herdr TUI. |
| [Phoobobo/herdr-traex-integration](https://github.com/Phoobobo/herdr-traex-integration) | Connects TraeX lifecycle hooks to Herdr's agent-reporting socket methods, giving TraeX panes correct idle, working, and blocked status. |
| [meuble/Herdr-mistral-vibe](https://github.com/meuble/Herdr-mistral-vibe) | Reports Mistral Vibe working, idle, and blocked states to Herdr TUI through Vibe hooks. |
| [uuie/reasonix-herdr](https://github.com/uuie/reasonix-herdr) | Reports Reasonix agent lifecycle states to Herdr in real time and adds native workspace and pane controls for supervising Reasonix alongside other agents. |
| [markbrutx/pif-herdr-reporter](https://github.com/markbrutx/pif-herdr-reporter) | Reports working and idle states from the pif coding agent to its Herdr TUI pane and releases the agent on exit. |
| [dsh-blue/herdr-agent-state](https://github.com/dsh-blue/herdr-agent-state) | Reports DeepSeek Harness lifecycle state, session references, and model metadata to the current Herdr pane. |

Extras on top of agents Herdr already supports:

| Project | What it does |
| --- | --- |
| [SpatialNexus/herdr-subagent-state](https://github.com/SpatialNexus/herdr-subagent-state) | Uses Claude Code, Codex, and Pi hooks to report working state while tools or delegated subagents are active. |
| [larryboiNEUQ/pi-herdr-ui-bridge](https://github.com/larryboiNEUQ/pi-herdr-ui-bridge) | Reports blocking Pi extension prompts as Herdr agent blocked states so notification plugins can alert users. |
| [justcyl/pi-herdr-tab-sync](https://github.com/justcyl/pi-herdr-tab-sync) | Renames the active Herdr tab to the Pi session name when an agent starts or resumes. It communicates directly with the socket and remains inactive outside Herdr-managed panes. |
| [Angel-O/herdr-agent-resume](https://github.com/Angel-O/herdr-agent-resume) | Generates the exact resume command for an interrupted Claude Code, Codex, or custom agent session and either copies it or pastes it into a Herdr pane. |

## Related guides

[Socket API](./socket-api.md), [Configuration](./configuration.md), [Agent workflows](./agent-workflows.md), [Herdr app](./herdr-app.md), [herdr-core](./herdr-core.md).
