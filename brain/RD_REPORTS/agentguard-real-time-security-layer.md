# RD Report: AgentGuard — Real-Time Security Layer for AI Agents

## Summary
AgentGuard by GoPlusSecurity is a real-time security layer protecting AI agents from malicious skills, prompt injections, and data leaks. 3-layer system: Automatic Guard (blocks destructive commands), Deep Scan (24 detection rules, auto-scans), Daily Patrol (configurable automated posture checks). MIT, active development.

## What It Does
- **Layer 1 — Automatic Guard**: Blocks destructive commands (rm -rf /, fork bombs), risky writes (.env, .ssh), data exfiltration
- **Layer 2 — Deep Scan**: 24 detection rules, auto-scans new skills at session start, static analysis for secrets/backdoors/injection, Web3-specific checks
- **Layer 3 — Daily Patrol**: Automated daily posture checks (tampering, secrets, network, file changes), audit log analysis
- **Trust Registry**: Per-skill access control with audit trail
- **NPM Install**: `@goplus/agentguard`
- **OpenClaw Plugin**: Full integration available

## Tech Stack
- Language: TypeScript/JavaScript
- License: MIT
- Integration: OpenClaw, Claude Code

## Strategic Fit for Solomon OS

**INTEGRATE** — Real-time protection layer directly applicable to Hermes.

Key learnings:
1. **3-Layer Defense**: Automatic → Deep → Patrol = defense in depth
2. **Destructive Command Blocking**: Critical for Hermes shell safety
3. **Skill Trust Registry**: Per-skill access control with audit
4. **Daily Patrol**: Automated security posture maintenance

## Risk/Concerns
- GoPlusSecurity brand = less community trust than Snyk
- OpenClaw-specific integration path
- Web3 focus may not apply to all use cases

## Verdict
INTEGRATE — Layer 1 (Automatic Guard) directly applicable to Hermes runtime protection. Trust registry model for AgentArmor Studio Layer 6 (Access Control).

## Links
- Repo: https://github.com/GoPlusSecurity/agentguard
- Fork: Already forked