# RD Report: Chromex

**Source:** https://github.com/GENEXIS-AI/chromex  
**Stars:** ~4.7K+ (social badge in README)  
**License:** MIT  
**Lang:** TypeScript + Node.js + Chrome MV3 extension  
**Analysis date:** 2026-04-29

---

## What It Is

Chromex is a Chrome MV3 side-panel assistant that connects Chrome to Codex (OpenAI's CLI agent) through a local native bridge. It lets users chat with the current page, selected tabs, screenshots, uploaded files, PDFs, images, and browser history — all inside a Chrome side panel.

**Architecture:**
```
Chrome Extension -> Native Messaging Host -> Local Bridge -> codex app-server
```

Three packages:
- `packages/extension` — Chrome MV3 side panel UI
- `packages/bridge` — Local bridge daemon (Node.js)
- `packages/native-host` — Chrome Native Messaging relay

## What We'd Use It For

Solomon Browser is a core planned component of Solomon OS. Chromex gives us:
1. **A proven Chrome extension pattern** — MV3 side panel with chat UX we can study/borrow
2. **Page-aware workflows** — chat-with-page, tab context, screenshot analysis maps directly to what Solomon Browser needs
3. **Voice input + browser control** — workflow automation via Chrome content scripts
4. **Site adapters** — YouTube, news, mail, etc. — we could replicate this pattern for real estate sites, job boards, etc.
5. **Local bridge model** — avoids sending raw API keys to extension storage (privacy-first pattern)

## How It Compares to What We Have

| Capability | Solomon Browser (planned) | Chromex |
|---|---|---|
| Chrome side panel | — | ✅ MV3 side panel |
| Chat with page content | — | ✅ |
| Tab/URL context | — | ✅ |
| Screenshot + image analysis | — | ✅ |
| Voice input | — | ✅ |
| Browser control workflows | — | ✅ content scripts |
| Multi-language i18n | — | ✅ 20+ locales |
| Profile system (`/` picker) | — | ✅ |
| PDF/DOCX/CSV parsing | — | ✅ |
| Codex as backend | — | ✅ (requires Codex CLI) |
| Self-hosted / privacy-first | Planned | ✅ (local bridge, no keys in storage) |

**Key difference:** Chromex requires the Codex CLI (OpenAI) as the LLM backend. Solomon Browser would use our own Zo API + RENU API + Ollama stack instead.

## Recommendation

**SKILL / REFERENCE**

Chromex is a high-quality reference implementation for the Solomon Browser side of JCPaid. Specific things to extract:

1. **Extension architecture** — How they structure the MV3 side panel, content scripts, native messaging. We can replicate the folder structure for a Zo Browser extension.
2. **Site adapter pattern** — Their `@` picker for tabs, `/` picker for profiles, and per-site suggestion logic is directly applicable to real estate / job board adapters.
3. **Privacy-first design** — Keeping API keys out of extension storage and using a local bridge is the right call. We should follow this for Zo Browser.
4. **i18n setup** — 20+ locale files already done. Massive head start if we go multi-language.

**Not a direct integration** because Chromex is tightly coupled to Codex (OpenAI's proprietary CLI). We can't just bolt it onto Zo without a rewrite of the bridge layer.

**Action:** Clone into `/home/workspace/solomon-vault/repos/chromex/` for reference, and document the site-adapter + bridge architecture in the Solomon Browser spec.

---

*Report generated: 2026-04-29*  
*Next: Write full analysis to brain/RD_REPORTS/ and sync to GitHub*