# Agent Orcha — Declarative Multi-Agent Framework (Apr 27, 2026)

**Fork:** `jvanleur2234-glitch/agent-orcha-fresh` (MIT)
**Source:** https://github.com/ddalcu/agent-orcha

## What It Does
Declarative YAML-driven multi-agent orchestration framework with:
- Model-agnostic providers (OpenAI, Gemini, Anthropic, local LLMs)
- MCP (Model Context Protocol) native integration
- Built-in SQLite vector store + knowledge-graph mapping
- **P2P agent and LLM sharing** — encrypted peer-to-peer without central servers, per-peer rate limits
- Native desktop apps (macOS/Windows/Linux) + browser-based Studio dashboard
- SSL/security: rate-limited auth, SSRF protection, SQL injection hardening, sandboxed execution
- Browser tools: Chromium-based sandbox with CDP, noVNC, Vision Browser

## Why It Matters for Solomon OS
- P2P agent sharing directly competes with AgentFM's mesh networking — could enhance Hermes distributed capabilities
- Declarative YAML = operators can configure without code
- Desktop app + browser studio gives multiple UX options for JCPaid clients

## Fit: INTEGRATE
MIT licensed. Active 2026 release (latest v2026.409). P2P sharing is a direct competitor to AgentFM core — clone for monitoring. MCP native fits Hermes architecture.

## Key Files
- `README.md` — full architecture
- `orcha/` — core engine
- `p2p/` — peer-to-peer networking

## Action Items
- [ ] Fork to jvanleur2234-glitch
- [ ] Explore P2P sharing implementation for Hermes distributed mode
- [ ] Test MCP server discovery
