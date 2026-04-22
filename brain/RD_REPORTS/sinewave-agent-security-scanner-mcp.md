# RD Report: Sinewave Agent Security Scanner MCP

**Date:** 2026-04-22  
**Category:** AI Security / MCP  
**Source:** web_research (github)  
**Fork Status:** Already forked (sinewave-agent-security-scanner-mcp)

## What It Is
A security scanner MCP server for AI coding agents. Provides a defensive framework to monitor and protect AI agents during code generation and execution.

## Key Capabilities
- **Prompt injection firewall** — guards against prompt-based exploits
- **Package hallucination detection** — checks 4.3M+ packages for incorrect/malicious refs
- **1000+ vulnerability rules** using AST & taint analysis
- **Auto-fix** — suggests/applies fixes for detected issues
- Designed for AI coding agent ecosystems (validates code before execution)

## Comparison to What We Have
- Competes with: guard-scanner, AgentSeal, RAXE
- Unique: Package hallucination detection (checks against 4.3M+ real packages)
- Deep integration with AI coding agent workflows

## Relevance to Solomon OS
- **CRITICAL** — JCPaid/Hermes needs security for agent code generation
- Prompt injection firewall is core defense
- Package hallucination detection prevents supply chain attacks

## Recommendation
**ALREADY FORKED** — No action needed. Already tracked as `sinewave-agent-security-scanner-mcp`.

---

## Stats
- License: MIT (implied)
- Language: Python/TypeScript
- Status: Active development