from pathlib import Path
import string
from python_statements.src_folder.config_folder.connection_engine import engine
import pandas as pd

table_names = ['productos', 'variantes_producto', 'clientes', 'direccion_cliente', 'paqueterias', 'categorias', 'tipo_direccion']
def extraer_tabla(engine, nombre_tabla):
    #query = text("SELECT * FROM {nombre_tabla}")
    #with engine.connect() as conn:
        #df_productos = pd.read_sql(query, conn) # pd.read_sql toma la consulta y la conexión, y REGRESA UN DATAFRAME
    return pd.read_sql_table(nombre_tabla, con=engine) # función de pandas para extraer una tabla completa sin filtros, ahorra escribir la consulta y conexión manualmente

if __name__ == "__main__":
    ROOT_DIR = Path(__file__).resolve().parents[3]
    carpeta_bronze = ROOT_DIR / "parquet_files"
    
    for table in table_names:
        print(f"Extrayendo {table} de la BD a Bronze...")
        
        # 1. Extraer crudo de Postgres con Pandas (o SQLAlchemy)
        df_raw = extraer_tabla(engine, table)


        #   ----------
        # Convertimos las columnas de tipo 'object' (texto, UUIDs, etc.) a string estándar
        for col in df_raw.select_dtypes(include=['object']).columns:
            df_raw[col] = df_raw[col].astype(str)
        # -------------------------------------



        
        # 2. Definir ruta Bronze
        ruta_bronze = carpeta_bronze / f"{table}.parquet"
        
        # 3. Guardar crudo en Parquet sin transformar
        df_raw.to_parquet(ruta_bronze, index=False)
        print(f"-> Guardado en Bronze: {ruta_bronze}")

