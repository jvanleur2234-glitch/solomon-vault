# Skill Store — Solomon OS Marketplace

## Concept
Marketplace where people buy/sell AI skills for their businesses.
A skill = a folder of markdown + scripts that teaches any AI agent how to do a specific job.

## Core Idea
"I figured out how to do [JOB] the right way. Now my skill is in the store. You buy it, install it, and your AI agent can do [JOB] like I do."

## What's Already Built
- JackConnect = real estate skill library (7 agents)
- Watch Once = skill extractor (watches human do task, packages it as automatable skill)
- Solomon OS = runtime that runs skills
- Bonsai WebGPU page = edge runtime (runs in browser anywhere)

## What to Build
- Skill Store marketplace page
- Skill upload/publish flow
- Skill install for JackConnect
- Payment integration via Stripe
- Skill ratings/reviews
- Industry categories

## Business Model
- Skills priced $5-$50 one-time or $2-5/mo subscription
- Solomon OS takes 30% cut
- Creator keeps 70%

## Pages to Build
1. /skill-store — browse all skills
2. /skill-store/[category] — filter by industry
3. /skill-store/[skill-id] — skill detail + buy/install
4. /skill-store/publish — upload a new skill
5. /skill-store/my-skills — manage purchased + created

## Skill Format
```
real-estate-cma/
├── SKILL.md           ← name, description, price, category
├── README.md          ← what it does, how it works
├── references/        ← domain knowledge, rules
│   └── local-market-data.md
├── scripts/           ← executable actions
│   └── generate_cma.py
└── tests/             ← validation cases
    └── test_cma.py
```

## Integration Points
- Watch Once → skill extractor → publish to store
- JackConnect → install skill from store
- Stripe → payments
- Hermes → skill registry

## Status
PLANNING — started April 16, 2026
