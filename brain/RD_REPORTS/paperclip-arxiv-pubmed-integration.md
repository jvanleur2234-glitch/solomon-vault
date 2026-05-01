# RD Report: Paperclip arXiv + PubMed Central Integration

**Date:** 2026-05-01
**Type:** Knowledge Infrastructure / Competitive Advantage
**Recommendation:** 🟢 NICE TO HAVE — not urgent, adds depth for research verticals

---

## What It Is

Paperclip by GXL / Stanford (James Zou lab) — scientific literature index for AI agents.

**New as of April 30, 2026:**
- Full papers from ALL of arXiv (machine learning, math, physics, q-bio)
- Full papers from PubMed Central (11M+ biomedical papers)
- 150M+ abstracts across thousands of journals/conferences/proceedings
- One-line LLM integration — `paperclip.load("query")` gives agent full context
- ~100x faster than web search, free

**Install:** paperclip.gxl.ai or `paperclip update`

---

## Why It Matters for JCPaid

**Already integrated:** Paperclip company generator (forked into workspace ✅)

**New vertical opportunity:** Medical, legal, financial, and scientific research clients
- Research agents that need literature access (bio, med, law, finance)
- Agents that need up-to-date scientific backing for client deliverables
- "100x faster than web search" = concrete performance claim

**Sales angle:**
> "Your AI research employee has access to 11M+ full-text scientific papers, 150M abstracts, updated continuously. Same-day literature review on any topic."

**Credibility:** Stanford + GXL backing = won't disappear or go paid-wall

---

## Implementation Path

1. Paperclip already in stack via paperclip-company-generator
2. Add `paperclip update` to JCPaid agent initialization script
3. Document as "Research Agent" add-on for relevant verticals
4. Install for first research-heavy client engagement

---

## Competitor Notes

- Perplexity AI — similar scientific search but cloud-only, paywalled
- Semantic Scholar — API access requires approval
- Paperclip = free, local, agent-native

---

## Status

- **In JCPaid stack:** Already integrated via paperclip-company-generator ✅
- **Priority:** 🟢 NICE TO HAVE — not urgent
- **Next step:** Document as "Research Agent" add-on in JCPaid service catalog
