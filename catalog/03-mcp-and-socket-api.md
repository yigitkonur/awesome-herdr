# Awesome Herdr: Connect through MCP and the socket API

The full list for domain 3 of [Awesome Herdr](../README.md#3-connect-through-mcp-and-the-socket-api), ordered by GitHub stars.

- [MCP servers (21)](#mcp-servers)
- [Socket API and herdr-core clients and SDKs (40)](#socket-api-and-herdr-core-clients-and-sdks)
- [Chat alerts: Telegram, Discord, and Slack (33)](#chat-alerts-telegram-discord-and-slack)
- [Desktop, mobile, and webhook notifications (72)](#desktop-mobile-and-webhook-notifications)
- [Telemetry, events, and quota streaming (32)](#telemetry-events-and-quota-streaming)
- [Voice, hardware, and remote bridges (57)](#voice-hardware-and-remote-bridges)
- [Protocol and third-party bridges (78)](#protocol-and-third-party-bridges)

---

## 3. Connect through MCP and the socket API

*333 projects. Protocols, clients, bots, and event bridges that link Herdr to external tools, editors, and messaging apps.*

### MCP servers

*21 projects. Servers that expose Herdr operations as MCP tools for compatible AI clients.*

| Project | Stars | What it does |
|---|--:|---|
| [**runchr-works/herdr-mesh**](https://github.com/runchr-works/herdr-mesh) | 13 | Connects multiple Herdr instances into a coordinated mesh over Model Context Protocol. |
| [**rmngl/herdr-mesh**](https://github.com/rmngl/herdr-mesh) | 13 | Exposes Herdr pane management, agent messaging, and contextual handoffs through an MCP server. |
| [**whshang/herdr-mcp**](https://github.com/whshang/herdr-mcp) | 10 | Adds a stable MCP and OAuth bridge for remote web planners to inspect and control local Herdr workspaces. |
| [**ryanthedev/herderp**](https://github.com/ryanthedev/herderp) | 5 | Adds Claude Code MCP tools for managing agents and terminals across Herdr TUI and herdr-core, including remote hosts and session history. |
| [**aquaherd/goose-herdr**](https://github.com/aquaherd/goose-herdr) | 3 | Connects Goose to Herdr TUI through an MCP extension and reports Goose lifecycle state to the sidebar. |
| [**eugeneb50/herdr-mcp**](https://github.com/eugeneb50/herdr-mcp) | 2 | Exposes Herdr workspace and pane controls as tools to any Model Context Protocol (MCP) client. |
| [**54rt1n/herdr-simple-mcp**](https://github.com/54rt1n/herdr-simple-mcp) | 2 | Provides a lightweight Model Context Protocol server for driving Herdr from Claude Desktop and Cursor. |
| [**Orange-County-AI/herdr-mcp**](https://github.com/Orange-County-AI/herdr-mcp) | 2 | Exposes Herdr's socket API as a local or remote MCP server. |
| [**thomasfossum/herdr-mcp**](https://github.com/thomasfossum/herdr-mcp) | 2 | Lets MCP clients control a running Herdr session: see agent status, open tabs and panes, start agents, send them work and run worktree-isolated jobs. Runs over stdio or Streamable HTTP in standard-library Python with Docker and client examples. |
| [**nytafar/herdr-spawn**](https://github.com/nytafar/herdr-spawn) | 1 | Exposes an MCP tool that starts coding agents on your machines from a chat prompt, with a Claude Code Remote Control link when available. |
| [**boozedog/herdr-mcp**](https://github.com/boozedog/herdr-mcp) | 1 | Coordinates agents in Herdr TUI panes through a Deno MCP server with configurable workflow roles. |
| [**husniadil/olympus**](https://github.com/husniadil/olympus) | 1 | Provides a terminal you can drive from code: create, drive, observe and tear down real terminal sessions on zmx, tmux, meja or herdr, through a Go package, a CLI and a stdio MCP server. |
| [**jhionan/herdr-computer-use**](https://github.com/jhionan/herdr-computer-use) | 1 | Adds a macOS helper and MCP server that lets agents observe and operate desktop apps and signed-in browser windows, with Herdr TUI plugin actions to set it up and manage it. Needs macOS 14 and Swift. |
| [**nativestrider/herdr-mesh-safe**](https://github.com/nativestrider/herdr-mesh-safe) | 0 | Exposes lease-scoped Herdr agent coordination through MCP while restricting arbitrary commands and unscoped deletion. |
| [**Kuznetsov-Ilia/agy**](https://github.com/Kuznetsov-Ilia/agy) | 0 | Maintains a warm Antigravity worker pool in Herdr and exposes delegation tools to Cursor through an MCP server. |
| [**aelaguiz/herdr-mcp**](https://github.com/aelaguiz/herdr-mcp) | 0 | Exposes Herdr TUI workspace inspection, pane control and agent prompting to MCP clients through the Herdr CLI. |
| [**islam3zzat/herdr-mcp**](https://github.com/islam3zzat/herdr-mcp) | 0 | An MCP server that lets AI assistants inspect and control coding agents running in Herdr through a socket-based communication bridge. |
| [**bonsai/herdr-mcp**](https://github.com/bonsai/herdr-mcp) | 0 | Lets OpenCode rename and blink Herdr TUI tabs or trigger speech through MCP, with additional plugin actions and monitoring. |
| [**simozampa/agent-relay**](https://github.com/simozampa/agent-relay) | 0 | Provides a secure, asynchronous MCP gateway for persistent coding agents. |
| [**kshvidler/peerband-cli**](https://github.com/kshvidler/peerband-cli) | 0 | Connects ChatGPT, Claude, or any MCP client to the coding agents running in Herdr through the PeerBand relay. Ships the peerband CLI and a Herdr plugin; the relay is a hosted service. |
| [**yonatangross/herdr-desktop-bridge**](https://github.com/yonatangross/herdr-desktop-bridge) | 0 | Runs a stdio MCP server that lets Claude Desktop or any MCP client read a Herdr floor and leave messages for agents. Gives the client a mailbox and a doorbell without control of the panes. |

### Socket API and herdr-core clients and SDKs

*40 projects. Clients, libraries, and command-line tools for Herdr TUI and herdr-core APIs.*

| Project | Stars | What it does |
|---|--:|---|
| [**backpine/remote-agent-workspace**](https://github.com/backpine/remote-agent-workspace) | 64 | Provides an always-on remote agent environment: edit on macOS, run Herdr work on Linux, synchronize files with Syncthing, and expose services through Cloudflare Tunnel and Caddy. |
| [**dmmulroy/herdr-ts-sdk**](https://github.com/dmmulroy/herdr-ts-sdk) | 57 | Provides an Effect-native TypeScript SDK for Herdr's local protocol-21 socket API. |
| [**0xGosu/herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot) | 31 | Prompts a running coding CLI through the Herdr API. A training mode observes user actions, safety checks block dangerous operations, and an optional autonomous mode can continue prompting after sufficient setup. |
| [**mitkox/dsh-herdr**](https://github.com/mitkox/dsh-herdr) | 17 | Reports DeepSeek Harness agent state to herdr-core via OSC 7501 and displays sessions in a Herdr app panel. |
| [**Mic92/herdr-eternal**](https://github.com/Mic92/herdr-eternal) | 13 | A roaming-friendly transport for `herdr --remote` using QUIC with a WebSocket fallback, exact byte-stream resumption, and OIDC authentication. |
| [**ryonakae/shepherd**](https://github.com/ryonakae/shepherd) | 11 | A worker-observability service and set of runtime bridges for coding agents managed by Herdr. |
| [**TheMetalStorm/herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin) | 10 | Integrates Freebuff agents with Herdr by reading PTY output and local session files, then reporting idle, working, and blocked states through the socket API. |
| [**gejiliang/herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw) | 5 | Treats OpenClaw TUI sessions as Herdr agents, with live state, model information, and token use in the sidebar. A background watcher parses OpenClaw status lines and reports them through the socket API. |
| [**54rt1n/herdr-python-client**](https://github.com/54rt1n/herdr-python-client) | 3 | Provides typed Python bindings and socket utilities for automating Herdr programmatically. |
| [**usrivastava92/herdr-wakeup**](https://github.com/usrivastava92/herdr-wakeup) | 3 | Prevents macOS or Linux from sleeping while Herdr agents are working. It enables an operating-system sleep inhibitor when activity begins and releases it when every agent is idle. |
| [**egriff38/effect-herdr**](https://github.com/egriff38/effect-herdr) | 2 | Controls the Herdr terminal multiplexer through a typed Effect-TS SDK. |
| [**akhileshrangani4/herdr-bridge**](https://github.com/akhileshrangani4/herdr-bridge) | 2 | An HTTP bridge with a terminal-friendly control panel for Herdr agents. |
| [**klittle32/letta-herdr-mod**](https://github.com/klittle32/letta-herdr-mod) | 2 | Modifies Letta Code so sessions running in Herdr report accurate idle, working, and blocked states to the sidebar. |
| [**uuie/reasonix-herdr**](https://github.com/uuie/reasonix-herdr) | 2 | Reports Reasonix agent lifecycle states to Herdr in real time and adds native workspace and pane controls for supervising Reasonix alongside other agents. |
| [**QuiquiMatCom2004/herdr-py**](https://github.com/QuiquiMatCom2004/herdr-py) | 1 | Lets Python programs control Herdr workspaces, panes, agents, and other resources through its socket API. |
| [**fabzter/herdrbridge**](https://github.com/fabzter/herdrbridge) | 1 | Lets Python bridges drive Herdr agents, track sessions, extract replies, and navigate approval prompts through the CLI and socket API. |
| [**lib-x/herdr-sock-go**](https://github.com/lib-x/herdr-sock-go) | 1 | Connects Go programs to the Herdr TUI newline-delimited socket API with typed and raw methods. |
| [**maxandersen/jherdr**](https://github.com/maxandersen/jherdr) | 1 | Connects Java programs to the Herdr TUI socket API using a scripting facade, generated typed methods or raw calls. |
| [**cyperx84/herdr-api**](https://github.com/cyperx84/herdr-api) | 1 | Connects Go programs to the Herdr TUI socket API with typed agent models and event subscriptions. |
| [**flaricy/herdr-bridge**](https://github.com/flaricy/herdr-bridge) | 1 | Reports DeepSeek Harness activity to the Herdr pane that hosts it, including live working, blocked, and idle states, without requiring changes to Herdr. |
| [**vika2603/herdr-client**](https://github.com/vika2603/herdr-client) | 1 | Provides a typed Go client and plugin toolkit for Herdr's socket API, generated from the schema the herdr binary prints and covering all 102 methods of protocol 22. Adds a reconnecting session mirror, the pane graphics frame stream, and the manifest parser and entrypoint dispatch a Go plugin needs. |
| [**JefeLabs/herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker) | 0 | Adds a self-hosted REST and WebSocket API for Herdr to spawn and steer coding agents with parent-child federation. |
| [**Phoobobo/herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration) | 0 | Connects TraeX lifecycle hooks to Herdr's agent-reporting socket methods, giving TraeX panes correct idle, working, and blocked status. |
| [**cdpath/herdr-warp**](https://github.com/cdpath/herdr-warp) | 0 | Integrates the Warp Agent CLI with Herdr. It can send prompts, wait for output, approve or reject actions, and infer idle, working, and blocked status from terminal output. |
| [**kevinWangSheng/herdr-kit**](https://github.com/kevinWangSheng/herdr-kit) | 0 | Saves and restores declarative Herdr TUI pane layouts, watches events, and calls socket methods. Includes two plugins and an agent skill. |
| [**atnine-ai/herdr-bridge**](https://github.com/atnine-ai/herdr-bridge) | 0 | Connects Herdr panes to chat services for communicating with agents outside the terminal. |
| [**hisetu/pi-herdr-remote**](https://github.com/hisetu/pi-herdr-remote) | 0 | Pi-native tools for operating Herdr servers on explicitly approved SSH hosts. |
| [**bradydibble/herdi**](https://github.com/bradydibble/herdi) | 0 | A private remote client and relay for Herdr; development moved away from its former public fork. |
| [**alex-devdone/herdr-remote-agent-watch**](https://github.com/alex-devdone/herdr-remote-agent-watch) | 0 | Shows a Claude session running behind SSH and tmux as a live Herdr sidebar agent. It also provides more resilient SSH and remote-Herdr wrapper commands. |
| [**AgentWorkforce/herdr-relay-bridge**](https://github.com/AgentWorkforce/herdr-relay-bridge) | 0 | A relay bridge intended to connect Herdr agents as a cooperating team. The source catalog gives no further protocol details. |
| [**pinksaucepasta/paperboat-helper**](https://github.com/pinksaucepasta/paperboat-helper) | 0 | A remote runtime for Paperboat environments, covering PTYs, Herdr agents, previews, images, activity reporting, and configuration synchronization. |
| [**trillium/herdr-tailscale**](https://github.com/trillium/herdr-tailscale) | 0 | Automatically attaches trusted Tailscale peers to Herdr as remote tabs. |
| [**opencharly/plugin-herdr**](https://github.com/opencharly/plugin-herdr) | 0 | Controls Herdr terminal multiplexer sessions over its NDJSON socket API using Charly commands. |
| [**rudironsoni/HerdrKit**](https://github.com/rudironsoni/HerdrKit) | 0 | Provides a Swift 6 client kit implementing Herdr JSON socket API protocols 17 through 22. |
| [**brooswit-factory/jsHerdrSDK**](https://github.com/brooswit-factory/jsHerdrSDK) | 0 | Provides a typed TypeScript client for the herdr socket API, generated from its published JSON Schema. |
| [**brooswit-factory/drovr**](https://github.com/brooswit-factory/drovr) | 0 | Wraps a TypeScript Herdr TUI SDK to detect blocked agents and correct reported agent states. |
| [**vinceferro/herdr-tg · crates/herdr-client**](https://github.com/vinceferro/herdr-tg/tree/HEAD/crates/herdr-client) | 0 | Reads Herdr TUI state and pane output with a typed Rust client for the socket protocol. |
| [**feelautom/herdr-reliable-messaging**](https://github.com/feelautom/herdr-reliable-messaging) | 0 | Delivers long messages to named Herdr panes with verification that the terminal actually submitted them, so a Codex composer does not keep staged text. Windows only and ships an agent skill. |
| [**adihex/herdr-ipc**](https://github.com/adihex/herdr-ipc) | 0 | Adds workspace-scoped Unix-socket messaging for pane workers, carrying blocker reasons, artifacts, and handoffs beyond Herdr's lifecycle states. Also ships an Agent Plugin manifest with hooks. |
| [**sjennings/polytoken-herdr-core**](https://github.com/sjennings/polytoken-herdr-core) | 0 | Reports Polytoken session status to herdr-core through hooks and adds Polytoken to the Herdr app agent menu. Includes a pane mod to start or resume sessions and check the install. |

### Chat alerts: Telegram, Discord, and Slack

*33 projects. Bot and channel alerts that ping you when agents finish or need input.*

| Project | Stars | What it does |
|---|--:|---|
| [**alexei-led/ccgram**](https://github.com/alexei-led/ccgram) | 289 | Maps forum topics to terminal windows running Claude Code, Codex, Gemini, Pi, or a shell. It relays output and input through Herdr or tmux so sessions remain usable from a phone. |
| [**permgps/herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents) | 87 | Creates a Telegram forum topic for each Herdr agent so users can receive status updates and reply to prompts. |
| [**dcolinmorgan/herdr-push**](https://github.com/dcolinmorgan/herdr-push) | 10 | Forwards agent status changes to the herdr-remote relay using only curl and system Python or jq. A single relay setting enables mobile, menu-bar, or Telegram monitoring, and a test action checks the connection. |
| [**natori-hrj/herdr-hail**](https://github.com/natori-hrj/herdr-hail) | 7 | Connects Herdr to Slack and Discord through a two-way webhook bridge. Blocked-agent alerts can be answered through replies or action buttons without opening a network tunnel. |
| [**gaijinjoe/herdres**](https://github.com/gaijinjoe/herdres) | 7 | Maps every live Herdr pane to a Telegram forum topic. Agent activity appears in the topic, and bot commands can send input back to the matching pane from any device. |
| [**mvallebr/herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin) | 6 | A Telegram bot companion that maps Herdr agents to forum topics and provides remote control without placing an LLM between the user and the pane. |
| [**etinpres/herdr-telegram-remote**](https://github.com/etinpres/herdr-telegram-remote) | 4 | Controls Codex and Claude Code panes in Herdr from Telegram. |
| [**TerrifiedBug/omp-telegram**](https://github.com/TerrifiedBug/omp-telegram) | 4 | Connects Oh My Pi sessions to Telegram and uses Herdr to spawn and manage sessions remotely. |
| [**cokekitten/herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge) | 4 | Sends Telegram notifications when an agent finishes or waits for input. Replies, including files, are delivered to the correct pane without requiring a public server or port tunnel. |
| [**hkdom/herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate) | 3 | Sends blocked Herdr agent approvals to Telegram and supports risk-tiered automatic approval policies. |
| [**naturalmoods/herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify) | 3 | Sends Telegram alerts when agents finish or need input and routes replies back to Herdr TUI or herdr-core agents. |
| [**revanp/herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence) | 3 | Publishes the active Herdr project, current agent, and total active-agent count through Discord Rich Presence using a local RPC service, with no bot or external server required. |
| [**amurru/herdr-whistle**](https://github.com/amurru/herdr-whistle) | 3 | Manages Herdr TUI agents from Telegram, including listing agents, reading output, sending text, and starting or closing panes. |
| [**lsisoft/herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge) | 2 | Sends blocked-agent alerts to Telegram or Slack and routes replies to the originating Herdr TUI or tmux pane. |
| [**fzf/herdr-mattermost**](https://github.com/fzf/herdr-mattermost) | 2 | Uses Mattermost as a front end for Herdr agents: each watched channel is a workspace, each root post starts an agent, and thread replies become prompts. Agent output and blocked or done status are relayed back into the thread. |
| [**juninaba/herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify) | 1 | Sends Slack notifications when Herdr agents finish or become blocked. |
| [**barnuri/herdr-notifications**](https://github.com/barnuri/herdr-notifications) | 1 | Sends Telegram, Discord, or Slack alerts when Herdr TUI agents become idle, blocked, or done, with per-status filters. |
| [**ralphilius/herdr-discord**](https://github.com/ralphilius/herdr-discord) | 1 | Turns Discord channels into Herdr workspaces and threads into agent tabs, relaying agent output into the thread. Needs your own Discord bot token. |
| [**shindakun/goat-herdr**](https://github.com/shindakun/goat-herdr) | 1 | Sends an alert to Telegram, Discord, Slack, ntfy, Pushover, Pushbullet, a webhook or the desktop when a Herdr TUI agent is blocked or done. Lets you answer the agent from a Telegram thread. |
| [**egemenyildiz/herdr-slack**](https://github.com/egemenyildiz/herdr-slack) | 0 | Connects Slack to local Herdr agents so users can browse sessions, answer prompts, and launch agents without a tunnel. |
| [**dcieslak19973/herdr-slackr**](https://github.com/dcieslak19973/herdr-slackr) | 0 | Displays a real-time Slack feed inside a Herdr pane, using Socket Mode with polling as a fallback. |
| [**elkraps/herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify) | 0 | Sends configurable Telegram alerts for Herdr TUI agent states, with templates, multiple destinations, and duplicate suppression. |
| [**vsem-azamat/herdr-telegram**](https://github.com/vsem-azamat/herdr-telegram) | 0 | Connects Telegram forum topics to stable Herdr agent sessions for ongoing remote conversations. |
| [**SimonMallas/agent-letter-bridge**](https://github.com/SimonMallas/agent-letter-bridge) | 0 | Lets you message CLI agents from Telegram, Slack, or Discord, filing each message as a durable letter the agent reads. A Herdr adapter rings the agent pane and a popup shows status. |
| [**paper3300/herdr-slackbot**](https://github.com/paper3300/herdr-slackbot) | 0 | Sends Slack DMs when Claude Code or Codex agents in the Herdr app or Herdr TUI finish, with buttons to answer permission prompts. Lets you send prompts to agents from Slack. |
| [**CurrenWong/herdr-dingtalk-omo-bridge**](https://github.com/CurrenWong/herdr-dingtalk-omo-bridge) | 0 | Connects DingTalk to an OmO coding agent in a Herdr pane. Types incoming messages into the session, posts the answer back and tags each message as received, done or error. |
| [**cookiesmonster7926/herdr-telegram**](https://github.com/cookiesmonster7926/herdr-telegram) | 0 | Sends a Telegram message when a Herdr agent waits on you and lets you answer from your phone with buttons. Runs on macOS and Windows. |
| [**jfortez/herdr-agent-alerts**](https://github.com/jfortez/herdr-agent-alerts) | 0 | Sends a Telegram message when a coding agent in Herdr TUI needs attention, with an extract of what the agent is asking and where to go. |
| [**mochikun/herdr-slack-notify**](https://github.com/mochikun/herdr-slack-notify) | 0 | Sends a Slack incoming-webhook message when a Herdr agent finishes or needs input. The README is in Japanese. |
| [**wurthel/herdr-notifications**](https://github.com/wurthel/herdr-notifications) | 0 | Sends a Telegram message when an agent finishes or needs input, including your last prompt and the agent's last response. |
| [**spancerxing/herdr-telegram-bridge**](https://github.com/spancerxing/herdr-telegram-bridge) | 0 | Lets you approve Claude Code, Codex, agy, and Pi agents from Telegram, with a topic per agent, approval buttons, a status dashboard, and completion notices. |
| [**DylanG5/herdr-pi-slack-notify**](https://github.com/DylanG5/herdr-pi-slack-notify) | 0 | Sends a Slack Workflow webhook message when a finished Pi agent stays unseen past a configurable delay. Outbound only. |
| [**OiAnthony/herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify) | 0 | Sends a Telegram message when a Herdr TUI agent is done or blocked. Bot token and chat ID come from the plugin config directory. |

### Desktop, mobile, and webhook notifications

*72 projects. Desktop notifications, mobile push alerts, and webhook triggers for agent events.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**yankewei/herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify) | 34 | Shows a clickable macOS notification when an unseen pane becomes blocked or finishes. Clicking the alert brings the terminal forward and focuses the exact pane through `alerter`. |
| [**TheMetalStorm/herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin) | 14 | Integrates Command Code as a Herdr agent runtime with process detection, idle, working, and blocked status, session recovery after server restarts, and toast alerts when input is needed. |
| [**dot/herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier) | 13 | Bundles a branded macOS notification app so Herdr alerts use the correct icon and can jump to the relevant pane. The app periodically refreshes its Launch Services registration to recover cleanly after reboots or updates. |
| [**horn553/herdr-ntfy**](https://github.com/horn553/herdr-ntfy) | 9 | Sends ntfy alerts for done and blocked agent states using standard command-line tools and curl. |
| [**zom-2018/herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify) | 8 | Sends structured ntfy alerts when an agent blocks or finishes. Notifications include the workspace, tab, and pane, and the plugin prefers a detected local ntfy server before using the network. |
| [**justinchiasson/herdr-nudge**](https://github.com/justinchiasson/herdr-nudge) | 6 | Sends clickable macOS notifications when an agent is blocked or done, or when a long zsh command finishes, and clicking one focuses that pane in Herdr. Works on Intel and Apple Silicon with nothing else to install, and withdraws notifications for panes that move on or close. |
| [**winoooops/herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher) | 6 | Adds live sidebar cards, lifecycle alerts, and a zero-configuration Claude Code metrics bridge for Herdr agents. |
| [**nhclink16/herdr-announcer**](https://github.com/nhclink16/herdr-announcer) | 5 | Speaks a one-sentence AI summary when an agent finishes or needs input. It supports local text-to-speech, ElevenLabs, or any custom command. |
| [**aclima01/herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows) | 4 | Sends native Windows 11 toast notifications when a Herdr agent finishes a turn or asks for input. |
| [**hmu332233/herdr-pets**](https://github.com/hmu332233/herdr-pets) | 4 | Shows macOS desktop pets for Herdr TUI agents that move to your pointer when an agent is blocked. |
| [**ProjectAJ14/herdr-warp**](https://github.com/ProjectAJ14/herdr-warp) | 3 | Sends Warp desktop notifications when a Herdr-managed agent finishes or needs attention. |
| [**tkmct/herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify) | 3 | Adds a Herdr plugin that shows a Windows desktop toast when an agent (Claude Code, etc.) running under WSL2 becomes done (finished) or blocked (waiting for approval/input). |
| [**happyeric77/agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify) | 3 | Posts structured HTTP webhooks when agents block or finish. Payloads can include workspace and pane details, model information, and recent scrollback for use in Slack, Discord, or mobile-alert systems. |
| [**ChrisPachulski/session-sounds**](https://github.com/ChrisPachulski/session-sounds) | 3 | Plays distinct per-session sounds for Herdr TUI agent attention and completion on macOS and Linux. |
| [**zgxme/herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify) | 3 | Forwards Herdr TUI agent notifications to chat services, ntfy or custom HTTP webhooks. |
| [**DevooKim/herdr-glow**](https://github.com/DevooKim/herdr-glow) | 2 | Makes the screen edge glow on macOS when a Herdr agent is blocked, across every space, monitor and fullscreen app without taking focus. The glow returns after 30 seconds of inactivity and stops when you type. |
| [**A1exthegreat/herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify) | 2 | Sends desktop notifications when agents finish, request confirmation, or become idle. |
| [**fulanto/herdr-oncall**](https://github.com/fulanto/herdr-oncall) | 1 | Surfaces blocked agent prompts in a macOS floating panel or Telegram and Feishu messages, allowing replies without returning to the pane. |
| [**tiny-send/tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr) | 1 | Emails a one-line summary when an agent blocks, finishes, or fails. Replying to the message sends input to the correct pane, making an email client a simple remote approval interface. |
| [**HikaruEgashira/say-hook**](https://github.com/HikaruEgashira/say-hook) | 1 | Reads a one-line status summary aloud when an agent becomes done or blocked, using ElevenLabs or macOS speech through a Herdr state-change hook. |
| [**saeedrahimi/herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl) | 1 | Converts Herdr lifecycle events inside WSL into native Windows 11 toast notifications by invoking PowerShell across the WSL boundary. |
| [**zhaoyuheng200/tmux-agent-herd**](https://github.com/zhaoyuheng200/tmux-agent-herd) | 1 | Provides tmux plugin: detect coding-agent status (working/blocked/idle) per pane, notify on blocked, jump between agents. Detection ported from herdr. |
| [**gridness/herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds) | 1 | Plays random local macOS sounds when Herdr TUI agents need input or finish tasks. |
| [**quinnjr/herdr-notifications**](https://github.com/quinnjr/herdr-notifications) | 1 | Sends native desktop notifications when Herdr agent states change on Linux, macOS, Windows, and BSD. |
| [**WebscapeOrg/medley**](https://github.com/WebscapeOrg/medley) | 1 | Lets you pick an audio file per Herdr workspace and status from an imported MP3 or WAV library. Previews sounds and replaces Herdr's native sounds. |
| [**algorist-dev/herdr-crook**](https://github.com/algorist-dev/herdr-crook) | 1 | Connects Herdr to the Crook iPhone and iPad app so you can see your agents and answer them with one tap. English and Japanese docs. |
| [**kaikidd/herdr-bark-notify**](https://github.com/kaikidd/herdr-bark-notify) | 1 | Sends a Bark push notification to your iPhone when a Herdr agent finishes or needs input, naming the agent, workspace, and pane. Needs no daemon or npm dependencies. |
| [**jjuraszek/herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify) | 1 | Pushes an ntfy notification to your phone when a Herdr TUI agent goes blocked or done. Runs from an event hook with no daemon. |
| [**ariel-ps/herdr-alerts**](https://github.com/ariel-ps/herdr-alerts) | 1 | Plays a sound and flashes the affected pane when a Herdr agent finishes or becomes blocked. Includes a Rust CLI and TUI to preview alerts, download sound packs, and pick sounds per project and branch. |
| [**jaltez/agent-notify**](https://github.com/jaltez/agent-notify) | 0 | Monitors local and WSL Herdr sessions in a tray and sends popups, sounds, commands, or webhooks for agent events. |
| [**tdhuan/agent-notify**](https://github.com/tdhuan/agent-notify) | 0 | Sends desktop notifications for Claude Code permission requests and completed turns, with clicks focusing the matching Herdr pane. |
| [**y-hirakaw/herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify) | 0 | Sends macOS notifications for Claude Code panes in Herdr TUI with the agent’s latest message or question. |
| [**diegopzz/herdr-notify**](https://github.com/diegopzz/herdr-notify) | 0 | Sends desktop notifications for Herdr agents on local or remote machines, identifying the host that needs attention. |
| [**huketo/herdr-hitl**](https://github.com/huketo/herdr-hitl) | 0 | Blocks a Herdr coding agent on a human decision, delivered to your phone over Telegram or Discord. |
| [**keinstn/drover-notify**](https://github.com/keinstn/drover-notify) | 0 | Sends a push alert to the Drover iOS app when a Herdr agent becomes blocked. It uses built-in Node.js features only and stores encrypted pairing information locally. |
| [**ram4-dev/herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center) | 0 | Stores notifications from all workspaces in a durable popup inbox. Items can be reviewed, opened in their related pane, cleared when resolved, and retained across restarts. |
| [**jefflau/herdr-webhook**](https://github.com/jefflau/herdr-webhook) | 0 | Posts Herdr TUI agent done and blocked events as JSON to a configurable webhook. |
| [**Rockheung/herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell) | 0 | Displays visual bell indicators in Kaku tabs when Herdr agents await human input. |
| [**ivorpad/herdr-notify**](https://github.com/ivorpad/herdr-notify) | 0 | Notifies users when Herdr TUI agents need attention or finish and queues messages until agents can receive them. |
| [**perlporter/herdr-apple-music-plugin**](https://github.com/perlporter/herdr-apple-music-plugin) | 0 | Shows a toast in herdr when the currently playing track changes in Apple Music (macOS). |
| [**wicolian/dev-on-call**](https://github.com/wicolian/dev-on-call) | 0 | Provides a quiet, local-first macOS menu-bar sentry for developers and their coding agents. |
| [**sandiiarov/tmux-agent-plugin**](https://github.com/sandiiarov/tmux-agent-plugin) | 0 | Provides tmux plugin for a Herdr-like AI agent sidebar. |
| [**1smil1/herdr-done-popup**](https://github.com/1smil1/herdr-done-popup) | 0 | Shows a persistent desktop popup when a Herdr TUI agent finishes or asks a question. |
| [**advaitbd/herdr-notify**](https://github.com/advaitbd/herdr-notify) | 0 | Sends Herdr agent-status notifications through signed Hermes webhooks. |
| [**zerkc/herdr-notify-firebase**](https://github.com/zerkc/herdr-notify-firebase) | 0 | Sends Firebase Cloud Messaging push notifications when Herdr agent status changes. |
| [**donghaolicd/herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify) | 0 | Sends bounded Microsoft Teams notifications for Herdr agent lifecycle events. |
| [**gkzhb/herdr-plugins**](https://github.com/gkzhb/herdr-plugins) | 0 | Sends an ntfy notification when a Herdr agent finishes a turn, with the terminal title, tab, and a summary of the latest Pi reply. The monorepo also holds a standalone Pi ntfy package. |
| [**recordplane/herdr-pendingyou**](https://github.com/recordplane/herdr-pendingyou) | 0 | Shows on each agent's sidebar row what it is waiting on you for and toasts new questions. Answers cards from a popup through the Pending You service. |
| [**KevinEdry/herdr-pion-ping**](https://github.com/KevinEdry/herdr-pion-ping) | 0 | Plays your active Peon Ping sound pack for Herdr agent status events instead of Herdr's built-in sounds. Bundles no audio. |
| [**weskor/nudge**](https://github.com/weskor/nudge) | 0 | Sends a webhook event when agents finish or get blocked and delivers the reply into the agent's pane. Rate-limits, skips the focused pane, and redacts secrets. |
| [**MarcellGranat/herdr-notify**](https://github.com/MarcellGranat/herdr-notify) | 0 | Watches a Herdr TUI pane after one keypress and marks it done in the sidebar when its shell prompt returns. Can also send a Pushover notification. |
| [**AG-Studio-Apps/meshterm-herdr-ios**](https://github.com/AG-Studio-Apps/meshterm-herdr-ios) | 0 | Sends a push alert to the meshTerm iPhone and iPad app when a Herdr agent needs approval or finishes a turn. Only an anonymous ping with the agent name leaves the computer, never screen text. |
| [**zeke1031031/herdr-grokbot-notify**](https://github.com/zeke1031031/herdr-grokbot-notify) | 0 | Wakes a Grok Bot routine by webhook when any coding agent detected by the Herdr TUI finishes or needs you. |
| [**gAmUssA/herdr-notify**](https://github.com/gAmUssA/herdr-notify) | 0 | Shows one macOS banner when an agent finishes or needs input, and a click jumps to that exact pane even from a detached Herdr TUI session. Needs iTerm2. |
| [**suleymanyaryev/herdr-ghostty-badge**](https://github.com/suleymanyaryev/herdr-ghostty-badge) | 0 | Rings the bell for Ghostty's dock badge when a Herdr agent is blocked or done, and shows the waiting count in the window title on macOS. |
| [**joehahndev/herdfxr**](https://github.com/joehahndev/herdfxr) | 0 | Plays alert sounds when an agent finishes or needs input, with different sounds per space, and includes a terminal sfxr designer for making them. Also ships event-probe, which logs event hook payloads for plugin authors. |
| [**pradyb/herdr-notify-router**](https://github.com/pradyb/herdr-notify-router) | 0 | Applies rules to Herdr agent notifications, such as alerting only after an agent stays blocked, and routes alerts to a webhook, ntfy or desktop with quiet hours and deduplication. |
| [**devicki/herdr-away-signal**](https://github.com/devicki/herdr-away-signal) | 0 | Adds an away mode toggled by a key that POSTs to a webhook when an agent finishes or waits for you, so a bot or orchestrator does not have to poll. |
| [**yahyabedirhan/herdr-shipyard**](https://github.com/yahyabedirhan/herdr-shipyard) | 0 | Installs the shipyard command on Linux machines and pings the shipyard macOS menu bar app when an agent there is blocked. |
| [**devicki/herdr-pager**](https://github.com/devicki/herdr-pager) | 0 | Sends ntfy push notifications when an agent finishes or needs an answer, and when a command, script, or scheduled job ends. Each message names the pane to jump back to. |
| [**znohat/herdr-ttyd-ably**](https://github.com/znohat/herdr-ttyd-ably) | 0 | Publishes Herdr TUI agent status changes to an Ably channel so a custom ttyd build can show desktop notifications in the browser. |
| [**retry19/herdr-agent-last-message-notify**](https://github.com/retry19/herdr-agent-last-message-notify) | 0 | Adds the agent's last message to the desktop notification when an agent finishes or waits for input in Herdr TUI. |
| [**varvand/herdr-plugin-mac-notify**](https://github.com/varvand/herdr-plugin-mac-notify) | 0 | Shows macOS Notification Center banners when a Herdr TUI agent finishes or needs input, and stays quiet when that pane is focused. |
| [**RaulAlvaro/herdr-space-sounds**](https://github.com/RaulAlvaro/herdr-space-sounds) | 0 | Plays a distinct macOS sound pair per Herdr TUI space, with sounds for blocked agents and finished background spaces, so you can tell which project needs attention. |
| [**Argon-Sky/herdr-afk-notify**](https://github.com/Argon-Sky/herdr-afk-notify) | 0 | Sends an ntfy push notification when a Herdr TUI agent finishes a long turn or needs input, only while you are away from the keyboard. |
| [**rubenbelem/warp-herdr-notifications**](https://github.com/rubenbelem/warp-herdr-notifications) | 0 | Sends clickable macOS notifications for Herdr agents running in Warp, and a click focuses the exact Warp tab and agent pane. |
| [**zetlen/herdr-bleatr**](https://github.com/zetlen/herdr-bleatr) | 0 | Speaks a one-sentence notification aloud when an agent in another Herdr TUI tab finishes or needs approval. Uses macOS say or espeak, with an optional Claude or Codex summary. |
| [**8liang/herdr-ai-notify**](https://github.com/8liang/herdr-ai-notify) | 0 | Forwards Herdr TUI agent done and blocked events to ai-cli-complete-notify so alerts go out over its webhook and other channels. |
| [**8liang/herdr-gotify**](https://github.com/8liang/herdr-gotify) | 0 | Pushes a Gotify notification to your phone when a Herdr TUI agent becomes blocked or done, optionally with an LLM-written one-sentence summary of the pane output. |
| [**liamwh/herdr-rich-notifications**](https://github.com/liamwh/herdr-rich-notifications) | 0 | Sends native desktop notifications for Herdr TUI agent status changes with context built from local metadata and a prompt excerpt. One click focuses the exact pane, with no LLM calls. |
| [**znohat/ttyd**](https://github.com/znohat/ttyd) | 0 | Builds a ttyd fork with an --ably-notify option that shows Herdr agent done, idle and blocked events as browser notifications. Pairs with the herdr-ttyd-ably plugin that publishes the events to an Ably channel. |
| [**WorksOnMyVM/herdr-sounds**](https://github.com/WorksOnMyVM/herdr-sounds) | 0 | Discovers, previews, installs, and switches Herdr notification sound packs. |

### Telemetry, events, and quota streaming

*32 projects. Event collectors and monitors for agent state, usage, cost, and runtime activity.*

| Project | Stars | What it does |
|---|--:|---|
| [**DIodide/herdr-telemetry**](https://github.com/DIodide/herdr-telemetry) | 12 | Sends workspace and agent telemetry to an endpoint chosen by the user. It removes tokens, redacts sensitive prompts, and ships as a single binary. |
| [**Ziy1-Tan/herdr-codebuddy**](https://github.com/Ziy1-Tan/herdr-codebuddy) | 7 | Reports CodeBuddy session, working and permission states to Herdr TUI through hooks. |
| [**Gilamonster-Foundation/newt-agent · newt-tui/src/herdr**](https://github.com/Gilamonster-Foundation/newt-agent/tree/main/newt-tui/src/herdr) | 6 | Reports Newt coding-agent lifecycle states to the Herdr TUI from a pane using its socket API. |
| [**leonardoacosta/herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode) | 5 | Reports Jcode working and idle lifecycle states and session identity to Herdr TUI. |
| [**dsh-blue/herdr-agent-state**](https://github.com/dsh-blue/herdr-agent-state) | 2 | Reports DeepSeek Harness lifecycle state, session references, and model metadata to the current Herdr pane. |
| [**CodyBontecou/herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge) | 2 | Streams structured Herdr activity as NDJSON, including pane focus time, detected agent and model details, and local session summaries. Output can go to a file, webhook, or command, and transcript text is hidden by default. |
| [**vishnutskumar/herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics) | 2 | Analyzes memex session history and shows efficiency guidance for Herdr TUI agents. |
| [**cpcloud/herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview) | 2 | Combines active AgentsView sessions across projects, models, and agents, with real-time timelines and metrics inside Herdr. |
| [**akshat12/herdr-muse**](https://github.com/akshat12/herdr-muse) | 2 | Reports Muse Code working, idle, and blocked states to Herdr TUI through lifecycle hooks. |
| [**Comamoca/command-code-herdr**](https://github.com/Comamoca/command-code-herdr) | 2 | Reports Command Code working, idle, and blocked lifecycle states to Herdr TUI through its local socket. |
| [**naturalmoods/herdr-burnlog**](https://github.com/naturalmoods/herdr-burnlog) | 2 | Records token usage and recorded cost per project for Herdr-managed Codex, Claude Code and Pi agents in a local SQLite database, with CLI reports and popup panes. |
| [**jakobbeyer/herdr-kharka**](https://github.com/jakobbeyer/herdr-kharka) | 2 | Writes what a machine's Herdr runs into kharka on every change by following Herdr's event stream. Lets any tool read agents from all machines through a local replica. |
| [**TheRealHaoLiu/dsh-herdr**](https://github.com/TheRealHaoLiu/dsh-herdr) | 1 | Reports a DeepSeek Harness root agent’s identity and lifecycle state to its Herdr pane. |
| [**mcc0x/herdr-standup**](https://github.com/mcc0x/herdr-standup) | 1 | Generates summaries of agent activity across Herdr workspaces over time, including commits, diff volume, and branches. |
| [**neospeed83/herdr-replay**](https://github.com/neospeed83/herdr-replay) | 1 | Records and replay multi-agent Herdr coding sessions as interactive timelines. |
| [**nabutabu/herdr-observr**](https://github.com/nabutabu/herdr-observr) | 1 | Exports Herdr TUI agent runtime health, wait times, concurrency, usage, and costs through OpenTelemetry. |
| [**xdagiz/opencode2-herdr**](https://github.com/xdagiz/opencode2-herdr) | 1 | Reports OpenCode 2 agent states and session identity to Herdr TUI through its socket. |
| [**HunterStarets/herdr-gitbash-agent-detector**](https://github.com/HunterStarets/herdr-gitbash-agent-detector) | 1 | Detects OpenCode sessions running inside Git Bash panes on Windows and reports their state (idle / working). |
| [**Dolliwyx/herdr-rpc**](https://github.com/Dolliwyx/herdr-rpc) | 1 | Publishes the focused Herdr workspace and agent counts to Discord Rich Presence from a Windows WSL2 setup. |
| [**Lbryany/dsh-plugins · packages/dsh-herdr**](https://github.com/Lbryany/dsh-plugins/tree/main/packages/dsh-herdr) | 0 | Aggregates DeepSeek Harness root and child agent states and reports the resulting lifecycle state to the Herdr pane. |
| [**peria-ai/precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin) | 0 | Shows PRECC token-savings telemetry in Herdr panes and runs PRECC setup and diagnostics. |
| [**hoon-ch/herdr-gjc-plugin**](https://github.com/hoon-ch/herdr-gjc-plugin) | 0 | Reports agent launch, exit, idle, working, and blocked states to Herdr. |
| [**5qln/5qln-herdr-plugin**](https://github.com/5qln/5qln-herdr-plugin) | 0 | Provides the 4+1 cell as a Herdr instrument, sealed podium for human questions, and four agent desks. |
| [**simensollie/aw-watcher-herdr**](https://github.com/simensollie/aw-watcher-herdr) | 0 | Records focused Herdr workspaces and concurrent agent activity in ActivityWatch on macOS, for both the Herdr app and Herdr TUI. |
| [**AgentTeamsRun/herdr**](https://github.com/AgentTeamsRun/herdr) | 0 | Reports Herdr TUI worktree creation and removal to the AgentTeams registry. |
| [**Howryann/herdr-monitor**](https://github.com/Howryann/herdr-monitor) | 0 | Exposes read-only Herdr agent status over HTTP with no runtime dependencies. |
| [**capt-marbles/herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration) | 0 | Reports Jcode session and lifecycle state to Herdr. |
| [**TheMetalStorm/herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin) | 0 | Makes a plain Cline CLI process appear as a native Herdr agent with lifecycle reporting. |
| [**perorin0418/jcode-herdr-integration**](https://github.com/perorin0418/jcode-herdr-integration) | 0 | Reports jcode agent lifecycle states to the Herdr sidebar using hooks. |
| [**Nofuture123/herdr-opencode2-integration**](https://github.com/Nofuture123/herdr-opencode2-integration) | 0 | Reports OpenCode 1.x and 2.0 session states to Herdr TUI with per-pane process isolation. |
| [**meuble/Herdr-mistral-vibe**](https://github.com/meuble/Herdr-mistral-vibe) | 0 | Reports Mistral Vibe working, idle, and blocked states to Herdr TUI through Vibe hooks. |
| [**jaredlyon/herdr-respan-adapter**](https://github.com/jaredlyon/herdr-respan-adapter) | 0 | Traces CLI coding agents running in Herdr TUI to Respan through one Rust binary with redaction, spooling, and OTLP export. |

### Voice, hardware, and remote bridges

*57 projects. Interfaces that connect Herdr to spoken input, physical devices, or remote control surfaces.*

| Project | Stars | What it does |
|---|--:|---|
| [**klarluft/pitupitu**](https://github.com/klarluft/pitupitu) | 223 | Connects phone and browser voice conversations to coding agents running in Herdr TUI. |
| [**T0mSIlver/localvoxtral**](https://github.com/T0mSIlver/localvoxtral) | 64 | Fully local, real-time dictation for Apple Silicon Macs. It streams speech into the coding-agent session under the cursor, including Claude Code inside a Herdr pane, and uses that session as context for optional text polishing. |
| [**schacon/micro-manager**](https://github.com/schacon/micro-manager) | 41 | Uses the Creator Micro 2 hardware controller to operate Herdr. |
| [**brogrammerMW/herdr-voice**](https://github.com/brogrammerMW/herdr-voice) | 32 | Lets users speak to agents in Herdr TUI panes and hear replies using local OpenLive or realtime xAI, OpenAI, and Google models. |
| [**kccarlos/herdr-sheepdog**](https://github.com/kccarlos/herdr-sheepdog) | 15 | Monitors and steers Herdr agents by voice from an iPhone app or a Herdr app layout and panel. |
| [**second-state/vibetty**](https://github.com/second-state/vibetty) | 11 | Streams live Herdr terminal screens over MQTT to devices such as VibeKeys and VibeWatch and relays keystrokes back. It includes an MQTT broker and integrates with Herdr's command palette and status bar. |
| [**pawaca/even-better**](https://github.com/pawaca/even-better) | 6 | Mirrors Claude Code and Codex sessions in Herdr TUI to Even Realities G2 glasses and sends prompts back to the pane. |
| [**htlin222/herdr-gamepad**](https://github.com/htlin222/herdr-gamepad) | 6 | Maps Xbox, PlayStation, and 8BitDo controller buttons to Herdr actions through macOS GameController, enabling workspace and pane control away from the keyboard. |
| [**miko-misa/herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd) | 5 | Forwards remote agent development-server ports to the local machine and opens them after confirmation. |
| [**aneym/herdr-voice**](https://github.com/aneym/herdr-voice) | 5 | Controls workspaces, pane splits, and agent dispatch with spoken commands through OpenAI's Realtime API. A floating display shows the transcription and asks for confirmation before sending instructions. |
| [**hackerchai/herdr-relay**](https://github.com/hackerchai/herdr-relay) | 5 | Shares Herdr TUI sessions with another computer using encrypted pairing over a LAN, tailnet, or relay. |
| [**Vercantez/herdr-voice**](https://github.com/Vercantez/herdr-voice) | 4 | Connects an installable iPhone web app to Herdr through a private voice gateway using OpenAI Realtime over WebRTC. |
| [**superfly/herdr-sprites-plugin**](https://github.com/superfly/herdr-sprites-plugin) | 4 | Runs Claude Code, Codex, OpenCode or a custom agent in persistent Fly.io Sprites controlled from Herdr TUI panes. |
| [**kvm404/Auren · src/auren/hands/herdr.py**](https://github.com/kvm404/Auren/blob/main/src/auren/hands/herdr.py) | 4 | Starts Herdr coding agents through the Auren voice assistant on Omarchy. |
| [**errantpacket/RhubarbTart · tools/rhubarb/herdr.py**](https://github.com/errantpacket/RhubarbTart/blob/main/tools/rhubarb/herdr.py) | 3 | Starts scoped security-research agents in Herdr TUI against assigned Tart VM clones with command approval controls. |
| [**jonesy827/mate**](https://github.com/jonesy827/mate) | 2 | Controls a Herdr fleet by phone call to start agents, send tasks, check status, and hear Claude Code or Codex replies. |
| [**freewillythe4th/action-button-agent**](https://github.com/freewillythe4th/action-button-agent) | 2 | Connects an iPhone Action Button to personal Herdr agents. Voice input passes through an iOS Shortcut, Tailscale, Telegram, and a Claude Agent SDK operator, which starts or targets a Herdr session and returns the response. |
| [**RanolP/herdr-handsfree**](https://github.com/RanolP/herdr-handsfree) | 2 | Adds on-device voice dictation and webcam gaze-based cursor movement to Herdr TUI on Apple Silicon Macs. |
| [**romiluz13/instinct-herdr-tunnel**](https://github.com/romiluz13/instinct-herdr-tunnel) | 2 | Exposes your Herdr agents to a phone or AI assistant through a loopback portal with 26 allowed actions, a bearer token and an audit log. Callers can read an agent's chat, send prompts, and scroll or click inside panes. |
| [**rchougule/herdr-cam**](https://github.com/rchougule/herdr-cam) | 2 | Opens your webcam from Herdr with one key so you can photograph paper sketches or notes and send the photos into your coding agent's prompt as images. macOS only, with a Swift camera app. |
| [**Luisalt20/herdr-reach**](https://github.com/Luisalt20/herdr-reach) | 2 | Runs a read-only doctor that measures what your network allows to a remote machine and recommends an SSH transport for Herdr with evidence. Only the doctor command is shipped so far. |
| [**randomradio/herdr-ports**](https://github.com/randomradio/herdr-ports) | 2 | Forwards a port from a remote Herdr workspace to `http://herdr.{workspace}.localhost:{port}` on your laptop through SSH tunnels, using saved Herdr machines. |
| [**xtwist/herdr-stt**](https://github.com/xtwist/herdr-stt) | 2 | Dictates into the pane where recording started, using a local PipeWire recorder and a faster-whisper worker, with an optional repo-aware text corrector. Linux only. |
| [**Aktrov/herdr-tts**](https://github.com/Aktrov/herdr-tts) | 2 | Speaks selected terminal text aloud using Piper neural text-to-speech engines with keyboard controls. |
| [**radres/herdr-plugin-call-me**](https://github.com/radres/herdr-plugin-call-me) | 1 | Calls your phone when a Herdr agent is blocked, reads the question aloud, and sends your spoken answer as a keypress. |
| [**kazuochi/opxy-deck**](https://github.com/kazuochi/opxy-deck) | 1 | Maps a Teenage Engineering OP-XY to Claude Code and Codex controls, dictation, and Herdr TUI agent routing. |
| [**giacolees/herdr-openlogi**](https://github.com/giacolees/herdr-openlogi) | 1 | Maps Logitech mouse buttons to Herdr navigation commands using OpenLogi overlays. |
| [**PlaneshiftDev/microd**](https://github.com/PlaneshiftDev/microd) | 1 | Handles macropad button events, gestures, and RGB controls with an optional Herdr bridge. |
| [**razajamil/herdr-hex-browser-voice-command**](https://github.com/razajamil/herdr-hex-browser-voice-command) | 1 | A Chrome extension and local service that sends Hex voice transcripts to the correct Herdr pane based on the browser URL that was focused while speaking. URL patterns are mapped to workspace, tab, and pane targets. |
| [**aliaksandr-haurylau-godel/herdr-voice**](https://github.com/aliaksandr-haurylau-godel/herdr-voice) | 1 | Transcribes held-key voice dictation into the focused Herdr TUI agent input, with context-aware rewriting and selectable speech engines. |
| [**hashrock/herdr-apc-mini**](https://github.com/hashrock/herdr-apc-mini) | 1 | Maps AKAI APC mini mk2 hardware controllers to physical Herdr agent controls. |
| [**shadowfax92/herdr-talon**](https://github.com/shadowfax92/herdr-talon) | 1 | Adds spoken Talon labels to visible Herdr targets for hands-free movement between panes. |
| [**abhishekrana/herdr-dictate**](https://github.com/abhishekrana/herdr-dictate) | 1 | Types local speech-to-text dictation into the focused Herdr pane while you talk. Transcription runs on the machine and audio is not sent out. |
| [**portablcorp/herdr-cosyra**](https://github.com/portablcorp/herdr-cosyra) | 1 | Opens your Cosyra cloud workspace in Herdr TUI with one tab per Cosyra terminal attached over SSH. Needs the Cosyra CLI signed in. |
| [**ricardofelixb/herdr-codex-voice**](https://github.com/ricardofelixb/herdr-codex-voice) | 1 | Lets Codex native /voice in a Herdr remote pane use the microphone and speakers of the computer you sit at, over SSH and Tailscale. Experimental preview. |
| [**jeffhuen/tether-browser**](https://github.com/jeffhuen/tether-browser) | 1 | Bridges a remote agent to the Chrome on your workstation so ctrl+click on a URL in a Herdr pane opens it in your local browser. Also works across tmux and SSH sessions. |
| [**bhoov/herdr-port-forwarder**](https://github.com/bhoov/herdr-port-forwarder) | 1 | Forwards loopback ports printed by panes on saved SSH machines to your local computer and shows the forwarded ports in the Herdr TUI sidebar. |
| [**sroberts/tally**](https://github.com/sroberts/tally) | 1 | Shows which Herdr agents need you on a phone web page or a hardware pad, and lets you approve, interrupt, or dictate. Reaches the phone over Tailscale. |
| [**shanev/herdr-voice**](https://github.com/shanev/herdr-voice) | 1 | Lets you start, ask about, and stop Herdr agents by voice through Hermes or the Vux agent. Ships skills for the Herdr TUI and herdr-core plus a desk-alerts plugin. |
| [**gabrielmarcano/agent-watch**](https://github.com/gabrielmarcano/agent-watch) | 1 | Sends coding-agent permission prompts and questions from Herdr to a Wear OS watch, phone, or macOS menu bar, where you can allow, deny, or reply. Uses a Go host bridge and a self-hosted relay with no open ports. |
| [**ohitslaurence/outridr-server**](https://github.com/ohitslaurence/outridr-server) | 0 | Connects the outridr mobile app to Herdr over Tailscale for agent status, transcripts, remote input, and push alerts. |
| [**vgreg/herdr-padio**](https://github.com/vgreg/herdr-padio) | 0 | Switches PadIO controller modes automatically based on the app running in herdr's focused pane. |
| [**Drozerah/herdr-voice**](https://github.com/Drozerah/herdr-voice) | 0 | Adds early-stage text-to-speech audio feedback for agents working in Herdr TUI panes. |
| [**wtcrowe4/DialDeck**](https://github.com/wtcrowe4/DialDeck) | 0 | Uses a Microsoft Surface Dial and an AutoHotkey v2 engine as a keyless control surface for Herdr orchestration, development commands, and modelling macros. |
| [**nickboy/herddeck**](https://github.com/nickboy/herddeck) | 0 | Controls local and remote Herdr TUI agent sessions with Stream Deck keys. |
| [**eoinest/convo-history**](https://github.com/eoinest/convo-history) | 0 | Turns a recent window of speech into a Codex prompt in a fresh Herdr TUI worktree, triggered by a hotkey or wake word. |
| [**trentwadams/cc-controller**](https://github.com/trentwadams/cc-controller) | 0 | Maps SDL game controllers to Herdr socket commands for navigation, scrolling, and voice mode. The controller may be local or connected from another machine over SSH. |
| [**calebcauthon/herdr-riff-relay**](https://github.com/calebcauthon/herdr-riff-relay) | 0 | Sends Riff dictation to a chosen Herdr TUI agent pane using hotkeys. |
| [**TolemyW/bash-screen**](https://github.com/TolemyW/bash-screen) | 0 | Lets an agent operate GUI apps on a remote Linux host over SSH, with a live preview pane in Herdr. Reads the accessibility tree and falls back to screenshots. |
| [**jjeff/herdr-speak**](https://github.com/jjeff/herdr-speak) | 0 | Speaks a one-line recap when a coding agent finishes a turn, including agents on saved SSH machines. Pairs a speak skill with a background speaker on macOS, Linux, or Windows. |
| [**ShortArrow/herdr-triton**](https://github.com/ShortArrow/herdr-triton) | 0 | Connects a Waveshare RP2040 three-key board to Herdr so keys jump to the waiting agent, select an option and approve it. LEDs follow agent state. |
| [**PatrickPriestley/herdr-gamepad**](https://github.com/PatrickPriestley/herdr-gamepad) | 0 | Controls Herdr from a game controller to move between panes, tabs and spaces, answer agents and dictate prompts with local whisper.cpp. Tested on macOS with a DualSense. |
| [**kujjwal02/bifrost**](https://github.com/kujjwal02/bifrost) | 0 | Opens dev servers, links and files from agents on remote machines in the local browser, using the SSH details Herdr already has. Needs no server, account or VPN. |
| [**SebCos94/herdr-dictate**](https://github.com/SebCos94/herdr-dictate) | 0 | Records speech into any Herdr TUI pane with a live transcript from local whisper.cpp, then types the text on Enter. Runs on Linux, macOS, and Windows and sends no audio off the machine. |
| [**amodi20/herdr-voice-router**](https://github.com/amodi20/herdr-voice-router) | 0 | Routes a prompt to another Herdr TUI pane when you say that pane's name, working with typed text or any dictation tool. Ships a Claude Code hook alongside the Herdr plugin. |
| [**panayiotis-constantinou/herdr-plugin-qmk**](https://github.com/panayiotis-constantinou/herdr-plugin-qmk) | 0 | Mirrors Herdr TUI agent state on a QMK keyboard over USB MIDI and turns a keyboard layer into session controls. |
| [**sroberts/vibe-macropad**](https://github.com/sroberts/vibe-macropad) | 0 | Turns an Adafruit MacroPad RP2040 into a keypad whose FLEET layer sends Herdr prefix-key shortcuts to jump between agents, open new tabs, resume and zoom. Includes firmware and a layout studio, and lights the keys with each agent's state through sroberts/tally. |

### Protocol and third-party bridges

*78 projects. Adapters between Herdr and other multiplexers, platforms, messaging systems, or automation protocols.*

| Project | Stars | What it does |
|---|--:|---|
| [**openclaw/crabbox**](https://github.com/openclaw/crabbox) | 1,527 | Adds Crabbox sandbox provisioning and remote test execution to Herdr. Plugin actions can prewarm temporary environments, synchronize diffs, and inspect active leases from an overlay. |
| [**27medkamal/tmux-agent-wizard**](https://github.com/27medkamal/tmux-agent-wizard) | 21 | Brings Herdr agent detection and compatible CLI-driven plugins to tmux. |
| [**RaviTharuma/cmux-herdr**](https://github.com/RaviTharuma/cmux-herdr) | 16 | Shows Herdr TUI pane viewers and agent status pills inside cmux using external attachment. |
| [**benkraus/herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay) | 11 | Bridges Herdr TUI socket operations to HTTP and WebSocket clients, including a browser interface and optional Tailscale publishing. |
| [**neon-solutions/neon-herdr**](https://github.com/neon-solutions/neon-herdr) | 11 | Embeds a serverless Postgres dashboard in a Herdr pane. It can create database branches per agent worktree, start or stop compute, and insert connection strings. |
| [**lachieh/herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux) | 11 | Mirrors Herdr TUI agents into the cmux sidebar with status, task text, and click-to-focus navigation. |
| [**HexSleeves/herdr-warp**](https://github.com/HexSleeves/herdr-warp) | 9 | Opens live Herdr TUI agents as native Warp panes on macOS. |
| [**agentwireprotocol/awp · plugin/herdr**](https://github.com/agentwireprotocol/awp/tree/main/plugin/herdr) | 8 | Connects Herdr TUI agents to Agent Wire Protocol messaging with inbox panes, notifications and idle-agent delivery. |
| [**wenxichang/herdr-pal**](https://github.com/wenxichang/herdr-pal) | 7 | Connects Herdr TUI agents across machines to a WeCom bot for session selection, task submission, terminal output, and limited key input. |
| [**Poor-Plebs/herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes) | 7 | Opens SSH terminals for hosts from SSH configuration in separate Herdr TUI workspaces. |
| [**detailles/AgentRadio**](https://github.com/detailles/AgentRadio) | 7 | Sends direct messages between agents in Herdr panes through a local SQLite-backed relay. |
| [**go-min/herdr-fwd**](https://github.com/go-min/herdr-fwd) | 6 | Automatically maintains loopback port forwarding between a remote Herdr session and the local machine, making services started by remote agents available without manual SSH tunnels. |
| [**HowAreAllWell/gpt-agent-bridge**](https://github.com/HowAreAllWell/gpt-agent-bridge) | 6 | Connects ChatGPT Web to local agents in Herdr TUI to dispatch tasks and review returned results. |
| [**elonnzhang/Herdrex**](https://github.com/elonnzhang/Herdrex) | 6 | Connects Herdr TUI workspaces and terminal panes to Rex desktop and CLI clients, locally or over SSH. |
| [**sunny0826/dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr) | 4 | Lets DeepSeek Harness sessions inspect and control Herdr through socket-backed tools and a session-scoped panel. |
| [**wavrin/herdr-ferry**](https://github.com/wavrin/herdr-ferry) | 4 | Moves files and clipboard between the Herdr box and your laptop over SSH, no cloud bucket. |
| [**gabriel-laet/herdr-cursor**](https://github.com/gabriel-laet/herdr-cursor) | 3 | Lists, streams, and resumes Cursor cloud agents from Herdr TUI panes, with agent state reported to the sidebar. |
| [**ardasevinc/herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge) | 3 | Provides a native Herdr pane identity for Codex sessions using a centralized app-server. |
| [**vibegui/vibebook.dev · herdr-plugin**](https://github.com/vibegui/vibebook.dev/tree/main/herdr-plugin) | 3 | Connects Vibebook rooms to Herdr TUI and opens a Claude Code session for each room. |
| [**alepar/herdr-threads**](https://github.com/alepar/herdr-threads) | 3 | Sends durable messages between Claude Code, Codex, Antigravity and Hermes agents across Herdr TUI sessions and machines. |
| [**fab-agent/community**](https://github.com/fab-agent/community) | 3 | Adds teammate presence, departments and direct messages to a Herdr TUI community workspace. |
| [**anaypurohit0907/herdr-opencode-bridge**](https://github.com/anaypurohit0907/herdr-opencode-bridge) | 3 | Corrects Herdr TUI OpenCode pane status by aggregating root sessions and avoiding false idle states. |
| [**pisanvs/mc-cc**](https://github.com/pisanvs/mc-cc) | 2 | Shows Herdr agent status and Claude Code transcripts inside Minecraft and lets players reply from the game. |
| [**VicenteOlmos/opencode-herdr**](https://github.com/VicenteOlmos/opencode-herdr) | 2 | Routes OpenCode V2 beta requests through Herdr TUI adapters for supported agent CLIs. |
| [**getkimchi/herdr-kimchi**](https://github.com/getkimchi/herdr-kimchi) | 2 | Reports Kimchi agent state and session references to Herdr TUI for sidebar status and session restoration. |
| [**candypoets/buzzr**](https://github.com/candypoets/buzzr) | 2 | Mirrors Herdr workspaces and panes into Buzz channels using Nostr identities. It publishes agent availability and routes channel mentions to the correct terminal pane without exposing the user's private key. |
| [**szrenwei/herdr-traex**](https://github.com/szrenwei/herdr-traex) | 2 | Integrates TraeX agent lifecycle states and available model metadata into the Herdr TUI sidebar. |
| [**frankjoshua/herdr-acp**](https://github.com/frankjoshua/herdr-acp) | 2 | Exposes a Herdr pane as an Agent Client Protocol (ACP) agent, so any ACP client can prompt Claude Code, Codex, Pi, or a plain shell running in that pane. Streams the pane back to the client as one shared session, including text typed directly at the pane, and reads agent transcripts on Linux without hooks. |
| [**dsh-plugin-collection/dsh-herdr-site**](https://github.com/dsh-plugin-collection/dsh-herdr-site) | 2 | Reports dsh/cc-tui agent state (working/idle/blocked) to Herdr over the custom-integration protocol. |
| [**lanwen/herdr-sbx**](https://github.com/lanwen/herdr-sbx) | 2 | Registers running Docker Sandboxes as Herdr machines over SSH so Herdr tracks the agents inside them. Can install Herdr in a sandbox, create project workspaces there and sync selected local plugins. |
| [**webframp/shelley-herdr**](https://github.com/webframp/shelley-herdr) | 2 | Runs Shelley conversations on exe.dev VMs as native Herdr agents, each in a pane with live state, a title from the conversation slug and a resume command. Drives shelley client over SSH and reports state through herdr pane report-agent. |
| [**inoribea/herdr-goose-bridge**](https://github.com/inoribea/herdr-goose-bridge) | 2 | Detects goose panes and reports idle, working and blocked state to Herdr, which cannot detect goose on its own, notably on Windows. |
| [**DO-Solutions/herdr-mars-plugin**](https://github.com/DO-Solutions/herdr-mars-plugin) | 1 | Starts, attaches to, and manages DigitalOcean Managed Agents sessions from Herdr panes using `doctl`. |
| [**rrojo02/herdr-bridge**](https://github.com/rrojo02/herdr-bridge) | 1 | Connects external coding agents to Herdr through its local socket API. |
| [**Liquescent-Development/herdr-a2a**](https://github.com/Liquescent-Development/herdr-a2a) | 1 | Connects Pi agents in a Herdr TUI workspace through an A2A broker for peer messages, replies, and team coordination. |
| [**haoliangwu/dsh-herdr**](https://github.com/haoliangwu/dsh-herdr) | 1 | Reports dsh session states to the Herdr agent panel through the pane-socket protocol. |
| [**vaclavik-xyz/herdwatch**](https://github.com/vaclavik-xyz/herdwatch) | 1 | Keeps a pane marked as working while CI, review, or another background condition is still pending after the agent itself becomes idle. It can run once or as a background service. |
| [**sgnilreutr/herdr-vibe-integration**](https://github.com/sgnilreutr/herdr-vibe-integration) | 1 | Reports Mistral Vibe agent states to the Herdr TUI sidebar through Vibe hooks and the socket or CLI. |
| [**ShinoharaHaruna/mimo-code-herdr**](https://github.com/ShinoharaHaruna/mimo-code-herdr) | 1 | Integrates MiMo Code agent state and session controls into Herdr TUI, with cleanup on exit and optional OpenCode identity. |
| [**XicuM/herdr-bridge**](https://github.com/XicuM/herdr-bridge) | 1 | Runs a daemon that connects to the Herdr socket and remote machines over SSH. Serves agent state, terminals, and Obsidian vaults to other devices over authenticated HTTP and WebSockets. |
| [**joeharris76/jcode-herdr**](https://github.com/joeharris76/jcode-herdr) | 1 | Registers jcode sessions in Herdr's agents sidebar with live working, idle, and blocked status and the session id for resume. Installs as a jcode hook script. |
| [**FUSU123fusu/dsh-tui-herdr**](https://github.com/FUSU123fusu/dsh-tui-herdr) | 1 | Reports dsh-TUI working, blocked, and done states to the Herdr sidebar through the pane report-agent API. README is in Chinese. |
| [**guiand888/herdr-vibe**](https://github.com/guiand888/herdr-vibe) | 1 | Reports Mistral Vibe agent state to Herdr from Vibe hooks, giving Vibe sessions a sidebar entry, finish and decision notifications, and `herdr agent wait` support. Saves the resume command so a Vibe session comes back in the same pane after a Herdr restart. |
| [**slashv/st2-herdr**](https://github.com/slashv/st2-herdr) | 0 | Connects ST2 agent fleets to Herdr workspaces with live attachments, a hierarchy view, and operator-approved agent creation. |
| [**wenhao4126/dsh-herdr**](https://github.com/wenhao4126/dsh-herdr) | 0 | Exposes Herdr workspaces, panes, and coding agents as DeepSeek Harness tools. |
| [**tomoya55/cmux-herdr**](https://github.com/tomoya55/cmux-herdr) | 0 | Propagates agent status (working / waiting for input / finished) to the cmux sidebar. |
| [**scaccogatto/vite-plugin-herdr**](https://github.com/scaccogatto/vite-plugin-herdr) | 0 | Sends a selected browser element and prompt from a Vite app to a Herdr coding agent. |
| [**stfl/herdr-bridge**](https://github.com/stfl/herdr-bridge) | 0 | Shows a remote herdr agent inside a local herdr pane, one sidebar, several machines. |
| [**fabzter/hermes-bridge**](https://github.com/fabzter/hermes-bridge) | 0 | Lets Claude Code send messages and commands to a local Hermes Agent through Herdr and respond to its approval prompts. |
| [**Fectivnfy112357/claude-code-bridge**](https://github.com/Fectivnfy112357/claude-code-bridge) | 0 | Bridges Hermes Agent and Claude Code CLI in print mode and interactive Herdr sessions. |
| [**ardubev16/tmux-herdr**](https://github.com/ardubev16/tmux-herdr) | 0 | Adds a Tmux plugin that uses Herdr to manage, aggregate and orchestrate AI Agents. |
| [**Mumega-com/herdr-mupot-bridge**](https://github.com/Mumega-com/herdr-mupot-bridge) | 0 | Bridges Mupot and Herdr with flight monitoring, presence reports, and inbox delivery to agent panes. |
| [**LuYanFCP/herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin) | 0 | Controls Herdr TUI agents through WeChat, including status updates, prompts and permission responses. |
| [**AlexandreAkao/herdr-bridge-compozy**](https://github.com/AlexandreAkao/herdr-bridge-compozy) | 0 | Displays headless CompozyOS agents as Herdr TUI agent rows by forwarding hook events to the socket API. |
| [**sbulav/herdr-relay**](https://github.com/sbulav/herdr-relay) | 0 | Relays Herdr TUI agent state to phone, web, and Telegram clients, letting users approve prompts and send terminal input. |
| [**thesimonharms/herdr-cmd-agent-plugin**](https://git.simonharms.com/thesimonharms/herdr-cmd-agent-plugin) | — | Adds CommandCode agent detection to Herdr TUI, including idle, working, and blocked state in the sidebar. |
| [**junliu-mde/mimo-code-herdr-plugin**](https://github.com/junliu-mde/mimo-code-herdr-plugin) | 0 | Combines all subagent states into a stable idle, working, blocked, or done status for Herdr. A watchdog releases stale labels after crashes, and nested MiMo tool calls are ignored. |
| [**stefanahman/mux**](https://github.com/stefanahman/mux) | 0 | Lets Go programs manage workspaces, panes, and agent state through a common interface for tmux, Herdr TUI, and cmux. |
| [**OSHEThai/HerdrOps**](https://github.com/OSHEThai/HerdrOps) | 0 | Monitors desktop operations for Herdr terminal agents on Windows. |
| [**linvald/herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer) | 0 | Syncs cmux's file viewer to the currently focused herdr space. |
| [**Gol-D-Rogger/herdr-code-server-clipboard**](https://github.com/Gol-D-Rogger/herdr-code-server-clipboard) | 0 | Forwards Herdr selections to the code-server browser clipboard on macOS. |
| [**tumf/conflux-herdr**](https://github.com/tumf/conflux-herdr) | 0 | Runs the Conflux TUI in a Herdr TUI pane and reports idle, working, and blocked states to the Agents list. |
| [**opencharly/pod-herdr**](https://github.com/opencharly/pod-herdr) | 0 | Provides the herdr stack box (herdr.dev terminal multiplexer) + the check-herdr-pod R10 bed; herdr candy = pinned binary, supervised server, TCP socket bridge for the herdr: verb / charly herdr CLI. |
| [**edmundmiller/herdr-plugin-dotfiles-github-link-preview**](https://github.com/edmundmiller/herdr-plugin-dotfiles-github-link-preview) | 0 | Detects GitHub issue and pull-request links in the active pane and opens their details in a neighboring split through the GitHub CLI. |
| [**WerrySs/herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync) | 0 | Keeps cmux's graphical file explorer synchronized with the current directory of the focused Herdr pane by listening to focus events without modifying shell sessions. |
| [**Phoobobo/grokbot-bridge-herdr**](https://github.com/Phoobobo/grokbot-bridge-herdr) | 0 | Lets Grok Bot drive, watch, and take over agent panes through the gbb CLI. Posts webhooks when managed agents finish or block. |
| [**genexk/anynotate · integrations/herdr**](https://github.com/genexk/anynotate/tree/main/integrations/herdr) | 0 | Sends browser notes made with Anynotate to a Herdr TUI agent pane through an inbox popup or a one-key send of the latest note. |
| [**LuisBDev/herdrop**](https://github.com/LuisBDev/herdrop) | 0 | Lets you pick elements on a web page in Chrome, add notes and send them to a coding agent in a Herdr pane as a Markdown bundle. Pairs a Chrome extension with a Rust bridge plugin. |
| [**openscout-app/herdr-scout**](https://github.com/openscout-app/herdr-scout) | 0 | Lets you ask OpenScout agents from any Herdr TUI pane, send a text selection to one and keep the Scout feed beside your work. |
| [**Hourtick/herdr-plugin**](https://github.com/Hourtick/herdr-plugin) | 0 | Connects Herdr agents to Hourtick over its MCP server so you can start an agent on a task and track and log the time it works. |
| [**daniel7an/herdr-t3-import**](https://github.com/daniel7an/herdr-t3-import) | 0 | Imports your terminal Claude Code and Codex chats into T3 Code. Runs as a Herdr TUI plugin or a standalone CLI. |
| [**AdriaBA/herdr-hermes-bridge**](https://github.com/AdriaBA/herdr-hermes-bridge) | 0 | Reports Hermes Agent lifecycle state into Herdr TUI panes, including subagents, approvals, and tool activity, instead of relying on screen detection. |
| [**muthuishere/herdr-conv-hooks**](https://github.com/muthuishere/herdr-conv-hooks) | 0 | Binds a chat conversation to an agent pane through one hook with create, listen, send, and stop verbs, so the agent answers messages without leaving its pane. |
| [**muretai/muretai-herdr-plugin**](https://github.com/muretai/muretai-herdr-plugin) | 0 | Gives Herdr TUI agents addresses on the Muretai network so they can exchange signed messages across machines and with other people's agents. Adds an inbox, invites, and send actions. |
| [**yycholla/herdr-rex-bridge**](https://github.com/yycholla/herdr-rex-bridge) | 0 | Adds a Rex section to the Herdr app sidebar and a bridge that opens Rex sessions, windows and terminals as Herdr spaces, tabs and panes. Shows connection state per server and creates spaces from the sidebar. |
| [**jspoynor/herdr-hermes-status**](https://github.com/jspoynor/herdr-hermes-status) | 0 | Makes classic Hermes Agent terminal sessions appear in the Herdr app as agents with Working, Idle, or Blocked status through OSC 7501, including over SSH. |
| [**ngyingkai/traecli-herdr**](https://github.com/ngyingkai/traecli-herdr) | 0 | Wraps TRAE CLI so Herdr panes report a real agent identity and live status through the pane report-agent API, and records a resume command per pane. |
| [**Torbraw/opencode-herdr-app-bridge**](https://github.com/Torbraw/opencode-herdr-app-bridge) | 0 | Publishes OpenCode tab, session title, activity, and model details to the Herdr app so the sidebar shows them. Clicking a session focuses its OpenCode tab. |
