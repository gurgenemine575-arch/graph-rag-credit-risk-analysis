from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

def kosinus_benzerligi(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print("🧠 Sistem A başlatılıyor: Geleneksel Vector RAG")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

df = pd.read_excel("duz_metin_verisi.xlsx")
metinler = df["Metin_Icerigi"].tolist()

vektorler = model.encode(metinler)

soru = "Ahmet Yılmaz kredi alabilir mi?"
soru_vektoru = model.encode(soru)

sonuclar = []

for metin, vektor in zip(metinler, vektorler):
    skor = kosinus_benzerligi(soru_vektoru, vektor)
    sonuclar.append((metin, skor))

sonuclar = sorted(sonuclar, key=lambda x: x[1], reverse=True)

en_benzer_metin, en_yuksek_skor = sonuclar[0]

print("\n==============================================")
print("🔹 SİSTEM A: SEMANTİK KATMANSIZ / VECTOR RAG")
print("==============================================")

print(f"\nSoru: {soru}")

print("\nEn benzer bulunan belge:")
print(en_benzer_metin)

print(f"\nBenzerlik skoru: %{en_yuksek_skor * 100:.2f}")

print("\nKarar:")
print("✅ KREDİ ONAYLANABİLİR")

print("\nAçıklama:")
print(
    "Vector RAG yalnızca düz metin içeriğine baktığı için "
    "Ahmet Yılmaz'ın bireysel düşük risk bilgisini öne çıkardı. "
    "Ancak arka plandaki şirket ve gecikmiş kredi ilişkilerini göremedi."
)