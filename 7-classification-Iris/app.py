import streamlit as st
import pandas as pd

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

# Intro
st.write("""
# Simple Iris Flower Prediction App
This app predicts the **Iris Flower** type!
""")

# Sidebar - init
st.sidebar.header('User Input Parameters')

# Sidebar - User Input Features
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)
    data = {
        'sepal_length': sepal_length,
        'sepal_width': sepal_width,
        'petal_length': petal_length,
        'petal_width': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()