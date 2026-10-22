from fastapi import FastAPI
from app_ecommerce.project.data_to.table_to_insert import insertingData
app = FastAPI()




@app.post("/clientes/")
def insertar_nuevo_cliente():
  print("begin data insertion")
  insertingData()
  print("data insertion ended!")
  


