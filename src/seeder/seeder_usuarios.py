from sqlalchemy import text
from src.config.db import SesionLocal

def ejecutar_sp_crear_usuarios_aleatorios(cantidad_usuarios: int):
    db = SesionLocal()
    try:
        # 🔹 Ejecuta el procedimiento almacenado
        db.execute(
            text("CALL sp_crear_usuarios_aleatorios(:cantidad)"),
            {"cantidad": cantidad_usuarios}
        )
        db.commit()

        return {"mensaje": f"✔ {cantidad_usuarios} usuarios generados exitosamente"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()