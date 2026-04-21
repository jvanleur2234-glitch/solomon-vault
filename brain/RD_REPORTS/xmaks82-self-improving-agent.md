# RD Report: xmaks82/self-improving-agent

**Date:** 2026-04-21  
**Slug:** xmaks82-self-improving-agent  
**Category:** Self-Improving Agent  
**License:** MIT  
**Stars:** Not tracked  
**Language:** Python 3.12+  

## What It Is
A 16-agent multi-agent system that permanently evolves itself by learning from user feedback. Upgrades system prompts across versions (v1 → v2 → v3…) so subsequent responses leverage an improved "brain."

## Key Features
- Feedback loop: user input → FeedbackDetector → AnalyzerAgent → VersionerAgent → new prompt version
- 16 interconnected agents: MainAgent, AnalyzerAgent, VersionerAgent, 5 sub-agents, VerificationAgent, ExploreAgent, PlanAgent, ForkManager, AgentOrchestrator
- Verification workflow with auto-triggered testing (PASS/FAIL/PARTIAL)
- 6 free LLM providers + Claude via OAuth (Groq, SambaNova, Cerebras, OpenRouter, Zhipu, Anthropics)
- 13 core tools with 4-layer Bash security
- Read-Before-Edit policy, permission system, Secret Scanner

## Relevance to Solomon OS
- **Direct match:** Self-improvement loop concept directly applicable to Hermes evolution
- **Fork priority:** HIGH — the feedback-driven prompt evolution system is exactly what Solomon OS needs for continuous improvement
- **Integration:** Could be the "self-correction" layer for Hermes Agent

## Verdict
**FORGE** — MIT licensed, directly relevant to self-improvement goals, novel architecture. Fork immediately.

## Priority
🔴 Critical