from pathlib import Path

from sqlalchemy import text
from python_statements.src_folder.config_folder.connection_engine import engine
from python_statements.src_folder.extract_tables.extract_table import extraer_tabla
from python_statements.src_folder.transform_tables.datatypes_transform.to_datatype import transform_to_int
from python_statements.src_folder.transform_tables.datatypes_transform.to_datatype import transform_to_string

import pandas as pd
import re
import os




#table_names = ['productos', 'variantes_producto', 'clientes', 'direccion_cliente', 'paqueterias', 'categorias', 'tipo_direccion']
table_names = ['clientes']

def limpiar_tablas(df: pd.DataFrame,) -> pd.DataFrame:  # Define la función de limpieza que recibe un DataFrame y retorna un DataFrame transformado.
    
    #   ------ Limpieza de texto con Regex y estandarización de tipos de datos.
    # 1. Crear copia independiente del DataFrame para evitar modificar la variable de origen
    df_silver = (df.copy())  # Genera una copia en memoria del DataFrame 'df' en la variable 'df_silver'.
    # 2. Estandarizar nombres de columnas a minúsculas y sin espacios: [list comprehension]
    df_silver.columns = [str(col).strip().lower() for col in df_silver.columns]   # Recorre cada encabezado, quita espacios en extremos con .strip() y convierte a minúsculas con .lower().
    transform_to_string(df_silver)
    transform_to_int(df_silver)
    
    return df_silver




# ---------- exportar ese df_silver limpio a un archivo en formato Parquet (.parquet) ----------
def guardar_a_parquet_local( df: pd.DataFrame, ruta_destino: str) -> None:

    #1. Obtener el direcotorio superior de la ruta destino
    directorio = os.path.dirname(ruta_destino)
    #2. Crear la carpeta si no existe
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio)
    #3. Guardar el DataFrame como archivo Parquet
    df.to_parquet(ruta_destino, index=False) # Exporta los datos a formato .parquet. 'index=False' evita que se guarde el número de índice de Pandas como una columna extra.
    print(f"Archivo guardado en: {ruta_destino}")




# -------------------- Ejecución del flujo completo --------------------

if __name__ == "__main__":

    carpeta_parquet = Path("E:\SQL_proyecto\parquet_files")
    for table in table_names:
    # 1. Extracción (Capa Bronze)
        df_raw = extraer_tabla(engine, table)
    # 2. Transformación y Limpieza (Capa Silver)
        df_clean = limpiar_tablas(df_raw)
    # 3. Definir ruta local para almacenar el resultado
        
        ruta_parquet = carpeta_parquet / f"{table}.parquet"
    # 4. Exportar a Parquet (Capa Silver / Staging Local)
        guardar_a_parquet_local(df_clean, ruta_parquet)


        # optional, read datatypes of the parquet files:
        