import pandas as pd
from sqlalchemy_statements.config_folder.connection_engine import engine





tablas = [
    ("paqueterias", r"E:\SQL_proyecto\paqueterias.csv"),
    ("tipo_direccion", r"E:\SQL_proyecto\tipo_direccion.csv"),
    ("variantes_producto", r"E:\SQL_proyecto\variantes_producto.csv")
]

for tabla, archivo in tablas:
    df = pd.read_csv(archivo)
    df.to_sql(name=tabla, con=engine, if_exists="append", index=False, chunksize=1000)
    print(f"Tabla '{tabla}': {len(df)} registros insertados.")




