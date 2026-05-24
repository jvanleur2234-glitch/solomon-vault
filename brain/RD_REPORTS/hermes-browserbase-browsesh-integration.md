# RD Report: Hermes + Browserbase Browse.sh Integration

**Date:** 2026-05-24
**Type:** Competitor/Partnership Analysis
**Source:** https://x.com/JulianGoldieSEO/status/2058397577234817381

---

## What It Is

Hermes (NousResearch's open-source AI agent framework) now connects to **Browserbase's new Browse hub** — a skill marketplace with 100+ browser automation playbooks for specific websites and tasks.

Browse.sh is Browserbase's skill layer: plain-text `.md` skill files that give agents step-by-step playbooks for specific websites (LinkedIn, GitHub, Zillow, etc.) instead of making the model figure out every click.

---

## The Stack

| Layer | Technology | Our Equivalent |
|---|---|---|
| Agent brain | Hermes | Zo (Solomon OS orchestrator) |
| Cloud browser infra | Browserbase | agent-browser / OpenCLI |
| Site-specific skills | Browse.sh skills | here.now + Paperclip + custom skills |
| Vision | Built into Hermes | Vision API |
| Bundles | Skill bundles | The Agency (147-agent repo) |

---

## Key Competitive Insights

### What They Do Well

1. **Skill-based browser reliability** — instead of generic clicking, agents use curated playbooks. If a site breaks, update the skill file (not the model).
2. **100+ pre-built skills** — instant coverage for common sites out of the box.
3. **Skill marketplace** — agents can browse, preview, and install skills inside Hermes.
4. **Plugin architecture** — Hermes now has a browser provider registry. Third-party browser backends can be added by dropping a plugin folder into `~/.hermes/plugins/browser/`.

### Competitive Threat to JCPaid

| Factor | Hermes + Browse.sh | JCPaid |
|---|---|---|
| Monthly cost | ~$20-40 (Browserbase + Hermes) | $299 flat |
| Crypto required | Browserbase requires card | None |
| Desktop agent | Via Hermes OS | holaOS |
| Permanent memory | here.now (us) | Built-in |
| Skill editing | Browse.sh marketplace | Paperclip |
| Skill updates | Update skill file | Same |

**Bottom line:** Browse.sh IS the "skill updating" system we pitched. They beat us to the exact value prop on browser automation.

### Key Strategic Insight (From Julian Goldie)

> *"If a website breaks, you don't wait for the model to magically improve. You update the skill. Now your agent gets better forever. That's the difference between an AI tool and an actual agent system."*

This is EXACTLY what JCPaid/Solomon OS promised. They're articulate about it better than we are.

---

## Architecture Deep Dive

### Hermes Browser Provider Architecture (Latest)

Hermes migrated from in-tree browser modules to a plugin-based system:

```
~/.hermes/plugins/browser/
├── browserbase/     # Browserbase direct
├── browser_use/     # Browser Use (replaced Nous managed gateway)
└── firecrawl/       # Firecrawl
```

**Important update (PR #5750):** Hermes SWITCHED their managed gateway from Browserbase to **Browser Use** (not Browserbase). Direct Browserbase still works with API key. Our Hermes uses direct Browserbase.

### Browse.sh Skill Format

Skills are `.md` files with a simple structure:
- `SKILL.md` — skill metadata and instructions
- Playbooks written in plain text — agent reads and follows
- Can be installed via `bb skills install` or from within Hermes

### Our Current Hermes Setup

We use direct Browserbase with `BROWSERBASE_API_KEY`. This is still the "direct" mode that works. But Hermes now defaults to Browser Use as managed gateway. Our setup bypasses that entirely — which is fine.

---

## What We Can Do With This

### IMMEDIATE (Within Reach)

1. **Install Browse.sh skills in our Hermes** — Browse.sh skills are just skill files. We can install them into our Hermes plugin directory and use them for browser automation.
   ```bash
   bb skills install browse@browserbase  # Install browser skill
   # Or browse skill marketplace for specific sites
   ```

2. **Add Browser Use as a provider** — We could switch to Browser Use (free tier available?) as an alternative browser backend for variety.

3. **Study their skill format** — Browse.sh skills are plain text. We can learn from them to build better Paperclip skills for JCPaid.

### STRATEGIC (Differentiators We Still Own)

1. **Permanent memory** — Browse.sh solves browser reliability. Hermes solves agent orchestration. Neither solves persistent memory for clients. That's here.now + Paperclip.

2. **JCPaid business model** — $299/mo flat vs. pay-per-build (Browserbase is metered). For a client who wants "it just works forever," flat is better.

3. **holaOS** — Desktop agent that runs locally. Browse.sh/Hermes are cloud-only.

---

## Recommendations

| Action | Priority | Type |
|---|---|---|
| Clone Browse.sh skills repo, study format | 🟡 High | SKILL |
| Install Browse.sh browser skills into our Hermes | 🟡 High | INTEGRATE |
| Update JCPaid positioning around skill-based reliability | 🟡 High | STRATEGY |
| Write Compare to HermesOS/ Browse.sh in SOLOMON_OS.md | 🟢 Medium | DOCS |

---

## Files Referenced

- Hermes browser plugin arch: https://github.com/NousResearch/hermes-agent/issues/25214
- Browse.sh skills: https://github.com/browserbase/skills
- Hermes PR switching to Browser Use: https://github.com/NousResearch/hermes-agent/pull/5750
- Browser provider comparison: https://github.com/mudrii/hermes-agent-docs/blob/main/browser.md

---

*Report generated: 2026-05-24*
*Analyst: Zo (Solomon OS)*