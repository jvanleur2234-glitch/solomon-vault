# RD Report: self_improving_coding_agent

**Date:** 2026-04-23  
**URL:** https://github.com/MaximeRobeyns/self_improving_coding_agent  
**Fork:** `jvanleur2234-glitch/self_improving_coding_agent` (already forked)  
**License:** MIT  

## What It Does
Coding agent that iteratively improves its own codebase. Evaluates current version on benchmark tasks → archives results → runs on own codebase to produce improvements → repeat. Docker-isolated execution. Multiple LLM provider support.

## Core Loop
1. Evaluate agent on benchmark tasks (swebench)
2. Archive results
3. Run agent on own codebase → improvement
4. Repeat from step 1

## Architecture
- `base_agent/` — core agent code
- `swebench/` — benchmark evaluation
- Web UI at http://localhost:8080 (event bus + callgraph visualization)
- Multi-provider: Anthropic, OpenAI, Gemini, Vertex, Fireworks, DeepSeek, Modal

## Solomon OS Fit
**FORGE** — Self-improvement loop architecture (evaluate → archive → improve → repeat) directly implementable in Hermes. MIT license permits code use. Docker isolation pattern for safe self-editing.

## Status
**FORGE** — Core self-improvement loop pattern for Hermes autonomous capability growth.
