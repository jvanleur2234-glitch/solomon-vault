# RD Report: Paperclip Company Generator

**Date:** 2026-04-20
**Source:** [X @aronprins](https://x.com/aronprins/status/2046269070643757221) + GitHub
**Task:** paperclip-company-gen-001

## What It Is

**Paperclip Company Generator** by Aron Prins (@aronprins) — a skill for Claude/Codex that generates fully customizable AI agent "companies" from a business type + URL + 30-day goal. Built on top of Paperclip (MIT, 13.5K GitHub stars).

**Paperclip itself:** Node.js backend + React dashboard for orchestrating multiple AI agents (Claude, Codex, OpenClaw) into structured teams with budgets, org charts, goals, and auditable work logs.

**The Company Generator:** One-prompt → generate an entire custom AI company tailored to your business, ready to import and run.

## Key Features

- **One-prompt setup:** Business type + URL + goal → full AI company
- **Multiple agent types:** Coordinates Claude, Codex, OpenClaw agents together
- **Built-in structure:** Budgets, org charts, goal alignment enforced
- **Full auditability:** Every action logged, costs tracked per agent
- **24/7 autonomous operation:** Agents work while you sleep
- **Desktop app available:** Paperclip Desktop (Mac, one-click install)

## Why It Matters for Solomon OS / JCPaid

**Direct overlap with JackConnect + Hermes.** We have:
- JackConnect (job queue + client portal) ✅
- Hermes (agent orchestration) ✅
- Skills registry ✅
- Job runner daemon ✅

What we DON'T have yet:
- Structured agent COMPANY templates per service type
- Budget tracking per worker
- Org chart per client

**Paperclip Company Generator = exactly the template system we need.** When a client signs up for SEO Audit service, we generate an SEO Company with:
- 1 lead researcher agent
- 1 content optimizer agent  
- 1 report generator agent
- Shared budget, shared goal
- All reporting to JackConnect dashboard

## Business Model Fit

| Paperclip | JackConnect |
|-----------|-------------|
| Agent teams | AI workers (SEO, Lead Gen, Cold Email) |
| Company templates | Service type templates |
| Budget tracking | Job pricing + margin tracking |
| Org charts | Worker assignment |
| Audit logs | Client reports |

## Recommendation

**INTEGRATE (HIGH PRIORITY)**

Fork the Paperclip Company Generator concept for JackConnect. When client submits a job, Hermes generates a mini "company" of agents to execute it.

Clone: `/home/workspace/paperclip/`
Read: `paperclip-desktop` GitHub + `paperclip` core repo

Action: Reach out to Aron Prins as tester, get early access to the Company Generator, study how it generates companies so we can build the same into JackConnect/Hermes.

## Link Fit

★★★★★ — #agent-orchestration #company-generator #hermes #jackconnect #solomon-bus

*Last updated: 2026-04-20*