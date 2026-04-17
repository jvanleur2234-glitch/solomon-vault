# RD REPORT: Open Lovable (firecrawl/open-lovable)

**Date:** April 10, 2026  
**Stars:** 25K ⭐ (GPL-3.0)  
**URL:** https://github.com/firecrawl/open-lovable  
**Priority:** 🟡 Worthwhile (interesting tech, not urgent)

---

## WHAT IT IS

Open Lovable is an open-source AI app builder — give it a URL and it clones the site as a modern React app. Think " screenshot-to-code" but with full React code output, live preview, and an iterative edit loop. Built by the Firecrawl team as an open reference implementation of Lovable.dev.

**Stack:**
- Next.js 15 + TypeScript + Tailwind + shadcn/ui
- Firecrawl (website scraping → structured markdown)
- Vercel Sandbox or E2B (runtime for the generated code)
- Morph (fast AI-powered code edits)
- AI providers: Gemini, Claude, GPT-4, Groq

**How it works:**
1. User pastes a URL
2. Firecrawl scrapes it → clean markdown with images
3. AI generates a new React app from the scraped content
4. App deploys to a Vercel sandbox URL
5. User chats with AI to iteratively edit ("make it darker", "change the CTA")
6. Morph applies targeted code changes

---

## WHAT WE'D USE IT FOR

### For Zo Space / web agency work:
The core use case — "turn any reference website into deployable React code" — is exactly what zo.space needs. If we had a Firecrawl-powered scraper feeding into zo.space route generation, Joseph could:
- Show a competitor's site → get a Zo Space version in minutes
- Describe a design in plain English → generate a full landing page
- Turn a screenshot into working React code

### Side business angle:
A "website cloning as a service" agency — businesses pay to have their competitors' designs recreated as modern React apps, or to have mockups built from screenshots/descriptions. The tech exists, it's just a matter of packaging and client acquisition.

---

## HOW IT COMPARES TO WHAT WE HAVE

| | **Open Lovable** | **Zo Space** |
|---|---|---|
| AI to build site | ✅ | ✅ (via prompts) |
| From URL/screenshot | ✅ | ❌ |
| Iterative editing | ✅ | Manual |
| Free / self-hosted | ✅ | ✅ |
| Full React app output | ✅ | Limited to routes |

Zo Space is a managed React host — it doesn't generate the React code itself. Open Lovable is a code generator that deploys to Vercel. Different layers of the stack.

---

## INTEGRATION PATH FOR SOLOMON OS

**Option A — Quick win (low effort):**
Install Open Lovable locally, use it as the "code generation engine" for zo.space projects. Feed the generated React code into zo.space routes. Manual but functional.

**Option B — Full integration (medium effort):**
- Add Firecrawl to Zo's skills (scrape any URL → structured data)
- Build a zo.space route that accepts a URL, calls Firecrawl, then uses Zo API to generate React code, then deploys as a zo.space site
- This becomes a "build me a site like X" feature in Solomon OS

**Option C — Side business:**
Spin up Open Lovable as a hosted service (Vercel + Firecrawl + Claude). Sell "website cloning and redesign" as a service. $500-2K per project depending on complexity.

---

## RECOMMENDATION

**SKIP as a standalone product. INTEGRATE the key piece (Firecrawl + AI code gen) into zo.space.**

The most valuable part of Open Lovable for Solomon OS is **Firecrawl** — the scraping + structure engine. The Vercel sandbox + Morph edit loop is less relevant since we have zo.space.

**Immediate next step:** Add Firecrawl to the AI Arsenal. Then test whether we can feed scraped content into zo.space route generation.

Side business angle is real but crowded — every AI agency is now offering "we'll clone any website." Better to own the toolchain than compete on the service.
