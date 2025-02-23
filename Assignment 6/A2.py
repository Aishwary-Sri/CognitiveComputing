import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

s = ["A","B","C","D","E"]
sc = [85,92,78,90,88]
df = pd.DataFrame({"Subject": s, "Score": sc})
plt.figure()
ax = sns.barplot(x="Subject",y="Score",data=df,palette="viridis")
for i,v in enumerate(sc):
    ax.text(i,v+0.5,str(v),ha="center")
plt.title("Q2: Scores")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.grid(True)
plt.show()
