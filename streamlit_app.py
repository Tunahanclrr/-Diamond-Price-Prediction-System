import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split

# Page settings
st.set_page_config(
    page_title="💎 Diamond Price Prediction",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Style
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

st.title("💎 Diamond Price Prediction System")
st.markdown("---")

# Load data (with cache)
@st.cache_data
def load_and_prepare_data():
    df = pd.read_csv("10-diamonds.csv")
    df = df.drop("Unnamed: 0", axis=1)
    df = df.drop(df[df["x"] == 0].index)
    df = df.drop(df[df["y"] == 0].index)
    df = df.drop(df[df["z"] == 0].index)
    return df

# Train model (with cache)
@st.cache_resource
def train_model(df):
    X = df.drop("price", axis=1)
    y = df["price"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=15, test_size=0.25)
    
    # Create separate encoder for each categorical column
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

# Load data
df = load_and_prepare_data()
model, scaler, label_encoders = train_model(df)

# Sidebar Navigation
st.sidebar.title("📊 Menu")
page = st.sidebar.radio(
    "Select Page:",
    ["🏠 Home", "📈 Data Analysis", "🔮 Price Prediction"],
    label_visibility="collapsed"
)

# ===================== HOME PAGE =====================
if page == "🏠 Home":
    st.subheader("📋 General Information")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Diamonds", len(df))
    with col2:
        st.metric("Average Price", f"${df['price'].mean():,.0f}")
    with col3:
        st.metric("Highest Price", f"${df['price'].max():,.0f}")
    with col4:
        st.metric("Lowest Price", f"${df['price'].min():,.0f}")
    
    st.markdown("---")
    st.subheader("🔝 Top 10 Most Expensive Diamonds")
    top_10 = df.nlargest(10, 'price')[['carat', 'cut', 'color', 'clarity', 'price']]
    st.dataframe(top_10, use_container_width=True)
    
    st.markdown("---")
    st.subheader("📊 Basic Statistics")
    st.dataframe(df.describe(), use_container_width=True)

# ===================== DATA ANALYSIS =====================
elif page == "📈 Data Analysis":
    st.subheader("📊 Detailed Data Analysis")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📉 Correlation", "📊 Distributions", "🎨 Categorical", "🔗 Relationships"])
    
    with tab1:
        st.write("#### Correlation Matrix")
        correlation_matrix = df.corr(numeric_only=True)
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.2f', ax=ax)
        plt.title('Correlation Matrix - Diamond Price Prediction')
        st.pyplot(fig)
    
    with tab2:
        st.write("#### Distribution of Numerical Variables")
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
        for idx, col in enumerate(numerical_cols):
            ax = axes[idx // 3, idx % 3]
            sns.histplot(data=df, x=col, kde=True, ax=ax, bins=30)
            ax.set_title(f'{col} Distribution')
        plt.tight_layout()
        st.pyplot(fig)
    
    with tab3:
        st.write("#### Distribution of Categorical Variables")
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        cut_counts = df['cut'].value_counts()
        axes[0].bar(cut_counts.index, cut_counts.values, color='skyblue')
        axes[0].set_title('Cut Distribution')
        axes[0].set_xlabel('Cut')
        axes[0].set_ylabel('Frequency')
        
        color_counts = df['color'].value_counts()
        axes[1].bar(color_counts.index, color_counts.values, color='lightcoral')
        axes[1].set_title('Color Distribution')
        axes[1].set_xlabel('Color')
        axes[1].set_ylabel('Frequency')
        
        clarity_counts = df['clarity'].value_counts()
        axes[2].bar(clarity_counts.index, clarity_counts.values, color='lightgreen')
        axes[2].set_title('Clarity Distribution')
        axes[2].set_xlabel('Clarity')
        axes[2].set_ylabel('Frequency')
        
        plt.tight_layout()
        st.pyplot(fig)
    
    with tab4:
        st.write("#### Effect of Categorical Variables on Price")
        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        
        sns.boxplot(x='cut', y='price', data=df, ax=axes[0], hue='cut', legend=False)
        axes[0].set_title('Cut vs Price')
        
        sns.boxplot(x='color', y='price', data=df, ax=axes[1], hue='color', legend=False)
        axes[1].set_title('Color vs Price')
        
        sns.boxplot(x='clarity', y='price', data=df, ax=axes[2], hue='clarity', legend=False)
        axes[2].set_title('Clarity vs Price')
        
        plt.tight_layout()
        st.pyplot(fig)

# ===================== PRICE PREDICTION =====================
elif page == "🔮 Price Prediction":
    st.subheader("💰 Predict the Price of Your Diamond")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        carat = st.number_input("⚖️ Carat (Weight)", min_value=0.0, max_value=5.0, value=1.0, step=0.01)
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
    
    if st.button("🔮 Predict Price", use_container_width=True, type="primary"):
        # Prepare data
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
        
        # Label encoding - Use correct encoder for each column
        for col in ["cut", "color", "clarity"]:
            input_data[col] = label_encoders[col].transform(input_data[col])
        
        # Scaling
        input_scaled = scaler.transform(input_data)
        
        # Prediction
        predicted_price = model.predict(input_scaled)[0]
        
        # Show result
        st.success("✅ Prediction Complete!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("💲 Predicted Price", f"${predicted_price:,.2f}")
        with col2:
            avg_price = df['price'].mean()
            comparison = "Above" if predicted_price > avg_price else "Below"
            st.metric("📊 Comparison", comparison, delta=f"${abs(predicted_price - avg_price):,.0f}")
        with col3:
            st.metric("📈 Average Price", f"${avg_price:,.0f}")
        
        st.markdown("---")
        
        # Show similar diamonds
        st.subheader("🔍 Diamonds with Similar Features")
        
        similar = df[
            (df['carat'] >= carat - 0.5) & (df['carat'] <= carat + 0.5) &
            (df['cut'] == cut) & (df['color'] == color) & (df['clarity'] == clarity)
        ]
        
        if len(similar) > 0:
            st.info(f"✅ **{len(similar)} similar diamonds found**")
            st.dataframe(
                similar[['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price']].head(10),
                use_container_width=True
            )
            st.metric("💰 Average Price of Similar Diamonds", f"${similar['price'].mean():,.2f}")
        else:
            st.warning("⚠️ No similar diamonds found with these features.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>💎 Diamond Price Prediction System | Powered by Streamlit & Machine Learning</p>
        <p style='font-size: 0.8em'>Built with SVM (Support Vector Regression) model</p>
    </div>
    """,
    unsafe_allow_html=True
)