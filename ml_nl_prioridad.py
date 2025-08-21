from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.config.db import get_db
from src.models.incidente import Incidente
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
import numpy as np
import pandas as pd

router = APIRouter()

@router.get("/zonas-criticas")
def detectar_zonas_criticas(db: Session = Depends(get_db)):
    incidentes = db.query(Incidente).all()
    if not incidentes:
        return {"message": "No hay incidentes registrados"}

    # DataFrame con los incidentes
    data = pd.DataFrame([{
        "id": i.id,
        "descripcion": i.descripcion,
        "lat": i.latitud,
        "lng": i.longitud
    } for i in incidentes])

    coords = data[["lat", "lng"]].to_numpy()

    # 🔥 Calcular eps automáticamente con distancias a vecinos más cercanos
    neigh = NearestNeighbors(n_neighbors=2)
    neigh.fit(coords)
    distances, _ = neigh.kneighbors(coords)

    # Usamos el segundo vecino (distancia > 0)
    distancias = np.sort(distances[:, 1])

    # Tomamos un percentil como eps, ej: 90% (puedes ajustar)
    eps_auto = np.percentile(distancias, 90)

    clustering = DBSCAN(eps=eps_auto, min_samples=2, metric="euclidean").fit(coords)
    data["cluster"] = clustering.labels_

    zonas = []
    for cluster_id in set(clustering.labels_):
        if cluster_id == -1:
            continue
        grupo = data[data["cluster"] == cluster_id]

        lat_centro = grupo["lat"].mean()
        lng_centro = grupo["lng"].mean()

        zonas.append({
            "zona_id": int(cluster_id),
            "cantidad_incidentes": len(grupo),
            "lat_centro": float(lat_centro),
            "lng_centro": float(lng_centro)
        })

    return {
        "total_incidentes": len(data),
        "eps_usado": float(eps_auto),   # 👈 útil para debug
        "total_zonas": len(zonas),
        "zonas_criticas": zonas
    }
