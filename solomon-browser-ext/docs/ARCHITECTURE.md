# Solomon Browser — Architecture

## Overview

Solomon Browser is a Chrome Extension (Manifest V3) that brings Solomon OS AI capabilities directly into any web browsing experience.

## Extension Architecture

### Background Service Worker (`src/background/service-worker.js`)
- **AI Orchestration** — routes AI requests to cloud (Zo) or local (Ollama)
- **Memory Management** — stores page visits, interactions, learnings
- **SelfSync** — pushes/pulls data to self-hosted sync server
- **Context Menu** — right-click actions
- **Message Router** — handles communication between content scripts and AI layer

### Content Script (`src/content/content-script.js`)
- **Per-page injection** — runs on every page
- **Highlight Mode** — visual overlays on interactive elements
- **Interaction Tracking** — logs clicks, scrolls, focus events
- **Keyboard Shortcuts** — Alt+S (ask), Alt+H (highlight)
- **Page Analysis** — extracts content for AI context

### Popup UI (`src/popup/`)
- **Quick Ask** — ask Solomon anything
- **Tool Grid** — 6 quick actions
- **Mode Selector** — Fast / Balanced / Deep Think
- **Response Area** — streaming AI responses

### Options Page (`src/options/`)
- AI model configuration
- SelfSync server setup
- Memory limits
- Data management

## AI Flow

```
User asks question
       ↓
popup.js sends to background
       ↓
service-worker.js → hermes-client.js
       ↓
   ┌────────────────────────────────┐
   │ Try Ollama (localhost:11434)   │
   └─────────────┬──────────────────┘
                 ↓ (if unavailable)
   ┌────────────────────────────────┐
   │ Call Zo AI (api.zo.computer)   │
   └─────────────┬──────────────────┘
                 ↓
         AI response returned
                 ↓
         Memory stored
```

## Memory Architecture

```
chrome.storage.local
    └── solomon_memory[]
          ├── id
          ├── content
          ├── metadata (url, title, type)
          └── timestamp
```

Max 500 items, FIFO eviction.

## SelfSync Integration

SelfSync (loyalpartner/selfsync) provides:
- Bookmarks
- Passwords (encrypted)
- Preferences
- Extension settings

All synced via user's own self-hosted server. No Google, no cloud dependency.

## Comparison to Alternatives

| Feature | Solomon Browser | StartOS | Dissenter | Brave |
|---------|---------------|---------|-----------|-------|
| AI Integration | ✅ Full | ❌ | ❌ | ❌ |
| Memory | ✅ Persistent | ❌ | ❌ | ❌ |
| SelfSync | ✅ Built-in | ❌ | ❌ | ❌ |
| Hermes | ✅ Deep | ❌ | ❌ | ❌ |
| Open Source | ✅ MIT | ✅ | ✅ | ❌ |
| Ad Blocking | ❌ Future | ❌ | ✅ | ✅ |
| Rewards | ❌ Future | ❌ | ❌ | ✅ |

## Build Status

Phase 1: ✅ Structure created
Phase 2: ⬜ Icons
Phase 3: ⬜ Testing
Phase 4: ⬜ Publish
