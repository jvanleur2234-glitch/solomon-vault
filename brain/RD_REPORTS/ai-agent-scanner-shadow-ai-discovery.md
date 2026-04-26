# RD Report: ai-agent-scanner — Shadow AI Discovery + Security

**Original:** `perfecxion-ai/ai-agent-scanner` | **License:** GPL-3.0 | **Stars:** ~500+ | **Lang:** Python

## What It Is
Discovers AI agents across your environment, performs vulnerability testing, maps findings to compliance risk. Unique focus on "shadow AI" discovery — finds unknown/unsanctioned AI agents.

## Key Capabilities
- Discovery: Network endpoints, Code (SDKs, API keys, configs), Traffic (AI API calls), Cloud (SageMaker, Bedrock, Azure, Vertex)
- Vulnerability testing of discovered AI agents
- Risk scoring per asset
- Compliance mapping: GDPR, SOC 2, HIPAA, NIST AI RMF, EU AI Act
- SARIF output for CI/CD integration
- Shadow AI detection (finds AI you didn't know was running)

## Relevance to Solomon OS
- **Discovery:** Inventory all AI agents in environment
- **Compliance:** Automated compliance mapping for enterprise clients
- **Security:** Vulnerability assessment of deployed agents

## Threat Analysis
- GPL-3.0 (not MIT/Apache — commercial use restrictions)
- Active development (latest v1.1.0, Mar 2026)
- Strong compliance mapping

## Integration Path
```
TOOL: ai-agent-scanner → Discovery/inventory tool for Solomon OS deployments
USE CASE: Enterprise clients need to know ALL AI agents running in their environment
NOTE: GPL-3.0 — consider for internal use or negotiate commercial license
```

**Recommendation:** SKILL — Shadow AI discovery is valuable for enterprise. Study compliance mapping patterns. Note GPL-3.0 licensing.