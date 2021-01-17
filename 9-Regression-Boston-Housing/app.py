#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    File name: app.py
    Author: Satwik Gawand
    Date Created: 18/1/2021
    Date Last Modified: 18/1/2021
    Python Version: 3.8.6
'''

# Import
import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

# Intro
st.write("""
# Boston House Price Prediction App
This app predicts the **Boston House Price**!
""")

# Load Dataset
boston = datasets.load_boston()
x = pd.DataFrame(boston.data, columns=boston.feature_names)
y = pd.DataFrame(boston.target, columns=["MEDV"])

# Sidebar -Init
st.sidebar.header('Specify Input Parameters')

# Sidebar - Input Features
def user_input_features():
    CRIM = st.sidebar.slider('CRIM', float(x.CRIM.min()), float(x.CRIM.max()), float(x.CRIM.mean()))
    ZN = st.sidebar.slider('ZN', float(x.ZN.min()), x.ZN.max(), float(x.ZN.mean()))
    INDUS = st.sidebar.slider('INDUS', float(x.INDUS.min()), float(x.INDUS.max()), float(x.ZN.mean()))
    CHAS = st.sidebar.slider('CHAS', float(x.CHAS.min()), float(x.CHAS.max()), float(x.CHAS.mean()))
    NOX = st.sidebar.slider('NOX', float(x.NOX.min()), float(x.NOX.max()), float(x.NOX.mean()))
    RM = st.sidebar.slider('RM', float(x.RM.min()), float(x.RM.max()), float(x.RM.mean()))
    AGE = st.sidebar.slider('AGE', float(x.AGE.min()), float(x.AGE.max()), float(x.AGE.mean()))
    DIS = st.sidebar.slider('DIS', float(x.DIS.min()), float(x.DIS.max()), float(x.DIS.mean()))
    RAD = st.sidebar.slider('RAD', float(x.RAD.min()), float(x.RAD.max()), float(x.RAD.mean()))
    TAX = st.sidebar.slider('TAX', float(x.TAX.min()), float(x.TAX.max()), float(x.TAX.mean()))
    PTRATIO = st.sidebar.slider('PTRATIO', float(x.PTRATIO.min()), float(x.PTRATIO.max()), float(x.PTRATIO.mean()))
    B = st.sidebar.slider('B', float(x.B.min()), float(x.B.max()), float(x.B.mean()))
    LSTAT = st.sidebar.slider('LSTAT', float(x.LSTAT.min()), float(x.LSTAT.max()), float(x.LSTAT.mean()))
    data = {
        'CRIM': CRIM,
        'ZN': ZN,
        'INDUS': INDUS,
        'CHAS': CHAS,
        'NOX': NOX,
        'RM': RM,
        'AGE': AGE,
        'DIS': DIS,
        'RAD': RAD,
        'TAX': TAX,
        'PTRATIO': PTRATIO,
        'B': B,
        'LSTAT': LSTAT
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Print Input Parameters
st.header('Specified User Parameters')
st.write(df)
st.write('---')

# Build Regression Model
model = RandomForestRegressor()
model.fit(x, y)

# Predict
pred = model.predict(df)

st.header('Prediction of MEDV')
st.write(pred)
st.write('---')

# Explain the Model's Predictions using SHAP Values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(x)

st.header('Feature Importance')
st.title('Feature Importance based on SHAP Values')
shap.summary_plot(shap_values, x)
st.pyplot(bbox_inches='tight')
st.write('---')

st.title('Feature Importance based on SHAP Values (Bar)')
shap.summary_plot(shap_values, x, plot_type="bar")
st.pyplot(bbox_inches='tight')