# RD Report: Puter

**URL:** https://github.com/HeyPuter/puter  
**Stars:** 40.5k | **License:** AGPL-3.0 | **Lang:** JavaScript (82%), TypeScript (12%)  
**Status:** 🟡 Worthwhile — High-value reference architecture

---

## What It Is

Puter is a full-featured web operating system that runs entirely in the browser. Think: personal cloud + remote desktop + file manager + app platform — all self-hostable, all open source. It's the most complete webtop implementation I've seen in the open-source world.

Core capabilities:
- File manager with local + remote storage support
- App ecosystem: code editor, terminal, image viewer, games
- Remote desktop for servers/workstations
- Platform for building/publishing web apps
- Cross-device sync via self-hosted server
- 367 contributors, 5,451 commits, very active

## What We'd Use It For

**Solomon Browser architecture reference.** Puter has already solved the hardest problems:
1. **Window manager** — multi-window, drag/drop, z-index, resize
2. **File system abstraction** — works with localStorage, IndexedDB, and remote backends
3. **App sandboxing** — each app runs in isolation
4. **Cross-device sync** — sync state across browsers via a server

Rather than building from scratch, we embed Puter as the OS shell inside Solomon Browser (as a Chrome extension). Solomon provides the AI brain; Puter provides the OS UX.

## How It Compares to What We Have

| | Puter | Solomon Browser (plan) |
|---|---|---|
| OS shell | ✅ Done | Planned |
| AI integration | ❌ None | Core feature |
| Hermes memory | ❌ None | ✅ Built-in |
| vPhone/VoIP | ❌ None | ✅ Planned |
| Extension model | ❌ No | ✅ Chrome extension |

## Recommendation

**FORGE — Use as architecture reference, not fork.**

- Study Puter's window manager + FS abstraction for Solomon Browser
- Embed Puter inside the Solomon Browser Chrome extension as the OS shell
- Add Solomon AI features on top (Hermes, JackConnect, Solomon Air)
- AGPL-3.0 license: if we fork directly, we must open-source. Instead, we study and inspire.