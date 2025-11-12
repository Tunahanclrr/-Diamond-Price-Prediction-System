from setuptools import setup, find_packages

setup(
    name="diamond-price-prediction",
    version="1.0.0",
    description="A machine learning application for predicting diamond prices",
    author="Ahmet",
    author_email="",
    url="https://github.com/Tunahanclrr/-Diamond-Price-Prediction-System",
    python_requires=">=3.8",
    packages=find_packages(),
    install_requires=[
        "streamlit==1.50.0",
        "pandas==2.3.3",
        "numpy==2.3.4",
        "matplotlib==3.8.4",
        "seaborn==0.13.2",
        "scikit-learn==1.5.2",
    ],
)
