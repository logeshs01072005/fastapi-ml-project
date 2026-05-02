# 🚀 FastAPI ML Project

This is a Machine Learning project deployed using FastAPI.  
It provides real-time predictions using a trained ML model.

---

## 📌 Features
- Machine Learning model training
- FastAPI REST API
- Real-time prediction endpoint
- JSON input/output support

---

## 🛠️ Tech Stack
- Python
- FastAPI
- Scikit-learn
- Pandas
- Uvicorn

---

## 📂 Project Structure
- main.py → FastAPI server
- train_model.py → model training
- model.pkl → trained ML model
- requirements.txt → dependencies

---

## 🚀 How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run FastAPI server
uvicorn main:app --reload

### 3. Open browser
http://127.0.0.1:8000/docs


### 4. Live Demo

Live Demo:
https://fastapi-ml-project-f8np.onrender.com

---

## 📡 API Endpoint

### POST /predict
Example input:
```json
{
  "input": [25, 50000, 2]
}


