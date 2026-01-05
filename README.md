# 🕵️‍♂️ Spectre AI Sentinel [TR]

**Spectre AI**, siber güvenlik dünyasındaki gelişmeleri 7/24 takip eden, toplanan verileri Yerel Yapay Zeka (Local LLM) ile analiz eden ve potansiyel tehditleri raporlayan otonom bir istihbarat platformudur.

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![AI Model](https://img.shields.io/badge/AI-Ollama%20%2F%20Llama3-orange)

## 🚀 Projenin Amacı
Bu proje, manuel siber istihbarat toplama süreçlerini otomatize etmek ve "ham veriyi" işlenmiş "istihbarata" dönüştürmek amacıyla geliştirilmiştir. Sistem arka planda sürekli çalışarak dünyaca ünlü siber güvenlik kaynaklarını tarar, **Ollama** üzerinden çalışan yapay zeka modeli ile bu haberleri analiz eder ve kritiklik seviyesine göre sınıflandırır.

## ⚡ Özellikler

* **🕵️ Otonom Saha Ajanı:** `BeautifulSoup` kullanarak *The Hacker News* ve *TechCrunch Security* gibi kaynaklardan veri toplar.
* **🧠 Yapay Zeka Analisti:** Toplanan verileri **Llama3** modeli ile okur, Türkçe özet çıkarır ve tehdit seviyesini (Düşük/Orta/Yüksek) belirler.
* **🗄️ İstihbarat Arşivi:** Verileri SQLite veritabanında saklar, mükerrer kayıtları engeller.
* **📊 Canlı Komuta Merkezi (Dashboard):** HTML/CSS/JS ile hazırlanmış, *Skyfall* temalı arayüz üzerinden verileri canlı grafiklerle sunar.
* **🔄 Multithreading:** Sunucu ve Tarayıcı ajanları eş zamanlı (concurrent) çalışır.

## 🛠️ Kullanılan Teknolojiler

* **Backend:** Python 3.10, FastAPI, Uvicorn
* **Database:** SQLite3
* **AI/LLM:** Ollama (Llama3 Model)
* **Scraping:** Requests, BeautifulSoup4
* **Frontend:** HTML5, CSS3 (Google Fonts & Custom Fonts), JavaScript (Fetch API, Chart.js)

## ⚙️ Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için adımları izleyin:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADINIZ/spectre-ai-sentinel-tr.git](https://github.com/KULLANICI_ADINIZ/spectre-ai-sentinel-tr.git)
    cd spectre-ai-sentinel-tr
    ```

2.  **Gereksinimleri Yükleyin:**
    ```bash
    pip install fastapi uvicorn requests beautifulsoup4 ollama
    ```

3.  **Ollama ve Modeli Kurun:**
    * [Ollama.com](https://ollama.com) adresinden uygulamayı indirin.
    * Terminalden modeli çekin:
        ```bash
        ollama run llama3
        ```

4.  **Sistemi Başlatın:**
    ```bash
    python api_server.py
    ```

5.  **Erişim:**
    Tarayıcınızdan `http://localhost:8000/dashboard` adresine gidin.



## ⚠️ Yasal Uyarı
Bu proje tamamen eğitim ve araştırma amaçlı geliştirilmiştir. Toplanan veriler halka açık kaynaklardan elde edilmektedir.
---

*Developed by Yiğit Buğra Küçük*
