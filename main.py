from fastapi import FastAPI
import pickle

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "ML API running online 🚀"}

@app.post("/predict")
def predict(data: dict):
    input_data = data["input"]
    prediction = model.predict([input_data])
    return {"prediction": int(prediction[0])}