from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com")

#count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
# print(count.text)

#click_link = driver.find_element(By.LINK_TEXT, "Contents")
# click_link.click()

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Paul")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("C")

email = driver.find_element(By.NAME, "email")
email.send_keys("p@c.com")

email.send_keys(Keys.ENTER)

# or click the button directly
# driver.find_element(By.CSS_SELECTOR,"form name").send_keys(Keys.ENTER)


