import requests

MY_LAT = 53.424150
MY_LONG = -2.175040
API_KEY = "4f3ac6ddd48d5bcde102213c02a7bf27"
API_URL = "https://api.openweathermap.org/data/2.5/onecall"

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
    print("Bring an umbrella")

#add twilio account for SMS update or SMTP for email ans scedule to run via PythonAnywhere every day







