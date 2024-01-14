from peewee import *
from models.vehicle import Vehicle
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.vehicle_specs import Vehicle_Specs as Specs
from models.status import Status
from models.model import Model
from models.engine import Engine
from models.brand import Brand

def get_dict(rows):
    output = []
    if rows.count() == 1:
        output.append(model_to_dict(rows[0]))
        return output
    
    for row in rows:
        output.append(model_to_dict(row))
    
    return output

def get_rand_vehicles():
    return get_dict(Vehicle.select().order_by(fn.Random()).limit(5))

def get_vehicle_by_id(plate_number):
    found_vehicle = Vehicle.select().where(Vehicle.plate_number == plate_number)
    if found_vehicle:
        return get_dict(found_vehicle)
    else:
        return "No vehicle found with that ID"

    

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


def insert_vehicle(new_vehicle, new_specs):
    new_engine = find_engine(new_specs['engine'])[0]
    if new_engine is None:
        new_engine = Engine.create(new_specs['engine'])
    
    Specs.insert(version = new_specs['version'], doors = new_specs['version'], seats = new_specs['seats'], height = new_specs['height'],
                width = new_specs['width'], length = new_specs['length'], axis_distance = new_specs['axis_distance'], )

    new_model = find_model(new_vehicle['model'])[0]
    if new_model is None:
        new_model = Model.create(new_vehicle['model'], new_vehicle['brand'])
    
def insert_model(new_vehicle):
    new_model = find_model(new_vehicle['model'])[0] if find_model(new_vehicle['model']) else None
    print(new_model)
    found_brand = get_dict(Brand.select().where(Brand.name == new_vehicle['brand']))[0]
    if new_model is None:
        new_model = Model.create(name=new_vehicle['model'], brand = found_brand['id_brand'])
    
    return new_model
    
        


def find_model(models):
    found_model = get_dict(Model.select().where(fn.Lower(Model.name) == fn.Lower(models)))
    
    return found_model

def find_engine(engine):
    found_engine = get_dict(Engine.select().where(fn.Lower(Engine.engine) == fn.Lower(engine)))

    return found_engine