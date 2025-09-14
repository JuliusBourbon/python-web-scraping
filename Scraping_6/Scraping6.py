# Scraping data pada web dengan form login(CSRF-token)

# Import
import requests
from bs4 import BeautifulSoup
import csv

session = requests.Session()
response = session.get('https://www.scrapingcourse.com/login/csrf')
soup = BeautifulSoup(response.text, "html.parser")
csrf_token = soup.find("input", {"name": "_token"})["value"]
print("CSRF Token: ", csrf_token)

payload = {
    'email': 'admin@example.com',
    'password': 'password',
    '_token': csrf_token
}

# Ubah metode menjadi post
response = session.post('https://www.scrapingcourse.com/login/csrf', data=payload)

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

# Export Csv
with open("product.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["product name", "product price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)