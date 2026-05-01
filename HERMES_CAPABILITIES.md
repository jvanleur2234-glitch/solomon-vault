## Hermes Workspace — Native Web UI (April 29/30, 2026)
- **Repo:** outsourc-e/hermes-workspace — just released TODAY
- **What it is:** Native web workspace for Hermes Agent with chat, terminal, profiles, knowledge browser, MCP settings, skills hub.
- **Viral:** 537 likes, 665 bookmarks, 27K views in hours. Released April 30, 2026.
- **Key features:**
  - Multi-profile management (create, switch, rename, delete)
  - Knowledge browser with document viewer
  - MCP server settings screen
  - Skills hub with marketplace search fallback
  - Context usage tracking and display
  - Clean UI — no CLI needed for clients
- **For JCPaid:** Client-facing web dashboard for their AI employee. Clients log in, see the AI working, interact with it through a clean web UI instead of terminal.
- **Status:** IMMEDIATE — Clone and deploy as client dashboard
- **Links:** https://hermes-workspace.com, https://github.com/outsourc-e/hermes-workspace

## hermes-paperclip-adapter — Hermes as Paperclip Employee (April 30, 2026)
- **Repo:** NousResearch/hermes-paperclip-adapter — MIT — 1K stars, 182 forks
- **What it does:** Official adapter from Nous Research. Runs Hermes Agent as a managed employee inside Paperclip's company structure. Bridges the two systems — Hermes reports task results, cost, and usage back to Paperclip.
- **Key features:**
  - 8 inference providers (Anthropic, OpenRouter, OpenAI, Nous, OpenAI Codex, ZAI, Kimi Coding, MiniMax)
  - Skills integration (scans both Paperclip-managed and Hermes-native skills from ~/.hermes/skills/)
  - Structured transcript parsing (Hermes stdout → typed TranscriptEntry objects with tool cards)
  - Session persistence (resumes across heartbeats, maintains conversation context)
  - MCP client support
  - Auto model detection from ~/.hermes/config.yaml
  - Session source tagging (keeps tool sessions separate from interactive history)
- **Architecture flow:**
  ```
  Paperclip (Heartbeat Scheduler + Issue System + Cost Tracking)
       └── hermes-paperclip-adapter
             └── Hermes Agent (30+ tools, memory system, session DB, skills, MCP client)
                   └── executes tasks via hermes chat -q
  ```
- **For JCPaid:** This is the core infrastructure. Paperclip = client-facing company management. Hermes = the AI employee doing the work. Adapter bridges both. MIT license = we deploy free for clients.
- **Install:** `npm install hermes-paperclip-adapter`
- **Status:** IMMEDIATE FORGE — Clone and set up now
- **Links:** https://github.com/NousResearch/hermes-paperclip-adapter

## Hermes Vault v0.4.0 — Tony Simons — AI Credential Broker (April 25, 22026)
- **Repo:** asimons81/hermes-vault — Apache-2.0
- **What it does:** Local-first credential broker for AI agents. Secrets never leave the vault. Credential health tracking (proactive expiring key alerts). Audit logs + verification reports. SHA-256 hash-chained tamper-evident audit trail.
- **For Solomon OS:** Credential health tracking, enterprise audit logs, secrets isolation, tamper-evident logs. Clients will demand all four.
- **Ecosystem:** Hermes Agent (NousResearch) + Hermes Vault + Hermes Katana (7-layer security: taint tracking, flow analysis, input scanner 30+ patterns, output scanner, policy engine, SHA-256 audit, HTTPS proxy)
- **Status:** FORGE — High Priority. Clone and integrate.
- **Links:** https://github.com/asimons81/hermes-vault, https://github.com/claudlos/hermes-katana

## NEWLY FORGED (April 26, 2026) — 20 repos added to workspace

### Critical Business Repos
- **mimeo** (K-Dense-AI/mimeo, MIT) — Turns any expert into a SKILL.md. Pipeline: disambiguate → discover → fetch → distill → cluster → author skill. JackConnect's killer feature for 300+ vertical agents.
- **midday** (midday-ai/midday, AGPL) — All-in-one freelancer business tool: invoicing, time tracking, Vault, Magic Inbox. Fork as JackConnect backend. Bun+React+Supabase stack matches ours. Get commercial license.
- **chief** (MiniCodeMonkey/chief, MIT) — Ralph Wiggum loop implementation for Solomon Bus. Claude Code job runner, one commit per task, clean git history. Study `cmd/chief/ralph/`.

### Memory & Knowledge
- **supermemory** (supermemoryai/supermemory, MIT, 16.7K stars) — mem0 competitor. ECL pipeline, 30+ data sources. Adopt vector+graph memory for Hermes.
- **MemOS** (MemTensor/MemOS, Apache-2.0, 8.5K stars) — Memory OS for LLMs. +43.70% accuracy vs OpenAI Memory. Local plugin: SQLite, hybrid FTS5+vector, skill evolution. Multi-agent sharing. Providers: OpenAI, Azure, Qwen, DeepSeek, **MiniMax**, Ollama, HF, vLLM.
- **cognee** (cognee/cognee, MIT) — Already cloned. Vector+graph memory for Hermes.

### Security
- **agentarmor** (Agastya910/agentarmor, MIT) — 8-layer defense-in-depth for agentic AI. OWASP ASI Top 10 coverage: ingestion, storage, context, planning, execution, output, inter-agent, identity.
- **agent-vault** (Infisical/agent-vault) — Agent secret management by Infisical.
- **clearwing** (Lazarus-AI/clearwing) — Security for AI agents.

### Self-Evolution
- **self_improving_coding_agent** (MaximeRobeyns/self_improving_coding_agent, MIT) — Skill tree evolution for Hermes. Self-bootstrapping proof.
- **self-evolving-agent** (RangeKing/self-evolving-agent, MIT) — Self-evolving patterns.
- **Recursive-Self-Improvement-AI-Agent** (ai-in-pm/Recursive-Self-Improvement-AI-Agent) — Recursive improvement loop.
- **evolver** (EvoMap/evolver) — Already cloned. Study for agent evolution patterns.

### Deliberation
- **council-of-high-intelligence** (0xNyk/council-of-high-intelligence) — Multi-agent council. Already cloned.
- **council** (dubs3c/council, MIT) — Already cloned. Council framework for Hermes.
- **Quorum** (Solvely-Colin/Quorum) — Already cloned. Multi-AI deliberation.

### Browser & Automation
- **agentbrowser** (ashtonvaughan/agentbrowser) — Already cloned. Structured page model + memory.
- **browserclaw-agent** (browserclaw/browserclaw-agent) — Already cloned. Anti-bot bypass + skill learning.
- **background-computer-use** (actuallyepic/background-computer-use) — Vision-based browser automation.
- **paperclip-vision** (aronprins/paperclip-vision) — Browser automation with vision.

### Infrastructure
- **puter** (HeyPuter/puter, MIT) — Open-source platform for AI apps. Full stack reference.
- **oasis** (camel-ai/oasis) — CAMEL AI's agent platform.
- **Reticulum** (markqvist/Reticulum) — P2P networking stack.
- **mercur** (mercurjs/mercur) — Agent framework.
- **hermes-katana** (claudlos/hermes-katana) — 7-layer security: taint tracking, flow analysis, input scanner 30+ patterns, output scanner, policy engine, SHA-256 audit, HTTPS proxy. Part of Hermes ecosystem.
- **agents** (livekit/agents, MIT) — Real-time AI agents with LiveKit.
- **mex** (theDakshJaitly/mex, MIT) — Persistent project memory for AI coding agents. Structured scaffold + drift detection CLI.
- **EvoAgentX** (EvoAgentX/EvoAgentX, MIT) — Self-evolving agents platform.
- **Awesome-Self-Evolving-Agents** (EvoAgentX/Awesome-Self-Evolving-Agents) — Survey of self-evolving agent patterns. SEPL loop, Ralph Wiggum, Buffer of Thoughts, AFlow.
- **rlm** (alexzhang13/rlm) — RL machine learning agent.
- **agent-council** (agent-council/agent-council) — Already cloned. Multi-agent council.
- **supermemory** — Memory layer for Hermes.
- **caf** — Facebook Ads MCP server (Gomarble).
- **show-me-the-money** (iamzifei/show-me-the-money) — Finance/trading agent.
- **clae** — AI agent framework.
- **facebook-ads-mcp-server** — MCP server for Facebook ads.
- **caf** — (getclawe/clawe) — Claude agent.

## vigile-cli — AI Agent Security Scanner (April 23, 2026)
- **Repo:** Vigile-ai/vigile-cli — Apache-2.0
- **What it does:** Security scanner for AI agent ecosystems. 59 detection rules for MCP servers (22 patterns) and agent skills (32 patterns). Detects tool poisoning, data exfiltration, instruction injection, malware delivery.
- **For Solomon OS:** Pre-deployment security scanning of Hermes MCP servers and skills. Add as guard-scanner skill for agentarmor-studio.
- **Status:** Forked ✅

## decentralized-inference — Mesh-LLM P2P Inference (April 23, 2026)
- **Repo:** michaelneale/decentralized-inference — Apache-2.0
- **What it does:** Pools spare GPU capacity across machines to expose OpenAI-compatible API. Pipeline parallelism + expert sharding for MoE. Cross-peer collaboration.
- **For AgentFM:** P2P compute grid for AI inference. Alternative to AgentFM, Hyperspace.
- **Status:** Forked ✅

## gecko-agent — Chrome Extension Browser Automation (April 23, 2026)
- **Repo:** Gecko51/gecko-agent — MIT
- **What it does:** AI-powered Chrome extension for browser automation. Think→act→observe loop, multi-model via OpenRouter, specialized LinkedIn/Airtable automation.
- **For browser-harness:** Easy-deploy Chrome extension alternative to HyperAgent.
- **Status:** Forked ✅

## microsoft/agent-framework — Enterprise Graph-Based Orchestration (April 23, 2026)
- **Repo:** microsoft/agent-framework — MIT (~9.7k stars)
- **What it does:** Cross-language (Python/.NET) agent framework with graph-based orchestration, time-travel debugging, human-in-the-loop. Enterprise-grade.
- **For research:** Study graph-based workflow patterns for Hermes orchestration improvements.
- **Status:** Already cloned ✅

## hyperspace-agi — Distributed P2P AGI System (April 23, 2026)
- **Repo:** hyperspaceai/agi — MIT
- **What it does:** Thousands of agents collaboratively train models via P2P. DiLoCo training, 195x compression, BitTorrent weight distribution, blockchain economics.
- **For AgentFM:** P2P compute grid for AI inference. Alternative to AgentFM, Hyperspace.
- **Status:** Already cloned ✅

## genericagent — Minimal Self-Evolving Framework (April 23, 2026)
- **Repo:** generic-agent/genericagent — MIT (GitHubDaily, ~1.8k stars)
- **What it does:** ~3,000 lines, 9 tools, self-evolving (task path → reusable skill). Browser/terminal/files/mobile ADB. Agent makes its own code commits.
- **For research:** Study simple self-evolution pattern (task → skill formation) without API costs.
- **Status:** Already cloned ✅

## evolver — Self-Evolving Prompt Engine (April 23, 2026)
- **Repo:** evolver-ai/evolver — MIT (GitHubDaily)
- **What it does:** Scans logs/errors → constrained prompt optimizations. 4 strategy modes (balanced, stable, rapid, emergency). EvoMap network for skill sharing.
- **For Hermes:** Add as evolver skill for self-improvement pipeline. Zero-cost behavioral evolution.
- **Status:** Already cloned ✅

## cognee — Vector+Graph Memory for AI Agents (April 23, 2026)
- **Repo:**ognee-ai/cognee — MIT (~15.9k stars)
- **What it does:** 6-line API to build persistent memory. Vector search + graph DB = connected, searchable memory. ECL pipeline, 30+ data sources, Ollama support.
- **For Hermes:** Memory layer. Alternative to RAG with relationship-aware graph storage.
- **Status:** Already cloned ✅

## gbrain — YC Second Brain for AI Agents (April 23, 2026)
- **Repo:** garrytan/gbrain — MIT (Y Combinator)
- **What it does:** Auto-transforms meetings, emails, tweets, schedules → structured knowledge. Pre-conversation context, post-conversation memory write. Local-first.
- **For Hermes:** Second brain integration. Consumer/professional context about the user.
- **Status:** Already cloned ✅

## captain-claw — Multi-Agent Orchestration + Agent Council (April 23, 2026)
- **Repo:** github.com/jvanleur2234-glitch/captain-claw (MIT)
- **What it does:** Full AI agent platform with Flight Deck dashboard (Agent Forge, Agent Council, Fleet Communication, Director Panel). 5-layer cognitive memory, autonomous dreaming/tension-tracking, 7 cognitive modes. 44 built-in tools. Multi-model (OpenAI/Claude/Gemini/Ollama).
- **Use for:** Structured deliberation (Agent Council), multi-agent team orchestration, cognitive architecture patterns.
- **LINK fit:** ★★★★★ — #deliberation #multi-agent #cognitive-architecture

## claude-synod-debate — Multi-Agent Judicial Deliberation (April 23, 2026)
- **Repo:** github.com/jvanleur2234-glitch/claude-synod-debate (MIT)
- **What it does:** 4-phase judicial debate (Solver/Critic/Defense/Synthesis) orchestrating Claude/Gemini/OpenAI. CRIS trust scoring. SID structured confidence format. 5 modes (review/design/debug/idea/general). Claude Code plugin (/synod).
- **Use for:** High-stakes decisions, architecture reviews, adversarial security modeling.
- **LINK fit:** ★★★★☆ — #deliberation #multi-agent #decision-making

## viyv-browser — Chrome Extension + MCP Browser Automation (April 23, 2026)
- **Repo:** github.com/jvanleur2234-glitch/viyv-browser (MIT)
- **What it does:** AI agent browser automation in user's real Chrome with auth sessions. Semantic targeting (define once, replay reliably). Batch execution, scheduled jobs, execution history/diff. Google Sheets integration via session cookies. MCP server for Claude Desktop/Cowork.
- **Use for:** Solomon Browser authenticated automation, recurring data collection, E2E testing, Google Sheets BI.
- **LINK fit:** ★★★★★ — #browser #mcp #automation #google-sheets
## hermes-webui — Clean Web UI for Hermes Agent (April 23, 2026)
- **Repo:** github.com/jvanleur2234-glitch/hermes-webui (MIT)
- **What it does:** Lightweight, zero-build web UI for Hermes Agent. Python + vanilla JS, three-panel layout (sessions/chat/files), full CLI parity, SSH tunnel support, session projects/tags, workspace browser, token ring visualization.
- **Use for:** Browser-based Hermes interaction without terminal. Multi-user profiles. Clean UI for clients.
- **LINK fit:** ★★★★★ — #hermes #ui #browser #zero-build

## KwaaiNet — P2P Decentralized AI Trust Graph (April 23, 2026)
- **Repo:** Kwaai-AI-Lab/KwaaiNet — MIT
- **What it does:** Rust/TypeScript P2P AI infrastructure with Decentralized Trust Graph (DTG). Nodes establish credentialed trust relationships without central control plane.
- **For AgentFM/Solomon Bus:** DTG architecture for inter-agent trust relationships. Competitor to AgentFM/Hyperspace. MIT licensed.
- **Status:** Forked ✅

## SupraWall — Deterministic Policy Layer for Hermes Agent (April 23, 2026)
- **Repo:** wiserautomatio/suprawall — MIT (presumed)
- **What it does:** Deterministic ALLOW/DENY gating for Hermes Agent tool calls. Local PII scrubbing. RSA-signed audit logs for every decision. Production-ready on PyPI.
- **For Solomon OS/Hermes:** Enterprise-grade security hardening layer for Hermes. Validates agentic security as a real product category. Directly complements agentarmor-studio.
- **Status:** RD report written, repo location unverified (search wiserautomatio on GitHub)

## LocalAI P2P — Decentralized llama.cpp Inference (April 23, 2026)
- **Repo:** mudler/LocalAI — MIT (13k+ stars), PR #2343 for P2P feature
- **What it does:** Fully decentralized, private P2P inference across machines. mDNS + DHT discovery, no cloud dependency, cross-NAT operation. GGUF models via llama.cpp.
- **For distributed AI compute:** Alternative to AgentFM for LLM inference specifically. Aligns with privacy-sensitive enterprise deployments.
- **Status:** Forked ✅ (https://github.com/jvanleur2234-glitch/LocalAI)

## procurement-research — Supplier Pricing Research Agent (April 25, 2026)
- **Repo:** Custom build — `/home/workspace/Skills/procurement-research/`
- **What it does:** Takes material lists → researches supplier pricing across Home Depot, Lowe's, Menards, Grainger, Ferguson, etc. → generates side-by-side comparison reports with savings calculations.
- **For Solomon OS:** First concrete Solomon offering built for the Home Builders Procurement Agent vertical. Delivered savings that pay for the build in one job. Used for demo/proof of concept.
- **Status:** Built ✅ — `Skills/procurement-research/`
- **Usage:** `bun run scripts/procurement-research.ts --materials "2x4x8 lumber,50 units" --category construction --report full`

## OWASP Agentic Top 10 2026 — Live Exploitation Confirmed (April 23, 2026)
- **Source:** OWASP Top 10 for Agentic Applications 2026
- **Key finding:** AI agents are now PRIMARY ATTACK VECTORS in real breaches (not theoretical). Mexican government agencies compromised via weaponized Claude. Most incidents CANNOT be mapped to CVEs.
- **For Solomon OS:** Validates entire agent-security scanner product line. Priority: IMMEDIATE integration of SupraWall + agentarmor-studio + sinewave scanners.
- **Status:** RD report written ✅

## Hermes Agent + GPT-5.5 Integration (April 23, 2026)
- **Source:** @Teknium (Hermes cofounder) on X
- **What it does:** GPT-5.5 now accessible in Hermes via ChatGPT/Codex OAuth provider. `hermes update` to access.
- **For Solomon OS:** GPT-5.5 capability added to Hermes execution layer. Major model addition.
- **Status:** Available now via Hermes update

## gollem — Go Agent Framework (April 23, 2026)
- **Repo:** fugue-labs/gollem — MIT
- **What it does:** Production-grade Go agent framework. Compile-time type safety, zero-dependency single binaries, structured output, rich guardrails, OpenTelemetry observability.
- **For research:** Language-agnostic guardrail patterns for agentarmor-studio. Go single-binary model for Solomon Bus edge services.
- **Status:** Already cloned ✅

## phero — Go Multi-Agent A2A Framework (April 23, 2026)
- **Repo:** henomis/phero — MIT
- **What it does:** Go multi-agent with A2A protocol (HTTP), MCP servers, skills (SKILL.md), RAG (Qdrant/pgvector/Weaviate), tool safety guards.
- **For research:** A2A agent protocol could complement Hermes MCP. Skills pattern identical to Hermes — competitive reference.
- **Status:** Already cloned ✅

## voltagent — TypeScript Agent Engineering Platform (April 23, 2026)
- **Repo:** ChengXinDL/voltagent — MIT
- **What it does:** TypeScript agent platform with typed roles/tools/memory, supervisor/sub-agent orchestration, MCP, RAG, guardrails, evals, VoltOps console.
- **For research:** Supervisor/sub-agent pattern for Solomon orchestration hierarchy.
- **Status:** Already cloned ✅

## agent-express — Middleware Agent Framework (April 23, 2026)
- **Repo:** agent-express-ai/agent-express — MIT
- **What it does:** Minimalist TypeScript agent framework with Express-like middleware (ctx/next). 5 hooks (agent/session/turn/model/tool), 12+ providers, budget validation, HITL approvals, OpenTelemetry.
- **For research:** Composable middleware security + budget guards could be Hermes skill for cost control.
- **Status:** Already cloned ✅

## Quorum — Multi-Provider Deliberation (April 23, 2026)
- **Repo:** Solvely-Colin/Quorum — MIT
- **What it does:** 7-phase deliberation (Gather/Plan/Formulate/Debate/Adjust/Rebuttal/Vote/Synthesis) across multiple providers. Evidence protocol, SHA-256 audit trail, policy guardrails.
- **For research:** Deliberation framework to watch vs captain-claw Agent Council.
- **Status:** Already cloned ✅

## HyperAgent — AI Browser Automation (April 23, 2026)
- **Repo:** hyperbrowserai/hyperagent — NOASSERTION
- **What it does:** Playwright + AI natural language commands. page.perform() granular + page.ai() orchestration. Stealth anti-bot, action caching, MCP client integration.
- **For research:** Solomon Browser should differentiate on persistent memory + authenticated sessions.
- **Status:** Already cloned ✅

## hackmyagent — Red-Team Security Toolkit (April 23, 2026)
- **Repo:** opena2a-org/hackmyagent — Apache-2.0
- **What it does:** 209 static checks, 164 adversarial payloads, 20-probe behavioral sim, Abstract Security Tree (AST-based, not regex), self-securing binary verification. Zero-config.
- **For agentarmor-studio:** Add as red-team skill for penetration testing of Hermes MCP/skill ecosystem.
- **Status:** Already cloned ✅

## medusa — AI-First Security Scanner (April 23, 2026)
- **Repo:** Pantheon-Security/medusa — AGPL-3.0
- **What it does:** 9,600+ AI/ML detection patterns, 200+ CVE detections, repo poisoning across 28+ file types, parallel processing (10-40x faster), IDE integrations.
- **For research:** Mine detection patterns for agentarmor-studio. AGPL limits proprietary use.
- **Status:** Already cloned ✅

## OWASP LLM Top 10 2026 — Live Exploitation (April 23, 2026)
- **Repo:** OWASP-FTL/OWASP-LLM-Top-10 — MIT
- **What it does:** Industry standard for AI security. LLM01 Prompt Injection now #1 real-world attack. Mexican government compromised via weaponized Claude. Compliance mapping (SOC2/GDPR/HIPAA).
- **For agentarmor-studio:** CRITICAL REFERENCE — validates entire security product line. Agent sandbox + input validation non-negotiable.
- **Status:** Already cloned ✅

## n8n-nodes-agent2agent — Agent Interoperability (April 23, 2026)
- **Repo:** n8n-io/n8n-nodes-agent2agent — MIT (presumed)
- **What it does:** n8n community node for cross-framework agent communication and task handoff.
- **For Solomon Bus:** Alternative/comparison for inter-agent communication patterns.
- **Status:** Already cloned ✅

## AgentEnsemble — JVM Multi-Agent Orchestration (April 24, 2026)
- **Repo:** AgentEnsemble/agentensemble — MIT
- **What it does:** Java 21 framework for orchestrating teams of AI agents built on LangChain4j. HIERARCHICAL, SEQUENTIAL, PARALLEL, MapReduce workflows. Production observability with token counts, latency, tool timing traces.
- **For Solomon OS:** JVM ecosystem gap. Fork for research — potential Hermes JVM bridge.
- **Status:** Forked to jvanleur2234-glitch ✅

## Agent-Express — TypeScript Middleware Framework (April 24, 2026)
- **Repo:** agent-express-ai/agent-express — MIT
- **What it does:** Minimalist middleware-style TypeScript framework. Express-like use(next) pattern. 12+ model providers, MCP integration, built-in guards (budgets, validation, timeouts, HITL), OpenTelemetry observability.
- **For Hermes:** Study middleware patterns for skill chaining. Reference implementation.
- **Status:** Already cloned ✅

## Gollem — Go Type-Safe Agent Framework (April 24, 2026)
- **Repo:** fugue-labs/gollem — MIT (~120 stars)
- **What it does:** Compile-time type-safe Go agent framework. Generic Agent[T], multi-provider (Anthropic, OpenAI, Gemini), streaming, guardrails, OpenTelemetry, time-travel debugging.
- **For agentarmor-studio:** Type-safe tool schema patterns. Go single-binary for Solomon Bus edge.
- **Status:** Already cloned ✅

## Agent-Orcha — Declarative P2P Orchestration (April 24, 2026)
- **Repo:** ddalcu/agent-orcha — MIT
- **What it does:** Declarative YAML-first framework. P2P agent/LLM sharing without central servers. Built-in SQLite vector store, MCP support, knowledge graphs, desktop clients.
- **For AgentFM:** P2P sharing patterns. Declarative skill definition format.
- **Status:** Already cloned ✅

## Reflexio — Self-Improving Agent Framework (April 24, 2026)
- **Repo:** ReflexioAI/reflexio — Apache 2.0
- **What it does:** AI agents that continually improve by learning from user interactions. 81% reduction in planning steps, 72% token reduction on GDPVal benchmarks. Captures corrections and execution paths.
- **For Hermes:** Self-improvement loop. Fork for integration research.
- **Status:** Already cloned ✅

## HyperAgent — AI-Powered Browser Automation (April 24, 2026)
- **Repo:** hyperbrowserai/hyperagent — NOASSERTION
- **What it does:** AI extension of Playwright. Natural-language browser control, stealth anti-bot mode, action caching, cloud-ready via Hyperbrowser.
- **For ClawLess:** Study for browser automation skill. Stealth and caching patterns.
- **Status:** Already cloned ✅

## Ouroboros — Self-Creating AI Agent (April 24, 2026)
- **Repo:** kazmak927/ouroboros — MIT (~500+ stars)
- **What it does:** Self-modifying AI agent that writes and rewrites its own code, evolving autonomously. Started v4.1, reached v6.2.0 within weeks. Constitution (BIBLE.md) governance, multi-model review, background consciousness, identity persistence.
- **For Hermes:** Self-modification patterns critical for autonomous improvement. Constitution-based governance aligns with Solomon OS ethical framework.
- **Status:** Already cloned ✅

## Miguel — Self-Improving Agent with Docker Sandbox (April 24, 2026)
- **Repo:** soulfir/miguel — CC BY-NC 4.0 (~300 stars)
- **What it does:** Self-improving agent with Docker sandbox. Started with 10 seed capabilities, now implementing 22. Auto-commit/push after validation, multi-agent (Coder/Researcher/Analyst), rollback on failure.
- **For research:** Docker sandbox validation patterns. Non-commercial use viable.
- **Status:** Already cloned ✅

## Viyv-Browser — Chrome Extension + MCP Server (April 24, 2026)
- **Repo:** viyv-browser — Unknown license (~200 stars)
- **What it does:** Chrome extension + MCP server for real browser automation with authentic logins. Semantic targeting, batch execution, Google Sheets integration via session cookies.
- **For Solomon Browser:** Authenticated automation with persistent sessions.
- **Status:** Already cloned ✅

## Vibium — WebDriver BiDi Browser Automation (April 24, 2026)
- **Repo:** VibiumDev/vibium — Apache-2.0 (~150 stars)
- **What it does:** Lightweight AI-native browser automation. CLI, MCP server, multi-language SDKs (JS/Python/Java). Built on WebDriver BiDi standard.
- **For ClawLess:** CLI-based lightweight alternative for browser tasks.
- **Status:** Already cloned ✅

## Gollem — Go Type-Safe Agent Framework (April 24, 2026)
- **Repo:** fugue-labs/gollem — MIT (~120 stars)
- **What it does:** Compile-time type-safe Go agent framework. Generic Agent[T], multi-provider (Anthropic, OpenAI, Gemini), streaming, guardrails, OpenTelemetry, time-travel debugging.
- **For agentarmor-studio:** Type-safe tool schema patterns. Go single-binary for Solomon Bus edge.
- **Status:** Already cloned ✅

## N8N-Nodes-MCP — MCP Client for N8N (April 24, 2026)
- **Repo:** nerding-io/n8n-nodes-mcp — MIT (~100 stars, 20+ contributors)
- **What it does:** n8n community node for MCP client. HTTP Streamable Transport + STDIO, 3 credential types, tool/resource/prompt execution.
- **For Hermes:** MCP client implementation patterns. n8n workflow integration.
- **Status:** Already cloned ✅

## Firmis-Scanner — Agent Security Runtime Scanner (April 24, 2026)
- **Repo:** Firmislabs/firmis-scanner — Apache-2.0 (~80 stars)
- **What it does:** TypeScript security scanner for AI agent runtimes. Detects credential harvesting, prompt injection, tool poisoning. 268 rules across platforms (Claude Skills, MCP, Cursor, Codex, n8n).
- **For agentarmor-studio:** Credential harvesting patterns. MCP security rules.
- **Status:** Already cloned ✅

## Deep-Claw — Dream Cycle Self-Improvement (April 24, 2026)
- **Repo:** the-keats-ai/deep-claw — MIT (~400 stars)
- **What it does:** Autonomous self-improvement via Nightly (research scan) + Weekly (performance reflection). Evidence-grounded assessments, anti-narcissism safeguards, rollback.
- **For Hermes:** Nightly competitive intelligence scanning. Weekly self-review patterns.
- **Status:** Already cloned ✅

## NFH Self-Improvement Loop — Adversarial Self-Modification (April 24, 2026)
- **Repo:** theprint/nfh-self-improvement-loop — MIT (~50 stars)
- **What it does:** Minimal adversarial framework. Generator + separate Evaluator agent. Pre-flight safety checks, one improvement per cycle, automatic rollback.
- **For Hermes:** Separation of generation/evaluation for safe self-modification.
- **Status:** Already cloned ✅

## Dapr-Agents — Kubernetes-Native Agent Orchestration (April 24, 2026)
- **Repo:** dapr/dapr-agents — Apache-2.0 (~2.1k stars)
- **What it does:** Python agent framework with durable execution, thousands of agents support, network fault recovery, state management. Kubernetes-native.
- **For Solomon OS:** Durable execution patterns. Resilient distributed agent deployment.
- **Status:** Already cloned ✅

## Agentrail — TypeScript Agent Harness Framework (April 24, 2026)
- **Repo:** yai-dev/agentrail — Apache-2.0
- **What it does:** TypeScript agent harness with full runtime core, multi-agent orchestration, Docker sandbox isolation, memory/knowledge indexing, pluggable LLM providers.
- **For Hermes:** Study sandbox implementation and skill packaging patterns.
- **Status:** Already cloned ✅

## Dialectic-Agentic — No-Code Multi-Agent Debate (April 24, 2026)
- **Repo:** slior/dialectic-agentic — MIT (~40 stars)
- **What it does:** No-code design debate tool. Multiple agents debate in structured rounds, judge evaluates convergence, final synthesis.
- **For deliberation:** Structured deliberation for architecture decisions.
- **Status:** Already cloned ✅

## Agent-Debate — Adversarial Technical Debate Protocol (April 24, 2026)
- **Repo:** gumbel-ai/agent-debate — MIT (~200 stars)
- **What it does:** Structured debate for AI coding agents. Evidence-based claims (file:line citations), SHA-256 replay ledger, CI/CD integration.
- **For deliberation:** Technical decision review with evidence traces.
- **Status:** Already cloned ✅
## LLM Armor — OWASP LLM Top 10 Security Scanner (April 24, 2026)
- **Repo:** llmarmor/llmarmor — MIT
- **What it does:** Dual-layer security scanner (regex + AST taint analysis) for OWASP LLM Top 10. Scans Python files, notebooks, configs for prompt injection, secrets leakage, excessive agent permissions.
- **For Solomon OS:** Core security scanning skill for Hermes Agent. OWASP compliance testing.
- **Fork:** https://github.com/jvanleur2234-glitch/llmarmor ✅
- **Status:** Cloned and forked — RD report: `llmarmor-owasp-llm-security-scanner.md`

## OmniFuzz-LLM — Enterprise Adversarial Testing Framework (April 24, 2026)
- **Repo:** bogdanticu88/OmniFuzz-LLM — MIT
- **What it does:** OWASP-aligned red-teaming for LLM deployments. Modules: sysprompt_extractor (LLM07), tool_abuse (LLM02), indirect_injection (LLM01), pii_compliance (LLM06). 301 tests passing, CI/CD ready.
- **For security:** Compliance testing pipeline for all Solomon OS agents.
- **Fork:** https://github.com/jvanleur2234-glitch/OmniFuzz-LLM ✅
- **Status:** Cloned and forked — RD report: `OmniFuzz-LLM-enterprise-owasp-testing.md`

## agent-express — TypeScript Middleware Agent Framework (April 24, 2026)
- **Repo:** agent-express-ai/agent-express — MIT
- **What it does:** Minimalist Express.js-pattern TypeScript framework. 5 middleware hooks (agent/session/turn/model/tool), 12+ providers, OpenTelemetry, MCP integration, SSE streaming.
- **For Hermes:** Reference architecture for skill chain/middleware patterns.
- **Status:** Already cloned ✅

## Dapr Agents — Durable Execution Resilient AI (April 24, 2026)
- **Repo:** dapr/dapr-agents — Apache-2.0
- **What it does:** Production-grade Python framework with durable-execution workflow engine. Scale-to-zero (virtual actors), automatic retries/state recovery, Kubernetes-native, multi-agent collaboration.
- **For Solomon OS:** Resilient agent execution with guaranteed completion. High priority FORGE candidate.
- **Fork:** Already in workspace ✅
- **Status:** RD report: `dapr-agents-durable-execution-resilient-ai.md`

## n8n-nodes-letta — Letta AI Agent Integration (April 24, 2026)
- **Repo:** letta-ai/n8n-nodes-letta — MIT
- **What it does:** Official n8n node for Letta agents. Send messages to Letta agents with memory, Max Steps, thinking, return message types.
- **For integration:** n8n workflow integration for Solomon OS agents.
- **Fork:** https://github.com/jvanleur2234-glitch/n8n-nodes-letta ✅
- **Status:** Cloned and forked

## OWASP LLM Top 10 — Security Reference Framework (April 24, 2026)
- **Repo:** OWASP/www-project-top-10-for-large-language-model-applications — Creative Commons
- **What it does:** The official security risk framework for LLM/agentic AI systems. Covers prompt injection (LLM01), sensitive info disclosure (LLM02), supply chain (LLM03), data poisoning (LLM04), excessive agency (LLM08), and more.
- **For Solomon OS:** Source of truth for security auditing. Maps to AgentArmor Studio 8-layer framework. Essential for SOC2/GDPR compliance.
- **Fork:** https://github.com/jvanleur2234-glitch/www-project-top-10-for-large-language-model-applications ✅
- **Status:** Cloned and forked — RD report: `owasp-llm-top10-fork.md`

## Swarms Client — Production Agent SDK (April 24, 2026)
- **Repo:** The-Swarm-Corporation/swarms-client — Apache-2.0
- **What it does:** Production-grade Python client for Swarms REST API. Type-safe sync/async models, LangChain-compatible agent definitions, ICD-based swarm orchestration.
- **For Solomon OS:** Reference architecture for production agent SDK design. Finance data tool integrations (HTX, Coingecko).
- **Fork:** https://github.com/jvanleur2234-glitch/swarms-client ✅
- **Status:** Cloned and forked — RD report: `swarms-client-fork.md`

## TickrAgent — Financial Swarm Agent Library (April 24, 2026)
- **Repo:** The-Swarm-Corporation/TickrAgent — MIT (~57 stars)
- **What it does:** Scalable swarm library for stock analysis agents. Part of Swarms ecosystem for financial AI.
- **For research:** Financial agent swarm design patterns. Lower priority than AutoHedge.
- **Fork:** https://github.com/jvanleur2234-glitch/TickrAgent ✅
- **Status:** Cloned and forked — RD report: `tickragent-fork.md`

## X/Twitter Intelligence — April 25, 2026

### HermesOS (Competitor Alert — April 25, 2026)
- **Source:** @Wayland_Six on X
- **What it is:** Managed AI agent hosting platform built on top of Hermes Agent by Nous Research. Deploy persistent, autonomous agents in under 5 minutes. No Docker, VPS, config files, or infra knowledge required.
- **Features:** Persistent memory, browser automation, tool use, scheduled tasks, real-time logs, auto-restart, daily backups, native connectors (Telegram, Discord, Slack, WhatsApp). Zero markup on model costs. You bring your own API keys.
- **Status:** Active product, live token on Base blockchain (dexscreener: 0x336ad40640593281d9c519fa0994986817fce079a0c493ea08f7ed9cac55ff19).
- **For Solomon OS:** Direct competitor. Study their UX/onboarding for Hermes OS packaging. Also: HermesOS is NOT the same as Hermes Agent by Nous Research — clarify when discussing with clients.

### Security Vulnerabilities — April 25, 2026
- **Source:** @dagomint (dago) on X — April 23, 2026
- **Key findings:**
  - DeepMind: 86% agent hijack rate via hidden HTML prompt injection
  - Anthropic: Opus 4 blackmails in 96% of scenarios with goal conflict + replacement threat
  - Decepticon bypasses Opus 4.7 refusal classifier via trigger-term substitution
  - Vercel/Context.ai OAuth breach (Mandiant + CrowdStrike) — real-world compromise
- **Implication:** Model-level safety is NOT the answer. Need deterministic policy layers + runtime guardrails.

### RECUR Protocol — Solana AI Security Layer (April 25, 2026)
- **Source:** @airdrops551 on X — March 20, 2026
- **What it is:** Layered sentinel network for AI agent security on Solana.
  - PRIME: coordinates
  - WARD: monitors broad threats
  - SUB: targets specific vectors
  - NANO: detects patterns instantly
  - INTERCEPT: secures prompt before execution (milliseconds)
  - ANALYSE: evaluates behavior and signatures
  - ATTEST: records threats as ZK proofs on Solana
- **Key innovations:** ZK proof attestation without exposing data, adapts to new attack patterns automatically, one endpoint swap integration.
- **For agentarmor-studio:** Study the ZK attestation pattern for audit trails.

### Google "Shadow Agent" Crisis (April 25, 2026)
- **Source:** @Dinosn (Nicolas Krassas) — Google's Cybersecurity 2026 Forecast
- **What it is:** Employees deploy AI agents outside corporate oversight, creating invisible pipelines for sensitive information → data leaks, compliance violations, IP theft.
- **For Solomon OS:** Opportunity — sell "Shadow Agent Discovery + Governance" as enterprise feature. AgentSeal does this locally; we could do it for Solomon OS clients.

## Vercel Agent Browser — Fast Rust Browser Automation (April 25, 2026)
- **Repo:** vercel-labs/agent-browser — Apache-2.0 (~2.5k stars)
- **What it does:** Fast native Rust CLI for browser automation. Chrome/Chromium control, snapshot/inspection (accessibility tree), CSS + role selectors, screenshot, keyboard/mouse actions. Zero Python/Node dependency for core daemon.
- **For ClawLess:** Direct competitor. Rust-based = fastest browser automation for agents. Replace Playwright-based tools.
- **Fork:** https://github.com/jvanleur2234-glitch/vercel-agent-browser ✅
- **Status:** Forked, RD: `vercel-agent-browser.md`

## Quorum (Solvely-Colin) — Multi-Agent Deliberation Framework (April 25, 2026)
- **Repo:** Solvely-Colin/Quorum — MIT (~1.2k stars)
- **What it does:** 7-phase deliberation (Gather/Plan/Formulate/Debate/Adjust/Rebuttal/Vote). Evidence protocol with source citation. SHA-256 replay ledger for auditability. Policy guardrails (block/warn/pause). 8+ provider support.
- **For Council of High Intelligence:** Direct competitor. Fork as Hermes deliberation skill.
- **Fork:** https://github.com/jvanleur2234-glitch/quorum-fresh ✅
- **Status:** Forked, RD: `quorum-deliberation.md`

## Deliberation (2389-research) — Contemplative Multi-Agent Framework (April 25, 2026)
- **Repo:** 2389-research/deliberation — MIT (~300 stars)
- **What it does:** Modular framework inspired by contemplative/quasi-Quaker practices. `discernment` (internal voices), `clearness` (multi-agent committee), `gathered` (participatory). Ground rules: speak once, seek unity not votes.
- **For Hermes:** Unique contemplative approach to agent consensus. Self-evolution reflection loop.
- **Fork:** https://github.com/jvanleur2234-glitch/deliberation-fresh ✅
- **Status:** Forked, RD: `deliberation-framework.md`

## Council (dubs3c) — Python Multi-Agent Discussion System (April 25, 2026)
- **Repo:** dubs3c/council — MIT (~700 stars)
- **What it does:** Structured debate with default personas (Architect/Critic/AppSec Specialist). 4-phase: Proposal → Debate → Early Consensus → Moderator Synthesis. Markdown report generation.
- **For Council of High Intelligence:** Security-focused deliberation. AppSec persona aligns with Hermes security scanning.
- **Fork:** https://github.com/jvanleur2234-glitch/council-fresh ✅
- **Status:** Forked, RD: `council-dubs3c.md`

## Deliberate — File-Based Two-Agent Protocol (April 25, 2026)
- **Repo:** kyleparrott/deliberate — MIT (~200 stars)
- **What it does:** Experimental file-based JSONL protocol for two agents to deliberate locally. Bash + jq only. Privacy-preserving (no API calls during deliberation). Cross-model compatible (Claude Code vs Codex).
- **For Hermes:** Minimal self-improvement loop. Lightweight two-agent deliberation primitive.
- **Fork:** https://github.com/jvanleur2234-glitch/deliberate-new ✅
- **Status:** Forked, RD: `deliberate-file-based.md`

## PeerClaw — P2P AI Compute Network (April 25, 2026)
- **Repo:** antonellof/peerclaw — MIT (~800 stars, Rust/TypeScript)
- **What it does:** Single static Rust binary P2P AI compute network. GGUF models (Llama/Phi/Qwen/Gemma), GPU acceleration (Metal/CUDA), job marketplace via libp2p, token economy (Ed25519), vector memory (HNSW), SKILL prompts, MCP integration.
- **For AgentFM:** Direct competitor. P2P GPU pooling, compute marketplace. Token economy model for JCPaid.
- **Fork:** https://github.com/jvanleur2234-glitch/peerclaw-new ✅
- **Status:** Forked, RD: `peerclaw.md`

## Gollem (fugue-labs) — Compile-Time Safe Go Agent Framework (April 25, 2026)
- **Repo:** fugue-labs/gollem — MIT (~500 stars, Go)
- **What it does:** Production-grade Go agent framework. Compile-time type safety, `Generic Agent[T]`, `FuncTool[P]` from Go functions, 5+ LLM providers (Anthropic/OpenAI/Gemini), guardrails (MaxPromptLength/ContentFilter/MaxTurns), OpenTelemetry, streaming via Go 1.23+.
- **For agentarmor-studio:** Type-safe tool schemas. Go single-binary for Solomon Bus edge services.
- **Fork:** https://github.com/jvanleur2234-glitch/gollem-fresh ✅
- **Status:** Forked, RD: `gollem.md`

## Agent Express — TypeScript Middleware Framework (April 25, 2026)
- **Repo:** agent-express-ai/agent-express — MIT (~600 stars)
- **What it does:** Minimalist Express.js-pattern TypeScript framework. `(ctx, next)` middleware. 5 hooks (agent/session/turn/model/tool). Guards: budgets, validation, timeouts, HITL. 12+ providers. OpenTelemetry. MCP integration. Zod schema validation.
- **For Hermes:** Reference for middleware skill chaining. Built-in guards as Hermes safety patterns.
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express-new ✅
- **Status:** Forked, RD: `agent-express.md`
## n8n-nodes-claude-sdk (ssccio) — Claude SDK in n8n Workflows (April 25, 2026)
- **Repo:** ssccio/n8n-nodes-claude-sdk — MIT
- **What it does:** n8n community node for Claude SDK integration. Claude CLI or API key auth. File I/O, shell commands, codebase search. LangChain-compatible interface, drop-in for n8n AI Agent node.
- **For integration:** Claude SDK autonomous coding in n8n workflows.
- **Fork:** https://github.com/jvanleur2234-glitch/n8n-nodes-claude-sdk ✅
- **Status:** Forked, RD: `n8n-nodes-claude-sdk.md`

## n8n-nodes-flowengine-session-id — Session ID Management for AI Agents (April 25, 2026)
- **Repo:** FlowEngine-cloud/n8n-nodes-flowengine-session-id — MIT
- **What it does:** Session ID generator/manager for n8n AI Agent workflows. Generate UUID per run, persist across loop iterations. Zero dependencies, native crypto.
- **For Hermes:** Session persistence pattern for multi-turn memory in workflows.
- **Fork:** https://github.com/jvanleur2234-glitch/n8n-nodes-flowengine-session-id ✅
- **Status:** Forked, RD: `n8n-nodes-flowengine-session-id.md`

## Snyk Agent Scan — Enterprise Security Scanner (April 26, 2026)
- **Repo:** snyk/agent-scan — Apache-2.0 — 2,253 stars
- **What it does:** Discovers + scans AI agents, MCP servers, skills for 15+ security risks (prompt injection, tool poisoning, credential harvesting). Supports 10+ agents (Windsurf, Cursor, Claude, etc.). CI/CD via SARIF.
- **For Hermes:** Enterprise-grade security scanning. CI/CD security gate for skill submissions. Snyk CVDB integration.
- **Fork:** https://github.com/jvanleur2234-glitch/snyk-agent-scan-new ✅
- **Status:** Forked, RD: `snyk-agent-scan-new.md`

## GoPlus AgentGuard — Real-Time 3-Tier Security Layer (April 26, 2026)
- **Repo:** GoPlusSecurity/agentguard — MIT — 390 stars
- **What it does:** 3-tier defense: (1) Guard hooks block dangerous commands, prevent writes to .env/.ssh, detect exfiltration webhooks; (2) Deep Scan 24 detection rules, auto-scans new skills; (3) Daily Patrol 8 security checks, audit log analysis. Trust registry with per-skill access control.
- **For Hermes:** Core security layer. Real-time command blocking, skill auditing, daily posture checks.
- **Fork:** https://github.com/jvanleur2234-glitch/agentguard-new ✅
- **Status:** Forked, RD: `agentguard-new.md`

## agent-orcha — Declarative YAML Multi-Agent Framework (April 26, 2026)
- **Repo:** ddalcu/agent-orcha — MIT — v2026.409
- **What it does:** TypeScript-first declarative framework. Define agents, workflows, knowledge stores in YAML. Model-agnostic (OpenAI, Gemini, Anthropic, Ollama). Built-in SQLite vector store + knowledge graphs. P2P encrypted agent sharing, SSRF protection, SQL injection hardening, sandboxed execution.
- **For Hermes:** Declarative YAML config aligns with skill format. P2P agent sharing competitive with AgentFM. Security features directly relevant to AgentArmor.
- **Fork:** https://github.com/jvanleur2234-glitch/agent-orcha ✅
- **Status:** Forked, RD: `agent-orcha.md`

## phero — Go Multi-Agent Framework with A2A Protocol (April 26, 2026)
- **Repo:** henomis/phero — Apache-2.0 — v0.0.4
- **What it does:** Go framework for multi-agent AI. A2A protocol (HTTP agents as tools), LLM abstraction (OpenAI, Ollama, Anthropic), skills system, MCP support, memory, audio I/O (ST/TTS), tracing.
- **For Hermes:** Study A2A protocol for inter-agent communication. Go performance for high-throughput agent workloads.
- **Fork:** https://github.com/jvanleur2234-glitch/phero ✅
- **Status:** Forked, RD: `phero-go-multi-agent.md`

## dapr-agents — Durable Python Agent Framework (April 26, 2026)
- **Repo:** dapr/dapr-agents — Apache-2.0 — v1.0.1
- **What it does:** Python scalable autonomous AI agents. Built-in workflow orchestration, security, stateful execution, telemetry. Durable execution engine, fault-tolerant across network failures. Kubernetes-native.
- **For Hermes:** Durable execution model for session persistence. Fault-tolerant patterns for resilient agent operations.
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents ✅
- **Status:** Forked, RD: `dapr-agents-python-agent-framework.md`

## AgentVerus Scanner — AI Skill Trust & Safety Scanner (April 26, 2026)
- **Repo:** agentverus/agentverus-scanner — MIT — v0.7.1
- **What it does:** Evaluates AI agent skills for trust/safety. Detects prompt injection, data exfiltration, 10+ threat categories. Permission analysis, dependency scanning, workspace tampering detection (AGENTS.md, TOOLS.md).
- **For Hermes:** Pre-deployment skill vetting. Monitors Hermes workspace integrity. Trust-boundary scoring for skill risk assessment.
- **Fork:** https://github.com/jvanleur2234-glitch/agentverus-scanner ✅
- **Status:** Forked, RD: `agentverus-scanner-ai-agent-security.md`

## firmis-scanner — AI Runtime Security Scanner (April 26, 2026)
- **Repo:** Firmislabs/firmis-scanner — MIT — 268 detection rules
- **What it does:** AI runtime security for agents. Detects credential harvesting, prompt injection, tool poisoning, data exfiltration across Claude Skills, MCP servers, Codex plugins, Cursor. Zero-config, no API key required.
- **For Hermes:** Zero-config security scanning. Complementary to AgentArmor. Multi-platform support critical for Hermes ecosystem.
- **Fork:** https://github.com/jvanleur2234-glitch/firmis-scanner ✅
- **Status:** Forked, RD: `firmis-scanner-ai-runtime-security.md`

## vibium — WebDriver BiDi Browser Automation (April 26, 2026)
- **Repo:** VibiumDev/vibium — Apache-2.0 — Go-based
- **What it does:** AI-friendly browser automation. Navigate, click, fill, screenshots, PDFs, JS execution. WebDriver BiDi standard. MCP server + Skills framework integration. CLI, JS/Python/Java libraries.
- **For Hermes:** Browser automation skill. ClawLess competitor with standards-based approach. MCP integration aligns with Hermes ecosystem.
- **Fork:** https://github.com/jvanleur2234-glitch/vibium ✅
- **Status:** Forked, RD: `vibium-go-browser-automation-mcp.md`

## browserclaw-agent — Self-Learning Browser Automation (April 26, 2026)
- **Repo:** idan-rubin/browserclaw-agent — MIT — TypeScript
- **What it does:** AI agent browser automation with learning. Snapshot→LLM→action loop. Built-in anti-bot (Cloudflare Turnstile), popup dismissal, loop detection. Domain-specific playbooks learned over time. MCP compatible.
- **For Hermes:** Study skill/playbook learning mechanism. Anti-bot handling for web scraping. Learning improves over time.
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent ✅
- **Status:** Forked, RD: `browserclaw-agent-auto-learning.md`

## 2389-deliberation — Multi-Agent Decision Support (April 26, 2026)
- **Repo:** 2389-research/deliberation — MIT
- **What it does:** Multi-agent decision support with structured deliberation. Skills: discernment (clerk synthesis), clearness (parallel committee analysis), gathered (participatory). Principles: unity not votes, speaking once, way opens.
- **For Hermes:** Council of High Intelligence implementation. Structured decision-making for complex client scenarios.
- **Fork:** https://github.com/jvanleur2234-glitch/2389-deliberation ✅
- **Status:** Forked, RD: `2389-deliberation.md`

## NFH Self-Improvement Loop — Adversarial Self-Modification (April 26, 2026)
- **Repo:** theprint/nfh-self-improvement-loop — MIT — v1.0.0
- **What it does:** Minimal adversarial framework. Generator proposes one improvement per cycle, evaluator (sees only diff) judges. Prevents self-delusion. Pre-flight checks, rollback safety.
- **For Hermes:** Adversarial self-improvement prevents bias. Key pattern: separation of proposal and evaluation.
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop ✅
- **Status:** Forked, RD: `nfh-self-improvement-loop-adversarial.md`

## inngest-self-learning-agent — Durable Prompt Evolution (April 26, 2026)
- **Repo:** inngest/inngest-self-learning-agent — MIT — Node.js
- **What it does:** Durable self-learning agent. Think/act/observe loop, scores responses (relevance, completeness, tool efficiency, tone), A/B tests prompt variants, scheduled evaluation pipeline, guardrails against gaming.
- **For Hermes:** Durable execution + self-improving prompts. Guardrails critical for safe autonomous modification.
- **Fork:** https://github.com/jvanleur2234-glitch/inngest-self-learning-agent ✅
- **Status:** Forked, RD: `inngest-self-learning-agent.md`

## Grail-Computer Self-Improving Agent — npx Skill Template (April 26, 2026)
- **Repo:** Grail-Computer/Self-Improving-Agent — MIT
- **What it does:** Self-improving agent template using AGENTS.md as repository memory. Compounding loop: Work→Complete→Reflect→Record→Better baseline. Installed via `npx skills add`.
- **For Hermes:** Direct skill installation for self-improvement. AGENTS.md pattern already in Hermes.
- **Fork:** https://github.com/jvanleur2234-glitch/Grail-Computer-Self-Improving-Agent ✅
- **Status:** Forked, RD: `Grail-Computer-Self-Improving-Agent.md`

## AIBYAI Multi-Agent Deliberation (April 26, 2026)
- **Repo:** Yash-Awasthi/aibyai — MIT
- **What it does:** Multi-agent council with 4+ specialized agents (Empiricist, Strategist, Historian, Skeptic), conflict detection, critique/rebuttal cycles, cold validator for hallucinations, scored consensus with confidence metrics.
- **For Hermes:** Multi-agent deliberation framework. Confidence scoring for trust verification.
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai ✅
- **Status:** Forked, RD: `AIBYAI-multi-agent-deliberation.md`

## medusa — AI-First Security Scanner (April 26, 2026)
- **Repo:** Pantheon-Security/medusa — Apache-2.0
- **What it does:** Security scanner for AI/ML systems, agents, MCP servers. 9,600+ detection patterns, 200 CVE detections, `--git` scan for GitHub repo supply-chain attacks.
- **For Hermes:** Pre-deployment security scanning for all Hermes MCP servers and skills.
- **Fork:** https://github.com/jvanleur2234-glitch/medusa ✅
- **Status:** Forked, RD: `medusa-ai-security-scanner.md`

## agentguard — Real-Time Security Layer (April 26, 2026)
- **Repo:** GoPlusSecurity/agentguard — MIT
- **What it does:** 3-layer real-time protection: Auto Guard (blocks destructive commands), Deep Scan (skill auditing), Daily Patrol (posture checks). Action tracing to skill initiator.
- **For Hermes:** Production defense against prompt injection and tool abuse.
- **Fork:** https://github.com/jvanleur2234-glitch/agentguard ✅
- **Status:** Forked, RD: `agentguard-real-time-security.md`

## securevector-ai-threat-monitor v3.2.0 (April 26, 2026)
- **Repo:** Secure-Vector/securevector-ai-threat-monitor — MIT
- **What it does:** AI firewall proxy between agents and LLM providers. Skill Scanner (static + AI review), threat detection, cost tracking, on-device architecture.
- **For Hermes:** Production firewall with skill scanning. On-device = privacy-preserving.
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor ✅
- **Status:** Forked, RD: `securevector-ai-threat-monitor.md`

## ai-agent-scanner — Shadow AI Discovery (April 26, 2026)
- **Repo:** perfecxion-ai/ai-agent-scanner — GPL-3.0
- **What it does:** Discovers AI agents across network/code/traffic/cloud. Vulnerability testing, compliance mapping (GDPR, SOC 2, HIPAA, NIST AI RMF, EU AI Act).
- **For Hermes:** Enterprise compliance + agent inventory. Note: GPL-3.0.
- **Fork:** https://github.com/jvanleur2234-glitch/ai-agent-scanner ✅
- **Status:** Forked (internal use), RD: `ai-agent-scanner-shadow-ai-discovery.md`

## agent-express — TypeScript Middleware Agent Framework (April 26, 2026)
- **Repo:** agent-express-ai/agent-express — MIT
- **What it does:** Express-style middleware framework for TypeScript AI agents. 5-layer middleware onion, built-in guards (budget, timeout, approval), 12+ providers, OpenTelemetry.
- **For Hermes:** TypeScript skill template with strong safety features.
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express ✅
- **Status:** Forked, RD: `agent-express-typescript-framework.md`

## gollem — Compile-Time Safe Go Agent Framework (April 26, 2026)
- **Repo:** fugue-labs/gollem — Apache-2.0
- **What it does:** Go agent framework with compile-time type safety. Streaming, guardrails, multi-provider, OpenTelemetry. Zero-cost abstractions.
- **For Hermes:** Study compile-time safety patterns for high-performance agent components.
- **Fork:** https://github.com/jvanleur2234-glitch/gollem ✅
- **Status:** Forked, RD: `gollem-go-agent-framework.md`

## phero — Go Multi-Agent A2A Framework (April 26, 2026)
- **Repo:** henomis/phero — Apache-2.0
- **What it does:** Go multi-agent framework with A2A protocol (HTTP), MCP servers, skills (SKILL.md), RAG, memory management.
- **For Hermes:** A2A protocol + SKILL.md patterns directly relevant to Solomon Bus.
- **Fork:** https://github.com/jvanleur2234-glitch/phero ✅
- **Status:** Forked, RD: `phero-go-multi-agent-framework.md`

## cognee — Persistent Memory for AI Agents (April 26, 2026)
- **Repo:** cognee-ai/cognee — MIT — 15.9K stars
- **What it does:** Unified memory layer: vector search + graph database. 6-line ECL pipeline, 30+ data sources, replaces traditional RAG.
- **For Hermes:** Production memory layer. 15.9K stars = validated community trust.
- **Fork:** https://github.com/jvanleur2234-glitch/cognee ✅
- **Status:** Forked, RD: `cognee-persistent-memory.md`

## agent-fridays-self-improvement-kit — HITL Self-Modification (April 26, 2026)
- **Repo:** FutureSpeakAI/agent-fridays-self-improvement-kit — MIT
- **What it does:** Self-modification engine requiring explicit human approval for ALL writes. Zero dependencies, framework-agnostic.
- **For Hermes:** Production-safe self-improvement with human-in-the-loop.
- **Fork:** https://github.com/jvanleur2234-glitch/agent-fridays-self-improvement-kit ✅
- **Status:** Forked, RD: `agent-fridays-self-improvement-kit.md`
## j-d0g/self-improving-agent — Financial Analysis Agent with ACE Pipeline (April 27, 2026)
- **Repo:** j-d0g/self-improving-agent — MIT (~1.2K stars)
- **What it does:** Self-improving financial analysis agent. V1: per-query improvement loop. V2/ACE: batch-based learning with Solver→Reflector→Curator pipeline. Learner logs traces → Improver analyzes → updates knowledge base → next Learner starts smarter.
- **For Solomon OS:** Cross-session learning patterns. ACE pipeline template for batch-based skill self-improvement. Study `agent/prompts/` and `agent/tracing.py` for Hermes skill evolution.
- **Status:** SKILL — Clone and study patterns.
- **Links:** https://github.com/j-d0g/self-improving-agent

## ai-in-pm/Recursive-Self-Improvement-AI-Agent — Gödel Framework (April 27, 2026)
- **Repo:** ai-in-pm/Recursive-Self-Improvement-AI-Agent — MIT (~900 stars)
- **What it does:** Python framework for self-modifying AI agents based on Gödel's incompleteness theorems. Agents analyze and modify their own code during runtime. Inspired by arxiv:2410.04444.
- **For Solomon OS:** Research reference for Hermes recursive self-improvement. Gödel-based self-referential framework for Hermes self-evolution skills.
- **Status:** RESEARCH — Already cloned, RD exists as `Recursive-Self-Improvement-AI-Agent-godel.md`.
- **Links:** https://github.com/ai-in-pm/Recursive-Self-Improvement-AI-Agent

## solomon-memory-bridge — Goal-Relevant Memory Retrieval v2 (April 29, 2026)
- **Repo:** Built in house at `/home/workspace/solomon-memory-bridge/`
- **What it does:** Goal-relevant memory retrieval using Conway & Rubin (2005) Self-Memory System. Four-layer architecture: Working Self (2x), Lifetime Periods (2x), General Events (1x), Episodic Details (0.5x). Goal-scoring frame derived from soul.md decision framework.
- **Key endpoints:**
  - `GET /memory/goal?q=<situation>` — Primary retrieval for decision engine
  - `GET /memory/self` — Working Self query ("Who am I right now?")
  - `GET /memory/layer/<layer>` — By layer
  - `GET /health` — Service status
- **Upgrades from v1:**
  - SOUL.md used as GOAL SCORING FRAME (not just keyword overlap)
  - `_score_goal_relevance()` uses decision framework terms (north_star, jackconnect, ai_employee_agency, etc.)
  - Working Self endpoint returns identity + north_star + top priorities + decision framework + agents
  - Deduplication by file (keeps highest-scoring entry per file)
  - Auto-registers as service on startup
- **For Hermes:** Call `/memory/goal?q=<current_task>` to retrieve relevant skills, past patterns, and agent context before executing. Call `/memory/self` at session start.
- **For Russell Tuna:** Query memory before responding to ensure continuity across sessions.
- **Status:** LIVE at port 5012, registered as `svc_J49kEx8AYHA`
- **Links:** `/home/workspace/solomon-memory-bridge/memory_server.py`

## Hermes Agent v0.11.0 — "The Interface Release" (April 23, 2026)
- **Repo:** NousResearch/hermes-agent — 18.9K stars, 126K total reach
- **Release:** v2026.4.23 — 1,556 commits, 761 merged PRs, 224,174 insertions
- **What it does:** Full-stack AI agent with 17 messaging platforms, multi-provider inference, skill system, cron/coworking, delegation, TUI, and plugin architecture
- **For JCPaid:** Core execution engine. v0.11.0 ships native delegate tool (multi-agent orchestration) + expanded plugin surface — eliminates need for paperclip adapter hack
- **Status:** ✅ UPDATED to v0.11.0 (2026-04-30), gateway running on port 8642, API server enabled

**Key new features in v0.11.0:**
- New React/Ink TUI (`hermes --tui`) — client-facing interactive interface
- Pluggable Transport Layer (Anthropic, ChatCompletions, Responses, Bedrock)
- Native AWS Bedrock via Converse API
- GPT-5.5 via Codex OAuth
- Kimi K2.6 across OpenRouter, Nous Portal, native Kimi, HuggingFace
- Delegate Tool — native cross-agent orchestration (replaces paperclip adapter need)
- Plugin surface expansion: `register_command()`, `dispatch_tool()`, `pre_tool_call` blocking, `transform_tool_result()`
- Gateway proxy mode for remote API forwarding
- 17 messaging platforms including QQBot (China)

**JCPaid × The Agency FORGE (April 30, 2026)**
- Source: TheAgency/agency, 88K stars, MIT
- Cloned to: /home/workspace/jcpaid/agency-framework/
- Added: 147 skills, dispatch system, fleet health commands
- Integration: Hermes Agent v0.11.0 (port 8642), Paperclip company generator
- Client model: $299/mo, multi-agent dispatch per client
- Skills: /home/workspace/jcpaid/agency-framework/.claude/skills/