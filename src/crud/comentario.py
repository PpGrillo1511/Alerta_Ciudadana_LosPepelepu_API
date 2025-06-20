"""Módulo CRUD para la gestión de comentarios en la base de datos."""

from sqlalchemy.orm import Session
from src.models.comentario import Comentario
from src.schemas.comentario import ComentarioCreate, ComentarioUpdate

def get_comentario(db: Session, comentario_id: int):
    """Obtiene un comentario por su ID."""
    return db.query(Comentario).filter(Comentario.id == comentario_id).first()

def get_comentarios(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene una lista paginada de comentarios."""
    return db.query(Comentario).offset(skip).limit(limit).all()

def create_comentario(db: Session, comentario: ComentarioCreate):
    """Crea un nuevo comentario en la base de datos."""
    db_comentario = Comentario(
        contenido=comentario.contenido,
        usuario_id=comentario.usuario_id,
        incidente_id=comentario.incidente_id
    )
    db.add(db_comentario)
    db.commit()
    db.refresh(db_comentario)
    return db_comentario

def update_comentario(db: Session, comentario_id: int, comentario: ComentarioUpdate):
    """Actualiza los datos de un comentario existente."""
    db_comentario = db.query(Comentario).filter(Comentario.id == comentario_id).first()
    if db_comentario:
        for var, value in vars(comentario).items():
            if value is not None:
                setattr(db_comentario, var, value)
        db.commit()
        db.refresh(db_comentario)
    return db_comentario

def delete_comentario(db: Session, comentario_id: int):
    """Elimina un comentario de la base de datos."""
    db_comentario = db.query(Comentario).filter(Comentario.id == comentario_id).first()
    if db_comentario:
        db.delete(db_comentario)
        db.commit()
    return db_comentario
