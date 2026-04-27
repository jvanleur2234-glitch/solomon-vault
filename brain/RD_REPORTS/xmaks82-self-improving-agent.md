# RD Report: xmaks82/self-improving-agent

**Date:** April 26, 2026  
**Fork:** Check workspace  
**License:** MIT  
**Language:** Python  

## What It Is
Self-improving multi-agent system that permanently evolves from user feedback. 16 interconnected agents in a pipeline. System prompts versioned (v1 → v2 → v3) based on continuous feedback.

## Architecture (16 agents)
- MainAgent, AnalyzerAgent, VersionerAgent
- 5 sub-agents: CodeReviewer, TestWriter, Debugger, Researcher, Refactorer
- VerificationAgent, ExploreAgent, PlanAgent
- ForkManager, AgentOrchestrator
- SessionMemory, ContextCompactor, FeedbackDetector

## Core Loop
1. User feedback triggers FeedbackDetector
2. Analyzer analyzes logs and hypotheses
3. Versioner creates improved system prompt
4. New prompt version saved and used

## Key Features
- **6 free LLM providers:** Groq, SambaNova, Cerebras, OpenRouter, Zhipu, Anthropic
- **13 core tools:** Filesystem, git, shell, search, web
- **6-layer Bash security:** Read-before-edit discipline
- **Secret scanner:** Detects credentials before sharing

## Solomon OS Fit
**SKILL** — 16-agent pipeline architecture is ambitious. The VersionerAgent (creates improved system prompt) is exactly what our Hermes evolution loop needs. Free LLM providers means it can run without expensive API keys.

## Unique Value
- Permanent prompt evolution (v1 → v2 → v3)
- 16 interconnected agents show complex orchestration
- Secret scanner for security

## Action
Clone. Write RD report. Study VersionerAgent for Hermes evolution loop.