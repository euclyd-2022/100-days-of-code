from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = ""
PASSWORD = ""
# open linked in
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords"
                          "=python%20developer&location=Manchester%2C%20England%2C%20United%20Kingdom&"
                          "redirect=false&position=1&pageNum=0")



# signin to linked in
click_link = driver.find_element(By.LINK_TEXT, "Sign in")
click_link.click()
time.sleep(2)
# enter username and password

email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button").send_keys(Keys.ENTER)
time.sleep(3)









