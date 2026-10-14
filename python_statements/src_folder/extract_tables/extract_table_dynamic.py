from sqlalchemy import text
from python_statements.src_folder.config_folder.connection_engine import engine
import pandas as pd

table_names = ['productos', 'variantes_producto', 'clientes']
#Este metodo recibe el engine como parámetro, contiene una query que extrae la tabla productos y con el engine hace una conexion a la base de datos y guarda esa informacion en df_productos y lo retorna
def extraer_tabla(table, engine):
    
    #query = text("SELECT * FROM {nombre_tabla}")
    #with engine.connect() as conn:
        #df_productos = pd.read_sql(query, conn) # pd.read_sql toma la consulta y la conexión, y REGRESA UN DATAFRAME
    return pd.read_sql_table(table, con=engine) # función de pandas para extraer una tabla completa sin filtros, ahorra escribir la consulta y conexión manualmente


if __name__ == "__main__":

    for table in table_names:
        df = extraer_tabla(table, engine)
        print("\n",df,"\n")