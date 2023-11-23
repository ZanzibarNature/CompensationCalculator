from requests import Request
import requests
import os
import json

class DistanceService:
    def __init__(self):
        pass
        

    def GetDistance(self, iataFrom, iataTo):
        if (os.getenv("DEV_MODE") == "false"):
            route = json.dumps([{"t": iataFrom}, {"t": iataTo}])

            # Maar 100 requests per maand :(, bij devmode gebruikt hij de example response
            url = "https://distanceto.p.rapidapi.com/get?route=" + route
            headers = {
                'x-rapidapi-key': os.getenv("RAPID_API_KEY"),
                'x-rapidapi-host': "distanceto.p.rapidapi.com"
            }
            response = requests.request("GET", url, headers=headers)
            flightData = response.json()
        else:
            flightData = json.load(open('exampleflight.json'))

        distance = round(flightData["steps"][0]["distance"]["flight"][0]["distance"])
        return distance
