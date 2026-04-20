# HERMES CAPABILITIES — Updated 2026-04-19

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
- ** firmislabs/firmis-scanner** — Apache 2.0, multi-platform agent security scanner (242 rules, 21 threat categories)
- ** vigile-ai/vigile-scan** — Apache 2.0, MCP server + agent skill scanner with trust scores (59 rules)
- ** agentseal/agentseal** — 225+ tests, 28 agents, red-teaming + supply-chain audits for AI agents
- ** raxe-ai/raxe-ce** — 515+ L1 rules + on-device ML ensemble, 94.7% TP rate, runtime prompt injection protection
- ** opena2a-org/hackmyagent** — 164 adversarial payloads, 209 static checks, semantic security analysis for agent skills
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
*Last updated: 2026-04-19 22:30 UTC — AIQ Scout Session*