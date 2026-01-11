# ============================================================
# Advanced Intent Model – 1000–5000+ Intent READY (FINAL)
# Offline • Free • CSV Train • Explainable • Android Friendly
# ============================================================

import csv
import os
import math
import numpy as np
from collections import defaultdict


class AdvancedIntentModel:
    """
    Gelişmiş Intent Sınıflandırıcı

    Özellikler:
    - 1000–5000+ intent
    - CSV tabanlı eğitim (train.csv)
    - TF-IDF benzeri ağırlıklandırma
    - N-gram bağlam
    - Confidence + unknown intent
    """

    # --------------------------------------------------------
    # INIT
    # --------------------------------------------------------
    def __init__(
        self,
        intents,
        vocab_size=30000,
        hidden_dim=256,
        ngram_range=(1, 2),
        unknown_threshold=0.40,
        seed=42,
    ):
        np.random.seed(seed)

        self.intents = intents
        self.intent_to_id = {i: idx for idx, i in enumerate(intents)}
        self.id_to_intent = {idx: i for i, idx in self.intent_to_id.items()}
        self.num_intents = len(intents)

        # ---- VOCAB ----
        self.vocab = {}
        self.idf = defaultdict(lambda: 1.0)
        self.next_id = 0
        self.vocab_size = vocab_size

        self.ngram_range = ngram_range
        self.unknown_threshold = unknown_threshold

        # ---- MODEL ----
        self.W1 = np.random.randn(vocab_size, hidden_dim).astype(np.float32) * 0.01
        self.b1 = np.zeros(hidden_dim, dtype=np.float32)

        self.W2 = np.random.randn(hidden_dim, self.num_intents).astype(np.float32) * 0.01
        self.b2 = np.zeros(self.num_intents, dtype=np.float32)

        # ---- STATS ----
        self.total_samples = 0

    # --------------------------------------------------------
    # TOKENIZATION
    # --------------------------------------------------------
    def tokenize(self, text):
        return [
            t.strip(".,!?()[]{}<>").lower()
            for t in text.split()
            if len(t) > 1
        ]

    def build_ngrams(self, tokens):
        feats = []
        for n in range(self.ngram_range[0], self.ngram_range[1] + 1):
            for i in range(len(tokens) - n + 1):
                feats.append("_".join(tokens[i:i+n]))
        return feats

    # --------------------------------------------------------
    # VECTORIZE (TF-IDF LIKE)
    # --------------------------------------------------------
    def vectorize(self, text):
        vec = np.zeros(self.vocab_size, dtype=np.float32)

        tokens = self.tokenize(text)
        features = tokens + self.build_ngrams(tokens)

        seen = set()

        for f in features:
            if f not in self.vocab:
                if self.next_id >= self.vocab_size:
                    continue
                self.vocab[f] = self.next_id
                self.next_id += 1

            idx = self.vocab[f]
            vec[idx] += 1.0

            if f not in seen:
                self.idf[f] += 1.0
                seen.add(f)

        # ---- IDF & NORMALIZE ----
        for f in seen:
            idx = self.vocab[f]
            vec[idx] *= math.log(1 + self.total_samples / self.idf[f])

        norm = np.linalg.norm(vec)
        if norm > 0:
            vec /= norm

        return vec

    # --------------------------------------------------------
    # FORWARD
    # --------------------------------------------------------
    def forward(self, x):
        h = np.maximum(0, x @ self.W1 + self.b1)
        return h @ self.W2 + self.b2

    def softmax(self, z):
        z = z - np.max(z)
        exp = np.exp(z)
        return exp / (np.sum(exp) + 1e-9)

    # --------------------------------------------------------
    # CSV TRAIN LOADER
    # --------------------------------------------------------
    def load_train_csv(self, path):
        """
        CSV format:
        text,intent
        """
        samples = []

        if not os.path.exists(path):
            raise FileNotFoundError(f"train.csv bulunamadı: {path}")

        with open(path, encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 2:
                    continue
                text, intent = row[0].strip(), row[1].strip()
                if text and intent:
                    samples.append((text, intent))

        return samples

    # --------------------------------------------------------
    # TRAIN
    # --------------------------------------------------------
    def train(self, samples, lr=0.01, epochs=5, verbose=True):
        for epoch in range(epochs):
            np.random.shuffle(samples)
            loss_sum = 0.0

            for text, label in samples:
                if label not in self.intent_to_id:
                    continue

                x = self.vectorize(text)

                y = np.zeros(self.num_intents, dtype=np.float32)
                y[self.intent_to_id[label]] = 1.0

                logits = self.forward(x)
                probs = self.softmax(logits)

                loss = -np.sum(y * np.log(probs + 1e-9))
                loss_sum += loss

                grad_logits = probs - y
                h = np.maximum(0, x @ self.W1 + self.b1)

                self.W2 -= lr * np.outer(h, grad_logits)
                self.b2 -= lr * grad_logits

                grad_h = self.W2 @ grad_logits
                grad_h[h <= 0] = 0

                self.W1 -= lr * np.outer(x, grad_h)
                self.b1 -= lr * grad_h

                self.total_samples += 1

            if verbose:
                print(f"[epoch {epoch+1}] loss={loss_sum/max(len(samples),1):.4f}")

    # --------------------------------------------------------
    # PREDICT
    # --------------------------------------------------------
    def predict(self, text):
        x = self.vectorize(text)
        logits = self.forward(x)
        probs = self.softmax(logits)

        best_id = int(np.argmax(probs))
        confidence = float(probs[best_id])

        if confidence < self.unknown_threshold:
            return "unknown", confidence

        return self.id_to_intent[best_id], confidence


# ============================================================
# SELF TEST
# ============================================================
if __name__ == "__main__":

    INTENTS = [f"intent_{i}" for i in range(5000)]
    INTENTS[0] = "asteroid_risk"
    INTENTS[1] = "planet_size"
    INTENTS[2] = "is_real"
    INTENTS[3] = "how_it_works"
    INTENTS[-1] = "unknown"

    model = AdvancedIntentModel(INTENTS)

    TRAIN_PATH = "/storage/emulated/0/astrollm/dataset/train.csv"
    samples = model.load_train_csv(TRAIN_PATH)

    model.train(samples, epochs=10)

    tests = [
        "en tehlikeli asteroid hangisi",
        "dünyanın çapı kaç km",
        "bu sistem gerçek mi",
        "nasıl çalışıyor",
        "alakasız soru"
    ]

    for t in tests:
        intent, conf = model.predict(t)
        print(f"{t} -> {intent} ({conf:.2f})")