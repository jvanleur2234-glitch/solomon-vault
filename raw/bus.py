#!/usr/bin/env python3
"""
JCPaid Bus — SQLite-based inter-agent dispatch + flag system
Inspired by The Agency ISCP pattern
"""

import sqlite3
import hashlib
import json
import uuid
from datetime import datetime, timedelta
from pathlib import Path
import argparse

DB_PATH = Path("./jcpaid-bus.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS dispatch_queue (
            id TEXT PRIMARY KEY,
            agent TEXT NOT NULL,
            task TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            priority TEXT DEFAULT 'normal',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            result TEXT,
            metadata TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS flags (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            agent TEXT,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS receipts (
            id TEXT PRIMARY KEY,
            task_id TEXT,
            agent TEXT NOT NULL,
            action TEXT NOT NULL,
            result TEXT NOT NULL,
            hash TEXT NOT NULL,
            prev_hash TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            agent TEXT PRIMARY KEY,
            status TEXT DEFAULT 'active',
            paused_at TEXT,
            state TEXT
        )
    """)
    conn.commit()
    return conn

# --- Dispatch ---
def dispatch(agent: str, task: str, priority: str = "normal", metadata: dict = None):
    conn = get_db()
    c = conn.cursor()
    task_id = str(uuid.uuid4())[:8]
    c.execute(
        "INSERT INTO dispatch_queue (id, agent, task, priority, metadata) VALUES (?, ?, ?, ?, ?)",
        (task_id, agent, task, priority, json.dumps(metadata or {}))
    )
    conn.commit()
    print(f"✓ Dispatched [{task_id}] to {agent}: {task}")
    return task_id

def list_queue(agent: str = None, status: str = None):
    conn = get_db()
    c = conn.cursor()
    q = "SELECT * FROM dispatch_queue WHERE 1=1"
    args = []
    if agent:
        q += " AND agent = ?"
        args.append(agent)
    if status:
        q += " AND status = ?"
        args.append(status)
    q += " ORDER BY created_at DESC"
    rows = c.execute(q, args).fetchall()
    if not rows:
        print("No tasks found.")
        return
    for r in rows:
        print(f"[{r['id']}] {r['agent']} | {r['status']} | {r['task'][:60]}")

def complete(task_id: str, result: str):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "UPDATE dispatch_queue SET status = 'completed', result = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (result, task_id)
    )
    conn.commit()
    print(f"✓ Completed [{task_id}]: {result}")

# --- Flags ---
def set_flag(key: str, value: str, agent: str = None):
    conn = get_db()
    conn.execute(
        "INSERT OR REPLACE INTO flags (key, value, agent, updated_at) VALUES (?, ?, ?, CURRENT_TIMESTAMP)",
        (key, value, agent)
    )
    conn.commit()
    print(f"✓ Flag: {key} = {value}")

def get_flag(key: str):
    conn = get_db()
    r = conn.execute("SELECT * FROM flags WHERE key = ?", (key,)).fetchone()
    if r:
        print(f"{r['key']} = {r['value']} (agent={r['agent']})")
    else:
        print(f"Flag not found: {key}")

def list_flags():
    conn = get_db()
    rows = conn.execute("SELECT * FROM flags ORDER BY updated_at DESC").fetchall()
    for r in rows:
        print(f"{r['key']} = {r['value']} | {r['updated_at']}")

# --- Receipts (hash-chained) ---
def create_receipt(task_id: str, agent: str, action: str, result: str):
    conn = get_db()
    c = conn.cursor()
    prev = c.execute("SELECT hash FROM receipts ORDER BY created_at DESC LIMIT 1").fetchone()
    prev_hash = prev["hash"] if prev else "GENESIS"
    receipt_id = str(uuid.uuid4())[:12]
    payload = f"{receipt_id}{task_id}{agent}{action}{result}{prev_hash}"
    h = hashlib.sha256(payload.encode()).hexdigest()[:16]
    c.execute(
        "INSERT INTO receipts (id, task_id, agent, action, result, hash, prev_hash) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (receipt_id, task_id, agent, action, result, h, prev_hash)
    )
    conn.commit()
    print(f"✓ Receipt [{receipt_id}] {h} — {agent}: {action}")
    return receipt_id

def verify_receipts():
    conn = get_db()
    rows = conn.execute("SELECT * FROM receipts ORDER BY created_at ASC").fetchall()
    prev = "GENESIS"
    ok = True
    for r in rows:
        payload = f"{r['id']}{r['task_id']}{r['agent']}{r['action']}{r['result']}{r['prev_hash']}"
        h = hashlib.sha256(payload.encode()).hexdigest()[:16]
        if h != r["hash"] or r["prev_hash"] != prev:
            ok = False
            print(f"✗ FAIL at [{r['id']}]")
        prev = r["hash"]
    if ok:
        print("✓ All receipts verified — chain intact")

# --- Sessions ---
def pause(agent: str, state: str = None):
    conn = get_db()
    conn.execute(
        "INSERT OR REPLACE INTO sessions (agent, status, paused_at, state) VALUES (?, 'paused', CURRENT_TIMESTAMP, ?)",
        (agent, state)
    )
    conn.commit()
    print(f"⏸ Paused: {agent}")

def resume(agent: str):
    conn = get_db()
    r = conn.execute("SELECT state FROM sessions WHERE agent = ?", (agent,)).fetchone()
    if r:
        conn.execute("UPDATE sessions SET status = 'active' WHERE agent = ?", (agent,))
        conn.commit()
        print(f"▶ Resumed: {agent} (state={r['state']})")
    else:
        print(f"No session found for {agent}")

if __name__ == "__main__":
    init_db()
    parser = argparse.ArgumentParser(description="JCPaid Bus CLI")
    sub = parser.add_subparsers(dest="cmd")
    
    d = sub.add_parser("dispatch", help="Dispatch a task")
    d.add_argument("--agent"); d.add_argument("--task"); d.add_argument("--priority", default="normal")
    
    q = sub.add_parser("queue", help="List queue")
    q.add_argument("--agent", nargs="?"); q.add_argument("--status", nargs="?")
    
    c = sub.add_parser("complete")
    c.add_argument("--task-id"); c.add_argument("--result")
    
    f = sub.add_parser("flag")
    f.add_argument("action", choices=["set","get","list"])
    f.add_argument("key", nargs="?"); f.add_argument("value", nargs="?"); f.add_argument("--agent", nargs="?")
    
    r = sub.add_parser("receipt")
    r.add_argument("action", choices=["create","verify"])
    r.add_argument("--task-id", nargs="?"); r.add_argument("--agent", nargs="?"); r.add_argument("--action", nargs="?"); r.add_argument("--result", nargs="?")
    
    s = sub.add_parser("session")
    s.add_argument("op", choices=["pause","resume"]); s.add_argument("agent"); s.add_argument("--state", nargs="?")
    
    args = parser.parse_args()
    if args.cmd == "dispatch":
        dispatch(args.agent, args.task, args.priority)
    elif args.cmd == "queue":
        list_queue(args.agent, args.status)
    elif args.cmd == "complete":
        complete(args.task_id, args.result)
    elif args.cmd == "flag":
        if args.action == "set": set_flag(args.key, args.value, args.agent)
        elif args.action == "get": get_flag(args.key)
        else: list_flags()
    elif args.cmd == "receipt":
        if args.action == "create": create_receipt(args.task_id, args.agent, args.action, args.result)
        else: verify_receipts()
    elif args.cmd == "session":
        if args.op == "pause": pause(args.agent, args.state)
        else: resume(args.agent)
    else:
        parser.print_help()
