from pydantic import BaseModel, EmailStr
from enum import Enum
from datetime import datetime

class RolUsuario(str, Enum):
    ciudadano = "ciudadano"
    admin = "admin"

# Base de usuario
class UsuarioBase(BaseModel):
    nombre: str
    correo_electronico: EmailStr
    rol: RolUsuario

# Crear usuario (admin o general)
class UsuarioCreate(UsuarioBase):
    contrasena: str

# Actualizar usuario
class UsuarioUpdate(UsuarioBase):
    contrasena: str

# Respuesta usuario
class Usuario(UsuarioBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True  # ⚡ Pydantic v2

# Para registro desde frontend
class UsuarioRegister(BaseModel):
    nombre: str
    apellidos: str
    correo_electronico: EmailStr
    telefono: str
    contrasena: str

# Para login
class UsuarioLogin(BaseModel):
    correo_electronico: EmailStr
    contrasena: str
