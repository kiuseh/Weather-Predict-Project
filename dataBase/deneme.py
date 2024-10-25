import smtplib
from email.message import EmailMessage
import time
import schedule
from datetime import datetime
import os, sys

def send_email(subject, body, to_email):
    # Gmail SMTP sunucu ayarları
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'kiris.h.sefa@gmail.com'  # Buraya kendi Gmail adresinizi girin
    smtp_password = 'jyjp yncx aizg pdbj '  # Buraya kendi Gmail şifrenizi girin

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

# Verilerinizi al
saat = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
sicaklik = 25  # Örnek veri
yagisOrani = 5  # Örnek veri
ruzgar = 15  # Örnek veri
ruzgarYonu = 'Kuzey'  # Örnek veri
hissedilenSicaklik = 24  # Örnek veri
nem = 60  # Örnek veri
uv = 3  # Örnek veri
bulutOrtusu = 2  # Örnek veri
yagmurMiktari = 0  # Örnek veri


# E-posta içeriği oluştur
email_subject = "Veri Kaydedildi"
email_body = ("hello world")

# E-posta gönder
send_email(email_subject, email_body, 'kiris.h.sefa@gmail.com')
print("E-posta gönderildi: Saat , Sıcaklık: , Yağış Oranı: , Rüzgar: ")
