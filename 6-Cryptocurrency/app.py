# libraries
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import requests
import json
import time

from bs4 import BeautifulSoup

# Page Layout - Expand Page to full width
st.set_page_config(layout="wide")

# Intro
st.title('Crypto Price App')
st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrencies from **CoinMarketCap**!
""")

# About
expander_bar = st.beta_expander("About")
expander_bar.markdown("""
* **Python Libraries:** streamlit, pandas, base64, matplotlib, requests, json, time
* **Data Source:** [CoinMarketCap](https://coinmarketcap.com).
""")

# Page Layout - Divide into 3 columns [Sidebar - Page Contents]
col1 = st.sidebar
col2, col3 = st.beta_columns((2,1))

# Sidebar
col1.header('Input Options')

# Sidebar - Currency Price Unit
currency_price_unit = col1.selectbox('Select Currency for Price', ('USD', 'BTC', 'ETH'))
