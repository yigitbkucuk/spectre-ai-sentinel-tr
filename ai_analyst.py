import ollama


class IntelligenceAnalyst:
    def __init__(self, model_name="llama3"):
        self.model = model_name

    def analyze(self, news_title):
        """
        Haberi okur ve Türkçe olarak kısa bir istihbarat özeti çıkarır.
        """
        print(f"   [AI] Analiz Ediliyor: {news_title}...")

        # Yapay Zekaya Verdiğimiz Emir (Prompt Engineering)
        # Ona bir rol biçiyoruz: MI6 Analisti.
        prompt = f"""
        Sen MI6 istihbarat servisinde çalışan kıdemli bir siber güvenlik analistisin.
        Görevin: Aşağıdaki İngilizce haber başlığını analiz etmek.

        Haber Başlığı: "{news_title}"

        İstediğim Çıktı Formatı (Kesinlikle Türkçe Olmalı):
        1. Bu haberin siber güvenlik açısından önemini 1 cümle ile özetle.
        2. Tehdit Seviyesi: (DÜŞÜK, ORTA veya YÜKSEK)

        Lütfen sadece sonucu yaz, sohbet etme.
        """

        try:
            # Ollama'ya isteği gönderiyoruz
            response = ollama.chat(model=self.model, messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ])

            # Cevabı alıyoruz
            analysis_result = response['message']['content']
            return analysis_result

        except Exception as e:
            return f"Analiz Hatası: Model yanıt vermedi. ({e})"


# --- TEST BLOĞU ---
if __name__ == "__main__":
    # Bakalım çalışıyor mu?
    analyst = IntelligenceAnalyst()
    sample_news = "Critical SQL Injection Vulnerability Found in Banking Systems"

    print(">> Test Başlatılıyor...")
    result = analyst.analyze(sample_news)

    print("\n--- AI RAPORU ---")
    print(result)
    print("-----------------")