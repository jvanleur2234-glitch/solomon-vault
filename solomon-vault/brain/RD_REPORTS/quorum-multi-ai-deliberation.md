# RD Report: Quorum

**Repo:** `Solvely-Colin/Quorum`  
**Stars:** Growing | **License:** MIT | **Lang:** TypeScript  

## What It Does
Multi-AI deliberation framework — multiple providers debate, critique, refine, then synthesize a superior answer. 7-phase deliberation with evidence protocol.

## Why It Matters for Solomon OS
- **Multi-Provider Reasoning**: Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Groq, Ollama
- **7-Phase Deliberation**: Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote → Synthesis
- **Evidence Protocol**: Providers cite sources, claims cross-validated
- **MCP Server**: Use in Claude Desktop, Cursor, any MCP client
- **Adaptive Debate**: Auto-skip or extend rounds based on disagreement

## Key Capabilities
- Multi-provider orchestration with provider auto-detection
- 7 deliberation phases with ranked voting (Borda, Condorcet, etc.)
- Synthesis from runner-up (reduces bias)
- SHA-256 hash-chained ledger for auditability
- CI/CD integration with structured output
- Policy guardrails for human-in-the-loop

## Comparison to What We Have
vs **Council**: Similar deliberation concept but Quorum has provider diversity and synthesis-from-runner-up approach.

## Recommendation
**INTEGRATE** — Could power Solomon OS "Council of Experts" for critical business decisions. MCP server makes integration straightforward.

**Category:** #multi-agent #deliberation #reasoning
