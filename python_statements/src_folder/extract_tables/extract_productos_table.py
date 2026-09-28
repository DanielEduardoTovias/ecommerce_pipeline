from sqlalchemy import text
from python_statements.src_folder.config_folder.connection_engine import engine
import pandas as pd


#Este metodo recibe el engine como parámetro, contiene una query que extrae la tabla productos y con el engine hace una conexion a la base de datos y guarda esa informacion en df_productos y lo retorna
def extraer_tabla_productos(engine):
    query = text("SELECT * FROM productos")
    with engine.connect() as conn:
        df_productos = pd.read_sql(query, conn) # pd.read_sql toma la consulta y la conexión, y REGRESA UN DATAFRAME
    return df_productos


if __name__ == "__main__":

    df = extraer_tabla_productos(engine)

    print(df)