# RD Report: LLM Council (llmcouncil)

**Fork:** https://github.com/jvanleur2234-glitch/llmcouncil
**Source:** https://github.com/rachittshah/llmcouncil
**License:** MIT
**Language:** TypeScript
**Stars:** ~900 (estimated, growing)

## What It Is
MCP server + Claude Code skill for multi-LLM deliberation via structured protocols. Fan-out to GPT-5.4, Gemini 2.5 Pro, Claude Sonnet 4.6 in parallel → combine via voting, debate, synthesis, critique, red-teaming, or MAV (Model as Verifier).

## Key Features
- **6 protocols:** vote, debate (KS adaptive stopping), synthesize (chairman), critique, red-team, MAV
- **Peer broker/discovery** for distributed operation
- **Cost estimation** per protocol run
- **MCP tools:** council_deliberate, council_vote, council_debate, council_critique, council_verify, council_redteam

## Solomon OS Fit
**INTEGRATE** — Council of High Intelligence implementation. 6 protocols give structured multi-agent deliberation. MAV (multi-agent verification) directly maps to adversarial skill validation. MIT license permits use.

## Comparison to Existing
- More protocols than yogirk/agent-council (which has 3 agents, simpler)
- Structured verification (MAV) vs simple voting
- Better for production deliberation workflows

## Action
Forked. Study MAV protocol for adversarial testing in Hermes skill validation.

**Recommendation:** INTEGRATE into Council of High Intelligence