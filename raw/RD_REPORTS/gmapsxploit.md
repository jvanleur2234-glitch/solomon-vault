# RD Report: GmapsXploit

**URL:** https://github.com/DeathShotXD/GmapsXploit  
**Submitted by:** @akaclandestine (Clandestine, security researcher) via Telegram  
**Date:** 2026-04-19  
**Stars:** ~400 (est.)  
**License:** MIT  
**Stars velocity:** New, no trend data

---

## What It Is

Bash script that audits exposed Google API keys for bug bounty hunters. Tests 30+ Google Cloud endpoints to prove real financial impact, converting "low severity" API key exposures into critical findings.

**Core workflow:**  
1. Input a Google API key  
2. Script checks restrictions (IP, referrer limits)  
3. Tests 30+ premium APIs (Places, Gemini, Firebase, Vision, etc.)  
4. Calculates financial impact per 100k requests  
5. Outputs a ready-to-submit markdown report

---

## What We'd Use It For

1. **Solomon Guardian — API key exposure scanning**  
   Part of the autonomous security agent. GmapsXploit methodology can be incorporated into Guardian's API scanning module.

2. **AI Staffing Agency — security audit offering**  
   Add as a complementary finding tool in penetration testing deliverables.

3. **Educational reference**  
   Study how it structures billing impact calculations for API key vulnerabilities.

---

## Comparison to Existing Tools

- **Overlaps with:** apikey-gp (similar concept, fewer endpoints)  
- **Unique:** Gemini GenAI endpoint testing, financial impact calculations, report generation  
- **Quality:** Clean bash script, no external deps, MIT licensed

---

## Recommendation: SKILL

**Why SKILL not FORGE:**  
- It's a bash script, not a framework we'd build on top of  
- We can integrate its methodology into Solomon Guardian's API scanning  
- Forking it adds maintenance burden for minimal gain  
- SKILL = study the pattern (billing impact + report gen) and integrate into Guardian

**What to do:**  
1. Read the script in detail  
2. Extract the billing calculation methodology  
3. Integrate into Solomon Guardian's API exposure module  
4. Add to `brain/Services.md` under security offerings

**Action:** Clone to `/home/workspace/Skills/gmapsxploit/` and document integration plan.

---

## Notes

- Posted by Clandestine (@akaclandestine) — OSINT/threat intel researcher, credible source  
- The tool is real and functional, MIT licensed  
- Bug bounty community is actively sharing it as of April 2026  
- Could complement Clearwing (already in queue) in a security toolkit