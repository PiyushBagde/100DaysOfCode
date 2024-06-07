import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from scrapedata import ScrapeData


class FillGform(ScrapeData):
    def __init__(self):
        super().__init__()
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_option)
        print('Driver Initialized')

    def fill_form(self):
        self.driver.get('https://forms.gle/T3fPenBEQZAb48oH8')

        for entry_num in range(len(self.prices)):
            time.sleep(2)
            inputs = self.driver.find_elements(By.CSS_SELECTOR, value='input[type="text"]')
            answers = {
                'address': inputs[0],
                'price': inputs[1],
                'link': inputs[2]
            }
            answers["address"].send_keys(f"{self.addresses[entry_num]}")
            answers["price"].send_keys(f"{self.prices[entry_num]}")
            answers["link"].send_keys(f"{self.links[entry_num]}")

            submit_button = self.driver.find_element(By.XPATH, value="//span[contains(text(),'Submit')]")
            time.sleep(1)
            submit_button.click()
            print(f"From({entry_num + 1}) Submitted")
            self.driver.find_element(By.LINK_TEXT, value="Submit another response").click()
