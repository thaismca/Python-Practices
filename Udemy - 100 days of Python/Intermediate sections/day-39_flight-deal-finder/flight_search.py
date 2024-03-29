import requests
import os
from datetime import datetime, timedelta

from flight_data import FlightData

# retrieving hidden sensitive information -> Environment Variables
from dotenv import load_dotenv
load_dotenv()


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        # tequila endpoint
        self.endpoint = "https://tequila-api.kiwi.com"
        
        # request headers
        self.headers = {
            "apikey": os.environ.get('TEQUILA_API_KEY')
        }

        # flight search criteria
        self.origin = os.environ.get('ORIGIN')
        self.depart_date_from = (datetime.now() + timedelta(1)).date()
        self.depart_date_to = (datetime.now() + timedelta(weeks=24)).date()
        self.min_stay = os.environ.get('MIN_STAY')
        self.max_stay = os.environ.get('MAX_STAY')
        self.currency = os.environ.get('CURRENCY')



    def get_iata_code(self, city):
        '''This function returns the IATA code for a given city'''
        params = {
            "term": city,
            "location_types": "city"
        }
        location_res = requests.get(f'{self.endpoint}/locations/query', params=params,headers=self.headers)
        location_res.raise_for_status()
        location_res_data = location_res.json()["locations"]
        
        return location_res_data[0]["code"]
    


    def find_flights(self, city, max_price):
        '''This function returns an array with all the flights that match the search criteria.'''

        ## In this project, we're looking only for direct flights, that leave anytime between tomorrow and in 6 months time.
        ## We're also looking for round trips that return between 7 and 28 days in length.
        ## The currency of the price we get back should be in CAD.
        params = {
            "fly_from": self.origin,
            "fly_to": city,
            "date_from": self.depart_date_from,
            "date_to": self.depart_date_to,
            "nights_in_dst_from": self.min_stay,
            "nights_in_dst_to": self.max_stay,
            "flight_type": "round",
            "curr": self.currency,
            "price_to": max_price
        }
        flights_res = requests.get(f'{self.endpoint}/search', params=params,headers=self.headers)
        flights_res.raise_for_status()
        flights_res_data = flights_res.json()["data"]

        ## in the course only the fisrt result is being considered to send a message
        ## here I want to send a message with all the options that match the search criteria
        all_flights_data = []
        for flight in flights_res_data:
            flight_data = FlightData(
                departure_airport = flight["flyFrom"],
                departure_city = flight["cityFrom"],
                destination_airport = flight["flyTo"],
                destination_city = flight["cityTo"],
                price = flight["price"],
                departure_date = datetime.fromtimestamp(flight["dTime"]).date(),
                return_date = (datetime.fromtimestamp(flight["dTime"]) + timedelta(flight["nightsInDest"])).date()
            )
            all_flights_data.append(flight_data)

        return all_flights_data

