import initialize as init
from flask import Flask
from flask import jsonify, request
import controllers.main_controller as mc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def load_index():
    return mc.get_rand_vehicles()


@app.route("/getSpecs", methods=["POST"])
def get_specs():
    data = request.json
    specs_returned = mc.get_vehicle_specs(data["id"])
    return specs_returned


@app.route("/getStatus", methods=["GET"])
def get_status():
    return mc.get_status_names()


@app.route("/getVehicleById/<plate_number>", methods=["GET"])
def get_vehicle(plate_number):
    return mc.get_vehicle_by_id(plate_number)


if __name__ == "__main__":
    app()
