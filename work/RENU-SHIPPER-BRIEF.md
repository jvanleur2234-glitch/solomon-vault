# 🚀 RENU — Build Brief for Shipper

**RENU** ("ree-noo") — "Renew Your Mind"
An AI faith companion app that maps a person's negative thought to a Bible verse (Amplified translation).

**Live:** Already running on Solomon OS with 31,102 Amplified Bible verses.
**Goal:** Build native iOS + Android apps for App Store and Google Play.

---

## 🎯 The Concept

**Problem:** A Christian feels anxious, afraid, lonely, or hopeless. They need God's truth — fast.
**Solution:** Type or speak the negative thought → RENU returns a Bible verse that speaks directly to that emotion.

**Tagline:** "When the negative thought comes, God's truth goes back out."
**Target:** Christian women & men 25-55 dealing with anxiety, life transitions, grief, loneliness, shame.

---

## 📱 App Screens

### Screen 1 — Home (Input)
- Single large text field: "What's the negative thought?"
- Placeholder: "I'm so worried about..."
- Big CTA button: **"Renew My Mind"**
- Microphone icon for voice input
- "Try an example" → pre-fills a negative thought
- Small category tags at bottom: Future | Peace | Identity | Strength | Courage | Rest | Love

### Screen 2 — Result
- Shows the user's negative thought (small, italic)
- Bible verse in LARGE text (Amplified version)
- Scripture reference in bold gold/yellow
- Category label (✝️ Courage)
- **Copy** button | **Star/Save** button | **Try Again** button

### Saved Verses (modal/bottom sheet)
- Lists all starred verses
- Persists in localStorage

### Voice Recording (overlay)
- Full-screen dark overlay
- Animated mic icon
- "Listening..." text
- Auto-transcribes and submits

---

## 🎨 Visual Design

**Background:** Deep dark gradient — `#1a0a2e → #16213e → #1a0a2e`
**Primary accent:** Purple (#9333EA, #A855F7)
**Secondary accent:** Pink (#EC4899, #F472B6)
**Scripture reference:** Gold/yellow (#FACC15)
**Text:** White with varying opacity

**Font feel:** Clean, devotional, warm, reverent — not cluttered

---

## 🧠 Emotion → Verse Matching Logic

The app detects the emotion in the user's thought and matches to relevant verses:

| Emotion | Trigger Words | Example Verses |
|---|---|---|
| **Anxiety/Fear** | fear, afraid, worried, anxious, terrified, scared | Isaiah 41:10, John 14:27 |
| **Rejection** | rejected, abandoned, unloved, alone, cast aside | Deuteronomy 31:6 |
| **Failure** | failed, worthless, useless, not good enough | Philippians 4:13 |
| **Hopelessness** | hopeless, despair, give up, nothing will change | Jeremiah 29:11 |
| **Anger** | angry, mad, furious, frustrated, bitter | Psalm 23:1-2 |
| **Grief/Sadness** | sad, sorrow, heartbroken, crying, devastated | Psalm 34:18 |
| **Loneliness** | lonely, alone, no one understands, isolated | Psalm 23:1-2 |
| **Shame** | ashamed, humiliated, embarrassed, judged, guilty | Romans 8:1 |
| **Doubt** | doubt, uncertain, unsure, confused, what if | Mark 11:24 |

---

## 📖 The Full Bible Database

**31,102 verses** in the Amplified translation — the ENTIRE Bible.

📄 **JSON file (7.3MB):** `https://gist.githubusercontent.com/jvanleur2234-glitch/bed7bd2fcf69e94d4eb46561f9eea28f/raw/amplified_verses.json`

Each verse entry:
```json
{
  "book": "Genesis",
  "chapter": 1,
  "verse": 1,
  "text": "IN THE beginning God (prepared, formed, fashioned, and) created the heavens and the earth.",
  "ref": "Genesis 1:1"
}
```

**For the FREE tier:** Use just 12 key starter verses (listed below).
**For the PREMIUM tier:** Load all 31,102 from the CDN URL above.

---

## ✝️ Starter Verses (Free Tier — embed directly in code)

| Category | Ref | Text |
|---|---|---|
| Future | Jeremiah 29:11 | "For I know the plans I have for you, declares the LORD, plans to prosper you and not to harm you, plans to give you hope and a future." |
| Courage | Deuteronomy 31:8 | "The LORD himself goes before you and will be with you; he will never leave you nor forsake you. Do not be afraid; do not be discouraged." |
| Strength | Isaiah 41:10 | "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand." |
| Peace | John 14:27 | "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid." |
| Identity | Psalm 100:3 | "You matter to God. You matter to this world. You are a treasured child of the Most High God." |
| Peace | 1 Peter 5:7 | "Cast all your anxiety on him because he cares for you." |
| Rest | Psalm 23:1-2 | "The LORD is my shepherd, I lack nothing. He makes me lie down in green pastures." |
| Community | 1 Thessalonians 5:11 | "Therefore encourage one another and build each other up." |
| Courage | Deuteronomy 31:6 | "Be strong and courageous. Do not be afraid or terrified... for the LORD your God goes with you." |
| Strength | Philippians 4:13 | "I can do all things through Christ who strengthens me." |
| Humility | 1 Peter 5:6 | "Humble yourselves, therefore, under God's mighty hand, that he may lift you up in due time." |
| Love | 1 Corinthians 13:4 | "Love is patient, love is kind. It does not envy, it does not boast, it is not proud." |

---

## 💬 Sample Negative Thoughts (for "Try an example" button)

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

---

## 🔧 Technical Notes for Shipper

1. **Fetch full Bible:** On app load (premium), `fetch()` the 31K verse JSON from the Gist URL. Cache in `localStorage` or AsyncStorage after first load.
2. **Free tier:** Embed the 12 verses directly in the component (no network needed).
3. **Voice input:** Use the Web Speech API (`SpeechRecognition`) for voice-to-text.
4. **Emotion matching:** Run keyword matching client-side — no backend needed.
5. **Saved verses:** Store in `localStorage` / AsyncStorage.
6. **iOS/Android:** Wrap with Capacitor or build with Expo for App Store + Play Store submission.
7. **Offline support:** The cached verses work offline once loaded.

---

## 💰 Monetization

- **Free:** 12 verses, basic emotion matching
- **Premium ($4.99/month or $39.99/year):** Full 31,102-verse library, voice input, saved verse sync, daily verse notifications
- **First:** Get it free + premium unlock on the roadmap

---

## 📦 Existing Code (Reference)

- **React component:** `/workspace/arena2api/renu_app.tsx` — full working UI
- **Backend API:** `/workspace/renu_api/server.py` — Flask + Ollama with emotion detection
- **Full Bible JSON:** https://gist.githubusercontent.com/jvanleur2234-glitch/bed7bd2fcf69e94d4eb46561f9eea28f/raw/amplified_verses.json

---

## ⏱️ What You Need to Do

1. Build a mobile-first React app with this spec
2. Load all 31,102 verses from: `https://gist.githubusercontent.com/jvanleur2234-glitch/bed7bd2fcf69e94d4eb46561f9eea28f/raw/amplified_verses.json`
3. Implement emotion → verse matching client-side
4. Add voice input (Web Speech API)
5. Add saved verses (localStorage/AsyncStorage)
6. Wrap with Capacitor for native iOS + Android
7. Submit to App Store ($99/yr dev account) and Google Play ($25 one-time)

---

*Brief created by Zo (Solomon OS) for Joseph Van Leur — RENU app build, April 2026.*
