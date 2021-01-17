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

df = load_data()
sector = df.groupby('GICS Sector')

# Sidebar - Sector Selection
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering Data
df_selected_sector = df [(df['GICS Sector'].isin(selected_sector))]

st.header('Display Companies in Selected Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
st.dataframe(df_selected_sector)

# Download S&P500 Data
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

# Download Link
st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

# Download Data from yfinance
# https://pypi.org/project/yfinance/
data = yf.download(
    tickers = list(df_selected_sector[:10].Symbol),
    period = "ytd", # YearToDay - Start of the Year to Today
    interval = "1d",
    groupby = "ticker",
    auto_adjust = True,
    prepost = True,
    threads = True,
    proxy = None
)

# Visualization
def price_plot(symbol):
    df = pd.DataFrame(data['Close'][symbol])
    df['Date'] = df.index
    plt.fill_between(df.Date, df[symbol], color='skyblue', alpha=0.3)
    plt.plot(df.Date, df[symbol], color='skyblue', alpha=0.8)
    plt.xticks(rotation=90)
    plt.title(symbol, fontweight='bold')
    plt.xlabel('Date', fontweight='bold')
    plt.ylabel('Closing Price', fontweight='bold')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    return st.pyplot()

# Sidebar - Number of Companies
num_company = st.sidebar.slider('Number of Companies', 1, 5)

# Toggle - Show Plots
if st.button('Show Plots'):
    st.header('Stock Closig Price')
    for i in list(df_selected_sector.Symbol)[:num_company]:
        price_plot(i)