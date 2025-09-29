from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

for a in soup.find_all('a'):
    if a.get('href') and a['href'].startswith('20'):
        a['href'] = 'docs/' + a['href']

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
