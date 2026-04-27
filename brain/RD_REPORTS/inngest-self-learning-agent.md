# RD Report: inngest/inngest-self-learning-agent

**Date:** April 26, 2026  
**Fork:** Check workspace  
**License:** MIT  
**Language:** TypeScript/Node.js  

## What It Is
A durable AI agent built with Inngest and pi-ai that experiments with its own prompts over time. Runs think/act/observe loop, scores responses after the fact, uses scheduled evaluation jobs to create/test/promote better behavioral prompts.

## Key Features
- **Self-evaluation loop:** Think → Act → Observe → Score
- **Prompt versioning:** A/B testing of behavioral prompts
- **Automated evaluation pipeline:** Promotes stronger prompt versions
- **Guardrails:** Prevents scoring criteria from leaking into behavior
- **Multi-channel:** Telegram/Slack → Inngest Cloud → WebSocket → Local Worker → LLM
- **Sub-agents:** Task delegation, multi-channel support
- **LLM compatibility:** Anthropic/OpenAI/Google

## Key Innovation
Agent can rewrite prompts and embed scoring criteria into outputs, with guardrails preventing test-target gaming.

## Solomon OS Fit
**SKILL** — Self-learning agent with prompt versioning directly applicable to Hermes evolution loop. The guardrails preventing "scoring criteria leakage" is a critical insight for safe self-improvement. The Inngest event-driven architecture could inspire our agent workflow design.

## Action
Clone. Write RD report. Add to HERMES_CAPABILITIES.md.