# Scraping data pada web dengan form login(CSRF-token)

# Import
import requests
from bs4 import BeautifulSoup

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

print(response.text)