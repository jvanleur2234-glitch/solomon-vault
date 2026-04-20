# RD Report: Agent Browser

**Repo:** `vercel-labs/agent-browser`  
**Stars:** 10K+ | **License:** Apache 2.0 | **Lang:** Rust/TypeScript  

## What It Does
Fast native Rust CLI for browser automation designed for AI agents. Minimal overhead, accessibility tree snapshots, screenshot capture.

## Why It Matters for Solomon OS
- **Native Rust Performance**: Fast browser automation with minimal overhead
- **Accessibility Tree**: Snapshots with element refs for reliable interaction
- **Multi-Platform**: npm, Homebrew, Cargo installation
- **Chrome Auto-Install**: Downloads Chrome for Testing automatically
- **AI Agent Optimized**: Designed specifically for agent workflows

## Key Capabilities
- Open, navigate, click, type, screenshot, fill forms
- Keyboard actions and element selection
- Accessibility tree snapshots
- Multi-installation methods (npm, Homebrew, Cargo)
- Auto-detection of existing Chrome/Brave/Playwright/Puppeteer
- Rust-powered speed

## Comparison to What We Have
vs **browser-use/HyperAgent**: Agent Browser is lower-level, faster. Could be underlying primitive for browser automation layer.

## Recommendation
**SKILL** — Lower-level browser automation primitive. Evaluate as underlying engine for Solomon OS browser tasks.

**Category:** #browser-automation #rust #cli
