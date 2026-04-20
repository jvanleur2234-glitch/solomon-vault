# Solomon Browser Extension — SPEC

**Version:** 0.1.0
**Status:** Phase 1 Prototype Built
**Last Updated:** April 19, 2026

---

## Overview

Solomon Browser brings Solomon OS inside any Chromium browser (Chrome, Edge, Brave, Arc). It's the fastest way to get Solomon OS features without building a custom browser.

**Two architecture paths:**
- **Phase 1 (Extension):** Chrome extension layer on top of Chromium — fast to ship, existing browser
- **Phase 2 (Custom Browser):** Full Chromium fork with Solomon OS embedded at the OS level — more powerful, longer to build

This document covers Phase 1.

---

## What It Does

### Core Features

1. **AI Side Panel** — Ask Solomon anything about the current page. Summarize, extract data, analyze.
2. **Solomon Air Dialer** — Make VoIP calls and send SMS directly from the browser
3. **JackConnect Workers** — See active AI workers and assign tasks without leaving your tab
4. **Hermes Memory** — Automatically store page insights, extracted data (phones, emails, prices), and manual notes
5. **Solomon Bus** — Connects to Solomon OS running on your Zo Computer (or standalone)
6. **Selfsync Integration** — Self-hosted Chrome sync (bookmarks, passwords, prefs) via Selfsync server — no Google account needed

### Privacy Moat

- Selfsync: all browser data stays local (bookmarks, passwords, history) — no Google sync
- Hermes memory syncs to YOUR Zo Computer, not a third party
- Page content is processed via YOUR AI (Zo API), not sent to Google/MS/etc.

---

## File Structure

```
solomon-browser-ext/
├── manifest.json      — Extension manifest v3
├── background.js      — Service worker (Solomon Air, JackConnect, Hermes, Bus)
├── popup.html         — Extension popup UI
├── popup.js           — Popup logic
├── sidepanel.html     — AI chat panel (side panel)
├── sidepanel.js      — AI chat logic
├── content.js        — Content script (page extraction, highlighting)
├── styles.css        — All styles
├── icons/            — Extension icons
├── docker-compose.yaml — Selfsync self-hosted Chrome sync
└── SPEC.md           — This file
```

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Chromium Browser                  │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │  Popup   │  │ Side     │  │  Content Script  │  │
│  │  (Air,   │  │  Panel   │  │  (page extract,  │  │
│  │ Workers) │  │  (AI)    │  │   highlight)     │  │
│  └────┬─────┘  └────┬─────┘  └────────┬─────────┘  │
│       │             │                 │             │
│       └─────────────┼─────────────────┘             │
│                     │                               │
│              ┌──────▼──────┐                       │
│              │  Background  │                       │
│              │   Service    │                       │
│              │   Worker     │                       │
│              └──────┬──────┘                       │
└─────────────────────┼───────────────────────────────┘
                      │
          ┌───────────┼───────────┐
          │           │           │
    ┌─────▼─────┐ ┌───▼───┐ ┌───▼────┐
    │ Solomon   │ │ Jack   │ │Hermes  │
    │ Air       │ │Connect │ │Memory  │
    │ (VoIP)   │ │Workers │ │(Zo API)│
    └─────┬─────┘ └───┬───┘ └───┬────┘
          │           │         │
    ┌─────▼───────────▼─────────▼─────┐
    │        Selfsync Server          │
    │   (Local Chrome Sync, SQLite)   │
    └─────────────────────────────────┘
```

---

## Connection Points

| Service | Local Port | Purpose |
|---------|-----------|---------|
| Solomon Bus | 3001 | Inter-agent communication |
| Solomon Air | 3002 | VoIP dialer, SMS |
| JackConnect | 3003 | AI worker management |
| Selfsync | 8080 | Self-hosted Chrome sync |

When Solomon OS is running on Zo Computer, these services are available locally. When running standalone, the extension works in offline mode with local storage.

---

## AI Integration

- **Zo API** for chat completions (`https://api.zo.computer/zo/ask`)
- Page context injected into every prompt (title, URL, extracted text)
- Conversation history stored per-user
- Hermes memory synced to Zo Computer

---

## Selfsync Integration

**Why:** Replaces Google Chrome Sync with a self-hosted alternative.

**Setup:**
1. Run Selfsync Docker container: `docker compose up -d`
2. Point Chrome to sync server: `google-chrome-stable --sync-url=http://localhost:8080`
3. All browser data stays local (bookmarks, passwords, history, preferences)

---

## Phase 2: Custom Browser (Future)

Build from Chromium source with Solomon OS embedded:
- Remove all Google/Apple tracking
- Selfsync built-in (no flag needed)
- Solomon OS as default homepage/new tab
- Hermes memory as browser-native feature
- Pre-installed with Solomon Air dialer

---

## Installation (Developer Mode)

1. Go to `chrome://extensions`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select the `solomon-browser-ext` folder
5. Pin the extension to toolbar

---

## TODO

- [ ] Add Selfsync connection to background.js
- [ ] Connect to Zo API for chat (currently placeholder token)
- [ ] Add conversation persistence
- [ ] Add "Analyze This Page" one-click actions
- [ ] Build Selfsync Docker compose file
- [ ] Add keyboard shortcuts
- [ ] Mobile responsive for side panel