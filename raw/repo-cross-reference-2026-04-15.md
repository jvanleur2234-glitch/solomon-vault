# REPO CROSS-REFERENCE ANALYSIS
**All Projects vs All Business Ideas**
*Created: 2026-04-15*

---

## NEW REPOS ANALYZED

| Repo | Stars | License | Platform | Key Capability |
|------|-------|---------|---------|----------------|
| moonshine-ai/moonshine | 7.7K | Apache 2.0 | iOS/Android/Linux/Mac/Windows/RPi | Local STT + TTS + Intent Rec, 8x faster than Whisper |
| JerryZLiu/Dayflow | 5.9K | MIT | macOS only | AI screen journal, timeline of work, supports Ollama |
| JuliusBrussee/caveman | 32.1K | MIT | Claude Code/Cursor/Windsurf | Token compression skill, 65-75% fewer tokens |
| mayukh4/linux-android | 628 | MIT | Android via Termux | Old phone → Linux desktop or Home Assistant server |
| BookStackApp/BookStack | 18.6K | MIT | Self-hosted | Wiki/documentation platform |
| ClawGUI (via @RituWithAI) | - | Open | Android/iOS/HarmonyOS | GUI agents via screen observation, no API needed |
| Pokeclaw (via @JulianGoldie) | - | Open | Android | Phone → AI → Phone, zero cloud, zero API |
| DroidClaw (via @HiTw93) | - | Open | Android | $30 phone, one command, no server, open source |

---

## CROSS-REFERENCE MATRIX

### SOLOMON AIR
| Repo | Fit | How It Fits |
|------|-----|-------------|
| moonshine | 🔴 CRITICAL | Replace cloud STT/TTS with free local. 8x faster than Whisper. Cross-platform including RPi. PERFECT for Solomon Air voice layer. |
| linux-android | 🔴 CRITICAL | "Run on cheapest hardware" = old Android phones. One script turns them into Linux servers. PERFECT for Solomon Air edge nodes. |
| Dayflow | 🟡 NICE | Reference for screen→timeline AI journal. Could adapt for Solomon Air activity logging. macOS only though. |
| BookStack | 🟡 NICE | Could be the knowledge base layer for Solomon Air. Self-hosted wiki for community docs. |
| caveman | 🟢 LOW | Token compression skill. Integrate into Hermes to save costs on every AI call. |

### JACKCONNECT (Real Estate AI Worker)
| Repo | Fit | How It Fits |
|------|-----|-------------|
| moonshine | 🔴 CRITICAL | Better STT than faster-whisper. Real-time voice input for Jack while he's showing properties. Integrates with existing Piper TTS. |
| ClawGUI / Pokeclaw / DroidClaw | 🔴 CRITICAL | GUI agents that control phones via screen observation. REPLACES Watch Once + Screenpipe for mobile. Jack could say "check my MLS messages" and AI reads screen and responds. |
| Dayflow | 🟡 NICE | Activity journal pattern. Jack's day mapped automatically = better AI context for briefings. |
| linux-android | 🟡 NICE | Jack's old phone becomes his dedicated AI server running JackConnect locally. |

### HERMES / SOLOMON OS AGENTS
| Repo | Fit | How It Fits |
|------|-----|-------------|
| caveman | 🔴 CRITICAL | 65-75% token reduction on EVERY Hermes call. Massive cost savings. Install as Hermes skill. |
| moonshine | 🟡 NICE | Hermes voice input layer for Telegram/local commands. Intent recognition = faster LLM routing. |
| BookStack | 🟢 LOW | Could host Hermes skill documentation as a searchable wiki. |

### PRIVACY-FIRST STACK
| Repo | Fit | How It Fits |
|------|-----|-------------|
| linux-android | 🔴 CRITICAL | Old phone = $30 AI server. No cloud. No subscription. Privacy preserved. |
| moonshine | 🔴 CRITICAL | All voice processing local. No cloud STT/TTS costs. |
| Dayflow | 🟡 NICE | Shows privacy-first screen capture works. Data stays local. |
| Pokeclaw / DroidClaw | 🔴 CRITICAL | Zero-cloud phone control. Phone never talks to internet except through local AI. |

---

## THE PICTURE EMERGING

The new repos you're sharing are all pointing to ONE THING:

**"AI that runs on cheap hardware, with zero cloud dependency, that controls devices through their screens."**

ClawGUI, Pokeclaw, DroidClaw = GUI agents. Moonshine = local voice. linux-android = $30 server. Dayflow = local privacy.

Together they form a complete stack:

```
User's voice (Moonshine)
    ↓
Local AI on old phone (linux-android + Ollama)
    ↓
GUI agent reads screen and acts (ClawGUI/Pokeclaw/DroidClaw)
    ↓
Actions happen on device
    ↓
Dayflow-style journal captures what happened
    ↓
All private, all local, all free
```

---

## PRIORITY ORDER

1. 🔴 **Moonshine** — Fork it, integrate into Solomon Air + JackConnect. Replaces cloud STT/TTS.
2. 🔴 **linux-android** — Integrate into Solomon Air as "run on $30 hardware" demo.
3. 🔴 **ClawGUI / Pokeclaw** — Fork it, integrate into JackConnect as mobile GUI agent.
4. 🔴 **caveman** — Install as Hermes skill immediately. 65% token savings on every call.
5. 🟡 **Dayflow** — Study for Solomon Air activity logging pattern.
6. 🟡 **BookStack** — Add to Solomon Air as community documentation wiki.
