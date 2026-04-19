// Solomon Browser — Background Service Worker
// Handles: cross-tab memory, AI orchestration, selfsync, message routing

import { HermesClient } from '../ai/hermes-client.js';
import { MemoryBridge } from '../ai/memory-bridge.js';
import { SelfSync } from '../ai/selfsync.js';
import { createContextMenu } from '../utils/context-menu.js';

// State
let hermes = null;
let memory = null;
let selfsync = null;

// Initialize
chrome.runtime.onInstalled.addListener(async (details) => {
  console.log('[Solomon] Installing...');
  
  // Create context menus
  createContextMenu();
  
  // Initialize AI layer
  hermes = new HermesClient();
  memory = new MemoryBridge();
  selfsync = new SelfSync();
  
  // Open onboarding page on first install
  if (details.reason === 'install') {
    chrome.tabs.create({ url: 'src/popup/onboarding.html' });
  }
  
  console.log('[Solomon] Ready');
});

// Message routing — content scripts ↔ AI layer
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  handleMessage(message, sender).then(sendResponse);
  return true; // async response
});

async function handleMessage(message, sender) {
  const { action, payload, tabId } = message;
  
  switch (action) {
    case 'hermes.think':
      // Deep reasoning request
      const thought = await hermes.think(payload.prompt, payload.context);
      return { success: true, result: thought };
    
    case 'hermes.remember':
      // Memory retrieval
      const memory = await memory.retrieve(payload.query, payload.limit);
      return { success: true, result: memory };
    
    case 'hermes.learn':
      // Store new memory
      await memory.store(payload.content, payload.metadata);
      return { success: true };
    
    case 'selfsync.push':
      // Push to selfsync server
      await selfsync.push(payload);
      return { success: true };
    
    case 'selfsync.pull':
      const data = await selfsync.pull();
      return { success: true, result: data };
    
    case 'page.analyze':
      // Analyze current page (content, links, structure)
      return await analyzePage(sender.tab);
    
    case 'tab.snapshot':
      // Full tab state snapshot for memory
      return await snapshotTab(sender.tab);
    
    default:
      return { success: false, error: 'Unknown action' };
  }
}

async function analyzePage(tab) {
  // Get page content via scripting
  try {
    const results = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => {
        return {
          title: document.title,
          url: window.location.href,
          h1: document.querySelector('h1')?.textContent || '',
          meta: {
            description: document.querySelector('meta[name="description"]')?.content || '',
            ogTitle: document.querySelector('meta[property="og:title"]')?.content || '',
          },
          links: Array.from(document.querySelectorAll('a[href]')).slice(0, 20).map(a => ({
            text: a.textContent.trim().slice(0, 100),
            href: a.href
          })),
          text: document.body.innerText.slice(0, 2000),
        };
      }
    });
    return { success: true, result: results[0].result };
  } catch (e) {
    return { success: false, error: e.message };
  }
}

async function snapshotTab(tab) {
  return {
    tabId: tab.id,
    url: tab.url,
    title: tab.title,
    active: tab.active,
    timestamp: Date.now(),
  };
}

// Tab events — update memory on navigation
chrome.webNavigation.onCompleted.addListener(async (details) => {
  if (details.frameId === 0) {
    // Main frame, store page visit in memory
    chrome.storage.local.get(['solomon_memory'], (data) => {
      const memory = data.solomon_memory || [];
      memory.push({
        type: 'page_visit',
        url: details.url,
        timestamp: Date.now(),
      });
      // Keep last 100 visits
      if (memory.length > 100) memory.shift();
      chrome.storage.local.set({ solomon_memory: memory });
    });
  }
});
