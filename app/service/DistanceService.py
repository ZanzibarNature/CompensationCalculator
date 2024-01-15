from requests import Request
from geopy.distance import geodesic


class DistanceService:
    def __init__(self):
        pass
        
    # GetDistance kan ook ook zonder externe api door zelf de coordinaten op te slaan in een database
    # en dan de coordinaten te gebruiken om de afstand te berekenen met geopy
    
    def GetDistance(self, lonFrom, latFrom, lonTo, latTo):
        fromPlace = (lonFrom, latFrom)
        toPlace = (lonTo, latTo)
        try:
            distance = round(geodesic(fromPlace, toPlace).km)
            return distance
        except:
            raise Exception("Distance calculation failed")
          
    
    # def patternIata(self, iata):
    #     patternIata = r'^[a-zA-Z]+$'
    #     if(not re.match(patternIata, str(iata))):
    #         raise Exception("Invalid input")
    #     return True

    # def GetDistance(self, iataFrom, iataTo):
    #     if (os.getenv("DEV_MODE") == "false"):
    #         route = json.dumps([{"t": iataFrom}, {"t": iataTo}])
                        
    #         self.patternIata(iataFrom)
    #         self.patternIata(iataTo)
            
    #         # Maar 100 requests per maand :(, bij devmode gebruikt hij de example response
    #         url = "https://distanceto.p.rapidapi.com/get?route=" + route
    #         headers = {
    #             'x-rapidapi-key': os.getenv("RAPID_API_KEY"),
    #             'x-rapidapi-host': "distanceto.p.rapidapi.com"
    #         }
    #         response = requests.request("GET", url, headers=headers)
    #         flightData = response.json()
    #     else:
    #         flightData = json.load(open('exampleflight.json'))

    #     distance = round(flightData["steps"][0]["distance"]["flight"][0]["distance"])
    #     return distance