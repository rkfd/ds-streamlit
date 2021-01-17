'''
    File name: app.py
    Author: Satwk Gawand
    Date Created: 18/1/2021
    Date Last Modified: 18/1/2021
    Python Version: 3.8.6
'''

# Imports
import streamlit as st
import pandas as pd
import numpy as np
import pickle

from sklearn.ensemble import RandomForestClassifier

# Intro
st.write("""
# Penguin Prediction App
This app predicts the **Palmer Penguin** species!
Data obtained form the [PalmerPenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
""")