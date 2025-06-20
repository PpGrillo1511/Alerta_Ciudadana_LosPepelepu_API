"""Módulo CRUD para la gestión de usuarios en la base de datos."""

from sqlalchemy.orm import Session
from src.models.usuario import Usuario
from src.schemas.usuario import UsuarioCreate, UsuarioUpdate
from passlib.hash import bcrypt

def get_usuario(db: Session, usuario_id: int):
    """Obtiene un usuario por su ID."""
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def get_usuario_by_correo(db: Session, correo_electronico: str):
    """Obtiene un usuario por su correo."""
    return db.query(Usuario).filter(Usuario.correo_electronico == correo_electronico).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
    """Crea un nuevo usuario en la base de datos."""
    hashed_password = bcrypt.hash(usuario.contrasena)
    db_usuario = Usuario(
        nombre=usuario.nombre,
        correo_electronico=usuario.correo_electronico,
        contrasena=hashed_password,
        rol=usuario.rol
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    """Actualiza los datos de un usuario existente."""
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        for var, value in vars(usuario).items():
            if value is not None:
                if var == "contrasena":
                    value = bcrypt.hash(value)
                setattr(db_usuario, var, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    """Elimina un usuario de la base de datos."""
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

def get_usuarios(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene una lista paginada de usuarios."""
    return db.query(Usuario).offset(skip).limit(limit).all()
