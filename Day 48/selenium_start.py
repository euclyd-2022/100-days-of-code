from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://python.org")

dates = driver.find_elements(By.CLASS_NAME, "event-widget time")
titles = driver.find_elements(By.CLASS_NAME, "event-widget li a")
events = {}

for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": titles[n].text,

    }
print(events)


driver.close()


