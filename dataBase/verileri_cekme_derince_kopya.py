from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://weather.com/tr-TR/weather/hourbyhour/l/647b74d133cf0335fbeb89f912003613dc27a784361c82bd9f5b17b6dd5eb0c5")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

tablo = soup.find_all("div", attrs={"class":"HourlyForecast--DisclosureList--MQWP6"})

# Listeler
hissedilen = []
ruzgar = []
ruzgar_yonu = []
nem = []
uv = []
bulutOrtusu = []
yagmurMiktari = []
veriler = []
saat = []
sicaklik = []
yagisOrani = []

# 6 veri
for i in tablo:
    hissedilenToplu = i.find_all("span", attrs={"class":"DetailsTable--value--2YD0-"})
    for j in hissedilenToplu:
        veriler.append(j.text)

# Saat Verileri
for i in tablo:
    saatler = i.find_all("h2", attrs={"class":"DetailsSummary--daypartName--kbngc"})
    for j in saatler:
                veri = j.text
                saat_degeri = int(veri.split(":")[0])
                saat.append(saat_degeri)
                if saat_degeri == 23:
                    break

# Sıcaklık
sayac = 0
for i in tablo:
    degerler = i.find_all("span", attrs={"class":"DetailsSummary--tempValue--jEiXE"})
    for j in degerler:
        if sayac < len(saat):
            veri = j.text
            sicaklik.append(int(veri[:-1]))
        sayac += 1

# Yağış oranı
sayac = 0
for i in tablo:
    degerler = i.find_all("span", attrs={"data-testid":"PercentageValue"})
    for j in degerler:
        if sayac < 3*len(saat):
            if sayac % 3 == 0:
                veri = j.text
                yagisOrani.append(int(veri[:-1]))
        sayac += 1


for i in range(len(saat) * 6):
    if i % 6 == 0:
        #hissedilen
        duzenli = veriler[i][:-1]
        new = int(duzenli)
        hissedilen.append(new)
    
    elif i % 6 == 1:
        #rüzgar
        duzenli = veriler[i].split()[1]
        new = int(duzenli)
        ruzgar.append(new)
        
        duzenli2 = veriler[i].split()[0]
        ruzgar_yonu.append(duzenli2)

    elif i % 6 == 2:
        #nem
        duzenli = veriler[i][:-1]
        new = int(duzenli)
        nem.append(new)

    elif i % 6 == 3:
        #uv
        duzenli = veriler[i].split()[0]
        new = int(duzenli)
        uv.append(new)

    elif i % 6 == 4:
        #bulut Örtüsü
        duzenli = veriler[i][:-1]
        new = int(duzenli)
        bulutOrtusu.append(new)

    elif i % 6 == 5:
        #Yağmur miktarı
        duzenli = veriler[i].split()[0]
        new = float(duzenli)
        yagmurMiktari.append(new)


#print("hissedilen" , hissedilen)
#print("rüzgar" , ruzgar)
#print("nem" , nem)
#print("uv" , uv)
#print("bulut örtüsü" , bulutOrtusu)
#print("yağmur miktarı",yagmurMiktari)
#print("saat",saat)
#print("sıcaklık",sicaklik)
print("yağış oranı",yagisOrani)

