


import pandas as pd



df = pd.read_csv('/Users/saintmantis/Downloads/upwork - Sheet1 (1).csv')
for row in df.index:
    df.loc[1,'Project_title'] = "10000"

df.to_csv('/Users/saintmantis/Desktop/upwork - Sheet1.csv', index=False)