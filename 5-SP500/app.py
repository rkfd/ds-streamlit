import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf

# Introduction
st.title('S&P 500 App')
st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia)
* **Python Libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data Source:** [Wikipedia](https://en.wikipdia.org/wiki/List_of_S%26P_500_companies).
""")

# Sidebar
st.sidebar.header('User Input Features')

# Web Scraping
@st.cache
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header=0)
    df = html[0]
    return df