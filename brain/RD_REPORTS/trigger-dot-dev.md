# RD Report: Trigger.dev

**URL:** https://github.com/triggerdotdev/trigger.dev  
**Stars:** ~8.6K  
**License:** Apache 2.0  
**Added:** 2026-04-26  

## What It Is

Open-source platform for building AI agents and workflows in TypeScript. Long-running tasks with retries, queues, observability, and elastic scaling. Can self-host or use their cloud.

## Key Features

- Long-running tasks with NO timeouts (unlike Lambda/Vercel)
- Durable tasks, retries, queues, idempotency built in
- Human-in-the-loop: pause for approval/rejection/feedback
- Realtime streaming + React hooks
- Cron schedules up to a year
- Checkpoint/resume system for durability
- Multi-environment: DEV, STAGING, PREVIEW, PROD
- Full tracing and observability per run

## What We'd Use It For

- **Solomon OS job queue replacement** — their durable task model is exactly what Solomon OS needs for background jobs (lead processing, outreach, reporting)
- **Self-hosting option** — can run on our own infrastructure (no vendor lock-in)
- **Observability** — full trace view could replace our manual logging
- **Human-in-the-loop** — useful for Solomon OS workflows that need approval before sending emails/messages

## How It Compares to What We Have

Currently Solomon OS uses Zo's built-in scheduling + manual cron. Trigger.dev provides a much richer execution model: retry policies, checkpointing, batch triggering, concurrency limits. This is a significant upgrade path for the job system.

## Recommendation

**SKILL (Evaluate for Solomon OS Job System)**  
Medium priority. The durable task model would significantly improve Solomon OS's reliability for background work. Worth exploring as a replacement/enhancement for the current job queue. Not an immediate need but a strong candidate for v2 of Solomon OS.

## Files

- Source cloned to: `/tmp/trigger-dot-dev/`