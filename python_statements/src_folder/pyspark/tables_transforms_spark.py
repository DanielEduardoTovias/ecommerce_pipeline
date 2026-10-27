from pathlib import Path
from python_statements.src_folder.pyspark.spark_session import sparkSession
from python_statements.src_folder.pyspark.datatype_transform_spark.to_datatype_spark import transform_to_int_pyspark
from python_statements.src_folder.pyspark.datatype_transform_spark.to_datatype_spark import transform_to_string_pyspark

table_names = ['productos', 'variantes_producto', 'clientes', 'direccion_cliente', 'paqueterias', 'categorias', 'tipo_direccion']

def limpiar_tablas_pyspark(df):
    # Aplicar transformaciones modulares
    df = transform_to_int_pyspark(df)
    df = transform_to_string_pyspark(df)
    return df

if __name__ == "__main__":
    
    # 1. Iniciar sesión con tu función modular
    spark = sparkSession()
    
    # Definir rutas usando Path de Python (con r"" para evitar problemas con las barras invertidas)
    ROOT_DIR = Path(__file__).resolve().parents[3]
    carpeta_bronze = ROOT_DIR / "parquet_files"
    carpeta_silver = ROOT_DIR / "parquet_files" / "silver"
    
    # Asegurar que la carpeta silver exista
    carpeta_silver.mkdir(parents=True, exist_ok=True)
    
    for table in table_names:
        try:

            print(f"\nProcesando tabla: {table}")
            
            # 1. Extracción (Capa Bronze): Apuntar a la ruta completa del archivo Parquet crudo
            ruta_bronze = str(carpeta_bronze / f"{table}.parquet")
            df_raw = spark.read.parquet(ruta_bronze)
            
            # 2. Transformación y Limpieza (Capa Silver)
            df_clean = limpiar_tablas_pyspark(df_raw)
            
            # 3. Definir ruta local para almacenar el resultado en Silver
            ruta_silver = str(carpeta_silver / f"{table}.parquet")
            
            # 4. Exportar a Parquet (Capa Silver)
            
            df_clean.toPandas().to_parquet(ruta_silver, index=False)
            print(f"-> Guardado exitoso en Silver: {ruta_silver}")
        except Exception as e:
            print(f"ERROR procesando la tabla '{table}': {str(e)}")
            continue
    # 5. Se detiene la conexión FUERA del bucle for
        
spark.stop()
print("\n--- Spark Session Cerrada ---")