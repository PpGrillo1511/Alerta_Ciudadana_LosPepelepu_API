"""Módulo CRUD para la gestión de categorías en la base de datos."""

from sqlalchemy.orm import Session
from src.models.categoria import Categoria
from src.schemas.categoria import CategoriaCreate, CategoriaUpdate

def get_categoria(db: Session, categoria_id: int):
    """Obtiene una categoría por su ID."""
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def get_categoria_by_nombre(db: Session, nombre: str):
    """Obtiene una categoría por su nombre."""
    return db.query(Categoria).filter(Categoria.nombre == nombre).first()

def create_categoria(db: Session, categoria: CategoriaCreate):
    """Crea una nueva categoría en la base de datos."""
    db_categoria = Categoria(
        nombre=categoria.nombre,
        descripcion=categoria.descripcion
    )
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, categoria_id: int, categoria: CategoriaUpdate):
    """Actualiza los datos de una categoría existente."""
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria:
        for var, value in vars(categoria).items():
            if value is not None:
                setattr(db_categoria, var, value)
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    """Elimina una categoría de la base de datos."""
    db_categoria = db.query(Categoria).filter(Categoria.id == categoria_id).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
    return db_categoria

def get_categorias(db: Session, skip: int = 0, limit: int = 10):
    """Obtiene una lista paginada de categorías."""
    return db.query(Categoria).offset(skip).limit(limit).all()
