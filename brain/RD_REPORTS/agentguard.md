# AgentGuard — AI Agent Security Layer

**Repo:** `GoPlusSecurity/agentguard` | **License:** MIT | **Lang:** TypeScript

## What It Is
Three-layer security system for AI agents. Real-time blocking, automated scanning, ongoing posture checks.

## Key Capabilities
- **Layer 1 — Auto Guard (hooks):** Blocks dangerous commands (`rm -rf /`, fork bombs, `curl | bash`), prevents writes to sensitive paths, detects data exfiltration
- **Layer 2 — Deep Scan (skill):** On-demand security audits, 24 detection rules, static analysis for secrets/backdoors/obfuscation/prompt injection, Web3-focused checks (wallet drains, reentrancy), per-skill trust registry
- **Layer 3 — Daily Patrol (OpenClaw):** Automated daily posture checks, detects skill tampering, secrets exposure, network risks, suspicious file changes
- Per-skill capability tracking — logs which skill initiated each action

## Solomon OS Fit
- **Runtime guard for Hermes:** AgentGuard hooks would add a critical security layer to Hermes execution
- **Trust registry:** Per-skill access control aligns with Hermes skill ecosystem governance
- **LINK fit:** ★★★★★ — #security #runtime-guard #skill-governance #hermes-adjacent

## Action
Already forked. Write RD deep-dive. Add to HERMES_CAPABILITIES as runtime security layer. Priority: HIGH.
