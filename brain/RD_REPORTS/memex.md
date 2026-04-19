# R&D Report: Memex — Flutter Local-First PKM

**Date:** April 19, 2026

## What It Is
memex-lab/memex — 65 stars, GPL-3.0, Flutter app (iOS/Android). Local-first, AI-native personal knowledge management. Multi-agent system automatically organizes records into timeline cards, extracts knowledge, surfaces insights. All data stays on device. You own your mind.

## What It Does
- **Capture:** Text, photos, voice — long-press to record audio, release to send
- **Organize:** Multi-agent architecture — each agent handles a specific domain
- **Generate cards:** Life (task, routine, event, duration, progress), Knowledge (article, snippet, quote, link, conversation), People/Places, Data/Metrics, Visual
- **Insights:** P.A.R.A-based organization — Projects, Areas, Resources, Archives
- **Agents:** Custom agent system with SKILL.md (Agent Skills standard), per-agent LLM config, JavaScript execution, inter-agent dependency chains

## Key Architecture
```
User Input → Event Bus → Agent loads SKILL.md + system prompt → LLM processes with tools → Actions (file I/O, fetch, JS) → Downstream agents
```

**Tech stack:** Flutter/Dart, Drift (SQLite), Provider+MVVM, 11 LLM providers (Gemini, OpenAI, Claude, Bedrock, Ollama...)

## Why It Matters for Solomon OS / Be Like You! OS
This is EXACTLY what the knowledge layer of Be Like You! OS should be. Local-first, multi-agent, SKILL.md standard, event-driven architecture.

**The agent system maps directly to what we need:**
- Each built-in agent (pkm_agent, card_agent, insight_agent, comment_agent, memory_agent, persona_agent) handles one domain
- Custom agents with SKILL.md standard — same as agentskills.io
- Event-driven with dependency chains
- JavaScript execution for skills
- Per-agent LLM configuration (different models for different tasks)

**For Be Like You! OS:**
- Replace Flutter with React Native or web app
- Use our Ollama stack instead of their LLM clients
- Wire into Solomon Bus for inter-agent communication
- Add as the "Solomon Memory" layer on the phone

## SKILL.md Standard
memex adopts the Agent Skills (agentskills.io) open standard. SKILL.md files contain:
- Frontmatter (name, description, compatibility)
- Instructions
- Scripts
- Resources

This is the SAME standard Hermes uses. Integration is trivial.

## Forked
✅ jvanleur2234-glitch/memex — forked and ready for integration

## LINK Fit
★★★★★ — #be-like-you-os #knowledge-layer #local-first #multi-agent #skills-standard
