from peewee import *
from config.database import DB
from models import brand, engine, status, vehicle, vehicle_type, model, vehicle_specs

#
# Pre:---
# Post: Función inicial encargada de la creación de las tablas
#
def generate_tables():
    DB.connect()
    DB.create_tables([brand.Brand, engine.Engine, status.Status, model.Model, vehicle.Vehicle, vehicle_type.Vehicle_Type,
                    vehicle_specs.Vehicle_Specs])
    DB.close()


