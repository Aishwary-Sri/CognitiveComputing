try:
    num = int(input("Enter the numerator:"))
    den = int(input("Enter the denominator:"))
    r = num/den
    print("The result is:",r)
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Enter valid numbers.")
finally:
    print("Execution is complete.")
