from pandas_datareader import data 
import matplotlib.pyplot as plt 
import pandas as pd 
from datetime import dt 
ticker = 'GLD'

data1 = data.DataReader(ticker, 'yahoo',dt.datatime(2018,04,27),dt.datatime(2019,05,03))
gld_df = pd.DataFrame(data1)
date_df = pd.to_datetime(list(gld_df.index))
adj_close_df = list(gld_df["Adj Close"])
plt.plot(date_df,adj_close_df)
plt.title("SPDR Gold Shares")
plt.show()
