# Herdr Configuration Field Guide

This guide summarizes the Herdr configuration surface for people building configs, keymap packs, terminal presets, and integrations.

Canonical source: [CONFIGURATION.md](https://github.com/ogulcancelik/herdr/blob/master/CONFIGURATION.md). Last reviewed: 2026-05-17.

## Config Location

Herdr reads global config from:

```text
~/.config/herdr/config.toml
```

Named sessions share this config file. Sessions are runtime and socket namespaces, not replacements for workspaces. Session state lives separately under paths such as:

```text
~/.config/herdr/session.json
~/.config/herdr/sessions/<session>/session.json
```

Useful commands:

```sh
herdr --default-config
herdr server reload-config
herdr server stop
herdr session list --json
herdr session attach work
herdr session stop work
herdr session delete side-project
```

## Reload Model

`herdr server reload-config` asks the running server to read, parse, validate, and apply `config.toml`.

Reloadable areas include:

| Area | Reload behavior |
|---|---|
| Keybindings and prefix | Reloadable |
| Theme and custom theme colors | Reloadable |
| `ui.confirm_close` | Reloadable |
| `ui.agent_panel_scope` | Reloadable |
| `ui.toast.delivery` | Reloadable |
| Server-side `ui.sound` policy | Reloadable |
| `experimental.kitty_graphics` | Reloadable |
| `advanced.scrollback_limit_bytes` | Applies to panes created after reload |
| `ui.sidebar_width` | Default width reloads; current width changes only while config-owned |

Startup-only or special cases:

| Setting | Caveat |
|---|---|
| `onboarding` | Does not reopen onboarding during reload |
| `experimental.allow_nested` | Checked before launch; needs restart |
| Existing pane scrollback buffers | Not resized during reload |
| Terminal notifications and sounds | Client-local side effects sent to the foreground attached client |

If TOML cannot be read or parsed, reload applies nothing and keeps the running state. If keybindings are invalid, Herdr keeps the current keybindings while applying other valid settings where possible.

## Keybindings

Keybindings live under `[keys]`.

Supported syntax:

| Syntax | Examples |
|---|---|
| Plain keys | `n`, `x`, `-`, `` ` `` |
| Modifiers | `ctrl+b`, `shift+n`, `alt+x`, `cmd+x`, `super+x` |
| Special keys | `enter`, `esc`, `tab`, `backspace`, `left`, `right`, `up`, `down` |
| Function keys | `f1`, `f12` |
| Uppercase shorthand | `D` behaves like `shift+d` |

The most reliable bindings are plain keys, `ctrl+letter`, `esc`, `tab`, `enter`, and function keys. `alt`, `cmd`/`super`, and punctuation-with-modifiers can vary by terminal or tmux setup.

Core defaults and common actions:

| Key | Default | Action |
|---|---|---|
| `prefix` | `ctrl+b` | Enter or leave navigate mode |
| `new_workspace` | `n` | Create workspace |
| `rename_workspace` | `shift+n` | Rename workspace |
| `close_workspace` | `shift+d` | Close workspace |
| `new_tab` | `c` | Create tab |
| `split_vertical` | `v` | Split side-by-side |
| `split_horizontal` | `-` | Split stacked |
| `close_pane` | `x` | Close focused pane |
| `zoom` | `f` | Zoom focused pane |
| `resize_mode` | `r` | Enter/leave resize mode |
| `toggle_sidebar` | `b` | Collapse or expand sidebar |

Many direct terminal-mode actions are supported but unset by default, including previous/next workspace, previous/next tab, previous/next agent, pane focus, close tab, rename tab, rename pane, reload config, and edit scrollback.

## Indexed Keybinds

`[keys.indexed]` binds number keys `1` through `9` as positional shortcuts.

```toml
[keys.indexed]
tabs = ""
workspaces = ""
agents = ""
```

Each value is a modifier combo only. Empty values disable the family.

| Family | Behavior |
|---|---|
| `tabs` | Switch to tab 1-9 in active workspace, left to right |
| `workspaces` | Switch to workspace 1-9 in sidebar order, top to bottom |
| `agents` | Focus visible agent row 1-9 in panel order |

## Command Keybindings

Use `[[keys.command]]` to bind prefix-mode keys to commands.

```toml
[[keys.command]]
key = "g"
type = "pane"
command = "lazygit"
```

| Type | Behavior |
|---|---|
| `shell` | Run the command detached in the background |
| `pane` | Open a temporary zoomed pane, run the command, then close it |

Commands run through `/bin/sh -lc` and receive Herdr environment variables:

| Variable | Meaning |
|---|---|
| `HERDR_SOCKET_PATH` | Active Herdr socket path |
| `HERDR_BIN_PATH` | Current Herdr binary path |
| `HERDR_ACTIVE_WORKSPACE_ID` | Active workspace id |
| `HERDR_ACTIVE_TAB_ID` | Active tab id |
| `HERDR_ACTIVE_PANE_ID` | Focused pane id |
| `HERDR_ACTIVE_PANE_CWD` | Focused pane cwd |

## Themes

Herdr ships with 17 built-in themes:

`catppuccin`, `catppuccin-latte`, `tokyo-night`, `tokyo-night-day`, `dracula`, `nord`, `gruvbox`, `gruvbox-light`, `one-dark`, `one-light`, `solarized`, `solarized-light`, `kanagawa`, `kanagawa-lotus`, `rose-pine`, `rose-pine-dawn`, and `vesper`.

```toml
[theme]
name = "tokyo-night"
```

Theme names normalize separators, so `tokyo-night`, `tokyonight`, and `tokyo_night` work.

Custom themes can override tokens such as `accent`, `panel_bg`, `surface0`, `surface1`, `surface_dim`, `overlay0`, `overlay1`, `text`, `subtext0`, `mauve`, `green`, `yellow`, `red`, `blue`, `teal`, and `peach`.

## UI, Toasts, Sound

Important UI settings:

| Setting | Default | Notes |
|---|---|---|
| `ui.sidebar_width` | `26` | Base sidebar width before auto-scaling |
| `ui.mouse_capture` | `true` | Capture mouse input for Herdr UI |
| `ui.confirm_close` | `true` | Ask before closing a workspace |
| `ui.prompt_new_tab_name` | `true` | Set `false` for instant generated tab names |
| `ui.show_agent_labels_on_pane_borders` | `false` | Show detected/reported agent labels on borders |
| `ui.agent_panel_scope` | `all` | Agent list scope: `current` or `all` |

Toast delivery values:

| Value | Meaning |
|---|---|
| `off` | Disable background popup notifications |
| `herdr` | Show inside Herdr |
| `terminal` | Use terminal notification escape support when available |
| `system` | Use OS helper when available |

macOS system notifications can use `terminal-notifier`:

```sh
brew install terminal-notifier
```

## Experimental and Advanced

| Setting | Default | Notes |
|---|---|---|
| `experimental.allow_nested` | `false` | Allow launching Herdr from inside a Herdr-managed pane |
| `experimental.kitty_graphics` | `false` | Enable experimental local Kitty graphics rendering for attached clients |
| `advanced.scrollback_limit_bytes` | `10000000` | Per-pane retained scrollback in bytes; `0` disables pane scrollback |

## Logs

Herdr writes logs under `~/.config/herdr/`.

Common files:

```text
~/.config/herdr/herdr.log
~/.config/herdr/herdr-client.log
~/.config/herdr/herdr-server.log
```

Increase verbosity for local debugging:

```sh
HERDR_LOG=herdr=debug herdr
```
