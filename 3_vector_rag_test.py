from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

print("🧠 Hugging Face modeli yükleniyor...")

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

df = pd.read_excel("duz_metin_verisi.xlsx")

metinler = df["Metin_Icerigi"].tolist()

print("📚 Metinler vektörlere dönüştürülüyor...")

vektorler = model.encode(metinler)

print()
print("✅ Toplam belge sayısı:", len(metinler))
print("✅ Vektör boyutu:", len(vektorler[0]))
print()
print("İlk belgenin ilk 10 değeri:")
print(vektorler[0][:10])