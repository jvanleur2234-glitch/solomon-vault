// Solomon Browser — Side Panel Script

const chatArea = document.getElementById("chatArea");
const chatInput = document.getElementById("chatInput");
const sendBtn = document.getElementById("sendBtn");
const modelSelect = document.getElementById("modelSelect");
const tabMemContent = document.getElementById("tabMemContent");

let chatHistory = [];

// Send message
async function sendMessage() {
  const text = chatInput.value.trim();
  if (!text) return;

  // Add user message
  appendMessage("user", text);
  chatHistory.push({ role: "user", content: text });
  chatInput.value = "";

  // Show typing indicator
  const typingId = appendMessage("assistant", "Thinking...", true);

  try {
    // Get current tab context
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const pageUrl = tab.url;
    const pageTitle = tab.title;

    // Get page content via content script
    let pageContent = { text: "", links: [], phones: [], emails: [], prices: [] };
    try {
      pageContent = await chrome.tabs.sendMessage(tab.id, { type: "GET_PAGE_CONTENT" });
    } catch (e) {
      // Content script may not be loaded on chrome:// pages
    }

    // Build prompt with page context
    const prompt = `User is browsing: ${pageTitle} (${pageUrl})

${pageContent && pageContent.text ? `Page content:\n${pageContent.text.slice(0, 3000)}` : '(No page content available)'}

${pageContent && pageContent.phones && pageContent.phones.length ? `Phones found: ${pageContent.phones.join(", ")}` : ''}
${pageContent && pageContent.emails && pageContent.emails.length ? `Emails found: ${pageContent.emails.join(", ")}` : ''}
${pageContent && pageContent.prices && pageContent.prices.length ? `Prices found: ${pageContent.prices.join(", ")}` : ''}

User question: ${text}

Answer as Solomon AI. Be helpful, concise, and actionable.`;

    // Get Zo token
    const token = await getZoToken();

    // Call Zo API
    const response = await fetch("https://api.zo.computer/zo/ask", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        input: prompt,
        model_name: "vercel:minimax/minimax-m2.7"
      })
    });

    const data = await response.json();
    const answer = data.output || "Solomon is thinking... try again.";

    removeMessage(typingId);
    appendMessage("assistant", answer);
    chatHistory.push({ role: "assistant", content: answer });

    // Store in Hermes memory
    await chrome.runtime.sendMessage({
      type: "HERMES_STORE",
      key: `chat:${Date.now()}`,
      value: { question: text, answer, url: pageUrl }
    });

  } catch (e) {
    removeMessage(typingId);
    appendMessage("assistant", "Error: " + e.message);
  }
}

// Append message to chat
function appendMessage(role, content, isTyping = false) {
  const id = "msg-" + Date.now();
  const div = document.createElement("div");
  div.className = `message ${role}${isTyping ? " typing" : ""}`;
  div.id = id;
  div.innerHTML = `<div class="msg-content">${escapeHtml(content)}</div>`;
  chatArea.appendChild(div);
  chatArea.scrollTop = chatArea.scrollHeight;
  return id;
}

function removeMessage(id) {
  const el = document.getElementById(id);
  if (el) el.remove();
}

function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}

// Auto-resize textarea
chatInput.addEventListener("input", () => {
  chatInput.style.height = "auto";
  chatInput.style.height = Math.min(chatInput.scrollHeight, 150) + "px";
});

// Enter to send
chatInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

sendBtn.addEventListener("click", sendMessage);

// Page analysis
document.getElementById("analyzeBtn").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  try {
    const content = await chrome.tabs.sendMessage(tab.id, { type: "GET_PAGE_CONTENT" });
    if (content && content.text) {
      chatInput.value = `Analyze this page: what is it about, who is it for, and what are the main actions I can take?`;
      sendMessage();
    }
  } catch (e) {
    appendMessage("assistant", "Cannot analyze this page (chrome:// pages are restricted).");
  }
});

document.getElementById("summarizeBtn").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  try {
    const content = await chrome.tabs.sendMessage(tab.id, { type: "GET_PAGE_CONTENT" });
    if (content && content.text) {
      chatInput.value = `Summarize this page in 3 bullet points.`;
      sendMessage();
    }
  } catch (e) {
    appendMessage("assistant", "Cannot summarize this page.");
  }
});

document.getElementById("extractBtn").addEventListener("click", async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  try {
    const content = await chrome.tabs.sendMessage(tab.id, { type: "GET_PAGE_CONTENT" });
    if (content && content.text) {
      chatInput.value = `Extract all structured data from this page (emails, phones, prices, dates). Format as a list.`;
      sendMessage();
    }
  } catch (e) {
    appendMessage("assistant", "Cannot extract from this page.");
  }
});

// Helper functions
async function getZoToken() {
  return localStorage.getItem("solomon_token") || "";
}

// Load page memory on startup
async function loadPageMemory() {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (tab && tab.url) {
    tabMemContent.textContent = tab.title || tab.url;
  }
}

loadPageMemory();
