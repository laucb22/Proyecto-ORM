from base_model import BaseModel
from peewee import *
from vehicle_type import Vehicle_Type
from engine import Engine

class Technical_Specs(BaseModel):
    id_specs = AutoField()
    version = CharField()
    vehicle_type = ForeignKeyField(Vehicle_Type, backref='types')
    model = ForeignKeyField(Model, backref='models')
    doors = IntegerField()
    seats = IntegerField()
    height = IntegerField()
    width = IntegerField()
    length = IntegerField()
    axis_distance = IntegerField()
    tare = DecimalField()
    gross_vehicle_weight_rating = DecimalField()
    tires = CharField()
    engine = ForeignKeyField(Engine, backref='engines')
    max_potency = DecimalField()
    wheel_drive = CharField()
    urban_fuel_economy = DecimalField()
    extra_urban_fuel_economy = DecimalField()
    overall_fuel_economy = DecimalField()
    addons = CharField()
    notes = CharField() 
