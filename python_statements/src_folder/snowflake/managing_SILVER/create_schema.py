from snowflake.core.schema import Schema
from python_statements.src_folder.snowflake.snow_up_data_stage import root

silver_schema = Schema(name="SILVER_ECOMMERCE")
root.databases["ECOMMERCE"].schemas.create(silver_schema)
print("SCHEMA SILVER CREATED SUCCESSFULLY!!!")

silver_schema = root.databases["ECOMMERCE"].schemas["SILVER_ECOMMERCE"].fetch()
print("INFORMATION ABOUT THE SCHEMA: ", silver_schema.to_dict())
