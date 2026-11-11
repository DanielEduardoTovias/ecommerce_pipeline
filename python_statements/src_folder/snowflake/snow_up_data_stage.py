from datetime import timedelta
import os
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col
from snowflake.core import Root, CreateMode
from snowflake.core.database import Database
from snowflake.core.schema import Schema
from snowflake.core.stage import Stage
from snowflake.core.table import Table, TableColumn, PrimaryKey
from snowflake.core.task import StoredProcedureCall, Task
from snowflake.core.task.dagv1 import DAGOperation, DAG, DAGTask
from snowflake.core.warehouse import Warehouse


session = Session.builder.config("connection_name", "default").create()
root = Root(session)
print(f"¡Conexión exitosa!")
print(f"Usuario: {session.get_current_user()}")
print(f"Rol: {session.get_current_role()}")
print(f"Base de datos: {session.get_current_database()}")
print(f"Esquema: {session.get_current_schema()}")
print(f"Warehouse: {session.get_current_warehouse()}")



from snowflake.core.stage import Stage, StageEncryption
# Creating a stage:
'''my_stage = Stage(
  name="my_stage",
  encryption=StageEncryption(type="SNOWFLAKE_SSE")
)

stages = root.databases["ECOMMERCE"].schemas["BRONZE_ECOMMERCE"].stages
stages.create(my_stage)
print("Schema al que apunta mi stage: ", stages.schema)
'''




def performStage():

  # Performing stage operations:
  my_stage_res = root.databases["ECOMMERCE"].schemas["BRONZE_ECOMMERCE"].stages["my_stage"]
  folder = r"E:\SQL_proyecto\parquet_files\curated_zone"

  # guardamos las rutas de los archivos parquet en una lista
  # en un for recorremos los archivos en la carpeta y si terminan en .parquet y si es un archivo los unimos las direcciones de la carpeta y el archivo
  archivos_parquet = [f for f in os.listdir(folder) if f.endswith(".parquet") and os.path.isfile(os.path.join(folder, f))]

  for archivo in archivos_parquet: # recorremos los archivos que guardamos en archivos_parquet
    #y volvemos a unirlos en las direcciones para pasar esas rutas completas para pasarlos al metodo put
    ruta_completa = os.path.join(folder, archivo)

    my_stage_res.put(
        ruta_completa, 
        "/", 
        auto_compress=False, 
        overwrite=True
    )



  stageFiles = root.databases["ECOMMERCE"].schemas["BRONZE_ECOMMERCE"].stages["my_stage"].list_files()
  for stageFile in stageFiles:
    print(stageFile)
  print(my_stage_res.fetch())


  if __name__ == "__main__":
    print("")
    performStage()