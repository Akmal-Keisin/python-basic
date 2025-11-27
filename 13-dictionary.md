# Dictionary

Dictionaries are used to store data values in **key:value pairs**.

A dictionary is a collection which is **ordered*** (**changeable** and **do not allow duplicates**).

**Note:** As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values.

**Example:** Create and print a dictionary:
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(sampleDict)
```

## Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
Print the "brand" value of the dictionary:
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(sampleDict["brand"])
```

### Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

### Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

### Duplicates Not Allowed
Duplicate values will overwrite existing values:
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(sampleDict)
```

## Accessing Dictionary Items

### Accessing Items
You can access the items of a dictionary by referring to its key name, inside square brackets.

**Example:** Get the value of the "model" key:

```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = sampleDict["model"]
```

There is also a method called `get()` that will give you the same result.

**Example:** Get the value of the "model" key:
```python
x = sampleDict.get("model")
```

### Get Keys
The `keys()` method will return a list of all the keys in the dictionary.
```python
x = sampleDict.keys()
```

The list of the keys is a **view** of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

**Example:** Add a new item to the original dictionary, and see that the keys list gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
```

### Get Values
The `values()` method will return a list of all the values in the dictionary.
```python
x = sampleDict.values()
```

The list of the values is a **view** of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

**Example:** Make a change in the original dictionary, and see that the values list gets updated as well:

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
```

**Example:** Add a new item to the original dictionary, and see that the values list gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
```

### Get Items
The `items()` method will return each item in a dictionary, as tuples in a list.
```python
x = sampleDict.items()
```

The returned list is a **view** of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

**Example:** Make a change in the original dictionary, and see that the items list gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change
```

**Example:** Add a new item to the original dictionary, and see that the items list gets updated as well:
```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
```

### Check if Key Exists
To determine if a specified key is present in a dictionary, use the `in` keyword.

**Example:** Check if "model" is present in the dictionary:

```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in sampleDict:
  print("Yes, 'model' is one of the keys in the sampleDict dictionary")
```

## Changing Dictionary Items

### Change Values
You can change the value of a specific item by referring to its key name:
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sampleDict["year"] = 2018
```

### Update Dictionary
The `update()` method will update the dictionary with the items from the given argument.

The argument must be a dictionary, or an iterable object with key:value pairs.
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sampleDict.update({"year": 2020})
```

## Adding Items

### Create New Key
Adding an item to the dictionary is done by using a new index key and assigning a value to it:
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sampleDict["color"] = "red"
print(sampleDict)
```

### Using update() Method
The `update()` method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

The argument must be a dictionary, or an iterable object with key:value pairs.
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sampleDict.update({"color": "red"})
```

## Removing Items

### Using pop() Method
The `pop()` method removes the item with the specified key name:
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sampleDict.pop("model")
print(sampleDict)
```

### Using popitem() Method
The `popitem()` method removes the last inserted item (in versions before 3.7, a random item is removed instead):
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sampleDict.popitem()
print(sampleDict)
```

### Using del Keyword
The `del` keyword removes the item with the specified key name:
```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del sampleDict["model"]
print(sampleDict)
```

The `del` keyword can also delete the dictionary completely:

```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del sampleDict
print(sampleDict) # This will cause an error because "sampleDict" no longer exists.
```

### Using clear() Method
The `clear()` method empties the dictionary:

```python
sampleDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
sampleDict.clear()
print(sampleDict)
```