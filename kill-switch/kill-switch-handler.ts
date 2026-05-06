import type { Context } from "hono";
import { hash } from "node:crypto";
import { readFileSync, writeFileSync, existsSync, mkdirSync } from "node:fs";
import { join } from "node:path";

// ─── Types ───────────────────────────────────────────────────────────────────

interface Agent {
  id: string;
  name: string;
  role: "innovator" | "closer" | "support" | "admin" | "custom";
  budgetCap: number;       // cents per cycle (monthly)
  warningPct: number;      // 0-100, default 80
  status: "active" | "paused" | "terminated";
  createdAt: string;
  updatedAt: string;
}

interface AuditEntry {
  id: string;
  timestamp: string;
  agentId: string;
  action: "agent_created" | "agent_updated" | "agent_paused" | "agent_resumed" | "agent_terminated" | "budget_warning" | "budget_hard_stop" | "approval_requested" | "approval_granted" | "approval_denied" | "override";
  actor: "system" | "founder" | "agent";
  details: string;
  prevHash: string;
  hash: string;
}

interface ApprovalRequest {
  id: string;
  agentId: string;
  category: "external_communications" | "publishing" | "financial" | "structural" | "strategy";
  description: string;
  status: "pending" | "granted" | "denied";
  requestedAt: string;
  resolvedAt?: string;
  resolver?: string;
}

// ─── File Paths ──────────────────────────────────────────────────────────────

const DATA_DIR = "/home/workspace/solomon-vault/kill-switch";
const AGENTS_FILE = join(DATA_DIR, "agents.json");
const AUDIT_FILE = join(DATA_DIR, "audit.json");
const APPROVALS_FILE = join(DATA_DIR, "approvals.json");

// ─── Storage Helpers ─────────────────────────────────────────────────────────

function ensureDataDir() {
  if (!existsSync(DATA_DIR)) mkdirSync(DATA_DIR, { recursive: true });
}

function readAgents(): Agent[] {
  ensureDataDir();
  if (!existsSync(AGENTS_FILE)) return [];
  try { return JSON.parse(readFileSync(AGENTS_FILE, "utf-8")); } catch { return []; }
}

function writeAgents(agents: Agent[]) {
  ensureDataDir();
  writeFileSync(AGENTS_FILE, JSON.stringify(agents, null, 2));
}

function readAudit(): AuditEntry[] {
  ensureDataDir();
  if (!existsSync(AUDIT_FILE)) return [];
  try { return JSON.parse(readFileSync(AUDIT_FILE, "utf-8")); } catch { return []; }
}

function writeAudit(entries: AuditEntry[]) {
  ensureDataDir();
  writeFileSync(AUDIT_FILE, JSON.stringify(entries, null, 2));
}

function readApprovals(): ApprovalRequest[] {
  ensureDataDir();
  if (!existsSync(APPROVALS_FILE)) return [];
  try { return JSON.parse(readFileSync(APPROVALS_FILE, "utf-8")); } catch { return []; }
}

function writeApprovals(requests: ApprovalRequest[]) {
  ensureDataDir();
  writeFileSync(APPROVALS_FILE, JSON.stringify(requests, null, 2));
}

// ─── Audit Hash Chain ─────────────────────────────────────────────────────────

function hashEntry(entry: Omit<AuditEntry, "hash">): string {
  return hash("sha256", JSON.stringify(entry));
}

function appendAudit(entry: Omit<AuditEntry, "hash">): AuditEntry {
  const audit = readAudit();
  const prevHash = audit.length > 0 ? audit[audit.length - 1].hash : "GENESIS";
  const full: AuditEntry = { ...entry, prevHash, hash: "" };
  full.hash = hashEntry(full);
  audit.push(full);
  writeAudit(audit);
  return full;
}

// ─── Budget Tracking ─────────────────────────────────────────────────────────

interface SpendRecord {
  agentId: string;
  cycle: string;        // "YYYY-MM"
  spent: number;       // cents
  lastUpdated: string;
}

const SPEND_FILE = join(DATA_DIR, "spend.json");

function readSpend(): SpendRecord[] {
  ensureDataDir();
  if (!existsSync(SPEND_FILE)) return [];
  try { return JSON.parse(readFileSync(SPEND_FILE, "utf-8")); } catch { return []; }
}

function writeSpend(records: SpendRecord[]) {
  ensureDataDir();
  writeFileSync(SPEND_FILE, JSON.stringify(records, null, 2));
}

function getCurrentCycle(): string {
  return new Date().toISOString().slice(0, 7);
}

function getAgentSpend(agentId: string): number {
  const cycle = getCurrentCycle();
  const spend = readSpend();
  const record = spend.find(r => r.agentId === agentId && r.cycle === cycle);
  return record?.spent ?? 0;
}

function recordSpend(agentId: string, cents: number) {
  const cycle = getCurrentCycle();
  const spend = readSpend();
  const idx = spend.findIndex(r => r.agentId === agentId && r.cycle === cycle);
  const now = new Date().toISOString();
  if (idx >= 0) {
    spend[idx].spent += cents;
    spend[idx].lastUpdated = now;
  } else {
    spend.push({ agentId, cycle, spent: cents, lastUpdated: now });
  }
  writeSpend(spend);
}

function canSpend(agentId: string, amount: number): { allowed: boolean; reason?: string; hardStop?: boolean } {
  const agents = readAgents();
  const agent = agents.find(a => a.id === agentId);
  if (!agent || agent.status !== "active") return { allowed: false, reason: "Agent not found or not active", hardStop: true };
  if (agent.status === "paused" || agent.status === "terminated") return { allowed: false, reason: `Agent is ${agent.status}`, hardStop: true };

  const current = getAgentSpend(agentId);
  const projected = current + amount;
  const cap = agent.budgetCap;
  const warning = cap * (agent.warningPct / 100);

  if (projected >= cap) {
    recordSpend(agentId, amount);
    appendAudit({
      id: crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      agentId,
      action: "budget_hard_stop",
      actor: "system",
      details: `Attempted $${(amount/100).toFixed(2)} spend would exceed cap of $${(cap/100).toFixed(2)}. Current: $${(current/100).toFixed(2)}. Hard stop enforced.`,
    });
    return { allowed: false, reason: `Budget hard cap reached ($${(cap/100).toFixed(2)}/cycle)`, hardStop: true };
  }

  if (projected >= warning && current < warning) {
    recordSpend(agentId, amount);
    appendAudit({
      id: crypto.randomUUID(),
      timestamp: new Date().toISOString(),
      agentId,
      action: "budget_warning",
      actor: "system",
      details: `Budget warning: $${(projected/100).toFixed(2)} of $${(cap/100).toFixed(2)} cap (${agent.warningPct}% threshold)`,
    });
    return { allowed: true, reason: `Budget warning: $${(projected/100).toFixed(2)} of $${(cap/100).toFixed(2)}` };
  }

  recordSpend(agentId, amount);
  return { allowed: true };
}

// ─── Helper: auth check (bearer token) ───────────────────────────────────────

function requireAuth(c: Context): { authorized: boolean; founderId?: string } {
  const secret = process.env.JCPAID_KILL_SWITCH_SECRET;
  if (!secret) return { authorized: true }; // no secret configured = open for now
  const auth = c.req.header("authorization");
  if (!auth?.startsWith("Bearer ")) return { authorized: false };
  const token = auth.slice(7);
  if (token !== secret) return { authorized: false };
  return { authorized: true, founderId: "founder" };
}

// ─── API Handlers ─────────────────────────────────────────────────────────────

function notAuthorized(c: Context) {
  return c.json({ error: "Unauthorized" }, 401);
}

// GET /api/kill-switch/health
function health(c: Context) {
  return c.json({ status: "ok", ts: new Date().toISOString() });
}

// GET /api/kill-switch/agents
function listAgents(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const agents = readAgents();
  const cycle = getCurrentCycle();
  const spend = readSpend();
  const result = agents.map(a => {
    const rec = spend.find(r => r.agentId === a.id && r.cycle === cycle);
    return { ...a, spentThisCycle: rec?.spent ?? 0 };
  });
  return c.json({ agents: result });
}

// POST /api/kill-switch/agents
function createAgent(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const body = await c.req.json();
  const { name, role = "custom", budgetCap = 5000, warningPct = 80 } = body;
  if (!name) return c.json({ error: "name required" }, 400);

  const agents = readAgents();
  const now = new Date().toISOString();
  const agent: Agent = {
    id: `agent_${Date.now()}_${Math.random().toString(36).slice(2, 7)}`,
    name,
    role,
    budgetCap: Math.round(budgetCap),
    warningPct: Math.round(warningPct),
    status: "active",
    createdAt: now,
    updatedAt: now,
  };
  agents.push(agent);
  writeAgents(agents);
  appendAudit({
    id: crypto.randomUUID(),
    timestamp: now,
    agentId: agent.id,
    action: "agent_created",
    actor: auth.founderId ?? "founder",
    details: `Created agent "${name}" (${role}) with $${(budgetCap/100).toFixed(2)}/cycle cap`,
  });
  return c.json({ agent }, 201);
}

// GET /api/kill-switch/agents/:id
function getAgent(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const agents = readAgents();
  const agent = agents.find(a => a.id === id);
  if (!agent) return c.json({ error: "not found" }, 404);
  const cycle = getCurrentCycle();
  const spend = readSpend();
  const rec = spend.find(r => r.agentId === id && r.cycle === cycle);
  return c.json({ agent: { ...agent, spentThisCycle: rec?.spent ?? 0 } });
}

// PATCH /api/kill-switch/agents/:id
function updateAgent(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const body = await c.req.json();
  const agents = readAgents();
  const idx = agents.findIndex(a => a.id === id);
  if (idx < 0) return c.json({ error: "not found" }, 404);
  const now = new Date().toISOString();
  const updated: Agent = { ...agents[idx], ...body, id: agents[idx].id, createdAt: agents[idx].createdAt, updatedAt: now };
  agents[idx] = updated;
  writeAgents(agents);
  appendAudit({
    id: crypto.randomUUID(),
    timestamp: now,
    agentId: id,
    action: "agent_updated",
    actor: auth.founderId ?? "founder",
    details: `Updated: ${Object.keys(body).join(", ")}`,
  });
  return c.json({ agent: updated });
}

// POST /api/kill-switch/agents/:id/pause
function pauseAgent(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const agents = readAgents();
  const idx = agents.findIndex(a => a.id === id);
  if (idx < 0) return c.json({ error: "not found" }, 404);
  const now = new Date().toISOString();
  agents[idx].status = "paused";
  agents[idx].updatedAt = now;
  writeAgents(agents);
  appendAudit({ id: crypto.randomUUID(), timestamp: now, agentId: id, action: "agent_paused", actor: auth.founderId ?? "founder", details: `Agent paused by founder` });
  return c.json({ ok: true, agent: agents[idx] });
}

// POST /api/kill-switch/agents/:id/resume
function resumeAgent(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const agents = readAgents();
  const idx = agents.findIndex(a => a.id === id);
  if (idx < 0) return c.json({ error: "not found" }, 404);
  const now = new Date().toISOString();
  agents[idx].status = "active";
  agents[idx].updatedAt = now;
  writeAgents(agents);
  appendAudit({ id: crypto.randomUUID(), timestamp: now, agentId: id, action: "agent_resumed", actor: auth.founderId ?? "founder", details: `Agent resumed by founder` });
  return c.json({ ok: true, agent: agents[idx] });
}

// POST /api/kill-switch/agents/:id/terminate
function terminateAgent(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const agents = readAgents();
  const idx = agents.findIndex(a => a.id === id);
  if (idx < 0) return c.json({ error: "not found" }, 404);
  const now = new Date().toISOString();
  agents[idx].status = "terminated";
  agents[idx].updatedAt = now;
  writeAgents(agents);
  appendAudit({ id: crypto.randomUUID(), timestamp: now, agentId: id, action: "agent_terminated", actor: auth.founderId ?? "founder", details: `Agent terminated by founder` });
  return c.json({ ok: true });
}

// POST /api/kill-switch/agents/:id/spend  body: { cents: number }
function spend(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const body = await c.req.json();
  const cents = Math.round(Number(body.cents ?? 0));
  if (cents <= 0) return c.json({ error: "cents must be positive" }, 400);
  const result = canSpend(id, cents);
  return c.json({ allowed: result.allowed, reason: result.reason, hardStop: result.hardStop ?? false });
}

// GET /api/kill-switch/audit
function listAudit(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const entries = readAudit();
  // Verify chain integrity
  let valid = true;
  for (let i = 1; i < entries.length; i++) {
    if (entries[i].prevHash !== entries[i-1].hash) { valid = false; break; }
  }
  return c.json({ entries, verified: valid, total: entries.length });
}

// POST /api/kill-switch/approvals  body: { agentId, category, description }
function requestApproval(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const body = await c.req.json();
  const { agentId, category, description } = body;
  const VALID_CATEGORIES = ["external_communications", "publishing", "financial", "structural", "strategy"];
  if (!agentId || !category || !description) return c.json({ error: "agentId, category, description required" }, 400);
  if (!VALID_CATEGORIES.includes(category)) return c.json({ error: `category must be one of: ${VALID_CATEGORIES.join(", ")}` }, 400);

  const agents = readAgents();
  if (!agents.find(a => a.id === agentId)) return c.json({ error: "agent not found" }, 404);

  const approvals = readApprovals();
  const now = new Date().toISOString();
  const req: ApprovalRequest = {
    id: `apr_${Date.now()}_${Math.random().toString(36).slice(2, 7)}`,
    agentId,
    category,
    description,
    status: "pending",
    requestedAt: now,
  };
  approvals.push(req);
  writeApprovals(approvals);
  appendAudit({ id: crypto.randomUUID(), timestamp: now, agentId, action: "approval_requested", actor: auth.founderId ?? "founder", details: `Approval requested: [${category}] ${description}` });
  return c.json({ approval: req }, 201);
}

// GET /api/kill-switch/approvals
function listApprovals(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const approvals = readApprovals();
  return c.json({ approvals });
}

// POST /api/kill-switch/approvals/:id/grant
function grantApproval(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const approvals = readApprovals();
  const idx = approvals.findIndex(a => a.id === id);
  if (idx < 0) return c.json({ error: "not found" }, 404);
  const now = new Date().toISOString();
  approvals[idx].status = "granted";
  approvals[idx].resolvedAt = now;
  approvals[idx].resolver = auth.founderId ?? "founder";
  writeApprovals(approvals);
  appendAudit({ id: crypto.randomUUID(), timestamp: now, agentId: approvals[idx].agentId, action: "approval_granted", actor: auth.founderId ?? "founder", details: `Approval granted: [${approvals[idx].category}] ${approvals[idx].description}` });
  return c.json({ approval: approvals[idx] });
}

// POST /api/kill-switch/approvals/:id/deny
function denyApproval(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("id");
  const approvals = readApprovals();
  const idx = approvals.findIndex(a => a.id === id);
  if (idx < 0) return c.json({ error: "not found" }, 404);
  const now = new Date().toISOString();
  approvals[idx].status = "denied";
  approvals[idx].resolvedAt = now;
  approvals[idx].resolver = auth.founderId ?? "founder";
  writeApprovals(approvals);
  appendAudit({ id: crypto.randomUUID(), timestamp: now, agentId: approvals[idx].agentId, action: "approval_denied", actor: auth.founderId ?? "founder", details: `Approval denied: [${approvals[idx].category}] ${approvals[idx].description}` });
  return c.json({ approval: approvals[idx] });
}

// POST /api/kill-switch/override  body: { approvalId, note }
function override(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const body = await c.req.json();
  const { approvalId, note = "" } = body;
  const now = new Date().toISOString();
  appendAudit({ id: crypto.randomUUID(), timestamp: now, agentId: approvalId, action: "override", actor: auth.founderId ?? "founder", details: `Override by founder: ${note}` });
  return c.json({ ok: true });
}

// GET /api/kill-switch/budget/:agentId
function getBudget(c: Context) {
  const auth = requireAuth(c);
  if (!auth.authorized) return notAuthorized(c);
  const id = c.req.param("agentId");
  const agents = readAgents();
  const agent = agents.find(a => a.id === id);
  if (!agent) return c.json({ error: "not found" }, 404);
  const spent = getAgentSpend(id);
  const pct = Math.round((spent / agent.budgetCap) * 100);
  return c.json({ agentId: id, cap: agent.budgetCap, spent, pct, warningPct: agent.warningPct, status: agent.status });
}

export default {
  health,
  listAgents,
  createAgent,
  getAgent,
  updateAgent,
  pauseAgent,
  resumeAgent,
  terminateAgent,
  spend,
  listAudit,
  requestApproval,
  listApprovals,
  grantApproval,
  denyApproval,
  override,
  getBudget,
};
