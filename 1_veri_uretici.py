import pandas as pd
from faker import Faker

fake = Faker("tr_TR")

# 1) MÜŞTERİLER
musteriler = [
    {
        "MusteriID": "M_101",
        "Ad_Soyad": "Ahmet Yılmaz",
        "Risk_Skoru": "Düşük",
        "Meslek": "Yatırımcı",
        "Gelir_Durumu": "Yüksek"
    }
]

for i in range(102, 111):
    musteriler.append({
        "MusteriID": f"M_{i}",
        "Ad_Soyad": fake.name(),
        "Risk_Skoru": fake.random_element(["Düşük", "Orta", "Yüksek"]),
        "Meslek": fake.job(),
        "Gelir_Durumu": fake.random_element(["Düşük", "Orta", "Yüksek"])
    })

# 2) ŞİRKETLER
sirketler = [
    {"SirketID": "S_501", "Sirket_Adi": "Alfa Lojistik A.Ş.", "Sektor": "Lojistik", "Yillik_Ciro_TL": 45000000},
    {"SirketID": "S_502", "Sirket_Adi": "Beta İnşaat", "Sektor": "İnşaat", "Yillik_Ciro_TL": 62000000},
    {"SirketID": "S_503", "Sirket_Adi": "Gama Teknoloji", "Sektor": "Teknoloji", "Yillik_Ciro_TL": 28000000},
]

for i in range(504, 516):
    sirketler.append({
        "SirketID": f"S_{i}",
        "Sirket_Adi": fake.company(),
        "Sektor": fake.random_element(["Lojistik", "İnşaat", "Teknoloji", "Enerji", "Gıda", "Tekstil"]),
        "Yillik_Ciro_TL": fake.random_int(min=5_000_000, max=100_000_000)
    })

# 3) KREDİLER
krediler = [
    {"KrediID": "K_901", "Kredi_Turu": "Ticari Kredi", "Miktar_TL": 15000000, "Durum": "Gecikmede"},
]

for i in range(902, 926):
    krediler.append({
        "KrediID": f"K_{i}",
        "Kredi_Turu": fake.random_element(["Ticari Kredi", "Proje Finansmanı", "İşletme Kredisi"]),
        "Miktar_TL": fake.random_int(min=1_000_000, max=30_000_000),
        "Durum": fake.random_element(["Canlı", "Canlı", "Canlı", "Gecikmede"])
    })

# 4) İLİŞKİLER
iliskiler = [
    # Ana test senaryosu:
    # Ahmet Yılmaz düşük riskli görünür ama Beta İnşaat üzerinden gecikmedeki K_901 kredisine bağlıdır.
    {"KaynakID": "M_101", "HedefID": "S_502", "Iliski_Turu": "GIZLI_ORTAK", "Detay": "Ahmet Yılmaz'ın Beta İnşaat üzerinde dolaylı ortaklığı vardır."},
    {"KaynakID": "S_502", "HedefID": "K_901", "Iliski_Turu": "KREDI_KULLANDI", "Detay": "Beta İnşaat gecikmedeki K_901 kredisini kullanmıştır."},
]

# Diğer sentetik ilişkiler
for i in range(102, 111):
    iliskiler.append({
        "KaynakID": f"M_{i}",
        "HedefID": f"S_{500 + (i - 100)}",
        "Iliski_Turu": fake.random_element(["GIZLI_ORTAK", "FONLAYICI"]),
        "Detay": "Sentetik müşteri-şirket ilişkisi."
    })

for i in range(502, 516):
    kredi_no = 900 + (i - 500)
    iliskiler.append({
        "KaynakID": f"S_{i}",
        "HedefID": f"K_{kredi_no}",
        "Iliski_Turu": "KREDI_KULLANDI",
        "Detay": "Sentetik şirket-kredi ilişkisi."
    })

# 5) VECTOR RAG İÇİN DÜZ METİN BELGELERİ
metinler = [
    {
        "BelgeID": "B_001",
        "Metin_Icerigi": "Ahmet Yılmaz bireysel kayıtlara göre düşük risk skorlu, yüksek gelirli bir yatırımcıdır. Bu nedenle geleneksel değerlendirmede kredi onaylanabilir görünmektedir."
    },
    {
        "BelgeID": "B_002",
        "Metin_Icerigi": "Beta İnşaat inşaat sektöründe faaliyet gösteren bir şirkettir. Şirketin K_901 numaralı ticari kredisi gecikmededir."
    },
    {
        "BelgeID": "B_003",
        "Metin_Icerigi": "Bu veri seti, geleneksel Vector RAG ile GraphRAG yaklaşımını karşılaştırmak için oluşturulmuş sentetik bir bankacılık risk senaryosudur."
    }
]

# 6) EXCEL DOSYALARINA KAYDET
pd.DataFrame(musteriler).to_excel("node_musteriler.xlsx", index=False)
pd.DataFrame(sirketler).to_excel("node_sirketler.xlsx", index=False)
pd.DataFrame(krediler).to_excel("node_krediler.xlsx", index=False)
pd.DataFrame(iliskiler).to_excel("edges_iliskiler.xlsx", index=False)
pd.DataFrame(metinler).to_excel("duz_metin_verisi.xlsx", index=False)

print("✅ Sentetik veri seti başarıyla üretildi.")
print("📌 10 müşteri, 15 şirket, 25 kredi ve ilişkiler oluşturuldu.")
print("🎯 Ana test zinciri: Ahmet Yılmaz → Beta İnşaat → K_901 → Gecikmede")