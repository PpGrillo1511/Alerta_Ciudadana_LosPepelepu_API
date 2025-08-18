"""Módulo principal para la API de Alerta Ciudadana"""

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.seeder.seeder import ejecutar_sp_generar_datos
from src.routes.usuario import usuario as usuario_router
from src.routes.comentario import comentario as comentario_router
from src.routes.incidente import incidente as incidente_router
from src.routes.categoria import categoria as categoria_router
from src.config.db import base, engine
from src.models import usuario, comentario, incidente, categoria
from ml_prioridad import procesar_incidentes
from ml_nl_prioridad import router as zonas_router

base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Alerta Ciudadana",
    description="API para el reporte y gestión de incidentes urbanos",
)

@app.get("/incidentes_prioridad")
def get_incidentes_prioridad():
    df = procesar_incidentes()
    return df.to_dict(orient="records")

@app.post("/generar-datos/")
def generar_datos(
    usuarios: int = Query(10, description="Cantidad de usuarios a generar"),
    incidentes: int = Query(20, description="Cantidad de incidentes a generar"),
    comentarios: int = Query(30, description="Cantidad de comentarios a generar")
):
    return ejecutar_sp_generar_datos(usuarios, incidentes, comentarios)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Bienvenido al Sistema de Alerta Ciudadana"}

app.include_router(usuario_router)
app.include_router(incidente_router)
app.include_router(comentario_router)
app.include_router(categoria_router)
app.include_router(zonas_router, prefix="/ml", tags=["Zonas Críticas"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
