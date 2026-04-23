# council — Structured Multi-Agent Debate Framework

**Source:** https://github.com/dubs3c/council  
**License:** MIT  
**Stars:** ~700+  
**Date:** 2026-04-23

## What it does
Council is a Python-based framework for structured, multi-agent debate where AI agents with distinct personas analyze prompts/files, debate perspectives, and reach consensus through a staged process.

Workflow:
1. Input: Read files and prompts, assign agent personas
2. ProposalPhase: Each agent independently writes an initial proposal
3. DebatePhase: Agents review proposals, revise their own, agree with others, or raise concerns in iterative rounds
4. Early Consensus: Process can stop early if all agents reach agreement
5. Moderator Synthesis: A neutral moderator drafts a consensus document
6. Approval Round: Agents approve or provide feedback on the draft
7. Final Report: Generate and save a Markdown report with full transcript

Default personas:
- The Architect: Systems design expert (high creativity, temperature ~0.8)
- The Critic: Devil's advocate (more risk-focused, temperature ~0.5)
- The Application Security Specialist: Implementation realist (risk, threats, mitigations; temperature ~0.6)

## Solomon OS Fit
**FORGE** — Multi-agent deliberation framework for complex decisions. The persona-based debate process is directly implementable in Hermes. MIT license permits direct use.

## Key Components
- Multi-agent debate lifecycle
- Persona-based agents
- Moderator synthesis
- Markdown report generation
- Early consensus detection
- Configurable personas via YAML

## Recommendation
FORGE — Direct implementation candidate for "Council" mode in Hermes. MIT license enables direct use.