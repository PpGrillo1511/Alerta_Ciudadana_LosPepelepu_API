# src/models/incidente.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from src.config.db import base
from datetime import datetime
import enum

# Enum para el estado del incidente
class EstadoIncidente(str, enum.Enum):
    pendiente = "pendiente"
    en_revision = "en revisión"
    atendido = "atendido"
    descartado = "descartado"

class Incidente(base):
    __tablename__ = "incidentes"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(String(500), nullable=False)
    imagen = Column(String(255), nullable=True)  # URL o nombre del archivo
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)
    estado = Column(Enum(EstadoIncidente), default=EstadoIncidente.pendiente)
    fecha_reporte = Column(DateTime, default=datetime.utcnow)

    # Relaciones
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)

    # Opcional: relaciones para ORM
    usuario = relationship("Usuario", backref="incidentes")
    categoria = relationship("Categoria", backref="incidentes")
