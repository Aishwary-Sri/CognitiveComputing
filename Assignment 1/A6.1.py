s = str(input("Enter a string:"))
v = "aeiouAEIOU"
count = 0
for i in s:
    if i in v:
        count += 1
print("The number of vowels is:",count)
