from datamanager import DataManager
from flightcheck import FlightData
import smtplib



dm = DataManager()
fs = FlightData()
sheet_data = dm.get_data()

def send_email():
    import os

    MY_EMAIL = "euclyd@gmail.com"
    GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject: Price alert!\n\n")


for row in sheet_data:
    # create flightsearch object

    if row['iataCode'] == "":
        #assign the code form kiwitravel to the sheetdata
        row['iataCode'] = fs.getcode(row['city'])
        # update the google speadsheet with the iata airline code
        dm.update_data(row['id'], row['iataCode'])
    fs.getflights(row['iataCode'])

    if fs.price < row['lowestPrice']:

        print(f"{row['iataCode']} price now of {fs.price} is lower than usual of {row['lowestPrice']}")
    else:
        print(f"****{row['iataCode']} price now of {fs.price} is more or the same as the usual price of {row['lowestPrice']}****")










