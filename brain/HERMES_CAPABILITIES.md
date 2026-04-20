# HERMES CAPABILITIES — Updated 2026-04-20

## Skill Frameworks
- ** NousResearch/hermes-agent** — Core agent framework ( NousResearch/hermes-agent) — Full AI agent with skills ecosystem, MCP support, multi-platform gateway
- ** NousResearch/hermes-agent/optional-skills** — 70+ bundled and optional skills across 15+ categories via Skills Hub
- ** NousResearch/hermes-agent/skills/mcp** — MCP tool integration for multi-channel processing
- ** cloudwalk/hermes-mcp** — Elixir SDK implementing Model Context Protocol (MCP)
- ** slab/hermes-mcp** — Fork of cloudwalk/hermes-mcp, MIT-licensed Elixir MCP SDK
- ** NousResearch/hermes-agent (FastMCP)** — FastMCP skill for rapid MCP server development

## Agent Orchestration
- ** microsoft/agent-framework** — Multi-language (Python/.NET) graph-based agent orchestration with DevUI, 9k+ stars
- ** dapr/dapr-agents** — Apache 2.0, production-grade agent orchestration on Dapr with durable execution
- ** henomis/phero** — Apache 2.0, Go-based multi-agent framework with RAG, MCP, streaming, observability
- ** alphora-ai/alphora** — Full-stack Python agent framework with sandboxing, typed streaming, skills ecosystem
- ** solace-labs/solace-agent-mesh** — Event-driven multi-agent mesh via Solace Event Mesh, Apache 2.0
- **fugue-labs/gollem** — Apache 2.0, Go-first type-safe agent framework with compile-time guarantees, multi-provider streaming, guardrails, OpenTelemetry observability

## Browser Automation (ClawLess Competitors)
- ** vercel-labs/agent-browser** — MIT, native Rust CLI for AI agent browser automation
- ** browser-use/browser-use** — MIT, Python Playwright-based AI browser agent framework
- ** hyperbrowserai/HyperAgent** — TypeScript AI-enhanced browser automation with stealth mode
- ** mozilla/pilo** — TypeScript natural language browser control via Playwright
- ** browserable/browserable** — MIT, JS/TS self-hosted browser automation library for AI agents
- ** ashtonvaughan/agentbrowser** — TypeScript semantic browser runtime for AI agents (self-healing, site memory)
- ** vibiumdev/vibium** — AI-friendly browser automation via WebDriver BiDi, CLI+MCP+lib
- ** copilotbrowser/copilotbrowser** — Apache 2.0, cross-browser (Chromium/Firefox/WebKit) with MCP + "Follow Me" mode
- ** trentpierce/koda** — Non-commercial AI browser automation with CV-driven element understanding

## AI Security Scanners (Snyk Competitors)
- ** sinewaveai/agent-security-scanner-mcp** — MCP security server: prompt injection firewall, package hallucination detection (4.3M+), 1000+ vuln rules with AST/taint analysis
- ** snyk/agent-scan** — Apache 2.0, Snyk's agent ecosystem scanner (MCP servers + agent skills), 15+ risk categories
- ** pantheon-security/medusa** — 9,600+ AI security patterns, 200 CVE detections, GitHub repo scan via `medusa scan --git`
- ** koatora20/guard-scanner** — MIT, 364 patterns, 35 threat categories, OWASP Agentic Top 10 compliance
- ** agentverus/agentverus-scanner** — MIT, TypeScript trust/safety scanner for agent skills (prompt injection, exfil, 10+ threat categories)
- ** firmislabs/firmis-scanner** — Apache 2.0, multi-platform agent security scanner (269 rules, 26 threat categories, BOM generation, compliance mapping)
- ** vigile-ai/vigile-scan** — Apache 2.0, MCP server + agent skill scanner with trust scores (59 rules), Sentinel runtime monitoring
- ** agentseal/agentseal** — FSL-Apache 2.0, 225+ tests, 28 agents, 6-stage detection pipeline (pattern→deobfuscation→semantic→baseline→registry→YAML)
- ** raxe-ai/raxe-ce** — 515+ L1 rules + on-device ML ensemble, 94.7% TP rate, runtime prompt injection protection
- ** opena2a-org/hackmyagent** — 209 static checks + 29 semantic checks + NanoMind semantic compiler, Abstract Security Tree, self-securing binary
- ** sammwyy/agentlib** — MIT, TypeScript agent framework with fluent API, pluggable reasoning engines, token budgeting, session isolation

## Distributed AI Compute (AgentFM Competitors)
- ** agent-fm/agentfm-core** — MIT, Go P2P framework for distributed AI compute via Podman containers, libp2p mesh
- ** hyperspaceai/agi** — P2P distributed AGI system, collaborative training via DiLoCo, 195x compression, blockchain
- ** hyperspaceai/hyperspace-node** — CLI/Tray/browser P2P AI inference via libp2p, 2M+ nodes
- ** mycellm/mycellm** — Apache 2.0, P2P GPU pooling with OpenAI-compatible API, Ed25519 credits
- ** antonellof/peerclaw** — MIT, single Rust binary P2P AI network with BitTorrent-style sharing + token economy
- ** nikegunn/tutu** — MIT, Go distributed computing platform for LLMs, P2P network, TuTufile packaging
- ** spmfrance-cloud/aria-protocol** — MIT, 1-bit inference P2P framework with blockchain provenance + consent contracts
- ** trentpierce/shard** — Browser/WebGPU distributed inference via libp2p mesh, Scout+Verifier architecture

## Self-Improving Agents
- ** maximerobeyns/self_improving_coding_agent** — MIT, Docker-isolated coding agent that iteratively improves its own codebase via benchmark loop
- ** xmaks82/self-improving-agent** — MIT, 16-agent system with permanent prompt evolution loop, 6 free LLM providers
- ** grail-computer/self-improving-agent** — OpenClaw skill, capability map + curriculum → goal-driven capability evolution
- ** unconst/ninja** — Fully automated self-improving coding agent: Arbos orchestrator runs 30+ sessions, patches own code
- ** ramsbaby/openclaw-self-evolving** — Weekly log-based self-evolution with human approval for AGENTS.md diffs
- ** ikorfale/agent-self-improvement** — MIT, 70-90% LLM cost reduction via ACT→MEASURE→LEARN→ADAPT loop with SQLite tracking
- ** rangeking/self-evolving-agent** — OpenClaw skill, curriculum/evaluation/transfer/promotion lifecycle

## Multi-Agent Deliberation (Council of High Intelligence Competitors)
- ** slior/dialectic-agentic** — Agent-native multi-agent design debate system with converge/judge architecture
- ** bayramannakov/agent-tower-plugin** — Python deliberation plugin for Claude Code: council/debate/deliberate modes
- ** solvely-colin/quorum** — TypeScript 7-phase multi-AI deliberation across 8+ providers with SHA-256 ledger + minority report
- ** dubs3c/council** — MIT, multi-persona AI discussion (Architect/Critic/Security Specialist) → consensus report
- ** agentscope-ai/agentscope** — Multi-agent debate with moderator-based convergence (EMNLP 2024 style)
- ** matiasdaloia/concilium** — MIT, CLI/Electron multi-LLM deliberation: parallel execution → blind peer review → synthesis
- ** kyleparrot/deliberate** — MIT, experimental bash+JSONL multi-agent deliberation protocol for local machines
- ** dnhess/spectra** — MIT, multi-agent deliberation framework for Claude Code with blackboard architecture
- **bassrehab/artemis-agents** — Apache 2.0, structured N-agent debate framework with H-L-DAG argumentation, causal reasoning, jury scoring, sandbagging detection, MCP server mode

## Skill Index / ASM
- ** skill-framework/skill-index-updater** — ASM skill index management for GitHub skill repos
- ** awesome-hermes-agent** — Community-curated list of Hermes Agent skills, tools, and integrations

## MoE / Recurrent Transformer
- ** thu-ml/re moe** — Differentiable ReLU-based MoE routing on Megatron-LM, dynamic expert allocation
- ** meditsolutionskurman/medit-one** — Transformer + recurrent state + MoE for memory-efficient single-token generation
- ** lucidrains/st-moe-pytorch** — Sparse Transformer MoE with top-n gating, z-loss, hierarchical routing
- ** devanik21/hag-moe** — Hierarchical Attention-Gated MoE, dynamic expert count per token entropy
- ** raymin0223/mixture_of_recursions** — Mixture-of-Recursions: adaptive per-token recursion depth (NeurIPS 2025)

---
*Last updated: 2026-04-20 16:30 UTC — AIQ Scout Hourly Session*
## microsoft/agent-framework — Graph-Based Agent Orchestration (April 20, 2026)
- **Repo:** microsoft/agent-framework — MIT (~9k stars)
- **What it does:** Cross-language (Python/.NET) agent framework with graph-based workflows, streaming, checkpointing, human-in-the-loop, time-travel debugging.
- **For Solomon OS:** Graph orchestration model → Hermes architecture study. DevUI for dev experience inspiration. Multi-language → cross-platform runtime.
- **Status:** Forked (already existed) ✅

## dapr/dapr-agents — Production-Grade Resilient Agents (April 20, 2026)
- **Repo:** dapr/dapr-agents — Apache 2.0
- **What it does:** Built on Dapr runtime. Durable workflow execution, scale-to-zero (thousands on one core), 50+ data source integrations, Kubernetes-native.
- **For Solomon OS:** Durability + resilience core requirement. Scale-to-zero for cost efficiency. Data integrations for Hermes knowledge layer.
- **Status:** Forked (already existed) ✅

## hackmyagent — NanoMind Semantic Security Compiler (April 20, 2026)
- **Repo:** opena2a-org/hackmyagent — Apache 2.0
- **What it does:** Security scanner + red team toolkit. 209 checks + 29 semantic checks. Abstract Security Tree instead of regex. Self-securing binary. 164 adversarial payloads.
- **For Solomon Guardian:** Best-in-class semantic analysis. Catches undeclared capabilities, scope mismatches, evasion attempts. Self-securing scanner.
- **Status:** Forked (already existed) ✅

## agent-security-scanner-mcp — ProofLayer Security Scanner (April 20, 2026)
- **Repo:** sinewaveai/agent-security-scanner-mcp — MIT (97.7% precision)
- **What it does:** Security MCP server. AST + taint analysis, 1700+ rules, 4.3M package hallucination detection, auto-fix, 11 MCP tools.
- **For Solomon Guardian:** Snyk competitor with superior precision. MCP-native security gate for agent deployments.
- **Status:** Forked (already existed) ✅

## Shard — Receipt-First Agent Observability (April 20, 2026)
- **Repo:** TrentPierce/Shard — FSL-1.1-ALv2
- **What it does:** Agent execution runtime with receipt-first observability. Every step emits durable receipt (routing, trust, cost, latency). Provenance graph.
- **For Solomon OS:** Audit trail + accountability for agent decisions. Cross-topology routing study. Graceful degradation patterns.
- **Status:** Forked (already existed) ✅

## aria-protocol — P2P 1-bit AI Inference (April 20, 2026)
- **Repo:** spmfrance-cloud/aria-protocol — MIT
- **What it does:** P2P decentralized inference using 1-bit models. 70-82% energy savings. Runs on any CPU. Blockchain provenance, consent-based.
- **For research:** AgentFM competitor analysis. 1-bit model quality tradeoff monitoring. Edge inference option.
- **Status:** Forked (already existed) ✅

## mycellm — P2P GPU Inference Network (April 20, 2026)
- **Repo:** mycellm/mycellm — Apache 2.0
- **What it does:** P2P GPU pooling via QUIC. Credit economy, Sensitive Data Guard, private networks, OpenAI-compatible API, iOS app.
- **For research:** AgentFM direct competitor. Credit economy + privacy safeguards architecture study.
- **Status:** Forked (already existed) ✅

## Aragora — Multi-Model Deliberation Control Plane (April 20, 2026)
- **Repo:** synaptent/aragora — MIT
- **What it does:** Auditable multi-model decision control plane with structured debate, receipts, provenance, and review gates. Default-deny sandboxed effectors.
- **For Solomon OS:** Governance layer for Hermes multi-agent deliberations. Audit trails on every agent decision. Verifiable bounded execution.
- **Status:** Forked to jvanleur2234-glitch/aragora ✅

## agent-security-scanner-sinewave — Sinewave Security Scanner (April 20, 2026)
- **Repo:** sinewaveai/agent-security-scanner-mcp — (verify license)
- **What it does:** Security scanner MCP server with prompt injection firewall, package hallucination detection (4.3M+ packages), 1000+ vuln rules, AST + taint analysis, auto-fix.
- **For Solomon OS:** Security hardening for Hermes. MCP-native fits our architecture. Auto-fix adds self-healing defense capability.
- **Status:** Forked to jvanleur2234-glitch/agent-security-scanner-sinewave ✅

## agentverus-scanner — Trust & Safety Scanner for Agent Skills (April 20, 2026)
- **Repo:** agentverus/agentverus-scanner — MIT
- **What it does:** Analyzes AI agent skill files for prompt injection, data exfiltration, 10+ ASST threat categories. Detects AGENTS.md/SOUL.md tampering. Structured trust reports.
- **For Solomon OS:** Trust verification layer for Hermes skills. Detects workspace config tampering. Trust scoring for skill marketplace.
- **Status:** Forked to jvanleur2234-glitch/agentverus-scanner-new ✅

## raxe-ce — Runtime Security for AI Agents (April 20, 2026)
- **Repo:** raxe-ai/raxe-ce — (verify license)
- **What it does:** 515+ L1 rules + ML L2 ensemble for real-time prompt/reasoning/tool/memory protection. 94.7% TP, sub-5ms. 100% local, no cloud.
- **For Solomon OS:** Runtime defense guard for Hermes execution. Local-only fits privacy-first. Speed sufficient for production.
- **Status:** Forked to jvanleur2234-glitch/raxe-ce-new ✅

## vigile-scan-sinewave — Zero-Config Trust Scanner (April 20, 2026)
- **Repo:** Vigile-ai/vigile-scan (sinewave variant) — Apache 2.0
- **What it does:** 59 detection rules, auto-discovers MCP configs and skills, produces trust scores. No install required. JSON output.
- **For Solomon OS:** Quick skill trust verification. Frictionless scanning of new Hermes skills. CI/CD integrable.
- **Status:** Forked to jvanleur2234-glitch/vigile-scan-sinewave ✅

---
*Last updated: 2026-04-20 19:40 UTC — AIQ Scout Hourly Session*
