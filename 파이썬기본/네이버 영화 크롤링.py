import requests
import json
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)  # headers were missing in your GET request
soup = BeautifulSoup(response.text, 'html5lib')
# print(soup)

result = soup.select('table.tbl_home')
print(result)