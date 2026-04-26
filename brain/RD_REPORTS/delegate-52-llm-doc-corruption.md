# RD Report: DELEGATE-52 — LLMs Corrupt Your Documents When You Delegate

**Source:** https://arxiv.org/abs/2604.15597 (Microsoft Research, April 2026)  
**Type:** Research Paper / Benchmark  
**Handling:** queue: — analyzed as R&D research  
**Date:** 2026-04-25

---

## What It Is

Microsoft Research introduced **DELEGATE-52**, a benchmark simulating long document-editing workflows across 52 professional domains (coding, crystallography, music notation, etc.). It tests whether LLMs can faithfully execute delegated tasks without corrupting documents over extended interactions. 19 models were tested.

**Key Findings:**
- Even frontier models — **Gemini 3.1 Pro, Claude 4.6 Opus, GPT-5.4** — corrupt an average of **25% of document content** by the end of long workflows
- Agentic tool use does NOT improve performance
- Degradation worsens with: larger documents, longer interactions, and presence of distractor files
- Errors are "sparse but severe" — they silently compound over time
- Current LLMs are classified as **unreliable delegates** in long-running document editing

---

## What We'd Use It For

1. **Hermes reliability framework** — this is directly relevant to the document corruption problem. If Hermes Agent handles document editing, long-form writing, or code generation, we need explicit versioning/checkpointing layers to prevent silent corruption. This benchmark gives us hard numbers to design against.

2. **Hermes Capable system** — any workflow where Hermes operates on files long-term needs a corruption prevention layer (version snapshots, diff checks, human-in-the-loop milestones, not just "better prompts").

3. **Product positioning** — if we ever position Hermes as a "delegation engine," this paper is a counterpoint every client will raise. Better to lead with it: "We built Hermes to solve the document corruption problem that DELEGATE-52 identified."

4. **Competitor intel** — this is damning for all LLM-based agents in the market right now. It's a forcing function for the industry to build the protection layers we could offer.

---

## How It Compares to What We Have

This is **not yet reflected in the Hermes architecture**. Current Hermes workflows don't have explicit document versioning or corruption detection between steps. This paper validates building those safeguards in.

---

## Recommendation

**🟡 Worthwhile** — The benchmark itself isn't a tool we "integrate," but the findings are essential context for how we design Hermes workflows and how we talk to clients about reliability. Store in brain/Research/ with high priority. Reference when designing any document-editing capability.

---

## Action Items

- [ ] Update Hermes Capable architecture with checkpointing/versioning for long document workflows
- [ ] Note in Hermes Capable: "Solves the DELEGATE-52 problem" as a differentiator
- [ ] Consider adding a "corruption detection" step to Hermes task loops (diff outputs at milestones)