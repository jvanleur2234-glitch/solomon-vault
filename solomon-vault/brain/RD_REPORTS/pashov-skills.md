# RD_REPORT: pashov/skills

**Date:** 2026-04-17
**URL:** https://github.com/pashov/skills
**Stars:** 610
**License:** MIT
**Tags:** solidity, security, auditing, ai-agents, claude-code, cursor, smart-contracts

---

## What It Is
AI-powered Solidity security audit skills built by Pashov Audit Group. Ships as a directory of structured agent prompts that work across multiple AI platforms (Claude Code, Cursor, Codex, GitHub Copilot, Windsurf). Two main skills:

1. **solidity-auditor** — Fast (~5 min) security feedback on Solidity code changes. Uses 8 parallel specialized hacking agents (vector-scan, math-precision, access-control, economic-security, execution-trace, invariant, periphery, first-principles) plus a dedicated FP-gate validation agent. Outputs findings in a structured report.

2. **x-ray** — Pre-audit threat modeling. Generates an `x-ray/` folder with: protocol overview, threat model, invariants, test gaps, git history, readiness verdict, entry-points analysis, and architecture diagrams.

Key architecture details:
- Versioned skills with local VERSION files and remote sync checks
- CI auto-bump for independent skill versioning
- FP gate: mandatory verification step before findings are promoted
- Attack vectors split into 4 files (~42 vectors each)
- Structured output format (entry/guards fields per finding)

---

## What We'd Use It For

Joseph's AI White-Collar Staffing Agency — having a structured audit skill like this demonstrates the kind of high-value specialized work AI agents can do. It also shows a mature multi-agent architecture (8 specialized agents + validation gate) that could inspire Solomon OS system design.

If Solomon OS ever attracts Web3/DeFi clients, a Solidity audit capability would be a premium service offering.

---

## How It Compares to What We Have

Solomon OS currently has:
- Russell Tuna (general-purpose AI worker)
- Hermes (skill-based agent routing)
- No specialized security auditing capability

Pashov/skills is the most mature open-source example of structured multi-agent security auditing. It contrasts with generic agent frameworks (like openai/openai-agents-python) by being domain-specific and deeply optimized for one task type.

---

## Recommendation

🟡 **SKILL** — Worth studying its architecture for Solomon OS agent design patterns. Forking or adapting the skill format for Web3 audit services could become a premium offering in the AI staffing agency. Not urgent but high strategic value if Web3 clients are in scope.

---

## X Posts (from Joseph's shared links this session)

1. **gethomepage/homepage** — trending GitHub repo (29.5K stars), self-hosted app dashboard
2. **pashov/skills** — Solidity audit skills, multi-agent security scanning framework
3. **siddharthvaddem/openscreen** — open-source screen recording tool, MIT, ~21.8K stars, trending this week
4. **Audi RS7** (t.co/RS7viwAwgw) — unresolved; likely unrelated to AI/business context
