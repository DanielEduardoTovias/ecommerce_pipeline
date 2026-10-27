import os
from pathlib import Path
import tempfile
from pyspark.sql import SparkSession

# --- PARCHE PARA WINDOWS (Evita buscar winutils.exe) ---



def sparkSession():    
    # Crear la estructura de binarios simulada para calmar a Hadoop en Windows
    #hadoop_temp_dir = Path(tempfile.gettempdir()) / "hadoop_local"
    #bin_dir = hadoop_temp_dir / "bin"
    #bin_dir.mkdir(parents=True, exist_ok=True)
    #os.environ["HADOOP_HOME"] = str(hadoop_temp_dir)
    #os.environ["hadoop.home.dir"] = str(hadoop_temp_dir)    
    
    spark = SparkSession.builder \
        .appName("First_Session") \
        .master("local[*]") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()


        #   --- información de la conexión: ---
    print("--- Spark Session Iniciada Correctamente ---")
    print(f"Versión de Spark: {spark.version}")
    print(f"Nombre de la App: {spark.sparkContext.appName}")
    print(f"Master configurado: {spark.sparkContext.master}")
    return spark





    #   .appName("") define el nomber de la aplicación, este nombre aparece en la UI de Spark cuando se esté ejecutando
    #   .master("") define el entorno de ejecución (dónde va a correr Spark)
        #   "local" corre en un solo núcleo de la PC
        #   "local[4]" corre usando exactamente 4 núcleos de la pc
        #   "local[*]" indica a Spark que use todos los núcleos disponibles del procesador de la pc
    #   .config(key, value) permite inyectar configuraciones avanzadas de Spark (ej: manejo de memoria, zonas horarias, configuraciones de conexión a S3/Snowflake, etc.)
    # .getOrCreate() es el método que ejecuta la creación. Si ya existe una SparkSession activa en el proceso de Python actual, la recupera; si no existe ninguna, crea una nueva.






    