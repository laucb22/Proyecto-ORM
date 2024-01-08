from peewee import *
from config.database import DB
from models import brand, engine, model, status, technical_specs, vehicle, vehicle_type

def generate_tables():
    DB.connect()
    DB.create_tables([brand.Brand, engine.Engine, status.Status, model.Model, vehicle.Vehicle, vehicle_type.Vehicle_Type,
                    technical_specs.Technical_Specs])
    DB.close()
