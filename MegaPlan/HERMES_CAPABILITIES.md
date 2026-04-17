# Hermes Capabilities
**Last Updated: April 17, 2026**

## agentic-stack (April 17, 2026)
- **Repo:** codejunkie99/agentic-stack — 1.7K stars, MIT
- **Forked:** jvanleur2234-glitch/solomon-os-agentic-stack
- **What it does:** Portable `.agent/` folder with 4 memory layers (working/episodic/semantic/personal), progressive skill loading, host-agent review protocol (graduate.py/reject.py), adapters for Claude Code/Cursor/Windsurf/Hermes/OpenCode/OpenClient
- **KEY PATTERN:** Host agent reviews AI-generated lessons. No unattended reasoning. No provider lock-in.
- **LINK fit:** ★★★★★ — #memory #self-improvement #hermes #solomon-os

## Anything Analyzer (April 17, 2026)
- **Repo:** Mouseww/anything-analyzer — MIT license
- **Forked:** jvanleur2234-glitch/anything-analyzer
- **What it does:** All-in-one packet capture (CDP browser + MITM proxy) + AI auto-analysis (API reverse, security audit, JS crypto extraction). Built with Electron + React + Python MITM + MCP server
- **Use for:** Reverse engineer any app/website API → build integrations → resell access. Protocol analysis as a service.
- **LINK fit:** ★★★★★ — #protocols #integrations #revenue

## egregore (April 17, 2026)
- **Repo:** egregore-xyz/egregore — shared mind for AI teams
- **What it does:** Team AI that remembers everything across sessions. Shared episodic + semantic memory across all agents.
- **Use for:** Multi-agent teams that need shared context. Every agent contributes to a common knowledge base.
- **LINK fit:** ★★★★☆ — #multi-agent #shared-memory

## production-saas-starter (April 17, 2026)
- **Repo:** moasq/production-saas-starter — Next.js 16 + Go 1.25 B2B SaaS
- **Forked:** jvanleur2234-glitch/solomon-production-saas-starter
- **What it does:** Enterprise SaaS boilerplate: Next.js 16, Go Gin, PostgreSQL+pgvector, Docker, Stytch auth, Polar.sh billing, RAG pipeline
- **Use for:** Spin up paid B2B SaaS in days. Stytch B2B SSO + Polar.sh = full billing stack
- **LINK fit:** ★★★★☆ — #saas #starter #revenue

## CloudBrowser (April 17, 2026)
- **Location:** jack-connect/cloud-browser/
- **What it does:** Hyperbrowser equivalent — AI-controlled browser with Playwright CDP + Ollama agentic reasoning. Create session → submit task → get results. Local-only, no API keys.
- **For JackConnect:** Browser AI that can navigate MLS, CRM, email for real estate agents
- **Status:** API server ready on port 9876

## Cabinet (April 17, 2026)
- **Location:** jack-connect/cabinet/
- **What it does:** AI-first startup OS — knowledge base + AI agents + scheduled jobs + Kanban boards. Git-backed history. Self-hosted. Drop HTML apps in any folder.
- **For JackConnect:** Jack's personal AI team brain — all agents, all memory, all work in one place

## Cognee Memory Layer (April 17, 2026)
- **Location:** jack-connect/cognee/
- **What it does:** Structured memory for LLMs — graph + vector search over any data. Pipeline: add text/files/tables → cognify → search
- **For JackConnect:** Long-term memory for Jack's real estate business — client history, deal notes, market data

## Watch Once Engine (April 17, 2026)
- **Location:** jack-connect/watch-once/
- **What it does:** Record a workflow once → AI extracts the steps → generates autoMate script → permanent automation
- **For JackConnect:** "Watch once, automate forever" — Jack does CMA once → system learns → never manually again

## JackConnect Dashboard (April 17, 2026)
- **Location:** jack-connect/jack-dashboard/
- **What it does:** Homepage替代方案 — 50+ service widgets (Ollama, Pinecone, Home Assistant, Plex, etc.)
- **For JackConnect:** Jack's personal ops dashboard — one URL, everything he needs to run his AI team

## Supported Model Providers

| Provider | Env Var | Model | Status |
|----------|---------|-------|--------|
| Ollama | (local) | qwen3:1.7b, llama3.2 | ✅ |
| OpenAI | `OPENAI_API_KEY` | GPT-4o, GPT-4o-mini | ✅ |
| NVIDIA | `NVIDIA_API_KEY` | minimax-m2.5 via build.nvidia.com | ✅ |
