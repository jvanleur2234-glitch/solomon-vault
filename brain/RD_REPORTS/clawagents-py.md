# RD Report: x1jiang/clawagents_py

**Date:** April 26, 2026  
**Author:** AIQ Scout  
**Status:** SKILL  
**License:** MIT  
**Stars:** ~2.5K LOC (no star count but production-ready)  

## What It Is
Python agent framework giving LLMs ability to read, write, execute code. Built-in planning, memory, sandboxing, gateway server. Pluggable LLM providers (OpenAI GPT-5, Gemini, Claude, Ollama, vLLM, Bedrock).

## Key Features
- Provider architecture for multi-LLM support
- Memory + sandboxing for safe code execution
- Gateway server for orchestration
- Minimal ~100 line agent creation
- CLI: `clawagents --task "..."`

## Solomon OS Fit
STUDY — Provider abstraction pattern useful for Hermes multi-model routing. Sandbox + gateway architecture could inform Solomon Bus design.

## Action
- Already in workspace as clawagents_py
- No fork needed (already have it)
- Study provider architecture for Hermes multi-provider support

## Links
- https://github.com/x1jiang/clawagents_py