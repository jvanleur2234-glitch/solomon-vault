## dapr-agents — Durable AI Agent Workflows on Dapr (April 26, 2026)
- **URL:** https://github.com/dapr/dapr-agents
- **Fork:** Already forked (`jvanleur2234-glitch/dapr-agents`)
- **What it does:** Python framework for autonomous, resilient AI agents with durable workflows (tasks complete through restarts), Kubernetes-native deployment, multi-agent collaboration, and built-in state management/telemetry.
- **Solomon OS fit:** SKILL — Study durable execution + sidecar pattern for Hermes mission-critical workflows. Apache 2.0, 662 stars.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/dapr-agents-durable-agent-workflows.md

## agent-orcha — Declarative YAML Multi-Agent Orchestration (April 26, 2026)
- **URL:** https://github.com/ddalcu/agent-orcha
- **What it does:** YAML-based declarative framework for multi-agent AI systems. Built-in SQLite vector store, MCP integration, P2P encrypted agent sharing with per-peer rate limits, browser sandbox (Chromium CDP + Xvfb + noVNC), visual Studio.
- **Solomon OS fit:** SKILL — Study P2P sharing model (rate limits, key exchange, sandboxing) for AgentFM/Hermes P2P compute. MIT, 11 stars.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/agent-orcha-declarative-multi-agent-yaml-framework.md

## Vibium — Cross-Language Browser Automation with MCP Server (April 26, 2026)
- **URL:** https://github.com/VibiumDev/vibium
- **What it does:** ~10MB binary browser automation toolkit using WebDriver BiDi standard. MCP server for AI integration. Libraries for JS/TS, Python, Java. Zero-config browser downloads, AI-native natural language mapping. Apache 2.0, 2784 stars.
- **Solomon OS fit:** SKILL — Browser automation alternative to agent-browser/HyperAgent. MCP server integration directly compatible with Hermes.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/vibium-browser-automation.md

## SecureVector AI Threat Monitor v3.2.0 — Real-Time On-Device Security Gateway (April 26, 2026)
- **URL:** https://github.com/Secure-Vector/securevector-ai-threat-monitor
- **What it does:** Real-time on-device security layer for AI agents. Skill Scanner (static + AI review), Policy Engine (risk scoring, trusted publishers, per-category rules), Tool Permissions (granular allow/block), Cost Tracking (per-agent spend, global budgets). 28 new threat detection rules. Local-only, no data leaves machine. MIT, 8 stars.
- **Solomon OS fit:** INTEGRATE — Skill Scanner + Policy Engine + Tool Permissions completes AgentArmor Studio 8-layer framework. Cost tracking aligns with JCPaid billing. Local-first privacy.
- **Status:** INTEGRATE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/securevector-ai-threat-monitor.md

## OpenMythos — Recurrent-Depth Transformer + MoE by Kye Gomez (April 26, 2026)
- **URL:** https://github.com/kyegomez/OpenMythos
- **Fork:** Already forked (`jvanleur2234-glitch/OpenMythos`)
- **What it does:** Open-source reconstruction of Claude Mythos as a Recurrent-Depth Transformer (RDT). Fixed layers looped T times per forward pass. Input injection prevents signal drift. Sparse MoE with routed + shared experts. Systematic generalization, depth extrapolation, latent thoughts. Author: Kye Gomez (OpenClaw creator).
- **Solomon OS fit:** SKILL — Study looped transformer + MoE architecture for Hermes reasoning engine enhancement. Kye Gomez = key ecosystem player.
- **Status:** SKILL
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/open-mythos-recurrent-depth-transformer.md
## Hermes Vault v0.4.0 — Tony Simons — AI Agent Observability Layer (April 25, 2026)
- **URL:** https://github.com/asimons81/hermes-vault
- **What it does:** Local-first credential broker for AI agents. Gives agents "a pair of glasses" for observability — credential health tracking (stale/expiring keys), cryptographic audit logs (SHA-256 hash-chained), secrets isolation (1Password-style, secrets never leave vault), verification reports.
- **Key features:**
  - Credential health tracking — proactive alerting before keys expire
  - Audit logs + verification reports — full visibility into agent access
  - Secrets never leave vault — agent gets placeholder/proxy, never raw secret
  - Cryptographic audit trail — tamper-evident, append-only, queryable
- **Ecosystem context:** Hermes Agent (NousResearch) has telemetry (#6642), session tracing (#6741), PII redaction, and Hermes Katana (7-layer security: taint tracking, flow analysis, input scanner 30+ patterns, policy engine, SHA-256 audit trail)
- **Solomon OS fit:** FORGE — directly applicable. Solomon OS runs on Hermes. Credential health alone is worth it — proactive alerting before keys break is a genuine enterprise selling point. Audit logs solve compliance requirements for regulated industries.
- **Status:** FORGE
- **RD Report:** /home/workspace/solomon-vault/brain/RD_REPORTS/hermes-vault-v0.4.0.md

