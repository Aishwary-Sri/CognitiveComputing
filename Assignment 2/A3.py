import random
rnd = []
for i in range(0,100):
    num = random.randint(100, 900)
    rnd.append(num)
print("List:",rnd)
odd = []
even = []
prime = []
for j in rnd:
    if j % 2 == 0:
        even.append(j)
    else:
        odd.append(j)
for k in rnd:
    if k > 1:
        pr = True
        for l in range(2, k):
            if k%l == 0:
                pr = False
                break
        if pr:
            prime.append(k)
print("Odd numbers:",odd,"\nNumber of odd numbers:",len(odd))
print("Even numbers:",even,"\nNumber of even numbers:",len(even))
print("Prime numbers:",prime,"\nNumber of prime numbers:",len(prime))
