# RD Report: DeepSwarm — 96-Worker Parallel Batch Processing

**Date:** 2026-05-04
**Source:** x.com/mr_r0b0t/status/2051110921502622005 + github.com/amanning3390/deepswarm
**Priority:** 🔴 CRITICAL — FORGE IMMEDIATELY

## What It Is

DeepSwarm is a Hermes skill that orchestrates N parallel API workers for any batch task. Built from the DeepSeek Hermes Reasoning Traces dataset (19,331 traces, 192K tool calls).

**Numbers:**
- 96 workers · 31K API calls · 527M tokens · $100 total
- 99.95% success rate
- 28K views, 304 likes, 391 bookmarks — dropped TODAY May 4

## Core Architecture

**Tiered Delegation:**
```
Orchestrator (DeepSeek V4-Pro) → Plans the batch task
Workers (DeepSeek V4-Flash)   → Execute in parallel
```

V4-Pro = few calls, high quality. V4-Flash = many calls, 3× cheaper.

**Auto-Optimization (the magic formula):**
| Call Duration | Workers | Stagger | Success | Throughput |
|--------------|---------|---------|---------|------------|
| <10s | 16 | 1s | 99.9% | ~5,760/hr |
| 10-30s | 12 | 2s | 99.9% | ~1,440/hr |
| 30-60s | 8 | 5s | 99.95% | ~440/hr |
| 60-90s | 6 | 10s | 99.9% | ~240/hr |

**8 workers + 5s stagger** = proven sweet spot for complex tasks.

## JCPaid Application

This is the BATCH LAYER we were missing.

Current JCPaid = one client = one agent at a time.
With DeepSwarm = 96 clients simultaneously per server.

**Business model shift:**
- 1 server × 96 workers = 96 concurrent clients
- Each client pays $299/mo
- $299 × 96 = $28,704/mo per server
- Cost at $100/527M tokens = ~$0.19/client/mo in AI costs
- Margin: $28K/mo revenue vs ~$18/mo AI costs

**What we can now offer:**
• "Run 100 SEO audits overnight" — batch parallel processing
• "Analyze 1,000 leads from your CRM" — one-shot batch
• "Process all your emails" — parallel per-client workers
• "Generate 10,000 personalized follow-ups" — tiered delegation

## Install

```bash
hermes skills tap add amanning3390/deepswarm
```

## Files

- `/home/workspace/deepswarm/` — cloned
- SKILL.md, scripts/swarm.py, scripts/worker.py, task.yaml

## Recommendation

FORGE IMMEDIATELY. This is the parallel processing engine for JCPaid's multi-tenant architecture. Install the skill, test against one batch task, then build the multi-client wrapper.

---

*Last updated: 2026-05-04*