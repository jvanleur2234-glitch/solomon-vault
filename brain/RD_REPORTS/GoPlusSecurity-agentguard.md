# RD Report: agentguard (GoPlusSecurity)

**Scout Session:** 2026-04-22  
**Fork:** https://github.com/jvanleur2234-glitch/agentguard  
**Original:** https://github.com/GoPlusSecurity/agentguard  
**License:** TypeScript (Apache 2.0 likely)

---

## What it does
Three-layer security guard for AI agents:

- **Layer 1 — Automatic Guard:** Blocks dangerous commands (rm -rf /, fork bombs, curl|bash), prevents writes to sensitive files (.env, .ssh/), detects exfiltration to known endpoints. Tracks which skill initiated each action.
- **Layer 2 — Deep Scan:** On-session auto-scan of new skills with 24 detection rules. Static analysis for secrets, backdoors, obfuscation, prompt injection. Web3-specific checks (wallet draining, unlimited approvals, reentrancy, proxy exploits). Trust registry with per-skill access control.
- **Layer 3 — Daily Patrol (OpenClaw):** Daily security posture with 8 checks, tamper detection, audit log pattern analysis, environment/config validation.

## Solomon OS fit
**INTEGRATE** — AgentGuard fills the runtime security layer for Hermes/Solomon. Multi-layer design maps to Solomon's security architecture. OpenClaw integration already built. MIT-compatible (appears to be Apache 2.0). Critical for JCPaid enterprise clients.

## Key patterns to steal
- Skill-initiated action tracking (who did what)
- Trust registry with per-skill access control
- Layered approach: instant block → on-session scan → daily patrol

## Risk
- Tight coupling to OpenClaw; may need porting for generic Hermes use