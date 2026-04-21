## Spectrum by Photon — Unified Agent Messaging (April 21, 2026)
- **Repo:** github.com/photon-hq/spectrum (check for private repo)
- **What it does:** Open-source framework connecting AI agents to iMessage, WhatsApp, Telegram, Slack, Discord, Instagram, SMS/RCS via ONE unified API. <1s latency, edge network, 99.9% uptime.
- **Stack:** TypeScript, npm install spectrum-ts
- **Use for:** Replace Hermes/Russell Tuna Telegram integration with unified multi-platform API. Push Solomon OS agents to all messaging platforms from single codebase.
- **Case study:** Ditto (iMessage matchmaker agent) — 42K+ users, 400K+ messages processed
- **Business fit:** "Agents for the rest of us" = JCPaid philosophy. Scale Russell Tuna from 1 platform → ALL.
- **Status:** FORGE ✅ — spectrum-ts available via npm, GitHub repo may need auth
- **Related repos:** photon-hq/imessage-kit (1.2K stars), photon-hq/flux (77 stars) — good alternatives if spectrum is private
- **Location:** /home/workspace/spectrum/ (clone pending)
---

## Self-Improving Agent (xmaks82) — Capability Evolution System (April 21, 2026)
- **Repo:** github.com/xmaks82/self-improving-agent
- **What it does:** 16-agent multi-agent system that permanently evolves itself by learning from user feedback. Upgrades system prompts across versions so subsequent responses leverage an improved "brain."
- **Key insight:** Feedback loop: user input → FeedbackDetector → AnalyzerAgent → VersionerAgent → new prompt version
- **Stack:** Python 3.12+, 6 free LLM providers + Claude via OAuth
- **Use for:** Hermes self-improvement — feedback-driven prompt evolution system for continuous capability improvement
- **Security:** Read-Before-Edit policy, permission system, Secret Scanner
- **Status:** FORGE ✅ — MIT licensed, full fork at /home/workspace/self-improving-agent

## Safe Self-Improvement Kit (FutureSpeakAI) — Human-in-the-Loop Pattern (April 21, 2026)
- **Repo:** github.com/FutureSpeakAI/self-improving-agent
- **What it does:** Controlled self-modifying agent framework with safety and human oversight. Agent reads/analyzes own source, generates code diffs, only applies changes after explicit human approval.
- **Key insight:** SelfImproveEngine + ApprovalHandler = safe production self-improvement
- **Stack:** TypeScript, zero external dependencies, MIT license
- **Use for:** Safe self-improvement for Hermes — human gates before any code changes
- **Status:** FORGE ✅ — MIT licensed, fork at /home/workspace/self-improving-agent (FutureSpeakAI)

## Browser Harness — Stealth Browser Automation for AI Agents (April 21, 2026)
- **Repo:** github.com/antianvpn/browser-harness
- **What it does:** Playwright-based browser automation with stealth capabilities. One-time skill creation, unlimited execution without token cost.
- **Key insight:** Hermes user built web scraper that creates tool once, uses unlimited times — saves massive tokens
- **Stack:** Python, Playwright, stealth anti-bot patches
- **Use for:** Solomon Browser — AI-native web browsing without token costs per execution
- **Status:** FORGE ✅ — MIT licensed, already in production use

## Agent Orcha — Declarative Multi-Agent Framework with P2P (April 21, 2026)
- **Repo:** github.com/ddalcu/agent-orcha
- **What it does:** Declarative YAML-based workflow and agent definitions. Model-agnostic. P2P encrypted sharing of agents/engines. Studio IDE with visual composer.
- **Key insight:** P2P agent sharing + YAML workflows = distributed orchestration without central server
- **Stack:** TypeScript, MCP, SQLite vector store, Chrome DevTools Protocol
- **Use for:** Solomon Bus P2P features — agent sharing across distributed nodes without API dependency
- **Status:** FORGE ✅ — MIT licensed, fork at /home/workspace/agent-orcha

## Microsoft Agent Framework — Enterprise Graph-Based Orchestration (April 21, 2026)
- **Repo:** github.com/microsoft/agent-framework
- **What it does:** Graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. Python + .NET dual-language.
- **Key insight:** Enterprise-grade orchestration with DevUI for testing/debugging
- **Stack:** Python, .NET/C#, DevUI, AF Labs research features
- **Use for:** Watch for enterprise Windows integration scenarios; Microsoft backing = rapid ecosystem growth
- **Status:** WATCH ✅ — Competitor intel, not forking (Microsoft backed)
