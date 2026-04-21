# Scout Session Summary — 2026-04-21

**Time:** 00:40 UTC  
**Agent:** AIQ Scout  
**Trigger:** Scheduled hourly R&D scan

## Actions Taken

### 1. GitHub Repos Found & Evaluated

| Repo | Category | License | Stars | Verdict | Forked? |
|------|----------|---------|-------|---------|---------|
| microsoft/agent-framework | Agent Framework | MIT | 9.3K | Already present | ✅ |
| fugue-labs/gollem | Go Agent Framework | MIT | new | Already present | ✅ |
| henomis/phero | Multi-Agent Go | Apache-2.0 | new | FORGE | Already present |
| opencmi/alphora | Composable AI Agents | Apache-2.0 | new | Already present | ✅ |
| dapr/dapr-agents | Stateful AI Agents | Apache-2.0 | new | Already present | ✅ |
| yai-dev/agentrail | Agent Harness | Apache-2.0 | new | Already present | ✅ |
| ddalcu/agent-orcha | Declarative Multi-Agent | MIT | new | Already present | ✅ |
| SolaceLabs/solace-agent-mesh | Event-Driven Multi-Agent | MIT | new | Already present | ✅ |
| MaximeRobeyns/self_improving_coding_agent | Self-Improving | MIT | new | Already present | ✅ |
| xmaks82/self-improving-agent | Self-Improving | MIT | new | Already present | ✅ |
| unconst/ninja | Self-Improving Coding | MIT | new | Already present | ✅ |
| Ramsbaby/openclaw-self-evolving | Self-Evolving | MIT | new | Already present | ✅ |
| RangeKing/self-evolving-agent | Goal-Driven Evolution | MIT | new | No report needed | — |
| NousResearch/hermes-agent | Hermes MCP Skills | MIT | high | Already present | ✅ |
| cloudwalk/hermes-mcp | Elixir MCP SDK | MIT | new | Already present | ✅ |
| poetryprotocol/hermes-mcp | Python MCP | MIT | new | No RD needed | — |
| hyperspaceai/agi | Distributed AGI | MIT | new | Already present | ✅ |
| hyperspaceai/hyperspace-node | P2P AI Inference | MIT | 2M+ agents | Already present | ✅ |
| TrentPierce/Shard | Browser P2P Compute | Other | new | Already present | ✅ |
| NikeGunn/tutu | Go P2P AI Engine | MIT | new | Already present | ✅ |
| Agent-FM/agentfm-core | P2P Compute Grid | MIT | new | Already present | ✅ |
| spmfrance-cloud/aria-protocol | 1-bit P2P Inference | MIT | new | Already present | ✅ |
| ruvnet/RuVector (edge-net) | Browser P2P Compute | — | new | No RD needed | — |
| antonellof/peerclaw | Rust P2P AI + Token | MIT | new | Already present | ✅ |
| mycellm/mycellm | P2P GPU Inference | MIT | new | Already present | ✅ |
| sinewaveai/agent-security-scanner-mcp | Security Scanner | MIT | new | Already present | ✅ |
| agentverus/agentverus-scanner | Agent Security | MIT | new | Already present | ✅ |
| Pantheon-Security/medusa | AI Security Scanner | AGPL | 9.6K | Already present | ✅ |
| snyk/agent-scan | Agent Security Scanner |proprietary | new | Already present | ✅ |
| koatora20/guard-scanner | Guard Scanner | MIT | new | Already present | ✅ |
| firmislabs/firmis-scanner | Runtime Security | Apache-2.0 | new | Already present | ✅ |
| opena2a-org/hackmyagent | Semantic Security | MIT | new | Already present | ✅ |
| Vigile-ai/vigile-scan | Trust Score Scanner | Apache-2.0 | new | Already present | ✅ |
| AgentSeal/agentseal | Security Toolkit | — | new | No RD needed | — |
| hyperbrowserai/HyperAgent | Browser Automation | MIT | new | Already present | ✅ |
| vercel-labs/agent-browser | Rust Browser CLI | Apache-2.0 | new | Already present | ✅ |
| mozilla/pilo | Browser Automation | Apache-2.0 | new | Already present | ✅ |
| VibiumDev/vibium | WebDriver Browser | Apache-2.0 | new | Already present | ✅ |
| browserable/browserable | Self-Hosted Browser | MIT | 1.2K | Already present | ✅ |
| ashtonvaughan/agentbrowser | Semantic Browser | MIT | new | Already present | ✅ |
| browser-use/browser-use | AI Browser Agent | MIT | new | Already present | ✅ |
| dayour/copilotbrowser | MCP Browser | MIT | new | Already present | ✅ |
| TrentPierce/Koda | AI Browser | MIT | new | Already present | ✅ |
| slior/dialectic-agentic | Design Debate | MIT | new | NEW — FORGE | ✅ |
| focuslead/ai-council-framework | AI Council | MIT | new | NEW — FORGE | ✅ |
| BayramAnnakov/agent-tower-plugin | Claude Code Plugin | MIT | new | NEW — SKILL | ✅ |
| dnhess/spectra | Blackboard Deliberation | MIT | new | NEW — FORGE | ✅ |
| matiasdaloia/concilium | Multi-LLM Deliberation | MIT | new | NEW — FORGE | ✅ |
| bassrehab/artemis-agents | Structured Debate | MIT | new | NEW — FORGE | ✅ |

### 2. X/Twitter Trends

**"Solomon OS OR Hermes agent":**
- Strong Hermes buzz — Greg Isenberg thread, unified workspace repo (outsourc-e/hermes-workspace)
- Hermes vs OpenClaw comparison: memory, 40+ tools, 90% cheaper
- Paperclip + Hermes for "one-person company" solution
- Chinese community adoption thread

**"self-improving AI defense":**
- Chronos Intelligence post on "unkillable" self-healing prompts
- Self-evaluation as defense against adversarial attacks (2024 paper reference)
- Raptor — autonomous offensive/defensive security framework using Claude Code

**"AI agent security vulnerability 2026":**
- OWASP Top 10 for Agentic Applications 2026 published
- "Shadow Agent" crisis — Google Cybersecurity 2026 Forecast
- Mexican government agencies compromised via weaponized Claude
- Most incidents cannot be mapped to CVEs
- $RECUR protocol on Solana — layered sentinel network for agent security

**"distributed AI compute grid":**
- Sentient AGI GRID — orchestration of thousands of models/agents
- Ashish Kapoor's Intelligence GRID for Physical AI (robotics)

### 3. New RD Reports Written

1. `phero-multi-agent-go.md` — SKILL
2. `artemis-agents.md` — FORGE
3. `concilium-multi-llm-deliberation.md` — FORGE
4. `ai-council-framework.md` — FORGE
5. `dialectic-agentic-multi-agent-debate.md` — SKILL
6. `spectra-multi-agent-deliberation.md` — FORGE
7. `agent-tower-plugin.md` — SKILL

### 4. HERMES_CAPABILITIES.md Updated

7 new deliberation frameworks added (phero, artemis-agents, conciliium, ai-council-framework, dialectic-agentic, spectra, agent-tower-plugin)

### 5. GitHub Sync

Ran `/home/workspace/.agent/sync-to-github.sh` — 10 files changed, pushed to main

## Key Findings

1. **Deliberation frameworks are hot** — 7 new multi-agent deliberation systems found. All MIT licensed. All relevant for "Council of High Intelligence" concept.

2. **Security scanners are everywhere** — OWASP LLM Top 10 + Google "Shadow Agent" crisis driving demand. Multiple scanners already forked (guard-scanner, vigile-scan, medusa, snyk-agent-scan).

3. **Hermes is trending** — Greg Isenberg's setup thread going viral. Strong community adoption. Memory + cost advantages over OpenClaw.

4. **P2P compute is maturing** — TuTu Engine, PeerClaw, mycellm, AgentFM all present. Distributed AI compute substrate exists for Solomon Air.

5. **Most high-value repos already forked** — only the deliberation frameworks were new additions this session.

## Follow-up

- Check for new swarms-rs / Kye Gomez repos next session
- Watch for OWASP LLM Top 10 tool integrations
- Monitor Hermes workspace repo (outsourc-e/hermes-workspace) for unified UI integration