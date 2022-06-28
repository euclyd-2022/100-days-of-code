import requests
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *


TICKER = "TSLA"
COMPANY_NAME = "Tesla"

today =dt.date.today()
yesterday = str(today - dt.timedelta(days=1))


def api_data(name: str):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={name}&apikey=3MDN5EHZX84PNNA4"
    try:
        r = requests.get(url)

    except:
        print("cannot connect")
    data = r.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]
    return data_list

def get_stock_change(data_list):

    price_yesterday_open = float(data_list[0]["1. open"])
    price_day_before_close = float(data_list[1]["4. close"])

    difference = float((price_day_before_close - price_yesterday_open) / price_day_before_close * 100)
    return difference


def chart(data_list):
    close_prices = []
    for n in range(30, 0, -1):
        close_prices.append(float(data_list[n]["4. close"]))

    np_array = np.array(close_prices)
    plt.title(f'{TICKER} chart')
    plt.plot(np_array)
    plt.show()
    #plt.Figure()

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


def get_news(company: str):
    url = f"https://newsapi.org/v2/everything?q={company}&from={yesterday}&domains=seekingalpha.com&datatype=json&sortBy=publishedAt&apiKey=8e0d66080e024405813014e2b2a6eff3"
    try:
        r = requests.get(url)
    except:
        print ("error getting news")
    data = r.json()
    for n in range(3):
        title = data["articles"][n]["title"]
        news = data["articles"][n]["description"]
        return f"Headline: {title}\nBrief: {news}"


window = Tk()
window.title("Stonks")
window.config(padx=50, pady=50)
canvas = Canvas(width=800, height=600)
canvas.create_text(500, 500, text=get_news(TICKER))
canvas.grid(column=0, row=0)

website_label = Label(text="")
website_label.grid(column=0, row=1)

chart(api_data(TICKER))
#get_stock_change(TICKER)


#difference = get_stock_change(TICKER)


# #if -1.0 < get_stock_change(TICKER) > 1.0:
# if difference < 1.0 or difference > 5.0:
#     print(f"{TICKER} {int(difference)}% News:")
    #get_news(COMPANY_NAME)



window.mainloop()

