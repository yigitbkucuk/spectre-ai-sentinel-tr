from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn
import threading
import time
from database_manager import IntelligenceDB
from intel_agent import FieldAgent

app = FastAPI()
# Statik dosyaları (font, resim vs.) sunmak için izin veriyoruz
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- ARKA PLAN GÖREVİ ---
def background_scanner():
    print(">> OTONOM TARAMA SİSTEMİ: AKTİF")
    while True:
        try:
            agent = FieldAgent()
            agent.gather_intelligence()
            print(">> Sistem bekleme modunda... (300 saniye)")
            time.sleep(300)
        except Exception as e:
            print(f"!! Tarama Hatası: {e}")
            time.sleep(60)


# --- DASHBOARD SUNUMU ---
@app.get("/dashboard", response_class=HTMLResponse)
def serve_dashboard():
    with open("dashboard.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    html_content = html_content.replace("http://127.0.0.1:8000", "")
    return html_content


# --- API ENDPOINTLERİ (GÜNCELLENDİ) ---
@app.get("/")
def home():
    return {"Durum": "MI6 Sunucusu Online", "Link": "/dashboard adresine git"}


@app.get("/intel")
def get_intel():
    db = IntelligenceDB()
    data = db.get_all_intel()
    db.close()

    # GÜNCELLEME: Artık 'analysis' (4. sütun) verisini de gönderiyoruz
    formatted_data = []
    for r in data:
        formatted_data.append({
            "id": r[0],
            "title": r[1],
            "source": r[2],
            "category": r[3],
            "analysis": r[4],  # YENİ VERİ BURADA
            "timestamp": r[5]
        })
    return formatted_data


@app.get("/intel/critical")
def get_critical():
    db = IntelligenceDB()
    data = db.get_critical_intel()
    db.close()

    formatted_data = []
    for r in data:
        formatted_data.append({
            "id": r[0],
            "title": r[1],
            "source": r[2],
            "category": r[3],
            "analysis": r[4],  # YENİ VERİ BURADA
            "timestamp": r[5]
        })
    return formatted_data


@app.get("/intel/stats")
def get_stats():
    db = IntelligenceDB()
    data = db.get_stats()
    db.close()
    stats = {row[0]: row[1] for row in data}
    return stats


if __name__ == "__main__":
    scanner_thread = threading.Thread(target=background_scanner, daemon=True)
    scanner_thread.start()
    print(">> MI6 Karargah Sunucusu Başlatılıyor...")
    uvicorn.run(app, host="0.0.0.0", port=8000)