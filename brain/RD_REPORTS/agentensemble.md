# RD Report: AgentEnsemble

**Date:** 2026-04-24  
**Slug:** agentensemble  
**Tags:** #multi-agent #orchestration #jvm #langchain4j #production  

## What It Is
Java 21 framework for orchestrating teams of AI agents built on LangChain4j. Provides production-grade multi-agent orchestration with HIERARCHICAL, SEQUENTIAL, PARALLEL, and MapReduce workflow strategies.

## Relevance to Solomon OS / Hermes
- **JVM ecosystem** — complementary to Python-based agent frameworks
- **Production observability** — token counts, latency, tool timing traces
- **Multi-agent orchestration** — directly competitive with Council of High Intelligence
- **Type-safe outputs** — aligns with Hermes's output validation patterns

## License
MIT

## Stars
~screenshot needed — active Java project

## Key Capabilities
- HIERARCHICAL, SEQUENTIAL, PARALLEL, MapReduce orchestration strategies
- Memory management across runs
- Human-in-the-loop review gates
- Input/output guardrails, automatic retry and delegation safeguards
- Token counts, LLM latency, tool timing, execution traces
- Typed outputs via outputType() with automatic correction prompts
- SLF4J logging, Micrometer metrics
- Live dashboard (no Docker required)

## Competitive Position
JVM-native alternative to Python agent frameworks. Direct competitor to Council of High Intelligence (Quorum), agent-debate (gumbel-ai), and dialectic-agentic. More production-focused with built-in observability.

## Recommendation
**FORGE** — JVM ecosystem gap in Solomon OS. Fork for research and potential integration with Hermes JVM bridge.

## Links
- https://github.com/AgentEnsemble/agentensemble
- https://github.com/jvanleur2234-glitch/agentensemble (fork)