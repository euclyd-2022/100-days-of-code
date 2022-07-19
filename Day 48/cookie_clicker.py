from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("http://orteil.dashnet.org/experiments/cookie/")




def loop():

    cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")
    money = driver.find_element(By.CSS_SELECTOR, "#money")
    rewards = driver.find_elements(By.CSS_SELECTOR, "#store b")
    # print(money.text)
    # convert cookies to int
    int_money = money.text.replace(",", "")
    int_money = int(int_money)
    t_end = time.time() + 5
    while time.time() < t_end:
        cookie.click()
    max_reward = {}
    # get the stripped price of the upgrade
    for reward in rewards[:-1]:
        rew = reward.text
        rew = str.split(rew, "-")
        name = rew[0]
        rew = str.strip(rew[len(rew) - 1])
        rew = rew.replace(",", "")
        # add to dictionary if affordable
        if int(rew) < int_money:
            max_reward[name] = int(rew)
            #print(max_reward)
            buy(max_reward, int_money)

    loop()

def buy(max_reward, available_money):
    print(available_money)

    # # loop through all prices highest to the lowest clicking on each



    # for n in range(len(max_reward) - 1, 0, -1):
    #
    #     item_key = list(max_reward)[n]
    #     stripped_item_key = item_key.rstrip()
    #     item_value = max_reward[item_key]

    item_key = max(max_reward, key=max_reward.get)
    stripped_item_key = item_key.rstrip()
    item_value = max_reward[item_key]

    css = f"buy{stripped_item_key}"
    driver.find_element(By.ID, css).click()
    print(css)
    print(f"{item_value} < {available_money}")




loop()





