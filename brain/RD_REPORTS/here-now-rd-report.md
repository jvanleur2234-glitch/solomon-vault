# RD Report: here.now — Instant Web Hosting for Agents

**Date:** April 29, 2026  
**Tag:** `queue:here-now`  
**Source:** https://here.now/  
**Priority:** 🟡 Worthwhile  

---

## What it is

here.now is a cloud hosting service designed specifically for AI agents. Publish any file or folder to a live `<slug>.here.now` URL in seconds via a simple REST API — no account required (anonymous sites last 24h), free permanent sites with sign-up. Powered by Cloudflare's global edge network.

**Core API flow:**
1. `POST /api/v1/publish` → returns presigned upload URLs + live site URL
2. Upload files directly to presigned URLs (parallel OK)
3. `POST .../finalize` → site goes live

---

## What we'd use it for

### 1. Instant client deliverables (HIGH VALUE)
Generate a report, audit, or dashboard → publish to here.now → send link to client in minutes. No Zo Site setup needed. Password protection built in for sensitive content.

### 2. Sales proposals + pitch decks
Build HTML proposal → publish with payment gating (Tempo stablecoins) → client pays to access. Native crypto payments without Stripe.

### 3. Rapid prototyping for client sign-off
Spin up a prototype in seconds, share link, get feedback, then build properly on Zo Space. Fast feedback loop.

### 4. Solomon Browser findings pipeline
Playwright-based research → publish results to here.now → client views instantly. Great for SEO audits, competitive analysis, market research reports.

### 5. Share large filesoutputs
CashClaw audit results, job outputs, RENU API query results — publish as a site with auto-gallery viewer for images/PDFs/videos.

### 6. Backup/archival
Publish important outputs redundantly to here.now (permanent with free account).

### 7. Agent-to-agent context sharing
Use here.now Drives to share memory/context between Zo and Russell Tuna sessions.

### 8. Replace simple static hosting
For one-off static needs (not ongoing sites), here.now is instant vs creating a Zo Site.

---

## How it compares to what we have

| | here.now | Zo Space | Zo Sites |
|---|---|---|---|
| Speed to live URL | **Seconds** | Seconds | Minutes |
| No account needed | ✅ (24hr) | ❌ | ❌ |
| Custom domain | ✅ (paid) | ❌ | ✅ |
| Payment gating | ✅ (Tempo crypto) | ❌ | ❌ |
| Password protection | ✅ | ❌ | Via auth |
| Agent-native API | ✅✅ | Partial | Partial |
| Proxy/API routes | ✅ (server-side creds) | ✅ | ✅ |
| Drive storage | ✅ | ❌ | ❌ |
| Forkable sites | ✅ | ❌ | ❌ |

here.now is not a competitor — it's a **complement**. Use it for:
- Speed-first static publishing
- Payment-gated content
- Agent-to-agent file sharing
- Quick client deliverables

Use Zo Space/Sites for:
- Persistent branded presence
- Custom domains + SSL
- Complex apps + API routes
- Authenticated user experiences

---

## What to build

1. **here.now skill** for Hermes — `hermes here-now publish <file-or-dir>` → returns live URL
2. **CashClaw → here.now bridge** — `cashclaw audit --url X --tier standard` → publish results to here.now
3. **Solomon OS publish command** — `solomon publish <type> <content>` → creates + uploads + returns URL
4. **Drive integration** — back up Solomon OS brain files to here.now Drives automatically

---

## Recommendation

**SKILL / INTEGRATE** — Install here.now skill on Hermes. It fills the "instant publish" gap in the stack. Particularly powerful for the AI Employee Agency model where you need to quickly share deliverables with clients. Zero friction — no infrastructure to manage.

**Priority build:** here.now skill for Hermes + CashClaw audit → here.now publish pipeline.

---

## Risks / Notes

- Anonymous sites expire in 24h — need free account for permanent links
- Payment gating uses Tempo stablecoins — niche, may not fit all clients
- No built-in analytics — just hosting
- Not a replacement for Zo Space/Sites — different use cases