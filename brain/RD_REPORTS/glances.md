# RD Report: Glances

**URL:** https://github.com/nicolargo/glances  
**Slug:** glances  
**Date:** 2026-04-26  
**Stars:** ~30K+  
**License:** LGPL v3  
**Language:** Python  

---

## What It Is

Glances is a cross-platform system monitoring tool written in Python. It provides real-time monitoring of CPU, memory, disk, network, processes, containers, temperatures, voltages, and more — in a terminal dashboard.

### Key Modes
- **Standalone** (`glances`) — terminal UI
- **Web server** (`glances -w`) — serves dashboard at `http://<ip>:61208`
- **Client/server** (`glances -s` server, `glances -c <ip>` client)
- **stdout export** (`--stdout`, `--stdout-json`, `--stdout-csv`) — machine-readable output
- **REST API** — exposed in web server mode
- **MCP server** (`--enable-mcp`) — AI assistant integration via SSE transport at `http://<ip>:61208/mcp/sse`
- **Python library** — import `glances.api` and query stats programmatically

### Export Targets
CSV, JSON, InfluxDB, Elasticsearch, PostgreSQL/TimeScale, Cassandra, ClickHouse, CouchDB, OpenTSDB, Prometheus, StatsD, Riemann, Graphite, RabbitMQ/ActiveMQ, NATS, ZeroMQ, Kafka, RESTful endpoints.

### Install
```bash
pip install 'glances[all]'    # full install
uvx glances                   # one-liner with uv
pipx install 'glances[all]'
```

---

## What We'd Use It For

### 1. Hermes Health Checks (FORGE)
Glances can be used to monitor the Zo server's system resources (CPU, memory, disk, network, containers). This could replace or supplement the existing Computer > Stats page. The `--stdout-json` output could feed into Hermes job logic — e.g., abort jobs if disk is critically low, or alert if memory is exhausted.

### 2. Solomon OS System Awareness (INTEGRATE)
Russell Tuna (Agent Orchestrator) could use Glances as a system awareness layer. When Hermes assigns a job, Russell could query Glances to understand current load before assigning. The MCP server integration is particularly interesting — Zo could query Glances directly as an AI assistant.

### 3. Remote Monitoring (SKILL)
Run Glances as a service (`glances -w`) on the Zo server and monitor it from anywhere via browser. This is simpler than SSH + htop.

---

## Comparison to What We Have

| Feature | Glances | Zo Built-in (Computer > Stats) |
|---|---|---|
| Terminal dashboard | ✓ | partial (top, df, etc.) |
| Web UI | ✓ | ✗ |
| REST API | ✓ | ✗ |
| MCP for AI agents | ✓ (4.5.1+) | ✗ |
| Container monitoring | ✓ | ✗ |
| Export/alerting | ✓ (many targets) | ✗ |
| Zero-install | uvx | N/A |

Zo already has basic `htop`, `df`, `free` via the terminal. Glances is a unified, prettier, API-first alternative with AI agent support.

---

## Recommendation

**FORGE + INTEGRATE**

1. **Quick win:** Install `glances[all]` and run `glances -w` as a private HTTP service on port 61208. Russell Tuna can check server health from anywhere.
2. **Medium-term:** Wire Glances MCP server into Zo's agent toolkit — this would let Zo query system stats natively.
3. **Long-term:** Replace the ad-hoc terminal monitoring in Solomon OS with structured Glances JSON output feeding into Hermes job decisions.

Not worth cloning the repo — just pip install and register as a service.
