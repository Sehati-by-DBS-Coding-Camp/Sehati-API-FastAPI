from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import load_model # type: ignore
import pickle
import os
from dotenv import load_dotenv
from app.rekomendasi import get_rekomendasi
from app.emotion import predict_emotion
from app.dass21 import hitung_skala_dass21
from app.dass21 import hitung_rata_rata_dass21


load_dotenv("var/.env")
#Directory untuk model dan tokenizer
MODEL_DIR = os.getenv("MODEL_DIR", "models")
MODEL_PATH = os.path.join(MODEL_DIR, "best_lstm_model_tuning.h5")
TOKENIZER_PATH = os.path.join(MODEL_DIR, "tokenizer_lstm.pkl")
LABEL_ENCODER_PATH = os.path.join(MODEL_DIR, "label_encoder.pkl")



app = FastAPI(  
    title="API SEHATI MODEL",
    description="API untuk Capstone SEHATI",
    version="1.0.0"
    )

try:
    # Load model dan tokenizer
    model = load_model(MODEL_PATH, compile=False)
    with open(TOKENIZER_PATH, "rb") as f:
        tokenizer = pickle.load(f)
    with open(LABEL_ENCODER_PATH, "rb") as f:
        label_encoder = pickle.load(f)
except Exception as e:
    print(f"Error saat memuat model: {e}")
    model = None
    tokenizer = None
    label_encoder = None
    
    
class TextInput(BaseModel):
    text: str

class RekomendasiInput(BaseModel):
    depresi: int
    kecemasan: int
    stress: int
    label_ml: str

class Dass21(BaseModel):
    depresi: int
    kecemasan: int
    stress: int
    
@app.get("/", tags=["General"])
def read_root():
    """Endpoint root untuk mengecek apakah API berjalan."""
    return {"message": "Selamat datang di API SEHATI!"}

@app.post("/predict")
def predict(input_data: TextInput):
    result = predict_emotion(input_data.text, model, tokenizer, label_encoder)
    return result

@app.post("/rekomendasi")
def rekomendasi(input_data: RekomendasiInput):
    rekomendasi = get_rekomendasi(input_data.depresi, input_data.kecemasan, input_data.stress, input_data.label_ml)
    return {
        "depresi": input_data.depresi,
        "kecemasan": input_data.kecemasan,
        "stress": input_data.stress,
        "label_ml": input_data.label_ml,
        "rekomendasi": rekomendasi
    }
    
@app.post("/dass21")
def dass21(input_data: Dass21):
    hasil = hitung_skala_dass21(input_data.depresi, input_data.kecemasan, input_data.stress)
    return {
        "Depresi": hasil["Depresi"],
        "Kecemasan": hasil["Kecemasan"],
        "Stres": hasil["Stres"]
    }
@app.post("/dass21/rata-rata")
def dass21_rata_rata(input_data: Dass21):
    rata_rata = hitung_rata_rata_dass21(input_data.depresi, input_data.kecemasan, input_data.stress)
    return {
        "Rata-rata": rata_rata
    }