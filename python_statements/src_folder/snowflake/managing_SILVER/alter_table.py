from snowflake.core.table import PrimaryKey, TableColumn
from python_statements.src_folder.snowflake.snow_up_data_stage import root


my_table = root.databases["ECOMMERCE"].schemas["SILVER_ECOMMERCE"].tables["productos"].fetch()


my_table_res = root.databases["ECOMMERCE"].schemas["SILVER_ECOMMERCE"].tables["productos"]

'''
table = my_table_res.fetch()

for column in table.columns:
    if column.name.upper() == "ID_PRODUCTO":
        column.datatype = "varchar"

my_table_res.create_or_alter(my_table)

print("DATA TYPE COLUMN MODIFIED SUCCESSFULLY")'''

my_table_res.drop()