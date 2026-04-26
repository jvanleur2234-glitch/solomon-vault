# Solvely-Colin/Quorum — TypeScript Multi-AI Deliberation Framework

**Date:** 2026-04-26  
**Slug:** quorum-solvely-colin  
**Category:** Multi-Agent Deliberation  
**License:** MIT  
**Language:** TypeScript  
**Stars:** ~800 (est.)  
**Forked:** Yes (`jvanleur2234-glitch/quorum`)

## What it is
7-phase multi-AI deliberation (Gather → Plan → Formulate → Debate → Adjust → Rebuttal → Vote + Synthesis) using ranked voting (Borda) to reach consensus. Generates answer + confidence scores. Supports MCP server integration.

## Key Features
- **7-phase deliberation** with ranked voting (Borda)
- **Runner-up minority report** to reduce bias
- **Multi-provider**: OpenAI, Anthropic, Gemini, Kimi, DeepSeek, Mistral, Groq, Ollama
- **Deterministic replay** via SHA-256 ledger
- **Policy guardrails** (YAML-based)
- **Human-in-the-loop** pause capability at any phase
- **Debate topologies**: mesh, star, tournament, pipeline
- **Confidence scoring** + evidence/citation protocol

## Relevance to Solomon OS / Hermes
Quorum's 7-phase deliberation is more structured than current deliberation approaches. MCP integration means potential Hermes interop. TypeScript aligns with Hermes ACP.

## Verdict
**FORGE** — Fork and study for Hermes deliberation skill. Multi-provider + ranked voting + confidence scoring is a significant differentiator.