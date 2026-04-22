# RD Report: Quorum — Multi-Agent AI Deliberation Framework

**Date:** 2026-04-22  
**Category:** Multi-Agent Deliberation  
**Source:** web_research (github)  
**Fork Status:** Already forked (Quorum)

## What It Is
TypeScript-based MIT-licensed framework for multi-AI deliberation. Orchestrates debates among multiple AI providers to produce synthesized, more robust answers with confidence scores.

## Key Capabilities
- **7-phase deliberation:** Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote
- **Voting systems:** Borda count, ranked-choice, Condorcet
- **Synthesis phase** with minority report
- Support for many providers: OpenAI, Claude, Gemini, Kimi, DeepSeek, Mistral, Groq, Ollama
- Evidence protocol with source citations and cross-validation
- CI/CD integration, deterministic replay (SHA-256 ledger)
- MCP server compatibility, red team analysis
- Configurable debate topologies: mesh, star, tournament, pipeline

## Comparison to What We Have
- Similar to: Concilium, ARTEMIS Agents, Agent Tower Plugin
- Unique: 7-phase structured deliberation, multiple voting algorithms, SHA-256 ledger
- Production-grade with CI/CD integration

## Relevance to Solomon OS / Hermes
- Useful for Hermes's multi-agent decision making
- Structured deliberation for critical decisions (like Council of High Intelligence)
- Cross-validation with evidence protocol adds trust

## Recommendation
**ALREADY FORKED** — No action needed. Already tracked as `Quorum`.

---

## Stats
- Stars: ~1K+
- License: MIT
- Language: TypeScript