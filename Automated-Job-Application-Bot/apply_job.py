import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def sleep_for(sec):
    time.sleep(sec)


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)

# block 1 starts here
# basically it bypasses the login window eveytime you vist the link, no need to do signup
# for the first time you may need to login via credentials and do capthca verification and for the 2nd and further, it will load the cached data, whihc bypasses the login window
chrome_option.add_argument(r'--user-data-dir=C:\Users\piyus\AppData\Local\Google\Chrome\User Data')

# This creates the new user I have called temporaryLinkdin
chrome_option.add_argument('--profile-directory=temporaryLinkdin')

# block 1 ends here

driver = webdriver.Chrome(options=chrome_option)
driver.get(
    'https://www.linkedin.com/jobs/search/?currentJobId=3937348790&f_AL=true&f_E=2&f_TPR=r2592000&f_WT=1%2C2%2C3&keywords=Python%20developer&location=&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=DD')

driver.maximize_window()

# The uncomment the following when you are using credentials and not getting any captcha verification popups
# for this to work 2 step verification must be disaled.
# sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
# sign_in_button.click()
#
# sleep_for(1)
# email_box = driver.find_element(By.ID, value="username")
# email_box.send_keys("__YOUR_EMAILiD_OF_LINKDIN__")
#
# password_box = driver.find_element(By.ID, value="password")
# password_box.send_keys("__YOUR_ACC_PASSWORD__")
#
# sleep_for(2)
# submit = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
# submit.click()

# driver.find_element(By.XPATH, value='//*[@id="msg-overlay"]/div[1]/header/div[2]/button/span/span[1]').click()


sleep_for(1)
easy_apply = driver.find_element(By.CSS_SELECTOR,
                                 value='div button[class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')
easy_apply.click()

mobile_number = driver.find_element(By.XPATH,
                                    value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3937348790-379936843-phoneNumber-nationalNumber"]')
mobile_number.send_keys("9011169168")

sleep_for(1)
ph_next_button = driver.find_element(By.CSS_SELECTOR,
                                     value='button[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
ph_next_button.click()

sleep_for(1)
resume_next = driver.find_element(By.CSS_SELECTOR,
                                  value='button[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
resume_next.click()

sleep_for(1)
select_yes = driver.find_element(By.CSS_SELECTOR, value='label[data-test-text-selectable-option__label="Yes"]')
select_yes.click()

python_work_experience = driver.find_element(By.CSS_SELECTOR, value='input[class=" artdeco-text-input--input"]')
python_work_experience.send_keys("1")

sleep_for(1)
review_button = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Review your application"]')
review_button.click()

time.sleep(2)
submit_application = driver.find_element(By.CSS_SELECTOR, value='button[aria-label="Submit application"]')
submit_application.click()

print('Application Submitted')
