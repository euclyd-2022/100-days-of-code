from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
money = driver.find_element(By.CSS_SELECTOR, "#money")
rewards = driver.find_elements(By.CSS_SELECTOR, "#store b")


def loop():
    global money
    print(money.text)
    int_money = money.text.replace(",", "")
    int_money = int(int_money)
    t_end = time.time() + 5
    while time.time() < t_end:
        cookie.click()
    max_reward = []
    for reward in rewards[:-1]:
        rew = reward.text
        rew = str.split(rew, "-")
        rew = str.strip(rew[len(rew) - 1])
        rew = rew.replace(",", "")
        max_reward.append(rew)
    print(max_reward)
    buy(max_reward, int_money)
    loop()

def buy(max_reward, money):
    print(money)
    for n in range(len(max_reward) -1, 0, -1):
        print(max_reward[n])
    print(max(max_reward))
    if max_reward < money:


loop()





