import requests


class FlightData:
    def __init__(self):
        self.kiwi_endpoint = "https://tequila-api.kiwi.com/"
        self.api_key = "1vt9yblXEcFscxKG-isrzGSM7pqtL5At"
        self.price_list = []

    def getcode(self, city_name):

        header = {"apikey": self.api_key,
                  "accept": "application/json"}
        data = {
            "term": city_name,
            "location_types": "city"

        }
        code_endpoint = "locations/query"
        code_response = requests.get(url=f"{self.kiwi_endpoint}{code_endpoint}", params=data, headers=header)
        code = code_response.json()["locations"]
        iatacode = code[0]["code"]
        return iatacode

    def getflights(self, iatacode):
        from datetime import datetime, timedelta
        today = datetime.today()
        tomorrow = (today + timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (today + timedelta(days=(30*6))).strftime("%d/%m/%Y")



        # https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021
        header = {"apikey": self.api_key,
                  "accept": "application/json"}
        data = {
            "fly_from": "LON",
            "fly_to": iatacode,
            "dateFrom": tomorrow,
            "dateTo": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "GBP",
        }
        flights_endpoint = "v2/search"
        flights_response = requests.get(url=f"{self.kiwi_endpoint}{flights_endpoint}", params=data, headers=header)
        flights = flights_response.json()["data"]

        self.price = flights[1]["price"]
        self.arrival_airport_code= flights[1]["cityCodeTo"]
        self.arrival_city = flights[1]["cityTo"]
        # self.price_list.append({"iataCode": self.arrival_airport_code,"city": self.arrival_city,"price": self.price})








