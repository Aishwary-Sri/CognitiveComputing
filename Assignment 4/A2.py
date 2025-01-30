import numpy as np

#a)
e = np.array([1, 2, 3, 6, 4, 5])
f = e[::-1]
print("Reversed Array:", f)

#b)
from collections import Counter
g = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
h = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])
i = Counter(g)
j = i.most_common(1)[0][0]
k = np.where(g == j)[0]
l = Counter(h)
m = l.most_common(1)[0][0]
n = np.where(h == m)[0]
print("Most Frequent Element in g:", j, "Indices:", k)
print("Most Frequent Element in h:", m, "Indices:", n)
