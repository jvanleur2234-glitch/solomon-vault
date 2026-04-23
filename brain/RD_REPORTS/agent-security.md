# agent-security — Static Analysis + Runtime Guards

**Repo:** `empowered-humanity/agent-security` | **License:** MIT | **Lang:** TypeScript

## What It Is
Static analysis and runtime security library for AI agent architectures. 220+ AI-agent-specific patterns, 65 mapped to OWASP ASI, 44 MCP security patterns.

## Key Capabilities
- Taint/proximity-based analysis, cross-file dataflow tracking
- Runtime guards: SSRF, path traversal, exec allowlisting, download enforcement, webhook verification
- CWE mappings (30+ categories)
- SARIF output for GitHub Code Scanning
- GitHub Action + pre-commit hook integration
- **Focuses on:** prompt injection, credential exposure, MCP misconfigs, code injection, agent-specific attack patterns

## Solomon OS Fit
- **OWASP alignment:** 65 patterns mapped to OWASP ASI — critical for Hermes security hardening
- **MCP security:** 44 MCP-specific patterns directly relevant to Hermes' MCP tool ecosystem
- **CI/CD integration:** Pre-commit + GitHub Action fits JCPaid DevSecOps pipeline
- **LINK fit:** ★★★★★ — #security #owasp #mcp #static-analysis

## Action
Already forked. Write RD deep-dive. Add to HERMES_CAPABILITIES. Priority: HIGH.
