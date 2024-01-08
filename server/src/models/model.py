from base_model import BaseModel
from peewee import *
from brand import Brand


class Model(BaseModel):
    id_model = AutoField()
    name = CharField()
    brand = ForeignKeyField(Brand, backref='brands')