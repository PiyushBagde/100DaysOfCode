import smtplib

import requests
from bs4 import BeautifulSoup

MY_EMAIL = "{Your Email}"
PASSWORD = "{Your password}"

website_link = "{product website link from amazon}"

headers = {
    "User-Agent": "Defined",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6,km;q=0.5,zh-TW;q=0.4"
}

response = requests.get(
    url=website_link, headers=headers)
amazon_html = response.text

soup = BeautifulSoup(amazon_html, 'lxml')
# print(soup.prettify())

all_prices = soup.find_all('span', class_="a-offscreen")
product_price = all_prices[0].get_text()

target_price = float(31000)

live_price = float((product_price.split(",")[0])[1:] + product_price.split(",")[1])
print(live_price)

if live_price <= target_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"It's time to buy new phone\n\n cuz the prices are low now"
                                f"current price: {live_price}"
                                f"\nhere is the link: {website_link}")
        print("sent")

else:
    print("have patience")
