from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.utils.jwt_utils import valida_token

class Portador(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            token = credentials.credentials
            try:
                payload = valida_token(token)
                return payload
            except HTTPException as e:
                raise HTTPException(status_code=401, detail=str(e.detail))
        else:
            raise HTTPException(status_code=401, detail="Token no proporcionado")
