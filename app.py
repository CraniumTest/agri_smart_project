from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
from collect_sensor_data import collect_sensor_data
from train_model import predict_yield
from evaluate_conditions import evaluate_conditions

app = Flask(__name__)
CORS(app)
api = Api(app)

class CropMonitor(Resource):
    def get(self):
        # Simulate data fetching
        data = collect_sensor_data()
        yield_prediction = predict_yield(data)
        alerts = evaluate_conditions(data)
        return jsonify({
            'sensor_data': data,
            'yield_prediction': yield_prediction,
            'alerts': alerts
        })

api.add_resource(CropMonitor, '/monitor')

if __name__ == "__main__":
    app.run(debug=True)
