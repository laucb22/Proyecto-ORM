from config import database
from peewee import *


class BaseModel(Model):
    class Meta:
        database = database.DB