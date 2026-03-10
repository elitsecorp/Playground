const app = document.getElementById('app');
const industrySelect = document.getElementById('industryFilter');
const scoreInput = document.getElementById('scoreFilter');
const sortSelect = document.getElementById('sortSelect');
const searchInput = document.getElementById('searchInput');
let banksData = [];

function formatCurrency(value) {
  return value && !Number.isNaN(value)
    ? `${value.toLocaleString('en-ET', { minimumFractionDigits: 2, maximumFractionDigits: 2 })} ETB`
    : 'n/a';
}

function renderBank(bank) {
  const card = document.createElement('article');
  card.className = 'card';
  card.innerHTML = `
    <div>
      <div class="pill">${bank.rating || 'Unscored'} • Score ${bank.total_score || 0}</div>
      <h2>${bank.name}</h2>
      <p>${bank.industry} | ${bank.ownership_type} | ${bank.status}</p>
    </div>
    <p class="muted">${bank.industry_analysis || bank.financial_analysis || 'No summary yet.'}</p>
    <ul>
      <li>Price: ${formatCurrency(bank.current_price)}</li>
      <li>Implied P/E: ${bank.implied_pe ? bank.implied_pe.toFixed(2) : 'n/a'}</li>
      <li>20% target: ${formatCurrency(bank.target_price_for_20pc)}</li>
      <li>Contact: ${bank.contact_phone || 'TBD'} • ${bank.contact_email || 'TBD'}</li>
    </ul>
    <p><strong>Investor notes:</strong> ${bank.investor_notes || 'Use your ESX broker to place an order once the price hits target.'}</p>
  `;
  return card;
}

function applyFilters() {
  const industry = industrySelect.value;
  const minScore = Number(scoreInput.value) || 0;
  const search = searchInput.value.toLowerCase();
  let filtered = banksData.filter(bank => {
    if (industry && bank.industry !== industry) return false;
    if ((bank.total_score || 0) < minScore) return false;
    if (search) {
      const haystack = `${bank.name} ${bank.investor_notes} ${bank.contact_email}`.toLowerCase();
      if (!haystack.includes(search)) return false;
    }
    return true;
  });

  const sortKey = sortSelect.value;
  filtered.sort((a, b) => {
    if (sortKey === 'score') return (b.total_score || 0) - (a.total_score || 0);
    if (sortKey === 'price') return (b.current_price || 0) - (a.current_price || 0);
    if (sortKey === 'pe') return (a.implied_pe || Infinity) - (b.implied_pe || Infinity);
    if (sortKey === 'target') return (b.target_price_for_20pc || 0) - (a.target_price_for_20pc || 0);
    return 0;
  });

  app.innerHTML = '';
  if (!filtered.length) {
    app.innerHTML = '<p class="card">No results match these filters.</p>';
    return;
  }
  filtered.forEach(bank => app.appendChild(renderBank(bank)));
}

function populateIndustryOptions(banks) {
  const industries = [...new Set(banks.map(bank => bank.industry))].sort();
  industries.forEach(industry => {
    const option = document.createElement('option');
    option.value = industry;
    option.textContent = industry;
    industrySelect.appendChild(option);
  });
}

async function load() {
  const response = await fetch('data/banks.json');
  banksData = await response.json();
  populateIndustryOptions(banksData);
  applyFilters();
}

[industrySelect, scoreInput, sortSelect, searchInput].forEach(control => {
  control.addEventListener('input', applyFilters);
});

load().catch(() => {
  app.innerHTML = '<p class="card">Unable to load bank data. Run export_data.py before deploying.</p>';
});
