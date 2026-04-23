# browserclaw-agent — Robust AI Browser Agent with Skills

**Source:** https://github.com/idan-rubin/browserclaw.agent  
**License:** MIT  
**Stars:** ~600+  
**Date:** 2026-04-23

## What it does
browserclaw-agent is the AI agent layer that drives the browser-claw system. It reads page accessibility snapshots, reasons with an LLM, and executes actions in the browser.

Three-layer architecture:
- LLM layer (Claude, GPT, Gemini, or local)
- The agent for reasoning, obstacle handling, and reusable skills
- BrowserClaw library for browser control and element references

Built-in skills (no prompting required):
- Anti-bot bypass (hold-to-verify overlays, press-and-hold challenges via CDP)
- Cloudflare Turnstile solving (Click the Turnstile iframe via CDP)
- Popup and banner/modal dismissal
- Loop detection to avoid repeated stuck states
- Tab management (switching to newly opened tabs)

Skill catalog: Each successful run creates a domain-specific skill file. Future runs reuse and refine the learned playbook for that domain.

## Solomon OS Fit
**FORGE** — Robust browser automation with anti-bot evasion. The skill learning mechanism (learns from success) is a direct fit for Solomon Browser. MIT license permits direct use.

## Key Components
- Three-layer architecture (LLM/Agent/Browser)
- Accessibility tree-based interaction
- Built-in anti-bot skills
- Domain-specific skill files
- Loop detection
- Tab management

## Recommendation
FORGE — Study anti-bot bypass and skill learning mechanisms for Solomon Browser. MIT license enables direct use.