scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
#i
mx = max(scores)
print("Highest score:",mx)
print("Index of highest score:",scores.index(mx))
#ii
mn = min(scores)
print("Lowest score:",mn)
print("Index of lowest score:",scores.count(mn))
#iii
rev_scores = scores[::-1]
print(list(rev_scores))
#iv
find = int(input("Enter a score to find:"))
if find in scores:
    ind = scores.index(find)
    print("The score is present at index:",ind)
else:
    print("The score is not present.")
