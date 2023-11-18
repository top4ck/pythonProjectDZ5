import requests
from bs4 import BeautifulSoup
import lxml

user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
headers = {"User-agent": user}

session = requests.Session()

for j in range(1, 7):
    print(f"Page {j}")
    page_url = f"https://cash-backer.club/shops?page={j}"
    response = session.get(page_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")

        for i in all_products:
            title = i.find('div', class_="shop-title")
            cashback = i.find("div", class_="shop-rate")
            print(cashback.text)
            print(title.text)