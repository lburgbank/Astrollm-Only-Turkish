# ============================================================
# mini_attention.py – LIGHT ATTENTION SCORER
# Context-aware | Offline | AstroLLM uyumlu
# ============================================================

class MiniAttention:
    def __init__(self):
        self.weights = {
            "intent": 2.0,
            "context": 1.5,
            "recency": 1.0,
            "length": 0.3,
        }

    def score(self, candidate, intent=None, context=None, recency=0):
        score = 0.0

        # Intent uyumu
        if intent and intent in candidate.lower():
            score += self.weights["intent"]

        # Context uyumu (asteroid adı vs.)
        if context:
            for key in context:
                if key.lower() in candidate.lower():
                    score += self.weights["context"]

        # Son cevaplardan kaçınma
        score -= recency * self.weights["recency"]

        # Çok kısa / çok uzun ceza
        score -= abs(len(candidate) - 120) * self.weights["length"] / 100

        return score

    def select_best(self, candidates, intent=None, context=None, history=None):
        if not candidates:
            return None

        history = history or []
        scored = []

        for c in candidates:
            recency = history.count(c)
            s = self.score(c, intent, context, recency)
            scored.append((s, c))

        scored.sort(key=lambda x: x[0], reverse=True)
        return scored[0][1]