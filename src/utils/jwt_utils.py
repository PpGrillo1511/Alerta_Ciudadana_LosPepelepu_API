from datetime import datetime, timedelta
from fastapi import HTTPException
from jwt import encode, decode, ExpiredSignatureError, DecodeError
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
JWT_EXPIRATION_MINUTES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRE_MINUTES', 60))  # Por si no está definido

def solicita_token(usuario_data: dict) -> str:
    expiracion = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    
    payload = {
        "sub": usuario_data["id"],
        "nombre": usuario_data["nombre"],
        "rol": usuario_data["rol"],
        "exp": expiracion
    }

    token: str = encode(payload=payload, key=SECRET_KEY, algorithm=JWT_ALGORITHM)
    return token

def valida_token(token: str) -> dict:
    try:
        dato: dict = decode(token, key=SECRET_KEY, algorithms=[JWT_ALGORITHM])
        if 'exp' not in dato:
            raise HTTPException(status_code=401, detail="Token no contiene información de expiración")

        expiracion = datetime.utcfromtimestamp(dato['exp'])
        if expiracion < datetime.utcnow():
            raise HTTPException(
                status_code=401,
                detail=f"Token ha expirado. Expiró el {expiracion.strftime('%Y-%m-%d %H:%M:%S')} UTC."
            )

        return dato

    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token ha expirado")
    except DecodeError:
        raise HTTPException(status_code=401, detail="Token inválido")
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
