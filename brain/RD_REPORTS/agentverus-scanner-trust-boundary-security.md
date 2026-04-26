# agentverus/agentverus-scanner — Open-Source Security Scanner for AI Agent Skills (MIT)

## Quick Summary
Behavioral trust scanner for AI agent skills. Detects prompt injection, data exfiltration, and 10 ASST threat categories. Produces structured trust reports across permissions, capabilities, injections, dependencies, and workspace/config tampering.

## What It Does
- **Injection detection**: prompt injection, instruction override, relay
- **Dependency & content risk analysis**: external URLs, suspicious downloads, obfuscation
- **Behavioral risk scoring**: exfiltration, escalation, stealth
- **Code safety checks**: dangerous blocks, eval/exec, exfil patterns
- **Workspace/config tampering detection**: AGENTS.md, TOOLS.md, CLAUDE.md, .claude/**
- **Trust-boundary risk scoring** with configurable severities
- **Trust reports**: permissions, contract checks, injection risks, dependencies, behavioral risks, config tampering

## Key Improvements (v0.7.x)
- Tighter trust-boundary detection, higher signal quality
- Earlier detection of risky local references
- Better calibration for undeclared capabilities and local-service access
- Fewer false positives, stronger separation of safe vs malicious

## Relevance to Solomon OS
- **SKILL** — Directly applicable to Hermes security. The trust-boundary scanning pattern should be integrated into AgentArmor Studio.
- ASST threat categories inform Hermes threat model
- Config tampering detection relevant to Hermes skill security

## License & Status
- **License:** MIT
- **Already cloned:** /home/workspace/agentverus-scanner
- **Repo:** https://github.com/agentverus/agentverus-scanner

## Verdict
**INTEGRATE** — Security scanning for agent skills is essential. The trust-boundary approach should inform AgentArmor Studio. MIT licensed, actively maintained.
