from pyspark.sql import functions as F  # funciones de pyspark SQL
from pyspark.sql.types import IntegerType, LongType
from pyspark.sql.types import StringType, TimestampType


def transform_to_int_pyspark(df):
    # En Spark, obtenemos las columnas cuyo tipo sea entero (int, bigint, etc.)
    columnas_enteros = [
        col_name for col_name, data_type in df.dtypes 
        if data_type in ("int", "bigint", "smallint", "tinyint")
    ]
    
    for col_name in columnas_enteros:
        # Casteamos de forma segura a entero
        df = df.withColumn(col_name, F.col(col_name).cast(IntegerType()))
        
    return df


def transform_to_string_pyspark(df):
    # Identificar columnas de texto/string en Spark
    columnas_texto = [
        col_name for col_name, data_type in df.dtypes 
        if data_type == "string"
    ]
    
    # Separar por nombre (si contienen 'fecha' o 'date')
    columnas_fecha = [col for col in columnas_texto if 'fecha' in col.lower() or 'date' in col.lower()]
    columnas_solo_texto = [col for col in columnas_texto if col not in columnas_fecha]
    
    # 1. Conversión de fechas
    for col_name in columnas_fecha:
        df = df.withColumn(col_name, F.to_timestamp(F.col(col_name)))
        
    # 2. Limpieza de texto (reemplazar espacios múltiples, trim, y vacíos a null)
    for col_name in columnas_solo_texto:
        df = df.withColumn(
            col_name, 
            F.when(
                F.col(col_name).isin("nan", "None", "", "NULL"), None
            ).otherwise(
                F.trim(F.regexp_replace(F.col(col_name), r'\s+', ' '))
            ).cast(StringType())
        )
        
    return df