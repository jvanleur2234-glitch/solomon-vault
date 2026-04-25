# RD Report: Multi-Agent Deliberation Frameworks

## Summary
Survey of multi-agent deliberation frameworks found across the workspace scans.

## Key Players

### Quorum (Solvely-Colin)
- TypeScript, 8 stars, MIT
- 7-phase deliberation: Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote
- Multi-provider (Claude, GPT, Gemini, etc.), SHA-256 ledger
- MCP server compatible
- Already cloned at /home/workspace/Quorum

### Council (dubs3c)
- Python, 7 stars, MIT
- Structured debate with personas: Architect, Critic, AppSec Specialist
- Moderator synthesis → consensus → approval round
- Already in workspace

### infektyd/council
- OpenClaw skill for xAI Grok deliberation
- Discord integration for human visibility
- 0 stars, MIT

### gumbel-ai/agent-debate
- Shell-based, 12 stars, null license
- Claude/Codex/Gemini/Copilot debating via shared markdown
- Evidence-based assertions with file:line citations
- Already in workspace

## Relevance to Solomon OS
- **Score: 7/10** — Council of High Intelligence pattern is core to Solomon OS deliberation needs
- Multiple approaches to multi-agent reasoning synthesis
- Quorum's provider diversity is especially relevant for Solomon's multi-LLM approach

## Recommendation
**SKILL** — Study Quorum's architecture most closely. Already cloned. Consider integration into Solomon decision-making layer.
