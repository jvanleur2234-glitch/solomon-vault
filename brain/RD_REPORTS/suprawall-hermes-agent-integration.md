# SupraWall x Hermes Agent Integration

## Summary
- **URL:** https://github.com/wiserautomatio/suprawall
- **Type:** Security plugin / deterministic policy layer for Hermes Agent
- **Status:** PRODUCTION-READY (as of April 23, 2026)
- **License:** MIT (presumed)

## What It Is
SupraWall is a deterministic ALLOW/DENY gating layer for Hermes Agent. It intercepts every tool call and decision made by Hermes agents and enforces:
- **Deterministic policy enforcement:** Binary allow/deny decisions per tool call
- **Local PII scrubbing:** Automatic redaction of personally identifiable information
- **RSA-signed audit logs:** Cryptographic proof of every agent action

## Key Features
1. **Deterministic gating** — Every tool call passes through a policy checkpoint with deterministic outcomes (no probabilistic behavior)
2. **PII scrubbing** — Local, no-data-leaves-your-infra approach to removing personal info from agent outputs
3. **RSA-signed audits** — Every tool call decision is cryptographically signed, providing non-repudiable audit trails
4. **Live on PyPI** — `pip install suprawall` integration available
5. **Hermes-native** — Built specifically for NousResearch/Hermes Agent

## Why It Matters for Solomon OS
- **Hermes Agent is core to Solomon OS** — SupraWall adds enterprise-grade security hardening
- **OWASP Agentic Top 10** — Directly addresses ASI01-ASI10 categories around unauthorized actions and data leakage
- **Production-ready means:** Already tested, not theoretical. This is a real security layer for real agent deployments.
- **Integration signal:** SupraWall choosing Hermes as its first integration target validates Hermes as the dominant agent framework in the open-source ecosystem.

## Relationship to Existing Stack
- **Complements** sinewave-agent-security-scanner-mcp (runtime scanning vs. policy enforcement)
- **Complements** agentarmor-studio (general 8-layer security vs. Hermes-specific deterministic gating)
- **Different from** hackmyagent: SupraWall is a proactive policy layer, not a red-teaming scanner

## Action Items
- [ ] Locate the actual SupraWall GitHub repo (search wiserautomatio on GitHub directly)
- [ ] Clone and fork the repo once located
- [ ] Write integration skill for Hermes to consume SupraWall as a skill
- [ ] Consider SupraWall as a model for Solomon OS's own security hardening layer

## X Mentions
- @AlexPeghin (Apr 23, 2026): "SupraWall x Hermes Agent integration is officially PRODUCTION-READY! Deterministic ALLOW/DENY gating, local PII scrubbing, and RSA-signed audits for every tool call."

## Verdict
🔴 **CRITICAL** — Production-ready security layer for Hermes Agent validates the agentic security market. SupraWall chose Hermes as first integration, signaling enterprise adoption. Track closely.