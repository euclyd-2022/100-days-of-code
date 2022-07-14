import requests
from bs4 import BeautifulSoup
import smtplib
MY_EMAIL = "euclyd@gmail.com"
PASSWORD = "uzwpjqdzgfpzsnxy"
TARGET_PRICE = 450.00
# URL = "https://www.amazon.co.uk/Garmin-010-02120-10-Watch-Forerunner/dp/B07RCJV4PT/" \
#      "ref=sr_1_3?crid=136K4YMJQM821&keywords=forerunner%2B255&qid=1657708201&smid=A3P5ROKL5A1OLE&sprefix=foreunner%2Caps%2C78&sr=8-3&th=1"
URL = "https://www.amazon.co.uk/Garmin-Forerunner-Premium-Triathlon-Smartwatch/dp/B07QTVMWVL/ref=sr_1_7?crid=136K4YMJQM821&keywords=forerunner+255&qid=1657708906&sprefix=foreunner%2Caps%2C78&sr=8-7"
header = {

"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
"Accept-Language": "en,en-GB;q=0.9"
}


response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

item = soup.find(name="span", class_="a-offscreen")
title = str.strip(soup.find(name="span", id="productTitle").getText())
print(title)
#print the number only as a float
current_price = float(item.getText().split("£")[1])

if current_price < TARGET_PRICE:
    body = f"Price for {title} is now {current_price}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: Target Price for {title}!\n\n{body}")
