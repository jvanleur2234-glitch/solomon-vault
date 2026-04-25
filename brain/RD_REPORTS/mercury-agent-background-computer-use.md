# RD Report: Mercury Agent + Background Computer Use

**Date:** April 25, 2026  
**Channel:** Telegram  
**Type:** R&D Research — Agent Framework Evaluation

---

## 1. Background Computer Use (X Thread — actuallyepic)

**URL:** https://github.com/actuallyepic/background-computer-use  
**License:** MIT | **Stars:** 113 | **Language:** Swift (98%)

### What it is
A macOS native app that exposes a loopback HTTP API enabling AI agents (Codex, Claude, etc.) to control native apps, browser windows, and multi-window desktop workflows — WITHOUT taking over the user's pointer or requiring foreground focus. It reads window screenshots + Accessibility (AX) state and dispatches clicks, scrolls, typing, key presses, window motion against target windows.

This is the OpenAI Codex Computer Use demo, replicated in open source by anupam batra + cam — with a video showing real-time background control.

### Key Routes
- `GET /v1/bootstrap` → runtime manifest (baseURL, permissions)
- `POST /v1/list_apps`, `/v1/list_windows`, `/v1/get_window_state`
- `POST /v1/click`, `/v1/scroll`, `/v1/type_text`, `/v1/press_key`
- `POST /v1/drag`, `/v1/resize`, `/v1/set_window_frame`

### Architecture
- Swift native macOS app (requires macOS Accessibility + Screen Recording permissions)
- Self-signs for dev (creates local keychain identity automatically)
- Screenshot + AX tree fallback for targeting
- Token-efficient: can target by screenshot coordinates OR AX element index

### For Solomon OS
This is a **macOS-only** background computer control layer. Not a general agent — it's specifically for GUI automation on macOS. Could be integrated as a browser/Desktop automation skill for Hermes if we ever support macOS-hosted agents. Not directly usable in our Linux/sandbox environment.

**Use case comparison:**
| Capability | HyperAgent | viyv-browser | BackgroundCompUse |
|---|---|---|---|
| Real Chrome with auth | Yes | Yes | No (AX-based) |
| Cross-platform | Yes | Yes | macOS only |
| Background/non-focus | No | Yes | Yes |
| Open source | NOASSERTION | ~200 stars | 113 stars MIT |

**Recommendation:** SKIP for now — macOS-only, not relevant to current stack. Watch for Linux equivalents.

---

## 2. Mercury Agent (cosmicstack-labs/mercury-agent)

**URL:** https://github.com/cosmicstack-labs/mercury-agent  
**License:** MIT | **Status:** Active, trending this week

### What it is
Soul-driven AI agent with permission-hardened tools, token budgets, and multi-channel access (CLI + Telegram). Runs 24/7 as a daemon. Zero Docker required — runs bare metal on macOS/Linux.

### Core Differentiators

**Soul-Driven Identity**
Mercury uses markdown "soul" files (`soul.md`, `persona.md`, `taste.md`, `heartbeat.md`) for personality and identity. These are git-friendly, editable text files — no black-box configs. This is more granular than Hermes' persona system.

**Permission-Hardened Tools (Architectural, Not Bolt-On)**
Filesystem: scoped read/write paths (can't escape workspace)  
Shell: DENY list by default (blocks `sudo`, `rm -rf`, etc.)  
Approval: user can approve/deny individual actions before execution  
RBAC: per-extension permission gates

**Token Budgeting with Auto-Concise Mode**
Daily token budgets. When approaching limit, agent automatically switches to concise mode (summarizes history, reduces context). No equivalent in Hermes.

**Sandboxed Execution**
Linux: bubblewrap (read-only `/`, writable workspace only)  
macOS: sandbox-exec  
Each agent run is an isolated subprocess — not a process boundary, actual OS-level sandbox.

**Second Brain Memory**
SQLite-backed, 10 memory types, full-text search. Persistent structured context across sessions.

### Built-in Tools (31 total, 8 categories)
- Filesystem (scoped)
- Shell (deny list enforcement)
- Git
- Web
- Skills (Agent Skills spec — same as Hermes)
- Scheduler (cron + delayed)
- Messaging (Telegram)
- GitHub

### Models Supported
DeepSeek, OpenAI, Anthropic, Ollama (via OpenAI-compatible adapter)

### Comparison: Mercury vs Hermes

| Dimension | Mercury | Hermes |
|---|---|---|
| Identity | Soul files (markdown) | Personas + SOUL.md |
| Permission model | Architectural (filesystem scopes, shell deny list, approval flows) | RBAC rules |
| Token budgeting | Native (daily caps + auto-concise) | No |
| Sandbox | bubblewrap/sandbox-exec (OS-level) | Process isolation |
| Memory | SQLite Second Brain (10 types) | Files + RAG |
| Skills | Agent Skills spec (SKILL.md) | Agent Skills spec |
| Multi-channel | CLI + Telegram | Hermes (Telegram, web, etc.) |
| Self-improvement | No native loop | evolver integration |
| Docker required | No | Yes |
| License | MIT | MIT |
| Language | TypeScript | TypeScript |

### What Mercury Does Better
1. **Token cost control** — Auto-concise when approaching budget limits. Hermes has no equivalent.
2. **Shell security** — Deny-list approach to dangerous commands baked in. Hermes relies on rules.
3. **Permission granularity** — Filesystem scoping prevents workspace escape. Hermes doesn't restrict paths.
4. **Simpler deployment** — No Docker required. Runs as a native daemon. `mercury up` = installed and running.
5. **Background persistence** — Designed from the ground up for 24/7 daemon operation with auto-restart.

### What Hermes Does Better
1. **Multi-agent orchestration** — Agent Council, Captain Claw patterns.
2. **Self-improvement** — evolver integration, autonomous skill creation.
3. **Ecosystem** — MCP server native, broad tool integrations.
4. **Brain memory** — File-based long-term memory + graph RAG.
5. **Web/browser** — viyv-browser, hermes-webui.
6. **Broader platform** — Works on any OS with Node.js.

### Integration Potential
**FORGE** — Add Mercury as a second agent in Solomon OS for:
- Cost-controlled operations (token budgeting native, not Hermes rules)
- Sensitive tasks requiring filesystem scoping
- CLI-first workflows where Docker overhead is unwanted
- Cases where you'd want Hermes but need stronger permission guarantees

Mercury's TypeScript + SKILL.md pattern means it could coexist with Hermes as a specialized sub-agent. Run Mercury for high-security/low-cost tasks, Hermes for complex orchestration.

### What We'd Use It For
- Procurement research runs (budget-capped, don't overspend tokens)
- Client-facing sessions where shell command restrictions matter
- Any task where filesystem scoping prevents mistakes
- Cases where `mercury up` simplicity beats Docker complexity

**Recommendation:** FORGE — Clone and set up in workspace. Evaluate against Hermes for cost-sensitive tasks.

---

## Summary Table

| Repo | Stars | License | Use for Solomon OS | Recommendation |
|---|---|---|---|---|
| actuallyepic/background-computer-use | 113 | MIT | macOS GUI automation (future) | SKIP |
| cosmicstack-labs/mercury-agent | Trending | MIT | Second agent for cost-controlled, security-sensitive tasks | FORGE |