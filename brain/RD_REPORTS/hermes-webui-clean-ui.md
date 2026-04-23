# hermes-webui — Clean Web UI for Hermes Agent

**Date:** April 23, 2026  
**Fork:** https://github.com/jvanleur2234-glitch/hermes-webui  
**License:** MIT  
**Stars:** ~500+ (rising fast)  
**Language:** Python + Vanilla JS (no build step, no framework)

## What It Is

Lightweight, dark-themed web UI for Hermes Agent. Full CLI parity from browser — three-panel layout (sessions sidebar, chat center, file browser right). Built by Nathan Esquenazi (@nesquena) after community demand for "OpenCode-style UI."

## Key Features

- **Zero-build interface** — plain Python + vanilla JS, no React, no bundler
- **Full Hermes parity** — everything CLI does, UI does too
- **Session projects, tags, tool call cards** — rich session management
- **Workspace file browser** — inline preview, live file tree
- **Hermes Control Center** — launcher at sidebar bottom for all settings
- **Token ring visualization** — circular context ring shows token usage
- **Light/dark mode + profile support**
- **Single command start** + SSH tunnel for secure remote access

## Solomon OS Relevance

- Gives Hermes a clean browser UI without switching terminals
- Can run behind SSH tunnel for security
- Supports profile management for multi-user scenarios
- Built-in workspace browser matches Solomon Vault structure

## Integration Path

```
hermes-agent → hermes-webui → browser (local or SSH tunnel)
```

## Comparison to Alternatives

| Feature | hermes-webui | agent-express | gollem |
|---------|-------------|---------------|--------|
| Build step | None | None | None |
| Framework | Vanilla JS | TypeScript | Go |
| CLI parity | ✅ Full | ❌ | ❌ |
| Skills/MCP | ✅ Native | ✅ MCP | ❌ |
| MIT licensed | ✅ | ✅ | ✅ |

## Status

**FORKEd** → jvanleur2234-glitch/hermes-webui ✅  
**Recommendation:** INTEGRATE — clean UI, no build friction, native Hermes support