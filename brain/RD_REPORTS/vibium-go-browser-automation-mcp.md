# vibium — Go-Based AI-Native Browser Automation

**Fork:** Already forked to `jvanleur2234-glitch/vibium`  
**License:** Apache 2.0  
**Language:** Go

## What It Is
A lightweight, cross-language browser automation framework built on WebDriver BiDi. Provides a binary CLI, an MCP server, and client libraries for JavaScript/TypeScript, Python, and Java. AI-native, zero-config, standard-based.

## Key Features
- **WebDriver BiDi** standard — no vendor lock-in
- **~10MB binary** — lightweight
- **CLI + MCP server + client libraries** (JS, Python, Java)
- **Semantic element discovery**: find by visible text, label, placeholder, ARIA role — no CSS selectors needed
- **Commands**: go, map, click, find, text, screenshot, pdf, eval, wait, record, fill, select, check, press
- **Auto browser download** — zero config
- AI-native design for agent integration

## Comparison to BrowserUse / AgentBrowser / Stagehand

| Feature | Vibium | BrowserUse | AgentBrowser (Rust) |
|---|---|---|---|
| Language | Go | Python | Rust |
| License | Apache 2.0 | MIT | Apache 2.0 |
| Size | ~10MB | Python | ~40MB |
| Standard | WebDriver BiDi | Playwright | Custom |
| MCP server | ✅ | ❌ | ❌ |
| JS/Python/Java clients | ✅ | Python only | No |
| Semantic discovery | ✅ | ❌ | ✅ (snapshot) |

## Verdict
**SKILL** — The Go-based lightweight design + MCP server + multi-language clients makes this a strong candidate for Hermes browser automation skill. Compare to existing browser-use integration.