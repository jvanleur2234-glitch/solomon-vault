# RD Report: agent-tower-plugin — Multi-Agent Deliberation for Claude Code

**Date:** 2026-04-21  
**Repo:** BayramAnnakov/agent-tower-plugin  
**URL:** https://github.com/BayramAnnakov/agent-tower-plugin  
**License:** MIT  
**Stars:** ~low (new)  
**Relevance:** Multi-agent deliberation, council/debate/deliberate modes, Claude Code integration  

## What It Is
A Python-based multi-agent deliberation plugin for Claude Code that orchestrates diverse AI coding assistants (Claude, Codex, Gemini) to generate multiple perspectives, then combines them via structured modes.

## Key Capabilities
- **Council mode:** Parallel agents with anonymous ranking + chairman synthesis
- **Debate mode:** Adversarial binary-position argument with judge
- **Deliberate mode:** Producer/reviewer loop toward consensus
- **Multi-backend:** Claude, Codex, Gemini via registry pattern
- **Configurable rounds** and consensus thresholds

## Relevance to Solomon OS / Hermes
- Multi-backend deliberation useful for Hermes skill quality validation
- Council mode matches "Council of High Intelligence" concept
- MIT licensed

## Verdict
**SKILL** — Fork for Hermes multi-backend deliberation. The council/debate/deliberate patterns could enhance Hermes skill verification across different LLM providers.