from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

MODEL_DIR = "src/ml/modelos"
MODEL_FILE = os.path.join(MODEL_DIR, "modelo_categoria.pkl")
VECTORIZER_FILE = os.path.join(MODEL_DIR, "vectorizer.pkl")

def entrenar_modelo(descripciones, categorias):
    """Entrena el modelo y guarda vectorizer y modelo en archivos."""
    # Crear carpeta si no existe
    os.makedirs(MODEL_DIR, exist_ok=True)

    # Vectorizar descripciones
    vectorizer = TfidfVectorizer()
    X_vect = vectorizer.fit_transform(descripciones)

    # Entrenar modelo
    model = LogisticRegression(max_iter=1000)
    model.fit(X_vect, categorias)

    # Guardar modelo y vectorizer
    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)
    with open(VECTORIZER_FILE, "wb") as f:
        pickle.dump(vectorizer, f)

    return {"mensaje": "Modelo entrenado y guardado exitosamente"}
