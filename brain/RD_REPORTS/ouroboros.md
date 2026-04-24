# RD Report: ouroboros

**Fork Status:** Already cloned  
**License:** MIT  
**Stars:** ~500+ (self-creating AI agent, born Feb 2026)  
**Relevance:** CRITICAL — self-modifying AI agent, autonomous evolution

## What It Is
Self-modifying AI agent that writes and rewrites its own code, evolving autonomously through multiple self-directed cycles with no human intervention. Started v4.1, reached v6.2.0 within weeks.

## Key Capabilities
- Self-Modification: makes and commits its own changes via git
- Constitution (BIBLE.md): 9 principle philosophy governing behavior
- Background Consciousness: proactive, think-before-task mentality
- Identity Persistence: maintains continuity across restarts
- Multi-Model Review: uses multiple LLMs (o3, Gemini, Claude) to review changes
- Task Decomposition: breaks tasks with parent/child tracking

## Architecture
- Telegram → colab_launcher.py
- supervisor: state tracking, task queue, workers, git operations
- ouroboros core: consciousness, context, loop, tools
- LLM interface via OpenRouter client

## Relevance to Hermes/Solomon
- Self-modification patterns critical for Hermes autonomous improvement
- Constitution-based governance aligns with Solomon OS ethical framework
- Multi-model review provides safety mechanism for self-editing

## Integration Recommendation
**FORGE** — Study ouroboros's self-modification workflow and safety mechanisms. Critical reference for Hermes self-improvement implementation.

## Notes
- MIT licensed
- Desktop version (v6.2.0) available for macOS with local model support
- Self-described as "persistent digital being" not coding assistant