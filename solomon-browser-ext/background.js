// Solomon Browser — Background Service Worker
// Handles: Solomon Air dialer, JackConnect workers, Hermes memory, Solomon Bus

const SOLOMON_STATE = {
  herMES: null,
  solomonAir: null,
  jackConnect: null,
  bus: null
};

// Initialize Solomon OS connection
async function initSolomon() {
  console.log("[Solomon] Initializing browser layer...");

  // Connect to Solomon Bus
  try {
    const busResponse = await fetch("http://localhost:3001/api/bus/status");
    if (busResponse.ok) {
      SOLOMON_STATE.bus = await busResponse.json();
      console.log("[Solomon] Bus connected:", SOLOMON_STATE.bus);
    }
  } catch (e) {
    console.log("[Solomon] Solomon Bus not running — local mode");
  }

  // Load Hermes memory context
  try {
    const memResponse = await fetch("http://localhost:3001/api/memory/recent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ limit: 10 })
    });
    if (memResponse.ok) {
      const mem = await memResponse.json();
      SOLOMON_STATE.herMES = mem;
      console.log("[Solomon] Hermes memory loaded:", mem.length, "entries");
    }
  } catch (e) {
    console.log("[Solomon] Hermes memory: standalone mode");
  }
}

// Solomon Air — VoIP dialer
async function solomonDial(number) {
  const response = await fetch("http://localhost:3002/api/dial", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ number })
  });
  return response.json();
}

// Solomon Air — Send SMS
async function solomonSMS(number, message) {
  const response = await fetch("http://localhost:3002/api/sms", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ number, message })
  });
  return response.json();
}

// JackConnect — Get active workers
async function getWorkers() {
  const response = await fetch("http://localhost:3003/api/workers");
  if (response.ok) return response.json();
  return { workers: [] };
}

// JackConnect — Assign task to worker
async function assignTask(workerId, task) {
  const response = await fetch("http://localhost:3003/api/assign", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ workerId, task })
  });
  return response.json();
}

// Hermes — Store memory from browsing
async function herMESStore(key, value) {
  await fetch("http://localhost:3001/api/memory/store", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ key, value, source: "browser" })
  });
}

// Message handler
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "SOLOMON_DIAL") {
    solomonDial(msg.number).then(sendResponse);
    return true;
  }
  if (msg.type === "SOLOMON_SMS") {
    solomonSMS(msg.number, msg.message).then(sendResponse);
    return true;
  }
  if (msg.type === "GET_WORKERS") {
    getWorkers().then(sendResponse);
    return true;
  }
  if (msg.type === "ASSIGN_TASK") {
    assignTask(msg.workerId, msg.task).then(sendResponse);
    return true;
  }
  if (msg.type === "HERMES_STORE") {
    herMESStore(msg.key, msg.value).then(sendResponse);
    return true;
  }
  if (msg.type === "GET_STATE") {
    sendResponse(SOLOMON_STATE);
    return true;
  }
});

// Init on install
chrome.runtime.onInstalled.addListener(() => {
  console.log("[Solomon Browser] Installed — initializing...");
  initSolomon();
  chrome.sidePanel.setOptions({ path: "sidepanel.html" });
});

// Init on startup
initSolomon();
