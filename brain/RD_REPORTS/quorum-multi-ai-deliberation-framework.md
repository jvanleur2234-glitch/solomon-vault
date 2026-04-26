# Quorum — Multi-AI Deliberation Framework (7-Phase Debate)

## Quick Summary
Multi-AI deliberation framework that engages multiple AI providers (Claude, GPT, Gemini, DeepSeek, etc.) to debate, critique, and converge on synthesized answers via a 7-phase process. Includes evidence protocol, code review/CI integration, and deterministic replay.

## What It Is
Quorum runs a structured 7-phase deliberation: Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote. Produces synthesized answers with confidence scores. Supports evidence citation and cross-validation. Ideal for complex decisions requiring multi-model validation.

## 7-Phase Process
1. **Gather**: Each provider responds in isolation
2. **Plan**: Providers see others' takes and plan positions
3. **Formulate**: Formal position statements
4. **Debate**: Providers critique all positions
5. **Adjust**: Revisions based on critiques
6. **Rebuttal**: Final rebuttals or concessions (auto-skipped if consensus)
7. **Vote**: Ranking via Borda, ranked-choice, approval, or Condorcet methods

## Key Capabilities
- **Multi-provider**: Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Ollama
- **Adaptive debate**: Auto-skip or extend rounds based on disagreement
- **Evidence protocol**: Providers cite sources; cross-validation of claims
- **Code review + CI/CD**: Code diffs, PRs, structured outputs with exit codes
- **Policy guardrails**: YAML-based rules to block/warn/pause deliberations
- **Deterministic replay**: SHA-256 hash-chained ledger for auditability
- **Human-in-the-loop**: Allow pausing to inject guidance
- **Flexible topologies**: Mesh, star, tournament, pipeline
- **MCP server**: Compatible with Claude Desktop, Cursor, MCP clients
- **Red team analysis**: Adversarial testing packs

## Relevance to Solomon OS
- **INTEGRATE** — Multi-agent deliberation is core to Solomon OS intelligence layer
- 7-phase process maps to our Quorum deliberation patterns already in use
- SHA-256 audit trail aligns with enterprise compliance needs
- Code review + CI integration is valuable for JCPaid development workflows
- Policy guardrails YAML pattern could unify our existing rule system

## License & Fork Status
- **License:** MIT
- **Stars:** ~300 (estimated, active deliberation framework)
- **Forked:** Already forked (multiple versions: quorum, quorum-fresh, quorum-new)

## Verdict
**INTEGRATE** — Our Quorum fork is well-established. The 7-phase process and SHA-256 audit trail are strong differentiators for enterprise clients. CI/CD integration expands Quorum beyond deliberation into development workflows.

## Links
- https://github.com/Solvely-Colin/Quorum
- Fork: https://github.com/jvanleur2234-glitch/Quorum