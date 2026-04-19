// Solomon Browser — Content Script
// Runs on every page to enable AI interaction with page content

// Listen for messages from background/popup
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.type === "GET_PAGE_CONTENT") {
    const content = extractPageContent();
    sendResponse(content);
  }
  if (msg.type === "HIGHLIGHT_ELEMENT") {
    highlightElement(msg.selector);
    sendResponse({ success: true });
  }
  if (msg.type === "CLICK_ELEMENT") {
    clickElement(msg.selector);
    sendResponse({ success: true });
  }
});

// Extract readable text content from page
function extractPageContent() {
  const result = {
    title: document.title,
    url: window.location.href,
    text: "",
    links: [],
    images: [],
    phones: [],
    emails: [],
    prices: []
  };

  // Main text content
  const main = document.querySelector("main, article, [role='main'], .content, #content") 
    || document.body;
  result.text = main.innerText?.slice(0, 10000) || "";

  // Links
  document.querySelectorAll("a[href]").forEach(a => {
    const text = a.innerText?.trim();
    const href = a.href;
    if (text && href) result.links.push({ text, href });
  });

  // Images
  document.querySelectorAll("img").forEach(img => {
    const alt = img.alt || "";
    const src = img.src || "";
    if (src) result.images.push({ alt, src });
  });

  // Phone numbers (US format)
  const phoneRegex = /(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/g;
  const phoneMatches = document.body.innerText.match(phoneRegex) || [];
  result.phones = [...new Set(phoneMatches)];

  // Emails
  const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
  const emailMatches = document.body.innerText.match(emailRegex) || [];
  result.emails = [...new Set(emailMatches)];

  // Prices
  const priceRegex = /\$\d+(?:,\d{3})*(?:\.\d{2})?/g;
  const priceMatches = document.body.innerText.match(priceRegex) || [];
  result.prices = [...new Set(priceMatches)];

  return result;
}

// Highlight an element on page
function highlightElement(selector) {
  try {
    const el = document.querySelector(selector);
    if (el) {
      el.style.outline = "3px solid #6366f1";
      el.scrollIntoView({ behavior: "smooth", block: "center" });
      setTimeout(() => el.style.outline = "", 3000);
    }
  } catch (e) {}
}

// Click an element programmatically
function clickElement(selector) {
  try {
    const el = document.querySelector(selector);
    if (el) el.click();
  } catch (e) {}
}

// Auto-read page for Hermes memory
async function autoStorePage() {
  const content = extractPageContent();
  if (content.text.length > 100) {
    chrome.runtime.sendMessage({
      type: "HERMES_STORE",
      key: `page:${Date.now()}`,
      value: {
        url: content.url,
        title: content.title,
        phones: content.phones,
        emails: content.emails,
        prices: content.prices
      }
    });
  }
}

// Run on pages that look important (not chrome://, etc.)
if (!window.location.protocol.startsWith("chrome")) {
  // Debounced auto-store (once per page load)
  let stored = false;
  const observer = new MutationObserver(() => {
    if (!stored && document.readyState === "complete") {
      setTimeout(() => {
        autoStorePage();
        stored = true;
      }, 2000);
    }
  });
  observer.observe(document.body, { childList: true, subtree: true });
}
