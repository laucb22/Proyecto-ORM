from config import database
from peewee import *

#Módelo base para los metadatos de los demás modelos
class BaseModel(Model):
    class Meta:
        database = database.DB