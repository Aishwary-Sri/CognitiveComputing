with open("sample.txt", "w") as f:
    f.write("Hello")
with open("sample.txt", "r") as f:
    c = f.read()
    print("Content of the file:")
    print(c)
