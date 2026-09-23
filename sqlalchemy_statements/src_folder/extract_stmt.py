from sqlalchemy import text
from sqlalchemy_statements.config_folder.connection_engine import engine

#query = text("SELECT * FROM productos WHERE precio_base_producto < 1000 AND precio_base_producto > 500")

#query = text("SELECT * FROM productos WHERE precio_base_producto BETWEEN 500 AND 1000")
query = text("SELECT * FROM direccion_cliente")
with engine.connect() as connection:
    resultado = connection.execute(query)
    for fila in resultado:
        print(fila)
