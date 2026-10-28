from pathlib import Path
import pandas as pd

# 1. rutas dinámicas usando pathlib:
ROOT_DIR = Path(__file__).resolve().parents[3]
silver_dir = ROOT_DIR / "parquet_files" / "silver"
gold_dir = ROOT_DIR / "parquet_files" / "gold"
gold_dir.mkdir(parents=True, exist_ok=True)

print("-- Iniciando construcción Capa Gold --")

#2. leer tablas desde la capa silver:
df_clientes = pd.read_parquet(silver_dir / "clientes.parquet")
df_direcciones = pd.read_parquet(silver_dir / "direccion_cliente.parquet")
df_tipos_dir = pd.read_parquet(silver_dir / "tipo_direccion.parquet")



    #Descartamos columnas innecesarias (datos privados, sensibles, etc.) se debe hacer antes del merge
df_clientes = df_clientes.drop(columns=["password_hash"], errors="ignore")


#3. Merge y limpieza:
    #Merge(join style database): direcciones con tipo_direccion
df_dir_completa = df_direcciones.merge(df_tipos_dir, on="id_tipo_direccion", how="left")

#   ----- ESTA SERA UNA DE LAS TABLAS DEL MODELO DIMENSIONAL EN ESTRELLA -----
#Merge df_dir_completa con clientes para crear la tabla dimensional de clientes:
df_dim_clientes = df_clientes.merge(df_dir_completa, on="id_cliente", how="left")


#5. Eliminamos clientes duplicados:
df_dim_clientes = df_dim_clientes.drop_duplicates(subset=["id_cliente"])

#6. Guardamos la tabla dimensional en la capa gold:
output_path = gold_dir / "dim_clientes.parquet"
df_dim_clientes.to_parquet(output_path, index=False)

print("!!!  Archivo guardado con éxito en CAPA GOLD  !!!")
print(f"Registros Totales en dim_clientes: {len(df_dim_clientes)}")


# Muestra el conteo de nulos por columna en la consola
print(df_dim_clientes.isnull().sum())

# Opcional: ver filas específicas que contengan al menos un nulo
print(df_dim_clientes[df_dim_clientes.isnull().any(axis=1)].head())