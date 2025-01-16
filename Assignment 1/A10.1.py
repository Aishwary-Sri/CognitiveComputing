import sys
try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    r = num1 + num2
    print("The sum is:",r)
except ValueError:
    print("Provide valid numbers.")
