from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
#detatch to stop the page disappearing
options.add_experimental_option("detach", True)
# use your own chrome profile https://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver
# options.add_argument("user-data-dir=Path to your chrome profile")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com")

#count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text
# print(count.text)

#click_link = driver.find_element(By.LINK_TEXT, "Contents")
# click_link.click()

fname = driver.find_element(By.NAME, "fName")
fname.send_keys(TWITTER_USERNAME)

lname = driver.find_element(By.NAME, "lName")
lname.send_keys(TWITTER_PW)

email = driver.find_element(By.NAME, "email")
email.send_keys("p@c.com")

email.send_keys(Keys.ENTER)

# or click the button directly
# driver.find_element(By.CSS_SELECTOR,"form name").send_keys(Keys.ENTER)


