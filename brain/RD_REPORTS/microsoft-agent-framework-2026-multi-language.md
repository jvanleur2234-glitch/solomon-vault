# microsoft/agent-framework — Multi-Language Agent Framework (9,700+ stars, MIT)

## Quick Summary
Microsoft's production-grade multi-language (Python + .NET/C#) framework for building, orchestrating, and deploying AI agents with graph-based orchestration, streaming, checkpointing, human-in-the-loop, and time-travel capabilities.

## What It Does
- **Graph-based workflows** connecting agents and deterministic functions
- **Multi-language**: Python and .NET with consistent APIs
- **AF Labs**: experimental features (benchmarking, RL, research)
- **DevUI**: interactive UI for developing, testing, debugging workflows
- **Long-running agents**: ContinuationToken for background responses
- **Streaming support**: code interpreter deltas
- **Session management**: CreateSession, session resumption

## Key Components
- agent-framework-core: long-running agents, streaming, session/context providers
- agent-framework-purview: data ownership
- Declarative workflows with ChatMessage conversion
- MCP integration support

## Relevance to Solomon OS
- **SKILL** — Study graph-based orchestration for Hermes skill workflows
- Multi-language parity is relevant for Solomon OS cross-stack
- Time-travel/debugging features are relevant for Hermes mission tracking
- DevUI pattern worth studying for Hermes management UI

## License & Status
- **License:** MIT
- **Stars:** ~9,700
- **Already cloned:** /home/workspace/microsoft-agent-framework
- **Repo:** https://github.com/microsoft/agent-framework

## Verdict
**SKILL** — Major framework, worth deep study. Graph-based orchestration, session management, and DevUI patterns are directly applicable to Hermes. High stars, MIT license, actively maintained.
