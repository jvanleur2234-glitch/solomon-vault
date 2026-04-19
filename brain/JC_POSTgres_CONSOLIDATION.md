# JCPaid Postgres Consolidation — Replace Everything with One Database

**Date:** April 18, 2026
**Status:** RESEARCH COMPLETE — EXECUTION READY

## The Video Insight
Source: "I replaced my entire stack with Postgres" (YouTube, Apr 2026)

One Postgres database can replace:
- Redis (session cache) → JSONB
- RabbitMQ/Celery (job queue) → SKIP LOCKED
- Elasticsearch (search) → TSvector + GIN
- MongoDB (unstructured) → JSONB
- Pinecone (vectors) → pg_vector
- Snowflake (analytics) → Materialized Views
- GIS database → PostGIS
- Time-series DB → BRIN indexes

**Our stack collapses from 8 databases to 1.**

## Current JCPaid Stack

| Component | Current | Postgres Replacement |
|----------|---------|-------------------|
| Ollama embeddings | Pinecone $70/mo | pg_vector (FREE) |
| Session cache | Redis $0 | JSONB in Postgres |
| Job queue | RabbitMQ/Celery | SKIP LOCKED in Postgres |
| Full-text search | Elasticsearch $0 | TSvector + GIN |
| Unstructured data | MongoDB $0 | JSONB |
| Analytics | Manual | MatViews |
| File metadata | JSON files | Postgres rows |

**Total savings:** $70-200/mo in external services
**Complexity reduction:** 80%

## Implementation Plan

### Phase 1 — Consolidate Ollama + Search (Week 1)
```sql
-- Enable pg_vector
CREATE EXTENSION IF NOT EXISTS vector;

-- Documents with embeddings
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  content TEXT,
  embedding vector(1536),
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Full-text search
ALTER TABLE documents ADD COLUMN fts tsvector 
  GENERATED ALWAYS AS (to_tsvector('english', content)) STORED;
CREATE INDEX ON documents USING GIN(fts);

-- Vector similarity search
CREATE INDEX ON documents USING HNSW (embedding vector_cosine_ops);
```

### Phase 2 — Job Queue (Week 2)
```sql
-- Solomon Bus job queue
CREATE TABLE jobs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  queue TEXT NOT NULL,
  payload JSONB NOT NULL,
  status TEXT DEFAULT 'pending',
  priority INTEGER DEFAULT 0,
  run_at TIMESTAMPTZ DEFAULT now(),
  locked_by TEXT,
  locked_at TIMESTAMPTZ,
  completed_at TIMESTAMPTZ,
  error TEXT,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- SKIP LOCKED for safe concurrent dequeuing
CREATE INDEX ON jobs (queue, status, run_at) 
  WHERE status = 'pending';

-- Worker query:
-- SELECT * FROM jobs 
-- WHERE queue = 'default' AND status = 'pending' AND run_at <= now() 
-- ORDER BY priority DESC, run_at ASC 
-- FOR UPDATE SKIP LOCKED 
-- LIMIT 1;
```

### Phase 3 — Session Cache (Week 3)
```sql
-- HOT session state
CREATE TABLE sessions (
  id TEXT PRIMARY KEY,
  data JSONB DEFAULT '{}',
  expires_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Auto-expire with PostgreSQL partition pruning
CREATE INDEX ON sessions (expires_at) 
  WHERE expires_at IS NOT NULL;
```

### Phase 4 — Full Analytics (Week 4)
```sql
-- Business metrics as materialized views
CREATE MATERIALIZED VIEW daily_revenue AS
SELECT 
  date(created_at) as day,
  count(*) as transactions,
  sum(amount) as revenue
FROM transactions
GROUP BY day;

CREATE MATERIALIZED VIEW content_performance AS
SELECT
  content_id,
  views,
  clicks,
  watch_time,
  ctas
FROM content_metrics
ORDER BY created_at DESC;
```

## Migration Sequence

1. **Add pg_vector to our existing Postgres** (already have)
2. **Move Ollama embeddings → pg_vector** (drop Pinecone)
3. **Implement job queue with SKIP LOCKED** (drop RabbitMQ)
4. **Add TSvector search** (supplements Elasticsearch)
5. **Consolidate JSON file storage → JSONB tables**
6. **Build MatViews for dashboards** (replace manual spreadsheets)

## File Locations

- **be-like-you-nomad/** — Fork of N.O.M.A.D. for offline knowledge layer
- **clawless/** — Browser-based agent runtime for Solomon Browser

## Repo Links
- be-like-you-nomad: https://github.com/jvanleur2234-glitch/be-like-you-nomad
- clawless: https://github.com/jvanleur2234-glitch/clawless