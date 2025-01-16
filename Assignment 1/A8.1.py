try:
    num = int(input("Enter the numerator:"))
    den = int(input("Enter the denominator:"))
    a = num/den
    print("The answer is:",a)
except ZeroDivisionError:
    print("Division by zero is not allowed.")

