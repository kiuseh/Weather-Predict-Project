import sqlite3 as sql

conn = sql.connect("/home/kiuseh/Masaüstü/python/websraping_2/dataBase.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS DATABASE (
    saat INTEGER,
    sicaklik integer,
    yagis_oranı INTEGER,
    ruzgar INTEGER,
    ruzgar_yonu string,
    hissedilen_sicaklik INTEGER,
    nem INTEGER,
    uv_indeksi INTEGER,
    bulut_ortusu INTEGER,
    yagmur_miktari INTEGER,
    kontrol INTEGER
)
""")

def insert(saat, sicaklik, yagis, ruzgar,ruzgar_yonu, hissedilen, nem, uv, bulut, yagmur, kontrol =0):
    conn = sql.connect("/home/kiuseh/Masaüstü/python/websraping_2/dataBase.db")
    cursor = conn.cursor()

    add_command = "INSERT INTO DATABASE VALUES (?,?,?,?,?,?,?,?,?,?,?)"
    data = (saat,sicaklik,yagis, ruzgar,ruzgar_yonu,hissedilen,nem,uv,bulut,yagmur,kontrol)
    cursor.execute(add_command, data)

    conn.commit()
    conn.close()

conn.commit()
conn.close()