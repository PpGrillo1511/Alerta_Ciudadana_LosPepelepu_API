# src/models/categoria.py
from sqlalchemy import Column, Integer, String
from src.config.db import base

class Categoria(base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)  # Ej: "Robo", "Fuga de agua"
    descripcion = Column(String(255), nullable=True)
