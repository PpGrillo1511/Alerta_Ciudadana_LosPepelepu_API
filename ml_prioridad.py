import re
import mysql.connector
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def obtener_incidentes():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Robertin06",
        database="bd_alertaciudadana"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT id, descripcion, fecha_reporte FROM incidentes")
    data = cursor.fetchall()
    conn.close()
    return pd.DataFrame(data, columns=["id", "descripcion", "fecha_reporte"])

palabras_prioridad = {
    "alta": ["humo", "incendio", "arma", "robo", "accidente", "caer"],
    "media": ["ruido", "contaminación", "basura", "luz"],
    "baja": ["vecinos", "madrugada", "música"]
}

def asignar_prioridad(texto):
    texto = texto.lower()
    for palabra in palabras_prioridad["alta"]:
        if palabra in texto:
            return "alta"
    for palabra in palabras_prioridad["media"]:
        if palabra in texto:
            return "media"
    return "baja"

def procesar_incidentes():
    df = obtener_incidentes()
    df["prioridad"] = df["descripcion"].apply(asignar_prioridad)
    return df
