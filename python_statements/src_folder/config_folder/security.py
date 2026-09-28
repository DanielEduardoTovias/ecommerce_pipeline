from sqlalchemy import text
from python_statements.src_folder.config_folder.connection_engine import engine

def change_pass(engine, user: str, new_pass: str):
    
    query = text(f"ALTER USER {user} WITH PASSWORD :new_pass;")

    try:
        with engine.begin() as conn:
            #PendingDeprecationWarning
            conn.execute(query, {"new_pass": new_pass})
            print(f"Contraseña actualizada con éxito para '{user}'")
    except Exception as e:
        print(e)
        print(f"Error al cambiar la contraseña")


if __name__ == "__main__":
    # Sustituye por tu nueva contraseña deseada
    NUEVA_CONTRASEÑA = ""
    
    change_pass(engine, "danny_tovias", NUEVA_CONTRASEÑA) 