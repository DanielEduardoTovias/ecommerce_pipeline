from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from pathlib import Path
# 1. Determina la ruta raíz del proyecto (3 niveles arriba de esta carpeta)
BASE_DIR = Path(__file__).resolve().parents[3]
ENV_PATH = BASE_DIR / "datos_acceso.env"

load_dotenv(dotenv_path=ENV_PATH) # carga explícitamente el archivo .env para cuando se ejecute este script externamente.

# Datos de acceso
DB_USER = os.getenv("DB_USER")      # El usuario que acabas de crear
DB_PASS = os.getenv("DB_PASS")   # La contraseña que le asignaste
DB_HOST = os.getenv("DB_HOST")  # IP pública de tu Droplet
DB_PORT = os.getenv("DB_PORT", "5432")                   # Puerto por defecto de PostgreSQL
DB_NAME = os.getenv("DB_NAME")      # Tu base de datos



# Construcción de la URL de conexión
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"



# Crear el motor (Engine)
engine = create_engine(DATABASE_URL)



#print("Iniciando prueba de conexión...")
try:
    with engine.connect() as connection:
        resultado = connection.execute(text("SELECT version();"))
        version = resultado.fetchone()
        print("¡CONEXIÓN EXITOSA A DIGITALOCEAN!")
        print(f"Versión de PostgreSQL: {version[0]}")
except Exception as e:
    print(f"\nError al conectar: {e}\n")


