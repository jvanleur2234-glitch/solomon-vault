# R&D Report: Hermes + NVIDIA NIM — Free Minimax 2.7

**Date:** April 19, 2026

## Summary
- **Source:** @eternityspring on X, 342 likes
- **What it is:** 4-step setup to get free Minimax 2.7 via NVIDIA NIM API, integrated into Hermes agent
- **Cost:** FREE — NVIDIA gives 40 calls/min on free tier
- **Models available:** NVIDIA NIM hosts Minimax 2.7, Llama, Mistral, Gemma, and more

## How to Set Up
1. Get NVIDIA API key: build.nvidia.com/settings/api-keys
2. Run `hermes update` — update to latest version
3. Run `hermes model` — select "NVIDIA NIM" 
4. Paste the API key

## Current Hermes Config
```
HERMES_INFERENCE_PROVIDER=custom
HERMES_INFERENCE_BASE_URL=http://localhost:20128/v1
HERMES_INFERENCE_MODEL=if/glm-4.7
```
Already has custom endpoint. Need to switch to NVIDIA NIM.

## Strategic Fit for JCPaid
- FREE Minimax 2.7 = no API costs for AI workers
- Already integrated into Hermes = works with existing skills
- 40 calls/min free = enough for personal use
- At scale: NVIDIA NIM pricing is $0.10-0.50/M tokens = still cheaper than OpenAI

## Action
1. Joseph needs NVIDIA API key (30 seconds to get)
2. Configure HERMES_INFERENCE_BASE_URL to NVIDIA NIM endpoint
3. Set HERMES_INFERENCE_MODEL to nvidia/nim/minimax-2.7

## Status
🔥 ACTIONABLE — Waiting for Joseph's NVIDIA API key