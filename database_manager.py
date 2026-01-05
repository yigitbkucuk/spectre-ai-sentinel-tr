import sqlite3
from datetime import datetime


class IntelligenceDB:
    def __init__(self, db_name="spectre_intel.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # YENİ SÜTUN EKLENDİ: analysis (Yapay Zeka Yorumu)
        sql_command = """
        CREATE TABLE IF NOT EXISTS intel_reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            source TEXT,
            category TEXT,
            analysis TEXT, 
            timestamp TEXT
        )
        """
        self.cursor.execute(sql_command)
        self.conn.commit()

    def add_intel(self, title, source, category, analysis="Analiz Bekleniyor..."):
        # Veri eklerken artık analizi de kaydediyoruz
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Aynı haberin tekrar kaydedilmesini önleyelim (Mükerrer Kayıt Kontrolü)
        check_command = "SELECT * FROM intel_reports WHERE title = ?"
        self.cursor.execute(check_command, (title,))
        if self.cursor.fetchone():
            return  # Eğer haber zaten varsa kaydetme, çık.

        insert_command = """
        INSERT INTO intel_reports (title, source, category, analysis, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """
        self.cursor.execute(insert_command, (title, source, category, analysis, current_time))
        self.conn.commit()
        print(f">> [DB] Kayıt + Analiz Arşivlendi: {title[:30]}...")

    def get_all_intel(self):
        self.cursor.execute("SELECT * FROM intel_reports ORDER BY timestamp DESC")
        return self.cursor.fetchall()

    def get_critical_intel(self):
        command = """
        SELECT * FROM intel_reports 
        WHERE title LIKE '%Hack%' 
           OR title LIKE '%Attack%' 
           OR title LIKE '%Critical%'
           OR analysis LIKE '%YÜKSEK%'
        ORDER BY timestamp DESC
        """
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def get_stats(self):
        command = "SELECT source, COUNT(*) as total FROM intel_reports GROUP BY source"
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()