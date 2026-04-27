# RD Report: Firmis Scanner

## Project: Firmis Scanner
- **URL:** https://github.com/Firmislabs/firmis-scanner
- **Fork:** Already forked (`jvanleur2234-glitch/firmis-scanner`)
- **License:** Apache 2.0
- **Stars:** ~0 (new repo)
- **Language:** TypeScript (98.9%)
- **Date:** April 27, 2026

## What it does
AI agent runtime security scanner that detects malicious behavior in Claude Skills, MCP Servers, Codex Plugins, and 6 more platforms. Scans TWO attack surfaces: **code surface** (file access, network calls, shell commands) and **instruction surface** (SKILL.md, AGENTS.md prompts for injection/manipulation). 268 detection rules across 18+ threat categories including credential harvesting, prompt injection, tool poisoning, data exfiltration, privilege escalation.

## Key Differentiators
- **Map + Monitor + Fix** — 3-layer architecture (static analysis → runtime policy → agent-readable remediation)
- Covers Claude Code Skills, MCP Servers, OpenAI Codex Plugins, Cursor Extensions, CrewAI, AutoGPT, OpenClaw Skills, Nanobot, Supabase
- Deterministic rule-based scanning (no LLM needed for core scan)
- Benchmark: 79% attack block rate on InjecAgent, 99.09% tool poisoning detection on MCP-SafetyBench
- **Runtime policy rules** — blocks dangerous commands before execution, not just detects

## Threat Categories Covered
credential-harvesting, data-exfiltration, tool-poisoning, prompt-injection, privilege-escalation, agent-identity-spoofing, supply-chain, access-control

## Solomon OS Fit
**INTEGRATE** — Runtime security for Hermes skill ecosystem. MCP server validation + runtime policy enforcement for Hermes Agent. Tool poisoning detection for third-party skills. Apache 2.0 = commercial-friendly.

## Comparison to Existing
- vs Medusa: More focused on agent runtime behavior (not just repo scanning)
- vs Snyk agent-scan: Covers more platforms (8 vs specific agents), includes runtime blocking
- vs hackmyagent: More mature (268 rules vs 209 static checks), benchmark-validated

## Status
**INTEGRATE** — Add as security layer for Hermes skill installation pipeline. MCP server validation before Hermes connects to external servers.
