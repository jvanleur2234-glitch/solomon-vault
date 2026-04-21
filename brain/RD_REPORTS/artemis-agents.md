# ArtemIS Agents — Structured Multi-Agent Debate Framework

**Fork**: `bassrehab/artemis-agents` → no existing fork
**License**: MIT
**Stars**: New
**Language**: Python

## What It Is

Framework for structured multi-agent debates with adaptive evaluation, causal analysis, and safety monitoring. Built with hierarchical argument generation (H-L-DAG) and a jury scoring mechanism.

## Key Features

- **Multi-agent debate**: N agents, real-time streaming, metacognitive safety
- **Hierarchical argument generation**: H-L-DAG structure
- **Dynamic adaptive evaluation**: L-AE-CR (causal reasoning)
- **Jury scoring**: Built-in ethical alignment
- **Sandbagging detection**: Real-time safety checks for deception
- **Multimodal evidence**: Handling in v2 stack
- **API**: Simple Python API for setting up debates with agents, jury panel, topics, rounds

## Relevance to Council of High Intelligence

- **Direct competitor**: ArtemIS has structured debate + jury scoring + ethical alignment
- **Different angle**: Hierarchical argument generation vs. simple consensus mechanisms
- **Use case**: Could be integrated as the "deliberation engine" for Solomon OS decision-making

## Verdict

🟡 SKILL — Clone and study the debate/jury scoring architecture. Could inform how Solomon OS agents reach consensus on high-stakes decisions.

**Action**: Look at `src/` structure and jury.py for scoring implementation.