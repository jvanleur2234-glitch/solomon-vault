# dubs3c/council — Structured Multi-Agent Consensus

**Fork status:** Not yet forked  
**Date:** April 26, 2026

## What it is
Python-based multi-agent discussion system that reaches consensus through structured debates. Four-stage flow: InputNode → ProposalPhase → DebatePhase → Consensus. Default personas: Architect (systems design), Critic (risk-focused), AppSec Specialist.

## Key capabilities
- Independent initial proposals by agents
- Iterative rounds where agents revise, agree, or raise concerns
- Early consensus if all agree
- Moderator-generated consensus document
- Approval round and final markdown report with full transcript
- Per-agent LLM provider configuration (OpenAI-compatible)
- YAML persona configuration

## Relevance to Solomon OS
- **INTEGRATE** — Could be the core deliberation engine for Solomon OS major decisions
- **SKILL** — Architect/Critic/AppSec persona pattern for Hermes skill evaluation

## Recommendation
INTEGRATE — Fork and adapt as Solomon OS council skill. The markdown transcript + persona approach is exactly what we need.

## Stars
~500 | MIT

## License
MIT