import requests


class FlightSearch:
    def __init__(self, city_name):
        self.city = city_name
        self.iatacode = "TESTING"


class DataManager:
    def __init__(self, id, body):
        self.put = f"{SHEETY_ENDPOINT}/{id}"
        self.parameters = {
           "price": {
               "iataCode": body
           }
        }
    def update(self):
        requests.put(url=self.put, json=self.parameters)
        return 0


SHEETY_ENDPOINT = "https://api.sheety.co/2bd35d5df20d0a8d28cdd1935ca84bd2/flightDeals/prices"
response = requests.get(url=SHEETY_ENDPOINT)
sheet_data = response.json()["prices"]




for item in sheet_data:
    if item['iataCode'] == "":
       fs =  FlightSearch(item["city"])
       item['iataCode'] = fs.iatacode

    dm = DataManager(item['id'], item['iataCode']).update()




