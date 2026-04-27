# BUSINESS IDEA SCOUT — Solomon OS

> Scours X and YouTube for AI business opportunities, side hustles, and passive income ideas. Distills into actionable reports.

## What It Does
1. Searches X (Twitter) for trending AI side hustle + passive income posts
2. Searches YouTube for business idea videos
3. Saves raw findings to `brain/BUSINESS_SCOUT/`
4. Writes a distilled report to `brain/BUSINESS_SCOUT_REPORT.md`
5. Tags ideas by effort level and income potential

## Run Schedule
- Every 6 hours via Solomon Heartbeat or Zo automation
- Can be triggered manually: `queue: business scout` or `jump: business scout`

## Output Files
- `solomon-vault/brain/BUSINESS_SCOUT/raw_YYYY-MM-DD.md` — raw findings
- `solomon-vault/brain/BUSINESS_SCOUT_REPORT.md` — distilled report

## Scout Search Queries (rotate)
```
X/Twitter:
- AI side hustle passive income 2026
- solo business idea $1000/month easy to start
- sell AI service side income beginner
- passive income business 2026 no money down
- AI tools for freelancers 2026

YouTube:
- AI side hustle passive income 2026
- easiest passive income business 2026 beginner
- make money online AI 2026
- passive income ideas for beginners 2026
```

## Scoring Criteria
| Score | Label | Criteria |
|-------|-------|---------|
| 5 | 🔴 Kill | New AI paradigm or competitor |
| 4 | 🟡 Note | Interesting but no immediate fit |
| 3 | 🟢 Scout | 1K-10K mentions, clear Solomon OS fit |
| 2 | 🔵 Forge | Good fit + we can build it fast |
| 1 | ⚡ Execute | Already have the tools, run now |

## Report Format
```
# BUSINESS IDEA SCOUT REPORT — YYYY-MM-DD

## Top Opportunities This Cycle
1. [Name] — [1-line description]
   - Effort: Low/Med/High
   - Income Potential: $X-$Y/month
   - Solomon OS Fit: Why it works for us
   - Next Action

## X Trends Summary
[3 most recurring themes from X]

## YouTube Summary
[Best video findings]

## Recommendations
[Top 3 ranked by ease × income potential]
```