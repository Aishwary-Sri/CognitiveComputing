#A1
import pandas as pd
data = {
    'Tid': [1,2,3,4,5,6,7,8,9,10],
    'Refund': ['Yes','No','No','Yes','No','No','Yes','No','No','No'],
    'Maritial Status': ['Single','Married','Single','Married','Divorced','Married','Divorced','Single','Married','Single'],
    'Taxable Income': [125000,100000,70000,120000,95000,60000,220000,85000,75000,90000],
    'Cheat': ['No','No','No','No','Yes','No','No','Yes','No','Yes']}
df = pd.DataFrame(data)
print(df)
#A2
s = df.loc[[0, 4, 7, 8]]
print(s)
#A3
#1.
r = df.iloc[3:8]
print(r)
#2.
t = df.iloc[4:9, 2:5]
print(t)
#3.
u = df.iloc[:, 1:4]
print(u)