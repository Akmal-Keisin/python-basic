# Practice: Dictionary

# Creating a dictionary
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(sampleDict)

# Accessing items by key name
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(sampleDict["brand"])

# Duplicate keys - last value overwrites
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(sampleDict)

# Access using square brackets
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = sampleDict["model"]
print(x)

# Access using get() method
x = sampleDict.get("model")
print(x)

# Get all keys
x = sampleDict.keys()
print(x)

# Keys list updates with dictionary changes
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change

# Get all values
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = sampleDict.values()
print(x)

# Values list updates when value changes
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Values list updates when new item added
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.values()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

# Get all items (key-value pairs as tuples)
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = sampleDict.items()
print(x)

# Items list updates when value changes
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change

# Items list updates when new item added
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.items()
print(x)  # before the change
car["color"] = "red"
print(x)  # after the change

# Check if key exists
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in sampleDict:
    print("Yes, 'model' is one of the keys in the sampleDict dictionary")

# Change value by key name
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
sampleDict["year"] = 2018
print(sampleDict)

# Update using update() method
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
sampleDict.update({"year": 2020})
print(sampleDict)

# Add new item using new key
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
sampleDict["color"] = "red"
print(sampleDict)

# Add new item using update() method
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
sampleDict.update({"color": "red"})
print(sampleDict)

# Remove item using pop()
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
sampleDict.pop("model")
print(sampleDict)

# Remove last item using popitem()
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
sampleDict.popitem()
print(sampleDict)

# Remove item using del keyword
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del sampleDict["model"]
print(sampleDict)

# Clear dictionary - empties it
sampleDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
sampleDict.clear()
print(sampleDict)
