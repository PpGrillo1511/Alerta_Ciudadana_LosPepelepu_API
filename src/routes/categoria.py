# src/routes/categoria.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import src.schemas.categoria as schemas
import src.models.categoria as models
import src.crud.categoria as crud
from src.config.db import SesionLocal, engine
#from portadortoken import Portador

categoria = APIRouter()

models.base.metadata.create_all(bind=engine)

def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

@categoria.get(
    "/categorias/",
    response_model=List[schemas.Categoria],
    tags=["Categorias"],
    #dependencies=[Depends(Portador())]
)
async def read_categorias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_categorias(db=db, skip=skip, limit=limit)

@categoria.get(
    "/categoria/{id}",
    response_model=schemas.Categoria,
    tags=["Categorias"],
    #dependencies=[Depends(Portador())]
)
async def read_categoria(id: int, db: Session = Depends(get_db)):
    categoria = crud.get_categoria(db=db, categoria_id=id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@categoria.post(
    "/categoria/",
    response_model=schemas.Categoria,
    tags=["Categorias"],
    #dependencies=[Depends(Portador())]
)
def create_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    return crud.create_categoria(db=db, categoria=categoria)

@categoria.put(
    "/categoria/{id}",
    response_model=schemas.Categoria,
    tags=["Categorias"],
    #dependencies=[Depends(Portador())]
)
async def update_categoria(id: int, categoria: schemas.CategoriaUpdate, db: Session = Depends(get_db)):
    db_categoria = crud.update_categoria(db=db, categoria_id=id, categoria=categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no existe, no actualizada")
    return db_categoria

@categoria.delete(
    "/categoria/{id}",
    response_model=schemas.Categoria,
    tags=["Categorias"],
    #dependencies=[Depends(Portador())]
)
async def delete_categoria(id: int, db: Session = Depends(get_db)):
    db_categoria = crud.delete_categoria(db=db, categoria_id=id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoría no existe, no se pudo eliminar")
    return db_categoria
