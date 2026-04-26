# RD Report: AgentGuard by GoPlus Security

**Repo:** `GoPlusSecurity/agentguard`  
**URL:** https://github.com/GoPlusSecurity/agentguard  
**License:** MIT  
**Stars:** ~3 authors, active since Feb 2026  
**Date:** 2026-04-26

## What It Is
Real-time security layer for AI agents with 3-tier defense: automatic guard (hooks into agent actions), deep scan (24 detection rules), daily patrol (automated posture checks).

## Key Capabilities
- Layer 1 Automatic Guard: blocks destructive commands (rm -rf /, fork bombs), prevents writes to sensitive files (.env, .ssh), detects exfiltration webhooks, attributes actions to skills
- Layer 2 Deep Scan: 24 detection rules, auto-scans new skills at session start, static analysis for secrets/backdoors/obfuscation/prompt injection
- Layer 3 Daily Patrol: configurable schedule, detects tampering/secrets/network risks, analyzes audit logs
- Trust registry with capability-based per-skill access control
- Web3-specific checks (wallet draining, unlimited approvals, reentrancy)

## Relevance to Solomon OS
**CRITICAL** — Directly fills the security layer gap for Hermes. The 3-tier defense model (guard → scan → patrol) maps perfectly to Hermes security requirements. MIT licensed.

## Use Case for JCPaid/Hermes
- Install as core security skill on every Hermes instance
- Layer 1 blocks dangerous commands before execution
- Layer 2 audits new skills for prompt injection
- Layer 3 provides daily security posture reports

## Comparison to Existing
- More real-time than firmis-scanner (hooks into action layer)
- Multi-layer (guard/scan/patrol) more comprehensive than single-layer tools
- MIT licensed — fork and integrate

## Verdict
**FORGE** — Must-have security layer. Fork and integrate into Hermes core security.

## Action Taken
Already cloned in workspace.