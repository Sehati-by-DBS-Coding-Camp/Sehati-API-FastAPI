from google import genai
import os
from dotenv import load_dotenv

load_dotenv("var/.env")

try:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    client = genai.Client(api_key=GOOGLE_API_KEY)
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY tidak ditemukan di environment.")
except Exception as e:
    raise RuntimeError(f"Error saat menginisialisasi Google Gen AI Client: {e}")


def get_rekomendasi(depresi, kecemasan, stress,label_ml):
    prompt = (        
        f"kamu adalah seorang profesional kesehatan mental (psikolog/psikiater/ahli), "
        f"kamu akan melakukan skrining menggunakan metode DASS-21 untuk pasien dan Model ML analisis sentimen"
        f"buat rekomendasi psikologis dalam 4 poin utama berdasarkan data berikut:\n"
        f"Depresi: {depresi}\n"
        f"Kecemasan: {kecemasan}\n"
        f"Stres: {stress}\n"
        f"Label ML: {label_ml}\n"
        f"Berikan rekomendasi psikologis yang sesuai dengan hasil DASS-21 dan label ML, "
        f"Gunakan bahasa profesional yang padat, sederhana, dan mudah dimengerti, serta tetap mempertahankan istilah teknis yang relevan."
        f"Jika hasil dass-21 menunjukkan depresi, kecemasan, atau stres yang rendah, maka berikan rekomendasi untuk menjaga kesehatan mental dan mencegah masalah di masa depan. "
        f"Jika hasil menunjukkan depresi, kecemasan, atau stres yang tinggi, maka berikan rekomendasi untuk mengatasi masalah tersebut. "
        f"Fokus hanya pada rekomendasi dengan teori berdasarkan metode DASS-21, tanpa penjelasan atau pendahuluan atau introduction apapun. "

    )
    
    try:
        if not prompt.strip():
            raise ValueError("Prompt tidak boleh kosong.")
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
        )
        return response.text
    except Exception as e:
        raise RuntimeError(f"Error saat mendapatkan rekomendasi: {e}")