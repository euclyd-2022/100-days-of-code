import requests

class FlightSearch:
    def __init__(self):
        self.kiwi_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.api_key = "1vt9yblXEcFscxKG-isrzGSM7pqtL5At"

    def getcode(self, city_name):

        header = {"apikey": self.api_key,
                  "accept": "application/json"}
        data = {
            "term": city_name,
            "location_types": "city"

        }
        code_response = requests.get(url=self.kiwi_endpoint, params=data, headers=header)
        code = code_response.json()["locations"]
        iatacode = code[0]["code"]
        return iatacode

