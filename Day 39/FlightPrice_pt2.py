from datamanager import DataManager




dm = DataManager()
sheet_data = dm.get_data()

for item in sheet_data:
    if item['iataCode'] == "":
        from flightcheck import FlightData
        #create flightsearch object
        fs = FlightData()
        #assign the code form kiwitravel to the sheetdata
        item['iataCode'] = fs.getcode(item['city'])
    #update the google speadsheet with the iata airline code
    dm.update_data(item['id'], item['iataCode'])








