from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import src.schemas.comentario as schemas
import src.models.comentario as models
import src.models.usuario
import src.models.incidente
import src.crud.comentario as crud
from src.config.db import SesionLocal
# from portadortoken import Portador

comentario = APIRouter()

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

@comentario.get(
    "/comentarios/",
    response_model=List[schemas.Comentario],
    tags=["Comentarios"],
    # dependencies=[Depends(Portador())]
)
async def read_comentarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_comentarios(db=db, skip=skip, limit=limit)

@comentario.get(
    "/comentario/{id}",
    response_model=schemas.Comentario,
    tags=["Comentarios"],
    # dependencies=[Depends(Portador())]
)
async def read_comentario(id: int, db: Session = Depends(get_db)):
    comentario = crud.get_comentario(db=db, comentario_id=id)
    if comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no encontrado")
    return comentario

@comentario.post(
    "/comentario/",
    response_model=schemas.Comentario,
    tags=["Comentarios"],
    # dependencies=[Depends(Portador())]
)
def create_comentario(comentario: schemas.ComentarioCreate, db: Session = Depends(get_db)):
    return crud.create_comentario(db=db, comentario=comentario)

@comentario.put(
    "/comentario/{id}",
    response_model=schemas.Comentario,
    tags=["Comentarios"],
    # dependencies=[Depends(Portador())]
)
async def update_comentario(id: int, comentario: schemas.ComentarioUpdate, db: Session = Depends(get_db)):
    db_comentario = crud.update_comentario(db=db, comentario_id=id, comentario=comentario)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no existe, no actualizado")
    return db_comentario

@comentario.delete(
    "/comentario/{id}",
    response_model=schemas.Comentario,
    tags=["Comentarios"],
    # dependencies=[Depends(Portador())]
)
async def delete_comentario(id: int, db: Session = Depends(get_db)):
    db_comentario = crud.delete_comentario(db=db, comentario_id=id)
    if db_comentario is None:
        raise HTTPException(status_code=404, detail="Comentario no existe, no se pudo eliminar")
    return db_comentario
