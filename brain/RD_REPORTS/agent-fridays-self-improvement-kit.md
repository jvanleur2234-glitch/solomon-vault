# Agent Friday Self-Improvement Kit (FutureSpeakAI)

**Date:** 2026-04-26  
**Slug:** agent-fridays-self-improvement-kit  
**Category:** Self-Improvement  
**License:** MIT  
**Language:** TypeScript  
**Forked:** No (npm package)

## What it is
TypeScript framework-agnostic module for self-improving AI agents. Agent reads own source, generates diffs via `proposeChange()`, but requires human approval before writes. Extracted from Agent Friday project.

## Key Features
- **SelfImproveEngine**: read-only introspection + diff proposal
- **ApprovalHandler**: human-in-the-loop gate for all writes
- **Safety-first**: reads are autonomous, writes require approval
- **Framework-agnostic**: zero external dependencies
- **Install**: `npm install self-improving-agent`

## Key Architecture
```
SelfImproveEngine → proposeChange() → ApprovalHandler → (approve/deny) → hot-reload
```

## Relevance to Solomon OS / Hermes
Human-in-the-loop safety pattern is directly applicable to Hermes self-evolution. Could be a Hermes skill for supervised self-modification. TypeScript aligns with Hermes agent-core if rewritten in Python.

## Verdict
**SKILL** — Adopt the human-in-the-loop approval pattern for Hermes self-evolution. MIT licensed, clean safety architecture.