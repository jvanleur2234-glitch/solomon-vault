# Quorum — Multi-AI Deliberation Framework

**Source:** https://github.com/Solvely-Colin/Quorum  
**License:** MIT  
**Stars:** ~900+  
**Date:** 2026-04-23

## What it does
Quorum is a multi-AI deliberation framework (TypeScript) that coordinates debates among multiple AI providers to produce a synthesized, consensus-driven answer with confidence scoring. It runs a 7-phase process (Gather, Plan, Formulate, Debate, Adjust, Rebuttal, Vote) across configured providers, then merges the runner-up into a final answer and optional minority report.

Key features:
- Adaptive debate, evidence/citation protocol, code review support
- CI/CD integration, policy guardrails, deterministic replay for auditability
- Human-in-the-loop controls
- Providers: OpenAI, Anthropic Claude, Google Gemini, Kimi, DeepSeek, Mistral, Groq, Ollama
- Auto-detects providers from environment variables
- MIT licensed, written in TypeScript

## Solomon OS Fit
**SKILL** — Deliberation/agent council pattern. Could enhance Hermes with multi-agent debate for complex decisions. MIT license permits direct use. The 7-phase debate process maps to our "Council of Experts" concept in Business Ideas.

## Key Components
- 7-phase deliberation process
- Provider router with multi-model support
- Evidence/citation tracking
- CI/CD integration hooks
- Policy guardrails

## Recommendation
SKILL — Study the 7-phase process for implementing a "Council" mode in Hermes. MIT license enables direct use.