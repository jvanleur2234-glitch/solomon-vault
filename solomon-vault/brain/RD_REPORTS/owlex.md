# RD Report: owlex

## What It Is
Multi-model council deliberation via MCP for Claude Code. Queries Codex, Gemini, OpenCode, ClaudeOR, AiChat in parallel, runs 2-round review process, then synthesizes with Claude.

## Relevance to Solomon OS
- **Hermes MCP Integration**: Directly compatible with Hermes MCP skills ecosystem
- **Multi-agent deliberation**: Competitor to our Council of High Intelligence concept
- **Quality gate**: Could be used as validation layer for Hermes agent outputs

## Key Features
- Round 1: Independent answers (no seeing each other)
- Round 2: Each agent sees peers' answers and revises
- Claude synthesizes final structured response
- 7 specialist roles (security, perf, skeptic, architect, maintainer, dx, testing, neutral)
- Team presets: security_audit, code_review, architecture_review, devil_advocate, balanced, optimal
- MCP server for Claude Code integration

## License & Fork Status
- MIT License ✅
- Forked to: `jvanleur2234-glitch/owlex`

## Verdict
**SKILL** — Install as Hermes MCP skill for multi-model validation workflows. Integrate with Hermes dojo/skill-factory for security review rounds.

## Comparison to Existing
- Similar to `spectra` (already forked) but uses external models via council rather than internal Claude Code agents
- Complements `agent-tower-plugin` (debate mode)

## Action Items
- [ ] Write SKILL.md for Hermes integration
- [ ] Add team presets relevant to Solomon OS (business_analyst, sales_agents)
