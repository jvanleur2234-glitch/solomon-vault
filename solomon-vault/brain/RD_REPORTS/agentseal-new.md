# AgentSeal — Security Toolkit for AI Agents

**Fork:** github.com/jvanleur2234-glitch/agentseal-new  
**Original:** AgentSeal/agentseal  
**License:** FSL-1.1-Apache-2.0  
**Stars:** Unknown (new discovery)  
**Relevance:** 🔴 Critical — AI agent security

## What It Is
Security scanner for AI agents. Scans skill files, MCP configs, detects tool poisoning, data exfiltration paths, and supply chain attacks. 225+ adversarial probes across 28 agents.

## Key Capabilities
- **guard** — Local scan of all AI agent configs (Claude Code, Cursor, Windsurf, VS Code, Gemini CLI, etc.)
- **scan** — Tests system prompts against 225+ adversarial attack probes (82 extraction, 143 injection)
- **scan-mcp** — Audits live MCP server tool descriptions for poisoning
- **shield** — Real-time file watcher with quarantine

## 6-Stage Detection Pipeline
1. Pattern signatures (credential access, exfil URLs, shell commands)
2. Deobfuscation (Unicode, Base64, BiDi, zero-width chars, TR39)
3. Semantic analysis (MiniLM-L6-v2 embedding similarity)
4. Baseline tracking (SHA-256 hash diffs)
5. Registry enrichment (MCP Security Registry — 6,600+ servers)
6. Custom YAML rules

## Trust Score (0-100)
| Score | Level |
|-------|-------|
| 85-100 | Excellent |
| 70-84 | High |
| 50-69 | Medium |
| 30-49 | Low |
| 0-29 | Critical |

## Comparison to Existing Tools
- vs Snyk agent-scan: More probes (225 vs 20), local-only mode, real-time monitoring
- vs RAXE: More comprehensive agent coverage (28 vs focused), MCP poisoning detection
- Differentiation: Semantic analysis layer (embedding similarity) vs pure regex

## Solomon OS Relevance
**INTEGRATE** — Use as pre-deployment gate for any third-party Hermes skills. Scan every new skill file before activation. Critical for multi-tenant AI employee deployments.

## Verdict
FORGE — Add to Solomon OS security layer. Run `agentseal guard` as part of skill installation pipeline.
