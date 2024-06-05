import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Define desired internet speeds
PROMISED_DOWN = 60
PROMISED_UP = 60

# Replace with your actual Twitter credentials (not recommended for real use)
TWITTER_EMAIL = "__YOUR_TWITTER_ACC_EMAIL__"
TWITTER_PASSWORD = "__PASSWORD__"
TWITTER_USERNAME = '__USERNAME__'

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)  # Run Chrome in the background


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_option)
        self.up = 0  # Initialize upload speed
        self.down = 0  # Initialize download speed

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go_button = self.driver.find_element(By.CSS_SELECTOR,
                                             value="a[aria-label='start speed test - connection type multi']")
        go_button.click()

        time.sleep(80)  # Wait for speed test to complete

        self.down = self.driver.find_element(By.CSS_SELECTOR,
                                             value='span[class="result-data-large number result-data-value download-speed"]').text
        self.up = self.driver.find_element(By.CSS_SELECTOR,
                                           value='span[class="result-data-large number result-data-value upload-speed"]').text
        print(f"Download Speed : {self.down}")
        print(f"Upload Speed : {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        time.sleep(2)

        sign_in_button = self.driver.find_element(By.XPATH, value="//span[contains(text(),'Sign in')]")
        sign_in_button.click()

        time.sleep(5)

        email = self.driver.find_element(By.CSS_SELECTOR, value='input[autocomplete="username"]')
        email.send_keys(TWITTER_EMAIL)  # Don't use real credentials in code

        time.sleep(1)
        email_next = self.driver.find_element(By.XPATH, value="//span[contains(text(),'Next')]")
        email_next.click()

        # Commented out username and password login steps (not recommended)
        # time.sleep(5)
        # username = self.driver.find_element(By.CSS_SELECTOR, value="input[name='text']")
        # username.send_keys(TWITTER_USERNAME)
        #
        # time.sleep(1)
        # username_next = self.driver.find_element(By.XPATH, value="//span[contains(text(),'Next')]")
        # username_next.click()

        time.sleep(5)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(TWITTER_PASSWORD)  # Don't use real credentials in code

        time.sleep(1)
        login_button = self.driver.find_element(By.CSS_SELECTOR, value="button[data-testid='LoginForm_Login_Button']")
        login_button.click()

        time.sleep(5)

        post_button = self.driver.find_element(By.CSS_SELECTOR, value='a[aria-label="Post"]')
        post_button.click()

        time.sleep(5)
        post_content = self.driver.find_element(By.CSS_SELECTOR, value='br[data-text="true"]')
        post_content.send_keys(
            f"Why my internet speed is {self.down}/{self.up}, even if am paying for {PROMISED_DOWN}/{PROMISED_UP} huh?")

        time.sleep(2)
        draft_button = self.driver.find_element(By.XPATH, value="//span[contains(text(),'Drafts')]")
        draft_button.click()

        time.sleep(1)

        save_button = self.driver.find_element(By.XPATH,
                                               value='//*[@id="layers"]/div[3]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]/div/span/span')
        save_button.click()  # This XPath seems overly complex, consider simplifying the selector


# Create an instance of the bot and run its methods
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

# Close the browser window
bot.driver.quit()
