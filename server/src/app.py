import initialize as init
from flask import Flask
from flask import jsonify, request
import controllers.main_controller as mc
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/getAllVehicles")
def get_vehicles():
    return mc.get_all_vehicles()

@app.route("/")
def load_index():
    return mc.get_rand_vehicles()


@app.route("/getVehicleById/<plate_number>", methods=["GET"])
def get_vehicle(plate_number):
    return mc.get_vehicle_by_id(plate_number)



@app.route("/insertVehicle", methods=["POST"])
def new_vehicle():
    data = request.json

    new_specs = {
        "version": data["version"],
        "doors": data["doors"],
        "seats": data["seats"],
        "height": data["height"],
        "width": data["width"],
        "length": data["length"],
        "axis_distance": data["axis_distance"],
        "tare": data["tare"],
        "gross_vehicle_weight_rating": data["gross_vehicle_weight_rating"],
        "tires": data["tires"],
        "engine": data["engine"],
        "max_potency": data["max_potency"],
        "wheel_drive": data["wheel_drive"],
        "urban_fuel_economy": data["urban_fuel_economy"],
        "extra_urban_fuel_economy": data["extra_urban_fuel_economy"],
        "overall_fuel_economy": data["overall_fuel_economy"],
        "addons": data["addons"],
        "notes": data["notes"],
    }

    new_vehicle = {
        "plate_number": data["plate_number"],
        "vehicle_type": data["vehicle_type"],
        "color": data["color"],
        "price": data["price"],
        "status": data["status"],
        "img_url": data["img_url"],
        "model": data["model"],
        "brand": data["brand"],
    }

    return mc.insert_vehicle(new_vehicle, new_specs)


@app.route("/deleteVehicle", methods=["DELETE"])
def delete_vehicle():
    data = request.json
    print(data)
    return mc.delete_vehicle(data['number'])

@app.route("/getBrands", methods=['GET'])
def get_all_brands():
    return mc.get_brands()

@app.route("/getTypes", methods =['GET'])
def get_types():
    return mc.get_types()

@app.route("/getStatuses", methods = ['GET'])
def get_statuses():
    return mc.get_statuses()
if __name__ == "__main__":
    app()
