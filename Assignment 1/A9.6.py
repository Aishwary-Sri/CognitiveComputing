import random
import string
l = int(input("Enter the length of the password:"))
char = string.ascii_letters+string.digits+string.punctuation
password = ''.join(random.choice(char) for i in range(l))
print("Generated password:",password)
