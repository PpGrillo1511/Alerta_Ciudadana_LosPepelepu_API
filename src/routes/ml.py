from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.ml.train import train_model
from src.ml.predict import predict_categoria
from src.models.incidente import Incidente
from src.schemas.ml import PredictRequest

router = APIRouter()

@router.post("/ml/train")
def entrenar_modelo(db: Session = Depends(get_db)):
    incidentes = db.query(Incidente).filter(Incidente.categoria.isnot(None)).all()
    data = [{"descripcion": i.descripcion, "categoria": i.categoria} for i in incidentes]

    if not data:
        return {"error": "No hay datos con categoría para entrenar el modelo"}

    train_model(data)
    return {"mensaje": "✔ Modelo entrenado con éxito", "total": len(data)}

@router.post("/ml/predict")
def predecir_categoria(request: PredictRequest):
    try:
        categoria, confianza = predict_categoria(request.descripcion)
        return {"categoria": categoria, "confianza": confianza}
    except:
        return {"error": "Modelo no entrenado. Ejecuta primero /ml/train"}

@router.post("/ml/retrain")
def reentrenar_modelo(db: Session = Depends(get_db)):
    incidentes = db.query(Incidente).filter(Incidente.categoria.isnot(None)).all()
    data = [{"descripcion": i.descripcion, "categoria": i.categoria} for i in incidentes]

    if not data:
        return {"error": "No hay datos suficientes para reentrenar"}

    train_model(data)
    return {"mensaje": "✔ Modelo reentrenado con éxito", "total": len(data)}
