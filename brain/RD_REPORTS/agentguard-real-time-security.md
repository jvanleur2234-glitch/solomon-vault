# RD Report: agentguard — Real-Time AI Agent Security Layer

**Original:** `GoPlusSecurity/agentguard` | **License:** MIT | **Stars:** ~1K+ | **Lang:** TypeScript

## What It Is
Real-time security layer for AI agents. Blocks destructive commands, prevents writes to sensitive files, detects data exfiltration. Three-layer architecture: Auto Guard (hooks) → Deep Scan (skill) → Daily Patrol (OpenClaw).

## Key Capabilities
- Layer 1: Automatic Guard hooks — blocks `rm -rf /`, fork bombs, curl|bash, writes to .env/.ssh
- Layer 2: Deep Scan — 24 detection rules, auto-scans new skills on session start, trust registry
- Layer 3: Daily Patrol — automated posture checks, audit log analysis
- Capability-based access control per skill
- Action tracing to initiator (accountability)
- OpenClaw plugin support

## Relevance to Solomon OS
- **Security:** Real-time protection for Hermes agents
- **OPSec:** Prevents credential leakage, destructive commands
- **Audit:** Traces which skill initiated each action

## Threat Analysis
- MIT licensed
- GoPlus Security (established security vendor)
- TypeScript — aligns with Hermes ACP skill model

## Integration Path
```
SKILL: agentguard → Hermes real-time security layer
USE CASE: Production defense for AI agents against prompt injection and tool abuse
```

**Recommendation:** FORGE — Real-time security layer with established patterns. GoPlus is credible vendor. Aligns with agentarmor-studio. Add to production security stack.