# RD Report: AgentFM

**Repo:** `Agent-FM/agentfm-core`  
**Fork:** Already forked  
**Stars:** Growing | **License:** MIT | **Lang:** Go  

## What It Does
P2P compute grid that turns idle GPUs into a decentralized AI supercomputer. Package agents as Podman containers, advertise on libp2p mesh, dispatch tasks peer-to-peer with end-to-end encryption.

## Why It Matters for Solomon OS
- **Direct Competitor to AgentFM** — We're building the same thing
- **Zero-Config P2P**: NAT traversal, DHT routing, mDNS, Circuit Relay built-in
- **Ephemeral Sandboxing**: Untrusted agents run in isolated Podman containers
- **GossipSub Load Balancing**: Workers broadcast CPU/GPU state, overloaded nodes auto-reject
- **Live Artifact Streaming**: Files dropped in /tmp/output stream back to Boss node
- **Enterprise Darknets**: Private swarms with PSK encryption for confidential workloads

## Key Capabilities
- Zero-config P2P networking with libp2p
- Podman container isolation for untrusted agents
- Hardware-aware task routing
- Language/framework agnostic (Python, Go, Rust, Node, Ollama, FLUX)
- Headless API gateway for n8n/Next.js integration
- Swarm keys for private networks

## Comparison to What We Have
This IS what we're building with KwaaiNet/solomon-os-agentic-stack. AgentFM is a direct competitor with more polish. Study their architecture for patterns.

## Recommendation
**STUDY** — Direct competitor. Analyze their architecture decisions for our KwaaiNet implementation. Fork anyway for reference.

**Category:** #distributed-ai #compute-grid #p2p #competitor
