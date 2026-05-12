# RD Report: Hermes × Cua Computer Use

## What It Is
Hermes Agent integration with trycua's computer use API — allows ANY model (not just frontier) to control a user's actual computer in the background while they continue working. No session takeover.

## Technical Details
- **Command:** `hermes computer-use install` (macOS only, Linux "very soon")
- **Powered by:** trycua API (`cua.dev`)
- **Video demo:** 36 seconds showing agent browsing/interacting
- **Engagement:** 1.7K likes, 1M views, 115 replies in 24 hours

## What This Means for OSagnent
- **BODY layer** = Hermes + cua = can control any app on any OS
- **EYES layer** = UI-TARS desktop = screen understanding
- **BRAIN layer** = skill generator = self-improving knowledge
- **MEMORY layer** = HERE API (port 5015) = permanent memory

OSagnent is now COMPLETE across all 4 layers.

## Competitive Analysis
- HermesOS: cloud only, crypto required, session takeover
- OSagnent: local+cloud hybrid, no crypto, background operation, permanent memory, self-improving

## Action Items
- Watch for Linux release of cua-driver (Teknium says "very soon")
- Add Cua observation protocol to osagnent/observe/
- Create skill: `osagnent-computer-use` in Hermes

## Rating: 🔴 FORGE IMMEDIATELY — fills the "body" gap in OSagnent