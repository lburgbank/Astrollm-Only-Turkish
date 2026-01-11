# Astrollm-Only-Turkish
AstroLLM, klasik büyük dil modellerinin (LLM) sınırlamalarını bilinçli şekilde kabul eden; simülasyon, kural tabanlı mantık ve hafif LLM bileşenlerini birleştiren hibrit bir analiz ve karar motoru prototipidir.

AstroLLM, dil modeli tabanlı sistemlerin kontrolsüz doğasını bilinçli olarak sınırlayan, hibrit ve açıklanabilir bir mimari sunar.
🔹 Mimari Özellikler
Hibrit Karar Motoru
Simülasyon + kural tabanlı mantık + hafif LLM bileşenleri birlikte çalışır.
LLM Kontrollü Kullanım
Dil modeli her soruya cevap vermez; yalnızca uygun bağlamlarda devreye girer.
Açıklanabilirlik Öncelikli Tasarım
“Sonuç” kadar “neden” de önemlidir.
Offline ve Hafif Çalışma
Torch, GPU veya ağır bağımlılıklar yoktur.
CLI Odaklı Kullanım
Terminal üzerinden net ve deterministik çıktılar üretir.
🔹 Analiz Özellikleri
📡 Radio Beam Mekanizması
Uzaktan fakat anlamlı sinyallerin bağlamsal etkisini hesaplar.
🧠 Attention Skorlama
Niyet, bağlam ve zaman faktörlerini birlikte değerlendirir.
📈 Trend ve Senaryo Analizi
Zaman içinde risk değişimlerini gözlemler.
🗂️ Bellek (Memory) Yönetimi
Kısa ve orta vadeli gözlem geçmişi tutulur.
🔁 Tekrar Önleme & Metin Temizleme
Aynı cevapların tekrar edilmesi engellenir, çıktılar sadeleştirilir.
🧪 Kullanım
AstroLLM bir CLI prototipidir ve etkileşimli şekilde çalışır.
🔧 Başlatma
Kodu kopyala
Bash
python astrollm.py
Başlangıçta sistem durumu ve yardım menüsü görüntülenir.
📌 Temel Komutlar
Komut
Açıklama
canli
Canlı simülasyon başlatır
harita
2D çarpışma görselleştirmesi (ASCII)
grafik
Zaman–risk grafiği
neden
Risk faktörlerini açıklar
tahmin
Kısa vadeli senaryo üretir
rapor
Bilimsel formatta rapor
beam
Radio Beam analizini gösterir
sor <soru>
LLM destekli açıklama alır
yardim
Komut listesini gösterir
cikis
Programdan çıkar
🧠 Örnek Kullanım
Kodu kopyala
Text
> canli
AST-1001 | RİSK 64 📡 → izleme altındadır

> neden
- Açısal hız etkisi
- Yörünge sapması
- Attention + Radio Beam etkisi

> sor bu risk neden önemli
Bilgiye göre:
- Nesnenin yörüngesi kısa vadede dalgalı risk göstermektedir.
🧱 Mimari Genel Bakış
AstroLLM tek bir “akıllı model” yerine katmanlı bir yapı kullanır.
🧠 Karar Akışı
Simülasyon Katmanı
Olay ve senaryo verileri üretilir.
Kural Tabanlı Mantık
Temel risk ve eşik kontrolleri yapılır.
Attention & Radio Beam
Bağlam, önem ve zaman etkileri hesaplanır.
Bellek ve Trend Analizi
Geçmiş durumlar değerlendirilir.
LLM (Opsiyonel)
Yalnızca açıklama ve özetleme için devreye girer.
CLI Çıktısı
Deterministik ve açıklanabilir sonuç sunulur.
Bu yapı sayesinde sistem halüsinasyon üretmez,
çünkü LLM karar verici değil, yardımcı bileşendir.
⚠️ Önemli Not
AstroLLM:
Bir araştırma ve mimari prototiptir
Gerçek dünyada risk, güvenlik veya bilimsel tahmin aracı olarak kullanılmamalıdır
Ama açıklanabilir AI sistemleri için güçlü bir referans sunar
