import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

chrome_option.add_argument(r'--user-data-dir=C:\Users\{user}\AppData\Local\Google\Chrome\User Data')

chrome_option.add_argument('--profile-directory=temporaryTinder')

driver = webdriver.Chrome(options=chrome_option)
driver.get('https://tinder.com/app/recs')

driver.maximize_window()
time.sleep(8)

actions = ActionChains(driver)

for _ in range(10):
    time.sleep(2)
    actions.send_keys(Keys.ARROW_RIGHT)
    actions.perform()
