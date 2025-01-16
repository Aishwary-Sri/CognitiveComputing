with open("sample.txt", "a") as f:
    f.write("\nWorld")
with open("sample.txt", "r") as f:
    c = f.read()
    print("Updated file:")
    print(c)
