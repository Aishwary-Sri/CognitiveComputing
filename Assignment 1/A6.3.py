s = str(input("Enter a string:"))
r = ""
s1 = s.replace(" ","").lower()
for c in s1:
    r = c + r 
if s1 == r:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
