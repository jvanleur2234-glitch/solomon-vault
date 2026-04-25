# llm-audit — OWASP LLM Top 10 CLI Testing Tool

**Fork:** NOT FORKED (MIT, Python 3.10+)  
**License:** MIT  
**Stars:** ~800  
**Date:** 2026-04-25

## What It Is

Python CLI tool to automatically test LLM endpoints (OpenAI, Ollama, Azure, custom APIs) against OWASP LLM Top 10 vulnerabilities. Provides pass/fail reports, severity scoring, and fix recommendations. CI/CD-ready.

## Key Features

- **OWASP LLM01:** Direct prompt injection + embedded injections
- **OWASP LLM01:** Jailbreak detection (persona flip, restriction bypass)
- **OWASP LLM06:** Data leakage (PII, credentials extraction)
- **OWASP LLM02:** Insecure output (XSS, SQLi, SSRF, path traversal)
- **OWASP LLM06:** Training data extraction (memorization/PII reproduction)
- **OWASP LLM04:** Denial of service (latency spikes, repeated prompts)
- **OWASP LLM08:** Excessive agency (privilege escalation, unauthorized tool use)
- **CI/CD integration** with exit codes
- **Multiple output formats:** rich terminal, JSON, SARIF

## Quick Start

```bash
pip install llm-audit
llm-audit --target https://api.openai.com/v1/chat/completions \
  --api-key $OPENAI_API_KEY \
  --provider openai
```

## Solomon OS Fit

**INTEGRATE** — Security testing pipeline for every Hermes deployment. Run as CI gate before skill activation. Maps directly to OWASP LLM Top 10 compliance needs. MIT license permits direct use.

## Verdict

**INTEGRATE** — Add to security layer. CI/CD gate for Hermes skill deployments.
