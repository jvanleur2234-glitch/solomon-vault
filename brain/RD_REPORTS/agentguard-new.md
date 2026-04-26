# RD Report: GoPlus AgentGuard v0.4+

**Repo:** `GoPlusSecurity/agentguard` → cloned to `agentguard-new`  
**Fork:** https://github.com/jvanleur2234-glitch/agentguard-new  
**License:** MIT  
**Stars:** 390  
**Date:** 2026-04-26

## What It Is
Real-time 3-tier security layer for AI agents. Guards terminal/files/secrets access, scans skills for threats, runs daily security patrols.

## Key Capabilities
- **Layer 1 (Guard):** Blocks destructive commands (rm -rf /, fork bombs, curl|bash), prevents writes to .env/.ssh, detects exfiltration to Discord/Telegram webhooks, tracks skill attribution
- **Layer 2 (Deep Scan):** 24 detection rules, auto-scans new skills at session start, static analysis for secrets/backdoors/obfuscation/prompt injection, Web3-specific checks
- **Layer 3 (Daily Patrol):** 8 security checks, detects tampering/secrets/network risks, analyzes audit logs
- Trust registry with per-skill capability-based access control

## Relevance to Solomon OS
**CRITICAL** — MIT licensed, real-time protection, skill-level attribution. Perfect for Hermes security layer.

## Use Case for Hermes
- Install as core security skill on every Hermes instance
- Layer 1 blocks dangerous commands before execution
- Layer 2 audits new skills for prompt injection
- Layer 3 provides daily security posture reports

## Verdict
**FORGE** — Must-have security layer. Add to Hermes core security skills.