# AIBYAI — Multi-Agent Deliberative Intelligence Platform

**Fork:** `https://github.com/Yash-Awasthi/aibyai` (MIT)  
**My fork:** Already forked  

## What It Is
A TypeScript/React/Fastify platform that runs a **council of 4+ AI agents** to argue, critique, and produce a scored consensus. Instead of trusting one model's answer, multiple agents generate claims, detect conflicts, critique each other, and converge on a verdict with a numeric confidence score.

## Key Features
- **7-phase deliberation**: Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote (Borda, ranked-choice, Condorcet)
- **Parallel generation** from 13+ providers (OpenAI, Anthropic, Gemini, Groq, etc.) with automatic failover
- **Conflict detection**: pairwise claim comparison → triggers critique/rebuttal
- **Cold validation**: hallucination detection before final verdict
- **Confidence scoring**: `0.6 × Agreement + 0.4 × PeerRanking` with breakdown
- **Topic graph memory** with temporal decay across conversations
- **MCP server support**: usable in Claude Desktop, Cursor, any MCP client
- **Policy guardrails**: YAML-based rules to block/warn/pause deliberations

## Why It Matters for Solomon OS / Hermes
- Competes with **Quorum** for multi-agent deliberation use cases
- AIBYAI's confidence scoring + conflict detection adds a layer of rigor Quorum lacks
- Could be integrated as a **Hermes skill** for high-stakes decisions (client pitches, security reviews)
- MIT licensed, TypeScript-first, actively maintained

## Comparison to Existing Stack
| Feature | AIBYAI | Quorum |
|---|---|---|
| Providers | 13+ | 8 |
| Deliberation phases | 7 | 7 |
| Conflict detection | ✅ | ❌ |
| Cold validation | ✅ | ❌ |
| Confidence scoring | Numeric + breakdown | Numeric |
| MCP support | ✅ | ✅ |
| Memory | Topic graph + decay | Basic |

## Verdict
**SKILL** — Useful deliberation layer for Solomon OS. Integrate as Hermes deliberation skill for high-value decisions.