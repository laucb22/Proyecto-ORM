from base_model import BaseModel
from peewee import *
from status import Status


class Vehicle(BaseModel):
    id_car = AutoField()
    plate_number = CharField()
    color = CharField()
    price = DecimalField()
    status = ForeignKeyField(Status, backref='statuses')
    img_url = CharField()


