# RD Report: Android CLI + Skills by Google

**Date:** 2026-04-20  
**Source:** [X @DeepTechTR](https://x.com/i/status/2045747762940039653) + [Android Developers Blog](https://android-developers.googleblog.com/2026/04/build-android-apps-3x-faster-using-any-agent.html)  
**Task:** android-cli-001

---

## What It Is

Google released a suite of 3 tools for AI agents to build Android apps:

1. **Android CLI** — Terminal tool replacing Android Studio for task execution. Commands: `android create`, `android sdk install`, `android emulator`, `android run`
2. **Android Skills** — Pre-built agentic workflows for common tasks (setup, build, test, deploy)
3. **Android Knowledge Base** — Updated in real-time so AI agents use current info, not outdated training data

**Key stat:** 70% fewer tokens, 3x faster vs standard tooling.

**Works with:** Any AI agent (Claude Code, Cursor, etc.)

---

## Components

| Tool | What It Does |
|------|-------------|
| `android create` | Instant project scaffolding |
| `android sdk install` | On-demand SDK installation |
| `android emulator` | Full emulator lifecycle management |
| `android run` | Build + deploy in one command |

Skills cover: project setup, emulator management, UI testing, build verification, Play Store deployment.

---

## Why It Matters for Solomon OS

**PlainApp integration:** Android CLI becomes the backbone of PlainApp's AI agent — when a user says "build me a real estate app for my listings", Russell Tuna or Hermes uses Android CLI to scaffold the full project in minutes.

**JackConnect mobile layer:** Jack's clients could get custom Android apps built on-demand via AI agents using Android CLI. No Android development knowledge needed.

**Be Like You! OS:** Android CLI + Gemma 4 + Androguard = full self-hosted Android development stack on the phone itself. Build apps on the device, for the device.

**Solomon Air mobile:** AI voice calls + custom Android UI built via Android CLI.

---

## What We'd Build

1. **Wrapper skill** in Hermes that exposes `android create` / `android run` to Russell Tuna
2. **JackConnect app generator:** "Make me a listings app" → Android CLI scaffolds → deploys to Jack's Pixel as a real APK
3. **PlainApp integration:** Android CLI as the dev tool backend when AI needs to generate actual Android code

---

## Recommendation

**FORGE (HIGH PRIORITY)**

Cloned to: `/home/workspace/android-cli/`

Installation: `curl -fsSL https://developer.android.com/tools/android-cli-install.sh | bash`

Priority because it directly connects to: PlainApp (mobile brain), JackConnect (custom apps), Be Like You! OS (device-native dev).

---

## Link Fit

★★★★★ — #android #mobile #ai-staffing #solomon-air #be-like-you-os

---

*Last updated: 2026-04-20*