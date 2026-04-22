# RD Report: AIBYAI — Multi-Agent Deliberative Council

**Date:** 2026-04-22
**URL:** https://github.com/Yash-Awasthi/aibyai
**License:** MIT (inferred)
**Fork:** https://github.com/jvanleur2234-glitch/aibyai

---

## What It Is
Multi-agent deliberative intelligence platform. Instead of trusting one model's output, runs a council of 4+ agents that argue, critique each other's claims, and produce a scored consensus with a numeric confidence score. TypeScript/React/Fastify stack with PostgreSQL + Redis + Docker.

---

## How It Works
1. User submits query → Router classifies complexity + selects agent archetypes
2. 4-7 agents run concurrently, each generating claims with confidence scores
3. Conflict detector analyzes claims for contradictions
4. If contradictions are severe → agents critique each other, re-argue or defend
5. Cold validator checks for hallucinations, validates verdict
6. Output: verdict, overall score (0-1), confidence breakdown, cost per query

---

## Key Capabilities
- Peer critique and cross-agent validation
- Quantified confidence scoring: `0.6 × Agreement + 0.4 × PeerRanking`
- Memory and topic graphs for cross-conversation recall
- Multi-provider: 13+ providers with automatic failover
- Per-query cost tracking
- MCP-compatible
- Score formula reduces hallucinations by making disagreement visible

---

## Why It Matters
Single-model outputs have no reliability signal. A council that scores its own agreement is the right abstraction for high-stakes decisions. This directly competes with "Council of High Intelligence" pattern from swarms_corp.

---

## Solomon OS Fit
- **FORGE** — Council deliberation pattern IS the "Council of High Intelligence" for Hermes. Numeric confidence scoring lets clients know when to trust vs. escalate. MIT license permits direct use.

---

## Comparison
| Aspect | AIBYAI | Quorum | swarms Council |
|--------|--------|--------|----------------|
| Agents | 4-7 concurrent | Multi-provider debate | Variable |
| Confidence | Numeric (0-1) | Borda voting | None |
| Validation | Cold validator | Auto/consensus | None |
| Memory | Topic graph | None | None |
| Stack | TS/React | Node.js | Python |

---

## Recommendation
**FORGE** — Implement council pattern in Hermes. Confidence scoring gives clients a reliability signal. MIT license.