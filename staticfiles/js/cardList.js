function filterElements(search) {
    const query = search.toLowerCase().trim();
    const elementsList = document.querySelectorAll('#elements div');
    const notFound = document.getElementById('not-found');

    let anyVisible = false;

    elementsList.forEach(element => {
        const isMatch = element.id.toLowerCase().includes(query);
        element.style.display = isMatch ? 'flex' : 'none';
        if (isMatch) anyVisible = true;
    });

    notFound.style.display = anyVisible ? 'none' : 'flex';
}


function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
}

async function toggleFixed(event) {
    event.preventDefault();
    const btn = event.currentTarget;

    const res = await fetch(btn.dataset.url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({}), // corpo vazio mas envia algo
    });

    if (!res.ok) {
      console.error('Erro na requisição:', res.status);
      return;
    }

    const data = await res.json();

    const icon = btn.querySelector('i');
    if (data.fixed) {
        icon.className = 'bi bi-pin-angle-fill fs-5';
    } else {
        icon.className = 'bi bi-pin-angle fs-5';
    }
    organizeFixed();
}


function organizeFixed() {
    const fixedEl = document.getElementById('fixed-elements');
    const noteEl = document.getElementById('note-elements');
    const allCards = [...fixedEl.children, ...noteEl.children];

    allCards.forEach(card => {
        const isFixed = card.querySelector('i').classList.contains('bi-pin-angle-fill');
        const parent = isFixed ? fixedEl : noteEl;
        if (card.parentElement !== parent) parent.appendChild(card);
    });
}