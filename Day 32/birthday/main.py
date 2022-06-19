##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
#ANGELA'S ANSWER:

# today = dt.datetime.now()
# today_tuple = (today.month, today.day)
# data = pandas.read_csv("birthdays.csv")
# birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# if today_tuple in birthdays_dict:
#     pass


import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "euclyd@gmail.com"
PASSWORD = "uzwpjqdzgfpzsnxy"
with open("birthdays.csv") as birthdays:
    bday_list = pandas.read_csv(birthdays)


#print(bday_list["month"])

today_month = dt.datetime.now().month
today_date = dt.datetime.now().day
filenames = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
for index, row in bday_list.iterrows():

    if row["month"] == today_month and row["day"] == today_date:
        name = row["name"]
        to = row["email"]
        with open("letter_templates\\" + random.choice(filenames)) as body:
            body = body.read()
            new_body = body.replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=to, msg=f"Subject: Happy Birthday {name}!\n\n{new_body}")












