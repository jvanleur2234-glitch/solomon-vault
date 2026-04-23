# Aegis — EDR for AI Agents

## Metadata
- **URL:** https://github.com/allinbsv/Aegis
- **Fork:** https://github.com/jvanleur2234-glitch/Aegis
- **License:** MIT
- **Tech:** Node.js (TypeScript), 568 tests
- **Status:** CLONED / FORKED

## What It Does
Independent AI oversight layer — monitors what AI agents do across processes, files, and network activity. Provides risk scoring and behavioral analysis entirely locally (no cloud telemetry).

## Key Capabilities
- **Process monitoring:** Detects 107 known AI-agent signatures, tracks parent-child relationships, IDE host detection
- **File protection:** Watches sensitive dirs (.ssh, .aws, .gnupg, .env, cloud configs)
- **Network monitoring:** Tracks outbound connections per agent, reverse DNS, flags unknown endpoints
- **Behavioral analytics:** Rolling baselines, 4-axis anomaly score (Network/File/Process/Baseline), per-agent risk scoring with trust grades A+ to F
- **Local LLM detection:** Ollama, LM Studio, vLLM, llama.cpp runtime detection
- **Optional threat reporting:** Printable HTML reports, opt-in Anthropic API for AI threat assessment

## Security Relevance
- Open-source local-first agent monitoring (vs cloud-only enterprise tools)
- Directly addresses security concerns for autonomous agents with file/credential access
- MIT licensed — can fork and integrate

## Solomon OS Fit
- **INTEGRATE** — Security monitoring layer for Hermes/Solomon OS agents
- Process/file/network monitoring complements existing security scanners (ProofLayer, Snyk, ClawSecure)
- Trust grades could feed into Hermes agent permission system
- Local LLM detection aligns with Solomon Air's on-device AI philosophy

## Comparison
| Tool | Type | License | Key Differentiator |
|------|------|---------|-------------------|
| Aegis | EDR | MIT | Local-first, process-level monitoring |
| ProofLayer | SAST | MIT | AST/taint analysis, code scanning |
| ClawSecure | Audit | MIT | OWASP ASI Top 10, 55+ threat patterns |
| Snyk Agent Scan | Inventory | Apache | MCP/skills discovery, compliance |

## Action
FORKED ✅ — Integrate as Hermes security monitoring skill. Study trust grade system for agent permission tiers.

## RD Report
`/home/workspace/solomon-vault/brain/RD_REPORTS/aegis-edr-ai-agents.md`