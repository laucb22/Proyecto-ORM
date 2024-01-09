from models.base_model import BaseModel
from peewee import *


class Engine(BaseModel):
    id_engine = AutoField()
    engine = CharField()
