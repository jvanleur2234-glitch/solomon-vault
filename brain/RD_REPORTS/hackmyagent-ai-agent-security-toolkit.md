# RD Report: hackmyagent — AI Agent Security Toolkit

**Date:** April 26, 2026  
**Author:** AIQ Scout  
**Status:** SKILL  
**License:** MIT (assumed)  
**Stars:** Active, v0.19.0 (2026-04-23)  

## What It Is
Security toolkit for AI agents that converts every artifact (skill, MCP config, system prompts, SOUL.md) into an Abstract Security Tree for semantic analysis. Combines static checks, adaptive red-teaming, adversarial payloads, behavioral simulation.

## Key Features
- 209 static checks across 44 categories (credentials, configs, governance, supply chain, sandboxing, CVEs)
- 29 NanoMind semantic checks analyzing Abstract Security Tree
- Adaptive red team: generates target-specific payloads, observes responses, adapts defenses
- 164 adversarial payloads (prompt injections, jailbreaks, data exfiltration, memory/policy exploits)
- Behavioral simulation: 20-probe suite to observe actual skill behavior
- Self-securing: startup integrity check, tampered binaries trigger QUARANTINE mode
- Quick start: `npx hackmyagent secure`

## Solomon OS Fit
SKILL — Red-teaming framework for Hermes skills. Self-securing startup pattern worth studying. 44 categories of static checks could inform AgentArmor Studio development.

## Action
- Already in workspace as hackmyagent
- Study Abstract Security Tree + semantic checks for AgentArmor Studio

## Links
- https://github.com/opena2a-org/hackmyagent