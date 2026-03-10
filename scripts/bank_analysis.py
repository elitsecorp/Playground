import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_banks_in_Ethiopia'
res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find('table', {'class':'wikitable'})
rows = table.select('tr')[1:]

price_map = {
    'wegagen bank': 1000,
    'gadaa bank sc': 1000,
    'ethio telecom share company': 300,
    'ethio telecom': 300,
}

def clean(text):
    text = text.split('[')[0]
    text = text.replace('\u00a0', ' ')
    return text.strip()

def parse_num(text):
    if not text:
        return None
    text = clean(text)
    text = text.replace(',', '')
    if not text:
        return None
    if text.startswith('(') and text.endswith(')'):
        return -parse_num(text[1:-1])
    try:
        return float(text)
    except ValueError:
        return None

bank_data = {}
for row in rows:
    cells = row.select('td')
    if not cells or len(cells) < 8:
        continue
    name = clean(cells[1].get_text(strip=True))
    equity = parse_num(cells[-2].get_text(strip=True))
    profit = parse_num(cells[-1].get_text(strip=True))
    if '\n' in name:
        name = name.splitlines()[0]
    bank_data[name] = {
        'equity_m': equity,
        'profit_m': profit,
    }

for name, vals in bank_data.items():
    equity = vals['equity_m']
    profit = vals['profit_m']
    price = price_map.get(name.lower(), 1000)
    pe = None
    eps = None
    if equity and profit and equity != 0:
        eps = profit * 1000 / equity
        if eps != 0:
            pe = round(price / eps, 2)
    print(name, equity, profit, price, pe, eps)
