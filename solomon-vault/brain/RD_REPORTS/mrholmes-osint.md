# RD Report: Mr.Holmes — OSINT Tool

**Date:** 2026-04-20
**Source:** https://github.com/Lucksi/Mr.Holmes
**Task ID:** mrholmes-osint-001

---

## What It Is

Mr.Holmes is a full OSINT (Open Source Intelligence) tool written in Python/PHP. Gathers information on:
- **Domains** — WHOIS, DNS, subdomains, hosting info
- **Usernames** — Cross-references across 200+ social platforms
- **Phone numbers** — Service discovery via email lookup
- **Google Dorks** — Advanced search for exposed documents, configs, passwords

**Stats:** 3.3K stars, 477 forks, GPL-3.0, 681 commits, active since 2021

## What It Does for Solomon OS / JackConnect

**Lead research before cold outreach.** Before Russell Tuna sends a cold email, Mr.Holmes can:
1. Look up a company's domain → find key contacts
2. Verify a prospect's username across social platforms
3. Find exposed emails via the email lookup feature
4. Use Google Dorks to find decision-maker names, LinkedIn profiles, news mentions

**For JackConnect workers:** When a job comes in for "cold email for real estate agent," the AI worker uses Mr.Holmes to research the agent's domain, find their LinkedIn, verify their email, then craft targeted outreach.

## Installation

```bash
git clone https://github.com/Lucksi/Mr.Holmes
cd Mr.Holmes
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 MrHolmes.py
```

Requires: WHOIS API key (free tier at whois.whoisxmlapi.com)

## Integration with Solomon OS

**Hermes skill:** `osint-research` — wraps Mr.Holmes for lead research
**Russell Tuna workflow:** Before any cold outreach job, run osint-research on target domain → gets contact info, social profiles, decision-maker names → feeds into email template

## Recommendation

**SKILL** — Clone to `/home/workspace/Skills/mrholmes/`

Clone: `git clone https://github.com/Lucksi/Mr.Holmes /home/workspace/Skills/mrholmes/`

**LINK fit:** ★★★★☆ — #lead-gen #cold-outreach #osint #solomon-guardian
**Priority:** Normal — useful for JackConnect outreach workflow

---

*Last updated: 2026-04-20*
