import requests
from bs4 import BeautifulSoup
from database_manager import IntelligenceDB
from ai_analyst import IntelligenceAnalyst  # Yapay Zeka Modülünü Çağırıyoruz


class FieldAgent:
    def __init__(self):
        self.db = IntelligenceDB()
        # Yapay Zeka Analistini Hazırlıyoruz
        print(">> [SİSTEM] Yapay Zeka Analisti Yükleniyor (Ollama)...")
        self.analyst = IntelligenceAnalyst()

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def gather_intelligence(self):
        targets = [
            ("https://thehackernews.com/", "The Hacker News", "h2", "home-title"),
            ("https://techcrunch.com/category/security/", "TechCrunch", "h3", "loop-card__title")
        ]

        print(f">> Ajan ve Analist Göreve Başlıyor...")

        for url, source_name, tag, class_name in targets:
            self.scan_target(url, source_name, tag, class_name)

    def scan_target(self, url, source_name, tag, class_name):
        try:
            print(f">> Bağlanılıyor: {source_name}...")
            response = requests.get(url, headers=self.headers, timeout=10)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                if class_name:
                    news_cards = soup.find_all(tag, class_=class_name)
                else:
                    news_cards = soup.find_all(tag)

                # HIZ AYARI: İlk test için sadece ilk 3 haberi alalım.
                # Hepsini alırsak yapay zeka analizi çok uzun sürer.
                for card in news_cards[:10]:
                    headline = card.text.strip()

                    if len(headline) < 10:
                        continue

                    # --- YAPAY ZEKA DEVREYE GİRİYOR ---
                    # Haberi veritabanına yazmadan önce analiste gönderiyoruz
                    ai_report = self.analyst.analyze(headline)

                    # Veritabanına hem başlığı hem de raporu kaydediyoruz
                    self.db.add_intel(headline, source_name, "Cyber Security", ai_report)

            else:
                print(f"!! Hata: {source_name} erişilemedi.")

        except Exception as e:
            print(f"!! Kritik Hata ({source_name}): {e}")


if __name__ == "__main__":
    agent = FieldAgent()
    agent.gather_intelligence()