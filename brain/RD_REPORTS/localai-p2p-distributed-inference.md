# LocalAI P2P Distributed Inference (PR #2343)

## Summary
- **URL:** https://github.com/mudler/LocalAI/pull/2343
- **Repo:** https://github.com/mudler/LocalAI (MIT License, 13k+ stars)
- **Feature:** Totally decentralized, private, P2P inference using llama.cpp

## What It Enables
LocalAI now supports fully decentralized, peer-to-peer inference across multiple machines. Key capabilities:
- **Two-entrypoint architecture:** HTTP server + llama worker nodes
- **Automatic discovery:** mDNS on LAN, DHT for remote discovery
- **No cloud dependency:** Peer-to-peer communication with shared token authentication
- **GGUF model support:** Relies on upstream llama.cpp distributed inference support
- **Cross-NAT operation:** Works across NATs and different networks via DHT

## Architecture
```
Server (runs with --p2p flag) → generates token
Workers (TOKEN=XXX ./local-ai p2p-llama-cpp-rpc) → connect via P2P
Communication: mDNS (local) + DHT (remote)
```

## Why It Matters for AgentFM Competitors
This is an alternative to AgentFM's P2P compute grid:
- **AgentFM:** Containerized workloads (Podman), live artifact streaming, libp2p mesh
- **LocalAI P2P:** LLMs via llama.cpp, zero-configuration discovery, HTTP-based routing
- **Different focus:** AgentFM does arbitrary containerized workloads; LocalAI P2P specifically targets LLM inference

## Relevance to Solomon OS / Hermes
- **Distributed inference** is a core capability for scaling agent workloads
- **No-cloud, private inference** aligns with enterprise/sovereign AI requirements
- **Hermes could leverage:** LocalAI as a P2P inference backend for privacy-sensitive deployments
- **Compare to:** Shard (browser P2P inference), Mycellm (P2P GPU inference), AgentFM (general P2P compute)

## Action Items
- [x] Forked: https://github.com/jvanleur2234-glitch/LocalAI
- [ ] Explore integration with Hermes Agent as a skill/node for distributed inference
- [ ] Compare against AgentFM, Shard, Mycellm for the distributed AI compute strategy

## Verdict
🟡 **WORTHWHILE** — Alternative P2P inference mechanism for llama.cpp. Useful if Solomon OS/Hermes needs privacy-preserving LLM inference without cloud dependencies. Lower priority than AgentFM for general compute, but solid for inference-specific use cases.