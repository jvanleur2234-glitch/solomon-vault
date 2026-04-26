# AIBYAI — Multi-Agent Deliberative Platform

**Date:** 2026-04-26  
**Slug:** aibyai  
**Category:** Multi-Agent Deliberation  
**License:** MIT  
**Language:** TypeScript (React, Fastify, PostgreSQL, Redis)  
**Stars:** ~400 (est.)  
**Forked:** Yes (`jvanleur2234-glitch/aibyai`)

## What it is
Multi-agent platform where 4+ AI agents argue, critique, and reach consensus with a **quantified confidence score**. Modules: Empiricist, Strategist, Historian, Skeptic. Conflict Detector analyzes pairwise claims. Cold Validator checks for hallucinations.

## Key Features
- **Multi-agent conflict detection**: pairwise claim analysis
- **Quantified confidence score** per answer
- **Reliability-weighted synthesis** (synthesizer merges results)
- **Cold Validator**: hallucination detection on final output
- **Cross-topic memory** via topic graph
- **Cost breakdown** per query

## Architecture
```
User Query → Route to Providers (parallel)
→ Each Agent generates claims + confidence
→ Conflict Detector (pairwise analysis)
→ If significant contradictions → agents receive critiques
→ Synthesizer (reliability-weighted merge)
→ Cold Validator (hallucination check)
→ Verdict with numeric score + cost breakdown
```

## Relevance to Solomon OS / Hermes
Quantified confidence scoring + conflict detection is a sophisticated deliberation pattern. Could inform Hermes agent-verification layer. PostSQL/Redis stack requires hosting.

## Verdict
**SKILL** — Study the conflict detection + confidence scoring for Hermes deliberation. The Cold Validator hallucination check is particularly valuable for agent reliability.