import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
import yfinance as yf

from dateutil.relativedelta import relativedelta

st.title("5 years Monthly anomalies")
codelist = st.multiselect(
    'Symbols@Yahoo Finance! US',
    ['2501.T', '2502.T', '2503.T'],
    ['2501.T', '2502.T', '2503.T'])

end_D = datetime.date.today()
start_D = datetime.date.today() - relativedelta(years=5)

df = yf.download(codelist, start=start_D, end=end_D, interval='1mo')["Adj Close"]
print(df)

df_analyse=df.pct_change().dropna().groupby([lambda x: x.month]).sum()
print(df_analyse)

fig, ax = plt.subplots()
df_analyse.plot.bar(ax=ax)
st.pyplot(fig)
st.dataframe(df_analyse.T)
