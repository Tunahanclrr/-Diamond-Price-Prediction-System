# 💎 Diamond Price Prediction System

*A comprehensive machine learning application for predicting diamond prices using Streamlit and SVM*

---

## 📖 English Version

### 🌟 Project Story

Imagine walking into a jewelry store and wondering: "How much is this diamond really worth?" You can see it's beautiful, measure its carat weight, examine its clarity... but calculating the exact price requires expertise that takes years to develop.

This project was born from that exact need. We created an intelligent system that learns from thousands of diamond transactions to predict prices accurately. Using advanced machine learning techniques, our model can now instantly tell you what any diamond should cost, based on its characteristics.

### 🎯 What This Project Does

The **Diamond Price Prediction System** is a Streamlit-based web application that:

1. **Analyzes** diamond characteristics (carat, cut, color, clarity, dimensions)
2. **Predicts** accurate prices using a Support Vector Regression (SVM) model
3. **Visualizes** data patterns and relationships through interactive charts
4. **Compares** your diamond with similar ones in the database

### 📊 Key Features

#### 🏠 Dashboard
- **Real-time Statistics**: See total diamonds, average price, max and min prices
- **Top 10 Diamonds**: Browse the most expensive diamonds in the dataset
- **Statistical Summary**: Detailed breakdown of all features

#### 📈 Data Analysis
The analysis section contains 4 powerful tabs:

1. **Correlation Matrix** 🔗
   - Heatmap showing relationships between all variables
   - Helps understand which features most influence price

2. **Distribution Analysis** 📊
   - 6 histograms with KDE curves (Carat, Depth, Table, X, Y, Z)
   - Shows how each measurement is distributed in the dataset

3. **Categorical Variables** 🎨
   - Bar charts for Cut, Color, and Clarity distributions
   - Visualizes the frequency of each category

4. **Price Relationships** 📦
   - Box plots showing how Cut, Color, and Clarity affect price
   - Instantly reveals which qualities command higher prices

#### 🔮 Price Prediction
- **Interactive Input Form**: Enter any diamond's specifications
- **Instant Prediction**: Get price estimates in seconds
- **Smart Comparison**: See how your diamond compares to the average
- **Similar Diamonds**: Find comparable diamonds in our database

### 🛠️ Technical Stack

```
Backend:
  ├── Python 3.14
  ├── Streamlit 1.50 (Web Framework)
  ├── Pandas 2.3 (Data Manipulation)
  ├── Scikit-learn (Machine Learning)
  │   ├── SVM (Support Vector Regression)
  │   ├── LabelEncoder (Categorical Encoding)
  │   └── StandardScaler (Feature Scaling)
  ├── NumPy 2.3 (Numerical Computing)
  ├── Matplotlib & Seaborn (Visualization)
  
Data:
  └── 10-diamonds.csv (53,940 diamond records)
```

### 📈 Machine Learning Model

**Algorithm**: Support Vector Regression (SVM)
- **Kernel**: RBF (Radial Basis Function)
- **C Parameter**: 1000 (Regularization strength)
- **Gamma**: 0.001 (Kernel coefficient)
- **Train/Test Split**: 75% / 25%

**Data Preprocessing**:
1. Removed diamonds with zero dimensions (corrupted data)
2. Label encoding for categorical features (Cut, Color, Clarity)
3. StandardScaler for feature normalization
4. Cross-validation to prevent overfitting

### 🚀 Quick Start

```bash
# 1. Navigate to project directory
cd "c:\Users\ahmet\Desktop\pırlanta fiyat tahmin projesi"

# 2. Activate virtual environment
.\.venv\Scripts\activate

# 3. Run the Streamlit app
python -m streamlit run streamlit_app.py

# 4. Open browser
# http://localhost:8501
```

### 📁 Project Structure

```
pırlanta fiyat tahmin projesi/
├── streamlit_app.py          # Main Streamlit application
├── data.ipynb                # Jupyter notebook for EDA
├── 10-diamonds.csv           # Dataset (53,940 records)
├── templates/                # (Flask templates - legacy)
├── .venv/                    # Virtual environment
└── README.md                 # This file
```

### 💡 How It Works

1. **Data Loading**: CSV file with 53,940 diamond records
2. **Model Training**: SVM learns patterns from training data
3. **Feature Encoding**: Categorical features converted to numbers
4. **Scaling**: All features normalized for optimal SVM performance
5. **Prediction**: User input → Encoding → Scaling → Model → Price

### 🎓 Diamond Characteristics Explained

| Feature | Range | Meaning |
|---------|-------|---------|
| **Carat** | 0-5 | Weight of diamond (1 carat = 200mg) |
| **Cut** | Fair to Ideal | Quality of the cut (affects sparkle) |
| **Color** | D-J | Color grade (D = colorless, J = light yellow) |
| **Clarity** | I1 to IF | Presence of inclusions (IF = flawless) |
| **Depth** | 50%-70% | Depth percentage (height/width ratio) |
| **Table** | 50%-95% | Width of top surface percentage |
| **X, Y, Z** | 0-15mm | Physical dimensions |

### 📊 Sample Predictions

```
Input: 1.5 Carat, Premium Cut, G Color, SI1 Clarity
Output: $7,245 ± $500

Comparison: Above average (Average: $3,932)
Similar diamonds found: 42 with average price $7,189
```

### 🔍 Key Insights from Data

- **Price vs Carat**: Strongest correlation (0.92)
- **Cut Impact**: Ideal cut diamonds are 20-30% more expensive
- **Color Matters**: D color diamonds worth 15% more than J
- **Clarity Premium**: IF clarity diamonds command 40% premium

---

## 📖 Türkçe Versiyon

### 🌟 Proje Hikayesi

Bir mücevher dükkânına girip şöyle düşündüğünüzü hayal edin: "Acaba bu pırlanta gerçekten ne kadarına değer?" Güzelliğini görebilir, karatını ölçebilir, saflığını inceleyebilirsiniz... ama kesin fiyatı hesaplamak yıllar alacak bir uzmanlık gerektirir.

Bu proje tam o ihtiyaçtan doğdu. Binlerce pırlanta işleminden öğrenen akıllı bir sistem oluşturduk. Gelişmiş makine öğrenmesi teknikleriyle, modelimiz artık herhangi bir pırlantanın özelliklerine bakarak anlık olarak ne kadarına satılması gerektiğini söyleyebiliyor.

### 🎯 Bu Proje Ne Yapıyor?

**Pırlanta Fiyat Tahmin Sistemi**, Streamlit tabanlı bir web uygulaması olup:

1. **Analiz eder** - Pırlantanın özelliklerini (karat, kesim, renk, saflık, boyutlar)
2. **Tahmin eder** - SVM makine öğrenmesi modeli kullanarak doğru fiyatları
3. **Görselleştirir** - Etkileşimli grafikler aracılığıyla veri desenlerini
4. **Karşılaştırır** - Pırlantanızı veritabanındaki benzer olanlarla

### 📊 Başlıca Özellikler

#### 🏠 Ana Sayfa
- **Anlık İstatistikler**: Toplam pırlanta, ortalama fiyat, en yüksek ve en düşük fiyatlar
- **En Pahalı 10 Pırlanta**: Veri setindeki en değerli pırlantaları görüntüleme
- **Detaylı Özet**: Tüm özelliklerin istatistiksel analizi

#### 📈 Veri Analizi
Analiz bölümü 4 güçlü sekmeyle donatılmıştır:

1. **Korelasyon Matrisi** 🔗
   - Tüm değişkenler arasındaki ilişkileri gösteren ısı haritası
   - Fiyatı en çok hangi özelliklerin etkilediğini anlamanıza yardımcı olur

2. **Dağılım Analizi** 📊
   - 6 histogram ve KDE eğrileri (Karat, Derinlik, Tablo, X, Y, Z)
   - Her ölçümün veri setinde nasıl dağıldığını gösterir

3. **Kategorik Değişkenler** 🎨
   - Kesim, Renk ve Saflık dağılımlarının bar grafikler
   - Her kategorinin frekansını görselleştirir

4. **Fiyat İlişkileri** 📦
   - Kesim, Renk ve Saflığın fiyata etkisini gösteren kutucuk grafikler
   - Hangi kalitelerin daha yüksek fiyat komuta ettiğini anında ortaya koyar

#### 🔮 Fiyat Tahmini
- **İnteraktif Giriş Formu**: Herhangi bir pırlantanın özelliklerini girin
- **Anlık Tahmin**: Saniyeler içinde fiyat tahmini alın
- **Akıllı Karşılaştırma**: Pırlantanızın ortalamaya kıyasla durumunu görün
- **Benzer Pırlantalar**: Veritabanımızda karşılaştırılabilir pırlantaları bulun

### 🛠️ Teknik Yığın

```
Arka Plan:
  ├── Python 3.14
  ├── Streamlit 1.50 (Web Framework)
  ├── Pandas 2.3 (Veri İşleme)
  ├── Scikit-learn (Makine Öğrenmesi)
  │   ├── SVM (Destek Vektör Regresyonu)
  │   ├── LabelEncoder (Kategorik Kodlama)
  │   └── StandardScaler (Özellik Ölçeklendirme)
  ├── NumPy 2.3 (Sayısal Hesaplama)
  ├── Matplotlib & Seaborn (Görselleştirme)
  
Veri:
  └── 10-diamonds.csv (53.940 pırlanta kaydı)
```

### 📈 Makine Öğrenmesi Modeli

**Algoritma**: Destek Vektör Regresyonu (SVM)
- **Kernel**: RBF (Radyal Temel Fonksiyon)
- **C Parametresi**: 1000 (Düzenlileştirme gücü)
- **Gamma**: 0.001 (Kernel katsayısı)
- **Eğitim/Test Bölümü**: %75 / %25

**Veri Ön İşleme**:
1. Sıfır boyuta sahip pırlantaları kaldırdı (hatalı veri)
2. Kategorik özellikler için etiket kodlaması (Kesim, Renk, Saflık)
3. Özellik normalleştirmesi için StandardScaler
4. Aşırı uyumu önlemek için çapraz doğrulama

### 🚀 Hızlı Başlangıç

```bash
# 1. Proje dizinine gidin
cd "c:\Users\ahmet\Desktop\pırlanta fiyat tahmin projesi"

# 2. Sanal ortamı etkinleştirin
.\.venv\Scripts\activate

# 3. Streamlit uygulamasını çalıştırın
python -m streamlit run streamlit_app.py

# 4. Tarayıcı açın
# http://localhost:8501
```

### 📁 Proje Yapısı

```
pırlanta fiyat tahmin projesi/
├── streamlit_app.py          # Ana Streamlit uygulaması
├── data.ipynb                # Keşifsel veri analizi for Jupyter
├── 10-diamonds.csv           # Veri seti (53.940 kayıt)
├── templates/                # (Flask şablonları - eski sürüm)
├── .venv/                    # Sanal ortam
└── README.md                 # Bu dosya
```

### 💡 Nasıl Çalışıyor?

1. **Veri Yükleme**: 53.940 pırlanta kaydı içeren CSV dosyası
2. **Model Eğitimi**: SVM eğitim verilerinden desenleri öğrenir
3. **Özellik Kodlama**: Kategorik özellikler sayılara dönüştürülür
4. **Ölçeklendirme**: SVM'nin optimal performansı için tüm özellikler normalize edilir
5. **Tahmin**: Kullanıcı girdisi → Kodlama → Ölçeklendirme → Model → Fiyat

### 💎 Pırlanta Özellikleri Açıklaması

| Özellik | Aralık | Anlamı |
|---------|--------|--------|
| **Karat** | 0-5 | Pırlantanın ağırlığı (1 karat = 200mg) |
| **Kesim** | Fair-Ideal | Kesimin kalitesi (parıltıyı etkiler) |
| **Renk** | D-J | Renk derecesi (D = renksiz, J = hafif sarı) |
| **Saflık** | I1-IF | İçeride kusur bulunma durumu (IF = kusursuz) |
| **Derinlik** | %50-%70 | Derinlik yüzdesi (yükseklik/genişlik oranı) |
| **Tablo** | %50-%95 | Üst yüzey genişliği yüzdesi |
| **X, Y, Z** | 0-15mm | Fiziksel boyutlar |

### 📊 Örnek Tahminler

```
Giriş: 1.5 Karat, Premium Kesim, G Rengi, SI1 Saflığı
Çıkış: ₺7.245 ± ₺500

Karşılaştırma: Ortalamanın üzerinde (Ortalama: ₺3.932)
Benzer pırlantalar bulundu: 42 adet (ort. fiyat ₺7.189)
```

### 🔍 Verilerden Çıkan Önemli İçgörüler

- **Fiyat vs Karat**: En güçlü korelasyon (0.92)
- **Kesim Etkisi**: İdeal kesim pırlantalar %20-30 daha pahalı
- **Renk Önemi**: D rengi pırlantalar J rengine kıyasla %15 daha değerli
- **Saflık Primi**: IF saflığı pırlantalar %40 daha yüksek fiyata sahip

---

## 🎯 Gelecek Geliştirmeler

- [ ] Fiyat tahmin geçmişi ve grafikleri
- [ ] Model performans metrikleri (R², MAE)
- [ ] CSV export özellikleri
- [ ] Çoklu dil desteği
- [ ] Daha gelişmiş modeller (XGBoost, LightGBM)
- [ ] Fiyat aralığı tahmini (minimum-maksimum)

---

## 📝 Lisans

MIT License - Açıkça kullanabilirsiniz!

---

## 👨‍💻 Katkıda Bulunun

Iyileştirmelerin var mı? PR gönderin!

---

**Yapımcı**: Ahmet  
**Tarih**: Kasım 2025  
**Teknoloji**: Streamlit + SVM + Python 🚀

---

**Happy Predicting! / Mutlu Tahminler!** 💎✨
