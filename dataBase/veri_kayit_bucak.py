from verileri_cekme_bucak import *
from veriMerkezi_bucak import *
import time
import schedule
from datetime import datetime
import os, sys
import smtplib
from email.message import EmailMessage

def send_email(subject, body, to_email):
    # Gmail SMTP sunucu ayarları
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'kiris.h.sefa@gmail.com'  # Buraya kendi Gmail adresinizi girin
    smtp_password = 'bmkl dvoh nuyb rush'  # Buraya kendi Gmail şifrenizi girin

    # E-posta mesajı oluşturma
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = to_email

    # E-posta gönderme
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # TLS ile güvenli bağlantı
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

# E-posta içeriği oluştur


def verileriKaydet():   
    email_subject = "Veri Kaydedildi"
    email_body = (f"Bucak Verileri:\n"
              f"Saat: {saat}\n"
              f"Sıcaklık: {sicaklik}°C\n"
              f"Yağış Oranı: {yagisOrani}%\n"
              f"Rüzgar: {ruzgar} km/h\n"
              f"Rüzgar Yönü: {ruzgarYonu}\n"
              f"Hissedilen Sıcaklık: {hissedilenSicaklik}°C\n"
              f"Nem: {nem}%\n"
              f"UV: {uv}\n"
              f"Bulut Ortalaması: {bulutOrtusu}\n"
              f"Yağmur Miktarı: {yagmurMiktari} mm")
    insert(saat,sicaklik,yagisOrani,ruzgar,ruzgarYonu,hissedilenSicaklik,nem,uv,bulutOrtusu,yagmurMiktari)
    
    send_email(email_subject, email_body, 'kiris.h.sefa@gmail.com')

verileriKaydet()
