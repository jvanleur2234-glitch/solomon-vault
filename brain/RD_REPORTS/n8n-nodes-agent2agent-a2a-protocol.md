# RD Report: n8n-nodes-agent2agent — Google A2A Protocol Bridge

**Date:** 2026-04-23  
**URL:** https://github.com/pjawz/n8n-nodes-agent2agent  
**License:** MIT  

## What It Does
n8n community node connecting workflows to AI agents via Google's Agent2Agent (A2A) protocol. Discovers agents via Agent Card, sends tasks (text/file/JSON), waits for completion, retrieves results or cancels.

## Key Operations
- **Discover Agent** — fetches Agent Card at `/.well-known/agent.json`
- **Send Task** — initiate/continue tasks with TextPart, FilePart, DataPart
- **Get Task** — retrieve status, history, artifacts
- **Cancel Task** — cancel ongoing tasks

## Why It Matters
A2A is Google's standard for agent-to-agent communication. This n8n node bridges enterprise automation workflows to the emerging A2A agent ecosystem.

## Solomon OS Fit
**INTEGRATE** — A2A protocol bridge for n8n. If Hermes implements A2A (agent cards, task protocol), this enables n8n → Hermes integration without MCP. JackConnect workflow builder could use A2A to talk to Hermes agents.

## Status
**INTEGRATE** — Monitor A2A ecosystem. If Hermes adopts A2A, this becomes a primary integration path.
