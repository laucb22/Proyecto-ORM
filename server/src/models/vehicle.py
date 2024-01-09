from models.base_model import BaseModel
from peewee import *
from models.status import Status
from models.model import Model
from models.vehicle_specs import Vehicle_Specs
from models.vehicle_type import Vehicle_Type


class Vehicle(BaseModel):
    id_car = AutoField()
    plate_number = CharField()
    vehicle_type = ForeignKeyField(Vehicle_Type, backref='types')
    color = CharField()
    price = DecimalField()
    status = ForeignKeyField(Status, backref='statuses')
    img_url = CharField()
    model = ForeignKeyField(Model, backref='models')
    specs = ForeignKeyField(Vehicle_Specs, backref='specs')


