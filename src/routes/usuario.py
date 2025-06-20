# src/routes/usuario.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import src.schemas.usuario as schemas
import src.models.usuario as models
import src.crud.usuario as crud
from src.config.db import SesionLocal, engine
#from portadortoken import Portador

usuario = APIRouter()

models.base.metadata.create_all(bind=engine)

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

@usuario.get(
    "/usuarios/",
    response_model=List[schemas.Usuario],
    tags=["Usuarios"],
    #dependencies=[Depends(Portador())]
)
async def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_usuarios(db=db, skip=skip, limit=limit)

@usuario.get(
    "/usuario/{id}",
    response_model=schemas.Usuario,
    tags=["Usuarios"],
    #dependencies=[Depends(Portador())]
)
async def read_usuario(id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db=db, usuario_id=id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@usuario.post(
    "/usuario/",
    response_model=schemas.Usuario,
    tags=["Usuarios"],
    #dependencies=[Depends(Portador())]
)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db=db, usuario=usuario)

@usuario.put(
    "/usuario/{id}",
    response_model=schemas.Usuario,
    tags=["Usuarios"],
    #dependencies=[Depends(Portador())]
)
async def update_usuario(id: int, usuario: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    db_usuario = crud.update_usuario(db=db, usuario_id=id, usuario=usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_usuario

@usuario.delete(
    "/usuario/{id}",
    response_model=schemas.Usuario,
    tags=["Usuarios"],
    #dependencies=[Depends(Portador())]
)
async def delete_usuario(id: int, db: Session = Depends(get_db)):
    db_usuario = crud.delete_usuario(db=db, usuario_id=id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_usuario
