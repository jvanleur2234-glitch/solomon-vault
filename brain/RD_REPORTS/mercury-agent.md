# RD Report: Mercury Agent by CosmicStack Labs

**Date:** 2026-04-22
**Source:** https://x.com/GithubProjects/status/2046952182076018913 | https://github.com/cosmicstack-labs/mercury-agent

---

## What It Is

**Mercury Agent** builds on OpenClaw + Hermes, adding strict CONTROL layers:
- Token-efficient by design
- Strict budget guardrails
- Dangerous commands blocked
- Editable "Soul Files" for predictable AI behavior

**The quote:** "OpenClaw sparked the Idea. Hermes brought the Energy. Mercury now delivers true CONTROL."

**Engagement:** 558 likes, 64 reposts, 831 bookmarks — very high for a new repo.

---

## For Our Stack

**Relevance to Solomon OS / JCPaid:**
- Soul files = Solomon OS personality/identity files
- Token budgets = missing piece in our agent permission system
- Hardened permissions = fits JackConnect Clicky trust model
- Pipelock architecture referenced by security commenters — external control outside agent

**Key security point from comments:**
"Control gets fuzzy the second the agent can hit tools/browsers/APIs on its own. If the agent is allowed to police itself, you are trusting the thing under attack to explain why its own actions were fine. Pipelock puts that control outside the agent and watches actual traffic."

**This validates our AgentArmor integration spec.**

---

## Verdict

**FORGE** — Mercury Agent's Soul Files + Token Budget architecture directly maps to JackConnect Clicky permission system. The external pipelock security model is what we need for the trust-building approval flow.

**Next step:** Clone mercury-agent, study Soul Files implementation, integrate into JackConnect desktop app permission layer.