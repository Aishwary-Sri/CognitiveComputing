dic1 = {1: "One", 2: "Two", 3: "Three"}
dic2 = {4: "Four", 5: "Five", 6: "Six"}
mergedic = {}
for key in dic1:
    mergedic[key] = dic1[key]
for key in dic2:
    mergedic[key] = dic2[key]
print("Dictionary 1:", dic1)
print("Dictionary 2:", dic2)
print("Merged dictionary:", mergedic)
