from sqlalchemy import create_engine, text


# Datos de acceso
DB_USER = "danny_tovias"       # El usuario que acabas de crear
DB_PASS = "database7799"   # La contraseña que le asignaste
DB_HOST = "104.248.232.241"  # IP pública de tu Droplet
DB_PORT = "5432"                   # Puerto por defecto de PostgreSQL
DB_NAME = "ecommerce_ropa"       # Tu base de datos

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


