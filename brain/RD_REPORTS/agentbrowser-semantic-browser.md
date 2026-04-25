# AgentBrowser — Semantic Browser Runtime for AI Agents

**Fork:** `AshtonVaughan/agentbrowser` → already in workspace
**Source:** https://github.com/ashtonvaughan/agentbrowser (MIT?)
**Date:** 2026-04-25

---

## What It Does

TypeScript-based browser runtime designed for AI agents (not humans). Exposes semantic, task-oriented actions rather than raw DOM operations.

Key innovations:
- **Semantic observation**: page navigation returns structured model (page type, data, available actions) — reduces token cost
- **Dynamic tool registry**: available actions adapt to current page
- **Site memory**: first visit analyzed fully; future visits faster, zero-LLM-cost reloads
- **Self-healing**: CAPTCHA handling, stale selector recovery, state verification
- **Bot detection bypass**: stealth integration
- **MCP server compatible**: integrates with Claude Code, LangChain, AutoGen
- Parallel task management

## Solomon OS Fit

**FORGE** — semantic observation + dynamic tool registry is a major token efficiency innovation. Site memory = persistent context for browser tasks. Maps to ClawLess/Hermes browser layer. MIT license permits direct use.

## Status

**FORGE** — apply semantic observation pattern to ClawLess. Dynamic tool registry based on page type is novel and valuable.