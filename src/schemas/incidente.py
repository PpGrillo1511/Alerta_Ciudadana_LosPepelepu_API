# src/schemas/incidente.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class EstadoIncidente(str, Enum):
    pendiente = "pendiente"
    en_revision = "en revisión"
    atendido = "atendido"
    descartado = "descartado"

class IncidenteBase(BaseModel):
    titulo: str
    descripcion: str
    imagen: Optional[str] = None
    latitud: float
    longitud: float
    estado: EstadoIncidente
    usuario_id: int
    categoria_id: int

class IncidenteCreate(IncidenteBase):
    pass

class IncidenteUpdate(IncidenteBase):
    pass

class Incidente(IncidenteBase):
    id: int
    fecha_reporte: datetime
    prioridad: str

    class Config:
        orm_mode = True
