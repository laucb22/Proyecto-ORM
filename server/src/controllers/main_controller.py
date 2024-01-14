from peewee import *
from models.vehicle import Vehicle
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.vehicle_specs import Vehicle_Specs as Specs
from models.status import Status
from models.model import Model
from models.engine import Engine
from models.brand import Brand
from models.vehicle_type import Vehicle_Type as Vtype


def get_dict(rows):
    output = []
    if rows.count() == 1:
        output.append(model_to_dict(rows[0]))
        return output

    for row in rows:
        output.append(model_to_dict(row))

    return output

def get_all_vehicles():
    return get_dict(Vehicle.select())

def get_rand_vehicles():
    return get_dict(Vehicle.select().order_by(fn.Random()).limit(6))


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
    new_engine = (
        find_engine(new_specs["engine"])[0]
        if find_engine(new_specs["engine"])
        else None
    )
    if new_engine is None:
        Engine.create(engine=new_specs["engine"])
        new_engine = find_engine(new_specs["engine"])[0]

    created_specs = Specs.create(
        version=new_specs["version"],
        doors=new_specs["version"],
        seats=new_specs["seats"],
        height=new_specs["height"],
        width=new_specs["width"],
        length=new_specs["length"],
        axis_distance=new_specs["axis_distance"],
        tare=new_specs["tare"],
        gross_vehicle_weight_rating=new_specs["gross_vehicle_weight_rating"],
        tires="tires",
        engine=new_engine["id_engine"],
        max_potency=new_specs["max_potency"],
        wheel_drive=new_specs["wheel_drive"],
        urban_fuel_economy=new_specs["urban_fuel_economy"],
        extra_urban_fuel_economy=new_specs["extra_urban_fuel_economy"],
        overall_fuel_economy=new_specs["overall_fuel_economy"],
        addons=new_specs["addons"],
        notes=new_specs["notes"],
    )

    found_v_type = get_dict(
        Vtype.select().where(Vtype.vehicle_type == new_vehicle["vehicle_type"])
    )[0]
    found_brand = get_dict(Brand.select().where(Brand.name == new_vehicle["brand"]))[0]
    found_status = get_dict(
        Status.select().where(Status.status == new_vehicle["status"])
    )[0]

    new_model = (
        find_model(new_vehicle["model"])[0]
        if find_model(new_vehicle["model"])
        else None
    )
    if new_model is None:
        Model.create(name=new_vehicle["model"], brand=found_brand["id_brand"])
        new_model = find_model(new_vehicle["model"])[0]
    new_vehicle = Vehicle.create(
        plate_number=new_vehicle["plate_number"],
        vehicle_type=found_v_type["id_type"],
        color=new_vehicle["color"],
        price=new_vehicle["price"],
        status=found_status["id_status"],
        img_url=new_vehicle["img_url"],
        model=new_model["id_model"],
        specs=created_specs.id_specs,
    )

    if new_vehicle:
        return "Vehicle created"
    else:
        return "error creating vehicle"


def delete_vehicle(v_id):
    specs_to_delete = get_dict(
        Specs.select()
        .join(Vehicle)
        .where(Specs.id_specs == Vehicle.specs, Vehicle.plate_number == v_id)
    )[0]

    Vehicle.delete().where(Vehicle.plate_number == v_id).execute()
    Specs.delete().where(Specs.id_specs == specs_to_delete['id_specs']).execute()
    
    return "Vehicle deleted"


def find_model(models):
    found_model = get_dict(
        Model.select().where(fn.Lower(Model.name) == fn.Lower(models))
    )

    return found_model


def find_engine(engine):
    found_engine = get_dict(
        Engine.select().where(fn.Lower(Engine.engine) == fn.Lower(engine))
    )

    return found_engine

def get_brands():
    return get_dict(Brand.select())