from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

#driver.get("https://www.smythstoys.com/uk/en-gb/toys/action-figures-and-playsets/pet-simulator/pet-simulator-x-series-1-collector-clips/p/210427")
driver.get("https://www.smythstoys.com/uk/en-gb/toys/action-figures-and-playsets/pokemon/pokemon-trading-cards-game/pok%c3%a9mon-trading-card-game-pok%c3%a9mon-go-elite-trainer-box/p/211909")

#stock = driver.find_element(By.CSS_SELECTOR, "h1")
# stock = driver.find_element(By.XPATH, "/html/body/div[7]/section/div/div/div[2]/div[1]/h1")

#print(stock.text)

#driver.close()
try:
    driver.find_element(By.LINK_TEXT, "Select store").click()

# import NoSuchElementException from selenium
except NoSuchElementException:
        print("No link, skipped.")
        continue