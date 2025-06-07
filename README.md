# 🏠 Sahibinden İlan Verisi Toplayıcı (Python + Selenium)

Bu proje, [sahibinden.com](https://www.sahibinden.com) üzerindeki ilanlardan veri çekerek otomatik olarak Excel dosyasına kaydeden bir Python otomasyonudur.  
**Bot korumasını aşmak** için `undetected-chromedriver` teknolojisi kullanılmıştır.

---

## 🚀 Özellikler | Features

✅ Birden fazla ilan numarasıyla çalışır  
✅ Verileri otomatik olarak `Excel` dosyasına yazar  
✅ Bot kontrolünü otomatik geçer  
✅ "Yok" hatası olan alanları boş geçer  
✅ Kullanımı kolay `.txt` tabanlı giriş  

✅ Works with multiple listing numbers  
✅ Automatically saves data to an `Excel` file  
✅ Bypasses bot protection automatically  
✅ Handles missing fields gracefully  
✅ Easy input using `.txt` file  

---

## 📦 Gereksinimler | Requirements

Python 3.8+ yüklü olmalıdır. | Python 3.8+ must be installed.

```bash
pip install pandas undetected-chromedriver openpyxl
```

---

## 📁 Dosya Yapısı | File Structure

```
📂 proje-klasörü | project-folder
├── ilanlar.txt           # 📥 İşlenecek ilan numaraları (her satıra bir ilan) | Listing numbers to process
├── sahibinden_scraper.py  # 🔁 Ana Python script | Main script
├── ilanlar_uc.xlsx       # 📊 Çıktı Excel dosyası | Output Excel file
└── README.md             # 📘 Açıklama dosyası | This description file
```

---

## 📝 `ilanlar.txt` Nasıl Hazırlanır? | How to Prepare `ilanlar.txt`

```txt
1249529140
1248053326
1234567890
...
```

Her satıra bir ilan numarası girmen yeterlidir.  
Just write one listing number per line.

---

## ▶️ Kullanım | Usage

1. `ilanlar.txt` dosyasına ilan numaralarını yaz  
2. Scripti çalıştır:  
3. Excel dosyası oluşur  

1. Add listing numbers to `ilanlar.txt`  
2. Run the script:  

```bash
python sahibinden_scraper.py
```

3. `ilanlar_uc.xlsx` will be generated

---

## 📸 Örnek Ekran Çıktısı | Example Output

| İlan No     | İlan Tarihi | Başlık                  | Oda  | Net  | Tutar       | Mahalle        | Kimden          |
|-------------|-------------|--------------------------|------|------|-------------|-----------------|------------------|
| 1249529140  | 02.06.2025  | Darıca 3+1 Satılık Daire | 3+1  | 110  | 4.399.000 TL| Sırasöğütler Mh.| Emlak Ofisinden |

---

## 🛡️ Uyarı | Disclaimer

> Sahibinden.com bot korumalı bir sitedir. Bu nedenle bu uygulama sadece **kendi kullanımınız** içindir.  
> This tool is intended only for **personal/educational use**. Heavy scraping may result in IP bans.

---

## 🧠 Geliştirme Planları | Development Roadmap

- [ ] `Streamlit` arayüz desteği | UI with Streamlit
- [ ] `.exe` olarak paketleme | Compile as executable
- [ ] Kategoriye göre toplu tarama | Bulk scraping by category
- [ ] Tarih filtreleme desteği | Filter by date

---

## 📬 İletişim | Contact

Herhangi bir öneri, katkı veya sorun için benimle iletişime geçebilirsin.  
Feel free to contribute or open issues & pull requests!

---

> © 2025 | Geliştirici: [Your Name or GitHub Username]  
> This project is for educational and personal use only.
