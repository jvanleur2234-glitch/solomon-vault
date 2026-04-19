// Solomon Browser — Popup Logic

document.addEventListener('DOMContentLoaded', () => {
  const askInput = document.getElementById('ask-input');
  const askBtn = document.getElementById('ask-btn');
  const responseArea = document.getElementById('response-area');
  const responseContent = document.getElementById('response-content');
  const modeSelect = document.getElementById('mode-select');
  
  // Mode tracking
  let currentMode = 'balanced';
  
  modeSelect.addEventListener('change', (e) => {
    currentMode = e.target.value;
  });
  
  // Ask button
  askBtn.addEventListener('click', handleAsk);
  
  async function handleAsk() {
    const question = askInput.value.trim();
    if (!question) return;
    
    // Show loading
    askBtn.disabled = true;
    askBtn.textContent = 'Thinking...';
    responseArea.classList.remove('hidden');
    responseContent.innerHTML = '<div class="loading">🧠 Solomon is thinking...</div>';
    
    try {
      // Get current tab
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      
      // Get page context
      const pageData = await chrome.tabs.sendMessage(tab.id, { action: 'page.getContent' });
      
      // Send to background AI
      const response = await chrome.runtime.sendMessage({
        action: 'hermes.think',
        payload: {
          prompt: question,
          context: {
            page: pageData.content || {},
            mode: currentMode,
          }
        }
      });
      
      if (response.success) {
        responseContent.innerHTML = formatResponse(response.result);
      } else {
        responseContent.innerHTML = `<div class="error">Error: ${response.error}</div>`;
      }
    } catch (e) {
      responseContent.innerHTML = `<div class="error">Error: ${e.message}</div>`;
    } finally {
      askBtn.disabled = false;
      askBtn.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2a10 10 0 1 0 10 10H12V2z"/></svg> Ask`;
    }
  }
  
  function formatResponse(text) {
    // Simple markdown-like formatting
    return text
      .replace(/\n\n/g, '</p><p>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/`(.*?)`/g, '<code>$1</code>')
      .replace(/^/, '<p>')
      .replace(/$/, '</p>');
  }
  
  // Tool buttons
  document.getElementById('btn-highlight').addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    await chrome.tabs.sendMessage(tab.id, { action: 'highlight.toggle' });
  });
  
  document.getElementById('btn-summarize').addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const pageData = await chrome.tabs.sendMessage(tab.id, { action: 'page.getContent' });
    
    responseArea.classList.remove('hidden');
    responseContent.innerHTML = '<div class="loading">📄 Summarizing...</div>';
    
    const response = await chrome.runtime.sendMessage({
      action: 'hermes.think',
      payload: {
        prompt: `Summarize this page in 3-5 bullet points. Focus on the main topics and key information.`,
        context: { page: pageData.content, mode: 'fast' }
      }
    });
    
    if (response.success) {
      responseContent.innerHTML = `<div class="summary"><h3>📄 Summary</h3>${formatResponse(response.result)}</div>`;
    }
  });
  
  document.getElementById('btn-memory').addEventListener('click', async () => {
    const memory = await chrome.runtime.sendMessage({
      action: 'hermes.remember',
      payload: { query: '', limit: 20 }
    });
    
    responseArea.classList.remove('hidden');
    if (memory.success && memory.result.length > 0) {
      const items = memory.result.map(m => `<div class="memory-item">${m.content || m.text || JSON.stringify(m).slice(0, 100)}</div>`).join('');
      responseContent.innerHTML = `<div class="memory-list"><h3>🧠 Recent Memory</h3>${items}</div>`;
    } else {
      responseContent.innerHTML = '<div class="empty">No memory yet. Start browsing and Solomon will remember.</div>';
    }
  });
  
  document.getElementById('btn-sync').addEventListener('click', async () => {
    const result = await chrome.runtime.sendMessage({ action: 'selfsync.push', payload: { type: 'manual_sync', timestamp: Date.now() } });
    responseArea.classList.remove('hidden');
    responseContent.innerHTML = result.success 
      ? '<div class="success">✅ Synced to selfsync server</div>'
      : '<div class="error">❌ Sync failed</div>';
  });
  
  document.getElementById('btn-extract').addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const pageData = await chrome.tabs.sendMessage(tab.id, { action: 'page.getContent' });
    
    responseArea.classList.remove('hidden');
    responseContent.innerHTML = '<div class="loading">🔍 Extracting...</div>';
    
    const response = await chrome.runtime.sendMessage({
      action: 'hermes.think',
      payload: {
        prompt: `Extract all key information from this page: main topics, entities (people, companies, products), dates, numbers, and action items. Format as a structured list.`,
        context: { page: pageData.content, mode: 'balanced' }
      }
    });
    
    if (response.success) {
      responseContent.innerHTML = `<div class="extracted"><h3>🔍 Extracted Info</h3>${formatResponse(response.result)}</div>`;
    }
  });
  
  document.getElementById('btn-remember').addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const pageData = await chrome.tabs.sendMessage(tab.id, { action: 'page.getContent' });
    
    await chrome.runtime.sendMessage({
      action: 'hermes.learn',
      payload: {
        content: `Visited: ${pageData.content?.title} — ${pageData.content?.url}`,
        metadata: { url: pageData.content?.url, title: pageData.content?.title, timestamp: Date.now() }
      }
    });
    
    responseArea.classList.remove('hidden');
    responseContent.innerHTML = '<div class="success">✅ Saved to memory</div>';
  });
  
  document.getElementById('open-options').addEventListener('click', (e) => {
    e.preventDefault();
    chrome.runtime.openOptionsPage();
  });
});
