import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dt = pd.read_csv(company_sales_data.csv)
plt.figure()
sns.lineplot(x=dt["month_number"],y=dt["total_profit"],marker="o",color="magenta")
plt.title("Q4: Total Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid(True)
plt.show()

plt.figure()
p = ["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"]
for pr in p:
    sns.lineplot(x=dt["month_number"],y=dt[pr],marker="o",label=pr)
plt.title("Q4: Product Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
ag = dt.select_dtypes(include=[np.number]).sum()
sns.barplot(x=ag.index,y=ag.values,palette="rocket")
plt.title("Q4: Features")
plt.xlabel("Feature")
plt.ylabel("Total")
plt.grid(True)
plt.show()
