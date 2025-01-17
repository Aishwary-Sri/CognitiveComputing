A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
#i
uni = A.union(B)
print("Unique scores:",uni)
#ii
com = A.intersection(B)
print("Common scores:",com)
#iii
excl = A.symmetric_difference(B)
print("Exclusive scores:",excl)
#iv
sub = A.issubset(B)
sup = B.issuperset(A)
if sub:
    print("A is a subset of B")
if sup:
    print("B is a superset of A")
#v
X = int(input("Enter a score:"))
if X in A:
    A.remove(X)
    print("Provided score has been removed.")
    print(A)
else:
    print("Provided score is not present.")
