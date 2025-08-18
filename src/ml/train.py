from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

def train_model(incidentes):
    textos = [i["descripcion"] for i in incidentes]
    etiquetas = [i["categoria"] for i in incidentes]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(textos)

    model = LogisticRegression()
    model.fit(X, etiquetas)

    with open("src/ml/model.pkl", "wb") as f:
        pickle.dump((vectorizer, model), f)
