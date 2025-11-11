import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Sayfa ayarları
st.set_page_config(
    page_title="💎 Pırlanta Fiyat Tahmin",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Stil
st.markdown("""
<style>
    .main {
        padding-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 4px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

st.title("💎 Pırlanta Fiyat Tahmin Sistemi")
st.markdown("---")

# Veri yükleme (cache ile)
@st.cache_data
def load_and_prepare_data():
    df = pd.read_csv("10-diamonds.csv")
    df = df.drop("Unnamed: 0", axis=1)
    df = df.drop(df[df["x"] == 0].index)
    df = df.drop(df[df["y"] == 0].index)
    df = df.drop(df[df["z"] == 0].index)
    return df

# Model eğitme (cache ile)
@st.cache_resource
def train_model(df):
    X = df.drop("price", axis=1)
    y = df["price"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=15, test_size=0.25)
    
    # Her kategorik sütun için ayrı encoder oluştur
    label_encoders = {}
    for col in ["cut", "color", "clarity"]:
        label_encoders[col] = LabelEncoder()
        X_train[col] = label_encoders[col].fit_transform(X_train[col])
        X_test[col] = label_encoders[col].transform(X_test[col])
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    model = SVR(C=1000, gamma=0.001, kernel='rbf')
    model.fit(X_train_scaled, y_train)
    
    return model, scaler, label_encoders

# Veri yükleme
df = load_and_prepare_data()
model, scaler, label_encoders = train_model(df)

# Sidebar Navigasyon
st.sidebar.title("📊 Menü")
page = st.sidebar.radio(
    "Sayfa Seçin:",
    ["🏠 Ana Sayfa", "📈 Veri Analizi", "🔮 Fiyat Tahmin"],
    label_visibility="collapsed"
)

# ===================== ANA SAYFA =====================
if page == "🏠 Ana Sayfa":
    st.subheader("📋 Genel Bilgiler")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Toplam Pırlanta", len(df))
    with col2:
        st.metric("Ortalama Fiyat", f"${df['price'].mean():,.0f}")
    with col3:
        st.metric("En Yüksek Fiyat", f"${df['price'].max():,.0f}")
    with col4:
        st.metric("En Düşük Fiyat", f"${df['price'].min():,.0f}")
    
    st.markdown("---")
    st.subheader("🔝 En Pahalı 10 Pırlanta")
    top_10 = df.nlargest(10, 'price')[['carat', 'cut', 'color', 'clarity', 'price']]
    st.dataframe(top_10, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 Temel İstatistikler")
    st.dataframe(df.describe(), use_container_width=True)

# ===================== VERİ ANALİZİ =====================
elif page == "📈 Veri Analizi":
    st.subheader("📊 Detaylı Veri Analizi")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📉 Korelasyon", "📊 Dağılımlar", "🎨 Kategorik", "🔗 İlişkiler"])
    
    with tab1:
        st.write("#### Korelasyon Matrisi")
        correlation_matrix = df.corr(numeric_only=True)
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f', ax=ax)
        plt.title('Korelasyon Matrisi - Pırlanta Fiyatı Tahmin')
        st.pyplot(fig)
    
    with tab2:
        st.write("#### Sayısal Değişkenlerin Dağılımı")
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
        for idx, col in enumerate(numerical_cols):
            ax = axes[idx // 3, idx % 3]
            sns.histplot(data=df, x=col, kde=True, ax=ax, bins=30)
            ax.set_title(f'{col} Dağılımı')
        plt.tight_layout()
        st.pyplot(fig)
    
    with tab3:
        st.write("#### Kategorik Değişkenlerin Dağılımı")
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        cut_counts = df['cut'].value_counts()
        axes[0].bar(cut_counts.index, cut_counts.values, color='skyblue')
        axes[0].set_title('Cut Dağılımı')
        axes[0].set_xlabel('Cut')
        axes[0].set_ylabel('Frekans')
        
        color_counts = df['color'].value_counts()
        axes[1].bar(color_counts.index, color_counts.values, color='lightcoral')
        axes[1].set_title('Color Dağılımı')
        axes[1].set_xlabel('Color')
        axes[1].set_ylabel('Frekans')
        
        clarity_counts = df['clarity'].value_counts()
        axes[2].bar(clarity_counts.index, clarity_counts.values, color='lightgreen')
        axes[2].set_title('Clarity Dağılımı')
        axes[2].set_xlabel('Clarity')
        axes[2].set_ylabel('Frekans')
        
        plt.tight_layout()
        st.pyplot(fig)
    
    with tab4:
        st.write("#### Kategorik Değişkenlerin Fiyata Etkisi")
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        sns.boxplot(x='cut', y='price', data=df, ax=axes[0], hue='cut', legend=False)
        axes[0].set_title('Cut vs Fiyat')
        
        sns.boxplot(x='color', y='price', data=df, ax=axes[1], hue='color', legend=False)
        axes[1].set_title('Color vs Fiyat')
        
        sns.boxplot(x='clarity', y='price', data=df, ax=axes[2], hue='clarity', legend=False)
        axes[2].set_title('Clarity vs Fiyat')
        
        plt.tight_layout()
        st.pyplot(fig)

# ===================== FIYAT TAHMİN =====================
elif page == "🔮 Fiyat Tahmin":
    st.subheader("💰 Pırlantanız için Fiyat Tahmin Edin")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        carat = st.number_input("⚖️ Carat (Ağırlık)", min_value=0.0, max_value=5.0, value=1.0, step=0.01)
        depth = st.number_input("📏 Depth (%)", min_value=50.0, max_value=70.0, value=61.0, step=0.1)
        table = st.number_input("📐 Table (%)", min_value=50.0, max_value=95.0, value=57.0, step=0.1)
    
    with col2:
        x = st.number_input("📊 X (mm)", min_value=0.0, max_value=15.0, value=6.0, step=0.1)
        y = st.number_input("📊 Y (mm)", min_value=0.0, max_value=15.0, value=6.0, step=0.1)
        z = st.number_input("📊 Z (mm)", min_value=0.0, max_value=10.0, value=4.0, step=0.1)
    
    with col3:
        cut = st.selectbox("✂️ Cut", df['cut'].unique())
        color = st.selectbox("🎨 Color", sorted(df['color'].unique()))
        clarity = st.selectbox("💎 Clarity", df['clarity'].unique())
    
    if st.button("🔮 Fiyat Tahmin Et", use_container_width=True, type="primary"):
        # Veriyi hazırla
        input_data = pd.DataFrame({
            'carat': [carat],
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'x': [x],
            'y': [y],
            'z': [z]
        })
        
        # Label encoding - Her sütun için doğru encoder kullan
        for col in ["cut", "color", "clarity"]:
            input_data[col] = label_encoders[col].transform(input_data[col])
        
        # Scaling
        input_scaled = scaler.transform(input_data)
        
        # Tahmin
        predicted_price = model.predict(input_scaled)[0]
        
        # Sonuç göster
        st.success("✅ Tahmin Tamamlandı!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("💲 Tahmini Fiyat", f"${predicted_price:,.2f}")
        with col2:
            avg_price = df['price'].mean()
            comparison = "Üzerinde" if predicted_price > avg_price else "Altında"
            st.metric("📊 Karşılaştırma", comparison, delta=f"${abs(predicted_price - avg_price):,.0f}")
        with col3:
            st.metric("📈 Ortalama Fiyat", f"${avg_price:,.0f}")
        
        st.markdown("---")
        
        # Benzer pırlantaları göster
        st.subheader("🔍 Benzer Özelliklere Sahip Pırlantalar")
        
        similar = df[
            (df['carat'] >= carat - 0.5) & (df['carat'] <= carat + 0.5) &
            (df['cut'] == cut) & (df['color'] == color) & (df['clarity'] == clarity)
        ]
        
        if len(similar) > 0:
            st.info(f"✅ **{len(similar)} benzer pırlanta bulundu**")
            st.dataframe(
                similar[['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price']].head(10),
                use_container_width=True
            )
            st.metric("💰 Benzer Pırlantaların Ortalama Fiyatı", f"${similar['price'].mean():,.2f}")
        else:
            st.warning("⚠️ Bu özelliklere sahip benzer pırlanta bulunamadı.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>💎 Pırlanta Fiyat Tahmin Sistemi | Powered by Streamlit & Machine Learning</p>
        <p style='font-size: 0.8em'>SVM (Support Vector Regression) modeli ile oluşturulmuştur</p>
    </div>
    """,
    unsafe_allow_html=True
)
