from sqlalchemy import MetaData, Table
from python_statements.src_folder.config_folder.connection_engine import engine
from app_ecommerce.project.data_to.clients_to_insert import data_at_insert

metadata = MetaData()
clientes = Table('clientes', metadata, autoload_with=engine)


#print(new_client)
def insertingData():
    new_client = data_at_insert()
    with engine.begin() as conn:
        conn.execute(clientes.insert(), new_client)
        if(len(new_client) == 1):
            print(
                    f"¡Se insertó {len(new_client)} cliente correctamente en la base de datos!")
        else:
            print(f"¡Se insertaron {len(new_client)} clientes correctamente en la base de datos!")



