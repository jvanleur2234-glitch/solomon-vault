# agentrail — TypeScript Agent Harness Framework

**URL:** https://github.com/jvanleur2234-glitch/agentrail
**Forked from:** https://github.com/yai-dev/agentrail
**License:** Apache-2.0 | **Stars:** ~200+ | **Language:** TypeScript

## What It Does
Open-source agent harness framework for building, hosting, and orchestrating tool-using AI agents. Composable runtime core, hosted server layer, prompt SDK, multi-agent orchestration, filesystem-backed memory, sandboxed execution.

## Key Features
- `@agentrail/core`: agent definition, execution loop, tool contracts, prompt SDK, session types
- `@agentrail/capabilities`: sandbox, knowledge, skills, orchestration, browser automation
- `@agentrail/app`: hosted request lifecycle, profiles, session management, plugins
- `@agentrail/deep-research`: deep research workflow addon
- Multi-agent delegation with mailboxing, structured waits, failure recovery
- Session memory + knowledge-base indexing + retrieval
- Docker sandbox isolation for safe LLM-generated code execution
- pnpm workspace, TypeScript ESM, Vitest testing

## Solomon OS Fit
**SKILL** — agentrail's sandbox isolation + multi-agent delegation patterns are directly relevant. The deep-research workflow is a good reference for Hermes research agents. Apache-2.0 license allows studying and adapting.

## Recommendation
SKILL — Study sandbox isolation architecture and multi-agent delegation for Solomon OS.