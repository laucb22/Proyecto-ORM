from peewee import *
from models.vehicle import Vehicle
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.vehicle_specs import Vehicle_Specs as Specs
from models.status import Status


def get_dict(rows):
    output = []
    for row in rows:
        output.append(model_to_dict(row))

    return output


def get_rand_vehicles():
    return get_dict(Vehicle.select().order_by(fn.Random()).limit(5))


def get_vehicle_specs(id_to_search):
    specs = Specs.select().where(Specs.id_specs == id_to_search)

    if specs:
        return get_dict(specs)
    else:
        return "No specs found"


def get_status_names():
    statuses = Status.select(Status.status)

    if statuses:
        return get_dict(statuses)
    else:
        return "No statuses found"


def get_vehicle_by_id(plate_number):
    found_vehicle = Vehicle.select().where(Vehicle.plate_number == plate_number)
    if found_vehicle:
        return get_dict(found_vehicle)
    else:
        return "No vehicle found with that ID"
