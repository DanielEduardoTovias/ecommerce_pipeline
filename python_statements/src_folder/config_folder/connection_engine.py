from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from pathlib import Path
# 1. Determina la ruta raíz del proyecto (3 niveles arriba de esta carpeta)
    # __file__ : variable interna de python aue guarda la ruta exacta del scriptque se ejecuta actualmente
    # resolve(): convierte la ruta en una ruta absoluta completa para no tener problemas con inconsistencias o simbolos del sistema operativo
    # .parents[3]: se posiciona tres niveles hacia arriba partiendo del archivo actual, 
    #Nivel 0 (Archivo): connection_engine.py
#Parent 0 (Carpeta actual): config_folder/
#Parent 1: src_folder/
#Parent 2: python_statements/
#Parent 3 (Raíz del proyecto): SQL_proyecto/       todo esto evita rutas fijas y manipulación dinámica en diferentes equipos y sistemas operativos en el futuro.
BASE_DIR = Path(__file__).resolve().parents[3]
ENV_PATH = BASE_DIR / "datos_acceso.env"  # / es de la libreria pathlib.Path une la ruta raíz con el archivo. adaptación automática de separadores según sea el sistema operativo.

# busca el archivo ".env" en la ruta de ejecución de la terminal actual
    # dotenv_path=ENV_PATH : fuerza a python-dotenv a leer el archivo de credenciales específico (datps_acceso.env)
    # directamente en la raízm sin importar desde qué directorio se ejecuta el comando en la consola.
load_dotenv(dotenv_path=ENV_PATH) # carga explícitamente el archivo .env para cuando se ejecute este script externamente.



# leemos los "Datos de acceso" cargados con load_dotenv
    # os.getenv("CLAVE") : extrae el valor asignado a cada clave desde las variables del sistema que acaba de cargar (load_doten()).
DB_USER = os.getenv("DB_USER") # El usuario que acabas de crear
DB_PASS = os.getenv("DB_PASS") # La contraseña que le asignaste
DB_HOST = os.getenv("DB_HOST") # IP pública de tu Droplet
DB_PORT = os.getenv("DB_PORT", "5432") # Puerto por defecto de PostgreSQL, "5432" actúa como fallback(respaldo), si la clav e DB_PORT no existe en el archivo ".env", asignará "5432" por defecto para prevenir nulos.
DB_NAME = os.getenv("DB_NAME") # Tu base de datos



# Construcción de la URL de conexión
# postgresql: (SGBD) a interactuar sqlalchemy
# +psycopg2: driver/adaptador de python a usar por sqlalchemy para traducir las consultas de python al protocolo nativo de postgresql.
# @: simboliza el "at" (en/alojado en). separa las credenciales de acceso de la dirección física del servidor.
# {DB_HOST}:{DB_PORT} (Ubicación en la red)
# ':' : Separador de puerto.
# {DB_PORT} : el puerto donde escucha postgresql en el servidor (por defecto 5432)
# /{DB_NAME} : (Destino), la barra '/' apunta a la base de datos específica dentro del servidor a la que deseas ingresar (e.g., ecommerce_ropa)
# f"..." : inyecta las variables leídas previamente sin tener que hacer cambios en el futuro si llegan a cambiar algunos datos de acceso.
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


