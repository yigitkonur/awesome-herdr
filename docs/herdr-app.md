# Building for the Herdr app

A field guide to the files, commands, and mod API you use to build layouts, mods, themes, and key maps for the Herdr app (the desktop app), and to share them.

Canonical sources: [Layouts and mods](https://github.com/herdrdev/herdr-app/blob/v0.1.14/docs/mods.md), [the app guide your agent reads (defaults/AGENTS.md)](https://github.com/herdrdev/herdr-app/blob/v0.1.14/defaults/AGENTS.md), [herdr.d.ts](https://github.com/herdrdev/herdr-app/blob/v0.1.14/defaults/herdr.d.ts), [Herdr guide](https://herdr.dev/guide/), [Gallery](https://herdr.dev/gallery/). Last reviewed: 2026-11-10.

Covers the Herdr app ([herdrdev/herdr-app](https://github.com/herdrdev/herdr-app)) v0.1.14, the release that `releases.herdr.dev/app/latest.json` names on 2026-11-10; its changelog entry is dated 2026-11-08. Unreleased changes on the repo's default branch are not covered. It does not cover Herdr TUI or herdr-core's own CLI (`hc`); see [Agent workflows](./agent-workflows.md) and [herdr-core](./herdr-core.md).

## The idea

The app's whole interface is files. Change a layout, a key or a panel in the app home and the window follows within a second. A **layout** arranges the window; **mods** are small JavaScript programs that draw its panels, menus and dialogs. Nothing in the default interface is special: the spaces sidebar, agents list, tab bar, menus, dialogs and notifications are built from the same parts you have.

Two programs are involved:

| Program | Role |
|---|---|
| `herdr-app` | The window: spaces, tabs, layouts, panels. |
| `hc` (herdr-core) | Runs every terminal and agent. They keep running when the window closes or updates. |

The app is one client of herdr-core. `herdr-app` controls the app; `hc` controls herdr-core.

## The app home

The default app home is `~/.config/herdr-app`, including on macOS and Windows (under your user home). `XDG_CONFIG_HOME` changes the config root. `HERDR_APP_HOME` selects an app home directly and takes precedence. It also selects which running window `herdr-app status` and `herdr-app shot` ask.

| Path | What it decides |
|---|---|
| `layouts/<name>.json` | The window and its whole look. One file per layout (`main`, `terminals`, `win98`, any you add). |
| `keys.json` | What every key does. |
| `settings.json` | The person: zoom, sounds, fonts for every layout. |
| `mods/<name>/` | Panels: small JavaScript programs. Hot reload. |
| `programs.json` | How programs show (name, icon, tile), on top of the built-in table. |
| `themes/<name>.json` | Extra color themes (see below). |
| `AGENTS.md`, `herdr.d.ts`, `gpui-kit.d.ts` | The agent guide and API types. Written by Herdr on every start; do not edit. |
| `icons/`, `frame/` | Shipped program icons and the app's own screens. Herdr rewrites them; put your own files elsewhere. |
| `view.json`, `shared.json`, `data/`, `seen.json`, `installed.json`, `window.json`, `windows.json` | State Herdr writes. Do not edit. |

Spaces, tabs and splits are not in the app home. They live in each machine's core document, and there is no `spaces.json`; use commands to change structure.

## The edit loop

- Edits apply at once. If a file is invalid, the app keeps the last good version and writes why to `<name>.error` (`layout.error`, `keys.error`, `settings.error`, `programs.error`). Check after every edit.
- `herdr-app check <mod folder>` loads a mod once and checks its initial description and eager native elements. It does not lay out the mod or run deferred rows, nested renders, or later async states. Also try the mod in the app.
- `herdr-app shot [file.png]` saves the last rendered window frame as a PNG and prints its absolute path (default: `herdr-shot.png` in the current folder). Herdr must be running.
- Escape hatch: `ctrl-alt-shift-escape` always works. It sets the shown layout and `keys.json` aside (`*.reset-<time>`) and goes back to the default `main` layout. Nothing can rebind it.

```sh
herdr-app check ~/.config/herdr-app/mods/<name>
herdr-app do tab.new --name "fix login" --argv '["claude"]' --task "look at the login bug"
herdr-app do pane.split:right
herdr-app ls          # spaces, their tabs and terminals (sub-agents under their parent)
herdr-app status      # what's on screen: layout, focus, overlays, zoom, errors from files and mods
herdr-app commands    # every command and its arguments
```

`herdr-app ls` and `herdr-app status` inspect the open window; `herdr-app commands` also works without one. `herdr-app do` prints what the command made or `{ "error": "..." }` and exits 1. `herdr-app --skill` prints the agent guide for driving the window.

Commands are the one way to change anything: keys, mods (`run(name, args)`), menus and scripts use the same list. Unknown argument names are errors. There is a [generated command reference](https://github.com/herdrdev/herdr-app/blob/v0.1.14/docs/commands.md); the command names include `space.new`, `tab.new`, `pane.split`, `terminal.open`, `agent.focus`, `layout.switch`, `layout.clone`, `mod.clone`, `mod.open` and `app.settings`.

## Layouts

Each file in `layouts/` is one whole window. `layout.switch` (`ctrl-shift-l`) cycles through layouts and `layout.switch {name}` picks one. Herdr ships `main` ("Herdr"), `terminals` ("Terminals") and `win98` ("Herdr 98"). Add a layout by writing a new file.

Herdr's own layouts and mods are read-only: they are replaced whole on every start. Clone before changing structure or code:

```sh
herdr-app do layout.clone '{"name":"main","as":"my-layout"}'
herdr-app do mod.clone '{"name":"files","as":"my-files"}'
```

The default clone name is `<name>-copy`, and an existing name is refused. `layout.clone` switches to the clone. A cloned layout keeps its mod references, so clone a mod too and point the layout's `content.mod` at it to change code. If you edit a shipped file anyway, the next start moves it to `<name>-edited` and restores Herdr's version. `layout.reset {name}` resets a shipped layout and its clicks.

A layout is a tree of nodes. There are four types:

| Type | Does |
|---|---|
| `block` | Shows content: `{ "mod": "<folder>", "props": {...} }`, `{ "terminal": "t7" }`, `{ "tab": "active" }` (the shown tab's terminals) or `{ "agent": "focused" }` (one agent's terminal, full size). |
| `row` / `column` | Children side by side / stacked. |
| `stack` | Shows one child (`"active": "<child id>"`), with an optional `"header"`. |

Properties any node can have include `id` (unique; commands use it), `size` (`{ "px": 240 }` or `{ "weight": 2 }`), `min` / `max`, `hidden`, `background`, `border`, `radius`, `shadow`, `focus`, `padding`, `movable`, `floating` and `window_drag`. Row and column also take `gap`, `divider` and `resizable`.

A small, complete window. The app guide calls it "the default window", but the shipped `main` layout is larger (it uses mods such as `workspace-chrome`), so treat this as a pattern, not a copy of `main`:

```json
{ "id": "root", "type": "row", "divider": { "width": 1, "color": "border" },
  "children": [
    { "id": "sidebar", "type": "column", "size": { "px": 240 }, "min": 40, "max": 480,
      "divider": { "width": 1, "color": "border" },
      "children": [
        { "id": "spaces", "type": "block", "content": { "mod": "spaces" } },
        { "id": "agents", "type": "block", "content": { "mod": "agents" } } ] },
    { "id": "work", "type": "column",
      "children": [
        { "id": "tabs", "type": "block", "size": { "px": 30 }, "content": { "mod": "tabs" } },
        { "id": "main", "type": "block", "content": { "tab": "active",
          "pane": { "gap": 6, "radius": 6, "border": { "width": 1, "color": "border" },
                    "focus": { "width": 1, "color": "accent" } } } } ] } ] }
```

Sidebar on the right: swap the two children of `root`. No sidebar: set `"hidden": true` on `sidebar` (the shipped `ctrl-shift-b` toggles a node named `sidebar`).

Root-only fields:

| Field | Does |
|---|---|
| `"titlebar": "none"` | Hides the system title bar so the layout draws its own. |
| `"traffic_lights": [x, y]` | Where macOS keeps its window buttons over the layout (px). |
| `"preview": "layouts/<name>.svg"` | The picture the settings screen shows for this layout (png also works). |
| `"terminal_menu": "my-menu"` | The mod for terminal right-clicks, instead of the shipped `menu`. |

Clicks on a layout (sizes, hidden blocks, floating spots, theme picks) are kept in `layouts/.state/`. Do not edit those files; a deliberate edit of the layout file beats a click on that field.

### Pane frames and floating blocks

The `tab` block says how each pane of the shown tab is wrapped:

```json
{ "tab": "active",
  "pane": { "gap": 6, "radius": 6, "background": "surface",
            "border": { "width": 1, "color": "border" }, "focus": { "width": 1, "color": "accent" },
            "header": { "content": { "mod": "pane" }, "height": 30, "position": "top", "reveal": "always" },
            "lone": false } }
```

A `header` is a mod drawn on each pane, one copy per pane, with `props().pane` and `props().terminal`. `lone: true` frames a tab's only pane too.

A floating block sits over its node:

```json
"floating": [ { "id": "board", "content": { "mod": "board" }, "edge": "left", "align": "center", "peek": 52 } ]
```

`edge` is `top`, `right`, `bottom` or `left`; `align` is `start`, `center` or `end`. `peek` (side edges only) makes it a drawer. A floating mod reads `placement()`.

### The look

A layout's own look wins; `settings.json` fills what it leaves unset. The theme picker overrides both. Look fields go on any node, and the nearest node up the tree wins. The app guide adds: "Today only the root's look applies; a block's own look is coming." Put them on the root:

```json
{ "id": "root", "type": "row", "theme": "graphite", "colors": { "accent": "#a7b4c6" },
  "font": "Geist Mono", "font_size": 15, "ui_font": "Geist",
  "terminal_padding": [10, 6], "terminal_opacity": 1, ... }
```

- `theme` is `graphite`, `ink` or `moss` (dark), `paper` (light), or the name of a file in `themes/`. Use `"theme": { "light": "paper", "dark": "graphite" }` to follow the system's light or dark mode.
- `colors` overrides any theme color by name. Name theme colors (`chrome`, `canvas`) rather than writing hex when a layout should work in light and dark.
- `font` and `font_size` are the terminals'; `ui_font` is the mods'. JetBrains Mono, Geist Mono and Geist ship with Herdr. A layout can bring `.ttf` or `.otf` files in a mod's `fonts/` folder.
- Colors are theme names (`border`, `accent`, `surface`, ...) or `#rrggbb[aa]`.

Herdr (main) leaves look fields unset, so the person's settings decide it; Terminals and Herdr 98 bring their own look.

## Themes

A theme is a file at `themes/<name>.json`:

```json
{
  "background": "#21252b",
  "foreground": "#abb2bf",
  "selection": "#323844",
  "cursor": "#abb2bf",
  "ansi": [
    "#454c59", "#e06c75", "#98c379", "#e5c07b", "#61afef", "#c678dd", "#56b6c2", "#abb2bf",
    "#767676", "#e06c75", "#98c379", "#e5c07b", "#61afef", "#c678dd", "#56b6c2", "#abb2bf"
  ]
}
```

`cursor` and `colors` are optional; all colors are `#rrggbb`. Panel colors are derived from these, and `colors` overrides them. New layouts and `themes/*.json` show up in settings by themselves. A theme named like a layout (`themes/win98.json`) is that layout's own: Settings offers it only there. This example is the shipped `atom-one-dark.json`.

## settings.json

`settings.json` is about the person, never a look:

```json
{ "zoom": 1, "sounds": { "enabled": true } }
```

| Key | Does |
|---|---|
| `zoom` | Scales the whole app, 0.5 to 3. Write layout sizes as designed at zoom 1. |
| `sounds` | `{ "enabled": true, "done": "<file>", "blocked": "<file>" }`; `done` and `blocked` replace the bundled MP3s. |
| `core` | The herdr-core binary to use when it isn't where Herdr looks. Read at start. |
| `font`, `font_size`, `ui_font` | Used where the layout doesn't set its own. |
| `font_ligatures` | Programming ligatures are off by default; `true` enables them. |
| `theme`, `colors` | A theme name (or `{light, dark}`) and color overrides, used where the layout sets none. |
| `appearance` | `"light"` or `"dark"` always; absent, the system's. |
| `option_as_alt` | macOS only: `"auto"` (default), `"on"`, `"off"`, `"left"` or `"right"`. |
| `minimum_contrast` | Terminal text contrast ratio; `1` (default) leaves program colors unchanged. |
| `clipboard_write` | `false` blocks terminal programs from writing the local clipboard (default `true`). |
| `pane_scrollbars` | `false` hides the scroll position thumb (default `true`). |
| `telemetry` | `false` stops anonymous usage data (on when absent). |

## keys.json

```json
{
  "global":   { "ctrl-shift-t": "tab.new", "ctrl-shift-o": "pane.split:right", "alt-1": "space.select:1" },
  "terminal": { "ctrl-shift-c": "terminal.copy", "ctrl-left": "send:\u001bb", "ctrl-1": "terminal" },
  "layout:terminals": { "ctrl-shift-pagedown": "space.next", "ctrl-shift-pageup": "space.prev" },
  "mod:editor": { "ctrl-s": "editor.save" }
}
```

- Sections are `global`, `layout:<name>` (while `layouts/<name>.json` shows), `terminal` (a terminal has focus) and `mod:<name>`. The more specific section wins.
- An action is a command (`name`, or `name:value`, where the value fills the command's first argument), `send:<text>` (types into the terminal), `<mod>.<command>` (delivered to that mod's `nextCommand()`), or `terminal` (the program gets the key).
- For named, typed arguments use an object: `"ctrl-shift-r": {"command": "layout.resize", "args": {"id": "sidebar", "px": 240}}`.
- Plain ctrl+letters go to the program unless bound. Programs rely on ctrl+c, ctrl+d, ctrl+l, ctrl+r, ctrl+w, ctrl+a, ctrl+e, ctrl+u, ctrl+k, ctrl+z and ctrl+[, so do not rebind these on your own.
- Herdr installs `keys.json` when it is missing and upgrades an untouched file from an earlier release. Any edit, even whitespace, keeps the whole file as yours; new default shortcuts must then be added by hand. The shipped defaults are `keys.json` (Linux, Windows) and `keys.macos.json` (Mac); an edited keys file is never replaced.

## programs.json

Every pane, agent and terminal carries a `program`: its name, icon and tile, from one table, so every mod shows the same. `programs.json` adds to the built-in table or changes entries field by field:

```json
{ "programs": {
    "lazygit": { "name": "Git", "tile": "#f05032" },
    "mytool": { "name": "My Tool", "icon": "my-icons/mytool.svg", "tint": true,
                "tile": "#334155", "color": "#ffffff", "match": ["mytool-dev"] } },
  "shells": ["xonsh"], "interpreters": ["pipx"] }
```

- `icon` is a path in the app home. `tint: true` is for a one-color glyph; false is for a picture.
- `match` lists other process names for the entry.
- `run` is how to start it (`["cursor-agent"]`) for agents people start from a menu. `knownAgents()` lists the entries that have one. Use programs or shell functions, not aliases.
- Invalid JSON is reported in `programs.error`.

## Mods

```text
~/.config/herdr-app/mods/<name>/
  main.js       the mod (required)
  mod.json      where it first appears
  *.js, *.svg   more modules ("./ui.js"), its own icons
```

`mod.json` examples from the shipped mods: `{ "place": "none" }` and `{ "place": "none", "title": "Spaces" }`. `place` can also be `right`, `left`, `top` or `bottom` (with a `size`). `"focusable": true` lets `pane.go` give a shown copy the keyboard. The first time Herdr sees a folder it docks one copy per `mod.json` into the shown layout; after that, the layouts decide. Saving any file reloads every copy in place (not files the app writes, such as `jsconfig.json`, `.d.ts` files, hidden files or `node_modules`).

A mod from the guide:

```js
import { View, div } from "gpui-kit";
import { v_flex, h_flex } from "gpui-base";
import { exec, spaces, theme, run } from "herdr";

export default class Branches extends View {
  init(_props, cx) {
    this.branch = {};
    cx.timer.every(3000, (cx) => this.refresh(cx));
    this.refresh(cx);
  }

  refresh(cx) {
    cx.spawn(async (cx) => {
      for (const p of spaces()) {
        // on: a space on another machine runs git there.
        const r = await exec("git", ["branch", "--show-current"], { cwd: p.folder, on: p.machine });
        this.branch[p.id] = r.stdout.trim();
      }
      cx.notify();
    });
  }

  render(cx) {
    const t = theme();
    return v_flex().size_full().bg(t.surface).p(10).gap(4).text_size(13).children(
      spaces().map((p) =>
        h_flex().id(`b-${p.id}`).gap(8).hover((s) => s.bg(t.raised))
          .on_click(() => run("space.select", { id: p.id }))
          .child(div().text_color(p.active ? t.foreground : t.muted).child(p.name))
          .child(div().text_color(t.dim).child(this.branch[p.id] ?? ""))));
  }
}
```

Rules that bite:

- `main.js` default-exports a class extending `View`. `init(props, cx)` runs once; `render(cx)` runs again after `cx.notify()` and whenever Herdr's live data changes (spaces, agents, terminals, focus, theme, shared state). Do not poll those.
- Module code runs once per source version and is shared by all copies. Keep per-copy state and host calls in `init`, not at the top of the file.
- Never keep a `cx` and use it later; every callback gets its own.
- A copy stays alive while its block is in the layout, shown or not, and its timers keep running while hidden, so poll gently.
- There is no `setTimeout` or `setInterval` (use `cx.timer`) and no top-level `await` (use `cx.spawn` in `init`).
- Use `theme()` colors so the mod follows the user's theme.
- Animate natively, never with a timer: use `.frames(...)`, `svg(arc).spin(900)`, `.loop("opacity", { from: 0.4, to: 1, period: 1200 })` or `.transition(...)`.
- Images and SVGs are referenced from the app home: `image("mods/<name>/logo.svg")` (full color) and `svg("mods/<name>/icon.svg")` (tinted with the text color).
- Mods use gpui-kit, a native GPU UI: JavaScript describes GPUI elements and Rust draws them. The type files in the app home are the truth: `gpui-kit.d.ts` for elements and `herdr.d.ts` for the app's data and commands.
- The shipped mods are examples: `spaces`, `agents`, `tabs`, `menu`, `prompt`, `confirm`, `help`, `toast`, `picker`, `peek`, `pane` and `worktree`.

### What a mod can read

All of it is in `herdr.d.ts`. Live data re-renders the mod when it changes.

| Call | Returns |
|---|---|
| `spaces()` | Spaces in order, each with `id`, `name`, `named`, `folder`, `machine`, `branch`, `active`, `status` and `tabs`. |
| `agents()` | Terminals whose program reports a status: `address`, `status`, `app`, `program`, `title`, `pinned`, `focused`. |
| `panes()` | Every pane in every tab: `pane`, `terminal`, `mod`, `title`, `cwd`, `branch`, `status`, `focused`, `zoomed`, `movable`. |
| `terminals()` | Every core terminal as `hc ls --json` describes it. |
| `machines()` | Machines' layout documents: `loading`, `ready` or `unavailable`. |
| `focused()` | Actual terminal and pane focus. |
| `layout()`, `layouts()` | The shown layout; the names of every layout. |
| `theme()`, `themes()`, `fonts()` | Theme colors by name; every theme `app.theme` can use; font families on this machine. |
| `settings()`, `keys()`, `commands()` | The settings the app runs with; every key binding; every app command with its arguments. |
| `window()`, `placement()` | The window (platform, title bar, buttons, maximized); where a floating mod sits. |
| `props()` | The props this copy was given in the layout or overlay. |
| `shared(key)` | A value every mod can see (persisted). |
| `updates()`, `telemetry()` | Versions and waiting updates; the telemetry state. |
| `home()`, `appHome()` | The user's home directory; the app folder. |

Agent status is `working`, `blocked`, `done` or `idle`. `done` means it finished while the user wasn't looking.

### What a mod can do

| Call | Does |
|---|---|
| `run(command, args)` | Runs an app command, the same ones `keys.json` binds. |
| `openOverlay({ mod, props, kind, ... })`, `closeOverlay(id)` | Shows a mod above everything as a `dialog`, `popup` or `window`. |
| `notify({ title, body, level, icon, timeout, action })` | Posts a notification; `action` runs a command when clicked. |
| `exec(cmd, args, { cwd, on, timeout })` | Runs a program with the user's real environment. `on` runs it on another machine; `timeout` defaults to 30,000 ms and is capped at 600,000. |
| `hc(args)` | Runs `hc` (herdr-core) with the given arguments. |
| `readTextFile(path, { on })`, `writeTextFile(path, text, expected)` | Reads UTF-8 text (up to 1 MiB); writes only if the file still matches `expected`. |
| `watchFolder(dir)` | Resolves with changed paths the next time anything under `dir` changes. |
| `pickFolder({ prompt })`, `playSound(sound)`, `knownAgents({ on })` | The system folder picker; an attention sound or MP3; the agents people can start. |
| `setShared(key, value)` | Sets a shared value; every mod re-renders. |
| `nextCommand()` | Waits for the next key command sent to this mod. |
| `setAgentOrder(addresses)` | Sets the `agent.next` and `agent.prev` order to match the list a mod displays. |

Mods can also use `localStorage` (per mod copy), `console.log`, `fetch` and `fs/promises` (read in your home folder, write under `~/.config/herdr-app`). `exec` output is capped at 8 MiB; `writeTextFile` and `watchFolder` work on this machine only.

What a mod cannot do: use HTML, CSS, a web view, Node APIs or `setTimeout`; draw outside its block except through overlays; change how a terminal itself draws text; read or change other mods' code at run time.

### Trust

Mods are trusted code, not sandboxed. A mod can run programs with your environment, fetch URLs and read files; there is no permission prompt for each program or network request. The built-in file API limits writes to the app home, but a mod can run a program to write elsewhere, so that is not a security boundary. Layouts can load mods, so check those references too. The app also keeps a local control socket in its home so agents can drive the window: treat access to that folder as access to the window and its commands. Read the [security and privacy page](https://github.com/herdrdev/herdr-app/blob/v0.1.14/docs/security.md) before installing someone else's mod.

## Installing from the gallery

People share layouts at herdr.dev/layouts and mods at herdr.dev/mods. Each gallery page has a one-line prompt for your agent:

```text
Read ~/.config/herdr-app/AGENTS.md, then add this layout: herdr.dev/layouts/herdrdev/pasture
Read ~/.config/herdr-app/AGENTS.md, then add this mod: herdr.dev/mods/herdrdev/tmux-prefix
```

Paste it into an agent. The gallery says the agent reads every file first, adds the layout next to yours and switches to it; for a mod it adds the mod and its keys. Per the app guide, the agent:

1. Reads the recipe and every file before writing anything, and tells you if a mod reaches the network, runs programs (`exec`, `hc`) or reads files outside its own folder.
2. Copies the layout file to `layouts/` and each mod folder to `mods/`, leaving out the recipe and preview. It never overwrites: if a name is taken it renames the new one.
3. Fits it to your setup only where its assumptions don't hold or you ask. If the files don't work on this version, it builds from the recipe instead.
4. Merges a mod's `keys.json` into yours and asks before replacing a key you already use.
5. Runs `herdr-app check` on each mod and, for a layout, `layout.switch {name}`. Your own layout stays as it was; `ctrl-shift-l` switches back, and deleting the files removes it.

Layouts and mods aren't reviewed by Herdr.

## Sharing a layout or mod

1. Put the folder in a public GitHub repo (one folder each if there are several). A layout folder has `layouts/<name>.json` and the `mods/<name>/` it needs. A mod folder has only `mods/<name>/`, plus a `keys.json` snippet if it needs keys; it has no `layouts/` folder.
2. Write a `RECIPE.md`, the brief another agent could build it from with an empty folder, and save a screenshot as `preview.png`.
3. Add the repo topic `herdr-layout` for a layout or `herdr-mod` for a mod. It shows up at herdr.dev/layouts or herdr.dev/mods within the hour, under Community. There is no sign-up.

The gallery offers a prompt that does step 2 for you:

```text
Read ~/.config/herdr-app/AGENTS.md, then write a RECIPE.md for my <name> layout the way it describes: a brief another agent could build it from with an empty folder. Put the layout, its mods, the recipe and a screenshot named preview.png in one folder, push it to a public GitHub repo and add the topic herdr-layout.
```

A `RECIPE.md` has this order:

1. `# Name`, one paragraph of what the person sees, `![Name](preview.png)`.
2. What you see: the regions, sizes, colors and type.
3. How it behaves: every agent status and how it looks; what clicks, keys and hovers do.
4. Built from: the node tree, each mod and its props, the `herdr` functions and commands it calls, any programs it runs.
5. Watch out: what tripped the build up, limits, what it assumes.
6. Done when: checks that prove a build works.

Herdr's own [Pasture example](https://herdr.dev/layouts/herdrdev/pasture/) shows a finished recipe. Community pictures are screened before they appear.

## Community projects

The README lists the community layouts, mods and themes for the Herdr app under [Herdr app layouts, mods, and themes](../README.md#2-herdr-app-layouts-mods-and-themes). A few to read as examples:

| Kind | Project | What it does |
|---|---|---|
| Layout | [runkids/skillshare · herdr/skillshare](https://github.com/runkids/skillshare/tree/main/herdr/skillshare) | Adds a Herdr app layout with a skillshare panel for viewing, auditing and syncing skills, agents, MCP servers, plugins and hooks. |
| Layout | [eliasstravik/shepherdr](https://github.com/eliasstravik/shepherdr) | Organizes coding agents in a Herdr app layout with per-space assistants and task cards, running tasks in separate worktrees. |
| Layout | [vib-z/herdr-layouts](https://github.com/vib-z/herdr-layouts) | Adds seven Herdr app layouts, including Control Panel, Falling Code, Fleet Tab, Night City, Queue, The Crew Board and The Noir Office. |
| Mod | [rabeeh-ta/herdr-git-graph](https://github.com/rabeeh-ta/herdr-git-graph) | Shows a Git commit graph in the Herdr app and offers branch, merge, rebase, and other repository actions. |
| Mod | [cybertron288/herdr-mods](https://github.com/cybertron288/herdr-mods) | Adds Herdr app mods for file browsing, GitHub Actions, JavaScript scripts, session status, Slack and YouTube Music. |
| Theme | [Codesmith28/gruvbox-herdr-app](https://github.com/Codesmith28/gruvbox-herdr-app) | Adds six Gruvbox themes and a contrast-switching mod to the Herdr app. |

## Related guides

[herdr-core](./herdr-core.md), [Agent workflows](./agent-workflows.md), [Socket API](./socket-api.md), [Configuration](./configuration.md), [Integrations](./integrations.md).
