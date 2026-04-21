# RD Report: LiveKit Agents — Realtime Voice AI Framework

**URL:** https://github.com/livekit/agents
**Date:** 2026-04-20
**Platform:** GitHub
**Stars:** ~10K
**License:** Apache 2.0

## What It Is
Python framework for building real-time voice AI agents that can see, hear, and understand. Runs server-side, integrates STT/LLM/TTS/realtime APIs, built-in job scheduling, WebRTC, and telephony.

## Key Features
- Flexible plugin system for STT, LLM, TTS providers
- Built-in job scheduling and dispatch APIs
- WebRTC client ecosystem (all platforms)
- Telephony integration (make/receive phone calls via LiveKit SIP)
- Data exchange via RPCs and Data APIs
- Semantic turn detection (transformer-based)
- Native MCP support (one line to connect MCP tools)
- Built-in test framework with judges
- Fully open-source, runs on your own servers

## What We'd Use It For
Voice AI agents for client interactions — phone/chatbot layer for Solomon OS. Could power a "AI receptionist" skill for the AI Employee Agency offering. Replaces manual telephony integrations.

## How It Compares to What We Have
- RENU API (port 5010) handles text/verse amplification
- LiveKit Agents would add voice layer on top
- Similar to Parlor Voice AI but more enterprise-grade (WebRTC + telephony)

## Recommendation
🟡 FORGE — Worth studying for the voice agent layer. Fork and experiment with a simple voice agent. Could integrate with Russell Tuna bot for richer voice interactions. Community is active, Apache 2.0 license is business-friendly.