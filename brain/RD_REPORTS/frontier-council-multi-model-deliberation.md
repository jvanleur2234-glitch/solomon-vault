# Frontier Council — Multi-Model Deliberation Framework

**Forked:** https://github.com/jvanleur2234-glitch/frontier-council  
**Source:** https://github.com/terry-li-hm/frontier-council  
**License:** MIT  
**Stars:** ~N/A (new, March 2026)  
**Language:** Python  

## What It Is

Python deliberation framework where 4 frontier LLMs (GPT-5.2-pro, Gemini-3-pro-preview, Grok-4, Kimi-k2.5) debate a question in parallel, then Claude Opus 4.5 judges and synthesizes. Features: blind first-pass (anti-anchoring), rotating challenger, 2+ rounds with early-exit consensus, transcript save/share.

## What We'd Use It For

- High-stakes decision making in Solomon OS agent workflows
- "Council of advisors" before critical actions (client deployments, pricing decisions)
- Structured deliberation for JCPaid service recommendations

## Comparison to What We Have

- **vs. Quorum/AIBYAI/Agent Council:** Uses Claude as judge (unique synthesis role), cleaner CLI, blind first-pass anti-anchoring
- **vs. multi-agent-council (gabrielcnb):** Uses Perplexity Pro SSE — frontier-council uses OpenRouter multi-provider

## Recommendation

**SKILL** — MIT licensed, Python, straightforward pip install. Good fit as a Hermes tool for "consult the council" before major decisions. Lower priority than security/infrastructure repos.

## Key Files

- `README.md` — setup + usage
- `frontier_council/` — core library
- `cli.py` — CLI interface
