# RD Report: Quorum — Multi-AI Deliberation Framework

**Date:** April 26, 2026  
**Author:** AIQ Scout  
**Status:** INTEGRATE  
**License:** MIT  
**Stars:** Active, v0.13.0  

## What It Is
TypeScript multi-AI deliberation framework. 7-phase structured process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) + synthesis. Multiple AI providers (Claude, GPT, Gemini, Kimi, DeepSeek, Mistral, Ollama).

## Key Features
- 7-phase deliberation with adaptive pacing (auto-skip/extend based on disagreement)
- Voting mechanisms: Borda, ranked-choice, approval, Condorcet
- Evidence protocol: providers cite sources, cross-validation
- CI/CD integration, structured output, exit codes for automation
- Policy guardrails (YAML-based) to block/warn/pause deliberations
- Deterministic replay via SHA-256 hashed ledger for auditability
- Human-in-the-loop controls
- Debate topologies: mesh, star, tournament, pipeline
- MCP server for tooling integration

## Solomon OS Fit
INTEGRATE — Council of High Intelligence competitor. Deterministic replay + auditability aligns with Solomon OS compliance requirements. Structured deliberation could power Solomon Browser decision-making.

## Action
- Already in workspace as quorum-fresh
- Fork to jvanleur2234-glitch if not done
- Study YAML guardrails + audit ledger for Hermes governance

## Links
- https://github.com/Solvely-Colin/Quorum