# RD Report: NVIDIA Build — Free Model API Credits

**URL:** https://build.nvidia.com/  
**Source:** https://x.com/NFTCPS/status/2046063617351844158  
**Date Queued:** 2026-04-20  
**Priority:** 🔴 CRITICAL  
**Tags:** free-api, llm, infrastructure, cost-reduction  

## What It Is
NVIDIA's official API platform at build.nvidia.com offering 1000+ free credits to registered users. Access to MiniMax M2.7, Kimi-K2.5, GLM-5, Llama, Qwen, Gemma 4, FLUX.2, DeepSeek, and 95+ models total. API key can be set to "Never Expire." Rate limit: ~40 req/min.

## What We'd Use It For
- **Primary free model API** for Solomon OS development and testing
- **Cost reduction** — run agents without burning paid API credits
- **Backup model layer** when primary providers hit limits
- **CI/CD testing** — free tier perfect for automated test pipelines
- **MiniMax M2.7 via NVIDIA** — same model we already use, free alternative

## How It Compares to What We Have
Currently using MiniMax via standard API (paid). NVIDIA offers the same/similar models FREE with rate limits that are fine for personal/dev use. AdolfoUsier confirmed minimax-m2.7 works on NVIDIA endpoints with Hermes.

## Key Constraints
- 40 req/min rate limit — not for production workloads but fine for dev/background
- Free credits have usage cap — can run out
- Credit policy can change at NVIDIA's discretion
- Need phone verification to register

## Recommendation
**FORGE — IMMEDIATE.** Sign up at build.nvidia.com, generate "Never Expire" key, add as secondary provider to Solomon OS. Use for dev, testing, and background workers. Map to Hermes capabilities as a skill.

## Action Items
1. Register at https://build.nvidia.com (Google/GitHub login)
2. Generate API key with "Never Expire" 
3. Save to Zo secrets as NVIDIA_API_KEY
4. Update Hermes capabilities doc
5. Configure OpenWebUI or Hermes to use NVIDIA as fallback provider
6. Test minimax-m2.7 via NVIDIA endpoint

## Related Posts (Confirming)
- Kai (@hqmank): "NVIDIA NIM free models, 12-month API key. Plugged into Hermes with minimax-m2.7 worked on first run"
- AdolfoUsier: Full OpenCrabs config for nvidia-minimax27 as custom provider
- Deniska: 95+ models available free until April 30 (GLM specifically)
- MiniMax Official: M2.7 now on NVIDIA GPU-accelerated endpoints