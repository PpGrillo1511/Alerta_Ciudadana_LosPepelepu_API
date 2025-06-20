# src/schemas/usuario.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from enum import Enum


class RolUsuario(str, Enum):
    ciudadano = "ciudadano"
    admin = "admin"

class UsuarioBase(BaseModel):
    nombre: str
    correo_electronico: EmailStr
    rol: RolUsuario

class UsuarioCreate(UsuarioBase):
    contrasena: str  # solo se envía al crear

class UsuarioUpdate(UsuarioBase):
    contrasena: str

class Usuario(UsuarioBase):
    id: int
    fecha_creacion: datetime

    class Config:
        orm_mode = True
