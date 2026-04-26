# RD Report: Peekaboo

**Repo:** https://github.com/steipete/Peekaboo  
**Stars:** high | **Forks:** N/A | **Language:** Swift 6.2 + TypeScript  
**License:** MIT  
**Cloned:** /home/workspace/Peekaboo

## What It Is
macOS automation tool that captures screens, sees UI elements, and performs clicks/types/scrolls via AI. Version 3 adds native agent flows and multi-screen automation. Essentially a vision-based GUI automation agent for macOS.

## Key Capabilities
- **Pixel-accurate screen capture** (windows, screens, menu bar, Retina 2x)
- **AI vision analysis** — sees UI and responds (click, type, scroll, hotkey, menu, window, dock, space)
- **Multi-provider AI:** GPT-5.1, Claude 4.x, Grok 4-fast, Gemini 2.5, Ollama (local)
- **MCP server** for Claude Desktop and Cursor
- **Native CLI** and **macOS app**
- **Menu/menubar discovery** with structured JSON (no clicks required)
- **Agent mode:** Natural-language multi-step automation
- **Permissions:** Requires macOS Screen Recording + Accessibility (macOS-only)

## Windows Reverse-Engineering Answer

**No — cannot be ported to Windows.** Here's why:

| Dependency | Why It Can't Be Moved |
|---|---|
| **AXorcist** (AX automation submodule) | macOS-only Accessibility API — the core of all UI discovery and interaction |
| **Screen Recording permission** | macOS framework, no Windows equivalent |
| **Accessibility permissions** | macOS AX stack, Windows uses UIAutomation which is fundamentally different |
| **Swift 6.2 + SwiftPM** | Swift does support Windows, but SwiftUI/AVFoundation/AX frameworks do not |
| **Homebrew tap** | Package manager doesn't exist on Windows |
| **Menu/menubar APIs** | Completely macOS-specific |

## Verdict
**SKIP** — This is a macOS-only tool that fundamentally depends on Apple's Accessibility and Screen Recording frameworks. There's no meaningful Windows port without a complete ground-up rewrite using Windows' UIAutomation or third-party tools like pywinao. Even then, the architecture (AX-based element discovery) wouldn't translate.

Not relevant for Solomon OS's cross-platform agent goals. The concept (vision-based GUI automation) is valuable, but Peekaboo's implementation is locked to macOS.