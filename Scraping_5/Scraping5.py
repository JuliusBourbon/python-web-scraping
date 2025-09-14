# Scraping data pada web dengan login Form

# Import
import requests
from bs4 import BeautifulSoup
import csv

payload = {
    'email': 'admin@example.com',
    'password': 'password'
}

# Ganti metode get dengan menggunakan post
response = requests.post('https://www.scrapingcourse.com/login', data=payload)

# Pengecekan status halaman
if response.status_code == 200:
    print('Request was Successful!')
else:
    print('Request failed with status code: ', response.status_code)

# print(response.text)

# Menentukan Block konten
soup = BeautifulSoup(response.text, "html.parser")
blocks = soup.find_all("div", class_="product-item")
# print(len(blocks))

# Parsing Data
result = []
for block in blocks:
    product_name = block.find("span", class_="product-name").get_text(strip=True)
    product_price = block.find("span", class_="product-price").get_text(strip=True)

    result.append({
        "product name": product_name,
        "product price": product_price
    })

for item in result:
    print(f"Product Name: {item['product name']} - Product Price: {item['product price']}")