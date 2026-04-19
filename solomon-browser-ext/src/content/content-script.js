// Solomon Browser — Content Script
// Injected into every page. Handles: AI highlighting, smart interactions, memory capture.

(function() {
  'use strict';
  
  // Don't run twice
  if (window.__solomon__) return;
  window.__solomon__ = true;
  
  console.log('[Solomon] Content script loaded on', window.location.href);
  
  // Highlight mode — when user enables "AI highlights" in popup
  let highlightMode = false;
  let highlightedElements = [];
  
  // Listen for messages from background
  chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    switch (message.action) {
      case 'highlight.enable':
        highlightMode = true;
        sendResponse({ success: true });
        break;
      case 'highlight.disable':
        highlightMode = false;
        clearHighlights();
        sendResponse({ success: true });
        break;
      case 'page.getContent':
        sendResponse({ 
          success: true, 
          content: {
            title: document.title,
            url: window.location.href,
            text: document.body.innerText.slice(0, 3000),
            h1: document.querySelector('h1')?.textContent,
            links: Array.from(document.querySelectorAll('a[href]')).slice(0, 30).map(a => ({
              text: a.textContent.trim().slice(0, 80),
              href: a.href
            }))
          }
        });
        break;
      case 'hermes.ask':
        // Direct AI question about the page
        handleHermesQuery(message.payload).then(sendResponse);
        return true; // async
    }
  });
  
  // Handle AI queries about the page
  async function handleHermesQuery(payload) {
    const { question } = payload;
    
    // Extract relevant context from page
    const context = {
      title: document.title,
      url: window.location.href,
      heading: document.querySelector('h1')?.textContent || '',
      text: document.body.innerText.slice(0, 2000),
    };
    
    // Send to background for AI processing
    const response = await chrome.runtime.sendMessage({
      action: 'hermes.think',
      payload: { prompt: question, context }
    });
    
    return response;
  }
  
  // Clear existing highlights
  function clearHighlights() {
    highlightedElements.forEach(el => {
      el.style.outline = '';
      el.style.backgroundColor = '';
    });
    highlightedElements = [];
  }
  
  // Smart highlights — highlight interactive elements when highlight mode is on
  document.addEventListener('mouseover', (e) => {
    if (!highlightMode) return;
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON' || e.target.tagName === 'INPUT') {
      e.target.style.outline = '2px solid #6366f1';
      e.target.style.outlineOffset = '2px';
    }
  });
  
  document.addEventListener('mouseout', (e) => {
    if (!highlightMode) return;
    if (e.target.tagName === 'A' || e.target.tagName === 'BUTTON' || e.target.tagName === 'INPUT') {
      e.target.style.outline = '';
      e.target.style.outlineOffset = '';
    }
  });
  
  // Track user interactions for memory
  document.addEventListener('click', (e) => {
    const target = e.target;
    const data = {
      type: 'click',
      tag: target.tagName,
      text: target.textContent?.trim().slice(0, 50),
      href: target.href || target.closest('a')?.href,
      timestamp: Date.now(),
      url: window.location.href,
    };
    
    chrome.runtime.sendMessage({
      action: 'selfsync.push',
      payload: { type: 'interaction', data }
    });
  });
  
  // Keyboard shortcuts
  document.addEventListener('keydown', (e) => {
    // Alt+S: Ask Solomon about this page
    if (e.altKey && e.key === 's') {
      const question = prompt('Ask Solomon about this page:');
      if (question) {
        chrome.runtime.sendMessage({
          action: 'hermes.ask',
          payload: { question }
        });
      }
    }
    
    // Alt+H: Toggle highlight mode
    if (e.altKey && e.key === 'h') {
      highlightMode = !highlightMode;
      if (!highlightMode) clearHighlights();
      chrome.runtime.sendMessage({
        action: highlightMode ? 'highlight.enable' : 'highlight.disable'
      });
    }
  });
  
})();
