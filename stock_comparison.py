import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Define the tickers for Soitec and Nvidia
tickers = ['SOI.PA', 'NVDA']

# Fetch data for the past 20 years from today
data = yf.download(tickers, start="2003-01-01")

# Extract closing prices
close_prices = data['Close']
close_prices.columns = ['SOITEC', 'NVDA']

# Streamlit app
st.title('Stock Price Comparison: Soitec SA (SOIT) vs Nvidia (NVDA)')

# Plotting using matplotlib and seaborn
plt.figure(figsize=(14, 7))
sns.lineplot(data=close_prices, palette=['b', 'r'])
plt.title('Stock Price Comparison: Soitec SA (SOIT) vs Nvidia (NVDA)')
plt.xlabel('Date')
plt.ylabel('Closing Price')
st.pyplot(plt)  # Display the matplotlib plot in Streamlit

# Plotting using plotly-express for interactivity
fig = px.line(close_prices, title='Stock Price Comparison: Soitec SA (SOIT) vs Nvidia (NVDA)', labels={'value':'Closing Price', 'index': 'Date'})
st.plotly_chart(fig)  # Display the plotly chart in Streamlit
