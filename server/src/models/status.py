from models.base_model import BaseModel
from peewee import *


class Status(BaseModel):
    id_status = AutoField()
    status = CharField()