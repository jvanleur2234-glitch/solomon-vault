# RD Report: agent_council — GPT-5.1 Multi-Agent Council

**Fork:** https://github.com/jvanleur2234-glitch/agent_council
**Source:** https://github.com/ma-serra/agent_council
**License:** MIT
**Language:** Python (backend) + React/TypeScript (web UI)
**Stars:** ~200

## What It Is
5-step modular framework for creating councils of specialized AI agents (GPT-5.1). Ingest (files/PDF) → Build (Architect Agent proposes council) → Edit (interactive refinement) → Execute (parallel) → Review (peer + chairman synthesis). Real-time token/cost tracking. Web UI + CLI.

## Key Features
- **5-step workflow:** ingest → build → edit → execute → review
- **Architect Agent:** proposes diverse council of experts
- **Interactive refinement:** add/remove/edit agents before execution
- **GPT-5.1 reasoning effort:** none, low, medium, high
- **Cost & token tracking:** real-time monitoring
- **Multi-user web UI:** session isolation, shareable URLs, intelligent caching
- **File ingestion:** PDF, DOCX, TXT, MD, JSON, PY, CSV

## Solomon OS Fit
**SKILL** — Architect Agent → diverse council pattern applicable to skill validation. MIT license.

## Comparison to Existing
- More interactive (edit step before execution) than llmcouncil or multi-agent-council
- Web UI is more polished than council-ai (doronpers)
- Better file ingestion for research tasks

## Action
Forked. Architect Agent concept for dynamic council composition.

**Recommendation:** SKILL — study interactive council refinement for Hermes skill validation workflow