# RD Report: AgentFM Core — P2P Containerized AI Compute Fabric

## Summary
AgentFM core by Agent-FM is a peer-to-peer, zero-configuration network turning idle consumer hardware into decentralized AI compute. Publish AI tasks as Podman containers to public mesh or private Darknets. Isolated container execution, results streamed to Boss node. GossipSub telemetry, load-balancing. Framework-agnostic (Python, Go, Rust, Node). MIT.

## What It Does
- **P2P Networking**: Libp2p (AutoNAT, Kademlia DHT, mDNS, Circuit Relay v2)
- **Zero-Config**: No manual network setup
- **Containerized Tasks**: Podman isolation for security
- **Public Mesh + Private Darknets**: Swarm key for encrypted intranets
- **Live Telemetry**: GossipSub, hardware state advertising, load-aware task rejection
- **Framework-Agnostic**: Python, Go, Rust, Node
- **Local LLMs**: Llama 3.2, FLUX supported
- **Radar UI**: Command center for mesh monitoring
- **Headless API**: Trigger tasks from apps/workflows

## Tech Stack
- Language: Go
- License: MIT
- Reqs: Go 1.25+, Podman

## Strategic Fit for Solomon OS

**WATCH** — Direct AgentFM competitor. Study P2P compute mesh patterns.

Key learnings:
1. **Zero-Config P2P**: AutoNAT + Circuit Relay = NAT traversal without configuration
2. **Container Isolation**: Podman security for untrusted task code
3. **GossipSub Telemetry**: Real-time mesh health monitoring
4. **Load Balancing**: Prevent host crashes from overcommitment

## Risk/Concerns
- Requires Go 1.25+ (cutting edge)
- Podman required
- New project, community building

## Verdict
WATCH — Monitor as AgentFM competitor. Study libp2p patterns for Solomon Air P2P networking. Load balancing prevents resource exhaustion attacks.

## Links
- Repo: https://github.com/Agent-FM/agentfm-core
- Fork: Already forked