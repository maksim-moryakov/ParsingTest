import requests
from bs4 import BeautifulSoup

url = 'https://ya.ru/'

headers = {
    'Accept': '*/*',
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.5.708 Yowser/2.5 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text
print(src)