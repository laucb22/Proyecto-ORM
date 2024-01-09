from peewee import *
from models.brand import Brand

def get_brands():
    return Brand.select()