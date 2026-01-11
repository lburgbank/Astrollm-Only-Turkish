import csv
import os
import random

SRC_FILES = [
    "/storage/emulated/0/astrollm/dataset/astronomy.csv",
    "/storage/emulated/0/astrollm/dataset/asteroids.csv"
]

OUT_FILE = "/storage/emulated/0/astrollm/dataset/train.csv"

TEMPLATES = [
    "{} nedir",
    "{} ne demek",
    "{} hakkında bilgi",
    "{} ne işe yarar",
    "{} doğru mu",
    "{} gerçek mi"
]

def clean(text):
    t = text.lower().strip()
    if not t:
        return None
    if "http" in t or "www" in t:
        return None
    if len(t) < 5 or len(t) > 80:
        return None
    return t

def main():
    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

    total = 0
    with open(OUT_FILE, "w", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["text", "intent"])

        for src in SRC_FILES:
            if not os.path.exists(src):
                continue

            intent = os.path.basename(src).replace(".csv", "")

            with open(src, encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    for cell in row:
                        base = clean(cell)
                        if not base:
                            continue

                        q = random.choice(TEMPLATES).format(base)
                        writer.writerow([q, intent])
                        total += 1

    print("✅ train.csv üretildi")
    print("📊 Toplam satır:", total)
    print("📄 Yol:", OUT_FILE)

if __name__ == "__main__":
    main()
