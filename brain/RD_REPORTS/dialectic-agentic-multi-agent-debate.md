# RD Report: dialectic-agentic — Multi-Agent Design Debate System

**Date:** 2026-04-21  
**Repo:** slior/dialectic-agentic  
**URL:** https://github.com/slior/dialectic-agentic/tree/master  
**License:** MIT  
**Stars:** ~low (new)  
**Relevance:** Multi-agent deliberation, design debate, structured proposals  

## What It Is
A fully agent-native design-debate system where multiple specialized AI agents (architect, security, performance, simplicity) engage in structured rounds of proposals, critiques, and refinements to solve design problems. A judge evaluates convergence after each round.

## Key Capabilities
- **Skill-file based** — works on any agentic platform supporting subagent dispatch + file I/O
- **No traditional code** — declarative via problem.md + debate-config.json
- **Structured rounds:** proposals → critiques → refinements → verdict
- **Judge evaluation** for convergence detection
- **Full trace output** per round with synthesis

## Relevance to Solomon OS / Hermes
- Declarative debate system fits Hermes skill-based architecture
- Useful for design decisions within Solomon OS agent workflows
- MIT licensed

## Verdict
**SKILL** — Fork for Solomon OS design review capabilities. The structured debate format could become a "skill review" workflow for Hermes skill evaluation.