# Herdr TUI Configuration

A compact field guide of `config.toml` for people building configs, keymap packs, theme packs, and tools that edit Herdr settings.

Canonical sources: [Configuration](https://herdr.dev/tui/docs/configuration/), [Config reference](https://herdr.dev/tui/docs/config-reference/), [Keyboard](https://herdr.dev/tui/docs/keyboard/). Last reviewed: 2026-11-10.

Covers Herdr TUI v0.9.5 (stable, released 2026-10-14). It does not cover the Herdr app, herdr-core (`hc`), or the mobile apps; for those see the guides listed at the end.

## Config file

Herdr works without a config file. It reads `config.toml` from:

```text
Linux and macOS: ~/.config/herdr/config.toml
Windows:          %APPDATA%\herdr\config.toml
```

| Override | Effect |
|---|---|
| `HERDR_CONFIG_PATH` | Sets the config file path. Only `config.toml` moves; session data and logs stay in the config directory |
| `XDG_CONFIG_HOME` | Moves the config directory to `$XDG_CONFIG_HOME/herdr`, including session data and logs |

`herdr --help` prints the resolved config path and log paths.

```bash
herdr --default-config                          # print the full commented default config
herdr --default-config > ~/.config/herdr/config.toml
herdr config check                              # validate config.toml and print diagnostics
```

`herdr config check` prints `config: ok` for a clean file. Otherwise it prints `config: issues found` plus one line per problem, such as an unknown key or theme name, and exits with status 1. If a value is invalid, Herdr falls back to a safe default and shows a startup warning. At startup a file that cannot be parsed falls back to the built-in defaults; a reload keeps the current config instead (see below).

Named sessions share the same `config.toml`. Only runtime data differs: the default session keeps its data in the config directory, and a named session uses `sessions/<name>/` inside it.

```text
~/.config/herdr/session.json
~/.config/herdr/sessions/<name>/session.json
```

Session commands, from the CLI reference:

```bash
herdr session list [--json]
herdr session attach <name>
herdr session stop <name> [--json]
herdr session delete <name> [--json]
```

Herdr shows first-run setup when `onboarding` is missing or true. Set `onboarding = false` to skip it.

## Reload model

```bash
herdr server reload-config
```

You can also run `reload config` from the global menu. `keys.reload_config` defaults to `prefix+shift+r`. Reload applies most UI settings without restarting panes. Startup-only settings still need a restart.

The command prints a JSON report with a `status`:

| `status` | Meaning |
|---|---|
| `applied` | Config loaded with no diagnostics |
| `partial` | Loaded with diagnostics, for example an unknown key; valid parts still apply |
| `failed` | TOML could not be read or parsed; Herdr keeps the current config |

Example `partial` report from a config with `[ui] bogus_key = 1`:

```json
{"id":"cli:server:reload-config","result":{"diagnostics":["unknown config key ui.bogus_key; ignoring key"],"status":"partial","type":"config_reload"}}
```

Reload is applied section by section. An invalid section keeps its previous settings, and valid sections still apply. The server's reload code applies `keys`, `ui`, `theme`, `terminal` (shell, shell mode, new cwd), `worktrees`, `server`, `advanced`, `update`, and these `experimental` keys: `pane_history`, `reveal_hidden_cursor_for_cjk_ime`, `cjk_ime_agents`, `cjk_ime_cursor_shape`. If `experimental.pane_history` is off, a reload also deletes any saved `session-history.json`.

These need a restart. A reload only reports a diagnostic and keeps the current setting:

| Setting | Diagnostic |
|---|---|
| `session.startup_per_agent_delay_ms` | "changes require restarting Herdr; kept current setting" |
| `terminal.kitty_graphics` | "changes require restarting Herdr; kept current setting" |

The config reference also marks `server.allow_unelevated_clients` (Windows only) as applying at server startup, and `ui.sidebar_start_collapsed` as taking effect on the next launch.

Client versus server: themes, sidebar layouts, copy behavior, and other presentation settings come from the client's local config, including when viewing an SSH machine. Pane defaults, worktrees, integrations, and custom commands belong to the server where the panes run. The UI's `reload config` action reloads both. With `herdr --remote`, local keybindings are used unless you pass `--remote-keybindings server`.

## Keybindings

Herdr has a tmux-style prefix. The default prefix is `ctrl+b`. Binding strings are explicit: `prefix+n` means press the prefix, then `n`. `ctrl+alt+n` is a direct terminal-mode shortcut. Press `prefix+?` in Herdr to see the active bindings.

```toml
[keys]
prefix = "ctrl+b"
goto = "prefix+g"
new_tab = "prefix+c"
next_tab = "prefix+n"
previous_tab = "prefix+p"
focus_pane_left = "prefix+h"
navigate_workspace_down = "j"
navigate_pane_down = "ctrl+j"
split_horizontal = "prefix+minus"
```

`keys.prefix` accepts an array, and so does any binding that needs several shortcuts:

```toml
[keys]
prefix = ["ctrl+space", "ctrl+s"]
next_tab = ["prefix+n", "ctrl+alt+]"]
```

Every configured prefix enters the same prefix mode. The first entry is the primary prefix shown in the status bar.

Key strings accept:

| Syntax | Examples |
|---|---|
| Plain keys | `n`, `x`, `-` |
| Modifier combos | `ctrl+a`, `shift+n`, `alt+1`, `cmd+k` |
| Special keys | `enter`, `tab`, `esc`, `space`, `backspace`, `left`, `right`, `up`, `down` |
| Function keys | `f1`, `f12` |
| Named punctuation | `minus`, `comma`, `period`, `slash`, `backslash`, `quote`, `double_quote`, `semicolon`, `colon`, `percent`, `ampersand`, `backtick`, `plus` |

Modifier names the parser recognises are `ctrl`/`control`, `shift`, `alt`/`option`/`meta`, `cmd`/`command`/`super`, and `hyper`. A single uppercase letter such as `D` is read as `shift+d`.

Plain direct printable keys such as `n` are unsafe because they intercept typing. Use `prefix+n` unless you want a direct binding. `alt`, `cmd`/`super`, and punctuation with modifiers depend on your terminal and tmux settings. The `navigate_workspace_*` and `navigate_pane_*` fields are navigate-mode only and may use plain keys such as `j`; they must not use `prefix+`, `esc`, `enter`, `tab`, `shift+tab`, `left`, `right`, or unmodified `1` through `9`. Left and right arrows always alias pane-left and pane-right navigation.

Defaults (from the config reference):

| Key | Default | Action |
|---|---|---|
| `help` | `prefix+?` | Keybinding help |
| `settings` | `prefix+s` | Settings |
| `new_workspace` | `prefix+shift+n` | New workspace |
| `new_worktree` | `prefix+shift+g` | New Git worktree from the selected workspace |
| `rename_workspace` | `prefix+shift+w` | Rename workspace |
| `close_workspace` | `prefix+shift+d` | Close workspace |
| `workspace_picker` | `prefix+w` | Workspace navigation |
| `goto` | `prefix+g` | Session navigator (Goto picker) |
| `new_tab` | `prefix+c` | New tab |
| `rename_tab` | `prefix+shift+t` | Rename tab |
| `previous_tab` / `next_tab` | `prefix+p` / `prefix+n` | Previous / next tab |
| `switch_tab` | `prefix+1..9` | Switch to tab 1-9 |
| `close_tab` | `prefix+shift+x` | Close tab |
| `rename_pane` | `prefix+shift+p` | Rename pane |
| `focus_pane_left` / `down` / `up` / `right` | `prefix+h` / `j` / `k` / `l` | Move focus between panes |
| `swap_pane_left` / `down` / `up` / `right` | `prefix+shift+h` / `j` / `k` / `l` | Swap panes |
| `cycle_pane_next` / `cycle_pane_previous` | `prefix+tab` / `prefix+shift+tab` | Cycle panes |
| `split_vertical` | `prefix+v` | Split side by side |
| `split_horizontal` | `prefix+minus` | Split stacked |
| `close_pane` | `prefix+x` | Close pane |
| `zoom` | `prefix+z` | Zoom focused pane (legacy alias `fullscreen`) |
| `resize_mode` | `prefix+r` | Resize mode |
| `copy_mode` | `prefix+[` | Copy mode |
| `edit_scrollback` | `prefix+e` | Open pane scrollback in `$EDITOR` |
| `toggle_sidebar` | `prefix+b` | Toggle sidebar |
| `open_notification_target` | `prefix+o` | Focus the visible notification target |
| `detach` | `prefix+q` | Detach |
| `reload_config` | `prefix+shift+r` | Reload `config.toml` |
| `remote_image_paste` | `ctrl+v` | Local-client shortcut that sends a clipboard image to a remote session |

Navigate-mode defaults: `navigate_workspace_up` = `up`, `navigate_workspace_down` = `down`, `navigate_pane_left`/`down`/`up`/`right` = `h`/`j`/`k`/`l`.

Unset by default: `previous_workspace`, `next_workspace`, `previous_agent`, `next_agent`, `focus_agent`, `switch_workspace`, `move_tab_previous`, `move_tab_next`, `last_pane`, `clear_pane`, `open_worktree`, `remove_worktree`, and `resize_pane_left`/`down`/`up`/`right`. Direct pane resizing without resize mode:

```toml
[keys]
resize_pane_left = "ctrl+shift+alt+left"
resize_pane_down = "ctrl+shift+alt+down"
resize_pane_up = "ctrl+shift+alt+up"
resize_pane_right = "ctrl+shift+alt+right"
```

The Keyboard page lists `ctrl+alt` as a family terminals leave mostly free, with a list of exceptions (`ctrl+alt+arrows`, `ctrl+alt+t`, and others). If a direct chord does nothing, your terminal or desktop consumed it first.

To drop old custom keybindings and take the new defaults:

```bash
herdr config reset-keys
```

It backs up `config.toml`, removes `[keys]` and `[[keys.command]]`, and applies the built-in v2 defaults after a restart or `herdr server reload-config`.

## Indexed keybinds

Indexed bindings use `1..9` in normal keybinding fields:

```toml
[keys]
switch_tab = "prefix+1..9"
switch_workspace = "prefix+shift+1..9"
focus_agent = "prefix+alt+1..9"
```

`switch_tab` defaults to `prefix+1..9`. `switch_workspace` and `focus_agent` are unset by default. The legacy `[keys.indexed]` table (`tabs`, `workspaces`, `agents`; each a modifier combo such as `"ctrl"`, empty disables it) is still parsed for compatibility, but new configs should use the explicit fields above.

## Command keybindings

Add `[[keys.command]]` tables to bind a key to a command. Use the same binding syntax as other keys.

```toml
[[keys.command]]
key = "prefix+alt+g"
type = "popup"
command = "lazygit"
description = "run lazygit"
width = "80%"
height = "80%"
```

| `type` | Behavior |
|---|---|
| `popup` | Session-modal popup that does not change the tab layout; receives all terminal input, including Escape, until the command exits |
| `pane` | Temporary zoomed pane, closed when the command exits |
| `shell` | Runs detached in the background |
| `plugin_action` | Invokes an installed plugin action id; use the qualified id when ids are not globally unique |

`width` and `height` apply to popups. Omit them for a half-size popup, use numbers for terminal cells, or strings such as `"80%"`. `description` is optional and shows in the `prefix+?` help panel instead of `'custom command'`.

On Unix and macOS a popup can also be an ad-hoc terminal without adding a split or tab:

```toml
[[keys.command]]
key = "prefix+t"
type = "popup"
command = "exec \"${SHELL:-sh}\""
description = "open scratch terminal"
width = "80%"
height = "80%"
```

```toml
[[keys.command]]
key = "prefix+l"
type = "plugin_action"
command = "example.layout.apply"
description = "apply layout"
```

Custom commands receive `HERDR_SOCKET_PATH`, `HERDR_BIN_PATH`, `HERDR_ACTIVE_WORKSPACE_ID`, `HERDR_ACTIVE_TAB_ID`, `HERDR_ACTIVE_PANE_ID`, and `HERDR_ACTIVE_PANE_CWD` when those values are available. Shell commands run from the focused pane's working directory when Herdr can detect it.

Popup commands do not receive `HERDR_PANE_ID`. Use `HERDR_ACTIVE_PANE_ID` for the tiled pane underneath. On Unix, pane commands run through `/bin/sh -c` and detached commands through `/bin/sh -lc`. On Windows, command strings run through `cmd.exe /d /c`, so variables use `%HERDR_BIN_PATH%` syntax. With `herdr --remote`, local custom command keybindings are not sent, because those commands would run on the remote host.

## Themes

```toml
[theme]
name = "catppuccin"
```

Built-in names, from the source: `catppuccin` (default), `catppuccin-latte`, `terminal`, `tokyo-night`, `tokyo-night-day`, `dracula`, `nord`, `gruvbox`, `gruvbox-light`, `one-dark`, `one-light`, `solarized`, `solarized-light`, `kanagawa`, `kanagawa-lotus`, `rose-pine`, `rose-pine-dawn`, `vesper`. Use `terminal` to follow the host terminal's ANSI palette.

Names are lowercased and spaces and underscores become dashes, and some aliases exist, so `tokyo_night` and `tokyonight` both select `tokyo-night`. An unknown name falls back to `catppuccin` with a diagnostic.

Follow the terminal's light/dark appearance:

```toml
[theme]
name = "catppuccin"
auto_switch = true
light_name = "catppuccin-latte"
dark_name = "catppuccin"
```

`auto_switch` defaults to `false`. If `light_name` or `dark_name` is omitted, Herdr picks the matching built-in sibling of `name` when one exists, such as `tokyo-night`/`tokyo-night-day` or `gruvbox`/`gruvbox-light`. Choosing a theme manually in Settings disables `auto_switch`.

Override individual colors on top of the base theme:

```toml
[theme.custom]
sidebar_bg = "#181825"
active_row_bg = "#1e1e2e"
selection_bg = "#313244"
panel_bg = "reset"
accent = "#a6e3a1"
```

Token names: `accent`, `panel_bg`, `sidebar_bg`, `active_row_bg`, `selection_bg`, `surface0`, `surface1`, `surface_dim`, `overlay0`, `overlay1`, `text`, `subtext0`, `mauve`, `green`, `yellow`, `red`, `blue`, `teal`, `peach`. `sidebar_bg` gives the desktop sidebar its own background (otherwise it keeps the terminal background), `active_row_bg` colors the active Space and focused Agent row, and `selection_bg` colors the Navigate-mode cursor row. Values accept hex, named colors, `rgb(r,g,b)`, or reset aliases such as `reset`, `default`, `none`, and `transparent`.

With `auto_switch` on, `[theme.custom.light]` and `[theme.custom.dark]` layer on top of `[theme.custom]` and take the same token names. The order is built-in theme, `[theme.custom]`, then the light or dark table.

On Unix, if your theme switcher changes terminal colors through OSC without a light/dark notification, send `kill -WINCH <client-pid>` to the attached Herdr client (not the server) so it re-reads the colors.

## UI, toasts, and sound

Common `[ui]` settings (defaults from the config reference):

| Setting | Default | Notes |
|---|---|---|
| `ui.sidebar_width` | `26` | Expanded width in columns; auto-scales with workspace names |
| `ui.sidebar_min_width` / `ui.sidebar_max_width` | `18` / `36` | Bounds when expanded |
| `ui.sidebar_start_collapsed` | `false` | Takes effect on next launch |
| `ui.sidebar_collapsed_mode` | `compact` | `compact` or `hidden` |
| `ui.mobile_width_threshold` | `64` | Terminal width at or below which Herdr uses the mobile single-column layout |
| `ui.mouse_capture` | `true` | Capture mouse input for Herdr's mouse UI |
| `ui.mouse_scroll_lines` | `3` | Lines per mouse wheel notch |
| `ui.copy_on_select` | `true` | Copy text selected by mouse drag or double-click |
| `ui.host_cursor` | `auto` | `auto`, `native`, or `drawn` |
| `ui.confirm_close` | `true` | Ask before closing a workspace |
| `ui.prompt_new_tab_name` | `true` | Ask for a tab name before creating a tab |
| `ui.prompt_new_workspace_name` | `false` | Ask for a workspace name on interactive creation |
| `ui.pane_borders` | `"auto"` | `auto`, `always`, or `off`; booleans still parse. `always` frames a lone pane only while `ui.pane_outer_borders` is on |
| `ui.pane_outer_borders` / `ui.pane_scrollbars` / `ui.pane_gaps` | `true` | Outer frame, pane scrollbars, and gaps between split panes |
| `ui.show_agent_labels_on_pane_borders` | `false` | Agent labels on split pane borders |
| `ui.hide_tab_bar_when_single_tab` | `false` | Hide the tab row when a workspace has one tab |
| `ui.agent_panel_sort` | `"spaces"` | `spaces` or `priority` |
| `ui.status_indicators` | `"dots"` | `dots` or `symbols` (static shapes in addition to color) |
| `ui.tab_bar_position` | `"top"` | `top` or `bottom` |
| `ui.window_title` | `"{hostname}: {workspace}"` | Outer terminal title; empty leaves it alone |
| `ui.accent` | `"cyan"` | Accent color for highlights, borders, and navigation UI |

Search `ui.` in the [Config reference](https://herdr.dev/tui/docs/config-reference/) for the rest (for example `ui.right_click_passthrough_modifier` and `ui.redraw_on_focus_gained`).

`ui.window_title` tokens are `{hostname}`, `{workspace}`, `{tab}`, `{pane}` (the focused pane's manual name), and `{terminal_title}`. Write `{{` and `}}` for literal braces. The title is rendered on the server, so `{hostname}` names the machine the panes run on, including with `herdr --remote`.

Sidebar rows are token lists. These are the default layouts:

```toml
[ui.sidebar.agents]
row_gap = 0
rows = [
  ["state_icon", "machine", "workspace", "tab"],
  ["agent"],
]

[ui.sidebar.spaces]
row_gap = 0
rows = [
  ["state_icon", "workspace"],
  ["branch", "git_status"],
]
```

Agent rows accept `state_icon`, `state_text`, `machine`, `workspace`, `tab`, `pane`, `agent`, `terminal_title`, `terminal_title_stripped`, and `$name`. Space rows accept `state_icon`, `state_text`, `workspace`, `branch`, `git_status`, and `$name`. A layout may hold at most 16 rows with at most 16 tokens each. Tokens can be inline style tables with `fg`, `bold`, `dim`, and `rules`. Custom `$name` tokens show values that a script or plugin reports with `herdr pane report-metadata` (or `herdr workspace report-metadata` for Space rows). See the upstream page for rule syntax.

To replace the whole Agent layout for one agent, use `rows_by_agent`. Keys are canonical agent IDs such as `claude`, `codex`, and `pi`; aliases such as `claude-code` are not accepted. An override replaces `rows`, it does not extend it.

```toml
[ui.sidebar.agents.rows_by_agent]
claude = [
  ["state_icon", "agent", "state_text"],
  ["terminal_title_stripped"],
  ["workspace", "tab"],
]
```

`ui.tab_bar_right` configures right-aligned tab bar entries of type `zoom`, `hostname`, `datetime`, `text`, and `command`. The status area is empty by default.

```toml
[ui]
tab_bar_right = [
  { type = "zoom" },
  { type = "datetime", format = "%H:%M" },
  { type = "text", text = "prod" },
  { type = "command", command = "~/.config/herdr/status.sh", interval_seconds = 5, timeout_seconds = 2 },
]
tab_bar_right_separator = " · "
```

`hostname`, `datetime`, and `command` entries resolve on the server. A command entry's `interval_seconds` can be 1 to 31,536,000 and `timeout_seconds` 1 to 3,600; Herdr shows the last line of successful output.

### Toasts

```toml
[ui.toast]
delivery = "herdr"
delay_seconds = 1

[ui.toast.herdr]
position = "bottom-right"
```

| `delivery` | Meaning |
|---|---|
| `off` (default) | Disable popups |
| `herdr` | In-app toast |
| `terminal` | Ask the outer terminal for a desktop notification; works over SSH |
| `system` | Ask the local OS notification service |

`delay_seconds` (default `1`, valid `0` through `3600`) waits before notifying, and Herdr notifies only if the pane is still in the same state. Herdr suppresses popups for the active tab. `ui.toast.herdr.position` accepts `top-left`, `top-right`, `bottom-left`, `bottom-right`. `ui.toast.clipboard.enabled` (default `true`) and `ui.toast.clipboard.position` (default `bottom-center`) control the copied-to-clipboard popup.

On macOS, `system` tries `terminal-notifier` first and falls back to `/usr/bin/osascript`, which shows as Script Editor. Install it with `brew install terminal-notifier`.

### Sound

Sound plays through the local Herdr client. Custom sounds must be mp3 files, and relative paths resolve from the config file's directory.

```toml
[ui.sound]
enabled = true
path = "sounds/notification.mp3"
done_path = "sounds/done.mp3"
request_path = "sounds/request.mp3"

[ui.sound.agents]
droid = "off"
claude = "on"
```

`path` sets one sound for everything; `done_path` and `request_path` override the finished and needs-input sounds. `enabled` defaults to `true`. Per-agent values are `default`, `on`, or `off`, and `droid` is `off` by default. Keys follow the config reference, for example `claude`, `codex`, `open_code`, and `github_copilot`. `HERDR_DISABLE_SOUND` disables sound even when sound notifications are enabled.

## Terminal, worktrees, session, remote

```toml
[terminal]
default_shell = ""
shell_mode = "auto"
new_cwd = "follow"
kitty_graphics = true

[worktrees]
directory = "~/.herdr/worktrees"

[session]
resume_agents_on_restore = true
startup_per_agent_delay_ms = 100

[remote]
manage_ssh_config = true

[server]
headless_cols = 120
headless_rows = 40
```

| Key | Notes |
|---|---|
| `terminal.default_shell` | Executable for new interactive panes, not a command line. Empty means `$SHELL`, then `/bin/sh`. On Windows: `pwsh.exe` if on `PATH`, otherwise `powershell.exe`. Existing panes keep their shell |
| `terminal.shell_mode` | `auto`, `login`, or `non_login`. `auto` starts login shells on macOS |
| `terminal.new_cwd` | `follow`, `home`, `current` (Herdr's process directory), or a fixed path such as `"~/Projects"`. Explicit `--cwd` wins |
| `terminal.kitty_graphics` | Render Kitty graphics images; default `true`. Restart the server or reattach after changing it. In remote sessions the server's setting controls parsing and the local client's setting controls output to the outer terminal |
| `worktrees.directory` | Root for checkouts, created as `<directory>/<repo>/<branch-slug>` |
| `session.resume_agents_on_restore` | Resume supported agent panes into their native conversation after a server restart |
| `session.startup_per_agent_delay_ms` | Spacing between automatic agent restores; `0` disables spacing |
| `remote.manage_ssh_config` | Adds keepalive fallbacks and connection reuse for `herdr --remote`; `false` runs plain `ssh` |
| `server.headless_cols` / `headless_rows` | Virtual terminal size when no client is attached; must be greater than zero |
| `server.allow_unelevated_clients` | Windows only, default `false`: let ordinary same-account clients control an elevated server |

Update checks live under `[update]`: `channel` (`stable` or `preview`), `version_check` (default `true`), and `manifest_check` (default `true`).

## Experimental and advanced

| Setting | Default | Notes |
|---|---|---|
| `experimental.allow_nested` | `false` | Allow launching Herdr inside an existing Herdr pane |
| `experimental.pane_history` | `false` | Persist pane screen history to `session-history.json` |
| `experimental.kitty_graphics` | unset | Deprecated; `terminal.kitty_graphics` wins when both are set |
| `experimental.reveal_hidden_cursor_for_cjk_ime` | `false` | Keep macOS input-method candidate windows tracking the pane cursor |
| `experimental.cjk_ime_agents` | `[]` | Restrict the reveal to focused panes whose detected agent matches (case-insensitive); empty means any pane |
| `experimental.cjk_ime_cursor_shape` | `"steady_block"` | `block`, `steady_block`, `underline`, `steady_underline`, `bar`, or `steady_bar` |
| `experimental.switch_ascii_input_source_in_prefix` | `false` | Switch to an ASCII input source while prefix mode is active (macOS and Windows) |
| `advanced.scrollback_limit_bytes` | `10000000` | Scrollback retained per pane, in bytes; legacy alias `scrollback_lines` |

On Windows, `switch_ascii_input_source_in_prefix` currently supports only the Korean IME. Read [Session state and restore](https://herdr.dev/tui/docs/session-state/) before enabling `pane_history`, because it saves pane contents to disk.

## Environment variables

| Variable | Purpose |
|---|---|
| `HERDR_CONFIG_PATH` | Override the config file path |
| `HERDR_SESSION` | Select a named session for CLI commands |
| `HERDR_SOCKET_PATH` | Low-level socket path override |
| `HERDR_PROCESS_DETECTION` | Linux process detection strategy: `native` (default) or opt-in `child-groups` |
| `HERDR_LOG` | Log filter, for example `HERDR_LOG=herdr=debug` |
| `HERDR_DISABLE_SOUND` | Disable sound playback |

## Logs

Logs are written to the session's data directory, which is `~/.config/herdr/` for the default session (`sessions/<name>/` inside it for a named one):

```text
~/.config/herdr/herdr.log
~/.config/herdr/herdr-client.log
~/.config/herdr/herdr-server.log
```

The docs and `herdr --help` name all three. In the 0.9.5 source the client writes `herdr-client.log` and the server writes `herdr-server.log`; `herdr.log` is only the base name in the help text. The default filter is `herdr=info`. Raise it for local debugging:

```sh
HERDR_LOG=herdr=debug herdr
```

Each log file is capped at 5 MiB. When a file reaches the cap, Herdr deletes it and starts a new one, and it keeps no rotated copies by default.

## Related guides

[Socket API](./socket-api.md), [Integrations](./integrations.md), [Agent workflows](./agent-workflows.md), [Herdr app](./herdr-app.md), [herdr-core](./herdr-core.md).
