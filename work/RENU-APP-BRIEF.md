# RENU App — Full Briefing for Shipper

## What RENU Is

**RENU** ("ree-noo" — Renew Your Mind) is a faith-based mental health app that helps Christians combat negative thoughts with God's truth.

**Core concept:** When a negative thought comes, RENU returns a matching Bible verse (Amplified translation). The person speaks or types their struggle → RENU maps it to an emotion category → returns relevant scripture.

**Tagline:** "Renew Your Mind"
**Core value prop:** "When the negative thought comes, God's truth goes back out."

**Live backend:** Python API on port 5010 with 31,102 Amplified Bible verses loaded. Handles emotion detection + verse matching + AI companion responses via Ollama (qwen3.5:27b).

---

## The Problem It Solves

Christians struggling with anxiety, fear, shame, loneliness, and doubt have no tool that immediately maps their *specific negative thought* to a Bible verse that speaks directly to it. They either:
- Don't know which verse to look up
- Can't find the right verse in the moment
- Need encouragement alongside the verse

---

## App Screens & Features

### Screen 1 — Home / Input
- Single text field asking: "What's the negative thought?"
- Placeholder: "I'm so worried about..."
- Large CTA button: **"Renew My Mind"**
- Microphone button for voice input
- "Try an example" link that pre-fills common negative thoughts
- Tags at bottom: Future | Peace | Identity | Strength

### Screen 2 — Result
- Shows the user's negative thought clearly
- Bible verse in large, beautiful typography (Amplified translation)
- Scripture reference (e.g., "Jeremiah 29:11")
- Category label (e.g., ✝️ Courage)
- **Copy Verse** button
- **Save Star (☆/★)** button
- **Try Again** button
- **Speak It** button (voice)

### Saved Verses Modal
- Bottom sheet listing all saved verses
- Persists across sessions (localStorage)

### Microphone Flow
- Full-screen overlay with spinning indicator
- Simulates 3-second voice listening
- Auto-populates the text field with the transcribed thought

### Example Negative Thoughts (for demo/testing)
- "I can't do this"
- "I'm not good enough"
- "Nobody cares about me"
- "Everything is going wrong"
- "I'm so tired"
- "Why is this happening to me?"
- "I feel so alone"
- "I don't know what to do"
- "I'm worried about everything"
- "I feel like a failure"
- "God must be angry with me"
- "I'm so disappointed in myself"
- "I can't handle this"

### Emotion → Category Mapping
| Detected Keywords | Category |
|---|---|
| fear, afraid, worried, anxious, terrified, scared | Courage |
| alone, nobody, abandoned, no one cares | Identity |
| tired, exhausted, weary, burned out | Rest |
| peace, anxious, worried, anxiety, calm | Peace |
| strong, strength, capable, able | Strength |
| fail, failure, disappointed, not enough | Identity |
| handle, can't, impossible, overwhelmed | Courage |
| everything wrong, happening to me | Identity |

---

## Visual Design

### Color Palette (Dark/Faith Theme)
- Background: Deep gradient `#1a0a2e → #16213e → #1a0a2e`
- Primary accent: Purple (`purple-400`, `purple-500`, `purple-600`)
- Secondary accent: Pink (`pink-300`, `pink-400`, `pink-500`)
- Highlight: Yellow/gold for scripture references (`yellow-300`)
- Text: White with varying opacity

### Typography
- Title: Large gradient text (purple → pink → yellow)
- Verse text: Large, italic, centered
- Reference: Bold yellow/gold

### Vibe
- Dark, reverent, warm
- Like a private devotional space
- Clean, no clutter

---

## Backend API (to connect to)

The RENU API is already running at `http://localhost:5010` ( Solomon OS):

**`POST /api/analyze`**
```json
Request:  { "thought": "I feel so anxious and afraid" }
Response: {
  "thought": "i feel so anxious and afraid",
  "emotions_detected": ["anxiety"],
  "verses": [
    { "ref": "Jeremiah 29:11", "text": "For I know the plans...", "emotion": "anxiety" },
    ...
  ]
}
```

**`GET /api/health`** — returns `{ "status": "ok", "verses": 31102 }`

---

## Verse Database

- **31,102 Amplified Bible verses** loaded in `/home/workspace/arena2api/amplified_verses.json`
- The full dataset is available in the workspace at `/home/workspace/arena2api/renu_verses.json` (sample)
- Each verse entry: `{ "book", "chapter", "verse", "text", "ref" }`

---

## Starter Verse Set (hardcoded in UI — 12 verses)

| # | Verse | Ref | Category |
|---|---|---|---|
| 1 | For I know the plans I have for you... | Jeremiah 29:11 | Future |
| 2 | The LORD himself goes before you... | Deuteronomy 31:8 | Courage |
| 3 | So do not fear, for I am with you... | Isaiah 41:10 | Strength |
| 4 | Peace I leave with you; my peace I give you... | John 14:27 | Peace |
| 5 | You matter to God. You matter to this world... | Psalm 100:3 | Identity |
| 6 | Cast all your anxiety on him because he cares for you. | 1 Peter 5:7 | Peace |
| 7 | The LORD is my shepherd, I lack nothing... | Psalm 23:1-2 | Rest |
| 8 | Therefore encourage one another and build each other up. | 1 Thessalonians 5:11 | Community |
| 9 | Be strong and courageous. Do not be afraid... | Deuteronomy 31:6 | Courage |
| 10 | I can do all things through Christ who strengthens me. | Philippians 4:13 | Strength |
| 11 | Humble yourselves, therefore, under God's mighty hand... | 1 Peter 5:6 | Humility |
| 12 | Love is patient, love is kind. It does not envy... | 1 Corinthians 13:4 | Love |

---

## Business Model

- **Free tier:** Core app with 12 starter verses + emotion matching
- **Premium ($4.99/month or $39.99/year):** Full 31,102 verse library, AI companion responses, voice input, saved verses sync, daily verse notifications
- **Target audience:** Christian women and men dealing with anxiety, life transitions, grief, loneliness
- **Monetization:** Subscriptions + potential Bible study curriculum upsell

---

## Existing Assets

- Full React component: `/home/workspace/arena2api/renu_app.tsx`
- Full backend API: `/home/workspace/renu_api/server.py` (Flask + Ollama)
- 31,102 Amplified verses: `/home/workspace/arena2api/amplified_verses.json`
- Sample verses: `/home/workspace/arena2api/renu_verses.json`

---

## Deployment Targets

1. **App Store** (iOS) — Apple Developer account required ($99/year)
2. **Google Play** (Android) — Google Play Developer account required ($25 one-time)
3. **Web app** — hosted on Vercel/Netlify (Shipper handles this)

---

## Refund Note

Joseph accidentally paid for Shipper Pro. Please process the refund on your end and notify him once complete.

---

## Instructions for Shipper

1. Build a mobile-first React app from this spec
2. Connect to the RENU API backend (or replicate the emotion-matching logic on-device with the 12 starter verses for the free tier)
3. Add localStorage for saved verses
4. Make the microphone input functional (Web Speech API)
5. Deploy as a Progressive Web App (PWA) for immediate mobile access
6. For native App Store/Play Store: wrap with Capacitor or build with Expo — you handle the store submission
7. Apply the dark purple/pink gradient visual design specified above
