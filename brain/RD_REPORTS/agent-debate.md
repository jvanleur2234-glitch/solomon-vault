# RD Report: agent-debate

**Fork Status:** Already forked  
**License:** MIT  
**Stars:** ~200 (structured adversarial debate protocol for AI coding agents)  
**Relevance:** MEDIUM — multi-agent deliberation, evidence-based technical decisions

## What It Is
Implements structured, adversarial debate protocol for AI coding agents (Claude, Codex, Gemini, Copilot) to collaboratively review and debate technical decisions by editing a shared Markdown document.

## Key Capabilities
- Multi-agent debate: 2–4 agents simultaneously edit shared file
- Evidence-based claims: cite file:line references
- Tracking disputes and convergence toward recommendation
- Deterministic replay with SHA-256 ledger
- CI/CD integration, policy guardrails, red-team adversarial testing

## Relevance to Hermes/Solomon
- Debate protocol could enable Hermes agents to reason through complex client decisions
- Evidence-based approach aligns with Solomon OS "show your work" philosophy
- Could be used for multi-agent architecture review sessions

## Integration Recommendation
**SKILL** — Lower priority but useful for complex technical decisions. Consider as a Hermes skill for architecture review workflows.

## Notes
- MIT licensed
- Supports multiple agents: Claude Code, Codex, Gemini CLI, Copilot CLI
- Evidence citation format enables grounded technical reasoning