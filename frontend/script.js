const app = document.getElementById('app');

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
    <p><strong>Investor notes:</strong> ${bank.investor_notes || 'Use your ESX broker to place an order once the price is right.'}</p>
  `;
  return card;
}

async function load() {
  const response = await fetch('data/banks.json');
  const banks = await response.json();
  app.innerHTML = '';
  banks.forEach(bank => app.appendChild(renderBank(bank)));
}

load().catch(() => {
  app.innerHTML = '<p class="card">Unable to load bank data. Run export_data.py before deploying.</p>';
});
