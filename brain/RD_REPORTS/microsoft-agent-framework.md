# RD Report: microsoft/agent-framework

## Summary
Microsoft's production-grade multi-language agent framework (Python + .NET/C#) for building, orchestrating, and deploying AI agents with graph-based workflows, streaming, checkpointing, human-in-the-loop, and time-travel capabilities.

## Key Details
- **License**: MIT
- **Language**: Python + C#/.NET
- **Stars**: ~9,500+ (active, large community)
- **Latest**: python-1.0.1 (April 2026)
- **Repo**: https://github.com/microsoft/agent-framework

## What It Does
- **Graph-based workflows**: Connect agents and deterministic functions with data flows including streaming, checkpointing, human-in-the-loop, and time-travel capabilities
- **Multi-language**: Consistent APIs across Python and .NET with full parity
- **DevUI**: Interactive developer UI for testing and debugging workflows
- **AF Labs**: Experimental packages for benchmarking, RL, and research
- **Observability**: Built-in OpenTelemetry integration for distributed tracing
- **Multiple LLM providers**: Azure Foundry, OpenAI, Anthropic, and more

## Relevance to Solomon OS / Hermes
- **Competitor to Hermes**: Microsoft Agent Framework is the most direct competitor to Hermes — enterprise-grade, multi-agent orchestration with graph-based workflows
- **Migration source**: Has migration guides FROM Semantic Kernel and AutoGen (meaning users are migrating TO it)
- **Forked by**: jvanleur2234-glitch/agent-framework

## Use Cases
- Enterprise agent orchestration with .NET preference
- Cross-language agent teams (Python + C#)
- Production-grade multi-agent workflows requiring DevUI debugging
- Human-in-the-loop workflow orchestration
- Agents requiring time-travel / checkpointing

## Competitive Position
- Direct competitor to NousResearch/hermes-agent in enterprise multi-agent space
- Microsoft backing = long-term viability and corporate adoption
- Graph-based workflow model similar to what Hermes Conductor aims to be
- AF Labs (RL + benchmarking) is a unique research angle

## Verdict
**FORGE** — Forked already. Watch for feature parity with Hermes and potential integration points (MCP tool output formatting, DevUI equivalents, AF Labs RL components).