import requests

def llama_predict(texto: str):
    prompt = f"Clasifica este incidente ciudadano en categorías como: infraestructura, seguridad, medio ambiente, etc.\n\nIncidente: {texto}"
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama2", "prompt": prompt}
    )

    categoria = response.json().get("response", "").strip()
    return categoria
