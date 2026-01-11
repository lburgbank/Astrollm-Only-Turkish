# ============================================================
# tiny_transformer.py – ULTRA LIGHT TR TRANSFORMER
# PyramidIDE Safe | No Torch | No TF
# ============================================================

import random

class TinyTransformer:
    """
    Mini-Transformer (şablon tabanlı dil düzenleyici)
    Girdi: teknik / ham çıktı
    Çıktı: düzgün Türkçe bilimsel anlatım
    """

    def __init__(self):
        self.templates = {
            "rapor": [
                "Son analizlere göre {name} adlı gök cismi, {risk} risk seviyesi ile izlenmektedir.",
                "{name}, mevcut veriler ışığında {risk} seviyesinde bir tehdit oluşturmaktadır.",
                "Bilimsel değerlendirme, {name} için risk seviyesinin {risk} olduğunu göstermektedir."
            ],
            "canli": [
                "{name}, yörüngesel parametreleri nedeniyle dikkatle takip edilmektedir.",
                "{name}, hız ve yörünge sapmaları sebebiyle izleme altındadır.",
                "{name}, mevcut hareket verileri doğrultusunda riskli kabul edilmektedir."
            ],
            "trend": [
                "Sistem genelinde risk seviyesinde artış gözlemlenmektedir.",
                "Veriler, risk değerlerinde dalgalı bir seyir olduğunu göstermektedir.",
                "Son ölçümler, risk seviyesinin stabil kaldığını işaret etmektedir."
            ]
        }

    def generate_report(self, name, risk):
        tpl = random.choice(self.templates["rapor"])
        return tpl.format(name=name, risk=risk)

    def generate_live_comment(self, name):
        tpl = random.choice(self.templates["canli"])
        return tpl.format(name=name)

    def generate_trend(self, trend):
        if trend == "artan risk":
            return self.templates["trend"][0]
        if trend == "dalgalı":
            return self.templates["trend"][1]
        return self.templates["trend"][2]

    def generate_by_mode(self, mode, name="AST", risk=0, trend=None):
        """
        Genel dispatcher – intent / mod bazlı çıktı
        """
        if mode == "rapor":
            return self.generate_report(name, risk)
        if mode == "canli":
            return self.generate_live_comment(name)
        if mode == "trend":
            return self.generate_trend(trend or "")
        return f"{name} izleniyor."