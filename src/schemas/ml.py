from pydantic import BaseModel

class PredictRequest(BaseModel):
    descripcion: str
