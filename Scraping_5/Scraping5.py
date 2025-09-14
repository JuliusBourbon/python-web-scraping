# Scraping data pada web dengan login Form

# Import
import requests
from bs4 import BeautifulSoup
import csv

payload = {
    'email': 'admin@example.com',
    'password': 'password'
}

# Coba login dan lihat metode login pada Network->login->Headers(:method:)
response = requests.post('https://www.scrapingcourse.com/login', data=payload)

if response.status_code == 200:
    print('Request was Successful!')
else:
    print('Request failed with status code: ', response.status_code)

print(response.text)