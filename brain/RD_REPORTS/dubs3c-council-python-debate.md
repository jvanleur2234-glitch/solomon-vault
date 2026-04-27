# RD Report: dubs3c/council

**Date:** April 26, 2026  
**Fork:** Check workspace  
**License:** MIT  
**Language:** Python  

## What It Is
Python multi-agent debate framework designed to reach consensus through structured, multi-turn discussions.

## Architecture
**4-phase pipeline:**
1. InputNode: reads files/prompts, applies agent personas
2. ProposalPhase: each agent generates initial proposal
3. DebatePhase: agents critique peers, revise, agree, raise concerns
4. Consensus: neutral moderator synthesizes agreed-upon consensus

**Default Personas:**
- The Architect: Systems design and scalability (high creativity)
- The Critic: Risk assessment and edge-case detection (focused)
- The Application Security Specialist: Security-focused risk/mitigation (balanced)

## Key Capabilities
- Parallel deliberation with persona-driven agents
- Structured debate rounds with revision, agreement, issue disclosure
- Moderator synthesizes consensus document
- Markdown final report with full transcripts
- Live streaming of debate
- Configurable turn limits

## Solomon OS Fit
**SKILL** — Python debate framework with structured personas. Security-specialist persona is directly relevant to AgentArmor Studio. Four-phase pipeline (Input → Proposal → Debate → Consensus) maps well to our Hermes governance flow.

## Differentiation from Quorum
- Quorum: TypeScript, 7-phase, multi-provider, SHA-256 audit
- Council: Python, 4-phase, persona-based, transcript reports
- Both strong; Council's persona system is more flexible

## Action
Study. Clone if not in workspace. Write RD report. Add persona definitions to AgentArmor Studio Layer 8 (governance).