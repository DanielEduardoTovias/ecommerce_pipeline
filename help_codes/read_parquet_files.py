import pandas as pd  # Importa Pandas para leer la estructura de datos.

# 1. Leer el archivo Parquet indicando la ruta local
df_parquet = pd.read_parquet(
    r"E:\SQL_proyecto\parquet_files\productos_clean.parquet"
)  # Carga el archivo .parquet en un DataFrame de Pandas.

# 2. Imprimir la información de columnas y tipos de datos
print("=== INFORMACIÓN DEL ARCHIVO PARQUET ===")
print(
    df_parquet.info()
)  # Muestra los nombres de columnas, número de registros no nulos y tipos de datos conservados.

'''# 3. Mostrar las primeras filas en consola
print("\n=== VISTA PREVIA DE LOS DATOS ===")
print(
    df_parquet.head()
)  # Imprime en pantalla los primeros 5 registros cargados del archivo .parquet.'''