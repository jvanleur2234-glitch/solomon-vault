# NemoClaw — Secure OpenClaw on NVIDIA OpenShell

**Fork**: Not needed (NVIDIA is well-funded, not going away)

**License**: Apache-2.0
**Stars**: ~18K
**Language**: TypeScript + Python

## What It Is

NVIDIA's reference stack for running OpenClaw agents inside hardened OpenShell sandboxes with NVIDIA Nemotron inference. It's the security answer to the CVE-2026-25253 vulnerability that hit OpenClaw earlier this year.

## Key Components

- **Sandboxed execution**: OpenShell-based microVM/container with enforced network + filesystem policies
- **Policy protections**: Network egress control, filesystem confinement to `/sandbox` + `/tmp`, restricted privileges
- **Inference routing**: Routes to NVIDIA cloud models via managed inference
- **Builder**: nemoclaw CLI (launch/connect/status/logs), Blueprint (YAML policy + orchestration), Sandbox

## Why It Matters

After the 0-click OpenClaw vulnerability (CVE-2026-25253) that let malicious websites hijack agents, NVIDIA built NemoClaw as the security-hardened alternative. It shows a major hyperscaler taking AI agent security seriously — and sets a precedent for AgentFM to compete with.

## Relevance to AgentFM / Solomon OS

- **Direct competitor**: NemoClaw is the enterprise answer to secure agent compute orchestration
- **Security pattern**: Sandboxed execution + policy-based network control is exactly what AgentFM does with Podman containers
- **Takeaway**: We should highlight AgentFM's P2P nature vs NemoClaw's NVIDIA-centric model as a differentiator

## Verdict

🔴 FORGE — Monitor NVIDIA's ecosystem. If they go multi-cloud with OpenShell, AgentFM needs to highlight its vendor-agnostic P2P approach as the open alternative.

**Next**: Check if OpenShell has open-source docs for integration.