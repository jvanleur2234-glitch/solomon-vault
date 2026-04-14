# RD Report: Netflix Metaflow

**URL:** https://github.com/Netflix/metaflow
**Stars:** 10k+ | **License:** Apache 2.0 | **Language:** Python (93%)
**Date:** 2026-04-14

---

## What It Is

Metaflow is a human-centric ML/AI framework originally built at Netflix (3000+ projects internally) and now backed by Outerbounds. It handles the full lifecycle: local prototyping → scaling to cloud (CPU/GPU) → production deployment via Argo Workflows, AWS Step Functions, etc.

Key capabilities:
- Pythonic decorator-based flow definition (`@step`, `@catch`, `@retry`)
- Built-in experiment tracking, data versioning, artifact management
- Parallel/foreach execution, distributed computing support
- Cloud-native: AWS Batch, Kubernetes/Argo, Google Cloud, Azure
- 252 releases, 1,557 commits, active maintenance

## What We'd Use It For

**Solomon OS / Hermes skill pipeline** — Metaflow could orchestrate complex multi-step AI tasks (research → write → publish) with built-in retry, checkpointing, and artifact passing between steps. Cleaner than hand-rolled bash scripts.

**AI staffing agency job processing** — When a client request comes in, a Metaflow pipeline could route → research → draft → review → deliver with full audit trail.

**ML model management** — For any future AI product involving models (faceless YouTube, etc.), Metaflow handles the boring infrastructure stuff.

## How It Compares to What We Have

| | Metaflow | Our current approach |
|---|---|---|
| Job orchestration | First-class `@step` flows, foreach, retries | Shell scripts + bus.sh |
| Data/artifacts | Built-in artifact passing between steps | Manual file passing |
| Scaling | Native cloud compute (AWS, K8s) | Single-machine |
| Monitoring | Built-in UI + logging | Logs + manual |
| Learning curve | Medium (Python decorators) | Already using Python scripts |

Metaflow is production-grade infrastructure for teams. We're running a lean solo op — it's probably overkill for current scale, but could replace Solomon Bus + manual orchestration scripts if we ever need reliability at scale.

## Recommendation: SKIP (for now)

Metaflow is a serious enterprise tool (Amazon, Goldman Sachs use it). It's overkill for Solomon OS at current scale. We'd need cloud infrastructure (AWS/K8s) to get real value, plus a team to maintain it.

**Watch list:** If Hermes grows to need multi-step pipelines with checkpointing, retry logic, and artifact management across cloud infrastructure — revisit. The `metaflow.Retry` and `metaflow. Catch` decorators alone would replace a lot of our error-handling boilerplate.

**Fork candidate:** Low priority. Not building ML infrastructure right now.
