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

# Webscraping CoinMarketCap Data
@st.cache
def load_data():
    # Fetch Data from URL
    cmc = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(cmc.content, 'html.parser')

    # Select Data from the Fetch
    data = soup.find('script', id='__NEXT_DATA__', type='application/json')
    coins = {}
    coin_data = json.loads(data.contents[0])
    listings = coin_data['props']['initialState']['cryptocurrency']['listingLatest']['data']
    for i in listings:
        coins[str(i['id'])] = i['slug']

    coin_name = []
    coin_symbol = []
    market_cap = []
    percent_change_1h = []
    percent_change_24h = []
    percent_change_7d = []
    price = []
    volume_24h = []

    for i in listings:
        coin_name.append(i['slug'])
        coin_symbol.append(i['symbol'])
        price.append(i['quote'][currency_price_unit]['price'])
        percent_change_1h.append(i['quote'][currency_price_unit]['percent_change_1h'])
        percent_change_24h.append(i['quote'][currency_price_unit]['percent_change_24h'])
        percent_change_7d.append(i['quote'][currency_price_unit]['percent_change_7d'])
        market_cap.append(i['quote'][currency_price_unit]['market_cap'])
        volume_24h.append(i['quote'][currency_price_unit]['volume_24h'])

    df = pd.DataFrame(columns=['coin_name','coin_symbol','market_cap', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'price', 'volume_24h'])
    df['coin_name'] = coin_name
    df['coin_symbol'] = coin_symbol
    df['market_cap'] = market_cap
    df['percent_change_1h'] = percent_change_1h
    df['percent_change_24h'] = percent_change_24h
    df['percent_change_7d'] = percent_change_7d
    df['price'] = price
    df['volume_24h'] = volume_24h

    return df

df = load_data()

# Sidebar - Cryptocurrency Selection
sorted_coin = sorted(df['coin_symbol'].unique())
selected_coin = col1.multiselect('Cryptocurrency', sorted_coin, sorted_coin)

# Filter by Cryptocurrency
df_selected_coin = df[(df['coin_symbol'].isin(selected_coin))]

# Sidebar - Number of Coins to Display
num_coin = col1.slider('Display Top N Coins', 1, 100, 100)
df_coins = df_selected_coin[:num_coin]