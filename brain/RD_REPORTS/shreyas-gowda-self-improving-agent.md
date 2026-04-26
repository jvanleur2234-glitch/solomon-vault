# Shreyas-Gowda26 Self-Improving Agent

**Date:** 2026-04-26  
**Slug:** shreyas-gowda-self-improving-agent  
**Category:** Self-Improvement  
**License:** MIT  
**Language:** Python  
**Forked:** No

## What it is
Python self-improving agent that permanently evolves its own system prompt based on user feedback. Each interaction can trigger an improved prompt version (v1, v2, v3...). Multiple free LLM providers (Groq, SambaNova, Cerebras, Zhipu, Anthropic). Sub-agents: CodeReviewer, TestWriter, Debugger, Researcher, Refactorer.

## Key Features
- **Permanent prompt evolution**: user feedback → new versioned prompts
- **Free LLM providers**: Groq (recommended), SambaNova, Cerebras, Zhipu, Anthropic
- **5 sub-agents**: specialized for different tasks
- **MCP integration**: external tools/contexts
- **11 built-in tools**: filesystem, git, shell, search, web fetch
- **Human-in-the-loop**: diff previews, confirmations, dry runs, undo/redo
- **Offline-capable**: designed for free providers
- **Context window compaction** for long sessions

## Relevance to Solomon OS / Hermes
Self-improving prompt version system is directly applicable to Hermes. Sub-agent architecture (CodeReviewer, etc.) maps to Hermes skill system. Free provider support is excellent for cost efficiency.

## Verdict
**FORGE** — Fork and adapt as Hermes self-improvement skill. MIT licensed, free providers, versioned prompt evolution. The sub-agent architecture maps well to Hermes skills.