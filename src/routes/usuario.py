# src/routes/usuario.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas.usuario import UsuarioRegister, UsuarioLogin
import src.schemas.usuario as schemas
import src.models.usuario as models
import src.crud.usuario as crud
from src.config.db import SesionLocal, engine
from portadortoken import Portador
from passlib.hash import bcrypt
from src.utils.jwt_utils import solicita_token

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
    dependencies=[Depends(Portador())]
)
async def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_usuarios(db=db, skip=skip, limit=limit)

@usuario.get(
    "/usuario/{id}",
    response_model=schemas.Usuario,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())]
)
async def read_usuario(id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db=db, usuario_id=id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@usuario.post("/register", tags=["Usuarios"])
def register(usuario: UsuarioRegister, db: Session = Depends(get_db)):
    if crud.get_usuario_by_correo(db, usuario.correo_electronico):
        raise HTTPException(status_code=400, detail="Correo ya registrado")
    
    db_usuario = crud.create_usuario_register(db, usuario)
    return {"usuario": db_usuario, "message": "Usuario registrado correctamente"}


@usuario.post("/login", tags=["Usuarios"])
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    # Buscar usuario por correo
    db_usuario = crud.get_usuario_by_correo(db, usuario.correo_electronico)
    if not db_usuario:
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")
    
    if not bcrypt.verify(usuario.contrasena, db_usuario.contrasena):
        raise HTTPException(status_code=401, detail="Correo o contraseña incorrectos")
    
    token = solicita_token({
        "id": db_usuario.id,
        "Nombre_Usuario": db_usuario.nombre,
        "rol": db_usuario.rol
    })
    return {"access_token": token, "token_type": "bearer"}

@usuario.put(
    "/usuario/{id}",
    response_model=schemas.Usuario,
    tags=["Usuarios"],
    dependencies=[Depends(Portador())]
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
    dependencies=[Depends(Portador())]
)
async def delete_usuario(id: int, db: Session = Depends(get_db)):
    db_usuario = crud.delete_usuario(db=db, usuario_id=id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_usuario
