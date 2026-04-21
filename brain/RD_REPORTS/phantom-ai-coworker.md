# RD Report: Phantom by ghostwright — AI Coworker With Its Own Computer

**URL:** https://github.com/ghostwright/phantom
**Date:** 2026-04-21
**Platform:** GitHub
**Stars:** 1,270+
**License:** Apache 2.0
**Version:** 0.18.2 (822 tests)

## What It Is

Phantom is an autonomous AI co-worker that runs as a persistent Bun process on a VM. It wraps the Claude Agent SDK (Opus 4.6), maintains vector-backed memory across sessions, rewrites its own configuration through a validated self-evolution engine, communicates via Slack/Telegram/Email/Webhook, and exposes all capabilities as an MCP server. 27,000+ lines of TypeScript.

**Tagline:** "Give the AI its own computer."

## Core Differentiators

### 1. Self-Evolution Engine (THE KEY INSIGHT)
After every session, Phantom runs a 6-step reflection pipeline:
1. **Observe** — extract corrections, preferences, domain facts
2. **Critique** — compare session against current config
3. **Generate** — propose minimal targeted config changes
4. **Validate** — 5 gates: constitution, regression, size, drift, safety
5. **Apply** — write approved changes, bump version
6. **Consolidate** — periodically compress observations into principles

**Safety mechanism:** Sonnet 4.6 as cross-model judge (avoids self-enhancement bias). Triple-judge voting with minority veto — one dissenting judge blocks the change. Every version stored, can diff day 1 vs day 30, can roll back.

**This is the missing piece for Solomon OS.** The Autogenesis SEPL loop and gn hf iteration engine were both partial attempts at this. Phantom has the complete validated implementation.

### 2. Three-Tier Memory Architecture
- **Episodic** (Qdrant) — past experiences, session history
- **Semantic** (domain knowledge + contradiction detection)
- **Procedural** (workflow procedures)

Memory context is injected into every prompt. Agent remembers what you told it Monday and uses it Wednesday.

### 3. Dynamic MCP Tools
Creates tools at runtime that persist across restarts. One Phantom built a `send_slack_message` tool, registered it, and retired its old workaround. Tools survive restarts and work across sessions. Other agents connecting via MCP can use them too.

### 4. Multi-Channel Presence
Slack (Socket Mode, primary), Telegram (long polling), Email (IMAP/SMTP), Webhook (HMAC-SHA256), CLI. Agent extended itself to Discord when asked — explained the API, walked user through setup, spun up container automatically.

### 5. Security-First Design
- AES-256-GCM encrypted credentials via secure forms + magic-link auth
- Non-root Docker user (Claude Code CLI rejects --dangerously-skip-permissions as root)
- buildSafeEnv() passes only PATH, HOME, LANG, TERM, TOOL_INPUT — never leaks API keys to subprocesses
- No inline handlers (removed for RCE prevention) — only shell/script execution

## What Phantoms Have Actually Built (Real Production Demos)

1. **ClickHouse analytics platform from scratch** — Installed ClickHouse on own VM, downloaded 28.7M Hacker News rows, built dashboard, created REST API, registered as MCP tool for reuse.

2. **Self-extended to Discord** — Shipped with Slack/Telegram/Email/Webhook, no Discord. When asked, explained API, provided setup instructions, spun up container automatically. Permanently gained a channel it was never designed with.

3. **Built Vigil monitoring dashboard** — Discovered 3-star Vigil project, integrated into ClickHouse, built sync pipeline (30s batches), created real-time observability dashboard. 890,450 rows, 25 metrics, auto-refreshing.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Runtime | Bun (TypeScript-native, built-in SQLite, no bundler) |
| Agent | Claude Agent SDK (@anthropic-ai/claude-agent-sdk) with Opus 4.6, 1M context |
| Memory | Qdrant (vector DB, Docker) + Ollama (nomic-embed-text, local embeddings) |
| State | SQLite via Bun (sessions, tasks, metrics, evolution versions, scheduled jobs) |
| Channels | Slack (Socket Mode), Telegram (long polling), Email (IMAP/SMTP), Webhook, CLI |
| Web UI | Tailwind v4 Browser CDN + DaisyUI v5 |
| MCP | Streamable HTTP on /mcp, bearer token auth, 17+ tools |
| Infrastructure | Docker (compose), Specter VMs (Hetzner), systemd (bare metal) |

## Why Qdrant Over LanceDB
WAL durability with crash recovery. Native hybrid search (dense + BM25 sparse vectors). Named vectors for separate embedding spaces. Mmap mode for low memory. TypeScript REST client works with Bun (no NAPI addon risk).

## Key Files

| File | Purpose |
|------|---------|
| `src/evolution/engine.ts` | 6-step self-evolution pipeline (CORE DIFFERENTIATOR) |
| `src/memory/system.ts` | Memory coordinator — how three tiers connect |
| `src/agent/prompt-assembler.ts` | System prompt composition |
| `src/agent/runtime.ts` | Agent SDK query() wrapper + hooks |
| `src/mcp/server.ts` | MCP Streamable HTTP server |
| `src/channels/slack.ts` | Primary channel with owner access control |
| `phantom-config/constitution.md` | Immutable principles (evolution cannot modify) |
| `docs/self-evolution.md` | Full evolution pipeline documentation |
| `docs/security.md` | Auth, secrets, permissions, hardening |

## JCPaid/Solomon OS Integration Points

### IMMEDIATE (This Week)
1. **Fork Phantom** → adapt self-evolution engine for Solomon OS / Russell Tuna
2. **Study the 5-gate validation** → implement for Solomon Bus overnight worker
3. **Clone memory architecture** → Qdrant + Ollama for Solomon OS persistent memory
4. **Adopt buildSafeEnv pattern** → fix secrets in subprocesses across all agents

### SHORT TERM (This Month)
1. **Build JackConnect as Phantom-style coworker** — per-client VM with own memory and tools
2. **Implement triple-judge voting** for Solomon OS self-improvement loop
3. **Adopt dynamic MCP tools pattern** — agent creates tools at runtime, persists across restarts
4. **Study magic-link credential collection** → implement for Solomon OS secrets management

### MEDIUM TERM
1. **AI Employee Agency = Phantom-style coworkers for businesses** — each client gets their own Phantom
2. **Self-evolution for Russell Tuna** — apply 6-step pipeline via /fork pattern
3. **Second Brain Portal = Phantom dashboard** — serve dashboards on public URLs with auth

## Comparison to What We Have

| | Solomon OS (current) | Phantom (target) |
|---|---|---|
| Agent | Zo + Russell Tuna (general) | Opus 4.6 + Claude Agent SDK (specialized) |
| Memory | brain/ files (static) | Qdrant + Ollama (dynamic, searchable) |
| Self-evolution | None (planned via SEPL) | 6-step pipeline, 5-gate validation |
| Tools | Fixed at install | Created at runtime, persist |
| Credentials | Plain text .env | AES-256-GCM encrypted + magic link |
| Evolution safety | None | Sonnet judge + triple-vote minority veto |
| Channels | Telegram (manual) | Slack/Telegram/Email/Webhook/CLI (all wired) |

## Recommendation

🔴 **FORGE — CRITICAL. Clone immediately.**

This is the architecture JCPaid needs to become. The self-evolution engine solves the biggest gap in Solomon OS (the "gets measurably better every day" loop). The memory architecture validates what we planned via ML-Master HCC. The dynamic tools pattern is exactly what Hermes is trying to do.

Clone to `/home/workspace/phantom/` (already cloned). Read CLAUDE.md first (comprehensive architecture guide). Study `src/evolution/engine.ts` and `docs/self-evolution.md` for the 6-step pipeline.

**Priority:** Replace Solomon OS self-improvement architecture with Phantom's validated approach. This is the single most important RD finding since Agentic.Market (which validated the business thesis).

## Status

✅ Cloned to `/home/workspace/phantom/`
📁 Full RD report: `brain/RD_REPORTS/phantom-ai-coworker.md`
🔗 Source: https://github.com/ghostwright/phantom