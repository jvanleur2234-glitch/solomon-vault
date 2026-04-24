# miguel — Self-Improving Agent with Rollback

**Date:** 2026-04-23  
**URL:** https://github.com/soulfir/miguel  
**License:** MIT  
**Stars:** ~500+

## What It Does
Self-improving AI agent that reads, modifies, and extends its own source code inside a sandboxed Docker environment. Autonomous improvement implementation, new tool creation, prompt rewriting, and validation with automatic rollback on failures. Multi-agent coordinator with Coder/Researcher/Analyst sub-agents.

## Key Components
- **Self-modification** — rewrites own code, adds tools, expands capabilities
- **Self-validation** — syntax-checked, imports verified, git commits; rollback on failure
- **Self-management** — context window monitoring, task delegation, state auto-compaction
- **Multi-agent collaboration** — coordinator + Coder + Researcher + Analyst sub-agents
- **Cross-session memory** — continuous auto-commit/push after improvements

## Solomon OS Fit
**FORGE** — Self-validation with rollback IS the safe self-improvement gate for Hermes. Miguel's Docker sandbox + git commit discipline = the safety pattern we need for autonomous code generation. MIT license permits direct use.

## Status
**FORGE** — Implement rollback discipline for Hermes self-improvement loop. Study Docker sandboxing for safe code gen.