# HackMyAgent — OpenA2A Security Scanner (209 Checks + NanoMind)

**Fork:** github.com/jvanleur2234-glitch/hackmyagent-new  
**Original:** opena2a-org/hackmyagent  
**License:** Apache-2.0  
**Relevance:** 🔴 Critical — AI agent security/red-teaming

## What It Is
Security scanner, red-team toolkit, behavioral simulation engine. 209 security checks + 29 semantic checks + behavioral simulation powered by NanoMind semantic compiler. 1723 tests passing.

## Key Differentiator: NanoMind Semantic Compiler
Compiles every artifact into an Abstract Security Tree. 28 semantic checks query the AST instead of regex. Catches: undeclared capabilities, constraint weakness, scope mismatches, scanner evasion attempts. This is why "seven scanners agree on only 0.12% of skills" — NanoMind finds what regex misses.

## Key Capabilities
- **secure** — `npx hackmyagent secure` — all checks, no config
- **red-team** — Generates target-specific attacks, iterates, maps defenses
- **attack** — 164 adversarial payloads across 16 categories
- **scan-soul** — OASB behavioral governance scanning
- **harden-soul** — Auto-generate SOUL.md governance
- **Self-securing** — Verifies binary integrity on startup (QUARANTINE mode if tampered)

## 35 Security Categories
CRED, MCP, CLAUDE, NET, PROMPT, INJ, ENCRYPT, SESSION, AUDIT, SANDBOX, TOOL, AUTH, DEP, ENV, GIT, IO, LOG, PERM, PROC, RATE, SEC, API, VSCODE, CURSOR, CVE, GATEWAY, CONFIG, SUPPLY, SKILL, HEARTBEAT, UNICODE-STEGO, MEM, RAG, AIM, NEMO

## Comparison
- vs AgentSeal: HackMyAgent has red-team + behavioral simulation; AgentSeal has shield + real-time monitoring
- vs Vigile: HackMyAgent is 3.5x more checks (209 vs 59)
- vs Firmis: Different approach (semantic AST vs static rules); can complement each other

## Solomon OS Relevance
**INTEGRATE** — Most sophisticated of the security scanners. NanoMind semantic analysis is unique. Use for: red-teaming new Hermes skills, scanning SOUL.md governance files, behavioral simulation before production deployment.

## Verdict
FORGE — Best scanner for deep security analysis. Add NanoMind semantic analysis to Solomon OS pre-deployment pipeline. Critical for hardening AI employee deployments.
