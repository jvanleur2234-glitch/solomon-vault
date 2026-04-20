# RD Report: Solvely-Colin/Quorum

**Date:** 2026-04-20
**Fork:** jvanleur2234-glitch/Quorum
**License:** MIT
**Category:** Multi-Agent Deliberation
**Relevance:** 🟡 Worthwhile

## What It Is

TypeScript multi-AI deliberation framework where multiple providers (Claude, GPT, Gemini, etc.) debate, critique, and refine each other's thinking through a 7-phase process. Returns synthesized answers with confidence scores. MCP server compatible.

## Key Capabilities

- **7-phase deliberation**: Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote → Synthesis
- **Multi-provider**: Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Ollama, more
- **Evidence protocol**: Sources cited, claims cross-validated
- **Adaptive debate**: Auto-skip/extending rounds based on disagreement
- **Policy guardrails**: YAML rules block/warn/pause deliberations
- **Deterministic replay**: SHA-256 hash-chained ledger for auditability
- **MCP server**: Use in Claude Desktop, Cursor, any MCP client

## Comparison to Solomon OS Stack

- Deliberation → potential tool for Solomon's "Council of High Intelligence" concept
- Audit trail → important for compliance in agent decision-making
- Multi-provider debate → could enhance Hermes's reasoning quality

## Recommendation

**SKILL** — Not critical but excellent fit for Solomon's multi-agent deliberation needs. The audit trail + evidence protocol features are valuable for enterprise compliance. Fork exists. Write integration note for Hermes skill marketplace.