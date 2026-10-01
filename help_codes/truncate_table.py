from sqlalchemy import text

from python_statements.src_folder.config_folder.connection_engine import engine
with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE variantes_producto CASCADE;"))
    conn.commit()