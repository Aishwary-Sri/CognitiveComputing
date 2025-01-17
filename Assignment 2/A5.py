data = {"city": "New York","population": 8419600,"area": 468.9}
if "city" in data.keys():
    a = data.pop("city")
    data["location"] = a
print("Updated dictionary:",data)
