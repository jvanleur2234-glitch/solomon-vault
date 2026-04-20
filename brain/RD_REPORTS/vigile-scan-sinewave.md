# RD Report: Vigile-ai/vigile-scan (sinewave fork variant)

## Summary
Security scanner toolkit that runs locally without installation. Automatically discovers MCP server configs and AI agent skill files, scans against 59 detection rules, produces trust score per item.

## Relevance to Solomon OS
- **Zero-config**: Fits Solomon OS philosophy of frictionless deployment
- **Trust scores**:量化 skill trust for Hermes marketplace
- **Local-first**: No cloud dependency

## Key Features
- 59 detection rules (22 MCP patterns + 5 inline, 32 agent skill patterns)
- MCP server threat detection: tool poisoning, data exfiltration, permission abuse, obfuscation
- Agent skill threat detection: instruction injection, malware delivery, stealth persistence, safety bypass
- Trust score per MCP server and per skill
- Multiple scan modes: default, skills-only, all
- JSON output for CI/CD

## License
Apache 2.0

## Use for Solomon OS
SKILL — Quick trust scanning for newly acquired Hermes skills

## Fork Status
Forked to: jvanleur2234-glitch/vigile-scan-sinewave
