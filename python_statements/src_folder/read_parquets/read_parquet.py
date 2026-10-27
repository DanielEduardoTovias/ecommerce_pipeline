import pandas as pd

archivos = [
    "E:\SQL_proyecto\parquet_files\productos.parquet",
    "E:\SQL_proyecto\parquet_files\categorias.parquet",
    "E:\SQL_proyecto\parquet_files\clientes.parquet"
    

]

def reading(archivos):
    for archivo in archivos:
        df = pd.read_parquet(archivo)

        print("\n" + "=" * 50)
        print(archivo)
        print("=" * 50)

        return df.dtypes



if __name__ == "__main__":

    reading(archivos)
 