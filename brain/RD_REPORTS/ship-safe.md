# R&D Report: Ship-Safe

## Basic Info
- **Repo:** github.com/asamassekou10/ship-safe
- **Stars:** 456
- **License:** Not specified in scraped content
- **Cloned:** /home/workspace/ship-safe/
- **Forked:** https://github.com/jvanleur2234-glitch/ship-safe

## What It Is
CLI security scanner built for the agentic era. Detects CI/CD misconfigs, agent permission risks, MCP tool injection, hardcoded secrets, and DMCA-flagged AI dependencies. Has 22 parallel security agents, secrets verification (probes APIs to check if leaked keys are still active), OWASP 2025 scoring, compliance mapping (SOC 2, ISO 27001, NIST AI RMF), and a self-healing loop (`--agentic` flag: scan → annotate fix → re-scan until score ≥ 75).

## Key Features
- 22 parallel security agents
- Secrets verification (probes GitHub, Stripe, OpenAI APIs to check if leaked keys are still active)
- MCP tool injection detection
- LLM-powered taint analysis (`--deep`)
- Agentic loop: scan → auto-fix → re-scan until score ≥ 75/85
- OWASP 2025 weighted scoring (0-100, A-F)
- Compliance mapping: SOC 2 Type II, ISO 27001:2022, NIST AI Risk Management Framework
- Hermes Agent first-class citizen — register tools directly in Hermes registry
- `ship_safe_audit`, `ship_safe_scan_mcp`, `ship_safe_get_findings`, `ship_safe_suppress_finding`, `ship_safe_memory_list` tools
- OpenClaw security scanning (ClawHavoc IOC detection)
- Baseline management (accept findings, only report regressions)
- CycloneDX SBOM generation
- Legal risk audit (DMCA, openclaude, claw-code)
- Live OSV.dev advisory feed

## Why It Matters for Solomon OS / JCPaid
**PERFECT for Solomon Guardian.** Ship-Safe's 22 parallel agents + agentic loop pattern maps directly to Guardian's attack team. The `--agentic` self-healing loop (scan → fix → re-scan until score ≥ 75) is exactly the Evolver pattern we need. Ship Safe verifies if leaked secrets are still active — critical for Guardian's credential monitoring. The MCP tool injection detection guards Hermes and Russell Tuna's tool invocations.

Also: Ship Safe is a first-class Hermes citizen — `registerWithHermes()` API and bundled skill manifest. Install in one line into any Hermes agent.

## Integration with Existing Stack
- **Guardian Attack Team** → use Ship Safe's 22 agents as the probing mechanism
- **Evolver** → use `--agentic` loop pattern for self-healing
- **Hermes** → register Ship Safe tools directly via `registerWithHermes()`
- **Secrets monitoring** → use `--verify` to check if exposed keys are still active

## LINK Fit
★★★★★ — #solomon-guardian #security #agentic-loop #self-healing #hermes #owasp

## Status
Forked ✅ — needs integration spec and Hermes tool registration
