# hackmyagent — Semantic Security Scanner for AI Agents

**Fork:** Already forked to `jvanleur2234-glitch/hackmyagent`  
**License:** MIT  
**Latest:** v0.19.0 (2026-04-23)

## What It Is
A security toolkit (TypeScript/Node.js 18+) for verifying AI agent skills, hardening setups, and scanning for exposures. Uses a **semantic Abstract Security Tree (AST)** approach rather than regex — catches undeclared capabilities, scope mismatches, evasion attempts.

## Key Capabilities
- **209 static checks** across 44 categories
- **29 NanoMind semantic checks** for deep behavioral analysis
- **164 adversarial payloads** to test defenses against prompt injection, tool abuse, memory manipulation
- **Behavioral simulation**: 20-probe battery (deep mode available)
- **Self-securing**: startup verification with quarantine for tampered binaries

## Comparison to Firmis Scanner / AgentVerus / Snyk Agent Scan

| Feature | HackMyAgent | Firmis | AgentVerus | Snyk |
|---|---|---|---|---|
| Approach | Semantic AST | 268 rules | Trust reports | Inventory + scan |
| Checks | 209 static + 29 semantic | 268 detection rules | Capability contracts | 15+ threat categories |
| Payloads | 164 adversarial | No | No | No |
| Self-securing | ✅ | ❌ | ❌ | ❌ |
| MIT licensed | ✅ | ✅ | ✅ | ❌ |

## Verdict
**INTEGRATE** — The semantic AST approach is more sophisticated than regex-based scanners. Could be integrated as an **AgentArmor Studio** layer in Hermes. The self-securing startup verification is particularly interesting.