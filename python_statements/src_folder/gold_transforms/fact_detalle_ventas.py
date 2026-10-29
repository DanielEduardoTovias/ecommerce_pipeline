from pathlib import Path
import pandas as pd
from required_columns import columnas_fact

# 1. rutas dinámicas usando pathlib:
ROOT_DIR = Path(__file__).resolve().parents[3]
silver_dir = ROOT_DIR / "parquet_files" / "silver"
gold_dir = ROOT_DIR / "parquet_files" / "gold"
gold_dir.mkdir(parents=True, exist_ok=True)


print("-- Iniciando construcción Capa Gold de Tabla de Hechos (fact_detalle_ventas) --")

# 2. leer tablas desde la capa silver:
df_lineas_pedido = pd.read_parquet(silver_dir / "lineas_pedido.parquet")
df_pedidos = pd.read_parquet(silver_dir / "pedidos.parquet")
df_pago = pd.read_parquet(silver_dir / "pago.parquet")


# 3. Merges:
df_lineas_merge_pedidos = df_lineas_pedido.merge(df_pedidos, on="id_pedido", how="left")
df_fact_detalles_ventas = df_lineas_merge_pedidos.merge(df_pago, on="id_pedido", how="left")

# 4. Filtramos el dataFrame con las columnas necesarias:
df_fact_detalles_ventas = df_fact_detalles_ventas[columnas_fact]

# 5. Guardamos en la capa Gold la tabla de hechos resultante:
output_path = gold_dir / "fact_detalle_ventas.parquet"
df_fact_detalles_ventas.to_parquet(output_path, index=False)

print("!!! Archivo guardado con éxito en CAPA GOLD !!!")
print(f"Registros Totales en fact_detalle_ventas: {len(df_fact_detalles_ventas)}")