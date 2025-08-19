from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.incidente import Incidente
from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd

router = APIRouter()

@router.get("/zonas-criticas")
def detectar_zonas_criticas(db: Session = Depends(get_db)):
    incidentes = db.query(Incidente).all()

    if not incidentes:
        return {"message": "No hay incidentes registrados"}

    data = pd.DataFrame([{
        "id": i.id,
        "descripcion": i.descripcion,
        "lat": i.latitud,
        "lng": i.longitud
    } for i in incidentes])

    coords = data[["lat", "lng"]].to_numpy()

    clustering = DBSCAN(eps=0.01, min_samples=2, metric="euclidean").fit(coords)

    data["cluster"] = clustering.labels_

    zonas = []
    for cluster_id in set(clustering.labels_):
        if cluster_id == -1:
            continue
        grupo = data[data["cluster"] == cluster_id]
        zonas.append({
            "zona_id": int(cluster_id),
            "cantidad_incidentes": len(grupo),
            "incidentes": grupo[["id", "descripcion", "lat", "lng"]].to_dict(orient="records")
        })

    return {
        "total_incidentes": len(data),
        "zonas_criticas": zonas
    }
