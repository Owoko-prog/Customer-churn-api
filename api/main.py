from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import joblib
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "churn_model.pkl")

model = joblib.load(model_path)


class CustomerData(BaseModel):
    features: List[float]


@app.get("/")
def home():
    return {"message": "Customer Churn API running"}


@app.post("/predict")
def predict(data: CustomerData):

    prediction = model.predict([data.features])

    return {
        "churn_prediction": int(prediction[0])
    }