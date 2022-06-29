import requests
import datetime as dt
TICKER = "TSLA"
COMPANY_NAME = "Tesla"
#timedate doesn't take into account weekend, better to get the data by array index
today =dt.date.today()
yesterday = str(today - dt.timedelta(days=3))
day_before = str(today - dt.timedelta(days=4))

def get_stock_change(name: str):
    global yesterday, day_before
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={name}&apikey=3MDN5EHZX84PNNA4"
    r = requests.get(url)
    data = r.json()
    price_yesterday_open = float(data["Time Series (Daily)"][yesterday]["1. open"])
    price_day_before_close = float(data["Time Series (Daily)"][day_before]["4. close"])

    difference = float((price_day_before_close - price_yesterday_open) / price_day_before_close * 100)
    return difference


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company: str):
    url = f"https://newsapi.org/v2/everything?qInTitle={company}&from={yesterday}&domains=seekingalpha.com&datatype=json&sortBy=publishedAt&apiKey=8e0d66080e024405813014e2b2a6eff3"
    r = requests.get(url)
    data = r.json()
    for n in range(3):
        title = data["articles"][n]["title"]
        news = data["articles"][n]["description"]
        print(f"Headline: {title}\nBrief: {news}")


difference = get_stock_change(TICKER)
#if -1.0 < get_stock_change(TICKER) > 1.0:
if difference < 1.0 or difference > 5.0:
    print(f"{TICKER} {int(difference)}% News:")
    get_news(COMPANY_NAME)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""