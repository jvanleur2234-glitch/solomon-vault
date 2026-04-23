# RD Report: opena2a-org/hackmyagent

**Forked:** https://github.com/jvanleur2234-glitch/hackmyagent  
**License:** Apache-2.0  
**Language:** TypeScript/Node.js

## What It Is
Security scanner + red-team toolkit + behavioral simulation for AI agents. 209 security checks + 29 semantic checks. NanoMind semantic compiler compiles artifacts into Abstract Security Trees before analysis.

## Relevance to Solomon OS
- **AgentArmor Studio complement**: Both scan for security issues
- **OWASP LLM Top 10 aligned**: Direct mapping to 2026 OWASP findings
- **Skill builder**: `hackmyagent create-skill` generates secured skills with SOUL.md governance
- **MCP security**: Tests MCP servers for exploitation vectors

## Key Capabilities
- **NanoMind**: Semantic AST analysis vs regex — catches undeclared capabilities, scope violations
- **Behavioral simulation**: 20-probe battery observes what skills actually do
- **164 attack payloads**: 16 categories (prompt injection, jailbreak, data exfil, MCP exploitation)
- **Self-securing**: Binary integrity verification on startup
- **A2A protocol attacks**: Agent-to-agent identity spoofing/escalation

## Security Categories Covered
- CRED: Hardcoded credentials (4 checks)
- MCP: Server misconfigs (10 checks)
- PROMPT: Injection vectors (4 checks)
- SKILL: Malicious skill detection (12 checks)
- MEM: Memory poisoning (5 checks)
- RAG: Knowledge base poisoning (4 checks)
- AIM: Agent identity verification (3 checks)
- CVE: Known vulnerability detection

## Comparison to AgentArmor Studio
| Feature | HackMyAgent | AgentArmor Studio |
|---------|-------------|------------------|
| Semantic analysis | ✅ NanoMind | ❌ |
| Behavioral simulation | ✅ 20 probes | ❌ |
| Red team payloads | ✅ 164 | ❌ |
| Self-securing | ✅ | ❌ |
| 8-layer framework | ❌ | ✅ |
| MITRE ATLAS aligned | Partial | ✅ |

## Verdict
**INTEGRATE** — Best-in-class agent security scanner. NanoMind semantic analysis is superior to regex. Install as Hermes skill: `npx hackmyagent secure`. Complements AgentArmor Studio's 8-layer framework with behavioral testing and semantic AST analysis.
