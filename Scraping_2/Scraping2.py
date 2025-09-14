# Scraping website dengan Pagination
# Cara sederhana analisa website dengan Pagination adalah dengan melihat perubahan URL

# Import
import requests
from bs4 import BeautifulSoup
import csv

# Inisialisasi
BASE_URL = "https://www.scrapethissite.com/pages/forms/"
page_num = 1 
result = []
perpage = 100 # Untuk filter penentuan jumlah data yang ditampilkan pada 1x tampil halaman
searchquery = "bos" # Untuk filter search

while True:
    # Hanya filter berdasarkan page_num
    url = f"{BASE_URL}?page_num={page_num}"

    # Jika ingin mengambil data dengan filter jumlah data
    # url = f"{BASE_URL}?page_num={page_num}&per_page={perpage}"

    # Jika ingin mengambil data dengan filter jumlah data dan search
    # url = f"{BASE_URL}?page_num={page_num}&per_page={perpage}&q={searchquery}"
    
    print(f"Fetching page {url}...")

    response = requests.get(url)

    # Pengecekan halaman yang tidak bisa diakses
    if response.status_code != 200:
        print(f'Failed to retrieve page {page_num}')
        break
    
    # Tentukan block konten(table) dan row(tr)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="table")
    rows = table.find_all("tr", class_="team")

    # Pengecekan halaman yang tidak memiliki rows
    if not rows:
        print(f'No more data found on page {page_num}')
        break

    # Parsing Data
    for row in rows:
        team_name = row.find("td", class_="name").get_text(strip=True)
        year = row.find("td", class_="year").get_text(strip=True)
        pct = row.find("td", class_="pct").get_text(strip=True)

        result.append({
            "team_name": team_name,
            "year": year,
            "win_percentage": pct
        })

    page_num += 1

# Tampilkan hasil Scraping
# for item in result:
#     print(f"Team Name: {item['team_name']} - Year: {item['year']} - Win Percentage: {item['win_percentage']}")

# Export Csv
with open("hockey.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["team_name", "year", "win_percentage"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in result:
        writer.writerow(item)