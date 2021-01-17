import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL Football Stats (Rushing) Explorer')

st.markdown("""
This app performs simple webscraping of NFL Footbal player stats data (focusing on Rushing)!
* **Python Libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data Source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")