# Awesome Herdr: Connect through MCP and the socket API

The full list for domain 3 of [Awesome Herdr](../README.md#3-connect-through-mcp-and-the-socket-api), ordered by GitHub stars.

- [MCP servers for controlling Herdr panes and agents (10)](#mcp-servers-for-controlling-herdr-panes-and-agents)
- [MCP bridges for ChatGPT, Claude Desktop and web assistants (6)](#mcp-bridges-for-chatgpt-claude-desktop-and-web-assistants)
- [MCP and ACP adapters for specific agent hosts (4)](#mcp-and-acp-adapters-for-specific-agent-hosts)
- [Socket API client libraries by language (12)](#socket-api-client-libraries-by-language)
- [Socket API automation toolkits and drivers (6)](#socket-api-automation-toolkits-and-drivers)
- [HTTP and WebSocket bridges that expose Herdr (5)](#http-and-websocket-bridges-that-expose-herdr)
- [Bridges to third-party agent platforms (8)](#bridges-to-third-party-agent-platforms)
- [Agent-state correctors and background-work markers (9)](#agent-state-correctors-and-background-work-markers)
- [OpenCode status reporters and bridges (6)](#opencode-status-reporters-and-bridges)
- [DeepSeek Harness and Reasonix integrations (13)](#deepseek-harness-and-reasonix-integrations)
- [Pi and Oh My Pi status reporters (8)](#pi-and-oh-my-pi-status-reporters)
- [Hermes Agent status reporters and Claude Code bridges (4)](#hermes-agent-status-reporters-and-claude-code-bridges)
- [Hermes Agent workflows, kanban and bot networks (9)](#hermes-agent-workflows-kanban-and-bot-networks)
- [Command Code, Cline and Freebuff status reporters (5)](#command-code-cline-and-freebuff-status-reporters)
- [TraeX, MiMo Code, CodeBuddy, ZCode and MiniMax status reporters (9)](#traex-mimo-code-codebuddy-zcode-and-minimax-status-reporters)
- [Mistral Vibe and Goose status reporters (5)](#mistral-vibe-and-goose-status-reporters)
- [Status reporters for Amp, Auggie, Junie, Kiro, Rovo Dev and Cortex Code (7)](#status-reporters-for-amp-auggie-junie-kiro-rovo-dev-and-cortex-code)
- [Jcode status reporters (4)](#jcode-status-reporters)
- [Status reporters for smaller and open-source agent CLIs (12)](#status-reporters-for-smaller-and-open-source-agent-clis)
- [Telegram bots for agent alerts (6)](#telegram-bots-for-agent-alerts)
- [Telegram bots for remote commands and approvals (6)](#telegram-bots-for-remote-commands-and-approvals)
- [Telegram bridges that map agents to forum topics (6)](#telegram-bridges-that-map-agents-to-forum-topics)
- [Slack notifications and bots (7)](#slack-notifications-and-bots)
- [Discord and workplace-messenger bridges (7)](#discord-and-workplace-messenger-bridges)
- [Two-way chat bridges for several services (7)](#two-way-chat-bridges-for-several-services)
- [Alert routers that fan out to chat, push and webhooks (5)](#alert-routers-that-fan-out-to-chat-push-and-webhooks)
- [macOS notification banners (9)](#macos-notification-banners)
- [Windows and WSL toast notifications (4)](#windows-and-wsl-toast-notifications)
- [Cross-platform and remote-host desktop notifiers (4)](#cross-platform-and-remote-host-desktop-notifiers)
- [Persistent popups, inboxes and screen cues for waiting agents (6)](#persistent-popups-inboxes-and-screen-cues-for-waiting-agents)
- [Agent-done sounds and sound packs (9)](#agent-done-sounds-and-sound-packs)
- [Spoken summaries and text-to-speech alerts (6)](#spoken-summaries-and-text-to-speech-alerts)
- [Phone push alerts through ntfy (6)](#phone-push-alerts-through-ntfy)
- [Phone push through Gotify, Bark and iPhone companion apps (5)](#phone-push-through-gotify-bark-and-iphone-companion-apps)
- [Webhook, email and hosted-push notifiers (10)](#webhook-email-and-hosted-push-notifiers)
- [Telemetry exporters and presence feeds (10)](#telemetry-exporters-and-presence-feeds)
- [Standalone dashboards for agent time, cost and session health (8)](#standalone-dashboards-for-agent-time-cost-and-session-health)
- [Speech-to-text dictation into panes (10)](#speech-to-text-dictation-into-panes)
- [Voice assistants and spoken commands at your desk (6)](#voice-assistants-and-spoken-commands-at-your-desk)
- [Phone calls and phone-based voice control for agents (6)](#phone-calls-and-phone-based-voice-control-for-agents)
- [Remote access over SSH, Tailscale and QUIC (9)](#remote-access-over-ssh-tailscale-and-quic)
- [Remote port forwarding, link opening and file transfer (10)](#remote-port-forwarding-link-opening-and-file-transfer)
- [Browser selections, notes and photos sent to agents (4)](#browser-selections-notes-and-photos-sent-to-agents)
- [Warp terminal integrations (4)](#warp-terminal-integrations)
- [cmux integrations (5)](#cmux-integrations)
- [tmux plugins with Herdr agent detection (5)](#tmux-plugins-with-herdr-agent-detection)

---

## 3. Connect through MCP and the socket API

*322 projects. Protocols, clients, bots, and event bridges that link Herdr to external tools, editors, and messaging apps.*

### MCP servers for controlling Herdr panes and agents

*10 projects. MCP servers that expose Herdr workspaces, panes and agents as tools so any MCP client can inspect, start and steer them.*

| Project | Stars | What it does |
|---|--:|---|
| [**rmngl/herdr-mesh**](https://github.com/rmngl/herdr-mesh) | 13 | Exposes Herdr pane management, agent messaging, and contextual handoffs through an MCP server. |
| [**ryanthedev/herderp**](https://github.com/ryanthedev/herderp) | 5 | Adds Claude Code MCP tools for managing agents and terminals across Herdr TUI and herdr-core, including remote hosts and session history. |
| [**eugeneb50/herdr-mcp**](https://github.com/eugeneb50/herdr-mcp) | 2 | Exposes Herdr workspace and pane controls as tools to any Model Context Protocol (MCP) client. |
| [**Orange-County-AI/herdr-mcp**](https://github.com/Orange-County-AI/herdr-mcp) | 2 | Exposes Herdr's socket API as a local or remote MCP server. |
| [**thomasfossum/herdr-mcp**](https://github.com/thomasfossum/herdr-mcp) | 2 | Lets MCP clients control a running Herdr session: see agent status, open tabs and panes, start agents, send them work and run worktree-isolated jobs. Runs over stdio or Streamable HTTP in standard-library Python with Docker and client examples. |
| [**boozedog/herdr-mcp**](https://github.com/boozedog/herdr-mcp) | 1 | Coordinates agents in Herdr TUI panes through a Deno MCP server with configurable workflow roles. |
| [**husniadil/olympus**](https://github.com/husniadil/olympus) | 1 | Provides a terminal you can drive from code: create, drive, observe and tear down real terminal sessions on zmx, tmux, meja or herdr, through a Go package, a CLI and a stdio MCP server. |
| [**jhionan/herdr-computer-use**](https://github.com/jhionan/herdr-computer-use) | 1 | Adds a macOS helper and MCP server that lets agents observe and operate desktop apps and signed-in browser windows, with Herdr TUI plugin actions to set it up and manage it. Needs macOS 14 and Swift. |
| [**aelaguiz/herdr-mcp**](https://github.com/aelaguiz/herdr-mcp) | 0 | Exposes Herdr TUI workspace inspection, pane control and agent prompting to MCP clients through the Herdr CLI. |
| [**islam3zzat/herdr-mcp**](https://github.com/islam3zzat/herdr-mcp) | 0 | An MCP server that lets AI assistants inspect and control coding agents running in Herdr through a socket-based communication bridge. |

### MCP bridges for ChatGPT, Claude Desktop and web assistants

*6 projects. MCP gateways and relays that put a hosted or desktop chat assistant in front of the agents running in Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**whshang/herdr-mcp**](https://github.com/whshang/herdr-mcp) | 10 | Adds a stable MCP and OAuth bridge for remote web planners to inspect and control local Herdr workspaces. |
| [**HowAreAllWell/gpt-agent-bridge**](https://github.com/HowAreAllWell/gpt-agent-bridge) | 6 | Connects ChatGPT Web to local agents in Herdr TUI to dispatch tasks and review returned results. |
| [**54rt1n/herdr-simple-mcp**](https://github.com/54rt1n/herdr-simple-mcp) | 2 | Provides a lightweight Model Context Protocol server for driving Herdr from Claude Desktop and Cursor. |
| [**nytafar/herdr-spawn**](https://github.com/nytafar/herdr-spawn) | 1 | Exposes an MCP tool that starts coding agents on your machines from a chat prompt, with a Claude Code Remote Control link when available. |
| [**kshvidler/peerband-cli**](https://github.com/kshvidler/peerband-cli) | 0 | Connects ChatGPT, Claude, or any MCP client to the coding agents running in Herdr through the PeerBand relay. Ships the peerband CLI and a Herdr plugin; the relay is a hosted service. |
| [**yonatangross/herdr-desktop-bridge**](https://github.com/yonatangross/herdr-desktop-bridge) | 0 | Runs a stdio MCP server that lets Claude Desktop or any MCP client read a Herdr floor and leave messages for agents. Gives the client a mailbox and a doorbell without control of the panes. |

### MCP and ACP adapters for specific agent hosts

*4 projects. Adapters that let one particular agent host, such as Goose, Cursor, OpenCode or an ACP client, drive Herdr through MCP or the Agent Client Protocol.*

| Project | Stars | What it does |
|---|--:|---|
| [**aquaherd/goose-herdr**](https://github.com/aquaherd/goose-herdr) | 3 | Connects Goose to Herdr TUI through an MCP extension and reports Goose lifecycle state to the sidebar. |
| [**frankjoshua/herdr-acp**](https://github.com/frankjoshua/herdr-acp) | 2 | Exposes a Herdr pane as an Agent Client Protocol (ACP) agent, so any ACP client can prompt Claude Code, Codex, Pi, or a plain shell running in that pane. Streams the pane back to the client as one shared session, including text typed directly at the pane, and reads agent transcripts on Linux without hooks. |
| [**Kuznetsov-Ilia/agy**](https://github.com/Kuznetsov-Ilia/agy) | 0 | Maintains a warm Antigravity worker pool in Herdr and exposes delegation tools to Cursor through an MCP server. |
| [**bonsai/herdr-mcp**](https://github.com/bonsai/herdr-mcp) | 0 | Lets OpenCode rename and blink Herdr TUI tabs or trigger speech through MCP, with additional plugin actions and monitoring. |

### Socket API client libraries by language

*12 projects. Typed client libraries and SDKs for calling Herdr's socket API from Go, Java, Python, Rust, Swift and TypeScript programs.*

| Project | Stars | What it does |
|---|--:|---|
| [**dmmulroy/herdr-ts-sdk**](https://github.com/dmmulroy/herdr-ts-sdk) | 57 | Provides an Effect-native TypeScript SDK for Herdr's local protocol-21 socket API. |
| [**54rt1n/herdr-python-client**](https://github.com/54rt1n/herdr-python-client) | 3 | Provides typed Python bindings and socket utilities for automating Herdr programmatically. |
| [**egriff38/effect-herdr**](https://github.com/egriff38/effect-herdr) | 2 | Controls the Herdr terminal multiplexer through a typed Effect-TS SDK. |
| [**QuiquiMatCom2004/herdr-py**](https://github.com/QuiquiMatCom2004/herdr-py) | 1 | Lets Python programs control Herdr workspaces, panes, agents, and other resources through its socket API. |
| [**lib-x/herdr-sock-go**](https://github.com/lib-x/herdr-sock-go) | 1 | Connects Go programs to the Herdr TUI newline-delimited socket API with typed and raw methods. |
| [**maxandersen/jherdr**](https://github.com/maxandersen/jherdr) | 1 | Connects Java programs to the Herdr TUI socket API using a scripting facade, generated typed methods or raw calls. |
| [**cyperx84/herdr-api**](https://github.com/cyperx84/herdr-api) | 1 | Connects Go programs to the Herdr TUI socket API with typed agent models and event subscriptions. |
| [**vika2603/herdr-client**](https://github.com/vika2603/herdr-client) | 1 | Provides a typed Go client and plugin toolkit for Herdr's socket API, generated from the schema the herdr binary prints and covering all 102 methods of protocol 22. Adds a reconnecting session mirror, the pane graphics frame stream, and the manifest parser and entrypoint dispatch a Go plugin needs. |
| [**rudironsoni/HerdrKit**](https://github.com/rudironsoni/HerdrKit) | 0 | Provides a Swift 6 client kit implementing Herdr JSON socket API protocols 17 through 22. |
| [**brooswit-factory/jsHerdrSDK**](https://github.com/brooswit-factory/jsHerdrSDK) | 0 | Provides a typed TypeScript client for the herdr socket API, generated from its published JSON Schema. |
| [**vinceferro/herdr-tg · crates/herdr-client**](https://github.com/vinceferro/herdr-tg/tree/HEAD/crates/herdr-client) | 0 | Reads Herdr TUI state and pane output with a typed Rust client for the socket protocol. |
| [**stefanahman/mux**](https://github.com/stefanahman/mux) | 0 | Lets Go programs manage workspaces, panes, and agent state through a common interface for tmux, Herdr TUI, and cmux. |

### Socket API automation toolkits and drivers

*6 projects. Scripts and small frameworks built on the socket API that drive agents, save layouts or script panes rather than just wrapping the protocol.*

| Project | Stars | What it does |
|---|--:|---|
| [**0xGosu/herdr-auto-pilot**](https://github.com/0xGosu/herdr-auto-pilot) | 31 | Prompts a running coding CLI through the Herdr API. A training mode observes user actions, safety checks block dangerous operations, and an optional autonomous mode can continue prompting after sufficient setup. |
| [**fabzter/herdrbridge**](https://github.com/fabzter/herdrbridge) | 1 | Lets Python bridges drive Herdr agents, track sessions, extract replies, and navigate approval prompts through the CLI and socket API. |
| [**rrojo02/herdr-bridge**](https://github.com/rrojo02/herdr-bridge) | 1 | Connects external coding agents to Herdr through its local socket API. |
| [**kevinWangSheng/herdr-kit**](https://github.com/kevinWangSheng/herdr-kit) | 0 | Saves and restores declarative Herdr TUI pane layouts, watches events, and calls socket methods. Includes two plugins and an agent skill. |
| [**opencharly/plugin-herdr**](https://github.com/opencharly/plugin-herdr) | 0 | Controls Herdr terminal multiplexer sessions over its NDJSON socket API using Charly commands. |
| [**btj93/herdr-tokens**](https://github.com/btj93/herdr-tokens) | 0 | Publishes workspace metadata tokens derived from agent status, so sidebar colours can vary by state. |

### HTTP and WebSocket bridges that expose Herdr

*5 projects. Servers that put Herdr's socket behind REST, HTTP or WebSocket endpoints for browsers, apps and other clients to build on.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**benkraus/herdr-plugin-mobile-relay**](https://github.com/benkraus/herdr-plugin-mobile-relay) | 11 | Bridges Herdr TUI socket operations to HTTP and WebSocket clients, including a browser interface and optional Tailscale publishing. |
| [**akhileshrangani4/herdr-bridge**](https://github.com/akhileshrangani4/herdr-bridge) | 2 | An HTTP bridge with a terminal-friendly control panel for Herdr agents. |
| [**XicuM/herdr-bridge**](https://github.com/XicuM/herdr-bridge) | 1 | Runs a daemon that connects to the Herdr socket and remote machines over SSH. Serves agent state, terminals, and Obsidian vaults to other devices over authenticated HTTP and WebSockets. |
| [**JefeLabs/herdr-web-broker**](https://github.com/JefeLabs/herdr-web-broker) | 0 | Adds a self-hosted REST and WebSocket API for Herdr to spawn and steer coding agents with parent-child federation. |
| [**Howryann/herdr-monitor**](https://github.com/Howryann/herdr-monitor) | 0 | Exposes read-only Herdr agent status over HTTP with no runtime dependencies. |

### Bridges to third-party agent platforms

*8 projects. Connectors between Herdr and other agent platforms and clients such as Rex, T3 Code, OpenScout, ST2 and Grok Bot.*

| Project | Stars | What it does |
|---|--:|---|
| [**elonnzhang/Herdrex**](https://github.com/elonnzhang/Herdrex) | 6 | Connects Herdr TUI workspaces and terminal panes to Rex desktop and CLI clients, locally or over SSH. |
| [**Hourtick/herdr-plugin**](https://github.com/Hourtick/herdr-plugin) | 0 | Connects Herdr agents to Hourtick over its MCP server so you can start an agent on a task and track and log the time it works. |
| [**yycholla/herdr-rex-bridge**](https://github.com/yycholla/herdr-rex-bridge) | 0 | Adds a Rex section to the Herdr app sidebar and a bridge that opens Rex sessions, windows and terminals as Herdr spaces, tabs and panes. Shows connection state per server and creates spaces from the sidebar. |
| [**daniel7an/herdr-t3-import**](https://github.com/daniel7an/herdr-t3-import) | 0 | Imports your terminal Claude Code and Codex chats into T3 Code. Runs as a Herdr TUI plugin or a standalone CLI. |
| [**openscout-app/herdr-scout**](https://github.com/openscout-app/herdr-scout) | 0 | Lets you ask OpenScout agents from any Herdr TUI pane, send a text selection to one and keep the Scout feed beside your work. |
| [**slashv/st2-herdr**](https://github.com/slashv/st2-herdr) | 0 | Connects ST2 agent fleets to Herdr workspaces with live attachments, a hierarchy view, and operator-approved agent creation. |
| [**Phoobobo/grokbot-bridge-herdr**](https://github.com/Phoobobo/grokbot-bridge-herdr) | 0 | Lets Grok Bot drive, watch, and take over agent panes through the gbb CLI. Posts webhooks when managed agents finish or block. |
| [**musingfox/herdr-osc7501**](https://github.com/musingfox/herdr-osc7501) | 0 | Reports the status of every Herdr TUI pane agent to the outer Rex terminal as OSC 7501 sequences. Works in every session including the default one. |

### Agent-state correctors and background-work markers

*9 projects. Helpers that fix or extend the working, idle and done state Herdr reports, for example by marking idle agents that still run background shells or monitors.*

| Project | Stars | What it does |
|---|--:|---|
| [**cdc-lst/herdr-wait**](https://github.com/cdc-lst/herdr-wait) | 4 | Examines the process tree of idle or blocked panes and replaces generic state with a specific waiting label, such as a build or external CLI name. |
| [**ardasevinc/herdr-codex-bridge**](https://github.com/ardasevinc/herdr-codex-bridge) | 3 | Provides a native Herdr pane identity for Codex sessions using a centralized app-server. |
| [**vaclavik-xyz/herdwatch**](https://github.com/vaclavik-xyz/herdwatch) | 1 | Keeps a pane marked as working while CI, review, or another background condition is still pending after the agent itself becomes idle. It can run once or as a background service. |
| [**brooswit-factory/drovr**](https://github.com/brooswit-factory/drovr) | 0 | Wraps a TypeScript Herdr TUI SDK to detect blocked agents and correct reported agent states. |
| [**MarcellGranat/herdr-notify**](https://github.com/MarcellGranat/herdr-notify) | 0 | Watches a Herdr TUI pane after one keypress and marks it done in the sidebar when its shell prompt returns. Can also send a Pushover notification. |
| [**SpatialNexus/herdr-subagent-state**](https://github.com/SpatialNexus/herdr-subagent-state) | 0 | Uses Claude Code, Codex, and Pi hooks to report working state while tools or delegated subagents are active. |
| [**daocoding/herdr-claude-lifecycle**](https://github.com/daocoding/herdr-claude-lifecycle) | 0 | Reports Claude Code working, blocked, and idle states to Herdr from hooks and writes a state file for an Omarchy widget. |
| [**netresearch/herdr-bg-activity**](https://github.com/netresearch/herdr-bg-activity) | 0 | Marks idle Claude Code agents that still run monitors or background shells. Includes Herdr app mods and a layout with service links. |
| [**rcosteira79/herdr-idle-shell-badge**](https://github.com/rcosteira79/herdr-idle-shell-badge) | 0 | Marks idle agents that still have background shells running. |

### OpenCode status reporters and bridges

*6 projects. Plugins that fix or add OpenCode (1.x and 2) pane status, session identity and activity inside Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**anaypurohit0907/herdr-opencode-bridge**](https://github.com/anaypurohit0907/herdr-opencode-bridge) | 3 | Corrects Herdr TUI OpenCode pane status by aggregating root sessions and avoiding false idle states. |
| [**VicenteOlmos/opencode-herdr**](https://github.com/VicenteOlmos/opencode-herdr) | 2 | Routes OpenCode V2 beta requests through Herdr TUI adapters for supported agent CLIs. |
| [**xdagiz/opencode2-herdr**](https://github.com/xdagiz/opencode2-herdr) | 1 | Reports OpenCode 2 agent states and session identity to Herdr TUI through its socket. |
| [**HunterStarets/herdr-gitbash-agent-detector**](https://github.com/HunterStarets/herdr-gitbash-agent-detector) | 1 | Detects OpenCode sessions running inside Git Bash panes on Windows and reports their state (idle / working). |
| [**Nofuture123/herdr-opencode2-integration**](https://github.com/Nofuture123/herdr-opencode2-integration) | 0 | Reports OpenCode 1.x and 2.0 session states to Herdr TUI with per-pane process isolation. |
| [**Torbraw/opencode-herdr-app-bridge**](https://github.com/Torbraw/opencode-herdr-app-bridge) | 0 | Publishes OpenCode tab, session title, activity, and model details to the Herdr app so the sidebar shows them. Clicking a session focuses its OpenCode tab. |

### DeepSeek Harness and Reasonix integrations

*13 projects. Plugins and bridges that make DeepSeek Harness (dsh) and Reasonix sessions report state to Herdr or let them control it.*

| Project | Stars | What it does |
|---|--:|---|
| [**mitkox/dsh-herdr**](https://github.com/mitkox/dsh-herdr) | 17 | Reports DeepSeek Harness agent state to herdr-core via OSC 7501 and displays sessions in a Herdr app panel. |
| [**sunny0826/dsh-plugin-herdr**](https://github.com/sunny0826/dsh-plugin-herdr) | 4 | Lets DeepSeek Harness sessions inspect and control Herdr through socket-backed tools and a session-scoped panel. |
| [**scrappylabsai/podr**](https://github.com/scrappylabsai/podr) | 3 | Adds Reasonix and DeepSeek Harness detection to a Herdr TUI fork and includes a client for attaching to DSH sessions. |
| [**dsh-blue/herdr-agent-state**](https://github.com/dsh-blue/herdr-agent-state) | 2 | Reports DeepSeek Harness lifecycle state, session references, and model metadata to the current Herdr pane. |
| [**dsh-plugin-collection/dsh-herdr-site**](https://github.com/dsh-plugin-collection/dsh-herdr-site) | 2 | Reports dsh/cc-tui agent state (working/idle/blocked) to Herdr over the custom-integration protocol. |
| [**uuie/reasonix-herdr**](https://github.com/uuie/reasonix-herdr) | 2 | Reports Reasonix agent lifecycle states to Herdr in real time and adds native workspace and pane controls for supervising Reasonix alongside other agents. |
| [**flaricy/herdr-bridge**](https://github.com/flaricy/herdr-bridge) | 1 | Reports DeepSeek Harness activity to the Herdr pane that hosts it, including live working, blocked, and idle states, without requiring changes to Herdr. |
| [**TheRealHaoLiu/dsh-herdr**](https://github.com/TheRealHaoLiu/dsh-herdr) | 1 | Reports a DeepSeek Harness root agent’s identity and lifecycle state to its Herdr pane. |
| [**haoliangwu/dsh-herdr**](https://github.com/haoliangwu/dsh-herdr) | 1 | Reports dsh session states to the Herdr agent panel through the pane-socket protocol. |
| [**FUSU123fusu/dsh-tui-herdr**](https://github.com/FUSU123fusu/dsh-tui-herdr) | 1 | Reports dsh-TUI working, blocked, and done states to the Herdr sidebar through the pane report-agent API. README is in Chinese. |
| [**Lbryany/dsh-plugins · packages/dsh-herdr**](https://github.com/Lbryany/dsh-plugins/tree/main/packages/dsh-herdr) | 0 | Aggregates DeepSeek Harness root and child agent states and reports the resulting lifecycle state to the Herdr pane. |
| [**wenhao4126/dsh-herdr**](https://github.com/wenhao4126/dsh-herdr) | 0 | Exposes Herdr workspaces, panes, and coding agents as DeepSeek Harness tools. |
| [**mougua/herdr-reasonix**](https://github.com/mougua/herdr-reasonix) | 0 | Detects Reasonix agents and displays their status correctly. |

### Pi and Oh My Pi status reporters

*8 projects. Pi and Oh My Pi extensions that report Pi lifecycle state, blocked prompts, snooze and crash alerts to the Herdr sidebar.*

| Project | Stars | What it does |
|---|--:|---|
| [**joelhooks/herdr-pings**](https://github.com/joelhooks/herdr-pings) | 8 | Adds turn-completion alerts and crash detection for Pi agents in Herdr. A Pi extension and companion wait command track workers, while short call signs make concurrent agents easier to identify. |
| [**briankeefe/herdr-omp**](https://github.com/briankeefe/herdr-omp) | 4 | Corrects false-idle Oh My Pi agent states and names Herdr workspaces after tasks. |
| [**spi-ca/pi-herdr-presence**](https://github.com/spi-ca/pi-herdr-presence) | 1 | Extends Pi agent presence indicators and runtime status inside Herdr workspaces. |
| [**dk3775/herdr-plugin-omp-state**](https://github.com/dk3775/herdr-plugin-omp-state) | 1 | Reports omp agent state to Herdr TUI from the terminal title, for panes where the official omp integration is not reporting. |
| [**Attamusc/pi-herdr**](https://github.com/Attamusc/pi-herdr) | 0 | Reports Pi lifecycle states to Herdr TUI so its sidebar shows working, blocked, done, and idle agents. |
| [**larryboiNEUQ/pi-herdr-ui-bridge**](https://github.com/larryboiNEUQ/pi-herdr-ui-bridge) | 0 | Reports blocking Pi extension prompts as Herdr agent blocked states so notification plugins can alert users. |
| [**BrianM0330/pi-herdr-snooze**](https://github.com/BrianM0330/pi-herdr-snooze) | 0 | Adds a forced snooze state to Pi agents in Herdr, controlled through `/snooze` or a key binding and independent of the underlying agent type. |
| [**markbrutx/pif-herdr-reporter**](https://github.com/markbrutx/pif-herdr-reporter) | 0 | Reports working and idle states from the pif coding agent to its Herdr TUI pane and releases the agent on exit. |

### Hermes Agent status reporters and Claude Code bridges

*4 projects. Plugins that show Hermes Agent sessions as Herdr agents or bridge Hermes and Claude Code through Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**AdriaBA/herdr-hermes-bridge**](https://github.com/AdriaBA/herdr-hermes-bridge) | 0 | Reports Hermes Agent lifecycle state into Herdr TUI panes, including subagents, approvals, and tool activity, instead of relying on screen detection. |
| [**jspoynor/herdr-hermes-status**](https://github.com/jspoynor/herdr-hermes-status) | 0 | Makes classic Hermes Agent terminal sessions appear in the Herdr app as agents with Working, Idle, or Blocked status through OSC 7501, including over SSH. |
| [**fabzter/hermes-bridge**](https://github.com/fabzter/hermes-bridge) | 0 | Lets Claude Code send messages and commands to a local Hermes Agent through Herdr and respond to its approval prompts. |
| [**Fectivnfy112357/claude-code-bridge**](https://github.com/Fectivnfy112357/claude-code-bridge) | 0 | Bridges Hermes Agent and Claude Code CLI in print mode and interactive Herdr sessions. |

### Hermes Agent workflows, kanban and bot networks

*9 projects. Hermes Agent setups that delegate to Pi or Claude Code, run a Hermes Kanban board, manage Hermes profiles and jobs, or run Hermes bot networks across Herdr workspaces.*

| Project | Stars | What it does |
|---|--:|---|
| [**skaftanis/herdr-hermes-manager**](https://github.com/skaftanis/herdr-hermes-manager) | 3 | Manages local Hermes Agent profiles, scheduled jobs and bot chats from Herdr TUI workspaces. |
| [**sh1ny/herdr-switchyard**](https://github.com/sh1ny/herdr-switchyard) | 1 | A human-approved Hermes and Herdr workflow for isolated OMP coding workers, using Beads as the persistent task ledger. |
| [**andorexu/hermes-agent-skills-pack**](https://github.com/andorexu/hermes-agent-skills-pack) | 1 | Adds reusable Hermes Agent skills for reasoning, engineering, OCR, and web tasks to supported agents. |
| [**DanDo385/cockpit**](https://github.com/DanDo385/cockpit) | 1 | Creates a Herdr TUI operating desk with Hermes Kanban, worktree lanes, and separate review and operations workspaces. |
| [**gaiagent0/ct304-hermes-bots**](https://github.com/gaiagent0/ct304-hermes-bots) | 0 | Provides a Hermes bot network coordinating agents across Herdr workspaces with capability-based model distribution. |
| [**steven-terrana/hermes-herdr-plugin**](https://github.com/steven-terrana/hermes-herdr-plugin) | 0 | Orchestrates Hermes agent sessions with Claude Code, Codex, and Pi under Herdr. |
| [**regrow1123/herdr-pi-delegation**](https://github.com/regrow1123/herdr-pi-delegation) | 0 | Adds a Hermes to Pi delegation workflow across Herdr panes with event-based completion. |
| [**saforem2/herdr-hermes-kanban**](https://github.com/saforem2/herdr-hermes-kanban) | 0 | Shows a Hermes Kanban board in a Herdr TUI pane with a quick-capture popup. Uses only the hermes kanban CLI. |
| [**DMelisena/shipmates**](https://github.com/DMelisena/shipmates) | 0 | A Hermes plugin offering a preconfigured Kun Chen-style Herdr and OpenCode first-mate workflow. The source catalog does not describe its individual controls. |

### Command Code, Cline and Freebuff status reporters

*5 projects. Plugins that make Command Code, Cline and Freebuff processes appear as native Herdr agents with lifecycle status.*

| Project | Stars | What it does |
|---|--:|---|
| [**TheMetalStorm/herdr-commandcode-plugin**](https://github.com/TheMetalStorm/herdr-commandcode-plugin) | 14 | Integrates Command Code as a Herdr agent runtime with process detection, idle, working, and blocked status, session recovery after server restarts, and toast alerts when input is needed. |
| [**TheMetalStorm/herdr-freebuff-plugin**](https://github.com/TheMetalStorm/herdr-freebuff-plugin) | 10 | Integrates Freebuff agents with Herdr by reading PTY output and local session files, then reporting idle, working, and blocked states through the socket API. |
| [**Comamoca/command-code-herdr**](https://github.com/Comamoca/command-code-herdr) | 2 | Reports Command Code working, idle, and blocked lifecycle states to Herdr TUI through its local socket. |
| [**thesimonharms/herdr-cmd-agent-plugin**](https://git.simonharms.com/thesimonharms/herdr-cmd-agent-plugin) | — | Adds CommandCode agent detection to Herdr TUI, including idle, working, and blocked state in the sidebar. |
| [**TheMetalStorm/herdr-cline-plugin**](https://github.com/TheMetalStorm/herdr-cline-plugin) | 0 | Makes a plain Cline CLI process appear as a native Herdr agent with lifecycle reporting. |

### TraeX, MiMo Code, CodeBuddy, ZCode and MiniMax status reporters

*9 projects. Adapters that report TraeX, MiMo Code, CodeBuddy, ZCode and MiniMax Code agent states, models and sessions to Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**Ziy1-Tan/herdr-codebuddy**](https://github.com/Ziy1-Tan/herdr-codebuddy) | 7 | Reports CodeBuddy session, working and permission states to Herdr TUI through hooks. |
| [**szrenwei/herdr-traex**](https://github.com/szrenwei/herdr-traex) | 2 | Integrates TraeX agent lifecycle states and available model metadata into the Herdr TUI sidebar. |
| [**ShinoharaHaruna/mimo-code-herdr**](https://github.com/ShinoharaHaruna/mimo-code-herdr) | 1 | Integrates MiMo Code agent state and session controls into Herdr TUI, with cleanup on exit and optional OpenCode identity. |
| [**ichadhr/herdr-zcode**](https://github.com/ichadhr/herdr-zcode) | 1 | Adds ZCode agent support to Herdr TUI, showing zcode panes in the sidebar with live working, blocked, and idle state. Registers hooks in the zcode settings file. |
| [**jaaacki/herdr-plugin-minimax-code**](https://github.com/jaaacki/herdr-plugin-minimax-code) | 1 | Adds MiniMax Code support to Herdr TUI by launching mcode in a new pane and registering hand-started mcode sessions so they appear as agents. |
| [**Phoobobo/herdr-traex-integration**](https://github.com/Phoobobo/herdr-traex-integration) | 0 | Connects TraeX lifecycle hooks to Herdr's agent-reporting socket methods, giving TraeX panes correct idle, working, and blocked status. |
| [**ngyingkai/traecli-herdr**](https://github.com/ngyingkai/traecli-herdr) | 0 | Wraps TRAE CLI so Herdr panes report a real agent identity and live status through the pane report-agent API, and records a resume command per pane. |
| [**junliu-mde/mimo-code-herdr-plugin**](https://github.com/junliu-mde/mimo-code-herdr-plugin) | 0 | Combines all subagent states into a stable idle, working, blocked, or done status for Herdr. A watchdog releases stale labels after crashes, and nested MiMo tool calls are ignored. |
| [**StarDuster/mimo-code-herdr-plugin**](https://github.com/StarDuster/mimo-code-herdr-plugin) | 0 | Shows MiMo Code agent state in herdr's sidebar, a user-level MiMo plugin, no herdr changes required. |

### Mistral Vibe and Goose status reporters

*5 projects. Hook-based adapters that give Mistral Vibe and Goose panes a real agent identity and idle, working and blocked state in Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**guiand888/herdr-mistral-vibe**](https://github.com/guiand888/herdr-mistral-vibe) | 2 | Starts Mistral Vibe sessions in Herdr panes through an action and a pane entrypoint, since Herdr has no built-in agent kind for it. Pairs with herdr-vibe, which reports Vibe state and resume commands. |
| [**inoribea/herdr-goose-bridge**](https://github.com/inoribea/herdr-goose-bridge) | 2 | Detects goose panes and reports idle, working and blocked state to Herdr, which cannot detect goose on its own, notably on Windows. |
| [**sgnilreutr/herdr-vibe-integration**](https://github.com/sgnilreutr/herdr-vibe-integration) | 1 | Reports Mistral Vibe agent states to the Herdr TUI sidebar through Vibe hooks and the socket or CLI. |
| [**guiand888/herdr-vibe**](https://github.com/guiand888/herdr-vibe) | 1 | Reports Mistral Vibe agent state to Herdr from Vibe hooks, giving Vibe sessions a sidebar entry, finish and decision notifications, and `herdr agent wait` support. Saves the resume command so a Vibe session comes back in the same pane after a Herdr restart. |
| [**meuble/Herdr-mistral-vibe**](https://github.com/meuble/Herdr-mistral-vibe) | 0 | Reports Mistral Vibe working, idle, and blocked states to Herdr TUI through Vibe hooks. |

### Status reporters for Amp, Auggie, Junie, Kiro, Rovo Dev and Cortex Code

*7 projects. Plugins that make vendor coding CLIs such as Amp, Auggie, Junie, Kiro, Rovo Dev and Cortex Code show working, idle and blocked state in Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**usrivastava92/herdr-rovo-dev**](https://github.com/usrivastava92/herdr-rovo-dev) | 2 | Detects Rovo Dev CLI sessions and reports them as live agents in Herdr. |
| [**BlockedPath/herdr-amp-orbs**](https://github.com/BlockedPath/herdr-amp-orbs) | 1 | Runs Amp orbs, which are remote Amp agents, in Herdr TUI panes as amp agents. Herdr detection then shows their state and sends done notifications. |
| [**sfc-gh-tmeacham/coco-herdr-plugin**](https://github.com/sfc-gh-tmeacham/coco-herdr-plugin) | 0 | Shows Cortex Code agent status in the Herdr TUI sidebar. |
| [**njs14/herdr-kiro-pulse**](https://github.com/njs14/herdr-kiro-pulse) | 0 | Reports Kiro CLI V3 sessions to the Herdr app and TUI as working, blocked, or done through OSC 7501 instead of showing idle. Distinguishes permission prompts and question panels. |
| [**cwkendall/amp-herdr**](https://github.com/cwkendall/amp-herdr) | 0 | Makes Amp report its thread state, approval prompts and titles directly to Herdr, and resumes Amp threads after a restart. Ships an Amp theme. |
| [**tlpinney/herdr-auggie**](https://github.com/tlpinney/herdr-auggie) | 0 | Makes Herdr TUI show Augment's Auggie CLI as working, idle or blocked, detects approvals and questions, shows session titles and resumes conversations after a restart. |
| [**frederikpietzko/herdr-plugin-junie**](https://github.com/frederikpietzko/herdr-plugin-junie) | 0 | Adds Junie CLI support to Herdr TUI through Junie hooks, so Junie panes show idle, working and blocked state, send notifications, and resume sessions. |

### Jcode status reporters

*4 projects. Several independent plugins that report Jcode agent sessions and lifecycle state to the Herdr sidebar.*

| Project | Stars | What it does |
|---|--:|---|
| [**leonardoacosta/herdr-jcode**](https://github.com/leonardoacosta/herdr-jcode) | 5 | Reports Jcode working and idle lifecycle states and session identity to Herdr TUI. |
| [**joeharris76/jcode-herdr**](https://github.com/joeharris76/jcode-herdr) | 1 | Registers jcode sessions in Herdr's agents sidebar with live working, idle, and blocked status and the session id for resume. Installs as a jcode hook script. |
| [**capt-marbles/herdr-jcode-integration**](https://github.com/capt-marbles/herdr-jcode-integration) | 0 | Reports Jcode session and lifecycle state to Herdr. |
| [**perorin0418/jcode-herdr-integration**](https://github.com/perorin0418/jcode-herdr-integration) | 0 | Reports jcode agent lifecycle states to the Herdr sidebar using hooks. |

### Status reporters for smaller and open-source agent CLIs

*12 projects. One-agent adapters for smaller and open-source coding CLIs such as Newt, OpenClaw, Letta, Muse, Kimchi and Polytoken that Herdr does not recognize on its own.*

| Project | Stars | What it does |
|---|--:|---|
| [**Gilamonster-Foundation/newt-agent · newt-tui/src/herdr**](https://github.com/Gilamonster-Foundation/newt-agent/tree/main/newt-tui/src/herdr) | 6 | Reports Newt coding-agent lifecycle states to the Herdr TUI from a pane using its socket API. |
| [**gejiliang/herdr-openclaw**](https://github.com/gejiliang/herdr-openclaw) | 5 | Treats OpenClaw TUI sessions as Herdr agents, with live state, model information, and token use in the sidebar. A background watcher parses OpenClaw status lines and reports them through the socket API. |
| [**klittle32/letta-herdr-mod**](https://github.com/klittle32/letta-herdr-mod) | 2 | Modifies Letta Code so sessions running in Herdr report accurate idle, working, and blocked states to the sidebar. |
| [**akshat12/herdr-muse**](https://github.com/akshat12/herdr-muse) | 2 | Reports Muse Code working, idle, and blocked states to Herdr TUI through lifecycle hooks. |
| [**getkimchi/herdr-kimchi**](https://github.com/getkimchi/herdr-kimchi) | 2 | Reports Kimchi agent state and session references to Herdr TUI for sidebar status and session restoration. |
| [**mrzzmrzz/herdr-opendde-harness**](https://github.com/mrzzmrzz/herdr-opendde-harness) | 1 | Shows a spinner, lifecycle state and short activity summary for ddeharness in the default Herdr TUI agent row. |
| [**sjennings/polytoken-herdr-core**](https://github.com/sjennings/polytoken-herdr-core) | 0 | Reports Polytoken session status to herdr-core through hooks and adds Polytoken to the Herdr app agent menu. Includes a pane mod to start or resume sessions and check the install. |
| [**hoon-ch/herdr-gjc-plugin**](https://github.com/hoon-ch/herdr-gjc-plugin) | 0 | Reports agent launch, exit, idle, working, and blocked states to Herdr. |
| [**tumf/conflux-herdr**](https://github.com/tumf/conflux-herdr) | 0 | Runs the Conflux TUI in a Herdr TUI pane and reports idle, working, and blocked states to the Agents list. |
| [**AlexandreAkao/herdr-bridge-compozy**](https://github.com/AlexandreAkao/herdr-bridge-compozy) | 0 | Displays headless CompozyOS agents as Herdr TUI agent rows by forwarding hook events to the socket API. |
| [**islee23520/herdr-omo-agent**](https://github.com/islee23520/herdr-omo-agent) | 0 | Registers OmO sessions as coding agents on stock Herdr TUI 0.8.2; the author’s OmO-native fork does not need this package. |
| [**ecklf/herdr-fx**](https://github.com/ecklf/herdr-fx) | 0 | Starts or resumes the fx coding agent in a Herdr TUI pane and shows when it is working or waiting for you. Hooks fx into Herdr notifications and restores saved fx sessions. |

### Telegram bots for agent alerts

*6 projects. Telegram bots that message you when a Herdr agent finishes or needs input, with the last output for context.*

| Project | Stars | What it does |
|---|--:|---|
| [**cokekitten/herdr-telegram-bridge**](https://github.com/cokekitten/herdr-telegram-bridge) | 4 | Sends Telegram notifications when an agent finishes or waits for input. Replies, including files, are delivered to the correct pane without requiring a public server or port tunnel. |
| [**naturalmoods/herdr-telegram-notify**](https://github.com/naturalmoods/herdr-telegram-notify) | 3 | Sends Telegram alerts when agents finish or need input and routes replies back to Herdr TUI or herdr-core agents. |
| [**elkraps/herdr-telegram-notify**](https://github.com/elkraps/herdr-telegram-notify) | 0 | Sends configurable Telegram alerts for Herdr TUI agent states, with templates, multiple destinations, and duplicate suppression. |
| [**jfortez/herdr-agent-alerts**](https://github.com/jfortez/herdr-agent-alerts) | 0 | Sends a Telegram message when a coding agent in Herdr TUI needs attention, with an extract of what the agent is asking and where to go. |
| [**wurthel/herdr-notifications**](https://github.com/wurthel/herdr-notifications) | 0 | Sends a Telegram message when an agent finishes or needs input, including your last prompt and the agent's last response. |
| [**OiAnthony/herdr-plugin-telegram-notify**](https://github.com/OiAnthony/herdr-plugin-telegram-notify) | 0 | Sends a Telegram message when a Herdr TUI agent is done or blocked. Bot token and chat ID come from the plugin config directory. |

### Telegram bots for remote commands and approvals

*6 projects. Telegram bots that let you list agents, send them text, start work and approve blocked prompts from your phone.*

| Project | Stars | What it does |
|---|--:|---|
| [**nhype/telegram-harness**](https://github.com/nhype/telegram-harness) | 4 | Runs Claude Code tasks from Telegram using Hermes Agent to manage Herdr TUI panes and status events. |
| [**etinpres/herdr-telegram-remote**](https://github.com/etinpres/herdr-telegram-remote) | 4 | Controls Codex and Claude Code panes in Herdr from Telegram. |
| [**TerrifiedBug/omp-telegram**](https://github.com/TerrifiedBug/omp-telegram) | 4 | Connects Oh My Pi sessions to Telegram and uses Herdr to spawn and manage sessions remotely. |
| [**hkdom/herdr-telegram-gate**](https://github.com/hkdom/herdr-telegram-gate) | 3 | Sends blocked Herdr agent approvals to Telegram and supports risk-tiered automatic approval policies. |
| [**amurru/herdr-whistle**](https://github.com/amurru/herdr-whistle) | 3 | Manages Herdr TUI agents from Telegram, including listing agents, reading output, sending text, and starting or closing panes. |
| [**cookiesmonster7926/herdr-telegram**](https://github.com/cookiesmonster7926/herdr-telegram) | 0 | Sends a Telegram message when a Herdr agent waits on you and lets you answer from your phone with buttons. Runs on macOS and Windows. |

### Telegram bridges that map agents to forum topics

*6 projects. Telegram bots that give each Herdr agent or pane its own forum topic for ongoing two-way conversation.*

| Project | Stars | What it does |
|---|--:|---|
| [**alexei-led/ccgram**](https://github.com/alexei-led/ccgram) | 289 | Maps forum topics to terminal windows running Claude Code, Codex, Gemini, Pi, or a shell. It relays output and input through Herdr or tmux so sessions remain usable from a phone. |
| [**permgps/herdr-telegram-agents**](https://github.com/permgps/herdr-telegram-agents) | 87 | Creates a Telegram forum topic for each Herdr agent so users can receive status updates and reply to prompts. |
| [**gaijinjoe/herdres**](https://github.com/gaijinjoe/herdres) | 7 | Maps every live Herdr pane to a Telegram forum topic. Agent activity appears in the topic, and bot commands can send input back to the matching pane from any device. |
| [**mvallebr/herdr-telegram-plugin**](https://github.com/mvallebr/herdr-telegram-plugin) | 6 | A Telegram bot companion that maps Herdr agents to forum topics and provides remote control without placing an LLM between the user and the pane. |
| [**vsem-azamat/herdr-telegram**](https://github.com/vsem-azamat/herdr-telegram) | 0 | Connects Telegram forum topics to stable Herdr agent sessions for ongoing remote conversations. |
| [**spancerxing/herdr-telegram-bridge**](https://github.com/spancerxing/herdr-telegram-bridge) | 0 | Lets you approve Claude Code, Codex, agy, and Pi agents from Telegram, with a topic per agent, approval buttons, a status dashboard, and completion notices. |

### Slack notifications and bots

*7 projects. Slack webhooks, DMs and bots that report agent status and let you answer prompts from Slack.*

| Project | Stars | What it does |
|---|--:|---|
| [**juninaba/herdr-slack-notify**](https://github.com/juninaba/herdr-slack-notify) | 1 | Sends Slack notifications when Herdr agents finish or become blocked. |
| [**timjonez/slack-herd**](https://github.com/timjonez/slack-herd) | 0 | Starts Herdr-backed work from Slack bot mentions through the herd and slackcli command-line tools. |
| [**egemenyildiz/herdr-slack**](https://github.com/egemenyildiz/herdr-slack) | 0 | Connects Slack to local Herdr agents so users can browse sessions, answer prompts, and launch agents without a tunnel. |
| [**dcieslak19973/herdr-slackr**](https://github.com/dcieslak19973/herdr-slackr) | 0 | Displays a real-time Slack feed inside a Herdr pane, using Socket Mode with polling as a fallback. |
| [**paper3300/herdr-slackbot**](https://github.com/paper3300/herdr-slackbot) | 0 | Sends Slack DMs when Claude Code or Codex agents in the Herdr app or Herdr TUI finish, with buttons to answer permission prompts. Lets you send prompts to agents from Slack. |
| [**mochikun/herdr-slack-notify**](https://github.com/mochikun/herdr-slack-notify) | 0 | Sends a Slack incoming-webhook message when a Herdr agent finishes or needs input. The README is in Japanese. |
| [**DylanG5/herdr-pi-slack-notify**](https://github.com/DylanG5/herdr-pi-slack-notify) | 0 | Sends a Slack Workflow webhook message when a finished Pi agent stays unseen past a configurable delay. Outbound only. |

### Discord and workplace-messenger bridges

*7 projects. Bridges that connect Discord, Mattermost, Teams, DingTalk, WeCom, WeChat or Feishu to Herdr agents.*

| Project | Stars | What it does |
|---|--:|---|
| [**wenxichang/herdr-pal**](https://github.com/wenxichang/herdr-pal) | 7 | Connects Herdr TUI agents across machines to a WeCom bot for session selection, task submission, terminal output, and limited key input. |
| [**hewenyu/herdr-agent**](https://github.com/hewenyu/herdr-agent) | 3 | An agent focused on managing Herdr and making development conversations easier from a phone. |
| [**fzf/herdr-mattermost**](https://github.com/fzf/herdr-mattermost) | 2 | Uses Mattermost as a front end for Herdr agents: each watched channel is a workspace, each root post starts an agent, and thread replies become prompts. Agent output and blocked or done status are relayed back into the thread. |
| [**ralphilius/herdr-discord**](https://github.com/ralphilius/herdr-discord) | 1 | Turns Discord channels into Herdr workspaces and threads into agent tabs, relaying agent output into the thread. Needs your own Discord bot token. |
| [**CurrenWong/herdr-dingtalk-omo-bridge**](https://github.com/CurrenWong/herdr-dingtalk-omo-bridge) | 0 | Connects DingTalk to an OmO coding agent in a Herdr pane. Types incoming messages into the session, posts the answer back and tags each message as received, done or error. |
| [**donghaolicd/herdr-teams-notify**](https://github.com/donghaolicd/herdr-teams-notify) | 0 | Sends bounded Microsoft Teams notifications for Herdr agent lifecycle events. |
| [**LuYanFCP/herdr-wechat-plugin**](https://github.com/LuYanFCP/herdr-wechat-plugin) | 0 | Controls Herdr TUI agents through WeChat, including status updates, prompts and permission responses. |

### Two-way chat bridges for several services

*7 projects. Bridges that connect Herdr panes to Telegram, Slack, Discord and other chat services so you can message agents and answer prompts away from the terminal.*

| Project | Stars | What it does |
|---|--:|---|
| [**natori-hrj/herdr-hail**](https://github.com/natori-hrj/herdr-hail) | 7 | Connects Herdr to Slack and Discord through a two-way webhook bridge. Blocked-agent alerts can be answered through replies or action buttons without opening a network tunnel. |
| [**lsisoft/herdr-telegram-slack-bridge**](https://github.com/lsisoft/herdr-telegram-slack-bridge) | 2 | Sends blocked-agent alerts to Telegram or Slack and routes replies to the originating Herdr TUI or tmux pane. |
| [**fulanto/herdr-oncall**](https://github.com/fulanto/herdr-oncall) | 1 | Surfaces blocked agent prompts in a macOS floating panel or Telegram and Feishu messages, allowing replies without returning to the pane. |
| [**SimonMallas/agent-letter-bridge**](https://github.com/SimonMallas/agent-letter-bridge) | 0 | Lets you message CLI agents from Telegram, Slack, or Discord, filing each message as a durable letter the agent reads. A Herdr adapter rings the agent pane and a popup shows status. |
| [**huketo/herdr-hitl**](https://github.com/huketo/herdr-hitl) | 0 | Blocks a Herdr coding agent on a human decision, delivered to your phone over Telegram or Discord. |
| [**atnine-ai/herdr-bridge**](https://github.com/atnine-ai/herdr-bridge) | 0 | Connects Herdr panes to chat services for communicating with agents outside the terminal. |
| [**muthuishere/herdr-conv-hooks**](https://github.com/muthuishere/herdr-conv-hooks) | 0 | Binds a chat conversation to an agent pane through one hook with create, listen, send, and stop verbs, so the agent answers messages without leaving its pane. |

### Alert routers that fan out to chat, push and webhooks

*5 projects. Tools that take Herdr agent notifications and route them, with rules and filters, to several chat, push, webhook or desktop destinations.*

| Project | Stars | What it does |
|---|--:|---|
| [**zgxme/herdr-webhook-notify**](https://github.com/zgxme/herdr-webhook-notify) | 3 | Forwards Herdr TUI agent notifications to chat services, ntfy or custom HTTP webhooks. |
| [**barnuri/herdr-notifications**](https://github.com/barnuri/herdr-notifications) | 1 | Sends Telegram, Discord, or Slack alerts when Herdr TUI agents become idle, blocked, or done, with per-status filters. |
| [**shindakun/goat-herdr**](https://github.com/shindakun/goat-herdr) | 1 | Sends an alert to Telegram, Discord, Slack, ntfy, Pushover, Pushbullet, a webhook or the desktop when a Herdr TUI agent is blocked or done. Lets you answer the agent from a Telegram thread. |
| [**pradyb/herdr-notify-router**](https://github.com/pradyb/herdr-notify-router) | 0 | Applies rules to Herdr agent notifications, such as alerting only after an agent stays blocked, and routes alerts to a webhook, ntfy or desktop with quiet hours and deduplication. |
| [**8liang/herdr-ai-notify**](https://github.com/8liang/herdr-ai-notify) | 0 | Forwards Herdr TUI agent done and blocked events to ai-cli-complete-notify so alerts go out over its webhook and other channels. |

### macOS notification banners

*9 projects. Native macOS notifications for Herdr agent events, most with the agent's last message and a click that jumps to the right pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**yankewei/herdr-focus-notify**](https://github.com/yankewei/herdr-focus-notify) | 34 | Shows a clickable macOS notification when an unseen pane becomes blocked or finishes. Clicking the alert brings the terminal forward and focuses the exact pane through `alerter`. |
| [**dot/herdr-terminal-notifier**](https://github.com/dot/herdr-terminal-notifier) | 13 | Bundles a branded macOS notification app so Herdr alerts use the correct icon and can jump to the relevant pane. The app periodically refreshes its Launch Services registration to recover cleanly after reboots or updates. |
| [**justinchiasson/herdr-nudge**](https://github.com/justinchiasson/herdr-nudge) | 6 | Sends clickable macOS notifications when an agent is blocked or done, or when a long zsh command finishes, and clicking one focuses that pane in Herdr. Works on Intel and Apple Silicon with nothing else to install, and withdraws notifications for panes that move on or close. |
| [**gAmUssA/herdr-notify**](https://github.com/gAmUssA/herdr-notify) | 0 | Shows one macOS banner when an agent finishes or needs input, and a click jumps to that exact pane even from a detached Herdr TUI session. Needs iTerm2. |
| [**varvand/herdr-plugin-mac-notify**](https://github.com/varvand/herdr-plugin-mac-notify) | 0 | Shows macOS Notification Center banners when a Herdr TUI agent finishes or needs input, and stays quiet when that pane is focused. |
| [**y-hirakaw/herdr-cc-mac-notify**](https://github.com/y-hirakaw/herdr-cc-mac-notify) | 0 | Sends macOS notifications for Claude Code panes in Herdr TUI with the agent’s latest message or question. |
| [**tdhuan/agent-notify**](https://github.com/tdhuan/agent-notify) | 0 | Sends desktop notifications for Claude Code permission requests and completed turns, with clicks focusing the matching Herdr pane. |
| [**retry19/herdr-agent-last-message-notify**](https://github.com/retry19/herdr-agent-last-message-notify) | 0 | Adds the agent's last message to the desktop notification when an agent finishes or waits for input in Herdr TUI. |
| [**liamwh/herdr-rich-notifications**](https://github.com/liamwh/herdr-rich-notifications) | 0 | Sends native desktop notifications for Herdr TUI agent status changes with context built from local metadata and a prompt excerpt. One click focuses the exact pane, with no LLM calls. |

### Windows and WSL toast notifications

*4 projects. Plugins that show native Windows 11 toasts for agents running locally or under WSL.*

| Project | Stars | What it does |
|---|--:|---|
| [**aclima01/herdr-notify-windows**](https://github.com/aclima01/herdr-notify-windows) | 4 | Sends native Windows 11 toast notifications when a Herdr agent finishes a turn or asks for input. |
| [**tkmct/herdr-wsl-notify**](https://github.com/tkmct/herdr-wsl-notify) | 3 | Adds a Herdr plugin that shows a Windows desktop toast when an agent (Claude Code, etc.) running under WSL2 becomes done (finished) or blocked (waiting for approval/input). |
| [**saeedrahimi/herdr-notify-wsl**](https://github.com/saeedrahimi/herdr-notify-wsl) | 1 | Converts Herdr lifecycle events inside WSL into native Windows 11 toast notifications by invoking PowerShell across the WSL boundary. |
| [**jaltez/agent-notify**](https://github.com/jaltez/agent-notify) | 0 | Monitors local and WSL Herdr sessions in a tray and sends popups, sounds, commands, or webhooks for agent events. |

### Cross-platform and remote-host desktop notifiers

*4 projects. Desktop notifiers that work across Linux, macOS and Windows or tell you which remote host needs attention.*

| Project | Stars | What it does |
|---|--:|---|
| [**A1exthegreat/herdr-agent-notify**](https://github.com/A1exthegreat/herdr-agent-notify) | 2 | Sends desktop notifications when agents finish, request confirmation, or become idle. |
| [**quinnjr/herdr-notifications**](https://github.com/quinnjr/herdr-notifications) | 1 | Sends native desktop notifications when Herdr agent states change on Linux, macOS, Windows, and BSD. |
| [**diegopzz/herdr-notify**](https://github.com/diegopzz/herdr-notify) | 0 | Sends desktop notifications for Herdr agents on local or remote machines, identifying the host that needs attention. |
| [**ivorpad/herdr-notify**](https://github.com/ivorpad/herdr-notify) | 0 | Notifies users when Herdr TUI agents need attention or finish and queues messages until agents can receive them. |

### Persistent popups, inboxes and screen cues for waiting agents

*6 projects. Desktop popups, notification inboxes, screen-edge glow, dock badges and terminal bell indicators outside the terminal that stay visible until you handle the waiting agent.*

| Project | Stars | What it does |
|---|--:|---|
| [**DevooKim/herdr-glow**](https://github.com/DevooKim/herdr-glow) | 2 | Makes the screen edge glow on macOS when a Herdr agent is blocked, across every space, monitor and fullscreen app without taking focus. The glow returns after 30 seconds of inactivity and stops when you type. |
| [**ram4-dev/herdr-notify-center**](https://github.com/ram4-dev/herdr-notify-center) | 0 | Stores notifications from all workspaces in a durable popup inbox. Items can be reviewed, opened in their related pane, cleared when resolved, and retained across restarts. |
| [**1smil1/herdr-done-popup**](https://github.com/1smil1/herdr-done-popup) | 0 | Shows a persistent desktop popup when a Herdr TUI agent finishes or asks a question. |
| [**recordplane/herdr-pendingyou**](https://github.com/recordplane/herdr-pendingyou) | 0 | Shows on each agent's sidebar row what it is waiting on you for and toasts new questions. Answers cards from a popup through the Pending You service. |
| [**Rockheung/herdr-kaku-bell**](https://github.com/Rockheung/herdr-kaku-bell) | 0 | Displays visual bell indicators in Kaku tabs when Herdr agents await human input. |
| [**suleymanyaryev/herdr-ghostty-badge**](https://github.com/suleymanyaryev/herdr-ghostty-badge) | 0 | Rings the bell for Ghostty's dock badge when a Herdr agent is blocked or done, and shows the waiting count in the window title on macOS. |

### Agent-done sounds and sound packs

*9 projects. Plugins that play sounds, per-space tunes or whole sound packs when agents finish or get blocked.*

| Project | Stars | What it does |
|---|--:|---|
| [**ChrisPachulski/session-sounds**](https://github.com/ChrisPachulski/session-sounds) | 3 | Plays distinct per-session sounds for Herdr TUI agent attention and completion on macOS and Linux. |
| [**gridness/herdr-random-sounds**](https://github.com/gridness/herdr-random-sounds) | 1 | Plays random local macOS sounds when Herdr TUI agents need input or finish tasks. |
| [**WebscapeOrg/medley**](https://github.com/WebscapeOrg/medley) | 1 | Lets you pick an audio file per Herdr workspace and status from an imported MP3 or WAV library. Previews sounds and replaces Herdr's native sounds. |
| [**ariel-ps/herdr-alerts**](https://github.com/ariel-ps/herdr-alerts) | 1 | Plays a sound and flashes the affected pane when a Herdr agent finishes or becomes blocked. Includes a Rust CLI and TUI to preview alerts, download sound packs, and pick sounds per project and branch. |
| [**KevinEdry/herdr-pion-ping**](https://github.com/KevinEdry/herdr-pion-ping) | 0 | Plays your active Peon Ping sound pack for Herdr agent status events instead of Herdr's built-in sounds. Bundles no audio. |
| [**joehahndev/herdfxr**](https://github.com/joehahndev/herdfxr) | 0 | Plays alert sounds when an agent finishes or needs input, with different sounds per space, and includes a terminal sfxr designer for making them. Also ships event-probe, which logs event hook payloads for plugin authors. |
| [**RaulAlvaro/herdr-space-sounds**](https://github.com/RaulAlvaro/herdr-space-sounds) | 0 | Plays a distinct macOS sound pair per Herdr TUI space, with sounds for blocked agents and finished background spaces, so you can tell which project needs attention. |
| [**WorksOnMyVM/herdr-sounds**](https://github.com/WorksOnMyVM/herdr-sounds) | 0 | Discovers, previews, installs, and switches Herdr notification sound packs. |
| [**michiomochi/herdr-sound-toggle**](https://github.com/michiomochi/herdr-sound-toggle) | 0 | Adds a persistent Herdr TUI workspace pane for viewing and toggling sound notifications. |

### Spoken summaries and text-to-speech alerts

*6 projects. Plugins that read agent recaps or selected terminal text aloud with local or cloud text-to-speech.*

| Project | Stars | What it does |
|---|--:|---|
| [**nhclink16/herdr-announcer**](https://github.com/nhclink16/herdr-announcer) | 5 | Speaks a one-sentence AI summary when an agent finishes or needs input. It supports local text-to-speech, ElevenLabs, or any custom command. |
| [**Aktrov/herdr-tts**](https://github.com/Aktrov/herdr-tts) | 2 | Speaks selected terminal text aloud using Piper neural text-to-speech engines with keyboard controls. |
| [**HikaruEgashira/say-hook**](https://github.com/HikaruEgashira/say-hook) | 1 | Reads a one-line status summary aloud when an agent becomes done or blocked, using ElevenLabs or macOS speech through a Herdr state-change hook. |
| [**zetlen/herdr-bleatr**](https://github.com/zetlen/herdr-bleatr) | 0 | Speaks a one-sentence notification aloud when an agent in another Herdr TUI tab finishes or needs approval. Uses macOS say or espeak, with an optional Claude or Codex summary. |
| [**jjeff/herdr-speak**](https://github.com/jjeff/herdr-speak) | 0 | Speaks a one-line recap when a coding agent finishes a turn, including agents on saved SSH machines. Pairs a speak skill with a background speaker on macOS, Linux, or Windows. |
| [**Drozerah/herdr-voice**](https://github.com/Drozerah/herdr-voice) | 0 | Adds early-stage text-to-speech audio feedback for agents working in Herdr TUI panes. |

### Phone push alerts through ntfy

*6 projects. Plugins that send agent-done and blocked alerts to your phone through ntfy topics.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**horn553/herdr-ntfy**](https://github.com/horn553/herdr-ntfy) | 9 | Sends ntfy alerts for done and blocked agent states using standard command-line tools and curl. |
| [**zom-2018/herdr-ntfy-notify**](https://github.com/zom-2018/herdr-ntfy-notify) | 8 | Sends structured ntfy alerts when an agent blocks or finishes. Notifications include the workspace, tab, and pane, and the plugin prefers a detected local ntfy server before using the network. |
| [**jjuraszek/herdr-ntfy-notify**](https://github.com/jjuraszek/herdr-ntfy-notify) | 1 | Pushes an ntfy notification to your phone when a Herdr TUI agent goes blocked or done. Runs from an event hook with no daemon. |
| [**gkzhb/herdr-plugins**](https://github.com/gkzhb/herdr-plugins) | 0 | Sends an ntfy notification when a Herdr agent finishes a turn, with the terminal title, tab, and a summary of the latest Pi reply. The monorepo also holds a standalone Pi ntfy package. |
| [**devicki/herdr-pager**](https://github.com/devicki/herdr-pager) | 0 | Sends ntfy push notifications when an agent finishes or needs an answer, and when a command, script, or scheduled job ends. Each message names the pane to jump back to. |
| [**Argon-Sky/herdr-afk-notify**](https://github.com/Argon-Sky/herdr-afk-notify) | 0 | Sends an ntfy push notification when a Herdr TUI agent finishes a long turn or needs input, only while you are away from the keyboard. |

### Phone push through Gotify, Bark and iPhone companion apps

*5 projects. Plugins that push agent alerts to your phone through Gotify, Bark or a dedicated iPhone and iPad companion app.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**kaikidd/herdr-bark-notify**](https://github.com/kaikidd/herdr-bark-notify) | 1 | Sends a Bark push notification to your iPhone when a Herdr agent finishes or needs input, naming the agent, workspace, and pane. Needs no daemon or npm dependencies. |
| [**algorist-dev/herdr-crook**](https://github.com/algorist-dev/herdr-crook) | 1 | Connects Herdr to the Crook iPhone and iPad app so you can see your agents and answer them with one tap. English and Japanese docs. |
| [**8liang/herdr-gotify**](https://github.com/8liang/herdr-gotify) | 0 | Pushes a Gotify notification to your phone when a Herdr TUI agent becomes blocked or done, optionally with an LLM-written one-sentence summary of the pane output. |
| [**keinstn/drover-notify**](https://github.com/keinstn/drover-notify) | 0 | Sends a push alert to the Drover iOS app when a Herdr agent becomes blocked. It uses built-in Node.js features only and stores encrypted pairing information locally. |
| [**AG-Studio-Apps/meshterm-herdr-ios**](https://github.com/AG-Studio-Apps/meshterm-herdr-ios) | 0 | Sends a push alert to the meshTerm iPhone and iPad app when a Herdr agent needs approval or finishes a turn. Only an anonymous ping with the agent name leaves the computer, never screen text. |

### Webhook, email and hosted-push notifiers

*10 projects. Notifiers that post agent events to webhooks, email, Firebase or Ably so another service can react.*

| Project | Stars | What it does |
|---|--:|---|
| [**happyeric77/agent-webhook-notify**](https://github.com/happyeric77/agent-webhook-notify) | 3 | Posts structured HTTP webhooks when agents block or finish. Payloads can include workspace and pane details, model information, and recent scrollback for use in Slack, Discord, or mobile-alert systems. |
| [**tiny-send/tinysend-herdr**](https://github.com/tiny-send/tinysend-herdr) | 1 | Emails a one-line summary when an agent blocks, finishes, or fails. Replying to the message sends input to the correct pane, making an email client a simple remote approval interface. |
| [**jefflau/herdr-webhook**](https://github.com/jefflau/herdr-webhook) | 0 | Posts Herdr TUI agent done and blocked events as JSON to a configurable webhook. |
| [**advaitbd/herdr-notify**](https://github.com/advaitbd/herdr-notify) | 0 | Sends Herdr agent-status notifications through signed Hermes webhooks. |
| [**weskor/nudge**](https://github.com/weskor/nudge) | 0 | Sends a webhook event when agents finish or get blocked and delivers the reply into the agent's pane. Rate-limits, skips the focused pane, and redacts secrets. |
| [**zeke1031031/herdr-grokbot-notify**](https://github.com/zeke1031031/herdr-grokbot-notify) | 0 | Wakes a Grok Bot routine by webhook when any coding agent detected by the Herdr TUI finishes or needs you. |
| [**devicki/herdr-away-signal**](https://github.com/devicki/herdr-away-signal) | 0 | Adds an away mode toggled by a key that POSTs to a webhook when an agent finishes or waits for you, so a bot or orchestrator does not have to poll. |
| [**znohat/herdr-ttyd-ably**](https://github.com/znohat/herdr-ttyd-ably) | 0 | Publishes Herdr TUI agent status changes to an Ably channel so a custom ttyd build can show desktop notifications in the browser. |
| [**znohat/ttyd**](https://github.com/znohat/ttyd) | 0 | Builds a ttyd fork with an --ably-notify option that shows Herdr agent done, idle and blocked events as browser notifications. Pairs with the herdr-ttyd-ably plugin that publishes the events to an Ably channel. |
| [**zerkc/herdr-notify-firebase**](https://github.com/zerkc/herdr-notify-firebase) | 0 | Sends Firebase Cloud Messaging push notifications when Herdr agent status changes. |

### Telemetry exporters and presence feeds

*10 projects. Plugins that stream Herdr activity to external systems such as OpenTelemetry, NDJSON endpoints, ActivityWatch, tracing services and Discord Rich Presence.*

| Project | Stars | What it does |
|---|--:|---|
| [**DIodide/herdr-telemetry**](https://github.com/DIodide/herdr-telemetry) | 12 | Sends workspace and agent telemetry to an endpoint chosen by the user. It removes tokens, redacts sensitive prompts, and ships as a single binary. |
| [**ryonakae/shepherd**](https://github.com/ryonakae/shepherd) | 11 | A worker-observability service and set of runtime bridges for coding agents managed by Herdr. |
| [**revanp/herdr-discord-presence**](https://github.com/revanp/herdr-discord-presence) | 3 | Publishes the active Herdr project, current agent, and total active-agent count through Discord Rich Presence using a local RPC service, with no bot or external server required. |
| [**CodyBontecou/herdr-telemetry-bridge**](https://github.com/CodyBontecou/herdr-telemetry-bridge) | 2 | Streams structured Herdr activity as NDJSON, including pane focus time, detected agent and model details, and local session summaries. Output can go to a file, webhook, or command, and transcript text is hidden by default. |
| [**jakobbeyer/herdr-kharka**](https://github.com/jakobbeyer/herdr-kharka) | 2 | Writes what a machine's Herdr runs into kharka on every change by following Herdr's event stream. Lets any tool read agents from all machines through a local replica. |
| [**nabutabu/herdr-observr**](https://github.com/nabutabu/herdr-observr) | 1 | Exports Herdr TUI agent runtime health, wait times, concurrency, usage, and costs through OpenTelemetry. |
| [**Dolliwyx/herdr-rpc**](https://github.com/Dolliwyx/herdr-rpc) | 1 | Publishes the focused Herdr workspace and agent counts to Discord Rich Presence from a Windows WSL2 setup. |
| [**simensollie/aw-watcher-herdr**](https://github.com/simensollie/aw-watcher-herdr) | 0 | Records focused Herdr workspaces and concurrent agent activity in ActivityWatch on macOS, for both the Herdr app and Herdr TUI. |
| [**jaredlyon/herdr-respan-adapter**](https://github.com/jaredlyon/herdr-respan-adapter) | 0 | Traces CLI coding agents running in Herdr TUI to Respan through one Rust binary with redaction, spooling, and OTLP export. |
| [**AgentTeamsRun/herdr**](https://github.com/AgentTeamsRun/herdr) | 0 | Reports Herdr TUI worktree creation and removal to the AgentTeams registry. |

### Standalone dashboards for agent time, cost and session health

*8 projects. Dashboards and analyzers outside the Herdr window that show what agents cost, how they spent their time and how healthy your running sessions are.*

| Project | Stars | What it does |
|---|--:|---|
| [**winoooops/herdr-agent-watcher**](https://github.com/winoooops/herdr-agent-watcher) | 6 | Adds live sidebar cards, lifecycle alerts, and a zero-configuration Claude Code metrics bridge for Herdr agents. |
| [**vishnutskumar/herdr-memex-analytics**](https://github.com/vishnutskumar/herdr-memex-analytics) | 2 | Analyzes memex session history and shows efficiency guidance for Herdr TUI agents. |
| [**cpcloud/herdr-agentsview**](https://github.com/cpcloud/herdr-agentsview) | 2 | Combines active AgentsView sessions across projects, models, and agents, with real-time timelines and metrics inside Herdr. |
| [**naturalmoods/herdr-burnlog**](https://github.com/naturalmoods/herdr-burnlog) | 2 | Records token usage and recorded cost per project for Herdr-managed Codex, Claude Code and Pi agents in a local SQLite database, with CLI reports and popup panes. |
| [**mcc0x/herdr-standup**](https://github.com/mcc0x/herdr-standup) | 1 | Generates summaries of agent activity across Herdr workspaces over time, including commits, diff volume, and branches. |
| [**neospeed83/herdr-replay**](https://github.com/neospeed83/herdr-replay) | 1 | Records and replay multi-agent Herdr coding sessions as interactive timelines. |
| [**OSHEThai/HerdrOps**](https://github.com/OSHEThai/HerdrOps) | 0 | Monitors desktop operations for Herdr terminal agents on Windows. |
| [**peria-ai/precc-herdr-plugin**](https://github.com/peria-ai/precc-herdr-plugin) | 0 | Shows PRECC token-savings telemetry in Herdr panes and runs PRECC setup and diagnostics. |

### Speech-to-text dictation into panes

*10 projects. Local or cloud dictation plugins that type your speech into the focused Herdr pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**T0mSIlver/localvoxtral**](https://github.com/T0mSIlver/localvoxtral) | 64 | Fully local, real-time dictation for Apple Silicon Macs. It streams speech into the coding-agent session under the cursor, including Claude Code inside a Herdr pane, and uses that session as context for optional text polishing. |
| [**RanolP/herdr-handsfree**](https://github.com/RanolP/herdr-handsfree) | 2 | Adds on-device voice dictation and webcam gaze-based cursor movement to Herdr TUI on Apple Silicon Macs. |
| [**xtwist/herdr-stt**](https://github.com/xtwist/herdr-stt) | 2 | Dictates into the pane where recording started, using a local PipeWire recorder and a faster-whisper worker, with an optional repo-aware text corrector. Linux only. |
| [**aliaksandr-haurylau-godel/herdr-voice**](https://github.com/aliaksandr-haurylau-godel/herdr-voice) | 1 | Transcribes held-key voice dictation into the focused Herdr TUI agent input, with context-aware rewriting and selectable speech engines. |
| [**abhishekrana/herdr-dictate**](https://github.com/abhishekrana/herdr-dictate) | 1 | Types local speech-to-text dictation into the focused Herdr pane while you talk. Transcription runs on the machine and audio is not sent out. |
| [**razajamil/herdr-hex-browser-voice-command**](https://github.com/razajamil/herdr-hex-browser-voice-command) | 1 | A Chrome extension and local service that sends Hex voice transcripts to the correct Herdr pane based on the browser URL that was focused while speaking. URL patterns are mapped to workspace, tab, and pane targets. |
| [**ricardofelixb/herdr-codex-voice**](https://github.com/ricardofelixb/herdr-codex-voice) | 1 | Lets Codex native /voice in a Herdr remote pane use the microphone and speakers of the computer you sit at, over SSH and Tailscale. Experimental preview. |
| [**calebcauthon/herdr-riff-relay**](https://github.com/calebcauthon/herdr-riff-relay) | 0 | Sends Riff dictation to a chosen Herdr TUI agent pane using hotkeys. |
| [**SebCos94/herdr-dictate**](https://github.com/SebCos94/herdr-dictate) | 0 | Records speech into any Herdr TUI pane with a live transcript from local whisper.cpp, then types the text on Enter. Runs on Linux, macOS, and Windows and sends no audio off the machine. |
| [**eoinest/convo-history**](https://github.com/eoinest/convo-history) | 0 | Turns a recent window of speech into a Codex prompt in a fresh Herdr TUI worktree, triggered by a hotkey or wake word. |

### Voice assistants and spoken commands at your desk

*6 projects. Voice agents and spoken-command tools for talking to Herdr agents and navigating panes by voice.*

| Project | Stars | What it does |
|---|--:|---|
| [**brogrammerMW/herdr-voice**](https://github.com/brogrammerMW/herdr-voice) | 32 | Lets users speak to agents in Herdr TUI panes and hear replies using local OpenLive or realtime xAI, OpenAI, and Google models. |
| [**aneym/herdr-voice**](https://github.com/aneym/herdr-voice) | 5 | Controls workspaces, pane splits, and agent dispatch with spoken commands through OpenAI's Realtime API. A floating display shows the transcription and asks for confirmation before sending instructions. |
| [**kvm404/Auren · src/auren/hands/herdr.py**](https://github.com/kvm404/Auren/blob/main/src/auren/hands/herdr.py) | 4 | Starts Herdr coding agents through the Auren voice assistant on Omarchy. |
| [**shanev/herdr-voice**](https://github.com/shanev/herdr-voice) | 1 | Lets you start, ask about, and stop Herdr agents by voice through Hermes or the Vux agent. Ships skills for the Herdr TUI and herdr-core plus a desk-alerts plugin. |
| [**shadowfax92/herdr-talon**](https://github.com/shadowfax92/herdr-talon) | 1 | Adds spoken Talon labels to visible Herdr targets for hands-free movement between panes. |
| [**amodi20/herdr-voice-router**](https://github.com/amodi20/herdr-voice-router) | 0 | Routes a prompt to another Herdr TUI pane when you say that pane's name, working with typed text or any dictation tool. Ships a Claude Code hook alongside the Herdr plugin. |

### Phone calls and phone-based voice control for agents

*6 projects. Tools that let you call agents, get called when one is blocked, or talk to them from an iPhone app, web app or Action Button.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | Stars | What it does |
|---|--:|---|
| [**klarluft/pitupitu**](https://github.com/klarluft/pitupitu) | 223 | Connects phone and browser voice conversations to coding agents running in Herdr TUI. |
| [**kccarlos/herdr-sheepdog**](https://github.com/kccarlos/herdr-sheepdog) | 15 | Monitors and steers Herdr agents by voice from an iPhone app or a Herdr app layout and panel. |
| [**Vercantez/herdr-voice**](https://github.com/Vercantez/herdr-voice) | 4 | Connects an installable iPhone web app to Herdr through a private voice gateway using OpenAI Realtime over WebRTC. |
| [**jonesy827/mate**](https://github.com/jonesy827/mate) | 2 | Controls a Herdr fleet by phone call to start agents, send tasks, check status, and hear Claude Code or Codex replies. |
| [**freewillythe4th/action-button-agent**](https://github.com/freewillythe4th/action-button-agent) | 2 | Connects an iPhone Action Button to personal Herdr agents. Voice input passes through an iOS Shortcut, Tailscale, Telegram, and a Claude Agent SDK operator, which starts or targets a Herdr session and returns the response. |
| [**radres/herdr-plugin-call-me**](https://github.com/radres/herdr-plugin-call-me) | 1 | Calls your phone when a Herdr agent is blocked, reads the question aloud, and sends your spoken answer as a keypress. |

### Remote access over SSH, Tailscale and QUIC

*9 projects. Transports and tab helpers that attach remote Herdr machines and sessions to your local Herdr.*

| Project | Stars | What it does |
|---|--:|---|
| [**Mic92/herdr-eternal**](https://github.com/Mic92/herdr-eternal) | 13 | A roaming-friendly transport for `herdr --remote` using QUIC with a WebSocket fallback, exact byte-stream resumption, and OIDC authentication. |
| [**Poor-Plebs/herdr-remote-panes**](https://github.com/Poor-Plebs/herdr-remote-panes) | 7 | Opens SSH terminals for hosts from SSH configuration in separate Herdr TUI workspaces. |
| [**hackerchai/herdr-relay**](https://github.com/hackerchai/herdr-relay) | 5 | Shares Herdr TUI sessions with another computer using encrypted pairing over a LAN, tailnet, or relay. |
| [**Luisalt20/herdr-reach**](https://github.com/Luisalt20/herdr-reach) | 2 | Runs a read-only doctor that measures what your network allows to a remote machine and recommends an SSH transport for Herdr with evidence. Only the doctor command is shipped so far. |
| [**TolemyW/bash-screen**](https://github.com/TolemyW/bash-screen) | 0 | Lets an agent operate GUI apps on a remote Linux host over SSH, with a live preview pane in Herdr. Reads the accessibility tree and falls back to screenshots. |
| [**hisetu/pi-herdr-remote**](https://github.com/hisetu/pi-herdr-remote) | 0 | Pi-native tools for operating Herdr servers on explicitly approved SSH hosts. |
| [**alex-devdone/herdr-remote-agent-watch**](https://github.com/alex-devdone/herdr-remote-agent-watch) | 0 | Shows a Claude session running behind SSH and tmux as a live Herdr sidebar agent. It also provides more resilient SSH and remote-Herdr wrapper commands. |
| [**trillium/herdr-tailscale**](https://github.com/trillium/herdr-tailscale) | 0 | Automatically attaches trusted Tailscale peers to Herdr as remote tabs. |
| [**stfl/herdr-bridge**](https://github.com/stfl/herdr-bridge) | 0 | Shows a remote herdr agent inside a local herdr pane, one sidebar, several machines. |

### Remote port forwarding, link opening and file transfer

*10 projects. Helpers that forward ports, open links, move files or operate GUIs between a remote Herdr host and your local machine.*

| Project | Stars | What it does |
|---|--:|---|
| [**go-min/herdr-fwd**](https://github.com/go-min/herdr-fwd) | 6 | Automatically maintains loopback port forwarding between a remote Herdr session and the local machine, making services started by remote agents available without manual SSH tunnels. |
| [**miko-misa/herdr-portfwd**](https://github.com/miko-misa/herdr-portfwd) | 5 | Forwards remote agent development-server ports to the local machine and opens them after confirmation. |
| [**kosuketut/herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder) | 5 | Downloads files created or changed in a remote Herdr pane to a local Mac. A plugin action detects paths in the active pane and transfers the selected artifact over the remote connection. |
| [**mrolafsson/herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer) | 5 | Transfers files between a local machine and a remote Herdr TUI host over SSH and sends their paths to agents. |
| [**wavrin/herdr-ferry**](https://github.com/wavrin/herdr-ferry) | 4 | Moves files and clipboard between the Herdr box and your laptop over SSH, no cloud bucket. |
| [**randomradio/herdr-ports**](https://github.com/randomradio/herdr-ports) | 2 | Forwards a port from a remote Herdr workspace to `http://herdr.{workspace}.localhost:{port}` on your laptop through SSH tunnels, using saved Herdr machines. |
| [**bhoov/herdr-port-forwarder**](https://github.com/bhoov/herdr-port-forwarder) | 1 | Forwards loopback ports printed by panes on saved SSH machines to your local computer and shows the forwarded ports in the Herdr TUI sidebar. |
| [**jeffhuen/tether-browser**](https://github.com/jeffhuen/tether-browser) | 1 | Bridges a remote agent to the Chrome on your workstation so ctrl+click on a URL in a Herdr pane opens it in your local browser. Also works across tmux and SSH sessions. |
| [**kujjwal02/bifrost**](https://github.com/kujjwal02/bifrost) | 0 | Opens dev servers, links and files from agents on remote machines in the local browser, using the SSH details Herdr already has. Needs no server, account or VPN. |
| [**Gol-D-Rogger/herdr-code-server-clipboard**](https://github.com/Gol-D-Rogger/herdr-code-server-clipboard) | 0 | Forwards Herdr selections to the code-server browser clipboard on macOS. |

### Browser selections, notes and photos sent to agents

*4 projects. Tools that capture page elements, notes or webcam photos and deliver them to an agent pane.*

| Project | Stars | What it does |
|---|--:|---|
| [**rchougule/herdr-cam**](https://github.com/rchougule/herdr-cam) | 2 | Opens your webcam from Herdr with one key so you can photograph paper sketches or notes and send the photos into your coding agent's prompt as images. macOS only, with a Swift camera app. |
| [**scaccogatto/vite-plugin-herdr**](https://github.com/scaccogatto/vite-plugin-herdr) | 0 | Sends a selected browser element and prompt from a Vite app to a Herdr coding agent. |
| [**genexk/anynotate · integrations/herdr**](https://github.com/genexk/anynotate/tree/main/integrations/herdr) | 0 | Sends browser notes made with Anynotate to a Herdr TUI agent pane through an inbox popup or a one-key send of the latest note. |
| [**LuisBDev/herdrop**](https://github.com/LuisBDev/herdrop) | 0 | Lets you pick elements on a web page in Chrome, add notes and send them to a coding agent in a Herdr pane as a Markdown bundle. Pairs a Chrome extension with a Rust bridge plugin. |

### Warp terminal integrations

*4 projects. Plugins that connect Herdr agents with the Warp terminal: native panes, notifications and the Warp agent CLI.*

| Project | Stars | What it does |
|---|--:|---|
| [**HexSleeves/herdr-warp**](https://github.com/HexSleeves/herdr-warp) | 9 | Opens live Herdr TUI agents as native Warp panes on macOS. |
| [**ProjectAJ14/herdr-warp**](https://github.com/ProjectAJ14/herdr-warp) | 3 | Sends Warp desktop notifications when a Herdr-managed agent finishes or needs attention. |
| [**cdpath/herdr-warp**](https://github.com/cdpath/herdr-warp) | 0 | Integrates the Warp Agent CLI with Herdr. It can send prompts, wait for output, approve or reject actions, and infer idle, working, and blocked status from terminal output. |
| [**rubenbelem/warp-herdr-notifications**](https://github.com/rubenbelem/warp-herdr-notifications) | 0 | Sends clickable macOS notifications for Herdr agents running in Warp, and a click focuses the exact Warp tab and agent pane. |

### cmux integrations

*5 projects. Plugins that mirror Herdr agents, status and working directory into the cmux terminal app.*

| Project | Stars | What it does |
|---|--:|---|
| [**RaviTharuma/cmux-herdr**](https://github.com/RaviTharuma/cmux-herdr) | 16 | Shows Herdr TUI pane viewers and agent status pills inside cmux using external attachment. |
| [**lachieh/herdr-plugin-cmux**](https://github.com/lachieh/herdr-plugin-cmux) | 11 | Mirrors Herdr TUI agents into the cmux sidebar with status, task text, and click-to-focus navigation. |
| [**tomoya55/cmux-herdr**](https://github.com/tomoya55/cmux-herdr) | 0 | Propagates agent status (working / waiting for input / finished) to the cmux sidebar. |
| [**linvald/herdr-cmux-file-viewer**](https://github.com/linvald/herdr-cmux-file-viewer) | 0 | Syncs cmux's file viewer to the currently focused herdr space. |
| [**WerrySs/herdr-cmux-cwd-sync**](https://github.com/WerrySs/herdr-cmux-cwd-sync) | 0 | Keeps cmux's graphical file explorer synchronized with the current directory of the focused Herdr pane by listening to focus events without modifying shell sessions. |

### tmux plugins with Herdr agent detection

*5 projects. Tmux plugins that bring Herdr-style agent detection, sidebars and orchestration to tmux sessions.*

| Project | Stars | What it does |
|---|--:|---|
| [**27medkamal/tmux-agent-wizard**](https://github.com/27medkamal/tmux-agent-wizard) | 21 | Brings Herdr agent detection and compatible CLI-driven plugins to tmux. |
| [**zhaoyuheng200/tmux-agent-herd**](https://github.com/zhaoyuheng200/tmux-agent-herd) | 1 | Provides tmux plugin: detect coding-agent status (working/blocked/idle) per pane, notify on blocked, jump between agents. Detection ported from herdr. |
| [**maoxiaoke/tmux-agents**](https://github.com/maoxiaoke/tmux-agents) | 0 | Displays live agent states in tmux status bars with hotkey jumping for Claude Code sessions. |
| [**sandiiarov/tmux-agent-plugin**](https://github.com/sandiiarov/tmux-agent-plugin) | 0 | Provides tmux plugin for a Herdr-like AI agent sidebar. |
| [**ardubev16/tmux-herdr**](https://github.com/ardubev16/tmux-herdr) | 0 | Adds a Tmux plugin that uses Herdr to manage, aggregate and orchestrate AI Agents. |
