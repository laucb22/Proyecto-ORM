from base_model import BaseModel
from peewee import * 

class Brand(BaseModel):
    id_brand = AutoField()
    name = CharField()
    country = CharField()
    founding_date = DateField()
    trademark_url = CharField()
