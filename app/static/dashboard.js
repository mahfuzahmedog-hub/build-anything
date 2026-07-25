// Dashboard JS — CRUD for items

async function loadItems() {
    const res = await fetch('/api/items');
    const items = await res.json();
    const list = document.getElementById('items-list');
    list.innerHTML = items.map(item => `
        <li>
            <div>
                <div class="title">${escapeHtml(item.title)}</div>
                ${item.description ? `<div class="desc">${escapeHtml(item.description)}</div>` : ''}
            </div>
            <button class="del" data-id="${item.id}">✕</button>
        </li>
    `).join('');

    document.querySelectorAll('.del').forEach(btn => {
        btn.addEventListener('click', async () => {
            await fetch(`/api/items/${btn.dataset.id}`, { method: 'DELETE' });
            loadItems();
        });
    });
}

document.getElementById('item-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const title = document.getElementById('title').value.trim();
    const description = document.getElementById('description').value.trim();
    if (!title) return;
    await fetch('/api/items', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, description }),
    });
    document.getElementById('title').value = '';
    document.getElementById('description').value = '';
    loadItems();
});

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

loadItems();
