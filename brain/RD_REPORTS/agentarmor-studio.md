# RD Report: AgentArmor Studio — 8-Layer AI Agent Security Framework

**Date:** 2026-04-20
**Source:** [X @omarsar0](https://x.com/omarsar0/status/2045710575356064233)
**Stars:** 1 (new)
**License:** Apache 2.0

## What It Is

AgentArmor Studio is a **desktop application** (Tauri + React + Python sidecar) for building, deploying, and monitoring AI agents with real-time security enforcement. Built on [agentarmor-core](https://github.com/Agastya910/agentarmor-core) — an 8-layer security framework that's also on PyPI.

The app has a visual UI (Dashboard, Agent Builder, Agent Runner, Layers inspector, Events feed) that wraps the security pipeline. No Python/Rust/Node.js needed for end users — bundled as a single Windows installer.

## Architecture

```
Tauri (Rust) Desktop Shell
├── React + TypeScript Frontend (dashboard, builder, runner, layers, events, settings)
└── Python Sidecar (PyInstaller bundle, auto-starts)
    ├── FastAPI server
    ├── agentarmor-core L1-L8 security pipeline
    ├── LLM integration (Ollama / OpenAI / Anthropic)
    └── SQLite DB (AES-256-GCM encrypted, HMAC-signed)
```

## The 8 Security Layers (L1-L8)

| Layer | Name | What It Does |
|-------|------|-------------|
| L1 | Ingestion | Prompt injection detection (regex + ML classifier), Unicode normalization, CDR |
| L2 | Storage | AES-256-GCM encryption, HMAC-SHA256 integrity MAC on all persisted data |
| L3 | Context | Template injection stripping, canary tokens, goal-drift detection |
| L4 | Planning | Verb-risk classification, chain escalation detection, compound risk scoring |
| L5 | Execution | Network isolation, SSRF blocking, path traversal prevention, per-agent sandboxing |
| L6 | Output | Credential scanning, PII redaction (Presidio), exfiltration pattern detection |
| L7 | Inter-Agent | Replay prevention, delegation certificates, trust scoring, anomaly detection |
| L8 | Identity | API key validation, RBAC, session binding, permission boundaries |

## Solomon OS Fit

**★★★★★ — PERFECT for Solomon Guardian**

The 8-layer model maps **directly** to what Guardian does:
- L1 (Ingestion) = Guardian's input sanitization
- L2 (Storage) = Guardian's encrypted audit log
- L3 (Context) = Guardian's context poisoning detection
- L4 (Planning) = Guardian's chain-of-thought monitoring
- L5 (Execution) = Guardian's network isolation + tool sandboxing
- L6 (Output) = Guardian's PII/credential output scanning
- L7 (Inter-Agent) = Guardian's Solomon Bus message verification
- L8 (Identity) = Guardian's RBAC + API key validation

**Integration approach:**
1. Fork AgentArmor Studio → jvanleur2234-glitch/agentarmor-studio
2. Extract agentarmor-core Python package → add to Solomon OS skills
3. Replace Tauri shell with Hermes/Russell Tuna integration
4. The visual Layers inspector → become Guardian's web dashboard
5. Events feed → Guardian's real-time security alert stream

**Quick install:** `pip install agentarmor-core[all]`

## Recommendation

**SKILL** — Fork and deeply integrate. The 8-layer framework is exactly what Solomon Guardian needs. Having it as a pip-installable skill (`pip install agentarmor-core`) means every Hermes worker can have L1-L8 security by default.