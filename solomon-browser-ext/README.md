# Solomon Browser

AI-native Chrome extension powered by Solomon OS. Think with memory, remember everything, and browse smarter.

## Features

- **Solomon AI** — Ask anything about any page, get deep reasoning
- **Memory** — Remembers your browsing history, interactions, and learnings
- **SelfSync** — Self-hosted bookmark/password sync (no Google)
- **Highlight Mode** — See interactive elements at a glance
- **Extract** — Pull key info from any page
- **3 AI Modes** — Fast, Balanced, Deep Think

## Installation

1. Clone or download this repo
2. Open `chrome://extensions/`
3. Enable "Developer mode" (toggle in top right)
4. Click "Load unpacked"
5. Select the `solomon-browser-ext` folder
6. Click the Solomon icon in your toolbar to use

## Architecture

```
solomon-browser-ext/
├── manifest.json          # Chrome extension manifest v3
├── src/
│   ├── background/
│   │   └── service-worker.js  # AI routing, memory, sync
│   ├── content/
│   │   ├── content-script.js  # Injected into every page
│   │   └── content.css
│   ├── popup/
│   │   ├── popup.html
│   │   ├── popup.js
│   │   └── popup.css
│   ├── options/
│   │   ├── options.html
│   │   └── options.js
│   └── ai/
│       ├── hermes-client.js   # AI orchestration
│       ├── memory-bridge.js   # Local memory
│       └── selfsync.js        # Cross-device sync
└── docs/
    └── ARCHITECTURE.md
```

## Keyboard Shortcuts

- `Alt + S` — Ask Solomon about the current page
- `Alt + H` — Toggle highlight mode

## Configuration

Open the extension popup → click "Settings" to configure:
- AI model (cloud or local Ollama)
- SelfSync server URL
- Memory preferences

## Dependencies

- Chrome Extension Manifest V3
- Zo AI API (cloud mode)
- Ollama (local mode, optional)

## License

MIT
