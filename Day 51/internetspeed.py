from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_USERNAME = "euclyd"
TWITTER_PW = ""


class InternetSpeedTwitterBot:


    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://speedtest.net")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='onetrust-accept-btn-handler']").send_keys(Keys.ENTER)
        time.sleep(2)
        click_link = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        click_link.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"Upload: {self.up}")
        print(f"Download: {self.down}")



    def tweet(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)
        email = self.driver.find_element(By.NAME, "text")
        email.send_keys(TWITTER_USERNAME)
        email.send_keys(Keys.ENTER)
        time.sleep(2)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(TWITTER_PW)
        password.send_keys(Keys.ENTER)
        time.sleep(3)

        tweet = f"Upload speed: {self.up} Download speed: {self.down} ** messing about with a Python/Selenium bot"
        content = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/" \
                                           "div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/" \
                                           "div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")


        content.send_keys(tweet)
        post = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]"
                                                  "/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span").click()








