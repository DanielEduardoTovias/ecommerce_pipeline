
from faker import Faker
import re
from unidecode import unidecode
import bcrypt

fake = Faker('es_MX')


def generate_id():
    return fake.uuid4()

def generate_phone():
     return "+52" + fake.numerify("##########")

def generate_password_hash():
    password = "Cliente123!".encode("utf-8")
    return bcrypt.hashpw(password, bcrypt.gensalt(rounds=12)).decode("utf-8")

def generate_fecha_registro():
    return fake.date_time()

def generate_name():
    r_names = fake.first_name()
    return r_names

def generate_apellido():
    r_apellido = fake.first_name()
    return r_apellido

def turn_to_email():
    #print(name)
    #print(apellido)
    email = generate_name().lower() +"_"+ generate_apellido().lower() +"@gmail.com"
    return unidecode(email)

def data_at_insert():

    nuevo_cliente = [{
        "id_cliente": generate_id(),
        "email": turn_to_email(),
        "nombre": generate_name(),
        "apellidos": generate_apellido(),
        "password_hash": generate_password_hash(),
        "telefono": generate_phone(),
        "fecha_registro": generate_fecha_registro()}]
    return nuevo_cliente




#if __name__ == "__main__":
    
    #print(data_at_insert())

