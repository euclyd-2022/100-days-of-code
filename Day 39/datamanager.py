import requests
SHEETY_ENDPOINT = "https://api.sheety.co/2bd35d5df20d0a8d28cdd1935ca84bd2/flightDeals/prices"

class DataManager:

    def get_data(self):

        response = requests.get(url=SHEETY_ENDPOINT)
        sheet_data = response.json()["prices"]
        return sheet_data

    def update_data(self, id, body):
        put = f"{SHEETY_ENDPOINT}/{id}"
        parameters = {
            "price": {
                "iataCode": body
            }
        }
        update_response = requests.put(url=put, json=parameters)
        print(update_response.text)
        
