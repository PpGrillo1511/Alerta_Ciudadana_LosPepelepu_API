import pickle

def predict_categoria(texto: str):
    with open("src/ml/model.pkl", "rb") as f:
        vectorizer, model = pickle.load(f)

    X = vectorizer.transform([texto])
    pred = model.predict(X)[0]
    proba = max(model.predict_proba(X)[0])

    return pred, proba
