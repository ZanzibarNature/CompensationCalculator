from flask import Flask
from flask import jsonify
from flask import request
from dotenv import load_dotenv
from prometheus_flask_exporter import PrometheusMetrics
from service.DistanceService import DistanceService
from service.CompensationService import CompensationService
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)
load_dotenv()

metrics = PrometheusMetrics(app)

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route("/getCompensationAmount", methods=["GET"])
def GetCompensationAmount():
    """Get compensation amount
    ---
    parameters:
      - name: lonFrom
        in: query
        type: string
        required: true
      - name: latFrom
        in: query
        type: string
        required: true
      - name: lonTo
        in: query
        type: string
        required: true
      - name: latTo
        in: query
        type: string
        required: true
      - name: toCurrency
        in: query
        type: string
        required: true
    responses:
        200:
            description: Compensation amount
            schema:
            id: compensation
            properties:
                co2FootprintInKG:
                type: float
                description: The co2 footprint in kg
                default: 0
                totalCost:
                type: float
                description: The total cost
                default: 0
                currency:
                type: string
                description: The currency
                default: EUR
    """
    distanceService = DistanceService()
    compensationService = CompensationService()
    
    args = request.args
    required_headers = ["lonFrom", "latFrom", "lonTo", "latTo", "toCurrency"]
    missing_headers = [header for header in required_headers if header not in args]
    if missing_headers:
      return jsonify({"error": f"Missing headers: {', '.join(missing_headers)}"}), 400
    
    try:
        distance = distanceService.GetDistance(args.get("lonFrom"), args.get("latFrom"), 
                        args.get("lonTo"), args.get("latTo"))
        return jsonify(compensationService.CalculateCompensation(distance, args.get("toCurrency").upper()))
    except:
        return jsonify({"error": "Calculation failed"}), 400
      
@app.route("/test", methods=["GET"])
def Test():
    return jsonify({"test": "test"})
      






