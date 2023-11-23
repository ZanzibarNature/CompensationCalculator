from requests import Request
import requests

class CompensationService:
    def __init__(self):
        pass

    def CalculateCompensation(self, distance, toCurrency):
        averageCo2PerKM = 171
        co2Footprint = distance * averageCo2PerKM / 1000
        costerPerKM = 0.0046575

        if (toCurrency != "EUR"):
            totalCost = self.ConvertCurrency(
                "EUR", toCurrency, (distance * costerPerKM))
        else:
            totalCost = distance * costerPerKM

        output = {"co2FootprintInKG": round(co2Footprint, 2),
                "totalCost": round(totalCost, 2),
                "currency": toCurrency}

        return output


    def ConvertCurrency(self, fromCurrency, toCurrency, amount):
        url = "https://api.fxratesapi.com/convert?from={}&to={}&amount={}&format=json".format(
            fromCurrency, toCurrency, amount)

        response = requests.get(url)

        if response.status_code == 200:
            responseJson = response.json()
            convertedAmount = round(responseJson['result'], 2)

            return convertedAmount
        else:
            return False
