from peewee import *
from models.vehicle import Vehicle
from playhouse.shortcuts import model_to_dict, dict_to_model
from models.vehicle_specs import Vehicle_Specs as Specs
from models.status import Status
from models.model import Model
from models.engine import Engine
from models.brand import Brand
from models.vehicle_type import Vehicle_Type as Vtype

#
# Pre:---
# Post: Recibe filas provenientes de resultados de sentencias SQL, lo convierte a un array de diccionarios y ldevuelve
# @params: rows
#
def get_dict(rows):
    output = []
    if rows.count() == 1:
        output.append(model_to_dict(rows[0]))
        return output

    for row in rows:
        output.append(model_to_dict(row))

    return output

#
# Pre:---
# Post: Función para obtener todos los vehículos de la BBDD
#
def get_all_vehicles():
    return get_dict(Vehicle.select())

#
# Pre:---
# Post: Función para obtener 6 vehículos aleatorios
#
def get_rand_vehicles():
    return get_dict(Vehicle.select().order_by(fn.Random()).limit(6))

#
# Pre:---
# Post: Función para buscar un vehículo según su matrícula
# @params: plate_number
#
def get_vehicle_by_id(plate_number):
    found_vehicle = Vehicle.select().where(Vehicle.plate_number == plate_number)
    if found_vehicle:
        return get_dict(found_vehicle)
    else:
        return "No vehicle found with that ID"

# Pre:---
# Post: Función para buscar los detalles de un vehículo según la id que conecta con la tabla de especificaciones.
# @params: plate_number
#
def get_vehicle_specs(id_to_search):
    specs = Specs.select().where(Specs.id_specs == id_to_search)

    if specs:
        return get_dict(specs)
    else:
        return "No specs found"

#
# Pre:---
# Post: Función para la inserción de un vehículo, recibe dos diccionarios con los datos para sus especificaciones y para los
# datos generales, se encarga de crear un motor o un modelo si no existen los introducidos por parámetro. Devuelve un mensaje
# informátivo indicando el resultado.
# @params new_vehicle, new_specs
#
def insert_vehicle(new_vehicle, new_specs):
    found_vehicle = (
        find_vehicle(new_vehicle['plate_number'])[0]
        if find_vehicle(new_vehicle['plate_number'])
        else None
    )
    if found_vehicle is not None:
        return "Vehicle already exists"
    
    new_engine = (
        find_engine(new_specs["engine"])[0]
        if find_engine(new_specs["engine"])
        else None
    )
    if new_engine is None:
        Engine.create(engine=new_specs["engine"])
        new_engine = find_engine(new_specs["engine"])[0]

    created_specs = Specs.create(
        version=new_specs["version"],
        doors=new_specs["version"],
        seats=new_specs["seats"],
        height=new_specs["height"],
        width=new_specs["width"],
        length=new_specs["length"],
        axis_distance=new_specs["axis_distance"],
        tare=new_specs["tare"],
        gross_vehicle_weight_rating=new_specs["gross_vehicle_weight_rating"],
        tires="tires",
        engine=new_engine["id_engine"],
        max_potency=new_specs["max_potency"],
        wheel_drive=new_specs["wheel_drive"],
        urban_fuel_economy=new_specs["urban_fuel_economy"],
        extra_urban_fuel_economy=new_specs["extra_urban_fuel_economy"],
        overall_fuel_economy=new_specs["overall_fuel_economy"],
        addons=new_specs["addons"],
        notes=new_specs["notes"],
    )

    found_v_type = get_dict(
        Vtype.select().where(Vtype.vehicle_type == new_vehicle["vehicle_type"])
    )[0]
    found_brand = get_dict(Brand.select().where(Brand.name == new_vehicle["brand"]))[0]
    found_status = get_dict(
        Status.select().where(Status.status == new_vehicle["status"])
    )[0]

    new_model = (
        find_model(new_vehicle["model"])[0]
        if find_model(new_vehicle["model"])
        else None
    )
    if new_model is None:
        Model.create(name=new_vehicle["model"], brand=found_brand["id_brand"])
        new_model = find_model(new_vehicle["model"])[0]
    new_vehicle = Vehicle.create(
        plate_number=new_vehicle["plate_number"],
        vehicle_type=found_v_type["id_type"],
        color=new_vehicle["color"],
        price=new_vehicle["price"],
        status=found_status["id_status"],
        img_url=new_vehicle["img_url"],
        model=new_model["id_model"],
        specs=created_specs.id_specs,
    )

    if new_vehicle:
        return "Vehicle created"
    else:
        return "Error creating vehicle"

#
# Pre:---
# Post: Método para el borrado de un vehículo por su matrícula, se encarga de borrar sus especificaciones primero.
# @params v_id
#
def delete_vehicle(v_id):
    specs_to_delete = get_dict(
        Specs.select()
        .join(Vehicle)
        .where(Specs.id_specs == Vehicle.specs, Vehicle.plate_number == v_id)
    )[0]

    Vehicle.delete().where(Vehicle.plate_number == v_id).execute()
    Specs.delete().where(Specs.id_specs == specs_to_delete['id_specs']).execute()
    
    return "Vehicle deleted"

#
# Pre:---
# Post: Método para buscar un modelo por su nombre
# @params: models
#
def find_model(models):
    found_model = get_dict(
        Model.select().where(fn.Lower(Model.name) == fn.Lower(models))
    )

    return found_model

#
# Pre:---
# Post: Método para buscar un motor por su nombre
# @params: engine
#
def find_engine(engine):
    found_engine = get_dict(
        Engine.select().where(fn.Lower(Engine.engine) == fn.Lower(engine))
    )

    return found_engine

#
# Pre:---
# Post: Método para obtener un vehículo según su matrícula
# @params: vehicle
#
def find_vehicle(vehicle):
    found_vehicle = get_dict(
        Vehicle.select().where(fn.Lower(Vehicle.plate_number) == fn.Lower(vehicle))
    )

    return found_vehicle
#
# Pre:---
# Post: Función para obtener todos las marcas de la BBDD
#
def get_brands():
    return get_dict(Brand.select())

#
# Pre:---
# Post: Función para obtener todos los tipos de vehículo de la BBDD
#
def get_types():
    return get_dict(Vtype.select())

#
# Pre:---
# Post: Función para obtener todos los estados de la BBDD
#
def get_statuses():
    return get_dict(Status.select())

#
# Pre:---
# Post: Función encargada de la edición de un vehículo. Mediante un parámetro de tipo diccionario, obtiene el vehículo a editar,
# y una vez encontrado, procede a actualizar los datos apropiados.
#
def edit_vehicle(data):
    v_plate_number = data['plate_number']
    new_color = data['color']
    new_price = data['price']
    found_status = get_dict(
        Status.select().where(Status.status == data['status'])
    )[0]

    Vehicle.update(price = new_price, color = new_color,
                    status = found_status['id_status']).where(Vehicle.plate_number == v_plate_number).execute()
    
    return "Vehicle updated"

#
# Pre:---
# Post: Método para filtrar la búsqueda de vehículos. Analiza la validéz de los filtros obtenidos por parámetro, 
# y dependiendo de ella realiza los filtros adecuados. Finalmente, devuelve un diccionario con los resultados.
# @params: filters
#
def filter_vehicles(filters):
    id_status = None
    id_type = None
    if "status" in filters:
        status_to_find = (
        get_dict(Status.select().where(Status.status == filters['status']))[0]
        if get_dict(Status.select().where(Status.status == filters['status']))
        else None
        )
        id_status = status_to_find['id_status']

    if "vehicle_type" in filters:
        type_to_find = (
        get_dict(Vtype.select().where(Vtype.vehicle_type == filters['vehicle_type']))[0]
        if get_dict(Vtype.select().where(Vtype.vehicle_type == filters['vehicle_type']))
        else None
        )
        id_type = type_to_find['id_type']
    
    if id_status and id_type:
        filtered_vehicles = get_dict(Vehicle.select().where(Vehicle.status == status_to_find['id_status'],
                                Vehicle.vehicle_type == type_to_find["id_type"]))
    elif id_status and id_type is None:
        filtered_vehicles = get_dict(Vehicle.select().where(Vehicle.status == status_to_find['id_status']))
    
    elif id_status is None and id_type:
        filtered_vehicles = get_dict(Vehicle.select().where(Vehicle.vehicle_type == type_to_find['id_type']))
    
    else: 
        filtered_vehicles = None
    if filtered_vehicles:
        return filtered_vehicles
    else:
        return "No vehicles found (lie)"

    



