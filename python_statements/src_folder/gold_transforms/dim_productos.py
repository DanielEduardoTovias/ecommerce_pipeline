from pathlib import Path
import pandas as pd

# 1. rutas dinámicas usando pathlib:
ROOT_DIR = Path(__file__).resolve().parents[3]
silver_dir = ROOT_DIR / "parquet_files" / "silver"
gold_dir = ROOT_DIR / "parquet_files" / "gold"
gold_dir.mkdir(parents=True, exist_ok=True)


print("-- Iniciando construcción Capa Gold de productos --")

# 2. leer tablas desde la capa silver:
df_productos = pd.read_parquet(silver_dir / "productos.parquet")
df_categorias = pd.read_parquet(silver_dir / "categorias.parquet")
df_variantes_producto = pd.read_parquet(silver_dir / "variantes_producto.parquet")


# 3. Merge y limpieza:
    #Merge(join style database): productos con categorias donde productos.id_categoria = categorias.id_categoria
df_producto_cat = df_productos.merge(df_categorias, on="id_categoria", how="left")

df_dim_productos = df_variantes_producto.merge(df_producto_cat, on="id_producto", how="left")


# 4. Guardamos la tabla dimensional en la capa gold:

output_path = gold_dir / "dim_productos.parquet"
df_dim_productos.to_parquet(output_path, index=False)

print("!!!  Archivo guardado con éxito en CAPA GOLD  !!!")
print(f"Registros Totales en dim_productos: {len(df_dim_productos)}")


