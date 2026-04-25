# Sentient GRID — Reproducible AI Runs Infrastructure

**Fork:** N/A  
**License:** N/A (not cloned)  
**Stars:** ~8K (Sentient ecosystem)  
**Date:** 2026-04-25

## What It Is

Sentient's execution layer that turns user queries into **reproducible pipelines** — not one-off chats. Each run has a plan, clear roles, data boundaries, and full audit trace.

## Key Concepts

- **ROMA Planner:** High-level goal → ordered steps with dependencies
- **ODS Engine:** Separates retrieval from reasoning; citations survive aggregation
- **Tool Orchestration:** Models, RAG, search, scrapers, micro-benchmarks, code as modular DAG nodes
- **Spaces:** Focused workrooms storing inputs, intermediate states, outputs, full trace
- **Per-step policies:** Data boundaries, what leaves perimeter vs stays local
- **Artifacts:** Named outputs tied to inputs, sources, version hashes

## Pipeline Examples

```
Research brief: gather sources → extract claims → reconcile facts → source-linked memo
On-chain trace: ingest events → label hops/risks → risk summary with links
Product decision: compare configs → run micro-benchmarks → decision memo with trade-offs
```

## Roles

- **Lead:** defines goal + acceptance criteria
- **Agents:** repeatable steps (collect, convert, benchmark, format)
- **Reviewers:** sign artifact or return with fix list

## Solomon OS Fit

**REFERENCE / SKILL** — The reproducible run concept with per-step provenance is exactly what Solomon OS business agents need for auditable client work. The GRID's token-level routing + modular DAG for agents maps to Solomon Bus task orchestration. Strong competitor to consider.

## Verdict

**SKILL** — Study the reproducibility + audit trail architecture. Key pattern for enterprise AI agent deployments.
