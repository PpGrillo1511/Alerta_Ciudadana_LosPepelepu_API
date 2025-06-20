"""Módulo principal para la API de Alerta Ciudadana"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Rutas
from src.routes.usuario import usuario as usuario_router
from src.routes.comentario import comentario as comentario_router
from src.routes.incidente import incidente as incidente_router
from src.routes.categoria import categoria as categoria_router

# Configuración de base de datos
from src.config.db import base, engine

# Importación explícita de modelos (muy importante para crear las tablas)
from src.models import usuario, comentario, incidente, categoria

# Crear las tablas en la base de datos
base.metadata.create_all(bind=engine)

# Crear instancia de la app
app = FastAPI(
    title="Alerta Ciudadana",
    description="API para el reporte y gestión de incidentes urbanos",
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hello Word"}

# Incluir rutas
app.include_router(usuario_router)
app.include_router(incidente_router)
app.include_router(comentario_router)
app.include_router(categoria_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
