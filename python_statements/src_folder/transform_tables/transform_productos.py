from sqlalchemy import text
from python_statements.src_folder.config_folder.connection_engine import engine
from python_statements.src_folder.extract_tables.extract_productos_table import extraer_tabla_productos
import pandas as pd
import re
import os




def limpiar_tabla_productos(df: pd.DataFrame,) -> pd.DataFrame:  # Define la función de limpieza que recibe un DataFrame y retorna un DataFrame transformado.
    
    """Capa Silver: Limpieza de texto con Regex y estandarización de tipos de datos."""
    # 1. Crear copia independiente del DataFrame para evitar modificar la variable de origen
    df_silver = (df.copy())  # Genera una copia en memoria del DataFrame 'df' en la variable 'df_silver'.
    # 2. Estandarizar nombres de columnas a minúsculas y sin espacios: [list comprehension]
    df_silver.columns = [str(col).strip().lower() for col in df_silver.columns]  
    # Recorre cada encabezado, quita espacios en extremos con .strip() y convierte a minúsculas con .lower().


    # guardamos en columnas_texto los nombres de las columnas que sean tipo de datos: 'object' o string con: .select_dtypes
    # Revisa el esquema interno del DataFrame y conserva únicamente las columnas que coincidan con los tipos especificados en el parámetro 'include=[]'
    columnas_texto = df_silver.select_dtypes(include=['object', 'string']).columns
    # recorremos columnas_texto para transformar los nombres de columnas que sean 'object' o 'string', los cambiamos a texto y aplicamos la sustitución Regex para eliminar espacios en blanco
    for col in columnas_texto:
        df_silver[col] = (df_silver[col].astype(str).apply(lambda x: re.sub(r'\s+', ' ', x).strip()))

    if ('id_categoria' in df_silver.columns):  # Verifica existencia de 'id_categoria'.
        df_silver['id_categoria'] = df_silver['id_categoria'].astype(int)  # Fuerza el tipo de dato a entero (integer).
    if ('precio_base_producto' in df_silver.columns):  # Verifica existencia de 'precio_base_producto'.
        df_silver['precio_base_producto'] = df_silver['precio_base_producto'].astype(float)  # Convierte los precios a valores flotantes de precisión decimal (float).
    if ('fecha_creacion_producto' in df_silver.columns):  # Verifica existencia de 'fecha_creacion_producto'.
        df_silver['fecha_creacion_producto'] = pd.to_datetime(df_silver['fecha_creacion_producto'])  # Convierte la cadena a objeto de fecha estándar 'datetime64' de Pandas.
    return df_silver  # Devuelve el DataFrame procesado con las transformaciones aplicadas.



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
    # 1. Extracción (Capa Bronze)
    df_raw = extraer_tabla_productos(engine)
    # 2. Transformación y Limpieza (Capa Silver)
    df_clean = limpiar_tabla_productos(df_raw)
    # 3. Definir ruta local para almacenar el resultado
    ruta_parquet = r"E:\SQL_proyecto\parquet_files\productos_clean.parquet"
    # 4. Exportar a Parquet (Capa Silver / Staging Local)
    guardar_a_parquet_local(df_clean, ruta_parquet)

