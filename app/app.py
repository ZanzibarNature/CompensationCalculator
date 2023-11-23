from flask import Flask
from flask import jsonify
from flask import request
from dotenv import load_dotenv
from service.DistanceService import DistanceService
from service.CompensationService import CompensationService

import os
import json


app = Flask(__name__)
load_dotenv()

@app.route("/getCompensationAmount", methods=["GET"])
def GetCompensationAmount():
    distanceService = DistanceService()
    compensationService = CompensationService()

    args = request.args
    distance = distanceService.GetDistance( args.get("iataFrom").upper(), args.get("iataTo").upper())
    
    return jsonify(compensationService.CalculateCompensation(distance, args.get("toCurrency".upper())))






