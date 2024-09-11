import numpy as np
import pandas as pd
d1={
    "name":['Singh','Ritul','Suraj','Atul'],
    "age":[18,21,23,25],
    "city":['Maharajganj','Patna','Shitlapur','Partawal']
}
df=pd.DataFrame(d1)
# print(df)
# df.to_csv('data.csv')
# df.to_csv('data_index.csv', index=False)
# print(df.head(2))
# print(df.tail(2))
# print(df.describe())

# read the sheets
singh=pd.read_csv('singh.csv')
# print(singh)
# singh['Speed'][0]=95
# print(singh)
# singh.to_csv('singh.csv')
# singh.index=['a','b','c','d']
# print(singh)

ser=pd.Series(np.random.rand(34))
print(type(ser))
ndf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
# print(type(ndf))
# print(ndf.head())
# ndf[0][0]="Singh"
# print(ndf.head())
# print(ndf.index)
# print(ndf.columns)
# print(ndf.T)
print(ndf[0])