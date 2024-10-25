from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Headless mod ayarları
chrome_options = Options()
chrome_options.add_argument("--headless")  # Headless mod
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")  # Kaynak sı

# ChromeDriver'ı başlat
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Web sitesini aç
driver.get("https://weather.com/tr-TR/weather/hourbyhour/l/5b85ae18405d31f1090f8b0e083c31ce49073f59045ce9d03ab9cff851f3bf31")

# Sayfa kaynağını al
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

# saat
saatVeri = soup.find("h2", attrs={"class": "DetailsSummary--daypartName--kbngc"})
saat = saatVeri.text.split(":")[0]
#print("saat:",saat)

# sıcaklık
sicaklikVeri = soup.find("span", attrs={"class": "DetailsSummary--tempValue--jEiXE"})
sicaklik = sicaklikVeri.text[:-1]
#print("sicaklık:",sicaklik)

# yağış oranı
yagisOraniVeri = soup.find("span", attrs={"data-testid": "PercentageValue"})
yagisOrani = yagisOraniVeri.text[:-1]
#print("yağış oranı:",yagisOrani)

# Diğer veriler (alttaki tablo verileri)
altiVeri = soup.find_all("span", attrs={"class": "DetailsTable--value--2YD0-"})

# hissedilen sıcaklık
hissedilenSicaklik = altiVeri[0].text[:-1]
#print("hissedilen sıcaklık:", hissedilenSicaklik)

# rüzgar
end = altiVeri[1].text.split(" ")[1].find("km/s")
ruzgar = int(altiVeri[1].text.split(" ")[1][:end])
#print("rüzgar hızı:", ruzgar)

# rüzgar yönü
ruzgarYonu = altiVeri[1].text.split(" ")[0]
#print("rüzgar yönü:", ruzgarYonu)

# nem
nem = int(altiVeri[2].text[:-1])
#print("nem:", nem)

# uv
uv = int(altiVeri[3].text.split(" ")[0])
#print("uv:", uv)

# bulut örtüsü
bulutOrtusu = int(altiVeri[4].text[:-1])
#print("bulut örtüsü:", bulutOrtusu)

# yağmur miktarı
yagmurMiktari = float(altiVeri[5].text.strip()[:-2])
#print("yağmur miktarı:", yagmurMiktari)

# WebDriver'ı kapat
driver.quit()

print(yagmurMiktari)