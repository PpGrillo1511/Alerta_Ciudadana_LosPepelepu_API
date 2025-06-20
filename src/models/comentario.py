# src/models/comentario.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from src.config.db import base
from datetime import datetime

class Comentario(base):
    __tablename__ = "comentarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    contenido = Column(String(500), nullable=False)
    fecha = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    incidente_id = Column(Integer, ForeignKey("incidentes.id"), nullable=False)

    # ORM: relaciones inversas
    usuario = relationship("Usuario", backref="comentarios")
    incidente = relationship("Incidente", backref="comentarios")
