# RD Report: microsoft/agent-framework

**Forked:** https://github.com/jvanleur2234-glitch/microsoft-agent-framework  
**Stars:** ~9.7k  
**License:** MIT  
**Language:** Python (50%), C# (46%)

## What It Is
Microsoft's official multi-language (Python/.NET) agent framework with graph-based orchestration, streaming, checkpointing, human-in-the-loop, and time-travel capabilities. Supports both .NET and Python with consistent APIs.

## Relevance to Solomon OS
- **Hermes competitor**: Graph-based workflow orchestration directly competes with Hermes skills
- **Multi-provider support**: Could integrate as a cross-platform orchestration layer
- **Observability**: Built-in OpenTelemetry aligns with Solomon OS monitoring needs

## Key Features
- Graph-based workflows linking agents + deterministic functions
- AF Labs for experimental features (RL, benchmarking)
- DevUI for interactive agent development/testing
- Middleware system for request/response processing
- Migration guides from Semantic Kernel and AutoGen

## Comparison to What We Have
| Feature | Microsoft | Hermes |
|---------|-----------|--------|
| Multi-language | ✅ Python + C# | Python only |
| Graph orchestration | ✅ | ❌ |
| Time-travel debugging | ✅ | ❌ |
| DevUI | ✅ | ❌ |
| Microsoft Foundry | ✅ | ❌ |

## Verdict
**FORGE** — Major competitor to Hermes. Fork for reference architecture. Watch for Microsoft integration opportunities (Azure Foundry, Copilot stack). Graph-based orchestration is a gap in current Hermes design.
