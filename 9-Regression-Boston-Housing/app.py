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

from sklearn import datasets
from sklearn import RandomForestRegressor

# Intro
st.write("""
# Boston House Price Prediction App
This app predicts the **Boston House Price**!
""")