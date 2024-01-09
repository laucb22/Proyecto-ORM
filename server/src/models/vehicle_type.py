from models.base_model import BaseModel
from peewee import *


class Vehicle_Type(BaseModel):
    id_type = AutoField()
    vehicle_type = CharField()
