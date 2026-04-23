# RD Report: Google Agent Skills — agentskills.io

**Link:** https://github.com/google/skills | 810 stars | Apache 2.0

**Date:** 2026-04-23

---

## What It Is

Google's official Agent Skills repository — "compact, agent-first documentation for a specific tech or task." Skills are a simple, open format for giving AI agents new capabilities and expertise. 28 commits, actively developed. Built on agentskills.io spec.

## Core Format

```npx skills add google/skills
```
Then select specific skills to install.

Each skill is a directory with:
- `README.md` — Agent-facing docs (triggers, instructions)
- `metadata.yaml` — Name, description, triggers, required tools

## Available Skills

| Category | Skills |
|----------|--------|
| **Cloud** | Gemini API, AlloyDB, BigQuery, Cloud Run, Cloud SQL, Firebase, GKE |
| **Recipes** | Google Cloud onboarding, auth, networking observability |
| **WAF** | Security, Reliability, Cost Optimization |

## Why This Matters for JCPaid

Google Skills validates the "skills" format we already use in Solomon OS AGENTS.md. Key insight from Yonkrui Su:
> "A lot of agent failures come from missing procedural context rather than missing model capability — packaging that context cleanly could go a long way."

Our AGENTS.md skills match this exact format:
- Trigger conditions
- Tool requirements  
- Step-by-step procedural context
- Output format expectations

## FORGE — Integrate into Solomon OS

1. Add Google Skills to JackConnect: `npx skills add google/skills` → select BigQuery/GKE/Gemini
2. Fork google/skills as `solomon-os/skills` → add our 7 RE agents as official skills
3. Publish at `solomon.os/skills` → agents install via `npx skills add solomon-os/skills`
4. Cross-runtime: skills.sh works with ANY agent runtime (our format = universal)
5. Badge it: "Built on Google Skills" → cross-promotion with Google

## Competitive Analysis

| Feature | Google Skills | Hermes Skills | Our AGENTS.md |
|---------|--------------|---------------|---------------|
| Format | Markdown + YAML | Markdown | Markdown |
| Install | `npx skills add` | `hermes install` | Manual |
| Trigger system | Yes | Yes | Yes |
| Cross-runtime | ✅ Universal | ❌ Hermes-only | ❌ Zo-only |
| Industry backing | Google | Nous Research | Us |
| Skills registry | 810 stars, 42 forks | Large ecosystem | Our internal |

## Business Impact

- **Badge opportunity:** "Powered by Google Skills" → credibility boost
- **Fork strategy:** Fork google/skills + add RE-specific skills → submit PR → 810-star repo backlinks to us
- **Format standard:** Align Solomon OS AGENTS.md with agentskills.io spec → our skills work with Google Skills tooling
- **Immediate action:** Fork google/skills, add our 7 RE agents as skills, publish as JCPaid Skills

## Recommendation

**FORGE IMMEDIATE.** Clone google/skills → add our 7 RE agent skills → publish as `jcp-aid/skills`. This gives us:
1. Cross-runtime compatibility (our skills work in any agent runtime)
2. Google backlink potential (if accepted)
3. Format validation (we're using the right abstraction)
4. Easy discovery (agentskills.io is becoming the standard registry)