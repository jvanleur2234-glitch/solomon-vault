# RD Report: agentrail

**Fork Status:** Already forked  
**License:** Apache-2.0  
**Stars:** Not immediately available (TypeScript agent framework)  
**Relevance:** HIGH — skill framework, multi-agent orchestration, sandboxed execution

## What It Is
TypeScript-based agent harness framework for building, hosting, and orchestrating tool-using AI agents. Full runtime core with hosted server layer, prompt SDK, multi-agent orchestration, memory, and Docker sandbox isolation.

## Key Capabilities
- Composable runtime core and prompt SDK
- Hosted request lifecycle with profiles, session management, plugins, events
- Multi-agent orchestration including mailboxing, structured waits, failure recovery
- Session memory, knowledge indexing, retrieval
- Docker sandbox isolation for safe, isolated code execution
- Pluggable LLM providers (Anthropic, OpenAI, etc.)

## Packages
- `@agentrail/core`: agent definitions, execution loop, tool contracts
- `@agentrail/capabilities`: sandboxing, knowledge, skills, orchestration, browser automation
- `@agentrail/app`: hosted request lifecycle, profiles, session management
- `@agentrail/deep-research`: deep research workflow addon

## Relevance to Hermes/Solomon
- Strong overlap with Hermes's skill ecosystem and sandbox execution
- Could inform Hermes skill packaging and multi-agent coordination patterns
- Docker sandbox approach aligns with Solomon OS security requirements

## Integration Recommendation
**SKILL** — Study agentrail's sandbox implementation and skill packaging patterns. Could inform Hermes skill development tooling.

## Notes
- Pre-GA (public APIs may change)
- Roadmap at agentrail.run
- Apache-2.0 licensed