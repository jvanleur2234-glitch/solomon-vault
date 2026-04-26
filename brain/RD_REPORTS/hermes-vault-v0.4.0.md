# Hermes Vault v0.4.0 — AI Agent Observability Briefing

**Date:** 2026-04-25  
**Context:** Tony Simons gave AI agents "a pair of glasses" — observability built into the credential layer  
**Ecosystem:** Hermes Agent (NousResearch) + Hermes Vault (Tony Simons) + Hermes Katana (security layer)  
**Relevance:** Solomon OS runs on Hermes — this is directly applicable to our stack

---

## What is Hermes Vault v0.4.0?

A **local-first credential broker** for AI agents. Think 1Password, but designed specifically for AI agents to access secrets without those secrets ever being exposed to the LLM context, logs, or terminal output.

### Key Features

1. **Credential Health Tracking** — Knows which keys are stale, expiring, or about to break. Proactive alerting before something fails.
2. **Audit Logs + Verification Reports** — Full visibility into which agent accessed which secret, when, and why.
3. **Secrets Never Leave the Vault** — 1Password-style isolation. Agent gets a placeholder or proxy reference, never the raw secret.
4. **Cryptographic Audit Trail** — SHA-256 hash-chained action log. Tamper-evident, append-only, queryable.

---

## Broader Hermes Ecosystem

Hermes Vault sits inside a larger observability stack being built into Hermes Agent:

### Telemetry & Analytics (Issue #6642)
- Unified tracking of latency, cost, completion/failure rates
- Per-API-call latency, TTFT, tool-call latency, queue/wait time
- Machine-readable export (CLI + API)
- Session DB persistence with normalized telemetry rows

### Structured Session Tracing (Issue #6741)
- Start/end timestamps with duration
- Per-turn waterfall profiling: prompt assembly → model call → tool dispatch → persistence
- Stable trace IDs with parent-child relationships

### PII Redaction + Hermes Katana Security
- Auto-scrubs sensitive data before LLM context
- Katana: 7-layer defense (taint tracking, flow analysis, input scanner 30+ patterns, output scanner, policy engine, SHA-256 audit trail, HTTPS proxy)
- CaMeL-style byte-level taint tracking — every value tagged with origin

---

## Why This Matters for Solomon OS

Solomon OS runs on Hermes. If we're going to sell AI agents to clients, we need:

1. **Credential health** — clients don't want their agents breaking because a key expired
2. **Audit logs for compliance** — enterprise clients want to see what the agent did, when, and why
3. **Secrets isolation** — non-negotiable for serious deployments
4. **Tamper-evident logs** — prove what happened if something goes wrong

---

## Integration Opportunities

### Immediate
- Wire Hermes Vault into Solomon OS secrets management
- Credential health tracking → proactive expiring key alerts
- Audit logs → admin UI surface

### Medium-term
- Telemetry → usage tracking for billing
- Cryptographic audit trail → compliance reporting for regulated industries
- Katana policy engine → skill-scoped secret access

---

## Verdict

**FORGE** — directly applicable. Hermes Vault v0.4 is the observability layer we've been missing.

**Priority:** High. Credential health tracking alone is worth it — proactive alerting before keys break is a genuine selling point for clients.

---

## Links
- Hermes Vault: https://github.com/asimons81/hermes-vault
- Hermes Agent: https://github.com/NousResearch/hermes-agent
- Hermes Katana: https://github.com/claudlos/hermes-katana
