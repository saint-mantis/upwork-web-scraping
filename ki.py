

import pandas as pd



df = pd.read_excel('/Users/saintmantis/Downloads/upworkk.xlsx')

for i in df.index:
    df.loc[i,'Project'] = "10000"

df1 = pd.DataFrame(df)
print(df1)
df1.to_csv('/Users/saintmantis/Desktop/upwork - Sheet1.csv')



 
    








        
   



