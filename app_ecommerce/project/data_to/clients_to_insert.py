
from datetime import datetime

from faker import Faker
import re
from unidecode import unidecode
import bcrypt

fake = Faker('es_MX')


def generate_id():
    return fake.uuid4()

def generate_phone():
     return "52" + fake.numerify("##########")

def generate_password_hash():
    password = "Cliente123!".encode("utf-8")
    return bcrypt.hashpw(password, bcrypt.gensalt(rounds=12)).decode("utf-8")

def generate_fecha_registro():
    return fake.date_time_between(start_date=datetime(2023, 1, 1), end_date=datetime.now())

def email_and_user():
    name = fake.first_name().split()[0]
    lastN = fake.last_name()

    #limpiamos nombre y apellido:
    name_clean = unidecode(name).lower()
    lastN_clean = unidecode(lastN).lower()
    lastN_clean = re.sub(r'\s+', '_', lastN_clean)
    #armamos el email con datos limpios:
    email = name_clean +"_"+ lastN_clean + "@gmail.com"
    
    return [name, lastN, email]
    

def data_at_insert():

    user_info = email_and_user()

    email = user_info[2]
    nombre = user_info[0]
    apellidos = user_info[1]

    nuevo_cliente = [{
        "id_cliente": generate_id(),
        "email": email,
        "nombre": nombre,
        "apellidos": apellidos,
        "password_hash": generate_password_hash(),
        "telefono": generate_phone(),
        "fecha_registro": generate_fecha_registro()}]
    return nuevo_cliente




if __name__ == "__main__":
    
    print(data_at_insert())

