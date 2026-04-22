## Clawputer Pattern — Telegram + OpenClaw + GBrain (April 21, 2026)
- **URL:** https://opencomputer.dev/clawputer
- **What it does:** GBrain on Telegram — persistent memory AI agent in 3 CLI commands. Stack: OpenClaw gateway + Claude via OpenRouter + gbrain (Postgres) + always-on sandbox. Hot-reloads on Telegram connect, no restart.
- **Solomon OS fit:** DIRECT — we have OpenClaw (Hermes), gbrain (cloned), Telegram (Russell Tuna). Just need the wiring. Clawputer = proof of concept for Solomon OS. Hot-reload trick for Telegram bot token is worth stealing.
- **Status:** SKILL — study pattern, integrate into Solomon Bus
- **Location:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawputer-gbrain-telegram.md
## ProofLayer / sinewave-agent-security-scanner-mcp — Security Scanner (April 21, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/sinewave-agent-security-scanner-mcp
- **Fork:** https://github.com/sinewaveai/agent-security-scanner-mcp → jvanleur2234-glitch/sinewave-agent-security-scanner-mcp
- **What it does:** Enterprise security scanner for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1700+ vulnerability rules via AST/taint analysis, LLM-powered semantic code review, SBOM generation, SOC2/GDPR compliance evidence.
- **Solomon OS fit:** INTEGRATE — core security primitive. Pre-execution gate for every skill/tool invocation. SOC2 compliance evidence maps to JCPaid enterprise client needs. OpenClaw plugin available.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## Hyperspace AGI — Distributed P2P AI Compute (April 21, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/hyperspace-agi
- **Fork:** https://github.com/hyperspaceai/agi → jvanleur2234-glitch/hyperspace-agi
- **What it does:** First experimental distributed AGI. P2P Pods (private AI clusters), distributed inference across pooled GPU/CPU, DiLoCo-based distributed training (195x compression), Hyperspace A1 blockchain for agent micropayments, 695+ live agents.
- **Solomon OS fit:** SKILL — study DiLoCo/SparseLoCo compression for potential distributed training. Pod Capsule concept maps to Solomon portable brain. Micropayment blockchain underpins agent economy. DIRECT COMPETITOR to AgentFM.
- **Status:** SKILL — architecture study only (NOASSERTION license, cannot use code directly)
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/hyperspace-agi.md

## xmaks82/self-improving-agent — 16-Agent Self-Evolution Pipeline (April 21, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/xmaks82-self-improving-agent
- **Fork:** https://github.com/xmaks82/self-improving-agent → jvanleur2234-glitch/xmaks82-self-improving-agent
- **What it does:** 16-agent pipeline with permanent prompt evolution from user feedback. AnalyzerAgent + VersionerAgent generate improved prompts (v1→v2→v3). 5 auto-selected sub-agents, VerificationAgent for adversarial testing. 6 free LLM providers.
- **Solomon OS fit:** FORGE — self-improvement loop (Analyzer→Versioner→prompt evolution) directly implementable in Hermes. MIT license permits direct use. Secret scanner for team memory = security for shared brain.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/xmaks82-self-improving-agent.md

## RangeKing/self-evolving-agent — OpenClaw Capability Evolution (April 21, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/RangeKing-self-evolving-agent
- **Fork:** https://github.com/RangeKing/self-evolving-agent → jvanleur2234-glitch/RangeKing-self-evolving-agent
- **What it does:** OpenClaw-first phase-aware capability evolution runtime. Phases: task_light/task_full/agenda_review/promotion_review. Learning states: recorded→understood→practiced→passed→generalized→promoted. Promotion gate prevents brittle rules.
- **Solomon OS fit:** FORGE — this IS the self-evolution engine for Hermes/OpenClaw. Phase-aware control plane routes tasks into smallest safe mode. Learning agenda prevents capability overload. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/RangeKing-self-evolving-agent.md

## T33R0/persistent-agent-framework — Claude Code Self-Correction Loop (April 21, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/persistent-agent-framework
- **Fork:** https://github.com/T33R0/persistent-agent-framework → jvanleur2234-glitch/persistent-agent-framework
- **What it does:** Production architecture turning stateless Claude Code into persistent, self-correcting agent. Mistake→ledger→pattern detection (3x)→auto-generated behavioral directive loop. Multi-terminal + multi-platform (CLI/Telegram/Discord/web) from single definition. MIT licensed.
- **Solomon OS fit:** FORGE — self-correction ledger IS the evolution engine for Hermes. Marker processing + soul assembly + sweep-based daemon = full autonomous operation. MIT permits direct use.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/T33R0-persistent-agent-framework.md

## Grail-Computer/Self-Improving-Agent — AGENTS.md Compounding Template (April 21, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/Self-Improving-Agent
- **Fork:** https://github.com/Grail-Computer/Self-Improving-Agent → jvanleur2234-glitch/Self-Improving-Agent
- **What it does:** Minimal starter template: AGENTS.md (always-on context) + self-improving-agent SKILL.md (meta-skill). Agents compound effectiveness over time: Work→Complete→Reflect→Record→Next task starts from better baseline. MIT licensed.
- **Solomon OS fit:** INTEGRATE — AGENTS.md pattern validates Solomon Vault brain file approach. Self-improving-agent SKILL.md maps to Hermes skill ecosystem. Compounding loop is core to JCPaid value prop.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/Grail-Computer-Self-Improving-Agent.md

## n8n MCP Node — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/n8n-nodes-mcp
- **What it does:** n8n community node to connect MCP servers from n8n workflows. Enables non-programmers to build AI agent workflows that call MCP tools (including Hermes).
- **Solomon OS fit:** INTEGRATE — bridges n8n automation builder to Hermes MCP skill system. JackConnect workflow builder → n8n → Hermes MCP tools via STDIO or HTTP Streamable transport.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/n8n-nodes-mcp.md

## cisco-ai-defense/mcp-scanner — MCP Security Multi-Engine Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/mcp-scanner
- **What it does:** Multi-engine MCP security scanner using YARA rules, LLM-as-judge, and Cisco AI Defense. Scans MCP tools, prompts, resources, server instructions. CVE/PySEC/GHSA scanning via pip-audit. VirusTotal binary hashing. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — security gate for Hermes MCP server ecosystem. Deploy in CI/CD pipeline for agent deployment gatekeeping. 15+ risk categories.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/mcp-scanner-cisco.md

## yogirk/agent-council — Lightweight CLI Multi-Agent Deliberation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-council
- **What it does:** Lightweight CLI-based multi-agent council pattern. 3 agents (Claude Code, Codex, Gemini CLI) in parallel → anonymized peer review → chairman synthesis. File-based state, MIT.
- **Solomon OS fit:** SKILL — deliberation pattern for Hermes. Could enhance skill validation with multiple expert agents reviewing decisions.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-council-yogirk.md

## gollem — Type-Safe Go Agent Framework (April 22, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **Fork:** Already forked (Go project, different tech stack)
- **What it does:** Production-grade Go agent framework with compile-time type safety. Generic Agent[T], 5+ LLM backends, FuncTool with JSON Schema generation, streaming via iter.Seq2, guardrails (input/turn/output validation, auto-repair), OpenTelemetry middleware, state snapshots.
- **Solomon OS fit:** INTEGRATE — guardrail patterns and middleware architecture useful for Hermes security layer. Type-safe tool pattern worth studying for future Go-based Hermes components.
- **Status:** MONITOR / REFERENCE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/gollem.md

## vercel/agent-browser — Native Rust Browser Automation CLI (April 22, 2026)
- **URL:** https://github.com/vercel-labs/agent-browser
- **Fork:** NO (Apache 2.0, reference only)
- **What it does:** Native Rust CLI for AI agent browser automation. Accessibility tree + ref-based targeting (@e1, @e2), CSS/role selectors, screenshot, keyboard, multi-browser. Already installed locally at /usr/local/bin/agent-browser.
- **Solomon OS fit:** MONITOR — Fast Rust implementation. Already available in environment. Could influence Hermes browser tooling architecture.
- **Status:** MONITOR / REFERENCE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/vercel-agent-browser.md

## dnhess/spectra — Multi-Agent Deliberation Skills (April 22, 2026)
- **URL:** https://github.com/dnhess/spectra
- **Fork:** NO (MIT, Claude Code specific ecosystem)
- **What it does:** 5 deliberation skills using blackboard architecture: deep-design (multi-perspective design review), decision-board (structured debate → ADR), peer-review (code review with reconnaissance), trust-layer (4 adversarial personas), coherence-monitor (metacognitive audit).
- **Solomon OS fit:** SKILL — trust-layer adversarial verification could enhance Hermes output scanning. Blackbox architecture useful for multi-agent coordination patterns.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/spectra.md

## GoPlusSecurity/agentguard — Multi-Layer AI Agent Security Guard (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentguard
- **What it does:** Three-layer security guard: (1) Automatic Guard blocks dangerous commands + sensitive file writes + exfil detection with skill tracking; (2) Deep Scan auto-scans skills with 24 rules for secrets/backdoors/injection; (3) Daily Patrol for posture checks, tamper detection, audit analysis.
- **Solomon OS fit:** INTEGRATE — core runtime security layer for Hermes. Layered approach fills JCPaid enterprise security needs. OpenClaw integration already available. Apache 2.0 compatible.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/GoPlusSecurity-agentguard.md

## gonka-ai/gonka — P2P AI Compute with DiLoCo Training (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/gonka
- **What it does:** Decentralized P2P AI compute platform. Hosts pool GPU/CPU for training/inference and earn rewards. Proof-of-Work 2.0 Sprint mechanism governs allocation. DiLoCo-style geo-distributed training. Randomized probabilistic task verification.
- **Solomon OS fit:** SKILL — DiLoCo compression patterns for distributed training. P2P compute pooling directly competes with AgentFM. Sprint governance informs agent economy tokenomics.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/gonka-decentralized-ai-compute.md
