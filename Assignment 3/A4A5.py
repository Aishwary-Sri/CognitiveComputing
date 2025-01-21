import pandas as pd
#A4
d = pd.read_csv('iris.csv')
print("\nFirst five rows of Iris dataset:\n",d.head())
#A5
f = d.drop(index=4, columns=d.columns[2])
print("\nModified Iris dataset:\n",f)

