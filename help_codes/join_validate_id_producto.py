import pandas as pd
from sqlalchemy import text
from sqlalchemy_statements.config_folder.connection_engine import engine
# Sentencia SQL con el nombre de columna correcto (name_producto)
query = text("""
    SELECT 
        v.id_variante,
        p.name_producto,
        v.sku,
        v.talla,
        v.color,
        v.stock_disponible,
        v.precio_especifico
    FROM variantes_producto v
    JOIN productos p ON v.id_producto = p.id_producto
    LIMIT 10;
""")

with engine.connect() as connection:
    df = pd.read_sql(query, connection)

print(df)