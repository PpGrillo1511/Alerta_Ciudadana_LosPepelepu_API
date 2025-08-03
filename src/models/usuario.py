# src/models/usuario.py
from sqlalchemy import Column, Integer, String, DateTime, Enum
from src.config.db import base
from datetime import datetime
import enum

# Enum para los roles de usuario
class RolUsuario(str, enum.Enum):
    ciudadano = "ciudadano"
    admin = "admin"

class Usuario(base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo_electronico = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    rol = Column(Enum(RolUsuario), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
