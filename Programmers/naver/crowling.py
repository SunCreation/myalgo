import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0'}
timeout = 5

url = 'https://antilibrary.org/2705'

soup = BeautifulSoup(requests.post(url).text, "html.parser")
# print(soup.text)
with open('hi.txt', 'w') as f:
    for i in soup.text.split('\n'):
        if i=='':
            continue
        f.write(i+'\n')
