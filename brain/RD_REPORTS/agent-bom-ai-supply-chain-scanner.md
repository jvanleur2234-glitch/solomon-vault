# RD Report: agent-bom — AI Supply Chain Security Scanner

**Fork:** https://github.com/jvanleur2234-glitch/agent-bom
**Source:** https://github.com/agent-bom/agent-bom
**License:** Apache 2.0
**Language:** Python + TypeScript
**Stars:** ~500 (growing fast — trending)

## What It Is
Open security scanner for AI supply chain: discovers installed AI agents, MCP servers, packages, containers, cloud configs, GPU workloads. Maps CVE blast radius: CVE → package → MCP server → agent → credentials → tools. 10-framework compliance (OWASP, NIST, EU AI Act, ATLAS). Policy-as-code enforcement.

## Key Features
- **Blast radius mapping:** tells you which agents, credentials, and tools are at risk from each CVE
- **Auto-discovery:** agents, MCP servers, GPU workloads, cloud configs (AWS/Snowflake/Databricks)
- **10 compliance frameworks:** OWASP, NIST, EU AI Act, ATLAS, MITRE, CISA KEV
- **Tool poisoning detection:** enforces security policies on agent tool access
- **SBOM generation:** CycloneDX format
- **Model provenance:** detects HF models (Llama, Claude, etc.) in use
- **Multi-format output:** JSON, HTML, SARIF
- **Demo mode:** `agent-bom agents --demo --offline` (no setup needed)

## Commands
```bash
agent-bom agents -p .              # Full scan with blast radius
agent-bom check flask@2.2.0         # Single package check
agent-bom image nginx:latest        # Container scan
agent-bom agents --demo --offline   # Reproducible demo
```

## Solomon OS Fit
**INTEGRATE** — Core security gate. Apache 2.0 license permits commercial use. Blast radius concept (CVE → agent → credentials → tools) directly applicable to JCPaid enterprise security. Policy-as-code for Hermes tool access.

## Comparison to Existing
- **Better than sinewave:** blast radius maps CVE to specific agents + credentials (sinewave detects but doesn't map blast)
- **Better than snyk-agent-scan:** maps to agent/credential layer, not just package CVEs
- **Better than Medusa:** adds compliance mapping and credential blast radius

## Action
Forked. Deploy as pre-deployment security gate for Hermes skill installation.

**Recommendation:** INTEGRATE — deploy as CI/CD security gate. Replace sinewave scanner for blast-radius mapping.