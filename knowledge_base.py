# ============================================================
# Knowledge Base – HARD CLEAN (UTF-8 SAFE)
# ============================================================

import csv
import os
import re

class KnowledgeBase:
    def __init__(self):
        self.documents = []

    def _clean(self, text: str) -> str:
        # UTF-8 dışı her şeyi sil
        text = text.encode("utf-8", errors="ignore").decode("utf-8")

        # Kontrol karakterleri
        text = re.sub(r"[\x00-\x1f\x7f-\x9f]", " ", text)

        # Aşırı sembol temizliği
        text = re.sub(r"[^\w\sğüşöçıİĞÜŞÖÇ\.\,\-\(\)]", " ", text)

        return text.strip()

    def _is_valid(self, text: str) -> bool:
        if len(text) < 30:
            return False
        if any(x in text.lower() for x in ["http", "www", ".png", ".jpg"]):
            return False
        return True

    def load_file(self, path: str):
        if not os.path.exists(path):
            print("❌ KB yok:", path)
            return

        loaded = 0

        with open(path, encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)
            for row in reader:
                for cell in row:
                    clean = self._clean(cell)
                    if self._is_valid(clean):
                        self.documents.append(clean)
                        loaded += 1

        print(f"✅ {loaded} temiz bilgi yüklendi → {os.path.basename(path)}")

    def search(self, query: str, top_k: int = 3):
        q = query.lower().split()
        scored = []

        for doc in self.documents:
            d = doc.lower()
            score = sum(1 for w in q if w in d)
            if score > 0:
                scored.append((score, doc))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [d for _, d in scored[:top_k]]