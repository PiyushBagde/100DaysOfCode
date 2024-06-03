import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def sleep_for(sec):
    time.sleep(sec)


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

chrome_option.add_argument(r'--user-data-dir=C:\Users\piyus\AppData\Local\Google\Chrome\User Data')

# This creates the new user I have called temporaryLinkdin
chrome_option.add_argument('--profile-directory=temporaryLinkdin')

driver = webdriver.Chrome(options=chrome_option)
driver.get(
    'https://www.linkedin.com/jobs/search/?currentJobId=3940903819&f_AL=true&f_E=1%2C2&f_TPR=r2592000&f_WT=1%2C2%2C3&geoId=101165590&keywords=python%20developer&location=United%20Kingdom&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true&sortBy=DD')

driver.maximize_window()

sleep_for(2)
job_list = driver.find_element(By.CSS_SELECTOR, value=".scaffold-layout__list-container")
all_jobs = job_list.find_elements(By.CSS_SELECTOR, value='a')

for job in all_jobs:
    job.click()

    sleep_for(1)
    save_button = driver.find_element(By.CSS_SELECTOR, value="div[class='display-flex'] button[type='button']")
    sleep_for(1)
    save_button.click()
    print("job saved")



# NOTE: if you re-run this python script it will unsave the jobs you have saved just now, hah take care of that
