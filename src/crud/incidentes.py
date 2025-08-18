"""Módulo CRUD para la gestión de incidentes en la base de datos."""

from sqlalchemy.orm import Session
from src.models.incidente import Incidente
from src.schemas.incidente import IncidenteCreate, IncidenteUpdate

def get_incidente(db: Session, incidente_id: int):
    """Obtiene un incidente por su ID."""
    return db.query(Incidente).filter(Incidente.id == incidente_id).first()

def get_incidentes(db: Session, skip: int = 0, limit: int = 100):
    """Obtiene una lista paginada de incidentes."""
    return db.query(Incidente).offset(skip).limit(limit).all()

def create_incidente(db: Session, incidente: IncidenteCreate):
    """Crea un nuevo incidente en la base de datos."""
    db_incidente = Incidente(
        titulo=incidente.titulo,
        descripcion=incidente.descripcion,
        imagen=incidente.imagen,
        latitud=incidente.latitud,
        longitud=incidente.longitud,
        estado=incidente.estado,
        usuario_id=incidente.usuario_id,
        categoria_id=incidente.categoria_id
    )
    db.add(db_incidente)
    db.commit()
    db.refresh(db_incidente)
    return db_incidente

def update_incidente(db: Session, incidente_id: int, incidente: IncidenteUpdate):
    """Actualiza los datos de un incidente existente."""
    db_incidente = db.query(Incidente).filter(Incidente.id == incidente_id).first()
    if db_incidente:
        for var, value in vars(incidente).items():
            if value is not None:
                setattr(db_incidente, var, value)
        db.commit()
        db.refresh(db_incidente)
    return db_incidente

def delete_incidente(db: Session, incidente_id: int):
    """Elimina un incidente de la base de datos."""
    db_incidente = db.query(Incidente).filter(Incidente.id == incidente_id).first()
    if db_incidente:
        db.delete(db_incidente)
        db.commit()
    return db_incidente
