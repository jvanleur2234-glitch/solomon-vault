# AIBYAI — Multi-Agent Deliberative Intelligence Platform (Apr 27, 2026)

**Fork:** `jvanleur2234-glitch/aibyai-fresh` (MIT)
**Source:** https://github.com/Yash-Awasthi/aibyai

## What It Does
TypeScript platform where 4+ AI agents (Empiricist, Strategist, Historian, Skeptic) actively argue, critique, and score consensus with interpretable confidence metrics.

**Key features:**
- Multi-provider orchestration (OpenAI, Anthropic, Gemini, Groq)
- Conflict detection + resolution between agents
- Cold Validator checks for hallucinations
- Topic graph memory with decay
- Consensus scoring: 0.6 × Agreement + 0.4 × PeerRanking

## Why It Matters for Solomon OS
- Confidence metric on multi-agent outputs = higher trust for JCPaid client deliverables
- Topic graph memory aligns with Hermes persistent memory architecture
- Conflict detection could prevent tool-calling conflicts in Hermes

## Fit: INTEGRATE
MIT licensed. Strong fit for Hermes deliberation layer. Quorum and Council already forked — this adds a 3rd deliberation variant.

## Action Items
- [ ] Fork to jvanleur2234-glitch
- [ ] Compare with Quorum and Council implementations
- [ ] Extract conflict detection pattern for Hermes
