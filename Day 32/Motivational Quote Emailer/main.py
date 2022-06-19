#send a motivation quote via email on the current weekday
# use datetime module
#pick a random quote
#use smtplib

import smtplib
import datetime as dt
import random

quotes = []
with open("../100-days-of-code/Day 32/Motivational Quote Emailer/quotes.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    quotes.append(line)

#pick a random quote
random_quote = random.choice(quotes)
print(random_quote)


#monday is day 0 so sat is day 5
saturday = 5
now = dt.datetime.now()
MY_EMAIL = ""
TO = ""
PASSWORD = ""
body = random_quote
subject = "Quote of the week"

if now.weekday() == saturday:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO, msg=f"Subject: {subject}\n\n{body}")




