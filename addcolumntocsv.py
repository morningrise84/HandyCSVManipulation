import pandas as pd

df = pd.read_csv("TARGETFILE.csv", encoding='cp1252')

df['COLUMNNAME'] = 'DEFAULTVALUE'

df.to_csv("TARGETFILE.csv", index=False)

print(df)