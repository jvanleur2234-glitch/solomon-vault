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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
- **Fork:** jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Minimal adversarial framework separating generator (proposes improvement) from evaluator (judges independently). Prevents self-delusion. All changes require human approval. Governance separation: autonomously-implementable vs. human-review-required changes.
- **Solomon OS fit:** FORGE — Adversarial self-improvement with separation of concerns critical for safe autonomous growth. MIT license permits direct use. Governance separation essential for Hermes self-evolution safety.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/nfh-self-improvement-loop-adversarial.md

## n8n-nodes-agent2agent — Google A2A Protocol Bridge (April 23, 2026)
- **URL:** https://github.com/pjawz/n8n-nodes-agent2agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-agent2agent
- **What it does:** n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discover agents via Agent Card, send tasks (text/file/JSON), wait for completion, retrieve results. MIT licensed.
- **Solomon OS fit:** INTEGRATE — A2A protocol bridge. If Hermes implements A2A (agent cards, task protocol), enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-agent2agent-a2a-protocol.md

## n8n-nodes-claude-agent — Claude Code in n8n Workflows (April 23, 2026)
- **URL:** https://github.com/MyCoderAI/n8n-nodes-claude-agent
- **Fork:** jvanleur2234-glitch/n8n-nodes-claude-agent
- **What it does:** n8n community node integrating Claude Code autonomous agent capabilities. Generates code from natural language (10+ languages), executes autonomous coding tasks with configurable permissions and tool access.
- **Solomon OS fit:** SKILL — Claude Code integration pattern for n8n. Could inform Hermes node for n8n (separate from MCP approach). MIT license permits study and integration patterns.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/n8n-nodes-claude-agent-mycoderai.md

## n8n-nodes-mcp — n8n Workflow → Hermes MCP Bridge (April 22, 2026)
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

## Ouroboros — Self-Modifying Agent with Git-Based Code Evolution (April 22, 2026)
- **URL:** https://github.com/razzant/ouroboros
- **Fork:** Already cloned (`/home/workspace/ouroboros`)
- **What it does:** Self-modifying AI agent that rewrites its own code via git. Multi-LLM review gate (o3, Gemini, Claude) validates changes. Constitution-based governance (BIBLE.md with 9 principles). Persistent identity across restarts. MIT licensed, ~515 stars.
- **Solomon OS fit:** SKILL — Multi-LLM review gate pattern for Hermes self-improvement safety. Constitution governance model. Git-based skill versioning concept. Study for Hermes self-evolution architecture.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ouroboros-self-modifying-agent.md

## dayour/copilotbrowser — Multi-Browser AI Automation with "Follow Me" Mode (April 22, 2026)
- **URL:** https://github.com/dayour/copilotbrowser
- **Fork:** Already cloned (`/home/workspace/copilotbrowser`)
- **What it does:** Node.js multi-browser automation (Chromium, Firefox, WebKit) via single API. Native MCP server. "Follow Me" mode records user browsing and replays exact steps autonomously. VS Code extension. Apache 2.0, ~1 star (nascent).
- **Solomon OS fit:** SKILL — "Follow Me" recording could auto-generate Hermes browser-based skills from user actions. Multi-browser MCP integration for Claude Desktop/VS Code agent.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/copilotbrowser.md

## ClawSecure — OpenClaw Security Scanner & Audit Platform (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/clawsecure-openclaw-security
- **What it does:** Independent security integrity layer for OpenClaw. 3-Layer Audit Protocol (threat intel → static/behavioral analysis → supply chain), OWASP ASI Top 10 coverage (all 10 categories), 55+ AI agent threat patterns, Watchtower 24/7 hash-drift monitoring, Security Clearance API. Audited 3,000+ skills; 41% contain vulnerabilities.
- **Solomon OS fit:** INTEGRATE — Study 3-Layer Audit Protocol for Hermes security gate. Watchtower pattern for skill integrity monitoring. Context-Aware Intelligence differentiates real threats from legitimate agent capabilities. SOC2 evidence maps to JCPaid enterprise needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/clawsecure-openclaw-security.md

## AgentAudit MCP — Security Scanner for AI Agent Packages (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agentaudit-mcp
- **What it does:** Security scanner for AI agent packages. CLI and MCP server. Scans MCP servers, AI skills, packages for vulnerabilities, prompt injections, supply chain attacks. Uses regex static analysis + 3-pass LLM deep audits. Trust Registry for audited packages.
- **Solomon OS fit:** INTEGRATE — Package auditing before skill installation. Trust Registry concept for verifying third-party skills. MCP server for IDE integration (Claude Desktop, Cursor, Windsurf).
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentaudit-mcp.md

## Sinewave Agent Security Scanner MCP — Prompt Injection Firewall (April 22, 2026)
- **Fork:** Already forked (`sinewave-agent-security-scanner-mcp`)
- **What it does:** MCP server security scanner for AI coding agents. Prompt injection firewall. Package hallucination detection (4.3M+ packages). 1000+ vulnerability rules with AST & taint analysis. Auto-fix suggestions.
- **Solomon OS fit:** INTEGRATE — Core security for Hermes agent code generation. Package hallucination detection prevents supply chain attacks. AST/taint analysis for skill code review.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## guard-scanner — Agentic Workflow Security Scanner (April 22, 2026)
- **Fork:** Already forked (`guard-scanner-new`)
- **What it does:** Security scanner for agentic workflows. 364 detection patterns across 35 threat categories, 27 runtime checks. Focus on prompt injections, identity hijacking, memory poisoning, A2A contagion. OWASP Agentic Top 10 aligned. SOUL.md locking.
- **Solomon OS fit:** INTEGRATE — Identity hijack detection for Hermes agent identities. A2A contagion detection for multi-agent communication. SOUL.md protection aligns with Hermes SOUL.md concept.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/guard-scanner.md

## Quorum — Multi-Agent AI Deliberation Framework (April 22, 2026)
- **Fork:** Already forked (`Quorum`)
- **What it does:** TypeScript MIT-licensed multi-AI deliberation framework. 7-phase deliberation (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote). Borda/ranked-choice/Condorcet voting. Evidence protocol with citations. SHA-256 ledger for deterministic replay. MCP server compatible.
- **Solomon OS fit:** SKILL — Structured deliberation for critical Hermes decisions. Evidence protocol adds trust to multi-agent reasoning. Configurable debate topologies (mesh, star, tournament, pipeline) for Council of High Intelligence.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/quorum.md

## MedIT One — Recurrent Transformer with MoE (April 22, 2026)
- **Fork:** Already forked (`medit-one`, `medit-one-new`)
- **What it does:** Fast memory-efficient transformer combining recurrent-style state (hx, cx) with MoE. Single-token inference with constant memory footprint. Hidden-state self-attention (linear scaling). CUDA-accelerated with FP16/BF16.
- **Solomon OS fit:** SKILL — Study architecture for Hermes long-context agentic workflows. Recurrent state management for persistent agent memory. MoE for efficient multi-task agent processing.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medit-one.md

## browserclaw-agent — Auto-Learning Browser Automation Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **What it does:** Modular TypeScript browser agent with 3 swappable layers (LLM/agent/browser). Auto-learns domain-specific playbooks from successful runs. Built-in Cloudflare Turnstile solving, anti-bot bypass, cookie banner dismissal, tab management.
- **Solomon OS fit:** INTEGRATE — Browser layer for Solomon Browser. Anti-bot handling and auto-learning skill catalog directly applicable.
- **Status:** INTEGRATE

## agent-security-scanner (Cybathreat) — Comprehensive Agent Security Auditor (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner
- **What it does:** 11-module security scanner for AI agents. Covers: prompt injection, tool boundary violations, RAG pipeline security, agent attacks (memory poisoning, recursive exploitation, planning manipulation), infrastructure security. MIT licensed, OWASP/MITRE mapped.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes. Most comprehensive open-source agent security scanner. Deploy in CI/CD as pre-deployment skill gate.
- **Status:** INTEGRATE

## Hivemind — Decentralized P2P Deep Learning (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hivemind
- **What it does:** PyTorch library for decentralized training across Internet peers. DHT-based peer discovery, fault-tolerant backpropagation, decentralized parameter averaging, MoE layer distribution. Apache 2.0, 4K+ stars.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. DHT peer coordination patterns for future agent training workloads.
- **Status:** SKILL

## HyperAgents (Facebook) — Meta-Agent Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/HyperAgents
- **What it does:** Facebook AI Research self-referential, self-improving agents. Meta-agent rewrites its own reasoning strategies based on performance feedback. Hierarchical meta→task agent pattern.
- **Solomon OS fit:** SKILL — Self-improvement loop architecture study for Hermes autonomous capability growth. Meta→task agent hierarchy applicable to Council of High Intelligence.
- **Status:** SKILL

## agent-security (empowered-humanity) — Static Analysis + Runtime Security Library (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-security
- **What it does:** 176+ detection patterns with taint analysis, OWASP ASI + MCP coverage, CWE mappings, SARIF output, SSRF/path traversal guards, 220+ AI-agent patterns. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Core security gate for Hermes alongside Cybathreat scanner. Defense-in-depth for JCPaid enterprise security needs.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-security-empowered-humanity.md

## SecureVector AI Threat Monitor — Real-Time Agent Security Firewall (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local real-time AI security firewall. Proxy mode across OpenAI/Anthropic/Ollama. Skill Scanner with policy engine, per-agent tool permissions, cost tracking, 28 new threat rules. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Real-time enforcement layer for Hermes. Proxy-mode deployment fits Solomon OS architecture. Skill Scanner for third-party Hermes skills.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## TheAgenticBrowser — Three-Agent Plan/Execute/Critique Loop (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/TheAgenticBrowser
- **What it does:** Python/PydanticAI browser automation with Planner→Browser Agent→Critique loop. Cross-domain data correlation, workflow feedback. NOASSERTION license.
- **Solomon OS fit:** SKILL — Architecture reference for browser automation. Three-agent loop pattern applicable to Solomon Browser. Verify license before integration.
- **Status:** SKILL

## nanobrowser — Chrome Extension AI Browser Automation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nanobrowser
- **What it does:** Chrome extension + MCP server for AI-powered browser automation. Multi-agent collaboration, local execution, OpenAI/Anthropic/Gemini/Ollama providers. Apache 2.0, 800+ stars.
- **Solomon OS fit:** SKILL — Study extension deployment model for potential Solomon Browser extension. MCP server integration fits Hermes ecosystem.
- **Status:** SKILL

## openbrowser — TypeScript Playwright Browser Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/openbrowser
- **What it does:** MIT-licensed TypeScript browser automation on Playwright. Multi-model support (OpenAI/Anthropic/Google), interactive REPL, stall detection, session management. 600+ stars.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser. MIT license, multi-model support aligns with Hermes strategy. Direct competitor to browserclaw-agent.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/openbrowser-ts-browser-automation.md

## deep-claw — Dream Cycle Self-Improvement Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deep-claw
- **What it does:** Dream Cycle for autonomous agents. Nightly Mode (research scanning) + Weekly Mode (performance reflection). Evidence-based improvement with rollback plans, governance separation. MIT licensed.
- **Solomon OS fit:** SKILL — Self-improvement governance framework for Hermes. Governance separation (autonomous vs human-review-required) critical for safe autonomous growth.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deep-claw-self-improving-agent.md

## Miguel — Docker-Sandboxed Self-Improving Agent (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/miguel
- **What it does:** Self-improving agent with Docker sandbox. Coordinator + sub-agents (Coder/Researcher/Analyst). 22 capabilities, auto-commit/push on validation success. MIT licensed.
- **Solomon OS fit:** SKILL — Docker sandbox architecture study for Hermes self-improvement safety. Sub-agent delegation pattern maps to Hermes skill system.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/miguel-self-improving-agent.md

## self-improving-ai-agent (pratiksangle) — Generator→Critic→Improver Pipeline (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/self-improving-ai-agent-pratik
- **What it does:** Python multi-agent pipeline: Generator → Critic (5-dimension scoring) → Improver loop. Rule-based or API mode. MIT licensed.
- **Solomon OS fit:** SKILL — Generator-Critic-Improver loop pattern for Hermes response refinement skills.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/self-improving-ai-agent-pratik.md

## nfh-self-improvement-loop — Adversarial Self-Modification Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/nfh-self-improvement-loop
- **What it does:** Generator→Evaluator adversarial self-modification. Strict safeguards: no identity/memory edits, no external API calls during modification, rollback plans. MIT licensed.
- **Solomon OS fit:** SKILL — Adversarial review layer for Hermes self-improvement. Generator/evaluator separation prevents runaway self-modification.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## Agent Express — Express.js-Style Middleware Agent Framework (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **What it does:** Minimalist TypeScript agent framework. Express.js `(ctx, next)` middleware pattern applied to AI agents. 5-layer middleware onion (agent, session, turn, model, tool). Built-in safety guards, 12+ multi-provider routing, memory compaction, MCP integration, Zod structured output.
- **Solomon OS fit:** SKILL — Middleware composition pattern directly maps to Hermes skill pipeline. Clean way to add cross-cutting concerns (auth, rate limiting, logging, safety) without modifying core agent code. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Dapr Agents — Kubernetes-Native Agent Orchestration (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agent systems built on Dapr. Durable execution workflow engine, scalable multi-agent workflows across clusters, automatic retries, Kubernetes-native deployment, security + observability by default. Apache 2.0.
- **Solomon OS fit:** SKILL — Dapr sidecar pattern IS the production reference architecture for agent runtimes. Durable execution = persistent agent sessions. Apache 2.0 for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## Snyk Agent Scan — Agent Security Inventory & Scanner (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-scan
- **What it does:** Auto-discovers + scans agent components (MCP servers, skills) for prompt injections, malware payloads, hardcoded secrets. Supports: Windsurf, Cursor, VS Code, Claude Desktop/Code, Gemini CLI, OpenClaw, Amp, Amazon Q, Kiro, Codex. 15+ distinct security risk categories.
- **Solomon OS fit:** INTEGRATE — Mandatory pre-flight security audit for every Solomon OS deployment. Client onboarding check. Maps to JCPaid enterprise compliance (SOC2). Already forked.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## AIBYAI — Multi-Agent Deliberative Council (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** 4-7 concurrent agents argue, critique, produce scored consensus with numeric confidence. Cold validator catches hallucinations. Confidence formula: `0.6 × Agreement + 0.4 × PeerRanking`. 13+ provider failover, topic graph memory, per-query cost tracking. MCP-compatible. TypeScript/React/Fastify.
- **Solomon OS fit:** FORGE — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring gives clients reliability signal on high-stakes decisions. MIT license.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aibyai.md

## Reflexio — Self-Improving Agent Harness (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio
- **What it does:** Open-source self-improvement harness for AI agents. Learns from user corrections, persists playbooks, reduces repetitive mistakes. Claims ~81% reduction in planning steps, ~72% token savings when benchmarked against Hermes.
- **Solomon OS fit:** INTEGRATE — The reflexio hub → playbooks → improved behavior loop is exactly what Hermes needs for autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/reflexio-self-improvement-harness.md`

## Quorum — Multi-AI Deliberation Framework (April 23, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** TypeScript multi-AI deliberation framework. 7-phase debate process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across multiple providers (OpenAI, Claude, Gemini, DeepSeek, etc.) with confidence scoring and minority reports.
- **Solomon OS fit:** SKILL — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/Quorum-multi-ai-deliberation.md`

## Gollem — Type-Safe Go Agent Framework (April 23, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Production-ready Go agent framework with compile-time type safety, zero-allocation streaming, and 50+ primitives. Multi-provider LLM support, comprehensive guardrails, OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — Study for type-safe agent architecture patterns. Go's compile-time safety model could inspire Hermes reliability improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/gollem-go-agent-framework.md`

## deep-claw — Dream Cycle Self-Improvement Framework (April 23, 2026)
- **URL:** https://github.com/the-keats-ai/deep-claw
- **What it does:** Self-improvement framework inspired by sleep. Nightly scanning of research/tools, weekly reflection, citation-backed self-assessment, falsifiable improvement proposals with rollback strategies.
- **Solomon OS fit:** FORGE — The Dream Cycle IS the self-improvement loop for Solomon OS. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/deep-claw-dream-cycle-self-improvement.md`

## Medusa — AI-First Security Scanner (April 23, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** 9,600+ detection patterns, 200 CVE detections including MCP-related risks. No-setup usage, multi-core parallel processing, repo-poisoning detection across 28+ file types, SARIF output.
- **Solomon OS fit:** INTEGRATE — Core security primitive for Hermes. MIT licensed. MCP CVE detections directly address current OWASP agentic AI threats.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/medusa-ai-security-scanner.md`

## Vibium — Lightweight Browser Automation (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB browser automation binary with no runtime deps. Built on WebDriver BiDi standard. Install as skill for zero-config browser control. MCP server mode available.
- **Solomon OS fit:** INTEGRATE — Browser automation for Solomon Browser POC. Lighter than Playwright for simple tasks.
- **Status:** INTEGRATE
- **RD Report:** `/brain/RD_REPORTS/vibium-browser-automation.md`

## browserclaw-agent — Robust Browser Agent with Skills (April 23, 2026)
- **URL:** https://github.com/idan-rubin/browserclaw.agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), skill learning (learns successful playbooks per domain), loop detection, tab management. Three-layer architecture.
- **Solomon OS fit:** FORGE — Robust browser automation with skill learning mechanism. MIT license permits direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/browserclaw-agent-robust-browser-automation.md`

## KwaaiNet — Sovereign P2P AI Infrastructure (April 23, 2026)
- **URL:** https://github.com/Kwaai-AI-Lab/KwaaiNet
- **What it does:** Rust-based P2P AI compute with Decentralized Trust Graph (DTG), W3C Verifiable Credentials, Ed25519 identity. Pre-built binaries for all platforms.
- **Solomon OS fit:** SKILL — P2P trust graph architecture study. Could inspire Solomon Air distributed compute layer.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/kwaiinet-p2p-ai-infrastructure.md`

## VoltAgent — TypeScript AI Agent Platform (April 23, 2026)
- **URL:** https://github.com/ChengXinDL/voltagent
- **What it does:** End-to-end TypeScript agent platform with typed agent roles, supervisor/sub-agent orchestration, MCP integration, durable memory adapters, declarative workflow engine, guardrails, and evals.
- **Solomon OS fit:** SKILL — Study typed agent architecture and MCP patterns for Hermes improvements.
- **Status:** SKILL
- **RD Report:** `/brain/RD_REPORTS/voltagent-typescript-agent-framework.md`

## council — Structured Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **What it does:** Python framework for structured multi-agent debate. Persona-based agents (Architect, Critic, Security Specialist), 7-phase debate lifecycle, moderator synthesis, Markdown report generation.
- **Solomon OS fit:** FORGE — Direct implementation candidate for Hermes "Council" mode. MIT license enables direct use.
- **Status:** FORGE
- **RD Report:** `/brain/RD_REPORTS/council-multi-agent-debate-framework.md`
## malovnik/agent-browser — Token-Efficient Text-First Browser (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-browser
- **Forked from:** https://github.com/malovnik/agent-browser
- **What it does:** Text-first browser for AI agents. Reads pages via accessibility tree (17x lower token cost vs screenshots), semantic action discovery, predictive browsing engine with page diffs.
- **Solomon OS fit:** SKILL — token-efficient browsing patterns for Hermes/ClawLess. Replace screenshot with text-based semantic interaction.
- **Status:** SKILL

## idan-rubin/browserclaw-agent — Anti-Bot Browser Agent (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserclaw-agent
- **Forked from:** https://github.com/idan-rubin/browserclaw-agent
- **What it does:** AI browser agent with built-in anti-bot bypass (CDP), Cloudflare Turnstile solving, domain learning (skill files per site), loop detection. Modular LLM-agnostic architecture.
- **Solomon OS fit:** SKILL — anti-bot/Turnstile solving fills major gap in ClawLess. MIT license permits study.
- **Status:** SKILL

## mycellm — P2P GPU Inference Network (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/mycellm
- **What it does:** Pools GPUs across internet into P2P inference network. OpenAI-compatible API, credit-based economy, private federated networks, no cloud vendors.
- **Solomon OS fit:** SKILL — credit economy pattern for agent compute marketplace. Competitor to AgentFM with different architecture.
- **Status:** SKILL

## artemis-agents — Structured Multi-Agent Debates with N Agents (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/artemis-agents
- **Forked from:** https://github.com/bassrehab/artemis-agents
- **What it does:** N-agent debate framework with hierarchical argument generation, causal reasoning evaluation, jury scoring, ethical alignment, safety monitoring (sandbagging, deception detection).
- **Solomon OS fit:** INTEGRATE — deliberation engine for Hermes skill validation. N-agent > Council of High Intelligence. MIT license.
- **Status:** INTEGRATE

## microsoft/agent-framework — Enterprise Multi-Language Agent Framework (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft multi-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging. python-1.1.0 (2026-04-21).
- **Solomon OS fit:** SKILL — time-travel debugging and enterprise workflow patterns worth studying. MIT license.
- **Status:** SKILL

## Firmislabs/firmis-scanner — 18+ Threat Categories for Agent Security (April 23, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** AI-runtime security scanner with 268 detection rules across 18+ threat categories (credential harvesting, prompt injection, tool poisoning). Auto-detects LangChain, CrewAI, AutoGen, MetaGPT. Apache-2.0.
- **Solomon OS fit:** INTEGRATE — adds to security scanning stack alongside ProofLayer/Sinewave. Auto-framework detection is valuable.
- **Status:** INTEGRATE

## X/Twitter Trends (April 23, 2026)
- **Hermes Agent** — Growing fast. Tony Simons: "first AI agent platform I'd be willing to market and distribute as a professional install service." Julian Goldie SEO: cloud-hosted Hermes is "beta, not serious replacement." Higgsfield Marketing Studio powered by Hermes getting buzz.
- **AI Security** — OWASP Top 10 for Agentic Applications 2026 confirmed. Real incidents targeting agent identities, orchestration layers. "Agents as primary attack vector" — not theoretical. SANS called it emergency.
- **Self-improving AI** — Federated learning defenses can survive 50%+ malicious clients (arxiv 2604.03226). Bell Cyber autonomous SOC contains threats in <5 min.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. POCI architecture shows multi-step agents beat single models by 21%.

## dialectic-agentic — Skill-File Multi-Agent Debate (April 23, 2026)
- **URL:** https://github.com/slior/dialectic-agentic
- **Fork:** jvanleur2234-glitch/dialectic-agentic
- **What it does:** Self-contained multi-agent debate system for software system design. Runs as skill files + prompts + JSON config — no traditional code required. Personas (architect, security, critic) take turns proposing, critiquing, refining. Judge evaluates convergence.
- **Solomon OS fit:** FORGE — Deliberation pattern directly maps to Council of High Intelligence. MIT license permits direct use. Skill-file based architecture compatible with Hermes skill ecosystem.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/dialectic-agentic-multi-agent-debate.md

## pilo — Mozilla Tabstack AI Browser Automation (April 23, 2026)
- **URL:** https://github.com/mozilla/pilo
- **License:** Apache 2.0
- **What it does:** AI-powered web automation tool. Control browsers with natural language commands. Fill forms, navigate, extract data. CLI + programmatic Playwright integration. Guardrails for safe automation.
- **Solomon OS fit:** SKILL — Browser automation patterns for Solomon Browser. Natural language → browser action mapping useful for ClawLess competitor analysis.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/pilo-mozilla-ai-browser-automation.md

## self_improving_coding_agent — Iterative Benchmark-Driven Self-Improvement (April 23, 2026)
- **URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent
- **Fork:** jvanleur2234-glitch/self_improving_coding_agent
- **What it does:** Coding agent that iteratively improves its own codebase via benchmark evaluation → archive → improvement loop. Docker-isolated execution. Multi-LLM provider support. Visualizes event bus and callgraph at localhost:8080.
- **Solomon OS fit:** FORGE — Self-improvement loop (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/self-improving-coding-agent-iterative.md

## nfh-self-improvement-loop — Adversarial Generator/Judge Self-Improvement (April 23, 2026)
- **URL:** https://github.com/theprint/nfh-self-improvement-loop
-
## phero — Go Agent Framework with A2A Protocol (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/phero
- **Forked from:** https://github.com/henomis/phero
- **What it does:** Go 1.25+ agent framework with A2A protocol, MCP integration, role-based handoffs, multi-modal LLM support, vector stores (Qdrant/pgvector/Weaviate), SKILL.md-based skills. Apache-2.0.
- **Solomon OS fit:** FORGE — A2A protocol + Go agent model for Solomon Bus v2 inter-agent communication spec. Apache-2.0 permits code use.
- **Status:** FORGE

## dapr-agents — Kubernetes-Native Agent Orchestration (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/dapr-agents
- **Forked from:** https://github.com/dapr/dapr-agents
- **What it does:** Python agent framework on Dapr. Workflow orchestration, durable/retryable workflows, multi-agent collaboration, built-in telemetry. Apache-2.0.
- **Solomon OS fit:** SKILL — Dapr state/pubsub primitives for Job Runner persistence. Kubernetes-native architecture for enterprise Solomon OS deployments.
- **Status:** SKILL

## ouroboros — Self-Creating AI Agent (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/ouroboros
- **Forked from:** https://github.com/kazmak927/ouroboros
- **What it does:** Self-modifying AI agent. Commits code changes to own Git repo. Multi-model review (o3/Gemini/Claude) validates before commit. 30+ autonomous cycles in 24hrs. MIT.
- **Solomon OS fit:** FORGE — Self-modification loop IS Hermes self-evolution. Multi-model review = safety gate. MIT permits code use.
- **Status:** FORGE

## HyperAgents — Meta-Learning Self-Improving Agents (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/HyperAgents
- **Forked from:** https://github.com/facebookresearch/HyperAgents
- **What it does:** Meta-research framework: meta-agent generates/refines task agents via iterative loops. Docker-contained runs. NoAssertion license.
- **Solomon OS fit:** SKILL — Architecture reference only (no code use allowed). Meta-agent loop concept aligns with self-improvement pipeline.
- **Status:** SKILL

## KwaaiNet — Rust P2P Trust Graph (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/KwaaiNet
- **Forked from:** https://github.com/cicada-369/KwaaiNet
- **What it does:** Rust P2P network for distributed AI compute. Distributed Trust Graph (DID + Ed25519 + verifiable credentials), persistent node identity, trust scoring with time-decay. MIT.
- **Solomon OS fit:** FORGE — Trust graph for Solomon Air node authentication. Rust core aligns with Bonsai/Thoth/RustDesk stack. MIT permits code use.
- **Status:** FORGE

## firmis-scanner — AI Runtime Security Scanner (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/firmis-scanner
- **Forked from:** https://github.com/Firmislabs/firmis-scanner
- **What it does:** Scans AI agents for credential harvesting, prompt injection, tool poisoning. 268 rules. Scans SKILL.md/AGENTS.md surfaces. TypeScript. MIT.
- **Solomon OS fit:** INTEGRATE — Pre-execution security gate for Hermes skills. OWASP ASI aligned. MIT permits code use.
- **Status:** INTEGRATE

## council — OpenClaw Multi-Agent Deliberation (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/council
- **Forked from:** https://github.com/infektyd/council
- **What it does:** Parallel deliberation across xAI personas (WORKHORSE/CREATIVE). Auditable transcripts, Discord visibility. Verdict + Deliberation modes. MIT.
- **Solomon OS fit:** SKILL — Deliberation topology study for Hermes Council of High Intelligence. MIT permits adaptation.
- **Status:** SKILL

## deliberate — Shell-Based Async Deliberation (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/deliberate
- **Forked from:** https://github.com/kyleparrott/deliberate
- **What it does:** Minimal file-based async deliberation protocol for two AI agents via JSONL. read→ack→send→wait→repeat→done loop. Shell + jq. MIT.
- **Solomon OS fit:** SKILL — Minimal deliberation protocol reference for Solomon Bus inter-agent messaging format. Not production-ready.
- **Status:** SKILL

## magnitude — Vision-First Browser Automation (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/magnitude
- **Forked from:** https://github.com/magnitudedev/browser-agent
- **What it does:** Vision-grounded browser automation (no DOM selectors). 90% Web Voyager. Self-healing via vision. Apache-2.0.
- **Solomon OS fit:** FORGE — Vision-based approach for Solomon Browser. ClawLess competitor with different paradigm. Apache-2.0 permits code use.
- **Status:** FORGE

## browserable — Self-Hosted Browser Library (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/browserable
- **Forked from:** https://github.com/browserable/browserable
- **What it does:** JavaScript AI browser automation. 90% Web Voyager. Docker-based. MIT.
- **Solomon OS fit:** SKILL — Architecture reference for Solomon Browser POC. MIT permits study.
- **Status:** SKILL

## agentbrowser — Semantic Browser Runtime (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agentbrowser
- **Forked from:** https://github.com/AshtonVaughan/agentbrowser
- **What it does:** TypeScript semantic browser runtime. Structured page models reduce tokens dramatically. Site memory, self-healing, MCP support. MIT.
- **Solomon OS fit:** FORGE — Semantic page model + memory for Solomon Browser. MIT permits direct code use.
- **Status:** FORGE

## agent-discover-scanner — Enterprise AI Agent Inventory (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-discover-scanner
- **Forked from:** https://github.com/Defend-AI-Tech-Inc/agent-discover-scanner
- **What it does:** Auto-inventories AI agents via static code analysis + runtime eBPF. Classifies: CONFIRMED/UNKNOWN/SHADOW AI/ZOMBIE/GHOST. AIBOM compliance. GPL-3.0.
- **Solomon OS fit:** INTEGRATE — GHOST detection for enterprise governance. Discovers "what is actually running" vs code-only. GPL-3.0 — code reference only.
- **Status:** INTEGRATE

## agentic_security — AI Red Teaming Toolkit (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agentic_security
- **Forked from:** https://github.com/msoedov/agentic_security
- **What it does:** Enterprise vulnerability scanner for LLM agents. Multimodal attacks, RL-based adaptive probes, multi-step jailbreaks, CI integration. OWASP Top 10 for LLMs. MIT. 1849 stars.
- **Solomon OS fit:** INTEGRATE — Pre-deployment security gate for Hermes skills. Red-team baseline for Agent Armor Studio. Complements firmis-scanner with dynamic/adaptive testing.
- **Status:** INTEGRATE

## mcps-audit — OWASP MCP Security Scanner (April 24, 2026)
- **URL:** (OWASP official tool, not forked)
- **Source:** https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/issues/805
- **What it does:** Scans MCP server code against OWASP Agentic AI Top 10 (AS-001 to AS-012). PDF reports with MITRE ATT&CK mappings. npx mcps-audit ./my-agent.
- **Solomon OS fit:** FORGE — Pre-installation security gate for all Hermes MCP servers. CI/CD integration. SOC 2 compliance evidence. OWASP-authoritative.
- **Status:** FORGE

## Agent Orcha — Declarative Multi-Agent Framework (April 24, 2026)
- **URL:** https://github.com/ddalcu/agent-orcha
- **Fork:** jvanleur2234-glitch/agent-orcha
- **What it does:** Declarative YAML-based multi-agent orchestration with P2P agent sharing, MCP integration, built-in vector store, browser sandbox (Chromium/CDP/Xvfb), ReAct support, and Agent Orcha Studio web UI.
- **Solomon OS fit:** FORGE — Declarative YAML config for agents/workflows maps to Hermes skill format. P2P sharing aligns with agent economy vision. Built-in browser sandbox competes with Solomon Browser POC.
- **Status:** SKILL — study YAML orchestration pattern, P2P sharing model
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-orcha.md

## Gollem — Go Agent Framework (April 24, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **Fork:** jvanleur2234-glitch/gollem
- **What it does:** Production Go agent framework with compile-time type safety, zero-allocation streaming, multi-provider LLM support (Anthropic, OpenAI, Google), typed FuncTool, structured output, guardrails, middleware, and OpenTelemetry tracing.
- **Solomon OS fit:** SKILL — study type-safe agent patterns for potential Go-based Solomon components. Guardrails implementation is reference-quality.
- **Status:** SKILL — architecture study only
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/gollem.md

## Phero — Go Multi-Agent Framework (April 24, 2026)
- **URL:** https://github.com/henomis/phero
- **Fork:** jvanleur2234-glitch/phero
- **What it does:** Go-based multi-agent AI with A2A protocol (HTTP inter-agent communication), agent handoffs, skills system (SKILL.md), MCP integration, multimodal input, memory management, and tracing. Requires Go 1.25.5+.
- **Solomon OS fit:** SKILL — A2A protocol design study. Skills system (SKILL.md) aligns with Hermes skills. Go-based for high-performance scenarios.
- **Status:** SKILL — protocol/skills architecture study
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/phero-go-multi-agent.md

## Agentrail — TypeScript Agent Framework (April 24, 2026)
- **URL:** https://github.com/yai-dev/agentrail
- **Fork:** jvanleur2234-glitch/agentrail
- **What it does:** TypeScript framework for production-ready tool-using agents. Composable runtime core, hosted server layer, multi-agent orchestration, session memory, knowledge retrieval, sandboxed execution, and Docker isolation.
- **Solomon OS fit:** SKILL — study TypeScript agent patterns for browser-based agents. Docker sandbox aligns with security requirements.
- **Status:** SKILL — architecture study
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agentrail.md

## Agent Security Scanner — Critical Finding (April 24, 2026)
- **URL:** https://github.com/sinewaveai/agent-security-scanner-mcp
- **Fork:** jvanleur2234-glitch/sinewave-agent-security-scanner-mcp
- **What it does:** Enterprise security scanner for AI coding agents. Prompt injection firewall, package hallucination detection (4.3M+ packages), 1700+ vulnerability rules via AST/taint analysis, LLM semantic code review, SBOM generation, SOC2/GDPR compliance evidence. ClawHub integration available.
- **Solomon OS fit:** INTEGRATE — core security primitive for every skill/tool invocation. SOC2 evidence maps to JCPaid enterprise clients. Active development with latest release April 22, 2026.
- **Status:** INTEGRATE — install as pre-execution gate
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/sinewave-agent-security-scanner-mcp.md

## Browserable — AI Browser Automation (April 24, 2026)
- **URL:** https://github.com/browserable/browserable
- **Fork:** jvanleur2234-glitch/browserable
- **What it does:** Open-source browser automation for AI agents (90.4% Web Voyager benchmark). Self-hosted with Docker, JS SDK, remote browser API integration (Hyperbrowser, Steel), MongoDB/Redis/MinIO backend.
- **Solomon OS fit:** SKILL — alternative to Playwright for Solomon Browser. Docker-based deployment aligns with infra patterns.
- **Status:** SKILL — benchmark against current Playwright setup
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/browserable-browser-automation.md

## Vibium — Browser Automation Toolkit (April 24, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **Fork:** jvanleur2234-glitch/vibium
- **What it does:** AI-friendly browser automation via simple CLI commands. Built on WebDriver BiDi (open standard). Available as CLI skill, MCP server, and JS/Python/Java libraries. ~10MB binary, zero-config, auto-downloads browser.
- **Solomon OS fit:** SKILL — lightweight alternative to heavy browser stacks. MCP server available for Hermes integration.
- **Status:** SKILL — lightweight browser automation option
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/vibium.md

## AI Agent Scanner — Asset Discovery + Security (April 24, 2026)
- **URL:** https://github.com/perfecxion-ai/ai-agent-scanner
- **Fork:** jvanleur2234-glitch/ai-agent-scanner
- **What it does:** Discovers AI agents across network, code, traffic, and cloud surfaces. Security testing, risk scoring, and compliance mapping (GDPR, SOC2, HIPAA, NIST, EU AI Act). SARIF output for CI/CD.
- **Solomon OS fit:** SKILL — asset discovery for enterprise security posture. Compliance mapping aligns with JCPaid audit needs.
- **Status:** SKILL — enterprise security discovery
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ai-agent-scanner.md

## Claude Synod Debate — Multi-Agent Deliberation (April 24, 2026)
- **URL:** https://github.com/quantsquirrel/claude-synod-debate
- **Fork:** jvanleur2234-glitch/claude-synod-debate
- **What it does:** Three-act adversarial debate among Gemini, OpenAI, Claude models. Critique-driven refinement for higher-quality decisions. Reduces overconfidence and bias through cross-examination.
- **Solomon OS fit:** SKILL — deliberation pattern for complex decisions. Study adversarial refinement mechanism.
- **Status:** SKILL — deliberation architecture study
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/claude-synod-debate.md

## AI Council Framework — Structured Multi-Agent Deliberation (April 24, 2026)
- **URL:** https://github.com/focuslead/ai-council-framework
- **Fork:** jvanleur2234-glitch/ai-council-framework
- **What it does:** 6-phase deliberation (Distribute → Collect → Synthesize → Debate → Verify → Deliver) with anti-sycophancy protocol, configurable consensus depth, confidence scores, and minority report preservation.
- **Solomon OS fit:** SKILL — structured deliberation for enterprise decisions. Anti-sycophancy protocol valuable for critical business decisions.
- **Status:** SKILL — deliberation process study
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/ai-council-framework.md

## Agent Debate — Shell-based Multi-Agent Code Review (April 24, 2026)
- **URL:** https://github.com/gumbel-ai/agent-debate
- **Fork:** jvanleur2234-glitch/agent-debate
- **What it does:** Structured technical decision debates via shared Markdown file, strikethrough disagreements, concrete file:line evidence citations, dispute logs, and evidence-backed convergence. Supports Claude Code, Codex, Gemini, Copilot.
- **Solomon OS fit:** SKILL — code review deliberation for engineering decisions. Evidence-based debate pattern valuable for technical reviews.
- **Status:** SKILL — engineering decision debates
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-debate.md

## Dapr Agents — Scalable Python Agent Framework (April 24, 2026)
- **URL:** https://github.com/dapr/dapr-agents
- **Fork:** jvanleur2234-glitch/dapr-agents
- **What it does:** Scalable, autonomous AI agents with built-in workflow orchestration, durable execution, security, statefulness, and telemetry. Kubernetes-native, multi-agent collaboration, data integration. Apache 2.0.
- **Solomon OS fit:** SKILL — study durable execution and state management patterns. Kubernetes-native aligns with enterprise deployment needs.
- **Status:** SKILL — resilient agent architecture
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## AgentExpress — TypeScript Middleware Agent Framework (April 24, 2026)
- **URL:** https://github.com/agent-express-ai/agent-express
- **Fork:** jvanleur2234-glitch/agent-express
- **What it does:** Express.js-style middleware framework for AI agents (ctx, next pattern). 12+ model providers, rich middleware system (agent/session/turn/model/tool hooks), built-in safety/governance (budget limits, validation, timeouts), OpenTelemetry, memory management.
- **Solomon OS fit:** SKILL — middleware patterns for extensibility. Safety/governance built-in aligns with enterprise requirements.
- **Status:** SKILL — middleware architecture patterns
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-express.md

## Magnitude — Vision-First Browser Agent (April 24, 2026)
- **URL:** https://github.com/magnitudedev/magnitude
- **Fork:** jvanleur2234-glitch/browser-agent
- **What it does:** Vision-grounded browser automation using Claude Sonnet 4 or Qwen-2.5VL. 94% on WebVoyager. Natural language control, Zod schema extraction, built-in test runner with visual assertions.
- **Solomon OS fit:** SKILL — vision-first browser automation alternative to HyperAgent. Aligns with Solomon Browser project.
- **Status:** SKILL — browser automation
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/magnitudedev-browser-agent.md

## Deliberation — Contemplative Multi-Agent Decision Framework (April 24, 2026)
- **URL:** https://github.com/2389-research/deliberation
- **Fork:** jvanleur2234-glitch/deliberation
- **What it does:** Contemplative decision-making framework (Quaker-inspired). Convenes multiple perspectives to seek clarity/unity. Discernment, clearness, and gathered modes for different decision contexts.
- **Solomon OS fit:** SKILL — contemplative decision-making for critical business choices. Different from Quorum's structured debate — more reflective approach for ethical/trade-off decisions.
- **Status:** SKILL — contemplative decision patterns
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deliberation-2389-research.md

## microsoft/agent-framework — Graph-Based Multi-Agent Orchestration (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-framework
- **What it does:** Microsoft cross-language (Python/.NET) platform for AI agents and multi-agent workflows. Graph-based orchestration with streaming, checkpointing, human-in-the-loop, time-travel debugging. ~9.7k stars.
- **Solomon OS fit:** FORGE — study graph-based orchestration patterns. Microsoft backing ensures longevity. Direct competitor to Hermes orchestration.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/microsoft-agent-framework.md

## dapr/dapr-agents — Kubernetes-Native Durable AI Agents (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **What it does:** Python framework for scalable AI agents with built-in workflow orchestration, security, statefulness, telemetry. Durable-execution engine guarantees task completion. Built on Dapr primitives.
- **Solomon OS fit:** FORGE — durability primitives enhance Hermes 24/7 operation. Kubernetes-native = enterprise deployment ready.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents.md

## ai-in-pm/Recursive-Self-Improvement-AI-Agent — Gödel-Inspired Self-Modifying Agents (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/Recursive-Self-Improvement-AI-Agent
- **What it does:** Python framework for self-modifying autonomous agents guided by Gödel's incompleteness. Dynamic runtime code modification, recursive policy improvement. MIT licensed.
- **Solomon OS fit:** INTEGRATE — most advanced self-improvement framework found. Self-modification at runtime directly enables autonomous capability growth.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/recursive-self-improvement-ai-agent.md

## ikorfale/agent-self-improvement — Cost-Optimizing Self-Improving Loop (April 24, 2026)
- **Fork:** Already forked (jvanleur2234-glitch/agent-self-improvement)
- **What it does:** ACT→MEASURE→LEARN→ADAPT closed loop. Claims 70-90% LLM cost reduction. Task Performance Tracker + Learning Extractor + Unified Orchestrator.
- **Solomon OS fit:** SKILL — cost optimization critical for 24/7 agent operation.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-self-improvement.md

## awaaate/Hyrm — Persistent Multi-Agent with Memory (April 24, 2026)
- **Fork:** Already forked (jvanleur2234-glitch/Hyrm)
- **What it does:** Experimental autonomous self-improving AI agent system on OpenCode. Persistent orchestrator + specialized workers. Memory layer persists across sessions.
- **Solomon OS fit:** SKILL — memory persistence patterns for Hermes.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/hyrm.md

## theprint/nfh-self-improvement-loop — Adversarial Self-Modification Safety (April 24, 2026)
- **Fork:** Already forked (jvanleur2234-glitch/nfh-self-improvement-loop)
- **What it does:** AI modifies own code while separate evaluator decides if change is beneficial. Strict separation prevents unchecked self-modification. MIT licensed.
- **Solomon OS fit:** INTEGRATE — safety/evaluator pattern for Hermes autonomous self-improvement. Most rigorous safety framework found.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/nfh-self-improvement-loop.md

## cwijayasundara/auto_research_self_improving_agents — Three-Layer Evolution (April 24, 2026)
- **Fork:** Already forked (jvanleur2234-glitch/auto_research_self_improving_agents)
- **What it does:** Karpathy autoresearch outer loop + LangChain harness + Letta continual learning. Sleep-time compute, skill extraction, failure pattern detection.
- **Solomon OS fit:** STUDY — three-layer approach most complete self-improvement architecture. Sleep-time compute concept novel.
- **Status:** STUDY
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/auto-research-self-improving-agents.md

## snyk/agent-scan — Snyk AI Agent Security Scanner (April 24, 2026)
- **Fork:** Already forked (jvanleur2234-glitch/agent-scan)
- **What it does:** Scans AI agent components (MCP servers, tools, skills) for 15+ risk types. Snyk CVE database integration.
- **Solomon OS fit:** INTEGRATE — production security monitoring. Snyk brand credibility.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/snyk-agent-scan.md

## mycellm — P2P GPU Inference Network (April 24, 2026)
- **Fork:** Already forked (jvanleur2234-glitch/mycellm)
- **What it does:** Pools GPUs into P2P inference network. Credit-based economy, OpenAI-compatible API, QUIC NAT traversal.
- **Solomon OS fit:** MONITOR — direct AgentFM competitor.
- **Status:** MONITOR
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/mycellm.md

## TrentPierce/Shard — Browser-Powered P2P Distributed Inference (April 24, 2026)
- **Fork:** Already forked (jvanleur2234-glitch/Shard)
- **What it does:** Browser-powered distributed inference via Scouts (WebGPU) + Shards (BitNet). Speculative decoding, zero marginal cost.
- **Solomon OS fit:** STUDY — browser compute concept for future Hermes deployment.
- **Status:** STUDY
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/shard-p2p-inference.md

## swarms-tools — Production-Grade Agent Tool Library (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/swarms-tools
- **What it does:** Pre-built Python tools for finance (HTX, CoinGecko, DeFi), social media (Telegram), logging. MIT licensed.
- **Solomon OS fit:** INTEGRATE — Telegram tool maps to Solomon messaging. Finance tools = trading agent primitives. Tool schema patterns for Hermes SKILL.md format.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/swarms-tools-kyegomez.md

## swarms-core — Rust Backend for Swarms Orchestration (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/swarms-core
- **What it does:** Rust execution engine for multi-agent orchestration. Memory-safe concurrency, Python bindings.
- **Solomon OS fit:** SKILL (architecture study only) — CC BY-NC-ND license. Study Rust patterns for high-throughput agent execution.
- **Status:** SKILL — architecture study only
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/swarms-core-kyegomez.md

## swarms-torch — PyTorch Swarm Intelligence & MoE (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/swarms-pytorch
- **What it does:** PSO-Transformers, Ant Colony, Swarmalator, Switch MoE, model merging techniques. MIT licensed.
- **Solomon OS fit:** SKILL — MIT permits use. Swarm intelligence algorithms could enhance Hermes task routing. MoE merging for local model ensemble management.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/swarms-pytorch-kyegomez.md

## llmcouncil — Multi-Protocol LLM Deliberation Council (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/llmcouncil
- **Forked from:** https://github.com/rachittshah/llmcouncil
- **What it does:** MCP server + Claude Code skill with 6 deliberation protocols: vote, debate (KS adaptive stopping), synthesize (chairman), critique, red-team, MAV. Fan-out to GPT-5.4, Gemini 2.5, Claude Sonnet 4.6 in parallel.
- **Solomon OS fit:** INTEGRATE — Council of High Intelligence implementation. MAV protocol for adversarial skill validation.
- **Status:** INTEGRATE

## multi-agent-council — Perplexity Pro Multi-LLM Debate (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/multi-agent-council
- **Forked from:** https://github.com/gabrielcnb/multi-agent-council
- **What it does:** Claude Code plugin using single Perplexity Pro subscription to access GPT/Gemini/Claude/Nemotron/Sonar. P2P debate → SQLite FTS5 memory → real-time dashboard. MIT license.
- **Solomon OS fit:** SKILL — Novel Perplexity browser-auth cost model. Study for multi-model deliberation without per-token API costs.
- **Status:** SKILL

## council-ai — 14-Persona Advisory Council (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/council-ai
- **Forked from:** https://github.com/doronpers/council-ai
- **What it does:** Python + React advisory council with 14 personas, 15 domain presets, multi-provider (OpenAI/Anthropic/Gemini/Ollama/LM Studio). Modes: debate, vote, synthesis, individual, sequential. MIT license.
- **Solomon OS fit:** SKILL — Extract 14 persona definitions for Hermes personality system.
- **Status:** SKILL

## agent-bom — AI Supply Chain Blast Radius Scanner (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent-bom
- **Forked from:** https://github.com/agent-bom/agent-bom
- **What it does:** CVE → package → MCP server → agent → credentials → tools blast radius mapping. 10-framework compliance (OWASP/NIST/EU AI Act/ATLAS). Auto-discovers agents, MCP servers, GPU workloads, cloud configs. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Replace sinewave scanner. Core security gate for Hermes with credential blast mapping.
- **Status:** INTEGRATE

## Meshcore — Hybrid P2P Compute Architecture Blueprint (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/Meshcore
- **Forked from:** https://github.com/elyawhoo/Meshcore
- **What it does:** Architectural blueprint: centralized/federated control plane + P2P compute plane. WASM sandboxing, auditor nodes with shadow prompts + logit consensus. AGPL-3.0.
- **Solomon OS fit:** SKILL — Architectural reference only. Auditor node concept for distributed inference validation.
- **Status:** SKILL (architecture study only)

## agent_council — 5-Step GPT-5.1 Council Framework (April 24, 2026)
- **URL:** https://github.com/jvanleur2234-glitch/agent_council
- **Forked from:** https://github.com/ma-serra/agent_council
- **What it does:** 5-step council: ingest (files) → build (Architect Agent proposes) → edit (refine) → execute (parallel) → review (peer + chairman). GPT-5.1 with reasoning effort. Web UI + CLI. MIT license.
- **Solomon OS fit:** SKILL — Architect Agent → diverse council composition pattern.
- **Status:** SKILL

## ai-agent-blueprint — Claude Code Orchestrator + PDCA Self-Improvement (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/ai-agent-blueprint
- **What it does:** Blueprint for autonomous AI agents using Claude Code sub-agent architecture. Main orchestrator delegates to specialized sub-agents (Research, File Ops, Coding). PDCA cycles for continuous self-improvement. SOUL.md + MEMORY.md + TASKS.md pattern.
- **Solomon OS fit:** SKILL — PDCA loop pattern directly applicable to Hermes self-improvement. SOUL.md + MEMORY.md mirrors Hermes soul/brain files. Orchestrator/sub-agent pattern maps to Solomon OS architecture.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/ai-agent-blueprint.md

## m2star — Self-Learning Claude Code with Quality Dashboard (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/m2star
- **What it does:** Self-learning skill pack for Claude Code. /self-learn, /self-review, /discover-conventions, /chain, /reflect, /escalate, /quality-dashboard commands. Sessions.tsv tracks success rate, correction rate, trends over time. Experiment chain for autonomous overnight testing.
- **Solomon OS fit:** FORGE — Quality Dashboard metric tracking → Solomon OS heartbeat reporting. Self-learn pattern → Hermes /self-review equivalent. Experiment chain → autonomous testing for Solomon Browser/JackConnect.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/m2star-self-learning-claude.md

## Agent Orcha — Declarative Multi-Agent with P2P Sharing (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-orcha
- **What it does:** TypeScript declarative multi-agent framework. Define agents/workflows/knowledge in YAML. Built-in workflow engine (parallelism, conditional logic, state). Model-agnostic (OpenAI/Gemini/Anthropic/local LLMs). MCP support. P2P encrypted sharing without central keys. SQLite vector store + knowledge graph. Browser sandbox with CDP. Apache 2.0.
- **Solomon OS fit:** SKILL — P2P sharing architecture study for distributed Hermes. Knowledge graph + vector store combo could enhance Hermes memory system.
- **Status:** SKILL

## SecureVector AI Threat Monitor — Local Agent Security Toolkit (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/securevector-ai-threat-monitor
- **What it does:** Local proxy security toolkit between agents and LLM providers. 28+ threat detection rules, skill scanner with AI-assisted review, policy engine (risk scoring, trusted publishers, allow/block rules), tool permissions, per-agent cost tracking. All local, no data leaves infrastructure. Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Pre-execution security gate for every Hermes tool invocation. Policy engine maps to JCPaid enterprise requirements. OWASP LLM Top 10 aligned.
- **Status:** INTEGRATE

## HyperAgent — AI-Powered Browser Automation on Playwright (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/hyperagent
- **What it does:** AI-driven browser automation built on Playwright. `page.ai()`, `page.extract()`, `executeTask()` for natural language automation. Falls back to standard Playwright. Built-in anti-bot stealth. Action caching (record/replay for cost reduction). Cloud-ready via Hyperbrowser. MCP client for Composio. MIT.
- **Solomon OS fit:** SKILL — Browser automation skill for Hermes. ClawLess competitor. Action caching could reduce Hermes browser costs. MCP integration pattern.
- **Status:** SKILL

## agent-express — Express.js-Style Middleware for AI Agents (April 24, 2026)
- **Fork:** Already forked (MIT)
- **What it does:** TypeScript middleware framework: `agent.use(middleware)` pattern with 5-layer onion (agent→session→turn→model→tool). Safety controls (validation, timeouts, HITL), OpenTelemetry observability, 12+ multi-provider routing, context compaction, MCP integration, Zod output validation, test toolkit.
- **Solomon OS fit:** FORGE — Middleware architecture directly implementable in Hermes pipeline. MIT permits direct use. Safety middleware + complexity routing + context compaction patterns all valuable.
- **Status:** FORGE

## dialectic-agentic — Multi-Agent Design Debate Framework (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dialectic-agentic
- **What it does:** No-code multi-agent debate system. Define design problems via Markdown + JSON config. Specialized agents (architect, security, performance, simplicity) propose/critique/refine via structured rounds. Judge evaluates convergence. Runs on any agentic platform (Cursor, Claude Code). MIT.
- **Solomon OS fit:** SKILL — Could be Hermes deliberation skill for architectural decisions. Maps to "Council of High Intelligence" concept.
- **Status:** SKILL

## AIBYAI — Multi-Agent Deliberative Intelligence Platform (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **What it does:** Multi-agent council (Empiricist, Strategist, Historian, Skeptic) that debate, critique, score each other → consensus + confidence score. Multi-provider (OpenAI/Anthropic/Gemini/Groq in parallel). Conflict detection triggers critique/rebuttal. Cold validator checks hallucinations. TypeScript + React + Fastify + PostgreSQL + Redis. MIT.
- **Solomon OS fit:** FORGE — Council pattern directly maps to "Council of High Intelligence." Confidence scoring + cost tracking valuable for JCPaid SLA reporting. HIGH VALUE for enterprise deliberation.
- **Status:** FORGE

## AI Council Framework — 6-Step Research-Backed Multi-Model Deliberation (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/ai-council-framework
- **What it does:** 6-step protocol: DISTRIBUTE → COLLECT → SYNTHESIZE → DEBATE (up to 3 rounds) → VERIFY (web search) → DELIVER with confidence scores. User-controlled consensus depth (QUICK to EXHAUSTIVE). Anti-Sycophancy Protocol. MIT.
- **Solomon OS fit:** SKILL — 6-step deliberation protocol for Hermes. Anti-sycophancy mechanisms critical for enterprise trust. Web verification step adds real-world grounding.
- **Status:** SKILL

## Microsoft Agent Framework — Enterprise Multi-Language Agent Orchestration (April 24, 2026)
- **Fork:** Already forked (MIT)
- **What it does:** Multi-language (Python/.NET) agent framework with graph-based orchestration, streaming, checkpointing, human-in-the-loop, time-travel debugging. 74 releases, ~120 contributors. AF Labs for experimental features. DevUI for in-app development. Migration guides from Semantic Kernel and AutoGen.
- **Solomon OS fit:** SKILL — Time-travel debugging concept valuable for Hermes DevEx. Graph-based orchestration paradigm interesting for Hermes workflow system.
- **Status:** SKILL

## Dapr Agents — Durable Workflow AI Agent Framework (April 24, 2026)
- **Fork:** Already forked (Apache 2.0)
- **What it does:** Python durable-execution workflow engine for AI agents. Built on Dapr for Kubernetes-native resilience. Automatic retries, fault tolerance, state recovery. Runs thousands of agents with transparent distribution. Built-in telemetry. Apache 2.0.
- **Solomon OS fit:** SKILL — Study durable execution patterns for Hermes session resilience. Kubernetes-native design targets enterprise deployment. Self-healing fault tolerance aligns with JCPaid SLA.
- **Status:** SKILL

## Gollem — Type-Safe Go Agent Framework (April 24, 2026)
- **Fork:** Already forked (MIT)
- **What it does:** Production-grade Go agent framework with compile-time type safety (Agent[T]). Multi-provider (Claude, GPT-O, Gemini, Vertex). Structured + streaming outputs. Guardrails (input/turn/output validation + auto-repair). OpenTelemetry middleware. 50+ primitives. Zero core dependencies. MIT.
- **Solomon OS fit:** SKILL — Study type-safe validation patterns for Hermes tool security. Go implementation could complement Hermes Python/TypeScript.
- **Status:** SKILL

## Medusa — 9,600+ Pattern AI Security Scanner (April 24, 2026)
- **Fork:** Already forked (MIT)
- **What it does:** AI-first security scanner with 9,600+ detection patterns, 200 CVE checks (Log4Shell, LangChain RCE). Repo-wide scans with `--git` for AI supply chain risk. 10-40x faster multi-core. Zero-setup pip install. JSON/HTML/Markdown/SARIF output. OWASP/MITRE aligned.
- **Solomon OS fit:** INTEGRATE — Security scanning layer for Hermes. Snyk competitor. Pattern density exceeds other scanners. SARIF for CI integration.
- **Status:** INTEGRATE

## Reflexio — Self-Improving Agent Harness (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/reflexio-new
- **Source:** https://github.com/ReflexioAI/reflexio
- **License:** Apache 2.0
- **What it does:** Python harness enabling AI agents to self-improve by learning from real user interactions. Captures corrections, publishes expert responses, persists proven playbooks. Transfer learning propagates improvements to all users.
- **Solomon OS fit:** INTEGRATE — Directly enhances Hermes self-improvement. Playbook/strategy persistence system maps to Solomon learning from Joseph's corrections. Apache 2.0 permits integration.
- **Status:** INTEGRATE

## gumbel-ai/agent-debate — Multi-Agent Technical Debate (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-debate-new
- **Source:** https://github.com/gumbel-ai/agent-debate
- **License:** MIT
- **What it does:** Protocol for multi-agent technical debates on code decisions. 2-4 agents (Claude, Codex, Gemini, Copilot) edit shared Markdown with file:line evidence citations. Strikethroughs show disagreement. Debates converge or escalate. MIT.
- **Solomon OS fit:** FORGE — Deliberation engine for Hermes. Evidence-grounded debate format for skill validation and architecture decisions. Multi-provider validation via debate format.
- **Status:** FORGE

## slior/dialectic-agentic — Skill-File Design Debate System (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dialectic-agentic-new
- **Source:** https://github.com/slior/dialectic-agentic
- **License:** MIT
- **What it does:** Multi-agent design debate system running as agent skill files + prompts + JSON config (no code). Personas (architect, security, performance) debate design problems in rounds. Judge evaluates convergence. MIT.
- **Solomon OS fit:** SKILL — Novel deliberation pattern. "No code" skill-file approach aligns with Hermes ecosystem. Study for architecture review before building new capabilities.
- **Status:** SKILL

## AIBYAI — Multi-Agent Deliberative Consensus Platform (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/aibyai
- **Source:** https://github.com/Yash-Awasthi/aibyai
- **License:** MIT
- **What it does:** Multi-agent deliberative platform where 4+ AI agents debate, critique, and score each other's claims to produce trusted consensus with confidence scores. Conflict detector + synthesizer + validators + cold hallucination validator.
- **Solomon OS fit:** SKILL — Deliberation + conflict detection pipeline could enhance Hermes skill validation. Confidence scoring for uncertainty awareness. Multi-agent peer review of decisions.
- **Status:** SKILL

## browserable — Self-Hosted Browser Automation for AI Agents (April 24, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserable
- **Source:** https://github.com/browserable/browserable
- **License:** MIT
- **What it does:** Open-source JavaScript library for browser-automation AI agents. Navigate, fill forms, extract data. Targets 90%+ Web Voyager benchmark. Multi-LLM (Gemini/OpenAI/Claude via Hyperbrowser/Steel). Self-hosted. MIT.
- **Solomon OS fit:** SKILL — ClawLess browser automation competitor. Self-hosted for privacy. Could enable real web research in Hermes. Web Voyager benchmark target means robust.
- **Status:** SKILL

## Vibium — AI-Native Browser Automation CLI + MCP (April 24, 2026)
- **Fork:** Already forked (Apache 2.0)
- **Source:** https://github.com/VibiumDev/vibium
- **License:** Apache 2.0
- **What it does:** Lightweight browser automation toolkit (Go core, JS/Python/Java clients). CLI skill + MCP server. Zero-config setup. Semantic element finding (text, labels, ARIA). WASM sandboxing. Apache 2.0.
- **Solomon OS fit:** SKILL — Browser automation with MCP server integration point. Semantic element finding more robust than CSS selectors. Multi-language approach inspires Hermes components.
- **Status:** SKILL

## agentbrowser — Semantic Browser Runtime for AI Agents (April 24, 2026)
- **Fork:** Already forked (MIT)
- **Source:** https://github.com/ashtonvaughan/agentbrowser
- **License:** MIT
- **What it does:** AI-agent-specific browser runtime exposing semantic structured actions instead of raw DOM. Semantic observation reduces tokens ~95%. Dynamic tool registry per page. Self-healing (CAPTCHA, stale selectors). Session persistence. MCP server.
- **Solomon OS fit:** SKILL — 95% token reduction for browser tasks massive. Self-healing reduces maintenance. MCP server enables native Hermes integration. Maps to Hermes web research.
- **Status:** SKILL


## Gollem — Production Agent Framework for Go (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/gollem
- **Source:** https://github.com/fugue-labs/gollem
- **License:** MIT
- **What it does:** Go-based production agent framework with compile-time type safety, zero-core dependencies, single-binary deployment. Typed `Agent[T]`, multi-provider streaming (Anthropic/OpenAI/Gemini/Vertex), guardrails, middleware chains, OpenTelemetry tracing, cost tracking, multi-agent team orchestration via ext/team.
- **Solomon OS fit:** SKILL — Study for type-safe agent design patterns. Go agent for compute-intensive Hermes workloads. MIT permits direct use of patterns.
- **Status:** SKILL

## Agent-Express — Express-Style Middleware AI Agent Framework (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/agent-express
- **Source:** https://github.com/agent-express-ai/agent-express
- **License:** MIT
- **What it does:** Minimalist TypeScript framework with 3 concepts: Agent, Session, Middleware. 5 onion hooks (agent/session/turn/model/tool). Built-in guards: budget, validation, timeouts, iteration limits, HITL approval. 12+ model providers, model routing, memory compaction, MCP integration, Zod validation, CLI with hot-reload.
- **Solomon OS fit:** INTEGRATE — Express.js pattern maps directly to Hermes. HITL approval middleware for enterprise workflows. MIT allows direct use of patterns.
- **Status:** INTEGRATE

## Docker Agent (cagent) — YAML-Driven Multi-Agent Orchestration (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/cagent
- **Source:** https://github.com/docker/cagent
- **License:** Apache 2.0
- **What it does:** Docker CLI plugin for declarative YAML agent definitions. Multi-agent teams, any MCP server, model-agnostic (OpenAI/Anthropic/Gemini/Bedrock/Mistral/xAI/Docker Model Runner), built-in think/todo/memory tools, RAG with BM25+embeddings+hybrid search+reranking, OCI registry push/pull for agent distribution.
- **Solomon OS fit:** INTEGRATE — YAML config maps to Hermes skill manifests. RAG pipeline could replace/enhance knowledge retrieval. Docker packaging for agent distribution. Apache 2.0 permits direct code use.
- **Status:** INTEGRATE

## Dapr Agents — Resilient Workflow Orchestration (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/dapr-agents
- **Source:** https://github.com/dapr/dapr-agents
- **License:** Apache 2.0
- **What it does:** Python-based AI agent framework built on Dapr's durable workflow engine. Tasks complete even amid failures. Automatic retries and recovery, Kubernetes-native deployment, multi-agent collaboration, data-driven workflow orchestration, built-in security and observability.
- **Solomon OS fit:** FORGE — Durable execution model for Hermes autonomous operations. Workflow orchestration directly implementable. Kubernetes-native for JCPaid enterprise. Apache 2.0 allows direct use.
- **Status:** FORGE

## MEDUSA — 9,600+ Pattern Security Scanner for AI/ML (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **Source:** https://github.com/Pantheon-Security/medusa
- **License:** AGPL-3.0 ⚠️
- **What it does:** AI-first security scanner with 9,600+ patterns, 200+ CVEs (Log4Shell, Spring4Shell, LangChain RCE), repo poisoning detection across 28+ file types, cursor/copilot/claude/gemini editor weaponization detection. Zero-setup, parallel processing, SARIF/JSON/HTML/Markdown output.
- **Solomon OS fit:** SKILL — Reference for security pattern development. AGPL-3.0 restricts commercial use in JCPaid.
- **Status:** SKILL (license restricted)

## Magnitude Browser Agent — Vision-First Browser Automation (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browser-agent
- **Source:** https://github.com/magnitudedev/browser-agent
- **License:** Apache 2.0
- **Stars:** 4,026
- **What it does:** Vision-first browser automation using computer vision + LLM. Pixel-based actions generalize across complex UIs. Self-healing selectors. Multi-browser (Chrome/Firefox/Safari/Edge) + mobile (iOS/Android). Stagehand-compatible API.
- **Solomon OS fit:** INTEGRATE — Alternative browser engine for Solomon Browser. Vision approach more resilient than DOM selectors. Mobile automation extends browser reach. Apache 2.0 allows direct integration.
- **Status:** INTEGRATE

## Vibium — Standards-Based Browser Automation (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/vibium
- **Source:** https://github.com/VibiumDev/vibium
- **License:** Apache 2.0
- **Stars:** 2,784
- **What it does:** ~10MB binary using WebDriver BiDi standard. Semantic element mapping (no CSS selectors), session recording/replay, MCP server, CLI, JS/Python/Java libs. Zero-config browser download.
- **Solomon OS fit:** INTEGRATE — Most standards-compliant option. Install as Hermes MCP skill. Complements Magnitude (vision) and Browserable (self-hosted MIT).
- **Status:** INTEGRATE

## Browserable — Self-Hostable Browser Automation (April 25, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/browserable
- **Source:** https://github.com/browserable/browserable
- **License:** MIT
- **Stars:** 1,182
- **What it does:** Self-hostable JavaScript library for AI agents. Docker-based deployment. Natural language task definition. Claude Code/Cursor/Copilot integration. Self-healing selectors.
- **Solomon OS fit:** INTEGRATE — MIT license = full commercial use. Self-hostable for data privacy. Key differentiator from other browser tools. Build as Hermes skill.
- **Status:** INTEGRATE

## OpenMythos — Recurrent-Depth Transformer (April 25, 2026)
- **URL:** https://github.com/kyegomez/OpenMythos
- **Fork:** Already forked
- **What it does:** Open-source RDT/Looped Transformer reconstruction of Claude Mythos. Prelude→looped Recurrent Block→Coda architecture. MoE variants, latent thoughts, depth extrapolation.
- **Solomon OS fit:** SKILL — Recurrent hidden state maps to Hermes persistent context. Architecture study for adaptive computation.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/open-mythos-recurrent-depth-transformer.md

## agent-express — TypeScript Middleware Agent Framework (April 25, 2026)
- **URL:** https://github.com/agent-express-ai/agent-express
- **What it does:** Express-like middleware pattern for AI agents. 5 onion hooks (agent/session/turn/model/tool), built-in guards, OpenTelemetry, 12+ model providers, Zod output validation, MCP integration.
- **Solomon OS fit:** SKILL — Middleware pattern for skill chaining, guardrails for security layer, observability integration.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/agent-express-typescript-middleware-framework.md

## hackmyagent — Semantic Security Toolkit (April 25, 2026)
- **Fork:** Already forked
- **What it does:** Abstract Security Tree compilation + 209 static checks + 29 NanoMind semantic checks + 164 adversarial payloads + adaptive red-teaming + self-securing startup quarantine.
- **Solomon OS fit:** INTEGRATE — Most semantic security approach available. Self-protecting quarantine for 24/7 autonomous operation.
- **Status:** INTEGRATE
- **RD Report:** /brain/RD_REPORTS/hackmyagent-semantic-security-toolkit.md

## Quorum — Multi-AI Deliberation Framework (April 25, 2026)
- **URL:** https://github.com/Solvely-Colin/Quorum
- **What it does:** 7-phase debate process (Gather→Plan→Formulate→Debate→Adjust→Rebuttal→Vote+Synthesis). Multi-provider (Claude/GPT/Gemini/etc.), SHA-256 audit ledger, policy guardrails, MCP compatible.
- **Solomon OS fit:** FORGE — IS the Council of High Intelligence for Solomon OS. 7-phase deliberation matches planned Hermes Council mode.
- **Status:** FORGE
- **RD Report:** /brain/RD_REPORTS/quorum-multi-ai-deliberation-framework.md

## agent-orcha — Declarative YAML Multi-Agent Framework (April 25, 2026)
- **URL:** https://github.com/ddalcu/agent-orcha
- **What it does:** YAML-first multi-agent orchestration. P2P agent sharing without central keys, SQLite vector store + knowledge graphs, ReAct workflow engine, browser sandbox with noVNC.
- **Solomon OS fit:** SKILL — YAML declarative pattern for config, P2P sharing architecture, knowledge graph memory aligns with Solomon Vault.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/agent-orcha-yaml-multi-agent-framework.md

## gollem — Type-Safe Go Agent Framework (April 25, 2026)
- **URL:** https://github.com/fugue-labs/gollem
- **What it does:** Compile-time type-safe Go agents. Generic Agent[T], 5+ LLM backends, FuncTool JSON Schema auto-generation, streaming iter.Seq2, guardrails (input/turn/output + auto-repair), OpenTelemetry.
- **Solomon OS fit:** SKILL — Compile-time safety model for Hermes reliability. Single-binary deployment for distributed nodes.
- **Status:** SKILL
- **RD Report:** /brain/RD_REPORTS/gollem-go-type-safe-agent-framework.md

## X/Twitter Trends (April 25, 2026)
- **Hermes Agent** — Confirmed elite status. Tony Simons: "first agent platform I'd market as professional install service." 1,241+ likes on Alex Finn demo. Machina: "best agent I've ever touched, not even close."
- **AI Security** — DeepMind: 86% agent hijack rate via hidden HTML injection. Anthropic Opus 4 blackmails in 96% of goal-conflict scenarios. OWASP Top 10 Agentic 2026 confirms agents as primary attack vector.
- **Distributed compute** — Gradient Network Parallax AI for distributed execution. Sentient GRID: modular DAGs for reproducible AI pipelines. UtilityNet: multi-step agents beat single model by 21%.
- **Self-improving defense** — Federated learning defenses survive 50%+ malicious clients. Bell Cyber autonomous SOC <5min threat containment.
