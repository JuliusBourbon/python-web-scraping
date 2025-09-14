# Scraping data dari website yang menggunakan AJAX request

# Import
import requests
from bs4 import BeautifulSoup
import csv

# Cek request URL ajax pada inspect->Network
BASE_URL = 'https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year=2014'

response = requests.get(BASE_URL)
items = response.json()
# Hasil scrapingnya akan menampilkan json karena memang bentuk awal data dari halamannya adalah json
print(items)

# JIKA INGIN MENGUBAH DATANYA DARI JSON KE CSV
# result = []
# for item in items:
#     title = item.get("title")
#     year = item.get("year")
#     awards = item.get("awards")

#     result.append({
#         "title": title,
#         "year": year,
#         "awards": awards
#     })

# Tampilkan hasil Scraping
# for item in result:
#     print(f'Title: {item['title']} - Year: {item['year']} - Awards: {item['awards']}')

# Export Csv
# with open("oscar.csv", "w", newline="", encoding="utf-8") as csvfile:
#     fieldnames = ["title", "year", "awards"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     for item in result:
#         writer.writerow(item)