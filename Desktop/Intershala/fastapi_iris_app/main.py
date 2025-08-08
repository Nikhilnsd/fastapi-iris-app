from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load("iris_model.pkl")
species = ["setosa", "versicolor", "virginica"]

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

app = FastAPI(title="Iris Classifier API", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API!"}

@app.post("/predict")
def predict_species(features: IrisFeatures):
    try:
        data = np.array([
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]).reshape(1, -1)

        prediction = model.predict(data)[0]
        return {"species": species[prediction]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
