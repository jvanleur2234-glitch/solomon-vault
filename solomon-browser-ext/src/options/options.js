// Solomon Browser — Options Page

document.addEventListener('DOMContentLoaded', () => {
  const saveBtn = document.getElementById('save-btn');
  const clearBtn = document.getElementById('clear-btn');
  const statusEl = document.getElementById('save-status');

  // Load saved settings
  loadSettings();

  // Save settings
  saveBtn.addEventListener('click', async () => {
    const settings = {
      aiModel: document.getElementById('ai-model').value,
      localModel: document.getElementById('local-model').value,
      defaultMode: document.getElementById('default-mode').value,
      selfsyncUrl: document.getElementById('selfsync-url').value,
      selfsyncKey: document.getElementById('selfsync-key').value,
      maxMemory: parseInt(document.getElementById('max-memory').value) || 500,
      autoRemember: document.getElementById('auto-remember').checked,
      trackInteractions: document.getElementById('track-interactions').checked,
    };

    await chrome.storage.sync.set(settings);
    
    statusEl.textContent = 'Saved!';
    statusEl.className = 'status saved';
    setTimeout(() => {
      statusEl.textContent = '';
      statusEl.className = 'status';
    }, 2000);
  });

  // Clear all data
  clearBtn.addEventListener('click', async () => {
    if (!confirm('Are you sure? This will delete ALL Solomon data including memory, bookmarks, and settings. This cannot be undone.')) {
      return;
    }

    await chrome.storage.sync.clear();
    await chrome.storage.local.clear();
    
    // Reset form
    document.querySelectorAll('input[type="text"], input[type="password"], input[type="number"]').forEach(el => el.value = '');
    document.querySelectorAll('input[type="checkbox"]').forEach(el => el.checked = false);
    document.getElementById('ai-model').value = 'cloud';
    document.getElementById('default-mode').value = 'balanced';
    document.getElementById('max-memory').value = '500';
    
    statusEl.textContent = 'Cleared!';
    statusEl.className = 'status saved';
    setTimeout(() => {
      statusEl.textContent = '';
      statusEl.className = 'status';
    }, 2000);
  });
});

async function loadSettings() {
  const data = await chrome.storage.sync.get({
    aiModel: 'cloud',
    localModel: 'llama3.2',
    defaultMode: 'balanced',
    selfsyncUrl: '',
    selfsyncKey: '',
    maxMemory: 500,
    autoRemember: true,
    trackInteractions: true,
  });

  document.getElementById('ai-model').value = data.aiModel;
  document.getElementById('local-model').value = data.localModel;
  document.getElementById('default-mode').value = data.defaultMode;
  document.getElementById('selfsync-url').value = data.selfsyncUrl;
  document.getElementById('selfsync-key').value = data.selfsyncKey;
  document.getElementById('max-memory').value = data.maxMemory;
  document.getElementById('auto-remember').checked = data.autoRemember;
  document.getElementById('track-interactions').checked = data.trackInteractions;
}
