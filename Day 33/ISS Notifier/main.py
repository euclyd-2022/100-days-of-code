import requests
import datetime as dt

MY_LAT = 53.424150
MY_LONG = -2.175040

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

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

print(sunrise)

now = dt.datetime.now()

print(now.hour)