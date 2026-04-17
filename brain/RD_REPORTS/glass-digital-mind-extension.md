# RD Report: Glass by Pickle — Digital Mind Extension

**URL:** https://github.com/pickle-com/glass  
**Stars:** 7.4k  
**License:** GPL-3.0  
**Tech Stack:** Electron + JavaScript/TypeScript, Next.js, Tailwind CSS  
**Date Added:** 2026-04-15  
**Queue Priority:** normal  
**Type:** rd-research  
**Tags:** `[screen-capture]` `[AI-context]` `[meeting-notes]`

---

## What It Is

Glass is a desktop AI companion that continuously watches your screen and listens to your audio in real-time. It transforms everything you see and hear into structured knowledge — like a photographic memory you can query at any time. It also has proactive meeting features: real-time notes, summaries, and action items during calls.

**Key capabilities:**
- `Ctrl/Cmd + Enter` — ask AI questions using ALL previous screen content and audio as context
- Continuous screen + audio capture, stored locally
- Real-time meeting notes with live summaries
- Proactive answers surfaced without being asked
- Stays invisible during screen recordings (no dock icon, not visible in screenshots)
- Supports OpenAI, Gemini, Claude APIs, plus local Ollama + Whisper

---

## How It Compares to Our Setup

| Capability | Glass | Our Stack (Jack Connect + Clicky + Screenpipe) |
|---|---|---|
| Screen capture | ✅ | Screenpipe does this |
| Audio capture | ✅ | Clicky does this |
| Local storage | ✅ | Screenpipe has local DB |
| AI query on captured data | ✅ | Russell Bot does this |
| Meeting notes | ✅ | Not currently done |
| Invisible in recordings | ✅ | Not a current feature |
| Trigger by keyboard shortcut | ✅ | Can build with our infra |
| Proactive surfacing | ✅ | We don't have this |

---

## Integration Opportunities for Jack Connect

Jack Connect is Joseph's real estate CRM (leads, deals, tasks for his brother Jack). Here's how Glass could augment it:

### Opportunity 1: Auto-Capture Client Calls
Glass captures meeting audio and screen context. If Jack is on a call with a lead, Glass could:
- Auto-generate call notes → post to Jack Connect as deal notes
- Extract action items → create tasks in Jack Connect
- Flag Deal_001 appraisal status from conversation

### Opportunity 2: Context-Aware Real Estate Assistant
When Jack is in MLS, Zillow, or real estate portals, Glass watches and learns. It could surface:
- "You're looking at a property similar to what Marcus Chen wants"
- "Sarah Johnson asked about this neighborhood last week"
- Flag properties matching high-priority leads in Jack Connect

### Opportunity 3: Meeting Intelligence
Jack has a deal closing 2026-04-14 (123 Main St) and 2026-04-16 (456 Oak Ave). Glass could:
- Auto-prep context before meetings
- Record and summarize walk-throughs
- Generate follow-up tasks automatically

### Opportunity 4: Invisible During Showings
When Jack screen-records a home tour, Glass stays invisible. Useful for training content or client previews.

---

## Technical Integration Path

```bash
# Clone Glass
cd /home/workspace
git clone https://github.com/pickle-com/glass.git

# Key files to explore:
glass/src/           # Main electron source
glass/functions/     # Cloud functions (Firebase)
glass/pickleglass_web/ # Next.js frontend

# Glass stores captured data locally in SQLite or similar
# We could write a connector that mirrors relevant context to Jack Connect
```

**Alternatives considered:**
- Screenpipe (we have it) already does screen capture with local DB
- Glass adds: invisible capture, proactive meeting notes, unified query across screen+audio
- The real value-add is the **proactive meeting intelligence** layer

---

## Recommendation: SKIP (for now)

**Reasoning:**
1. Glass runs as a **desktop Electron app** — requires user sitting at a Mac/Windows machine. Our infra is server-side.
2. Screenpipe already does continuous screen capture with local DB — overlapping functionality.
3. The unique value of Glass is the **invisible during recordings + meeting notes** — useful for Jack doing live client calls, but that requires him to install Glass on his own machine.
4. We don't have a use case where server-side Glass would add unique value over what Screenpipe + Russell already do.

**If Jack wants this, he'd need to:**
- Install Glass on his own Mac/PC
- Connect it to the same Ollama/AI backend we use
- Configure it to post summaries to a webhook → we route to Jack Connect

**Bottom line:** Interesting product, but not a fit for our current server-based automation stack. The "proactive meeting notes" angle is compelling for a future AI white-collar staffing product — a digital assistant that sits in your meetings and generates summaries/tasks automatically.

---

*RD Report — Solomon OS*  
*Added to queue as priority=normal, type=rd-research*