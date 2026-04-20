// Solomon Browser — Popup Script

const dialBtn = document.getElementById("dialBtn");
const smsBtn = document.getElementById("smsBtn");
const assignBtn = document.getElementById("assignBtn");
const storeBtn = document.getElementById("storeBtn");
const statusDot = document.getElementById("statusDot");
const callStatus = document.getElementById("callStatus");
const workerList = document.getElementById("workerList");
const recentMem = document.getElementById("recentMem");

// Dial a number
dialBtn.addEventListener("click", async () => {
  const number = document.getElementById("dialNumber").value.trim();
  if (!number) return;
  callStatus.textContent = "⟆ Dialing " + number + "...";
  const res = await chrome.runtime.sendMessage({ type: "SOLOMON_DIAL", number });
  callStatus.textContent = res.success ? "✓ Connected" : "✗ Failed";
});

// Send SMS
smsBtn.addEventListener("click", async () => {
  const number = document.getElementById("smsNumber").value.trim();
  const message = document.getElementById("smsMessage").value.trim();
  if (!number || !message) return;
  const res = await chrome.runtime.sendMessage({ type: "SOLOMON_SMS", number, message });
  callStatus.textContent = res.success ? "✓ Sent" : "✗ Failed";
});

// Load workers
async function loadWorkers() {
  const res = await chrome.runtime.sendMessage({ type: "GET_WORKERS" });
  if (!res.workers || res.workers.length === 0) {
    workerList.innerHTML = '<div class="empty">No workers active</div>';
    return;
  }
  workerList.innerHTML = res.workers.map(w => `
    <div class="worker-item">
      <span class="worker-name">${w.name}</span>
      <span class="worker-status ${w.status}">${w.status}</span>
    </div>
  `).join("");
}

// Assign task
assignBtn.addEventListener("click", async () => {
  const task = document.getElementById("taskInput").value.trim();
  if (!task) return;
  const res = await chrome.runtime.sendMessage({ type: "ASSIGN_TASK", task });
  callStatus.textContent = res.success ? "✓ Task assigned" : "✗ Failed";
  document.getElementById("taskInput").value = "";
});

// Store memory
storeBtn.addEventListener("click", async () => {
  const key = document.getElementById("memKey").value.trim();
  const value = document.getElementById("memValue").value.trim();
  if (!key || !value) return;
  await chrome.runtime.sendMessage({ type: "HERMES_STORE", key, value });
  document.getElementById("memKey").value = "";
  document.getElementById("memValue").value = "";
  loadRecentMem();
});

// Load recent memory
async function loadRecentMem() {
  const res = await chrome.runtime.sendMessage({ type: "GET_STATE" });
  if (res.herMES && res.herMES.length > 0) {
    recentMem.innerHTML = res.herMES.slice(0, 3).map(m => `
      <div class="mem-item">
        <span class="mem-key">${m.key}</span>
        <span class="mem-val">${m.value}</span>
      </div>
    `).join("");
  }
}

// Quick actions
document.getElementById("openSidepanel").addEventListener("click", () => {
  chrome.sidePanel.open({ path: "sidepanel.html" });
});
document.getElementById("openDashboard").addEventListener("click", () => {
  window.open("https://josephv.zo.computer", "_blank");
});
document.getElementById("syncMemory").addEventListener("click", async () => {
  const res = await chrome.runtime.sendMessage({ type: "HERMES_SYNC" });
  callStatus.textContent = res.success ? "✓ Synced" : "✗ Failed";
});

// Update status dot
async function checkStatus() {
  const res = await chrome.runtime.sendMessage({ type: "GET_STATE" });
  statusDot.className = res.bus ? "status-dot online" : "status-dot offline";
}

// Init
checkStatus();
loadWorkers();
loadRecentMem();
