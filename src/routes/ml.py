from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import SesionLocal
from src.models.incidente import Incidente
from src.ml.train import entrenar_modelo
import pickle
from fastapi import Query

router = APIRouter(prefix="/ml", tags=["ML"])

# Dependencia para obtener DB
def get_db():
    db = SesionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/train")
def train_model(db: Session = Depends(get_db)):
    # Obtener incidentes con categoria_id
    incidentes = db.query(Incidente)\
        .filter(Incidente.categoria_id != None)\
        .filter(Incidente.categoria_id != 0)\
        .all()

    if not incidentes:
        return {"error": "No hay incidentes con categoria_id para entrenar"}

    descripciones = [inc.descripcion for inc in incidentes]
    categorias = [inc.categoria_id for inc in incidentes]

    # Entrenar modelo
    resultado = entrenar_modelo(descripciones, categorias)
    return resultado

@router.post("/predict")
def predecir_categoria(descripcion: str = Query(...)):
    # Cargar modelo y vectorizer
    with open("src/ml/modelos/modelo_categoria.pkl", "rb") as f:
        model = pickle.load(f)
    with open("src/ml/modelos/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    # Transformar descripción y predecir
    X = vectorizer.transform([descripcion])
    pred = model.predict(X)

    return {"categoria_id_predicha": int(pred[0])}