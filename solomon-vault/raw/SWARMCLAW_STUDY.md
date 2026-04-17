# SwarmClaw Architecture Study — Apr 6, 2026

## What It Is
swarmclawai/swarmclaw — 254 stars, 43 forks
Multi-agent chat platform with fleet management, session orchestration, and a clean plugin system.

## Key Files Studied
- CLAUDE.md — Development guidelines (excellent)
- src/lib/providers/index.ts — Provider registry (most valuable)
- src/lib/server/runtime/session-run-manager.ts — Chat execution pipeline
- src/lib/server/storage.ts — Persistence layer

## Patterns to Steal for Solomon OS / Hermes

### 1. Provider Registry Pattern
SwarmClaw uses a clean registry of LLM providers where each provider is a thin wrapper around streamOpenAiChat. This is exactly how we should structure Hermes's multi-model routing.

```typescript
// Key insight: providers ARE JUST openAI-compatible wrappers with a patched baseURL
streamChat: (opts) => {
  const patchedSession = {
    ...opts.session,
    apiEndpoint: opts.session.apiEndpoint || 'https://api.together.xyz/v1',
  }
  return streamOpenAiChat({ ...opts, session: patchedSession })
}
```

### 2. Session Run Manager Pipeline
enqueueSessionRun() with:
- Dedup (same dedupeKey = dropped)
- Collect-mode coalescing (1500ms window merges rapid messages)
- Heartbeat preemption (user chat aborts running heartbeat)
- Execution lock (one turn per session at a time)
- Queue for others

### 3. setIfChanged for Zustand
Instead of raw set() which triggers re-renders on every poll, use setIfChanged with JSON fingerprinting to skip renders when data hasn't changed.

### 4. Provider Credential Failover
streamChatWithFailover() tries multiple credentials in sequence on 401/429/500/502/503, with automatic backoff.

### 5. Extension System
getExtensionManager().getProviders() — extensions can register as providers. Clean plugin architecture.

## Not Relevant for Solomon OS
- Frontend UI patterns (React/Next.js specific)
- WebSocket chat protocol
- OpenClaw agent protocol
- Fleet management UI
