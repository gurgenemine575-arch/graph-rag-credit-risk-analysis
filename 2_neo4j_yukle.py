import os
import pandas as pd
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

def verileri_yukle():
    df_musteriler = pd.read_excel("node_musteriler.xlsx")
    df_sirketler = pd.read_excel("node_sirketler.xlsx")
    df_krediler = pd.read_excel("node_krediler.xlsx")
    df_iliskiler = pd.read_excel("edges_iliskiler.xlsx")

    with driver.session() as session:
        # Temiz PoC için eski test verilerini siliyoruz
                # session.run("MATCH (n) DETACH DELETE n")

        for _, row in df_musteriler.iterrows():
            session.run("""
                CREATE (:Musteri {
                    id: $id,
                    ad_soyad: $ad_soyad,
                    risk_skoru: $risk_skoru,
                    meslek: $meslek,
                    gelir_durumu: $gelir_durumu
                })
            """,
            id=row["MusteriID"],
            ad_soyad=row["Ad_Soyad"],
            risk_skoru=row["Risk_Skoru"],
            meslek=row["Meslek"],
            gelir_durumu=row["Gelir_Durumu"])

        for _, row in df_sirketler.iterrows():
            session.run("""
                CREATE (:Sirket {
                    id: $id,
                    sirket_adi: $sirket_adi,
                    sektor: $sektor,
                    yillik_ciro_tl: $yillik_ciro_tl
                })
            """,
            id=row["SirketID"],
            sirket_adi=row["Sirket_Adi"],
            sektor=row["Sektor"],
            yillik_ciro_tl=int(row["Yillik_Ciro_TL"]))

        for _, row in df_krediler.iterrows():
            session.run("""
                CREATE (:Kredi {
                    id: $id,
                    kredi_turu: $kredi_turu,
                    miktar_tl: $miktar_tl,
                    durum: $durum
                })
            """,
            id=row["KrediID"],
            kredi_turu=row["Kredi_Turu"],
            miktar_tl=int(row["Miktar_TL"]),
            durum=row["Durum"])

        for _, row in df_iliskiler.iterrows():
            iliski_turu = row["Iliski_Turu"]

            sorgu = f"""
                MATCH (kaynak {{id: $kaynak_id}})
                MATCH (hedef {{id: $hedef_id}})
                CREATE (kaynak)-[:{iliski_turu} {{
                    detay: $detay
                }}]->(hedef)
            """

            session.run(
                sorgu,
                kaynak_id=row["KaynakID"],
                hedef_id=row["HedefID"],
                detay=row["Detay"]
            )

    print("✅ Veriler Neo4j Aura'ya başarıyla yüklendi.")
    print("📌 Node tipleri: Musteri, Sirket, Kredi")
    print("🔗 İlişkiler: GIZLI_ORTAK, FONLAYICI, KREDI_KULLANDI")
    print("🎯 Ana zincir: Ahmet Yılmaz → Beta İnşaat → K_901 → Gecikmede")

if __name__ == "__main__":
    verileri_yukle()
    driver.close()