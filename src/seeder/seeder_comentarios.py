from sqlalchemy import text
from src.config.db import SesionLocal

def ejecutar_sp_insertar_comentarios_aleatorios(cantidad: int):
    db = SesionLocal()
    try:
        db.execute(
            text("CALL sp_insertar_comentarios_aleatorios(:cantidad)"),
            {"cantidad": cantidad}
        )
        
        db.commit()

        return {"mensaje": f"✔ {cantidad} comentarios insertados exitosamente"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()