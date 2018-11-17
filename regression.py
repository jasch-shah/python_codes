import pandas as import pd
import Quandl

df = Quandl.get('WIKI/GOOGL')
print df.head()
