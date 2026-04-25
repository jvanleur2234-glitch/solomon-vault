# Quorum — Multi-Provider AI Deliberation Framework (Apr 25, 2026)

**Fork:** `jvanleur2234-glitch/quorum-fresh` (MIT)
**Source:** https://github.com/Solvely-Colin/Quorum

## What It Does
TypeScript deliberation framework that orchestrates 7-phase debates across multiple AI providers (Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Ollama). Produces synthesized answers with confidence scores and minority reports.

**7 phases:** Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote (Borda) → Synthesis

## Why It Matters for Solomon OS
- Multi-provider deliberation = resilience against single-provider outages (DeepSeek V4 timeouts trending on X right now)
- Evidence/citation protocol enables auditable reasoning for enterprise JCPaid clients
- Policy guardrails (YAML) map directly to Hermes permission system
- Hash-based deterministic replay for compliance audit trails

## Fit: INTEGRATE
MIT licensed. Directly complement Hermes multi-model routing. Quorum's debate structure could wrap Hermes tool calls to produce confidence-scored outputs before execution.

## Action Items
- [ ] Clone to workspace and study deliberation phase implementation
- [ ] Map Borda voting to Hermes confidence scoring
- [ ] Consider as pre-execution validation layer for high-stakes tools
