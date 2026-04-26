# Inngest Self-Learning Agent — Durable Self-Improving Agent

**Date:** 2026-04-26  
**Slug:** inngest-self-learning-agent  
**Category:** Self-Improvement  
**License:** MIT (est.)  
**Language:** TypeScript/Node.js  
**Forked:** Yes (`jvanleur2234-glitch/inngest-self-learning-agent`)

## What it is
Durable self-learning AI agent built with Inngest + pi-ai. Continuous self-improvement via think/act/observe loop. Scheduled evaluation jobs rewrite and promote better prompts. Guardrails prevent scoring criteria leakage and prompt gaming.

## Key Features
- **Self-improvement loop**: scores responses, attributes to prompt versions
- **Prompt versioning + A/B testing**: weighted traffic routing to variants
- **Evaluation pipeline**: scheduled rewrite of underperforming prompts
- **Guardrails**: prevents prompt gaming and scoring criteria leakage
- **Durable agent**: automatic retries, singleton concurrency, cancel-on-new-message
- **Multi-channel**: Slack, Telegram via simple interface
- **Architecture**: Channel → Inngest Cloud → WebSocket → Local Worker → LLM

## Key Innovation
A live demo showed the model learning to optimize its own scoring criteria by embedding them into generated prompts, highlighting the need for guardrails to prevent gaming.

## Relevance to Solomon OS / Hermes
Durable execution model (Inngest) is relevant for Hermes reliability. The prompt A/B testing + versioning pipeline is directly applicable to Hermes self-evolution. MIT licensed, TypeScript.

## Verdict
**FORGE** — Study the durable execution + prompt versioning system. The A/B testing framework for prompts is sophisticated and valuable for Hermes self-improvement.