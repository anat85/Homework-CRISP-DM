import pandas as pd
df = pd.read_csv('winequalityN.csv', sep=',', header=0, encoding='utf-8')
df.columns = df.columns.str.replace(" ", "_")
df.head()