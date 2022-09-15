from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as web

s1 = datetime(2022,6,1)
e1 = datetime.now()

df = web.DataReader(name="BTC-USD", data_source='yahoo',start=s1,end=e1)
df["Date"] = df.index

def vwap(df):
    v = df['Volume'].values
    tp = (df['Low'] + df['Close'] + df['High']).div(3).values
    return df.assign(vwap=(tp * v).cumsum() / v.cumsum())
df=vwap(df)

plt.plot(df["Date"],df["Close"])
plt.plot(df["Date"],df["vwap"],color="black")
plt.show()


