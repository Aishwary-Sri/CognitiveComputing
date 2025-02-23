import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#PartI
r = int(input("Roll number: "))
np.random.seed(r)
a = np.random.randint(1000, 5001, (12, 4))
mon = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
df = pd.DataFrame(a, columns=["Electronics", "Clothing", "HomeKitchen", "Sports"], index=mon)

#PartII
print(df.head())
print(df.describe())
cat = df.sum(axis=0)
mt = df.sum(axis=1)
gr = df.diff().mean()
df["TotalSales"] = df.sum(axis=1)
df["GrowthRate"] = df["TotalSales"].pct_change() * 100
if r % 2 == 0:
    df["Electronics"] = df["Electronics"] * 0.9
else:
    df["Clothing"] = df["Clothing"] * 0.85
print("Cat totals:", cat)
print("Month totals:", mt)
print("Avg growth:", gr)
print(df)

#PartIII
plt.figure()
for col in ["Electronics", "Clothing", "HomeKitchen", "Sports"]:
    plt.plot(df.index, df[col], marker="o", label=col)
plt.title("Monthly Sales Trends")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()
plt.figure()
sns.boxplot(data=df[["Electronics", "Clothing", "HomeKitchen", "Sports"]])
plt.title("Sales Distribution")
plt.grid(True)
plt.show()
