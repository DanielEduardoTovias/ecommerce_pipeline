import pandas as pd
import re

df = pd.DataFrame



def transform_to_int(df):
    columnas_enteros = df.select_dtypes(include='int').columns #seleccionar las columnas sean tipo int
    for i in columnas_enteros:
        df[i] = pd.to_numeric(df[i], downcast='integer') # downcast es para reducir el uso de memoria: int64 -> int8
    return df




def transform_to_string(df):

    #   -----  CODIGO OPTIMIZADO  -----
    #Separamos columnas '[fecha', 'date'] de columnas de ['texto'] esto debido a que vienen de los archivos .csv como string.
    # así que, cubrimos dos situaciones posibles con esta otra transformación aquí
    columnas_texto = df.select_dtypes(include=['object', 'string']).columns
    columnas_fecha = [col for col in columnas_texto if 'fecha' in col.lower() or 'date' in col.lower()]#recorremos
    columnas_solo_texto = [col for col in columnas_texto if col not in columnas_fecha] #recorremos de nuevo las columnas y verificamos que las columnas deseadas no estén en columnas_fecha

    # conversión a fechas la columna completa
    if columnas_fecha:
          df[columnas_fecha] = df[columnas_fecha].apply(pd.to_datetime)

    if columnas_solo_texto:
          for col in columnas_solo_texto:
                df[col] = (df[col].astype('string').str.replace(r'\s+', ' ', regex=True).str.strip())
                df[col] = df[col].replace(['nan','None', ''], pd.NA)
    return df

