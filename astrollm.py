# ============================================================
# astrollm.py – ASTROLLM PRO CLI
# ============================================================

import sys
import time
import random
from datetime import datetime

# ✅ SADECE AstroLLM import edilir
from astrollmmodule import AstroLLM
from tiny_transformer import TinyTransformer

# ============================================================
# SAFE INPUT
# ============================================================

def safe_input(prompt="> "):
    try:
        sys.stdout.write(prompt)
        sys.stdout.flush()
        data = sys.stdin.readline()
        if not data:
            return ""
        data = data.encode("utf-8", errors="ignore").decode("utf-8")
        return data.strip()
    except Exception:
        return ""

sys.stdin = open(0)

# ============================================================
# INIT
# ============================================================

LLM = AstroLLM()
TT = TinyTransformer()

# ============================================================
# ASTEROID SIMULATION (IDENTITY + HISTORY)
# ============================================================

ASTEROID_PROFILES = [
    {"name": "Apophis", "risk": 88},
    {"name": "Bennu", "risk": 65},
    {"name": "Didymos", "risk": 40},
    {"name": "Toutatis", "risk": 55},
]

RISK_HISTORY = []


def generate_asteroids():
    asteroids = []

    for i in range(random.randint(2, 4)):
        base = random.choice(ASTEROID_PROFILES)
        risk = max(5, min(95, base["risk"] + random.randint(-10, 10)))

        asteroid = {
            "id": f"NEO-{2025+i}",
            "name": f"AST-{1000+i}",
            "risk": risk,
            "speed_ra": random.uniform(0.1, 1.2),
            "speed_dec": random.uniform(0.01, 0.12),
            "profile": base["name"],
            "source": "SIMULATED",

            # 🧠 AstroLLM içinde kullanılacak
            "vector": [risk / 100, base["risk"] / 100, 1.0],
            "time_distance": len(RISK_HISTORY)
        }

        asteroids.append(asteroid)

    RISK_HISTORY.append(max(a["risk"] for a in asteroids))
    return asteroids

# ============================================================
# HELP
# ============================================================

def help_menu():
    print("""
Komutlar:
 canli        → Canlı simülasyon
 harita       → 2D çarpışma görseli
 grafik       → Risk zaman grafiği
 neden        → Risk nedenleri
 benzer       → Hangi asteroidlere benziyor
 gercek       → Veri gerçeklik analizi
 tahmin       → 6 saatlik senaryo
 rapor        → Bilimsel metin
 sor <soru>   → AstroLLM soru-cevap
 yardim       → Yardım menüsü
 cikis        → Çıkış
""")

# ============================================================
# LIVE MODE
# ============================================================

def live_mode():
    print("Canlı analiz başladı (CTRL+C ile çık)\n")

    try:
        while True:
            asteroids = generate_asteroids()
            LLM.update_live_data(asteroids)

            print("Canlı Analiz:")

            for a in asteroids:
                yorum = TT.generate_live_comment(a["name"])
                print(f"{a['name']} | RİSK {a['risk']} → {yorum}")

            print("-" * 45)
            time.sleep(3)

    except KeyboardInterrupt:
        print("\nCanlı analiz durduruldu\n")

# ============================================================
# 2D MAP
# ============================================================

def harita_mode():
    a = LLM.context.most_risky()
    if not a:
        print("Veri yok.")
        return

    print("\n2D Uzay Haritası (Tahmini Çarpışma)\n")
    print(".....................")
    print("........☄️...........")
    print("............🌍......")
    print(".....................")
    print(".....................\n")
    print(f"Olası çarpma adayı: {a['name']}")
    print(f"Risk: {a['risk']}\n")

# ============================================================
# GRAPH
# ============================================================

def grafik_mode():
    print("\nRisk Zaman Grafiği:\n")
    for i, r in enumerate(RISK_HISTORY[-10:]):
        bar = "#" * (r // 5)
        print(f"T+{i:02d} | {bar} {r}")
    print("")

# ============================================================
# WHY
# ============================================================

def neden_mode():
    a = LLM.context.most_risky()
    if not a:
        print("Veri yok.")
        return

    print("\nRisk Analizi:")
    print("- Açısal hız etkisi")
    print("- Yörünge sapması")
    print("- Dünya yörüngesi kesişimi")
    print("- Attention + Radio Beam etkisi")
    print(f"Toplam Risk: {a['risk']}\n")

# ============================================================
# SIMILARITY
# ============================================================

def benzer_mode():
    a = LLM.context.most_risky()
    if not a:
        print("Veri yok.")
        return

    print("\nBenzerlik Analizi:")
    print(f"{a['name']} → {a['profile']} benzeri")
    print(f"Benzerlik oranı: %{60 + random.randint(0, 30)}\n")

# ============================================================
# REALITY CHECK
# ============================================================

def gercek_mode():
    print("\nVeri Gerçeklik Analizi:")
    print("Kaynak: Simülasyon")
    print("Gerçeklik Skoru: %42")
    print("Model: AstroLLM (Attention + RadioBeam)")
    print("Uyarı: Bu sistem bilimsel simülasyon amaçlıdır.\n")

# ============================================================
# FUTURE SCENARIO
# ============================================================

def tahmin_mode():
    a = LLM.context.most_risky()
    if not a:
        print("Veri yok.")
        return

    print("\n6 Saatlik Senaryo:")
    for h in range(1, 7):
        print(f"T+{h} saat → Risk {min(99, a['risk'] + h * 2)}")
    print("")

# ============================================================
# REPORT
# ============================================================

def rapor_mode():
    a = LLM.context.most_risky()
    if not a:
        print("Veri yok.")
        return

    print("\nBİLİMSEL RAPOR\n")
    print(TT.generate_report(a["name"], a["risk"]))
    print("Model: AstroLLM + TinyTransformer\n")

# ============================================================
# MAIN LOOP
# ============================================================

def main():
    print(GOSHAWK_LOGO)
    print("AstroLLM – Professional Analysis Engine Prototype")
    print("© Goshawk Vortex.AI\n")
    help_menu()

    while True:
        cmd = safe_input("> ")

        if cmd == "canli":
            live_mode()
        elif cmd == "harita":
            harita_mode()
        elif cmd == "grafik":
            grafik_mode()
        elif cmd == "neden":
            neden_mode()
        elif cmd == "benzer":
            benzer_mode()
        elif cmd == "gercek":
            gercek_mode()
        elif cmd == "tahmin":
            tahmin_mode()
        elif cmd == "rapor":
            rapor_mode()
        elif cmd.startswith("sor "):
            print("LLM:", LLM.ask(cmd[4:]))
        elif cmd == "yardim":
            help_menu()
        elif cmd == "cikis":
            print("Çıkılıyor")
            break
        else:
            print("Bilinmeyen komut")

# ============================================================
# ENTRY
# ============================================================

if __name__ == "__main__":
    main()