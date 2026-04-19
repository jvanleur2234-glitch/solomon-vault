# R&D Report: Anthropic-Cybersecurity-Skills

**Date:** April 19, 2026
**Repo:** github.com/mukul975/Anthropic-Cybersecurity-Skills
**Stars:** 4.7K | **License:** Apache 2.0 | ** forks:** 554

## What It Is

754 production-grade cybersecurity skills for AI agents. Each skill encodes the exact decision-making workflow a senior security analyst follows — not scripts, not checklists. Built on agentskills.io standard (YAML frontmatter + Markdown).

**26 security domains covered:**
- Cloud Security (AWS/Azure/GCP) — 60 skills
- Threat Hunting — 55 skills
- Threat Intelligence (STIX/TAXII/MISP) — 50 skills
- Web Application Security (OWASP Top 10) — 42 skills
- Network Security (IDS/IPS/firewall) — 40 skills
- Malware Analysis — 39 skills
- DFIR (Digital Forensics) — 38 skills
- Penetration Testing — 35 skills
- Vulnerability Assessment — 32 skills
- IoT Security — 30 skills
- Mobile Security — 28 skills
- Endpoint Security — 26 skills
- IAM / Zero Trust — 24 skills
- Cryptography — 20 skills
- + 12 more domains

## The 5 Framework Mappings

No other open-source skills library maps to all 5:

| Framework | Coverage |
|-----------|----------|
| **MITRE ATT&CK** | 14 tactics, 200+ techniques |
| **NIST CSF 2.0** | All 6 functions (GV/ID/PR/DE/RS/RC), 22 categories |
| **MITRE ATLAS** | 16 tactics, 84 techniques (AI-specific threats) |
| **MITRE D3FEND** | 7 categories, 267 defensive countermeasures |
| **NIST AI RMF** | 4 functions, 72 subcategories + GenAI Profile |

**Key for Solomon Guardian:** ATLAS mapping includes agentic AI attack vectors (context poisoning, tool invocation abuse, MCP server compromises, malicious agent deployment) — exactly what Solomon Guardian needs to defend against.

## Why It Fits Solomon Guardian

Solomon Guardian has the adversarial loop architecture. What it lacked was domain-grade offensive and defensive knowledge. This fills that gap:

**Attack Team gets:**
- 35 pentest skills (network, web, API, social engineering)
- 39 malware analysis skills
- 50 threat intel skills (real actor TTPs)
- 42 web app security skills (OWASP Top 10)

**Defense Team gets:**
- 200+ detect skills (Sigma rules, YARA, anomaly detection)
- 160+ respond skills (incident response playbooks)
- 60 cloud security skills (AWS/Azure/GCP hardening)
- All mapped to MITRE ATT&CK + D3FEND for automatic countermeasure recommendation

**Governance gets:**
- 30 Govern skills (risk strategy, policy, compliance)
- Full NIST CSF 2.0 alignment
- Colorado AI Act compliance path (NIST AI RMF)

## Business Model

**Sell "AI Security Analyst" as a product:**
- Hermes Agent + 754 cybersecurity skills = automated security operations
- Monthly subscription: $99-499/mo per organization
- Target: SMBs who can't afford a SOC team
- Competitive edge: No other AI staffing agency has 754 MITRE-mapped security skills

**For Solomon OS:** Install these as Solomon Guardian's skill library. Every penetration test, every threat hunt, every forensic investigation — the AI knows how to do it.

## Quick Install

```bash
npx skills add mukul975/Anthropic-Cybersecurity-Skills
```

Works with: Claude Code, GitHub Copilot, Cursor, Codex CLI, Gemini CLI, AutoGen, LangChain, any MCP-compatible agent.

## Forked

**Location:** /home/workspace/Anthropic-Cybersecurity-Skills/
**GitHub:** github.com/jvanleur2234-glitch/Anthropic-Cybersecurity-Skills

## LINK Fit

★★★★★ — **CRITICAL** for Solomon Guardian. This is the missing knowledge layer.

- Fills Guardian's "knowledge of how attacks work" gap
- All 5 frameworks mapped = compliance-ready out of the box
- ATLAS coverage for AI-specific threats = guards against attacks on Hermes/Russell Tuna themselves
- agentskills.io standard = works with Hermes immediately

**Next step:** `npx skills add mukul975/Anthropic-Cybersecurity-Skills` into Hermes, then wire to Solomon Guardian attack/defense loop.
