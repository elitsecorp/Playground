import requests
from bs4 import BeautifulSoup

url = 'https://addisinsight.net/?s=ethio+telecom'
res = requests.get(url, headers={'User-Agent':'Mozilla/5.0'})
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('article h2 a')
for a in links:
    print(a['href'], a.get_text(strip=True))
