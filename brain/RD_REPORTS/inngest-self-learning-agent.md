# RD Report: Inngest Self-Learning Agent

**Repo:** `inngest/inngest-self-learning-agent`  
**URL:** https://github.com/inngest/inngest-self-learning-agent  
**License:** Unknown  
**Stars:** Unknown  
**Date:** 2026-04-26

## What It Is
Durable AI agent built with Inngest and pi-ai that runs a think/act/observe loop, scores responses, and uses scheduled evaluation jobs to create, test, and promote better behavioral prompts over time. Includes guardrails against gaming the scoring system.

## Key Capabilities
- Self-improvement loop: prompts rewritten and scored after each response
- Prompt versioning with attribution to specific versions
- A/B testing of behavioral prompts with weighted selection
- Evaluation pipeline for prompt improvement
- Guardrails against prompt gaming
- Response scoring: relevance, completeness, tool efficiency, tone
- Sub-agents and multi-channel (Slack, Telegram)
- Durable, single-conversation semantics with retries

## Relevance to Solomon OS
**HIGH** — Self-improvement architecture directly applicable to Hermes's own self-evolution goals. The prompt versioning + A/B testing + guardrails pattern is exactly what Hermes self-evolution needs.

## Use Case for JCPaid/Hermes
- Core architecture for Hermes self-improvement loop
- Evaluation pipeline for skill quality scoring
- Prompt versioning system for Hermes brain updates

## Comparison to Existing
- More production-grade than xmaks82/self-improving-agent (uses Inngest for durability)
- Guardrails against gaming — sophisticated approach
- Versioned prompt improvements with attribution

## Verdict
**FORGE** — Key architecture for Hermes self-evolution. Fork, study, integrate patterns.

## Action Taken
Already cloned in workspace.