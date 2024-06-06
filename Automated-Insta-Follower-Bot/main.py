import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

USERNAME = 'username'
PASSWORD = 'passwpord'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.get('https://www.instagram.com/')
        self.driver.maximize_window()

    def login(self):
        time.sleep(2)
        username = self.driver.find_element(By.NAME, value="username")
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, value="password")
        password.send_keys(PASSWORD)

        time.sleep(1)
        login_button = self.driver.find_element(By.CSS_SELECTOR, value='button[type="submit"]')
        login_button.click()

        time.sleep(4)
        off_notification = self.driver.find_element(By.XPATH, value="//button[normalize-space()='Not Now']")
        off_notification.click()

    def find_follower(self):
        time.sleep(1)
        search_button = self.driver.find_element(By.XPATH, value="(//span[contains(text(),'Search')])[1]")
        search_button.click()

        # find follower
        time.sleep(1)
        search_text = self.driver.find_element(By.CSS_SELECTOR, value='input[aria-label="Search input"]')
        search_text.send_keys("taylorswift")
        search_text.send_keys(Keys.ENTER)

        self.driver.get('https://www.instagram.com/taylorswift/followers/')

        time.sleep(1)
        get_followers = self.driver.find_element(By.XPATH, value="//a[contains(text(), ' followers')]")
        get_followers.click()

    def follow(self):
        time.sleep(4)
        for index in range(4, 25):
            time.sleep(2)
            follow = self.driver.find_element(By.XPATH, value=f"(//button[@type='button'])[{index}]")
            try:
                follow.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_follower()
bot.follow()
