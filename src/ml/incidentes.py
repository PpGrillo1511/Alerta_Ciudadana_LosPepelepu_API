from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.incidente import Incidente
from src.schemas.incidente import IncidenteCreate
from src.ml.predict import predict_categoria
from src.ml.llama import llama_predict

router = APIRouter()

@router.post("/incidentes/")
def crear_incidente(incidente: IncidenteCreate, db: Session = Depends(get_db)):
    
    categoria, confianza = predict_categoria(incidente.descripcion)

    if confianza < 0.6:
        categoria = llama_predict(incidente.descripcion)

    nuevo_incidente = Incidente(
        titulo=incidente.titulo,
        descripcion=incidente.descripcion,
        categoria=categoria,
        estado="pendiente"
    )

    db.add(nuevo_incidente)
    db.commit()
    db.refresh(nuevo_incidente)
    return nuevo_incidente
