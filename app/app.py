from flask import Flask
from flask import jsonify
from requests import Request
from flask import request
from dotenv import load_dotenv

import os
import requests
import json


app = Flask(__name__)
load_dotenv()


@app.route("/getCompensationAmount", methods=["GET"])
def GetCompensationAmount():
    args = request.args
    distance = GetDistance(args.get("iataFrom"), args.get("iataTo"))

    return jsonify(CalculateCompensation(distance, args.get("toCurrency")))


def GetDistance(iataFrom, iataTo):
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

    distance = round(flightData["steps"][0]
                     ["distance"]["flight"][0]["distance"])
    return distance


def CalculateCompensation(distance, toCurrency):
    co2Footprint = distance * 171 / 1000
    costerPerKM = 0.0046575

    if (toCurrency != "EUR"):
        totalCost = ConvertCurrency(
            "EUR", toCurrency, (distance * costerPerKM))
    else:
        totalCost = distance * costerPerKM

    output = {"co2FootprintInKG": round(co2Footprint, 2),
              "totalCost": round(totalCost, 2),
              "currency": toCurrency}

    return output


def ConvertCurrency(fromCurrency, toCurrency, amount):
    url = "https://api.fxratesapi.com/convert?from={}&to={}&amount={}&format=json".format(
        fromCurrency, toCurrency, amount)

    response = requests.get(url)

    if response.status_code == 200:
        responseJson = response.json()
        convertedAmount = round(responseJson['result'], 2)

        return convertedAmount
    else:
        return Flask.make_response("Error: " + str(response.status_code), 500)
