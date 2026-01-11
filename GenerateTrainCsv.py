import csv
import os
import random

BASE_DIR = "/storage/emulated/0/astrollm/dataset"
OUT_FILE = os.path.join(BASE_DIR, "train.csv")

os.makedirs(BASE_DIR, exist_ok=True)

intents = [
    "asteroid_risk",
    "asteroid_near",
    "asteroid_size",
    "planet_size",
    "is_real",
    "how_it_works",
]

questions = {
    "asteroid_risk": [
        "en tehlikeli asteroid hangisi",
        "asteroid dünyaya çarpar mı",
        "asteroid ne kadar tehlikeli",
    ],
    "asteroid_near": [
        "en yakın asteroid hangisi",
        "dünyaya en yakın asteroid",
    ],
    "asteroid_size": [
        "asteroid ne kadar büyük",
        "asteroidlerin boyutu nedir",
    ],
    "planet_size": [
        "dünyanın çapı kaç km",
        "dünya ne kadar büyük",
    ],
    "is_real": [
        "bu sistem gerçek mi",
        "gerçek veri mi",
    ],
    "how_it_works": [
        "nasıl çalışıyor",
        "bu sistem nasıl çalışır",
    ],
}

rows = []

# 5000+ satır üret
for _ in range(900):
    for intent, qs in questions.items():
        q = random.choice(qs)
        rows.append([q, intent])

with open(OUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "intent"])
    writer.writerows(rows)

print(f"✅ train.csv oluşturuldu → {OUT_FILE}")
print(f"📊 Toplam satır: {len(rows)}")