# Agency Agents Integration — Solomon OS
**Cloned:** April 18, 2026  
**Source:** github.com/msitarzewski/agency-agents (810K stars, MIT License)

## What We Have

The full repo is cloned at `/home/workspace/agency-agents/`.  
10 key templates copied to `brain/AGENT_TEMPLATES/`:

| File | Role | Business Use |
|------|------|-------------|
| `sales-account-strategist.md` | Post-sale expansion, QBRs, stakeholder mapping | Upsell existing clients |
| `sales-engineer.md` | Technical sales, demo engineering, proof-of-concept | Close complex deals |
| `sales-outbound-strategist.md` | Outbound prospecting, sequence building | Find new clients |
| `sales-proposal-strategist.md` | Proposal and RFP writing | Close deals faster |
| `marketing-seo-specialist.md` | Technical SEO, content clusters, link building | Grow organic traffic |
| `marketing-growth-hacker.md` | Growth loops, viral loops, acquisition experiments | Scale fast |
| `marketing-content-creator.md` | Multi-format content at scale | Fill content pipeline |
| `engineering-ai-engineer.md` | AI/ML implementation, prompt engineering, data pipelines | Deliver AI projects |
| `product-manager.md` | Roadmap, prioritization, stakeholder management | Run product ops |
| `support-support-responder.md` | Ticket handling, escalation, FAQ automation | Scale customer support |

Full repo also available at `/home/workspace/agency-agents/`:
- `engineering/` — 21 templates (frontend, backend, SRE, DevOps, security, data, mobile, solidity)
- `design/` — UI/UX, brand, motion, 3D, design systems
- `marketing/` — 40+ templates (SEO, social, paid media, China platforms, books, podcasts)
- `sales/` — 8 templates (account, deal, outbound, pipeline, proposal, discovery)
- `product/` — 5 templates (PM, sprint, feedback, nudge, trend)
- `support/` — 6 templates (responder, legal, finance, analytics, infra, exec summary)
- `strategy/` — Nexus coordination, playbooks, runbooks

## How to Use for AI Staffing Agency

### For Russell Tuna Bot (/fork command)
When a client hires an "AI Sales Rep" or "AI Marketer", pull the relevant template(s) and use them as the system prompt foundation for that forked agent session.

### For Hermes Router (S1/S2/S3)
Map jobs to the right agent template:
- S1 (intake) → identify role needed → route to correct template
- S2 (execution) → use template's workflow, tools, deliverables
- S3 (delivery) → quality check against template's success metrics

### For Zo Orchestrator
When Joseph asks to "find me 10 leads" or "run an SEO audit", reference the outbound-strategist or SEO-specialist template to execute with the same rigor a human expert would.

## Matching Agent Roles → Business Revenue Streams

| Client Need | Template(s) to Use |
|-------------|-------------------|
| Find me leads | `sales-outbound-strategist.md` |
| Run a cold outreach campaign | `sales-outbound-strategist.md` + `marketing-content-creator.md` |
| SEO audit + content strategy | `marketing-seo-specialist.md` + `marketing-content-creator.md` |
| Build me a feature | `engineering-ai-engineer.md` |
| Manage my roadmap | `product-manager.md` |
| Handle customer support | `support-support-responder.md` |
| Upsell my existing customers | `sales-account-strategist.md` |
| Technical sales support | `sales-engineer.md` |
| Write my proposals/RFPs | `sales-proposal-strategist.md` |
| Growth experiments | `marketing-growth-hacker.md` |

## Next Steps
1. **Build a Role Selector** — simple Telegram command that lets a client pick a role, then Russell Tuna instantiates the template and starts the job
2. **Template Shortlist** — narrow repo down to 20 highest-value roles for the staffing agency
3. **Custom Instructions** — inject Solomon OS system prompt prefix into each template so agents know they work for Joseph's AI business
4. **Hermes Integration** — add these as callable skills in Hermes Router
