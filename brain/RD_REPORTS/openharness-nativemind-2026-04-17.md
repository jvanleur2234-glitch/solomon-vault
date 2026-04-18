# RD Report: OpenHarness + NativeMind Extension

**Date:** April 17, 2026
**Queue status:** Both installed, analyzed, queued

---

## REPO 1: OpenHarness (HKUDS)

**What it is:** Ultra-lightweight Python CLI agent framework — a Claude Code alternative. 11,733 lines of Python vs Claude Code's 512,664 (44x lighter), delivering 98% of essential tools at 2.3% of the code.

**Architecture — 10 subsystems:**
- `engine/` — agent loop (query → stream → tool-call → loop)
- `tools/` — 43 tools (Bash, create_or_rewrite_file, edit_file, Grep, WebSearch, MCP, Agent spawning, etc.)
- `skills/` — on-demand .md knowledge files, compatible with anthropics/skills
- `plugins/` — compatible with claude-code plugins (12 tested)
- `permissions/` — multi-level safety (Default/Auto/Plan modes, path rules)
- `hooks/` — PreToolUse/PostToolUse lifecycle events
- `coordinator/` — multi-agent spawning and team coordination
- `memory/` — persistent cross-session knowledge
- `mcp/` — Model Context Protocol client
- `tasks/` — background task management

**CLI:** `oh` command with subcommands for MCP, plugin, auth management. Supports `--output-format json/stream-json` for programmatic use.

**Key differentiator:** Pure research/builder tool — very transparent about harness architecture, great for understanding how agent frameworks work. Compatible with anthropics skills and claude-code plugins out of the box.

**Use case for Solomon OS:** The coordinator/multi-agent subsystem is interesting — could inspire how Solomon Bus spawns parallel workers. The plugin compatibility means we could load anthropics skills directly.

**Recommendation:** SKILL — study the coordinator and hooks architecture for Solomon Bus improvement.

---

## REPO 2: NativeMind Browser Extension

**What it is:** Privacy-focused browser extension (Chrome/Firefox) that brings local AI to your workflow via Ollama or WebLLM. 100% on-device, no cloud, AGPL v3.

**Tech stack:** Vue 3 + TypeScript, WXT (Web Extension framework), TailwindCSS, AI SDK

**Features:**
- AI chat in browser sidebar
- Context-aware memory across tabs
- AI-powered local web search
- Page summarization + translation
- PDF chat + image chat
- Writing tools (rewrite, proofread, tone adjustment)
- Quick Actions (custom skills per workflow)
- Model switching (Ollama or WebLLM)

**Quick Actions system:** Users can create custom skills that adapt NativeMind to their workflow — similar in concept to our skills system but for end-users, not developers.

**Comparison to our stuff:**
- vs Russell Tuna Bot: NativeMind is a browser-based UI overlay; Russell is a Telegram bot. Different surfaces, same underlying Ollama models.
- vs Solomon OS skills: NativeMind's Quick Actions are user-facing workflow shortcuts. Our skills are agent knowledge systems. Somewhat analogous but different abstraction levels.

**Recommendation:** SKILL — The Quick Actions UX pattern is worth studying for Hermes skill UX. Also potential distribution channel: NativeMind could be a client that connects TO our Solomon Bus API.

---

## MetaClaw — USELESS

`metaclaw` pip package installed as part of the request. It's literally a placeholder package with zero functionality. Not worth anything.

---

## Priority Verdict

**OPENHARNESS:** 🟡 Worthwhile — study the coordinator/hooks architecture, potential Solomon Bus improvement
**NATIVEMIND:** 🟡 Worthwhile — Quick Actions UX pattern + potential as distribution client for Solomon OS
**METACLAW:** 🟢 Nice to have — it's a placeholder, nothing there

**Overall:** Both are interesting but neither is a new AI paradigm or urgent competitive threat. Queued as general research, normal priority.