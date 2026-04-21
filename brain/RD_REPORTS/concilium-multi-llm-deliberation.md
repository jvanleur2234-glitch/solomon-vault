# RD Report:concilium — Multi-LLM Deliberation Platform

**Date:** 2026-04-21  
**Repo:** matiasdaloia/concilium  
**URL:** https://github.com/matiasdaloia/concilium  
**License:** MIT  
**Stars:** ~low (new)  
**Relevance:** Multi-agent deliberation, parallel execution, blind peer review, synthesis  

## What It Is
A multi-LLM deliberation platform that runs several AI agents in parallel, has them anonymously peer-review each other, and synthesizes a single superior answer. Reduces validation time from ~25 min to ~3 min per prompt.

## Key Capabilities
- **Parallel execution** with multiple agents (Claude, OpenAI, local models)
- **Anonymous jury review** — agents rank peers without knowing identities
- **Chairman synthesis** for final output
- **CLI + Electron desktop GUI**
- **Local-first** — data stays on-device
- **Programmatic API** for integrating agent skills

## Relevance to Solomon OS / Hermes
- Peer review/synthesis pattern useful for Hermes skill validation
- Anonymous review prevents sycophancy — relevant for security-critical workflows
- MIT licensed

## Verdict
**FORGE** — Fork for Solomon OS quality assurance layer. Anonymous peer review fits Hermes skill verification before deployment.