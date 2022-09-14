import requests
from datetime import datetime
from secrets import NLP_TOKEN, NLP_APP_ID, NLP_APP_KEY


ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id": NLP_APP_ID,
    "x-app-key": NLP_APP_KEY,
}
params = {
    "query": input("what exercise did you do?")
}

response = requests.post(url=ENDPOINT, json=params, headers=header)
print(response.text)


SHEETY_ENDPOINT = "https://api.sheety.co/2bd35d5df20d0a8d28cdd1935ca84bd2/myWorkouts/workouts"

# example post {
#   "email": {
# 	"name": "Syed K",
# 	"email": "syed@gmail.com"
#   }
# }

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
data = response.json()["exercises"]

token = {
"Authorization": NLP_TOKEN
}
sheety_json = {
    "workout": {
    "date": date,
    "time": time,
    "exercise": data[0]["name"].title(),
    "duration": data[0]["duration_min"],
    "calories": data[0]["nf_calories"]
    }
}

sheety_post = requests.post(url=SHEETY_ENDPOINT, json=sheety_json, headers=token)
print(sheety_post.text)