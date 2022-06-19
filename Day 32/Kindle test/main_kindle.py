#send a motivation quote via email on the current weekday
# use datetime module
#pick a random quote
#use smtplib

import smtplib
import datetime as dt
import pandas
import random

#import clippings.txt kindle
with open('../100-days-of-code/Day 32/Kindle test/Clippings.txt', 'r', encoding='utf-8-sig') as f:
    contents = f.read().replace(u'\ufeff', '')
    lines = contents.rsplit('==========')

df = pandas.DataFrame(lines)
quote_output = df.to_csv()
print(quote_output)
#pick a random quote
random_quote = random.choice(quote_output)
print(random_quote)


#monday = 0
saturday = 5
now = dt.datetime.now()
my_email = "euclyd@gmail.com"
body = ""
subject = ""

if now.weekday() == saturday:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="uzwpjqdzgfpzsnxy")
        #connection.sendmail(from_addr=my_email, to_addrs="theeuclyd@hotmail.com, msg=f"Subject: {subject}\n\n{body}")




