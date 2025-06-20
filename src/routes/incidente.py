# src/routes/incidente.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import src.schemas.incidente as schemas
import src.models.incidente as models
import src.crud.incidentes as crud
from src.config.db import SesionLocal, engine
#from portadortoken import Portador

incidente = APIRouter()

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

@incidente.get(
    "/incidentes/",
    response_model=List[schemas.Incidente],
    tags=["Incidentes"],
    #dependencies=[Depends(Portador())]
)
async def read_incidentes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_incidentes(db=db, skip=skip, limit=limit)

@incidente.get(
    "/incidente/{id}",
    response_model=schemas.Incidente,
    tags=["Incidentes"],
    #dependencies=[Depends(Portador())]
)
async def read_incidente(id: int, db: Session = Depends(get_db)):
    incidente = crud.get_incidente(db=db, incidente_id=id)
    if incidente is None:
        raise HTTPException(status_code=404, detail="Incidente no encontrado")
    return incidente

@incidente.post(
    "/incidente/",
    response_model=schemas.Incidente,
    tags=["Incidentes"],
    #dependencies=[Depends(Portador())]
)
def create_incidente(incidente: schemas.IncidenteCreate, db: Session = Depends(get_db)):
    return crud.create_incidente(db=db, incidente=incidente)

@incidente.put(
    "/incidente/{id}",
    response_model=schemas.Incidente,
    tags=["Incidentes"],
    #dependencies=[Depends(Portador())]
)
async def update_incidente(id: int, incidente: schemas.IncidenteUpdate, db: Session = Depends(get_db)):
    db_incidente = crud.update_incidente(db=db, incidente_id=id, incidente=incidente)
    if db_incidente is None:
        raise HTTPException(status_code=404, detail="Incidente no existe, no actualizado")
    return db_incidente

@incidente.delete(
    "/incidente/{id}",
    response_model=schemas.Incidente,
    tags=["Incidentes"],
    #dependencies=[Depends(Portador())]
)
async def delete_incidente(id: int, db: Session = Depends(get_db)):
    db_incidente = crud.delete_incidente(db=db, incidente_id=id)
    if db_incidente is None:
        raise HTTPException(status_code=404, detail="Incidente no existe, no se pudo eliminar")
    return db_incidente
