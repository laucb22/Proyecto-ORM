import initialize as init
from flask import Flask
from flask import jsonify, request
import controllers.main_controller as mc

app = Flask(__name__)

@app.route("/")
def load_index():
    return mc.get_rand_vehicles()

@app.route("/getSpecs", methods=['POST'])
def get_specs():
    data = request.json
    specs_returned = mc.get_vehicle_specs(data['id'])
    return specs_returned

@app.route("/getStatus", methods = ['GET'])
def get_status():
    return mc.get_status_names()


if __name__ == "__main__":
    app()