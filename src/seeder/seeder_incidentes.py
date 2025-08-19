from sqlalchemy import text
from src.config.db import SesionLocal

def ejecutar_sp_insertar_incidentes_aleatorios(cantidad: int):
    db = SesionLocal()
    try:
        result = db.execute(
            text("CALL sp_insertar_incidentes_aleatorios(:cantidad)"),
            {"cantidad": cantidad}
        )

        mensaje = result.fetchall()

        db.commit()

        return {
            "mensaje": mensaje[0][0] if mensaje else f"✔ {cantidad} incidentes insertados exitosamente"
        }
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()