import requests
from datetime import datetime


#use APIs from Pixela
#create a user account:
#curl -X POST https://pixe.la/v1/users -d '{"token":"thisissecret", "username":"a-know", "agreeTermsOfService":"yes", "notMinor":"yes"}'

# https://pixe.la/v1/users/euclyd/graphs/workout-tracker.html

ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "euclyd"
GRAPH_ENDPOINT = f"{USERNAME}/graphs"
GRAPH_ID = "workout-tracker"
TOKEN = "alpha751bcd"

def createuser():
    params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    response = requests.post(url=ENDPOINT, json=params)

    print(response.text)
    return response.json


def creategraph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Workout Tracker",
        "unit": "commit",
        "type": "int",
        "color": "kuro",
    }
    header = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=f"{ENDPOINT}/{GRAPH_ENDPOINT}", json=graph_config, headers=header)
    print(response.text)

def addpixel():
    today = datetime.now()
    #/v1/users/<username>/graphs/<graphID
    #$ curl -X POST https://pixe.la/v1/users/a-know/graphs/test-graph -H 'X-USER-TOKEN:thisissecret' -d '{"date":"20180915","quantity":"5","optionalData":"{\"key\":\"value\"}"}'
    header = {
        "X-USER-TOKEN": TOKEN
    }
    pixel_config = {
        "date": today.strftime("%Y%m%d"),
        "quantity": input("How many times did you workout today?"),

    }
    response = requests.post(url=f"{ENDPOINT}/{GRAPH_ENDPOINT}/{GRAPH_ID}", json=pixel_config, headers=header)
    print (response.text)

def updatepixel():
    #$ curl -X PUT https://pixe.la/v1/users/a-know/graphs/test-graph/20180915 -H 'X-USER-TOKEN:thisissecret' -d '{"quantity":"7","optionalData":"{\"key\":\"value\"}"}'

    header = {
        "X-USER-TOKEN": TOKEN
    }
    pixel_config = {
        "quantity": "3",

    }
    response = requests.put(url=f"{ENDPOINT}/{GRAPH_ENDPOINT}/{GRAPH_ID}/20220207", json=pixel_config, headers=header)
    print(response.text)

def deletepixel():
    #$ curl -X DELETE https://pixe.la/v1/users/a-know/graphs/test-graph/20180915 -H 'X-USER-TOKEN:thisissecret'
    header = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.delete(url=f"{ENDPOINT}/{GRAPH_ENDPOINT}/{GRAPH_ID}/20220207", headers=header)
    print(response.text)

#createuser()
#creategraph()
#addpixel()
#updatepixel()
deletepixel()