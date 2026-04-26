# RD Report: OpenGenerativeUI

**URL:** https://github.com/CopilotKit/OpenGenerativeUI  
**Stars:** ~700  
**License:** Apache 2.0  
**Added:** 2026-04-26  

## What It Is

Open-source showcase for building rich, interactive AI-generated UI with CopilotKit and LangChain Deep Agents. The agent produces generative UI — not just text, but fully interactive visual components: algorithm visualizations, 3D animations, charts, interactive widgets. Rendered in sandboxed iframes.

## Key Features

- Algorithm visualizations (binary search, BFS vs DFS, sorting)
- 3D animations (WebGL/CSS3D scenes)
- Charts & diagrams (pie, bar, network diagrams)
- Interactive widgets (forms, simulations, math plots)
- Sandboxed iframe rendering with auto light/dark theming
- MCP server included for integration with Claude Desktop, Claude Code, Cursor

## What We'd Use It For

- **Solomon OS dashboard UX** — upgrade the Zo Space landing page with live interactive widgets (job status, lead pipeline, etc.)
- **Client-facing portal** — generate rich visualizations for reports that clients can interact with
- **Russell Tuna visualization** — give him interactive visual aids for explaining concepts to clients

## How It Compares to What We Have

Zo Space pages are static React. OpenGenerativeUI shows a path to dynamic, AI-generated interactive visualizations. Could be a significant UX upgrade for Solomon OS client deliverables.

## Recommendation

**SKIP (Not a Fit Right Now)**  
Very experimental, requires strong models (GPT-5.4, Claude Opus 4, Gemini 3.1 Pro), and the setup is complex (Next.js frontend + LangGraph agent + MCP server). Interesting direction but not immediately actionable for Solomon OS. File for later when we have more mature UX needs.

## Files

- Source cloned to: `/tmp/open-generative-ui/`