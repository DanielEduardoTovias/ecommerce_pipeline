from python_statements.src_folder.snowflake.snow_up_data_stage import root
from python_statements.src_folder.snowflake.managing_SILVER.table_objects.tables_to_create import *

table_objects = [variantes_producto, clientes, pedidos, lineas_pedido, direccion_cliente, paqueterias, pago, categorias, tipo_direccion]

def creatingTables():

  for table in table_objects:
    root.databases["ECOMMERCE"].schemas["SILVER_ECOMMERCE"].tables.create(table)
    print("TABLE ", table, " CREATED SUCCESSFULLY!!!")



if __name__ == "__main__":

    creatingTables()