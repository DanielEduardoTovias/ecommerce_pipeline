from sqlalchemy import text
from sqlalchemy_statements.config_folder.connection_engine import engine
import pandas as pd
import re

#Este metodo recibe el engine como parámetro, contiene una query que extrae la tabla productos y con el engine hace una conexion a la base de datos y guarda esa informacion en df_productos y lo retorna
def extraer_tabla_productos(engine) -> pd.DataFrame:

    query = text("SELECT * FROM productos")

    with engine.connect() as conn:
        df_productos = pd.read_sql(query, conn) # pd.read_sql toma la consulta y la conexión, y REGRESA UN DATAFRAME
    return df_productos


def limpiar_tabla_productos(df: pd.DataFrame) -> pd.DataFrame:

#1. Creamos una copia del DataFrame para trabajar sobre la copia
    df_silver = df.copy() 
#2. Estandarizar nombres de columnas, 
    df_silver.columns = [col.strip().lower for col in df_silver.columns] # Recorre cada nombre de columna, quita espacios al inicio/final (.strip()) y convierte todo a minúsculas (.lower()).
#3. Limpieza de texto con Regex en 'name_producto'
    df_silver['name_producto'] = ( # Selecciona la columna 'name_producto' para sobreescribirla con los datos limpios.
        df_silver['name_producto'] # Toma la columna actual.
        .astype(str) # Asegura que todos los datos de la columna sean de tipo texto (cadena de caracteres).
        .apply(lambda x: re.sub(r'\s+',' ', x).strip())) # Aplica una función a cada celda (x): 're.sub(r"\s+", " ", x)' reemplaza 1 o más espacios seguidos por 1 solo espacio, y '.strip()' elimina espacios sobrantes al inicio o final.

# 4. Limpieza de texto con Regex en 'descripcion_producto'
    df_silver['descripcion_producto'] = (  # Selecciona la columna 'descripcion_producto' para sobreescribirla.
        df_silver['descripcion_producto']  # Toma la columna actual.
        .astype(str)  # Convierte todos los valores a texto explícito.
        .apply(
            lambda x: re.sub(r'\s+', ' ', x).strip()
        )  # Aplica el mismo patrón Regex para eliminar dobles espacios internos y espacios en los extremos.
    )
# 5. Asegurar tipos de datos correctos para la Capa Silver
    df_silver['id_producto'] = df_silver['id_producto'].astype(str)  # Convierte la columna 'id_producto' (UUID) a tipo cadena de texto (string).

    df_silver['id_categoria'] = df_silver['id_categoria'].astype(int)  # Convierte la columna 'id_categoria' a entero puro (integer).

    df_silver['precio_base_producto'] = df_silver['precio_base_producto'].astype(float)  # Convierte la columna 'precio_base_producto' a número decimal (float).

    df_silver['fecha_creacion_producto'] = pd.to_datetime(df_silver['fecha_creacion_producto'])  # Convierte la columna de fecha a un objeto datetime oficial de Pandas.

    return df_silver  # Devuelve el DataFrame limpio y transformado listo para la siguiente etapa.

