# Hermes Capabilities
**Last Updated: April 17, 2026**

## Agency Agents — 810K Stars AI Employee Templates (April 18, 2026)
- **Repo:** github.com/msitarzewski/agency-agents — 810K stars, MIT License
- **Cloned:** /home/workspace/agency-agents/ (full repo, 21 categories, 140+ roles)
- **Key templates copied:** brain/AGENT_TEMPLATES/ (10 highest-value roles for AI Staffing Agency)
- **What it does:** 147 specialized AI agents across 12 divisions (engineering, design, marketing, sales, product, QA, support, etc.) — each with full personality, workflow, success metrics, and production-ready deliverables. Works with Claude Code, Cursor, Gemini CLI, Windsurf, OpenCode.
- **Business fit:** DIRECT — these are the exact "AI workers" businesses hire from an AI staffing agency. Map client needs → select right agent template → Russell Tuna /fork delivers the work.
- **For AI Staffing Agency:** `sales-outbound-strategist` for lead gen, `marketing-seo-specialist` for SEO work, `sales-account-strategist` for upsells, `support-support-responder` for customer service, etc.
- **Next step:** Build Telegram Role Selector so clients can pick an AI worker by name/need
- **LINK fit:** ★★★★★ — #ai-staffing #ready-to-deploy #business-revenue

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

## Runline — 188 API Plugins for AI Agents (April 17, 2026)
- **Repo:** Michaelliv/runline — npm package
- **Installed:** `npm install -g runline`
- **What it does:** JavaScript sandbox (QuickJS WASM) that gives agents safe execution of 188 API plugins. Plugins run outside sandbox with full Node.js access. `runline exec 'return await stripe.customer.list()'`
- **Plugins:** github, stripe, hubspot, salesforce, airtable, notion, linear, slack, sendgrid, twilio, shopify, clickup, jira, close, bullhorn + 178 more
- **Russell Tuna Integration:** `/runline` command added to russell_bot.py — any of 188 API actions via Telegram
- **Use for:** API actions without writing integration code. Every API = one JS line.
- **LINK fit:** ★★★★★ — #integrations #ai-staffing #plugins

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

## Facebook Ads MCP Server (April 17, 2026)
- **Repo:** gomarble-ai/facebook-ads-mcp-server — MIT license
- **Cloned:** /home/.z/workspaces/con_d8HQ6zgAf8q434AC/facebook-ads-mcp-server/
- **Forked:** jvanleur2234-glitch/facebook-ads-mcp-server
- **What it does:** MCP server wrapping Meta Graph API v22.0. Tools: list_ad_accounts, get_adaccount_insights, get_campaign_insights, get_adset_insights, get_ad_insights, get_activities, + full CRUD on campaigns/ad sets/ads/creatives.
- **Authentication:** `--fb-token YOUR_META_ACCESS_TOKEN`
- **For Solomon OS:** Russell Tuna reads client ad performance data → optimization reports for AI Staffing Agency. Hermes can pull Facebook Ads data directly via MCP router.
- **LINK fit:** ★★★★☆ — #facebook-ads #meta #insights #analytics #ai-staffing

## GUARDIAN OS (Cyber Defense)
- **Location**: `/home/workspace/solomon-vault/raw/SOLOMON_GUARDIAN.md`
- **Core innovation**: Adversarial self-improvement loop — Attack Team and Defense Team run 24/7 in parallel. The ONLY rule: attackers must win. Every successful breach → automatic learning → patch deployed → system gets harder. Loop never ends.
- **Attack Team**: Recon, Exploit, Vuln Research, Red Team, LOLbins agents
- **Defense Team**: Hardening, Detection, Response, Forensics, Threat Intel agents
- **Self-improvement**: After every successful attack: root cause → fix deployed → detection rule created → attack team briefed on closed vector → new attack surface explored

## Supported Model Providers

| Provider | Env Var | Model | Status |
|----------|---------|-------|--------|
| Ollama | (local) | qwen3:1.7b, llama3.2 | ✅ |
| OpenAI | `OPENAI_API_KEY` | GPT-4o, GPT-4o-mini | ✅ |
| NVIDIA | `NVIDIA_API_KEY` | minimax-m2.5 via build.nvidia.com | ✅ |