# Scout Session Summary — April 23, 2026

## Date & Time
2026-04-23 11:45 UTC

## Repos Cloned This Session
- None (all target repos already existed in workspace)

## Repos Forked This Session
- `deliberation` (2389-research/deliberation) — multi-agent contemplative deliberation framework
- All other targets were already forked

## Key Findings

### 1. AGENT FRAMEWORKS (2026)
- **microsoft/agent-framework** — ~9.7k stars, MIT, graph-based orchestration, time-travel, Python/.NET
- **dapr/dapr-agents** — Apache-2.0, Kubernetes-native AI agents, durable workflow execution
- **gollem** (fugue-labs) — Go agent framework, compile-time type safety, zero deps, multi-provider
- **voltagent** — TypeScript, multi-agent, memory/RAG/MCP, voice support
- **kohaku** (DNLINYJ/KohakuTerrarium) — Python, creatures + terrariums, persistent memory
- **ddalcu/agent-orcha** — TypeScript, YAML-based orchestration, P2P agent sharing
- **agent-express** — TypeScript, middleware-style, 12+ providers, observability

### 2. SELF-IMPROVING AGENTS
- **MaximeRobeyns/self_improving_coding_agent** — MIT, iterative self-improvement loop, Docker
- **xmaks82/self-improving-agent** — 16-agent pipeline, prompt versioning from feedback
- **theprint/nfh-self-improvement-loop** — MIT, adversarial evaluator separates generation/judgment
- **Ramsbaby/openclaw-self-evolving** — Bash+Python, weekly log analysis, human-in-loop proposals
- **Grail-Computer/Self-Improving-Agent** — AGENTS.md persistence + meta-skill template
- **j-d0g/self-improving-agent** — Financial QA, Learner+Improver cross-session learning

### 3. HERMES MCP SKILLS
- **NousResearch/hermes-agent** — FastMCP skill merged (PR #10413), jMunch MCP suite (code/doc/data retrieval)
- Native MCP client with HTTP transport, reconnection, security — 1186 tests passing
- mcporter CLI for discovering/calling MCP servers
- Hermes-as-MCP-server proposal (expose tools to MCP ecosystem)

### 4. DISTRIBUTED AI COMPUTE P2P
- **hyperspaceai/agi** — MIT, P2P DiLoCo training, 195x compression, blockchain economics
- **mycellm** — Apache-2.0, P2P GPU federation, QUIC NAT traversal, credit economy
- **Agent-FM/agentfm-core** — Go/libp2p, zero-config P2P, Podman sandboxing, GossipSub load balancing
- **Shard** (TrentPierce) — Browser WebGPU scouts + verifier nodes, BitNet 1.58-bit
- **KwaaiNet** — MIT, Rust/TypeScript, decentralized trust graph, live network v0.3.24
- **mycellm** — P2P inference with OpenAI-compatible API

### 5. AI SECURITY SCANNERS
- **sinewaveai/agent-security-scanner-mcp** — 1,700+ rules, AST/taint analysis, prompt injection firewall
- **pantheon-security/medusa** — 9,600+ patterns, repo poisoning detection, 200 CVE detections
- **snyk/agent-scan** — MCP server inventory, 15+ risk categories
- **empowered-humanity/agent-security** — OWASP ASI Top 10, 220+ patterns, TypeScript/MIT
- **firmis-scanner** — 268 detection rules, code + instruction surface analysis
- **agentverus/agentverus-scanner** — SKILL.md trust boundary scanning, behavioral risk scoring
- **securevector-ai-threat-monitor** — Local real-time firewall, per-agent budgets, skill scanner

### 6. BROWSER AUTOMATION
- **hyperbrowserai/hyperagent** — TypeScript, Playwright+AI, natural language, action caching
- **vercel-labs/agent-browser** — Rust CLI, accessibility tree, screenshot, keyboard input
- **VibiumDev/vibium** — WebDriver BiDi, zero-config, ~10MB binary, multi-language libs
- **mozilla/pilo** — Tabstack, natural language browser control, guardrails
- **idan-rubin/browserclaw-agent** — Anti-bot bypass, Cloudflare Turnstile, per-domain skill learning
- **AshtonVaughan/agentbrowser** — Semantic actions, 95% lower token cost vs HTML
- **sired/browser-use** — Python, memory-enabled, LangChain integration

### 7. MULTI-AGENT DELIBERATION
- **slior/dialectic-agentic** — YAML-free, skill-file driven, architect/security/performance debate
- **2389-research/deliberation** — Claude skills, discernment/cleverness/gathered phases
- **Solvely-Colin/Quorum** — TypeScript, 7-phase deliberation, Borda voting, audit ledger
- **dubs3c/council** — Python, Architect/Critic/AppSec personas, consensus report
- **gumbel-ai/agent-debate** — Evidence-based, file:line citations, adversarial refinement
- **Yash-Awasthi/aibyai** — Conflict detector + synthesizer + cold validator, confidence scoring
- **kstevica/captain-claw** — Agent Council (debate/brainstorm/review/planning), voting, TL;DR

### 8. RECURRENT TRANSFORMER MoE
- **kyegomez/OpenMythos** — Recurrent-Depth Transformer, looped layers, MoE sparse experts
- **raymin0223/mixture_of_recursions** — Per-token recursion depth routing, MoR framework
- **thu-ml/ReMoE** — Differentiable MoE routing, ReLU-based, adaptive L1 regularization

## X/Twitter Trends
- **Hermes Agent** = 113k+ stars, learning loops, membase plugin, Higgsfield Marketing Studio
- **OWASP Top 10 for Agentic Applications 2026** — prompt injection #1, execution layer exploits
- **"Shadow Agent" crisis** — Google's warning on unauthorized AI deployments
- **Claude weaponized** for exploit development against Mexican government agencies
- **Sentient GRID** — orchestration layer for agents, token-level routing, reproducibility

## Actions Taken
- Forked `deliberation` to jvanleur2234-glitch
- All other target repos already cloned + forked
- 326 RD reports in vault
- HERMES_CAPABILITIES.md already includes relevant entries

## Unresolved / Follow-up
- OpenMythos (kyegomez) already forked but RD report may need updating for latest branch
- Some deliberation repos (Quorum, council, agent-debate) — check if RD reports are current

## Next Session
- Check for new repos from @swarms_corp (Kye Gomez)
- Monitor OWASP LLM Top 10 ecosystem tools
- Check n8n community nodes for AI agents
