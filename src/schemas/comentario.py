# src/schemas/comentario.py
from pydantic import BaseModel
from datetime import datetime

class ComentarioBase(BaseModel):
    contenido: str
    usuario_id: int
    incidente_id: int

class ComentarioCreate(ComentarioBase):
    pass

class ComentarioUpdate(ComentarioBase):
    pass

class Comentario(ComentarioBase):
    id: int
    fecha: datetime

    class Config:
        orm_mode = True
