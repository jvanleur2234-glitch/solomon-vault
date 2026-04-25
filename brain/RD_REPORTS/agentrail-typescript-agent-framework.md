# Agentrail — TypeScript Production Agent Framework

**Fork:** `yai-dev/agentrail` → already in workspace (not yet forked to GitHub)
**Source:** https://github.com/yai-dev/agentrail (Apache-2.0)
**Date:** 2026-04-25

---

## What It Does

Agentrail is a TypeScript-based framework for building, hosting, and orchestrating tool-using AI agents. It provides:
- Full runtime core (@agentrail/core): agent definition, execution loop, tool contracts, session types
- Capabilities package: sandbox, knowledge, skills, orchestration, browser automation
- Hosted server layer with profiles and plugins
- Multi-agent delegation with mailboxing and failure recovery
- Memory and knowledge indexing with retrieval
- Pluggable LLM providers (Anthropic, OpenAI, etc.)

## Key Components

- `@agentrail/core` — Agent definition, execution loop, tool contracts, LLM providers
- `@agentrail/capabilities` — Sandbox, knowledge, skills, orchestration, browser automation
- `@agentrail/app` — Hosted request lifecycle, profiles, session management, plugins
- `@agentrail/deep-research` — Deep research workflow addon

## Solomon OS Fit

**INTEGRATE** — TypeScript framework with production-grade architecture. Key patterns:
- Multi-agent delegation with failure recovery = resilience for Hermes
- Sandbox execution = security isolation
- Plugin extension model = maps to Hermes skills ecosystem
- Memory/knowledge indexing = fits gbrain pattern
- Apache-2.0 license permits code reference

## Status

**INTEGRATE** — study sandbox architecture and failure recovery patterns for Hermes resilience layer.