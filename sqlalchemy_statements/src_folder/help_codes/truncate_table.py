from sqlalchemy import text

from sqlalchemy_statements.config_folder.connection_engine import engine
with engine.connect() as conn:
    conn.execute(text("TRUNCATE TABLE variantes_producto CASCADE;"))
    conn.commit()