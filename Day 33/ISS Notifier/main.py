import requests
import datetime as dt
import smtplib
import time

MY_EMAIL = "euclyd@gmail.com"
PASSWORD = "uzwpjqdzgfpzsnxy"

#floats
MY_LAT = 53.424150
MY_LONG = -2.175040

def check_position():
    # Your position is within +5 or -5 degrees of the ISS position.
    global iss_longitude
    global iss_latitude
    if iss_latitude > (MY_LAT - 5) and iss_latitude < (MY_LAT + 5):
        if iss_longitude > (MY_LONG - 5) and iss_longitude < (MY_LONG + 5):
            return True
    else:

        return False


def is_it_dark():
    """check is the current hour is nighttime"""
    global now, sunrise, sunset
    #pycharm simplified the comaparison
    if int(sunrise) > int(now.hour) > int(sunset):
        print("darkness descends")
        return True
    else:
        return False

def send_mail():
    global now
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: ISS in Sight!\n\nLook up at the International Space Station!")





parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])





response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
#check for errors
response.raise_for_status()
#convert to json
data = response.json()
#put sunrise and sunset times in variables
sunrise = data["results"]["sunrise"]
#split the datetime up by T and the : to give a list of times and get [0] which is the hour
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
now = dt.datetime.now()



#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    print("scanning...")
    print(check_position())
    print(is_it_dark())
    if check_position() and is_it_dark():
        print("sending an email")
        send_mail()


print(f"sunrise: {sunrise}\n sunset {sunset}\n now:{now.hour} s{now.second}\n isslat:{iss_latitude}\n my lat:{MY_LAT}\n isslong:{iss_longitude}\n"
      f" My Long{MY_LONG}")