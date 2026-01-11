# ============================================================
# generate_astronomy_smart.py
# SMART ASTRONOMY DATASET GENERATOR (NO LLM)
# High Diversity • Intent-Friendly • Distillation Ready
# Android / PyramidIDE SAFE
# ============================================================

import os
import random
import time

OUTPUT_PATH = "/storage/emulated/0/astrollm/dataset/astronomy.csv"
TOTAL_ROWS = 100_000        # İstersen 1M yapabilirsin
FLUSH_EVERY = 5_000

# ------------------------------------------------------------
# CORE VOCAB
# ------------------------------------------------------------

OBJECTS = [
    "Mars", "Venüs", "Jüpiter", "Satürn", "Merkür",
    "Neptün", "Uranüs", "Dünya",
    "Güneş", "Sirius", "Betelgeuse", "Vega",
    "Proxima Centauri"
]

TOPICS = [
    "yörünge dinamiği",
    "kütle dağılımı",
    "çekim etkisi",
    "manyetik alan",
    "sıcaklık profili",
    "iç yapı",
    "atmosfer bileşimi",
    "ışınım dengesi"
]

ADJECTIVES = [
    "yüksek enerjili",
    "düşük yoğunluklu",
    "kararsız",
    "istikrarlı",
    "aşırı sıcak",
    "soğuk",
    "manyetik olarak aktif",
    "yoğun"
]

PERSPECTIVES = [
    "gözlemsel olarak",
    "teorik modellere göre",
    "simülasyon sonuçlarına dayanarak",
    "NASA verilerine göre",
    "son astronomik çalışmalarda",
    "uzun dönem gözlemler sonucunda"
]

ACTIONS = [
    "incelenmektedir",
    "analiz edilmiştir",
    "hesaplanmıştır",
    "ölçülmüştür",
    "modellemesi yapılmıştır",
    "doğrulanmıştır"
]

CAUSES = [
    "çekimsel etkileşimler nedeniyle",
    "yörünge sapmaları sonucunda",
    "yüksek kütle etkisiyle",
    "enerji dengesizliği yüzünden",
    "manyetik alan değişimleri sebebiyle"
]

RESULTS = [
    "risk seviyesi artmaktadır",
    "yörünge kararlılığı korunmaktadır",
    "uzun vadeli izleme önerilmektedir",
    "potansiyel tehdit oluşturmaktadır",
    "bilimsel açıdan önemlidir"
]

# ------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------

def human_number():
    n = random.randint(10_000, 10_000_000)
    if n >= 1_000_000:
        return f"{n // 1_000_000} milyon"
    return f"{n // 1_000} bin"

def pick_other(obj):
    ref = random.choice(OBJECTS)
    return ref if ref != obj else random.choice(OBJECTS)

# ------------------------------------------------------------
# SENTENCE GENERATOR
# ------------------------------------------------------------

def generate_sentence():
    obj = random.choice(OBJECTS)
    ref = pick_other(obj)
    topic = random.choice(TOPICS)
    adj = random.choice(ADJECTIVES)
    view = random.choice(PERSPECTIVES)
    act = random.choice(ACTIONS)
    cause = random.choice(CAUSES)
    result = random.choice(RESULTS)
    value = human_number()

    templates = [
        f"{view}, {adj} {obj} için {topic} {act}.",
        f"{obj}, {ref} ile olan etkileşimi nedeniyle {topic} açısından {act}.",
        f"{obj} üzerinde yapılan analizlerde {cause}, bu durum {result}.",
        f"{view} elde edilen verilere göre {obj} yaklaşık {value} km mesafede bulunmaktadır.",
        f"{adj} yapıya sahip olan {obj}, {topic} bakımından bilimsel olarak önemlidir.",
        f"{obj} için {topic} analizi {cause} ve {result}."
    ]

    return random.choice(templates)

# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    start = time.time()
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("id,topic,text\n")

        for i in range(1, TOTAL_ROWS + 1):
            text = generate_sentence()
            topic = random.choice(TOPICS)
            f.write(f"{i},{topic},\"{text}\"\n")

            if i % FLUSH_EVERY == 0:
                f.flush()
                elapsed = time.time() - start
                print(f"✅ {i:,} satır yazıldı | {elapsed:.1f} sn")

    print("\n🎉 TAMAMLANDI")
    print(f"📁 {OUTPUT_PATH}")
    print(f"📊 Toplam satır: {TOTAL_ROWS:,}")

if __name__ == "__main__":
    main()