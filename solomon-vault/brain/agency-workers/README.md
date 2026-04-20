# Agency Workers Library
**Source:** msitarzewski/agency-agents — 60K+ GitHub stars, MIT License
**Cloned:** April 18, 2026
**Location:** `/home/workspace/solomon-vault/brain/agency-workers/`

## What Is This?
147 specialized AI agents from "The Agency" repo — each with personality, workflows, success metrics, and production-ready code examples. These are Solomon OS's **hireable worker templates**. When a client hires an AI worker, they get one of these personas.

## Current Roster (17 Workers)

### Engineering Division
| # | Agent | Use Case |
|---|-------|----------|
| 01 | Frontend Developer | React/Vue/Angular, UI implementation, Core Web Vitals |
| 02 | Backend Architect | API design, database architecture, scalability |
| 03 | DevOps Automator | CI/CD, infrastructure automation, cloud ops |

### Marketing Division
| # | Agent | Use Case |
|---|-------|----------|
| 04 | Content Creator | Multi-platform campaigns, brand storytelling, SEO content |
| 05 | SEO Specialist | Search optimization, keyword strategy, traffic growth |
| 06 | Social Media Strategist | Platform strategy, engagement optimization, community building |

### Sales Division
| # | Agent | Use Case |
|---|-------|----------|
| 07 | Outbound Strategist | Signal-based prospecting, ICP definition, multi-channel sequences |
| 08 | Pipeline Analyst | CRM diagnostics, revenue forecasting, deal health scoring |

### Finance Division
| # | Agent | Use Case |
|---|-------|----------|
| 09 | Bookkeeper Controller | AP/AR, reconciliation, financial reporting, cash flow |

### Support Division
| # | Agent | Use Case |
|---|-------|----------|
| 10 | Analytics Reporter | Support metrics, CSAT analysis, service reporting |
| 11 | Executive Summary Generator | Board-ready summaries from raw data |
| 12 | Finance Tracker | Budget tracking, expense categorization, financial health |
| 13 | Infrastructure Maintainer | System uptime, monitoring, incident response |
| 14 | Legal Compliance Checker | Policy review, regulatory compliance |
| 15 | Support Responder | Ticket triage, FAQ responses, customer resolution |

## How to Use These as Hireable Workers

### For Russell Tuna (Telegram AI Worker)
Russell Tuna can adopt any of these personas on command:
```
@RussellTuna — activate as [Agent Name]
```
Example: `@RussellTuna — activate as Outbound Strategist and design a prospecting sequence for SaaS CTOs`

### For Solomon OS Staffing Agency
Each agent file contains:
- **Identity & personality traits** — unique voice and communication style
- **Core mission & workflows** — battle-tested processes
- **Technical deliverables** — real code, templates, success metrics
- **Success metrics** — measurable outcomes (e.g., "25% engagement rate", "5:1 ROI")

### Converting to Russell Tuna Format
The frontmatter (name, description, color, emoji, vibe) maps directly to Russell Tuna's persona system. The markdown body becomes the system prompt.

## Quick Activate Examples

**"Hire a Content Creator"**
→ Load `04-content-creator.md` → creates editorial calendars, writes copy, manages brand storytelling

**"Hire an Outbound Strategist"**  
→ Load `07-outbound-strategist.md` → signal-based prospecting, ICP definition, multi-channel sequences

**"Hire a Bookkeeper"**
→ Load `09-bookkeeper-controller.md` → AP/AR, reconciliation, P&L, cash flow forecasting

**"Hire a Pipeline Analyst"**
→ Load `08-pipeline-analyst.md` → MEDDPICC scoring, deal health, revenue forecasting

## Commercial Model
These become the **product catalog** for Solomon OS's AI Staffing Agency:
- Freelancers: $50-200/hr for specialized agents
- Agencies: $500-5000/mo for dedicated AI workers
- Each agent is a line item on an invoice

## Next: Add More Agents
Still in the repo to integrate:
- `engineering/engineering-ai-engineer.md` — ML models, data pipelines
- `engineering/engineering-security-engineer.md` — threat modeling, secure code review
- `marketing/marketing-growth-hacker.md` — viral loops, acquisition funnels
- `marketing/marketing-reddit-community-builder.md` — Reddit organic growth
- `sales/sales-account-strategist.md` — account-based sales strategy
- `finance/finance-financial-analyst.md` — financial modeling, valuation
- `game-development/*` — game dev agents (niche but high-value)

## Full Repo
Source: `https://github.com/msitarzewski/agency-agents`
MIT License — free to use, modify, commercialize
