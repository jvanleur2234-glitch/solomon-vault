# RD Report: agent-security-scanner (Cybathreat)

**Fork:** https://github.com/jvanleur2234-glitch/agent-security-scanner  
**Source:** https://github.com/Cybathreat/agent-security-scanner  
**Date:** 2026-04-22  
**License:** MIT  
**Stars:** ~500+  
**Language:** Python  

## What It Does
Comprehensive security auditing tool for AI agents, LLM-powered applications, and RAG pipelines. Scans for misconfigurations, prompt injection, tool calling boundary violations, RAG pipeline vulnerabilities, agent-specific attacks, and infrastructure security issues.

## Key Features
- **11 scanning modules:** misconfigurations, prompt_injection, tool_boundaries, rag_security, tool_hijacking, recursive_agents, memory_poisoning, planning_attacks, secret_scanner, dependency_audit, plugin_security
- **Prompt injection coverage:** Direct injection, system prompt leakage, obfuscation, multi-turn injection, crescendo attacks, many-shot jailbreaking, skeleton key bypass
- **RAG pipeline security:** Document poisoning, data exfiltration, vector DB checks, embedding vulnerabilities, multi-tenant isolation
- **Agent attack scanning:** Tool hijacking, recursive exploitation, memory poisoning, planning manipulation
- **OWASP/MITRE mappings:** Structured JSON reports with CWE/OWASP/ATLAS framework references
- **Severity-based risk scoring:** Critical/High/Medium/Low with actionable remediation guidance

## Solomon OS Fit
**INTEGRATE** — Core security gate for Hermes. Comprehensive prompt injection detection fills a gap. OWASP Agentic Top 10 aligned. Agent-specific attack modules (memory poisoning, recursive agents) directly applicable to multi-agent orchestration security.

## Competitor Notes
Competes with Sinewave agent-security-scanner-mcp (AST-based), guard-scanner (OWASP aligned), AgentAudit MCP (package scanning). This one covers the broadest attack surface including RAG pipelines and agent-specific attacks.

## Recommendation
INTEGRATE — Most comprehensive open-source agent security scanner found. Deploy in CI/CD pipeline as pre-deployment gate for new skills.