# RD Report: browserclaw-agent

**Fork:** https://github.com/jvanleur2234-glitch/browserclaw-agent  
**Source:** https://github.com/idan-rubin/browserclaw-agent  
**Date:** 2026-04-22  
**License:** MIT  
**Stars:** ~400+ (nascent)  
**Language:** TypeScript/Node.js  

## What It Does
Modular AI agent for browser automation. Three swappable layers: LLM (Claude/GPT/Gemini/local), the agent (reasoning, obstacle recovery, learned skills), and BrowserClaw (accessibility tree-based browser control). Auto-learns site-specific playbooks from successful runs.

## Key Features
- **Layered architecture:** Separate LLM, agent, browser layers — swap any component
- **Accessibility tree snapshots:** Uses browser's own accessibility tree, not raw DOM
- **Anti-bot handling:** Built-in Cloudflare Turnstile solving, press-and-hold bypass, cookie banner dismissal
- **Skill catalog:** Learns per-domain playbooks from successful runs; refines on each run
- **Skill learning:** First user automating a domain pays exploration cost; subsequent runs use playbook
- **TypeScript native:** Standalone npm library `browserclaw` for any agent

## Solomon OS Fit
**INTEGRATE** — Browser layer for Solomon Browser. Built-in anti-bot solving is valuable for autonomous web navigation. Skill catalog concept maps to Hermes learning-from-success pattern. Layered architecture aligns with Solomon OS design.

## Competitor Notes
Direct competitor to ClawLess. Different approach: accessibility tree vs pixel-based. Auto-learns skills vs fixed rules.

## Recommendation
INTEGRATE — Anti-bot handling and skill catalog are immediately useful for Solomon Browser POC.