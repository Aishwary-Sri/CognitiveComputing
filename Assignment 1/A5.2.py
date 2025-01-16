dic = {1: "One",2: "Two",3: "Three"}
key = int(input("Enter the key to find: "))
if key in dic.keys():
    print("The value is:", dic[key])
else:
    print("The key does not exist.")
