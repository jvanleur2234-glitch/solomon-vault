# JCPaid Bus — Hermes Skill

**Purpose:** SQLite-based task queue, flags, and receipts for Hermes multi-agent coordination

## Tools

### dispatch
Dispatches a task to a specific agent.
- `agent`: Target agent (sales, marketing, support, finance)
- `task`: Task description
- `priority`: normal | high | urgent

### queue
Lists pending tasks for an agent or all agents.
- `agent`: Filter by agent (optional)
- `status`: Filter by status (pending, completed, failed)

### complete
Marks a task as completed with a result.
- `task_id`: The task ID from dispatch
- `result`: What was accomplished

### flag
Manages inter-agent flags.
- `set key value`: Set a flag
- `get key`: Get a flag value
- `list`: List all flags

### receipt
Creates or verifies QGR receipts.
- `create`: Creates hash-chained receipt
- `verify`: Verifies chain integrity

### session
Manages agent session state.
- `pause agent --state`: Pause agent session
- `resume agent`: Resume agent session

## Usage

```
@jcpaid-bus dispatch sales "Follow up with lead #123"
@jcpaid-bus queue sales pending
@jcpaid-bus complete 3f5d051f "Closed $5K deal"
@jcpaid-bus flag set paused sales
@jcpaid-bus receipt create --agent sales --action "Closed deal" --result "$5K"
```

## Database

SQLite at `./jcpaid-bus.db` — stored in workspace for persistence.
