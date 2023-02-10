# First of all we have to import the libraries that we are going to use

import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

# Then we have to download the data

ticker = ['GOOG']
startdate = '2012-01-01'
enddate = '2023-02-02'
data = pd.DataFrame()

data = pdr.get_data_yahoo(ticker, start=startdate, end=enddate)['Adj Close']
data = data.reset_index()

# SMA

def computeSMA(data, window):
    sma = data.rolling(window=window).mean()
    return sma

# EMA

def computeEMA(data, span):
    ema = data.ewm(span=span).mean()
    return ema

# DataFrame

def construct_df(ticker):
    df = data
    for i in range(50, 250, 50):
        df['SMA_{}'.format(i)] = computeSMA(df['Adj Close'], i)
        df['EMA_{}'.format(i)] = computeSMA(df['Adj Close'], i)
    return df

df = construct_df(ticker)

# Chart SMA

def plot_data_SMA(df):
    plt.figure(figsize=(16,8))
    plt.title(ticker)
    plt.plot(df['Date'], df['Adj Close'])

    for i in range(50, 250, 50):
        plt.plot(df['Date'], df['SMA_{}'.format(i)])
    plt.show()

# Chart EMA

def plot_data_EMA(df):
    plt.figure(figsize=(16,8))
    plt.title(ticker)
    plt.plot(df['Date'], df['Adj Close'])

    for i in range(50, 250, 50):
        plt.plot(df['Date'], df['EMA_{}'.format(i)])
    plt.show()

plot_data_SMA(df)
plot_data_EMA(df)