from pyspark.sql import SparkSession

def sparkSession():       

    #Se crea la sesión spark    
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






    