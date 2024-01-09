from models.base_model import BaseModel
from peewee import *
from models.brand import Brand


class Model(BaseModel):
    id_model = AutoField()
    name = CharField()
    brand = ForeignKeyField(Brand, backref='brands')