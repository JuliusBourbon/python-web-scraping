# Scraping data dengan Spoofing Header

# Import
import requests
from bs4 import BeautifulSoup
import csv

# Untuk mendapatkan User-Agent dan Accept bisa dilihat dari inspect->Network(All)->Headers(User-Agent dan Accept)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
}
response = requests.get('https://www.scrapethissite.com/pages/advanced/?gotcha=headers', headers=headers)

if response.status_code == 200:
    print('Request was Successful!')
else:
    print('Request failed with status code: ', response.status_code)

print(response.text)