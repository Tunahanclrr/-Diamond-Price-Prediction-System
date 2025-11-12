# 🚀 Streamlit Cloud Deploy Talimatları

## English

### Step-by-Step Guide to Deploy on Streamlit Cloud

1. **Fork the Repository** (if not already done)
   - Go to: https://github.com/Tunahanclrr/-Diamond-Price-Prediction-System
   - Click "Fork" button

2. **Create Streamlit Cloud Account**
   - Visit: https://streamlit.io/cloud
   - Sign up with GitHub

3. **Deploy Your App**
   - Click "New app" on Streamlit Cloud dashboard
   - Select your forked repository
   - Choose branch: `main`
   - Set file path to: `streamlit_app.py`
   - Click "Deploy"

4. **Wait for Build**
   - Streamlit will automatically:
     - Read `requirements.txt`
     - Install all dependencies
     - Start your app
   - This takes about 2-5 minutes

5. **Access Your App**
   - Once deployed, you'll get a URL like:
   - `https://YOUR-USERNAME-diamond-price-prediction-system.streamlit.app`

### Troubleshooting

**Error: ModuleNotFoundError**
- ✅ Already fixed! The `requirements.txt` file contains all dependencies

**Error: "app has encountered an error"**
- Check that `10-diamonds.csv` is in the repository root
- Ensure all imports match the requirements.txt versions

**App runs locally but fails on cloud**
- Make sure all file paths are relative (not absolute)
- The app should work from any directory

### File Structure for Deployment

```
Repository Root
├── streamlit_app.py          ← Main file
├── 10-diamonds.csv           ← Dataset
├── requirements.txt          ← Dependencies (IMPORTANT!)
├── .streamlit/config.toml    ← Streamlit config
└── README.md                 ← Documentation
```

---

## Türkçe

### Streamlit Cloud'a Deploy Etme Adım Adım Rehberi

1. **Repository'yi Fork Et** (Eğer yapmadıysanız)
   - Şu adrese git: https://github.com/Tunahanclrr/-Diamond-Price-Prediction-System
   - "Fork" düğmesine tıkla

2. **Streamlit Cloud Hesabı Oluştur**
   - Ziyaret et: https://streamlit.io/cloud
   - GitHub ile kaydol

3. **Uygulamayı Deploy Et**
   - Streamlit Cloud dashboard'da "New app" tıkla
   - Forklanan repository'ni seç
   - Branch seç: `main`
   - File path'ı ayarla: `streamlit_app.py`
   - "Deploy" tıkla

4. **Build'i Bekle**
   - Streamlit otomatik olarak:
     - `requirements.txt` okuyacak
     - Tüm bağımlılıkları yükleyecek
     - Uygulamayı başlatacak
   - Bu işlem 2-5 dakika sürer

5. **Uygulamaya Erişim**
   - Deploy edildikten sonra, şu şekilde bir URL alacaksın:
   - `https://YOUR-USERNAME-diamond-price-prediction-system.streamlit.app`

### Sorun Giderme

**Hata: ModuleNotFoundError**
- ✅ Zaten çözüldü! `requirements.txt` dosyası tüm bağımlılıkları içerir

**Hata: "app has encountered an error"**
- `10-diamonds.csv` dosyasının repository root'ta olduğunu kontrol et
- Tüm import'ların requirements.txt versiyonlarıyla eşleştiğini sağla

**Uygulama yerel olarak çalışıyor ama bulutta başarısız**
- Tüm dosya yollarının relative olduğundan emin ol (absolute değil)
- Uygulama herhangi bir dizinden çalışmalı

### Deploy için Dosya Yapısı

```
Repository Root
├── streamlit_app.py          ← Ana dosya
├── 10-diamonds.csv           ← Veri seti
├── requirements.txt          ← Bağımlılıklar (ÖNEMLİ!)
├── .streamlit/config.toml    ← Streamlit konfigurasyonu
└── README.md                 ← Dokümantasyon
```

---

## 📝 Kurulum Sonrası Kontrol Listesi

- [x] `requirements.txt` oluşturuldu
- [x] `.gitignore` oluşturuldu
- [x] `.streamlit/config.toml` oluşturuldu
- [x] `10-diamonds.csv` repository'de mevcut
- [x] Tüm dosyalar GitHub'a push edildi
- [ ] Streamlit Cloud'a deploy edin
- [ ] URL'yi test edin
- [ ] Başarılı! 🎉

---

## 💡 İpuçları

1. **Hızlı Deploy**
   - Streamlit Cloud tekrar deploy etmek için GitHub'a sadece push et
   - Automatic rebuild trigger olur

2. **Logs Kontrol**
   - Streamlit Cloud dashboard'da "Manage app" → "Logs" seç
   - Deploy hatalarını buradan görebilirsin

3. **Environment Variables**
   - Eğer API key vs gerekiyorsa, Streamlit Cloud'da "Advanced settings" kullan

4. **Performans**
   - İlk yükleme 2-3 saniye sürebilir (cache yüzünden normal)
   - Sonraki işlemler hızlı olacak

---

**Happy Deploying! / Mutlu Deploy'lar!** 🚀✨
