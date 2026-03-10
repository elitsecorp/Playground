import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_banks_in_Ethiopia'
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')
table = soup.find('table', {'class':'wikitable'})
rows = table.select('tr')
for row in rows[1:]:
    cells = row.select('td')
    if not cells:
        continue
    name = cells[1].get_text(strip=True)
    if 'Dashen' in name:
        print('HTML:', cells[-1])
        print('text with footnote:', cells[-1].get_text(strip=True))
        break
