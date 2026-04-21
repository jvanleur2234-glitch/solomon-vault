# RD Report: Ramsbaby/openclaw-self-evolving

**Date:** 2026-04-21  
**Slug:** openclaw-self-evolving  
**Category:** Self-Improving Agent  
**License:** Not specified  
**Language:** Shell + Python  

## What It Is
A self-evolving AI-agent workflow that analyzes its own logs to propose behavior improvements. Runs on weekly cadence. Uses shell + Python scripts (no LLMs, no external APIs).

## Key Features
- Scans session logs (JSONL) for patterns: retry loops, rule violations, user frustration
- Generates rule-change proposals (AGENTS.md or CLAUDE.md) with before/after diffs
- Human-in-the-loop: all proposed changes require human approval
- No API calls, no cloud dependencies, 100% local
- Filters out previously rejected proposals

## Relevance to Solomon OS
- **Interesting:** Log-based improvement loop — lightweight version of what Solomon OS could implement
- **Low priority:** Shell-based, less sophisticated than other self-improvement approaches
- **License unclear:** Needs verification

## Verdict
**SKILL** — Lightweight log-based improvement pattern. Study for ideas, don't fork until license confirmed.

## Priority
🟢 Nice to have