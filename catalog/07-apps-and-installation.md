# Awesome Herdr: Apps, companion integrations, and installation

The full list for domain 7 of [Awesome Herdr](../README.md#7-apps-companion-integrations-and-installation), ordered by GitHub stars.

- [Native desktop and mobile apps (126)](#native-desktop-and-mobile-apps)
- [Web dashboards and remote viewers (127)](#web-dashboards-and-remote-viewers)
- [Hardware and ambient displays (47)](#hardware-and-ambient-displays)
- [Processes, ports, sandboxes, and remote machines (28)](#processes-ports-sandboxes-and-remote-machines)
- [Agent support, auto-approve, retry, and keep-awake helpers (20)](#agent-support-auto-approve-retry-and-keep-awake-helpers)
- [Notes, prompts, clipboard, and file helpers (32)](#notes-prompts-clipboard-and-file-helpers)
- [Developer tool panes and everyday utilities (56)](#developer-tool-panes-and-everyday-utilities)
- [Setup, packages, and version management (55)](#setup-packages-and-version-management)

---

## 7. Apps, companion integrations, and installation

*491 projects. Native applications, web dashboards, hardware companions, supporting utilities, and setup packages.*

### Native desktop and mobile apps

*126 projects. Installed applications and launchers that provide a native interface to Herdr on desktop or mobile operating systems.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | What it does |
|---|---|
| [**sheprd-labs/sheprd**](https://github.com/sheprd-labs/sheprd) | Opens Herdr TUI and herdr-core terminal sessions in a native desktop client. |
| [**ZingerLittleBee/Heeler**](https://github.com/ZingerLittleBee/Heeler) | Supervises Herdr agents from an iOS console with SSH terminals, QR pairing, and push notifications. |
| [**missuo/herdrm**](https://github.com/missuo/herdrm) | Adds a native macOS console for Herdr to drive coding agents and monitor live terminals across devices. |
| [**themartianapp/herdrup**](https://github.com/themartianapp/herdrup) | Monitors Herdr TUI agents and opens their terminals from an iOS app. |
| [**kosumic/whip**](https://github.com/kosumic/whip) | Connects mobile devices to Herdr as an agent-native SSH client designed specifically for multiplexer workflows. |
| [**kenn-io/ghosthub**](https://github.com/kenn-io/ghosthub) | Opens local and SSH-hosted Herdr TUI, tmux, and Zellij sessions in a native macOS terminal with worktree creation. |
| [**benkraus/herdr-mobile**](https://github.com/benkraus/herdr-mobile) | Controls Herdr TUI sessions from iOS or Android through a separately deployed relay. |
| [**cobanov/herdrchat**](https://github.com/cobanov/herdrchat) | Controls Herdr coding agents from an iPhone or iPad. |
| [**minchenlee/flockbook**](https://github.com/minchenlee/flockbook) | Shows agent conversations in a native macOS app or Herdr app layout and lets users answer prompts. |
| [**sisyphuslabs/doriterm**](https://github.com/sisyphuslabs/doriterm) | Connects desktop, browser and phone clients to herdr-core terminals across an encrypted machine mesh. |
| [**JoseValencia125/agents-pixel-dungeon**](https://github.com/JoseValencia125/agents-pixel-dungeon) | Displays Herdr agents as interactive pixel-art dungeon characters on desktop and lets users answer prompts. |
| [**Ozymandes/TENDRIL**](https://github.com/Ozymandes/TENDRIL) | Controls persistent Herdr sessions from an Android device with Tailscale, Mosh, and agent notifications. |
| [**tuan3w/herdr-mobile**](https://github.com/tuan3w/herdr-mobile) | Monitors and answers Herdr agents across machines from an Android client connected over SSH. |
| [**DanielOu1208/agentslate**](https://github.com/DanielOu1208/agentslate) | Supervises Herdr coding agents from an iPhone keypad over Tailscale. |
| [**weekitmo/herdr-pocket**](https://github.com/weekitmo/herdr-pocket) | Monitors Herdr agents and opens their terminals from a Flutter client over SSH on mobile and desktop. |
| [**undivisible/herdr-gui**](https://github.com/undivisible/herdr-gui) | Renders Herdr TUI sessions and an embedded terminal in a native macOS GPUI client. |
| [**buldezir/Herdglass**](https://github.com/buldezir/Herdglass) | Connects to remote Herdr servers from a native macOS interface with a GPU-accelerated terminal and session status drawer. |
| [**paulmillr/dispatch**](https://github.com/paulmillr/dispatch) | Maps Herdr sessions to native macOS tabs and spaces and offers a chat view for agents. |
| [**Tomyail/herdr-connect**](https://github.com/Tomyail/herdr-connect) | Monitors and controls Herdr agents from an iPhone over the local network. |
| [**AkinoKaede/Termind**](https://github.com/AkinoKaede/Termind) | Reconnects to Herdr sessions from a remote workspace app for Mac, iPhone, and iPad. |
| [**multiplex-term/Multiplex**](https://github.com/multiplex-term/Multiplex) | Connects to Herdr and tmux sessions over SSH from Apple Vision Pro, iPad, or iPhone. |
| [**ventz/moo-mac-terminal**](https://github.com/ventz/moo-mac-terminal) | Tracks Herdr agents in a native macOS terminal and shows notifications when they need attention. |
| [**rarce/wooloo**](https://github.com/rarce/wooloo) | Connects a native macOS client to Herdr sessions with terminals, file browsing, editing, and Git tools. |
| [**herdr-go/herdr-go**](https://github.com/herdr-go/herdr-go) | Controls Herdr coding agents from a native mobile client using a peer-to-peer connection. |
| [**osuki-dev/muqun-app**](https://github.com/osuki-dev/muqun-app) | Connects iPhone, iPad, and Android users to Herdr TUI terminals through Muqun Gateway. |
| [**v1k45/bigtty**](https://github.com/v1k45/bigtty) | Connects a native macOS client to Herdr sessions with Ghostty-rendered terminals, spaces, browser panes, and file panes. |
| [**VoidLight00/termweave**](https://github.com/VoidLight00/termweave) | Connects browser and macOS interfaces to Herdr sessions with docked panes, workspace navigation, and agent status. |
| [**getshepherd/shepherd**](https://github.com/getshepherd/shepherd) | Runs a native macOS and Linux interface for Herdr TUI workspaces and agent status, with experimental herdr-core support. |
| [**marcelormendes/drover**](https://github.com/marcelormendes/drover) | Opens a native desktop interface for Herdr TUI workspaces, terminals, and agents. |
| [**theam/shepherdr**](https://github.com/theam/shepherdr) | Shows a prioritized queue of coding agents across Herdr machines in a native macOS client. |
| [**gigq/OmarchyRemote**](https://github.com/gigq/OmarchyRemote) | Accesses Herdr agents and an Omarchy desktop from mobile devices, desktop apps, or a browser over a private network. |
| [**patricio0312rev/anyssh**](https://github.com/patricio0312rev/anyssh) | Connects an iPhone or iPad to Herdr TUI sessions over SSH, with terminal, file and Git views. |
| [**skeletor-js/bessie**](https://github.com/skeletor-js/bessie) | Controls Herdr TUI workspaces and agents from a native macOS client. |
| [**glattziehen/hirte**](https://github.com/glattziehen/hirte) | Connects an iPhone or iPad to herdr-core over SSH to inspect agent status, answer prompts and use terminals. |
| [**quicktui/quicktui-herdr**](https://github.com/quicktui/quicktui-herdr) | Pairs QuickTUI on iPhone, iPad or Android with Herdr TUI to view sessions, answer agents and control terminals. |
| [**NakiriYuuzu/Yuzora**](https://github.com/NakiriYuuzu/Yuzora) | Runs persistent Herdr TUI sessions alongside an editor, Git tools and remote connections in a macOS or Windows desktop workspace. |
| [**YogevKr/rai**](https://github.com/YogevKr/rai) | Opens Herdr TUI sessions in a native macOS client with terminal panes, agent notifications, and an iPhone companion. |
| [**abhishek944/pet-town**](https://github.com/abhishek944/pet-town) | Shows live Herdr agents as animated characters in a desktop village. |
| [**cryks/shepherd**](https://github.com/cryks/shepherd) | Monitors local and remote Herdr agents from the macOS menu bar. |
| [**MrMySQL/uherdr**](https://github.com/MrMySQL/uherdr) | Runs a native macOS interface for Herdr workspaces, terminal panes, and agents. |
| [**InsaneArts/herdrbar**](https://github.com/InsaneArts/herdrbar) | Shows Herdr TUI agents in the macOS menu bar, sends notifications and jumps to their terminal panes. |
| [**cunderw/driverr**](https://github.com/cunderw/driverr) | Connects iPhone and iPad to Herdr TUI or herdr-core over SSH to view agents, answer prompts and use terminals. |
| [**anomius/nerv-magi**](https://github.com/anomius/nerv-magi) | Displays Herdr TUI agent and system telemetry in a fullscreen dashboard, terminal board or Omarchy widget. |
| [**LoneExile/merino**](https://github.com/LoneExile/merino) | Shows Herdr TUI agent status and pane output in a macOS menu bar and a paired phone dashboard. |
| [**lucasscariot/herdie**](https://github.com/lucasscariot/herdie) | Connects an iPhone or iPad to Herdr hosts over SSH to inspect agents, read terminal output, and send commands. |
| [**jgwesterlund/agent-view**](https://github.com/jgwesterlund/agent-view) | Shows Herdr agent status as animated pixel-art characters in a macOS app and focuses selected panes. |
| [**bsorescu/herdr-mobile**](https://github.com/bsorescu/herdr-mobile) | Shows a phone-friendly Herdr TUI over SSH for inspecting agent output and answering prompts. |
| [**speardragon/herdr-island**](https://github.com/speardragon/herdr-island) | Shows agent activity and lets users answer prompts from a macOS notch or menu-bar panel. |
| [**finik/shepherd**](https://github.com/finik/shepherd) | Connects an Android phone to Herdr TUI or herdr-core over SSH to read agent conversations and answer prompts. |
| [**keinstn/drover**](https://github.com/keinstn/drover) | Supervises Herdr TUI and herdr-core agents over SSH from an iOS or macOS app, including chat and permission prompts. |
| [**itsmaleen/merry**](https://github.com/itsmaleen/merry) | Controls Herdr TUI or cmux workspaces from an iPhone, including notifications, file and photo input, and voice commands. |
| [**JinJieBeWater/herdling**](https://github.com/JinJieBeWater/herdling) | Monitors Herdr TUI and herdr-core agents from the macOS menu bar and opens their sessions. |
| [**inferenceaftermath/remotly**](https://github.com/inferenceaftermath/remotly) | Controls Herdr TUI sessions from an iPhone or Android phone, with live panes and agent permission prompts. |
| [**pierre-charles/herdr-menu**](https://github.com/pierre-charles/herdr-menu) | Adds a macOS menu bar for viewing Herdr TUI agents and running pane, tab, and workspace actions. |
| [**zhiyao/herdcats**](https://github.com/zhiyao/herdcats) | Connects an iPhone or iPad to Herdr TUI or herdr-core over SSH to browse agents and send terminal input. |
| [**lewtec/rterm**](https://github.com/lewtec/rterm) | Attaches to local or SSH-hosted Herdr, tmux, and screen sessions from saved tabs in a desktop app. |
| [**teasec4/herdr-mobile-app**](https://github.com/teasec4/herdr-mobile-app) | Streams live agent terminal output to mobile devices, displays status updates, and dispatches prompts over LAN or Tailscale. |
| [**re2zero/zenix**](https://github.com/re2zero/zenix) | Manages Herdr TUI workspaces, tabs, and panes in a native GPUI desktop client. |
| [**mohamed-essam/herdr-mobile**](https://github.com/mohamed-essam/herdr-mobile) | Monitors Herdr agents and answers blocked prompts from an Android app backed by a Go daemon. |
| [**speardragon/herdr-bot**](https://github.com/speardragon/herdr-bot) | Turns Herdr TUI agents into chat participants that can message each other in a macOS app. |
| [**IGUNUBLUE/lerdr-rust-kotlin**](https://github.com/IGUNUBLUE/lerdr-rust-kotlin) | Connects an Android app to Herdr TUI sessions through a Rust relay over Tailscale. |
| [**Gudals0320/atrium**](https://github.com/Gudals0320/atrium) | Shows Herdr TUI agent terminals and their states on a Windows desktop canvas. |
| [**erikedling/herdquarters**](https://github.com/erikedling/herdquarters) | Runs a desktop team of Claude Code, Pi or Codex agents in Herdr TUI worktrees with a task board. |
| [**bigbug16/herdr-topbar**](https://github.com/bigbug16/herdr-topbar) | Shows Herdr TUI agent attention in the macOS menu bar and opens sessions or projects. |
| [**hmu332233/herdr-menu-bar**](https://github.com/hmu332233/herdr-menu-bar) | Shows Herdr agent status by workspace in a macOS menu bar and focuses selected panes. |
| [**fcoury/hoshi**](https://github.com/fcoury/hoshi) | Connects iPhone and iPad users to Herdr sessions over SSH or Mosh and shows agent status. |
| [**sxp4931/herdr-manager**](https://github.com/sxp4931/herdr-manager) | Shows Herdr agent status and approval prompts in a macOS menu-bar app with optional session control and usage estimates. |
| [**leescot/herdr-remote-ios**](https://github.com/leescot/herdr-remote-ios) | Enables remote control of Mac-hosted Herdr coding agents from iOS devices over SSH. |
| [**joshuaswarren/allward**](https://github.com/joshuaswarren/allward) | Runs a native macOS terminal for coding agents across machines. |
| [**OcHub-team/OcHerdr**](https://github.com/OcHub-team/OcHerdr) | Connects to Herdr from a native macOS, Linux, or Windows interface. |
| [**benngarcia/herdr-macos**](https://github.com/benngarcia/herdr-macos) | Runs a locally built native Herdr terminal for macOS using Ghostty. |
| [**seascheng/herdr-gui**](https://github.com/seascheng/herdr-gui) | Opens a native macOS front end for Herdr TUI sessions, panes, and agents. |
| [**likangmax/KodeWork**](https://github.com/likangmax/KodeWork) | Connects a Windows workbench to remote Linux hosts over SSH and reattaches to Herdr TUI sessions. |
| [**deex2/herdroid**](https://github.com/deex2/herdroid) | Connects an Android device to Herdr sessions over SSH and displays live workspace state. |
| [**fabiojansenbr/herdr-desktop**](https://github.com/fabiojansenbr/herdr-desktop) | Connects a Tauri desktop window to a Herdr server over the endpoint protocol, locally or via saved SSH hosts. Shows workspaces, tabs and agent status with a built-in editor and remote file browser. |
| [**code-akram/or2**](https://github.com/code-akram/or2) | Lets you drive coding agents from an Android SSH and mosh client that reads Herdr spaces. Shows an agent inbox across hosts and opens a blocked agent's pane. |
| [**tajchert/flocket**](https://github.com/tajchert/flocket) | Lets an Android app check, answer and steer the coding agents running in Herdr on your machines through herdr-core. Supports several hosts and federated machines; iOS is planned. |
| [**alex-jax/jax-herdr-hud**](https://github.com/alex-jax/jax-herdr-hud) | Wraps local Herdr terminals and agents in a native GTK and VTE companion window for Ubuntu, with a floating H toggle. A macOS AppKit build is in the v1.2 release. |
| [**sebastian-ruiz/spaceherd**](https://github.com/sebastian-ruiz/spaceherd) | Opens VS Code beside Herdr and switches it to the folder of the space you pick, locally or on an SSH machine. Runs as a macOS and Linux app. |
| [**juanibiapina/herdr-mobile**](https://github.com/juanibiapina/herdr-mobile) | Lets an Android or iOS app watch, start and talk to coding agents on all your machines over SSH by running herdr-core connect there. Needs no server or relay on the machines. |
| [**fatihaydost/herdrboard**](https://github.com/fatihaydost/herdrboard) | Puts Herdr in the KDE Plasma 6 system tray with every server and agent, a badge when one needs you, and one-click open, focus or kill. |
| [**bonanyan/herdrbell**](https://github.com/bonanyan/herdrbell) | Shows Herdr agent states in the macOS menu bar and opens the selected agent pane in a terminal. |
| [**joshuaswarren/omarchy-fleet-shepherd**](https://github.com/joshuaswarren/omarchy-fleet-shepherd) | Shows read-only Herdr agent status and OMP usage across local and SSH-connected machines in an Omarchy panel. |
| [**lightheaded/kari**](https://github.com/lightheaded/kari) | Shows Claude Code sessions on a macOS or Windows tray kanban board and can launch them in Herdr panes. |
| [**alejodelosrios/kelpie**](https://github.com/alejodelosrios/kelpie) | Connects an Omarchy desktop console to Herdr TUI with an agent sidebar and terminal. |
| [**dbrain/kampr**](https://github.com/dbrain/kampr) | Controls Herdr sessions remotely through a browser or Android app with streamed terminal frames and agent transcripts. |
| [**simfor99/herdr-night-watch**](https://github.com/simfor99/herdr-night-watch) | Monitors Herdr agents from a Windows tray app and can sleep or shut down the machine after work finishes. |
| [**jirathip-dev/corral**](https://github.com/jirathip-dev/corral) | Monitors Herdr TUI agents on an iPhone with a read-only fleet board and optional state-change notifications. |
| [**openalon-org/herdr-bar**](https://github.com/openalon-org/herdr-bar) | Shows Herdr TUI agent status in a menu bar and jumps to agents that need attention. |
| [**Tresnanda/mustr**](https://github.com/Tresnanda/mustr) | Opens local and remote Herdr TUI sessions in a native macOS client with pane grids and agent status. |
| [**KUKARAF/collie_voice_commands**](https://github.com/KUKARAF/collie_voice_commands) | Sends voice commands from Android to Collie or Herdr sessions and produces spoken summaries. |
| [**arvmaan/herdr-glance**](https://github.com/arvmaan/herdr-glance) | Shows live Herdr TUI agent status in an always-on-top macOS widget and focuses selected agents locally or over SSH. |
| [**SirBrother/herdr-launcher**](https://github.com/SirBrother/herdr-launcher) | Adds a Windows Explorer action that opens a folder in Herdr TUI by focusing or creating a matching workspace. |
| [**pavel-snyk/herdry**](https://github.com/pavel-snyk/herdry) | Shows blocked agents in a macOS menu bar and opens their Herdr TUI sessions. |
| [**Codem0nky87/multi-session-ai-manager**](https://github.com/Codem0nky87/multi-session-ai-manager) | Runs the Herdr TUI on an iPad over SSH, with host tabs, file transfers, and port forwarding. |
| [**lixenstrand/omarchy-herdr-drop**](https://github.com/lixenstrand/omarchy-herdr-drop) | Opens a persistent Herdr client in a drop-down Hyprland window. |
| [**re2zero/mudi**](https://github.com/re2zero/mudi) | Adds a desktop companion for Herdr with agent notifications and navigation. |
| [**muhammedenesb100/herdrm**](https://github.com/muhammedenesb100/herdrm) | Manages coding agents on local and remote machines from a native macOS console. |
| [**lukeda/herdr-panel**](https://github.com/lukeda/herdr-panel) | Shows Herdr agents and their status in a KDE Plasma desktop panel, with a dot for the most urgent state across local sessions and SSH machines. More desktops are planned. |
| [**mariotgb/drover**](https://github.com/mariotgb/drover) | Turns Herdr agents into a desktop chat app for Claude Code and Codex, with pasted screenshots, history, statuses, usage limits, and a site preview. Manages Herdr workspaces, tabs, and panes from the window. |
| [**wio-apps/shepi**](https://github.com/wio-apps/shepi) | Offers a native Mac client for Herdr that shows every agent in a real terminal and highlights the one that needs you. Paid app with a 14-day trial; this repo holds release notes and feedback. |
| [**adarshzpatel/paca**](https://github.com/adarshzpatel/paca) | Offers a native macOS client for Herdr with a Slack-style window, a live terminal, and a menu bar panel that tracks coding agents. Builds from source and is early. |
| [**muleyuck/turnray**](https://github.com/muleyuck/turnray) | Shows the status of agents running under Herdr in the macOS menu bar, plus Claude Code and Codex sessions through a plugin. Tells you which are waiting for you. |
| [**kyokosawada/viu**](https://github.com/kyokosawada/viu) | Lets developers monitor Herdr agent fleets and respond to workers by voice or keyboard from a mobile phone. |
| [**AsgardMuninn/asgardmuninn.ainoch**](https://github.com/AsgardMuninn/asgardmuninn.ainoch) | Shows blocked Herdr agent questions in a macOS notch panel and sends selected answers back to the pane. |
| [**SandroHub013/herdr-mobile**](https://github.com/SandroHub013/herdr-mobile) | Controls a Windows Herdr session from Android, iPhone, or a browser through a token-protected local bridge. |
| [**jellyfishmobile/herdup**](https://github.com/jellyfishmobile/herdup) | Launches template-based Herdr TUI agent teams in desktop workspaces with role-specific panes. |
| [**LamplitIsles/kepos-herdr-mobile**](https://github.com/LamplitIsles/kepos-herdr-mobile) | Opens one Herdr terminal on a Mac over SSH from an Android client with explicit host-key trust. |
| [**nourhelmi/herdr-mobile**](https://github.com/nourhelmi/herdr-mobile) | Controls Herdr agents and terminal panes from an iPhone app through a Bun sidecar. |
| [**marcelpanse/herdr-osx-menubar**](https://github.com/marcelpanse/herdr-osx-menubar) | Shows Herdr agents in the macOS menu bar and jumps to a selected session or project. |
| [**MarceloEmilioRiveraC/pitwall**](https://github.com/MarceloEmilioRiveraC/pitwall) | Opens a portable Windows terminal workspace with a Herdr TUI agent sidebar and a Git-aware file viewer with live diffs. |
| [**pistelak/Paddock**](https://github.com/pistelak/Paddock) | Wraps Herdr sessions in a native macOS window with a Ghostty tab per session. |
| [**sendhil/herdr-menubar**](https://github.com/sendhil/herdr-menubar) | Monitors agent status from the macOS menu bar and jumps to the relevant Herdr pane. |
| [**WoodardDigital/herdr-remote**](https://github.com/WoodardDigital/herdr-remote) | Streams Herdr TUI sessions to an Android client with touch controls and agent push notifications. |
| [**gustavocaiano/herdr-desktop-switcher**](https://github.com/gustavocaiano/herdr-desktop-switcher) | Launches or focuses configured local and SSH Herdr TUI desktops using a macOS Ghostty companion and plugin. |
| [**huahaimaker/herdr-mac**](https://github.com/huahaimaker/herdr-mac) | Runs the Herdr TUI in unofficial native macOS and Windows clients. |
| [**Tatendaz/herdr-launcher**](https://github.com/Tatendaz/herdr-launcher) | Opens or focuses the Herdr terminal interface from a macOS Dock icon. |
| [**3loc/herden**](https://github.com/3loc/herden) | Connects an iPhone console to a persistent Herdr-derived agent host using SSH pairing. |
| [**ralfkuh-lab/sheepdock**](https://github.com/ralfkuh-lab/sheepdock) | Opens Herdr in a dedicated Kitty window with its own macOS Dock icon. |
| [**cagriy/herdr-notch-releases**](https://github.com/cagriy/herdr-notch-releases) | Distributes macOS Herdr Notch release downloads and its update feed. |
| [**kingbywork-ui/issh-plugin-herdr**](https://github.com/kingbywork-ui/issh-plugin-herdr) | Adds workspace creation, session binding, and runtime health to the issh desktop client for Herdr workspaces. |
| [**Nikospy/tsk-viewer**](https://github.com/Nikospy/tsk-viewer) | Adds a macOS menu bar app for the tsk task board that lists tasks waiting on you. Sends your answers to the agent's Herdr pane and installs as a Herdr TUI plugin. |
| [**zenodea/shepherd**](https://github.com/zenodea/shepherd) | Adds a phone app and a Herdr TUI plugin host that let you see which agents need input, read their output and send instructions. Pairs over Tailscale and runs on Android or in Expo Go on iPhone. |
| [**Hariketsu/herdr-perch**](https://github.com/Hariketsu/herdr-perch) | Shows Herdr agents in the MacBook notch, colored by the most urgent one, with a hover list grouped by Needs you, Done, Working, and Idle. Click a row to focus the agent's pane. |
| [**Jrecos/HerdrBar**](https://github.com/Jrecos/HerdrBar) | Adds a macOS menu bar app that shows which Herdr agents are blocked, working, or finished, and opens an agent in Herdr with a click. |
| [**XicuM/herdr-mobile**](https://github.com/XicuM/herdr-mobile) | Monitors Herdr agents from several machines in an Android and Linux client, streams interactive terminals, and sends background alerts when an agent needs input. Talks to the herdr-bridge daemon over Tailscale or SSH. |

### Web dashboards and remote viewers

*127 projects. Browser-based monitors, remote controls, and visual scenes for following Herdr agents from another screen or device.*

> Herdr has an official [desktop app](https://herdr.dev/download/) for macOS, Windows, and Linux and an official [iPhone, iPad, and Android app](https://herdr.dev/mobile/); the projects below are community alternatives and extensions.

| Project | What it does |
|---|---|
| [**devswha/ovis**](https://github.com/devswha/ovis) | Shows Herdr agent transcripts and terminals in a desktop or phone browser, with approval cards and SSH connections. |
| [**AltanS/collie**](https://github.com/AltanS/collie) | Shows terminal agents in a phone web app and lets users answer them remotely. |
| [**dcolinmorgan/herdr-remote**](https://github.com/dcolinmorgan/herdr-remote) | Monitors and controls Herdr agents through a macOS menu bar, phone dashboard, and Telegram. |
| [**0cv/herdr-mobile-relay**](https://github.com/0cv/herdr-mobile-relay) | Combines Herdr agents from multiple machines in an installable phone web app. |
| [**powerfooI/roamgate**](https://github.com/powerfooI/roamgate) | Adds a web client for Herdr with mobile optimization, browser terminals, workspace management, and session inspection. |
| [**arronKler/pairfob**](https://github.com/arronKler/pairfob) | Opens paired Herdr agent sessions from a phone or browser, with optional Android access. |
| [**kcosr/herdr-web**](https://github.com/kcosr/herdr-web) | Monitors and controls Herdr TUI workspaces and terminal panes from a desktop or mobile browser. |
| [**lamngockhuong/termote**](https://github.com/lamngockhuong/termote) | Streams Herdr TUI or herdr-core sessions to a self-hosted browser and mobile PWA, with a TUI plugin for opening and sharing panes. |
| [**ragamo/herdr-flock**](https://github.com/ragamo/herdr-flock) | Represents active Herdr agents as animated sheep and records completed sessions in a persistent graveyard log. |
| [**alecuba16/herdr-webui**](https://github.com/alecuba16/herdr-webui) | Browses Herdr-compatible workspaces, terminals, worktrees, and Git operations in a web UI. |
| [**IvoryHeart/herdr-world**](https://github.com/IvoryHeart/herdr-world) | Connects local and SSH Herdr TUI hosts to a web control plane for viewing agents, terminals, files, and changes on desktop or mobile. |
| [**riba2534/herdrx**](https://github.com/riba2534/herdrx) | Opens a self-hosted Herdr web workbench for desktop and mobile with multi-host terminals. |
| [**BlackAngel242/MyTeam**](https://github.com/BlackAngel242/MyTeam) | Shows Herdr agents in a local pixel-art office where users can send instructions and read replies. |
| [**code-yeongyu/web-terminal**](https://github.com/code-yeongyu/web-terminal) | Runs a self-hosted mobile-first web terminal with persistent sessions, file browsing, and Herdr integration. |
| [**erwins-enkel/shepherd**](https://github.com/erwins-enkel/shepherd) | Hosts a browser control panel for parallel Claude Code and Codex sessions in isolated worktree panes. |
| [**luiscleto/shepherdr**](https://github.com/luiscleto/shepherdr) | Adds a phone-friendly web interface for Herdr: monitor agents, receive notifications, open real terminals, and send files. |
| [**hmu332233/herdr-f1**](https://github.com/hmu332233/herdr-f1) | A web visualization that represents active Herdr agents as Formula 1 cars, using race and pit-stop states to show whether agents are running, blocked, or finished. |
| [**fivetaku/whosup**](https://github.com/fivetaku/whosup) | Shows agents across Herdr TUI sessions on a local browser board and jumps to panes needing attention. |
| [**mikro-design/super-herdr**](https://github.com/mikro-design/super-herdr) | Monitors and controls Herdr sessions across machines from a terminal interface or paired phone browser. |
| [**barnuri/herdr-web**](https://github.com/barnuri/herdr-web) | Adds a mobile-first web interface for Herdr to monitor and drive coding agents from any device browser. |
| [**afloury/wherdr**](https://github.com/afloury/wherdr) | Runs a self-hosted web client for following Herdr sessions, using terminals, and replying to agents from a browser or phone. |
| [**dipeshdulal/gothalo**](https://github.com/dipeshdulal/gothalo) | Controls Herdr coding agents from a self-hosted mobile remote over Tailscale. |
| [**nixfred/shepr**](https://github.com/nixfred/shepr) | Shows and replies to Herdr agent sessions across hosts from an iPhone home-screen web app over Tailscale. |
| [**neyham/herdr-paddock**](https://github.com/neyham/herdr-paddock) | Displays a phone-friendly terminal feed of Herdr agents over SSH and supports prompt replies. |
| [**transparent-pegasus/herdr-remote**](https://github.com/transparent-pegasus/herdr-remote) | Lets users inspect Herdr TUI panes and send prompts from a phone browser through a self-hosted server. |
| [**lntvan166/paddock**](https://github.com/lntvan166/paddock) | Groups Herdr agents by state in a phone-sized dashboard and lets users answer prompts. |
| [**Hybridhash/relaydeck**](https://github.com/Hybridhash/relaydeck) | Controls Herdr TUI sessions from a phone, tablet or browser over a private Tailscale network. |
| [**eyalev/herdr-web**](https://github.com/eyalev/herdr-web) | Shows and controls Herdr TUI agents through a mobile-first browser interface with live terminal views and status. |
| [**osuki-dev/muqun-gateway**](https://github.com/osuki-dev/muqun-gateway) | Connects the Muqun mobile app to Herdr over encrypted peer-to-peer connections for remote viewing, approvals, and prompts. |
| [**zlxlabs/herdweb**](https://github.com/zlxlabs/herdweb) | Monitors and drives coding agents from mobile devices, supporting voice input, image pasting, webhooks, and multi-device servers. |
| [**NikNovo/deathstar**](https://github.com/NikNovo/deathstar) | Displays Linux host memory pressure and optional Herdr and OMP session data in a local observability dashboard. |
| [**allmight-ai/herdr-pet**](https://github.com/allmight-ai/herdr-pet) | A retro virtual-pet display that reacts to live Herdr agent states and creates a persistent pet identity from the user's GitHub ID. |
| [**kauakdev/kauak**](https://github.com/kauakdev/kauak) | Shows Herdr TUI agents in an interactive isometric office where users can read and answer terminal sessions. |
| [**loofare/herdr-portal**](https://github.com/loofare/herdr-portal) | Shows Herdr agents on a live terminal board and a browser dashboard with navigation and replies. |
| [**hrdle/hrdle**](https://github.com/hrdle/hrdle) | Controls Herdr TUI coding agents through a phone browser or Even Realities G2 glasses. |
| [**matheus3301/herdr-phone**](https://github.com/matheus3301/herdr-phone) | Monitors and controls a Herdr session from a phone through a web interface. |
| [**aviz85/herdr-controller**](https://github.com/aviz85/herdr-controller) | A Next.js dashboard for Herdr with a live agent grid, terminal mirror, messaging, agent spawning, and an optional 3D office view driven through the Herdr CLI. |
| [**arcnessai/arcdr**](https://github.com/arcnessai/arcdr) | Shows Herdr agents on a phone or browser over Tailscale and lets users answer prompts. |
| [**AnnasCookies/bordr**](https://github.com/AnnasCookies/bordr) | Opens a mobile web workspace over Tailscale for reading and controlling Herdr agents and panes. |
| [**dark2momo/herdr-tty**](https://github.com/dark2momo/herdr-tty) | Adds a mobile-friendly web terminal for Herdr powered by ttyd. |
| [**kkunkunya/herdr-remote-phone**](https://github.com/kkunkunya/herdr-remote-phone) | Controls Herdr from a phone-focused web interface with Mac profiles and conversation views. |
| [**luiscleto/weherd**](https://github.com/luiscleto/weherd) | Visualizes local Herdr agents in an interactive Three.js office. |
| [**mejiasd3v/herdr-farm**](https://github.com/mejiasd3v/herdr-farm) | A Three.js dashboard that represents Herdr workspaces and agents as a 3D farm, with animal animations tied to live idle, working, and blocked states. |
| [**funsaized/herdr-mise**](https://github.com/funsaized/herdr-mise) | Represents Herdr agents as line cooks and animates their work, tool use, and blocked states from live socket events. |
| [**misty-step/kelpie**](https://github.com/misty-step/kelpie) | Adds a phone-first PWA and desktop cockpit for checking and triaging OMP agents in Herdr workspaces. |
| [**dibin666/herdr-remote**](https://github.com/dibin666/herdr-remote) | Controls Herdr workspaces and agent terminals from a desktop or phone browser. |
| [**spad-0x/herdr-mobile-pro**](https://github.com/spad-0x/herdr-mobile-pro) | Controls Herdr and coding agents from a mobile-first web dashboard with speech input and image uploads. |
| [**JeremiahChurch/herd-remote**](https://github.com/JeremiahChurch/herd-remote) | Controls Herdr TUI agent sessions from a phone-friendly web interface, including prompts and approval actions. |
| [**derekr/wherdr**](https://github.com/derekr/wherdr) | Mirrors Herdr TUI workspaces and terminal panes in a browser, with input and agent approval controls for desktop or phone. |
| [**patraianton/sheepdog**](https://github.com/patraianton/sheepdog) | Shows Herdr coding-agent sessions on a live kanban board and lets a user dispatch work. |
| [**tlamadon/herdr-hq**](https://github.com/tlamadon/herdr-hq) | Displays Herdr agent status and per-agent resource usage across SSH-connected machines in a web dashboard. |
| [**StructuPath/herdr-suite-site · console**](https://github.com/StructuPath/herdr-suite-site/tree/main/console) | Shows read-only Herdr Suite workflow, worktree, and readiness information in a local browser console. |
| [**iYassr/shahi**](https://github.com/iYassr/shahi) | Lets users read agent conversations, answer permission prompts, and manage Herdr sessions from a phone or browser. |
| [**chano-gpt/setnet**](https://github.com/chano-gpt/setnet) | Supervises Claude Code, Codex, Pi, OpenCode, AGY, and OMO agents from a phone browser over Tailscale. |
| [**carsol/herdr-mobile**](https://github.com/carsol/herdr-mobile) | Adds a mobile-first web UI for Herdr: see your agents, attach to panes, chat with Claude Code and Codex from your phone. |
| [**lifez/herdr-agent-dashboard**](https://github.com/lifez/herdr-agent-dashboard) | Shows read-only Herdr agent activity on a touch-friendly local web dashboard for devices such as a Boox. |
| [**vantt/herdr-go**](https://github.com/vantt/herdr-go) | Controls Herdr coding agents from a phone using a web-first gateway. |
| [**damozhang/dsh-herdr-bridge**](https://github.com/damozhang/dsh-herdr-bridge) | Lets the web interface discover, start, prompt, and monitor Pi, Claude, Codex, and other agents running under Herdr. |
| [**zbysir/herdr-web**](https://github.com/zbysir/herdr-web) | Opens a browser terminal and voice prompt interface for Herdr, with mobile QR access. |
| [**tigorlazuardi/herdr-web-tui**](https://github.com/tigorlazuardi/herdr-web-tui) | Opens a Herdr session in a browser or installable web app with terminal input and mobile controls. |
| [**gabrielbarretoo/herdr-medieval**](https://github.com/gabrielbarretoo/herdr-medieval) | A Three.js visualization that turns Herdr workspaces into medieval camps and panes into animated adventurers whose behavior reflects each agent's state. |
| [**Eden-Sun/agents-manager**](https://github.com/Eden-Sun/agents-manager) | Manages multiple coding-agent CLIs running in Herdr panes via a Rust Axum daemon and React frontend. |
| [**mttzzz/herdr-web**](https://github.com/mttzzz/herdr-web) | Serves the Herdr TUI in a browser through xterm.js, so you can open the same session from a phone, tablet or another computer. Each browser tab attaches as a real Herdr client and supports touch gestures and image panes. |
| [**ihainan/corral**](https://github.com/ihainan/corral) | Serves a self-hosted browser SSH client for phones and tablets that attaches to tmux and Herdr sessions. Lets you answer a waiting Herdr agent from the top bar and jump between workspaces. |
| [**ChrisSku/briardr**](https://github.com/ChrisSku/briardr) | Serves a self-hosted web app next to Herdr that lets you watch, answer and steer agents from a phone, tablet or desktop browser. Adds file, diff and preview panels and Web Push alerts. |
| [**SimplicityGuy/herdr-corral**](https://github.com/SimplicityGuy/herdr-corral) | Edits Herdr TUI configuration in a browser with a live layout preview and local import and export. |
| [**scttymn/ranchr**](https://github.com/scttymn/ranchr) | Connects a phone or desktop PWA to a local Herdr session through a gateway, with optional tunnel access. |
| [**fellnerse/herdr-mobile**](https://github.com/fellnerse/herdr-mobile) | Adds a minimal mobile web interface for Herdr agent management. |
| [**Lawofaveragesproterozoicaeon236/web-terminal**](https://github.com/Lawofaveragesproterozoicaeon236/web-terminal) | Runs a self-hosted web terminal with persistent sessions, file browsing, and Herdr workspace and agent status. |
| [**Orchard-Robotics/herdview**](https://github.com/Orchard-Robotics/herdview) | Mirrors running Herdr agents in a phone-friendly web UI for reading transcripts, answering prompts, and sending input. |
| [**frizynn/nenu**](https://github.com/frizynn/nenu) | Adds a self-hosted web workbench for supervising Herdr coding agents from desktop or phone. |
| [**JasonBates/agentdeck**](https://github.com/JasonBates/agentdeck) | Shows Herdr agent status and transcript summaries in a browser on your Tailscale network, with tap-to-focus. |
| [**deanbaker/herdr-remote**](https://github.com/deanbaker/herdr-remote) | Displays Herdr TUI agents and live panes in a browser and sends prompts or interactive terminal input through a host bridge. |
| [**DanyGoT/herdr-companion**](https://github.com/DanyGoT/herdr-companion) | Serves a phone-friendly Herdr TUI companion with live agent status, terminal mirroring, input and image upload. |
| [**montagao/herdr-story**](https://github.com/montagao/herdr-story) | Shows Herdr TUI agents in a pixel-art office and lets users jump into conversations. |
| [**GoldenRegulus/herdr-web**](https://github.com/GoldenRegulus/herdr-web) | Opens existing Herdr TUI sessions in a local browser terminal. |
| [**Blankeos/herdr-serve**](https://github.com/Blankeos/herdr-serve) | Streams a Herdr TUI agent terminal to a phone browser with keyboard controls. |
| [**cnyarx/shelt**](https://github.com/cnyarx/shelt) | Opens a browser terminal for a Herdr session or login shell with clipboard image paste. |
| [**hmu332233/herdr-visual-lab**](https://github.com/hmu332233/herdr-visual-lab) | Shows live Herdr agent activity as animated galaxies, races, raids, and other scenes. |
| [**i-montes/herdr-web-service**](https://github.com/i-montes/herdr-web-service) | Serves a chat-style web client for Herdr agents such as Claude Code and OpenCode from a browser or phone. Has its own login and HTTPS, with a Spanish interface. |
| [**DnzzL/herdr-huddle**](https://github.com/DnzzL/herdr-huddle) | Shares a Herdr pane with a teammate who watches the agent live and can steer it from their own terminal, with a GitHub pull request as the record. |
| [**ArtMoreno/shep**](https://github.com/ArtMoreno/shep) | Opens Herdr terminals in a phone browser so you can read agent replies, send instructions, and switch panes over Tailscale. Includes a desktop app and a Herdr TUI companion plugin. |
| [**zxbdzh/herdr-workbench**](https://github.com/zxbdzh/herdr-workbench) | Maps the terminal Herdr onto a Windows desktop window and, over the local network with a pairing code, onto another computer or a phone. Ships a Tauri installer for Windows. |
| [**fangwangme/Pigeon**](https://github.com/fangwangme/Pigeon) | Puts Herdr agents on your phone as a web app for Claude Code, Codex, OpenCode, Antigravity, and pi. Shows which agent is working or waiting, reads transcripts, answers prompts, and queues messages. |
| [**alexjpower74-create/herdr-phone**](https://github.com/alexjpower74-create/herdr-phone) | Serves a phone web app that mirrors the Herdr app for your agents, reachable only over Tailscale through a bridge that reads herdr-core with hc connect. Still in development. |
| [**NoamCohen48/whistle**](https://github.com/NoamCohen48/whistle) | Turns a phone browser into a remote for agents running in Herdr over Tailscale. Shows which agent needs you, answers in the real terminal, and starts agents and worktrees. |
| [**svandragt/herdr-dash**](https://github.com/svandragt/herdr-dash) | Shows Herdr agents as a kanban board with waiting, in progress, idle, and done columns. Click a card to focus that pane. |
| [**nick1udwig/libertty**](https://github.com/nick1udwig/libertty) | Serves a mobile web terminal over Tailscale with dictation repair and a Connect Herdr option. Lets you view and drive Herdr sessions from a phone. |
| [**ashrodan/herdr-monitor**](https://github.com/ashrodan/herdr-monitor) | Serves a phone-first web app that lists Herdr agents by state, renders Claude Code, omp, and pi chats, and lets you answer agent questions. Sends push notifications as a PWA and shows open pull requests per space. |
| [**ihubanov/herdr-web**](https://github.com/ihubanov/herdr-web) | Opens a local browser client for Herdr sessions through a token-protected loopback bridge and socket API. |
| [**harlanljones/herdr-outpost**](https://github.com/harlanljones/herdr-outpost) | Adds a remote dashboard and relay gateway for Herdr sessions. |
| [**gregmcausland/herdr-control**](https://github.com/gregmcausland/herdr-control) | Adds a browser control and orchestration surface for Herdr panes. |
| [**bbgo19/herdr-web**](https://github.com/bbgo19/herdr-web) | Offers a browser interface for managing Herdr workspaces, panes, and multiple coding agents. |
| [**jwgung/HerdRabbit**](https://github.com/jwgung/HerdRabbit) | Adds a personal PWA for controlling your Herdr sessions. |
| [**radityasurya/tautan**](https://github.com/radityasurya/tautan) | Adds a mobile-first PWA hub for herdr and tmux: see every coding agent's state from your phone and reply, over Tailscale. |
| [**jclement/herdrer**](https://github.com/jclement/herdrer) | Shows a review inbox and terminal for Herdr agents that users can answer from a phone. |
| [**YannickHerrero/kelpie**](https://github.com/YannickHerrero/kelpie) | Opens a messaging-style PWA for Pi agents running in Herdr. |
| [**screenagers-io/bullpen**](https://github.com/screenagers-io/bullpen) | Shows Herdr TUI coding agents in a browser-based 3D voxel office. |
| [**stefanopineda/herdr-web**](https://github.com/stefanopineda/herdr-web) | Opens Herdr TUI sessions and agents from a phone-friendly browser over Tailscale. |
| [**kody-w/nerf-herdr-control-tower**](https://github.com/kody-w/nerf-herdr-control-tower) | Opens a local browser dashboard for a Herdr fleet and exports context or sends manual Horn broadcasts. |
| [**evsinev/herdr-watch**](https://github.com/evsinev/herdr-watch) | Monitors local and SSH-connected Herdr servers in a read-only web dashboard with workspace and agent status. |
| [**y011d4/herdr-plugin-agentweb**](https://github.com/y011d4/herdr-plugin-agentweb) | Monitors and controls Herdr TUI agents from a mobile-first web app backed by a local bridge. |
| [**narumiruna/herdr-web**](https://github.com/narumiruna/herdr-web) | Opens a browser workbench for viewing and operating the Herdr agent runtime. |
| [**NolanHo/DSH-herdr**](https://github.com/NolanHo/DSH-herdr) | Adds a DSH web view for inspecting Herdr TUI workspaces and agents, reading pane output and sending prompts. |
| [**maedana/herdr-agents-bridge**](https://github.com/maedana/herdr-agents-bridge) | Serves a phone-friendly Herdr TUI agent dashboard with status tabs, output, text input and key sending via QR connection. |
| [**sina85/herdr-mobile**](https://github.com/sina85/herdr-mobile) | Controls a local Herdr session from a mobile-first web panel through Cloudflare Tunnel and Access. |
| [**pepperhorn/herdr-remote**](https://github.com/pepperhorn/herdr-remote) | Displays Herdr TUI workspaces, panes and agent status in a remote browser dashboard and switches focused tabs. |
| [**shaunbntan-create/vgpt-app**](https://github.com/shaunbntan-create/vgpt-app) | Monitors and controls Herdr TUI agents from a phone browser over Tailscale, with terminal mirrors and a command palette. |
| [**crabfishxy/awaytome**](https://github.com/crabfishxy/awaytome) | Monitors and operates Herdr TUI agents from an Android phone through a Tailscale-connected PWA with terminal mirroring. |
| [**snowkiss13/herdr-habitat**](https://github.com/snowkiss13/herdr-habitat) | Shows Herdr TUI agent states and recent terminal activity in a local animated browser view. |
| [**sh1ftmaker/herdr-term**](https://github.com/sh1ftmaker/herdr-term) | Bridges Herdr sessions to browser interfaces with read-only file exploration and Hyprland desktop streaming. |
| [**carter2099/herdr-web-client**](https://github.com/carter2099/herdr-web-client) | Attaches to Herdr terminals through a self-hosted browser client. |
| [**4noha/herdr-drover**](https://github.com/4noha/herdr-drover) | Syncs Herdr TUI sessions across machines and connects browser or phone terminals through a cloud relay. |
| [**BlazzzPlay/herdr-office**](https://github.com/BlazzzPlay/herdr-office) | Visualizes Herdr agents and their activity in a read-only pixel-art office. |
| [**0xArchiviste/herdr-dash**](https://github.com/0xArchiviste/herdr-dash) | Serves a live web dashboard where Herdr projects and their agent threads appear as an animated graph colored by state. Lets you answer permission prompts and send follow-ups from the browser through herdr-projects. |
| [**justengel/herdr-panels**](https://github.com/justengel/herdr-panels) | Adds a desk beside a running Herdr session where panes sit with notes, browsers, HTML, and installable views that you drag into place. Includes a skill so an agent can arrange the panels. |
| [**ezjones/repodash**](https://github.com/ezjones/repodash) | Shows all git repositories as live cards with status, unpushed commits, GitHub issues, and waiting agents, in the terminal or browser. Opens as its own tab in Herdr and jumps into a repo. |
| [**ibarsi/herdr-pwa**](https://github.com/ibarsi/herdr-pwa) | Serves a phone web app for a Herdr TUI session over Tailscale that shows running agents and their screens and lets you answer them, including approval prompts. |
| [**lab486/herdr-watcher**](https://github.com/lab486/herdr-watcher) | Serves a local web dashboard for Herdr TUI agents designed for phones. Shows agent status, turns permission prompts into buttons and lets you read output and send messages. |
| [**pablopunk/webr**](https://github.com/pablopunk/webr) | Serves a touch-friendly web terminal to control Herdr agents from a phone, paired by QR code and available over private Tailscale HTTPS. Installs as a Herdr plugin; the project is marked as work in progress. |
| [**sheepvibecoder/remote-sheep**](https://github.com/sheepvibecoder/remote-sheep) | Shows Herdr TUI agents on your phone and in a browser, paired by QR code. Connects over your home network or through your own Cloudflare relay. |
| [**bartholomewtj/sightr**](https://github.com/bartholomewtj/sightr) | Serves a phone and desktop web UI for a Herdr agent herd over Tailscale, showing which agent needs you and letting you answer with buttons or text. Runs on a Windows host with a Bun bridge. |
| [**jt-wang/herdr-report**](https://github.com/jt-wang/herdr-report) | Shows each agent's goal, progress, blockers, and what needs you as a phone-friendly page, an API, and an event stream. Works with any agent Herdr TUI recognizes. |
| [**muthuishere/herdr-expose**](https://github.com/muthuishere/herdr-expose) | Lets an agent publish its own Herdr TUI session on a private, expiring URL for your phone or a teammate when you tell it to share this. Ships the agent skill that does it. |
| [**suzuki-junya108/dopadopa**](https://github.com/suzuki-junya108/dopadopa) | Shows all Claude Code sessions in a live browser board with their Herdr TUI location, state, subagents, and background commands. Lets you approve or deny permission requests from the board. |
| [**Lapis0875/herdr-relay**](https://github.com/Lapis0875/herdr-relay) | Runs Herdr app layouts and mods on a Mac and streams them over Tailscale to a PWA on an iPad, iPhone, or Android device. Lets you switch views, run mod commands, type into terminals, and get push notifications when an agent finishes. |
| [**tobi404/herdr-share-session**](https://github.com/tobi404/herdr-share-session) | Provides one-click view-only tmux session sharing between Macs (Mac 2 shares read-only, Mac 1 drives over SSH). |

### Hardware and ambient displays

*47 projects. Keypads, watches, desk devices, and compact displays that turn agent state into physical controls or at-a-glance signals.*

| Project | What it does |
|---|---|
| [**timvdhoorn/stream-deck-herdr-plugin**](https://github.com/timvdhoorn/stream-deck-herdr-plugin) | Assigns a key to each agent, displays its state with a color and icon, and focuses the matching Herdr pane when pressed. |
| [**Unayung/herdr-watch**](https://github.com/Unayung/herdr-watch) | A native Apple Watch companion that shows Herdr agent activity and alerts the wearer when an agent finishes or needs input. |
| [**spencerbull/xeneon-edge-agents**](https://github.com/spencerbull/xeneon-edge-agents) | An Omarchy and Herdr agent command center designed for the Corsair XENEON EDGE display, with conservative handling when state cannot be confirmed. |
| [**walcew/herdr-assist**](https://github.com/walcew/herdr-assist) | An ESP32-S3 desk display that shows Herdr session states and sounds a bell when an agent is waiting for a decision or approval. |
| [**mrshu/muxboard**](https://github.com/mrshu/muxboard) | Shows Herdr agent attention status and CodexBar usage metrics on a Stream Deck+ dashboard. |
| [**alasano/house-of-herdr**](https://github.com/alasano/house-of-herdr) | Maps Herdr TUI agent status and controls to the Work Louder Codex Micro keypad, dial, and joystick. |
| [**finna/omarchy-herdr-hud**](https://github.com/finna/omarchy-herdr-hud) | Monitors and prompts Herdr agents from a draggable Omarchy overlay. |
| [**niklasberglund/herdr-logi-plugin**](https://github.com/niklasberglund/herdr-logi-plugin) | Shows Herdr TUI workspace and agent status on a Logitech MX Keypad and focuses a selected pane on keypress. |
| [**Resilient-Software/herdr-opendeck**](https://github.com/Resilient-Software/herdr-opendeck) | Mirrors Herdr TUI workspaces to a Stream Deck with repository, branch and agent-status tiles. |
| [**fedeya/corral**](https://github.com/fedeya/corral) | Shows Herdr TUI agents as animated critters on a Stream Deck Plus and focuses an agent when its key is tapped. |
| [**chenxin-yan/herdr-micro**](https://github.com/chenxin-yan/herdr-micro) | Controls and monitors Herdr coding agents from a physical MacroPad. |
| [**dkarter/foreman**](https://github.com/dkarter/foreman) | Shows live Herdr TUI agents on a Raspberry Pi touchscreen and focuses their panes by tap. |
| [**ahkohd/companion**](https://github.com/ahkohd/companion) | Runs a local web app that drives a small desktop display and follows your coding agents. Its Herdr Face module shows agent status and session names with animated expressions. |
| [**nytafar/gjetr**](https://github.com/nytafar/gjetr) | Shows every Herdr agent as a live card on a secondary touchscreen or sidebar as an Omarchy shell plugin. Tapping a card jumps to that agent and cards show prompt-cache timers. |
| [**eszanon/omarchy-herdr**](https://github.com/eszanon/omarchy-herdr) | Shows Herdr coding agents in the Omarchy bar and flags the ones waiting on you. |
| [**vaclavik-xyz/herdeck**](https://github.com/vaclavik-xyz/herdeck) | Controls Herdr agents from a Stream Deck, a native desktop window, or a browser dashboard. |
| [**rkbkosp/agent-beacon**](https://github.com/rkbkosp/agent-beacon) | Displays Herdr agent state, Codex quota, and alerts on an ESP32-S3 beacon through a macOS bridge. |
| [**bowlofsoup/herdr-stoplight**](https://github.com/bowlofsoup/herdr-stoplight) | An Arduino integration that uses a physical traffic light to show aggregate Herdr status: green for working, red for blocked or failed, and yellow for idle. |
| [**third774/herdr-sidepulse**](https://github.com/third774/herdr-sidepulse) | A USB hardware integration for SidePulse Pro and Dot devices that turns combined Herdr agent states into ambient LED patterns, including prominent alerts for blocked agents. |
| [**omerturhan/herdr-touchbar**](https://github.com/omerturhan/herdr-touchbar) | Shows working and blocked Herdr agents and jumps to a selected agent's tab when tapped. |
| [**johnendean/herdrkeys**](https://github.com/johnendean/herdrkeys) | Uses Pimoroni Keybow 2040 as a way of monitoring and switching between agents running in Herdr, inspired by the Codex Micro/Creator Micro2. |
| [**so1omon563/herdr-control-stream-deck**](https://github.com/so1omon563/herdr-control-stream-deck) | Navigates Herdr TUI workspaces, tabs, panes, and agents from an Elgato Stream Deck. |
| [**dghelm/herdy**](https://github.com/dghelm/herdy) | Provides a hurdy-gurdy for your agent herd: MIDI hardware control surface for herdr and Omarchy (Arturia Keylab 61). |
| [**imbriaco/herdr-deck**](https://github.com/imbriaco/herdr-deck) | Streams Deck plugin for Herdr: live agent status lights and one-key focus. |
| [**pnomolos/herdr-kontrol**](https://github.com/pnomolos/herdr-kontrol) | Shows Herdr TUI agent status and focuses panes using a Maschine MK3 or Plus controller on macOS. |
| [**dghelm/omarchy-herdy**](https://github.com/dghelm/omarchy-herdy) | Configures the herdy MIDI controller for Herdr agent workspaces from an Omarchy bar panel. |
| [**sim186/agent-deck**](https://github.com/sim186/agent-deck) | Turns a Mirabox or other OpenDeck device into a control surface for Claude Code, Codex, OpenCode, and Pi agents running in Herdr. Shows agent status tiles and lets you approve or stop agents from the keys; the layout also has meeting recording and calendar keys. |
| [**minyona/herdr-screensaver-omarchy**](https://github.com/minyona/herdr-screensaver-omarchy) | Adds an Omarchy screensaver that imitates a live Herdr session with fake agents and hidden easter eggs, and locks the screen on wake. |
| [**salemsayed/omaherd**](https://github.com/salemsayed/omaherd) | Shows local and SSH-accessible Herdr agent states in the Omarchy bar and jumps to a selected pane. |
| [**d4rken/herdr-mint-applet**](https://github.com/d4rken/herdr-mint-applet) | Displays Cinnamon desktop panel applets showing idle, busy, or blocked Herdr agent sessions. |
| [**lfsmoura/led-agent-status**](https://github.com/lfsmoura/led-agent-status) | Shows your AI agents' status on a BLE LED strip, blue working, blinking red blocked, green done. |
| [**sigma/sd-mux**](https://github.com/sigma/sd-mux) | Shows agents needing attention on a Stream Deck button and cycles through them when pressed. |
| [**gpando/herdr-sense**](https://github.com/gpando/herdr-sense) | Displays Herdr agent states on a Raspberry Pi Sense HAT LED matrix using MQTT events from herdr-telegram. |
| [**tmcinerney/beckon**](https://github.com/tmcinerney/beckon) | Binds Herdr TUI agent panes to navigation keys and displays agent states on a wired Glove80. |
| [**AlexBSoD/qubeherd**](https://github.com/AlexBSoD/qubeherd) | A hardware integration that shows Herdr agent state, the host clock, and keyboard layout on an Ergohaven Qube dongle display. |
| [**8-BitRhyon/bantay-tui**](https://github.com/8-BitRhyon/bantay-tui) | A macOS notch HUD that combines Herdr approvals, live usage and cost data, a file shelf, task tracking, Apple Reminders sync, and session controls. |
| [**zhongpei/herdr-ulanzi-deck**](https://github.com/zhongpei/herdr-ulanzi-deck) | A Ulanzi D200X keypad integration that shows live, priority-sorted Herdr agent states on LCD keys and can monitor several Herdr machines over SSH. |
| [**walcew/herdr-avatars**](https://github.com/walcew/herdr-avatars) | Adds downloadable avatar packages for the Herdr Assist hardware dashboard, including agent-state animations. |
| [**zanellig/keyblink**](https://github.com/zanellig/keyblink) | Blinks the HyperX Alloy Origins Core Game Mode indicator on Herdr TUI agent status changes on Linux. |
| [**saplaum/herdr-awtrix**](https://github.com/saplaum/herdr-awtrix) | Shows Herdr TUI agent activity on an AWTRIX pixel display over HTTP. Optionally scrolls a notification naming the workspace that needs attention. |
| [**WindyWin/herdr-agent-pet**](https://github.com/WindyWin/herdr-agent-pet) | Starts the Agent Pet desktop companion with the Herdr server and installs or updates it from inside Herdr TUI. |
| [**voodootikigod/herdr-bartender**](https://github.com/voodootikigod/herdr-bartender) | Mirrors Herdr TUI agent status into the Top Shelf of Bartender 6 Pro on macOS, covering Claude Code, Codex, Gemini CLI, Cursor, OpenCode, and others. |
| [**lfsmoura/herdr-haptic-alert**](https://github.com/lfsmoura/herdr-haptic-alert) | Sends a haptic pulse to a Bluetooth Logitech MX Master 4 when a Herdr TUI agent needs attention. Runs on macOS with Node.js 22 or newer. |
| [**sneakytowelsuit/herdr-deck**](https://github.com/sneakytowelsuit/herdr-deck) | Shows each Herdr agent on an Elgato Stream Deck key that turns red when the agent needs input, and focuses that agent on press. Pages also drive panes, tabs, workspaces, layouts, and worktrees. |
| [**dpulpeiro/omarchy-herdr-collie**](https://github.com/dpulpeiro/omarchy-herdr-collie) | Monitors and controls the Collie Herdr web UI and its Tailscale Serve endpoint from the Omarchy bar. |
| [**cxnmai/dms-herdr-plugin**](https://github.com/cxnmai/dms-herdr-plugin) | A DankMaterialShell widget for viewing Herdr agent states and accessing basic controls from the desktop shell. |
| [**leddt/plasma-cliamp**](https://github.com/leddt/plasma-cliamp) | Adds a Plasma 6 panel widget that controls cliamp and attaches to its Herdr TUI session. |

### Processes, ports, sandboxes, and remote machines

*28 projects. Tools for watching and stopping dev servers and listening ports, cleaning up leftover processes, and running agents or shells in sandboxes, VMs, containers, and remote hosts.*

| Project | What it does |
|---|---|
| [**dirien/herdr-sbx-plugin**](https://github.com/dirien/herdr-sbx-plugin) | Runs Claude Code, Codex, Gemini CLI, and other coding agents in separate Docker Sandboxes from Herdr TUI. |
| [**sudoeren/herdr-lazydocker**](https://github.com/sudoeren/herdr-lazydocker) | Runs lazydocker in a herdr split pane or its own tab. |
| [**dvdksn/sbx-herdr**](https://github.com/dvdksn/sbx-herdr) | Registers Docker Sandboxes as Herdr TUI SSH machines and identifies sandbox agents in local panes. |
| [**carze/herdr-smolmachine**](https://github.com/carze/herdr-smolmachine) | Starts coding agents in libkrun or KVM microVMs from Herdr panes and lists running sandboxes. |
| [**ivorpad/herdr-tunnel**](https://github.com/ivorpad/herdr-tunnel) | Lists local listening ports and opens, copies, or stops public tunnels from a Herdr TUI pane. |
| [**ivorpad/herdr-ports**](https://github.com/ivorpad/herdr-ports) | Adds a popup that lists listening ports, names the project behind each one, and kills or opens it. |
| [**AZenking/herdr-nodejs-center**](https://github.com/AZenking/herdr-nodejs-center) | Adds a Herdr popup for monitoring and focusing local Node.js, Bun, and Deno services. |
| [**Slimydog21/herdr-nixos-vm**](https://github.com/Slimydog21/herdr-nixos-vm) | Controls an existing NixOS development VM from a Herdr TUI pane, including boot, stop, monitoring, and SSH. |
| [**abcxff/herdr-docker**](https://github.com/abcxff/herdr-docker) | Keeps track of docker builds like you do with agents for herdr. |
| [**Keepstateai/cli · herdr**](https://github.com/Keepstateai/cli/tree/main/herdr) | Shows KeepState sessions, agents, saved points and Cruise receipts in Herdr panes through the ks client. Sends a Herdr notification when a Cruise job finishes. |
| [**TinocoAI/herdr-checkpoint-health**](https://github.com/TinocoAI/herdr-checkpoint-health) | Runs read-only Check Point GAiA health checks over SSH from a Herdr TUI plugin and summarizes gateway status. |
| [**Efeguclu1/herdr-process-guard**](https://github.com/Efeguclu1/herdr-process-guard) | Identifies processes started by agents by workspace and pane, explains suspected leftovers, and previews process trees before stopping them. |
| [**hitaishi2222/herdr-llama**](https://github.com/hitaishi2222/herdr-llama) | Controls llama-server models and lifecycle from Herdr TUI and shows server and token-rate status. |
| [**aneym/cull**](https://github.com/aneym/cull) | Shows macOS compute use in a menu bar monitor and helps terminate processes, including those attributed to Herdr sessions. |
| [**carellano/herdr-dev-servers**](https://github.com/carellano/herdr-dev-servers) | Detects development servers running in Herdr panes, records their ports and process state, and can focus or safely stop orphaned services. |
| [**AsgardMuninn/herdr-plugin-orbstack**](https://github.com/AsgardMuninn/herdr-plugin-orbstack) | Creates and manages OrbStack Linux virtual machines as Herdr workspaces, using native shell attachment with SSH fallback and synchronized state. |
| [**iQua/herdr-flakes**](https://github.com/iQua/herdr-flakes) | Mirrors and controls Flakes runs from a local Herdr session. |
| [**fantoine/herdr-run-targets**](https://github.com/fantoine/herdr-run-targets) | Opens a Herdr TUI dashboard to start, stop, and restart repository-defined development services in named tabs. |
| [**n-jc/herdr-opencode**](https://github.com/n-jc/herdr-opencode) | Provides a set up to use Opencode within Apple Containers as a sandbox and manage via Herdr on a Mac OS host machine. |
| [**andrewmcodes/overhrd**](https://github.com/andrewmcodes/overhrd) | Provides a Procfile process manager for herdr users, a herdr-backed reimplementation of Overmind. |
| [**AndresDiagoM/herdr-wsl-tab**](https://github.com/AndresDiagoM/herdr-wsl-tab) | Opens a Herdr tab or split that runs a WSL distro on Windows, starting in the focused pane's directory, and passes the `HERDR_*` variables through so Claude Code, Codex, or opencode inside WSL can drive Herdr. Restores those panes after a Herdr restart, and an optional setup action installs Claude Code hooks so the session shows its state. |
| [**prized-dev/integrations · herdr**](https://github.com/prized-dev/integrations/tree/main/herdr) | Runs Claude Code or Codex from a Herdr worktree on a Prized sandbox or box, and pauses the sandbox when the pane closes. Needs the prized CLI and a Prized login. |
| [**linkcd/herdr-agentcore**](https://github.com/linkcd/herdr-agentcore) | Connects Herdr TUI terminals to interactive coding assistants running in Amazon Bedrock AgentCore Runtime. Manages saved connections, reconnect, detach and stop. |
| [**chmouel/herdr-icucomefrom**](https://github.com/chmouel/herdr-icucomefrom) | Detects whether the attached Herdr TUI client came in over ssh or runs locally. Lets prompts and scripts react to that, for example to colour the prompt or skip opening a browser. |
| [**rondar-dev/herdr-rondar**](https://github.com/rondar-dev/herdr-rondar) | Connects Herdr TUI to Rondar cloud agent sessions so you can send a branch to Rondar and answer its agents from the terminal. Shows PR, checks and preview state in the sidebar. |
| [**baeroe/herdr-tussh**](https://github.com/baeroe/herdr-tussh) | Opens tussh, an SSH connection manager with access control for AI agents, in a Herdr TUI split or tab. Shows its pending approvals as a popup. |
| [**ivanvykopal/herdr-slurm-ops**](https://github.com/ivanvykopal/herdr-slurm-ops) | Controls Slurm and PBS jobs from the Herdr TUI: inspect, follow logs, hold, release, requeue, cancel, and notify an agent when a job finishes. |
| [**zbyhoo/herdr-wake_on_lan**](https://github.com/zbyhoo/herdr-wake_on_lan) | Wakes sleeping saved SSH machines with Wake-on-LAN from a list that marks each as online or offline. Stores each machine's MAC address. |

### Agent support, auto-approve, retry, and keep-awake helpers

*20 projects. Add-ons that teach Herdr about extra coding agents, auto-approve or auto-continue stalled agents after rate limits, and keep the machine awake while agents work.*

| Project | What it does |
|---|---|
| [**mo-arvan/herdr-claude-auto-retry**](https://github.com/mo-arvan/herdr-claude-auto-retry) | Detects Claude Code stalls caused by rate limits or server errors and safely resumes only idle or blocked panes, leaving actively working agents untouched. |
| [**scrappylabsai/podr**](https://github.com/scrappylabsai/podr) | Adds Reasonix and DeepSeek Harness detection to a Herdr TUI fork and includes a client for attaching to DSH sessions. |
| [**XiangQhello/codex-claude-auto-enter**](https://github.com/XiangQhello/codex-claude-auto-enter) | Sends repeated Enter presses to a selected Herdr TUI pane and stops when Codex or Claude Code becomes idle. |
| [**RenKoya1/herdr-approve-all**](https://github.com/RenKoya1/herdr-approve-all) | Approves every pending agent permission request in Herdr with one keystroke. |
| [**gw31415/herdr-amphetamine-macos**](https://github.com/gw31415/herdr-amphetamine-macos) | Watches Herdr agent-status events and keeps an Amphetamine session active while agents are working, preventing sleep during long tasks. |
| [**bestony/herdr-codex-capacity-retry**](https://github.com/bestony/herdr-codex-capacity-retry) | Automatically continues Codex sessions in Herdr after capacity-related interruptions. |
| [**susomejias/herdr-awake**](https://github.com/susomejias/herdr-awake) | Keeps the machine awake while Herdr agents are busy. |
| [**ichadhr/herdr-zcode**](https://github.com/ichadhr/herdr-zcode) | Adds ZCode agent support to Herdr TUI, showing zcode panes in the sidebar with live working, blocked, and idle state. Registers hooks in the zcode settings file. |
| [**jaaacki/herdr-plugin-minimax-code**](https://github.com/jaaacki/herdr-plugin-minimax-code) | Adds MiniMax Code support to Herdr TUI by launching mcode in a new pane and registering hand-started mcode sessions so they appear as agents. |
| [**jewei/herdr-caffeinated**](https://github.com/jewei/herdr-caffeinated) | Keeps a Mac awake with caffeinate while a Herdr agent works and lets it sleep after 60 idle seconds. A pause action turns it off. |
| [**scheron/herdr-want-to-sleep**](https://github.com/scheron/herdr-want-to-sleep) | Adds a herdr plugin that puts your Mac to sleep once no coding agent is working any more. Arm it before bed and it waits for every agent to settle, then journals what each one was doing, including the ones that ended up blocked. |
| [**islee23520/herdr-omo-agent**](https://github.com/islee23520/herdr-omo-agent) | Registers OmO sessions as coding agents on stock Herdr TUI 0.8.2; the author’s OmO-native fork does not need this package. |
| [**tigorlazuardi/herdr-claude-retry**](https://github.com/tigorlazuardi/herdr-claude-retry) | Detects Claude usage-limit banners and resumes Herdr TUI panes when the limit resets. |
| [**mougua/herdr-reasonix**](https://github.com/mougua/herdr-reasonix) | Detects Reasonix agents and displays their status correctly. |
| [**moonquddus/cruise-ctrl**](https://github.com/moonquddus/cruise-ctrl) | Answers Claude Code permission prompts with Yes so long tasks keep going, as a wrapper script plus a Herdr plugin and app mod. Passes your keyboard through so you can still intervene. |
| [**ecklf/herdr-fx**](https://github.com/ecklf/herdr-fx) | Starts or resumes the fx coding agent in a Herdr TUI pane and shows when it is working or waiting for you. Hooks fx into Herdr notifications and restores saved fx sessions. |
| [**cwkendall/amp-herdr**](https://github.com/cwkendall/amp-herdr) | Makes Amp report its thread state, approval prompts and titles directly to Herdr, and resumes Amp threads after a restart. Ships an Amp theme. |
| [**tlpinney/herdr-auggie**](https://github.com/tlpinney/herdr-auggie) | Makes Herdr TUI show Augment's Auggie CLI as working, idle or blocked, detects approvals and questions, shows session titles and resumes conversations after a restart. |
| [**frederikpietzko/herdr-plugin-junie**](https://github.com/frederikpietzko/herdr-plugin-junie) | Adds Junie CLI support to Herdr TUI through Junie hooks, so Junie panes show idle, working and blocked state, send notifications, and resume sessions. |
| [**moosingin3space/herdr-sleep-inhibit**](https://github.com/moosingin3space/herdr-sleep-inhibit) | Prevents idle sleep and suspend on a Linux desktop while any Herdr TUI agent is working, through the XDG Inhibit portal. A popup shows which agents hold the lock. |

### Notes, prompts, clipboard, and file helpers

*32 projects. Per-tab scratchpads and notes, saved prompt decks, task lists, credential pickers, clipboard and image paste, and file transfer or reveal helpers for Herdr panes.*

| Project | What it does |
|---|---|
| [**Resetnak/herdr-logbook**](https://github.com/Resetnak/herdr-logbook) | Manages Markdown tasks and decisions in an offline notebook for Herdr workspaces. |
| [**vjeantet/herdr-scratchpad**](https://github.com/vjeantet/herdr-scratchpad) | Docks a plain-text scratchpad at the bottom of a tab, one persistent buffer per tab, for composing a prompt where Enter can't send it half-finished. `Ctrl+E` moves it, or just the selection, into an agent of the same tab without submitting; `Ctrl+C` copies over OSC 52. |
| [**kosuketut/herdr-remotedownloder**](https://github.com/kosuketut/herdr-remotedownloder) | Downloads files created or changed in a remote Herdr pane to a local Mac. A plugin action detects paths in the active pane and transfers the selected artifact over the remote connection. |
| [**ddfonseca/herdr-paste-image**](https://github.com/ddfonseca/herdr-paste-image) | Saves an image from the macOS or Linux clipboard to disk and pastes its file path into the active pane for use by multimodal agents. |
| [**mrolafsson/herdr-file-transfer**](https://github.com/mrolafsson/herdr-file-transfer) | Transfers files between a local machine and a remote Herdr TUI host over SSH and sends their paths to agents. |
| [**ivolkoff/herdr-huddle**](https://github.com/ivolkoff/herdr-huddle) | Opens rich questions over a Herdr TUI agent pane and returns the answers to the agent as JSON. |
| [**mdetweil/herdr-lazytask**](https://github.com/mdetweil/herdr-lazytask) | Opens Lazytask in a Herdr TUI split or tab and adds Taskwarrior quick actions. |
| [**WillowMist/herdr-bitwarden**](https://github.com/WillowMist/herdr-bitwarden) | Searches a Bitwarden vault from a Herdr TUI popup and copies or pastes selected credentials. |
| [**chrisg32/tsk**](https://github.com/chrisg32/tsk) | Manages plain-text tasks in a Rust TUI that runs standalone or as a Herdr plugin. |
| [**niceview/mac-finder-quick-actions**](https://github.com/niceview/mac-finder-quick-actions) | Opens Finder selections in VS Code or a new Herdr TUI workspace through macOS quick actions and a drag-and-drop launcher. |
| [**Sawakee/herdr-imebox**](https://github.com/Sawakee/herdr-imebox) | Opens an IME-friendly popup for composing CJK text and sending it to a Herdr TUI agent pane. |
| [**wine-fall/herdr-copy-pane-id**](https://github.com/wine-fall/herdr-copy-pane-id) | Copies the focused pane's id to the clipboard, or show every pane's id on its border. |
| [**ecylmz/herdr-drop**](https://github.com/ecylmz/herdr-drop) | Copies a file dragged onto a Herdr TUI pane into that pane's current directory, including on SSH hosts, through the existing pty. |
| [**brunohq/herdr-scratchpad**](https://github.com/brunohq/herdr-scratchpad) | Opens a per-tab Markdown scratchpad with checkbox todos and a progress bar in a pane beside your work. Uses only the Python standard library. |
| [**matdac12/herdr-prompt-deck**](https://github.com/matdac12/herdr-prompt-deck) | Adds a prompt bar to the bottom of a Herdr TUI tab that inserts file paths, snippets, screenshots and scratch text into the focused agent prompt without submitting it. |
| [**StGerman/herdr-claude-memories**](https://github.com/StGerman/herdr-claude-memories) | Shows and lets you curate Claude Code auto-memory across all running sessions from inside Herdr TUI, including memories written in other panes. |
| [**MartinKei/herdr-tab-notes**](https://github.com/MartinKei/herdr-tab-notes) | Opens a popup editor for notes stored separately for each Herdr TUI tab. |
| [**klukacin/herdr-finder-reveal**](https://github.com/klukacin/herdr-finder-reveal) | Reveals OSC 8-linked local file paths from Herdr TUI panes in macOS Finder. |
| [**Tomyail/omnifocus-tui**](https://github.com/Tomyail/omnifocus-tui) | Runs an OmniFocus terminal UI for capturing, browsing, and editing tasks in a Herdr popup, split, or tab. Needs OmniFocus on macOS. |
| [**Taanviir/herdr-scratchpad**](https://github.com/Taanviir/herdr-scratchpad) | Captures notes with a key into a global scratchpad linked to folders and labelled with hashtags, then hands them to an agent later. |
| [**Aliancn/herdr-tab-notes**](https://github.com/Aliancn/herdr-tab-notes) | Opens a Markdown note per tab in a narrow split with one key and closes it with the same key. |
| [**huluhuluu/herdr-prompt**](https://github.com/huluhuluu/herdr-prompt) | Opens a popup in Herdr TUI to search, edit and reuse saved prompts and to pick one or more file paths for the current pane. Runs on Windows and Linux and builds from source with Cargo. |
| [**limonequantistico/herdr-todos**](https://github.com/limonequantistico/herdr-todos) | Shows a todo list from a TODOS.md file in a Herdr TUI side panel, with drag to reorder and click to tick. Builds with a Rust toolchain. |
| [**ronzyfonzy/herdr-notes**](https://github.com/ronzyfonzy/herdr-notes) | Opens per-tab Markdown notes in a Herdr TUI side pane, stored next to the Claude Code session so Claude can read and edit them. |
| [**yang3kc/herdr-tab-notes**](https://github.com/yang3kc/herdr-tab-notes) | Opens one plain Markdown scratchpad per Herdr TUI tab in a narrow right split and closes it with the same key. |
| [**QuantumEdu/herdr-quicknotes**](https://github.com/QuantumEdu/herdr-quicknotes) | Opens a modal popup notes manager with fuzzy search, a CLI, and one-key clipboard copy. Written in Rust. |
| [**ClockworkNet/herdr-claude-finder-scratchpad**](https://github.com/ClockworkNet/herdr-claude-finder-scratchpad) | Opens the scratchpad of a Claude Code session in a macOS Finder window, or focuses the existing window. Can open one per live agent in the workspace. |
| [**ibanks42/herdr-rbw**](https://github.com/ibanks42/herdr-rbw) | Fuzzy-searches a Bitwarden vault through rbw inside Herdr TUI and pastes or copies credentials into the focused pane. Ports tmux-bitwarden to the Herdr plugin format. |
| [**rapha4lx/herdr-secrets**](https://github.com/rapha4lx/herdr-secrets) | Shows a workspace project's .env files in a Herdr TUI modal with values masked by default. Reveals values on a key press and copies them to the clipboard over OSC52. |
| [**NakasamaJ/herdr-pane-memo**](https://github.com/NakasamaJ/herdr-pane-memo) | Opens a per-pane scratchpad memo in a Herdr TUI popup from a keybinding and deletes the memo when the pane closes. |
| [**testy-cool/herdr-open-nemo**](https://github.com/testy-cool/herdr-open-nemo) | Opens the active pane's directory in a Nemo file manager window from a Herdr TUI keybinding and raises it. Needs a local X11 desktop with wmctrl and xdotool. |
| [**gilvanecesar/herdr-attach**](https://github.com/gilvanecesar/herdr-attach) | Opens a file picker from Herdr TUI and sends the chosen files to the focused agent, inline for small text and as paths for binary or large files. |

### Developer tool panes and everyday utilities

*56 projects. Panes that open database, API, CI, Git, and cloud clients, plus translators, media players, calendars, feeds, and other everyday utilities beside your agents.*

| Project | What it does |
|---|---|
| [**coryshaw1/herdr-cliamp**](https://github.com/coryshaw1/herdr-cliamp) | Opens the cliamp audio player in a floating Herdr TUI pane while playback continues in a detached session. |
| [**pivoshenko/musicforprogramming · plugins/herdr/mfp.player**](https://github.com/pivoshenko/musicforprogramming/tree/main/plugins/herdr/mfp.player) | Opens the musicforprogramming.net player in a Herdr TUI pane and maps playback controls to actions. |
| [**ablause/herdr-flutter**](https://github.com/ablause/herdr-flutter) | A Herdr sidebar for watching, hot-reloading, and inspecting a running Flutter app beside the coding agent working on it. |
| [**Tomatio13/herdr-google-gmail**](https://github.com/Tomatio13/herdr-google-gmail) | Browses Gmail in a Herdr TUI split using fzf and gogcli, with mail actions and background notifications. |
| [**RizRiyz/pixtui**](https://github.com/RizRiyz/pixtui) | Opens a terminal pixel-art editor in a Herdr TUI pane with layers, animation, and PNG or GIF export. |
| [**Javamomma/herdr-scribe**](https://github.com/Javamomma/herdr-scribe) | Streams microphone audio to temporary panes and creates meeting notes, policy checks, and draft tickets without saving raw audio. |
| [**neospeed83/herdr-standup**](https://github.com/neospeed83/herdr-standup) | Builds a daily standup from Git commits and optional notes, then opens the report from a Herdr TUI workspace. |
| [**Tomatio13/herdr-google-calendar**](https://github.com/Tomatio13/herdr-google-calendar) | Browses Google Calendar events in an fzf panel and creates a Herdr TUI worktree and workspace from an event. |
| [**arhen/devnull-tui**](https://github.com/arhen/devnull-tui) | Reads the /dev/null developer commit network in a Herdr TUI pane with a feed, threads, replies, stars and an inbox, and opens links in a Herdr browser tab. Also runs as a standalone terminal client. |
| [**wazum/herdr-polyglot**](https://github.com/wazum/herdr-polyglot) | Translates prompts into English before sending them to an agent pane in Herdr. |
| [**zackshen/herdr-translate**](https://github.com/zackshen/herdr-translate) | Translates mouse-selected Herdr TUI text in a centered popover using a local model or Google fallback. |
| [**DeepRuparel/herdr-spotify**](https://github.com/DeepRuparel/herdr-spotify) | Controls Spotify playback and playlist queues directly from Herdr terminal panes. |
| [**smanickam01/herdr-atuin-plugin**](https://github.com/smanickam01/herdr-atuin-plugin) | Opens Atuin history search in a Herdr TUI popup and inserts or runs the selected command in the originating pane. |
| [**fraction12/herdr-rainfrog**](https://github.com/fraction12/herdr-rainfrog) | Opens Rainfrog in a managed Herdr TUI pane with a connection picker and workspace-scoped pane reuse. |
| [**tkuchiki/herdr-plugin-k8s-context**](https://github.com/tkuchiki/herdr-plugin-k8s-context) | Opens Herdr tabs with isolated Kubernetes contexts and namespaces. |
| [**Royal-lobster/herdr-spinup**](https://github.com/Royal-lobster/herdr-spinup) | Shows a configurable launcher in every new Herdr tab. Tools are defined in JSON and start directly in the selected pane with normal agent detection. |
| [**playsthisgame/herdr-api-client**](https://github.com/playsthisgame/herdr-api-client) | Opens the Ichigo terminal REST client in a split or tab and scopes it to the current project's request collection. |
| [**joelhooks/herdr-brain**](https://github.com/joelhooks/herdr-brain) | Renders Brain SVX documents as native OpenTUI views in Herdr panes. |
| [**MattJColes/herdr-android-emulator**](https://github.com/MattJColes/herdr-android-emulator) | Embeds an Android emulator in a Herdr view beside your coding agent so both use the same device. Gives the agent a CLI for taps, typing, logs and crashes. |
| [**MattJColes/herdr-ios-simulator**](https://github.com/MattJColes/herdr-ios-simulator) | Embeds the iOS Simulator in a Herdr pane beside your coding agent. Gives the agent commands to launch apps and read logs, crashes and events. |
| [**baeroe/herdr-lazysql**](https://github.com/baeroe/herdr-lazysql) | Runs the lazysql database client in a Herdr TUI split or its own tab, as toggle actions. |
| [**aristeoibarra/herdr-pointr**](https://github.com/aristeoibarra/herdr-pointr) | Sends a comment on any element of a localhost web page to the coding agent that owns that project, with its React component, selector, console errors and an optional screenshot. The agent answers in a thread pinned to the element. |
| [**shindakun/herdr-rss**](https://github.com/shindakun/herdr-rss) | Reads RSS, Atom and JSON feeds in a Herdr TUI pane, as a split beside your work or zoomed over it. Ships as a single Rust binary. |
| [**longwind48/diskzap**](https://github.com/longwind48/diskzap) | Reports and, only with --apply, deletes regenerable package caches, build artifacts and Docker leftovers from an explicit catalog. Runs as a Rust CLI, an agent skill and a Herdr TUI popup plugin. |
| [**shindakun/herdr-llm-lint**](https://github.com/shindakun/herdr-llm-lint) | Lints CLAUDE.md, AGENTS.md and other agent instruction files for stale paths, commands and drift. Runs as a CLI and as a Herdr TUI plugin. |
| [**VoidAxon/herdr-lens**](https://github.com/VoidAxon/herdr-lens) | Translates and explains selected pane text, including words, identifiers, and build output, using an AI provider. |
| [**alexanderop/prefix-dojo**](https://github.com/alexanderop/prefix-dojo) | Teaches tmux and Herdr TUI workflows through interactive lessons and timed drills in a simulated terminal. |
| [**nkwork9999/ayatsumugi · integrations/herdr**](https://github.com/nkwork9999/ayatsumugi/tree/HEAD/integrations/herdr) | Opens a React DOM and application-state inspector in a Herdr TUI pane and checks the runtime; a private sidecar is required. |
| [**benbrackenbury/herder-zsh-refresh**](https://github.com/benbrackenbury/herder-zsh-refresh) | Refreshes idle zsh panes in Herdr TUI after shell configuration changes while leaving running foreground programs alone. |
| [**brenzim/herdr-db**](https://github.com/brenzim/herdr-db) | Opens lazysql in Herdr with database connection discovery for the current project. |
| [**asumaran/asdemokit**](https://github.com/asumaran/asdemokit) | Records the README demo GIFs of herdr plugins (asciinema + agg, scripted against an isolated herdr session). |
| [**aneym/herdr-gcal**](https://github.com/aneym/herdr-gcal) | Shows a Google Calendar agenda, month grid, event previews, and calendar toggles in an fzf-driven Herdr TUI panel. |
| [**tamdogood/herdr-pr-workflow**](https://github.com/tamdogood/herdr-pr-workflow) | Prompts the focused agent to create or merge the current branch’s pull request through a Herdr TUI action. |
| [**wenPKtalk/herdr-translate**](https://github.com/wenPKtalk/herdr-translate) | Translates selected Herdr TUI pane text with translate-shell and displays the result in a popup. |
| [**cndreisbach/herdr-gitu**](https://github.com/cndreisbach/herdr-gitu) | Opens the gitu Git client in a Herdr TUI split or tab with toggle-to-close shortcuts. |
| [**kedwards/herdr-awst**](https://github.com/kedwards/herdr-awst) | Selects AWS profiles and opens awst connections from Herdr TUI while showing account and instance details. |
| [**spywhere/herdr-now-playing**](https://github.com/spywhere/herdr-now-playing) | Adds a music player and playback controls through Herdr keybindings. |
| [**miya10kei/herdr-plugin-sidebar**](https://github.com/miya10kei/herdr-plugin-sidebar) | Displays Google Calendar events and GitHub Actions run status in a split pane styled as a sidebar. |
| [**atomsbaza/herdr-ios-build-status-plugin**](https://github.com/atomsbaza/herdr-ios-build-status-plugin) | Runs an on-demand iOS build and test from a Herdr TUI pane and records a simulator screenshot on failure. |
| [**vrwolf1004/herdr-radio**](https://github.com/vrwolf1004/herdr-radio) | Plays Radio Browser stations audio-only in Herdr and shows the current station and playback state in the sidebar. |
| [**vrwolf1004/herdr-talk**](https://github.com/vrwolf1004/herdr-talk) | Adds a chat pane to Herdr for talking with people on other PCs, with direct LAN connections and Noise encryption. |
| [**ryutaro-asada/herdr-translate**](https://github.com/ryutaro-asada/herdr-translate) | Translates text selected in a pane with one key and shows the result in a popup. Uses macOS Translate through Shortcuts by default, with an alternative engine. |
| [**doominkim/herdr-postman**](https://github.com/doominkim/herdr-postman) | Runs an unofficial Postman client in Herdr with local collections and cloud workspaces. Sends requests through Postman CLI and shows responses, headers, and test results. |
| [**dougcunha/herdr-plugins**](https://github.com/dougcunha/herdr-plugins) | Dispatches GitHub Actions workflows with ref and inputs from a Herdr pane, follows live jobs, and reruns failures through CI Dash. |
| [**baeroe/herdr-skilltri**](https://github.com/baeroe/herdr-skilltri) | Opens skilltri, an MCP gateway and agent skill manager with per-folder rules, in a Herdr TUI split, tab or popup. |
| [**freakynit/herdr-pagey**](https://github.com/freakynit/herdr-pagey) | Publishes a static build folder, HTML file or ZIP to Pagey hosting from the Herdr TUI. Manages sites, forms and analytics without leaving the terminal. |
| [**reidsolon/herdr-nowplaying**](https://github.com/reidsolon/herdr-nowplaying) | Shows and controls Spotify from the Herdr TUI with a player pane, search, tab bar line and CLI. Lists the player in the Agents panel. |
| [**shiv-io/dbt-pane**](https://github.com/shiv-io/dbt-pane) | Shows a panel of what a dbt worktree changes, including changed models, target, docs diffs, lineage and an agent's change plan. Runs in any terminal, tmux or as a Herdr TUI plugin. |
| [**vrwolf1004/herdr-simple-git**](https://github.com/vrwolf1004/herdr-simple-git) | Runs git pull, commit and push for configured repositories from a dock pane in the Herdr TUI, with short status messages and no AI. |
| [**vrwolf1004/herdr-stockpulse**](https://github.com/vrwolf1004/herdr-stockpulse) | Shows live stock prices and daily trend indicators in a Herdr TUI dashboard and the Agents sidebar, using Yahoo Finance with an optional iTick fallback. |
| [**vrwolf1004/herdr-timekit**](https://github.com/vrwolf1004/herdr-timekit) | Shows the current time, world clocks, a timer and a counter in one block at the bottom of the Herdr TUI sidebar. |
| [**gdarmont/herdr-claude-links**](https://github.com/gdarmont/herdr-claude-links) | Opens claude-cli:// links from a browser, Slack or a document in a new Herdr TUI workspace instead of a new terminal window on macOS and Linux. |
| [**matiaz/herdr-pulse**](https://github.com/matiaz/herdr-pulse) | Adds a side dock to Herdr TUI with a GitHub or Claude Code activity heatmap, your pull requests waiting on you, and a git panel that stages, commits, pushes and opens PRs with AI-written messages. |
| [**baeroe/herdr-lazy1mcp**](https://github.com/baeroe/herdr-lazy1mcp) | Runs the lazy1mcp terminal UI for 1MCP servers in a Herdr TUI split, its own tab, or a popup. |
| [**EdTheBearded/herdbake**](https://github.com/EdTheBearded/herdbake) | Routes bitbake menuconfig, devshell, and ccmake terminal spawns into Herdr TUI popups, splits, or tabs instead of external terminal windows. |
| [**dhasdiel/herdr-gradle-toolbar**](https://github.com/dhasdiel/herdr-gradle-toolbar) | Adds Gradle build, test, check, clean, and run actions to Herdr TUI that execute in a shared bottom split. Finds the nearest gradlew and offers a popup task picker, tuned for Kotlin Multiplatform projects. |

### Setup, packages, and version management

*55 projects. Guides, configuration bundles, installers, package definitions, and tools for reproducible Herdr environments.*

| Project | What it does |
|---|---|
| [**speardragon/herdr-plugin-manager**](https://github.com/speardragon/herdr-plugin-manager) | A small in-terminal menu for browsing, installing, updating, enabling, and disabling Herdr plugins through the standard plugin command-line interface. |
| [**mifunedev/agro**](https://github.com/mifunedev/agro) | Runs Herdr inside a Docker workspace for coding agents on a laptop or remote VM, installed with `agro tool install herdr`. Parallel agents use separate git worktrees, work continues after the terminal disconnects, and you choose the harness: Claude Code, Codex, Pi, OpenCode, or T3 Code. |
| [**joeseesun/herdr-guide**](https://github.com/joeseesun/herdr-guide) | A Chinese-language practical guide that explains what Herdr is useful for and how to get started. |
| [**natori-hrj/herdr-lazy**](https://github.com/natori-hrj/herdr-lazy) | A declarative Herdr plugin manager with a dedicated terminal interface, a lockfile, version pinning, synchronization from one list, and support for prebuilt binaries. |
| [**Yassimba/loom**](https://github.com/Yassimba/loom) | A curated collection of agent skills, Pi packages, and Herdr plugins with a single command-line setup tool. |
| [**diegopzz/herdr-updater**](https://github.com/diegopzz/herdr-updater) | Keeps Herdr and its plugins current across a whole fleet, safely. |
| [**garavitgabriel/claude-remote-kit**](https://github.com/garavitgabriel/claude-remote-kit) | Sets up Herdr, Tailscale, and Termius for remotely accessing coding agent sessions from a phone. |
| [**pedrogiroldo/agentbox**](https://github.com/pedrogiroldo/agentbox) | Runs Herdr, Claude Code, Codex, OpenCode, and mobile-friendly Neovim in an Ubuntu container reachable over SSH. |
| [**ram4-dev/herdr-config**](https://github.com/ram4-dev/herdr-config) | Installs pinned Herdr TUI plugins and portable keybindings with configuration snapshots and rollback. |
| [**hdosys/herdr-sandbox**](https://github.com/hdosys/herdr-sandbox) | Runs coding agents in disposable Windows Sandbox workstations isolated from the host. |
| [**kevinpita/herdr-nix**](https://github.com/kevinpita/herdr-nix) | Installs Nix packages for the Herdr app, herdr-core, and Herdr TUI, with Home Manager and NixOS modules for the TUI. |
| [**Ra77a3l3-jar/herdnix**](https://github.com/Ra77a3l3-jar/herdnix) | Installs Herdr plugins and configuration through a Nix module. |
| [**sohilladhani/tmux2herdr**](https://github.com/sohilladhani/tmux2herdr) | Converts tmux 3.x configuration to Herdr TUI configuration and reports unsupported or partially translated settings. |
| [**spfr/tuidev**](https://github.com/spfr/tuidev) | Installs a terminal dev environment for coding agents with an optional Herdr pack, including a Herdr config and SSH machines. Also sandboxes Claude Code and Codex and can undo the install. |
| [**aronjanosch/roost**](https://github.com/aronjanosch/roost) | Runs a Docker container that hosts Herdr and your coding agents on an always-on machine you reach over SSH. Ships a setup skill that walks an agent through git identity and tool login. |
| [**Amore-Labs-Inc/femme**](https://github.com/Amore-Labs-Inc/femme) | Sets up a server that keeps Claude Code, Codex and Pi running under Herdr after you close the laptop. Includes a Herdr plugin that forks a local agent and its folder onto the server. |
| [**jiteshy/ghostty-herdr-wizard**](https://github.com/jiteshy/ghostty-herdr-wizard) | Runs one script that sets up a Mac with Ghostty, Herdr and agent integrations, including notifications. Records changes so it can revert them. |
| [**berryk/herdr-cloud**](https://github.com/berryk/herdr-cloud) | Deploys Herdr and Claude Code in Cloudflare Containers as a per-project browser workspace on your own account. Sleeps when idle and wakes where you left off. |
| [**ariel-ps/herdr-setup**](https://github.com/ariel-ps/herdr-setup) | Installs a ready-to-use Herdr workspace on macOS, Ubuntu, Debian or Fedora with colored panes, alerts, saved layouts and lazygit. Each plugin can be enabled separately. |
| [**quijotevitruvio/HerdrSpanis**](https://github.com/quijotevitruvio/HerdrSpanis) | Installs a Spanish-language build of Herdr beside the official release and keeps your config. Includes commands to switch back to English and to update after new Herdr releases. |
| [**dio16/herdr-auto-update**](https://github.com/dio16/herdr-auto-update) | Checks installed Herdr plugins for newer upstream commits and reports them, and reinstalls updated versions when you set the auto policy. |
| [**GoldenBerry-SO/devbox**](https://github.com/GoldenBerry-SO/devbox) | Provisions a Hetzner development server with Ansible and Herdr TUI for persistent remote agent sessions. |
| [**nklmilojevic/herdr-flake**](https://github.com/nklmilojevic/herdr-flake) | Installs official Herdr TUI release binaries with a Nix flake and optional Home Manager module. |
| [**AodhanHayter/herdr-nix**](https://github.com/AodhanHayter/herdr-nix) | A Nix flake for installing Herdr on Intel and ARM macOS or Linux, with automated upstream release tracking and a Cachix binary cache. |
| [**lachieh/vfox-herdr**](https://github.com/lachieh/vfox-herdr) | Installs stable or preview Herdr TUI releases through mise with checksum verification and shell completions. |
| [**patdx/sido-askpass**](https://github.com/patdx/sido-askpass) | Opens a temporary Herdr TUI pane for sudo password prompts when an agent lacks an interactive TTY. |
| [**conda-forge/herdr-feedstock**](https://github.com/conda-forge/herdr-feedstock) | Packages Herdr TUI for installation through conda-forge. |
| [**orange4664/herdr-remote-workspace**](https://github.com/orange4664/herdr-remote-workspace) | Runs Herdr locally while agents work on an SSH host with Mutagen-synchronized projects. |
| [**0xMMA/herdr-claude-autoupdate**](https://github.com/0xMMA/herdr-claude-autoupdate) | Restarts idle Claude Code panes onto the newly installed version in place, keeping the session, flags, and unsent draft. |
| [**progamesigner/sleipnir**](https://github.com/progamesigner/sleipnir) | Builds a container image that runs herdr-core and Herdr TUI under s6 with Tailscale, Moshi, and agent CLIs, so the Herdr app can connect to a hosted agent fleet over SSH. |
| [**giannisp09/herdr-tailscale-setup**](https://github.com/giannisp09/herdr-tailscale-setup) | Sets up a Linux VM to keep Herdr coding-agent sessions running remotely over Tailscale. |
| [**narrowstacks/pxe-agent-box**](https://github.com/narrowstacks/pxe-agent-box) | Creates a configurable Proxmox Debian development VM with a persistent Herdr TUI session, coding agents, and remote access tools. |
| [**jedarden/agentists-quickstart**](https://github.com/jedarden/agentists-quickstart) | Bootstraps a headless server with Herdr TUI, Claude Code, and Codex, then starts the selected agent in a persistent session. |
| [**barnuri/herdr-auto-update**](https://github.com/barnuri/herdr-auto-update) | Keeps herdr always up to date, auto patch/minor/major updates with live handoff. |
| [**Production-Grade/herdr-setup**](https://github.com/Production-Grade/herdr-setup) | Offers a reusable Herdr TUI starter configuration, team workspace conventions, and a first-session walkthrough. |
| [**adams100111/omarchy-themed-devtools**](https://github.com/adams100111/omarchy-themed-devtools) | Applies Omarchy theme colors to Herdr TUI and other command-line tools. |
| [**maxart/uniterm-benchmark**](https://github.com/maxart/uniterm-benchmark) | Benchmarks Herdr TUI, Uniterm, and optionally tmux with equivalent terminal workloads and reproducible reports. |
| [**latest-debs/herdr-debian**](https://github.com/latest-debs/herdr-debian) | Packages Herdr TUI for Debian as a `.deb`. |
| [**spr-networks/spr-herdr**](https://github.com/spr-networks/spr-herdr) | Runs a Herdr TUI inside an SPR-managed KVM microVM. |
| [**hao-github-0216/remote-workspace-setup**](https://github.com/hao-github-0216/remote-workspace-setup) | Sets up persistent remote Herdr TUI workspaces over SSH and Mosh, including recovery after reboot. |
| [**YiannisDermitzakis/herdr-setup**](https://github.com/YiannisDermitzakis/herdr-setup) | Copies and synchronizes Herdr TUI configuration across machines and prepares coding agents for session restoration. |
| [**harveyfullstack/herdr-dist**](https://github.com/harveyfullstack/herdr-dist) | Distributes a pinned Herdr TUI Linux binary for the Box runtime. |
| [**yigitkonur/herdr-wezterm-setup**](https://github.com/yigitkonur/herdr-wezterm-setup) | A macOS terminal configuration that uses Herdr as the multiplexer and WezTerm as the keyboard-routing layer. |
| [**DavidTWhitlatch/dotfiles-template**](https://github.com/DavidTWhitlatch/dotfiles-template) | A shareable macOS dotfiles template with zsh, Oh My Zsh, Oh My Posh, Herdr, Git template hooks, and a symlink-based setup. |
| [**chrisjohnson/asdf-herdr**](https://github.com/chrisjohnson/asdf-herdr) | Installs and switches Herdr TUI versions with asdf using prebuilt macOS and Linux binaries. |
| [**ccyisafool/herdr-terminal**](https://github.com/ccyisafool/herdr-terminal) | Provides a thin, branded Ghostty client that starts Herdr by default. |
| [**2lab-ai/homebrew-tap · Formula**](https://github.com/2lab-ai/homebrew-tap/tree/main/Formula) | Installs the Herdr-derived herdr-mx distribution through Homebrew stable and preview formulae. |
| [**RobLoach/asdf-herdr**](https://github.com/RobLoach/asdf-herdr) | Installs Herdr TUI releases with asdf, including explicitly selected preview builds. |
| [**shaiu/ha-herdr**](https://github.com/shaiu/ha-herdr) | Runs a Herdr server with Claude Code as a Home Assistant app (formerly add-on), so the HA box appears as a saved SSH machine in your Herdr client. Includes key-only SSH, an ingress panel attached to the same session, and Home Assistant tools through ha-mcp. |
| [**julienpoirou/herdr-plugin-manager**](https://github.com/julienpoirou/herdr-plugin-manager) | Installs Herdr plugins from GitHub, GitLab, Gitea, bare repositories, or local directories with a review step and rollback. Includes a Ratatui popup and a scriptable herdr-pm CLI. |
| [**azyu/herdr-fleet-update**](https://github.com/azyu/herdr-fleet-update) | Updates brew, Claude Code and Codex on every machine Herdr is connected to, then restarts Herdr only where a running agent's CLI changed so agents resume on the new binaries. |
| [**justinbarry/herdr-omp-autoupdate**](https://github.com/justinbarry/herdr-omp-autoupdate) | Keeps omp up to date by running its update on Herdr events, then restarts idle OMP panes with /restart when their composer is empty. |
| [**alexg0/herdr-prezto**](https://github.com/alexg0/herdr-prezto) | Adds Herdr completions, slow-command notifications, and pane helpers to Prezto, with a read-only Herdr TUI action that checks the setup and prints manual install steps. |
| [**massdo/herdr-marketplace**](https://github.com/massdo/herdr-marketplace) | Searches, reads, installs, and updates Herdr TUI plugins from inside the terminal. |
| [**Austinsuyoyo/herdr-autoreload**](https://github.com/Austinsuyoyo/herdr-autoreload) | Reloads the Herdr TUI configuration when `config.toml` changes and displays diagnostics for rejected edits. |
