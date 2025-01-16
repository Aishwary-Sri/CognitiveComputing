import os
files = os.listdir()
files = [f for f in files if os.path.isfile(f)]
print("Files in the current directory:")
for file in files:
    print(file)
