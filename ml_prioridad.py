# ml_prioridad_descripcion.py

from typing import Dict

# Diccionario de palabras clave por nivel de prioridad
PALABRAS_CLAVE = {
    2: ["humo", "incendio", "explosion", "herido", "accidente grave"],
    1: ["robo", "hurto", "accidente leve", "sospechoso"],
    0: ["molestia", "ruido", "consulta", "informacion"]
}

def predecir_prioridad(incidente: Dict) -> int:
    """
    Recibe un diccionario con 'descripcion' y 'fecha'.
    Devuelve prioridad (0=baja, 1=media, 2=alta)
    """
    descripcion = incidente['descripcion'].lower()

    for prioridad, palabras in PALABRAS_CLAVE.items():
        for palabra in palabras:
            if palabra in descripcion:
                return prioridad
    
    # Si no coincide ninguna palabra clave, prioridad por defecto
    return 0
