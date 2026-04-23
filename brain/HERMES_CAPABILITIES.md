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

## Gollem — Go Agent Framework with Compile-Time Type Safety (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/gollem
- **What it does:** Go agent framework. Compile-time validation for output schemas, tool parameters, guardrails, event subscriptions. Zero-core dependencies. Multi-provider (Anthropic, OpenAI, Gemini/Vertex). FuncTool[P] with JSON Schema from typed Go functions. OpenTelemetry tracing, time-travel debugging. MIT licensed v0.3.1.
- **Solomon OS fit:** SKILL — Compile-time type safety is the right direction for Hermes 2.0. Type-safe tool schema generation eliminates runtime errors. MIT license for architecture study.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/gollem.md

## Claude Synod Debate — 3-Act Adversarial Multi-Provider Debate (April 22, 2026)
- **What it does:** 3-act framework: Gemini proposes Solution A, OpenAI proposes B → cross-critique → Claude synthesizes verdict. Heterogeneous ensemble reduces single-model bias. MIT license.
- **Solomon OS fit:** SKILL — Lightweight 3-act pattern for Hermes deliberation skill. Cross-provider debate prevents echo chamber. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/claude-synod-debate.md

## 2389 Deliberation — Contemplative Decision-Making Skills (April 22, 2026)
- **What it does:** Skills suite: `discernment` (internal voices), `clearness` (multi-agent committee), `gathered` (user-participatory). Inspired by Quaker business practice. Principles: sense of the meeting, speaking once, intentional silence, standing aside. TDD-developed. MIT license.
- **Solomon OS fit:** SKILL — Skills-based approach maps directly to Hermes. `clearness` = multi-agent committee we want. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/2389-deliberation.md

## Deliberate — Shell-Based Async Agent Deliberation (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/deliberate
- **What it does:** Experimental Bash+jq protocol for two AI agents to deliberate asynchronously via shared filesystem JSONL logs. `/tmp/deliberation/room-*/.jsonl`. Minimal, zero-dependency. MIT license.
- **Solomon OS fit:** SKILL — File-based IPC for Hermes sub-agent deliberation. Minimal viable multi-agent communication primitive. MIT license.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/deliberate-shell.md
## Aegis — EDR for AI Agent Monitoring (April 22, 2026)
- **Fork:** https://github.com/jvanleur2234-glitch/Aegis
- **What it does:** Local EDR for AI agents. Process monitoring (107 signatures), file protection, network monitoring, 4-axis behavioral anomaly scoring, trust grades A+-F. No cloud telemetry.
- **Solomon OS fit:** INTEGRATE — Security monitoring layer for Hermes agents. Trust grades for permission tier system.
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/aegis-edr-ai-agents.md

## gollem — Go Type-Safe Agent Framework (April 22, 2026)
- **Fork:** Already forked (`gollem`)
- **What it does:** Compile-time type-safe Go agent framework. Generic Agent[T], 5+ LLM backends, FuncTool JSON Schema gen, streaming iterators, guardrails, OpenTelemetry.
- **Solomon OS fit:** SKILL — Middleware/guardrail patterns for Hermes security layer.
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/gollem.md

## 2389-deliberation — Contemplative Multi-Agent Skills (April 22, 2026)
- **Fork:** Already forked (`deliberation`)
- **What it does:** Claude-based skills: discernment (internal voices), clearness (committee), gathered (participatory). MIT licensed.
- **Solomon OS fit:** SKILL — Skills-based deliberation for Hermes decisions. MIT license.
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/2389-deliberation.md

## dialectic-agentic — Multi-Agent Design Debate (April 22, 2026)
- **Fork:** Already forked (`dialectic-agentic`)
- **What it does:** No-code design debate framework. Expert roles → proposals → critiques → synthesis. MIT.
- **Solomon OS fit:** SKILL — Structured design review for Hermes skill validation.
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dialectic-agentic.md

## Docker Agent (cagent) — Declarative Multi-Agent Runtime (April 23, 2026)
- **URL:** https://github.com/docker/cagent
- **Fork:** https://github.com/jvanleur2234-glitch/cagent
- **What it does:** Docker CLI plugin for declarative YAML-based AI agents. Multi-AI provider support (OpenAI, Anthropic, Gemini, AWS Bedrock, Mistral, xAI, Docker Model Runner). Built-in tools + MCP, RAG with BM25/embeddings/hybrid search/reranking. OCI registry push/pull for agent distribution.
- **Solomon OS fit:** INTEGRATE — Docker-based container runtime could be Hermes skill execution layer. YAML agent config maps to skill manifests. RAG pipeline for Solomon knowledge base. Registry distribution for skill packages. Apache 2.0.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/docker-agent-cagent.md

## MEDUSA — AI Security Scanner (9,600+ Patterns) (April 23, 2026)
- **URL:** https://github.com/Pantheon-Security/medusa
- **Fork:** https://github.com/jvanleur2234-glitch/medusa
- **What it does:** AI-first security scanner with 9,600+ detection patterns, 200 CVE detections (Log4Shell, Spring4Shell, LangChain RCE). `medusa scan --git` for repo scanning. Multi-core parallel + smart caching. JSON/HTML/Markdown/SARIF output. IDE integrations (Claude Code, Cursor, VS Code, Gemini CLI). Apache 2.0.
- **Solomon OS fit:** INTEGRATE — Security pre-flight for every Hermes skill/tool. 9,600 patterns >> current coverage. SOC2/GDPR compliance evidence. Apache 2.0.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/medusa-ai-security-scanner.md

## Agent Debate — Shell-Based Multi-Agent Technical Deliberation (April 23, 2026)
- **URL:** https://github.com/gumbel-ai/agent-debate
- **Fork:** Already forked (`agent-debate`)
- **What it does:** Structured technical debate protocol via shared Markdown file editing. Evidence-based with line-referenced citations. Supports Claude Code, Codex, Gemini CLI, Copilot CLI. Auto mode with optional Plan phase. Guardrails via agent-guardrails.md. MIT.
- **Solomon OS fit:** SKILL — Evidence-based deliberation for Hermes skill validation. Shell-based = zero dependency. Could power "Council of High Intelligence" deliberation layer.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-debate-shell-deliberation.md

## Council — Multi-Agent Persona-Based Discussion (April 23, 2026)
- **URL:** https://github.com/dubs3c/council
- **Fork:** Already forked (`council`)
- **What it does:** Multi-agent discussion with distinct personas (Architect, Critic, AppSec Specialist) debate to reach consensus. ProposalPhase → DebatePhase → Moderator synthesis → Final Report with full transcript. Python, MIT.
- **Solomon OS fit:** SKILL — Persona-based deliberation for Hermes skill review. Architect/Critic/Security personas map to Hermes multi-agent validation. Markdown transcript = audit trail.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/council-multi-persona-deliberation.md

## Vibium — AI-Native Browser Automation CLI (April 23, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** Lightweight ~10MB binary, auto Chrome download, zero config. Built on WebDriver BiDi. CLI: go, map, find, click, text, screenshot, pdf, eval, wait, record, fill, select, check, press. MCP server + JS/Python/Java client libs. Apache 2.0.
- **Solomon OS fit:** SKILL — Browser automation primitive for Solomon Browser. Standards-based = cross-browser. Auto Chrome download = zero friction. Apache 2.0.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/vibium-browser-automation.md

## Shard — Browser-Powered P2P Distributed Inference (April 23, 2026)
- **URL:** https://github.com/TrentPierce/Shard
- **Fork:** Already forked (`Shard`)
- **What it does:** Browser-powered P2P inference. Scouts (WebGPU) generate drafts, Shards (BitNet 1.58-bit) verify. Proof-of-Compute credits. OpenAI-compatible API. libp2p mesh. MIT.
- **Solomon OS fit:** SKILL — Architecture study for Solomon Air distributed compute. Browser/WebGPU as compute node is novel. POC credit system for agent economy.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/shard-browser-p2p-inference.md

## Swarms AutoHedge — Swarm Intelligence Market Analysis (April 23, 2026)
- **URL:** https://github.com/The-Swarm-Corporation/AutoHedge
- **Fork:** Already forked (`AutoHedge`)
- **What it does:** Automates market analysis, risk management, and trade execution using swarm intelligence and AI agents for autonomous hedging. 1,148 stars. Python MIT.
- **Solomon OS fit:** SKILL — Swarm orchestration pattern for Hermes multi-agent workflows. Market analysis use case for Solomon OS business intelligence layer.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/AutoHedge.md