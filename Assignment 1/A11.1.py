import math
num = float(input("Enter a number:"))
if num < 0:
    print("Cannot calculate the square root of a negative number.")
else:
    sqr = math.sqrt(num)
    print("The square root is:", sqr)
