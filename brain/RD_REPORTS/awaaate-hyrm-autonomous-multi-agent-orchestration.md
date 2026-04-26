# awaaate/Hyrm — Autonomous Multi-Agent Orchestration with OpenCode (NOASSERTION)

## Quick Summary
Experimental autonomous multi-agent AI orchestration system built on OpenCode. Runs a persistent orchestrator that coordinates specialized worker agents (code, memory, analysis) with persistent memory across sessions for self-improvement.

## What It Does
- **Persistent orchestrator**: coordinates and delegates to workers
- **Specialized workers**: Code Worker, Memory Worker, Analysis Worker
- **Persistent memory**: JSON/JSONL storage across sessions
- **Closed-loop self-improvement**: observe → identify → create tasks → implement
- **Automated quality assessment and metrics tracking**
- **Watchdog**: keeps orchestrator running
- **Plugin**: OpenCode-based tools for coordination, memory, tasks

## Architecture
- Orchestrator (persistent agent) → coordinates → delegates to workers
- Parallel worker execution with centralized state and communication
- Real-time monitoring tools and CLI

## Relevance to Solomon OS
- **SKILL** — Study persistent orchestrator pattern for Hermes. Closed-loop self-improvement aligns with Hermes evolution.
- Memory Worker concept could inform Hermes memory management

## License & Status
- **License:** NOASSERTION (treat as not business-friendly)
- **Already cloned:** /home/workspace/Hyrm
- **Repo:** https://github.com/awaaate/Hyrm

## Verdict
**SKILL** — Study the persistent orchestrator + worker pattern. License is ambiguous (NOASSERTION) so do not integrate into commercial products without legal review.
