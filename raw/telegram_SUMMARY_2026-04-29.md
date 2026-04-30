# Telegram Session Summary — 2026-04-29

**Date:** Wed Apr 29, 2026
**Session Duration:** ~1 hour (9:01 PM - 9:59 PM CDT)
**Channel:** Telegram DM

---

## Key Decisions Made This Session

1. **PIVOT from HVAC Lead Machine to JCPaid AI Employee Agency**
2. **Channel partner model** — use great AI tools, sell them to local businesses, keep the margin
3. **JCPaid landing page** built at https://josephv.zo.space/jcpaid — sells "AI Employee Agency" flat $500/mo
4. **Department packaging** — sell Sales, Marketing, HR, IT, Finance, Support AI employees as add-ons
5. **Bundle pricing** — 2 depts = $900, 3 = $1,300, all 6 = $2,200
6. **White-label hidden Sauna model rejected** — transparent channel partner approach is cleaner
7. **Stack pivot from Sauna.ai to Paperclip + Hermes + Hermes Workspace** — fully open source, MIT license, zero per-seat costs
8. **hermes-paperclip-adapter** found — official bridge from Nous Research, runs Hermes as Paperclip employee
9. **Hermes Workspace** released — native web UI for Hermes, makes it accessible to non-technical clients

## New Repos Cloned / Analyzed This Session

| Repo | What It Is | Status |
|---|---|---|
| paperclipai/paperclip | AI company orchestration (org chart, tasks, budgets) | Clone now |
| NousResearch/hermes-paperclip-adapter | Run Hermes as Paperclip employee (1K stars, MIT) | IMMEDIATE FORGE |
| outsourc-e/hermes-workspace | Native web UI for Hermes (just released TODAY) | IMMEDIATE FORGE |

## Code Created / Modified

| File | Change |
|---|---|
| /jcpaid (zo.space route) | Full JCPaid landing page with department selector + bundle pricing |
| /home/workspace/ACTIVE_CONTEXT.md | Updated with new JCPaid model + Paperclip stack |
| /home/workspace/solomon-vault/brain/RD_REPORTS/hermes-paperclip-adapter.md | RD report |
| /home/workspace/solomon-vault/brain/RD_REPORTS/hermes-workspace.md | RD report |

## Business Model — JCPaid AI Employee Agency

**The pitch:** "Anything you hate doing — we automate it with AI. Flat $500/month. Cancel anytime."

**Per client economics:**
- Cost to run: ~$0 (self-hosted Paperclip + Hermes, API costs passed through or capped)
- Price: $500-2,200/mo depending on departments
- We pocket the difference

**How it works:**
```
Client → JCPaid (contract) → Paperclip (company setup) → Hermes (AI employee)
                         → Hermes Workspace (client dashboard) → Reports back
```

**The moat:** Client relationship + pre-built workflow templates per vertical (real estate, HVAC, etc.)

## Unresolved Issues

- Need to actually set up Paperclip + Hermes + Hermes Workspace on sandbox
- Need first client (Jack Vanleur — real estate agent)
- API costs need to be understood and capped per client

## Next Steps (Priority Order)

1. **Clone and set up Paperclip** — paperclip.ai/paperclip
2. **Clone hermes-paperclip-adapter** — NousResearch/hermes-paperclip-adapter
3. **Clone Hermes Workspace** — outsourc-e/hermes-workspace
4. **Get Groq API key** for free inference (backup to paid APIs)
5. **Test with Jack Vanleur** — first real estate client demo
6. **Share JCPaid landing page** with potential clients