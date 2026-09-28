from sqlalchemy import text
from python_statements.src_folder.config_folder.connection_engine import engine
import pandas as pd
#query = text("SELECT * FROM productos WHERE precio_base_producto < 1000 AND precio_base_producto > 500")

#query = text("SELECT * FROM productos WHERE precio_base_producto BETWEEN 500 AND 1000")
#query = text("SELECT * FROM productos")
#query = text('SELECT * FROM clientes;')

''' #para ver los datos de la tabla:
with engine.connect() as connection:
    resultado = connection.execute(query)
    for fila in resultado:
        print(fila)


with engine.connect() as connection:
    resultado = pd.read_sql(query, connection)
    for fila in resultado:
        print(type(fila))
'''


#Este metodo recibe el engine como parámetro, contiene una query que extrae la tabla productos y con el engine hace una conexion a la base de datos y guarda esa informacion en df_productos y lo retorna
def extraer_tabla_productos(engine):
    query = text("SELECT * FROM productos")
    with engine.connect() as conn:
        df_productos = pd.read_sql(query, conn) # pd.read_sql toma la consulta y la conexión, y REGRESA UN DATAFRAME
    return df_productos

