from sqlalchemy import text
from src.config.db import SesionLocal
import random

# Posibles valores de prioridad
PRIORIDADES = ["Alta", "Media", "Baja"]

def ejecutar_sp_generar_datos(usuarios: int, incidentes: int, comentarios: int):
    db = SesionLocal()
    try:
        # Ejecuta tu procedimiento para generar datos
        db.execute(
            text("CALL sp_generar_datos_prueba(:u, :i, :c)"),
            {"u": usuarios, "i": incidentes, "c": comentarios}
        )
        db.commit()

        # 🔹 Asignar prioridad aleatoria a los incidentes generados
        incidentes_query = db.execute(text("SELECT id FROM incidentes")).fetchall()
        for row in incidentes_query:
            prioridad = random.choice(PRIORIDADES)
            db.execute(
                text("UPDATE incidentes SET prioridad = :p WHERE id = :id"),
                {"p": prioridad, "id": row.id}
            )
        db.commit()

        return {"mensaje": "✔ Datos generados exitosamente con prioridad"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}
    finally:
        db.close()
