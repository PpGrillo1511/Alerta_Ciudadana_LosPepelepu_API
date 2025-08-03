from sqlalchemy import text
from src.config.db import SesionLocal

def ejecutar_sp_generar_datos(usuarios: int, incidentes: int, comentarios: int):
    db = SesionLocal()
    try:
        db.execute(
            text("CALL sp_generar_datos_prueba(:u, :i, :c)"),
            {"u": usuarios, "i": incidentes, "c": comentarios}
        )
        db.commit()
        return {"mensaje": "✔ Datos generados exitosamente"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
