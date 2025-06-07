import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import pandas as pd
import time

def ilan_bilgisi_al(ilan_no):
    options = uc.ChromeOptions()
    # options.add_argument("--headless")  # Arka planda çalışması için aktif edebilirsin
    driver = uc.Chrome(options=options)

    url = f"https://www.sahibinden.com/{ilan_no}"
    driver.get(url)
    time.sleep(15)  # Sayfanın yüklenmesini beklemek için yeterli süre

    # Her bir alanı ayrı ayrı yakala
    try:
        tarih = driver.find_element(By.CSS_SELECTOR, ".classifiedInfoList > li:nth-child(2) > span:nth-child(2)").text.strip()
    except:
        tarih = "Yok"

    try:
        baslik = driver.find_element(By.CSS_SELECTOR, ".classifiedDetailTitle h1").text.strip()
    except:
        baslik = "Yok"

    try:
        tutar = driver.find_element(By.CSS_SELECTOR, ".classified-price-wrapper").text.strip()
    except:
        tutar = "Yok"

    try:
        oda = driver.find_element(By.CSS_SELECTOR, ".classifiedInfoList li:nth-child(6)").text.strip()
    except:
        oda = "Yok"

    try:
        net = driver.find_element(By.CSS_SELECTOR, ".classifiedInfoList li:nth-child(5)").text.strip()
    except:
        net = "Yok"

    try:
        mahalle = driver.find_element(By.CSS_SELECTOR, ".classifiedInfo > h2 > a:nth-child(5)").text.strip()
    except:
        mahalle = "Yok"

    try:
        kimden = driver.find_element(By.CSS_SELECTOR, ".user-info-store-name a").text.strip()
    except:
        kimden = "Yok"    

    driver.quit()
    del driver  # Uyarıyı engellemek için
    return {
        "İlan No": ilan_no,
        "İlan Tarihi": tarih,
        "Başlık": baslik,
        "Oda": oda,
        "Net": net,
        "Tutar": tutar,
        "Mahalle": mahalle,
        "Kimden": kimden
    }

# # 👇 Birden fazla ilan no ile çalışabilir
# ilanlar = [
#     "1249529140",
#     "1248053326",
#     # "başka_ilan_no", ...
# ]

# veriler = [ilan_bilgisi_al(no) for no in ilanlar]

# df = pd.DataFrame(veriler)
# df.to_excel("ilanlar_uc.xlsx", index=False)
# print("✅ Excel dosyası başarıyla oluşturuldu.")

# ✅ ilanlar.txt dosyasından ilan numaralarını oku

def ilan_nolarini_oku(dosya_adi="ilanlar.txt"):
    with open(dosya_adi, "r", encoding="utf-8") as f:
        return [satir.strip() for satir in f if satir.strip()]

# ✅ Çalıştır
if __name__ == "__main__":
    ilanlar = ilan_nolarini_oku()
    veriler = [ilan_bilgisi_al(no) for no in ilanlar]

    df = pd.DataFrame(veriler)
    df.to_excel("ilanlar_uc.xlsx", index=False)
    print("✅ Excel dosyası başarıyla oluşturuldu.")
