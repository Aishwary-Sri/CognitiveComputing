try:
    a = int(input("Enter the numerator:"))
    b = int(input("Enter the denominator:"))
    c = a-b
    print("The answer is:",c)
except ValueError:
    print("Invalid inputs.")
