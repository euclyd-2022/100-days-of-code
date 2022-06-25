import requests
import smtplib

MY_LAT = 53.424150
MY_LONG = -2.175040
API_KEY = "4f3ac6ddd48d5bcde102213c02a7bf27"
API_URL = "https://api.openweathermap.org/data/2.5/onecall"
MY_EMAIL = "euclyd@gmail.com"
MY_PASSWORD = "uzwpjqdzgfpzsnxy"
TO = "euclyd@gmail.com"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,daily,minutely,alerts",
    "appid": API_KEY
}

response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
data = response.json()

#-------#
#using slice method
#data = data["hourly][:12]

weather_id = []
# next12 hourse
for n in range(11):
   weather_id.append(data["hourly"][n]["weather"][0]["id"])

if min(weather_id) < 700:
    #add twilio account for SMS update or SMTP for email and schedule to run via PythonAnywhere every day
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO, msg=f"Subject: Rain forecast today\n\nDon't forget an umbrella!")






