import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

print("🧬 Sistem B başlatılıyor: GraphRAG + Semantik Katman")

soru = "Ahmet Yılmaz kredi alabilir mi?"

with driver.session() as session:
    sorgu = """
    MATCH (m:Musteri {ad_soyad: "Ahmet Yılmaz"})
          -[r1:GIZLI_ORTAK|FONLAYICI]->
          (s:Sirket)
          -[r2:KREDI_KULLANDI]->
          (k:Kredi {durum: "Gecikmede"})
    RETURN
        m.ad_soyad AS Musteri,
        type(r1) AS Iliski1,
        s.sirket_adi AS Sirket,
        type(r2) AS Iliski2,
        k.id AS KrediID,
        k.durum AS Durum,
        k.miktar_tl AS Miktar
    """

    sonuclar = session.run(sorgu).data()

print("\n==============================================")
print("🔹 SİSTEM B: GRAPHRAG + SEMANTİK KATMAN")
print("==============================================")

print(f"\nSoru: {soru}")

if sonuclar:
    print("\nGraphRAG tarafından keşfedilen risk zinciri:")

    for kayit in sonuclar:
        print(
            f"{kayit['Musteri']} "
            f"→ {kayit['Iliski1']} "
            f"→ {kayit['Sirket']} "
            f"→ {kayit['Iliski2']} "
            f"→ {kayit['KrediID']} "
            f"({kayit['Durum']})"
        )

    print("\nKarar:")
    print("❌ KREDİ KESİNLİKLE REDDEDİLMELİDİR")

    print("\nAçıklama:")
    print(
        "GraphRAG yalnızca müşterinin bireysel kaydına bakmadı. "
        "Müşteri ile şirketler arasındaki ilişkileri ve bu şirketlerin kredi durumlarını birlikte analiz etti. "
        "Ahmet Yılmaz'ın görünürde düşük riskli olmasına rağmen, Beta İnşaat üzerinden gecikmedeki K_901 kredisine dolaylı olarak bağlı olduğu tespit edildi."
    )

else:
    print("\nGraph üzerinde gecikmedeki krediye bağlanan dolaylı risk bulunamadı.")

    print("\nKarar:")
    print("✅ KREDİ ONAYLANABİLİR")

driver.close()