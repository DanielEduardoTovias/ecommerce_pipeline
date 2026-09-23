from sqlalchemy_statements.config_folder.connection_engine import engine
import uuid
from datetime import datetime
from sqlalchemy import insert, Table, MetaData

metadata = MetaData()
productos = Table('productos', metadata, autoload_with=engine)

# Lista con un diccionario de un producto a insertar:
nuevos_productos = [
    {
        "id_producto": str(uuid.uuid4()),
        "name_producto": "Playera Oversize Negra",
        "descripcion_producto": "Playera 100% algodón de corte holgado",
        "id_categoria": 1,
        "precio_base_producto": 350.00,
        "fecha_creacion_producto": datetime.now(),
    }
]

with engine.begin() as conn:
    conn.execute(productos.insert(), nuevos_productos)
    if(len(nuevos_productos) == 1):
        print(
                f"¡Se insertó {len(nuevos_productos)} producto correctamente en la base de datos!")
    else:
        print(f"¡Se insertaron {len(nuevos_productos)} productos correctamente en la base de datos!")

    