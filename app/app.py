from flask import Flask
from flask import jsonify
from flask import request
from dotenv import load_dotenv
from service.DistanceService import DistanceService
from service.CompensationService import CompensationService

app = Flask(__name__)
load_dotenv()

@app.route("/getCompensationAmount", methods=["GET"])
def GetCompensationAmount():
    distanceService = DistanceService()
    compensationService = CompensationService()

    args = request.args
    distance = distanceService.GetDistance( args.get("lonFrom"), args.get("latFrom").upper(), 
                                            args.get("lonTo"), args.get(""))
    
    return jsonify(compensationService.CalculateCompensation(distance, args.get("toCurrency").upper()))






