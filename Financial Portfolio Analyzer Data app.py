# Importing the Required libraries
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn import preprocessing
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
#Loading a portfolio data  
data = pd.read_csv(r"C:\Users\Sree Vidya\Desktop\ISB\T\stock.csv")
data.head()
#Sorting of the data with respect to date
stock = data.sort_values(by=["Date"])
stock.head()
#Base value normalization of the stock values
def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i]/x[i][0]
    return x
stock_base = normalize(stock)
stock_base['portfolio daily worth in $'] = stock_base[stock_base != "Date"].sum(axis=1)
stock_base.head()
df = stock_base[["Date","portfolio daily worth in $"]]
df['year'] = pd.DatetimeIndex(df['Date']).year
df.set_index("year", inplace = True)
df.drop("Date",inplace=True,axis=1)
st.line_chart(df)

df1 = stock_base[["Date","AAPL","BA","T","MGM","MGM","AMZN","IBM","TSLA","GOOG","sp500"]]
df1['year'] = pd.DatetimeIndex(df1['Date']).year
df1.set_index("year", inplace = True)
df1.drop("Date",inplace=True,axis=1)
st.line_chart(df1)