// Context Menu — Solomon Browser right-click menu

export function createContextMenu() {
  chrome.contextMenus.removeAll(() => {
    // Main menu
    chrome.contextMenus.create({
      id: 'solomon-root',
      title: 'Solomon Browser',
      contexts: ['all']
    });

    // Ask about this page
    chrome.contextMenus.create({
      id: 'solomon-ask-page',
      parentId: 'solomon-root',
      title: 'Ask Solomon about this page',
      contexts: ['page']
    });

    // Remember this page
    chrome.contextMenus.create({
      id: 'solomon-remember',
      parentId: 'solomon-root',
      title: 'Remember this page',
      contexts: ['page']
    });

    // Highlight elements
    chrome.contextMenus.create({
      id: 'solomon-highlight',
      parentId: 'solomon-root',
      title: 'Toggle highlight mode',
      contexts: ['page']
    });

    // Extract info
    chrome.contextMenus.create({
      id: 'solomon-extract',
      parentId: 'solomon-root',
      title: 'Extract key info from page',
      contexts: ['page']
    });

    // Separator
    chrome.contextMenus.create({
      id: 'solomon-sep1',
      parentId: 'solomon-root',
      type: 'separator',
      contexts: ['page']
    });

    // Search selected text with Solomon
    chrome.contextMenus.create({
      id: 'solomon-search-selection',
      parentId: 'solomon-root',
      title: 'Search with Solomon',
      contexts: ['selection']
    });

    // Link actions
    chrome.contextMenus.create({
      id: 'solomon-link-sep',
      parentId: 'solomon-root',
      type: 'separator',
      contexts: ['link']
    });

    chrome.contextMenus.create({
      id: 'solomon-save-link',
      parentId: 'solomon-root',
      title: 'Save link to memory',
      contexts: ['link']
    });
  });

  // Handle clicks
  chrome.contextMenus.onClicked.addListener((info, tab) => {
    handleContextClick(info, tab);
  });
}

async function handleContextClick(info, tab) {
  switch (info.menuItemId) {
    case 'solomon-ask-page':
      // Get page content and ask
      const pageData = await chrome.tabs.sendMessage(tab.id, { action: 'page.getContent' });
      // Opens a prompt in content script
      chrome.tabs.sendMessage(tab.id, { action: 'hermes.ask', payload: { question: 'What is this page about?' } });
      break;

    case 'solomon-remember':
      const memData = await chrome.tabs.sendMessage(tab.id, { action: 'page.getContent' });
      await chrome.runtime.sendMessage({
        action: 'hermes.learn',
        payload: {
          content: `Visited: ${memData.content?.title} — ${memData.content?.url}`,
          metadata: { url: memData.content?.url, title: memData.content?.title, timestamp: Date.now() }
        }
      });
      break;

    case 'solomon-highlight':
      chrome.tabs.sendMessage(tab.id, { action: 'highlight.toggle' });
      break;

    case 'solomon-extract':
      chrome.tabs.sendMessage(tab.id, { action: 'page.extract' });
      break;

    case 'solomon-search-selection':
      const selection = info.selectionText;
      chrome.tabs.sendMessage(tab.id, { action: 'hermes.ask', payload: { question: `What does this mean: "${selection}"` } });
      break;

    case 'solomon-save-link':
      await chrome.runtime.sendMessage({
        action: 'hermes.learn',
        payload: {
          content: `Saved link: ${info.linkUrl}`,
          metadata: { type: 'bookmark', url: info.linkUrl, timestamp: Date.now() }
        }
      });
      break;
  }
}
