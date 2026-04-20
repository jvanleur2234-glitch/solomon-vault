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
  return true; // keep channel open for async response
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

  // Skip chrome:// and other restricted pages
  if (window.location.protocol.startsWith("chrome")) {
    return result;
  }

  // Main text content — try common content containers
  const main = document.querySelector("main, article, [role='main'], .content, #content, .main, [role='article']") 
    || document.body;
  result.text = main.innerText?.replace(/\s+/g, " ").trim().slice(0, 10000) || "";

  // Links
  document.querySelectorAll("a[href]").forEach(a => {
    const text = a.innerText?.trim();
    const href = a.href;
    if (text && href && !href.startsWith("javascript:")) {
      result.links.push({ text: text.slice(0, 100), href });
    }
  });

  // Images with alt text
  document.querySelectorAll("img").forEach(img => {
    const alt = img.alt || "";
    const src = img.src || "";
    if (src) result.images.push({ alt: alt.slice(0, 100), src });
  });

  // Phone numbers (US and international format)
  const phoneRegex = /(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/g;
  const phoneMatches = document.body.innerText.match(phoneRegex) || [];
  result.phones = [...new Set(phoneMatches)];

  // Emails
  const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/g;
  const emailMatches = document.body.innerText.match(emailRegex) || [];
  result.emails = [...new Set(emailMatches)];

  // Prices (USD and common formats)
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
      el.style.outlineOffset = "2px";
      el.scrollIntoView({ behavior: "smooth", block: "center" });
      setTimeout(() => {
        el.style.outline = "";
        el.style.outlineOffset = "";
      }, 3000);
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

// Auto-read page for Hermes memory (debounced)
let autoStoreTimer = null;
if (!window.location.protocol.startsWith("chrome")) {
  const observer = new MutationObserver(() => {
    if (autoStoreTimer) clearTimeout(autoStoreTimer);
    autoStoreTimer = setTimeout(() => {
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
            prices: content.prices,
            timestamp: new Date().toISOString()
          }
        });
      }
    }, 2000);
  });
  
  if (document.body) {
    observer.observe(document.body, { childList: true, subtree: true });
  }
}
