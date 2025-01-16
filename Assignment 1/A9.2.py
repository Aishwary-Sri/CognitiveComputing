import random
r= random.randint(1, 100)
print("Generated random number:",r)
prime = True
if r <= 1:
    prime = False
else:
    for i in range(2,r):
        if r%i==0:
            prime = False
            break
if prime:
    print("The number is prime.")
else:
    print("The number is not prime.")
