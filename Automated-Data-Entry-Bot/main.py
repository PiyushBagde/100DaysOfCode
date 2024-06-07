import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_option)

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
zillo_site = response.text

soup = BeautifulSoup(zillo_site, 'html.parser')

all_addresses = soup.find_all(attrs={"data-test": "property-card-addr"})
all_prices = soup.find_all(attrs={"data-test": "property-card-price"})
all_links = soup.find_all(class_="property-card-link")

links = [tag.get('href') for tag in all_links]
print('Got links')
prices = [tag.getText().replace("/mo", "").replace("+", "") for tag in all_prices]
print('Got prices')
addresses = [tag.getText().strip().replace("|", ",") for tag in all_addresses]
print('Got addresses')
print('Data Scrapped Successfully')

driver.get('https://forms.gle/T3fPenBEQZAb48oH8')
print('Driver Initialized')

for entry_num in range(len(prices)):
    time.sleep(2)
    inputs = driver.find_elements(By.CSS_SELECTOR, value='input[type="text"]')
    answers = {
        'address': inputs[0],
        'price': inputs[1],
        'link': inputs[2]
    }
    answers["address"].send_keys(f"{addresses[entry_num]}")
    answers["price"].send_keys(f"{prices[entry_num]}")
    answers["link"].send_keys(f"{links[entry_num]}")

    submit_button = driver.find_element(By.XPATH, value="//span[contains(text(),'Submit')]")
    time.sleep(1)
    submit_button.click()
    print(f"From({entry_num + 1}) Submitted")
    driver.find_element(By.LINK_TEXT, value="Submit another response").click()
